init python:
    class Doll(DollMethods):
        # 0 - 50 = Skin/Body Layers
        # 51 - 100 = Face Layers
        # 101 - 300+ = Clothes Layers

        body_layers = {
            "frame": 0,
            "legs": 1,
            "hips": 2,
            "abdomen": 3,
            "chest": 4,
            "arms": 5,
            "head": 6,
        }

        face_layers = {
            "tears": 75,
            "eyebrows": 70,
            "pupils": 65,
            "eyes": 60,
            "mouth": 55,
            "cheeks": 51
        }

        clothing_layers = {
            "makeup": 111, # multislot
            "accessory": 121, # multislot
            "piercing": 131, # multislot
            "tattoo": 141, # multislot
            "pubes": 151,
            "stockings": 161,
            "panties": 171,
            "garterbelt": 181,
            "bottom": 191,
            "bra": 201,
            "top": 211,
            "gloves": 221,
            "robe": 231,
            "neckwear": 241,
            "hair": 251,
            "earrings": 261,
            "glasses": 271,
            "headgear": 281
        }

        __slots__ = ("wardrobe", "wardrobe_list", "blacklist", "outfits", "name", "states", "face", "body", "cum", \
            "pose", "emote", "_hash", "zorder", "layer", "animation", "tag", "pos", "zoom", "xzoom", "align", "modpath")

        def __init__(self, name, modpath=None):
            self.wardrobe = {}
            self.wardrobe_list = []
            self.blacklist = []
            self.outfits = []
            self.name = name
            self.states = {k: [None, v, True] for k, v in (self.clothing_layers | self.body_layers).items()}
            self.face = DollFace(self)
            self.body = DollBody(self)
            self.cum = DollCum(self)
            self.pose = "default"
            self.emote = Null()
            self._hash = None
            self._sprite = DefaultQueue()

            # Image properties
            self.zorder = 15
            self.layer = "screens"
            self.animation = None
            self.tag = f"{name}_main"

            # Transform properties
            self.pos = (0, 0)
            self.zoom = 0.5
            self.xzoom = 1

            self.modpath = "mods/" + posixpath.normpath(modpath) if modpath else ""

            self.build_image()

            # Add doll name to global doll states store
            try:
                renpy.store.states.dolls.add(name)
            except AttributeError:
                renpy.store.states.dolls = {name}

        def generate_hash(self):
            clothes_hash = str([x[0]._hash for x in self.states.values() if istype(x[0], (DollCloth, DollClothDynamic, DollMakeup)) and x[2]])
            salt = str( [self.name, self.pose, str(self.body._hash), str(self.face._hash), str(self.cum._hash), clothes_hash] )
            return hash(salt)

        def show(self, force=False, ignore_skipping=False):
            if renpy.get_screen(("wardrobe", "animatedCG", "studio")) or renpy.showing("cg"):
                return

            if renpy.is_skipping() and not ignore_skipping:
                return

            if not force and not renpy.showing(get_character_tag(self.name), layer=self.layer):
                return

            base_transform = doll_transform(self.pos, self.zoom, self.xzoom)
            animation = self.animation

            at_list = [base_transform]

            if animation:
                at_list.append(animation)

            renpy.show(name=self.tag, at_list=at_list, layer=self.layer, what=self.image, zorder=self.zorder)

        def hide(self):
            renpy.hide(name=self.tag, layer=self.layer)

        @functools.cache
        def _build_image(self, hash):
            from itertools import chain

            # Note: Bodyparts are a part of 'self.states' now.

            sprites = list(chain.from_iterable(
                (self.face.build_image(self.face._hash),
                self.cum.build_image(self.cum._hash),
                *(x[0].build_image(x[0]._hash) for x in self.states.values() if x[0] and x[2]))
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

            return Fixed(*sprites, self.emote, fit_first=True)

        def build_image(self):

            def _func(self, hash):
                result = self._build_image(hash)
                self._sprite.put(result)

            thread = DollThread(target=_func, args=(self, self._hash))
            thread.start()

        def _image(self, st, at):
            return self._sprite.get_with_default(Null()), None

        def is_stale(self):
            curr_hash = self.generate_hash()
            stale = curr_hash != self._hash
            self._hash = curr_hash

            if stale and settings.get("multithreading"):
                self.build_image()
            return stale

        @property
        def image(self):
            if not renpy.is_skipping() and self.is_stale():
                self.show()

            if settings.get("multithreading"):
                return DynamicDisplayable(self._image)
            else:
                return self._build_image(self._hash)

        def equip(self, obj, remove_old=True):
            """Takes DollCloth or DollOutfit object to equip."""

            def _equip_item(item, color=None):
                if item.is_multislot():
                    for i in range(100):
                        multislot = item.type + str(i)
                        if multislot not in self.states or self.states[multislot][0] is None:
                            zorder = self.states[item.type][1]
                            self.states[multislot] = [item, zorder, True]
                            break
                else:
                    zorder = self.states[item.type][1]
                    self.states[item.type] = [item, zorder, True]

                if self.is_blacklisted(item.type):
                    self.unequip(*self.get_blacklister(item.type))

                if item.blacklist:
                    self.unequip(*item.blacklist)

                for tracking in self.get_trackers_list(item.type):
                    tracking.is_stale()

                if color:
                    item.set_color(color)

                item.is_stale()

            def _equip_bodypart(item):
                _equip_item(item)
                self.body.is_stale()

            if istype(obj, (DollCloth, DollClothDynamic, DollMakeup)):
                _equip_item(obj)
            elif istype(obj, DollBodypart):
                _equip_bodypart(obj)
            elif isinstance(obj, DollOutfit):
                if remove_old:
                    self.unequip("clothes", "makeup")
                for item in obj.group:
                    _equip_item(item.parent, color=item.color)
            elif isinstance(obj, (list, tuple)):
                for item in obj:
                    _equip_item(item)

            self.rebuild_blacklist()
            update_chibi(self.name)
            self.cum.is_stale()
            self.is_stale()
            self.show()

        def unequip(self, *args):
            """Takes argument(s) containing string cloth type(s) to unequip."""

            def _unequip_all():
                for k, v in self.states.items():
                    if not k in self.blacklist_unequip:
                        v[0], v[2] = None, True

            def _unequip_type(type):
                for k, v in self.states.items():
                    if not k in self.blacklist_unequip and istype(v[0], type):
                        v[0], v[2] = None, True

            def _unequip_slot(slot):
                if slot in self.blacklist_unequip:
                    return

                if slot in self.multislots:
                    for k, v in self.states.items():
                        if v[0] and v[0].type == slot:
                            v[0], v[2] = None, True
                else:
                    self.states[slot][0], self.states[slot][2] = None, True

            for arg in args:
                if isinstance(arg, str):
                    if arg == "all":
                        _unequip_all()
                    elif arg == "clothes":
                        _unequip_type((DollCloth, DollClothDynamic))
                    elif arg == "bodyparts":
                        _unequip_type(DollBodypart)
                    elif arg == "makeup":
                        _unequip_type(DollMakeup)
                    else:
                        _unequip_slot(arg)

                elif isinstance(arg, DollCloth):
                    if arg.is_multislot():
                        slot = next((k for k, v in self.states.items() if v[0] == arg), None)

                        if not slot:
                            continue

                        _unequip_slot(slot)
                    else:
                        _unequip_slot(arg.type)
                elif isinstance(arg, DollOutfit):
                    for item in arg.group:
                        _unequip_slot(item.type)

            self.rebuild_blacklist()
            update_chibi(self.name)
            self.cum.is_stale()
            self.is_stale()
            self.show()

        def get_equipped(self, slot):
            """Takes argument containing string cloth type. Returns equipped object for cloth type."""
            return self.states[slot][0]

        def get_equipped_wardrobe_item(self, items, subcat):
            """Returns first equipped item from a list or None."""
            for i in items.get(subcat, []):
                if self.is_equipped_item(i):
                    return i
            return None

        def strip(self, *args):
            """Takes argument(s) containing string cloth type(s) to temporarily displace (hide)."""
            def _strip_all():
                for k, v in self.states.items():
                    if not k.startswith(self.blacklist_unequip):
                        v[2] = False

            def _strip_type(type):
                for k, v in self.states.items():
                    if istype(v[0], type) and not k in self.blacklist_unequip and (k in self.multislots or not k.startswith(self.blacklist_strip)):
                        v[2] = False

            def _strip_slot(slot):
                if slot in self.blacklist_unequip:
                    return

                if slot in self.multislots:
                    for k, v in self.states.items():
                        if k.startswith(slot):
                            v[2] = False
                else:
                    self.states[slot][2] = False

            for arg in args:

                if arg == "all":
                    _strip_all()
                elif arg == "clothes":
                    _strip_type((DollCloth, DollClothDynamic))
                elif arg == "makeup":
                    _strip_type(DollMakeup)
                elif arg == "bodyparts":
                    _strip_type(DollBodypart)
                else:
                    _strip_slot(arg)

            update_chibi(self.name)
            self.is_stale()
            self.show()

        def wear(self, *args):
            """Takes argument(s) containing string cloth type(s) to temporarily displace (hide)."""
            def _wear_all():
                for k, v in self.states.items():
                    v[2] = True

            def _wear_type(type):
                for k, v in self.states.items():
                    if istype(v[0], type):
                        v[2] = True

            def _wear_slot(slot):
                if slot in self.multislots:
                    for k, v in self.states.items():
                        if k.startswith(slot):
                            v[2] = True
                else:
                    self.states[slot][2] = True

            for arg in args:

                if arg == "all":
                    _wear_all()
                elif arg ==  "clothes":
                    _wear_type((DollCloth, DollClothDynamic))
                elif arg ==  "makeup":
                    _wear_type(DollMakeup)
                elif arg == "bodyparts":
                    _wear_type(DollBodypart)
                else:
                    _wear_slot(arg)

            update_chibi(self.name)
            self.is_stale()
            self.show()

        def is_equipped(self, *args):
            """Takes argument containing string cloth type. Returns True if slot is occupied, False otherwise."""
            for arg in args:
                if arg in self.multislots:
                    return any(bool(v[0]) for k, v in self.states.items() if k.startswith(arg))
                else:
                    if not self.states[arg][0]:
                        return False
            return True

        def is_any_equipped(self, *args):
            """Takes arguments containing string cloth types. Returns True if ANY of them is equipped, False otherwise."""
            def _is_equipped_type(type):
                for k, v in self.states.items():
                    if not k in self.blacklist_toggles and istype(v[0], type):
                        if self.is_equipped(k):
                            return True
                return False

            state = False

            for arg in args:

                if arg == "clothes":
                    state = _is_equipped_type((DollCloth, DollClothDynamic))
                elif arg == "makeup":
                    state = _is_equipped_type(DollMakeup)
                elif arg == "bodyparts":
                    state = _is_equipped_type(DollBodypart)
                else:
                    state = self.is_equipped(arg)

                if state is True:
                    break

            return state

        def is_equipped_item(self, item):
            """Takes DollCloth object or list of objects. Returns True if item is equipped, False otherwise."""

            if isinstance(item, DollCloth):
                if item.is_multislot():
                    return bool(next((k for k, v in self.states.items() if v[0] == item), False))

                return self.get_equipped(item.type) == item
            elif isinstance(item, DollOutfit):
                compare_object = self.create_outfit(temp=True)
                # current_item = next( (x for x in char_active.outfits if _outfit == x), None)

                return item == compare_object

        def is_worn(self, *args):
            """Takes argument(s) containing string cloth type(s). Returns True if worn, False otherwise."""

            for arg in args:
                if arg in self.multislots:
                    return any( (v[0] and v[2]) for k, v in self.states.items() if k.startswith(arg))
                else:
                    if not self.states[arg][0] or not self.states[arg][2]:
                        return False
            return True

        def is_any_worn(self, *args):
            """Takes arguments containing string cloth types. Returns True if ANY of them is worn, False otherwise."""
            def _is_worn_type(type):
                for k, v in self.states.items():
                    if not k in self.blacklist_toggles and istype(v[0], type):
                        if self.is_worn(k):
                            return True
                return False

            state = False

            for arg in args:

                if arg == "clothes":
                    state = _is_worn_type((DollCloth, DollClothDynamic))
                elif arg == "makeup":
                    state = _is_worn_type(DollMakeup)
                elif arg == "bodyparts":
                    state = _is_worn_type(DollBodypart)
                else:
                    state = self.is_worn(arg)

                if state is True:
                    break

            return state

        def set_face(self, **kwargs):
            self.face.set_face(**kwargs)

            for i in self.states.values():
                if istype(i[0], DollMakeup):
                    i[0].is_stale()

            self.cum.is_stale()

        def get_face(self):
            """Returns a dictionary containing currently set facial expressions. Used in character studio."""
            return self.face._face.copy()

        def set_body_hue(self, arg):
            """Takes integer between 0 - 359, rotates the character body colour by given amount."""
            self.body.set_hue(arg)

            for i in self.states.values():
                if i[0]:
                    i[0].is_stale()

            self.is_stale()
            self.show()

        def set_cum(self, *args, **kwargs):
            """Takes keyword argument(s) containing string name(s) of cum layers to apply or None."""
            self.cum.set_cum(*args, **kwargs)
            self.show()

        def set_pose(self, pose):
            pose = "default" if pose is None else pose
            self.pose = pose
            self.body.is_stale()
            self.face.is_stale()
            self.cum.is_stale()

            for i in self.states.values():
                if i[0]:
                    i[0].is_stale()
            self.is_stale()
            self.show()

        def rebuild_blacklist(self):
            blacklist = []
            for v in self.states.values():
                if v[0]:
                    blacklist.extend(v[0].blacklist)
            self.blacklist = list(set(blacklist))

        def is_blacklisted(self, type):
            """Takes string cloth type. Returns True if cloth type is blacklisted."""
            return True if type in self.blacklist else False

        def get_blacklister(self, type):
            """Takes string cloth type. Returns a list of clothing types that report incompatibility."""
            return [x[0].type for x in self.states.values() if x[0] and type in x[0].blacklist]

        def get_trackers_list(self, type):
            """Takes string cloth type. Returns a list of clothing types that report incompatibility."""
            return [x[0] for x in self.states.values() if istype(x[0], DollClothDynamic) and type == x[0].tracking]

        def create_outfit(self, temp=False):
            """Creates a copy of the current character clothes and stores it. Used only for comparing instances inside the wardrobe."""
            return DollOutfit([x[0] for x in self.states.values() if x[0] and x[0].type not in self.body_layers], True, temp=temp)

        def import_outfit(self, path, fromfile=True):
            """Imports outfit from .png file or clipboard text."""
            # Grab data
            if fromfile:
                try:
                    imported = ImagePayload().extract(path)
                except Exception as e:
                    renpy.notify("Import failed: Corrupted file.")
                    print(e)
                    renpy.block_rollback()
                    return None
            else:
                imported = get_clipboard()

            # Evaluate data
            if imported:
                try:
                    imported = make_revertable(evaluate(imported))
                except Exception as e:
                    renpy.notify("Import failed: Corrupted outfit data.")
                    print(e)
                    renpy.block_rollback()
                    return None

                group = []

                for i, x in enumerate(imported):
                    if i == 0 and not x == self.name:
                        renpy.notify("Import failed: Wrong character.")
                        return None

                    for o in self.wardrobe_list:
                        if x[0] == o.id:
                            if not o.unlocked and not game.cheats:
                                renpy.notify("Import failed: You don't own these items. Buy them first.")
                                return None

                            x[0] = o.clone()
                            x[0].set_color(x[1])
                            group.append(x[0])

                if group:
                    renpy.notify("Import successful!")
                    return DollOutfit(group, True)
            renpy.notify("Import failed: Unknown error.")
            return None

        def get_schedule(self):
            """Returns a list of outfits available for current time of day and weather conditions."""
            schedule = []

            for o in self.outfits:
                if o.unlocked and o.schedule["day" if game.daytime else "night"]:
                    if game.weather == "overcast" and o.schedule["cloudy"]:
                        schedule.append(o)
                    elif game.weather in {"storm", "rain"} and o.schedule["rainy"]:
                        schedule.append(o)
                    elif game.weather in {"snow", "blizzard"} and o.schedule["snowy"]:
                        schedule.append(o)
                    elif game.weather in {"clear", "cloudy"} and not (o.schedule["cloudy"] or o.schedule["rainy"] or o.schedule["snowy"]):
                        schedule.append(o)
            return schedule

        def equip_random_outfit(self):
            """Equips random outfit based on Outfits Schedule."""
            schedule = self.get_schedule()

            if schedule:
                self.equip(renpy.random.choice(schedule))

        def set_emote(self, emote):
            if isinstance(emote, str):
                path = posixpath.join(self.modpath, "characters", self.name, "poses", self.pose, "emote", emote)
                extensions = self.extensions

                for f in renpy.list_files():
                    fp, fn = os.path.split(f)
                    fn, ext = os.path.splitext(fn)

                    if not fp == path or not ext in extensions:
                        continue

                    self.emote = Image(f)
                    break
            else:
                self.emote = emote

            self.is_stale()

        def clear_outfit_button_cache(self):
            if not settings.get("multithreading"):
                return

            DollThread.stop_all()

            for i in self.outfits:
                i._button.last_item = i._loading
                i.clear_button_cache()
