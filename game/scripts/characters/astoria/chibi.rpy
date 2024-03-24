label ast_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ astoria_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ astoria_chibi.hide()
        return
    elif action == "leave":
        hide astoria_main
        hide screen bld1
        hide screen blktone
        play sound "sounds/door.ogg"
        $ astoria_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ astoria_chibi.do(None)
        return

    $ astoria_chibi.do(action)

    return

label ast_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None, flip=False):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        play sound "sounds/door.ogg"
        call ast_chibi(None, "door", "base", flip)
        with d3
        if xpos or ypos:
            $ astoria_chibi.move((xpos, ypos), speed, reduce)
    elif action == "leave":
        $ astoria_chibi.show()
        $ astoria_chibi.move(("door", "base"), speed, reduce)
        play sound "sounds/door.ogg"
        $ astoria_chibi.hide()
        with d3
        pause .5
    elif path:
        $ astoria_chibi.show()
        $ astoria_chibi.move(path, speed, reduce)
    else:
        $ astoria_chibi.show()
        $ astoria_chibi.move((xpos, ypos), speed, reduce)

    return

# Screens
screen ast_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag ast_cloth_pile
    zorder astoria_chibi.zorder
    add "characters/chibis/cloth_pile_r.webp" pos position zoom 0.5

# Chibi definition
default astoria_chibi = Chibi("astoria", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves"], update_astoria_chibi)

init python:
    def update_astoria_chibi(chibi):
        # Assume chibi action has a matching image definition
        chibi_image = "ch_ast {}".format(chibi.action or "stand")
        chibi["base"] = chibi_image

        # Determine clothing state

        if astoria.is_worn("top"):
            chibi["top"] = "ag_top.webp"

        if astoria.is_worn("bottom") or (astoria.is_worn("top") and astoria.get_equipped("top").id == ast_top_ann.id):
            chibi["bottom"] = "ag_skirt.webp"

        if astoria.is_worn("robe") and not chibi.special:
            chibi["robe"] = "ag_robe.webp"

        if astoria.is_any_worn("bottom", "stockings"):
            if chibi.action == "wand_imperio":
                chibi["shoes"] = "ch_ast imperio_shoes"
            elif chibi.action == "walk":
                chibi["shoes"] = "ch_ast walk_shoes"
            else:
                chibi["shoes"] = "ag_shoes.webp"
