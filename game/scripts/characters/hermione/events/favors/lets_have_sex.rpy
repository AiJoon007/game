

### Hermione Sex ###

label start_hg_pf_sex:

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her to have sex with me?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 65
    $ _temp_outfit_choice = "naked"
    return

label hg_pf_sex_fail:
    jump end_hermione_event

label end_hg_pf_sex:

    # Setup
    stop music fadeout 1.0

    show screen blkfade
    with d3

    hide hermione_main
    hide cg

    call weather_sound

    $ hermione.set_cum(None)
    $ hermione.equip(her_outfit_last)

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if states.her.mood != 0:
        her "" ("annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade, flip=False)
    else:
        her @ cheeks blush "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=blackfade)

    # Points
    gen "Alright then, [name_hermione_genie]. {number=current_payout} points to the Gryffindor house." ("base", xpos="far_left", ypos="head")
    $ gryffindor += current_payout
    her @ cheeks blush "Thank you, [name_genie_hermione]..." ("open", "base", "base", "R")

    # Hermione leaves
    her @ cheeks blush "Did you need anything else?" ("normal", "base", "base", "mid")
    gen "No, that shall do for today..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Okay..." ("soft", "base", "base", "R")
    if game.daytime:
        her @ cheeks blush "I'll head back to class then." ("open", "base", "base", "R")
    else:
        her @ cheeks blush "I'll head off to bed then..." ("open", "base", "base", "mid")

    gen "Until next time..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("normal", "base", "base", "mid")

    call her_walk("door", "base")
    call her_chibi("leave")

    # Increase level
    $ states.her.status.sex = True
    if states.her.level < 24: #Adds points till 24.
        $ states.her.level += 1

    $ achievements.unlock("nerdgasm")

    jump end_hermione_event

### Fail Events ###
label hg_pf_sex_T1_E1:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    menu:
        "\"Let's fuck!\"":
            pass
        "\"Let me pound your pussy!\"":
            pass
        "\"Your train to pound-town has arrived!\"":
            pass
        "\"Bend over! I'm going in!\"":
            pass
        "\"My dick, your pussy... What do you say?\"":
            pass
        "\"How many points to let me fuck your ass?\"":
            pass

    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare")
    her "How could you ask for such a thing!?"
    her "I think I better leave." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(Does she not want to earn points for her house after all?)" ("base", xpos="far_left", ypos="head")
    gen "(Hold on...)" ("base", xpos="far_left", ypos="head")
    gen "(She must just be shy! Yes, that's probably it...)" ("base", xpos="far_left", ypos="head")
    gen "(Better start with some less advanced favours...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 14

    jump hg_pf_sex_fail

label hg_pf_sex_T2_E1:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Why don't you come over here, and then I pound your pussy for a bit..." ("base", xpos="far_left", ypos="head")
    gen "With my cock!" ("grin", xpos="far_left", ypos="head")

    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare")
    her "How could you ask for such a thing!?"
    her "I think I better leave." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(Was it something that I said?)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 12

    jump hg_pf_sex_fail

label hg_pf_sex_T3_E1:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "This charade has been going on for far too long..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("angry", "base", "base", "mid")
    gen "Let's cut the bullshit, and get to why we're both here!" ("base", xpos="far_left", ypos="head")
    her "What do you--" ("angry", "base", "base", "mid")

    if game.daytime:
        gen "Let's fuck until sunrise!" ("base", xpos="far_left", ypos="head")
    else:
        gen "Let's fucking until the sun sets!" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare")
    her "I think I better leave." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(I may have made a slight miscalculation...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 10

    jump hg_pf_sex_fail

label hg_pf_sex_T4_E1:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Tell me... Why are we beating around the bush, when we could be fucking already?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare")
    her "Why would you say that?" ("angry", "base", "worried", "mid")
    her "I'm leaving." ("open", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(Didn't even answer the question...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 8

    jump hg_pf_sex_fail

label hg_pf_sex_T5_E1:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "I think it's about time we do the deed..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You... You don't mean..." ("soft", "base", "base", "mid")
    gen "That's right..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I... I need some time to think about this..." ("open", "squint", "base", "R")

    call her_walk(action="leave")

    gen "(She's getting there...)" ("base", xpos="far_left", ypos="head")
    gen "(Any day now...)" ("base", xpos="far_left", ypos="head")

    jump hg_pf_sex_fail

### Tier 6 ###

# Event 1 (i) - First time sex
# Event 2 (i) - Sex with different dialogue
# Event 3 (i) - Regular or anal sex (Once spread on desk CG is ready, we'll add new writing as a menu option)
# Event 3 (r) - Regular or anal sex, naked option (Once spread on desk CG is ready, we'll add new writing as a menu option)

label hg_pf_sex_T6_intro_E1:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "The favour I will be buying from you today..." ("base", xpos="far_left", ypos="head")
    her ".......?" ("base", "base", "base", "mid")
    gen "How should I put this delicately...?" ("base", xpos="far_left", ypos="head")
    her "Is it sex, [name_genie_hermione]?" ("base", "squint", "base", "mid")
    gen "Well, yes. How did you...?" ("base", xpos="far_left", ypos="head")
    her "Not a terribly difficult deduction all things considered..." ("base", "narrow", "base", "mid_soft")
    gen "You don't mind then?" ("base", xpos="far_left", ypos="head")
    her "Of course, I mind, [name_genie_hermione]!" ("upset", "closed", "base", "mid")
    her "I am not a prostitute!"
    gen "But you'll do it anyway??" ("base", xpos="far_left", ypos="head")

    if not is_in_lead(gryffindor):
        her "Gryffindor is falling behind again..." ("open", "closed", "base", "mid")
    else:
        her "I have to make sure Gryffindor stays in the lead..." ("open", "closed", "base", "mid")

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")
    her "What choice do I have...?"
    gen "Great!" ("base", xpos="far_left", ypos="head")
    gen "Get over here then!" ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "*Ehm*...{w=0.4} How do you...{w=0.4} How do you want me [name_genie_hermione]?" ("angry", "narrow", "base", "down")

    menu:
        "\"I want you in your school uniform, just how I met you!\"":
            $ _temp_outfit_choice = "uniform"
            her "Okay then." ("open", "narrow", "base", "down")
            hide hermione_main
            with fade

            $ her_outfit_last.save()
            $ hermione.equip(her_outfit_default)
            pause .8

        "\"Naked, of course!\"":
            $ _temp_outfit_choice = "naked"
            her @ cheeks blush "Alright..." ("angry", "base", "base", "mid")
            hide hermione_main
            with fade

            if hermione.is_any_worn("clothes"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("clothes")
                pause .8

    her "I'm ready..." ("open", "narrow", "base", "down")

    stop music fadeout 2.0
    call her_walk("desk", "base", reduce=0.8)
    pause .2

    show screen blkfade
    with d3
    pause 2

    call her_chibi_scene("grope_ass_back")
    hide screen blkfade
    with d5

    her "............." ("upset", "closed", "base", "mid", flip=True, trans=dissolve)
    gen "Relax, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her ".............." ("disgust", "base", "annoyed", "L")
    gen "Are you ready?" ("base", xpos="far_left", ypos="head")
    her "No..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Good girl." ("base", xpos="far_left", ypos="head")

    call hg_sex_1

    jump end_hg_pf_sex


label hg_pf_sex_T6_intro_E2:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Last night I had a dream..." ("base", xpos="far_left", ypos="head")
    gen "You were lying on my desk, and I was fucking your tight pussy like a madman..." ("grin", xpos="far_left", ypos="head")
    her "In that dream, [name_genie_hermione]..." ("upset", "closed", "base", "mid")
    her "Did I happen to receive sixty-five house points afterwards?" ("angry", "base", "angry", "mid")
    gen "Why yes, you did, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")
    her "..............................." ("disgust", "narrow", "base", "mid")

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")

    her "So, how are we doing this?" ("disgust", "narrow", "base", "down")

    menu:
        gen "We're doing it..."
        "\"... With clothes on!\"":
            $ _temp_outfit_choice = "uniform"
            her "You want me to wear my school uniform, I presume?" ("open", "narrow", "base", "mid")
            gen "Yes, please." ("grin", xpos="far_left", ypos="head")
            her "As you wish." ("open", "narrow", "base", "down")
            hide hermione_main
            with fade

            $ her_outfit_last.save()
            $ hermione.equip(her_outfit_default)
            pause .8

        "\"... Naked all the way!\"":
            $ _temp_outfit_choice = "naked"
            her @ cheeks blush "Fine..." ("angry", "base", "base", "mid")
            hide hermione_main
            with fade

            if hermione.is_any_worn("clothes"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("clothes")
                pause .8

    her "I'm done changing..." ("open", "narrow", "base", "down")

    stop music fadeout 2.0
    call her_walk("desk", "base", reduce=0.8)
    pause .2

    show screen blkfade
    with d3
    pause 2

    call her_chibi_scene("grope_ass_back")
    hide screen blkfade
    with d5

    gen "There we go...{w=0.4} Ready?" ("base", xpos="far_left", ypos="head")
    her "I...{w=0.3} think I--" ("disgust", "base", "base", "down", flip=True, trans=dissolve)

    call hg_sex_2

    jump end_hg_pf_sex


label hg_pf_sex_T6_intro_E3:

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], are you keeping your pussy wet and ready for me?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]!" ("scream", "closed", "angry", "mid")
    gen "Just say \"I do\", [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "..........." ("open", "base", "base", "mid")
    her "I do..." ("angry", "narrow", "base", "down")

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")

    gen "Great, then you can probably guess what favour I'll be buying from you today..." ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "base", "down")

    her "How do you want me?" ("soft", "narrow", "base", "R")

    menu:
        gen "*Hmm*..."
        "\"I want you in your school uniform!\"":
            $ _temp_outfit_choice = "uniform"
            her "Sure!" ("open", "narrow", "base", "down")
            hide hermione_main
            with fade

            $ her_outfit_last.save()
            $ hermione.equip(her_outfit_default)
            pause .8

        "\"I want you naked!\"":
            $ _temp_outfit_choice = "naked"
            her @ cheeks blush "That works for me..." ("angry", "base", "base", "mid")
            hide hermione_main
            with fade

            if hermione.is_any_worn("clothes"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("clothes")
                pause .8

    her "I'm all finished..." ("open", "narrow", "base", "down")

    stop music fadeout 2.0
    call her_walk("desk", "base", reduce=0.8)
    pause .2

    show screen blkfade
    with d3
    pause 2

    call her_chibi_scene("grope_ass_back")
    hide screen blkfade
    with d5

    gen "(*Hmm*... Now that I look at it, I feel like fucking her ass...)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "(Where should I put it in?)" ("base", xpos="far_left", ypos="head")
        "-Fuck her pussy-":
            gen "(On second thought, this hole is still good enough for me...)"
            call hg_sex_3

        "-Poke her butthole!-":
            gen "(Yes! Let's see if she's willing to take it up her ass!)" ("base", xpos="far_left", ypos="head")

            $ her_eventqueue_anal.start()

    jump end_hg_pf_sex


label hg_pf_sex_T6_E3: # repeats

    call start_hg_pf_sex

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], are you keeping your pussy wet and ready for me?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]..." ("upset", "base", "worried", "down")
    gen "Just say \"I do\", [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "..........." ("open", "base", "base", "mid")
    her "I do..." ("soft", "narrow", "base", "R")
    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")

    gen "Great, then you know what's coming..." ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "base", "down")

    her "How would you want me, [name_genie_hermione]?" ("soft", "narrow", "base", "R")

    menu:
        gen "*Hmm*..."
        "\"In your school uniform!\"":
            $ _temp_outfit_choice = "uniform"
            her "Sure!" ("open", "narrow", "base", "down")
            hide hermione_main
            with fade

            $ her_outfit_last.save()
            $ hermione.equip(her_outfit_default)
            pause .8

        "\"Naked!\"":
            $ _temp_outfit_choice = "naked"
            her @ cheeks blush "That works for me..." ("angry", "base", "base", "mid")
            hide hermione_main
            with fade

            if hermione.is_any_worn("clothes"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("clothes")
                pause .8

    her "Alright then... I'm ready." ("open", "narrow", "base", "down")

    stop music fadeout 2.0
    call her_walk("desk", "base", reduce=0.8)
    pause .2

    show screen blkfade
    with d3
    pause 2

    call her_chibi_scene("grope_ass_back")
    hide screen blkfade
    with d5

    menu:
        gen "(How should I fuck her this time?)" ("base", xpos="far_left", ypos="head")
        "-Use her pussy!-":
            gen "(On second thought, this hole is still good enough for me...)" ("base", xpos="far_left", ypos="head")
            call hg_sex_3

        "-Fuck her asshole!-":
            gen "(Let's see how well she takes it up the ass!)" ("angry", xpos="far_left", ypos="head")

            $ her_eventqueue_anal.start()

    jump end_hg_pf_sex

### First Time Sex ###

label hg_sex_1:

    show screen blkfade
    with d5
    pause.2

    #Stop wind and thunder sounds
    stop weather fadeout 4
    play sound "sounds/gltch.ogg"
    with kissiris
    hide hermione_main

    if _temp_outfit_choice == "naked":
        show her_sex_personal lean_back hold mouth_scream eyebrows_base eyes_wide_stare cheeks_blush as cg
    else:
        show her_sex_personal lean_back skirt shirt hold mouth_scream eyebrows_base eyes_wide_stare cheeks_blush as cg

    show her_sex_personal lean_back as cg zorder 17:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0

    hide screen blkfade
    with d5

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "*Ooooohhhhhhhhhhhh*....{heart}"

    show her_sex_personal lean_back as cg:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (0, 0)
        zoom 1.0
        rotate 0
        ease_quad 3.0 offset (-230, -100) zoom 0.5 rotate -15

    ###

    gen "Your pussy... It's so tight."
    gen "I'll start moving now."

    play background "sounds/slickloop.ogg" fadein 2

    show her_sex_personal mouth_normal eyebrows_worried eyes_happycl as cg
    her "................"
    gen "You alright?"

    show her_sex_personal mouth_angry eyebrows_base eyes_base_mid tears_soft as cg
    her "*A-ha*...{w=0.3} It's too big..."
    show her_sex_personal mouth_angry eyebrows_base eyes_happycl tears_soft_blink as cg
    her "You will rip me apart, [name_genie_hermione]!"

    show her_sex_personal hold_grin as cg
    gen "Nonsense! My cock is of a regular size."

    show her_sex_personal hold as cg
    gen "It's not my fault that you are so tight."

    show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush tears_none as cg
    her "......................"

    menu:
        "\"You should be ashamed of yourself!\"":
            show her_sex_personal mouth_mad eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "I am not ashamed, [name_genie_hermione]!"
            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "I am doing this for the sake of my house!"
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "To help my--"

            show her_sex_personal mouth_open_tongue eyebrows_worried eyes_happycl cheeks_blush as cg
            her "*Ah-ha-a*...{heart}"
            show her_sex_personal mouth_open eyebrows_worried eyes_happycl cheeks_blush as cg
            her "My housemates depend on--{w=0.1} *Ah-a*...{w=0.3} me...{heart}{heart}"
            gen "Are you sure that's the only reason?"

            show her_sex_personal mouth_disgust eyebrows_worried eyes_happycl cheeks_blush as cg
            her "I don't know--"

            show her_sex_personal mouth_open eyebrows_worried eyes_happycl cheeks_blush as cg
            her "*Ah-a*...{heart}"

            show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "I don't know what you mean, [name_genie_hermione]."
            gen "It seems to me that you are enjoying this a little bit too much."
            show her_sex_personal mouth_annoyed eyebrows_angry eyes_narrow_down cheeks_blush as cg
            her "I'm not, [name_genie_hermione]!"
            gen "Really?"

            show her_sex_personal mouth_normal eyebrows_angry eyes_narrow_down cheeks_blush as cg
            her "......................"

            show her_sex_personal hold_grin as cg
            gen "Then why is your pussy so wet?"

            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her ".................... *A-ha*.{heart}"
            gen "Admit it, you enjoy getting fucked by your headmaster!"

            show her_sex_personal mouth_annoyed eyebrows_annoyed eyes_narrow_mid cheeks_blush as cg
            her "I do not!"
            call ctc
            gen "Lean forward a bit will you, I want to grab that ass of yours..."
            show her_sex_personal mouth_disgust eyebrows_annoyed eyes_narrow_down cheeks_blush as cg
            her "Fine..."

            show her_sex_personal lean_forward caress as cg:
                offset (-230, -100)
                zoom 0.5
                rotate -15
                ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

            show her_sex_personal mouth_annoyed eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "..."
            play background "sounds/slickloopfast.ogg" fadeout 2
            pause .4
            show her_sex_personal mouth_angry eyebrows_worried eyes_wide_mid cheeks_blush as cg
            call ctc

            show her_sex_personal caress_grin as cg

            gen "That's much better, don't you think?"
            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Ah-ha*...{heart}"

            show her_sex_personal caress as cg

        "\"So... What's new in your life?\"":

            show her_sex_personal mouth_mad eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "...[name_genie_hermione]?"
            gen "Just trying to have a polite conversation."
            show her_sex_personal mouth_open eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "*Ah-ah*...{heart} But-- *Ah*...{heart}{heart}"
            gen "Any news from your folks?"

            show her_sex_personal mouth_angry eyebrows_worried eyes_wide_mid cheeks_blush as cg
            her "My parents?"

            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "[name_genie_hermione], *Ah-ah*...{w=0.3} Please...{w=0.4} I cannot talk."
            gen "Why not? Enjoying this too much?"
            show her_sex_personal mouth_disgust eyebrows_worried eyes_happycl cheeks_blush as cg
            her "I am-- *Ah*...{w=0.3} I am not...{heart}"
            gen "I think you are."
            show her_sex_personal mouth_annoyed eyebrows_worried eyes_happycl cheeks_blush as cg
            her "I am only doing this for the points, [name_genie_hermione]..."
            gen "Oh, I see..."
            gen "So you are like a prostitute then."

            show her_sex_personal mouth_disgust eyebrows_base eyes_wide_mid cheeks_blush as cg
            her "What?"
            gen "Well, I pay you to have sex with me... How would you call that?"

            show her_sex_personal mouth_angry eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "..........."

            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "I am not a prostitute..."

            show her_sex_personal mouth_mad eyebrows_base eyes_narrow_r cheeks_blush tears_soft as cg
            her "Why are you being so mean to me, [name_genie_hermione]?"
            gen "I think you like it when I'm mean."

            show her_sex_personal mouth_clench eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
            her "I do not!"

            gen "Really?"

            show her_sex_personal mouth_annoyed eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
            her "......................"

            show her_sex_personal hold_grin as cg
            gen "Then why is your pussy so wet?"

            show her_sex_personal mouth_angry eyebrows_annoyed eyes_narrow_down cheeks_blush as cg
            her "Not because of that!"
            gen "If you say so..."
            call ctc
            gen "Lean forward a bit will you, I want to grab that ass of yours..."
            show her_sex_personal mouth_disgust eyebrows_angry eyes_narrow_down cheeks_blush as cg
            her "Fine..."

            show her_sex_personal lean_forward caress as cg:
                offset (-230, -100)
                zoom 0.5
                rotate -15
                ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

            play background "sounds/slickloopfast.ogg" fadeout 2
            pause .4
            show her_sex_personal mouth_angry eyebrows_worried eyes_wide_mid cheeks_blush as cg
            call ctc

            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*A-ah*...{heart}"
            show her_sex_personal mouth_open_tongue eyebrows_worried eyes_happycl cheeks_blush tears_soft_blink as cg
            her "I am...{w=0.3} *ah*...{heart}{w=0.3} not a prostitute..."

        "\"......................................................\"":

            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*A-ha*...{w=0.3} *ah*..."
            gen "*Panting!*"
            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "*Ah*...{w=0.3} *ha-aha*..."
            gen "*Mmm*..."
            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Ah-ah*..."
            gen "......................"
            show her_sex_personal mouth_open eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "*Ah*...{w=0.3} *ah*..."

            show her_sex_personal mouth_soft eyebrows_base eyes_base_mid cheeks_blush as cg
            her "*Ah*...{w=0.4} [name_genie_hermione]?"
            gen "What is it?"

            show her_sex_personal mouth_soft eyebrows_worried eyes_closed cheeks_blush as cg
            her "*Ah*...{w=0.3} Do you....{w=0.4} like it?"
            gen "Do I like drilling your super-tight pussy?"

            show her_sex_personal hold_grin as cg
            gen "Very much so!"

            show her_sex_personal hold as cg
            gen "Why do you ask [name_hermione_genie]?"

            show her_sex_personal mouth_clench eyebrows_worried eyes_closed cheeks_blush as cg
            her "....................."

            show her_sex_personal mouth_angry eyebrows_worried eyes_closed cheeks_blush as cg
            her "*Ah*...{w=0.3} You...{w=0.2} You just got so quiet..."
            gen "Just enjoying the moment, [name_hermione_genie]."
            gen "What about you? You alright?"
            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Ah*...{w=0.3} {heart}yes...{heart}"

            show her_sex_personal mouth_angry eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "It hurts--{w=0.2} *Ah*...{w=0.4} It hurts a little though..."

            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "Your penis--{w=0.2} *Ah*...{w=0.4} is too big..."

            gen "*Hmm*..."
            gen "You need me to slow down or something?"

            show her_sex_personal mouth_open eyebrows_base eyes_wide_down cheeks_blush as cg
            her "No, [name_genie_hermione]...{w=0.4} You don't have to--"

            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "Please, don't mind me...{w=0.4} Enjoy yourself."
            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "I will--{w=0.2} *Ah*...{w=0.3} Get used to it eventually..."

            gen "As you say, [name_hermione_genie]..."
            call ctc
            gen "Lean forward a bit will you, I want to grab that ass of yours..."
            show her_sex_personal mouth_soft eyebrows_annoyed eyes_narrow_down cheeks_blush as cg
            her "Alright..."

            show her_sex_personal lean_forward caress as cg:
                offset (-230, -100)
                zoom 0.5
                rotate -15
                ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

            play background "sounds/slickloopfast.ogg" fadeout 2
            pause .4
            show her_sex_personal mouth_angry eyebrows_worried eyes_wide_mid cheeks_blush as cg
            call ctc

            show her_sex_personal mouth_open eyebrows_annoyed eyes_happycl cheeks_blush as cg
            her "*Ooooh*...{heart}"
            gen "Yes, this is great!"


    show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush as cg
    her "*Ah-ah*...{heart}"

    if game.daytime:
        gen "Going to classes after this?"
    else:
        gen "Going to bed after this?"

    show her_sex_personal mouth_angry eyebrows_worried eyes_happycl cheeks_blush as cg
    her "Yes--{w=0.2} *ah*...{heart}"
    show her_sex_personal mouth_disgust eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "If I'll be able to walk..."
    gen "*Ght*! {heart} Yes, you always say the right things, [name_hermione_genie]!"

    show her_sex_personal mouth_angry eyebrows_base eyes_base_mid cheeks_blush as cg
    her "Aah! I can't hold it!"

    show her_sex_personal mouth_scream eyebrows_base eyes_wide_stare cheeks_blush as cg
    with vpunch
    her "{size=+7}!!!!!!!!!!!!!!!{/size}{heart}{heart}{heart}"

    show her_sex_personal caress as cg
    gen "*huh*? You alright?"

    nar "Hermione's legs are shaking..."
    gen "[name_hermione_genie]?"
    show her_sex_personal mouth_grin eyebrows_annoyed eyes_wide_stare cheeks_blush as cg
    her "{heart}{heart}{heart}I--{w=0.2} I think I'm cumming, [name_genie_hermione]!{heart}{heart}{heart}"

    show her_sex_personal caress_grin as cg
    gen "*Tch*... You nasty slut!"

    show her_sex_personal mouth_mad eyebrows_base eyes_wide_mid cheeks_blush as cg
    her "Aah! I can't hold it!"
    gen "You need to be punished for being such a slut!"

    show her_sex_personal bent_over grab as cg:
        offset (-65, -240) 
        zoom 0.45 
        rotate -4
        easein 1.0 offset (0, -480) rotate 0
    with vpunch

    pause 1.0

    #Could add some sound effect here
    show her_sex_personal mouth_open eyebrows_base eyes_wide_r cheeks_blush as cg:
        offset (0, -480) 
        rotate 0
        ease_quad 3.0 offset (-60, -620) zoom 0.55
    nar "You push Hermione down onto the desk and start fucking her fiercely!"

    play background "sounds/slickloopveryfast.ogg" fadeout 2
    show her_sex_personal mouth_mad eyebrows_base eyes_wide_mid cheeks_blush as cg
    her "[name_genie_hermione]!"


    show her_sex_personal mouth_angry eyebrows_base eyes_narrow_stare cheeks_blush as cg
    her "NO! STOP! PLEASE!"
    gen "Who told you that you could cum, slut? This is your punishment!"

    show her_sex_personal mouth_open_wide_tongue eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "[name_genie_hermione], no, *ah-a*!{heart}"

    show her_sex_personal mouth_crooked_smile eyebrows_worried eyes_closed cheeks_blush as cg
    her "*Ah-a*...{heart}{w=0.2}I will go insane!{heart}{heart}{heart}"
    gen "{size=+7}*Grragh*!{/size}"
    call ctc

    show her_sex_personal mouth_angry eyebrows_worried eyes_wide_down cheeks_blush as cg
    her "No--{heart}{w=0.2} *Ah*...{heart}"
    show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_up cheeks_blush as cg
    her "I think I will...{heart}{w=0.2} pass out...{heart}"
    gen "*ARGH*! YOU WHORE!"


    menu:
        "-Cum all over her-":

            show her_sex_personal cum_outside2 as cg

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"
            show her_sex_personal mouth_mad eyebrows_worried eyes_narrow_r cheeks_blush as cg

            show her_sex_personal cum_outside as cg
            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg

            show her_sex_personal cum_outside2 as cg
            play sound "sounds/slick_02.ogg"
            gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"

            show her_sex_personal cum_outside mouth_grin eyebrows_worried eyes_narrow_r cheeks_blush as cg

            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_heavy as cg
            else:
                show her_sex_personal cum_ass_skirt_heavy as cg
            with d5

            play sound "sounds/slick_02.ogg"
            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            pause .8
            show her_sex_personal after as cg
            call ctc


            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "You came all over me..."
            call ctc

            gen "Well, that was rather intense..."

            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_up cheeks_blush as cg
            her "*Mmm*..."

            gen "You alright?"

            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "*Ah*...{w=0.4} yes...{heart}{heart}{heart}"
            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "Although my legs are still shaking...{heart}"
            call ctc

            if game.daytime:
                show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_mid cheeks_blush as cg
                her "But I think I will be able to make it to my classes..."
            else:
                show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
                her "But I think I will be able to make it to the common room..."

            gen "Good."
            gen "Did you enjoy getting fucked by your headmaster?"
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "[name_genie_hermione], I am only doing this for my house."
            gen "Seriously? Still?"
            show her_sex_personal mouth_disgust eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "Could I just get paid now... please?"

            gen "Of course!"

            show screen blkfade
            with d5

            nar "You take a step back to take in the view of Hermione, who is now fully coated in your cum."
            nar "Looking down you notice her legs still twitching slightly and a streak of liquid slowly beginning to trickle down her legs."
            nar "After composing herself for a moment, Hermione readies herself and then makes her way to the front of your desk."

            return

        "-Cum inside her-":
            $ states.her.status.creampie = True

            show her_sex_personal cum_inside as cg

            with hpunch
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"

            call cum_block

            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_r cheeks_blush cum_pussy_light as cg

            stop background fadeout 2
            play sound "sounds/slick_02.ogg"
            gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"

            call cum_block

            show her_sex_personal mouth_angry eyebrows_worried eyes_wide_mid cheeks_blush cum_pussy_heavy as cg

            play sound "sounds/slick_02.ogg"
            show her_sex_personal mouth_open_wide_tongue eyebrows_worried eyes_wide_mid cheeks_blush as cg
            call ctc

            show her_sex_personal mouth_open_tongue eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*...{heart}{heart}{heart}"

            show her_sex_personal mouth_grin eyebrows_base eyes_base_mid cheeks_blush as cg
            her "You came inside of me..."
            gen "I sure did."
            call ctc

            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "That was...{w=0.8}{nw}"
            show her_sex_personal mouth_soft eyebrows_base eyes_base_mid cheeks_blush as cg
            her "That was...{fast} Wait..."
            gen "What?"
            show her_sex_personal mouth_disgust eyebrows_worried eyes_wide_mid cheeks_blush as cg
            her "What if I get pregnant?"
            gen "Nah, you will be alright..."
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "B-But... How would you know, [name_genie_hermione]?"
            gen "We {i}witchers{/i} are infertile."
            show her_sex_personal mouth_angry eyebrows_worried eyes_base_down cheeks_blush as cg
            her "{i}Witchers{/i}?"
            gen "Sure... You are a witch, that makes me {i}a witcher{/i}, right?"
            gen "And everyone knows that {i}witchers{/i} are infertile..."
            show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "[name_genie_hermione], you make no sense..."
            show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "Can I please just get paid now...?"
            gen "Certainly..."


            play sound "sounds/slick_02.ogg"
            show her_sex_personal after as cg

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg
            with kissiris

            show her_sex_personal mouth_base eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{heart}*Ngh*!{heart}"

            show screen blkfade
            with d5

            nar "You hear Hermione take a swift intake of breath as you finally let go of her ass."
            nar "Her legs twitches slightly and as you take a step back you get a full view of your cum slowly beginning to drip onto the floor."
            nar "After composing herself for a moment, Hermione readies herself and then makes her way to the front of your desk."

            return

### Second Time Vaginal Sex ###

label hg_sex_2:

    show screen blkfade
    with d5
    pause.2

    #Stop wind and thunder sounds
    stop weather fadeout 4

    play sound "sounds/gltch.ogg"
    with hpunch
    with kissiris

    # Hermione Setup
    hide hermione_main

    if _temp_outfit_choice == "naked":
        show her_sex_personal lean_back hold mouth_open eyebrows_base eyes_wide_stare cheeks_blush as cg
    else:
        show her_sex_personal lean_back skirt shirt hold mouth_open eyebrows_base eyes_wide_stare cheeks_blush as cg

    show her_sex_personal lean_back as cg zorder 17:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0

    hide screen blkfade
    with d5

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "*Ooooohhhhhhhhhhhh*....{heart}"

    show her_sex_personal lean_back as cg:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0
        ease_quad 3.0 offset (-230, -100) zoom 0.5 rotate -15

    show her_sex_personal mouth_open eyebrows_base eyes_happycl cheeks_blush as cg
    her "*Ah*...{heart}"
    gen "Your pussy feels a bit looser now..."
    show her_sex_personal mouth_angry eyebrows_annoyed eyes_narrow_down cheeks_blush as cg
    her "It does?"

    play background "sounds/slickloop.ogg" fadein 2
    pause .6
    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "*Ah*...{heart}"

    show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "That's all-- *Ah*... because of you [name_genie_hermione]...{heart}"

    show her_sex_personal mouth_open_tongue eyebrows_annoyed eyes_narrow_up cheeks_blush as cg
    her "You are ruining my cute little pussy with your monstrous penis...{heart}"

    show her_sex_personal hold_grin as cg

    if name_genie_hermione == "Master":
        gen "*Agh*...{w=0.3} You deserve it!"
    elif name_genie_hermione == "Daddy":
        gen "*Agh*, you naughty girl!"
    else:
        gen "*Agh*, you whore!"
    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "*Ah*...{heart}{heart}"
    gen "Do you like it when I fuck you like this?"

    show her_sex_personal mouth_base eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "Yes, [name_genie_hermione]...{heart}"

    menu:
        gen "..."
        "-Be sweet but passionate-":
            gen "How about this?"

            show her_sex_personal lean_forward caress as cg:
                offset (-230, -100)
                zoom 0.5
                rotate -15
                ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "Whoa!"
            gen "Well?"
            show her_sex_personal mouth_base eyebrows_annoyed eyes_narrow_r cheeks_blush as cg
            her "I...{w=0.4} I do--{w=0.2} *Ah*...{w=0.4} I love it, [name_genie_hermione]... {heart}"
            gen "Good girl!"
            gen "Just relax and take my cock!"

            play background "sounds/slickloopfast.ogg" fadeout 2

            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "Yes...{w=0.3} *Ah*...{heart}"
            gen "All the way in... all the way..."

            show her_sex_personal mouth_open_tongue eyebrows_annoyed eyes_happycl cheeks_blush as cg
            her "*Ah*...{heart}{heart}"
            if name_hermione_genie == "Angel":
                gen "Yes, my little angel..."
            else:
                gen "Yes, my little princess..."

            show her_sex_personal mouth_mad eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "W--{w=0.2} What?"

            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "No, please don't call me that now...{w=0.4} *Ah*...{heart}"
            show her_sex_personal mouth_disgust eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "My daddy used to call me that when I was little..."
            if name_genie_hermione == "Daddy":
                gen "Well, you don't seem to mind calling me daddy!"
                gen "Right now I am your daddy!"
            else:
                gen "Well, right now, I am your daddy!"

            show her_sex_personal mouth_angry eyebrows_worried eyes_happycl cheeks_blush as cg
            her "*Ah*...{w=0.3}{heart} *Ah-ah*...{heart}{heart}"
            if name_hermione_genie == "Angel":
                gen "And you are my slutty angel!"
            else:
                gen "And you are my little princess-slut!"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "*Ah*...{w=0.3}{heart} *Mmm*...{heart}{heart}{heart}"

            if name_genie_hermione == "Daddy":
                her "[name_genie_hermione]...{heart}{heart}{heart}"

        "-Be mean to her!-": #Can add in more nickname variations here (the derogatory ones)
            gen "Yes, you slut!"
            gen "I bet you love every second of this!"
            nar "You push Hermione forward and pick up the pace."

            play background "sounds/slickloopfast.ogg" fadeout 2

            show her_sex_personal lean_forward caress as cg:
                offset (-230, -100)
                zoom 0.5
                rotate -15
                ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

            pause .4

            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg

            play background "sounds/sexloopfast.ogg"
            pause .3
            show her_sex_personal mouth_angry eyebrows_worried eyes_base_down cheeks_blush tears_soft as cg
            nar "You begin pumping your cock deep inside Hermione's pussy, her legs hitting the edge of your desk as you smack your pelvis hard up against her ass."
            show her_sex_personal mouth_mad eyebrows_worried eyes_happycl cheeks_blush tears_soft_blink as cg
            her "*Ah*...{heart} [name_genie_hermione]..."
            gen "You nasty slut!"

            show her_sex_personal mouth_open_tongue eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3}{heart} *Ah-a*...{heart}"
            gen "You are a disgrace, [name_hermione_genie]!"
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush tears_soft as cg
            her "*Ah-ah*...{heart}{heart}{heart}"
            gen "Your parents sent you here to study, not to screw your teachers!"
            show her_sex_personal mouth_disgust eyebrows_worried eyes_happycl cheeks_blush tears_soft_blink as cg
            her "*Ah-a*...{w=0.4}{heart} But I am only doing this--"
            if name_genie_hermione == "Master":
                gen "As if...{w=0.4} I can hear that tone in your voice every time you call me master..."
                gen "You're nothing but a cock-sleeve for me to do with as I please, and you know it..."
            elif name_genie_hermione == "Daddy":
                gen "What would your father say if he knew you're calling me daddy?"
            else:
                gen "I've never cared about why you are doing this, you ignorant cocksucker!"
            gen "Look at you...{w=0.3} What you've become!"
            gen "Cunt full of your headmaster's cock, taking it like a cheap whore!"

            show her_sex_personal mouth_soft eyebrows_annoyed eyes_narrow_down cheeks_blush tears_soft as cg
            her "*Ah*...{heart} No...{heart} stop saying--{heart} *Ah*...{heart}{heart}{heart}"
            nar "You pick up the pace some more."

            play background "sounds/sexloopveryfast.ogg"
            show her_sex_personal mouth_grin eyebrows_base eyes_wide_stare cheeks_blush tears_soft as cg
            nar "The room fills up with the rhythmical sound of flesh hitting flesh..."
            gen "You let me molest you...{w=0.4} You suck my cock..."
            show her_sex_personal mouth_angry eyebrows_base eyes_narrow_stare cheeks_blush tears_soft as cg
            gen "What does that make you!?"

            show her_sex_personal mouth_angry eyebrows_base eyes_narrow_mid cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.2}*Ah*...{w=0.2}*Ah*...{w=0.4}"

            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.2}{heart} *Ah*....{heart}{heart}{heart}"

            show her_sex_personal mouth_angry eyebrows_base eyes_base_down cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.2}*Ah*...{w=0.2}"
            show her_sex_personal mouth_open eyebrows_base eyes_narrow_down cheeks_blush tears_soft as cg
            her "{size=-5}A whore...{/size}"
            gen "Yes! That's exactly what you are!"
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*...{heart}"
            show her_sex_personal mouth_normal eyebrows_annoyed eyes_narrow_mid cheeks_blush tears_soft as cg
            her "...."
            show her_sex_personal mouth_normal eyebrows_annoyed eyes_narrow_r cheeks_blush tears_soft as cg
            her "....{fast}...."
            show her_sex_personal mouth_normal eyebrows_annoyed eyes_narrow_down cheeks_blush tears_soft as cg
            her "........{fast}...."

    #Note: Once Spread on Desk CG is ready we'll add menu option here to flip her over onto the desk (new writing) or continue fucking her from behind.

    show her_sex_personal mouth_normal eyebrows_worried eyes_narrow_down cheeks_blush as cg
    her "*Ehm*...{w=0.4} [name_genie_hermione]..."
    gen "Yes?"
    show her_sex_personal mouth_open eyebrows_annoyed eyes_narrow_down cheeks_blush as cg
    her "You think you could--{w=0.3} *Ah*..."

    show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_r cheeks_blush as cg
    her "Could you--{w=0.2} Spank me a little?"
    gen "Gladly!"

    stop background fadeout 2

    if not _temp_outfit_choice == "naked":
        nar "You grab Hermione's bottoms firmly and slide down along with her panties in one swift movement..."
        play sound "sounds/cloth_sound3.ogg"
        show her_sex_personal -skirt as cg
        with d3

    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_r cheeks_blush as cg
    her "Whoa!"

    play background "sounds/sexloop.ogg" fadein 2

    show her_sex_personal bent_over grab as cg:
        offset (-65, -240)
        zoom 0.45
        rotate -4
        easein 1.0 offset (0, -480) rotate 0
    with vpunch

    pause 1.0

    #Could add some sound effect here
    show her_sex_personal mouth_soft eyebrows_base eyes_wide_r cheeks_blush as cg:
        offset (0, -480)
        rotate 0
        ease_quad 3.0 offset (-60, -620) zoom 0.55

    nar "You push Hermione over your desk, and start fucking her fiercely as you begin spanking her ass."

    call slap_her

    show her_sex_personal mouth_grin eyebrows_base eyes_wide_up cheeks_blush tears_soft as cg
    her "*Aa-a-ah*!{heart}{heart}{heart}"
    gen "You liked that one, *huh*?"

    call slap_her

    show her_sex_personal mouth_crooked_smile eyebrows_base eyes_narrow_down cheeks_blush tears_soft as cg
    her "*Ah*...!{w=0.4}{heart}"
    gen "And some more!"
    call slap_her

    if name_genie_hermione == "Master":
        show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
        her "*Ah*...{w=0.3} Punish me [name_genie_hermione]!"
    elif name_genie_hermione == "Daddy":
        gen "For being such a..."
        call slap_her
        gen "For being such a...{fast} naughty girl!"
        call slap_her
        show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
        her "*Ahh*...{w=0.3} I'm sorry [name_genie_hermione]..."
    else:
        show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush tears_soft as cg
        her "*Ahh*!{w=0.3} Yes!"
    nar "You notice that with every slap of the girl's butt, her pussy clutches your cock ever so slightly..."
    nar "You love the sensation and unleash another series of slaps on Hermione's ass-cheeks."
    nar "Every single one met with a gasp of excitement from the girl."

    call slap_her
    call slap_her
    call slap_her

    if name_genie_hermione == "Master":
        show her_sex_personal mouth_grin eyebrows_base eyes_happycl cheeks_blush tears_soft_blink as cg
        her "*Aah*!!!{heart}{heart}{heart} Harder...{w=0.4} Harder [name_genie_hermione]!{heart}{heart}{heart}"
        call slap_her
        call slap_her
        call slap_her
        show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush tears_soft as cg
        her "Thank you...{heart}{heart}{heart}{w=0.5} Thank you [name_genie_hermione]...{heart}{heart}{heart}"
    elif name_genie_hermione == "Daddy":
        show her_sex_personal mouth_grin eyebrows_base eyes_happycl cheeks_blush tears_soft_blink as cg
        her "[name_genie_hermione]!{heart}{heart}{heart}"
        show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush tears_soft as cg
        her "I'm sorry...{heart}{heart}{heart}{w=0.5} For being such a bad girl [name_genie_hermione]...{heart}{heart}{heart}"
    else:
        show her_sex_personal mouth_grin eyebrows_base eyes_happycl cheeks_blush tears_soft_blink as cg
        her "*Aah*!!!{heart}{heart}{heart} IT HURTS!{heart}{heart}{heart}"
        show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush tears_soft as cg
        her "It hurts...{heart}{heart}{heart}{w=0.5} It hurts so good...{heart}{heart}{heart}"
    gen "*Hmm*?"
    gen "Why are your legs shaking, [name_hermione_genie]?"
    gen "Are you cumming?"

    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush tears_soft as cg
    her "Yes...{heart}{heart}{heart}{heart}{heart}{heart}"
    gen "Well, I think I will follow your example then."

    play background "sounds/sexloopfast.ogg"
    nar "You steady your pace and begin thrusting your pelvis hard against Hermione's ass, the sounds of her cheeks slapping reverberates across the office..."

    show her_sex_personal mouth_clench eyebrows_base eyes_base_ahegao cheeks_blush tears_soft as cg
    her "*Ah*!{w=0.2} No!{w=0.2} I can't...{w=0.3}{heart} I--{w=0.2}{heart} *Ah*...{heart}{heart}{heart}"
    gen "Shut it whore!"

    play background "sounds/sexloopveryfast.ogg"
    nar "Thrusting your cock deep into Hermione's pussy, you feel yourself getting close to the edge."
    call ctc

    menu:
        "-Cum inside of her-":

            show her_sex_personal cum_inside as cg

            gen "{size=+7}*Argh*, TAKE THIS!!!{/size}"

            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_light mouth_grin eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "!!!"

            gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"

            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal mouth_angry eyebrows_base eyes_happycl cheeks_blush as cg
            her "*AH*! IT'S FILLING ME UP!{heart}{heart}{heart}"
            gen "I'm not done yet, bitch!"
            gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}"

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_heavy mouth_angry eyebrows_base eyes_happycl cheeks_blush as cg

            pause 1

            show her_sex_personal mouth_open_wide_tongue eyebrows_base eyes_base_ahegao cheeks_blush tears_soft as cg
            her "*AH*! MY WOMB!"

            gen "*Ah*...{w=0.3} *Ah*...{w=0.3} That was awesome!"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_stare as cg
            her "*Ah*...{heart}"

            if name_genie_hermione == "Master":
                gen "You alright there, fuckhole?"
            else:
                gen "You alright there, [name_hermione_genie]?"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_stare as cg
            her "Yes...{w=0.3} I..."

            show her_sex_personal mouth_base eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "{heart}I feel so full...{heart}"

            show her_sex_personal mouth_clench eyebrows_base eyes_base_stare cheeks_blush as cg
            her "!!!"
            show her_sex_personal mouth_clench eyebrows_base eyes_base_r cheeks_blush as cg
            her "You came inside of me, [name_genie_hermione]!"

            gen "I sure did."
            if not states.her.status.creampie:
                show her_sex_personal mouth_disgust eyebrows_worried eyes_wide_mid cheeks_blush as cg
                her "What if I get pregnant?"
                gen "Nah, you will be alright..."
                show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush as cg
                her "B-But... How would you know, [name_genie_hermione]?"
                gen "We {i}witchers{/i} are infertile."
                show her_sex_personal mouth_angry eyebrows_worried eyes_base_down cheeks_blush as cg
                her "{i}Witchers{/i}?"
                gen "Sure... You are a witch, that makes me {i}a witcher{/i}, right?"
                gen "And everyone knows that {i}witchers{/i} are infertile..."
                show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_r cheeks_blush as cg
                her "[name_genie_hermione], you make no sense..."
                show her_sex_personal mouth_base eyebrows_base eyes_narrow_down cheeks_blush as cg
                her "But perhaps you are right, [name_genie_hermione]...{w=0.4} I shouldn't worry so much."
            else:
                show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_l cheeks_blush as cg
                her "You shouldn't have..."
                gen "Did you not enjoy it?"

                show her_sex_personal mouth_base eyebrows_worried eyes_narrow_r cheeks_blush as cg
                her "...{w=0.4} Maybe."

                show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_r cheeks_blush as cg
                her "I...{w=0.4} I think I came several times..."

                show her_sex_personal mouth_base eyebrows_base eyes_narrow_down cheeks_blush as cg
                her "Maybe you are right, [name_genie_hermione]...{w=0.4} I shouldn't worry so much."

            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "*Ehm*...{w=0.4} Can I get my payment now?"
            gen "As you wish."

            play sound "sounds/slick_02.ogg"

            if _temp_outfit_choice == "naked":
                show her_sex_personal after cum_ass_light mouth_base eyebrows_base eyes_narrow_up cheeks_blush as cg
            else:
                show her_sex_personal after cum_ass_skirt_light mouth_base eyebrows_base eyes_narrow_up cheeks_blush as cg
            with kissiris

            her "{heart}*Ngh*!{heart}"

            show screen blkfade
            with d5

            nar "You let go of Hermione's ass and take a few steps back."
            nar "You watch Hermione as your cum starts leaking out of her pussy and onto the floor."
            nar "After taking a couple of deep breaths, she pulls herself up, readies herself and makes her way to the front of your desk."

            $ states.her.status.creampie = True
            return

        "-Cum all over her-":

            show her_sex_personal cum_outside2 as cg

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"
            show her_sex_personal mouth_mad eyebrows_worried eyes_narrow_r cheeks_blush as cg

            show her_sex_personal cum_outside as cg
            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg

            play sound "sounds/slick_02.ogg"
            gen "{size=+7}That's it [name_hermione_genie], take this!!!!!!!!!!!!!!!!{/size}"
            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_r cheeks_blush as cg
            show her_sex_personal cum_outside2 as cg
            pause .8
            show her_sex_personal cum_outside as cg

            call cum_block
            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_heavy as cg
            else:
                show her_sex_personal cum_ass_skirt_heavy as cg
            with d5

            play sound "sounds/slick_02.ogg"
            show her_sex_personal after mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            call ctc

            if _temp_outfit_choice == "naked":
                gen "*Ah*...{w=0.4} All over your ass..."
            else:
                gen "*Ah*...{w=0.4} All over your clothes..."

            show her_sex_personal mouth_grin eyebrows_worried eyes_base_mid cheeks_blush tears_soft as cg
            her "*Ah-ah*...{heart}"
            gen "You alright there, [name_hermione_genie]?"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_stare as cg
            her "Yes...{w=0.3} I--"
            gen "Did you enjoy it?"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_stare as cg
            her "...{w=0.3} I think so..."
            call ctc

            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "I...{w=0.4} I think I came several times..."
            if name_genie_hermione == "Master":
                gen "Naughty...{w=0.4} But I'll allow it..."
            elif name_genie_hermione == "Daddy":
                gen "Good girl..."
            show her_sex_personal mouth_open eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "*Ehm*...{w=0.4} Can I get my payment now [name_genie_hermione]?"
            gen "Of course!"

            show screen blkfade
            with d5

            nar "You take a step back to give Hermione some room, giving her ass a last glance, you watch as your cum slowly begins sliding down her sides."
            nar "After a couple of moments, Hermione finally manages to pull herself together and after readying herself, she makes her way to the front of your desk."

            return

