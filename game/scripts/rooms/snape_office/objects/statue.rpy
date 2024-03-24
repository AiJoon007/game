
label snake_statue:

    if game.daytime:

        if not states.map.snape_office.statue_examined:
            $ states.map.snape_office.statue_examined = True
            $ snape_office_statue_OBJ.set_image("snape_office_statue")

            call gen_chibi("stand_alt", xpos="statue", ypos="statue")
            with d5

            gen "Creepy..." ("base", xpos="far_left", ypos="head")
            gen "There appears to be a slight hissing sound emanating from it..." ("base", xpos="far_left", ypos="head")
            gen "Hopefully it's just an air vent to suck up any fumes or smells." ("base", xpos="far_left", ypos="head")
            gen "I should probably install one of those for my office..." ("base", xpos="far_left", ypos="head")

            call gen_chibi("stand", xpos="door", ypos="base")
            with d5

            jump quests

        elif not states.map.snape_office.intro_e2:
            gen "(Nothing here, it's just a fancy ventilation shaft.)" ("base", xpos="far_left", ypos="head")
        else:
            gen "(Looks like this snake head statue acts as a ventilation shaft.)" ("base", xpos="far_left", ypos="head")
    else:
        gen "That's a solid snake statue you have there." ("base", xpos="far_left", ypos="head")
        sna "Thanks."

    jump snape_office_menu
