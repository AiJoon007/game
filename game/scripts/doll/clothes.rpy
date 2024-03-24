init python:
    class DollCloth(DollMethods):
        layer_types = {
            "mask": "-1",
            "skin": 10,
            "armfix": "+1",
            "outline": None,
            "extra": None,
            "overlay": None,
        }

        layer_modifiers = {
            "back": "-300",
            "front": "+300",
            "zorder": None,
        }

        _loading = Fixed(Text("Loading", align=(0.5, 0.5)), xysize=(96, 96))

        __slots__ = ("name", "categories", "type", "id", "color", "unlocked", "level", "blacklist", "modpath", "parent", "char", "color_default", "zorder", "seen", "_hash")

        def __init__(self, name, categories, type, id, color, zorder=None, unlocked=False, level=0, blacklist=[], modpath=None, parent=None):
            self.name = name
            self.categories = categories
            self.type = type
            self.id = id
            self.color = [Color( (tuple(x) if isinstance(x, list) else x) ) for x in color] if color else None
            self.unlocked = unlocked
            self.level = level
            self.blacklist = blacklist
            self.modpath = "mods/" + posixpath.normpath(modpath) if modpath else ""
            self.parent = parent

            self.char = eval(name)
            self.color_default = [x for x in self.color] if self.color else None
            self.zorder = zorder or self.char.states[type][1]
            self.seen = self.unlocked
            self._hash = self.generate_hash()
            self._button = DefaultQueue()

            if config.developer:
                self._loading = Fixed(Text(self.id, size=8), self._loading, xysize=(96, 96))

            # Add to character wardrobe and unordered list
            if not parent:
                self.char.wardrobe.setdefault(self.categories[0], {}).setdefault(self.categories[1], []).append(self)
                self.char.wardrobe_list.append(self)

                # Define new item slot type if doesn't exist
                self.char.states.setdefault(self.type, [None, (self.zorder or 1), True])

        def __repr__(self):
            return f"DollCloth(name={self.name}, categories={self.categories}, type={self.type}, id={self.id}, color={self.color}, zorder={self.zorder}, unlocked={self.unlocked}, level={self.level}, blacklist={self.blacklist}, parent={self.parent}, modpath={self.modpath or None})"

        def __hash__(self):
            return self._hash

        def __eq__(self, obj):
            if not isinstance(obj, DollCloth):
                return NotImplemented
            return self._hash == obj._hash

        def __lt__(self, obj):
            if not isinstance(obj, DollCloth):
                return NotImplemented
            return self._hash < obj._hash

        def generate_hash(self):
            salt = str( [self.name, self.char.pose, self.type, self.id, str(self.color), str(self.char.body._hash)] )
            return hash(salt)

        @functools.cache
        def get_layers(self, hash, subpath=""):
            path = posixpath.join(self.modpath, "characters", self.name, "poses", self.char.pose, subpath, "clothes", self.type, self.id)

            extensions = self.extensions
            types = self.layer_types
            modifiers = self.layer_modifiers

            layers = {}
            for f in renpy.list_files():
                fp, fn = os.path.split(f)
                fn, ext = os.path.splitext(fn)

                if not fp == path or not ext in extensions:
                    continue

                # For user's sake, simplicty, and compatibility reasons,
                # we sort the layers in the code instead.
                #
                # Each file name part represents the following:
                # layertype_subtype*_zorder*_INT*
                #
                # Parts marked with * are optional and can be inserted out of order,
                # with the exception of zorder, which requires an integer appendix.
                #
                # Example valid file name combinations:
                #
                # 0.webp
                # 0_zorder_15.webp
                # 0_front.webp
                # outline.webp
                # outline_back.webp
                #
                # If multiple files exist but with different extension,
                # only the first file will be added to the dictionary.

                ltype, *tails = fn.rsplit("_")

                if not ltype.isdigit() and not ltype in types:
                    print("Invalid layer type for file: {}".format(f))
                    continue

                zorder = z if (z := types.get(ltype)) is not None else self.zorder

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

        @functools.cache
        def build_image(self, hash, subpath="", matrix=None, maxsize=(1010, 1200)):
            # Note to self: This function is called from within the new chibi class during clothes iteration,
            # as a bridge to enable colourable clothing for chibis, double-check the changes before submitting them.

            if matrix is None:
                matrix = self.char.body.hue

            processors = {
                "skin": lambda file, _: Transform(file, maxsize=maxsize, matrixcolor=matrix),
                "armfix": lambda file, _: Transform(file, maxsize=maxsize, matrixcolor=matrix),
                "colored": lambda file, n: self.apply_color(file, int(n), maxsize),
                "default": lambda file, _: Transform(file, maxsize=maxsize),
            }

            layers = self.get_layers(hash, subpath)

            sprites = []
            for identifier, (file, zorder) in layers.items():

                if ((n := identifier.rsplit("_", 1)[0]).isdigit()):
                    processor = processors["colored"]
                else:
                    processor = processors.get(identifier, processors["default"])

                processed_file = processor(file, n)
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

        @functools.cache
        def build_icon(self, hash):
            matrix = SaturationMatrix(0.0)
            sprites = [i for i in self.build_image(hash, matrix=matrix) if not i[0] == "mask"]

            try:
                bounds = self.get_layers(hash).get("outline", [sprites[0][1]])[0]
            except IndexError:
                print(f"Missing textures:\n{self.__repr__()}")
                return Text(f"TexErr\n{{color=#00ffff}}{{size=-6}}ID:{self.id}{{/size}}{{/color}}", color="#ff0000")
            sprites.extend(self.char.body.build_image(self.char.body._hash, matrix=matrix))
            sprites.sort(key=itemgetter(2))

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

        @property
        def icon(self):
            return self.build_icon(self._hash)

        def _build_button(self, _hash):
            style = "wardrobe_button"
            is_seen = self.seen
            is_equipped = self.char.is_equipped_item(self)
            is_inadequate = bool(get_character_progression(self.char.name) < self.level)
            is_blacklisted = self.char.is_blacklisted(self.type)
            is_blacklister = any(self.char.is_equipped(x) for x in self.blacklist)
            is_modded = bool(self.modpath)

            warnings = []
            if is_blacklisted or is_blacklister:
                blacklisted = [x for x in self.blacklist if self.char.is_equipped(x)] # Offender (List currently blacklisted clothing types by this item)
                blacklister = self.char.get_blacklister(self.type) # Victim (List clothing types blacklisting this item )
                warnings.append("Incompatible with:{size=-4}\n" + "\n".join(set(blacklisted + blacklister)) + "{/size}")

            child = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
            hbox = []
            overlay = []

            action = [Return(["equip", self]), self.build_button]
            unhovered = None
            foreground = None
            hover_foreground = "#ffffff80"

            if is_inadequate:
                warnings.append("Character level too low")

            if is_modded:
                warnings.append("Item belongs to a mod:\n{size=-4}{color=#35aae2}" + self.get_modname() + "{/color}{/size}")
                hbox.append(Text("M", color="#00b200", style="wardrobe_button_text"))

            if is_blacklisted or is_blacklister:
                hbox.append(Text("!", color="#b20000", style="wardrobe_button_text"))

                for i in self.char.wardrobe_list:
                    if i.unlocked and i.type == self.type:
                        action.append(i.build_button)

            if config.developer and self.level > 0:
                hbox.append(Text(str(self.level), color="#00ffff", style="wardrobe_button_text"))

            if not is_seen:
                unhovered = [Function(self.mark_as_seen), self.clear_button_cache, self.build_button]
                overlay.append(Text("NEW", align=(1.0, 1.0), offset=(-6, -6), style="wardrobe_button_text"))

            if is_equipped:
                overlay.append(Transform("interface/topbar/icon_check.webp", align=(1.0, 1.0), offset=(-6, -6), size=(24, 24)))

            if hbox:
                overlay.append(HBox(*hbox, offset=(6, 6)))

            if overlay:
                child = Fixed(child, *overlay, fit_first=True)

            if is_inadequate:
                foreground = "#b2000040"
                hover_foreground = "#CD5C5C40"

            return Button(child=child, focus_mask=None, xysize=(96, 96), background=self.icon, action=action, tooltip=("\n".join(warnings)), foreground=foreground, hover_foreground=hover_foreground, unhovered=unhovered, style=style)

        @functools.cache
        def build_button(self, _=None):

            def _func(self, hash):
                result = self._build_button(self._hash)
                self._button.put(result)

            thread = DollThread(target=_func, args=(self, self._hash))
            thread.start()

        @property
        def button(self):
            if settings.get("multithreading"):
                return self._button.get_with_default(self._loading)
            else:
                return self._build_button(self._hash)

        def clear_button_cache(self):
            if not settings.get("multithreading"):
                return

            self.build_button.cache_clear()

        def apply_color(self, img, n, maxsize):
            """Takes image and int layer number. Used internally."""
            try:
                c = self.color[n]

                # Method 1

                # r,g,b = c.rgb
                # average = max(min((r + g + b) / 3, 0.6666), 0.3333)

                # Method 2

                # lightness = max(min(c.hls[1], 0.6666), 0.3333)
                # average = (lightness, lightness, lightness)

                # Method 3

                # r,g,b = c.rgb
                # luster = (max(r,g,b)+min(r,g,b)) / 2
                # c = c.replace_lightness(luster)
                # average = (luster, luster, luster)

                # Method 4

                average = (0.3333, 0.3333, 0.3333)
   
                return Transform(img, maxsize=maxsize, matrixcolor=SepiaMatrix(c, desat=average)*OpacityMatrix(c.alpha))

            except TypeError:
                print(f"Item doesn't support colors but was supplied with a list; Try removing numbered files in its directory:\n{self.__repr__()}")
                d = At(Frame(Text("TypeErr", color="#ffff00"), tile=True), blink_repeat)
                return Transform(AlphaMask(d, img))
            except IndexError:
                print(f"Mismatched number of textures and colors; Try reducing number of supplied colours in item definition:\n{self.__repr__()}")
                d = At(Frame(Text("IndxErr", color="#ff0000"), tile=True), blink_repeat)
                return Transform(AlphaMask(d, img))

        def set_color(self, n):
            """Takes int layer number for manual color picking or a list to replace the cloth color in its entirety."""
            if isinstance(n, int):
                col = self.color[n]
                dcol = self.color_default[n]

                cp.live_replace(col)
                cp.start_replace(col)
                cp.default_replace(dcol)

                renpy.show_screen("colorpickerscreen", self)

                while True:
                    try:
                        action, value = ui.interact()
                    except:
                        print(f"{ui.interact()}")
                        break

                    if action == "layer":
                        n = value
                        col = self.color[value]
                        dcol = self.color_default[value]

                        cp.live_replace(col)
                        cp.start_replace(col)
                        cp.default_replace(dcol)
                    elif action == "released":
                        self.color[n] = value
                        self.is_stale()
                    elif action == "replace":
                        self.color[n] = value
                        cp.live_replace(value)
                        self.is_stale()
                    elif action == "finish":
                        break

                renpy.hide_screen("colorpickerscreen")
            elif isinstance(n, list):
                self.color = [Color( (tuple(x) if isinstance(x, list) else x) ) for x in n]
                self.is_stale()

        def reset_color(self, n=None):
            """Reset cloth color. Takes optional int layer number to reset only specific layer color."""
            if n:
                self.color[n] = self.color_default[n]
            else:
                self.color = [x for x in self.color_default]
            self.is_stale()

        def clone(self):
            """Creates a clone of this cloth object. Since it requires a parent object it should be used internally only to avoid object depth issue."""
            modpath = self.modpath.lstrip("mods/")
            return DollCloth(self.name, self.categories, self.type, self.id, [x for x in self.color] if self.color else None, self.zorder, self.unlocked, self.level, self.blacklist, modpath, self)

        def is_modded(self):
            """Returns True if item comes from a mod."""
            return bool(self.modpath)

        def get_modname(self):
            """Return the name of the mod directory if exists."""
            return self.modpath.split("/")[1] if self.is_modded() else None

        def mark_as_seen(self):
            self.seen = True

        def is_multislot(self):
            return self.type in self.multislots

        def unlock(self):
            self.unlocked = True

            if self.parent:
                self.parent.unlock()
