
### Hermione Admire Breasts ###

label start_hg_pf_admire_breasts:

    if not _events_completed_any:
        gen "{size=-4}(I feel like gazing upon those titties.){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 10
    return

label end_hg_pf_admire_breasts:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    $ hermione.set_cum(None)
    $ hermione.wear("all")

    hide screen blkfade
    if states.her.tier <= 2:
        her ".................." ("annoyed", "base", "worried", "R", xpos="mid", ypos="base", trans=fade)
    elif states.her.tier <= 3:
        her "" ("annoyed", "base", "worried", "R", xpos="mid", ypos="base", trans=fade)
    elif states.her.tier <= 5:
        her "" ("soft", "base", "base", "R", xpos="mid", ypos="base", trans=fade)
    else:
        her "" ("base", "narrow", "annoyed", "up", xpos="mid", ypos="base", trans=fade)

    # Points
    $ gryffindor += current_payout
    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    stop music fadeout 10.0

    if states.her.tier <= 2:
        her ".................." ("annoyed", "base", "worried", "R")
        her "Thank you, [name_genie_hermione]..." ("open", "base", "base", "R")
    elif states.her.tier <= 5:
        her ".................." ("annoyed", "base", "worried", "R")
        her "Thank you, [name_genie_hermione]..." ("soft", "base", "base", "mid")
    else:
        her ".................." ("base", "happyCl", "base", "mid")
        her "Thank you, [name_genie_hermione]..." ("soft", "narrow", "base", "mid_soft")

    if game.daytime:
        her "Now if you don't mind, I'd better go... My classes are about to start."
    else:
        her "I'd better head off for today, It's getting pretty late..."

    # Hermione leaves
    call her_walk("door", "base")

    if states.her.tier <= 1 and not _events_filtered_completed_any:
        her @ cheeks blush "........................" ("disgust", "narrow", "base", "down", xpos="far_right", flip=True, trans=d3)
    elif states.her.tier <= 2 and not _events_filtered_completed_any:
        her @ cheeks blush "(How humiliating... What have I become...?)" ("disgust", "narrow", "base", "down", xpos="far_right", flip=True, trans=d3)
    elif states.her.tier <= 2 and not _event_completed:
        her @ cheeks blush "........................" ("disgust", "narrow", "base", "down", xpos="far_right", flip=True, trans=d3)
    elif states.her.tier <= 3 and not _events_filtered_completed_any:
        if not _cumming:
            her @ cheeks blush "{size=-5}(That was so humiliating...){/size}" ("base", "narrow", "base", "up", xpos="far_right", flip=True, trans=d3)
            her @ cheeks blush "{size=-5}(No, Hermione, you silly girl!){/size}" ("angry", "base", "angry", "mid")
            her @ cheeks blush "{size=-5}(We are doing this to protect the honour of our house!){/size}" ("angry", "base", "angry", "mid")
            her @ cheeks blush "................................." ("base", "narrow", "base", "up")
        else:
            her @ cheeks blush "{size=-5}(To think that I have to humiliate myself like this, just to have a chance at winning the cup...){/size}" ("angry", "narrow", "angry", "down")
            her @ cheeks blush "{size=-5}(Maybe this is going too far...){/size}" ("disgust", "narrow", "worried", "down")
            her @ cheeks blush "{size=-5}(No, Hermione, you must protect the honour of our house!){/size}" ("angry", "base", "angry", "mid")

    call her_chibi("leave")


    # Increase level
    if states.her.tier == 1:
        if states.her.level < 3: # Points til 3
            $ states.her.level += 1

    elif states.her.tier == 2:
        if states.her.level < 9: # Points til 9
            $ states.her.level += 1

    jump end_hermione_event



### Tier 1 ###

