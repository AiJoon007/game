
label end_hooch_event:
    hide hooch_main
    with d3
    pause.5

    $ hooch.xzoom = 1
    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.hoo.busy = True
    $ hooch.wear("all")
    $ hooch.set_cum(None)
    $ hooch.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

define character.hooch_say = Character("name_hooch_genie", show_icon="hooch", dynamic=True)

init python:
    def hoo(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
        emote=None, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            hooch.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        redraw = False
        tag = hooch.tag
        layer = hooch.layer

        if xpos is not None or ypos is not None:
            xpos = hooch.pos[0] if xpos is None else sprite_pos.get("x").get(xpos, xpos)
            ypos = hooch.pos[1] if ypos is None else sprite_pos.get("y").get(ypos, ypos)
            hooch.pos = (xpos, ypos)
            redraw = True

        head_only = hooch.pos[1] == sprite_pos.get("y").get("head")

        if any(face.values()):
            hooch.set_face(**face)
            redraw = True

        if temp_face:
            last_face = hooch.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            hooch.set_face(**d)
            redraw = True

        if emote:
            hooch.set_emote(emote)
            redraw = True

        if animation != False:
            hooch.animation = animation
            redraw = True

        if flip != None:
            hooch.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            character.hooch_say(what, **kwargs)

        if temp_face:
            hooch.set_face(**last_face)

        if head_only:
            hooch.hide()
