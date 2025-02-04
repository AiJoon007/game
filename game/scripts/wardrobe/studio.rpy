init offset = 3

default studio.faces = None
default studio.choices = None
default studio.drags = None

init python in studio:
    import os
    import functools
    import posixpath

    Transform = renpy.store.Transform
    Flatten = renpy.store.Flatten
    Drag = renpy.store.Drag
    get_character_object = renpy.store.get_character_object

    @functools.cache
    def get_faces():
        d = _dict()

        for charname in renpy.store.states.dolls:
            charobj = get_character_object(charname)
            extensions = charobj.extensions

            for part in charobj.face._face.keys():

                path = posixpath.join("characters", charname, "poses", charobj.pose, "face", part)

                for f in renpy.list_files():
                    fp, fn = os.path.split(f)
                    fn, ext = os.path.splitext(fn)
                    expression = os.path.split(fp)[1]
                    

                    if part in ("cheeks", "tears"):
                        expressions = d.setdefault(charname, _dict()).setdefault(part, _list((False,)))
                    else:
                        expressions = d.setdefault(charname, _dict()).setdefault(part, _list())

                    if not fp.startswith(path) or not ext in extensions:
                        continue

                    if not expression in expressions:
                        expressions.append(expression)
        return d

    def get_choices():
        d = {}

        for i in renpy.store.states.dolls:
            d[i] = {}
            d[i]["eyebrows"] = faces[i].get("eyebrows", [None]).index("base")
            d[i]["eyes"] = faces[i].get("eyes", [None]).index("base")
            d[i]["mouth"] = faces[i].get("mouth", [None]).index("base")
            d[i]["pupils"] = faces[i].get("pupils", [None]).index("mid")
            d[i]["cheeks"] = faces[i].get("cheeks", [False]).index(False)
            d[i]["tears"] = faces[i].get("tears", [False]).index(False)
            d[i]["zoom"] = 0.5
            d[i]["flip"] = 1
            d[i]["alpha"] = 1.0

        d["background"] = {
            "image": 0,
            "alpha": 1.0,
            "hue": 0,
            "saturation": 1.0,
            "brightness": 0.0,
            "blur": 0.0,
            "list": ["wall_day", "castle", "forest", "quidditch_pitch", "highlight", "versus", "corridor", "custom"]
        }

        d["overlay"] = {
            "image": 0,
            "alpha": 1.0,
            "hue": 0,
            "saturation": 1.0,
            "brightness": 0.0,
            "blur": 0.0,
            "list": [None, "curtains", "card", "g_bottom", "g_left", "g_circular"]
        }
        return d

    def get_drags():
        active_girl = renpy.store.states.active_girl
        d = {}

        for i in renpy.store.states.dolls:
            d[i] = [drag_init(getattr(renpy.store, i)), (i == active_girl)]
        return d

    def get_face(char):
        eyebrows = choices[char]["eyebrows"]
        eyes = choices[char]["eyes"]
        mouth = choices[char]["mouth"]
        pupils = choices[char]["pupils"]
        cheeks = choices[char]["cheeks"]
        tears = choices[char]["tears"]

        d = {
            "eyebrows": faces[char]["eyebrows"][eyebrows],
            "eyes": faces[char]["eyes"][eyes],
            "mouth": faces[char]["mouth"][mouth],
            "pupils": faces[char]["pupils"][pupils],
            "cheeks": faces[char]["cheeks"][cheeks],
            "tears": faces[char]["tears"][tears],
        }
        return d

    def drag_init(obj):
        char_obj = obj
        char_name = char_obj.name

        d = Transform(Flatten(char_obj.image), zoom=choices[char_name]["zoom"], xzoom=choices[char_name]["flip"], alpha=choices[char_name]["alpha"])
        pos = (250, 0)

        drag = Drag(d, activated=drag_activated, drag_offscreen=True, focus_mask=True)
        drag.char_obj = char_obj
        drag.char_name = char_name
        drag.initial_pos = pos
        drag.style.pos = pos

        return drag

    def drag_activated(drag):
        drag = drag[0]

        renpy.store.char_active = drag.char_obj
        renpy.store.states.active_girl = drag.char_name

        drag.top()
        renpy.restart_interaction()
        return

    def drag_update(drag):
        drag.char_obj.set_face(**get_face(drag.char_name))

        zoom = choices[drag.char_name]["zoom"]
        flip = choices[drag.char_name]["flip"]
        alpha = choices[drag.char_name]["alpha"]

        d = Flatten(drag.char_obj.image)
        d = Transform(d, zoom=zoom, xzoom=flip, alpha=alpha)
        drag.set_child(d)
        return

    def drag_reset(drag):
        choices[drag.char_name]["eyebrows"] = faces[drag.char_name]["eyebrows"].index("base")
        choices[drag.char_name]["eyes"] = faces[drag.char_name]["eyes"].index("base")
        choices[drag.char_name]["mouth"] = faces[drag.char_name]["mouth"].index("base")
        choices[drag.char_name]["pupils"] = faces[drag.char_name]["pupils"].index("mid")
        choices[drag.char_name]["cheeks"] = faces[drag.char_name]["cheeks"].index(False)
        choices[drag.char_name]["tears"] = faces[drag.char_name]["tears"].index(False)
        choices[drag.char_name]["zoom"] = 0.5
        choices[drag.char_name]["flip"] = 1
        choices[drag.char_name]["alpha"] = 1.0

        drag.char_obj.set_face(**get_face(drag.char_name))

        x, y = drag.initial_pos
        drag.snap(x, y, 0)

        drag_update(drag)
        return

