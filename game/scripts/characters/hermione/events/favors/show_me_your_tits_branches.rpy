

label hg_pf_admire_breasts_transition:
    stop music fadeout 1.0
    call hide_characters
    hide screen blktone
    with d3
    pause.2

    # Setup Pose

    if hermione.is_worn("robe"):
        pause .4
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        pause 1.2

    if hermione.is_worn("top", "bottom"):
        $ hermione.strip("top", "bra", "accessory")
        call her_chibi("lift_top","mid","base")
        pause 1.4
        play sound "sounds/boing02.ogg"
        pause 2.0
    elif hermione.is_any_worn("top", "bottom"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top", "bra", "accessory")
        pause 2.0
    else:
        $ hermione.strip("accessory", "bra")
        pause 2.0

    her @ cheeks blush "" ("angry", "happyCl", "base", "down", trans=d3)
    call ctc

    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    if states.her.tier <= 2:
        her @ cheeks blush "{size=-5}(My breasts are completely exposed...){/size}" ("disgust", "narrow", "base", "down")
    gen "Come closer [name_hermione_genie], let me take a better look..." ("base", xpos="far_left", ypos="head")

    # Move to desk
    call her_chibi("stand","mid","base")
    with d3
    pause.2

    call her_walk("desk", "base", reduce=0.8)

    show screen blkfade
    with d3

    call her_chibi_scene("behind_desk_front_show_tits", trans=fade)
    pause .5

    if states.her.tier <= 2:
        her @ cheeks blush "............" ("annoyed", "narrow", "angry", "R", xpos="mid", ypos="base")
        gen "Very good..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "....." ("annoyed", "base", "angry", "mid")
        call ctc

        her "...................................." ("annoyed", "narrow", "annoyed", "mid")

    elif states.her.tier == 3:
        her "" ("base", "closed", "base", "mid", xpos="mid", ypos="base")

        gen "Very good..." ("base", xpos="far_left", ypos="head")
        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
        her "...................................."

    else:
        her @ cheeks blush "" ("base", "narrow", "base", "mid_soft", xpos="mid", ypos="base")

        gen "Very good..." ("base", xpos="far_left", ypos="head")
        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
        her @ cheeks blush "............" ("base", "narrow", "base", "mid_soft")
    call ctc
    return

### Tier 2 ###

label hg_pf_admire_breasts_T2:

    $ states.her.status.show_tits = True

    call hg_pf_admire_breasts_transition

    menu:
        "-Break your promise. Grab the tits!-":     # Hermione gets mad.
            jump hg_pf_admire_breasts_T2_touch

        "-Keep promise. Admire visually-":
            call hg_pf_admire_breasts_T2_promise

            jump end_hg_pf_admire_breasts

        "-Start jerking off-":                      # 2/3 branches Hermione gets mad.
            jump hg_pf_admire_breasts_T2_masturbate

label hg_pf_admire_breasts_T2_promise: # Call label

    nar "You take a long look at Hermione's naked tits..."

    #First time event.
    #if states.her.level >= 6 and states.her.level <= 8:
    call ctc

    menu:
        "-Nod your head in approval-":
            nar "You Look at the girl's tits for a while and then nod in approval..."
            her "......................"

            return

        "-Shake your head in disapproval-":
            $ states.her.mood += 3
            nar "You Look at the girl's tits for a while and then shake your head in disappointment..."
            her ".....................?!"

            return

label hg_pf_admire_breasts_T2_touch: # Not a Call label

    #Event Fails
    # if states.her.level >= 6 and states.her.level <= 8:
    hide hermione_main
    show screen blkfade
    with d3

    nar "You reach out and dig your fingers into the girl's ample flesh..."
    her @ cheeks blush "[name_genie_hermione], what are you doing?" ("mad", "wide", "base", "stare")

    # Start Groping
    call her_chibi_scene("grope_tits")
    call ctc

    gen "Relax, [name_hermione_genie]. Just stand still!" ("base", xpos="far_left", ypos="head")
    gen "Oh... Those are some nice titties you've got..." ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "No, [name_genie_hermione], please! You mustn't do this..." ("shock", "happyCl", "worried", "mid")
    gen "This won't take long, just stand still." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "[name_genie_hermione], I didn't agree to this!" ("angry", "base", "angry", "mid")
    with hpunch
    her @ cheeks blush "You must unhand me now!!!" ("scream", "base", "angry", "mid",emote="angry")

    # End Groping
    show screen blkfade
    with d3

    play sound "sounds/cloth_sound3.ogg"
    nar "Hermione pulls away from you and covers up hastily."

    $ hermione.wear("all")
    call her_chibi_scene("reset", "desk", "base", trans=fade)
    pause .5

    her @ cheeks blush "I think I'd better go..." ("angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")
    gen "Go ahead, [name_hermione_genie]. You are not getting paid if you do..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But I showed you my..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "And you touched me..." ("angry", "base", "angry", "mid")
    her @ cheeks blush "And I am getting nothing in return?" ("scream", "base", "angry", "mid",emote="angry")
    gen "You are dismissed, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Grr*.........." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "{size=-5}(Burn in hell, you wretched old--){/size}" ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    $ states.her.mood += 22

    jump end_hermione_event

label hg_pf_admire_breasts_T2_masturbate: # Not a Call label

    $ states.her.mood += 2
    $ states.gen.stats.masturbated_to_hermione += 1
    $ states.gen.masturbating = True

    hide hermione_main
    with d3

    nar "You take your cock out and start stroking it..."
    show screen blkfade
    with d3

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "[name_genie_hermione]?!!" ("angry", "wide", "base", "stare")
    gen "Just stand still, [name_hermione_genie]..."

    # Start Jerking Off.
    hide screen blktone
    call her_chibi_scene("grope_tits_jerk_off", trans=fade)

    if not states.her.status.voyer:
        $ achievements.unlock("busted")
        $ states.her.status.voyer = True

    call ctc

    nar "You stare at Hermione's breasts with hunger..."
    her "[name_genie_hermione], what are you...?" ("shock", "happyCl", "worried", "mid")
    nar "You keep stroking your hard cock..."
    her @ cheeks blush "[name_genie_hermione], no..." ("disgust", "narrow", "base", "down")
    her @ cheeks blush "You must... Put it away..." ("disgust", "narrow", "base", "down")
    gen "Stop whining [name_hermione_genie]. I'm not touching you, am I?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "But I didn't agree to this!" ("angry", "base", "angry", "mid")
    her @ cheeks blush "I..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "I think I'd better leave now!" ("angry", "happyCl", "worried", "mid")

    menu:
        "\"Leave now, and you'll get no points!\"":
            $ states.her.mood += 30

            her @ cheeks blush "After {size=+5}this{/size}? Are you kidding me, [name_genie_hermione]?" ("scream", "wide", "base", "stare")
            her @ cheeks blush "I showed you my--" ("scream", "wide", "base", "stare")
            her @ cheeks blush ".........." ("annoyed", "narrow", "angry", "R")
            her @ cheeks blush "I am not going to sell you a single favour anymore, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
            show screen blkfade
            with d3

            play sound "sounds/cloth_sound3.ogg"
            nar "Hermione pulls away from you and covers up..."
            gen "Don't you dare to leave me in this state, [name_hermione_genie]!"

            $ hermione.wear("all")
            call gen_chibi("jerk_off", 225, "base", flip=True)
            call her_chibi("stand","desk","base", flip=False)
            pause .5

            hide screen blkfade
            with d3

            her @ cheeks blush "I am not setting a foot into your office ever again, [name_genie_hermione]!" ("angry", "squint", "base", "mid", xpos="mid", ypos="base")

            gen "Come on now... Just say something dirty! I'm almost there!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "You are a horrible person, [name_genie_hermione]..." ("angry", "squint", "base", "mid")

            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi(action="leave")

            call gen_chibi("dick_out_shocked", 225, "base", flip=True)
            gen "... Balls." ("base", xpos="far_left", ypos="head")

            show screen blkfade
            with d5

            call gen_chibi("sit_behind_desk")

            hide screen blkfade
            with d3
            jump end_hermione_event

        "\"Alright, alright. That's enough for now.\"":
            $ states.her.mood += 9

            jump end_hg_pf_admire_breasts

        "-Start jerking your cock faster-":
            $ states.her.mood += 35

            nar "You start jerking your cock furiously!"
            her @ cheeks blush "No, [name_genie_hermione], stop!" ("scream", "base", "angry", "mid",emote="angry")
            nar "You jerk it even faster!"
            her @ cheeks blush "[name_genie_hermione], think I will be leaving now..." ("annoyed", "narrow", "angry", "R")
            gen "No, wait, I'm almost there!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Ew! [name_genie_hermione]!" ("angry", "squint", "base", "mid")
            show screen blkfade
            with d3

            play sound "sounds/cloth_sound3.ogg"
            nar "Hermione pulls away from you and covers up..."

            $ hermione.wear("all")
            call her_chibi("stand","desk","base", flip=False)
            call gen_chibi("dick_out_shocked", 225, "base", flip=True)
            pause .5

            her @ cheeks blush "I'm leaving!"

            hide screen blkfade
            with d3

            call her_walk(action="leave")

            gen "... Balls." ("base", xpos="far_left", ypos="head")

            show screen blkfade
            with d5

            call gen_chibi("sit_behind_desk")

            hide screen blkfade
            with d3
            jump end_hermione_event

label hg_pf_admire_breasts_T3:

    $ states.her.status.show_tits = True
    $ _cumming = False # Checked during end label

    call hg_pf_admire_breasts_transition

    menu:
        "-Break your promise. Grab the tits!-":
            call hg_pf_admire_breasts_T3_touch

        "-Keep promise. Admire visually-":
            call hg_pf_admire_breasts_T3_promise

        "-Start jerking off-":
            call hg_pf_admire_breasts_T3_masturbate


    jump end_hg_pf_admire_breasts

label hg_pf_admire_breasts_T3_promise:
    nar "You take a long look at Hermione's naked tits..."
    # elif states.her.level >= 9 and states.her.level <= 11:
    call ctc

    menu:
        "\"A nice set of tits you got there.\"":
            her "" ("annoyed", "closed", "base", "mid")
            pause .5

            her "Thank--"
            her "..........." ("annoyed", "base", "base", "mid")
            her "You are being inappropriate, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")

            return

        "\"*Hmm*... I've seen better.\"":
            $ states.her.mood += 7

            her "*Tsk*..." ("soft", "closed", "annoyed", "R")
            her "Are we done then?" ("open", "closed", "worried", "mid")

            return


