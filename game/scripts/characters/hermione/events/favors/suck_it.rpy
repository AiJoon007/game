

### Hermione Blowjob ###

label start_hg_pf_blowjob:

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her for a blowjob?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    # Start Event
    $ current_payout = 55
    $ _mouth_full_of_cum = False
    return

label hg_pf_blowjob_fail:
    jump end_hermione_event

label end_hg_pf_blowjob:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    $ hermione.set_cum(None)
    $ hermione.wear("all")

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if states.her.mood != 0:
        if _mouth_full_of_cum:
            her @ cheeks blush tears mascara "" ("full_cum", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
        else:
            her "" ("angry", "base", "annoyed", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        if _mouth_full_of_cum:
            her @ cheeks blush tears mascara "" ("full_cum", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
        else:
            her "" ("soft", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if states.her.tier < 6:
        gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
        $ gryffindor += current_payout
    else:
        gen "You may go now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    if _mouth_full_of_cum:
        her @ cheeks blush tears mascara "..." ("full_cum", "narrow", "annoyed", "up")
    else:
        her "Thank you, [name_genie_hermione]..." ("soft", "base", "base", "R")

    # Hermione leaves
    call her_walk("door", "base")

    call her_chibi("leave")


    # Increase level
    if states.her.tier == 5:
        if states.her.level < 21: # Points til 21
            $ states.her.level +=1
    if states.her.tier == 6:
        if states.her.level < 24: # Points til 24
            $ states.her.level += 1

    $ states.her.status.blowjob = True

    jump end_hermione_event

### Fail Events ###

label hg_pf_blowjob_T1_E1: #Fail

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "We're done playing games..." ("base", xpos="far_left", ypos="head")
    gen "Get over here, and suck my cock!" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare")
    her "How could you ask for such a thing!?"
    her "I think I better leave." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(Welp, was worth a shot I guess.)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 12

    jump hg_pf_blowjob_fail

label hg_pf_blowjob_T2_E1: #Fail

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Why don't you open that pretty little mouth of yours... And then put it around my cock?" ("base", xpos="far_left", ypos="head")
    her "Put my mouth--" ("shock", "wide", "base", "stare")
    her "[name_genie_hermione]!" ("angry", "base", "worried", "mid")
    her "Why would you think asking me for something like that is a good idea?" ("angry", "base", "worried", "mid")
    gen "I figured there'd be less talking if your mouth was busy--" ("base", xpos="far_left", ypos="head")
    her "I'm leaving!" ("angry", "happyCl", "angry", "mid")

    call her_walk(action="leave")

    gen "(Did I say something wrong...?)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 10

    jump hg_pf_blowjob_fail

label hg_pf_blowjob_T3_E1: #Fail

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Ready to earn some more points?" ("base", xpos="far_left", ypos="head")
    her "Of course!" ("base", "base", "base", "mid")
    gen "Great!" ("grin", xpos="far_left", ypos="head")
    gen "Then get over here, and suck my cock!" ("grin", xpos="far_left", ypos="head")
    her "Suck your--" ("angry", "base", "base", "stare")
    her "What is the reason you believe I would do such a thing?" ("angry", "base", "angry", "mid")
    gen "So that you can earn points for your house? Or have your character motivation changed already?" ("base", xpos="far_left", ypos="head")
    her "I think I better leave..." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(*Hmm*... Judging by her reaction she's not yet ready for it...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 8

    jump hg_pf_blowjob_fail

label hg_pf_blowjob_T4_E1: #Fail

    call start_hg_pf_blowjob

    if not _event_completed_failed:
        her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
        gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
        gen "I plan to grant Gryffindor {number=current_payout} house points today..." ("base", xpos="far_left", ypos="head")
        gen "If you suck me off..." ("base", xpos="far_left", ypos="head")
        her "Suck you...{w=0.3} off?" ("disgust", "wide", "base", "mid")
        her "With my mouth?!" ("disgust", "wide", "base", "stare")

        if states.her.ev.give_me_a_handy.cock_kiss:
            gen "Wouldn't even be the first time you've done it!" ("grin", xpos="far_left", ypos="head")
            her "Yes, but..." ("disgust", "narrow", "worried", "down")
            her "That was something different entirely..." ("disgust", "happyCl", "worried", "mid")
            gen "How so?" ("base", xpos="far_left", ypos="head")
            her "All I wanted was to get done with that favour early, so I..." ("open", "narrow", "base", "down")
            her "I helped..." ("disgust", "base", "worried", "R")
            gen "By sucking on my cock! Indeed, you did!" ("grin", xpos="far_left", ypos="head")
            her "No! I was merely stroking it... And..." ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "I gave it a short kiss, but..." ("disgust", "narrow", "worried", "down")
            her @ cheeks blush "I'm sorry [name_genie_hermione], but I don't think I can do \"that\"!" ("open", "base", "worried", "R")
        else:
            gen "Preferably..." ("base", xpos="far_left", ypos="head")
            gen "But I'm always open to trying out new things!" ("grin", xpos="far_left", ypos="head")
            her "Are you out of your mind?!" ("scream", "closed", "angry", "mid")

        her @ cheeks blush "I should leave..." ("disgust", "narrow", "base", "down")
    else:
        her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
        gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
        gen "I plan to grant Gryffindor {number=current_payout} house points today..." ("base", xpos="far_left", ypos="head")
        her "Let me guess..." ("open", "closed", "angry", "mid")
        her "You want me to \"suck you off\" for it?" ("open", "base", "angry", "mid")
        gen "That is correct!" ("grin", xpos="far_left", ypos="head")
        her "I refuse..." ("open", "closed", "base", "mid")
        gen "It's only a blowjob, girl..." ("base", xpos="far_left", ypos="head")

        if states.her.ev.give_me_a_handy.cock_kiss:
            gen "It's not like you haven't done it before..." ("base", xpos="far_left", ypos="head")
            her "Are you talking about the kiss I gave it?" ("open", "base", "angry", "mid")
            her "That was something different entirely..." ("open", "closed", "base", "mid")
            gen "How so?" ("base", xpos="far_left", ypos="head")
            her "I wanted to get done with that favour early, so I helped a bit." ("open", "narrow", "angry", "R")
            gen "By sucking on my cock! Indeed, you did!" ("grin", xpos="far_left", ypos="head")
            her "It was nothing more than a short kiss..." ("annoyed", "base", "angry", "mid")
            gen "Still counts as a blowjob..." ("base", xpos="far_left", ypos="head") # See, no flag is set. It doesn't count! :)

        her "[name_genie_hermione], I've told you this last time..." ("open", "closed", "base", "mid")
        her "I refuse to do this sort of thing..." ("normal", "base", "angry", "mid")
        her "I have to go now..." ("annoyed", "narrow", "angry", "R")

    call her_walk(action="leave")

    gen "(Tough luck...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 6

    jump hg_pf_blowjob_fail

### Tier 5 ###

# Event 1 (i) - Hermione is okay with it.
# Event 2 (i) - Hidden blowjob with Snape watching.
# Event 3 (r) - Normal blowjob with choices.

label hg_pf_blowjob_T5_intro_E1:

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "I plan to grant Gryffindor {number=current_payout} house points today..." ("base", xpos="far_left", ypos="head")
    gen "If you suck me off..." ("base", xpos="far_left", ypos="head")
    her "Oh..." ("open", "narrow", "worried", "down")
    her "Alright." ("base", "narrow", "worried", "down")
    gen "Really? Just like that?" ("base", xpos="far_left", ypos="head")
    her "Yes. I know I'm supposed to feel outraged..." ("angry", "narrow", "base", "down")
    her "But somehow I do not..." ("angry", "base", "base", "mid")
    her "I suppose I am just glad that I can help out my house..." ("base", "narrow", "worried", "down")
    her "And if I must put your penis in my mouth to do that, then so be it..." ("upset", "closed", "base", "mid")
    gen "Well, alright then." ("base", xpos="far_left", ypos="head")
    her "Although, now when I say it out loud like this..." ("angry", "narrow", "base", "down")
    gen "Too late! You already said \"yes\"!" ("grin", xpos="far_left", ypos="head")
    her "I know..." ("grin", "happyCl", "worried", "mid", emote="sweat")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_blowjob_1


label hg_pf_blowjob_T5_intro_E2:

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "How would you like to give me another blowjob?" ("base", xpos="far_left", ypos="head")
    her "Using my mouth, preferably." ("open", "narrow", "base", "down")
    gen "What do you--" ("base", xpos="far_left", ypos="head")
    her "*Giggles*" ("grin", "narrow", "base", "down")
    gen "You cheeky little--{w=0.2} Get over here, before I change my mind on this favour trading thing." ("angry", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..." ("angry", "base", "base", "mid")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_hidden_blowjob # Snape

label hg_pf_blowjob_T5_repeat:

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "For today's favour, I want you to get on your knees and give me another blowjob." ("base", xpos="far_left", ypos="head")
    her "I suppose I can do that..." ("base", "narrow", "worried", "down")
    gen "Great! Come here then!" ("grin", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_blowjob_1

### Tier 6 ###

# Event 1 (i) - New event with a couple of choices.
# Event 2 (r) - Hidden blowjob (Snape, Tonks, or Luna.)
# Event 3 (r) - Blowjob with choices.

label hg_pf_blowjob_T6_intro_E1:

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "I want you..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You want... Me?" ("soft", "squint", "base", "mid")
    her @ cheeks blush "(Is he--)" ("soft", "narrow", "base", "down")
    gen "I want you to get over here, and suck my cock!" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("disgust", "base", "base", "mid")
    gen "Go on... Show me what that mouth can do." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "(He's playing with me... Well, I'll show him...)" ("annoyed", "narrow", "annoyed", "R")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her @ cheeks blush "[name_genie_hermione], how dare you propose such a thing to one of your pupils!" ("scream", "closed", "angry", "mid", emote="angry")
    gen "Wha--...?" ("angry", xpos="far_left", ypos="head")
    her "This is unbecoming of a man of your standing." ("soft", "narrow", "angry", "R", emote="angry")
    her "You should be ashamed of yourself, [name_genie_hermione]!" ("open", "closed", "angry", "mid")
    menu:
        gen "???" ("base", xpos="far_left", ypos="head")
        "\"Fine. No points to you then! Leave!\"":
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "But [name_genie_hermione], I--" ("disgust", "squint", "worried", "mid", emote="sweat")
            gen "You are dismissed, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione], please, I didn't mean any of the things I said." ("grin", "happyCl", "worried", "mid", emote="sweat")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her "I was just, *Ehm*..." ("angry", "narrow", "base", "R")
            her "......." ("angry", "narrow", "base", "down")
            her "Oh! I was just trying to imagine how the \"old me\" would've reacted to this. That's it!" ("grin", "base", "base", "mid")
            gen "So..." ("base", xpos="far_left", ypos="head")
            gen "You were messing with me then?" ("angry", xpos="far_left", ypos="head")
            her "*Ehm*... I'm sorry [name_genie_hermione], I didn't mean to..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "Well then... If you're not going to take this seriously anymore, then perhaps we should end it here." ("grin", xpos="far_left", ypos="head")

        "\"*Ehm*... I am sorry?\"":
            stop music fadeout 1.0
            her "*Giggles*" ("grin", "base", "base", "R")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "I got you... [name_genie_hermione]." ("grin", "happyCl", "worried", "mid", emote="sweat")
            gen "What?" ("base", xpos="far_left", ypos="head")
            gen "Is this some kind of joke to you?" ("angry", xpos="far_left", ypos="head")
            her "*Giggles*" ("grin", "happyCl", "base", "mid")
            gen "..." ("angry", xpos="far_left", ypos="head")
            gen "Well then... If you're not going to take this seriously anymore, then perhaps we should end it here." ("grin", xpos="far_left", ypos="head")

        "-Two can play that game...-":
            stop music fadeout 1.0
            gen "Oh nooooo... What am I ever going to do now." ("base", xpos="far_left", ypos="head")
            her "........?" ("soft", "base", "base", "mid")
            gen "My pupil has charged me with the crime of dishonour!" ("base", xpos="far_left", ypos="head")
            gen "I must perform honourable sudoku, and--" ("base", xpos="far_left", ypos="head")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "[name_genie_hermione]! I was just joking, please don't--" ("open", "wide", "worried", "mid")
            gen "*He-he*..." ("grin", xpos="far_left", ypos="head")
            her "Why are you--" ("soft", "wide", "worried", "mid")
            gen "I got you." ("grin", xpos="far_left", ypos="head")
            her "........" ("annoyed", "base", "angry", "R")
            her "*Sigh*" ("soft", "closed", "base", "mid")
            her "Was I really being that obvious?" ("soft", "closed", "base", "mid")
            gen "Very much so." ("base", xpos="far_left", ypos="head")
            gen "That said... I didn't expect this from you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "I suppose I do have a sense of humour, after all." ("base", "closed", "base", "mid")
            gen "A sense of--" ("base", xpos="far_left", ypos="head")
            gen "If you're not going to take this seriously anymore, then we should probably end things here." ("base", xpos="far_left", ypos="head")

    her "But, [name_genie_hermione]!" ("soft", "wide", "worried", "mid")
    gen "Quiet, [name_hermione_genie]... You've been a very bad girl..." ("grin", xpos="far_left", ypos="head")
    her "I'm sorry [name_genie_hermione], I didn't think--" ("angry", "narrow", "worried", "mid")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "Say it... Tell me that you've been a bad girl!" ("grin", xpos="far_left", ypos="head")
    her "I..." ("angry", "narrow", "base", "mid_soft")
    her @ cheeks blush "I've been a very, very bad girl, [name_genie_hermione]!" ("open", "narrow", "base", "down")
    gen "..............." ("grin", xpos="far_left", ypos="head")
    gen "Tell me, what wrongs did you do, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("disgust", "narrow", "worried", "down")
    her "I took your generosity for granted..." ("soft", "narrow", "worried", "down")
    gen "Yes you did!" ("grin", xpos="far_left", ypos="head")
    her "I didn't appreciate that you're helping me earn those points..." ("disgust", "happyCl", "worried", "mid")
    gen "That's right... And how are you meant to show that appreciation?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "By doing what you ask of me...{w=0.4} Unquestionably..." ("soft", "narrow", "base", "down")
    gen "That's right...{w=0.4} And--" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Please, let me suck your cock [name_genie_hermione]!" ("angry", "narrow", "base", "mid_soft")
    gen "Yes! You dirty slut!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "I need to be punished!" ("angry", "narrow", "base", "down")
    gen "Beg me for it, you slut!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "Please punish me with your cock, [name_genie_hermione]!" ("open", "happyCl", "base", "mid_soft")
    her @ cheeks blush "I beg you!" ("angry", "narrow", "worried", "mid")
    gen "Come here, you dirty little minx!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "{heart}{heart}{heart}" ("base", "narrow", "worried", "R")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_blowjob_2

label hg_pf_blowjob_T6_hidden_repeat:

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "Come here and suck my dick, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]..." ("soft", "squint", "base", "mid_soft")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_hidden_blowjob

label hg_pf_blowjob_T6_repeat:

    call start_hg_pf_blowjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "Come here and suck my dick, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]..." ("base", "narrow", "base", "mid_soft")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    jump hg_pf_blowjob_2

### First Blowjob ###

label hg_pf_blowjob_1:

    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj_pause", trans=d9)
    pause.8

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    call her_chibi_scene("bj", trans=d9)
    call ctc

    her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "mid_soft", ypos="head", flip=False)
    gen "*Ah*... Very good, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "But try to take it a bit deeper..." ("base", xpos="far_left", ypos="head")
    her "*Gulp*! *Gobble*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "stare")
    gen "Yes... Just like that..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Gltch*! *Gulp*!" ("open_wide_tongue", "closed", "base", "mid")
    gen "That's a good girl..." ("base", xpos="far_left", ypos="head")

    $ _MRM = False
    $ _proud = False
    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "\"Whatever happened to your \"MRM\" thing?\"":
            $ _MRM = True
            her "*Slurp*?" ("open_wide_tongue", "squint", "base", "mid")

            call her_chibi_scene("bj_pause")
            her "Oh, well..." ("angry", "base", "base", "up")
            her "We are still active, but... *Ahem*..." ("angry", "closed", "base", "mid")

            call her_chibi_scene("bj")
            her "*Slurp*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "R")

            gen "But?" ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj_pause")
            her "But... We are not getting as much support as I thought we would." ("angry", "wink", "base", "mid")

            call her_chibi_scene("bj")
            her "*Slurp*! *Gulp*! *Gulp*!" ("open_wide_tongue", "closed", "worried", "down")
            gen "Oh, well..." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "I suppose that's to be expected..." ("base", xpos="far_left", ypos="head")
            gen "I mean, you're selling sexual favours, by letting me play with your tits and such..." ("base", xpos="far_left", ypos="head")
            her "*Gobble*! *Gltch*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "No wonder you're having troubles trying to condemn such behaviour in front of the other students." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Gulp*!" ("open_wide_tongue", "narrow", "base", "down")
            gen "You perverted, little hypocrite." ("base", xpos="far_left", ypos="head")
            her "*Gulp*--" ("open_wide_tongue", "closed", "base", "mid")

            call her_chibi_scene("bj_pause")
            her "[name_genie_hermione], that's not what we stand for..." ("angry", "base", "worried", "mid")
            gen "What do you mean?" ("base", xpos="far_left", ypos="head")
            her "The \"MRM\" is about gender equality." ("open", "closed", "base", "mid")
            her "We are not against selling sexual favours to the teachers..." ("open", "closed", "base", "mid")
            her "We are against the gender inequality that the selling of sexual favour creates..." ("soft", "narrow", "base", "mid")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Gobble*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "So, you don't disapprove of selling favours?" ("base", xpos="far_left", ypos="head")
            her "*Slurp*--" ("open_wide_tongue", "narrow", "base", "up")

            call her_chibi_scene("bj_pause")
            her @ cheeks blush "*Ehm*..." ("upset", "narrow", "base", "R")
            her @ cheeks blush "I dislike that it's become a necessity, if you want your house to be in the running." ("open", "happy", "base", "R")
            her @ cheeks blush "If it wasn't for those Slytherin--{w=0.2} Well, I never would've imagined..." ("soft", "narrow", "base", "R")
            gen "So, you believe that it was the Slytherin house that instigated this favour trading business?" ("base", xpos="far_left", ypos="head")
            her "Either it was some Slytherin slut, or a teacher... All I know, is that I woke up one day to the Slytherin house earning more points than ever before." ("open", "closed", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "Either way... What instigated it hardly matters." ("soft", "narrow", "base", "R")
            her "The fact is... As soon as the ball began rolling, there was no way I could stand in its path." ("open", "happy", "base", "R")
            her "Not when there are teachers like Snape..." ("angry", "narrow", "base", "R")
            gen "Speaking of ball, why don't you roll that tongue--" ("base", xpos="far_left", ypos="head")
            her "What other choice did I have... I want Gryffindor to win the house-cup as much as any other Gryffindor student..." ("open", "closed", "annoyed", "R")
            her "Therefore, my decision to also sell sexual favours was the only logical--" ("soft", "closed", "base", "mid")
            gen "The cock, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Right... Sorry, [name_genie_hermione]..." ("open", "narrow", "worried", "up")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Slurp*! *Gulp*! *Gltch*!" ("open_wide_tongue", "narrow", "base", "up")

            gen "*Ah*... Yes... Work that tongue, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gulp*! *Gltch*!" ("open_wide_tongue", "narrow", "worried", "down")
            her "*Slurp*--" ("open_wide_tongue", "closed", "worried", "up")

            call her_chibi_scene("bj_pause")
            her "I mean, it made sense, right?--" ("upset", "squint", "worried", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her "Me, deciding to sell favours and help my house!" ("angry", "narrow", "worried", "mid")
            gen "Oh, yes! It certainly was the best course of action, and a noble one as well." ("base", xpos="far_left", ypos="head")
            her "Thank you, [name_genie_hermione]." ("angry", "narrow", "worried", "down")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Slurp*! *Gulp*! *Gltch*!" ("open_wide_tongue", "narrow", "base", "up")

            gen "I mean, if you can't beat them, join them!" ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Cough*! *Cough*!" ("open_wide_tongue", "wide", "base", "stare")

            call her_chibi_scene("bj_pause")
            her "Join them?!" ("angry", "base", "worried", "stare")
            her @ cheeks blush "[name_genie_hermione], I did not join them!" ("angry", "squint", "worried", "mid")
            gen "You didn't?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course not! I am nothing like those Slytherin harlots." ("clench", "squint", "worried", "mid")
            her "They're selling favours for entirely different, self-serving reasons!" ("open", "wink", "annoyed", "mid")
            gen "I see... So, you're saying that your own reasons aren't self-serving, then?" ("base", xpos="far_left", ypos="head")
            her "Of course they aren't!" ("angry", "base", "base", "R")
            her "I'm selling favours to help the entire house of Gryffindor, and at the same time, I am also striving for equality through the \"MRM\"." ("grin", "closed", "worried", "R")
            her "The \"MRM\" is open to anyone, not just students of the Gryffindor house." ("smile", "closed", "base", "mid")
            gen "I thought you just said that the group isn't getting much support." ("base", xpos="far_left", ypos="head")
            her "Well, that is hardly my fault..." ("angry", "narrow", "base", "R")
            gen "Sounds to me as if the purpose of this group is so that you can keep others from selling--" ("base", xpos="far_left", ypos="head")
            her "Why on earth would you think that!?" ("angry", "squint", "worried", "stare")
            gen "Well, if you truly wanted the group to gain traction, then should you not be teaching them things like how to strip for a teacher--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Teach them how to--" ("clench", "base", "base", "stare")
            her @ cheeks blush "*Ahem*... Well, I don't see how that's supposed to help with anything..." ("annoyed", "closed", "worried", "R")
            gen "I figured you'd say that..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "In fact... The \"MRM\" mostly consists of males, so I to try keep any distractions during our meetings at a minimum." ("angry", "closed", "base", "mid")
            gen "Sounds like a good time...{w=0.4} But I still think--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That said, this one time we did have a meeting right after I sold you another favour..." ("angry", "closed", "worried", "mid")
            gen "(Is she trying to change the subject?)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I had to give a speech with my clothes all messy and stained." ("angry", "narrow", "base", "down")
            gen "..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ahem*... Yes, it truly felt awful that I had to do that..." ("angry", "narrow", "base", "R")
            gen "I'm sure you enjoyed it a little bit though..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course I--" ("soft", "closed", "annoyed", "R")
            gen "Perhaps you'd enjoy teaching them--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, *Ehm*--{w=0.2} Yes, I certainly did enjoy it!" ("angry", "squint", "base", "stare")
            gen "I knew it! I knew you would, you little perv!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("base", "narrow", "worried", "down")
            gen "Speaking of enjoyment..." ("base", xpos="far_left", ypos="head")
            gen "Cock, back in your mouth." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes, [name_genie_hermione]." ("angry", "closed", "base", "mid")
            call her_chibi_scene("bj", trans=d3)
            pause.8

        "\"Your parents must be proud of you...\"":
            $ _proud = True
            her "*Slurp*--" ("open_wide_tongue", "squint", "base", "stare")

            call her_chibi_scene("bj_pause")
            her "Yes, I believe they are..." ("base", "closed", "base", "mid")
            her "With me being an excellent student despite being muggle-born and all..." ("smile", "closed", "base", "mid")
            her "Although at first, they were against sending me to some \"Bogus boarding school\"." ("angry", "base", "base", "mid")
            her "It took some effort to convince them that \"Hogwarts\" is a respectable institution." ("base", "closed", "base", "mid")
            gen "Yes, a respectable institution indeed." ("base", xpos="far_left", ypos="head")
            gen "Cock back in your mouth, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Slurp*! *Gulp*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Yes, just keep going at it like that, for a while..." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gltch*! *Gulp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Good, good..." ("base", xpos="far_left", ypos="head")
            gen "So, what would your folks say if they were to see you now, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "*Slurp*--" ("open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            her "They wouldn't understand, of course..." ("open", "narrow", "worried", "down")
            her "But I don't care." ("open", "closed", "worried", "down")
            her "I am not afraid to \"get my hands dirty\", and do what needs to be done." ("upset", "closed", "base", "mid")
            gen "A bit rebellious, aren't you?" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... I suppose I am." ("angry", "wink", "base", "mid")
            gen "Back to sucking then... Teach your folks a lesson." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")

        "\"Tell me about the Gryffindor house.\"":
            her "*Slurp*?--" ("open_wide_tongue", "squint", "base", "mid")

            call her_chibi_scene("bj_pause")
            her "What could I tell you that you don't already know, [name_genie_hermione]?" ("soft", "base", "base", "mid")
            gen "*Err*... That's true... I do know everything, of course." ("base", xpos="far_left", ypos="head")
            gen "But I want to see just how much you know." ("base", xpos="far_left", ypos="head")
            gen "To test your knowledge of the subject." ("base", xpos="far_left", ypos="head")
            nar "As soon as you mention \"test\", Hermione's eyes light up with excitement."
            her "Okay then, just give me a moment to gather my thoughts..." ("base", "base", "base", "R", emote="happy")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Slurp*! *Slurp*! *Gulp*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Oh, yes... Take as much time as you need, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            her "*Gulp*--" ("open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            her "The Gryffindor house was founded by Godric Gryffindor, thus the name." ("open", "closed", "base", "mid")
            her "The heraldic animal of Gryffindor is the lion..." ("open", "closed", "base", "mid")

            call her_chibi_scene("bj")
            her "*Gulp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            her "Professor Minerva McGonagall is the head of our house." ("open", "closed", "base", "mid")
            her "The Gryffindor house emphasises the traits of courage..." ("open", "closed", "base", "mid")
            her "As well as \"daring, nerve, and chivalry\"..." ("open", "closed", "base", "mid")
            her "And thus its members are generally regarded as brave, but also reckless..." ("open", "closed", "base", "mid")

            call her_chibi_scene("bj")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")

            call her_chibi_scene("bj_pause")
            her "Gryffindor corresponds roughly to the element of fire..." ("open", "closed", "base", "mid")
            her "And for that reason, the colours of red and gold were chosen." ("open", "closed", "base", "mid")

            call her_chibi_scene("bj")
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            gen "Well, I thought I could turn this around somehow to make fun of you..." ("base", xpos="far_left", ypos="head")
            her "*Slurp* ...?" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "With your house representing courage and righteousness and such..." ("base", xpos="far_left", ypos="head")
            gen "And you, being a nasty slut..." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj_pause")
            her "[name_genie_hermione]..." ("disgust", "narrow", "annoyed", "mid", emote="angry")
            gen "But to be honest..." ("base", xpos="far_left", ypos="head")
            gen "\"Daring, nerve, fire, recklessness\"..." ("base", xpos="far_left", ypos="head")
            gen "Those traits describe your personality quite well..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione]..." ("disgust", "narrow", "base", "down")

            call her_chibi_scene("bj", trans=d3)
            pause.8
            her "*Gobble*!! *Gltch*!! *Gobble*!!!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Perhaps diligence should also get added to that list..." ("grin", xpos="far_left", ypos="head")
            gen "What do you think?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Gobble*!! *Gltch*!! *Gobble*!!!" ("open_wide_tongue", "narrow", "base", "up")
            gen "I'll take that as a yes..." ("grin", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "closed", "base", "up")

    gen "*Ngh*--{w=0.2} Yes...{w=0.4} Keep going--{w=0.2} Just like that..." ("base", xpos="far_left", ypos="head")
    her "*Gobble*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
    gen "Good...{w=0.4} Back and forth, back and forth..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
    her "*Slurp*--" ("open_wide_tongue", "narrow", "annoyed", "up")

    call her_chibi_scene("bj_pause")
    her "[name_genie_hermione]... I am a... whore." ("soft", "narrow", "base", "down")
    gen "What?" ("base", xpos="far_left", ypos="head")

    call her_chibi_scene("bj")
    her "*Slurp-Slurp-Slurp*!" ("open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj_pause")
    her "I truly am a slut, and I greatly enjoy sucking your cock." ("angry", "squint", "base", "R")
    gen "Oh, yes, yes... Say more things like that." ("base", xpos="far_left", ypos="head")

    call her_chibi_scene("bj", trans=d3)
    pause.8
    her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")

    call her_chibi_scene("bj_pause")
    her "Please, [name_genie_hermione]... Cum for me." ("soft", "narrow", "annoyed", "up")
    with hpunch
    gen "*Argh*! You little--" ("angry", xpos="far_left", ypos="head")
    gen "{size=-4}(Here it comes!){/size}" ("angry", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Warn her-":
            $ states.her.status.gokkun = True

            her "Yes, I love to please--" ("soft", "narrow", "annoyed", "up")
            gen "Heads up, [name_hermione_genie]! Here it comes!" ("angry", xpos="far_left", ypos="head")
            her "!!!" ("angry", "wide", "base", "stare")

            call her_chibi_scene("bj", trans=d5)
            pause.8

            nar "Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion."

            call cum_block
            call her_chibi_scene("bj_cum_in", trans=d5)
            pause.8

            call cum_block
            gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
            her "*Gulp*! *Gulp*! *Gulp*!" ("open_wide_tongue_cum", "narrow", "annoyed", "up")
            with hpunch
            gen "And some more!" ("angry", xpos="far_left", ypos="head")
            her "*Gulp*! *Gulp*! *Gulp*!" ("open_wide_tongue_cum", "squint", "worried", "ahegao")
            call ctc

            call her_chibi_scene("bj_pause", trans=d5)
            pause.8

            gen "Well, I think that's it." ("base", xpos="far_left", ypos="head")
            her ".............." ("cum", "happyCl", "worried", "mid")
            gen "Are you alright there, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            play sound "sounds/gulp.ogg"
            pause .2
            her "Yes, [name_genie_hermione]..." ("grin", "narrow", "base", "dead")
            her "You came so much..." ("grin", "narrow", "base", "dead")
            gen "You managed to swallow it all, though." ("base", xpos="far_left", ypos="head")
            her "Yes... I thought I would choke..." ("grin", "narrow", "base", "dead")
            her "But I made a promise to myself that I won't let go of your penis no matter what!" ("grin", "narrow", "base", "dead")
            gen "Good girl." ("base", xpos="far_left", ypos="head")
            if _proud:
                gen "Your parents should be proud." ("grin", xpos="far_left", ypos="head")
            her "Thank you, [name_genie_hermione]." ("grin", "narrow", "base", "dead")
            her "I almost... Well, since you came so much..." ("base", "narrow", "base", "dead")
            her "I almost feel as if I just got fed..." ("soft", "narrow", "annoyed", "up")
            her "My stomach is so full..." ("soft", "closed", "annoyed", "up")
            gen "You did get fed, I fed you with my cum!" ("grin", xpos="far_left", ypos="head")

            if game.daytime:
                her "I suppose you did... I think I may skip lunch today..." ("soft", "closed", "base", "up")
            else:
                her "I suppose you did... I think I may skip supper tonight..." ("soft", "narrow", "annoyed", "up")

            her "May I get paid now?" ("base", "narrow", "base", "stare")
            gen "Certainly." ("grin", xpos="far_left", ypos="head")

            $ achievements.unlock("headlib")

        "-Don't bother-":
            her "Yes, I love to please---" ("soft", "narrow", "annoyed", "up")

            call cum_block
            gen "{size=+7}Whore!{/size}" ("angry", xpos="far_left", ypos="head")
            her "!!?" ("shock", "wide", "base", "stare")

            call her_chibi_scene("bj_cum_out", trans=d5)
            call ctc

            $ hermione.set_cum(face="heavy")
            her "[name_genie_hermione]..." ("shock", "wide", "base", "stare")
            gen "Don't you move now, [name_hermione_genie]." ("angry", xpos="far_left", ypos="head")
            $ hermione.set_cum(breasts="light")
            gen "Yes, just be still and take it." ("angry", xpos="far_left", ypos="head")
            gen "*Argh*! You little slut! All covered in cum!" ("angry", xpos="far_left", ypos="head")
            her @ tears soft ".............." ("angry", "base", "base", "mid")

            call her_chibi_scene("bj_cum_out_done")
            gen "Whew..." ("base", xpos="far_left", ypos="head")
            her ".............." ("normal", "happyCl", "worried", "mid")
            gen "Alright, I'm done..." ("base", xpos="far_left", ypos="head")
            her "................." ("disgust", "base", "base", "mid")

            if game.daytime:
                her "My classes are about to start..." ("disgust", "narrow", "base", "down")
            else:
                her "I just took a shower recently..." ("open", "base", "base", "mid")
                gen "And I gave you another one." ("grin", xpos="far_left", ypos="head")

            gen "Just wipe it off, and you'll be alright." ("base", xpos="far_left", ypos="head")
            her "............" ("annoyed", "narrow", "base", "down")
            gen "Unless, you don't want to." ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("angry", "squint", "worried", "mid", emote="sweat")
            gen "Perhaps you would rather go outside looking like this?" ("base", xpos="far_left", ypos="head")
            gen "You could let everyone see what a nasty little slut you are." ("base", xpos="far_left", ypos="head")
            if _proud:
                gen "Go on...{w=0.4} Didn't you say you were rebellious?" ("grin", xpos="far_left", ypos="head")
            if _MRM:
                gen "I'm sure that group of yours would love to see it." ("grin", xpos="far_left", ypos="head")
            her "No, thanks!" ("angry", "happyCl", "worried", "mid", emote="sweat")

            stop music fadeout 1.0
            if game.daytime:
                gen "Very well... Then quickly clean yourself up, or you'll be late for your classes..." ("base", xpos="far_left", ypos="head")
            else:
                gen "Very well... Then quickly clean yourself up and head to bed..." ("base", xpos="far_left", ypos="head")

            her "Yes, of course..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            her "May I get paid before I leave, [name_genie_hermione]?" ("upset", "wink", "base", "mid")
            gen "Certainly." ("base", xpos="far_left", ypos="head")

    jump end_hg_pf_blowjob

### Hidden Blowjob ###

label hg_pf_hidden_blowjob:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj", trans=d9)
    call ctc

    her "*Slurp*! *Slurp*! *Gulp*!" ("open_wide_tongue", "narrow", "annoyed", "up", ypos="head", flip=False)
    gen "Yes, good girl..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*!"
    her "{size=+7}!!!{/size}" ("open_wide_tongue", "squint", "base", "stare")
    gen "*Hmm*?!" ("base", xpos="far_left", ypos="head")

    if game.daytime:
        gen "Who could that be?" ("base", xpos="far_left", ypos="head")
    else:
        gen "Who could that be at this hour?" ("base", xpos="far_left", ypos="head")

    #Priority.
    if not states.her.ev.suck_it.snape_encounter:
        jump hg_hidden_blowjob_snape

    elif not states.her.ev.suck_it.tonks_encounter:
        jump hg_hidden_blowjob_tonks

    elif states.lun.unlocked and not states.her.ev.suck_it.luna_encounter:
        jump hg_hidden_blowjob_luna

    random:
        block if states.her.ev.suck_it.snape_encounter:
            jump hg_hidden_blowjob_snape

        block if states.her.ev.suck_it.tonks_encounter:
            jump hg_hidden_blowjob_tonks

        block if states.her.ev.suck_it.luna_encounter:
            jump hg_hidden_blowjob_luna

label hg_hidden_blowjob_snape:
    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    her "{size=-2}[name_genie_hermione], what should I do?{/size}" ("shock", "wide", "base", "stare")
    gen "Just keep sucking, [name_hermione_genie]... This doesn't concern you." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("soft", "narrow", "base", "down")
    call her_chibi_scene("bj", trans=d5)
    pause.8

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*!"

    sna "Are you there? I need to talk to you."
    her "(It's professor Snape!)" ("open_wide_tongue", "base", "worried", "stare")
    call her_chibi_scene("bj_pause")
    her "{size=-2}[name_genie_hermione], please, send him away, I beg you!{/size}" ("angry", "base", "worried", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Please, come on in, Severus.\"":
            pass

        "\"I am busy right now, Severus.\"":
            her "{size=-2}Thank you, [name_genie_hermione].{/size}" ("angry", "squint", "base", "mid")
            sna "Busy? With what?"
            sna "All you do is sit on your arse all day."
            sna "I really need to talk to you about something."
            gen "I said I am busy, Severus." ("base", xpos="far_left", ypos="head")
            gen "Understood? I... am... \"busy\"!" ("base", xpos="far_left", ypos="head")
            sna "Oh... You mean \"busy\" busy? Gotcha!"
            sna "Well, I'll talk to you later then."

            if states.her.tier > 5:
                jump hg_pf_blowjob_2
            else:
                jump hg_pf_blowjob_1

    $ states.her.ev.suck_it.snape_encounter = True

    stop music fadeout 1.0
    her "{size=-2}[name_genie_hermione], no!{/size}" ("angry", "squint", "worried", "mid", emote="angry")

    nar "Hermione gives your balls a firm twist full of frustration."
    gen "Ouch!" ("angry", xpos="far_left", ypos="head")

    play sound "sounds/door.ogg"
    call sna_chibi("stand","door","base")
    with d3
    pause.8

    sna "Good, you're here." ("snape_01", xpos="base", ypos="base")
    gen "{size=-2}Get to it, [name_hermione_genie]...{/size}" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("soft", "narrow", "angry", "down")

    call sna_walk("mid", "base")
    pause.2

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    call her_chibi_scene("bj", trans=d5)
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "worried", "stare")
    sna "Listen, there is something I want to discuss..." ("snape_06")
    gen "Oh... Yes..." ("base", xpos="far_left", ypos="head")
    sna "*Hmm*...?" ("snape_05")
    sna "Genie? Are you alright?" ("snape_05")
    her "{size=-4}(Ginny!!? Is she here as well?!){/size}" ("open_wide_tongue", "squint", "worried", "stare")
    her "{size=-4}(No, please! I will die of shame!){/size}" ("open_wide_tongue", "happyCl", "worried", "up")
    gen "Yes, Severus, I am fine..." ("base", xpos="far_left", ypos="head")
    her "{size=-4}(What? *Slurp*...? *Slurp*...? *Gulp*...?){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
    sna "What are you... looking at?" ("snape_05")
    gen "*Ehm*... Just admiring...{w=0.5} the cupboard." ("base", xpos="far_left", ypos="head")
    gen "Please, continue..." ("base", xpos="far_left", ypos="head")
    sna "..............." ("snape_05")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "base", "stare")
    gen "Did you want to discuss something?" ("base", xpos="far_left", ypos="head")
    sna "Yes. That Granger girl." ("snape_06")
    her "{size=-4}(*Slurp*...! *Gobble*...! *Gulp*...!){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Oh... What about her?" ("base", xpos="far_left", ypos="head")
    sna "You promised that you would take care of the little witch." ("snape_04")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "squint", "worried", "stare")
    sna "But she is still being a major pain in my arse!" ("snape_04")
    sna "Her tactics have changed..." ("snape_04")
    sna "But the amount of grief she manages to bring me is the same..." ("snape_03")

    nar "You feel Hermione's grip, tighten around your cock slightly."

    gen "*Ngh*--{w=0.2} I see..." ("angry", xpos="far_left", ypos="head")
    sna "That girl is driving me crazy!" ("snape_10")
    gen "Yeah, she is--{w=0.2} *Ah*...{w=0.2} Driving me crazy as well..." ("angry", xpos="far_left", ypos="head")
    gen "But I'm sure she'll come around, if she knows what's best for her..." ("angry", xpos="far_left", ypos="head")

    nar "Hermione lessens her grip once more."

    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "base", "up")
    sna "Will you take care of this then?" ("snape_04")
    gen "Certainly... I've got her covered--{w=0.2} I mean it! I've got it, covered!" ("angry", xpos="far_left", ypos="head")
    sna "Good... That is all I wanted to hear." ("snape_06")

    if game.daytime:
        gen "Well, have a good day, Severus." ("base", xpos="far_left", ypos="head")
        sna "Yes, thank you." ("snape_06")
    else:
        gen "Good night, Severus." ("base", xpos="far_left", ypos="head")
        sna "Right..." ("snape_06")

    stop music fadeout 1.0
    call hide_characters
    with d3

    call sna_chibi("stand","mid","base", flip=True)
    with d3
    pause.2

    call sna_walk(action="leave")
    pause.8

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    nar "Hermione doesn't say a thing... But her face glows crimson due to a mix of embarrassment, guilt, and excitement."

    jump hg_hidden_blowjob_cumming

label hg_hidden_blowjob_luna: #TODO Once Luna X Hermione sex scenes are added, add in dialogue variations.
    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    her "{size=-2}[name_genie_hermione], what should I do?{/size}" ("angry", "squint", "worried", "up")
    gen "Just keep sucking my cock, [name_hermione_genie]. This doesn't concern you..." ("base", xpos="far_left", ypos="head")
    lun "Sir? Are you there? I need to talk to you."
    her "(It's Luna!)" ("disgust", "wide", "base", "stare")
    her "{size=-2}Please, [name_genie_hermione], send her away, I beg you!{/size}" ("angry", "narrow", "worried", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Please, come on in, Miss Lovegood.\"":
            pass

        "\"I am busy right now, Miss Lovegood.\"":
            her "{size=-2}Thank you, [name_genie_hermione]{/size}." ("angry", "base", "base", "mid")
            lun "Oh... I suppose I'll visit you later then, sir."
            if game.daytime:
                lun "Have a good day!"
            else:
                lun "Have a good night!"
            gen "I definitely will, Miss Lovegood!" ("base", xpos="far_left", ypos="head")

            if states.her.tier > 5:
                jump hg_pf_blowjob_2
            else:
                jump hg_pf_blowjob_1

    $ states.her.ev.suck_it.luna_encounter = True

    stop music fadeout 1.0
    her "{size=-2}[name_genie_hermione], no! Why would you let-{/size}" ("angry", "base", "worried", "stare", emote="angry")
    gen "{size=-2}Quiet, [name_hermione_genie]! Unless you want to get noticed...{/size}" ("base", xpos="far_left", ypos="head")

    #Luna comes in
    call lun_walk("mid", action="enter")

    lun "Hello, Professor." ("base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    gen "{size=-4}Get back to sucking, [name_hermione_genie]...{/size}" ("base", xpos="far_left", ypos="head")
    her "..." ("soft", "happy", "worried", "up")
    gen "{size=+4}Miss Lovegood!{/size}" ("grin", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "base", "down")
    pause.2

    call her_chibi_scene("bj", trans=d5)
    pause.8

    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "happyCl", "annoyed", "up")
    gen "*Ngh*!" ("angry", xpos="far_left", ypos="head")
    lun "Sir? Why are you yelling?" ("soft", "base", "raised", "mid")
    gen "Oh, *Ahem*... Why, I was just so excited to see you, Miss Lovegood! How can I help you?" ("grin", xpos="far_left", ypos="head")
    lun "Oh! Excited to see you too!" ("grin", "base", "base", "mid")
    gen "... Did you need anything?" ("base", xpos="far_left", ypos="head")
    lun "Oh! Yes, I was asked to deliver you a message, sir! From Professor Sprout." ("smile", "base", "base", "mid")
    gen "Professor Sprout?" ("base", xpos="far_left", ypos="head")
    gen "(Who was that again?)" ("base", xpos="far_left", ypos="head")
    lun "Yes, she's sent me to inform you about the school's latest yield of {i}Venomous Tentacula{/i}." ("base", "base", "base", "L")
    gen "(Venomous Tentacles?)" ("base", xpos="far_left", ypos="head")
    her "{size=-4}(Those things are so nasty...){/size}" ("open_wide_tongue", "closed", "annoyed", "up")

    lun "Such feisty little plants." ("angry", "base", "annoyed", "mid")
    her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "*Ah*...{w=0.4} Plants..." ("base", xpos="far_left", ypos="head")
    lun "Yes, we've been learning how to care for them properly..." ("grin", "base", "low", "mid")
    gen "So, why tell me?" ("base", xpos="far_left", ypos="head")
    lun "Professor Sprout wanted me to inform you that they've just started sucking!" ("smile", "base", "raised", "mid")
    with hpunch
    gen "What?" ("angry", xpos="far_left", ypos="head")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "squint", "base", "stare")
    lun "Sucking, sir!" ("base", "base", "base", "mid")
    her "..." ("open_wide_tongue", "narrow", "base", "up")
    lun "They're so cute! They're sucking on each other's tentacles with their little mouths!" ("crooked_smile", "happyCl", "base", "mid")
    gen "(Plants with mouths?)" ("base", xpos="far_left", ypos="head")
    lun "Normally they only do that shortly before they spread their spores." ("open", "base", "base", "L")
    lun "It's a sign that they are almost ready!" ("grin", "base", "base", "mid")
    gen "Ready? for what?" ("base", xpos="far_left", ypos="head")
    lun "Pollination!" ("crooked_smile", "base", "base", "mid")
    lun "The way Professor Sprout described it, is that they weave their tentacles around each other, then squeeze the spores out." ("soft", "base", "low", "mid")
    gen "(How nasty!)" ("base", xpos="far_left", ypos="head")
    her "{size=-4}(*Slurp*... *Slurp*...* *Gulp...){/size}" ("open_wide_tongue", "squint", "base", "stare")
    lun "You won't believe how hard it actually is to get them to that stage..." ("annoyed", "base", "base", "R")
    gen "As a matter of fact, I'm quite familiar with the process." ("base", xpos="far_left", ypos="head")
    lun "You are?" ("soft", "base", "raised", "mid")
    gen "Indeed! I've got one right here, actually!" ("grin", xpos="far_left", ypos="head")
    gen "A troublemaker this one...{w=0.4} But she's sucking--{w=0.4} *Ugh*...{w=0.2} Real good though!" ("grin", xpos="far_left", ypos="head")
    her "{size=-4}(*Slurp*... *Slurp*...* *Gulp*...){/size}" ("open_wide_tongue", "narrow", "base", "mid")
    lun "Oh! Can I see it, sir?" ("smile", "base", "base", "up")
    her "..." ("open_wide_tongue", "squint", "annoyed", "up")
    gen "Not right now, I'm afraid." ("base", xpos="far_left", ypos="head")
    gen "It's such a shy little thing. You better not get any closer!" ("base", xpos="far_left", ypos="head")
    lun "*Aww*... Okay." ("annoyed", "base", "base", "L")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "closed", "base", "mid")
    gen "I know everything about those little devils..." ("base", xpos="far_left", ypos="head")
    gen "This one was especially whiny... She would moan about every tiny little thing I wanted to do." ("base", xpos="far_left", ypos="head")
    her "..." ("open_wide_tongue", "squint", "annoyed", "up")
    gen "But now, she immideately go down on her knees..." ("base", xpos="far_left", ypos="head")
    gen "And suck like crazy!" ("grin", xpos="far_left", ypos="head")
    her "..." ("open_wide_tongue", "squint", "base", "R")
    lun "So they do not only have a head, but also knees?" ("soft", "wide", "raised", "mid")
    lun "I didn't even know that!" ("angry", "base", "base", "mid")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "base", "up")
    gen "*Ngh*...{w=0.3} Well, you learn something new every day." ("angry", xpos="far_left", ypos="head")

    lun "I hope you're being careful... Sprout told us they like to spit, and bite!" ("angry", "base", "low", "mid")
    gen "Truly?" ("base", xpos="far_left", ypos="head")
    lun "Indeed! She said they'll hit you with their saliva, or bite at your limbs!" ("mad", "base", "base", "mid")
    gen "Maybe I should count myself lucky that you showed up and told me... I've got quite a sensitive third leg." ("base", xpos="far_left", ypos="head")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "angry", "R")
    lun "Lucky indeed! Because Professor Sprout taught us an easy way to make them stop such behaviour, sir!" ("smile", "wink", "base", "mid")
    gen "I'm all ears!" ("base", xpos="far_left", ypos="head")
    lun "They hate being spat on, just as much as you, sir... Maybe even more so!" ("crooked_smile", "base", "base", "L")
    gen "(Those are some weird fucking plants...)" ("base", xpos="far_left", ypos="head")
    lun "She said that if a {i}Venomous Tentacula{/i} ever acts up--" ("open", "closed", "base", "mid")
    lun "Then you should show dominance and spit on it to put it in its place!" ("crooked_smile", "closed", "raised", "mid")
    lun "Her words, of course." ("soft", "base", "base", "R")
    gen "I see... So, like this?" ("grin", xpos="far_left", ypos="head")
    call spit_on_her
    gen "Take that, you nasty little slu--{w=0.2} *Err*... plant." ("angry", xpos="far_left", ypos="head")
    her @ tears sweat "{size=-4}(What the--){/size}" ("open_wide_tongue", "squint", "annoyed", "up")
    lun "That's right, sir!" ("grin", "base", "base", "mid")
    gen "This one's feisty!" ("angry", xpos="far_left", ypos="head")
    gen "I think it might need some more spit!" ("grin", xpos="far_left", ypos="head")
    call spit_on_her
    her @ tears sweat "{size=-4}(Stop it!){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Looks like it's working!" ("base", xpos="far_left", ypos="head")
    lun "Great job, sir!" ("smile", "base", "base", "mid")
    lun "Professor Sprout did say that sometimes a bit of tough love is the only thing that can make them behave." ("grin", "closed", "base", "mid")
    gen "Hold on a moment, now she's fighting back!" ("grin", xpos="far_left", ypos="head")
    lun "Be careful, sir! Or it will bite you!" ("soft", "wide", "base", "mid")
    gen "Don't worry, this one's getting a beating!" ("angry", xpos="far_left", ypos="head")
    call slap_her
    her @ cheeks blush tears sweat "{size=-4}(Ouch!){/size}" ("open_wide_tongue", "happyCl", "base", "up")
    call slap_her
    call slap_her
    gen "Had enough, you nasty little thing?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush tears tears_soft_sweat "{size=-4}(*Mmmph*...{w=0.3} *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "worried", "up")
    call slap_her
    gen "Looks like it needs some more!" ("grin", xpos="far_left", ypos="head")
    call slap_her
    call slap_her
    her @ cheeks blush tears tears_soft_sweat "{size=-4}(Ouch!){/size}" ("open_wide_tongue", "narrow", "worried", "stare")
    gen "There we go... It seems to have calmed down..." ("base", xpos="far_left", ypos="head")
    lun "Impressive! I didn't think we would see such good results this quickly, sir!" ("soft", "wide", "base", "mid")
    lun "I'll have to tell Professor Sprout! She'll be overjoyed to hear about your training methods!" ("crooked_smile", "base", "base", "mid")
    gen "Spitting on her was a great idea!" ("grin", xpos="far_left", ypos="head")
    gen "Give her my thanks, Miss Lovegood." ("grin", xpos="far_left", ypos="head")
    lun "Certainly, sir." ("base", "base", "base", "mid")

    if game.daytime:
        lun "Have a nice day!" ("base", "base", "base", "R")
    else:
        lun "Good night!" ("base", "base", "base", "mid")

    #Luna leaves.
    call lun_walk(action="leave")

    stop music fadeout 1.0
    gen "Well that wasn't too bad, was it?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-4}(............................. *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "worried", "up")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    nar "Hermione doesn't say a thing... But her face glows crimson due to a mix of embarrassment, guilt, and excitement."

    jump hg_hidden_blowjob_cumming

#Needs Friendship level parameter added for tonks chat variations if states.ton.level < X:
#Needs event label check for Tonks to ask if it's susan in there. replace if ag_st_imperio.tier >= 5:
#Add Tonks BJ counter
label hg_hidden_blowjob_tonks:
    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    her "{size=-2}[name_genie_hermione], what should I do?{/size}" ("shock", "wide", "base", "stare")
    gen "{size=-2}Just keep sucking my cock, [name_hermione_genie]... This doesn't concern you.{/size}" ("base", xpos="far_left", ypos="head")
    ton "Professor? Is it okay if I come in?"
    her "(It's Professor Tonks!)" ("clench", "happyCl", "worried", "mid")
    her "{size=-2}Please, [name_genie_hermione], don't let her in!{/size}" ("open", "base", "worried", "mid")
    her "{size=-2}I don't want her to walk in on us like this...{/size}" ("angry", "narrow", "worried", "down")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Please, come on in.\"":
            pass

        "\"I am busy right now, Miss Tonks.\"":
            her "{size=-2}Thank you, [name_genie_hermione]...{/size}" ("soft", "base", "base", "mid")
            ton "Busy?"
            ton "Could it be..."
            ton "Is Snape with you?"
            if game.daytime:
                ton "Are you two having one of your silly little duels again?"
            else:
                ton "Don't stay up drinking again..."
                ton "We wouldn't want him to make a fool of himself... Not in front of the students."
                ton "He made such a mess last time..."

            call her_chibi_scene("bj", trans=d5)
            pause.8

            her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "squint", "worried", "up")
            gen "Yep, just me and Snape, duetting as always..." ("base", xpos="far_left", ypos="head")
            ton "Nice try... I just saw Severus on my way here... So, you're with a student, then?"
            her "{size=-4}(.......... *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "worried", "stare")
            ton "Who is she?"

            random:
                block if states.ast.ev.imperio_with_tonks.completed_once:
                    ton "Is it the blonde girl? Or..."
                    her "{size=-4}(Blonde!?! *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "squint", "worried", "up")
                    her "{size=-4}(*Slurp*... *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
                block if states.ast.ev.imperio_with_susan.completed_once:
                    ton "You aren't shagging that busty red head, are you?"
                    her "{size=-4}(Busty who? *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "squint", "worried", "up")
                    her "{size=-4}(Is she talking about Susan? *Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")

            gen "That's none of your concern, Miss Tonks!" ("base", xpos="far_left", ypos="head")
            gen "You may leave now..." ("base", xpos="far_left", ypos="head")
            her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "base", "up")

            if states.ton.level < 50:
                ton "You sure you don't need my assistance?"
                gen "I said, leave!" ("angry", xpos="far_left", ypos="head")
            else:
                ton "Perhaps I could help with--"
                gen "Maybe later, Miss Tonks." ("base", xpos="far_left", ypos="head")

            ton "Alright then..."
            ton "*Giggles*"
            her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "I think she's gone..." ("base", xpos="far_left", ypos="head")

            if states.her.tier > 5:
                jump hg_pf_blowjob_2
            else:
                jump hg_pf_blowjob_1

    $ states.her.ev.suck_it.tonks_encounter = True

    # Setup
    $ ton_outfit_last.save() # Store current outfit.
    $ tonks.equip(ton_outfit_default)

    stop music fadeout 1.0
    her "{size=-2}[name_genie_hermione], no! Please, she will--{/size}" ("angry", "base", "worried", "stare", emote="angry")
    gen "*Shhh*... Keep your voice down..." ("base", xpos="far_left", ypos="head")
    pause.2

    play sound "sounds/door.ogg"
    call ton_chibi("stand","door","base")
    call chibi_emote("hearts", "tonks")
    with d3
    pause.5

    call chibi_emote("hide", "tonks")
    with d3
    pause.1

    call ton_walk("mid","base")

    if game.daytime:
        ton "Hello, Sir." ("base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    else:
        ton "Good evening, Sir." ("base", "base", "shocked", "mid", xpos="right", ypos="base", trans=d3)

    gen "{size=-4}Just keep sucking, [name_hermione_genie]...{/size}" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("soft", "narrow", "base", "down")
    call her_chibi_scene("bj", trans=d5)
    pause.8

    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Tonks! What can I do for you?" ("grin", xpos="far_left", ypos="head")
    ton "I was wondering if we could--" ("open", "base", "raised", "R")
    ton "(...)" ("annoyed", "narrow", "raised", "L")
    ton "Am I interrupting something?" ("soft", "base", "raised", "down")
    her "(She's going to find out!!!)" ("open_wide_tongue", "narrow", "worried", "up")
    gen "Nothing important..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Tell the truth-":
            gen "Just stuffing Miss Granger's cute little mouth..." ("base", xpos="far_left", ypos="head")
            gen "With my cock!" ("grin", xpos="far_left", ypos="head")
            call her_chibi_scene("bj_pause", trans=d5)

        "-Lie-":
            gen "... Just polishing...{w=0.5} the woodwork." ("base", xpos="far_left", ypos="head")
            ton "Like I'm going to believe that..." ("upset", "base", "base", "downR")
            ton "Are you masturbating?" ("horny", "base", "raised", "mid")

            if states.ton.level < 50:
                ton "Or perhaps there's someone behind that desk who has their tongue wrapped around it?" ("soft", "base", "raised", "L")
                call her_chibi_scene("bj_pause", trans=d5)
                her "{size=-4}*Blergchhhgh*... *Cough*... *Cough*... *Cough*...{/size}" ("open_wide_tongue", "wide", "base", "stare")
                ton "What was that?" ("base", "base", "raised", "mid")
                ton "Surely there's nobody at this school who would be able to pleasure you in such a way..." ("grin", "base", "raised", "mid")
            else:
                ton "Are you stroking your hard, {w=0.3}magnificent, {w=0.3}cock?" ("soft", "base", "base", "stare")
                with hpunch
                call her_chibi_scene("bj_pause", trans=d5)
                her "{size=-4}(*Blergchhhgh*... *Cough*... *Cough*... *Cough*...){/size}" ("open_wide_tongue", "slit", "worried", "ahegao")
                her "{size=-4}What??{/size}" ("clench", "narrow", "base", "up")
                ton "What was that?" ("open", "base", "raised", "mid")
                ton "Professor?!" ("grin", "base", "base", "mid")
                gen "*Err*--{w=0.5} My belly?" ("base", xpos="far_left", ypos="head")
                ton "Sounded like somebody who doesn't know how to deep-throat a dick properly..." ("open", "base", "base", "R")

            her "(Excuse me?!)" ("annoyed", "narrow", "base", "up")
            gen "Don't be mean, she's doing her best..." ("base", xpos="far_left", ypos="head")
            ton "So, there is a girl over there!" ("horny", "wide", "raised", "down")
            ton "Who is it? Tell me!" ("soft", "shocked", "shocked", "mid")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            gen "It's Miss Granger." ("base", xpos="far_left", ypos="head")

    ton "Miss Granger?!" ("open", "wide", "shocked", "stare")

    if states.her.public_level <= 15:
        ton "*Hmm?*... I thought she'd be busy pretending to study in the library." ("open", "base", "raised", "mid")
        her "(Pretending???)" ("angry", "narrow", "base", "up")
    else:
        ton "*Oh?* I could've sworn I just saw her in the library fluttering her eyelashes to some Slytherin boy..." ("open", "base", "raised", "mid")
        her "(What!!?)" ("angry", "narrow", "annoyed", "up")
        with hpunch
        gen "Ouch, I felt that..." ("base", xpos="far_left", ypos="head")

    if states.ton.level < 50:
        ton "So, she has her lips wrapped around you? {w=0.5}Right now???" ("soft", "base", "shocked", "L")
    else:
        ton "You're telling me that you are fucking her mouth? {w=0.5}Right now???" ("soft", "base", "shocked", "mid")

    gen "Not at this very moment..." ("base", xpos="far_left", ypos="head")
    gen "Although I'm sure she knows what it best for her and will get back to it, any moment--" ("base", xpos="far_left", ypos="head")

    call her_chibi_scene("bj", trans=d5)
    gen "*Ngh*--{w=0.2} There she goes!" ("angry", xpos="far_left", ypos="head")
    ton "Oh, I've got to see this..." ("horny", "base", "base", "down")
    ton "" ("horny", "base", "base", "down", xpos="mid", trans=d3)
    pause.2
    gen "Wait!" ("angry", xpos="far_left", ypos="head")
    ton "*Hmm*?" ("horny", "base", "raised", "mid")

    gen "You better not come any closer..." ("base", xpos="far_left", ypos="head")
    gen "Or I fear she will bite me..." ("base", xpos="far_left", ypos="head")
    gen "Or worse..." ("angry", xpos="far_left", ypos="head")
    gen "She'll stop sucking..." ("base", xpos="far_left", ypos="head")
    her "(Damn right I will...)" ("open_wide_tongue", "narrow", "annoyed", "up")

    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "closed", "annoyed", "ahegao")
    ton "Very well..." ("base", "base", "raised", "R", xpos="right", trans=d3)
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "squint", "worried", "up")

    ton "Is that really, {w=0.5}Miss Hermione Granger,{w=0.5} back there?" ("horny", "narrow", "base", "mid")
    ton "I can't help but think..." ("open", "base", "raised", "L")
    ton "Well, let's say I wouldn't be surprised if you were just fucking with me..." ("soft", "base", "base", "mid")
    gen "Me, fucking with you?" ("base", xpos="far_left", ypos="head")
    gen "... The only fucking going on here, is me, fucking Miss Granger's mouth." ("grin", xpos="far_left", ypos="head")
    ton "That's too good to be true!" ("horny", "narrow", "base", "stare")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")

    ton "Miss Granger, If that's really you back there, why don't you say \"hi\" to your favourite teacher?" ("grin", "base", "raised", "down")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    ton "I will reward you with fifty house points if you say something!" ("base", "base", "raised", "down")
    with hpunch
    gen "What?!" ("angry", xpos="far_left", ypos="head")

    call her_chibi_scene("bj_pause", trans=d5)

    her "(Oh wow... That's a lot of points!)" ("clench", "squint", "base", "stare")
    gen "Don't listen to her! Keep sucking!" ("angry", xpos="far_left", ypos="head")
    her "..." ("mad", "squint", "base", "up")

    call her_chibi_scene("bj", trans=d5)

    gen "You can't give her that many points! She's already getting {number=current_payout} from me!" ("angry", xpos="far_left", ypos="head")
    gen "That's already a massive amount! I think..." ("base", xpos="far_left", ypos="head")
    ton "So what? The girl has clearly earned those, from sucking your cock!" ("soft", "base", "annoyed", "mid")
    ton "Now, what do you say Miss Granger?" ("horny", "base", "annoyed", "down")
    ton "Fifty points could be yours..." ("open", "base", "raised", "down")
    ton "You only have to say hello to me..." ("base", "narrow", "base", "L")
    ton "I promise I won't tell anybody..." ("base", "base", "base", "down")
    ton "It will be our little secret." ("soft", "base", "shocked", "down")
    her "(...)" ("open_wide_tongue", "narrow", "worried", "down")
    gen "Do what you must, girl..." ("base", xpos="far_left", ypos="head")
    her "(...............)" ("open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj_pause", trans=d5)

    her @ cheeks blush "*Ahem*..." ("disgust", "narrow", "worried", "down")

    pause 1.0

    ton "Oh my... Is that..." ("horny", "base", "base", "down")

    her "H-Hello, professor Tonks." ("clench", "happyCl", "worried", "mid")

    ton "Miss Granger... Such a pleasant surprise." ("grin", "wide", "raised", "L")
    ton "Are you having a good time back there?" ("base", "wide", "base", "L")
    her "(.......)" ("soft", "narrow", "worried", "up")
    her "*Ehm*........." ("disgust", "narrow", "worried", "down")
    ton "It certainly must be a sight to behold..." ("base", "base", "base", "mid")
    her "*Ehm*........." ("annoyed", "narrow", "worried", "down")
    ton "Well then... Don't let me stand in your way of completing your task..." ("base", "base", "base", "mid")
    her "........." ("soft", "narrow", "worried", "down")

    her "" ("open_wide_tongue", "squint", "worried", "up")
    call her_chibi_scene("bj", trans=d5)

    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")

    ton "*Giggles*" ("base", "base", "base", "down")

    if states.ton.level < 50:
        ton "You're really going to town, aren't you... I can hear those lips smacking, all the way from here..." ("base", "base", "base", "down")
        ton "You should make sure to breathe every once in a while, dear girl." ("horny", "base", "base", "mid")
        gen "If you need to have her vitals checked out afterwards - I'm sure we could come to an arrangement." ("grin", xpos="far_left", ypos="head")
    else:
        ton "I'd love to join you back there, Miss Granger..." ("base", "base", "base", "down")
        her "{size=-4}(She'd love to--){/size}" ("open_wide_tongue", "narrow", "worried", "up")
        gen "The more, the merrier!" ("grin", xpos="far_left", ypos="head")

    ton "I'm sorry, Professor... I'm already pre-occupied with something..." ("open", "narrow", "base", "R")
    if game.daytime:
        ton "I'm currently teaching a class, how to cast a simple deflection spell..." ("open", "base", "raised", "down")
    else:
        ton "I'm preparing some material, on how to cast a simple deflection spell..." ("open", "base", "raised", "down")

    ton "We are already two sessions behind my planned class schedule." ("annoyed", "base", "base", "mid")
    ton "I came to you to get consultation about some of the material I had prepared for them." ("open", "base", "shocked", "down")
    gen "(Yeah right... More like she wanted some of my firewhisky...)" ("base", xpos="far_left", ypos="head")
    ton "But since you have to take care of Miss Granger right now..." ("base", "base", "raised", "down")
    ton "I suppose it can wait." ("base", "base", "raised", "R")
    ton "Who said teaching would be easy, am I right?" ("open", "closed", "shocked", "mid")
    gen "It's quite easy, actually." ("base", xpos="far_left", ypos="head")
    ton "As a headmaster maybe... I'm sure your private tutelage is very popular..." ("horny", "base", "raised", "down")
    gen "It can get quite hard, taking care of all those girls." ("base", xpos="far_left", ypos="head")
    ton "I can certainly see that..." ("base", "base", "annoyed", "down")
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")

    ton "Anyhow..." ("open", "base", "raised", "R")
    ton "Hermione, for your exceptional and benevolent effort of sucking your headmaster's cock, {w=0.5}I hereby reward the house Gryffindor..." ("soft", "base", "base", "down")

    call her_chibi_scene("bj_pause", trans=d5)
    ton "Sixty-nine points!" ("grin", "wide", "base", "mid")
    $ gryffindor += 69

    her "(Sixty-nine! That's even more than she offered before!)" ("shock", "wide", "base", "up")
    gen "Didn't you say fifty, earlier?" ("angry", xpos="far_left", ypos="head")
    ton "Yes, but sixty-nine is so much better!" ("horny", "base", "raised", "mid")
    ton "Don't you think so too, Miss Granger?" ("base", "base", "angry", "down")
    her "*Ehm*... Yes... Thank you, Professor Tonks." ("disgust", "happyCl", "worried", "mid")
    gen "Less talking, more sucking, Miss Granger!" ("base", xpos="far_left", ypos="head")
    her "Sorry, sir..." ("soft", "narrow", "annoyed", "up")

    call her_chibi_scene("bj", trans=d5)
    her "{size=-4}(*Slurp*... *Slurp*... *Gulp*...){/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
    ton "I'm going to have to go, Professor." ("open", "closed", "shocked", "mid")
    ton "Of course, I wish I could stay for a bit longer..." ("soft", "base", "base", "L")
    gen "Yes, such a shame." ("base", xpos="far_left", ypos="head")
    ton "Make sure she swallows for me." ("horny", "base", "base", "mid")
    gen "Every last drop!" ("grin", xpos="far_left", ypos="head")

    if game.daytime:
        ton "See you in class, {i}Parseltongue{/i}!" ("horny", "base", "angry", "down")
    else:
        ton "Have a good night, {i}Parseltongue{/i}!" ("horny", "base", "annoyed", "down")

    her ".........." ("open_wide_tongue", "happyCl", "worried", "mid")

    #Tonks leaves.
    stop music fadeout 1.0

    call ton_walk(action="leave")
    pause.5

    $ tonks.equip(ton_outfit_last) # Equip custom outfit.

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    nar "Hermione doesn't say a thing... But her face glows crimson due to a mix of embarrassment, guilt, and excitement."

    jump hg_hidden_blowjob_cumming

