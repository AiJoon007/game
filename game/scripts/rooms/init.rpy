
init -1 python:

    class Room(object):
        def __init__(self, id):
            self.id = id
            self.objects = set()

        def add(self, obj):
            self.objects.add(obj)

        def remove(self, obj):
            self.objects.remove(obj)

    class RoomObject(object):

        def __init__(self, room, id, pos, idle, hover=None, foreground=None, background=None, anchor=(0.5, 0.5), focus_mask=True, action=NullAction(), hovered=None, unhovered=None, tooltip=None, decoration=None, zorder=0, hidden=False):
            self.room = room
            self.id = id
            self.pos = pos
            self.idle = idle
            self.hover = hover or self.idle
            self.foreground = foreground
            self.background = background
            self.anchor = anchor
            self.focus_mask = focus_mask
            self.action = action
            self.hovered = hovered
            self.unhovered = unhovered
            self.tooltip = tooltip
            self.decoration = decoration
            self.zorder = zorder
            self.hidden = hidden

            # Add to the main room if room was specified
            if self.room:
                self.room.add(self)

            # Backwards compatibility, to be resolved if possible.
            self.xpos, self.ypos = self.pos

        def generate_hash(self):
            salt = str( [self.id, self.pos, self.idle, self.hover, self.foreground, self.background, self.anchor, self.focus_mask, 
                self.action, self.hovered, self.unhovered, self.tooltip, self.decoration, self.zorder, self.hidden]
                )

            return hash(salt)

        def set_image(self, idle, hover=None):
            self.idle = idle
            self.hover = hover or idle

        def get_idle(self):
            return self._get_idle(self.generate_hash())

        @functools.cache
        def _get_idle(self, hash):
            if self.hidden:
                return Null()

            if self.decoration:
                if self.decoration.replaces:
                    return Fixed(self.decoration.room_image, fit_first=True)
                else:
                    return Fixed(self.idle, self.decoration.room_image, fit_first=True)
            return Fixed(self.idle, fit_first=True)

        def get_hover(self):
            return self._get_hover(self.generate_hash())

        @functools.cache
        def _get_hover(self, hash):
            if self.hidden:
                return Null()

            if self.decoration:
                if self.decoration.replaces:
                    return At(Fixed(self.decoration.room_image_hover, fit_first=True), pulse_hover)
                else:
                    return At(Fixed(self.hover, self.decoration.room_image_hover, fit_first=True), pulse_hover)
            return At(Fixed(self.hover, fit_first=True), pulse_hover)

            ### Shader needs more work.
            # if self.decoration:
            #     return Transform(Fixed(self.hover, self.decoration.room_image, fit_first=True), shader="outline_shader")
            # return Transform(self.hover, shader="outline_shader")

        def set_decoration(self, decoration):
            if not isinstance(decoration, (Decoration, NoneType)):
                raise TypeError("Decoration must be a Decoration instance reference or a NoneType")

            self.decoration = decoration

        def get_action(self):
            deco = self.decoration

            if deco and deco.replace_action:
                return deco.replace_action

            return self.action

        def get_anchor(self):
            deco = self.decoration

            if deco and deco.replace_anchor:
                return deco.replace_anchor
            return self.anchor

        def get_pos(self):
            deco = self.decoration

            if deco and deco.replace_pos:
                return deco.replace_pos
            return self.pos

default room_menu_active = False

screen room_menu():
    tag room_menu
    on "show" action SetVariable("room_menu_active", True)
    on "hide" action SetVariable("room_menu_active", False)