# Her Bra will stay on for this tier.
# Event 1 (i) - Hermione will remove her vest.
# Event 2 (i) - Hermione will lift up her top.
# Event 3 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T1_intro_E1:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..." ("normal", "base", "base", "mid")
    gen "Has anyone ever told you what sweet-looking breasts you have?" ("base", xpos="far_left", ypos="head")
    stop music fadeout 1.0
    her "!!!" ("shock", "wide", "base", "stare")
    gen "How much would it cost me for you to lift up your top?" ("grin", xpos="far_left", ypos="head")
    her "My top?!" ("shock", "wide", "base", "stare")
    gen "And show me what's underneath..." ("grin", xpos="far_left", ypos="head")
    her "Why would I--?!" ("angry", "wide", "base", "mid")

    her "[name_genie_hermione], I refuse to bare my breasts for you!" ("open", "closed", "angry", "mid")
    her "How could you even suggest such a thing?!" ("angry", "base", "angry", "mid")
    gen "Don't you want to earn some house points?" ("base", xpos="far_left", ypos="head")
    her "Yes... But not in a way such as this!" ("angry", "narrow", "angry", "R")

    gen "I will award Gryffindor {number=current_payout} whole house points if you remove your top." ("base", xpos="far_left", ypos="head")
    gen "Isn't that a steal?" ("grin", xpos="far_left", ypos="head")
    her "No it isn't!" ("clench", "closed", "angry", "mid", emote="angry")
    gen "Please?" ("base", xpos="far_left", ypos="head")
    if hermione.is_worn("bra"):
        gen "You can keep your bra on for all I care..." ("base", xpos="far_left", ypos="head")
    her "Three seconds! Not even a second longer!" ("angry", "base", "angry", "mid")
    gen "How about fi--" ("base", xpos="far_left", ypos="head")
    her "{size=+4}Not even a second longer!{/size}" ("scream", "narrow", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    menu:
        "\"Very well, [name_hermione_genie].\"":
            gen "Better than nothing I guess..." ("base", xpos="far_left", ypos="head")
            pass

        "\"That won't be enough, [name_hermione_genie]...\"":
            gen "I'm not giving Gryffindor {number=current_payout} whole points for a mere glimpse..." ("angry", xpos="far_left", ypos="head")
            her "But--" ("open", "wide", "base", "stare")
            gen "No buts! You are dismissed." ("base", xpos="far_left", ypos="head")
            her "Please, [name_genie_hermione]. I need those points!" ("disgust", "happyCl", "worried", "mid")
            gen "Then might I suggest you put in some work to earn them..." ("base", xpos="far_left", ypos="head")
            her "(................)" ("annoyed", "narrow", "angry", "R")
            gen "Have a nice day, Miss Granger." ("base", xpos="far_left", ypos="head")
            her "(................)" ("annoyed", "base", "angry", "mid")
            her "Fine! I'm leaving..." ("open", "closed", "angry", "mid")
            her "Good day, Sir." ("angry", "base", "angry", "mid")

            call her_walk(action="leave")

            $ states.her.mood += 3

            gen "(Well... Next time, I guess.)" ("base", xpos="far_left", ypos="head")

            # Event resets. (No progress)
            $ _event.cancel()
            jump end_hermione_event

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "(................)" ("annoyed", "narrow", "angry", "R")

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")
        call ctc


    play sound "sounds/cloth_sound3.ogg"
    $ hermione.strip("top")
    her "" ("annoyed", "narrow", "angry", "R")
    call ctc

    gen "*Hmmmmm*" ("base", xpos="far_left", ypos="head")
    gen "..........." ("base", xpos="far_left", ypos="head")
    her "Sir?" ("clench", "base", "angry", "mid")
    gen "(I wonder what cup size those are.)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/cloth_sound3.ogg"
    $ hermione.wear("top")
    with d3
    pause .5

    her "Sir, I would like to have my points now." ("open", "closed", "angry", "mid")
    gen "What? Oh, yes... Of course." ("base", xpos="far_left", ypos="head")

    call hide_characters
    show screen blkfade
    with d3

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T1_intro_E2:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie], Is it just me?" ("base", xpos="far_left", ypos="head")
    gen "Or is it getting really hot in here?!" ("grin", xpos="far_left", ypos="head")
    her "Sir...?" ("open", "wink", "base", "mid")
    gen "Take off your top for me, would you..." ("base", xpos="far_left", ypos="head")
    her "(...............)" ("annoyed", "base", "angry", "mid")
    her "Sir, this is a very inappropriate thing to ask of me!!!" ("scream", "closed", "angry", "mid")
    gen "Yeah, yeah... What else is new..." ("base", xpos="far_left", ypos="head")
    her "Sir!!!" ("clench", "wide", "base", "stare")
    gen "Please. All I'm asking for is to get a little peek..." ("base", xpos="far_left", ypos="head")
    her "A peek at what?" ("open", "base", "angry", "mid")

    menu:
        "\"Your bra!\"":
            gen "It looked really cute..." ("grin", xpos="far_left", ypos="head")
            her "(......................)" ("clench", "closed", "angry", "mid")
            her "You get three seconds like the last time, alright?" ("open", "closed", "base", "mid")
            gen "No, no, no, Miss Granger." ("base", xpos="far_left", ypos="head")
            gen "As you've already pointed out..." ("base", xpos="far_left", ypos="head")
            her "" ("angry", "base", "worried", "mid")
            gen "That was last time!" ("grin", xpos="far_left", ypos="head")
            gen "Now if you would like those points I suggest you remove that top of yours..." ("base", xpos="far_left", ypos="head")
            her "How many points did you say I'd get for this?" ("open", "base", "angry", "mid")
            gen "{number=current_payout} points." ("base", xpos="far_left", ypos="head")
            her "(.............................)" ("annoyed", "base", "angry", "mid")
            gen "And I expect you to do it today, if you don't mind. I have... *Err*..." ("base", xpos="far_left", ypos="head")
            gen "I have other things to take care off." ("base", xpos="far_left", ypos="head")
            her "Very well, Sir..." ("open", "base", "angry", "mid")
            her "I'll do it." ("annoyed", "base", "angry", "mid")

            pass

        "\"Your tits!\"":
            her "W-what?" ("shock", "wide", "base", "stare")
            gen "Your breasts, Miss Granger. I would very much like to see them!" ("grin", xpos="far_left", ypos="head")
            her "M-My--... my breasts?!" ("angry", "base", "angry", "mid")

            # Hermione gets angry
            her "*Tztzzz*!..." ("angry", "closed", "angry", "mid", emote="angry")

            her "Good day, Sir." ("scream", "base", "angry", "mid")

            call her_walk(action="leave")

            $ states.her.mood += 6

            gen "Bummer..." ("base", xpos="far_left", ypos="head")

            # Event resets. (No progress)
            $ _event.cancel()
            jump end_hermione_event

    call hg_pf_admire_breasts_T1

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T1_E2:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie], how would you like to lift up your top for me?" ("base", xpos="far_left", ypos="head")
    her "Will I be getting points for this, Sir?" ("annoyed", "base", "angry", "mid")
    gen "Of course. {number=current_payout} points, as always." ("grin", xpos="far_left", ypos="head")
    her "(...............)" ("annoyed", "base", "angry", "mid")
    her "Very well then." ("angry", "base", "angry", "mid")

    call hg_pf_admire_breasts_T1

    jump end_hg_pf_admire_breasts



