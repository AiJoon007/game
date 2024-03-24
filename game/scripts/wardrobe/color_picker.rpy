init python:

    renpy.register_shader("color_picker.gradient",
        variables="""
            varying vec2 v_tex_coord;
            attribute vec2 a_tex_coord;
            uniform float u_hue;
        """,
        fragment_functions="""
            vec3 hsv2rgb(vec3 c) {
                vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
                vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
                return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
            }

            float lerp(float a, float b, float f){
                return a + f * (b - a);
            }
        """,
        vertex_300="""
            // Flip gradient
            v_tex_coord = vec2(a_tex_coord.s, 1.0 - a_tex_coord.t);
        """,
        fragment_300="""
            vec2 uv = v_tex_coord;
            vec4 pixel = vec4(hsv2rgb(vec3(u_hue, 1.0, 1.0)), 1.0);
            pixel = vec4(uv.y * lerp(1.0, pixel.x, uv.x), uv.y * lerp(1.0, pixel.y, uv.x), uv.y * lerp(1.0, pixel.z, uv.x), 1.0);
            gl_FragColor = pixel;
            // Gamma correction, but is it really needed here?
            //gl_FragColor = pow(pixel, vec4(1.0/2.2));
        """
    )

    renpy.register_shader("color_picker.hue",
        variables="""
            varying vec2 v_tex_coord;
            attribute vec2 a_tex_coord;
        """,
        fragment_functions="""
            vec3 hsv2rgb(vec3 c) {
                vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
                vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
                return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
            }
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 uv = v_tex_coord;
            vec4 pixel = mix(vec4(hsv2rgb(vec3(uv.y, 1.0, 1.0)), 1.0), gl_FragColor, smoothstep(0.0, 1.0, gl_FragColor.x));
            // Gamma correction
            gl_FragColor = pow(pixel, vec4(1.0/2.2));
        """
    )

    renpy.register_shader("color_picker.alpha",
        variables="""
            uniform vec3 u_color;
            uniform vec2 u_model_size;
            varying float direction;
            attribute vec4 a_position;
        """,
        vertex_300="""
            direction = a_position.x / u_model_size.x;
        """,
        fragment_functions="""
            float pattern(vec2 uv, float size) {
                vec2 pos = floor(uv / size);
                return mod(pos.x + pos.y, 2.0);
            }
        """,
        fragment_300="""
            const float size = 8.0;
            float c = pattern(gl_FragCoord.xy, size);
            vec4 checkerboard = vec4(c, c, c, 1.0);

            vec4 gradient = vec4(u_color, 1.0);
            gradient = mix(gradient, vec4(0.0, 0.0, 0.0, 0.0), direction);

            gl_FragColor = mix(gradient, checkerboard, direction);
        """
    )

    class ColorPickerBase(renpy.Displayable):
        canvas = Solid("#ffffff")

        def __init__(self, controller, **kwargs):
            super(ColorPickerBase, self).__init__(**kwargs)

            self.controller = controller
            self.size = (0, 0)
            self.pos = (0, 0)

        def update(self):
            raise NotImplementedError(self.__class__.__name__)

        def render(self, width, height, st, at):
            raise NotImplementedError(self.__class__.__name__)

        def place_cursor(self, x, y):
            w, h = self.size
            x = max(min(x, w), 0)
            y = max(min(y, h), 0)

            self.pos = (x, y)
            renpy.redraw(self, 0)

        def unfocus(self):
            self.controller.focus = None

        def focus(self):
            self.controller.focus = self

        def focused(self):
            return (self.controller.focus == self)

        def apply(self):
            self.controller.apply()

        def per_interact(self):
            return

        def visit(self):
            return []

        def event(self, ev, x, y, st):
            w, h = self.size

            if not self.focused() and (not (0 < x <= w) or not (0 < y <= h)):
                return
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # Button pressed
                self.focus()
                return

            if not self.focused():
                return

            if ev.type == pygame.MOUSEBUTTONUP:
                # Button released
                self.place_cursor(x, y)
                self.update()
                self.unfocus()
                self.apply()
                renpy.restart_interaction()
                return ["released", self.controller.live_color]

            if ev.type == pygame.MOUSEMOTION and ev.buttons[0]:
                # Dragged
                self.place_cursor(x, y)
                self.update()
                return

    class ColorPickerHue(ColorPickerBase):
        cursor = renpy.displayable("cph_cursor")

        def __init__(self, controller, **kwargs):
            super(ColorPickerHue, self).__init__(controller, **kwargs)

        def update(self):
            _, y = self.pos
            _, h = self.size

            self.controller.hue = max(min(float(y) / h, 1.0), 0.0)
            self.controller.update()

        def place_cursor(self, x, y):
            w, h = self.size
            x = 0
            y = max(min(y, h), 0)

            self.pos = (x, y)
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            self.size = (width, height)

            # Hue Slider
            sr = renpy.Render(width, height)
            slider = renpy.render(self.canvas, width, height, st ,at)

            sr.mesh = True
            sr.add_shader("color_picker.hue")
            sr.blit(slider, (0, 0))

            # Cursor

            cr = renpy.Render(width, height)
            cursor = renpy.render(self.cursor, width, height, st, at)
            cr.blit(cursor, self.pos)

            # Main

            rv = renpy.Render(width, height)
            rv.blit(sr, (0, 0))
            rv.blit(cr, (0, -3))

            return rv

    class ColorPickerSatVal(ColorPickerBase):
        cursor = renpy.displayable("cpsv_cursor")

        def __init__(self, controller, **kwargs):
            super(ColorPickerSatVal, self).__init__(controller, **kwargs)

        def update(self):
            x, y = self.pos
            w, h = self.size

            self.controller.saturation = max(min(float(x) / w, 1.0), 0.0)
            self.controller.value = 1 - max(min(float(y) / h, 1.0), 0.0)
            self.controller.update()

        def render(self, width, height, st, at):
            self.size = (width, height)

            # Gradient map

            gr = renpy.Render(width, height)
            gr.mesh = True
            gr.add_shader("color_picker.gradient")
            gr.add_uniform("u_hue", self.controller.hue)

            canvas = renpy.render(self.canvas, width, height, st ,at)

            gr.blit(canvas, (0, 0))

            # Cursor

            cr = renpy.Render(width, height)
            cursor = renpy.render(self.cursor, width, height, st, at)
            cr.blit(cursor, self.pos)

            # Main

            rv = renpy.Render(width, height)
            rv.blit(gr, (0, 0))
            rv.blit(cr, (-7, -8))

            return rv

    class ColorPickerPreview(ColorPickerBase):
        def __init__(self, controller, **kwargs):
            super(ColorPickerPreview, self).__init__(controller, **kwargs)

        def render(self, width, height, st, at):
            self.size = (width, height)

            # Live colour

            live_color = Solid(self.controller.live_color)
            lcr = renpy.render(live_color, width, height, st, at)

            # # Start colour

            # start_color = Solid(self.controller.start_color)
            # scr = renpy.render(start_color, one_third*2, height, st, at)

            # # # Default colour

            # default_color = Solid(self.controller.default_color)
            # dcr = renpy.render(default_color, width, height, st, at)

            # Main

            rv = renpy.Render(width, height)
            # Laid out from back to front
            #rv.blit(dcr, (0, 0))
            #rv.blit(scr, (0, 0))
            rv.blit(lcr, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return

    class ColorPickerAlpha(ColorPickerBase):
        cursor = renpy.displayable("cpa_cursor")

        def __init__(self, controller, **kwargs):
            super(ColorPickerAlpha, self).__init__(controller, **kwargs)

        def update(self):
            x, _ = self.pos
            w, _ = self.size

            self.controller.alpha = 1.0 - max(min(float(x) / w, 1.0), 0.0)
            self.controller.update()

        def place_cursor(self, x, y):
            w, h = self.size
            x = max(min(x, w), 0)
            y = 0

            self.pos = (x, y)
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            self.size = (width, height)

            # Alpha Slider
            sr = renpy.Render(width, height)
            slider = renpy.render(self.canvas, width, height, st ,at)

            sr.mesh = True
            sr.add_shader("color_picker.alpha")
            sr.add_uniform("u_color", self.controller.live_color.rgb)
            sr.blit(slider, (0, 0))

            # Cursor

            cr = renpy.Render(width, height)
            cursor = renpy.render(self.cursor, width, height, st, at)
            cr.blit(cursor, self.pos)

            # Main

            rv = renpy.Render(width, height)
            rv.blit(sr, (0, 0))
            rv.blit(cr, (0, 0))

            return rv

    class ColorPicker(NoRollback):

        def __init__(self, start_color=Color("#fff"), default_color=Color("#fff")):
            self.live_color = start_color
            self.start_color = start_color
            self.default_color = default_color

            self.hue, self.saturation, self.value = start_color.hsv
            self.alpha = start_color.alpha

            self.cph = ColorPickerHue(self)
            self.cpsv = ColorPickerSatVal(self)
            self.cpp = ColorPickerPreview(self)
            self.cpa = ColorPickerAlpha(self)
            self.focus = None

            h, s, v = start_color.hsv
            a = start_color.alpha
            self.cph.pos = (0, 255 * h)
            self.cpsv.pos = (255 * s, 255 * (1- v))
            self.cpa.pos = (255 * (1 - a), 0)

        def update(self):
            hsv = (self.hue, self.saturation, self.value)
            col = Color(hsv=hsv, alpha=self.alpha)
            self.live_color = col
            self.redraw()

        def redraw(self):
            renpy.redraw(self.cpsv, 0)
            renpy.redraw(self.cph, 0)
            renpy.redraw(self.cpp, 0)
            renpy.redraw(self.cpa, 0)

        def apply(self):
            self.add_history(self.live_color)

        def live_replace(self, color):
            h, s, v = color.hsv
            a = color.alpha
            self.hue, self.saturation, self.value = h, s, v
            self.alpha = a
            self.live_color = color

            self.cph.pos = (0, 255 * h)
            self.cpsv.pos = (255 * s, 255 * (1- v))
            self.cpa.pos = (255 * (1 - a), 0)

            self.redraw()

        def start_replace(self, color):
            self.start_color = color
            self.redraw()

        def default_replace(self, color):
            self.default_color = color
            self.redraw()

        @staticmethod
        def add_history(col):
            colorpicker.history.append(col)

            if len(colorpicker.history) > 10:
                del colorpicker.history[0]

        @staticmethod
        def add_favorite(index, col):
            colorpicker.favorites[index] = col

    cp = ColorPicker()

default colorpicker.history = []
default colorpicker.favorites = [Color((167, 77, 42)), Color((237, 179, 14)), Color((89, 116, 194)), Color((216, 163, 10)), Color((58, 115, 75)), Color((205, 205, 206)), Color((251, 198, 10)), Color((51, 43, 54))] + ([Color((255, 255, 255))] * 22)

screen colorpickerscreen(item=None):
    zorder 30
    modal True

    if item:
        default is_cheating = config.developer or cheat_wardrobe_alpha
        default is_blacklisted = item.type.startswith(tuple(item.blacklist_unequip))
        default is_allowed = item.type.startswith(("makeup", "tattoo"))
    default transparency = item and not is_blacklisted and (is_allowed or is_cheating)

    frame:
        style_prefix "colorpicker"
        background "cp_frame"
        align (0.2, 0.5)
        padding (18, 18)

        has vbox

        if item:
            $ layers = item.color

            label "Layers" xalign 0.0

            hbox:
                spacing 4
                for i, col in enumerate(layers):
                    button:
                        xysize (32, 32)
                        background col
                        foreground "cp_borders"
                        action Return(["layer", i])
                        alternate Return(["replace", col])
                        text str(i+1) style "colorpicker_innertext"

        hbox:
            vbox:
                label "Colour Picker"

                frame:
                    add cp.cpsv xysize (255, 255)

                if transparency:
                    label "Transparency"

                    frame:
                        add cp.cpa xysize (255, 30)

            vbox:
                label "Hue"

                frame:
                    add cp.cph xysize (30, 255)

            vbox:

                label "Previews"

                hbox:
                    spacing 4
                    frame:
                        add cp.cpp xysize (32, 32)
                    frame:
                        button:
                            xysize (32, 32)
                            background cp.start_color
                            action Return(["replace", cp.start_color])
                            text "Old" style "colorpicker_innertext" size 8
                    frame:
                        button:
                            xysize (32, 32)
                            background cp.default_color
                            action Return(["replace", cp.default_color])
                            text "Org" style "colorpicker_innertext" size 8

                label "Swatches"

                grid 5 6:
                    xalign 0.5
                    spacing 4

                    for i, col in enumerate(colorpicker.favorites):
                        frame:
                            button:
                                xysize (12, 12)
                                background col
                                action Return(["replace", col])
                                alternate Function(cp.add_favorite, i, cp.live_color)

                label "History"

                grid 5 2:
                    xalign 0.5
                    spacing 4

                    for col in colorpicker.history:
                        frame:
                            button:
                                xysize (12, 12)
                                background col
                                action Return(["replace", col])

        hbox:
            align (1.0, 1.0)

            if item:
                textbutton "Reset":
                    action [Function(item.reset_color), Function(cp.live_replace, cp.default_color)]

            textbutton "Finish":
                action Return(["finish", cp.live_color])
                keysym ["K_ESCAPE", "K_RETURN"]

    if config.developer:
        vbox:
            pos (15, 15)
            spacing 0
            style_prefix "colorpickerdev"

            text "Hue:[cp.hue]"
            text "Sat:[cp.saturation]"
            text "Val:[cp.value]"
            text "Alpha:[cp.alpha]"

            if item:
                $ colorcode = [i.hexcode for i in item.color]
                textbutton "Colour code: [colorcode]":
                    action [Function(set_clipboard, json.dumps(colorcode)), Notify("Colorcode copied to clipboard.")]
                    #alternate [Function(item.set_color, evaluate(str(get_clipboard())))]
                    keysym ["ctrl_K_c"]
                    #alternate_keysym ["ctrl_K_v"]

style colorpickerdev_text:
    size 12
    color "#fff"
    outlines [(1, "#00000080", 1, 0)]

style colorpickerdev_button_text is colorpickerdev_text:
    color "#cccccc"
    hover_color "#ffffff"

style colorpicker_innertext is colorpickerdev_text:
    color "#ffffff00"
    outlines []
    hover_color "#ffffff"
    hover_outlines [(1, "#00000080", 1, 0)]

style colorpicker_label:
    align (0.5, 0.5)

style colorpicker_label_text:
    color "#402313"

style colorpicker_button_text:
    outlines []

style colorpicker_frame:
    background "cp_borders"
    hover_background image_hover("cp_borders")
    padding (3, 3)

style colorpicker_vbox:
    spacing 6

style colorpicker_hbox:
    spacing 22

image cp_frame = ConditionSwitch(
    "not game.daytime", Frame("gui/dark_frame.png", 8, 8),
    "True", Frame("gui/light_frame.png", 8, 8)
    )

image cp_borders = ConditionSwitch(
    "not game.daytime", Frame("interface/color_picker/gray/cursor_sq.webp", 3, 3),
    "True", Frame("interface/color_picker/gold/cursor_sq.webp", 3, 3)
    )

image cph_cursor = ConditionSwitch(
    "not game.daytime", "interface/color_picker/gray/cursor_h.webp",
    "True", "interface/color_picker/gold/cursor_h.webp"
    )

image cpa_cursor = ConditionSwitch(
    "not game.daytime", "interface/color_picker/gray/cursor_v.webp",
    "True", "interface/color_picker/gold/cursor_v.webp"
    )

image cpsv_cursor = ConditionSwitch(
    "not game.daytime", "interface/color_picker/gray/cursor_sq.webp",
    "True", "interface/color_picker/gold/cursor_sq.webp"
    )
