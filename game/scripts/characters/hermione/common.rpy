
label update_hermione:

    $ hermione_chibi.update()
    $ hermione.xzoom = 1

    return

label end_hermione_event:
    call her_chibi("hide")
    hide hermione_main
    with d3
    pause.5

    call update_hermione

    $ states.last_girl = states.active_girl
    $ states.active_girl = None
    $ states.her.busy = True
    $ hermione.wear("all")
    $ hermione.set_cum(None)
    $ hermione.set_face(tears=False, cheeks=False)

    call music_block
    jump main_room_menu

define character.hermione_say = Character("name_hermione_genie", show_icon="hermione", dynamic=True)

init python:
    def her(what, mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None,
        emote=None, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):

        def show():
            hermione.show(force=True)

            if not renpy.in_rollback():
                renpy.with_statement(trans or d2)

        face = {"mouth": mouth, "eyes": eyes, "eyebrows": eyebrows, "pupils": pupils, "cheeks": cheeks, "tears": tears}
        temp_face = renpy.game.context().temporary_attributes
        redraw = False
        tag = hermione.tag
        layer = hermione.layer

        if xpos is not None or ypos is not None:
            xpos = hermione.pos[0] if xpos is None else sprite_pos.get("x").get(xpos, xpos)
            ypos = hermione.pos[1] if ypos is None else sprite_pos.get("y").get(ypos, ypos)
            hermione.pos = (xpos, ypos)
            redraw = True

        head_only = hermione.pos[1] == sprite_pos.get("y").get("head")

        if any(face.values()):
            hermione.set_face(**face)
            redraw = True

        if temp_face:
            last_face = hermione.get_face()

            d = dict(zip(temp_face[::2], temp_face[1::2]))
            hermione.set_face(**d)
            redraw = True

        if emote:
            hermione.set_emote(emote)
            redraw = True

        if animation != False:
            hermione.animation = animation
            redraw = True

        if flip != None:
            hermione.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            show()

        if what:
            character.hermione_say(what, **kwargs)

        if temp_face:
            hermione.set_face(**last_face)

        if head_only:
            hermione.hide()

label too_much:
    stop music fadeout 2.0
    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare",xpos="mid",trans=fade)
    her "How could you ask for such a thing!?"
    her "I think I better leave." ("angry", "happyCl", "worried", "mid",emote="sweat")

    call her_walk(action="leave")

    random:
        gen "(*Hmm*... I guess it was a little too soon for that.)" ("base", xpos="far_left", ypos="head")
        gen "(Did I say something wrong...?)" ("base", xpos="far_left", ypos="head")
        gen "(Welp, was worth a shot I guess.)" ("base", xpos="far_left", ypos="head")
        gen "(Perhaps I should rethink my approach...)" ("base", xpos="far_left", ypos="head")
        gen "(Judging by her reaction she's not yet ready for it...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 6

    jump end_hermione_event

label too_much_public:
    stop music fadeout 2.0
    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare",xpos="mid",trans=fade)
    her "How could you ask for such a thing!?"
    her "People would take me for a whore, I cannot let it happen!"
    her "I think I better leave." ("angry", "happyCl", "worried", "mid",emote="sweat")

    call her_walk(action="leave")

    random:
        gen "(*Hmm*... Maybe I should start with some easier tasks to lower her reputation first.)" ("base", xpos="far_left", ypos="head")
        gen "(I guess she still cares too much about her precious reputation.)" ("base", xpos="far_left", ypos="head")
        gen "(Silly girl still doesn't understand that her *reputation* isn't as important as she thinks.)" ("base", xpos="far_left", ypos="head")
        gen "(Did I ask too much of her...?)" ("base", xpos="far_left", ypos="head")
        gen "(She doesn't seem to be ready for this just yet.)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 6

    jump end_hermione_event
