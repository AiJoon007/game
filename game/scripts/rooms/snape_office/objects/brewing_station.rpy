
label brewing_station:

    if game.daytime:
        if not states.map.snape_office.station_examined:
            $ states.map.snape_office.station_examined = True
            $ snape_office_brewing_station_OBJ.set_image("snape_office_brewing_station_off")

            call gen_chibi("stand_alt", xpos="station", ypos="station")
            with d5

            gen "Brewing supplies...{w=0.4} Feels like home." ("base", xpos="far_left", ypos="head")
            gen "Looks like it just has some base liquids for potions..." ("base", xpos="far_left", ypos="head")
            gen "Water... Breastmilk... The usual stuff..." ("base", xpos="far_left", ypos="head")
            gen "I'll probably need to bring some more ingredients if I want to brew anything here..." ("base", xpos="far_left", ypos="head")

            call gen_chibi("stand", xpos="door", ypos="base")
            with d5

            jump quests

        elif not states.map.snape_office.intro_e2:
            gen "(I've already examined it, I should leave it for now.)" ("base", xpos="far_left", ypos="head")
        else:
            $ experimental_recipes_ITEM.used = True
            call tutorial("brewing")
            call brewing
            jump snape_office_menu
    else:
        # Genie is talking about alcohol, while Snape thinks he's talking about Madam Hooch

        if not states.map.snape_office.intro_e2:
            gen "(*Hmm*... I didn't know Snape was into distillery. Let's see if I can guess the type of booze by the smell.)" ("base", xpos="far_left", ypos="head")
            "*Sniff* *Sniff*"
            gen "*Ugh*! It smells like wet hair mixed with cat poo or something!" ("angry", xpos="far_left", ypos="head")
            sna "*Snickers* What did you expect? Lillies?"
            gen "I thought you were soaking some hooch in here." ("base", xpos="far_left", ypos="head")
            sna "W-What?!" # blushing
            sna "Madam Hooch is not my type." # blushing, eyes closed
            gen "Figures. I had a feeling you're more into old wines." ("base", xpos="far_left", ypos="head")
            sna "Huh? What is that supposed to--" # annoyed
            sna "*Tsk* You know what, forget it, just let me work in peace."
            gen "(His alcoholism is a touchy subject I guess...)" ("base", xpos="far_left", ypos="head")
        elif states.map.snape_office.intro_e3:
            sna "What did I tell you?"
            sna "You can use my brewing station when I'm not in the office..."
            sna "I don't want to smell your failure." # grin
            gen "Asshole..." ("base", xpos="far_left", ypos="head")

    jump snape_office_menu
