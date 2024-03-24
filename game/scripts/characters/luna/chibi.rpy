label lun_chibi(action=None, xpos=None, ypos=None, flip=False):
    hide screen luna_chibi_scene # screen tag

    $ luna_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ luna_chibi.hide()
        return
    elif action == "leave":
        hide luna_main
        hide screen bld1
        hide screen blktone
        play sound "sounds/door.ogg"
        $ luna_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ luna_chibi.do(None)
        return

    $ luna_chibi.do(action)

    return

label lun_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None, flip=False):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        play sound "sounds/door.ogg"
        call lun_chibi(None, "door", "base", flip)
        with d3
        if xpos or ypos:
            $ luna_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ luna_chibi.show()
        $ luna_chibi.move(("door", "base"), speed, reduce)
        play sound "sounds/door.ogg"
        $ luna_chibi.hide()
        with d3
        pause .5
    elif path:
        $ luna_chibi.show()
        $ luna_chibi.move(path, speed, reduce)
    else:
        $ luna_chibi.show()
        $ luna_chibi.move((xpos, ypos), speed, reduce)

    return

# Chibi definition
default luna_chibi = Chibi("luna", ["base"], update_luna_chibi, actions=luna_chibi_actions)

define luna_chibi_actions = {
    "lie": (False, "chibi_lie", "float_move"),
    "float_move": (False, "chibi_float_move", 0)
}

init python:
    def update_luna_chibi(chibi):
        if chibi.action == "walk":
            if luna.is_worn("robe"):
                chibi["base"] = "ch_lun walk_robe"
            elif luna.is_worn("top") and luna.is_worn("bottom"):
                chibi["base"] = "ch_lun walk_a"
            elif luna.is_worn("bottom"):
                chibi["base"] = "ch_lun walk_topless"
            else:
                chibi["base"] = "ch_lun walk_n"

        elif not chibi.action or chibi.action in ("stand", "lie", "float_move"):
            if luna.is_worn("robe"):
                chibi["base"] = "ch_lun blink_robe"
            elif luna.is_worn("top") and luna.is_worn("bottom"):
                chibi["base"] = "ch_lun blink_a"
            elif luna.is_worn("bottom"):
                chibi["base"] = "ch_lun blink_topless"
            else:
                chibi["base"] = "ch_lun blink_n"

        else:
            # Assume chibi action has a matching image definition
            chibi_image = "ch_lun {}".format(chibi.action or "stand")
            chibi["base"] = chibi_image


# Sets up a chibi scene with Luna and Genie in it
label lun_chibi_scene(action="reset", xpos="mid", ypos="base"):
    hide screen bld1
    hide screen blkfade

    call lun_chibi("hide")
    call gen_chibi("hide")

    if states.room == "main_room":
        $ desk_OBJ.hidden = True
        $ chair_left_OBJ.hidden = True

    if action == "reset":
        $ menu_y = 0.5
        call lun_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")

    elif action in ("sit_on_lap", "sit_on_lap_grope"):
        show screen luna_chibi_scene("ch_lun_scene " + action, pos=(218, 205))

    elif action in ("inspect_idle", "inspect_idle_naked", "inspect_lean_idle_naked", "inspect_grope_breasts_naked",
         "inspect_grope_vagina_naked", "inspect_lean_grope_breasts_naked", "inspect_lean_grope_vagina_naked"):
        show screen luna_chibi_scene("ch_lun_scene " + action, pos=(218, 205))

    return

screen luna_chibi_scene(img, pos=None):
    tag luna_chibi_scene
    zorder states.desk_chibi_zorder

    add img pos pos
