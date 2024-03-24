init python:
    class Inventory(object):
        def __init__(self):
            self.items = set()

        def add(self, item):
            self.items.add(item)

        def remove(self, item):
            self.items.remove(item)

        def get_instances(self):
            return self.items

        def get_instances_of_type(self, type):
            return [x for x in self.get_instances() if x.type == type]

    class Item(object):
        def __init__(self, id, type, name, price=0, desc="", unlocked=True, func=None, label=None, limit=100, image="default", givable=False, currency="gold", caption="use", owned=0, infinite=False, give_label=None, usable_on=[]):
            self.id = id
            self.type = type
            self.name = name
            self.price = price
            self.desc = desc
            self.unlocked = unlocked
            self.func = func
            self.label = label
            self.limit = limit
            self.image = "interface/icons/{}.webp".format(self.id) if image == "default" else image
            self.currency = currency
            self.caption = caption

            self.givable = givable
            self.usable = bool(self.func or self.label)
            self.used = False
            self._owned = owned
            self.infinite = infinite
            self.give_label = give_label
            self.usable_on = usable_on

            inventory.add(self)

        def use(self):
            if not self.usable:
                raise Exception("Item '{}' is not usable as it does not have any function or a label.".format(self.name))

            if self.owned == 0:
                raise Exception("Item '{}' owned count is equal to zero.".format(self.name))

            if not self.type == "quest":
                # Quest items require manual triggers, it's more convenient.
                self.used = True

            if self.func:
                self.func()

            if self.label:
                if renpy.context_nesting_level() > 0:
                    renpy.jump_out_of_context(self.label)
                else:
                    renpy.jump(self.label)

        def give(self, who):
            if not self.givable:
                raise Exception("Item '{}' is not marked as givable.".format(self.name))

            if self.owned == 0:
                raise Exception("Item '{}' owned count is equal to zero.".format(self.name))

            if not self.type == "quest":
                # Quest items require manual triggers, it's more convenient.
                self.used = True

            if self.func:
                self.func()

            if self.give_label:
                if renpy.context_nesting_level() > 0:
                    renpy.jump_out_of_context(self.give_label)
                else:
                    renpy.jump(self.give_label)

        def get_image(self):
            if isinstance(self.image, str):
                return self.image
            else:
                return self.image()

        @property
        def owned(self):
            return self._owned

        @owned.setter
        def owned(self, value):
            if not self.unlocked:
                self.unlocked = True

            self._owned = max(min(value, self.limit), 0)

    class Decoration(Item):
        room_scale = 0.5

        def __init__(self, id, type, name, placement, price=0, desc="", unlocked=True, image="default", room_image="default", room_image_hover=None, owned=0, replaces=False, use_action=None, replace_action=None, replace_anchor=None, replace_pos=None):
            super(Decoration, self).__init__(id, type, name, price, desc, unlocked, None, None, 1, image, False, "tokens", "Apply", owned)

            self.room_image = Transform("images/rooms/main_room/decorations/{}.webp".format(self.id), zoom=self.room_scale) if room_image == "default" else Transform(room_image, zoom=self.room_scale)
            self.room_image_hover = Transform(room_image_hover, zoom=self.room_scale) if room_image_hover else self.room_image
            self.usable = True
            self.placement = placement
            self.in_use = False
            self.replaces = replaces
            self.use_action = use_action
            self.replace_action = replace_action
            self.replace_anchor = replace_anchor
            self.replace_pos = replace_pos

            if not isinstance(self.placement, RoomObject):
                raise TypeError("Placement must be a RoomObject instance reference.")

        def use(self):
            if self.owned == 0:
                raise Exception("Decoration '{}' owned count is equal to zero.".format(self.name))

            achievements.unlock("decorator")

            target = self.placement

            if not target.decoration is None:
                target.decoration.in_use = False

            if self.use_action:
                self.use_action()

            # Toggle
            if not target.decoration == self:
                target.set_decoration(self)
                self.in_use = True
            else:
                target.set_decoration(None)
                self.in_use = False

    class Potion(Item):
        def __init__(self, id, type, name, price=0, desc="", unlocked=True, label=None, limit=100, image="default", currency="gold", caption="give", owned=0, recipe=None, usable_on=[], levels={}):
            super(Potion, self).__init__(id, type, name, price, desc, unlocked, None, label, limit, image, True, currency, caption, owned)

            # self.givable = bool(self.give_label)
            self.label = label
            self.recipe = recipe
            self.usable_on = usable_on
            self.levels = levels

            self.make_intro = False
            self.in_progress = {i: False for i in usable_on}

            self.usable = bool( renpy.has_label("{}_use".format(self.label)) )

            if self.recipe is None:
                raise Exception("Potion '{}' recipe is empty!".format(self.name))

        def has_ingredients(self):
            return all(x.owned > 0 for x in self.recipe)

        def set_active(self, who):
            """Marks the event as 'in progress' and will trigger a return event in the morning/evening."""
            if not who in list(self.in_progress.keys()):
                raise Exception("Potion '{}' is not marked as usable on '{}'.".format(self.name, who))

            self.in_progress[who] = True

        def make(self):
            if not self.has_ingredients():
                return

            for i in self.recipe:
                if not i.infinite:
                    i.owned -= 1

            self.owned += 1
            label = "{}_make".format(self.label)

            if renpy.has_label(label) and not self.make_intro:
                self.make_intro = True
                self.jump(label)

        def check_progression(self, who):
            """Check if progression is eligible to play this event"""
            progression = get_character_progression(who)

            return (progression >= self.levels.get(who))

        def give(self, who):
            """Use potion on <active_girl>"""

            give_label = "{}_{}_give".format(who[:3], self.label)
            check_label = "{}_potion_check".format(who[:3])

            if not renpy.has_label(give_label):
                raise Exception("Potion '{}' give label doesn't exist.".format(self.name))

            if not renpy.has_label(check_label):
                raise Exception("Potion '{}' check label doesn't exist for '{}'.".format(self.name, who))

            if self.owned == 0:
                raise Exception("Potion '{}' owned count is equal to zero.".format(self.name))

            if not self.check_progression(who):
                self.jump(check_label)

            self.owned -= 1
            self.jump(give_label)

        def use(self):
            """Use potion on Genie"""

            label = "{}_use".format(self.label)

            if not renpy.has_label(label):
                raise Exception("Potion '{}' has no use label.".format(self.name))

            if self.owned == 0:
                raise Exception("Potion '{}' owned count is equal to zero.".format(self.name))

            self.owned -= 1
            self.jump(label)

        def ret(self, who):
            """Play the return event for <girl>"""

            if not self.in_progress[who]:
                raise Exception("Potion '{}' is not marked as in progress.".format(self.name))

            label = "{}_{}_return".format(who[:3], self.label)

            if not renpy.has_label(label):
                raise Exception("Potion '{}' has no return label.".format(self.name))

            self.in_progress[who] = False
            self.jump(label)

        def jump(self, label):
            if renpy.context_nesting_level() > 0:
                renpy.jump_out_of_context(label)
            else:
                renpy.jump(label)

init offset = -5

default inventory = Inventory()