label hg_pf_admire_breasts_T3_touch:
    # elif states.her.level >= 9 and states.her.level <= 11:
    hide hermione_main
    show screen blkfade
    with d3

    nar "You reach out and dig your fingers into the girl's ample flesh..."
    her @ cheeks blush "[name_genie_hermione], what are you doing?" ("mad", "wide", "base", "stare")

    # Start Groping
    call her_chibi_scene("grope_tits")
    call ctc

    gen "Relax, [name_hermione_genie]. Just stand still!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I didn't agree to this, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "I don't think you should..." ("annoyed", "narrow", "angry", "R")
    gen "Don't you like it...?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What?" ("disgust", "narrow", "base", "down")
    gen "Don't you like how I squeeze and pull on your breasts?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..............." ("disgust", "narrow", "base", "down")
    gen "Admit it, you like it a little bit..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I--" ("disgust", "narrow", "base", "down")
    her @ cheeks blush "{size=-5}(I never thought I'd see my breasts in someone else's hands like this...){/size}" ("disgust", "narrow", "base", "down")
    her "[name_genie_hermione], I am letting you do this to me to help my house out, nothing more!" ("shock", "happyCl", "worried", "mid")
    her @ cheeks blush "Please, unhand me now!" ("annoyed", "narrow", "angry", "R")
    show screen blkfade
    with d5

    play sound "sounds/cloth_sound3.ogg"
    nar "Hermione pulls away from you suddenly, and covers up."

    $ hermione.wear("all")
    call her_chibi_scene("reset", "desk", "base")

    hide screen blkfade
    with d5

    her @ cheeks blush "You promised not to touch, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    gen "It was too hard to resist..." ("base", xpos="far_left", ypos="head")

    pause.8

    her @ cheeks blush "............." ("soft", "base", "base", "R")
    her @ cheeks blush "Can I get paid now, please?" ("angry", "happyCl", "worried", "mid",emote="sweat")
    gen "Sure..." ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 9

    return


