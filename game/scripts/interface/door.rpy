####################################
############# Menu #################
####################################

default summon_show_busy = True

label summon:
    $ gui.in_context("summon_menu")
    jump main_room_menu

label summon_menu(xx=723, yy=90):

    call update_stats

    $ map_transcript_loc = {"library": "Library", "room_g": "Gryffindor Dormitory", "room_s": "Slytherin Dormitory", "room_r": "Ravenclaw Dormitory", "room_h": "Hufflepuff Dormitory", "great_hall": "Great Hall", "courtyard": "Courtyard", "forest": "Forest", "greenhouse": "Greenhouse", "defense": "D.A.D.A Classroom", "training_grounds": "Training Grounds", "Lake": "Lake", "randomstudent": renpy.random.choice(["Classroom", "Bathroom", "Hagrid's Hut", "Weasley's Store", "Mafkin's Store", "Broom Cupboard", "Attic"]), "randomsnape": renpy.random.choice(["Classroom", "Boathouse", "Bathroom", "Snape's Office", "Hall", "Slytherin Dormitory", "Library", "Attic", "Forest", "Lake", "Dungeons", "Quidditch Cave", "Staircase", "Behind your door", "Room of Doom"]), "randomtonks": renpy.random.choice(["Classroom", "Bathroom", "Hall", "Gryffindor Dormitory", "Slytherin Dormitory", "Hufflepuff Dormitory", "Ravenclaw Dormitory", "Training Grounds", "Tonks' Room", "Quidditch Pitch", "Infirmary", "Sex Dungeon", "Hospital Wing", "Forest", "Lake", "Greenhouse", "Mafkin's Store"])}

    # Door dictionary
    $ summon_dict = {
                    "Snape": {"ico": "snape", "flag": states.sna.unlocked, "busy": states.sna.busy, "loc": "randomsnape"},
                    "Tonks": {"ico": "tonks", "flag": states.ton.unlocked, "busy": states.ton.busy, "loc": "randomtonks"},
                    "Hermione": {"ico": "hermione", "flag": states.her.unlocked, "busy": states.her.busy, "loc": states.her.map_location },
                    "Cho": {"ico": "cho", "flag": states.cho.unlocked, "busy": states.cho.busy, "loc": states.cho.map_location},
                    "Luna": {"ico": "luna", "flag": states.lun.unlocked, "busy": states.lun.busy, "loc": states.lun.map_location},
                    "Astoria": {"ico": "astoria", "flag": states.ast.unlocked, "busy": states.ast.busy, "loc": states.ast.map_location },
                    "Susan": {"ico": "susan", "flag": states.sus.unlocked, "busy": states.sus.busy, "loc": states.sus.map_location}
                    }

    $ summon_categories_sorted = ["Snape", "Tonks", "Hermione", "Cho", "Luna", "Astoria", "Susan"] #"Ginny", "Daphne", "Padma", "Patil", "Myrtle", "Mafkin"
    $ summon_categories_sorted_length = len(summon_categories_sorted)

    $ current_sorting = summon_show_busy

    label .after_init:

    show screen summon(xx, yy)

    $ _choice = ui.interact()

    if _choice[0] == "summon":
        hide screen summon
        if not _choice[2]:
            $ enable_game_menu()
            $ renpy.jump_out_of_context("summon_"+_choice[1].lower())
        else:
            if game.daytime or _choice[1] in ["Tonks", "Snape"]:
                nar "[_choice[1]] is currently busy. Try again later."
            else:
                nar "[_choice[1]] is currently asleep. Try again tomorrow."
    else:
        hide screen summon
        return

    jump .after_init

screen summon(xx, yy):
    tag summon
    zorder 15
    modal True

    add "gui_fade"

    if renpy.mobile:
        use close_button_background
    use close_button(key=["summon", "game_menu"])

    fixed:
        if settings.get("animations"):
            at gui_animation
        use summon_menu(xx, yy)

screen summon_menu(xx, yy):
    tag summon_menu
    modal True
    zorder 15

    window:
        style "empty"
        pos (xx, yy)
        xysize (207, 454)

        use invisible_button()

        add gui.format("interface/achievements/{}/panel_left.webp")

        vbox:
            pos (6, 384)
            spacing 32

            null
            frame:
                style "empty"
                textbutton "Show Busy:":
                    style gui.theme("overlay_button")
                    xsize 195 ysize 32
                    text_align (0.4, 0.5)
                    text_size 12
                    action ToggleVariable("summon_show_busy", True, False)
                add gui.theme("check_{}").format(str(summon_show_busy).lower()) xalign 0.7 ypos 4

        vbox:
            pos (6, 6)
            $ tmp_x = 0
            for char in summon_categories_sorted:
                if summon_dict[char]["flag"]:
                    if summon_show_busy or not summon_dict[char]["busy"]:
                        $ tmp_x += 1
                        frame:
                            style "empty"
                            xsize 195
                            ysize 50
                            vbox:
                                textbutton char:
                                    style "empty"
                                    xsize 195 ysize 46
                                    hover_background gui.format("interface/achievements/{}/highlight_left_b.webp")
                                    text_xalign 0.6 text_yalign 0.5
                                    text_xanchor 0.5
                                    text_size 20
                                    if not summon_dict[char]["busy"]:
                                        action Return(["summon", char, False])
                                    else:
                                        text_color "#8C8C70"
                                        action Return(["summon", char, True])

                                add gui.format("interface/achievements/{}/spacer_left.webp")

                            $ image_zoom = crop_image_zoom("interface/icons/head/"+summon_dict[char]["ico"]+".webp", 42, 42, summon_dict[char]["busy"])

                            button:
                                style gui.theme("overlay_button")
                                background gui.format("interface/achievements/{}/iconbox.webp")
                                foreground "interface/achievements/glass_iconbox.webp"
                                xysize (48, 48)
                                add image_zoom align (0.5, 0.5)

                            text map_transcript_loc[summon_dict[char]["loc"]] size 10 xalign 0.625 yalign 0.9 xanchor 0.5

        if not states.sna.unlocked:
            text "You don't know anyone" size 12 at truecenter
        else:
            if tmp_x <= 0:
                text "All characters are busy" size 12 at truecenter
