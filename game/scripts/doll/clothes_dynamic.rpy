init python:
    class DollClothDynamic(DollCloth):
        prefixes = ["!=", "?=", "+=", "!", "?", "+"]

        def __init__(self, name, categories, type, id, color, zorder=None, unlocked=False, level=0, blacklist=[], modpath=None, tracking=None, parent=None):
            self._tracking = tracking

            super().__init__(name, categories, type, id, color, zorder, unlocked, level, blacklist, modpath, parent)

        def __repr__(self):
            return f"DollClothDynamic(name='{self.name}', categories={self.categories}, type='{self.type}', id='{self.id}', color={self.color}, zorder={self.zorder}, unlocked={self.unlocked}, level={self.level}, blacklist={self.blacklist}, modpath={self.modpath or None}, tracking='{self._tracking}', parent={self.parent})"

        @functools.cached_property
        def prefix(self):
            return next((p for p in self.prefixes if self._tracking.startswith(p)), None)

        @functools.cached_property
        def tracking(self):
            prefixes = "".join(self.prefixes)
            return self._tracking.strip(self.prefix)

        @property
        def tracking_object(self):
            if self.prefix in ("!", "?", "+"):
                return self.char.states.get(self.tracking)[0]
            else:
                return eval(self.tracking)

        def generate_hash(self):
            tracking_object = self.tracking_object
            tracking_hash = str(tracking_object._hash) if tracking_object else "default"
            salt = str( [self.name, self.char.pose, self.type, self.id, str(self.color), str(self.char.body._hash)] ) + tracking_hash
            return hash(salt)

        @functools.cache
        def get_layers(self, hash, subpath="", _ignore_equipped=False):
            path = posixpath.join(self.modpath, "characters", self.name, "poses", self.char.pose, subpath, "clothes", self.type, self.id)
            _tracking = self._tracking

            def _negative_lookahead():
                return None if self.tracking_object else "default"

            def _lookahead(path):
                tracking_object = self.tracking_object
                tracking_id = tracking_object.id if tracking_object else None
                path = posixpath.join(path, tracking_id)

                if not any(fp.startswith(path) for fp in renpy.list_files()):
                    return "default"
                return tracking_id

            def _chainload():

                def __wrapper(obj):

                    def ___chain(obj):
                        if isinstance(obj, DollClothDynamic):
                            return "+".join( (obj.id, ___chain(obj.tracking_object)) )
                        return obj.id

                    return ___chain(obj)

                tracking_object = self.tracking_object

                if tracking_object:

                    chain = __wrapper(tracking_object)
                    tracking_id = chain

                    return tracking_id
                return None

            def _negative_lookahead_item():
                tracking_object = self.tracking_object
                return None if self.char.is_equipped_item(tracking_object) else "default"

            def _lookahead_item():
                tracking_object = self.tracking_object
                return tracking_object.id if self.char.is_equipped_item(tracking_object) else "default"

            def _default():
                tracking_object = self.tracking_object
                return tracking_object.id if tracking_object else None

            if _ignore_equipped:
                tracking_id = "default"
            else:
                processors = {
                    "!": lambda tracking, _: _negative_lookahead(),
                    "?": lambda tracking, path: _lookahead(path),
                    "+": lambda tracking, _: _chainload(),
                    "!=": lambda tracking, _: _negative_lookahead_item(),
                    "?=": lambda tracking, _: _lookahead_item(),
                    "+=": lambda tracking, _: _chainload(),
                    None: lambda tracking, _: _default()
                }

                processor = processors[self.prefix]
                tracking_id = processor(_tracking, path)

                if tracking_id is None:
                    print(f"Invalid tracker for object: {self}")
                    return {}

            path = posixpath.join(path, tracking_id)

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

        @functools.cache
        def build_icon(self, hash):
            if self.prefix in ("!", "!="):
                self.layers = self.get_layers(hash, _ignore_equipped=True)
                hash = self.generate_hash()
                tracking_object = None
            else:
                tracking_object = self.tracking_object

            matrix = SaturationMatrix(0.0)
            sprites = [i for i in self.build_image(hash, matrix=matrix) if not i[0] == "mask"]

            if not tracking_object is None:
                sprites.extend([i for i in tracking_object.build_image(tracking_object._hash, matrix=matrix) if not i[0] == "mask"])

            sprites.extend(self.char.body.build_image(self.char.body._hash, matrix=matrix))
            sprites.sort(key=itemgetter(2))
            bounds = self.get_layers(hash).get("outline", [sprites[0][1]])[0]

            wmax, hmax = self.sizes
            wmin = hmin = 96

            x, y, w, h = crop_whitespace(bounds)
            xoffset, yoffset = w/2, h/2

            w = h = max(w, h, wmin, hmin)

            w = max(wmin, w + w/2)
            h = max(hmin, h + h/2)

            x = clamp( (x - w/2) + xoffset, 0, wmax)
            y = clamp( (y - h/2) + yoffset, 0, hmax)

            # Forbid exceeding the image height.
            if y+h > hmax:
                y = hmax-h

            return Transform(Fixed(*[i[1] for i in sprites], fit_first=True), crop=(x, y, w, h), size=(96, 96), fit="contain", align=(0.5, 0.5))

        def clone(self):
            """Creates a clone of this cloth object. Since it requires a parent object it should be used internally only to avoid object depth issue."""
            modpath = self.modpath.lstrip("mods/")
            return DollClothDynamic(self.name, self.categories, self.type, self.id, [x for x in self.color] if self.color else None, self.zorder, self.unlocked, self.level, self.blacklist, modpath, self._tracking, self)
