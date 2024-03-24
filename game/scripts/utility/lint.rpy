init:
    if config.developer:
        # Dummy code used to stop lint from reporting false errors.
        image snape_main = Null()
        image genie_main = Null()
        image tonks_main = Null()
        image hermione_main = Null()
        image cho_main = Null()
        image luna_main = Null()
        image astoria_main = Null()
        image susan_main = Null()
        image hooch_main = Null()
        image hooch = Null()

init -1 python:
    if config.developer:

        def lint_characters():
            renpy.execute_default_statement(False)

            # Add images to linting list to avoid undefined errors
            for i in states.dolls:
                prefix = get_character_tag(i)
                renpy.lint.image_prefixes[prefix] = True

            nodes = [i for i in renpy.game.script.all_stmts if isinstance(i, (renpy.ast.Say, renpy.ast.Menu))]
            nodes.sort(key=lambda x: (x.filename, x.linenumber))
            files = renpy.list_files()

            SELF_CLOSING_TAGS = re.compile(r'(\{\{)|(\{(p|w|nw|fast|done|image|space)(?:\=([^}]*))?\})', re.S)

            EXPRESSIONS = ["mouth", "eyes", "eyebrows", "pupils", "cheeks", "tears"]
            POSITIONS = ["xpos", "ypos", "pos"]
            OTHER = ["flip", "trans", "animation", "hair", "emote"]
            KEYS = EXPRESSIONS + POSITIONS + OTHER
            INTERPUNCT = (".", "!", "?", "--", "*", ")", "}")
            SAYERS = {i[:3]:i for i in states.dolls}
            RE_SPACES = re.compile(r"\s[^\S\r\n]")
            RE_COMMA = re.compile(r"\w+, \w+, \w+ and")
            RE_BRACKET = re.compile(r"\([^)]*$")
            RE_REPEATED = re.compile(r"\b(\w+)\b \b\1\b")
            RE_QUOTES = re.compile(r"[.,]\\\"")
            RE_ARTICLES = re.compile(r" a [aeiou][^uni|eu|ur|usa]")

            for node in nodes:

                if isinstance(node, renpy.ast.Say):
                    who = node.who
                    what = [node.what]
                    file = node.filename
                    line = node.linenumber
                    args = node.arguments
                    code = node.get_code()
                    type = "say"
                elif isinstance(node, renpy.ast.Menu):
                    who = None
                    what = [x[0] for x in node.items]
                    file = node.filename
                    line = node.linenumber
                    args = None
                    code = None
                    type = "menu"

                has_failed = False
                has_xpos = False
                has_ypos = False
                uses_ypos_head = False

                if args:
                    kwargs = dict.fromkeys(KEYS)

                    args = args.arguments

                    for i, arg in enumerate(args):
                        key, val = arg

                        if key is None:
                            kwargs[KEYS[i]] = val
                        else:
                            kwargs[key] = val

                    for key, val in list(kwargs.items()):
                        # Validate facial expressions
                        if key in EXPRESSIONS and who in iter(list(SAYERS.keys())):

                            if val is None:
                                continue

                            if not val.startswith(("\"", "'")) and not val.endswith(("\"", "'")): # Ignore variables
                                continue

                            # Node argument values are (fucking) raw
                            val = strip(val)

                            msg = "'{}'".format(key)
                            fp = f"characters/{SAYERS.get(who)}/poses/default/face/{key}/{val}/"
                            fn = next((f for f in files if f.startswith(fp)), f"{fp}expression.webp")

                            if not has_failed:
                                # Avoid repeating node destination
                                renpy.lint.report_node = node
                                has_failed = True

                            renpy.lint.check_file(msg, fn)

                        # Validate positional arguments
                        if key in POSITIONS:
                            if val is None:
                                continue

                            # Node argument values are (fucking) raw
                            val = strip(val)

                            # Skip integers
                            try:
                                int(val)
                                continue
                            except:
                                pass

                            if key == "xpos":
                                has_xpos = True

                                val = sprite_pos.get("x").get(val, val)

                            elif key == "ypos":
                                has_ypos = True

                                if val == "head":
                                    uses_ypos_head = True

                                val = sprite_pos.get("y").get(val, val)

                            if not isinstance(val, int):
                                if not has_failed:
                                    # Avoid repeating node destination
                                    renpy.lint.report_node = node
                                    has_failed = True

                                msg = "'{}' requires an integer, or a pre-defined named position, not '{}'".format(key, val)
                                renpy.lint.report(msg)

                            # This would require fixing hundreds of calls. Might postpone it...

                            # if uses_ypos_head and not has_xpos:
                            #     if not has_failed:
                            #         # Avoid repeating node destination
                            #         renpy.lint.report_node = node
                            #         has_failed = True

                            #     msg = "'ypos' uses pre-defined 'head' position, but is lacking 'xpos'"
                            #     renpy.lint.report(msg)

                            if key in OTHER:

                                if val is None:
                                    continue

                                # Node argument values are (fucking) raw
                                val = strip(val)

                                if key == "emote":
                                    msg = "'{}'".format(key)
                                    fn = "characters/{}/emote/{}.webp".format(SAYERS.get(who), val)

                                    if not has_failed:
                                        # Avoid repeating node destination
                                        renpy.lint.report_node = node
                                        has_failed = True

                                    renpy.lint.check_file(msg, fn)

                for string in what:

                    if not string:
                        continue

                    if string.startswith("[") and string.endswith("]"): # Ignore string interpolation
                        continue

                    if "{#LINT_IGNORE}" in string:
                        continue

                    # Check for multiple spaces inside 'what' string
                    match = re.search(RE_SPACES, string.strip())

                    if match:
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string contains multiple spaces"
                        renpy.lint.report(msg)

                    # Check for the (lack of) oxford comma inside 'what' string
                    match = re.search(RE_COMMA, string.strip())

                    if match:
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string is missing oxford comma(s)"
                        renpy.lint.report(msg)

                    # Check for missing brackets inside 'what' string
                    match = re.search(RE_BRACKET, string.strip())

                    if match:
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string is missing a closing bracket"
                        renpy.lint.report(msg)

                    # Check for repeated words words inside 'what' string
                    match = re.search(RE_REPEATED, string.strip())

                    if match:
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string contains repeated words"
                        renpy.lint.report(msg)

                    # Check for punctuation inside quotes, inside 'what' string
                    match = re.search(RE_QUOTES, string.strip())

                    if match:
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string contains non-british punctuation for quotes"
                        renpy.lint.report(msg)

                    # Check for wrong articles inside 'what' string
                    match = re.search(RE_ARTICLES, string.strip())

                    if match:
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string contains wrong articles"
                        renpy.lint.report(msg)

                    if type == "menu" and string.startswith(("-", "\"")) and string.endswith(("-", "\"")):
                        continue

                    # Check punctuation errors
                    if not string.endswith(INTERPUNCT):
                        if not has_failed:
                            # Avoid repeating node destination
                            renpy.lint.report_node = node
                            has_failed = True

                        msg = type + " string punctuation is not adhering to the set text styling"
                        renpy.lint.report(msg)

        config.lint_hooks.append(lint_characters)
