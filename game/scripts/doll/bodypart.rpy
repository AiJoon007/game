init 1 python:
    class DollBodypart(DollCloth):
        layer_types = {
            "mask": "-1",
        }

        layer_modifiers = {
            "zorder": None,
        }

        def __init__(self, name, categories, type, id, zorder=None, unlocked=False, level=0, blacklist=[], parent=None, modpath=None):
            super().__init__(name, categories, type, id, None, zorder, unlocked, level, blacklist, parent, modpath)

        def __repr__(self):
            return f"DollBodypart(name={self.name}, categories={self.categories}, type={self.type}, id={self.id}, color={self.color}, zorder={self.zorder}, unlocked={self.unlocked}, level={self.level}, blacklist={self.blacklist}, parent={self.parent}, modpath={self.modpath or None})"

        def generate_hash(self):
            salt = str( [self.name, self.type, self.char.pose, self.id, str(self.char.body._hash)] )
            return hash(salt)

        @functools.cache
        def get_layers(self, hash, subpath=""):
            path = posixpath.join(self.modpath, "characters", self.name, "poses", self.char.pose, subpath, "bodyparts", self.type, self.id)

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

                # if not ltype in types:
                #     print("Invalid layer type for file: {}".format(f))
                #     continue

                zorder = types.get(ltype) or self.zorder

                if isinstance(zorder, str):
                    # Note: Layer uses relative zorder if it's passed as a string
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

        def apply_color(self, img, n):
            raise NotImplementedError

        def set_color(self, n):
            raise NotImplementedError

        def reset_color(self, n=None):
            raise NotImplementedError
