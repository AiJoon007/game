init python:
    if renpy.android:
        settings.default("crashdefendersetting", 0)

        # Attempts at fixing the texture leak plaguing
        # android devices, mainly running on Android11 & Android 12.
        class Android11TextureLeakFix(NoRollback):
            def __init__(self, limit=100):
                self.statements = 0

                self.set_mode(settings.get("crashdefendersetting"))

            def set_mode(self, mode):
                if mode == 3:
                    self.limit = 15
                elif mode == 2:
                    self.limit = 25
                elif mode == 1:
                    self.limit = 55
                else:
                    self.limit = 0

            def __call__(self, name):
                if renpy.is_init_phase() or self.limit == 0:
                    return

                self.statements += 1

                if self.statements > self.limit:
                    self.statements = 0

                    # Big thanks to Andykl (https://github.com/Andykl)
                    # for finding the issue and inventing this workaround.
                    # https://github.com/renpy/renpy/issues/3643

                    cache = renpy.display.im.cache
                    cache_size = cache.get_total_size()
                    cache_limit = cache.cache_limit * 0.95

                    if cache_size >= cache_limit:
                        if config.developer:
                            print("Cache limit reached, purging cache... ({}/{})\n{}".format(cache_size, cache_limit, renpy.get_filename_line()))

                        cache.clear()

                    if renpy.game.interface is not None:
                        if config.developer:
                            print("Statements limit reached, cleaning textures... ({})\n{}".format(self.limit, renpy.get_filename_line()))

                        renpy.game.interface.full_redraw = True
                        renpy.game.interface.restart_interaction = True

                        if renpy.display.draw is not None:
                            renpy.display.draw.kill_textures()

                        renpy.display.render.free_memory()

        crashdefender = Android11TextureLeakFix()

        config.statement_callbacks.append(crashdefender)

python early hide:
    import functools

    if renpy.windows:
        # On windows, Renpy does not support backslashes in some of its functions,
        # but because the code needs to be platform-independent,
        # we require to monkey patch those functions in order
        # to remain compatible with all platforms without losing functionality.

        @renpy.pure
        def _loadable(filename):
            filename = filename.replace("\\", "/")

            return renpy.loader.loadable(filename)

        renpy.loadable = _loadable

    # renpy.list_files does not use cached results, let's fix that.

    @functools.cache
    def _list_files(common=False):
        rv = [fn for dir, fn in renpy.loader.listdirfiles(common) if not fn.startswith("saves/")]
        rv.sort()
        return rv

    renpy.list_files = _list_files

    # Default focus behaviour restarts the interaction whenever
    # any element that contains a tooltip is being hovered or unhovered.
    # Restarting interactions in a short timespan causes massive lag spikes,
    # in order to fix it, we'll refresh just the tooltip screen and skip the rest.

    def set_focused(widget, arg, screen):
        global _tooltip
        renpy.display.focus.argument = arg
        renpy.display.focus.screen_of_focused = screen

        if screen is not None:
            renpy.display.focus.screen_of_focused_names = { screen.screen_name[0], screen.tag }
        else:
            renpy.display.focus.screen_of_focused_names = set()

        renpy.game.context().scene_lists.focused = widget
        renpy.display.tts.displayable(widget)

        # Figure out the tooltip.

        _tooltip = widget._get_tooltip() if widget else None

        # setattr(renpy.store, "widget", widget) # DEBUG

        # if renpy.display.focus.tooltip != new_tooltip:
        #     renpy.display.focus.tooltip = new_tooltip
        #     renpy.display.focus.capture_focus("tooltip")

        #     renpy.exports.restart_interaction()

        #     if renpy.display.focus.tooltip is not None:
        #         renpy.display.focus.last_tooltip = renpy.display.focus.tooltip
        #         renpy.display.focus.screen_of_last_focused_names = renpy.display.focus.screen_of_focused_names

    renpy.display.focus.set_focused = set_focused

    # Add callbacks for label calls and jumps, we use them for the event class
    # in order to figure out if the event was completed or if it's just a call,
    # and also for debugging.
    # class _CallException(Exception):

    #     from_current = False

    #     def __init__(self, label, args, kwargs, from_current=False):
    #         Exception.__init__(self)

    #         self.label = label
    #         self.args = args
    #         self.kwargs = kwargs
    #         self.from_current = from_current

    #         for i in renpy.config.call_callbacks:
    #             i(label, args, kwargs)

    #     def __reduce__(self):
    #         return (_CallException, (self.label, self.args, self.kwargs, self.from_current))

    # class _JumpException(Exception):
        
    #     def __init__(self, label):
    #         for i in renpy.config._label_callbacks:
    #             i(label)

    # class _JumpOutException(Exception):
        
    #     def __init__(self, label):
    #         for i in renpy.config._label_callbacks:
    #             i(label)

    # renpy.game.CONTROL_EXCEPTIONS = tuple(list(renpy.game.CONTROL_EXCEPTIONS) + [_CallException, _JumpException, _JumpOutException])
    # renpy.game.CallException = _CallException
    # renpy.game.JumpException = _JumpException
    # renpy.game.JumpOutException = _JumpOutException

    # class _Call(renpy.ast.Call):
    #     def execute(self):
    #         statement_name("call")

    #         label = self.label
    #         if self.expression:
    #             label = renpy.python.py_eval(label)

    #         rv = renpy.game.context().call(label, return_site=self.next.name)
    #         next_node(rv)
    #         renpy.game.context().abnormal = True

    #         if self.arguments:
    #             args, kwargs = self.arguments.evaluate()
    #             renpy.store._args = args
    #             renpy.store._kwargs = kwargs
    #         else:
    #             renpy.store._args = None
    #             renpy.store._kwargs = None

    #         setattr(store, "_last_label_call", label)

    #         if config.developer:
    #             last_label = getattr(store, "_last_label_jump", None)
    #             caller_id = renpy.get_filename_line()
    #             print(f"Called '{stdcol.PURPLE}{label}{stdcol.END}' from '{stdcol.PURPLE}{last_label}{stdcol.END}' with ARGS:'{stdcol.YELLOW}{args}{stdcol.END}' KWARGS:'{stdcol.YELLOW}{kwargs}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'...")

    # class _Jump(renpy.ast.Jump):
    #     def execute(self):

    #         statement_name("jump")

    #         target = self.target
    #         if self.expression:
    #             target = renpy.python.py_eval(target)

    #         rv = renpy.game.script.lookup(target)
    #         renpy.game.context().abnormal = True

    #         next_node(rv)

    #         setattr(store, "_last_label_jump", target)

    #         if config.developer:
    #             last_label = getattr(store, "_last_label_jump", None)
    #             caller_id = renpy.get_filename_line()
    #             print(f"Jumped '{stdcol.PURPLE}{target}{stdcol.END}' from '{stdcol.PURPLE}{last_label}{stdcol.END}' with ARGS:'{stdcol.YELLOW}{args}{stdcol.END}' KWARGS:'{stdcol.YELLOW}{kwargs}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'...")

    # renpy.ast.Call = _Call
    # renpy.ast.Jump = _Jump

