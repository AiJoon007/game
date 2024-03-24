label her_chibi(action=None, xpos=None, ypos=None, flip=False, pic=None):
    hide screen favor # screen tag

    $ hermione_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ hermione_chibi.hide()
        return
    elif action == "leave":
        hide hermione_main
        hide screen bld1
        hide screen blktone
        play sound "sounds/door.ogg"
        $ hermione_chibi.hide()
        with d3
        pause .5
        return

    elif action == "reset":
        $ hermione_chibi.do(None)
        return

    $ hermione_chibi.do(action)

    return

label her_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None, flip=False):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        play sound "sounds/door.ogg"
        call her_chibi(None, "door", "base", flip)
        with d3
        if xpos or ypos:
            $ hermione_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ hermione_chibi.show()
        $ hermione_chibi.move(("door", "base"), speed, reduce)
        play sound "sounds/door.ogg"
        $ hermione_chibi.hide()
        with d3
        pause .5
    elif action == "run":
        $ hermione_chibi.show()
        $ hermione_chibi.move((xpos, ypos), speed, reduce, action)
    elif path:
        $ hermione_chibi.show()
        $ hermione_chibi.move(path, speed, reduce)
    else:
        $ hermione_chibi.show()
        $ hermione_chibi.move((xpos, ypos), speed, reduce)

    return

# Chibi definition
default hermione_chibi = Chibi("hermione", ["base"], update_hermione_chibi)

#TODO Hermione's chibis need clothing layers and then update logic must be reworked to set clothing state (using chibi class best practice, see Cho chibi for example)

