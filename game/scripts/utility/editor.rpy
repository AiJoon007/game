init python:

    from renpy.parser import ParseError
    from copy import deepcopy

    class Editor(python_object):

        doll_keywords = ["mouth", "eyes", "eyebrows", "pupils", "cheeks", "tears", "emote",\
            "xpos", "ypos", "pos", "flip", "trans", "animation", "hair"]
        other_keywords = ["expression", "xpos", "ypos", "pos", "flip", "trans", "animation", "wand"]

        def __init__(self):
            self.node = None
            self._live_code = None # Volatile; Can be changed at any given moment.
            self.history = _dict()
            self.expressions = self.define_expressions()
            self.active_expressions = _dict()
            self.persistent_expressions = _set()
            self.last_expressions = _dict()
            self.active = False
            self.sayers = {i[:3]:i for i in states.dolls}

        def catch(self, *args, **kwargs):
            if not self.active or renpy.is_init_phase():
                return

            self.node = None
            self.live_code = None

            #stack = renpy.get_return_stack()
            statement = renpy.game.context().current

            if not statement:
                return

            node = renpy.game.script.namemap.get(statement, None)

            # Console call fallback
            if node.filename == "<string>":
                return

            if not isinstance(node, renpy.ast.Say):
                return

            self.node = node

            who = node.who
            file = node.filename
            line = node.linenumber
            code = node.get_code()
            code_file = self.read_file(file, line)

            # We need to use deepcopy, otherwise the dict
            # would be participating in rollback
            self.last_expressions = deepcopy(self.active_expressions)
            self.active_expressions.update(self.resolve_expressions())
            self.live_code = code

            # Consistency check
            if not matches(code, code_file):
                s = "Active {color=#e54624}node code{/color} differs from the {color=#40bf77}file code{/color},"\
                    " would you like to update the node?\n\n\n"\
                    "{color=#e54624}" + code + "{/color}\n->\n"\
                    "{color=#40bf77}" + code_file + "{/color}"
                prompt = Text(s, style="editor_text")
                layout.yesno_screen(prompt, [SetField(e, "live_code", code_file), e.live_replace, Notify("Updated.")], Notify("Cancelled."))

            self.write_history(file, line, self.live_code)

        def replace(self, what, contents):
            node = self.node

            if what in ("who", "what"):
                setattr(node, what, contents)
            elif what == "args":
                args = node.arguments

                if not args:
                    args = renpy.ast.ArgumentInfo(contents, None, None)
                    node.arguments = args
                else:
                    if args.starred_indexes or args.doublestarred_indexes:
                        raise Exception("Starred arguments are not implemented.")

                    node.arguments.arguments = contents
            elif what == "temp_attr":
                setattr(node, "temporary_attributes", tuple(contents))
            else:
                raise TypeError("Type '{}' is not implemented.".format(what))

        def replace_expression(self, expr, val):
            node = self.node
            who = node.who
            no_kw_args= ("mouth", "eyes", "eyebrows", "pupils", "expression")
            kw_args = ("tears", "cheeks", "hair")

            # We need to make sure not to add quotes
            # to expressions or variables.
            if isinstance(val, str):
                val = "\"{}\"".format(val)

            # Insert new expression
            d = self.get_expressions_active(who)
            d[expr] = val

            # Convert to list of tuples
            # l = [(k, "\"{}\"".format(v)) for k, v in d.items() if not v is None] # This is faster, but not robust enough.

            l = _list()
            l2 = _list()

            for key, val in d.items():

                if key in kw_args:
                    if val is None:
                        continue
                    elif key in self.persistent_expressions:
                        pass
                    else:
                        val = val.strip("\"") # When accessed, temporary attribute values have quotes by default, we need to strip them.
                        l2.extend((key, val))
                        continue

                # First four arguments are preferred to be keywordless,
                # so we'll just insert them into positions to avoid issues.
                if key in no_kw_args:
                    key = None

                l.append((key, val))

            self.replace("args", l)
            self.replace("temp_attr", l2)

            file = node.filename
            line = node.linenumber
            code = node.get_code()

            self.write_file(file, line, code)
            self.write_history(file, line, code)
            self.live_code = code
            renpy.run(RestartStatement()) # This has to be run last.

        @property
        def live_code(self):
            return self._live_code

        @live_code.setter
        def live_code(self, code):
            if self._live_code == code:
                return

            # Additional validation goes here

            self._live_code = code

        def live_replace(self):
            node = self.node
            file = node.filename
            line = node.linenumber
            code = node.get_code()
            live_code = self.live_code

            if code == live_code:
                return

            rnode = self.parse(file, line, live_code)

            if rnode is None:
                return

            # It's simpler to replace node attributes
            # than the entire node in every linked context.
            node.who = rnode.who
            node.attributes = rnode.attributes
            node.temporary_attributes = rnode.temporary_attributes
            node.interact = rnode.interact
            node.what = rnode.what
            node.arguments = rnode.arguments
            node.with_ = rnode.with_

            self.write_file(file, line, live_code)
            self.write_history(file, line, live_code)
            renpy.run(RestartStatement()) # This has to be run last.

        def live_reset(self):
            node = self.node
            self.live_code = node.get_code()

        def parse(self, file, line, code):
            renpy.game.exception_info = 'While parsing ' + file + '.'

            try:
                lines = renpy.parser.list_logical_lines(file, code, line)
                nested = renpy.parser.group_logical_lines(lines)
            except ParseError as e:
                renpy.notify("Parsing failed.\n{size=-8}(Check console for details){/size}")
                print(e)
                return None

            lexer = renpy.parser.Lexer(nested)
            block = renpy.parser.parse_block(lexer)

            if not block:
                renpy.notify("Parsing failed.\n{size=-8}(Check console for details){/size}")
                print("Fatal error while parsing the code block.")
                return None

            return block[-1]

        def read_file(self, file, line):
            file = os.path.join(config.basedir, file)
            line = line-1

            try:
                with open(file, "r") as f:
                    data = f.readlines()

                return data[line].partition("#")[0].strip() # Remove comments and strip spaces.
            except EnvironmentError as e:
                renpy.notify("File read error.\n{size=-8}(Check console for details){/size}")
                print(e)
            except IndexError as e:
                renpy.notify("File index error.\n{size=-8}(Check console for details){/size}")
                print(e)
                print("(Most likely the file was tampered with.)")

        def write_file(self, file, line, code):
            file = os.path.join(config.basedir, file)
            line = line-1

            try:
                with open(file, "r+", newline="\n") as f:
                    data = f.readlines()

                    old = data[line].partition("#")[0].strip() # Remove comments and strip spaces.
                    new = data[line].replace(old, code)

                    data[line] = new

                    f.seek(0)
                    f.truncate()
                    f.writelines(data)

                renpy.notify("Saved.")
            except FileNotFoundError as e:
                renpy.notify("Source file is missing.")
                print(e)
            except EnvironmentError as e:
                renpy.notify("File write error.\n{size=-8}(Check console for details){/size}")
                print(e)

        def read_history(self, file, line):
            # _dict, and _list methods do not participate in rollback
            # unlike their revertable counterparts, so that's what we'll use.
            return self.history.get(file, _dict()).get(line, _list())

        def write_history(self, file, line, code):
            if code in self.read_history(file, line):
                return

            self.history.setdefault(file, _dict()).setdefault(line, _list()).append(code)

        def clear_history(self, file, line):
            self.history.setdefault(file, _dict())[line] = _list()

        def launch_editor(self, file, line):
            renpy.launch_editor([file], line)

        def define_expressions(self):
            # This function is kind of messy,
            # because each character has unique display methods.
            # Some things are required to be hardcoded.

            # Define expressions for Doll type characters.
            all_files = renpy.list_files()
            d = OrderedDict()

            for charname in states.dolls:
                charobj = get_character_object(charname)
                extensions = charobj.extensions
                who = charname[:3]

                for part in sorted(charobj.face._face.keys()):

                    path = posixpath.join("characters", charname, "poses", charobj.pose, "face", part)

                    for f in renpy.list_files():
                        fp, fn = os.path.split(f)
                        fn, ext = os.path.splitext(fn)
                        expression = os.path.split(fp)[1]

                        if not fp.startswith(path) or not ext in extensions:
                            continue

                        if part in ("cheeks", "tears"):
                            expressions = d.setdefault(who, OrderedDict()).setdefault(part, _list((None,)))
                        else:
                            expressions = d.setdefault(who, OrderedDict()).setdefault(part, _list())

                        if not expression in expressions:
                            expressions.append(expression)

                imap = {v: i for i, v in enumerate(self.doll_keywords)}
                d[who] = OrderedDict(sorted(list(d[who].items()), key=lambda x: imap[x[0]]))

            # Define additional Tonks' hair choices.
            d["ton"]["hair"] = [None] + list(tonks_haircolor_table.keys())

            # Define expressions for Genie.
            filters = None
            path = "characters/genie/"
            files = None

            d["gen"] = OrderedDict()
            d["gen"]["expression"] = ["angry", "grin", "base", "open"]

            # Define expressions for Snape.
            filters = ("b01", "b01_01", "b02", "picture_Frame", "wand")
            path = "characters/snape/main/"
            files = [x for x in all_files if path in x]

            d["sna"] = OrderedDict()
            d["sna"]["expression"] = [x.split(path)[1].split(".webp")[0] for x in files if x.endswith(".webp") and not any(f in x for f in filters)]
            d["sna"]["special"] = [None, "wand", "picture_frame"]

            return d

        def resolve_expressions(self):
            node = self.node
            who = node.who
            args = node.arguments

            if who in self.sayers:
                keywords = self.doll_keywords
            else:
                keywords = self.other_keywords

            # Arguments are contained within a list,
            # they consist of opaque tuples,
            # each one containing a keyword, and a value.
            # keyword can be a None if the keyword
            # is implied by the argument position.
            d = _dict()
            d[who] = _dict()

            # Args is an ArgumentInfo object, or None,
            # the true list of arguments is kept
            # within the object itself.
            if not args:
                return d

            args = args.arguments

            # Resolve arguments for character statements.
            # (There should be a simpler way to do this, right?)
            for i, (key, val) in enumerate(args):

                if key is None:
                    key = keywords[i]

                d[who][key] = val

            # Resolve temporary attributes
            temp_attr = node.temporary_attributes

            if temp_attr:
                d[who].update(dict(zip(temp_attr[::2], temp_attr[1::2])))

            # Sort our dictionary using an index map,
            # if we don't, we'll end up messing up
            # the order of keywordless arguments.
            imap = {v: i for i, v in enumerate(keywords)}
            d[who] = OrderedDict(sorted(list(d[who].items()), key=lambda x: imap[x[0]]))
            return d

        def get_expression_types(self, who):
            return self.expressions.get(who, _dict())

        def get_expressions_active(self, who):
            return self.active_expressions.get(who, _dict())

        def get_expressions_active_type(self, who, type):
            expr = self.get_expressions_active(who).get(type)
            if isinstance(expr, str):
                expr = strip(expr)
            return expr

        def get_expressions_last(self, who):
            return self.last_expressions.get(who, _dict())

        def get_expressions_last_type(self, who, type):
            expr = self.get_expressions_last(who).get(type, None)
            if isinstance(expr, str):
                expr = strip(expr)
            return expr

        def get_node_history(self):
            node = self.node
            file = node.filename
            line = node.linenumber

            return self.read_history(file, line)

        def toggle_persistent(self, expr):
            if expr in self.persistent_expressions:
                self.persistent_expressions.remove(expr)
            else:
                self.persistent_expressions.add(expr)

    class ToggleEditor(Action, NoRollback):
        def __call__(self):
            if not config.developer:
                return

            if not hasattr(store, "e"):
                global e
                e = Editor()
            e.expressions = e.define_expressions()
            #config.all_character_callbacks.append(e.catch) # This is more efficient.
            config.start_interact_callbacks.append(e.catch) # This allows to catch more statements and reset them if node types don't match.

            if renpy.get_screen("editor", layer="interface"):
                e.active = False
                renpy.hide_screen("editor", layer="interface")
            else:
                e.active = True
                renpy.show_screen("editor")

            renpy.restart_interaction()
            renpy.game.context().force_checkpoint = True
            renpy.checkpoint(hard=True)

