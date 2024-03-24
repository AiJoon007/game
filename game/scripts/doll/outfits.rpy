init python:
    class DollOutfit(DollMethods):
        default_schedule = {"day": False, "night": False, "cloudy": False, "rainy": False, "snowy": False}
        _loading = Fixed(Text("Loading", align=(0.5, 0.5)), xysize=(96, 168))

        __slots__ = ("group", "name", "desc", "price", "char", "unlocked", "schedule", "temp", "hidden", "addons", "_hash", "_button")

        def __init__(self, group, unlocked=False, name="", desc="", price=0, temp=False, schedule={}, hidden=False, addons=[]):
            self.group = [x.clone() if not x.parent else x for x in group]
            self.group.sort()
            self.name = name
            self.desc = desc
            self.price = price
            self.char = self.group[0].char
            self.unlocked = unlocked
            self.schedule = dict(list(self.default_schedule.items()) + list(schedule.items()))
            self.temp = temp
            self.hidden = hidden
            self.addons = addons
            self._hash = self.generate_hash()
            self._button = DefaultQueue()

            if not self.temp:

                if unlocked:
                    self.unlock()

                if not self.hidden and not self in self.char.outfits:
                    self.char.outfits.append(self)

        def __hash__(self):
            return self._hash

        def __eq__(self, obj):
            if not isinstance(obj, DollOutfit):
                return NotImplemented
            return self._hash == obj._hash

        def generate_hash(self):
            salt = str( [x._hash for x in self.group] ) + str(self.schedule)
            return hash(salt)

        def delete(self):
            if self in self.char.outfits:
                self.char.outfits.remove(self)

        @functools.cache
        def build_image(self, hash):
            from itertools import chain

            matrix = SaturationMatrix(0.0)

            sprites = list(chain.from_iterable(
                (self.char.body.build_image(self.char.body._hash, matrix=matrix),
                *(x.build_image(x._hash, matrix=matrix) for x in self.group))
            ))

            masks = [sprites.pop(sprites.index(x)) for x in sprites if x[0] == "mask"]

            sprites.sort(key=itemgetter(2))
            masks.sort(key=itemgetter(2))

            back_sprites = [x[1] for x in sprites if x[2] < 0]

            #Apply alpha mask
            for m in masks:
                _, mask, mask_zorder = m

                for i, s in enumerate(sprites):
                    _, sprite, sprite_zorder = s

                    if i < 1 or mask_zorder > sprite_zorder:
                        continue

                    masked = AlphaMask(Fixed(*(x[1] for x in sprites[:i]), fit_first=True), mask)
                    sprites = sprites[i:]
                    sprites.insert(0, (None, masked, mask_zorder))
                    break

            sprites = back_sprites + [x[1] for x in sprites]

            return Fixed(*sprites, fit_first=True)

        @property
        def image(self):
            return self.build_image(self._hash)

        @functools.cache
        def build_icon(self, hash):
            sprite = self.build_image(self._hash)

            return Transform(sprite, crop=(220, 0, 680, 1200), size=(96, 168), fit="contain", align=(0.5, 1.0), yoffset=-6)

        @property
        def icon(self):
            return self.build_icon(self._hash)

        def _build_button(self, _hash, subcat):
            global wardrobe_outfit_schedule

            style = "wardrobe_button"
            # is_equipped = self.char.is_equipped_item(self)
            is_modded = self.is_modded()
            is_inadequate = subcat in ("save", "load", "schedule") and not wardrobe_check_equip_outfit(self)
            has_schedule = any(self.schedule.values())

            child = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
            warnings = []
            hbox = []
            vbox = []
            overlay = []

            if is_modded:
                warnings.append("Outfit contains items from these mods:\n{size=-4}{color=#35aae2}"+ "\n".join(self.get_modname()) + "{/color}{/size}")
                hbox.append(Text("M", color="#00b200", style="wardrobe_button_text"))

            action = None
            alternate = None
            unhovered = None
            foreground = None
            hover_foreground = "#ffffff80"
            selected_foreground = None

            if is_inadequate:
                foreground = "#b2000040"
                hover_foreground = "#CD5C5C40"
                selected_foreground = "#CD5C5C40"

            ## MOVE ACTIONS OUT OF THE FUNCTION, THEY FUCK THINGS UP.
            ## One can manipulate the button actions using Button.action

            if subcat == "delete":
                action = Return(["deloutfit", self])
            elif subcat == "load":
                action = Return(["equip", self])
            elif subcat == "save":
                action = Return(["addoutfit", self])
            # elif subcat == "import": # Imports are taken care of outside the class.
            #     action = Return(["import", self])
            elif subcat == "export":
                action = Return(["export", self])
            elif subcat == "schedule":
                if not has_schedule and not is_inadequate:
                    action = Return(["schedule", self])
                    alternate = Return(["schedule", self])
                    foreground = "#00000040"
                    hover_foreground = "#80808040"
                    selected_foreground = "#80808040"
                elif has_schedule:
                    action = Return(["schedule", self])
                    alternate = Return(["schedule", self])
                # elif is_inadequate:
                #     foreground = "#b2000040"
                #     hover_foreground = "#CD5C5C40"
                #     selected_foreground = "#CD5C5C40"

            if has_schedule:
                for i in wardrobe_outfit_schedule:
                    if self.schedule[i]:
                        vbox.append(Transform(f"interface/wardrobe/icons/outfits/{i}.webp", size=(16, 16), offset=(6, 6)))

            # if is_equipped:
            #     hbox.append(Transform("interface/topbar/icon_check.webp", align=(1.0, 1.0), offset=(-6, -6), size=(24, 24)))

            if vbox:
                hbox.append(VBox(*vbox))

            if hbox:
                child = Fixed(child, HBox(*hbox), fit_first=True)

            return Button(child=child, focus_mask=None, xysize=(96, 168), background=self.icon, action=action, alternate=alternate, tooltip=("\n".join(warnings)), foreground=foreground, hover_foreground=hover_foreground, selected_foreground=selected_foreground, unhovered=unhovered, style=style)

        @functools.cache
        def build_button(self, subcat):

            def _func(self, hash, subcat):
                result = self._build_button(self._hash, subcat)
                self._button.put(result)

            thread = DollThread(target=_func, args=(self, self._hash, subcat))
            thread.start()

        @property
        def button(self):
            if settings.get("multithreading"):
                return self._button.get_with_default(self._loading)
            else:
                global current_subcategory
                return self._build_button(self._hash, current_subcategory)

        def clear_button_cache(self):
            self.build_button.cache_clear()

        def exists(self):
            return (self in self.char.outfits)

        def export_data(self, filename, tofile=True):
            """Exports outfit to .png file or clipboard text."""
            exported = [self.group[0].name]

            for i in self.group:
                if i.color:
                    color = [j.hexcode for j in i.color]
                    exported.append([i.id, color])

            # Encode data
            if tofile:
                path = os.path.join(config.gamedir, "outfits")

                if not os.path.exists(path):
                    os.makedirs(path)

                path = os.path.join(path, "_temp.png")

                d = Transform(self.image, crop=(210, 200, 700, 1000), anchor=(0.5, 1.0), align=(0.5, 1.0), xsize=310, ysize=470, fit="contain")
                d = Fixed(
                    "interface/wardrobe/export_background.webp",
                    d,
                    "interface/wardrobe/export_frame.webp",
                    Text(states.active_girl, align=(0.5, 0.995)),
                    Text("Ver. {}".format(config.version), size=10, align=(0.99, 0.99))
                )

                displayable_to_file(d, path, size=(310, 470) )
                ImagePayload().inject("_temp.png", filename, str(exported))
                os.remove(path)
            else:
                set_clipboard(exported)
            renpy.notify("Export successful!")

        def unlock(self):
            """Unlocks outfit and respective clothing objects from which they were cloned."""
            self.unlocked = True
            for i in self.group:
                i.unlock()

            for i in self.addons:
                i.unlock()

        def save(self):
            """Overwrites this outfit with clothes currently equipped by the character."""
            self.group = [x[0].clone() for x in self.char.states.values() if x[0]]
            return

        def is_modded(self):
            """Returns True if one of the group items comes from a mod."""
            for i in self.group:
                if i.is_modded():
                    return True
            return False

        def get_modname(self):
            """Returns a list of mods contained within the outfit group."""
            return list(set([i.get_modname() for i in self.group if i.is_modded()]))

        def get_schedule(self):
            """Returns a dictionary with the current schedule."""
            return self.schedule

        def set_schedule(self, **kwargs):
            for k, v in kwargs.items():
                self.schedule[k] = v

        def has_type(self, *args):
            """Takes argument(s) containing string cloth type(s). Returns True if worn, False otherwise."""
            types = set(x.type for x in self.group)

            for arg in args:
                if arg in self.multislots:
                    if not any(x.startswith(arg) for x in types):
                        return False
                else:
                    if not arg in types:
                        return False
            return True

        def has_any_type(self, *args):
            """Takes arguments containing string cloth types. Returns True if ANY of them is worn, False otherwise."""
            if "clothes" in args:
                for k in self.char.states.keys():
                    if not k.startswith(self.blacklist_toggles):
                        if self.has_type(k):
                            return True
            else:
                for arg in args:
                    if self.has_type(arg):
                        return True
            return False

