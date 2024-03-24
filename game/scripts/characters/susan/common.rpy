
label end_susan_event:
    call sus_chibi("hide")
    hide susan_main
    with d3
    pause.5

    call update_susan

    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.sus.busy = True
    $ susan.wear("all")
    $ susan.set_cum(None)
    $ susan.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

label update_susan:
    # Chibi Update
    $ susan_chibi.update()
    $ susan_chibi.position(flip=False)
    $ susan.xzoom = 1
    hide screen susan_cloth_pile

    return

define character.susan_say = Character("name_susan_genie", show_icon="susan", dynamic=True)

init python:
    def sus(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
        emote=None, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            susan.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        redraw = False
        tag = susan.tag
        layer = susan.layer

        if xpos is not None or ypos is not None:
            xpos = susan.pos[0] if xpos is None else sprite_pos.get("x").get(xpos, xpos)
            ypos = susan.pos[1] if ypos is None else sprite_pos.get("y").get(ypos, ypos)
            susan.pos = (xpos, ypos)
            redraw = True

        head_only = susan.pos[1] == sprite_pos.get("y").get("head")

        if any(face.values()):
            susan.set_face(**face)
            redraw = True

        if temp_face:
            last_face = susan.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            susan.set_face(**d)
            redraw = True

        if emote:
            susan.set_emote(emote)
            redraw = True

        if animation != False:
            susan.animation = animation
            redraw = True

        if flip != None:
            susan.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            character.susan_say(what, **kwargs)

        if temp_face:
            susan.set_face(**last_face)

        if head_only:
            susan.hide()
