

label summon_hermione:
    #play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    #play sound "sounds/door.ogg"

    $ states.active_girl = "hermione"

    $ states.her.busy = True

    call update_hermione
    call update_her_tier

    $ renpy.checkpoint(hard=True)

    # Clothes Events
    call hermione_summon_setup

    label hermione_requests:

    # Reset
    call reset_menu_position
    her "" (xpos="base",ypos="base")

    menu:
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if states.her.mood > 0:
                her "I have nothing to say to you sir..."
                jump hermione_requests

            call hermione_chitchat
            jump hermione_talk

        "-Tutoring-" (icon="interface/icons/small/book.webp") if not game.daytime and states.her.ev.tutoring.stage < 15: #14 is last level.
            if states.her.mood >=1 and states.her.mood < 3:
                her "I'm sorry, maybe tomorrow..."
                jump hermione_requests
            elif states.her.mood >=3 and states.her.mood < 10:
                her "I am not in the mood today..."
                jump hermione_requests
            elif states.her.mood >= 10 and states.her.mood < 20:
                her "Absolutely not, [name_genie_hermione]."
                her "I {i}might{/i} consider it once you've said sorry..."
                jump hermione_requests
            elif states.her.mood >=20:
                her "After what you did, [name_genie_hermione]?"
                her "I don't think so..."
                jump hermione_requests
            else:
                jump hg_tutor_start

        "-Tutoring-" (icon="interface/icons/small/book.webp", style="disabled") if game.daytime and states.her.ev.tutoring.stage < 15:
            nar "Tutoring is available during the night only."
            jump hermione_requests

        "-Sexual favours-" (icon="interface/icons/small/condom.webp") if states.her.favors_unlocked:
            if states.her.mood >=1 and states.her.mood < 3:
                her "I'm sorry, [name_genie_hermione]... Maybe some other time." ("annoyed", "base", "base", "R")
                jump hermione_requests
            elif states.her.mood >=  3 and states.her.mood < 10:
                her "I don't feel like it today..." ("open", "closed", "base", "mid")
                her "Maybe some other time..." ("normal", "closed", "base", "mid")
                her "" ("normal", "base", "base", "mid")
                jump hermione_requests
            elif states.her.mood >= 10 and states.her.mood < 20:
                her "No thank you..." ("angry", "narrow", "base", "mid")
                jump hermione_requests
            elif states.her.mood >= 20 and states.her.mood < 30:
                her "After what you did, [name_genie_hermione]?" ("angry", "narrow", "annoyed", "mid")
                her "I don't think so..." ("disgust", "narrow", "annoyed", "mid")
                jump hermione_requests
            elif states.her.mood >= 30 and states.her.mood < 40:
                her "You can't be serious!" ("angry", "narrow", "angry", "mid")
                jump hermione_requests
            elif states.her.mood >= 40:
                her "Is this some twisted joke to you, sir?!" ("angry", "squint", "angry", "mid")
                her "After what you did I don't feel like doing this ever again!" ("disgust", "base", "angry", "mid")
                jump hermione_requests
            else:
                jump hermione_favor_menu

        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if states.her.wardrobe_unlocked: # Unlocks after first summoning her.
            hide hermione_main with d1
            call wardrobe
            jump hermione_requests

        "-Let's Duel-" (icon="interface/icons/small/cards.webp") if states.sna.ev.cardgame.stage >= 2:
            jump hermione_cardgame_menu

        "-Give Item-" (icon="interface/icons/small/gift.webp") if states.her.favors_unlocked:
            hide hermione_main with d1
            call gift_menu
            jump hermione_requests

        "-Dismiss her-":
            stop music fadeout 3.0

            if game.daytime:
                if states.her.mood >=3 and states.her.mood < 7:
                    her "..............................."
                elif states.her.mood >=7:
                    her "*Humph*!..."
                else:
                    her "Oh, alright. I will go to classes then."
            else:
                if states.her.mood >=3 and states.her.mood < 7:
                    her "..............................."
                elif states.her.mood >=7:
                    her "*Tch*..."
                else:
                    her "Oh, alright. I will go to bed then."

            play sound "sounds/door.ogg"

            jump end_hermione_event