init python:
    def update_hermione_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_hem {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Certain actions require more complex image selection, which is handled below

        if chibi.action == "walk":

            # Determine clothing state
            if hermione.pose in ("hold_book",):
                chibi["base"] = "ch_hem walk"
            else:
                if not hermione.is_worn("top") and not hermione.is_worn("bottom") and not hermione.is_worn("robe"):
                    chibi["base"] = "ch_hem walk_n"
                elif hermione.is_worn("robe"):
                    if hermione.is_worn("top"):
                        chibi["base"] = "ch_hem walk_robe"
                    else:
                        chibi["base"] = "ch_hem walk_robe_n"
                else:
                     chibi["base"] = "ch_hem walk"

        elif not chibi.action or chibi.action == "stand":
            # Determine clothing state
            if hermione.pose in ("hold_book",):
                chibi["base"] = "ch_hem blink"
            else:
                if not hermione.is_worn("top") and not hermione.is_worn("bottom") and not hermione.is_worn("robe"):
                    chibi["base"] = "ch_hem blink_n"
                elif hermione.is_worn("robe"):
                    if hermione.is_worn("top"):
                        chibi["base"] = "ch_hem blink_robe"
                    else:
                        chibi["base"] = "ch_hem blink_robe_n"
                else:
                     chibi["base"] = "ch_hem blink"

        elif chibi.action == "dance":
            # Determine clothing state
            if hermione.is_worn("top"):
                if hermione.get_equipped("top").id in ("top_school_1", "top_school_6"):
                    chibi["base"] =  "clothed_dance_ani"
                elif hermione.is_worn("bottom"):
                    chibi["base"] = "no_vest_dance_ani"
                else:
                    chibi["base"] = "no_skirt_dance_ani"
            else:
                if hermione.is_worn("bottom"):
                    chibi["base"] = "no_shirt_dance_ani"
                elif hermione.is_worn("panties"):
                    chibi["base"] = "no_shirt_no_skirt_dance_ani"
                else:
                    chibi["base"] = "no_panties_dance_ani"

        elif chibi.action == "dance_pause":
            # Determine clothing state
            if hermione.is_worn("panties"):
                chibi["base"] = "no_shirt_no_skirt_dance_pause"
            else:
                chibi["base"] = "no_panties_dance_pause"

        elif chibi.action == "top_naked":
            chibi["base"] = "dance/03_no_shirt_03.webp" #TODO Should be 'stand' action without top clothes (needs layers first)

        elif chibi.action == "lift_skirt":
            if hermione.is_worn("panties"):
                #TODO Figure out a better way to determine the expression (so it can be reused in a different event)
                if not states.her.status.show_panties:
                    # Reluctant expression
                    chibi["base"] = "~/lift_skirt/panties_00.webp"
                else:
                    # Happy expression
                    chibi["base"] = "~/lift_skirt/panties_01.webp"
            else:
                chibi["base"] = "~/lift_skirt/panties_02.webp"

        elif chibi.action in ("drink_potion", "sniff_potion", "hold_potion"):
            if not hermione.is_any_worn("top", "bottom"):
                chibi["base"] = "ch_hem {}_nude".format(chibi.action)
            else:
                chibi["base"] = "ch_hem {}".format(chibi.action)


# Sets up a chibi scene with Hermione and Genie in it
label her_chibi_scene(action="reset", xpos="mid", ypos="base", trans=None):
    if trans != None:
        call hide_characters

    hide screen bld1
    hide screen blkfade

    call her_chibi("hide")
    call gen_chibi("hide")

    # Defaults
    $ img = None
    $ pos = (0,0)
    $ zord = hermione_chibi.zorder

    # Note: Images are inconsistent, some have the chair already in it, some don't, it's kind of stupid.
    if states.room == "main_room":
        $ desk_OBJ.hidden = True # Hide desk object
        $ chair_left_OBJ.hidden = True # Hide left chair object

    if action == "reset":
        call her_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")
        hide screen her_chibi_scene
        return

    # Stand beside desk back
    elif action == "behind_desk_back":
        $ pos = (-77, 10)

        if not hermione.is_any_worn("bottom", "top"):
            $ img = "behind_desk_back_naked"
        elif not hermione.is_worn("top"):
            $ img = "behind_desk_back_topless"
        elif not hermione.is_worn("bottom"):
            $ img = "behind_desk_back_bottomless"
        else:
            $ img = "behind_desk_back"

    # Stand beside desk front
    elif action == "behind_desk_front":
        $ pos = (-77, 10)

        if not hermione.is_any_worn("bottom", "top"):
            $ img = "behind_desk_front_naked"
        elif not hermione.is_worn("top"):
            $ img = "behind_desk_front_topless"
        elif not hermione.is_worn("bottom"):
            $ img = "behind_desk_front_bottomless"
        else:
            $ img = "behind_desk_front"

    # Stand beside desk front lean on desk lift top
    elif action == "behind_desk_front_show_tits":
        $ pos = (-77, 10)
        $ img = "behind_desk_front_show_tits"

    # Stand beside desk lift top
    elif action == "behind_desk_show_tits":
        $ pos = (-77, 10)
        $ img = "behind_desk_show_tits"

    # Grope ass
    elif action == "grope_ass_back":
        $ pos = (-77, 10)

        if not hermione.is_any_worn("bottom", "top"):
            $ img = "grope_ass_back_naked"
        elif not hermione.is_worn("top"):
            $ img = "grope_ass_back_topless"
        elif not hermione.is_worn("bottom"):
            $ img = "grope_ass_back_bottomless"
        else:
            $ img = "grope_ass_back"

    elif action == "grope_ass_back_fast":
        $ pos = (-77, 10)
        $ img = "grope_ass_back_topless_fast"

    elif action == "grope_ass_front":
        $ pos = (-77, 10)

        if not hermione.is_any_worn("bottom", "top"):
            $ img = "grope_ass_front_naked"
        elif not hermione.is_worn("top"):
            $ img = "grope_ass_front_topless"
        elif not hermione.is_worn("bottom"):
            $ img = "grope_ass_front_bottomless"
        else:
            $ img = "grope_ass_front"

    elif action == "grope_ass_front_fast":
        $ pos = (-77, 10)
        $ img = "grope_ass_front_topless_fast"

    # Grope tits
    elif action == "grope_tits":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits"
        elif hermione.is_worn("bottom"):
            $ img = "grope_tits_topless"
        elif hermione.is_worn("top"):
            $ img = "grope_tits_bottomless"
        else:
            $ img = "grope_tits_naked"

    elif action == "lift_top":

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_lift_top"
        else:
            $ img = "grope_tits_bottomless_lift_top"

    elif action == "grope_tits_jerk_off":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_jerk_off_clothed"
        elif hermione.is_worn("bottom"):
            $ img = "grope_tits_jerk_off_topless"
        elif hermione.is_worn("top"):
            $ img = "grope_tits_jerk_off_bottomless"
        else:
            $ img = "grope_tits_jerk_off_naked"

    elif action == "grope_tits_jerk_off_lift_top":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_jerk_off_lift_top"
        elif hermione.is_worn("top"):
            $ img = "grope_tits_jerk_off_bottomless_lift_top"

    elif action == "grope_tits_cum":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_cum_clothed"
        elif hermione.is_worn("bottom"):
            $ img = "grope_tits_cum_topless"
        elif hermione.is_worn("top"):
            $ img = "grope_tits_cum_bottomless"
        else:
            $ img = "grope_tits_cum_naked"

    elif action == "grope_tits_cum_done":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_cum_clothed_done"
        elif hermione.is_worn("bottom"):
            $ img = "grope_tits_cum_topless_done"
        elif hermione.is_worn("top"):
            $ img = "grope_tits_cum_bottomless_done"
        else:
            $ img = "grope_tits_cum_naked_done"

    elif action == "grope_tits_cum_lift_top":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_cum_lift_top"
        else:
            $ img = "grope_tits_cum_bottomless_lift_top"

    elif action == "grope_tits_cum_lift_top_done":
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)

        if hermione.is_worn("top", "bottom"):
            $ img = "grope_tits_cum_done"
        else:
            $ img = "grope_tits_cum_bottomless_lift_top_done"

    # Grope on podium (Quidditch pitch)
    elif action in ("grope_on_podium", "grope_on_podium_idle", "grope_on_podium_horny", "grope_on_podium_close", "grope_on_podium_cum"):
        $ pos = (255, 211)
        $ img = action
        $ zord = 9 # Override zorder; In front of screen quidditch_stands_mid w/ podium.

    # Lie on desk (admire ass)
    elif action == "lie_on_desk":
        $ pos = (-77, 10)

        if hermione.is_worn("bottom"):
            $ img = "lie_on_desk"
        else:
            $ img = "lie_on_desk_naked"

    elif action == "lie_on_desk_fingering":
        $ pos = (-77, 10)
        $ img = "finger_naked"

    elif action == "lie_on_desk_fingering_slow":
        $ pos = (-77, 10)
        $ img = "finger_naked_slow"

    elif action == "lie_on_desk_fingering_pause":
        $ pos = (-77, 10)
        $ img = "finger_naked_pause"

    elif action == "lie_on_desk_fingering_pause_ahegao":
        $ pos = (-77, 10)
        $ img = "finger_naked_pause_ahegao"

    elif action == "lie_on_desk_fingering_cumming":
        $ pos = (-77, 10)
        $ img = "finger_naked_cumming"

    elif action == "lie_on_desk_jerk_off":
        $ pos = (-77, 10)

        if hermione.is_worn("bottom"):
            $ img = "lie_on_desk_jerk_off"
        else:
            $ img = "lie_on_desk_naked_jerk_off"

    elif action == "lie_on_desk_cum":
        $ pos = (-77, 10)

        if hermione.is_worn("bottom"):
            $ img = "lie_on_desk_cum"
        else:
            $ img = "lie_on_desk_naked_cum"

    # Handjob
    elif action in ("hj", "hj_pause", "hj_cum_in", "hj_cum_in_done", "hj_cum_on", "hj_cum_on_done", "hj_kiss", "hj_kiss_cum"):
        $ desk_OBJ.hidden = False # Unhide desk object
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (230, 0)
        $ img = action

    # Titjob
    elif action in ("tj", "tj_pause", "tj_idle", "tj_cum_on", "tj_cum_on_done", "tj_mouth", "tj_cum_in", "tj_cum_in_done"):
        $ desk_OBJ.hidden = False # Unhide desk object
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (450, 200)
        $ img = action

    # Blowjob
    elif action in ("bj", "bj_pause", "bj_cum_in", "bj_cum_out", "bj_cum_out_done"):
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-7, 14)
        $ img = action

    # Sex
    elif action in (
        "sex_hotdog", "sex", "sex_pause", "sex_slow", "sex_fast",
        "sex_cum_out", "sex_cum_out_done", "sex_cum_in", "sex_cum_in_done",
        "sex_naked", "sex_naked_pause", "sex_naked_slow", "sex_naked_fast",
        "sex_naked_cum_out", "sex_naked_cum_out_done", "sex_naked_cum_in", "sex_naked_cum_in_done"
    ):
        $ chair_left_OBJ.hidden = False # Unhide left chair object
        $ pos = (-77, 10)
        $ img = action

    show screen her_chibi_scene(img, pos, zord)

    if trans:
        with trans

    return

screen her_chibi_scene(img, pos, zord):
    tag hermione_chibi
    zorder zord

    add img pos pos
