init python:
    class DollFace(DollMethods):
        layer_types = {
            "eyemask": -1,
            "skin": 1,
            "expression": None,
        }

        layer_modifiers = {
            "zorder": None,
        }

        __slots__ = ("char", "_cum", "_hash")

        def __init__(self, obj):
            self.char = obj
            self._face = {k: None for k in self.char.face_layers.keys()}
            self._hash = None

        def set_face(self, **kwargs):
            self._face.update((k, v) for k, v in kwargs.items() if not v is None)
            self.is_stale()

        def generate_hash(self):
            salt = str( [self.char.name, self.char.pose, str(self.char.body._hash), sorted(list(self._face.items()))] )
            return hash(salt)

        @functools.cache
        def get_layers(self, hash, subpath=""):
            face = self._face

            extensions = self.extensions
            types = self.layer_types
            modifiers = self.layer_modifiers
            face_layers = self.char.face_layers

            layers = {}
            for part, name in face.items():

                if name in (None, False):
                    continue

                path = posixpath.join(self.char.modpath, "characters", self.char.name, "poses", self.char.pose, subpath, "face", part, name)

                for f in renpy.list_files():
                    fp, fn = os.path.split(f)
                    fn, ext = os.path.splitext(fn)

                    if not fp == path or not ext in extensions:
                        continue

                    ltype, *tails = fn.rsplit("_")

                    if not ltype in types:
                        print("Invalid layer type for file: {}".format(f))
                        continue

                    zorder = types.get(ltype) or face_layers.get(part)

                    if tails:
                        lmodifier, *tails = tails

                        if not lmodifier in modifiers:
                            print("Invalid modifier for file: {}".format(f))
                            continue

                        zorder_mod = modifiers.get(lmodifier)
                        zorder = (zorder + int(zorder_mod)) if lmodifier != "zorder" else int(tails[-1])
                        layers.setdefault(" ".join([part, name, ltype, lmodifier]), [f, zorder])
                    else:
                        layers.setdefault(" ".join([part, name, ltype]), [f, zorder])

            return layers

        @functools.cache
        def build_image(self, hash, subpath="", matrix=None):
            layers = self.get_layers(hash, subpath)
            eyemask = next((layers.pop(k, None) for k in layers if "eyemask" in k), [None])[0]

            if matrix is None:
                matrix = self.char.body.hue

            processors = {
                "skin": lambda file: Transform(file, matrixcolor=matrix),
                "pupils": lambda file: AlphaMask(file, eyemask),
                "default": lambda file: Image(file),
            }

            sprites = []
            for identifier, (file, zorder) in layers.items():

                expr_type, name, ltype, *tails = identifier.rsplit(" ")

                if expr_type == "pupils":
                    if not eyemask:
                        continue

                    processor = processors["pupils"]
                else:
                    processor = processors.get(ltype, processors["default"])

                processed_file = processor(file)
                sprites.append((identifier, processed_file, zorder))

            return sprites

        @property
        def image(self):
            if not renpy.is_skipping() and self.is_stale():
                hash = self._hash

                sprites = self.build_image(hash)
                sprites.sort(key=itemgetter(2))
                sprites = [x[1] for x in sprites]

                self._image = Fixed(*sprites, fit_first=True)
            return self._image
