
label summon_luna:

    $ states.active_girl = "luna"

    $ states.lun.busy = True

    call update_luna
    call update_lun_tier

    $ renpy.checkpoint(hard=True)

    play music "music/wallpaper-by-kevin-macleod.ogg" fadein 1 if_changed
    play sound "sounds/door.ogg"
    call lun_chibi("stand","mid","base")
    with d3

    lun "[name_genie_luna]..." ("base", "base", "base", "mid", xpos="base", ypos="base")

    if states.lun.ev.spectrespecs.e3_complete and not states.lun.ev.spectrespecs.e4_complete:
        jump spectrespecs_E4

    label luna_requests:

    # Reset
    call reset_menu_position
    lun "" (xpos="base",ypos="base")

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.webp"):
            if states.lun.mood > 0:
                lun "I have nothing to say to you sir..."
                jump luna_requests

            call luna_chitchat
            jump luna_talk

        # Personal Favors
        "-Sexual Favours-" (icon="interface/icons/small/condom.webp") if states.lun.favors_unlocked:
            jump luna_favor_menu

        "-Sexual Favours-" (style="disabled") if not states.lun.favors_unlocked:
            nar "You haven't unlocked this feature yet."
            jump luna_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.webp") if states.lun.wardrobe_unlocked:
            hide luna_main with d1
            call wardrobe
            jump luna_requests

        "-Wardrobe-" (style="disabled") if not states.lun.wardrobe_unlocked:
            nar "You haven't unlocked this feature yet."
            jump luna_requests

        "-Give Item-" (icon="interface/icons/small/gift.webp"):
            $ TBA_message()
            jump luna_requests

            # hide luna_main with d1
            # call gift_menu
            # jump luna_requests

        # Dismiss
        "-Dismiss her-":
            stop music fadeout 3.0

            if game.daytime:
                if states.lun.mood >= 3:
                    lun "Good day..."
                else:
                    lun "Sure thing, [name_genie_luna]. I will head to class."
            else:
                if states.lun.mood >= 3:
                    lun "Good night..."
                else:
                    lun "Sure thing, good night [name_genie_luna]."

            jump end_luna_event

label update_lun_tier:
    if states.lun.tier == 1 and states.lun.level >= 3:
        if not states.lun.ev.talk_to_me.t1_e3_complete:
            return

        $ lun_level_up = 1
    elif states.lun.tier == 2 and states.lun.level >= 6:
        if not states.lun.ev.inspect_her_body.t2_e3_complete:
            return

        $ lun_level_up = 2
    elif states.lun.tier == 3 and states.lun.level >= 9:
        if not states.lun.ev.play_with_yourself.t3_e3_complete:
            return

        $ lun_level_up = 3
    elif states.lun.tier == 4 and states.lun.level >= 13:
        # T5 NOT AVAILABLE
        return

        # Requirement: Tier 4 - Blow me T4 E3
        $ lun_level_up = 4
    return

label luna_level_up(tier=None):

    if tier == 1:
        gen "(I think it's about time to give her a proper inspection...)" ("base", xpos="far_left", ypos="head")
    elif tier == 2:
        gen "(Let's see if she's ready for some self-care...)" ("base", xpos="far_left", ypos="head")
    elif tier == 3:
        gen "(I wonder if she'll be able to get the spurts out with her mouth...)" ("base", xpos="far_left", ypos="head")
    elif tier == 4:
        gen "(Getting the spurts out of two people at the same time...)" ("base", xpos="far_left", ypos="head")
        gen "(Now that's going to require some careful timing!)" ("grin", xpos="far_left", ypos="head")

    $ states.lun.tier = tier+1
    $ lun_level_up = None
    $ states.lun.mood = 0

    pause.5
    nar "Luna has reached {i}favour tier{/i} [states.lun.tier]!"

    call update_lun_tier

    return

# Luna Favor Menu
label luna_favor_menu:
    menu:
        "-Level Up-" (icon="interface/icons/small/levelup.webp") if lun_level_up != None:
                call luna_level_up(tier=lun_level_up)
                jump luna_favor_menu

        "-Personal Favours-" (icon="interface/icons/small/heart_red.webp"):
            call tutorial("hearts")

            label .personal:

            $ result = show_events_menu(luna_favors)

            if result in ("disabled", "noncompliant"):
                "You haven't unlocked this favour opportunity yet."
                jump .personal
            elif result == "exit":
                jump luna_favor_menu
            else:
                $ result.start()

        "-Public Requests-" (icon="interface/icons/small/star_yellow.webp", style="disabled"):
            label .requests:

            call not_available
            
            # $ result = show_events_menu(hermione_requests)

            # if result in ("disabled", "noncompliant"):
            #     "You haven't unlocked this request opportunity yet."
            #     jump .requests
            # elif result == "exit":
            #     jump .skip_points_check
            # else:
            #     $ result.start()

            jump luna_favor_menu

        "-Never mind-":
            jump luna_requests