label hg_pf_admire_breasts_T1: # Call label

    $ states.her.status.show_bra = True

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "............." ("annoyed", "base", "worried", "R")

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")
        call ctc


    play sound "sounds/cloth_sound3.ogg"
    $ hermione.strip("top")
    her "" ("annoyed", "base", "worried", "R")
    call ctc

    gen "............." ("base", xpos="far_left", ypos="head")
    gen "Very good, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Can I get my points then?" ("disgust", "happyCl", "worried", "mid")
    gen "Of course..." ("base", xpos="far_left", ypos="head")

    return



### Tier 2 ###

# Hermione will bare her breasts after some convincing.
# Event 1 (i) - Choice: Pay Hermione more points take off top and bra.
# Event 2 (i) - Hermione will lift up her top.
# Event 3 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T2_intro_E1:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..." ("normal", "base", "base", "mid")
    gen "How much will it cost me to see your tits?" ("base", xpos="far_left", ypos="head")

    stop music fadeout 1.0
    if not states.her.ev.admire_breasts.T2_intro_E1_failed:
        her "How much will it cost you to...?" ("open", "base", "base", "mid")

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
        her "[name_genie_hermione]!" ("scream", "closed", "angry", "mid")
        gen "*Hmm*... I thought your house could use some extra points..." ("base", xpos="far_left", ypos="head")
        gen "But I guess I was wrong..." ("base", xpos="far_left", ypos="head")
        her ".........?" ("open", "base", "base", "mid")
        gen "Please don't mind me..." ("base", xpos="far_left", ypos="head")
        gen "All I want to do is help you..." ("base", xpos="far_left", ypos="head")
        her "............." ("annoyed", "base", "worried", "R")
        her "Two hundred house points, [name_genie_hermione]." ("normal", "happyCl", "worried", "mid")
        gen "So if I give you two hundred house points, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "You will shamelessly bare your melons before me?" ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]! No need to be so vulgar!" ("angry", "base", "angry", "mid")
    else:
        her "How much..." ("open", "base", "base", "mid")

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
        her "This again?!" ("angry", "base", "angry", "mid")
        gen "Just asking..." ("base", xpos="far_left", ypos="head")
        her "I already told you... Two hundred points..." ("angry", "narrow", "worried", "mid")
        gen "*Hmm*... That's a lot, just to have you show me your tits, don't you think?" ("base", xpos="far_left", ypos="head")
        her "Two hundred!" ("disgust", "narrow", "angry", "R")
        gen "How about a pat on the back and a Snickers bar to help with that terrible mood of yours?" ("base", xpos="far_left", ypos="head")
    her "I think I'd better go..."

    menu:
        "\"Wait. Two hundred points are yours. Show me!\"":
            $ current_payout = 200
            her "Really?" ("open", "base", "base", "mid")
            gen "Well?" ("base", xpos="far_left", ypos="head")
            her "......................................" ("annoyed", "base", "worried", "R")
            her "You have to promise me not to touch them, [name_genie_hermione]."
            gen "Sure, sure..." ("base", xpos="far_left", ypos="head")
            her "I am only doing this for the honour of my house, [name_genie_hermione]!" ("scream", "happyCl", "worried", "mid")

            pass

        "\"I will give you five points to see your tits.\"":
            her "Five?!" ("scream", "wide", "base", "mid")
            her "[name_genie_hermione], I am not going to expose myself for a meagre five points!" ("angry", "base", "angry", "mid",emote="angry")
            gen "Well, your tits sure aren't worth two hundred, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her "(They aren't?)" ("annoyed", "narrow", "worried", "down")
            her "Maybe one hundred - then?" ("annoyed", "narrow", "angry", "R")

            menu:
                "\"Fine. A hundred it is! Bare them already!\"":
                    $ current_payout = 100
                    $ states.her.mood = 0

                    her "................." ("annoyed", "wide", "base", "stare")
                    her "A hundred points..." ("annoyed", "base", "base", "R")
                    her "So be it..." ("mad", "narrow", "base", "R")
                    her "You have to promise me not to touch them, [name_genie_hermione]."
                    gen "Sure, sure..." ("base", xpos="far_left", ypos="head")
                    her "So be it..." ("smile", "happyCl", "base", "mid")

                    pass

                "\"Twenty-five house points, that's my final offer!\"":
                    $ current_payout = 25
                    $ states.her.mood += 9

                    her "..............." ("annoyed", "narrow", "worried", "down")
                    her "You have to promise me not to touch them, [name_genie_hermione]."
                    gen "Sure, sure..." ("base", xpos="far_left", ypos="head")
                    her "Well, so be it..." ("clench", "narrow", "base", "down")

                    pass

        "\"Fine, leave. I don't care...\"":
            her "*Tsk*!" ("clench", "closed", "angry", "mid")

            call her_walk(action="leave")

            gen "... She really left." ("base", xpos="far_left", ypos="head")
            gen "Maybe I have pushed her a bit too hard." ("base", xpos="far_left", ypos="head")

            $ states.her.mood += 12
            $ states.her.ev.admire_breasts.T2_intro_E1_failed = True #repeat writing

            # Event resets. (No progress)
            $ _event.cancel()
            jump end_hermione_event

    jump hg_pf_admire_breasts_T2

label hg_pf_admire_breasts_T2_intro_E2:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie], how would you like to show me your breasts again?" ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "I'd rather not, [name_genie_hermione]..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Are you sure?" ("base", xpos="far_left", ypos="head")
    gen "You could earn twenty-five house points for it!" ("grin", xpos="far_left", ypos="head")
    her "............." ("annoyed", "base", "worried", "R")
    her "Very well, [name_genie_hermione]." ("angry", "base", "angry", "mid")
    her @ cheeks blush "But you better keep your hands to yourself!" ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "Don't you dare touch them!" ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "You need to promise me, [name_genie_hermione]!" ("annoyed", "narrow", "angry", "R")
    gen "Of course. I promise I won't touch..." ("base", xpos="far_left", ypos="head")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T2

