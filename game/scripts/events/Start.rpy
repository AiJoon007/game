label start_wt:
    $ disable_game_menu()

    show screen blkfade
    with d3
    show image "images/rooms/_bg_/castle.webp"
    hide screen blkfade
    with d3
    show screen close_button(action=MainMenu())

    menu:
        "Difficulty" "How difficult do you want the game to be?"
        "-Easy-{size=-8}\nIncreased gold, item drop rate and Slytherin-points gains.\nMood will improve faster.\nCheats are available.{/size}":
            $ game.difficulty = 1
            $ game.cheats = True
        "-Normal-{size=-8}\nBalanced gold, item drop rate and Slytherin-points gains.\nMood will improve normally.\nCheats are available.{/size}":
            $ game.difficulty = 2
            $ game.cheats = True
        "-Hardcore-{size=-8}\nReduced gold, item drop rate and Slytherin-points gains.\nMood will not improve over time.\nNo cheats.{/size}":
            $ game.difficulty = 3
            $ game.cheats = False

    if persistent.game_complete:
        menu:
            "NEW GAME+" "Would you like to carry over your hard earned gold from your previous playthrough?"
            "-Yes please-":
                $ game.gold += (persistent.gold or 0)
                nar "[persistent.gold] gold has been added to your funds."

            "-No need-":
                pass

    menu:
        "Skip content" "Would you like to skip early sections of the game?"
        "-Play the intro-":
            pass
        "-Skip the intro-":
            $ states.map.unlocked = True
            $ states.sna.level = 5
            $ states.ton.level = 5
            jump skip_to_hermione

    hide image "images/rooms/_bg_/castle.webp"
    hide screen close_button
    $ enable_game_menu()

    jump genie_intro_E1

label genie_intro_E1:
    $ game.weather = "clear"
    $ game.daytime = False
    $ game.day = 0
    call send_letters

    stop background
    stop weather

    call room("main_room")
    call gen_chibi("hide")
    play music "music/the-chamber-by-kevin-macleod.ogg" fadein 1 if_changed
    $ desk_OBJ.idle = "desk_dumbledore"
    $ desk_OBJ.foreground = "letter_on_desk"
    $ chair_OBJ.hidden = True
    $ chair_left_OBJ.hidden = True
    hide screen blkfade
    with d5

    pause 0.5
    $ renpy.block_rollback()

    $ name_dumbledore_genie = "Old Bearded Man"

    play sound "sounds/snore1.ogg"
    dum1 "*Sounds of an old man sleeping like a baby*"
    pause 1
    play sound "sounds/thunder_2.ogg"
    $ game.weather = "storm"
    call weather_sound
    with flashbulb
    dum3 "Oh my!"
    dum2 "A storm at this hour?"
    dum2 "How peculiar... My pocket watch usually tells me when--"
    dum1 "Hold on... I'm sensing something--"
    dum1 "Strange...{w=0.4} No...{w=0.4} Unfamiliar..."
    dum3 "Magic."
    dum1 "How curious."
    dum2 "*Yawn*...{w=0.4} Well... It begins to dawn."

    # Swap to day seamlessly
    $ game.daytime = True
    $ game.day = 1
    $ mailbox.tick()
    with d9

    dum2 "Perhaps I should--"

    $ name_dumbledore_genie = "Albus Dumbledore"

    play sound "sounds/magic4.ogg"
    $ desk_OBJ.idle = "ch_gen sit_behind_desk"
    $ game.weather = "rain"
    call weather_sound
    with flash

    pause 1.0

    call bld
    gen "Your majesty! Don't touch--" ("angry", xpos="far_left", ypos="head")
    gen "............................." ("base", xpos="far_left", ypos="head")
    gen "I did it again, didn't I?" ("base", xpos="far_left", ypos="head")
    gen "Teleported myself to who knows where..." ("angry", xpos="far_left", ypos="head")
    gen "Those magical ingredients must have been way more potent than I thought..." ("base", xpos="far_left", ypos="head")
    gen "Well... Whatever this place is I have no business here." ("base", xpos="far_left", ypos="head")
    gen "Better to undo the spell and return to my magic shop before Princess Jasmine gets angry with me again..." ("base", xpos="far_left", ypos="head")
    gen "....................." ("base", xpos="far_left", ypos="head")
    gen "Although..." ("base", xpos="far_left", ypos="head")
    gen "There is something odd about this place..." ("base", xpos="far_left", ypos="head")
    gen "It's almost brimming with..." ("base", xpos="far_left", ypos="head")
    gen "{size=+5}MAGIC?!{/size}" ("angry", xpos="far_left", ypos="head")
    gen "Yes... magic, I can feel it. So powerful and yet somehow..." ("base", xpos="far_left", ypos="head")
    gen "... alien." ("base", xpos="far_left", ypos="head")
    gen "Interesting..." ("base", xpos="far_left", ypos="head")
    gen "I think I will stick around for a little bit..." ("base", xpos="far_left", ypos="head")

    # Highlight important objects
    python:
        fireplace_OBJ.idle = At("fireplace_idle_shadow", pulse_hover)
        cupboard_OBJ.idle = At("cupboard_idle", pulse_hover)
        phoenix_OBJ.idle = At("phoenix_idle", pulse_hover)
        door_OBJ.idle = At("door_idle", pulse_hover)
        desk_OBJ.idle = At("ch_gen sit_behind_desk", pulse_hover)

        achievements.unlock("start")
        states.gen.ev.intro.e1_complete = True

    jump main_room_menu

label genie_intro_E2:
    call bld
    gen "It's getting darker already..." ("base", xpos="far_left", ypos="head")
    gen "Did I just spend an entire day examining this room?" ("base", xpos="far_left", ypos="head")
    call bld("hide")

    $ states.gen.ev.intro.e2_complete = True

    # Next is Snape intro E1

    jump night_start

# TIme pass intro.
label genie_intro_E3:
    play music "music/Brittle Rille.ogg" fadein 1 if_changed

    call bld
    gen ".............." ("base", xpos="far_left", ypos="head")
    gen "Another boring day in the office." ("base", xpos="far_left", ypos="head")
    gen "All I can do here is sleep or jerk off..." ("angry", xpos="far_left", ypos="head")
    gen "..........." ("base", xpos="far_left", ypos="head")
    gen "Yet still... This magic... There's something strange going on here." ("base", xpos="far_left", ypos="head")
    call bld("hide")

    call tutorial("time")

    $ states.gen.ev.intro.e3_complete = True

    jump main_room_menu

# Owl intro.
label genie_intro_E4:
    play music "music/Brittle Rille.ogg" fadein 1 if_changed

    call bld
    gen "An owl? Here?" ("base", xpos="far_left", ypos="head")
    call bld("hide")

    call tutorial("mail")

    $ states.gen.ev.intro.e4_complete = True

    jump main_room_menu

label skip_to_hermione:
    $ renpy.block_rollback()

    hide image "images/rooms/_bg_/castle.webp"
    hide screen close_button
    $ enable_game_menu()

    call send_letters
    call cheats.hermione_skip_intro

    python:
        for letter in mailbox.letters:
            letter.wait -= 13

    jump day_start

label send_letters:
    python:
        letter_hg_2.send() # Arrives on day 2
        letter_work_unlock.send() # Arrives on day 4
        letter_favors.send() # Arrives on day 8
        letter_cards_unlock.send() # Arrives on day 24
    return