### Third Time and repeatable Vaginal Sex ###

label hg_sex_3:




    ### Will be added with Missionary pose ###
    #gen "Let's see... How shall we do this..."
    #her "[name_genie_hermione]?"
    #menu:
        #"-Flip her onto the desk-":
            #jump hg_sex_missionary
        #"-Take her from behind-":
            #pass

    ##Doggystyle Vaginal scene setup##

    show screen blkfade
    with d5
    pause.2

    #Stop wind and thunder sounds
    stop weather fadeout 4

    play sound "sounds/gltch.ogg"
    with kissiris

    # Hermione Setup
    if _temp_outfit_choice == "naked":
        show her_sex_personal lean_back hold eyes_narrow_mid as cg
    else:
        show her_sex_personal lean_back hold skirt shirt eyes_narrow_mid as cg

    hide hermione_main

    show her_sex_personal lean_back as cg zorder 17:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0

    hide screen blkfade
    with d5

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "*Ah*..."

    show her_sex_personal lean_back as cg:
        transform_anchor True
        anchor (0.0, 0.0)
        offset (-500, -650)
        rotate (15)
        zoom 1.0
        ease_quad 3.0 offset (-230, -100) zoom 0.5 rotate -15

    gen "There it is...{w=0.3} I've been looking forward to this."
    show her_sex_personal mouth_base eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "..."

    play background "sounds/slickloop.ogg" fadein 2
    pause 1

    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
    her "*Ah*...{w=0.3} *Ah*...{w=0.3} *Mmm*...{heart}"
    gen "Enjoying yourself?"
    show her_sex_personal mouth_mad eyebrows_base eyes_narrow_down cheeks_blush as cg
    her "N--No..."
    gen "Liar..."
    gen "You've been wet since before we even started..."
    show her_sex_personal mouth_upset eyebrows_base eyes_narrow_r cheeks_blush as cg
    her "{heart}{heart}{heart}..."
    gen "That's what I thought..."
    show her_sex_personal mouth_angry eyebrows_worried eyes_closed cheeks_blush as cg
    her "*Ah*...{w=0.3} I can't--{w=0.2} *Ah*...{w=0.3} This is a perfectly ordinary response to--"
    play background "sounds/slickloopfast.ogg" fadeout 2
    show her_sex_personal mouth_base eyebrows_base eyes_narrow_up cheeks_blush as cg
    her "*Mmm*....{heart}"
    menu:
        "-Agree with her-":
            gen "Indeed [name_hermione_genie]... A perfectly normal response to getting ploughed by your headmaster."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "{heart}*Mmm*...{heart}"
            gen "Because why shouldn't you enjoy it..."
            gen "You've put so much work into getting where you are..."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "*Ah-ah*...{w=0.3} *Ah*..."
            gen "Why not let yourself have a bit of fun!"
            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Ah*...{w=0.3} Yes...{w=0.3} I've deserved this..."
            gen "That's right [name_hermione_genie]..."
            gen "This is your reward..."
            show her_sex_personal mouth_base eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Mmm*...{w=0.3} {heart}My reward{heart}..."
            gen "You should be proud to have your headmaster take care of your needy little fuckhole."
            nar "You feel Hermione's legs twitch slightly as you continue praising her."
            gen "For being such a good student and doing whatever is necessary to please him..."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..."
            gen "Earning so many points for your house in the process..."
            show her_sex_personal mouth_base eyebrows_worried eyes_narrow_up cheeks_blush as cg
            her "{heart}{heart}*Mmm*...{heart}{heart}"
            gen "You really are the top student of this school."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "I..."

            show her_sex_personal lean_forward caress as cg:
                offset (-230, -100)
                zoom 0.5
                rotate -15
                ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

            show her_sex_personal mouth_angry eyebrows_base eyes_base_r cheeks_blush as cg
            her "Whoa!"
            gen "You've got to be quick on your feet if you want to stay on top [name_hermione_genie]..."

            show her_sex_personal caress_grin as cg

            gen "(On top of this dick.)"
            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "*Ah*...{w=0.3} Yes, [name_genie_hermione]..."
            if name_genie_hermione == "Master":
                gen "Master...{w=0.3} Oh how I love it when you call me that..."
                gen "That's it [name_hermione_genie]...{w=0.3} Take good care of your master..."
            elif name_genie_hermione == "Daddy":
                gen "Yes, that's it...{w=0.3} I'm your daddy..."
                if name_hermione_genie == "Angel":
                    gen "And you're my sweet little angel..."
                elif name_hermione_genie == "Princess":
                    gen "And you're my sweet little princess..."
                show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
                her "*Ah*...{w=0.3}[name_genie_hermione] please..."
            elif name_genie_hermione == "Fuckmachine9000":
                gen "That's it, feel the power of the greatest fuck machine of all time!"

            show her_sex_personal mouth_grin eyebrows_annoyed eyes_narrow_r cheeks_blush as cg
            nar "As you continue pounding Hermione, you suddenly feel her clench her pelvic muscles, creating an even tighter grip around your cock."
            gen "There you go, girl... You're learning!"
            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "*Ah*...{w=0.3} {heart}*Ah-ah*...{heart}"
            gen "I think it's for someone to get another reward..."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "*Ah*...{w=0.3} Another--"

        "-Scold her-":
            random:
                block:
                    gen "Maybe for a slut."
                    show her_sex_personal mouth_disgust eyebrows_worried eyes_narrow_mid cheeks_blush as cg
                    her "*Ah*...{w=0.3} Don't--{w=0.2} *Ah*...{w=0.3} Don't call me that [name_genie_hermione]..."
                    gen "How else would you explain being so wet already?"
                    gen "Probably been touching yourself in class no doubt..."
                    show her_sex_personal mouth_upset eyebrows_worried eyes_happycl cheeks_blush as cg
                    her "*Ah*...{w=0.3} I--{w=0.2} I have not!"
                    gen "Edging and readying yourself to take your headmasters cock."
                    show her_sex_personal mouth_angry eyebrows_worried eyes_happycl cheeks_blush as cg
                    her "*Ah*...{w=0.3} That's--{w=0.3} That's not..."
                    gen "Are you even wearing your panties in class anymore?"
                    show her_sex_personal mouth_angry eyebrows_base eyes_narrow_down cheeks_blush as cg
                    her "I--{w=0.2} *Ah*...{w=0.3} Of course I am!"
                    show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_r cheeks_blush as cg
                    her "Don't...{w=0.3} *Ah*...{w=0.3} Don't be so crude [name_genie_hermione]..."
                    gen "Then I suppose the wet spot on your chair that miss Tonks told me about was a mere fabrication..."
                    show her_sex_personal mouth_angry eyebrows_worried eyes_wide_mid cheeks_blush as cg
                    her "*She--{w=0.2} She knows?!"
                    gen "*Heh-Heh*... Got you..."
                    show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_down cheeks_blush as cg
                    her "..."
                    gen "Now lean forward, slut!"
                    show her_sex_personal mouth_angry eyebrows_base eyes_narrow_mid cheeks_blush as cg
                    call ctc

                    show her_sex_personal lean_forward caress mouth_normal eyebrows_base eyes_closed cheeks_blush as cg:
                        offset (-230, -100)
                        zoom 0.5
                        rotate -15
                        ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

                    show her_sex_personal caress_grin as cg
                    gen "That's much better, don't you think?"

                    show her_sex_personal mouth_base eyebrows_worried eyes_closed cheeks_blush as cg
                    her "{heart}{heart}{heart}..."

                    show her_sex_personal caress as cg
                    gen "Miss Granger?"
                    show her_sex_personal mouth_base eyebrows_base eyes_closed cheeks_blush as cg
                    her "*Mmm*..."
                    gen "Slut?"
                    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
                    her "*Huh*?"

                    show her_sex_personal caress_grin as cg
                    gen "*Tsk*...{w=0.3} Not even responding to your own name now are we?"

                    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_l cheeks_blush as cg
                    her "*Ah*...{w=0.3} No, I just didn't hear--"
                    gen "Don't they teach you to pay attention in class?"
                    gen "I thought you were supposed to be a model student..."
                    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
                    her "*Ah*...{w=0.3} *Ah*...{w=0.3} I am a--"
                    gen "Model that ass then!"
                    show her_sex_personal mouth_angry eyebrows_base eyes_narrow_r cheeks_blush as cg
                    her "My--"

                block:
                    gen "Do you even care about the points anymore?"
                    show her_sex_personal mouth_angry eyebrows_base eyes_happy_down cheeks_blush as cg
                    her "*Ah*...{w=0.3} Of course I--{w=0.2} *Ah*...{w=0.3} Why else would I be doing this..."
                    gen "Don't you think it's a bit suspicious that as soon as Gryffindor takes the lead it's quickly taken from them?"
                    show her_sex_personal mouth_angry eyebrows_annoyed eyes_narrow_down cheeks_blush as cg
                    her "*Ah*...{w=0.3} That...{w=0.3} That's Snape's work, no doubt..."
                    show her_sex_personal mouth_disgust eyebrows_annoyed eyes_narrow_mid cheeks_blush as cg
                    her "All those Slytherin--{w=0.2} *Ah*...{w=0.3} Whores..."
                    gen "You're no different to them.... You're nothing but a cum hungry slut!"
                    show her_sex_personal mouth_angry eyebrows_annoyed eyes_happy_r cheeks_blush as cg
                    her "[name_genie_hermione]!"

                    show her_sex_personal lean_forward caress as cg:
                        offset (-230, -100)
                        zoom 0.5
                        rotate -15
                        ease_quad 1.0 offset (-65, -240) zoom 0.45 rotate -4

                    show her_sex_personal mouth_mad eyebrows_base eyes_base_mid cheeks_blush as cg
                    her "Whoa!"
                    show her_sex_personal mouth_mad eyebrows_base eyes_narrow_r cheeks_blush as cg
                    her "At least give me a warning if you let go of my--"

                    call slap_her

                    show her_sex_personal mouth_clench eyebrows_base eyes_wide_up cheeks_blush as cg
                    her "{heart}*Ah*!{heart}"
                    gen "Let go of your what, sorry?"
                    show her_sex_personal mouth_angry eyebrows_base eyes_base_mid cheeks_blush as cg
                    her "My... My A--"

                    call slap_her

                    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
                    her "{heart}*Ah*!!{heart}"
                    gen "Sorry, you'll have to speak up..."

                    call slap_her
                    call slap_her
                    call slap_her

                    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
                    her "*Mmm*...{w=0.2} More...{heart}"
                    gen "What was that?"
                    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
                    her "Don't...{w=0.2} Please don't make me say it [name_genie_hermione]..."
                    gen "You're never going to amount to anything if you don't take what you want [name_hermione_genie]..."
                    gen "For example..."

    show her_sex_personal bent_over grab as cg:
        offset (-65, -240)
        zoom 0.45
        rotate -4
        easein 1.0 offset (0, -480) rotate 0
    with vpunch

    pause 1.0

    #Could add some sound effect here
    show her_sex_personal mouth_open eyebrows_base eyes_wide_r cheeks_blush as cg:
        offset (0, -480)
        rotate 0
        ease_quad 3.0 offset (-60, -620) zoom 0.55

    nar "You push Hermione down onto the desk and start fucking her fiercely!"

    play background "sounds/sexloopveryfast.ogg" fadeout 2
    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_up cheeks_blush as cg
    her "[name_genie_hermione]!"
    gen "There you go [name_hermione_genie]!"
    gen "Isn't this what you wanted?"
    show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_up cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
    gen "Say it!"
    show her_sex_personal mouth_clench eyebrows_base eyes_narrow_down cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} [name_genie_hermione]..."
    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_down cheeks_blush as cg
    her "Not so fast..."
    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "I'm not going to be able to...{w=0.2} Hold it if you--"
    gen "You better hold it because I'm not done yet!"
    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} Please..."
    gen "Please, what?"
    show her_sex_personal mouth_crooked_smile eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} Please spank me again!"

    menu:
        "\"My pleasure!\"":
            pass

        "\"I don't think so!\"":
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_r cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*... But..."
            show her_sex_personal mouth_angry eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "I did what you--"
            gen "You need to know your place [name_hermione_genie]!"
            show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush as cg
            her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
            gen "I'm the one giving out the points am I not?"
            show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Ah*...{w=0.3} Yes...{w=0.3} But..."
            gen "I should be the one to make demands!"
            show her_sex_personal mouth_angry eyebrows_base eyes_narrow_r cheeks_blush as cg
            her "*Ah*... Yes, [name_genie_hermione]... I'm--"
            gen "Naughty girls such as yourself should be punished!"

    call slap_her

    show her_sex_personal mouth_open_tongue eyebrows_worried eyes_wide_up cheeks_blush as cg
    her "{size=+5}*Aah*....{/size}{w=0.4}{nw}"
    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "{size=+5}*Aah*....{/size}{fast}"

    call slap_her

    show her_sex_personal mouth_open_tongue eyebrows_base eyes_wide_up cheeks_blush as cg
    her "{size=+5}*Ah*....{/size}{w=0.4}{nw}"
    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "{size=+5}*Ah*....{/size}{fast}"

    gen "You should be grateful--"

    call slap_her

    show her_sex_personal mouth_open_tongue eyebrows_base eyes_wide_up cheeks_blush as cg
    her "{size=+5}*Ah*....{/size}{w=0.4}{nw}"
    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
    her "{size=+5}*Ah*....{/size}{fast}"

    gen "That I--"

    call slap_her

    show her_sex_personal mouth_open_tongue eyebrows_base eyes_wide_up cheeks_blush as cg
    her "{size=+5}*Ah*....{/size}{w=0.4}{nw}"
    show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "{size=+5}*Ah*....{/size}{fast}"

    gen "Take such good care of you!"

    call slap_her
    call slap_her
    call slap_her
    show her_sex_personal mouth_grin eyebrows_base eyes_base_ahegao cheeks_blush as cg
    pause .4

    play sound "sounds/slick_01.ogg"
    with kissiris
    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
    her "{size=+7}*Aah*!!!{heart}{heart}{heart} [name_genie_hermione]{/size}!"


    if name_genie_hermione == "Master":
        gen "Yes, I'm your Master [name_hermione_genie]..."
        gen "And you're nothing but my slave to do with as I please..."
    elif name_genie_hermione == "Daddy":
        gen "That's it [name_hermione_genie]... Let your daddy take good care of you..."

    nar "Hermione clenches her thighs around your cock as waves of pleasure washes over her."

    gen "Cumming again are we [name_hermione_genie]?"
    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_down cheeks_blush as cg
    her "{heart}*Ah*...{w=0.2} *Ah-ha*...{heart}"

    menu:
        "-Punish her-":
            gen "Such selfishness shall be punished!"

            call slap_her

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "{heart}*Ah*...{w=0.2} [name_genie_hermione] I--{heart}"

            call slap_her

            show her_sex_personal mouth_grin eyebrows_worried eyes_happycl cheeks_blush as cg
            her "*Ah*..."

            if name_genie_hermione == "Master":
                gen "Cumming before her master..."
            elif name_genie_hermione == "Daddy":
                gen "Is that how you treat your daddy?"

            call slap_her

            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "*Ah*... [name_genie_hermione], I'm sorry!"
            gen "You better be sorry!"

            call slap_her

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "*Ah*... [name_genie_hermione]... I-- I can't stop it... I'm--"
            gen "Don't you dare cum again!"

            call slap_her
            call slap_her
            call slap_her
            show her_sex_personal mouth_grin eyebrows_base eyes_base_ahegao cheeks_blush as cg
            pause .4

            play sound "sounds/slick_01.ogg"
            with kissiris
            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{size=+7}{heart}*Ah*!!!{heart}{heart}{/size}"


            gen "What did I just tell you!"
        "-Slow your pace down for a moment-":

            play background "sounds/sexloopfast.ogg" fadeout 2

            show her_sex_personal mouth_soft eyebrows_worried eyes_closed cheeks_blush as cg
            her "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "[name_genie_hermione]..."
            show her_sex_personal mouth_base eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "Please..."
            show her_sex_personal mouth_angry eyebrows_base eyes_closed cheeks_blush as cg
            her "Please keep going...{w=0.3} I'm--"
            show her_sex_personal mouth_mad eyebrows_base eyes_narrow_down cheeks_blush as cg
            her "*Ah*...{w=0.3} I'm so close to--"

            play background "sounds/sexloopveryfast.ogg" fadeout 2
            show her_sex_personal mouth_open_wide_tongue eyebrows_worried eyes_wide_ahegao cheeks_blush as cg:
                rotate 1
                xoffset -70
                pause 1.0
                offset (-60, -620) 
                zoom 0.55
                ease_quad 1.0 offset (-60, -635)
            with hpunch
            nar "You pin Hermione down as you pick up the pace once again."
    if name_genie_hermione == "Master":
        nar "The sound of Hermione's moans fill the room as her master shows no mercy."
    else:
        nar "The sounds of Hermione's moans fill the room as you feel yourself getting closer to the edge."

    show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
    her "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..."
    show her_sex_personal mouth_soft eyebrows_worried eyes_narrow_up cheeks_blush as cg
    her "*Ah*...{w=0.3} [name_genie_hermione]...{w=0.3} Please tell me you're close..."
    show her_sex_personal mouth_angry eyebrows_base eyes_narrow_up cheeks_blush as cg
    her "I don't...{w=0.3} *Ah*...{w=0.3} I don't think I can--"
    show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
    her "{size=+7}I'm-- I'm cumming, [name_genie_hermione]!{/size}"
    gen "{size=+7}Me too!{/size}"
    menu:
        "-Fill her up!-":

            show her_sex_personal cum_inside as cg

            gen "{size=+7}*Argh*, Yes!!!{/size}"
            call cum_block
            play sound "sounds/slick_01.ogg"

            show her_sex_personal cum_pussy_light mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "!!!"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{heart}[name_genie_hermione] I'm--{heart}"
            play sound "sounds/slick_01.ogg"
            with kissiris
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{heart}*Ngh*{heart}"

            gen "That's it [name_hermione_genie]!"
            gen "{size=+15}Cum for me!!!!!!!!!!!!!!!!{/size}"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "[name_genie_hermione], you're--"
            play sound "sounds/slick_01.ogg"
            with kissiris
            show her_sex_personal mouth_open_tongue eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{heart}*Ah*!{heart}"
            gen "Take my seed, [name_hermione_genie]!"

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            call cum_block

            show her_sex_personal cum_pussy_heavy mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg

            her "{heart}{heart}{heart}*Mmm*...{heart}{heart}{heart}"
            nar "You empty your final load into Hermione's pussy and feel it convulsing around your cock as a final wave of pleasure hits her."
            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg
            her "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..."
            gen "Are you alright?"
            if not states.her.status.creampie:
                show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
                her "*Ah*...{w=0.4} Yes, I...{w=0.4} Hold on..."
                show her_sex_personal mouth_disgust eyebrows_worried eyes_wide_mid cheeks_blush as cg
                her "What if I get pregnant?"
                gen "Nah, you will be alright..."
                show her_sex_personal mouth_angry eyebrows_worried eyes_narrow_down cheeks_blush as cg
                her "B-But... How would you know, [name_genie_hermione]?"
                gen "We {i}witchers{/i} are infertile."
                show her_sex_personal mouth_angry eyebrows_worried eyes_base_down cheeks_blush as cg
                her "{i}Witchers{/i}?"
                gen "Sure... You are a witch, that makes me {i}a witcher{/i}, right?"
                gen "And everyone knows that {i}witchers{/i} are infertile..."
                show her_sex_personal mouth_disgust eyebrows_base eyes_narrow_r cheeks_blush as cg
                her "[name_genie_hermione], you make no sense..."
            else:
                show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
                her "*Ah*...{w=0.4} Yes, I...{w=0.4} Just give me a minute..."

            play sound "sounds/slick_02.ogg"
            show her_sex_personal after as cg

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg

            with kissiris

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{heart}*Ngh*!{heart}"

            show screen blkfade
            with d5

            nar "You pull your cock out of Hermione's pussy and take a step back."
            nar "Globules of semen begin leaking out and fall onto the floor as Hermione clenches her pelvic muscles involuntarily."
            nar "After some time, she finally manages to stand up."
            nar "Still stumbling somewhat, she readies herself and makes her way to the front of your desk."

            $ states.her.status.creampie = True
            return

        "-Pull out!-":

            show her_sex_personal cum_outside2 as cg

            stop background fadeout 2
            play sound "sounds/slick_01.ogg"
            gen "{size=+7}*Argh*!!!{/size}"
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "*Ngh*!!"
            with kissiris

            show her_sex_personal cum_outside as cg
            call cum_block
            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_light as cg
            else:
                show her_sex_personal cum_ass_skirt_light as cg

            play sound "sounds/slick_02.ogg"
            gen "{size=+15}Take this, [name_hermione_genie]!!!!!!!!!!!!!!!!{/size}"
            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_r cheeks_blush as cg
            show her_sex_personal cum_outside2 as cg
            pause .8
            show her_sex_personal cum_outside as cg

            call cum_block

            if _temp_outfit_choice == "naked":
                show her_sex_personal cum_ass_heavy as cg
            else:
                show her_sex_personal cum_ass_skirt_heavy as cg

            play sound "sounds/slick_02.ogg"
            show her_sex_personal mouth_grin eyebrows_worried eyes_narrow_mid cheeks_blush as cg

            show her_sex_personal after as cg

            if _temp_outfit_choice == "naked":
                gen "All over your ass!"
            else:
                gen "All over your clothes!"

            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "..."
            show her_sex_personal mouth_grin eyebrows_base eyes_narrow_up cheeks_blush as cg
            her "{heart}*Mmmmm*....{heart}"
            if name_genie_hermione == "Master":
                gen "Good slave..."
                gen "Letting your master coat your precious body with his semen..."
            elif name_genie_hermione == "Daddy":
                gen "That's it [name_hermione_genie]..."
                gen "You've been such a good girl, letting your daddy release his seed on you..."
            else:
                gen "Good job [name_hermione_genie]..."
                gen "You've very much earned your points today."
            show her_sex_personal mouth_base eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "Thank you, [name_genie_hermione]..."
            gen "You can get up now..."
            show her_sex_personal mouth_soft eyebrows_base eyes_narrow_mid cheeks_blush as cg
            her "I...{w=0.4} I might need a moment..."

            show screen blkfade
            with d5

            nar "With no other sound but Hermione's breathing returning to a normal pace, you take a step back to admire your work."
            nar "The girl's defiled body still sprawled and presenting herself in front of you, you can't help but take another glance at her glistening pussy before she stands up."
            her "I..."
            nar "Blushing and without finishing her sentence, Hermione readies herself and makes her way to the front of your desk."

            return