label hg_hidden_blowjob_cumming:
    call her_chibi_scene("bj", trans=d5)
    pause.8

    her @ cheeks blush "*Slurp*! *Slurp*! *Gulp*!" ("open_wide_tongue", "squint", "worried", "up", flip=False)
    nar "She continues to suck on your cock with an almost vicious determination."
    nar "Her technique is lacking, but she makes up for it with the amount of effort she puts in."

    gen "Yes... I love your eager, little mouth, girl..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Gobble*! *Gobble*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")

    call her_chibi_scene("bj_pause", trans=d5)

    her @ cheeks blush "[name_genie_hermione]?" ("soft", "squint", "worried", "up")
    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Are you going to cum on my face today?" ("open", "squint", "worried", "up")
    her @ cheeks blush "Or are you planning on finishing in my mouth?" ("soft", "narrow", "base", "up")

    $ _facial = False
    $ _mouth = False
    menu:
        "\"My plan is to splatter your face with cum!\"":
            $ _facial = True
            her @ cheeks blush "I see..." ("soft", "squint", "base", "up")
            her "Well, I suppose semen does contain numerous antioxidants..." ("open", "narrow", "base", "dead")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her "It's good for the skin..." ("open", "closed", "base", "mid")
            gen "I see... One facial, coming right up!" ("base", xpos="far_left", ypos="head")
            gen "But first, you'll have to suck it some more!" ("base", xpos="far_left", ypos="head")

        "\"My plan is to fill your mouth with cum!\"":
            $ _mouth = True
            her @ cheeks blush "I see..." ("soft", "narrow", "base", "up")
            gen "Why do you ask?" ("base", xpos="far_left", ypos="head")
            if not states.her.status.gokkun:
                her @ cheeks blush "(I've never done that before...)" ("soft", "narrow", "worried", "down")
                gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her "Oh!" ("angry", "narrow", "worried", "mid")
            her "Well, I am trying to watch my calorie-intake..." ("soft", "narrow", "worried", "down")
            her "I was just considering how many calories your load may contain..." ("soft", "narrow", "base", "down")
            her "I'd like to know if I should consider skipping my next meal..." ("soft", "squint", "worried", "R")
            gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Yes?" ("soft", "narrow", "annoyed", "up")
            gen "Dick back in the mouth." ("base", xpos="far_left", ypos="head")

        "\"I don't plan so far ahead.\"":
            her @ cheeks blush "I see..." ("soft", "squint", "worried", "up")
            gen "Don't you like surprises?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Not really..." ("soft", "closed", "worried", "mid")
            her @ cheeks blush "I much rather plan ahead..." ("open", "closed", "base", "up")
            gen "Well, some things in life are unpredictable..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("clench", "narrow", "base", "up")
            gen "Now, get back to sucking." ("base", xpos="far_left", ypos="head")

        "\"What would you like?\"":
            random:
                block:
                    her "I suppose I wouldn't mind if you came on my face..." ("base", "narrow", "base", "down")
                    her "At least it's good for the skin." ("open", "closed", "base", "mid")
                    gen "*Hmm*... You're not trying to get out of swallowing, are you?" ("base", xpos="far_left", ypos="head")
                    her "Of course not..." ("soft", "closed", "base", "mid")
                    gen "Well, we'll see about that." ("base", xpos="far_left", ypos="head")
                    gen "Dick back in the mouth." ("base", xpos="far_left", ypos="head")
                block:
                    her "I suppose I wouldn't mind if you came in my mouth..." ("base", "narrow", "base", "down")
                    gen "Oh?" ("base", xpos="far_left", ypos="head")
                    if game.daytime:
                        her "I mean, since this has taken so long, I'm sure I've missed lunch..." ("soft", "closed", "base", "mid")
                    else:
                        her "I mean, I need to go to bed soon... I'd rather not spend time cleaning up...." ("open", "closed", "base", "mid")
                    gen "Trying to be cheeky, are you?" ("base", xpos="far_left", ypos="head")
                    her "..." ("normal", "base", "base", "mid")
                    gen "Now, put this back against the inside of those cheeks." ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "..." ("soft", "narrow", "base", "down")
    call her_chibi_scene("bj", trans=d5)
    her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "You're getting better at this, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Slurp*! *Gulp*!" ("open_wide_tongue", "narrow", "base", "up")
    gen "Okay, say something nasty now..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*--?" ("open_wide_tongue", "narrow", "annoyed", "up")
    call her_chibi_scene("bj_pause", trans=d5)

    if states.her.tier <= 5:
        her "*Uhm*..." ("angry", "narrow", "base", "down")
        her "I eat cockroaches?" ("angry", "base", "base", "mid")
        gen "What the fuck?" ("base", xpos="far_left", ypos="head")
        her "T-they are pretty nasty, [name_genie_hermione]..." ("angry", "base", "base", "mid")
        gen "No, [name_hermione_genie], I mean something dirty!" ("base", xpos="far_left", ypos="head")
        gen "And don't you dare to say \"mud\"!" ("base", xpos="far_left", ypos="head")
        gen "I meant dirty in a sexual way!" ("base", xpos="far_left", ypos="head")
        her "Oh... *Ehm*..." ("angry", "narrow", "base", "down")
        gen "Ah, never mind, the moment is gone..." ("base", xpos="far_left", ypos="head")
        her "*Ehm*... I'm sorry, [name_genie_hermione]." ("angry", "base", "base", "mid")
        gen "Then make it up to me, by sucking my cock some more." ("base", xpos="far_left", ypos="head")
        her "Of course, [name_genie_hermione]." ("upset", "closed", "base", "mid")
    else:
        her "I'm... I'm a cumslut, [name_genie_hermione]." ("base", "squint", "base", "mid")
        gen "Oh, yes you are, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "It's all I can think about, [name_genie_hermione]." ("base", "narrow", "worried", "down")
        her "As soon as I leave your office, always wonder when I'll get to enjoy your cum again..." ("base", "narrow", "worried", "down")
        her "Please [name_genie_hermione], I must have it!" ("base", "narrow", "worried", "down")
        gen "You'll have it in just a moment, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "But first, you must suck my cock some more." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]..." ("open", "narrow", "base", "dead")
        gen "You're welcome, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "..." ("base", "narrow", "base", "up")

    call her_chibi_scene("bj", trans=d5)
    her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Yes... Just like that..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "I think I'm almost-- *Ngh*..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
    gen "Yes... I'm definitely--" ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Gobble*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
    gen "Alright, [name_hermione_genie]... Final stretch!" ("base", xpos="far_left", ypos="head")
    gen "Show me what you've got!" ("angry", xpos="far_left", ypos="head")
    her "*Gobble-gobble-slurp-gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Yes! Faster!" ("angry", xpos="far_left", ypos="head")
    her "{size=+5}*Gobble-gobble-slurp-gobble*!{/size}" ("open_wide_tongue", "narrow", "base", "up")
    gen "{size=+5}Yes! Yes! Yes! Yes!{/size}" ("angry", xpos="far_left", ypos="head")
    gen "*Ngh*!!!" ("angry", xpos="far_left", ypos="head")

    menu:
        gen "!!!" ("angry", xpos="far_left", ypos="head")
        "-Cum in her mouth-":
            $ states.her.status.gokkun = True
            gen "Here it comes, [name_hermione_genie]! get ready to swallow, and fast!" ("angry", xpos="far_left", ypos="head")
            her "!!!" ("open_wide_tongue", "narrow", "base", "up")

            call cum_block
            call her_chibi_scene("bj_cum_in", trans=d5)
            pause.8

            gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
            gen "Do it! Swallow my cum, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
            her "*Gulp!-Gulp!-Gulp*!" ("open_wide_tongue_cum", "narrow", "annoyed", "up")
            with hpunch
            gen "Yes! Down your fucking throat!" ("angry", xpos="far_left", ypos="head")
            her "*Gulp-gulp-gulp-gulp-gulp*!" ("open_wide_tongue_cum", "narrow", "annoyed", "up")

            stop music fadeout 1.0
            call ctc

            gen "*Ah*... I think that's all of it." ("base", xpos="far_left", ypos="head")
            gen "You can let go now..." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj_pause", trans=d5)
            her "..........................." ("full_cum", "narrow", "base", "dead")
            her "................" ("full_cum", "narrow", "base", "dead")
            her "........" ("full_cum", "narrow", "base", "dead")
            play sound "sounds/gulp.ogg"
            her "*Gulp*!" ("cum", "happyCl", "worried", "mid")
            her "*Gua-ha*..." ("open_wide_tongue", "narrow", "base", "stare")
            gen "... Are you alright, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "Yes, [name_genie_hermione]..." ("grin", "narrow", "base", "dead")
            if _facial:
                her "Although I thought you said you were going to, \"splatter my face with cum\"..." ("soft", "narrow", "base", "dead")
                gen "Oh, right... My apologies..." ("base", xpos="far_left", ypos="head")
                her "It's fine [name_genie_hermione]... I don't mind..." ("base", "narrow", "base", "dead")
            if _mouth:
                her "You allowed me ample time to prepare myself..." ("grin", "narrow", "base", "dead")
            if game.daytime:
                gen "So, will you be skipping lunch today?" ("base", xpos="far_left", ypos="head")
                her "Yes, most likely..." ("grin", "narrow", "base", "dead")
            her "How come you always cum so much, [name_genie_hermione]..." ("open", "wink", "base", "mid")
            gen "*Heh*... You're saying that as if it's my fault." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "............." ("soft", "narrow", "base", "down")
            her @ cheeks blush "May I get paid now?" ("soft", "wink", "base", "mid")

            if states.her.tier >= 6:
                if game.daytime:
                    gen "You want points, even though I just gave you lunch?" ("base", xpos="far_left", ypos="head")
                else:
                    gen "You want points, even though I fed you dinner?" ("base", xpos="far_left", ypos="head")
                her "............." ("annoyed", "squint", "base", "mid")
                her "Fine, I suppose this was a worthy meal." ("annoyed", "squint", "base", "mid")
            else:
                gen "Certainly...." ("grin", xpos="far_left", ypos="head")

        "-Cum on her face-":
            call her_chibi_scene("bj_pause", trans=d5)
            gen "Ready for your facial, [name_hermione_genie]?" ("angry", xpos="far_left", ypos="head")
            if _mouth:
                her "My facial? But I thought you said--" ("soft", "narrow", "base", "up")
            else:
                her "Yes, [name_genie_hermione]!" ("grin", "narrow", "base", "dead")
            gen "Here it comes!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            call her_chibi_scene("bj_cum_out", trans=d5)
            pause.8

            $ hermione.set_cum(face="light")
            gen "{size=+7}Whore!{/size}" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "!!?" ("grin", "narrow", "base", "dead")
            call ctc

            $ hermione.set_cum(face="heavy")

            her @ cheeks blush "[name_genie_hermione]..." ("grin", "happyCl", "base", "stare")
            gen "All over your fucking face!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "*Aaah*!" ("grin", "narrow", "base", "dead")

            call her_chibi_scene("bj_cum_out_done", trans=d5)

            gen "Well then, I'm done." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...................................." ("grin", "narrow", "base", "dead")
            gen "I said I'm done, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Yes, I heard you [name_genie_hermione]..." ("base", "narrow", "base", "dead")
            gen "So... Aren't you going to clean up?" ("base", xpos="far_left", ypos="head")
            her "In a moment..." ("grin", "narrow", "base", "dead")
            gen "Take your time, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            call blkfade

            stop music fadeout 1.0
            $ hermione.set_cum(None)
            nar "After a relatively brief period of time later..."

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            call hide_blkfade
            pause.5

            her "I take it you enjoyed yourself, [name_genie_hermione]?" ("angry", "wink", "base", "mid", xpos="mid", ypos="base")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            gen "Yes I did, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Good... So, I may get paid now?" ("base", "squint", "base", "mid")

            if states.her.tier >= 6:
                gen "Even after I just gave you a salon treatment?" ("base", xpos="far_left", ypos="head")
                gen "Other women pay a lot of money for a good facial." ("base", xpos="far_left", ypos="head")
                her "............." ("annoyed", "squint", "base", "mid")
                her "Fine, but my skin better look glamorous by tomorrow." ("annoyed", "squint", "base", "mid")
                gen "You can always come back for more..." ("grin", xpos="far_left", ypos="head")
            else:
                gen "Certainly...." ("grin", xpos="far_left", ypos="head")

    jump end_hg_pf_blowjob

