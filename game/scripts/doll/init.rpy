# To add new doll character just add it to this named set inside your mod file
init offset = 2
init python:
    def wardrobe_init():
        for c in states.dolls:
            char = get_character_object(c)

            body_default = get_character_body(c, type="default")
            char.equip(body_default)

            outfit_default = get_character_outfit(c, type="default")
            char.equip(outfit_default)

            outfit_last = outfit = get_character_outfit(c, type="last")
            outfit_last.save()

            char.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid", cheeks="none", tears="none")

    def chibi_init():
        # TODO: Perhaps it could be automated?
        hooch_chibi.register("stand", 1, (600, 800))
        hooch_chibi.register("walk", 8, (600, 800))

    config.start_callbacks.extend([wardrobe_init, chibi_init])