screen editor():
    zorder 50
    style_prefix "editor"
    layer "interface"

    text "Active" pos (25, 25)

    default focused = None

    drag:
        pos (50, 50)
        maximum (500, 500)
        xsize 500

        frame:
            has vbox

            fixed:
                fit_first True
                text "Expression Editor {size=-2}ver 0.4b{/size}" style "editor_title"

            if e.node:
                vbox:
                    hbox:
                        for expr_type in e.get_expression_types(e.node.who).keys():
                            textbutton "[expr_type]":
                                action [CaptureFocus(expr_type), SetScreenVariable("focused", expr_type)]
                                selected GetFocusRect(expr_type)

                        if e.node.who in e.sayers:
                            textbutton "😊":
                                action Function(e.toggle_persistent, "cheeks")
                                selected ("cheeks" in e.persistent_expressions)
                                tooltip "Toggle persistent cheeks"
                            textbutton "😢":
                                action Function(e.toggle_persistent, "tears")
                                selected ("tears" in e.persistent_expressions)
                                tooltip "Toggle persistent tears"

                    add Solid("#ffffff80") xysize (480, 1)

                    hbox:
                        textbutton "History":
                            action [CaptureFocus("history"), SetScreenVariable("focused", "history")]
                            selected GetFocusRect("history")
                            sensitive bool(e.get_node_history())
                        textbutton "Copy":
                            action [Notify("Copied."), Function(set_clipboard, e.live_code)]
                            selected False
                        textbutton "Paste":
                            action [Notify("Pasted."), SetField(e, "live_code", get_clipboard()), Function(e.live_replace)]
                            selected False

                    if focused == 0:
                        dismiss action [SetScreenVariable("focused", 0), Function(e.live_reset)]

                        button:
                            input default "[e.live_code]" value FieldInputValue(e, "live_code")
                            action NullAction()
                            selected (focused == 0)
                            key_events True

                        key ["K_RETURN"] action Function(e.live_replace)
                        key ["ctrl_K_c"] action [Notify("Copied."), Function(set_clipboard, e.live_code)]
                        key ["ctrl_K_v"] action [Notify("Pasted."), SetField(e, "live_code", get_clipboard())]
                    else:
                        textbutton "[e.live_code]" action SetScreenVariable("focused", 0)

    if e.node:
        for expr_type, expr_list in e.get_expression_types(e.node.who).items():

            if GetFocusRect(expr_type):
                dismiss action [ClearFocus(expr_type), SetScreenVariable("focused", None)]

                nearrect:
                    focus expr_type

                    frame:
                        modal True

                        has vbox:
                            box_wrap True

                        style_prefix "editor_dropdown"

                        for expr in expr_list:
                            textbutton "[expr]":
                                action [ ClearFocus(expr_type), SetScreenVariable("focused", None), Function(e.replace_expression, expr_type, expr)]
                                selected (expr == e.get_expressions_active_type(e.node.who, expr_type))

        if GetFocusRect("history"):
                dismiss action [ClearFocus("history"), SetScreenVariable("focused", None)]

                nearrect:
                    focus "history"

                    frame:
                        modal True

                        has vbox:
                            box_wrap True

                        style_prefix "editor_history"

                        for i, entry in enumerate(e.get_node_history(), 1):
                            textbutton "[i]. [entry]":

                                action [ ClearFocus("history"), SetScreenVariable("focused", None), SetField(e, "live_code", entry), Function(e.live_replace)]
                                selected (entry == e.live_code)

    key ["K_ESCAPE"] action [ClearFocus(focused), SetScreenVariable("focused", None), Function(e.live_reset)]

style editor_text:
    color "#D0D0D0"
    hover_color "#e54624"
    selected_color "#40bf77"
    selected_hover_color "#E6A825"
    insensitive_color "#6b6b6b"
    bold True
    size 13
    font "DejaVuSans.ttf"
    outlines [ (1, "#000", 0, 0) ]
    adjust_spacing False

style editor_button:
    background None
    hover_background "#00000099"
    selected_background "#00000099"
    align (0, 0)
    padding (5, 5)

style editor_button_text is editor_text
style editor_input is editor_text:
    color "#40bf77"
    hover_color "#e54624"
    caret "caret"
    hover_caret "hover_caret"

style editor_dropdown_button is editor_button:
    xmaximum 200
    xfill True
    hover_background "#00000099"

style editor_dropdown_button_text is editor_text

style editor_history_button is editor_dropdown_button:
    xmaximum 600
    xfill True

style editor_history_button_text is editor_text:
    size 10

style editor_frame:
    background "#00000099"

style editor_title is editor_text:
    color "#fff"

image caret = Text("<", style="editor_text", color="#e54624", size=12)
image hover_caret = Text("<", style="editor_text", color="#40bf77", size=12)
