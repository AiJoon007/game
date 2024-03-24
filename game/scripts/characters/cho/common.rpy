
label update_cho:

    # Chibi Update
    $ cho_chibi.update()
    $ cho_chibi.position(flip=False)
    $ cho.xzoom = 1
    hide screen cho_cloth_pile

    return

label end_cho_event:
    call cho_chibi("hide")
    hide cho_main
    with d3
    pause.5

    call update_cho

    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.cho.busy = True
    $ cho.wear("all")
    $ cho.set_cum(None)
    $ cho.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

define character.cho_say = Character("name_cho_genie", show_icon="cho", dynamic=True)

init python in character:
    # Cho's name is short, therefore it needs to be initialised in character scope,
    # otherwise we won't be able to use the same name for both Doll and Character calls.
    def cho(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
        emote=None, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            renpy.store.cho.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or renpy.store.d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        redraw = False
        tag = renpy.store.cho.tag
        layer = renpy.store.cho.layer

        if xpos is not None or ypos is not None:
            xpos = renpy.store.cho.pos[0] if xpos is None else renpy.store.sprite_pos.get("x").get(xpos, xpos)
            ypos = renpy.store.cho.pos[1] if ypos is None else renpy.store.sprite_pos.get("y").get(ypos, ypos)
            renpy.store.cho.pos = (xpos, ypos)
            redraw = True

        head_only = renpy.store.cho.pos[1] == renpy.store.sprite_pos.get("y").get("head")

        if any(face.values()):
            renpy.store.cho.set_face(**face)
            redraw = True

        if temp_face:
            last_face = renpy.store.cho.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            renpy.store.cho.set_face(**d)
            redraw = True

        if emote:
            renpy.store.cho.set_emote(emote)
            redraw = True

        if animation != False:
            renpy.store.cho.animation = animation
            redraw = True

        if flip != None:
            renpy.store.cho.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            cho_say(what, **kwargs)

        if temp_face:
            renpy.store.cho.set_face(**last_face)

        if head_only:
            renpy.store.cho.hide()