label luna_talk:
    # General.
    menu:
        "-Ask her to cheer for Ravenclaw-" if states.cho.ev.quidditch.gryffindor_failed and not states.cho.ev.quidditch.e11_complete:
            jump cho_quid_E11

        "-Address me only as-" if states.lun.ev.spectrespecs.e4_complete:
            menu:
                "-Sir-":
                    $ name_genie_luna = "Sir"
                "-Dumbledore-":
                    $ name_genie_luna = "Dumbledore"
                "-Professor-":
                    $ name_genie_luna = "Professor"
                "-Partner-":
                    $ name_genie_luna = "Partner"
                "-Master-" if states.lun.tier >= 2:
                    $ name_genie_luna = "Master"
                "-Daddy-" if states.lun.tier >= 2:
                    $ name_genie_luna = "Daddy"
                "-Custom Input-" if states.lun.tier >= 3:
                    $ name_genie_luna = renpy.input("(Please enter the name.)", name_genie_luna, ALLOWED_CHARACTERS, length=14).strip() or "Professor"
                "-Never mind-":
                    jump luna_talk

            jump genie_luna_change

        "-From now on, I will refer to you as-" if states.lun.ev.spectrespecs.e4_complete:
            menu:
                "-Miss Lovegood-":
                    $ name_luna_genie = "Miss Lovegood"
                "-Luna-":
                    $ name_luna_genie = "Luna"
                "-Loony-":
                    $ name_luna_genie = "Loony"
                "-Girl-":
                    $ name_luna_genie = "Girl"
                "-Partner-":
                    $ name_luna_genie = "Partner"
                "-Bimbo-" if states.lun.tier >= 2:
                    $ name_luna_genie = "Bimbo"
                "-Minx-" if states.lun.tier >= 3:
                    $ name_luna_genie = "Minx"
                "-Cumslut-" if states.lun.tier >= 5:
                    $ name_luna_genie = "Cumslut"
                "-Custom Input-" if states.lun.tier >= 3:
                    $ name_luna_genie = renpy.input("(Please enter the name.)", name_luna_genie, ALLOWED_CHARACTERS, length=14).strip() or "Miss Lovegood"
                "-Never mind-":
                    jump luna_talk

            jump name_luna_genie

        "-Never mind-":
            jump luna_requests

