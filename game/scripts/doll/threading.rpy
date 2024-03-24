init python early:
    import threading
    import queue

    class DollThread(threading.Thread, NoRollback):
        __lock = threading.RLock()
        _count = 0
        _instances = _list()
        _interval = 0.05 if renpy.android else 0.025

        def __init__(self, interval=None, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
            threading.Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

            self._return = None
            self.interval = interval or self._interval
            self._delay = threading.Timer(self.interval, self._execute)
            self._stop = threading.Event()

        def start(self):
            DollThread._instances.append(self)
            DollThread._count += 1
            super().start()

        def run(self):
            with DollThread.__lock:
                self._delay.start()
                self._delay.join()
                self.stop()

        def _execute(self):
            while not self._stop.is_set():
                if self._target is not None:
                    self._return = self._target(*self._args, **self._kwargs)
                    renpy.restart_interaction()
                    break

        def join(self, timeout=None):
            super().join(timeout=timeout)
            return self._return

        def stop(self):
            self._stop.set()

            if self in DollThread._instances:
                DollThread._instances.remove(self)
                DollThread._count -= 1

                if DollThread._count <= 0:
                    renpy.restart_interaction()

        @classmethod
        def stop_all(cls):
            for thread in cls._instances:
                # Allow threads to exit gracefully before forceful termination
                thread.stop()

            # if not renpy.android:
            #     # Then forcefully terminate the remainders (except on android because that stalls the renderer)
            #     for thread in cls._instances:
            #         thread.join()

    class DefaultQueue(queue.Queue, NoRollback):
        def __init__(self):
            super().__init__()
            self.last_item = None

        def put(self, item, block=True, timeout=None):
            super().put(item, block, timeout)
            self.last_item = item

        def get_with_default(self, default):
            try:
                return self.get(block=False)
            except queue.Empty:
                return self.last_item or default

        def __getstate__(self):
            state = self.__dict__.copy()
            del state['last_item']
            del state['mutex']
            del state['not_empty']
            del state['not_full']
            del state['all_tasks_done']
            return state

        def __setstate__(self, state):
            self.__dict__.update(state)
            self.last_item = None
            self.mutex = threading.Lock()
            self.not_empty = threading.Condition(self.mutex)
            self.not_full = threading.Condition(self.mutex)
            self.all_tasks_done = threading.Condition(self.mutex)

        def __reduce__(self):
            return (DefaultQueue, ())

        def __reduce_ex__(self, protocol):
            return DefaultQueue, (), self.__getstate__(), None, iter([])
