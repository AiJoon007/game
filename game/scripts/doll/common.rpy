
init -1 python:

    ### Classes ###

    class DollDisplayable(renpy.Displayable):
        def __init__(self, child, **properties):
            super(DollDisplayable, self).__init__(**properties)
            self.focusable = None
            self.child = child

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            c = self.child
            cr = renpy.render(c, width, height, st, at)

            # We need to find the 'true' size of the displayable
            # otherwise it may end up being the size of a null,
            # or any other irrelevant element.

            xsize, ysize = cr.get_size()
            xoffset, yoffset = c.place(rv, 0, 0, width, height, cr)

            width = max(xoffset + xsize, width)
            height = max(yoffset + ysize, height)

            rv.width = width
            rv.height = height

            return rv

        def event(self, ev, x, y, st):
            return None
            #raise renpy.IgnoreEvent() # Seems to work similar to NullAction

        def focus(self, default=False):
            raise Exception("Not Implemented")

        def unfocus(self, default=False):
            raise Exception("Not Implemented")

        def is_focused(self):
            return False

        def visit_all(self, callback, seen=None):
            return

        def visit(self):
            return []

    class DollMethods(SlottedObject):
        """Container class for commonly used methods and attributes"""

        _loading = Text("Loading", align=(0.5, 0.5))
        _image = Null()
        _image_cached = False
        blacklist_toggles = ("hair", "glasses", "pubes", "piercing", "makeup", "tattoo", "earrings")
        blacklist_unequip = ("hair",)
        blacklist_strip = ("pubes", "piercing", "tattoo")
        multislots = ("makeup", "accessory", "piercing", "tattoo")
        extensions = {".webp", ".png", ".jxl", ".avif"}
        sizes = (1010, 1200) # Default sizes used for defining rare cases

        @property
        def image(self):
            if not renpy.is_skipping():
                if not self._image_cached:
                    self._image_cached = True
                    self._image = self.build_image()
            return self._image

        def is_stale(self):
            curr_hash = self.generate_hash()
            stale = curr_hash != self._hash
            self._hash = curr_hash
            return stale

    def DollRebuild():
        for i in states.dolls:
            doll = getattr(store, i)

            if doll.is_stale() and not settings.get("multithreading"):
                doll.show(ignore_skipping=True)

        renpy.restart_interaction()

    config.after_load_callbacks.append(DollRebuild)
    end_skip_callbacks.append(DollRebuild)
