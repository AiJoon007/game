init python:
    class DollBody(DollMethods):
        layer_types = {
            # Body class has no use for layer types
        }

        layer_modifiers = {
            "zorder": None,
        }

        __slots__ = ("char", "hue", "zorder", "_hash")

        def __init__(self, obj):
            self.char = obj
            self.hue = HueMatrix(0)
            self.zorder = 0
            self._hash = None

        def set_hue(self, hue):
            self.hue = HueMatrix(hue)
            self.is_stale()

        def generate_hash(self):
            bodyparts_hash = str([x[0]._hash for x in self.char.states.values() if istype(x[0], DollBodypart) and x[2]])
            salt = str( [self.char.name, self.char.pose, str(self.hue.__hash__()), bodyparts_hash])
            return hash(salt)

        @functools.cache
        def get_layers(self, hash):
            layers = {}

            for object, zorder, is_worn in self.char.states.values():
                if istype(object, DollBodypart) and is_worn is True:
                    layers.update(object.get_layers(object._hash))

            return layers

        @functools.cache
        def build_image(self, hash, matrix=None):
            if matrix is None:
                matrix = self.hue

            processors = {
                "default": lambda file: Transform(Image(file), matrixcolor=matrix),
            }

            layers = self.get_layers(hash)

            sprites = []
            for identifier, (file, zorder) in layers.items():
                processor = processors.get(identifier, processors["default"])
                processed_file = processor(file)
                sprites.append((identifier, processed_file, zorder))

            return sprites

        @property
        def image(self):
            if not renpy.is_skipping() and self.is_stale():
                hash = self._hash

                sprites = self.build_image(hash, self.hue)
                sprites.sort(key=itemgetter(2))
                sprites = [x[1] for x in sprites]

                self._image = Fixed(*sprites, fit_first=True)
            return self._image
