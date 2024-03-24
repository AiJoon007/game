
label update_astoria:

    $ name_susan_astoria = renpy.random.choice(["Suzy","Cow","Cow Tits","Milk Bag","Slut","Whore","Piggy","Pig","Bessie","Moo Moo"])
    $ name_tonks_astoria = renpy.random.choice(["Hag","Old Hag","Punk","Dyke","Lesbo"])
    $ name_astoria_tonks = renpy.random.choice(["Cutie","Kitty","Princess","Cupcake","Honey"])

    # Chibi Update
    $ astoria_chibi.update()
    $ astoria_chibi.position(flip=False)
    $ astoria.xzoom = 1
    hide screen astoria_cloth_pile

    return

label end_astoria_event:
    call ast_chibi("hide")
    hide astoria_main
    with d3
    pause.5

    call update_astoria

    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.ast.busy = True
    $ astoria.wear("all")
    $ astoria.set_cum(None)
    $ astoria.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

define character.astoria_say = Character("name_astoria_genie", show_icon="astoria", dynamic=True)

init python:
    def ast(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
        emote=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            astoria.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        redraw = False
        tag = astoria.tag
        layer = astoria.layer

        if xpos is not None or ypos is not None:
            xpos = astoria.pos[0] if xpos is None else sprite_pos.get("x").get(xpos, xpos)
            ypos = astoria.pos[1] if ypos is None else sprite_pos.get("y").get(ypos, ypos)
            astoria.pos = (xpos, ypos)
            redraw = True

        head_only = astoria.pos[1] == sprite_pos.get("y").get("head")

        if any(face.values()):
            astoria.set_face(**face)
            redraw = True

        if temp_face:
            last_face = astoria.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            astoria.set_face(**d)
            redraw = True

        if emote:
            astoria.set_emote(emote)
            redraw = True

        if animation != False:
            astoria.animation = animation
            redraw = True

        if flip != None:
            astoria.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            character.astoria_say(what, **kwargs)

        if temp_face:
            astoria.set_face(**last_face)

        if head_only:
            astoria.hide()
