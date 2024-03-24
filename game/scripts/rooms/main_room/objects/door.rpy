label door:
    if game.day == 1:
        if not states.gen.ev.intro.door_examined:
            $ states.gen.ev.intro.door_examined = True
            $ door_OBJ.idle = "door_idle"
            call gen_chibi("stand","door","base")
            with d5

            gen "A sturdy-looking door..." ("base", xpos="far_left", ypos="head")
            gen "I wonder what's behind it." ("base", xpos="far_left", ypos="head")
            label examining_the_door:
            menu:
                "-Knock on the door-":
                    show screen blktone
                    with d3
                    play sound "sounds/knocking.ogg"
                    "*Knock-knock-knock*"
                    "..................."
                    hide screen blktone
                    with d3
                    gen "No reply..." ("base", xpos="far_left", ypos="head")
                "-Put your ear on it-":
                    show screen blktone
                    with d3
                    nar "You put your ear on the door and listen intently..."
                    gen "I don't hear anything." ("base", xpos="far_left", ypos="head")
                    hide screen blktone
                    with d3
                "-Kick the door-":
                    show screen blktone
                    with d3
                    play sound "sounds/kick.ogg"
                    pause.2
                    with hpunch
                    "*Thump!*"
                    play sound "sounds/MaleGasp.ogg"
                    gen "Blimey! That hurts!" ("angry", xpos="far_left", ypos="head")
                    ".............................."
                    hide screen blktone
                    with d3
                    gen "This door could take a thousand kicks and it still wouldn't break..." ("base", xpos="far_left", ypos="head")
                "-Smell the door-":
                    show screen blktone
                    with d3
                    play sound "sounds/sniff.ogg"
                    gen "...{w} Smells like a door..." ("base", xpos="far_left", ypos="head")
                    hide screen blktone
                    with d3
                "-Leave it alone-":
                    gen "Who knows what kind of dangers could be lurking behind that door?" ("base", xpos="far_left", ypos="head")
                    gen "I think I'll let it be for now..." ("base", xpos="far_left", ypos="head")

            call gen_chibi("sit_behind_desk")
            with d3
        else:
            gen "I should leave this door alone for now." ("base", xpos="far_left", ypos="head")

        if states.gen.ev.intro.bird_examined and states.gen.ev.intro.desk_examined and states.gen.ev.intro.cupboard_examined and states.gen.ev.intro.door_examined and states.gen.ev.intro.fireplace_examined:
            jump genie_intro_E2
        else:
            jump main_room_menu

    call update_character_map_locations

    play sound "sounds/scroll.ogg"
    jump summon
