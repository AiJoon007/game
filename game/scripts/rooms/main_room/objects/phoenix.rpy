label phoenix:

    if game.day == 1:
        if not states.gen.ev.intro.bird_examined:
            $ states.gen.ev.intro.bird_examined = True
            $ phoenix_OBJ.idle = "phoenix_idle"
            call gen_chibi("stand","mid","base",flip=False)
            with d5
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            gen "Even this weird-looking bird radiates magic..." ("base", xpos="far_left", ypos="head")
            call gen_chibi("sit_behind_desk")
            with d5
        else:
            gen "It's just a bird. Nothing more to say." ("base", xpos="far_left", ypos="head")

        if states.gen.ev.intro.bird_examined and states.gen.ev.intro.desk_examined and states.gen.ev.intro.cupboard_examined and states.gen.ev.intro.door_examined and states.gen.ev.intro.fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    if not states.bird_fed:
        $ states.bird_fed = True
        $ states.bird_fed_times += 1

        call gen_chibi("grab_high", phoenix_OBJ.xpos, phoenix_OBJ.ypos+365, flip=False) # Note: Flip is inconsistent
        with d3
        pause .5

        $ phoenix_OBJ.foreground = "phoenix_food"
        with d3

        random:
            gen "There you go..." ("base", xpos="far_left", ypos="head")
            gen "Eat up, buddy." ("base", xpos="far_left", ypos="head")
            pause .8

        call gen_chibi("sit_behind_desk")
        jump main_room_menu

    if not states.bird_petted:
        $ states.bird_petted = True
        $ states.bird_petted_times += 1
        call gen_chibi("petting", phoenix_OBJ.xpos, phoenix_OBJ.ypos+270, flip=False) # Note: Flip is inconsistent
        with d3
        pause .5

        random:
            gen "Who's a good bird?" ("base", xpos="far_left", ypos="head")
            "*Pat *Pat *Pat..."
            "Glad you aren't as noisy as Iago..."
            pause 2.4

        call gen_chibi("sit_behind_desk")
        jump main_room_menu

    gen "I have already fed and petted it today." ("base", xpos="far_left", ypos="head")
    gen "Wouldn't want to overdo it." ("base", xpos="far_left", ypos="head")

    jump main_room_menu