label hermione_level_up(tier=None):

    if tier == 1:
        menu:
            "Would you like to increase Hermione's {i}favour tier{/i} now?"
            "-Yes, increase her tier-":
                pass
            "-No, stay on her current tier-":
                return

    elif tier == 2:
        gen "(I wonder if she's ready for some more advanced favours now...)" ("base", xpos="far_left", ypos="head")
    elif tier == 3:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        gen "(Would she know what a handjob is...?)" ("base", xpos="far_left", ypos="head")
    elif tier == 4:
        gen "(I wonder if I can get her to suck me off today...)" ("base", xpos="far_left", ypos="head")
        gen "(I'm dying to feel that mouth around my cock!)" ("angry", xpos="far_left", ypos="head")
    elif tier == 5:
        gen "(Yes, I think it's time...)" ("base", xpos="far_left", ypos="head")
        gen "(I'm gonna put my \"P\" in her \"V\"!)" ("grin", xpos="far_left", ypos="head")

    $ states.her.tier = tier+1
    $ her_level_up = None
    $ states.her.mood = 0

    pause.5
    nar "Hermione has reached {i}favour tier{/i} [states.her.tier]!"

    call update_her_tier

    return

label hermione_favor_menu:

    if not is_in_lead(gryffindor):

        label .skip_points_check:

        if her_level_up != None:
            call tutorial("milestones")

        menu:
            "-Level Up-" (icon="interface/icons/small/levelup.webp") if her_level_up != None:
                call hermione_level_up(tier=her_level_up)
                jump hermione_favor_menu

            "-Personal favours-" (icon="interface/icons/small/heart_red.webp"):
                label .favors:

                call tutorial("hearts")

                $ result = show_events_menu(hermione_favors)

                if result in ("disabled", "noncompliant"):
                    "You haven't unlocked this favour opportunity yet."
                    jump .favors
                elif result == "exit":
                    jump .skip_points_check
                else:
                    $ result.start()

            "-Public requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled") if not game.daytime:
                nar "Public requests are available during the day only."
                jump .skip_points_check

            "-Public requests-" (icon="interface/icons/small/star_yellow.webp") if game.daytime:
                label .requests:

                if states.her.public_level >= 16 and not "public" in states.her.ev.yule_ball.variant:
                    # Public whore ending choice
                    $ renpy.choice_for_skipping()
                    $ renpy.music.set_volume(0.5, 1.0)
                    nar "Attention!{w=1.0} If you continue tarnishing Hermione's reputation, you will lock yourself towards a certain game ending. (Public route)"
                    menu:
                        nar "Do you wish to continue?\n{size=-4}(You won't be asked again){/size}"
                        "Yes, I do.":
                            $ renpy.music.set_volume(1.0, 1.0)
                            $ states.her.ev.yule_ball.variant = "public"
                        "No, go back.":
                            $ renpy.music.set_volume(1.0, 1.0)
                            jump .skip_points_check

                $ result = show_events_menu(hermione_requests)

                if result in ("disabled", "noncompliant"):
                    "You haven't unlocked this request opportunity yet."
                    jump .requests
                elif result == "exit":
                    jump .skip_points_check
                else:
                    $ result.start()

            "-Odd Jobs-" (icon="interface/icons/small/gold.webp") if game.daytime:
                label .odd_jobs:

                $ result = show_events_menu(hermione_jobs, report_progress=False)

                if result in ("disabled", "noncompliant"):
                    "You haven't unlocked this job opportunity yet."
                    jump .odd_jobs
                elif result == "exit":
                    jump .skip_points_check
                else:
                    $ result.start()

            "-Odd Jobs-" (icon="interface/icons/small/gold.webp", style="disabled") if not game.daytime:
                nar "Public requests are available during the day only."
                jump .skip_points_check

            "-Never mind-":
                jump hermione_requests
    else:
        if states.her.favors_convinced_stage:
            her "We're in the lead already..." ("base", "base", "base", "mid_soft", trans=d3)
            if states.her.level >=22 and states.her.favors_convinced_stage == 2:
                random:
                    her "But I'll do anything for you, [name_genie_hermione]..." ("smile", "happy", "base", "mid")
                    her "But if you really need it, I may as well..." ("smile", "happy", "base", "mid")
                    her "But I'll do it anyway..." ("smile", "happy", "base", "mid")
                jump .skip_points_check
            elif states.her.level >=20 and states.her.favors_convinced_stage == 2:
                random:
                    her "But an even bigger lead wouldn't hurt, I suppose..." ("base", "happy", "base", "mid")
                    her "But since you've been helping me earn points for my house, I'll do it anyway..." ("base", "happy", "base", "mid")
                    her "But since I'm already here, I might as well do it..." ("base", "happy", "base", "mid")
                jump .skip_points_check
            elif states.her.level >=18 and states.her.favors_convinced_stage == 2:
                random:
                    her "Although, considering what you said before... I'll do it anyway." ("soft", "wink", "base", "mid")
                    her "Although, I suppose another house may catch up... Okay, I'll do it." ("soft", "wink", "base", "mid")
                    her "Although, an ever bigger lead would really show the Slytherins which house is the best." ("base", "wink", "base", "mid")
                jump .skip_points_check
            elif states.her.level >=16:
                her "I have told you before, [name_genie_hermione], it was just a one time thing..." ("open", "happy", "base", "mid")
                gen "What about tomorrow though?" ("base", xpos="far_left", ypos="head")
                her "What about tomorrow?" ("base","squint", "base", "mid")
                gen "I made a graph detailing the current daily average points Slytherin gain... It doesn't look that great." ("grin", xpos="far_left", ypos="head")
                gen "Just think about it." ("base", xpos="far_left", ypos="head")
                jump .convinced
        else:
            her "The Gryffindor house is in the lead. I don't need to do this." ("base", "base", "base", "mid_soft", trans=d3)
            if states.her.level >= 15:
                menu:
                    "-Change her mind-":
                        gen "Are you sure it's not within your house best interests?" ("base", xpos="far_left", ypos="head")
                        her "What do you mean?" ("soft", "happy", "base", "mid")
                        gen "Think about the future..." ("grin", xpos="far_left", ypos="head")
                        
                        label .convinced:

                        if states.her.level >=20:
                            gen "If you do it now it could secure--" ("base", xpos="far_left", ypos="head")
                            her "I'll do it!" ("angry", "happy", "base", "mid")
                            gen "Just like that?!" ("base", xpos="far_left", ypos="head")
                            her "Yes... Just like that." ("base", "closed", "base", "mid")
                            gen "That's my girl!" ("grin", xpos="far_left", ypos="head")
                            $ states.her.favors_convinced_stage = 2
                            jump .skip_points_check

                        gen "If you do it, you could secure the win for your house you know..." ("base", xpos="far_left", ypos="head")

                        if states.her.level >=18:
                            her "You really know how to talk me through, [name_genie_hermione]." ("soft", "narrow", "worried", "down")
                            her "Okay I agree." ("open", "narrow", "base", "down")
                            $ states.her.favors_convinced_stage = 2
                            jump .skip_points_check
                        elif states.her.level >=16 and not states.her.favors_convinced_stage == 1:
                            her "I guess you're right..." ("open", "happy", "base", "mid_soft")
                            her "I'll do it... But just this once okay?" ("grin", "happyCl", "base", "mid")
                            $ states.her.favors_convinced_stage = 1
                            jump .skip_points_check
                        else:
                            her "I could..." ("soft", "narrow", "base", "mid_soft")
                            her "But I don't want to." ("normal", "closed", "base", "mid")
                            jump hermione_requests
                    "-Forget it-":
                        pass
            else:
                if states.sna.level <= 10:
                    gen "What do you mean \"in the lead\"?" ("base", xpos="far_left", ypos="head")
                    gen "Explain yourself, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
                    her "With the current points distribution, I am certain getting the house cup for Gryffindor will be just a formality." ("smile", "closed", "base", "mid")
                    her "Thank you, [name_genie_hermione], but I don't need any more points." ("smile", "base", "base", "mid")

                    call tutorial("points")

                    gen "(That little...)" ("angry", xpos="far_left", ypos="head")
                    gen "(Perhaps I should hangout with that Snape dude tonight, he might know what to do.)" ("base", xpos="far_left", ypos="head")
                    her "Do you need anything else, [name_genie_hermione]?" ("smile", "base", "base", "mid")
                else:
                    gen "Right..." ("base", xpos="far_left", ypos="head")

                    call tutorial("points")

                    gen "(I guess another hangout with Snape is in order.)" ("base", xpos="far_left", ypos="head")
        jump hermione_requests

label update_her_tier:
    python:
        if states.her.tier == 1 and states.her.level >= 3:
            # Trigger: None
            her_level_up = 1
        elif states.her.tier == 2 and states.her.level >= 9 and states.her.status.voyer == True:
            # Trigger: Caught/saw Genie masturbate for the first time.
            her_level_up = 2
        elif states.her.tier == 3 and states.her.level >= 12 and states.her.status.stripping == True:
            # Trigger: After she has stripped completely for Genie.
            her_level_up = 3
        elif states.her.tier == 4 and states.her.level >= 18 and states.her.ev.give_me_a_handy.cock_kiss == True:
            # Trigger: Kissed Genie's dick during HJ favour.
            her_level_up = 4
        elif states.her.tier == 5 and states.her.level >= 21 and states.her.status.blowjob == True:
            # Trigger: First BJ
            her_level_up = 5

    return
