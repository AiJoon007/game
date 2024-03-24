label hermione_summon_setup:

    # Reset doll state
    $ hermione.wear("all")
    $ hermione.set_cum(None)
    $ hermione.animation = None

    #
    # TODO: Remove obsolete variables and fix the code after clothes have been added.
    #
    # if game.weather == "clear":

        # if states.her.tier >= 3 and game.daytime and not hg_muggle_hot_ITEM.unlocked:
            # $ hg_muggle_hot_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings   = True
                # $ h_top = "top_frilled_1"
                # $ h_bottom = "pants_jeans_short"
                # $ h_stockings = "stockings_cute"

                # call update_her_uniform

                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # gen "(Wow! Look at her!)" ("angry", xpos="far_left", ypos="head")
                # gen "That's quite a sexy outfit, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
                # if states.her.level < 11:
                    # her "*Ehm*... Thank you, [name_genie_hermione]." ("soft", "base", "base", "R")
                    # her "I normally don't wear something like this." ("open", "base", "base", "mid")
                    # her @ cheeks blush "(Showing so much cleavage...)" ("disgust", "narrow", "worried", "down")
                    # her "But the weather is just too hot today." ("base", "base", "base", "R")
                    # gen "You should wear this more often!" ("grin", xpos="far_left", ypos="head")
                # else:
                    # her "Thank you, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")

            # else:
                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = "New clothing items for Hermione have been unlocked!", item = hg_muggle_hot_ITEM)


    # if game.weather == "overcast":

        # #One time event.
        # if not hg_accs_wool_g_ITEM.unlocked:
            # $ hg_accs_wool_g_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wear_neckwear    = True
                # $ hermione_wear_gloves      = True
                # $ hermione_wear_stockings   = True
                # $ h_neckwear = "scarf_striped_g"
                # $ h_gloves = "gloves_wool_1"
                # $ h_stockings = "stockings_striped_1"

                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # gen "..." ("base", xpos="far_left", ypos="head")
                # gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                # gen "What's with all these clothes you are wearing?" ("base", xpos="far_left", ypos="head")
                # her @ cheeks blush "It's a bit cold outside, [name_genie_hermione]... and my..." ("soft", "base", "base", "R")

                # if states.her.level < 11:
                    # her @ cheeks blush "I better not mention it..." ("disgust", "narrow", "worried", "down")
                # elif states.her.level < 18:
                    # her @ cheeks blush "{size=-5}People can see my... my nipples...{/size}" ("disgust", "narrow", "worried", "down")
                # else:
                    # her "I can't have my nipples poking out all the time, [name_genie_hermione]! It's distracting!" ("annoyed", "narrow", "angry", "R")

                # her "" ("soft", "base", "base", "mid")
                # pause.2
                # gen "Alright... It looks cute on you." ("base", xpos="far_left", ypos="head")
                # gen "You can keep it on for now." ("base", xpos="far_left", ypos="head")
                # her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")

                # $ h_request_wear_top = True
                # $ h_request_wear_bottom = True
                # $ h_request_wear_neckwear = True
                # $ h_request_wear_gloves = True
                # $ h_request_wear_stockings = True

            # else:
                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = "New clothing items for Hermione have been unlocked!", item = hg_accs_wool_g_ITEM)


    # # Raining
    # if game.weather == "rain":

        # if states.her.tier >= 2 and not hg_muggle_rainy_ITEM.unlocked:
            # $ hg_muggle_rainy_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ hermione_wet_clothes = True
                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ h_top = "top_sweater_1"
                # $ h_bottom = "pants_jeans_long"

                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("disgust", "narrow", "worried", "down", xpos="base", ypos="base")
                # call ctc

                # gen "Damn girl. You look drenched..." ("base", xpos="far_left", ypos="head")
                # her "I'm sorry, [name_genie_hermione], but... It's raining cats and dogs out there!" ("open", "base", "base", "mid")
                # her "I couldn't find my robe so I just put on a sweater and some jeans..." ("open", "base", "base", "R")
                # her "I hope you don't mind my uniform not being up for standards. I didn't want it to get wet." ("disgust", "narrow", "worried", "down")
                # gen "It's fine, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                # gen "Besides, I wouldn't mind seeing you in jeans more often!" ("grin", xpos="far_left", ypos="head")
                # her "Thank you, [name_genie_hermione]." ("normal", "base", "base", "R")
                # $ states.her.mood -= 10
                # if states.her.mood < 0:
                    # $ states.her.mood = 0

            # else:
                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = "New clothing items for Hermione have been unlocked!", item = hg_muggle_rainy_ITEM)

        # # Robe
        # else:

            # $ hermione_wear_robe = True
            # call update_her_uniform
            # play sound "sounds/door.ogg"
            # call her_chibi("stand","mid","base")
            # with d3

            # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
            # if states.her.mood > 1:
                # her "" ("annoyed", "base", "base", "R", xpos="base", ypos="base")
            # else:
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")

            # if not h_request_wear_robe:
                # pause.5 #Shows Hermione with robe for a bit.

    # # Snow
    # if game.weather in ("snow", "blizzard"):

        # if states.her.tier >= 2 and not hg_muggle_cold_ITEM.unlocked:
            # $ hg_muggle_cold_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ h_request_wear_stockings = True
                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings = True
                # $ h_top = "top_pullover_1"
                # $ h_stockings = "stockings_pantyhose"

                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # gen "New outfit?" ("base", xpos="far_left", ypos="head")
                # her "Yes, [name_genie_hermione]. I brought it with me from home. It's a bit too cold for just my normal uniform..." ("open", "base", "base", "R")
                # her "Do you like it?" ("soft", "base", "base", "mid")
                # gen "I do, [name_hermione_genie]. It's cute." ("grin", xpos="far_left", ypos="head")
                # $ states.her.mood -= 10
                # if states.her.mood < 0:
                    # $ states.her.mood = 0

            # else:
                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = "New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_ITEM)

        # elif states.her.tier >= 3 and not hg_muggle_cold_sexy_ITEM.unlocked:
            # $ hg_muggle_cold_sexy_ITEM.unlocked = True

            # if not persistent.game_complete:
                # $ hermione_door_event_happened = True #Hermione won't greet you again.

                # $ h_request_wear_stockings = True

                # $ hermione_wear_neckwear    = False
                # $ hermione_wear_gloves      = False
                # $ hermione_wear_stockings   = True
                # $ h_top = "top_pullover_2"
                # $ h_stockings = "stockings_pantyhose"

                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")
                # call ctc

                # gen "That's quite the cute outfit, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                # her "Thank you, [name_genie_hermione]. I made some changes to the old one..." ("open", "base", "base", "R")
                # her "Do you like it?" ("soft", "base", "base", "mid")
                # gen "Very much so, [name_hermione_genie]. I love the breast window." ("grin", xpos="far_left", ypos="head")
                # $ states.her.mood -= 10
                # if states.her.mood < 0:
                    # $ states.her.mood = 0

            # else:
                # call update_her_uniform
                # play sound "sounds/door.ogg"
                # call her_chibi("stand","mid","base")
                # with d3

                # play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
                # her "" ("base", "base", "base", "mid", xpos="base", ypos="base")

            # #Unlocks rewards.
            # call unlock_clothing(text = "New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_sexy_ITEM)

    if states.her.wardrobe_scheduling:
        $ hermione.equip_random_outfit()

        if not config.developer and not tutorial_is_done("schedule") and states.her.wardrobe_unlocked:
            play sound "sounds/door.ogg"
            call her_chibi("stand","mid","base")
            with d3

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            her "Hello, [name_genie_hermione]." ("open", "base", "base", "R", xpos="base", ypos="base", trans=d3)
            her "" ("base", "base", "base", "mid", xpos="base", ypos="base")
            pause 1.0
            gen "You changed your clothes again..." ("base", xpos="far_left", ypos="head")

            call tutorial("schedule")

            menu:
                "Leave Outfits Scheduling turned {b}ON{/b}?"

                "-Yes-":
                    "Outfits scheduling remains turned {b}ON{/b}."
                "-No-":
                    $ states.her.wardrobe_scheduling = False
                    $ states.ton.wardrobe_scheduling = False
                    $ states.cho.wardrobe_scheduling = False
                    $ states.ast.wardrobe_scheduling = False
                    $ states.lun.wardrobe_scheduling = False
                    # Susan

                    "Outfit scheduling turned {b}Off{/b}."

                    $ hermione.equip(her_outfit_default)
                    with fade

            return

    play sound "sounds/door.ogg"
    call her_chibi("stand","mid","base")
    with d3

    #Hermione greeting.
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    if states.her.mood > 0:
        if 5 > states.her.mood >= 1:
            her "Yes, [name_genie_hermione]?" ("soft", "base", "worried", "mid", xpos="base", ypos="base", trans=d3)
        elif 10 > states.her.mood >= 5:
            her "*sigh*... Yes, [name_genie_hermione]?" ("annoyed", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        elif 20 > states.her.mood >= 10:
            her "What is it, [name_genie_hermione]?" ("open", "closed", "annoyed", "mid", xpos="base", ypos="base", trans=d3)
            her "" ("upset", "base", "annoyed", "mid")
        elif 30 > states.her.mood >= 20:
            her "What do you want, \"[name_genie_hermione]\"?" ("upset", "squint", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 40 > states.her.mood >= 30:
            her "*Hmph*..." ("normal", "squint", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif 50 > states.her.mood >= 40:
            her "*Tsk*" ("angry", "base", "angry", "R", xpos="base", ypos="base", trans=d3)
        elif states.her.mood >= 50:
            her "I have nothing to tell you, sir!" ("mad", "narrow", "angry", "L", xpos="base", ypos="base", trans=d3)

        call describe_mood("Hermione", states.her.mood)
        call tutorial("moodngifts")
    else:
        if game.daytime:
            her "Good morning, [name_genie_hermione]." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
        else:
            her "Good evening, [name_genie_hermione]." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    return