### Fourth Blowjob ###

label hg_pf_blowjob_2:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj", trans=d9)
    call ctc

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 #HERMIONE if_changed
    her "*Slurp*! *Slurp*! *Gulp*!" ("open_wide_tongue", "narrow", "base", "up", ypos="head", flip=False)
    gen "Yes, good girl..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
    gen "Lick the shaft..." ("base", xpos="far_left", ypos="head")
    her "*Lick*! *Slurp*! *Lick*!" ("open_wide_tongue", "narrow", "base", "up")
    nar "Hermione keeps sucking on your cock as if her life depended on it."
    nar "Her technique is almost perfect, and she is incredibly enthusiastic."
    gen "Yes... I love your eager, little mouth, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "*Gobble*! *Gobble*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")

    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    her "[name_genie_hermione]?" ("soft", "squint", "base", "up")
    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
    her "Are there any further actions you would like me to take that would please you today?" ("base", "squint", "worried", "up")
    gen "Well, since you asked..." ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Pretend I am your father.\"":
            her "My father?" ("angry", "wink", "base", "mid")
            gen "Would that be a problem?" ("base", xpos="far_left", ypos="head")
            her "I suppose not..." ("base", "narrow", "worried", "down")
            her "I mean it's just pretending, right?..." ("soft", "squint", "base", "mid")
            gen "Great! Get that dick back in your mouth then." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj", trans=d5)
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "That's it, princess... Suck daddy's dick." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Now, tell me how much you want it." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "I want it... I want it so much, daddy..." ("soft", "narrow", "annoyed", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "It's all I think about when we're home alone..." ("base", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Gulp*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "When we're sitting together on the couch watching T.V..." ("base", "narrow", "base", "up")
            her "I just imagine that I am sucking your cock instead..." ("base", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Lick*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Sometimes... I even wish that mum left you..." ("soft", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Slurp*! *Lick*!" ("open_wide_tongue", "narrow", "base", "dead")
            gen "And why is that?" ("base", xpos="far_left", ypos="head")
            call her_chibi_scene("bj_pause", trans=d5)
            her "So that I'm the only one to get your dick..." ("soft", "narrow", "worried", "down")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "You're doing very good, [name_hermione_genie]... Now, why don't you--" ("base", xpos="far_left", ypos="head")
            call her_chibi_scene("bj_pause", trans=d5)
            her "You'll come home every day, after work..." ("base", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "dead")
            call her_chibi_scene("bj_pause", trans=d5)
            her "And you'll throw me onto my bed..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "and then you'll use me..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "however you want..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "for as long as you want..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "you won't even ask..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "you'll just take me..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "That's it princess...{w=0.4} Almost there..." ("base", xpos="far_left", ypos="head")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Where do you want to cum today, daddy?" ("soft", "narrow", "annoyed", "up")
            her "Are you going to cover my face?" ("soft", "narrow", "annoyed", "up")
            her "Or make me swallow your big load?" ("grin", "narrow", "base", "dead")
            gen "Why don't you wait and find out?" ("base", xpos="far_left", ypos="head")
            her "Yes daddy..." ("soft", "narrow", "annoyed", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Yes... Keep sucking, just like that... Good girl..." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Do it for daddy." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Come on, princess." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gobble*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Alright, [name_hermione_genie]... I'm almost there." ("base", xpos="far_left", ypos="head")
            gen "Make daddy proud!" ("angry", xpos="far_left", ypos="head")
            her "*Gobble-gobble-slurp-gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Yes... Make me--" ("angry", xpos="far_left", ypos="head")
            her "{size=+5}*Gobble-gobble-slurp-gobble*!{/size}" ("open_wide_tongue", "narrow", "base", "dead")
            gen "{size=+5}Yes! Yes! Yes! Yes!{/size}" ("angry", xpos="far_left", ypos="head")
            gen "*Ngh*!!!" ("angry", xpos="far_left", ypos="head")

            menu:
                gen "!!!" ("angry", xpos="far_left", ypos="head")
                "-Cum in her mouth-":
                    $ states.her.status.gokkun = True
                    gen "Here it comes, [name_hermione_genie]! Here comes daddy!" ("angry", xpos="far_left", ypos="head")
                    her "!!!" ("open_wide_tongue", "narrow", "base", "up")

                    call cum_block
                    call her_chibi_scene("bj_cum_in", trans=d5)
                    pause.8

                    gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
                    gen "Drown in my cum, whore!" ("angry", xpos="far_left", ypos="head")

                    her "*Gulp!-Gulp!-Gulp*!" ("open_wide_tongue_cum", "narrow", "annoyed", "up")
                    with hpunch
                    gen "Yes! Down your fucking throat, slut!" ("angry", xpos="far_left", ypos="head")
                    her "*Gulp-gulp-gulp-gulp-gulp*!" ("open_wide_tongue_cum", "narrow", "base", "up")
                    stop music fadeout 1.0
                    call ctc

                    call her_chibi_scene("bj_pause", trans=d5)
                    pause.8

                    gen "*Ah*... Now that was some blowjob..." ("base", xpos="far_left", ypos="head")
                    gen "You can let it go now... Princess..." ("base", xpos="far_left", ypos="head")
                    her "..........................." ("full_cum", "narrow", "base", "dead")
                    her "................"
                    her "........"

                    play sound "sounds/gulp.ogg" #Sound of gulping down a liquid.
                    her "*GULP*!" ("cum", "happyCl", "worried", "mid")
                    her "*Gua-ha*..." ("open_wide_tongue", "narrow", "base", "stare")

                    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
                    her "So tasty..." ("grin", "narrow", "base", "dead")
                    gen "Really?" ("base", xpos="far_left", ypos="head")
                    her "Yes daddy..." ("grin", "narrow", "base", "dead")
                    her "It's always tasty when it's daddy's..." ("grin", "narrow", "base", "dead")
                    gen "*Heh*... Is that so?" ("base", xpos="far_left", ypos="head")
                    her "............." ("grin", "narrow", "base", "dead")
                    nar "She leans forward and gives your cock a small kiss."
                    with kissiris
                    her "Of course, daddy!" ("base", "closed", "base", "mid_soft")
                    her "I hope you enjoyed my little performance, [name_genie_hermione]..." ("angry", "wink", "base", "mid")
                    gen "Performance? Oh, yes, your performance! Yes, it was very good, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
                    her "Thank you, [name_genie_hermione]..." ("soft", "narrow", "base", "down")

                "-Cum on her face-":
                    call her_chibi_scene("bj_pause", trans=d5)
                    gen "Ready for your cum-load, princess?" ("angry", xpos="far_left", ypos="head")
                    her "Yes daddy!" ("grin", "narrow", "base", "dead")
                    gen "Here it comes then!" ("angry", xpos="far_left", ypos="head")

                    call cum_block
                    call her_chibi_scene("bj_cum_out", trans=d5)
                    pause.8

                    $ hermione.set_cum(face="light")

                    gen "{size=+7}Slut!{/size}" ("angry", xpos="far_left", ypos="head")
                    her @ cheeks blush "!!!" ("grin", "happyCl", "base", "mid")
                    call ctc

                    $ hermione.set_cum(face="heavy")

                    her "Daddy..." ("angry", "narrow", "base", "stare")
                    gen "That's it, princess! Take daddy's load!" ("angry", xpos="far_left", ypos="head")
                    her "*Aaah*!" ("grin", "narrow", "base", "dead")

                    call her_chibi_scene("bj_cum_out_done", trans=d5)
                    pause.8

                    gen "*Ah*... Finally..." ("base", xpos="far_left", ypos="head")
                    gen "Alright, I'm done..." ("base", xpos="far_left", ypos="head")
                    her "...................................." ("grin", "narrow", "base", "dead")
                    gen "I said it's over, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    her "Yes, I heard you, daddy... I mean, sir..." ("angry", "narrow", "base", "stare")
                    gen "So... Aren't you going to clean up?" ("base", xpos="far_left", ypos="head")
                    her "In a minute..." ("soft", "closed", "base", "dead")
                    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                    gen "Take your time, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

                    stop music fadeout 1.0
                    call blkfade

                    nar "A while later..."

                    $ hermione.set_cum(None)
                    $ hermione.wear("all")

                    call her_chibi("stand","desk","base", flip=False)
                    call gen_chibi("sit_behind_desk")

                    hide screen blkfade
                    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.

                    her "I take it you enjoyed my little performance, [name_genie_hermione]?" ("soft", "squint", "base", "mid", xpos="mid", ypos="base", trans=fade)
                    gen "Very much so, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    her "Great..." ("base", "closed", "base", "down")

        "\"Worship my cock.\"":
            $ states.her.status.gokkun = True

            her "You want me to... Worship it?" ("angry", "wink", "base", "mid")
            gen "Did I stutter?" ("base", xpos="far_left", ypos="head")
            her "Well... No, I just wasn't sure what you--" ("soft", "wink", "worried", "mid")
            her "Alright then... Just tell me what to do..." ("base", "narrow", "worried", "down")
            gen "You can start by putting my cock back in your mouth." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj", trans=d5)
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "That's it..." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "dead")
            gen "Now, I want you to tell me everything that is great about my cock... How much you love it." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "I... I love your cock... so much, [name_genie_hermione]..." ("soft", "narrow", "annoyed", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Slurp*! *Gobble*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "It's all I think about when I'm in class..." ("base", "narrow", "base", "up")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Gulp*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "*Mmm*... Very good, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

            if not states.her.status.public_blowjob:
                call her_chibi_scene("bj_pause", trans=d5)
                her "I love sucking your perfect dick..." ("base", "narrow", "base", "up")
                her "... and no one else's." ("base", "narrow", "base", "up")
                call her_chibi_scene("bj", trans=d5)
                her "*Lick*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
                call her_chibi_scene("bj_pause", trans=d5)
                her "The only thing I want... Is your perfect, {w}beautiful {w}{size=-4}cock{/size}!" ("grin", "narrow", "base", "dead")
                call her_chibi_scene("bj", trans=d5)
                her "*Gobble*! *Slurp*! *lick*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            else:
                call her_chibi_scene("bj_pause", trans=d5)
                her "Even when you make me suck another boy's dick..." ("base", "narrow", "base", "up")
                her "I still imagine that it's yours..." ("base", "narrow", "base", "up")
                call her_chibi_scene("bj", trans=d5)
                her "*Lick*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "dead")
                call her_chibi_scene("bj_pause", trans=d5)
                her "I imagine that it's your cum, sliding down my throat..." ("soft", "narrow", "annoyed", "up")
                call her_chibi_scene("bj", trans=d5)
                her "*Gobble*! *Slurp*! *Lick*!" ("open_wide_tongue", "narrow", "base", "dead")
                call her_chibi_scene("bj_pause", trans=d5)
                her "Or that it's your hot load, being shot across my face..." ("grin", "narrow", "base", "dead")
                call her_chibi_scene("bj", trans=d5)
                her "*Gobble*! *Slurp*! *Lick*!" ("open_wide_tongue", "narrow", "base", "up")

            gen "Is that so?" ("base", xpos="far_left", ypos="head")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Yes, [name_genie_hermione]..." ("soft", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Sometimes..." ("soft", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "dead")
            call her_chibi_scene("bj_pause", trans=d5)
            her "After you make me suck your tasty dick..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "I won't brush my teeth..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Just so I can go to sleep..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "With that perfect taste in my mouth..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "dead")
            call her_chibi_scene("bj_pause", trans=d5)
            her "And when I do brush my teeth..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "base", "up")
            call her_chibi_scene("bj_pause", trans=d5)
            her "I can only imagine your dick, going into my mouth..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "worried", "down")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Recently, I even started moaning whenever I'm brushing my teeth..." ("grin", "narrow", "base", "dead")
            call her_chibi_scene("bj", trans=d5)
            her "*Gobble*! *Lick*! *Gobble*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "That's it cock-slut... I'm almost there..." ("base", xpos="far_left", ypos="head")
            call her_chibi_scene("bj_pause", trans=d5)
            her "Where would you like to cum today, [name_genie_hermione]?" ("soft", "narrow", "annoyed", "up")
            her "I know it's greedy of me to ask..." ("angry", "narrow", "base", "down")
            her "But could you please cum in my mouth?" ("angry", "narrow", "base", "mid")
            her "{size=-4}Please...{/size} I promise I won't waste a drop of your precious seed." ("soft", "narrow", "worried", "mid")
            gen "I think that can be arranged..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid", emote="happy")
            call her_chibi_scene("bj", trans=d5)
            nar "Hermione devours your cock with renewed vigour."
            her "*Slurp*! *Gulp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Yes, like that... That's a good little slut..." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "A bit deeper now." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue", "narrow", "base", "up")
            gen "Go on, cum-whore." ("base", xpos="far_left", ypos="head")
            her "*Slurp*! *Gobble*! *Gobble*!" ("open_wide_tongue", "narrow", "worried", "down")
            gen "Alright, [name_hermione_genie], almost there!" ("base", xpos="far_left", ypos="head")
            gen "A bit deeper!" ("angry", xpos="far_left", ypos="head")
            her "!!! *Gobble-gobble-slurp-gobble*! !!!" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "Yes, just like that!" ("angry", xpos="far_left", ypos="head")
            her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}" ("open_wide_tongue", "narrow", "annoyed", "up")
            gen "{size=+5}Yes! Yes! Yes! Yes!{/size}" ("angry", xpos="far_left", ypos="head")
            gen "*Ngh*!!!" ("angry", xpos="far_left", ypos="head")
            gen "Here it comes, [name_hermione_genie]! Here's your reward!" ("angry", xpos="far_left", ypos="head")
            her "!!!" ("open_wide_tongue", "narrow", "worried", "down")

            call cum_block
            call her_chibi_scene("bj_cum_in", trans=d5)
            pause.8

            call cum_block
            gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
            gen "Take my cum, slut!" ("angry", xpos="far_left", ypos="head")
            her "*Gulp!-Gulp!-Gulp*!" ("open_wide_tongue_cum", "narrow", "annoyed", "up")
            with hpunch
            gen "Yes! Down your throat, you fucking cum dumpster!" ("angry", xpos="far_left", ypos="head")
            her "*Gulp-gulp-gulp-gulp-gulp*!" ("open_wide_tongue_cum", "narrow", "annoyed", "up")

            stop music fadeout 1.0
            call her_chibi_scene("bj", trans=d5)
            call ctc

            gen "*Ah*... I think that's all of it." ("base", xpos="far_left", ypos="head")
            gen "You can let it go now..." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("bj_pause", trans=d5)
            her @ tears mascara "..........................." ("full_cum", "narrow", "base", "dead", trans=fade)
            her @ tears mascara "................" ("full_cum", "narrow", "base", "dead")
            her @ tears mascara "........" ("full_cum", "narrow", "base", "dead")
            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ tears mascara "..."
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            gen "Are you going to swallow?" ("base", xpos="far_left", ypos="head")


            her @ tears mascara "*Shakes her head from side to side*" ("full_cum", "narrow", "base", "dead")

            if game.daytime:
                gen "So, you're going to leave my office, with a mouth full of cum?" ("base", xpos="far_left", ypos="head")
            else:
                gen "So, you're going to go to sleep, with a mouth full of cum?" ("base", xpos="far_left", ypos="head")

            her @ cheeks blush tears mascara "*Nods her head up and down enthusiastically*" ("full_cum", "narrow", "annoyed", "up") #Smile.

            gen "(She sure is taking this worshipping thing seriously...)" ("base", xpos="far_left", ypos="head")
            gen "Very well, [name_hermione_genie]... I'll allow you to keep my cum... Just this once..." ("base", xpos="far_left", ypos="head")
            $ _mouth_full_of_cum = True

    jump end_hg_pf_blowjob