label hg_pf_admire_breasts_T3_masturbate:

    # elif states.her.level >= 9 and states.her.level <= 11:
    hide hermione_main
    show screen blkfade
    with d3

    nar "You take your cock out and start stroking it..."

    her "[name_genie_hermione]?" ("angry", "wide", "base", "stare")
    nar "You stare at Hermione's breasts with hunger..."

    #Start Jerking Off.
    hide screen bld1
    hide screen blktone
    call her_chibi_scene("grope_tits_jerk_off", trans=fade)
    call ctc

    her "[name_genie_hermione], I didn't agree to this..." ("shock", "happyCl", "worried", "mid")
    gen "What are you complaining about, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    gen "I'm not even touching you..." ("base", xpos="far_left", ypos="head")
    her "Yes, but you are... Touching yourself, [name_genie_hermione]." ("shock", "happyCl", "worried", "mid")

    nar "You pick up the pace..."

    gen "just stand still, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "It will be over soon." ("base", xpos="far_left", ypos="head")
    her ".................." ("shock", "happyCl", "worried", "mid")
    her @ cheeks blush "(It's so big...)" ("disgust", "narrow", "base", "down")
    gen "Yes... Yes, just like that..." ("base", xpos="far_left", ypos="head")
    gen "Tits bare, and nipples perked..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush ".............." ("disgust", "narrow", "base", "down")
    her @ cheeks blush "Well, so be it..." ("open", "base", "base", "R")
    her @ cheeks blush "You can keep touching yourself, [name_genie_hermione]..." ("open", "base", "base", "R")
    her @ cheeks blush "But you must promise me not to..." ("soft", "base", "base", "R")
    her @ cheeks blush "Not to... *Ehm*..." ("open", "base", "base", "R")
    her @ cheeks blush "Not to discharge..." ("annoyed", "narrow", "angry", "R")
    her "Not in front of me, [name_genie_hermione]..." ("angry", "base", "angry", "mid")
    gen "Fine, whatever..." ("base", xpos="far_left", ypos="head")
    gen "(But we both know you want it... You nasty little slut!)" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "......................." ("angry", "happyCl", "worried", "mid")

    nar "You begin stroking your cock even faster..."

    gen "Yes, you do! Yes!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "................" ("angry", "happyCl", "worried", "mid")

    gen "*Ngh*--" ("angry", xpos="far_left", ypos="head")
    menu:
        "-Hold it as promised-":
            gen "Oh, alright..." ("base", xpos="far_left", ypos="head")
            gen "I'd better stop now I suppose..." ("base", xpos="far_left", ypos="head")
            gen "(Fuck me, that hurts...)" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "..............." ("angry", "happyCl", "worried", "mid")
            show screen blkfade
            with d3

            play sound "sounds/cloth_sound3.ogg"
            nar "Hermione quickly scoots around your desk and covers up..."

            return

        "-Just start cumming-":
            $ states.her.status.cumshot = True
            $ _cumming = True
            gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Proff--?" ("scream", "wide", "base", "stare")
            call cum_block
            gen "*Argh*! YES!" ("angry", xpos="far_left", ypos="head")
            hide screen bld1
            with d1

            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("grope_tits_cum")
            with d5

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            pause 1.0
            $ hermione.set_cum(body="light")

            call ctc



            her @ cheeks blush "[name_genie_hermione], you promised!" ("scream", "base", "angry", "mid",emote="angry")
            gen "*Ah*... That was amazing!" ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("grope_tits_cum_done")

            her @ cheeks blush "[name_genie_hermione], how could you...?" ("angry", "squint", "base", "mid")
            menu:
                "\"Very easily.\"":
                    gen "I just tug on it, like so, and white stuff comes out!" ("base", xpos="far_left", ypos="head")
                    gen "You should try it sometime." ("base", xpos="far_left", ypos="head")
                "\"What do you mean?\"":
                    gen "This is a great look for you!" ("base", xpos="far_left", ypos="head")
                    gen "We should do this more often." ("base", xpos="far_left", ypos="head")

            her "" ("disgust", "narrow", "base", "down", xpos="mid", ypos="base")
            call ctc

            her "My body..."
            her "It's been defiled..."
            gen "Don't worry, I will give you your house points, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            gen "You did good." ("base", xpos="far_left", ypos="head")

            her "................"
            her "I need to clean myself up..."

            hide hermione_main
            show screen blkfade
            with d3

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("all")
            $ hermione.set_cum(None)
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            pause .8

            hide screen blkfade
            with d5

            her "" ("angry", "base", "angry", "mid")
            call ctc

            her "How could you do this to me, [name_genie_hermione]?!"
            her "You gave me your word!"
            hide hermione_main
            with d3

            $ states.her.mood += 45

            return



