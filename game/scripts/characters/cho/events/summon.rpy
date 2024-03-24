label cho_summon_setup:

    $ states.cho.wardrobe_unlocked = True

    # Reset doll state
    $ cho.wear("all")
    $ cho.set_cum(None)
    $ cho.animation = None

    # Unlock favours at tier 3
    # this will probably move to a cho_quid_E# event once we've implemented Gryffindor lead-up events
    if states.cho.tier == 3:
        $ states.cho.favors_unlocked = True

    if states.cho.wardrobe_scheduling:
        $ cho.equip_random_outfit()

    play sound "sounds/door.ogg"
    call cho_chibi("stand", "mid", "base")
    with d3

    #Cho greeting.
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    if states.cho.mood > 0:
        if 5 > states.cho.mood >= 1:
            cho "Yes, [name_genie_cho]?" ("annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > states.cho.mood >= 5:
            cho "*Sigh*... Yes, [name_genie_cho]?" ("open", "base", "base", "R", xpos="base", ypos="base", trans=d3)
        elif 20 > states.cho.mood >= 10:
            cho "What is it, [name_genie_cho]?" ("annoyed", "base", "angry", "mid", xpos="base", ypos="base",trans=d3)
        elif 30 > states.cho.mood >= 20:
            cho "What do you want, \"[name_genie_cho]\"?" ("angry", "narrow", "angry", "mid", xpos="base", ypos="base",trans=d3)
        elif 40 > states.cho.mood >= 30:
            cho "*Hmph*..." ("upset", "base", "angry", "R", xpos="base", ypos="base",trans=d3)
        elif 50 > states.cho.mood >= 40:
            cho "*Tsk*" ("soft", "narrow", "angry", "R", xpos="base", ypos="base",trans=d3)
        elif states.cho.mood >= 50:
            cho "I can't believe you've done this!" ("scream", "wide", "angry", "mid", xpos="base", ypos="base",trans=d3)
            cho "" ("upset", "wide", "angry", "mid")

        call describe_mood("Cho", states.cho.mood)
        call tutorial("moodngifts")
    else:
        if game.daytime:
            cho "Good morning, [name_genie_cho]." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
            cho "Good evening, [name_genie_cho]." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)

    if states.cho.tier == 1:
        # Intro hints
        if not states.sna.ev.hangouts.cho_e1 or not states.cho.ev.intro.e4_complete:

            label .hint_menu:

            menu:
                "-Talk-" (icon="interface/icons/small/talk.webp"):
                    cho "Have you gotten Hermione to stop spreading rumours about me?" ("annoyed", "narrow", "base", "mid")
                    gen "Oh, was I supposed to do that?" ("base", xpos="far_left", ypos="head")
                    cho "Yes!" ("angry", "base", "base", "mid")
                    gen "Right..." ("base", xpos="far_left", ypos="head")
                    gen "(Hmm... I think I could use this tension between those two...)" ("base", xpos="far_left", ypos="head")
                    if not states.sna.ev.hangouts.cho_e1:
                        gen "(Better tell Snape about my plan before confronting Miss Granger...)" ("base", xpos="far_left", ypos="head")
                    elif not states.cho.ev.intro.e4_complete:
                        gen " (I should probably talk to Hermione...)" ("base", xpos="far_left", ypos="head")

                    jump cho_summon_setup.hint_menu

                "-Dismiss Her-":
                    stop music fadeout 3.0

                    if states.cho.mood == 0:
                        cho "Goodbye, [name_genie_cho]." ("base", "narrow", "base", "mid")
                    else:
                        cho "Goodbye, [name_genie_cho]." ("annoyed", "narrow", "base", "mid")

                    play sound "sounds/door.ogg"

                    jump end_cho_event

    return
