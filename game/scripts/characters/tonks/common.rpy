define tonks_haircolor_table = {
    "angry": [Color((164, 34, 34, 255)), Color((219, 83, 83, 255))],
    "upset": [Color((228, 93, 34, 255)), Color((246, 193, 170, 255))],
    "happy": [Color((255, 213, 23, 255)), Color((255, 239, 167, 255))],
    "disgusted": [Color((111, 205, 75, 255)), Color((200, 237, 186, 255))],
    "scared": [Color((238, 238, 241, 255)), Color((249, 249, 250, 255))],
    "horny": [Color((255, 105, 180, 255)), Color((251, 205, 222, 255))],
    "sad": [Color((64, 75, 205, 255)), Color((182, 186, 237, 255))],
}

label update_tonks:

    # Chibi Update
    $ tonks_chibi.update()
    $ tonks_chibi.position(flip=False)
    $ tonks.xzoom = 1
    hide screen ton_cloth_pile

    $ tonks.get_equipped("hair").set_color(tonks_haircolor)
    return

label end_tonks_event:
    call ton_chibi("hide")
    hide tonks_main
    with d3
    pause.5

    call update_tonks

    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.ton.busy = True
    $ tonks.wear("all")
    $ tonks.set_cum(None)
    $ tonks.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

define character.tonks_say = Character("name_tonks_genie", show_icon="tonks", dynamic=True)

init python:
    def ton(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
    emote=None, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            tonks.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        temp_hair = None
        redraw = False
        tag = tonks.tag
        layer = tonks.layer

        if xpos is not None or ypos is not None:
            xpos = tonks.pos[0] if xpos is None else sprite_pos.get("x").get(xpos, xpos)
            ypos = tonks.pos[1] if ypos is None else sprite_pos.get("y").get(ypos, ypos)
            tonks.pos = (xpos, ypos)
            redraw = True

        head_only = tonks.pos[1] == sprite_pos.get("y").get("head")

        if any(face.values()):
            tonks.set_face(**face)
            redraw = True

        if temp_face:
            last_face = tonks.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            temp_hair = d.pop("hair", None)

            tonks.set_face(**d)
            redraw = True

        if temp_hair:
            last_hair = tonks.get_equipped("hair").color
            col = tonks_haircolor_table.get(temp_hair)
            tonks.get_equipped("hair").set_color(col)
            redraw = True

        if emote:
            tonks.set_emote(emote)
            redraw = True

        if animation != False:
            tonks.animation = animation
            redraw = True

        if flip != None:
            tonks.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            character.tonks_say(what, **kwargs)

        if temp_face:
            tonks.set_face(**last_face)

        if temp_hair:
            tonks.get_equipped("hair").set_color(last_hair)

        if head_only:
            tonks.hide()
