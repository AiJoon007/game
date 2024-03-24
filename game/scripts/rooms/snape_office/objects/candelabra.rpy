
label candelabra:

    if game.daytime:

        if not states.map.snape_office.candelabra_examined:
            $ states.map.snape_office.candelabra_examined = True
            $ snape_office_candelabra_OBJ.set_image("snape_office_candelabra_on")

            call gen_chibi("stand_alt", xpos="candelabra", ypos="candelabra")
            with d5

            gen "That's a lot of candles..." ("base", xpos="far_left", ypos="head")
            gen "Yet it doesn't make the room look any more inviting." ("base", xpos="far_left", ypos="head")

            call gen_chibi("stand", xpos="door", ypos="base")
            with d5

            jump quests

        else:
            $ snape_office_candelabra_OBJ.set_image("snape_office_candelabra_off")
            show screen blkfade
            with d2
            play sound "sounds/fire_woosh.ogg"

            if not states.map.snape_office.intro_e2:
                gen "..." ("base", xpos="far_left", ypos="head")
                gen "I don't know what I expected to happen." ("base", xpos="far_left", ypos="head")
            else:
                gen "..." ("base", xpos="far_left", ypos="head")
                gen "What an unexpected turn of events." ("base", xpos="far_left", ypos="head")

            play sound "sounds/fire_woosh.ogg"
            $ snape_office_candelabra_OBJ.set_image("snape_office_candelabra_on")
            hide screen blkfade
            with d9
    else:
        $ snape_office_candelabra_OBJ.set_image("snape_office_candelabra_off")
        show screen blkfade
        with d2
        play sound "sounds/fire_woosh.ogg"
        sna "Why did you do that...?"
        gen "Sorry..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/fire_woosh.ogg"
        $ snape_office_candelabra_OBJ.set_image("snape_office_candelabra_on")
        hide screen blkfade
        with d9

    jump snape_office_menu
