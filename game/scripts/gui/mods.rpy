
init offset = -1

screen mods():
    tag menu

    use game_menu("Mods"):

        default selection = next(iter(mods_list.keys()))
        default checkbox_enabled = gui.theme("check_true")
        default checkbox_disabled = gui.theme("check_false")
        default mods_enabled_now = set(persistent.mods_enabled)
        $ awaits_restart = bool(mods_enabled_now != persistent.mods_enabled)

        fixed:

            ## The grid of file slots.
            hbox:
                spacing 5

                vpgrid:
                    cols 1
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    spacing gui.slot_spacing

                    style_prefix gui.theme("slot")

                    for mod in mods_list.values():
                        $ name = mod["Name"]
                        $ desc = mod["Description"]
                        $ author = mod["Author"]
                        $ version = mod["Version"]
                        $ compat = version_float(mod["GameVer"])
                        #$ order = mod["LoadOrder"]
                        $ logo = mod["Logo"]
                        $ enabled = bool(name in persistent.mods_enabled)
                        $ selected = (name == selection)


                        if selected:
                            $ action = ToggleMod(name)
                        else:
                            $ action = SetScreenVariable("selection", name)

                        button:
                            action action
                            selected selected
                            sensitive main_menu

                            has fixed

                            add logo pos (0, 0) size (70, 50)

                            vbox:
                                xpos config.thumbnail_width
                                xsize gui.slot_width - config.thumbnail_width - gui.slot_height
                                yalign 0.5

                                text "[name]":
                                    style "mods_text"
                                    size 16
                                    if not compat >= mods_compatible:
                                        color "#ff8000"

                                text "[version]":
                                    style "mods_text"

                            if enabled:
                                add checkbox_enabled align (0.95, 0.5)
                            else:
                                add checkbox_disabled align (0.95, 0.5)

                    if awaits_restart:
                        text "Awaiting game restart to apply changes..."

                frame:
                    style gui.theme("frame")
                    xfill True
                    ymaximum 400

                    $ name = mods_list[selection]["Name"]
                    $ desc = mods_list[selection]["Description"]
                    $ author = mods_list[selection]["Author"]
                    $ version = mods_list[selection]["Version"]
                    $ compat = version_float(mods_list[selection]["GameVer"])
                    #$ order = mods_list[selection]["LoadOrder"]
                    $ logo = mods_list[selection]["Logo"]

                    vbox:
                        spacing 3
                        xpos 3

                        frame:
                            style gui.theme("frame")
                            xoffset -3
                            ysize 252
                            add logo xalign 0.5 size (320, 240)
                            text "[name]\n[version]" offset (6, 6)

                            if not compat >= mods_compatible:
                                text "{color=#ff8000}[compat]{/color}" align (1.0, 1.0) offset (-6, -3)
                            else:
                                text "{color=#228B22}[compat]{/color}" align (1.0, 1.0) offset (-6, -3)

                        text "Author:\n{size=-4}[author]{/size}" size 14
                        text "Description:\n{size=-4}[desc]{/size}" size 14

style mods_text is slot_button_text:
    selected_color "#000"

style mods_text_desc:
    xalign 0.5
