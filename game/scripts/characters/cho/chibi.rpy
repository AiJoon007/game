label cho_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ cho_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ cho_chibi.hide()
        return
    elif action == "leave":
        hide cho_main
        hide screen bld1
        hide screen blktone
        play sound "sounds/door.ogg"
        $ cho_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ cho_chibi.do(None)
        return

    $ cho_chibi.do(action)

    return

label cho_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None, flip=False):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        play sound "sounds/door.ogg"
        call cho_chibi(None, "door", "base", flip)
        with d3
        if xpos or ypos:
            $ cho_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ cho_chibi.show()
        $ cho_chibi.move(("door", "base"), speed, reduce)
        play sound "sounds/door.ogg"
        $ cho_chibi.hide()
        with d3
        pause .5
    elif path:
        $ cho_chibi.show()
        $ cho_chibi.move(path, speed, reduce)
    else:
        $ cho_chibi.show()
        $ cho_chibi.move((xpos, ypos), speed, reduce)

    return

# Screens
screen cho_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag cho_cloth_pile
    zorder cho_chibi.zorder
    add "characters/chibis/cloth_pile_r.webp" pos position zoom 0.5

# Chibi definition
default cho_chibi = Chibi("cho", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves"], update_cho_chibi)

init python:
    def update_cho_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_cho {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Determine clothing state

        if cho.is_worn("top"):
            if cho.get_equipped("top").id == "top_sweater_1":
                chibi["top"] = "cc_sweater.webp"
            else:
                chibi["top"] = "cc_top.webp"

        if cho.is_worn("bottom"):
            if cho.get_equipped("bottom").id in ("pants_long_2", "pants_short_4"):
                if chibi.action == "walk":
                    chibi["bottom"] = "ch_cho trousers"
                else:
                    chibi["bottom"] = "cc_trousers.webp"
            else:
                chibi["bottom"] = "cc_skirt.webp"

        if cho.is_worn("gloves"):
            if cho.get_equipped("gloves").id == "quidditch":
                chibi["gloves"] = "cc_gloves.webp"

        if cho.is_worn("robe"):
            if cho.get_equipped("robe").id == "robe_quidditch_1":
                chibi["robe"] = "cc_quid_robe.webp"
                if not chibi.special:
                    chibi["fix"] = "cc_quid_robe_fix.webp"
            else:
                chibi["robe"] = "cc_robe.webp"

        if cho.is_any_worn("bottom", "stockings"):
            if cho.is_worn("gloves") and cho.get_equipped("gloves").id == "quidditch":
                if chibi.action == "walk":
                    chibi["shoes"] = "ch_cho walk_quid_shoes"
                else:
                    chibi["shoes"] = "cc_quid_shoes.webp"
            else:
                if chibi.action == "walk":
                    chibi["shoes"] = "ch_cho walk_shoes"
                else:
                    chibi["shoes"] = "cc_shoes.webp"
