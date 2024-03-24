
label summon_cho:
    #play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    #play sound "sounds/door.ogg"

    $ states.active_girl = "cho"

    $ states.cho.busy = True
    #call update_states.cho.tier
    call update_cho

    $ renpy.checkpoint(hard=True)

    if states.cho.ev.panty_thief.acquired:
        if states.cho.tier == 2:
            jump cho_panties_response_T2
        elif states.cho.tier == 3:
            jump cho_panties_response_T3

    # Slytherin Quidditch Intro.
    if states.cho.tier == 2 and not states.cho.ev.quidditch.e5_complete:
        jump cho_quid_E5
    # Gryffindor Quidditch Intro.
    elif states.cho.tier == 3 and not states.cho.ev.quidditch.e10_complete:
        jump cho_quid_E10
    # Quidditch Outro (Not yet finished, need a few more days)
    elif states.cho.tier == 4 and not states.cho.ev.quidditch.e14_complete:
        jump cho_quid_E14

    # Clothes Events
    call cho_summon_setup

    label cho_requests:

    # Reset
    call reset_menu_position
    cho "" (xpos="base", ypos="base")

    menu:

        # Main Matches
        "-Start Hufflepuff Match-" (icon="interface/icons/small/huff.webp") if (states.cho.tier == 1 and states.cho.ev.quidditch.hufflepuff_stage == "ready"):
            if states.cho.public_level == 0:
                gen "(If I want Cho to do anything in public with those {i}Muffletuffs{/i} I better do it before the match.)" ("base", xpos="far_left", ypos="head")
                gen "(Although maybe not...)" ("base", xpos="far_left", ypos="head")
                menu:
                    "Are you ready to begin the match?"
                    "-Yes-":
                        pass
                    "-no-":
                        jump cho_requests
            jump start_hufflepuff_match

        "-Start Slytherin Match-" (icon="interface/icons/small/slyt.webp") if (states.cho.tier == 2 and states.cho.ev.quidditch.slytherin_stage == "ready" and states.cho.ev.quidditch.e7_complete):
            if states.cho.public_level <= 3:
                gen "(If I want Cho to do anything in public with those {i}Slythershits{/i} I better do it before the match.)" ("base", xpos="far_left", ypos="head")
                gen "(Although maybe not...)" ("base", xpos="far_left", ypos="head")
                menu:
                    "Are you ready to begin the match?"
                    "-Yes-":
                        pass
                    "-no-":
                        jump cho_requests
            jump start_slytherin_match

        "-Start Gryffindor Match-" (icon="interface/icons/small/gryf.webp") if (states.cho.tier == 3 and states.cho.ev.quidditch.gryffindor_stage == "ready" and states.cho.ev.quidditch.e13_complete):
            if states.cho.public_level <= 6:
                gen "(If I want Cho to do anything in public with those {i}Gryphoncucks{/i} I better do it before the match.)" ("base", xpos="far_left", ypos="head")
                gen "(Although maybe not...)" ("base", xpos="far_left", ypos="head")

            nar "Starting the match will progress Cho's story to the next stage."
            nar "Make sure to save your game in case you want to return to this stage later."
            pause.5

            menu:
                "Are you ready to begin the match?"
                "-Yes-":
                    pass
                "-No-":
                    jump cho_requests
            jump start_gryffindor_match

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if states.cho.mood > 0:
                cho "I have nothing to say to you, [name_genie_cho]..." ("annoyed", "base", "base", "mid")
                jump cho_requests

            call cho_chitchat
            jump cho_talk

        # Quidditch Training
        "-Training-" (icon="interface/icons/small/quidditch.webp") if states.cho.tier < 4 and not states.cho.ev.quidditch.lock_training:
            if states.cho.mood > 0:
                gen "Ready to get back to training?" ("base", xpos="far_left", ypos="head")
                if states.cho.mood >= 5:
                    cho "No.{w=0.5} And I don't want to hear of it right now, Sir." ("open", "narrow", "angry", "mid")
                else:
                    cho "I'm sorry, [name_genie_cho]. But I don't feel like training today." ("soft", "base", "worried", "down")
                nar "Cho is still upset with you."
                jump cho_requests

            jump cho_training

        "-Training-" (icon="interface/icons/small/quidditch.webp", style="disabled") if states.cho.tier < 4 and states.cho.ev.quidditch.lock_training:
            gen "(She's as ready as one can be.)" ("base", xpos="far_left", ypos="head")
            jump cho_requests

        "-Sexual favours-" (icon="interface/icons/small/condom.webp") if states.cho.favors_unlocked:
            if states.cho.mood > 0:
                cho "I'm sorry, [name_genie_cho]. But I don't feel like it today..." ("upset", "base", "worried", "mid")
                jump cho_requests
            else:
                jump cho_favor_menu

        "-Sexual favours-" (icon="interface/icons/small/condom.webp", style="disabled") if not states.cho.favors_unlocked:
            if states.cho.tier == 1:
                gen "(I need to help her with her Quidditch training, before I can ask for something like this.)" ("base", xpos="far_left", ypos="head")
            elif states.cho.tier == 4:
                gen "(I have a feeling this is as far as I can progress with her at the moment.)" ("base", xpos="far_left", ypos="head")
            else:
                gen "(I should ask her about the next Quidditch match first. See who we're up against...)" ("base", xpos="far_left", ypos="head")
            jump cho_requests

        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if states.cho.wardrobe_unlocked:
            hide cho_main with d1
            call wardrobe
            jump cho_requests

        "-Wardrobe-" (style="disabled") if not states.cho.wardrobe_unlocked:
            nar "You haven't unlocked this feature yet."
            jump cho_requests

        "-Give Item-" (icon="interface/icons/small/gift.webp"):
            hide cho_main with d1
            call gift_menu
            jump cho_requests

        # Dismiss
        "-Dismiss Her-":
            stop music fadeout 3.0

            if states.cho.mood == 0:
                cho "Goodbye, [name_genie_cho]." ("base", "base", "base", "mid")
            else:
                cho "Goodbye, [name_genie_cho]." ("annoyed", "base", "base", "L")

            play sound "sounds/door.ogg"

            jump end_cho_event

# Cho Favor Menu
label cho_favor_menu:
    menu:
        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp"):
            label .favors:

            call tutorial("hearts")

            $ result = show_events_menu(cho_favors)

            if result in ("disabled", "noncompliant"):
                "You haven't unlocked this favour opportunity yet."
                jump .favors
            elif result == "exit":
                jump cho_favor_menu
            else:
                $ result.start()

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled") if not game.daytime or not states.cho.requests_unlocked:
            if not states.cho.requests_unlocked:
                nar "Progress further to unlock public requests."
            elif not game.daytime:
                nar "Public requests are available during the day only."
            jump cho_favor_menu

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp") if game.daytime and states.cho.requests_unlocked:
            label .requests:

            call tutorial("hearts")

            $ result = show_events_menu(cho_requests)

            if result in ("disabled", "noncompliant"):
                "You haven't unlocked this request opportunity yet."
                jump .requests
            elif result == "exit":
                jump cho_favor_menu
            else:
                $ result.start()

        "-Never mind-":
            jump cho_requests

label not_available:
    $ TBA_message("This feature is currently not available as of version %s." % config.version)
    return

