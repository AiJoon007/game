init -5 python:

    start_skip_callbacks = []
    end_skip_callbacks = []

    class SkipCallbacksHandler(NoRollback):

        def __init__(self):
            self.was_skipping = False

        def __call__(self):
            if renpy.in_rollback():
                return

            is_skipping = renpy.is_skipping()
            was_skipping = self.was_skipping

            if is_skipping and not was_skipping:
                self.was_skipping = True
                for c in start_skip_callbacks:
                    c()

            elif was_skipping and not renpy.is_skipping():
                self.was_skipping = False
                for c in end_skip_callbacks:
                    c()

    config.interact_callbacks.append(SkipCallbacksHandler())