### Tier 4 ###

label hg_pf_admire_breasts_T4:

    call hg_pf_admire_breasts_transition

    menu:
        "-Break your promise. Grab the tits!-":
            call hg_pf_admire_breasts_T4_touch

        "-Keep promise. Admire visually-":
            call hg_pf_admire_breasts_T4_look

        "-Start jerking off-":
            call hg_pf_admire_breasts_T4_masturbate

    jump end_hg_pf_admire_breasts

label hg_pf_admire_breasts_T4_look: # Call label

    nar "You take a long look at Hermione's naked tits..."

    menu:
        "\"You have great tits, [name_hermione_genie].\"":
            her "You really think so [name_genie_hermione]?" ("annoyed", "base", "base", "mid")
            her "I am glad you like them, [name_genie_hermione]..." ("base", "closed", "base", "mid")
        "\"Your tits are alright I suppose...\"":
            her "*Huh*?" ("annoyed", "base", "base", "mid")
            her "Does this mean you don't like them, [name_genie_hermione]?"
            her "I'm sorry..." ("disgust", "narrow", "base", "down")

    nar "You stare at her breasts for a while longer..."
    call ctc

    gen "Alright, we're done here, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "............."
    pause.5

    #End Admiring
    hide screen blktone
    hide screen bld1

    return

