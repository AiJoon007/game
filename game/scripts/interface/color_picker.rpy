default color_history = []
default color_favorites = [[167, 77, 42, 255], [237, 179, 14, 255], [89, 116, 194, 255], [216, 163, 10, 255], [58, 115, 75, 255], [205, 205, 206, 255], [251, 198, 10, 255], [51, 43, 54, 255]]

screen color_picker(color, alpha, title, pos_xy, color_default):
    tag color_picker
    zorder 25
    modal True

    # Screen variables
    default rgba = color
    default rgba_old = color
    default hue = 0
    default sat = 0
    default val = 0
    default _alpha = 0 # Avoid name conflict with 'alpha' screen variable in other active screens
    default edit_mode = False
    default preview_old = Solid(rgba)
    $ preview_new = Solid(rgba)
    $ gradient_map = SVGradientButton(
        color_picker_clicked,
        Fixed(
            Color( tuple( x * 255 for x in colorsys.hsv_to_rgb(1 - hue, 1, 1) ) ),
            Frame("interface/color_picker/saturation_value_gradient.webp")
        ),
        xysize=(255, 255),
        #area=(25, 25, 255, 255),
        focus_mask=None,
        keyboard_focus=False,
        key_events=False
    )

    default icon_frame = Frame(gui.format("interface/frames/{}/iconframe.webp"), 6, 6)
    default icon_transparent = Frame("interface/color_picker/checker.webp", tile=True)
    default slider_thumb = Image(gui.format("interface/color_picker/{}/cursor_h.webp"), xalign=0.5)

    # Set HSVA variables based on RGBA when screen shows
    on "show" action Function(color_picker_update_hsva)

    frame:
        style_prefix gui.theme()
        if pos_xy and False:
            pos pos_xy
        else:
            align (0.5, 0.5)
        padding (18, 18)

        vbox:
            spacing 12

            # Colour swatches
            hbox:
                ysize 80
                spacing 12
                vbox:
                    spacing 12
                    #pos (0,0)

                    hbox:
                        spacing 12
                        text "Colour swatches"
                        textbutton "Edit":
                            yoffset -4
                            text_size 12
                            action [SelectedIf(edit_mode),ToggleScreenVariable("edit_mode", True, False)]
                    hbox:
                        spacing 2
                        for i in range(8):
                            $ is_valid = (i < len(color_favorites))
                            $ background = Fixed(icon_transparent, Color(tuple(color_favorites[i])), icon_frame) if is_valid else icon_frame

                            if edit_mode:
                                if is_valid:
                                    $ action = Return(["rem_swatch", i])
                                    $ icon = Text("X", color="#b20000", align=(0.5, 0.5), outlines=[(1, "#000", 0, 0)])
                                    $ tooltip = "Remove"
                                else:
                                    $ action = Return(["add_swatch", list(rgba)])
                                    $ icon = Image("interface/icons/small/star_yellow.webp", align=(0.5, 0.5))
                                    $ tooltip = "Add"
                            elif is_valid:
                                $ action = Return(["use_swatch", color_favorites[i]])
                                $ icon = None
                                $ tooltip = "Select"

                            button:
                                xysize (32, 32)
                                background background
                                hover_foreground "#ffffff80"
                                tooltip tooltip
                                action action
                                add icon

                vbox:
                    text "History"
                    frame:
                        xsize 140
                        background icon_frame
                        viewport id "history":
                            scrollbars "vertical"
                            mousewheel True
                            draggable False
                            pagekeys True
                            side_yfill True
                            vbox:
                                for c in color_history[::-1]:
                                    textbutton rgba_to_hex(c):
                                        style "empty"
                                        xfill True
                                        ysize 16
                                        text_size 11
                                        text_color "#000"
                                        text_hover_color "#fff"
                                        text_outlines [(1, "#fff", 0, 0)]
                                        text_hover_outlines [(1, "#000", 0, 0)]
                                        text_align (0.5, 0.5)
                                        background Color(tuple(c))
                                        action Return(["history", c])

            # Colour picker
            text title xalign 0.5 text_align 0.5

            hbox:
                spacing 12

                fixed:
                    xysize (255, 255)
                    fit_first True
                    add gradient_map

                    add icon_frame

                    draggroup:
                        # Allow cursor to extend 8 pixels outside map
                        area (-8, -8, 255 + 16,  255 + 16)
                        drag:
                            pos (int(sat * 253), int((1 - val) * 253))
                            anchor (0, 0)
                            child gui.format("interface/color_picker/{}/cursor_sq.webp")
                            focus_mask None
                            dragged color_picker_dragged

                # Hue slider
                # frame:
                #     margin (-6, -6)
                fixed:
                    fit_first True
                    add hue_gradient_image
                    vbar:
                        xysize (30, 255)
                        value ScreenVariableValue("hue", range=1.0, action=Function(color_picker_update_rgba))
                        base_bar icon_frame
                        thumb slider_thumb
                        thumb_offset 0
                        top_gutter 0
                        bottom_gutter 0

                vbox:
                    xysize (110, 255)
                    fixed:
                        yfill False
                        fit_first True

                        # TODO: Merge RGB(A) input into a single action, add HEX(A) and add copy/paste functionality
                        vbox:
                            textbutton "Red: " + str(int(rgba[0])):
                                xfill True
                                size_group "rgba"
                                text_size 12
                                clicked Return(["input", 0])
                            textbutton "Green: " + str(int(rgba[1])):
                                size_group "rgba"
                                text_size 12
                                clicked Return(["input", 1])
                            textbutton "Blue: " + str(int(rgba[2])):
                                size_group "rgba"
                                text_size 12
                                clicked Return(["input", 2])
                            if alpha:
                                textbutton "Alpha: " + str(int(rgba[3])):
                                    size_group "rgba"
                                    text_size 12
                                    clicked Return(["input", 3])
                            if color_default:
                                textbutton "Reset":
                                    size_group "rgba"
                                    text_size 12
                                    text_xalign 0.5
                                    clicked Return("reset")
                        add icon_frame

                    # Selected color
                    fixed:
                        fit_first True
                        xysize (110, 110)
                        yalign 1.0
                        add Frame("interface/color_picker/checker.webp", tile=True, )
                        frame:
                            area (0, 0, 55, 110)
                            background preview_new
                            text "New" xalign 0.5 color "#fff" outlines [(1, "#00000080", 1, 0)]
                        frame:
                            area (55, 0, 55, 110)
                            background preview_old
                            text "Old" xalign 0.5 color "#fff" outlines [(1, "#00000080", 1, 0)]
                        add icon_frame

            if alpha:
                # Opacity slider
                fixed:
                    xysize (255, 30)
                    fit_first True
                    add Fixed(Frame("interface/color_picker/checker.webp", tile=True),
                                Transform(alpha_gradient_image, matrixcolor=ColorizeMatrix(rgba, rgba)))
                    bar:
                        xysize (255, 30)
                        value ScreenVariableValue("_alpha", range=1.0, action=Function(color_picker_update_rgba))
                        base_bar icon_frame
                        thumb Image(gui.format("interface/color_picker/{}/cursor_v.webp"), xalign=0.5)
                        thumb_offset 0
                        top_gutter 0
                        bottom_gutter 0

            # Window buttons
            hbox:
                align (1.0, 1.0)
                spacing 6
                textbutton "Cancel" action Return("cancel")
                textbutton "Apply" action Return(["apply", rgba])

