label fireplace:
    if game.day == 1:
        if not states.gen.ev.intro.fireplace_examined:
            $ states.gen.ev.intro.fireplace_examined = True
            $ fireplace_OBJ.idle = "fireplace_idle_shadow"
            call gen_chibi("stand","mid","base")
            with d5
            gen "*Hmm*... Looks like an ordinary fireplace..." ("base", xpos="far_left", ypos="head")
            call gen_chibi("sit_behind_desk")
            with d5
        else:
            gen "Looks like a normal fireplace to me." ("base", xpos="far_left", ypos="head")

        if states.gen.ev.intro.bird_examined and states.gen.ev.intro.desk_examined and states.gen.ev.intro.cupboard_examined and states.gen.ev.intro.door_examined and states.gen.ev.intro.fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    if is_puzzle_box_in_fireplace():
        call gen_chibi("stand", "fireplace", "fireplace")
        with d3
        gen "(*Hmm*... There's something glimmering in the fireplace.)" ("base", xpos="far_left", ypos="head")

        $ fireplace_OBJ.foreground = None

        gen "(A loose brick... If only I could--{nw}{w=1.0})" ("base", xpos="far_left", ypos="head")
        play sound "sounds/brick_scrape.ogg"
        gen "(A loose brick... If only I could--{fast} *Hhng*... There we go.)" ("base", xpos="far_left", ypos="head")
        call give_reward("A puzzle box has been added to your inventory!", "interface/icons/puzzle_box.webp")

        $ puzzle_box_ITEM.owned = 1

        gen "Seems straight forward enough." ("base", xpos="far_left", ypos="head")
        gen "Maybe I should give it a try?" ("base", xpos="far_left", ypos="head")
        menu:
            "-Try solving the puzzle-":
                call gen_chibi("sit_behind_desk")
                with d3
                $ puzzle_box_ITEM.use()
            "-Save it for later-":
                gen "I don't have time for this now." ("base", xpos="far_left", ypos="head")

        call gen_chibi("sit_behind_desk")
        with d3

        jump main_room_menu

    if states.fireplace_started:
        $ states.fireplace_started = False
        $ fireplace_OBJ.foreground = None
    else:
        $ states.fireplace_started = True
        $ fireplace_OBJ.foreground = "fireplace_fire"
        $ states.fireplace_started_times += 1

    jump main_room_menu

init python:
    def is_puzzle_box_in_fireplace():
        return game.day >= 25 and not game.daytime and game.moon and not puzzle_box_ITEM.unlocked and not states.map.seventh_floor.unlocked