label hg_pf_admire_breasts_T4_touch: # Call label
    # Event Also Succeeds
    hide hermione_main
    show screen blkfade
    with d3

    nar "You reach out and dig your fingers into the girl's ample flesh..."
    her @ cheeks blush "[name_genie_hermione], what are you doing?" ("mad", "wide", "base", "stare")

    # Start Groping
    call her_chibi_scene("grope_tits")
    call ctc

    call bld
    gen "Relax, [name_hermione_genie]. Just stand still!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But..." ("disgust", "narrow", "base", "down")
    her "*Ah*...{heart}" ("shock", "happyCl", "worried", "mid")
    her @ cheeks blush "I didn't agree to this..." ("disgust", "narrow", "base", "down")
    gen "But you like it, don't you?" ("base", xpos="far_left", ypos="head")

    if states.her.level >= 17:
        her @ cheeks blush "I love it [name_genie_hermione]!{heart}" ("open", "base", "base", "R")
    else:
        her "I do not, [name_genie_hermione]!{heart}" ("shock", "happyCl", "worried", "mid")

    nar "You give Hermione's tits a couple of firm squeezes..."

    if states.her.level >= 17:
        her @ cheeks blush "[name_genie_hermione], you promised not to touch..." ("base", "base", "base", "R")
        gen "I know, I know... But it's hard to resist..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush ".................{heart}{heart}{heart}" ("base", "narrow", "base", "up")
    else:
        her @ cheeks blush "[name_genie_hermione], you promised not to touch..." ("angry", "happyCl", "worried", "mid")
        gen "I know, I know... But it's hard to resist..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "................." ("angry", "base", "angry", "mid")

    her @ cheeks blush ".................... *Ah*...{heart}" ("base", "narrow", "base", "up")
    her @ cheeks blush "[name_genie_hermione], you need to stop now..." ("base", "narrow", "base", "up")
    gen "Just a bit longer..." ("base", xpos="far_left", ypos="head")

    nar "You keep on massaging the girl's breasts..."

    her @ cheeks blush "[name_genie_hermione]... Please, stop this..." ("open", "narrow", "base", "up")
    gen "Why? Because you like it too much?" ("base", xpos="far_left", ypos="head")
    if states.her.level < 17:
        her @ cheeks blush "No it's not that..." ("angry", "narrow", "base", "R")
    else:
        her @ cheeks blush "I mean..." ("base", "base", "base", "R")

    nar "You pull her breasts in opposite directions, and then squish them together..."

    her @ cheeks blush "*Ah*...{heart} [name_genie_hermione]... I really need to go." ("angry", "narrow", "base", "up")
    if game.daytime:
        her @ cheeks blush "Classes are about to start..." ("angry", "narrow", "base", "R")
    else:
        her @ cheeks blush "It is getting late..." ("open", "narrow", "base", "R")

    gen "Well, alright..." ("base", xpos="far_left", ypos="head")
    show screen blkfade
    with d5

    nar "You let go of the girl's breasts..."

    $ hermione.wear("all") #No sound since she might be naked
    call her_chibi_scene("reset", "desk", "base")

    hide screen blkfade
    with d5

    if states.her.level >= 17:
        her @ cheeks blush "You will have to make it up to me for breaking your promise, [name_genie_hermione]." ("base", "base", "base", "R")
    else:
        her @ cheeks blush "Please don't think I forgot that you broke your promise, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")

    gen "Right..." ("base", xpos="far_left", ypos="head")

    return