label genie_luna_change:
    # NickName responses
    if name_genie_luna == "Sir":
        lun "Certainly, [name_genie_luna]." ("base", "base", "base", "mid")
    elif name_genie_luna == "Dumbledore":
        lun "You want me to call you by your last name?" ("annoyed", "narrow", "base", "mid")
        gen "Is that going to be a problem?" ("base", xpos="far_left", ypos="head")
        lun "Of course not [name_genie_luna]..." ("angry", "base", "base", "mid")
        lun "[name_genie_luna]..." ("angry", "base", "base", "downL")
        lun "Don't think I've ever heard anyone call you just [name_genie_luna] before..." ("grin", "base", "base", "mid")
    elif name_genie_luna == "Professor":
        lun "Yes, [name_genie_luna]." ("base", "base", "base", "mid")
    elif name_genie_luna == "Partner":
        lun "[name_genie_luna]?" ("soft", "base", "raised", "mid")
        gen "Yes, we're working together now, so it's only appropriate." ("base", xpos="far_left", ypos="head")
        lun "Oh... Of course [name_genie_luna]." ("grin", "base", "base", "mid")
    elif name_genie_luna == "Master":
        lun "[name_genie_luna]?" ("soft", "narrow", "base", "mid")
        lun "What are you a [name_genie_luna] of exactly?" ("angry", "base", "base", "mid")
        if states.lun.tier >= 3:
            gen "A master baiter!" ("grin", xpos="far_left", ypos="head")
            lun "Oh, right!" ("smile", "base", "base", "mid")
            lun "Thank you for allowing me to be your pupil, [name_genie_luna]." ("base", "base", "base", "mid")
        else:
            gen "*Err*...{w=0.4} Of the arts?" ("base", xpos="far_left", ypos="head")
            lun "What arts?" ("angry", "narrow", "base", "mid")
            gen "Avoiding confrontation." ("base", xpos="far_left", ypos="head")
            lun "*Huh*?" ("mad", "base", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            lun "..." ("annoyed", "base", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            lun "Sir?" ("soft", "narrow", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            lun "[name_genie_luna]?" ("open", "base", "base", "mid")
            gen "That's me." ("base", xpos="far_left", ypos="head")
            lun "Okay, I'll call you [name_genie_luna] from now on." ("soft", "base", "base", "mid")
            gen "(Another confrontation expertly avoided...)" ("base", xpos="far_left", ypos="head")
    elif name_genie_luna == "Daddy":
        lun "[name_genie_luna]?" ("open", "narrow", "base", "mid")
        gen "Yes..." ("base", xpos="far_left", ypos="head")
        lun "But won't that be confusing?" ("annoyed", "narrow", "base", "mid")
        gen "Would it?" ("base", xpos="far_left", ypos="head")
        lun "Yes, that's usually what I call my father..." ("open", "base", "base", "R")
        gen "I'm your daddy now..." ("base", xpos="far_left", ypos="head")
        lun "*Huh*?" ("angry", "base", "base", "mid")
        gen "Call me daddy you naughty girl!" ("angry", xpos="far_left", ypos="head")
        lun "Oh...{w=0.3} Yes, I'm sorry [name_genie_luna]!" ("angry", "happyCl", "base", "mid")
    else: #custom/fallback
        lun "Okay, I'll call you [name_genie_luna] from now on..." ("base", "base", "base", "mid")
    jump luna_talk

label name_luna_genie:
    # NickName responses
    if name_luna_genie == "Miss Lovegood":
        lun "Of course, [name_genie_luna]." ("base", "wink", "base", "mid")
    elif name_luna_genie == "Luna":
        lun "But that's my first name!" ("angry", "base", "base", "mid")
        gen "So?" ("base", xpos="far_left", ypos="head")
        lun "Isn't it against the law?" ("mad", "narrow", "base", "mid")
        gen "... Is what against the law?" ("base", xpos="far_left", ypos="head")
        lun "Teachers and students referring to each other by their first name. I read an article about it in the quibbler." ("angry", "narrow", "raised", "mid")
        gen "*Err*... No, they recently made it legal." ("base", xpos="far_left", ypos="head")
        lun "Oh, How progressive!" ("soft", "base", "base", "stare")
        lun "In that case, you can call me that!" ("smile", "base", "base", "mid")
    elif name_luna_genie == "Loony":
        lun "Do you really need to call me that, [name_genie_luna]?" ("upset", "base", "base", "mid")
        lun "Other students call me that to make fun of me." ("upset", "base", "base", "R")
        gen "I like it." ("grin", xpos="far_left", ypos="head")
        lun "Alright then..." ("annoyed", "base", "base", "mid")
    elif name_luna_genie == "Girl":
        lun "Just [name_luna_genie]?" ("soft", "base", "raised", "mid")
        gen "Yep." ("base", xpos="far_left", ypos="head")
        lun "Alright, I suppose I am a girl after all." ("grin", "narrow", "base", "mid")
    elif name_luna_genie == "Partner":
        lun "[name_luna_genie]?" ("soft", "base", "base", "mid")
        gen "Yes, we're partners in this venture, are we not?" ("base", xpos="far_left", ypos="head")
        lun "Oh right!" ("angry", "base", "base", "mid")
        lun "Of course, you can call me that!" ("grin", "base", "base", "mid")
    elif name_luna_genie == "Bimbo":
        lun "A what?" ("soft", "base", "base", "mid")
        gen "A Bimbo..." ("base", xpos="far_left", ypos="head")
        lun "Oh... Okay..." ("base", "base", "base", "mid")
        gen "(...{w} Maybe she doesn't know what that means...)" ("base", xpos="far_left", ypos="head")
    elif name_luna_genie == "Minx":
        lun "A mink?" ("soft", "base", "base", "mid")
        gen "No, a--" ("base", xpos="far_left", ypos="head")
        lun "I love minks!" ("smile", "wide", "base", "mid")
        gen "...{w=0.3} Great." ("base", xpos="far_left", ypos="head")
    elif name_luna_genie == "Cumslut":
        lun "Well I do love helping you cum..." ("grin", "narrow", "base", "downL")
        lun "Sure, you can call me that." ("grin", "base", "base", "mid")
    else: #Custom/fallback
        lun "Sure, you can call me that!" ("base", "base", "base", "mid")

    jump luna_talk