default picking_color = None

define alpha_gradient_image = AlphaSlider()
define hue_gradient_image = HueSlider()

init -1 python:

    def color_picker(color=[0,0,0,0], alpha=True, title="Pick a colour", pos_xy=(240, 130), color_default=None):
        # TODO: Remove external dependencies and utilise built-in Color class instead.

        global picking_color
        picking_color = color # Color object (list) to be updated live
        start_color = list(color) # Keep a copy

        renpy.show_screen("color_picker", tuple(color), alpha, title, pos_xy, color_default)

        while True:
            _return = ui.interact()

            if _return[0] == "input":
                color_picker_input(_return[1])

            elif _return == "reset":
                scope = renpy.get_screen("color_picker").scope
                scope["rgba"] = tuple(color_default)
                color_picker_update_hsva()
                update_picking_color(color_default)

            elif _return[0] == "use_swatch":
                scope = renpy.get_screen("color_picker").scope
                scope["rgba"] = tuple(_return[1])
                color_picker_update_hsva()
                update_picking_color(_return[1])

            elif _return[0] == "add_swatch":
                color_picker_add(_return[1])

            elif _return[0] == "rem_swatch":
                color_picker_rem(_return[1])

            elif _return[0] == "history":
                scope = renpy.get_screen("color_picker").scope
                scope["rgba"] = tuple(_return[1])
                color_picker_update_hsva()
                update_picking_color(_return[1])

            elif _return == "cancel":
                hide_color_picker()
                update_picking_color(start_color) # Reset live color object
                picking_color = None
                return start_color

            elif _return[0] == "apply":
                hide_color_picker()
                picking_color = None
                return color # Return live color object instead of _return tuple

    def hide_color_picker():
        renpy.hide_screen("color_picker")

    def update_picking_color(rgba):
        global picking_color
        for (i, x) in enumerate(rgba):
            picking_color[i] = x

    def color_picker_input(comp):
        scope = renpy.get_screen("color_picker").scope
        x = renpy.input(["Red", "Green", "Blue", "Alpha"][comp], str(scope["rgba"][comp]), "0123456789", length=3)
        x = max(0, min(255, int(x)))
        tuplist = list(scope["rgba"])
        tuplist[comp] = x
        scope["rgba"] = tuple(tuplist)
        color_picker_update_hsva()
        update_picking_color(scope["rgba"])

    def color_picker_update_hsva():
        scope = renpy.get_screen("color_picker").scope
        (r, g, b, a) = scope["rgba"]
        (h, s, v) = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        scope["hue"] = 1 - h
        scope["sat"] = s
        scope["val"] = v
        scope["_alpha"] = a / 255.0

    def color_picker_update_rgba():
        scope = renpy.get_screen("color_picker").scope
        (r, g, b) = colorsys.hsv_to_rgb(1 - scope["hue"], scope["sat"], scope["val"])
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        a = int(scope["_alpha"] * 255)
        scope["rgba"] = (r, g, b, a)
        update_picking_color(scope["rgba"])
        renpy.restart_interaction()

    #def color_picker_clicked(offset, size):
    def color_picker_clicked(x, y, size):
        # Mouse screen position to local position
        # (x, y) = renpy.get_mouse_pos()
        # x = max(0, min(x - offset[0], size[0]))
        # y = max(0, min(y - offset[1], size[1]))
        # Update screen variables
        scope = renpy.get_screen("color_picker").scope
        scope["sat"] = float(x) / size[0]
        scope["val"] = 1 - float(y) / size[1]
        color_picker_update_rgba()
        color_picker_history()

    def color_picker_dragged(drags, drop=None):
        # Compensate for draggable area
        width = drags[0].parent_width - drags[0].w
        height = drags[0].parent_height - drags[0].h
        x = drags[0].x
        y = drags[0].y
        # Update screen variables
        scope = renpy.get_screen("color_picker").scope
        scope["sat"]  = float(x) / width
        scope["val"] = 1 - float(y) / height
        color_picker_update_rgba()
        color_picker_history()

    def color_picker_history():
        global color_history
        scope = renpy.get_screen("color_picker").scope
        color_history.append(scope["rgba"])
        if len(color_history) > 30:
            del color_history[0]

    def color_picker_add(item):
        global color_favorites
        color_favorites.append(item)

    def color_picker_rem(item):
        global color_favorites
        del color_favorites[item]

    def rgba_to_hex(c):
        return '#%02x%02x%02x%02x' % (c[0], c[1], c[2], c[3])

    class HueSlider(renpy.Displayable, NoRollback):
        def __init__(self, size=(30,255), **properties):
            super(HueSlider, self).__init__(**properties)
            self.size = size

        def render(self, width, height, st, at):
            w, h = self.size
            rv = renpy.Render(w, h)
            canvas = rv.canvas()
            surf = canvas.get_surface()

            for x in range(w):
                for y in range(h):
                    hue = float(y) / h
                    r, g, b = Color(hsv=(hue, 1.0, 1.0)).rgb
                    color = (r * 255, g * 255, b * 255)
                    surf.set_at((x, y), color)

            #surf = renpy.display.scale.smoothscale(surf, (w, h))

            rv.blit(surf, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return

    class AlphaSlider(renpy.Displayable, NoRollback):
        def __init__(self, size=(255,30), **properties):
            super(AlphaSlider, self).__init__(**properties)
            self.size = size

        def render(self, width, height, st, at):
            w, h = self.size
            rv = renpy.Render(w, h)
            canvas = rv.canvas()
            surf = canvas.get_surface()

            for x in range(w):
                for y in range(h):
                    hue = float(y) / h
                    color = (255.0, 255.0, 255.0, x)
                    surf.set_at((x, y), color)

            #surf = pygame.transform.scale(surf, (w, h))

            rv.blit(surf, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return

    class GradientImageBase(im.ImageBase):
        def __init__(self, **properties):
            super(GradientImageBase, self).__init__(**properties)
            self.size = properties.get('size')
            self.cached_surf = None

    class SVGradientButton(ImageButton):

        def __init__(self, on_click, idle_image, *args, **kwargs):
            kwargs['sensitive'] = True
            kwargs['action'] = NullAction()
            super(SVGradientButton, self).__init__(idle_image, *args, **kwargs)
            self.width = 0
            self.height = 0
            self.on_click = on_click

        def render(self, width, height, st, at):
            rv = super(SVGradientButton, self).render(width, height, st, at)
            self.width, self.height = rv.get_size()
            return rv

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP and 0 <= x <= self.width and 0 <= y <= self.height:
                self.on_click(x, y, (self.width, self.height))

            return super(SVGradientButton, self).event(ev, x, y, st)

# image testsurface = HueSlider()

# screen testzone():
#     tag testzone
#     zorder 1000
#     add "testsurface" #align (0.5, 0.5)