label studio(char):

    # TODO: Finish adding presets saving.
    # Add character drag offset based on zoom.

    hide screen wardrobe

    python:
        last_char = char_active
        last_girl = states.active_girl
        last_face = last_char.get_face()

        studio.faces = studio.get_faces()
        studio.choices = studio.get_choices()
        char_active.set_face(**studio.get_face(states.active_girl))
        studio.drags = studio.get_drags()

    call screen studio

    # Reset
    $ char_active = last_char
    $ states.active_girl = last_girl
    $ char_active.set_face(**last_face)

    return

screen studio():
    tag studio
    zorder 30
    style_prefix "studio"
    predict False

    default icon_size = (32, 32)
    default take_screenshot = False

    $ bg_hue = HueMatrix(studio.choices["background"]["hue"])
    $ bg_saturation = SaturationMatrix(studio.choices["background"]["saturation"])
    $ bg_brightness = BrightnessMatrix(studio.choices["background"]["brightness"])
    $ bg_blur = studio.choices["background"]["blur"]
    $ bg_matrix = bg_hue*bg_saturation*bg_brightness
    $ bg_image = studio.choices["background"]["list"][studio.choices["background"]["image"]]
    $ bg_image = "images/rooms/_bg_/{}.webp".format(bg_image)
    $ bg = Transform(bg_image, matrixcolor=bg_matrix, blur=bg_blur)

    $ ov_hue = HueMatrix(studio.choices["overlay"]["hue"])
    $ ov_saturation = SaturationMatrix(studio.choices["overlay"]["saturation"])
    $ ov_brightness = BrightnessMatrix(studio.choices["overlay"]["brightness"])
    $ ov_blur = studio.choices["overlay"]["blur"]
    $ ov_alpha = studio.choices["overlay"]["alpha"]
    $ ov_matrix = ov_hue*ov_saturation*ov_brightness
    $ ov_image = studio.choices["overlay"]["list"][studio.choices["overlay"]["image"]]

    if not ov_image is None:
        $ ov_image = "images/rooms/overlays/{}.webp".format(ov_image)
        $ ov = Transform(ov_image, matrixcolor=ov_matrix, blur=ov_blur, alpha=ov_alpha)
    else:
        $ ov = None

    $ active_drag = studio.drags[states.active_girl][0]

    add bg

    draggroup:
        for i in studio.drags.values():
            if i[1]:
                add i[0]

    add ov

    if not _windows_hidden:
        use close_button(action=Confirm("Exit Photo Studio?\n{size=-4}All changes will be lost.{/size}", Return("Close")))

        hbox:
            pos (25, 25)

            style_prefix gui.theme("studio")

            vbox:
                label (states.active_girl)
                $ drag_update = Function(studio.drag_update, active_drag)
                $ drag_reset = Function(studio.drag_reset, active_drag)

                hbox:
                    add "interface/studio/eyebrows.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "eyebrows", len(studio.faces[states.active_girl]["eyebrows"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character eyebrows"
                hbox:
                    add "interface/studio/eyes.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "eyes", len(studio.faces[states.active_girl]["eyes"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character eyes"
                hbox:
                    add "interface/studio/pupils.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "pupils", len(studio.faces[states.active_girl]["pupils"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character pupils"
                hbox:
                    add "interface/studio/mouth.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "mouth", len(studio.faces[states.active_girl]["mouth"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character mouth"
                hbox:
                    add "interface/studio/blush.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "cheeks", len(studio.faces[states.active_girl]["cheeks"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character blush"
                hbox:
                    add "interface/studio/tears.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "tears", len(studio.faces[states.active_girl]["tears"])-1, False, step=1, force_step=True, action=drag_update) tooltip "Character tears"
                hbox:
                    add "interface/studio/scale.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "zoom", 1.0, False, step=0.1, force_step=True, action=drag_update) tooltip "Character Scale"
                hbox:
                    add "interface/studio/opacity.webp" size icon_size
                    bar value DictValue(studio.choices[states.active_girl], "alpha", 1.0, False, step=0.1, force_step=True, action=drag_update) tooltip "Character Opacity"

                textbutton "Flip" action [ToggleDict(studio.choices[states.active_girl], "flip", -1, 1), drag_update] xpos 4
                textbutton "Reset" action drag_reset xpos 4

            vbox:
                label "Background"
                default bg_dict = studio.choices["background"]
                hbox:
                    add "interface/studio/background.webp" size icon_size
                    bar value DictValue(bg_dict, "image", len(bg_dict["list"])-1, False, step=1, force_step=True) tooltip "Background Image"
                hbox:
                    add "interface/studio/hue.webp" size icon_size
                    bar value DictValue(bg_dict, "hue", 360.0, False, step=1.0, force_step=True) tooltip "Background Hue"
                hbox:
                    add "interface/studio/saturation.webp" size icon_size
                    bar value DictValue(bg_dict, "saturation", 1.0, False, step=0.1, force_step=False) tooltip "Background Saturation"
                hbox:
                    add "interface/studio/brightness.webp" size icon_size
                    bar value DictValue(bg_dict, "brightness", 1.0, False, step=0.1, force_step=False) tooltip "Background Brightness"
                hbox:
                    add "interface/studio/blur.webp" size icon_size
                    bar value DictValue(bg_dict, "blur", 50.0, False, step=1.0, force_step=True) tooltip "Background Blur"

            vbox:
                label "Overlay"
                default ov_dict = studio.choices["overlay"]
                $ ov_active = bool(ov_dict["image"] > 0)

                hbox:
                    add "interface/studio/overlay.webp" size icon_size
                    bar value DictValue(ov_dict, "image", len(ov_dict["list"])-1, False, step=1, force_step=True) tooltip "Overlay Image"

                if ov_active:
                    hbox:
                        add "interface/studio/hue.webp" size icon_size
                        bar value DictValue(ov_dict, "hue", 360.0, False, step=1.0, force_step=True) tooltip "Overlay Hue"
                    hbox:
                        add "interface/studio/saturation.webp" size icon_size
                        bar value DictValue(ov_dict, "saturation", 1.0, False, step=0.1, force_step=False) tooltip "Overlay Saturation"
                    hbox:
                        add "interface/studio/brightness.webp" size icon_size
                        bar value DictValue(ov_dict, "brightness", 1.0, False, step=0.1, force_step=False) tooltip "Overlay Brightness"
                    hbox:
                        add "interface/studio/blur.webp" size icon_size
                        bar value DictValue(ov_dict, "blur", 50.0, False, step=1.0, force_step=True) tooltip "Overlay Blur"
                    hbox:
                        add "interface/studio/opacity.webp" size icon_size
                        bar value DictValue(ov_dict, "alpha", 1.0, False, step=0.1, force_step=True) tooltip "Overlay Opacity"

            vbox:
                label "Characters"
                vbox:
                    for k, v in studio.drags.items():
                        $ active = (states.active_girl == k and v[1])
                        $ unlocked = get_character_unlock(k)

                        if not v[1]:
                            $ action = [ SetDict(studio.drags[k], 1, True), Function(studio.drag_activated, [v[0]]), renpy.restart_interaction ]
                        elif not states.active_girl == k:
                            $ action = [ Function(studio.drag_activated, [v[0]]), renpy.restart_interaction]
                        else:
                            $ action = [ SetDict(studio.drags[k], 1, False), renpy.restart_interaction ]

                        if unlocked:
                            textbutton k:
                                action action
                                selected v[1] text_color ("#009900" if active else "#f9d592")
                                text_hover_color "#fff"
                                text_first_indent 20
                                background Transform("interface/icons/head/{}.webp".format(k), size=(16, 16), offset=(22, 3))

        vbox:
            align (1.0, 1.0)
            xoffset -12

            label "Actions"
            hbox:
                imagebutton:
                    idle Transform(image_alpha("interface/studio/screenshot.webp"), size=icon_size)
                    hover Transform("interface/studio/screenshot.webp", size=icon_size)
                    action [Function(_hide_windows), SetScreenVariable("take_screenshot", True)]
                    tooltip "Screenshot (Prnt Scrn)"
                imagebutton:
                    idle Transform(image_alpha("interface/studio/hide.webp"), size=icon_size)
                    hover Transform("interface/studio/hide.webp", size=icon_size)
                    action Function(_hide_windows)
                    tooltip "Hide interface (H)"

    if _windows_hidden:
        use invisible_button(action=Function(_hide_windows))

    if take_screenshot:
        timer 0.2 action [_screenshot, Function(_hide_windows), SetScreenVariable("take_screenshot", False)]

style studio_hbox:
    spacing 25

style studio_label_text:
    color "#f9d592"
    outlines [ (2, "#00000080", 0, 0) ]

style studio_bar:
    xsize 112
    xalign 0.5

style studio_button:
    xsize 106
    xalign 0.5

style studio_button_text:
    size 12

style dark_studio_bar is dark_slider:
    xsize 160
    yalign 0.5

style light_studio_bar is light_slider:
    xsize 160
    yalign 0.5

style light_studio_hbox is studio_hbox
style dark_studio_hbox is studio_hbox

style studio_hbox:
    spacing 5

style light_studio_button is light_radio_button
style dark_studio_button is dark_radio_button

style light_studio_button_text:
    first_indent 6
    size 10
    color "#f9d592"
    hover_color "#fff"
    outlines [ (2, "#00000080", 0, 0) ]

style dark_studio_button_text:
    first_indent 6
    size 10
    color "#9b8d84"
    hover_color "#fff"
    outlines [ (2, "#00000080", 0, 0) ]
