
label end_luna_event:

    call lun_chibi("hide")
    hide luna_main
    with d3
    pause.5

    call update_luna

    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.lun.busy = True
    $ luna.wear("all")
    $ luna.set_cum(None)
    $ luna.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

label update_luna:
    # Chibi Update
    $ luna_chibi.update()
    $ luna_chibi.position(flip=False)
    $ luna.xzoom = 1
    hide screen luna_cloth_pile

    return

define character.luna_say = Character("name_luna_genie", show_icon="luna", dynamic=True)

init python:
    def lun(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
        emote=None, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            luna.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        redraw = False
        tag = luna.tag
        layer = luna.layer

        if xpos is not None or ypos is not None:
            xpos = luna.pos[0] if xpos is None else sprite_pos.get("x").get(xpos, xpos)
            ypos = luna.pos[1] if ypos is None else sprite_pos.get("y").get(ypos, ypos)
            luna.pos = (xpos, ypos)
            redraw = True

        head_only = luna.pos[1] == sprite_pos.get("y").get("head")

        if any(face.values()):
            luna.set_face(**face)
            redraw = True

        if temp_face:
            last_face = luna.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            luna.set_face(**d)
            redraw = True

        if emote:
            luna.set_emote(emote)
            redraw = True

        if animation != False:
            luna.animation = animation
            redraw = True

        if flip != None:
            luna.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            character.luna_say(what, **kwargs)

        if temp_face:
            luna.set_face(**last_face)

        if head_only:
            luna.hide()