label hg_pf_admire_breasts_T2_E2:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie], I would very much like to see your breasts again!" ("grin", xpos="far_left", ypos="head")
    her "............." ("annoyed", "base", "worried", "R")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "Very well, [name_genie_hermione]." ("angry", "base", "angry", "mid")
    her @ cheeks blush "But you are not allowed to touch them!" ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "Promise me, [name_genie_hermione]!" ("annoyed", "narrow", "angry", "R")
    gen "Of course. I promise..." ("base", xpos="far_left", ypos="head")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T2

### Tier 3 ###

# Hermione reluctantly show you her breasts.
# You can touch them. But I'd advice you not to.

# Event 1 (i) - Hermione will lift up her top.
# Event 2 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T3_intro_E1:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("annoyed", "narrow", "angry", "R")
    gen "I need to see your tits." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "............" ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "Do you promise not to touch, [name_genie_hermione]?" ("annoyed", "narrow", "angry", "R")
    gen "Of course." ("base", xpos="far_left", ypos="head")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T3

label hg_pf_admire_breasts_T3_E1:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "I need to see your tits, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Are you only going to watch, [name_genie_hermione]?" ("angry", "happyCl", "worried", "mid")
    gen "Of course..." ("base", xpos="far_left", ypos="head")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T3

### Tier 4 ###

