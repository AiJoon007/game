label prev_at_hogwarts:
    #Story Unlock requirements: Finish the first 3 Wizard Cards challenges.

    # Setup
    $ hermione.equip(her_outfit_default)
    $ game.daytime = True
    $ game.weather = "clear"
    $ game.day = 1
    $ game.gold = 0
    $ desk_OBJ.idle = "desk_dumbledore"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Previously, at Hogwarts{w=1.0}\nschool of Witchcraft and Wizardry...{/color}{/size}"

    play music "music/Brittle Rille.ogg" fadein 1 if_changed
    hide screen blkfade
    with d5

    pause 3.0
    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    pause.8

    dum3 "Please, come in..."
    pause.2

    call sna_walk(action="enter", xpos="mid", ypos="base")
    pause.5

    dum1 "Ah, Severus..."
    sna "You called, sir?" ("snape_01",xpos="base",ypos="base")
    dum2 "Indeed, I wanted to talk to you about last night."
    sna "Last night, sir?" ("snape_03")
    dum1 "Yes, last night... Don't think that I had forgotten already..."
    sna "..." ("snape_04")
    sna "I might have had a few. I hope I didn't say something inappropriate..." ("snape_05")
    dum2 "Quite... Do you remember why I hired you, Severus?"
    sna "For my excellent potion making skills?" ("snape_25")
    dum1 "For your excellent potion making skills..."
    dum5 "{size=-6}And your piercing black eyes...{/size}"
    sna "What?" ("snape_05")
    dum4 "What?"
    dum2 "I said, you're fierce and wise."
    sna "..." ("snape_05")
    sna "Why did you call me here again?" ("snape_03")
    dum1 "Ah yes, my apologies.... I got distracted."
    dum2 "How much do you remember from our previous discussion?"
    sna "Not a lot... it's all a bit of a haze..." ("snape_04")
    dum1 "..."
    sna "I think I mentioned a student spilling some flobberworm mucus down themselves which halted the whole lesson..." ("snape_01")
    sna "And that Potter boy..." ("snape_08")
    dum3 "There it is..."
    sna "The Potter boy?" ("snape_25")
    dum1 "Yes, I've noticed you've been quite stressed lately about this... Potter situation of yours, for the lack of a better term."
    sna "And your point?" ("snape_09")
    dum2 "Ah yes... my point."
    dum1 "Where was I again..."
    dum2 "Ah yes, your stress situation..."
    sna "(You're not really helping old man...)" ("snape_08")
    dum1 "Have you tried a draught of peace?"
    sna "What?" ("snape_03")
    dum2 "A draught of peace, it's a potion you know..."
    sna "Are you joking with me right now?" ("snape_04")
    dum1 "I'm being quite serious... stress can be quite taxing on your body."
    sna "I..." ("snape_01")
    sna "I need a moment... I'll talk to you later, Albus." ("snape_06")
    dum1 "I thought we were getting somewhere..."
    sna "..." ("snape_01")
    hide snape_main
    hide screen bld1
    with d3
    pause.2

    call sna_chibi("hide")
    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    call sna_walk(action="leave")

    stop music fadeout 1

    dum2 "\"I don't think I'll ever understa\"--"

    play sound "sounds/magic4.ogg"
    $ desk_OBJ.idle = "ch_gen sit_behind_desk"
    $ game.weather = "rain"
    call weather_sound
    with flash

    pause.8
    call bld
    gen "Your majesty! Don't touch--" ("angry", xpos="far_left", ypos="head")
    gen "............................." ("base", xpos="far_left", ypos="head")
    gen "I did it again, didn't I?" ("base", xpos="far_left", ypos="head")
    pause.2

    show screen blkfade
    with d9
    pause.8

    $ renpy.end_replay()