default _last_label = None

python early:
    def catch_label_call(label, abnormal):
        if config.developer:
            # last_label = renpy.game.context().come_from_label <- Doesn't work as expected, other methods are just as unreliable.
            # from '{stdcol.PURPLE}{last_label}{stdcol.END}'
            caller_id = renpy.get_filename_line()
            print(f"Reached '{stdcol.PURPLE}{label}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'...")

        setattr(store, "_last_label", label)

    renpy.config.label_callbacks.append(catch_label_call)

    # def catch_label_call(label, args, kwargs):
    #     # Used in event queue system to differentiate jumps from calls.
    #     if config.developer:
    #         last_label = getattr(store, "_last_label_jump", None)
    #         caller_id = renpy.get_filename_line()
    #         print(f"Called '{stdcol.PURPLE}{label}{stdcol.END}' from '{stdcol.PURPLE}{last_label}{stdcol.END}' with ARGS:'{stdcol.YELLOW}{args}{stdcol.END}' KWARGS:'{stdcol.YELLOW}{kwargs}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'...")

    #     setattr(store, "_last_label_call", label)

    # def catch_label_jump(label):
    #     # if getattr(store, "_last_label_call", None) == label:
    #     #     return

    #     if config.developer:
    #         last_label = getattr(store, "_last_label_jump", None)
    #         caller_id = renpy.get_filename_line()
    #         print(f"Jumped '{stdcol.PURPLE}{label}{stdcol.END}' from '{stdcol.PURPLE}{last_label}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'...")

    #     setattr(store, "_last_label_jump", label)

    # renpy.config.call_callbacks = [catch_label_call] # CallException callback
    # renpy.config._label_callbacks = [catch_label_jump] # JumpException and JumpOutException callbacks; Please note this is not the same as `config.label_callbacks`

init -100 python:
    # Due to the sheer number of Doll-type objects we create and keep per each character,
    # we have to use each and every optimization technique we can get our hands on.
    # The below code implements revertable __slots__ support, which reduces memory,
    # without losing any functionality relevant to the objects that are using it.
    #
    # The code is taken from a PR proposed by Andykl:
    # https://github.com/renpy/renpy/pull/3282

    class _RevertableObject(_object):
        # Reimplementation of the Ren'py class,
        # but with slots support.
        def __new__(cls, *args, **kwargs):
            self = super(_RevertableObject, cls).__new__(cls)

            log = renpy.game.log
            if log is not None:
                log.mutated[id(self)] = None

            return self

        def __init__(self, *args, **kwargs):
            if (args or kwargs) and renpy.config.developer:
                raise TypeError("object() takes no parameters.")

        __setattr__ = renpy.revertable.mutator(object.__setattr__) # type: ignore
        __delattr__ = renpy.revertable.mutator(object.__delattr__) # type: ignore

        def _clean(self):
            return None

        def _compress(self, clean):
            return clean

        def _rollback(self, compressed):
            pass

    class SlottedObject(_RevertableObject):
        __slots__ = ()

        def __init_subclass__(cls):
            if renpy.config.developer:
                if hasattr(cls, "__getstate__"):
                    raise TypeError("slotted_object subclasses can't have "
                                    "__getstate__ method. Use __reduce__ instead.")

                for slot in cls.__dict__.get("__slots__", ()):
                    if slot.startswith("__") and not slot.endswith("__"):
                        raise ValueError("slotted_object __slots__ can not be mangled. "
                                         "If you need it, mangle it by yourself.")

        def _clean(self):
            rv = object.__reduce_ex__(self, 2)[2]
            # We need to make a copy of __dict__ to avoid its futher mutations.

            # No attributes are set
            if rv is None:
                rv = { }

            # Only __dict__ have attributes
            elif isinstance(rv, dict):
                rv = rv.copy()

            # Only __slots__ have attributes
            elif rv[0] is None:
                rv = rv[1]

            # Otherwise it is (__dict__, __slots__), so merge it together
            else:
                rv = dict(rv[0], **rv[1])

            return rv

        def _rollback(self, compressed):
            if hasattr(self, "__dict__"):
                self.__dict__.clear()

            for k, v in compressed.items():
                setattr(self, k, v)

    # The original does not support nested actions.
    @renpy.pure
    def If(expression, true=None, false=None):

        if isinstance(expression, Action):
            expression = expression()

        return true if expression else false
