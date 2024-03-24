

#Door Events (Astoria wears random clothing.)

label astoria_summon_setup:

    # Reset doll state
    $ astoria.wear("all")
    $ astoria.set_cum(None)
    $ astoria.animation = None

    if states.ast.wardrobe_scheduling:
        $ astoria.equip_random_outfit()

    play sound "sounds/door.ogg"
    call ast_chibi("stand","mid","base")
    with d3

    #Astoria greeting.
    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed

    if states.ast.mood > 0:
        if 5 > states.ast.mood >= 1:
            ast "[name_genie_astoria]?" ("annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > states.ast.mood >= 5:
            ast "What now?" ("annoyed", "base", "worried", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > states.ast.mood >= 10:
            ast "What is it, [name_genie_astoria]?" ("annoyed", "base", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 30 > states.ast.mood >= 20:
            ast "What do you want, [name_genie_astoria]?" ("angry", "base", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif 40 > states.ast.mood >= 30:
            ast "*Hmph*..." ("annoyed", "narrow", "worried", "L", xpos="base", ypos="base", trans=d3)
        elif 50 > states.ast.mood >= 40:
            ast "*Tsk*" ("angry", "narrow", "angry", "mid", xpos="base", ypos="base", trans=d3)
        elif states.ast.mood >= 50:
            ast "What?!" ("scream", "narrow", "angry", "mid", xpos="base", ypos="base", trans=d3)
            ast "" ("angry", "narrow", "angry", "mid")

        call describe_mood("Astoria", states.ast.mood)
        call tutorial("moodngifts")
    else:
        if game.daytime:
            ast "Mornin', [name_genie_astoria]." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
            ast "Evenin', [name_genie_astoria]." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    return
