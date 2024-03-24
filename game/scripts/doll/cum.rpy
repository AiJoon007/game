init python:
    class DollCum(DollMethods):
        layer_types = {
            "mask": "-1",
            "skin": 1,
            "cum": None,
        }

        layer_modifiers = {
            "back": "-300",
            "front": "+300",
            "zorder": None,
        }

        __slots__ = ("char", "_cum", "_hash")

        def __init__(self, obj):
            self.char = obj
            self._cum = {k: None for k in (self.char.clothing_layers | self.char.face_layers).keys()}
            self._hash = None

        def generate_hash(self):
            salt = str( [self.char.name, self.char.pose, str(self.char.face._hash), str(self.char.face._hash), str([x[0]._hash for x in self.char.states.values() if x[0] and x[2]]), sorted(list(self._cum.items()))] )
            return hash(salt)

        def set_cum(self, *args, **kwargs):
            if args:
                self._cum = {k: args[0] for k in self._cum}

            self._cum.update(kwargs)
            self.is_stale()

        @functools.cache
        def get_layers(self, hash, subpath=""):

            def _lookahead(path):
                return any(fp.startswith(path) for fp in renpy.list_files())

            cum = self._cum

            extensions = self.extensions
            types = self.layer_types
            modifiers = self.layer_modifiers
            face_layers = self.char.face_layers
            body_layers = self.char.body_layers
            clothing_layers = self.char.clothing_layers

            active_faces = self.char.face._face
            active_clothes = self.char.states

            layers = {}
            for part, name in cum.items():

                if name is None:
                    continue

                if part in face_layers:
                    zorder = face_layers.get(part) + 1
                    identifier = active_faces.get(part, "default")

                    if not isinstance(identifier, str):
                        continue

                    path = posixpath.join(self.char.modpath, "characters", self.char.name, "poses", self.char.pose, subpath, "cum", part, name, identifier)
                elif part in (clothing_layers | body_layers):

                    cloth, zorder, is_worn = active_clothes.get(part, [None, None, None])

                    if cloth is None or not is_worn:
                        continue

                    identifier = cloth.id
                    modpath = cloth.modpath
                    zorder = cloth.zorder + 1

                    path = posixpath.join(modpath, "characters", self.char.name, "poses", self.char.pose, "cum", part, name, identifier)
                    path = path if _lookahead(path) else posixpath.join(os.path.split(path)[0], (identifier := "default"))
                else:
                    zorder = 100
                    path = posixpath.join(self.char.modpath, "characters", self.char.name, "poses", self.char.pose, "cum", part, name)

                if config.developer and not _lookahead(path):
                    print(f"Files and/or directories are missing: {path}/")

                for f in renpy.list_files():
                    fp, fn = os.path.split(f)
                    fn, ext = os.path.splitext(fn)

                    if not fp == path or not ext in extensions:
                        continue

                    ltype, *tails = fn.rsplit("_")

                    if not ltype in types:
                        print(f"Invalid layer type for file: {f}")
                        continue

                    zorder = types.get(ltype) or zorder

                    if tails:
                        lmodifier, *tails = tails

                        if not lmodifier in modifiers:
                            print(f"Invalid modifier for file: {f}")
                            continue

                        zorder_mod = modifiers.get(lmodifier)
                        zorder = (zorder + int(zorder_mod)) if lmodifier != "zorder" else int(tails[-1])
                        layers.setdefault(" ".join([part, name, ltype, lmodifier]), [f, zorder])
                    else:
                        layers.setdefault(" ".join([part, name, ltype]), [f, zorder])

            return layers

        @functools.cache
        def build_image(self, hash, subpath="", matrix=None):
            if matrix is None:
                matrix = self.char.body.hue

            processors = {
                "skin": lambda file: Transform(file, matrixcolor=matrix),
                "default": lambda file: Image(file),
            }

            layers = self.get_layers(hash, subpath)

            sprites = []
            for identifier, (file, zorder) in layers.items():

                cum_type, name, ltype = identifier.rsplit(" ")
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
