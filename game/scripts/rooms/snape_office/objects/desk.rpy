
label snape_at_desk:

    if game.daytime:
        if not states.map.snape_office.desk_examined:
            $ states.map.snape_office.desk_examined = True
            $ snape_office_desk_OBJ.set_image("snape_office_desk")
            $ experimental_recipes_ITEM.owned = 1

            call gen_chibi("stand", xpos="beside_chair", ypos="beside_chair", flip=False)
            with d5

            play sound "sounds/drawer_open.ogg" volume 0.25
            pause 1.5

            gen "So much junk..." ("base", xpos="far_left", ypos="head")
            gen "What even are these scrolls?" ("base", xpos="far_left", ypos="head")
            gen "*Hmm*... Looks like invoices." ("base", xpos="far_left", ypos="head")
            gen "{i}The Basilick{/i}..." ("base", xpos="far_left", ypos="head")
            gen "What the hell is a {i}basi{/i}...{i}lick{/i}?" ("base", xpos="far_left", ypos="head")
            gen "There has to be something useful in here..." ("base", xpos="far_left", ypos="head")
            gen "What the--" ("base", xpos="far_left", ypos="head")
            gen "This drawer is full of panties!" ("angry", xpos="far_left", ypos="head")
            gen "And they're all labelled..." ("base", xpos="far_left", ypos="head")
            gen "I knew he was a perv but what the hell does he need all these for?" ("base", xpos="far_left", ypos="head")
            gen "Why hasn't he shared any of them with me!" ("base", xpos="far_left", ypos="head")
            gen "Hold on, there's something else..." ("base", xpos="far_left", ypos="head")
            gen "Looks like potion recipes!" ("base", xpos="far_left", ypos="head")
            gen "Let's see now...{w=0.3} Experimental...{w=0.3} Untested...{w=0.3} Theoretical..." ("base", xpos="far_left", ypos="head")
            gen "Sounds like these were made just for me!" ("grin", xpos="far_left", ypos="head")

            call gen_chibi("stand", xpos="door", ypos="base")
            with d5

            call give_reward("You have acquired experimental potion recipes!", experimental_recipes_ITEM)

            jump quests
        elif not states.map.snape_office.intro_e2:
            gen "(I have already checked the desk and got the recipes.)" ("base", xpos="far_left", ypos="head")
        else:
            gen "I'd better leave his desk alone." ("base", xpos="far_left", ypos="head")
    else:
        sna "Can't you see that I'm busy, Genie?"

    jump snape_office_menu