label hg_pf_admire_breasts_T4_masturbate: # Call label
    hide hermione_main
    show screen blkfade
    with d3

    nar "You take your cock out and start stroking it..."
    her @ cheeks blush "[name_genie_hermione]?" ("base", "narrow", "base", "up")
    nar "You stare at Hermione's breasts with hunger..."

    # Start Jerking off.
    call her_chibi_scene("grope_tits_jerk_off", trans=fade)
    call ctc

    if states.her.level < 17:
        her "[name_genie_hermione], I never actually agreed to this..." ("shock", "happyCl", "worried", "mid")
        gen "What are you complaining about, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        gen "I'm not even touching you..." ("base", xpos="far_left", ypos="head")
        her "Yes, but you are... touching yourself, [name_genie_hermione]." ("clench", "happyCl", "worried", "mid")
        gen "Just stand still, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "It will be over soon." ("base", xpos="far_left", ypos="head")
        her ".................." ("angry", "happyCl", "worried", "mid")
        gen "Yes... Just like that..." ("base", xpos="far_left", ypos="head")
        gen "With your tits all exposed..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush ".............." ("disgust", "narrow", "base", "down")
        her @ cheeks blush "Well, so be it..." ("disgust", "base", "base", "R")
        her @ cheeks blush "But you must promise me not to..." ("soft", "base", "base", "R")
        her @ cheeks blush "Not to... *Ehm*..." ("open", "base", "base", "R")
        her @ cheeks blush "Not to discharge..." ("annoyed", "narrow", "angry", "R")
        her @ cheeks blush "Not on me, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
        gen "Not on you, you say... So, you still don't mind if I finish!" ("base", xpos="far_left", ypos="head")
        gen "You nasty little--" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]." ("disgust", "narrow", "base", "down")
        gen "Fine, whatever..." ("base", xpos="far_left", ypos="head")

        nar "You begin stroking your cock even faster..."

        gen "Yes, you want to see your headmaster cum!" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "................" ("disgust", "narrow", "base", "down")

    else: # Different posing than above.
        her @ cheeks blush "*Ah*..." ("base", "narrow", "base", "up")
        her @ cheeks blush "It's so big..." ("open", "base", "base", "R")
        her @ cheeks blush "You just couldn't help yourself, could you [name_genie_hermione]?" ("base", "base", "base", "R")
        her @ cheeks blush ".................." ("base", "narrow", "base", "up")
        gen "Yes... Just like that..." ("base", xpos="far_left", ypos="head")
        gen "With your tits all exposed..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush ".............." ("base", "narrow", "base", "up")
        her @ cheeks blush "Well, so be it..." ("open", "base", "base", "R")
        her @ cheeks blush "But you must promise me not to..." ("soft", "base", "base", "R")
        her @ cheeks blush "Not to... *Ehm*..." ("open", "base", "base", "R")
        her @ cheeks blush "Not to cum on me, [name_genie_hermione]..." ("base", "narrow", "base", "up")
        gen "If that's what you want..." ("base", xpos="far_left", ypos="head")
        gen "But whether I finish or not, won't be up to you..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "......................." ("base", "narrow", "base", "up")

        nar "You begin stroking your cock even faster..."

        gen "Yes, I'm almost there, I can feel it!" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]!" ("base", "narrow", "base", "up")

    # Genie cums.
    menu:
        gen "*Argh*! (I'm about to cum!)" ("angry", xpos="far_left", ypos="head")
        "-Hold it in-": #Hermione tells him he can cum, and he thinks she meant onto her.
            gen "Oh, alright..." ("base", xpos="far_left", ypos="head")
            gen "I'd better stop now I suppose..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..............." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "*Ehm*... I read that it's bad for you, [name_genie_hermione]..." ("disgust", "narrow", "base", "down")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It is bad for your health to just hold it in like this..." ("angry", "closed", "worried", "mid")
            her @ cheeks blush "*Ehm*..." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "If you want to you could just aim it--" ("open", "closed", "base", "R")
            gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "???" ("mad", "wide", "base", "stare")
            gen "*Argh*! YES!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("grope_tits_cum")
            with d5

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            pause 1.0
            $ hermione.set_cum(body="light")

            her @ cheeks blush "[name_genie_hermione], I wasn't saying that you could release your semen on me..." ("angry", "happyCl", "worried", "mid",emote="sweat")
            gen "Ah... That was great..." ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("grope_tits_cum_done")

            her @ cheeks blush "......." ("angry", "narrow", "base", "down")
            her @ cheeks blush "Well, what's done is done I suppose..." ("open", "narrow", "base", "down")
            gen "Ah... I really needed that..." ("base", xpos="far_left", ypos="head")

            her "" ("disgust", "narrow", "base", "down")
            call ctc

            gen "You've done well today, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "Thank you [name_genie_hermione]... Although, my body is all sticky now..." ("base", "closed", "base", "mid")
            her "I better clean myself up a bit..." ("annoyed", "closed", "base", "mid")
            gen "If you must..." ("base", xpos="far_left", ypos="head")

            show screen blkfade
            with d5

            $ hermione.set_cum(None)
            $ hermione.wear("all") #No sounds since she might be naked
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            pause .8

            hide screen blkfade
            with d5

            her "" ("soft", "base", "base", "R")
            call ctc
            her "Well, I suppose this should do for now..."

            return

        "-Just start cumming-":
            gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "???" ("mad", "wide", "base", "stare")
            gen "*Argh*! YES!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("grope_tits_cum")
            with d5

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            pause 1.0
            $ hermione.set_cum(body="light")

            call ctc

            her @ cheeks blush "*Ah*...{heart} It's so warm...{heart}" ("clench", "happyCl", "worried", "mid")
            her @ cheeks blush "[name_genie_hermione], you promised..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "Ah yes... All covered in semen..." ("angry", xpos="far_left", ypos="head")

            call her_chibi_scene("grope_tits_cum_done")

            her @ cheeks blush "..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "Well, what's done is done I suppose..." ("open", "narrow", "base", "down")
            gen "Ah... I really needed that..." ("base", xpos="far_left", ypos="head")

            her "" ("disgust", "narrow", "base", "down", xpos="mid", ypos="base")
            call ctc

            her "My body... It's covered in semen..."
            gen "I'm sure I missed a spot or two." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "narrow", "base", "mid", xpos="mid", ypos="base")
            gen "Don't worry, it looks good on you." ("base", xpos="far_left", ypos="head")
            gen "You did great." ("base", xpos="far_left", ypos="head")

            her "Thank you [name_genie_hermione]." ("open", "closed", "base", "mid")
            her "I better clean myself up..." ("annoyed", "closed", "base", "mid")
            call ctc

            show screen blkfade
            with d3

            $ hermione.set_cum(None)
            $ hermione.wear("all") #No sounds since she might be naked
            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            pause .8

            hide screen blkfade
            with d5

            her "" ("soft", "base", "base", "R")
            call ctc
            her "Well, I suppose this should do for now..."

            return
