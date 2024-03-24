init python:
    class DollMakeup(DollCloth):
        def __init__(self, name, categories, type, id, color, zorder=None, unlocked=False, level=0, blacklist=[], modpath=None, parent=None, tracking=None):
            self.tracking = tracking

            super().__init__(name, categories, type, id, color, zorder, unlocked, level, blacklist, modpath, parent)

        def __repr__(self):
            return f"DollMakeup(name={self.name}, categories={self.categories}, type={self.type}, id={self.id}, color={self.color}, zorder={self.zorder}, unlocked={self.unlocked}, level={self.level}, blacklist={self.blacklist}, parent={self.parent}, modpath={self.modpath or None}, tracking={self.tracking})"

        def generate_hash(self):
            salt = str( [self.name, self.type, self.char.pose, self.id, str(self.color), str(self.char.face._hash), str(self.char.body._hash)] )
            return hash(salt)

        @functools.cache
        def get_layers(self, hash, subpath=""):
            tracking = self.char.face._face.get(self.tracking, None)

            if tracking is None:
                print(f"Invalid tracker for object: {self}")
                return []

            path = posixpath.join(self.modpath, "characters", self.name, "poses", self.char.pose, subpath, "clothes", self.type, self.id, tracking)

            extensions = self.extensions
            types = self.layer_types
            modifiers = self.layer_modifiers

            layers = {}
            for f in renpy.list_files():
                fp, fn = os.path.split(f)
                fn, ext = os.path.splitext(fn)

                if not fp == path or not ext in extensions:
                    continue

                ltype, *tails = fn.rsplit("_")

                if not ltype.isdigit() and not ltype in types:
                    print(f"Invalid layer type for file: {f}")
                    continue

                zorder = z if (z := types.get(ltype)) is not None else self.zorder

                if isinstance(zorder, str):
                    zorder = self.zorder + int(zorder)

                if tails:
                    lmodifier, *tails = tails

                    if not lmodifier in modifiers:
                        print("Invalid modifier for file: {}".format(f))
                        continue

                    zorder_mod = modifiers.get(lmodifier)
                    zorder = (zorder + int(zorder_mod)) if lmodifier != "zorder" else int(tails[-1])
                    layers.setdefault("_".join([ltype, lmodifier]), [f, zorder])
                else:
                    layers.setdefault(ltype, [f, zorder])

            return layers

        def clone(self):
            """Creates a clone of this cloth object. Since it requires a parent object it should be used internally only to avoid object depth issue."""
            modpath = self.modpath.lstrip("mods/")
            return DollMakeup(self.name, self.categories, self.type, self.id, [x for x in self.color] if self.color else None, self.zorder, self.unlocked, self.level, self.blacklist, modpath, self, self.tracking)
