
label shelves:

    if game.daytime:

        if not states.map.snape_office.shelves_examined:
            $ states.map.snape_office.shelves_examined = True
            $ snape_office_shelves_OBJ.set_image("snape_office_shelves")

            call gen_chibi("stand_alt", xpos="shelves", ypos="shelves", flip=False)
            with d5

            random:
                block:
                    gen "Who keeps a skull as decoration." ("base", xpos="far_left", ypos="head")
                    gen "..." ("base", xpos="far_left", ypos="head")
                block:
                    gen "A cactus..." ("base", xpos="far_left", ypos="head")
                    gen "Hopefully the only living thing here." ("base", xpos="far_left", ypos="head")
                block:
                    gen "What a slob..." ("base", xpos="far_left", ypos="head")
                    gen "Doesn't he know it's dangerous to have potions mix like this?" ("base", xpos="far_left", ypos="head")
                block:
                    gen "A wine bottle..." ("base", xpos="far_left", ypos="head")
                    gen "Wait a minute, why is he always coming to my place to drink?" ("base", xpos="far_left", ypos="head")
                    gen "There's plenty in here already..." ("base", xpos="far_left", ypos="head")

            call gen_chibi("stand", xpos="door", ypos="base", flip=True)
            with d5

            jump quests

        elif not states.map.snape_office.intro_e2:
            gen "(Already checked the shelves, there's nothing of value.)" ("base", xpos="far_left", ypos="head")
        else:
            gen "There's nothing useful to me on the shelves." ("base", xpos="far_left", ypos="head")
    else:
        gen "(And here I thought my office was dirty...)" ("base", xpos="far_left", ypos="head")

    jump snape_office_menu
