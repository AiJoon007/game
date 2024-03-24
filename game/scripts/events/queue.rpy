
default event_callbacks = []

default _events_completed_any = None
default _events_completed_all = None
default _events_filtered_completed_all = None
default _events_filtered_completed_any = None
default _event_completed = None
default _event_completed_failed = None
default _event_queue = None
default _event = None

init -1 python:

    class EventQueue(object):
        ignore_globals = ("mainloop",)

        def __init__(self, id=None):
            self.id = id

            self.queue = []
            self.freeze = False

            if config.developer:
                rollback = f"{stdcol.UNDERLINE}(Rollback){stdcol.END} " if renpy.in_rollback() else ""
                print(f"{rollback}Creating EventQueue object '{stdcol.BLUE}{id}{stdcol.END}' ...")

        def freeze(self):
            self.freeze = True

        def unfreeze(self):
            self.freeze = False

        def delay(self, n):
            for i in self.queue:
                i.wait += n

        def tick(self):
            """Causes time to pass."""
            if self.freeze:
                return

            for i in self.queue:
                i.wait -= 1

        def list_filtered(self, func=lambda ev: (ev.wait <= 0) and not ev.disabled and ev.requirements_met()):
            # queue = [ev for ev in self.queue if (ev.wait <= 0) and not ev.disabled and ev.requirements_met() ]
            # queue.sort(key=lambda x: x.priority)

            filtered = sorted(filter(func, self.queue), key=lambda x: x.priority)

            return filtered

        def initialize_globals(self):
            global _event_queue, _events_completed_all, _events_completed_any, _events_filtered_completed_all, _events_filtered_completed_any

            _event_queue = self

            queue = self.queue

            _events_completed_all = all(ev.completed for ev in queue)
            _events_completed_any = any(ev.completed for ev in queue)

            queue = self.list_filtered()

            _events_filtered_completed_all = all(ev.completed for ev in queue)
            _events_filtered_completed_any = any(ev.completed for ev in queue)

        def next(self):
            queue = self.list_filtered()
            repeatable = []

            for ev in queue:
                if ev.completed:
                    if ev.repeat:
                        repeatable.append(ev)
                        
                    continue

                return ev

            if repeatable:
                return renpy.random.choice(repeatable)

        def start(self):
            if not self.id in self.ignore_globals:
                self.initialize_globals()

            ev = self.next()

            if ev:
                return ev.start(self)

        def _debug(self, sort=lambda x: x.priority):
            queue = self.queue
            queue.sort(key=sort)

            for ev in queue:
                s = f"ID:{ev.id} QUE:{ev.queued} STA:{ev.started} COM:{ev.completed} COMF:{ev.completed_failed} DIS:{ev.disabled}"

                print(s)

        def _debug_menu(self):
            queue = self.queue
            queue.sort(key=lambda x: x.priority)

            menu = []

            for ev in queue:
                req = f"{{color=#00ff00}}{ev.req}{{/color}}" if ev.requirements_met() else f"{{color=#ff0000}}{ev.req}{{/color}}"

                s = f"{{size=12}}id:{ev.id} label:{ev.label}{{/size}}{{size=8}}\npriority:{ev.priority} Daytime:{ev.daytime} Req:{req} AutoENQ:{ev.autoenqueue} AutoDEQ:{ev.autodequeue}{{/size}}"
                l = ev.label

                menu.append( (s, l) )

            renpy.display_menu(menu)

    class Event(object):
        _queue = None
        _parent = None

        def __init__(self, id, wait=0, priority=5, daytime=None, req=None, label=None, func=None, queue="eventqueue", autoenqueue=False, autodequeue=True,
            repeat=True, fail_suffixes=("_fail", "too_much", "too_much_public"), ignore_labels=[], subevents=[], disabled=False):
            self.id = id
            self.wait = wait
            self.priority = priority
            self.daytime = daytime
            self.req = req
            self.label = label
            self.func = func
            self.queue = queue
            self.autoenqueue = autoenqueue
            self.autodequeue = autodequeue
            self.repeat = repeat
            self.fail_suffixes = tuple(fail_suffixes)
            self.ignore_labels = ignore_labels
            self.subevents = subevents 
            self.disabled = disabled

            for ev in subevents:
                getattr(store, ev)._parent = self

            self.queued = False
            self.started = False
            self.completed = False
            self.completed_failed = False

            # Validation
            if not renpy.has_label(self.label):
                raise Exception(f"Supplied label does not exist:\n{self.label}")

            if autoenqueue:
                self.enqueue()

        if config.developer:
            def __setattr__(self, attr, value):
                if hasattr(self, attr) and getattr(self, attr) != value:
                    id = getattr(self, "id")
                    rollback = f"{stdcol.UNDERLINE}(Rollback){stdcol.END} " if renpy.in_rollback() else ""
                    caller_id = renpy.get_filename_line()

                    if not "/00start.rpy" in caller_id[0]:
                        # Ignore init
                        print(f"{rollback}Setting '{stdcol.GREEN}{id}{stdcol.END}.{stdcol.RED}{attr}{stdcol.END}={stdcol.YELLOW}{value}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'...")

                super().__setattr__(attr, value)

        def disable(self):
            self.disabled = True

        def enable(self):
            self.disabled = False

        @property
        def queue(self):
            return getattr(store, self._queue).queue if self._queue else None

        @queue.setter
        def queue(self, name):
            self._queue = name

            if name is not None and not hasattr(store, name):
                setattr(store, name, EventQueue(name))

        def enqueue(self, queue=None):
            if queue:
                queue = getattr(store, queue).queue
            else:
                queue = self.queue

            if not self in queue:
                if config.developer:
                    rollback = f"{stdcol.UNDERLINE}(Rollback){stdcol.END} " if renpy.in_rollback() else ""
                    name = getattr(store, self._queue).id
                    caller_id = renpy.get_filename_line()

                    if not "/00start.rpy" in caller_id[0]:
                        print(f"{rollback}Enqueueing '{stdcol.GREEN}{self.id}{stdcol.END}' into '{stdcol.BLUE}{name}{stdcol.END}' ...")

                queue.append(self)
            self.queued = True

        def dequeue(self, queue=None):
            if queue:
                queue = getattr(store, queue).queue
            else:
                queue = self.queue

            if self in queue:
                if config.developer:
                    rollback = f"{stdcol.UNDERLINE}(Rollback){stdcol.END} " if renpy.in_rollback() else ""
                    name = getattr(store, self._queue).id
                    caller_id = renpy.get_filename_line()

                    if not "/00start.rpy" in caller_id[0]:
                        print(f"{rollback}Dequeued '{stdcol.GREEN}{self.id}{stdcol.END}' from '{stdcol.BLUE}{name}{stdcol.END}' ...")

                queue.remove(self)

            self.queued = False

        def requirements_met(self):
            if self.req:
                try:
                    return eval(self.req)
                except Exception as e:
                    msg = f"Event '{self.id}' requirements evaluation has failed:\n{e} for '{self.req}'"
                    if config.developer:
                        raise Exception(msg)
                    else:
                        print(msg)
                        renpy.notify("An error has occured. Check console for details.")
            return True

        def start(self, _caller=None):
            global _event, _event_completed, _event_completed_failed

            if config.developer:
                rollback = f"{stdcol.UNDERLINE}(Rollback){stdcol.END} " if renpy.in_rollback() else ""
                caller_id = _caller.id if _caller else renpy.get_filename_line()
                print(f"{rollback}Starting '{stdcol.GREEN}{self.id}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}' ... ")

            self.started = True

            _event = self
            _event_completed = self.completed
            _event_completed_failed = self.completed_failed

            if self.autodequeue:
                queue = _caller.queue or self.queue
                queue.remove(self)
                self.queued = False

            ## additional requirements check

            if not self._track_completion in event_callbacks:
                event_callbacks.append(self._track_completion)

            if self.func:
                self.func()

            if self.label:
                return renpy.jump(self.label)

        def cancel(self, _caller=None):
            if config.developer:
                rollback = f"{stdcol.UNDERLINE}(Rollback){stdcol.END} " if renpy.in_rollback() else ""
                caller_id = _caller.id if _caller else renpy.get_filename_line()
                print(f"{rollback}Cancelling '{stdcol.GREEN}{self.id}{stdcol.END}' caller '{stdcol.BLUE}{caller_id}{stdcol.END}'... ")

            self.started = False
            self.completed = False
            self.completed_failed = False

            if self._track_completion in event_callbacks:
                event_callbacks.remove(self._track_completion)

            if self._parent:
                self._parent.cancel()

            if renpy.get_return_stack():
                renpy.pop_call()

            renpy.block_rollback()

        def _track_completion(self, label, abnormal):
            if renpy.is_init_phase():
                return

            if label == self.label:
                # Ignore jumps to self.
                return

            if label in self.ignore_labels:
                # Postpone completing the event until end label returns.
                return

            if "." in label:
                # Ignore local labels
                return

            # if abnormal: # Irrelevant
            #     return

            if renpy.game.context().return_stack:
                # If return stack exists, ignore, because we're probably in a call label.
                # We only allow room_menu, to pass.
                return

            if self.started: # Event cancelled abnormally?

                if label.endswith(self.fail_suffixes):
                    self.completed_failed = True
                else:
                    self.completed = True

                self.started = False

                for ev in self.subevents:
                    if isinstance(ev, str):
                        ev = getattr(store, ev)
                    ev.enqueue()

            if self._track_completion in event_callbacks:
                event_callbacks.remove(self._track_completion)

    def execute_event_callbacks(label, abnormal):
        if renpy.is_init_phase() or not hasattr(store, "event_callbacks"):
            return

        for callback in event_callbacks: callback(label, abnormal)

    def initialize_event_callbacks():
        if renpy.in_rollback():
            return

        # We need to add these after defaults are finished.
        renpy.config.label_callbacks.append(execute_event_callbacks)

    def show_events_menu(queues, filter=False, report_progress=True, **kwargs):
        # This function is a stop gap until we update interfaces. Because it's not tied to any internals,
        # it can be easily replaced or changed in the future without breaking save compatibility.
        def menu_hints(queue, filter):
            filtered_queue = queue.list_filtered() if filter is False else queue.list_filtered(filter)
            total_applicable = len(filtered_queue)
            total_events = len(queue.queue)
            completed = 0
            icons = []

            for ev in filtered_queue:
                if ev.completed:
                    icons.append(f"interface/icons/small/heart_red.webp")
                    completed += 1
                elif ev.completed_failed:
                    icons.append(f"interface/icons/small/heart_black.webp")
                    completed += 1
                else:
                    icons.append(f"interface/icons/small/heart_empty.webp")

            hints = f" {completed}/{total_applicable}/{total_events}"

            return (hints, icons)

        l = []

        for queue, title in queues:
            if isinstance(queue, str):
                queue = getattr(store, queue)

            hints, icons = menu_hints(queue, filter)
            title = f"-{title}-"

            if config.developer:
                title += hints

            if ( ev := queue.next()) and ev.requirements_met():
                action = queue
            elif ( ev := queue.next()) and ev.disabled:
                action = "disabled"
            else:
                action = "noncompliant"

            _kwargs = {}

            if action in ("disabled", "noncompliant"):
                _kwargs["style"] = "disabled"
            elif report_progress:
                _kwargs = {"progress": icons}

            location = renpy.game.context().current
            choice = ui.ChoiceReturn(title, action, location, kwargs=_kwargs)

            l.append( (title, choice) )

        l.append( ("-Never mind-", "exit") )
        return renpy.display_menu(l, **kwargs)

    config.after_default_callbacks.append(initialize_event_callbacks)

init offset = -5

default eventqueue = EventQueue("mainloop")