# Hermione is more than okay with showing you her tits now.
# She doesn't mind if you touch them.

# Event 1 (i) - Hermione will lift up her top.
# Event 2 (r) - Hermione will lift up her top.
# Event 3 (r) - Hermione will lift up her top.

label hg_pf_admire_breasts_T4_intro_E1:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("soft", "narrow", "base", "mid_soft")
    gen "Did I ever tell you what magnificent tits you have?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "............" ("clench", "narrow", "base", "down")
    her @ cheeks blush "Why do you have to be so vulgar, [name_genie_hermione]?!" ("clench", "happyCl", "worried", "mid")
    gen "Just take the compliment, and show them to me..." ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "Are you only going to watch, [name_genie_hermione]?" ("angry", "narrow", "worried", "mid")
    gen "Of course..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Alright then..." ("soft", "narrow", "worried", "down")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T4

label hg_pf_admire_breasts_T4_E1:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "I need to see your tits, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course, [name_genie_hermione]." ("open", "base", "base", "mid")

    her @ cheeks blush "You're only going to watch, right?" ("open", "closed", "worried", "mid")
    gen "Of course..." ("base", xpos="far_left", ypos="head")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T4

label hg_pf_admire_breasts_T4_E2:

    call start_hg_pf_admire_breasts

    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "I have to see your marvellous knockers, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course, [name_genie_hermione]." ("open", "base", "base", "mid")

    her @ cheeks blush "Are you only going to watch, [name_genie_hermione]?" ("open", "closed", "worried", "mid")
    gen "Of course..." ("base", xpos="far_left", ypos="head")

    $ current_payout = 25

    jump hg_pf_admire_breasts_T4
