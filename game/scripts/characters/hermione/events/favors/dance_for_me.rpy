

### Hermione Dance ###

label start_hg_pf_strip:

    if not _events_completed_any:
        gen "{size=-4}(Ask her to dance for me?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 35
    return

label end_hg_pf_strip:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    call sna_chibi("hide")
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    $ hermione.set_cum(None)
    $ hermione.wear("all")

    hide screen blkfade
    if states.her.mood != 0:
        her "" ("annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=blackfade)
    else:
        her "" ("normal", "squint", "base", "mid", xpos="mid", ypos="base", trans=blackfade)

    # Points
    gen "{number=current_payout} points to the Gryffindor house." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]..." ("soft", "base", "base", "R")

    # Hermione leaves
    call her_walk("door", "base")
    call her_chibi("leave")

    # Increase level
    if states.her.tier == 3:
        if states.her.level < 12: # Points til 12
            $ states.her.level += 1

    if states.her.tier == 4:
        if states.her.level < 18: # Points til 18
            $ states.her.level += 1

    jump end_hermione_event

### Fail Events ###

label hg_pf_strip_fail:
    jump end_hermione_event

label hg_pf_strip_T1_E1: #Fails
    call start_hg_pf_strip

    $ states.her.ev.dance_for_me.strip_asked = True
    gen "[name_hermione_genie], I need you to dance for me a little." ("base", xpos="far_left", ypos="head")
    her "You want me to..." ("soft", "wide", "base", "stare")

    her "... Dance for you, [name_genie_hermione]?" ("open", "wide", "base", "stare")
    gen "Of course!" ("grin", xpos="far_left", ypos="head")
    her "Why would I--" ("clench", "base", "base", "stare")
    her "[name_genie_hermione]! That is going too far!" ("angry", "base", "angry", "mid")
    her "I think I better leave..." ("angry", "base", "base", "R")

    call her_walk(action="leave")

    $ states.her.mood += 5

    jump hg_pf_strip_fail

label hg_pf_strip_T2_E1: # Hermione starts dancing, but it will fail anyway.
    call start_hg_pf_strip

    if not _event_completed_failed:
        gen "[name_hermione_genie], I need you to dance for me a little." ("base", xpos="far_left", ypos="head")
        her "You want me to..." ("open", "base", "worried", "mid")
        her "... Dance for you, [name_genie_hermione]?" ("open", "wink", "base", "mid")
        gen "Yes... You think you could manage that?" ("base", xpos="far_left", ypos="head")
        her "*Ehm*... I suppose so..." ("soft", "base", "base", "R")
        her "Am I getting paid for this?"
        gen "Of course, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
        her "So... Just a little dancing then..." ("annoyed", "base", "worried", "R")
        gen "Whenever you're ready..." ("base", xpos="far_left", ypos="head")
        her "................."
        hide hermione_main
        with d3

        nar "Hermione starts dancing..."

        stop music fadeout 1.0
        call her_chibi("dance","mid","base")
        with d3
        pause.2

        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "{size=-5}(...........................................){/size}" ("disgust", "narrow", "base", "down", ypos="head", flip=False)
        her @ cheeks blush "{size=-5}(This is silly...){/size}" ("annoyed", "narrow", "angry", "R")
        nar "Hermione looks embarrassed, but she keeps on \"dancing\"..."
        gen "..................." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "{size=-5}(...........................................){/size}" ("annoyed", "narrow", "angry", "R")
        gen "Alright, you can start undressing now." ("base", xpos="far_left", ypos="head")

        call her_chibi("stand","mid","base") #Hermione stands still.
        with hpunch

        her @ cheeks blush "??!" ("mad", "wide", "base", "stare")
        gen "Take off your clothes..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You want me to...?" ("disgust", "narrow", "base", "down")

        her @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "angry", "mid")
        her @ cheeks blush "This is ridiculous on a whole other level!" ("angry", "closed", "angry", "mid")
        her @ cheeks blush "I won't let myself be forced to become some cheap stripper!!!" ("mad", "wide", "base", "stare")
        gen "Nobody is forcing you to do this." ("base", xpos="far_left", ypos="head")
        gen "If you don't need the points, please feel free to leave." ("base", xpos="far_left", ypos="head")
        her "Yes. I believe you're right, Sir." ("soft", "closed", "angry", "mid")
        her "Stripping for you won't be worth {b}any{/b} amount of points!" ("angry", "base", "angry", "mid")
        her "I will be leaving now!" ("annoyed", "base", "angry", "mid")
    else:
        gen "[name_hermione_genie], I need you to dance for me a little." ("base", xpos="far_left", ypos="head")
        her "And would you like me to take off my clothes as well?" ("soft", "closed", "base", "mid")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her "No! I will not!" ("scream", "base", "angry", "mid")
        her "And I'd appreciate it if you'd stop making such outrageous requests..." ("annoyed", "base", "angry", "mid")
        gen "You will get points for it..." ("base", xpos="far_left", ypos="head")
        her "Shove those points up your--" ("angry", "closed", "angry", "mid")
        her "I will be leaving now..." ("annoyed", "base", "angry", "mid")
        her "Good day, Sir..." ("annoyed", "narrow", "angry", "R")

    call her_walk(action="leave")

    $ states.her.mood += 5

    jump hg_pf_strip_fail

### Tier 3 ###

# Event 1 (i) - Hermione tries to strip for you but fails.
# Event 2 (i) - Hermione strips for you on your desk. Snape then enters.
# Event 3 (r) - Hermione strips for. You will get some event choices.

label hg_pf_strip_T3_intro_E1:

    call start_hg_pf_strip

    gen "[name_hermione_genie], I need you to dance for me a little." ("base", xpos="far_left", ypos="head")
    her "You want me to..." ("open", "base", "worried", "mid")
    her "... dance for you, [name_genie_hermione]?" ("open", "wink", "base", "mid")
    gen "Yes... You think you could manage that?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... I suppose so..." ("soft", "base", "base", "R")
    her "Am I getting paid for this?"
    gen "Of course, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her "So... Just a little dancing then..." ("annoyed", "base", "worried", "R")
    gen "Whenever you're ready..." ("base", xpos="far_left", ypos="head")
    her "................."
    hide hermione_main
    with d3

    nar "Hermione starts dancing..."

    stop music fadeout 1.0
    call her_chibi("dance","mid","base")
    with d3
    pause.2

    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-5}(...........................................){/size}" ("disgust", "narrow", "base", "down", ypos="head", flip=False)
    her @ cheeks blush "{size=-5}(This is silly...){/size}" ("annoyed", "narrow", "angry", "R")
    nar "Hermione looks embarrassed, but she keeps on \"dancing\"..."
    gen "..................." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-5}(...........................................){/size}" ("annoyed", "narrow", "angry", "R")
    gen "Alright, you can start undressing now." ("base", xpos="far_left", ypos="head")

    if not states.her.ev.dance_for_me.strip_asked:
        call her_chibi("stand","mid","base") #Hermione stands still.
        with hpunch

        her @ cheeks blush "??!" ("mad", "wide", "base", "stare")
        her "I thought all I had to do was dance?" ("angry", "base", "angry", "mid")
        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
        gen "Really? That's adorable." ("base", xpos="far_left", ypos="head")
    else:
        her "..." ("disgust", "base", "angry", "mid")
        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
        gen "Go on... You knew this was coming..." ("base", xpos="far_left", ypos="head")

    if hermione.is_any_worn("top", "bottom", "robe", "accessory"):
        gen "Now start taking off those clothes." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You want me to... Strip dance for you...?" ("disgust", "narrow", "base", "down")
    else:
        gen "Now take off your underwear." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "You want me to... Take off my underwear...?" ("disgust", "narrow", "base", "down")

    gen "Yes. And I expect you to do it today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=+4}[name_genie_hermione]!{/size}" ("angry", "happyCl", "worried", "mid")
    gen "Don't you raise your voice at me, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush ".....!!?" ("mad", "wide", "base", "stare")
    gen "Nobody is forcing you to do this." ("base", xpos="far_left", ypos="head")
    gen "I am doing you a favour!" ("base", xpos="far_left", ypos="head")
    gen "If you don't need the points, please feel free to leave." ("base", xpos="far_left", ypos="head")
    her "....................." ("angry", "base", "angry", "mid")
    her @ cheeks blush "......................................." ("disgust", "narrow", "base", "down")

    nar "Hermione starts dancing again..."

    call her_chibi("dance","mid","base") #Chibi takes off the vest here btw but Hermione does not even if she's wearing it
    with d5

    her @ cheeks blush "{size=-5}(...........................................){/size}" ("angry", "happyCl", "worried", "mid")
    gen "What are you waiting for then?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "............................................................." ("disgust", "narrow", "base", "down")

    nar "Hermione gives you a confused look..."

    pause .5
    her @ cheeks blush "{size=-5}(Am I really going to do this?){/size}" ("angry", "happyCl", "worried", "mid", xpos="base", ypos="base", trans=fade)

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "down")


    menu: #Hermione always wears underwear at this level
        gen "......................." ("base", xpos="far_left", ypos="head")
        "\"Now, get rid of your bottoms!\"" if hermione.is_worn("bottom", "panties"):
            her @ cheeks blush "................................." ("angry", "happyCl", "worried", "mid")
            nar "Hermione starts taking off her bottoms..."
            nar "She seems very hesitant and takes her time..."
            nar "Finally she takes a deep breath and takes them off..."

            her @ cheeks blush "{size=-5}(Here it comes then...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(For the honour of Gryffindor....){/size}" ("angry", "happyCl", "worried", "mid")
            pause .2

            $ hermione.strip("bottom")
            play sound "sounds/cloth_sound3.ogg"
            call ctc
            pause .5

            gen "..............." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "{size=-5}(.........................................){/size}" ("angry", "happyCl", "worried", "mid")
            nar "Hermione keeps on dancing..."
            if hermione.is_worn("top"):
                gen "Alright, your top is next!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "My top....?" ("disgust", "narrow", "worried", "down")
            else:
                gen "Alright, your bra is next!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "My bra....?" ("disgust", "narrow", "worried", "down")
            hide hermione_main
            with d3

            nar "Hermione looks extremely embarrassed..."
            nar "She clumsily shakes her body to and fro..."

        "\"Now, take off your top!\"" if hermione.is_worn("top", "bra"):
            $ states.her.status.show_bra = True
            her @ cheeks blush "................................." ("angry", "happyCl", "worried", "mid")
            nar "Hermione starts taking off her top..."
            nar "She seems very hesitant and takes her time..."
            nar "Finally she takes a deep breath and removes her top..."

            her @ cheeks blush "{size=-5}(Alright, here it comes...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(For the honour of Gryffindor!){/size}" ("angry", "base", "worried", "mid")
            pause .2

            $ hermione.strip("top")
            play sound "sounds/cloth_sound3.ogg"
            call ctc

            if hermione.is_worn("bra"):
                gen "And your bra..." ("base", xpos="far_left", ypos="head")
                her "..." ("angry", "base", "angry", "mid")
                $ hermione.strip("bra")
                play sound "sounds/cloth_sound3.ogg"
                call ctc
                her @ cheeks blush "{size=-5}(I...{w=0.4} I did it...){/size}" ("angry", "happyCl", "worried", "mid")
            else:
                her @ cheeks blush "{size=-5}(I actually did it...){/size}" ("angry", "happyCl", "worried", "mid")

            her @ cheeks blush "{size=-5}(He can see my breasts while I'm dancing for him...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(This is so demeaning...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(But I am doing this for my house...){/size}" ("angry", "happyCl", "worried", "mid")

            gen "Not bad..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "{size=-5}(.........................................){/size}" ("angry", "happyCl", "worried", "mid")

            nar "Hermione is topless now..."
            nar "She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
            nar "It seems like she's desperately trying to prevent her breasts from bouncing or swaying..."

            if hermione.is_worn("bottom"):
                gen "Alright, your bottoms are next!" ("base", xpos="far_left", ypos="head")
            else:
                gen "Alright, your panties are next!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...................." ("angry", "happyCl", "worried", "mid")
            hide hermione_main
            with d3

            nar "Hermione looks extremely embarrassed..."
            nar "Her fingers shaking as she fumbles somewhat..."
        "\"Get rid of your bra!\"" if not hermione.is_worn("top"):
            $ states.her.status.show_tits = True
            her @ cheeks blush "{size=-5}(Okay then...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(For the honour of Gryffindor!){/size}" ("angry", "base", "worried", "mid")

            $ hermione.strip("bra")
            play sound "sounds/cloth_sound3.ogg"
            call ctc

            her @ cheeks blush "{size=-5}(I...{w=0.4} I did it...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(He can see my breasts while I'm dancing for him...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(This is so demeaning...){/size}" ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush "{size=-5}(But I am doing this for my house...){/size}" ("angry", "happyCl", "worried", "mid")

            gen "Not bad..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "{size=-5}(.........................................){/size}" ("angry", "happyCl", "worried", "mid")

            nar "Hermione is topless now..."
            nar "She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
            nar "It seems like she's desperately trying to prevent her breasts from bouncing or swaying..."

            if hermione.is_worn("bottom"):
                gen "Alright, your bottoms are next!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "...................." ("angry", "happyCl", "worried", "mid")

                $ hermione.strip("bottom")
                play sound "sounds/cloth_sound3.ogg"
                call ctc
                pause .5

                gen "Nice..." ("base", xpos="far_left", ypos="head")
                gen "Now then, your panties!" ("base", xpos="far_left", ypos="head")
            else:
                gen "Alright, your panties are next!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...................." ("angry", "happyCl", "worried", "mid")
            hide hermione_main
            with d3

            nar "Hermione looks extremely embarrassed..."
            nar "Her fingers tremble as she fumbles somewhat..."
        "\"Take off your panties!\"" if not hermione.is_worn("bottom"):
            hide hermione_main
            with d3

            nar "Hermione looks at you pleadingly..."
            nar "Her fingers tremble slightly as she begins moving them towards her panties..."

            gen "That's it..." ("base", xpos="far_left", ypos="head")

            nar "Glancing up at you, she hesitates for a moment..."
            nar "And you watch as she moves her hands away from her panties..."

    stop music fadeout 1.0
    gen "What's the problem, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed

    her @ cheeks blush "I'm sorry, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "I...{w=0.4} I'm trying..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "But my hands..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "Why is this so hard! *Sob*" ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush tears messy "No, I can't do this, [name_genie_hermione]! *sob*" ("open", "wide", "worried", "stare")
    gen "What?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I thought I could, but..." ("angry", "squint", "base", "mid", trans=fade)
    her @ cheeks blush "Strip dancing for points, [name_genie_hermione]?" ("angry", "squint", "base", "mid")
    her @ cheeks blush "People look up to me in this school!" ("angry", "squint", "base", "mid")
    her @ cheeks blush "I have a reputation... *Sob*" ("angry", "squint", "base", "mid")
    her @ cheeks blush tears messy "And If I do this..." ("scream", "base", "angry", "mid")
    show screen blkfade
    with d5

    nar "Hermione quickly puts her clothes back on..."

    play sound "sounds/cloth_sound3.ogg"
    $ hermione.wear("all")
    call her_chibi("stand","desk","base")

    hide screen blkfade
    her @ cheeks blush tears messy "[name_genie_hermione], I think I'd better go now... *Sob!*" ("angry", "squint", "base", "mid", trans=fade)

    menu:
        "\"Alright. I had fun. Here are your points.\"":
            her @ tears soft "Really? I didn't ruin it completely then?" ("soft", "base", "base", "R")

            jump end_hg_pf_strip

        "\"Sure. You will receive no points, though.\"":
            her @ tears mascara_crying "[name_genie_hermione]... I may not be very good at this..." ("open", "base", "base", "mid")
            her @ tears mascara_crying "But I did my best... I think I deserve some--"
            gen "Just make sure you try harder next time, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her @ tears mascara_crying "Next time?!" ("open", "base", "base", "mid")
            her @ cheeks blush tears mascara "I assure you, [name_genie_hermione], there will be no next time..." ("angry", "base", "angry", "mid")
            gen "We'll see..." ("base", xpos="far_left", ypos="head")
            her @ tears mascara "*Tsk*!" ("disgust", "narrow", "base", "mid_soft")

            call her_walk(action="leave")

            # Event does not fail. She just gets mad, but no whoring increase.
            $ states.her.mood += 25

            jump end_hermione_event

label hg_pf_strip_T3_intro_E2:
    $ states.her.status.show_tits = True
    $ states.her.status.show_pussy = True

    call start_hg_pf_strip

    gen "[name_hermione_genie], I need you to dance for me." ("base", xpos="far_left", ypos="head")
    her "Again, [name_genie_hermione]...?" ("disgust", "narrow", "base", "mid_soft")
    gen "You will get paid accordingly, of course..." ("base", xpos="far_left", ypos="head")
    her "............................" ("annoyed", "narrow", "angry", "R")
    her "And you expect me to--{w=0.2} *Ehm*..." ("annoyed", "narrow", "angry", "R")
    gen "Take your clothes off. Naturally." ("base", xpos="far_left", ypos="head")
    stop music fadeout 1.0

    her "......................" ("annoyed", "narrow", "angry", "R")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "Well, why not?" ("disgust", "narrow", "base", "mid_soft")
    her "Yes, I don't see why not!" ("scream", "base", "angry", "mid", emote="angry")
    gen "*Hmm*...? {size=-4}(Look at her, so eager all of a sudden...){/size}" ("base", xpos="far_left", ypos="head")
    her "After all, as a pupil I am meant to obey your every order, isn't that right, [name_genie_hermione]?!" ("scream", "closed", "angry", "mid")
    gen "...................." ("base", xpos="far_left", ypos="head")
    her "If the Headmaster tells me to strip for him, Then I shall strip!!!" ("scream", "closed", "angry", "mid")
    her "Do I find this extremely inappropriate, disgraceful, and humiliating?" ("angry", "base", "angry", "mid")
    her "Of course not. What nonsense!" ("scream", "closed", "angry", "mid")
    gen ".............." ("base", xpos="far_left", ypos="head")
    her "Ha! Might as well do this the proper way!" ("angry", "base", "angry", "mid")

    call hide_characters
    with d3
    pause.2

    gen "??!" ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    play sound "sounds/08_hop_on_desk.ogg" #Sound of the desk squeaking.
    pause 3
    gen "!!!!!!" ("angry", xpos="far_left", ypos="head")
    nar "To your surprise, Hermione just hops onto your desk and starts dancing frantically..."

    call her_chibi("dance","on_desk","on_desk")

    hide screen blkfade
    with fade
    pause.5

    her "If I must degrade myself in order to protect the honour of my house..." ("scream", "closed", "angry", "mid", xpos="mid", ypos="base")

    her "So be it!" ("scream", "base", "angry", "mid", emote="angry")
    her "Just..." ("open", "narrow", "worried", "down")
    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")

    her "*Groan*" ("clench", "narrow", "base", "down")

    $ _wearing_top = False
    if hermione.is_worn("top"):
        $ _wearing_top = True
        nar "Hermione begins taking off her top..."
        nar "Pulling at the fabric in anger, making it more difficult than it should be..."
        her "Why won't it....?!"
        her "There!" ("annoyed", "narrow", "annoyed", "mid")
        nar "Hermione finally manages to untangle herself and sends her top flying to the other side of the room..."

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top")
        call ctc
        pause .5

    else:
        nar "The girl seems to contemplate about which piece of clothing she should take off first..."
        pause.1

    if hermione.is_worn("bottom"):
        her "Let's take these bottoms off then, shall we?" ("scream", "closed", "angry", "mid")

        menu:
            gen "..." ("base", xpos="far_left", ypos="head")
            "\"Yes, that's right. Take it off!\"":
                her "Of course!"
                her "Here it goes!" ("open", "narrow", "worried", "down")
            "\"You need to calm down, [name_hermione_genie].\"":
                her "Well, {size=+7}EXCUSE ME{/size}, [name_genie_hermione]!"
                her "You told me to strip for you, but you never told me your preferences regarding the pace!"
                gen "Well, I'm telling you now, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
                her "Too late!" ("angry", "base", "angry", "mid")

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bottom")
        call ctc
        pause .5

        nar "Hermione sends her bottoms flying across the room, just like she did with her top a moment earlier..."
    else:
        her "Alright then, let's do this thing!" ("scream", "closed", "angry", "mid")

    gen "{size=-4}(Wow, she is getting really worked up over this...){/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=-4}(Maybe it was still too early to--){/size}" ("base", xpos="far_left", ypos="head")
    her "Clothes?!!" ("disgust", "narrow", "base", "mid_soft")
    her "{size=+9}I don't need them!{/size}" ("scream", "base", "angry", "mid", emote="angry")
    if hermione.is_worn("bra"): #Should be on at this level, but might as well have the check
        nar "Hermione keeps dancing angrily, and then..."
        her "" ("angry", "base", "angry", "mid")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bra")
        pause.2
        gen "{size=-4}(When did she??!){/size}" ("angry", xpos="far_left", ypos="head")
    call ctc

    her "Are you enjoying this, [name_genie_hermione]?"
    her "" ("angry", "base", "angry", "mid")

    her "Shall I shake my breasts for you, like one of those harlots?" ("scream", "closed", "angry", "mid")
    gen "Well--" ("base", xpos="far_left", ypos="head")
    her "Of course I shall! Why wouldn't I degrade myself for your pleasure?!"
    her "This is completely {size=+7}acceptable!{/size}" ("scream", "base", "angry", "mid", emote="angry")
    her "" ("angry", "base", "angry", "mid")

    pause.2
    nar "Hermione is starting to shake her naked breasts rather clumsily..."
    nar "As you watch the girl's tits sway right and left, you find yourself fighting the urge to..."

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Grab them!-":
            gen "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}" ("grin", xpos="far_left", ypos="head")
            gen "{size=-4}(Maybe pull on them a little, yes...){/size}" ("grin", xpos="far_left", ypos="head")
            play sound "sounds/boing02.ogg"
            her "" ("disgust", "wide", "base", "stare")
            pause.8
            play sound "sounds/boing03.ogg"
            her "" ("shock", "wide", "worried", "shocked")
            pause.8

        "-Slap them!-":
            gen "{size=-4}(I want to slap the crap out of her fun bags.){/size}" ("base", xpos="far_left", ypos="head")
            call slap_her #Calls slapping sound and visual.
            her "" ("disgust", "wide", "base", "stare")
            pause.2
            gen "{size=-4}(Yes, just slap them around a little...){/size}" ("grin", xpos="far_left", ypos="head")
            call slap_her #Calls slapping sound and visual.
            her "" ("shock", "wide", "worried", "shocked")
            pause.2

        "-Bite on them!-":
            gen "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}" ("base", xpos="far_left", ypos="head")
            gen "{size=-4}(No, it's not weird!){/size}" ("base", xpos="far_left", ypos="head")
            gen "{size=-4}(Just a couple of gentle love-bites!){/size}" ("base", xpos="far_left", ypos="head")
            call kiss_her
            her @ tears soft "" ("shock", "wide", "base", "stare")
            pause.2
            gen "{size=-4}(Yes... Maybe more than just a couple...){/size}" ("grin", xpos="far_left", ypos="head")
            her @ tears soft_blink "" ("disgust", "happyCl", "worried", "mid")
            pause.2
            call kiss_her
            call kiss_her
            pause.2

        "-Motorboat them!-":
            gen "{size=-4}(I'm going to put my face right in between them!){/size}" ("base", xpos="far_left", ypos="head")
            call kiss_her
            her "" ("shock", "happyCl", "worried", "mid")
            pause.2
            gen "{size=-4}(Yes, motor boating these titties is the best!){/size}" ("grin", xpos="far_left", ypos="head")
            her "" ("shock", "wide", "worried", "shocked")
            pause.2

    nar "While you are having fun with her tits, Hermione keeps on dancing..."

    her "(Dancing naked in front of the headmaster...)" ("soft", "wide", "worried", "shocked")
    her "(Letting him touch my breasts...)" ("disgust", "wide", "worried", "shocked")
    her "(If my parents knew about this, they would lose their minds...)" ("soft", "wide", "worried", "shocked")
    her "(Especially my father...)" ("annoyed", "closed", "base", "mid")
    nar "Hermione is starting to shake her tits again..."
    her "(Hermione Granger - the stripper...)"
    her "(Forgive me father...)" ("annoyed", "narrow", "base", "dead")

    nar "Hermione puts her hands on her tits and starts squeezing them..."
    nar "You can only assume that she means to look seductive, but she just looks awkward and ashamed."
    her "(I used to be a top student...{w=0.4} Used to have standards...)"
    nar "Hermione clutches her tits even harder and then gives them a couple of twists..."
    nar "Almost looking as if she is mad at her own breasts and trying her best to punish them..."

    nar "You find the thought strangely arousing..."

    #TODO Hermione chibi: Stand in panties only (blinking?)
    call her_chibi("dance_pause","on_desk","on_desk")
    call ctc

    her "Well, I hope you enjoyed yourself, [name_genie_hermione]!" ("open", "narrow", "annoyed", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    her "I would like to get paid now..." ("open", "closed", "angry", "mid")
    if hermione.is_worn("panties"): #Should be on at this level but might as well have the check
        gen "Aren't you forgetting something, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]...?" ("open", "narrow", "annoyed", "mid")
        gen "Your panties...?" ("base", xpos="far_left", ypos="head")
        her "My panties?" ("open", "wide", "base", "stare")
        her "But, they always leave them on!"
        gen "Who exactly are \"they\"?" ("base", xpos="far_left", ypos="head")
        gen "Strippers in kid's cartoons?" ("base", xpos="far_left", ypos="head")
        gen "Stripping is stripping, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
        gen "Now take off your panties!" ("base", xpos="far_left", ypos="head")
        her "................" ("angry", "wide", "base", "stare")

        nar "Hermione looks at you horror-struck. All of her anger now gone..."
        her "................." ("annoyed", "closed", "base", "mid")
        nar "Without saying another word..."
        nar "She starts pulling down her panties..."

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("panties")

        gen "There it is!" ("grin", xpos="far_left", ypos="head")
        her "There, can I get paid now?" ("open", "closed", "angry", "mid")

    gen "*Hmm*... Well, I'm not sure whether we're quite done here yet..." ("base", xpos="far_left", ypos="head")
    her "..." ("upset", "squint", "annoyed", "mid")
    $ hermione.strip("clothes")

    #TODO Hermione chibi: Stand naked blinking (ch_hem blink_n)
    call her_chibi("dance_pause","on_desk","on_desk")
    her @ cheeks blush "" ("annoyed", "happyCl", "worried", "mid")
    pause.2

    gen "How about you--" ("grin", xpos="far_left", ypos="head")

    hide hermione_main
    with d1

    stop music

    call sna_walk(action="enter", xpos="mid", ypos="base")

    sna "Listen, Genie. I've been think--" ("snape_01", xpos="base", ypos="base")

    play sound "sounds/scratch.ogg"
    with hpunch

    sna "............................................" ("snape_11")

    call her_chibi("dance_pause","on_desk","on_desk", flip=True)
    pause 0.4

    her "(Professor Snape???????!)" ("angry", "wide", "base", "stare", flip=True)
    sna "Miss Granger?" ("snape_12")

    call set_her_action("covering")
    her @ cheeks blush "(No, no... This is not happening. Please...)" ("shock", "happyCl", "worried", "mid", trans=d5)
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "...................................." ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Severus, I am busy right now.\"":
            sna "Yes... I can see that..." ("snape_13")
            her "{size=-7}(I want to die!){/size}" ("angry", "happyCl", "worried", "mid")

        "\"Severus! Please, come join us.\"":
            $ states.her.mood += 20
            sna "Seriously?" ("snape_14")
            her "([name_genie_hermione], no, please.............................)" ("angry", "happyCl", "worried", "mid")
            sna "A very tempting offer indeed..." ("snape_13")
            her "!!!!!!......." ("angry", "wide", "base", "stare")
            sna "Well, maybe some other time..." ("snape_13")
            her "{size=-5}(There will be no other time!){/size}" ("angry", "happyCl", "worried", "mid")
            her "{size=-5}(I will stop selling favours from now on, I swear!){/size}"

    sna "I shall postpone our conversation then, Geni-- *ahem*! Albus." ("snape_12")
    sna "Miss Granger..." ("snape_13")
    her "................................." ("angry", "happyCl", "worried", "mid")

    call hide_characters
    with fade
    pause.2

    call sna_walk(action="leave")

    show screen blkfade
    with d5

    play sound "sounds/08_hop_on_desk.ogg"
    nar "Hermione hastily hops off your desk."
    play sound "sounds/cloth_sound3.ogg"
    $ hermione.wear("all")
    $ hermione.strip("top")
    nar "She starts putting some clothes back on rather frantically..."



    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d5

    if _wearing_top: # Wears Top
        her "My top! Where's my top?!" ("scream", "happyCl", "worried", "mid", xpos="mid", ypos="base", flip=False)
        gen "It's over there, by the fireplace..." ("base", xpos="far_left", ypos="head")

        hide hermione_main
        with d3
        pause.2

        call her_walk("mid", "base")

        her "................................" ("disgust", "narrow", "base", "down", flip=True)
        pause.2

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.wear("all")
        pause .8

        call her_chibi("stand","mid","base", flip=True)
        pause.2

        call her_walk("desk", "base")

    her "........................" ("normal", "happyCl", "worried", "mid", xpos="mid", ypos="base", flip=False)
    stop music fadeout 2.0
    her "Can I just get my points now, please?" ("angry", "happyCl", "worried", "mid", emote="sweat")
    pause.5

    if not states.her.status.stripping:
        $ achievements.unlock("herstrip")
        $ states.her.status.stripping = True

    jump end_hg_pf_strip

label hg_pf_strip_T3_E2:

    call start_hg_pf_strip

    gen "[name_hermione_genie], how about another strip?" ("base", xpos="far_left", ypos="head")
    her ".............." ("disgust", "narrow", "base", "mid_soft", xpos="base", ypos="base")
    her "I would really rather not, [name_genie_hermione]..."
    gen "Why? You're getting quite good at it." ("base", xpos="far_left", ypos="head")
    her "........................." ("annoyed", "narrow", "annoyed", "mid")
    her "{number=current_payout} house points..." ("open", "narrow", "worried", "down")
    gen "Sure! The usual rate." ("base", xpos="far_left", ypos="head")
    her "..................." ("annoyed", "narrow", "angry", "R")

    if states.sna.ev.hangouts.hermione_strip_invite: #Turns TRUE after Dance Event 2 and the next Date with Snape.
        gen "(*Hmm*... Should I invite Snape to watch as well?)" ("base", xpos="far_left", ypos="head")

        menu:
            "-Yes! Hermione needs an audience!-":
                jump hg_pf_strip_T3_snape

            "-Nah. That's not a good idea...-":
                pass

    # Locks Door.
    call hide_characters
    with d3
    pause.5

    call her_walk("door", "base")

    pause.2
    call chibi_emote("thought", "hermione")
    pause.5
    play sound "sounds/09_lock.ogg"
    call chibi_emote("hide", "hermione")
    pause.2

    gen "??!" ("base", xpos="far_left", ypos="head")
    pause.2


    # Walks back.
    call her_chibi("stand","door","base")
    pause.1

    call her_walk("mid", "base")
    pause.2

    her "Just in case..." ("annoyed", "narrow", "angry", "R", flip=False)
    stop music fadeout 1.0

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2
    call her_chibi("dance","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    her "Just for the record..." ("open", "closed", "base", "mid", xpos="mid", ypos="base")
    her "I still consider this a highly inappropriate favour to be buying from one of your students, [name_genie_hermione]." ("annoyed", "squint", "base", "mid")
    gen "Right. And an equally inappropriate favour to be selling to your headmaster. Wouldn't you agree?" ("base", xpos="far_left", ypos="head")
    her ".........." ("annoyed", "narrow", "angry", "R")
    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")

    if hermione.is_worn("top"):
        nar "Hermione shifts her body towards you and starts taking off her top..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top")
        pause .5
    if hermione.is_worn("bra"):
        nar "After struggling for a moment, Hermione then takes off her bra, somewhat clumsily..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bra")

    pause .2
    call ctc

    gen "Yes! The tits!" ("grin", xpos="far_left", ypos="head")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her ".............." ("open", "narrow", "worried", "down")
    her "What if my parents were to find out about this, [name_genie_hermione]?" ("disgust", "narrow", "base", "down")
    her "Mother would never understand..."
    her "As for my father..." ("upset", "wink", "base", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-3}\"Your father would be proud of you!\"{/size}":
            her "I doubt it..."
            her "Yes, I am doing this for the right reasons, but..."
            her "He would never see it that way..." ("annoyed", "base", "angry", "mid")
            her "He must never know about this..."

        "{size=-3}\"Your father would spank you hard!\"{/size}":
            her "He would not!" ("shock", "wide", "base", "stare")
            her "And I am too old for that anyway..." ("upset", "wink", "base", "mid")
            gen "I would say that you are the perfect age for that..." ("grin", xpos="far_left", ypos="head")
            her "*Huh*?"
            gen "If you know what I mean..." ("grin", xpos="far_left", ypos="head")
            her "I do not know what you mean, [name_genie_hermione]." ("grin", "happyCl", "worried", "mid", emote="sweat")

        "{size=-3}\"Your father would disown you!\"{/size}":
            her "You are probably right, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            her "(Oh father, I am so sorry...)" ("angry", "base", "base", "mid")
            her "he must never find out..." ("angry", "base", "base", "mid")

        "{size=-3}\"Your father would love to watch you strip!\"{/size}":
            her "He would not! He would be ashamed of me!" ("normal", "happyCl", "worried", "mid")
            gen "Are you sure about that?" ("base", xpos="far_left", ypos="head")
            her "Absolutely! My father is a man of integrity!" ("scream", "happyCl", "worried", "mid")
            gen "But he {size=+4}is{/size} a {size=+4}man{/size}, right?" ("base", xpos="far_left", ypos="head")
            her "....................." ("annoyed", "narrow", "annoyed", "mid")
            her "My father must never know about this..." ("annoyed", "base", "worried", "R")


    nar "Hermione is starting to sway her hips rather seductively..."

    if hermione.is_any_worn("bottom", "stockings"):
        nar "Whilst sliding her bottoms down..."
        if hermione.is_worn("stockings"):
            nar "Along with her stockings..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bottom", "stockings")
    pause.3
    call ctc

    menu:
        "-Take your cock out, start jerking off-":
            jump hg_pf_strip_T3_masturbate

        "-Show some manners, just watch-":
            jump hg_pf_strip_T3_watch

label hg_pf_strip_T3_watch:
    nar "You watch Hermione Dance..."
    her "(Time for the finishing act I suppose...)" ("angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")

    if hermione.is_worn("panties"):
        gen "Yes, [name_hermione_genie]! Take them off!" ("base", xpos="far_left", ypos="head")
        her "........" ("annoyed", "closed", "base", "mid")
        nar "Doing her best to please you, Hermione attempts to undress herself whilst still keeping her dance going."
        nar "Bending over slightly, she hurriedly slides her panties down..."
        play sound "sounds/cloth_sound3.ogg"
    else:
        nar "Hermione moves her body in an attempted seductive manner."
        nar "Your gaze on her current state of undress causes her some difficulty in maintaining her concentration."

    $ hermione.strip("clothes")
    pause 1.0


    nar "You can see that she is doing her best to not fall off the desk..."
    nar "But she looks rather ridiculous in her attempts to act like a professional stripper..."

    call ctc

    her ".........." ("disgust", "happyCl", "worried", "mid")
    nar "Hermione performs another set of rather awkward movements..."
    nar "if not for her naked tits bouncing all over the place, this would be quite embarrassing..."

    gen "................." ("grin", xpos="far_left", ypos="head")
    nar "A few more clumsy movements before Hermione slumps on her butt..."

    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    call hide_characters
    hide screen blkfade
    with d5
    call ctc

    her "I'm sorry, Sir. Was this good enough?..." ("disgust", "narrow", "base", "down", emote="sweat", ypos="head", flip=False)

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-3}\"Good job, [name_hermione_genie]! You certainly know how to dance!\"{/size}":
            her ".............." ("disgust", "narrow", "worried", "down")
            gen "You have a lot of talent for this!" ("base", xpos="far_left", ypos="head")
            her "Thank you [name_genie_hermione]." ("soft", "base", "worried", "R", emote="sweat")
        "{size=-3}\"*Hmm*... This was quite awful...\"{/size}":

            $ states.her.mood += 4
            call her_chibi("sit_naked_shocked","on_desk","on_desk")

            her "............" ("annoyed", "base", "angry", "mid")
            gen "You just need to practise more..." ("base", xpos="far_left", ypos="head")
            her "Whatever........." ("annoyed", "narrow", "angry", "R")
        "{size=-3}\".................................................\"{/size}":
            her "......................." ("silly", "happyCl", "worried", "mid", emote="sweat")
            call her_chibi("sit_naked_shocked","on_desk","on_desk")

    call ctc

    jump end_hg_pf_strip

label hg_pf_strip_T3_masturbate:
    show screen blkfade
    with d5

    her "[name_genie_hermione]?!" ("open", "wide", "base", "stare", flip=False)
    gen "It's alright, [name_hermione_genie]. Don't mind me..."

    call gen_chibi("jerk_off","behind_desk","base")
    call her_chibi("dance","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    her "B-but..." ("angry", "wide", "base", "stare", flip=False)
    her "Your..."
    gen "Yes...{w=0.3} *Ah*... Yes... This is good." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]!!!" ("scream", "happyCl", "worried", "mid")
    her "I must insist that you put away your..." ("angry", "happyCl", "worried", "mid")
    her "... thing."

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"I said, keep on dancing, [name_hermione_genie]!\"":
            stop music fadeout 1.0

            her "No, [name_genie_hermione]!" ("annoyed", "narrow", "angry", "R", flip=False)
            if states.her.status.cumshot:
                her "You've done this to me before, without telling me beforehand..." ("angry", "happyCl", "worried", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            show screen blkfade
            with d5

            nar "Hermione jumps off your desk and starts to dress herself, while glaring at you..."
            gen "Oh, come on! Don't leave me like that!" ("base", xpos="far_left", ypos="head")
            nar "You reluctantly put your cock away..."

            play sound "sounds/cloth_sound.ogg"
            $ hermione.wear("all")
            call her_chibi_scene("reset","desk","base", trans=fade)

            her "The dance is over, [name_genie_hermione]!" ("soft", "base", "angry", "mid")
            her "I would like to get paid now!" ("annoyed", "narrow", "annoyed", "mid")
            gen "Why do you always have to be so stubborn [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "My payment..." ("annoyed", "narrow", "annoyed", "mid")

            $ states.her.mood += 6

            jump end_hg_pf_strip

        "\"Fine. There is no need for drama!\"":
            her "......................" ("annoyed", "narrow", "angry", "R", flip=False)
            pause.1

            call gen_chibi("sit_behind_desk")
            call her_chibi("dance","on_desk","on_desk")
            with fade
            pause.5

            jump hg_pf_strip_T3_watch

### Tier 4 ###


# Event 1 (i) - Hermione tries her best at stripping.
# Event 2 (i) -
# Event 3 (r) -

label hg_pf_strip_T4_intro_E1:

    call start_hg_pf_strip

    gen "[name_hermione_genie], why don't you get on this desk for another show?" ("base", xpos="far_left", ypos="head")
    her ".............." ("annoyed", "squint", "base", "mid_soft", xpos="base", ypos="base")
    her "I would really rather not, [name_genie_hermione]..."
    gen "Why? You're getting quite good at it." ("base", xpos="far_left", ypos="head")
    her "........................." ("annoyed", "squint", "worried", "R")
    her "{number=current_payout} house points?" ("open", "squint", "worried", "R")
    gen "Sure!" ("grin", xpos="far_left", ypos="head")
    her "Very well, then..." ("open", "closed", "base", "R")

    jump hg_pf_strip_T4

label hg_pf_strip_T4_intro_E2:

    call start_hg_pf_strip

    gen "[name_hermione_genie], would you like to climb onto my desk for another show?" ("base", xpos="far_left", ypos="head")
    her "*Hmm*..." ("annoyed", "base", "base", "R", xpos="base", ypos="base")
    her "Sure! Why not..." ("base", "happyCl", "base", "mid")
    gen "Am I hearing some excitement in your voice?" ("grin", xpos="far_left", ypos="head")
    her "Oh... Well, I've been practising a bit more, so I won't make a fool out of myself." ("soft", "narrow", "worried", "down")
    if hermione.is_any_worn("top", "bottom", "panties", "bra"):
        gen "You've practised taking your clothes off?" ("base", xpos="far_left", ypos="head")
        her "No, I've been practising dancing..." ("disgust", "narrow", "worried", "mid")
        gen "I see..." ("base", xpos="far_left", ypos="head")
        gen "Well then, let me see your progress." ("base", xpos="far_left", ypos="head")
    else:
        gen "Very good... I'd love to see your progress." ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]..." ("open", "base", "base", "mid_soft")

    jump hg_pf_strip_T4

label hg_pf_strip_T4_E2:

    call start_hg_pf_strip

    gen "[name_hermione_genie], how do you feel about getting on my desk for another show?" ("base", xpos="far_left", ypos="head")
    if states.her.tier <= 5:
        her "Of course, [name_genie_hermione]..." ("open", "base", "base", "mid", xpos="base", ypos="base")
    else:
        her "Certainly, [name_genie_hermione]..." ("base", "narrow", "base", "stare", xpos="base", ypos="base")

    jump hg_pf_strip_T4

label hg_pf_strip_T4:
    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "-Invite Snape to watch-" if states.sna.ev.hangouts.hermione_strip_invite:
            jump hg_pf_strip_T4_snape

        "-Ask her to lock the door-":
            gen "Lock the door before you begin, will you?" ("base", xpos="far_left", ypos="head")
            if states.her.tier <= 5:
                her "Of course..." ("base", "base", "base", "mid")
            else:
                her "(How boring...)" ("annoyed", "narrow", "annoyed", "R")

            call hide_characters
            with d3
            pause.5

            call her_walk("door", "base")

            pause.5
            play sound "sounds/09_lock.ogg"
            pause.4

            # Walks back.
            call her_chibi("stand","door","base")
            pause.1

            call her_walk("mid", "base")
            pause.2

            her "All done!" ("smile", "closed", "base", "mid", trans=d3)

        "-Tell her to start the show-":
            gen "Go on then." ("base", xpos="far_left", ypos="head")
            if states.her.tier <= 4:
                her "Should I not lock the door first, [name_genie_hermione]?" ("soft", "base", "base", "mid")
                gen "Leave it unlocked, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her "But, what if somebody walks in again!" ("angry", "base", "base", "stare")
                gen "Nonsense... No such thing will happen." ("base", xpos="far_left", ypos="head")
                her "It happened before so why--" ("angry", "base", "angry", "mid")
                gen "Stop being such a fuzzy, and get over here..." ("base", xpos="far_left", ypos="head")
                her ".................." ("annoyed", "narrow", "angry", "R")

                $ states.her.mood += 4
            else:

                her "Yes, [name_genie_hermione]." ("soft", "narrow", "base", "mid_soft")

    stop music fadeout 1.0
    call her_walk("desk", "base", reduce=0.8)

    if hermione.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe", "accessory")
        pause .5

    # Climb desk
    call blkfade
    play sound "sounds/08_hop_on_desk.ogg"
    pause 2
    call her_chibi("dance","on_desk","on_desk")
    hide hermione_main
    hide screen blkfade
    with d5
    call ctc

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "..." ("soft", "narrow", "base", "mid_soft", xpos="mid", ypos="base", trans=d3)

    if hermione.is_worn("top"):
        nar "Hermione hastily starts pulling at her top..."

    gen "Slowly, please..." ("base", xpos="far_left", ypos="head")
    gen "There's no rush." ("base", xpos="far_left", ypos="head")

    if hermione.is_worn("top"):
        her "I'm not trying to--" ("open", "base", "angry", "mid")
        her "It's just--{w=0.2} I..." ("disgust", "narrow", "base", "down")
        gen "Would you like some help with it?" ("grin", xpos="far_left", ypos="head")
        if states.her.tier <= 5:
            her "No..." ("annoyed", "base", "angry", "mid")
            her "I can do it, [name_genie_hermione]." ("open", "closed", "base", "mid")
        else:
            her "No, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
            her "Just enjoy the show..." ("soft", "narrow", "base", "mid_soft")
            gen "I will, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")

    her "..." ("soft", "narrow", "worried", "down")

    if hermione.is_worn("top"):
        nar "Hermione pulls her top over her head..."
        nar "And takes it off somewhat gracefully..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top")
        pause.5

    if hermione.is_worn("bra"):
        nar "Hermione undoes her bra and lets it fall to the floor."

        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bra")
        pause.5

    nar "Hermione hesitates for a brief moment, then begins jiggling her tits at you..."
    gen "Yes! Shake those tits!" ("grin", xpos="far_left", ypos="head")

    if states.her.tier <= 4:
        her "Must you be so vulgar, [name_genie_hermione]?" ("annoyed", "closed", "base", "mid")
        gen "Should I not be voicing my enjoyment?" ("base", xpos="far_left", ypos="head")
        gen "How else are you supposed to know if you're doing it right?" ("base", xpos="far_left", ypos="head")
        her "Fine...{w=0.4} Go right ahead then, [name_genie_hermione]..." ("annoyed", "narrow", "worried", "down")

        nar "Hermione resumes shaking her tits..."
        nar "Her movements appear more repetitive than before, and you notice a blank expression across her face..."
        nar "After a couple of moments, she regains her focus and locks eyes with you."

        her "[name_genie_hermione]?" ("open", "base", "worried", "mid")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        her "May I ask you a question?" ("upset", "wink", "base", "mid")
        gen "Is it about how to shake your tits in a less repetitive manner?" ("base", xpos="far_left", ypos="head")
        her "*Huh*?" ("angry", "wink", "base", "mid")
        gen "Never mind... Go ahead..." ("base", xpos="far_left", ypos="head")
        her "..............." ("normal", "happyCl", "worried", "mid")
        her "Have you ever been in love...?" ("angry", "happyCl", "worried", "mid", emote="sweat")
        gen "In love?" ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]." ("angry", "narrow", "worried", "mid", emote="sweat")

        menu:
            gen "..." ("base", xpos="far_left", ypos="head")
            "\"Don't be ridiculous! Love is a lie!\"":
                her "I am sorry you think that way, [name_genie_hermione]!" ("annoyed", "base", "worried", "R")
                her "But you couldn't be more wrong!" ("annoyed", "narrow", "annoyed", "mid")
                her "I believe that true love is what makes the earth turn!" ("base", "base", "base", "R")
                gen "Actually the conservation of angular momentum is responsible for that." ("base", xpos="far_left", ypos="head")
                her "*Huh*?" ("upset", "wink", "base", "mid")
                if hermione.is_worn("bottom"):
                    gen "...{w=0.4} Just take off your bottoms already." ("base", xpos="far_left", ypos="head")
                else:
                    gen "...{w=0.4} Keep dancing!" ("base", xpos="far_left", ypos="head")
                her "............" ("annoyed", "narrow", "annoyed", "mid")

            "\"Be quiet and keep on dancing!\"":
                her "But you said I could ask you a question..." ("annoyed", "narrow", "annoyed", "mid")
                gen "And you did, didn't you?" ("base", xpos="far_left", ypos="head")
                her "!!!............" ("open", "base", "base", "stare")
                her "...................................." ("annoyed", "narrow", "annoyed", "mid")
                if hermione.is_worn("bottom"):
                    gen "Now hush... And take your bottoms off." ("base", xpos="far_left", ypos="head")
                else:
                    gen "Now hush... And let me enjoy this." ("base", xpos="far_left", ypos="head")
                her "........" ("annoyed", "narrow", "angry", "R")

            "\"Yes... A very long time ago...\"":
                her "!!!!!??.............................." ("open", "base", "base", "mid")
                gen "Her name was Eden..." ("base", xpos="far_left", ypos="head")
                her "Eden..." ("soft", "base", "base", "mid")
                her "Was she beautiful?" ("base", "base", "base", "mid")
                gen "She was so much more than that..." ("base", xpos="far_left", ypos="head")
                gen "She was smart, green, and perfect..." ("base", xpos="far_left", ypos="head")
                her "She was... \"green\"...?" ("open", "narrow", "worried", "down")
                her "Are you making fun of me, [name_genie_hermione]?" ("angry", "base", "angry", "mid")
                gen "You humans know nothing of true love..." ("base", xpos="far_left", ypos="head")
                her ".....................................?" ("soft", "base", "base", "mid")
                if hermione.is_worn("bottom"):
                    gen "*Err*... I mean, take off your bottoms, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
                else:
                    gen "*Err*... I mean, keep on dancing, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
                her "................." ("annoyed", "narrow", "angry", "R")

            "\"I feel like I'm in love right now!\"":
                her "What are you saying, [name_genie_hermione]!" ("angry", "narrow", "angry", "mid")
                her "Surely, you can't mean--" ("angry", "narrow", "angry", "R")
                gen "Oh, I mean it!" ("base", xpos="far_left", ypos="head")
                her "[name_genie_hermione], please!" ("disgust", "narrow", "base", "mid_soft")
                her "I'm one of your students!" ("soft", "base", "base", "mid")
                her "And you're older than my father!" ("grin", "happyCl", "worried", "mid", emote="sweat")
                gen "{size=-4}(You have no idea, girl.){/size}" ("base", xpos="far_left", ypos="head")
                her "Surely you must be looking at it scientifically, where \"love\" is described as nothing but a chemical reaction..." ("soft", "base", "base", "mid")
                her "Since I've been causing you to experience sexual arousal, you must've had an increase in endorphins-- Hormones-- Testosterone-- Estrogen--" ("angry", "closed", "base", "mid")
                gen "[name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
                her "Yes, [name_genie_hermione]?" ("soft", "base", "base", "mid")
                gen "Did you forget what you're supposed to be doing?" ("base", xpos="far_left", ypos="head")
                her "Oh, my apologies, [name_genie_hermione]... I get distracted sometimes." ("grin", "happyCl", "worried", "mid", emote="sweat")
                if hermione.is_worn("bottom"):
                    gen "Take off your bottoms already, would you?!" ("base", xpos="far_left", ypos="head")
                else:
                    gen "Get to the good stuff already, would you?!" ("base", xpos="far_left", ypos="head")
                her "Right..." ("annoyed", "base", "worried", "R")

    nar "Hermione begins swaying her hips rather seductively..."

    if hermione.is_worn("bottom"):
        nar "Whilst sliding her bottoms down..."
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("bottom")
        pause.5
    call ctc

    menu:
        "-Ask her to masturbate-":
            if states.her.tier == 4:
                jump hg_pf_strip_T4_fingering
            elif states.her.tier == 5:
                jump hg_pf_strip_T5_fingering
            else: # Tier 6, and a fallback for cheaters!
                jump hg_pf_strip_T6_fingering

        "-Take your cock out, start jerking off-":
            jump hg_pf_strip_T4_masturbate

        "-Show some manners, just watch-":
            jump hg_pf_strip_T4_watch

label hg_pf_strip_T4_watch:
    nar "You continue watching Hermione dance... Shifting your attention periodically between her heaving chest, and her swaying hips..."
    gen "(She certainly has improved her dancing routine...)" ("base", xpos="far_left", ypos="head")
    gen "(She might even be able to give the brothel whores of Agrabah a run for their money...)" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("angry", "narrow", "worried", "mid", xpos="mid", ypos="base")
    gen "(I'd say it might even be broadcast worthy.)" ("base", xpos="far_left", ypos="head")
    her "(I guess my dancing is better than I thought...)" ("soft", "narrow", "worried", "mid")
    her "(Time for the finishing act I suppose...)" ("angry", "happyCl", "worried", "mid")

    if hermione.is_any_worn("clothes"):
        her "[name_genie_hermione], I'm going to take off the rest now." ("open", "narrow", "worried", "mid")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        gen "Oh, yes, [name_hermione_genie]! Take it all off!" ("base", xpos="far_left", ypos="head")
        her "........" ("soft", "closed", "base", "mid")
        if hermione.is_worn("panties"):
            nar "Hermione begins taking off her panties..."
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("panties")
            nar "Once past her hips, she lets them go, and they slide down to her feet..."
            play sound "sounds/cloth_sound4.ogg"
            nar "After flicking them off the table, she resumes her dancing..."
        else:
            play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("clothes")
        gen "Yes... Very good..." ("base", xpos="far_left", ypos="head")
        nar "As Hermione stops talking, your focus quickly shifts away from her upper lips, and down to her lower..."
    else:
        nar "Just as Hermione is about to move on to the next part of her dance, your focus shifts towards her lower lips..."

    her "" ("angry", "narrow", "worried", "down")
    nar "Noticing your stare, Hermione's body becomes slightly more tense, yet she still tries to push on, in an attempted seductive manner..."
    her "" ("angry", "narrow", "worried", "R")
    nar "Determined to complete her task, she tries her best to continue her dance, while avoiding looking directly at you..."
    her "" ("angry", "narrow", "worried", "L")
    nar "You can see that she is trying to be graceful... But in her attempts at avoiding your gaze, she periodically stumbles on her own feet..."
    gen "*Hmm*... Perhaps I spoke too soon..." ("base", xpos="far_left", ypos="head")
    gen "She'd never get any tips at this rate..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("angry", "narrow", "worried", "mid")
    gen "Oh, did I say that out loud?" ("base", xpos="far_left", ypos="head")
    call ctc

    her ".........." ("annoyed", "narrow", "base", "mid_soft")
    her "" ("annoyed", "closed", "base", "mid")

    nar "Suddenly, Hermione breaks into a whole series of rather complex pirouettes..."
    gen "{size=-4}(Hold on... Now this is rather impressive actually...){/size}" ("base", xpos="far_left", ypos="head")
    pause.5
    nar "Hermione gives her breasts a squeeze, followed by another series of rather complex, and naughty movements..."
    call ctc

    gen "{size=-4}(Did she practise this?){/size}" ("base", xpos="far_left", ypos="head")
    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}" ("open", "closed", "base", "mid")
    pause.5
    nar "Hermione performs another set of movements that could be considered classy..."
    nar "If it wasn't for her naked tits bouncing all over the place..."

    gen "Yes, that's how it's done, you little harlot!" ("grin", xpos="far_left", ypos="head")
    gen "Show those brothel whores who's the boss!" ("grin", xpos="far_left", ypos="head")

    her "" ("base", "closed", "base", "mid")
    nar "Either due to focusing on her movements or your words, you notice that a smile has now spread across Hermione's face..."
    nar "Her every motion now comes across as purposeful and natural, and you can't help but almost getting hypnotized by her perky nipples..."
    nar "After a couple of gestures, she slows down, and finishes off with a little curtsy bow to an imaginary public..."
    gen "That's it, girl! That's how you do it!" ("grin", xpos="far_left", ypos="head")

    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    nar "Completely exhausted, Hermione slumps down onto her butt."
    nar "You watch her in silence for a couple of moments, until she's finally managed to catch her breath..."

    call hide_characters
    hide screen blkfade
    with d5
    call ctc

    her "Whew... This was rather exciting..." ("silly", "happyCl", "worried", "mid", emote="sweat", ypos="head", flip=False)

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-3}\"Good job, [name_hermione_genie]! You certainly know how to dance!\"{/size}":
            her "Really?" ("base", "happy", "base", "mid_soft")
            gen "Yes! You have a lot of talent for this!" ("base", xpos="far_left", ypos="head")
            her "Thank you [name_genie_hermione]." ("grin", "closed", "worried", "mid", emote="sweat")
        "{size=-3}\"*Hmm*... Overall, this was quite awful...\"{/size}":
            call her_chibi("sit_naked_shocked","on_desk","on_desk")
            her "Oh... I'm sorry [name_genie_hermione]..." ("soft", "happy", "base", "R")
            gen "That's alright... At least you got into it towards the end..." ("base", xpos="far_left", ypos="head")
            her "*Ehm*... I will keep that in mind, [name_genie_hermione]..." ("open", "base", "base", "R")
        "{size=-3}\".................................................\"{/size}":
            her "......................." ("silly", "happyCl", "worried", "mid", emote="sweat")

    call ctc

    jump end_hg_pf_strip

label hg_pf_strip_T4_masturbate:
    show screen blkfade
    with d5

    call gen_chibi("jerk_off","behind_desk","base")
    hide screen blkfade
    with fade

    her "But..." ("angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")
    her "............................."
    her "Well, alright...{w=0.4} But only if you will promise me not to--{w=0.2} Finish, [name_genie_hermione]." ("angry", "narrow", "angry", "R")

    $ _promise = False

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Promise her to hold it-":
            $ _promise = True #Promised to hold it.
            her "Well, alright then..." ("open", "closed", "base", "mid")

        "-Give her no such promise-":
            gen "Promise \"Not to finish\"? That would be like torture!" ("base", xpos="far_left", ypos="head")
            gen "Please keep your sadistic urges to yourself, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "I don't have any... Sadistic urges, [name_genie_hermione]!" ("disgust", "narrow", "annoyed", "R")
            her "I just don't want to get--" ("annoyed", "narrow", "base", "mid")
            gen "..." ("grin", xpos="far_left", ypos="head")
            her "[name_genie_hermione]... Are you even listening?" ("angry", "narrow", "worried", "mid")
            gen "*Ah*... Yes... You've truly got some shapely breasts, [name_hermione_genie]..." ("grin", xpos="far_left", ypos="head")
            her ".........." ("disgust", "narrow", "worried", "mid")
            her "Fine! Have it your way, I guess..." ("angry", "narrow", "worried", "R")
            her "{size=-5}(As usual...){/size}" ("annoyed", "narrow", "angry", "R")

    nar "Hermione moves her hips awkwardly, while trying her best not to look down towards your throbbing member..."
    nar "You speed up your pace, while focusing intently on Hermione's every move..."
    her "(Better get this done quickly, before it's too late...)" ("disgust", "happy", "worried", "R")

    if hermione.is_any_worn("clothes"):
        her "[name_genie_hermione], I'm going to take off the rest now." ("open", "narrow", "worried", "mid")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        gen "Oh, yes, [name_hermione_genie]! Take it all off!" ("base", xpos="far_left", ypos="head")
        her "........" ("soft", "closed", "base", "mid")
        if hermione.is_worn("panties"):
            nar "Hermione begins taking off her panties..."
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("panties")
            nar "Once past her hips, she lets them go, and they slide down to her feet..."
            play sound "sounds/cloth_sound4.ogg"
            nar "After flicking them off the table, she resumes her dancing..."
        else:
            play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("clothes")
        gen "Yes... Very good..." ("base", xpos="far_left", ypos="head")
        nar "As Hermione stops talking, your focus quickly shifts away from her upper lips, and down to her lower..."
    else:
        nar "Just as Hermione is about to move on to the next part of her dance, your focus shifts towards her lower lips..."

    nar "As if feeling your stare, Hermione finally gives in and looks down at your rock-hard cock..."
    her @ cheeks blush "*Gasp*" ("soft", "squint", "base", "down")
    her @ cheeks blush "" ("angry", "narrow", "base", "mid")
    nar "Catching herself in the act, she quickly looks back up at your face..."
    nar "You stare into her eyes, while still furiously beating yourself off..."
    her @ cheeks blush "" ("grin", "narrow", "base", "mid")
    nar "Doing her best to try and brush past her moment of weakness, she gives you a half-hearted smile, in an attempted seductive manner."
    her @ cheeks blush "" ("soft", "narrow", "base", "R")
    nar "Set on finishing her task, she does her best to avoid looking directly at you."
    her @ cheeks blush "" ("soft", "narrow", "base", "L")
    nar "You can see that she is doing her best to be graceful... But in her attempts at avoiding your gaze, she periodically stumbles on her own feet."
    call ctc

    nar "Nonetheless, you decide to show her some appreciation..."
    nar "By stroking your cock even faster!"
    her "........." ("angry", "narrow", "base", "dead")
    nar "Suddenly, Hermione breaks into a whole series of rather complex pirouettes."
    gen "*Ah*... That's it!" ("base", xpos="far_left", ypos="head")
    pause.5

    nar "She then gives her breasts a squeeze, followed by another series of rather complex, and naughty, movements."
    call ctc

    gen "{size=-4}(Did she practise this?){/size}" ("base", xpos="far_left", ypos="head")
    nar "You can't help but feel entranced by Hermione's movements."
    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}" ("open", "closed", "base", "mid")
    nar "You almost feel in sync with Hermione's dancing, and you begin stroking your dick along with her movements."
    gen "{size=-5}(One-two-three... One-two-three... And edge!){/size}" ("base", xpos="far_left", ypos="head")

    pause.5

    nar "Hermione performs another set of movements that could be considered classy..."
    nar "If not for her naked tits bouncing all over the place."

    gen "Yes, dance for me, you little whore!" ("grin", xpos="far_left", ypos="head")
    nar "Either due to wanting to finish things quickly, or being excited by your words, Hermione starts putting even more effort into her dance."
    nar "Her every motion now comes across as purposeful and natural, and you can't help but almost getting hypnotized by her perky nipples..."
    nar "And after a few more movements, a couple of gestures and a little curtsy bow to the imaginary public--"
    show screen blkfade
    with d5

    call her_chibi("sit_naked","on_desk","on_desk")

    nar "--Hermione slumps down onto her butt, completely exhausted."

    hide hermione_main
    hide screen blkfade
    with d5
    call ctc

    her "(Whew... I made it... And not a moment too--)" ("base", "closed", "base", "mid", ypos="head", flip=False)
    with hpunch
    gen "*ARGH*! YOU FUCKING CUNT!" ("angry", xpos="far_left", ypos="head")

    call cum_block
    call gen_chibi("cum","behind_desk","base")
    $ hermione.set_cum(hair="light")
    pause 0.7
    $ hermione.set_cum(face="light")
    pause 1
    $ hermione.set_cum(breasts="light")
    call ctc

    call her_chibi("sit_naked_shocked","on_desk","on_desk")
    call gen_chibi("cum","behind_desk","base")

    her "??!!!" ("shock", "wide", "base", "stare")
    her "[name_genie_hermione]!!!" ("angry", "squint", "worried", "stare")

    call gen_chibi("cum_done","behind_desk","base")

    if _promise: #Promised to hold it.
        her "No, [name_genie_hermione]! You promised!" ("angry", "happyCl", "worried", "mid", ypos="head", flip=False)
        gen "Oh, man... That was intense..." ("angry", xpos="far_left", ypos="head")
        her "You went back on your word, [name_genie_hermione]!" ("scream", "happyCl", "worried", "mid")
        gen "*Huh*? What are you talking about?" ("base", xpos="far_left", ypos="head")
        gen "You gave me the look! You looked at it and smiled!" ("base", xpos="far_left", ypos="head")
        her @ tears crying_blink "How could you do this to me, [name_genie_hermione]?" ("shock", "base", "angry", "mid")
        gen "Oh, calm down, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Now, put yourself together, before somebody discovers you like this." ("base", xpos="far_left", ypos="head")
        her @ tears messy "*Sob*!........................" ("shock", "narrow", "angry", "R")
        show screen blkfade
        with d5

        $ hermione.wear("all")
        stop music fadeout 5.0
        pause 1.5

        her "... Can I just get paid now, [name_genie_hermione]... Please?" ("annoyed", "narrow", "angry", "R")

        $ states.her.mood += 20

        jump end_hg_pf_strip

    else:
        her "{size=-3}It's so hot...{/size}" ("disgust", "happyCl", "worried", "mid", ypos="head", flip=False)
        call gen_chibi("hold_dick","behind_desk","base")
        gen "*Ah-ah*... That felt great..." ("base", xpos="far_left", ypos="head")
        her "You came all over me..." ("angry", "narrow", "base", "R")
        her "I'm your pupil... And..." ("disgust", "happy", "base", "R")
        her "{size=-3}You just came on me...{/size}" ("disgust", "narrow", "annoyed", "up")
        gen "I know! Pretty exciting, right?!" ("grin", xpos="far_left", ypos="head")
        her "*Hmph*... It was nothing of the sort!" ("annoyed", "narrow", "base", "R")
        her "You should have restrained yourself like a proper headmaster would!" ("angry", "narrow", "base", "R")
        gen "Really? I never heard that restraint was part of the job description..." ("base", xpos="far_left", ypos="head")
        her "You could've at the very least aimed it somewhere else!" ("annoyed", "narrow", "base", "mid")
        gen "The blood-flow was being redirected to my penis, I could hardly move my legs and turn away!" ("base", xpos="far_left", ypos="head")
        her "But your hands kept moving, so move them and point it at the floor!" ("angry", "happy", "annoyed", "mid")
        gen "Not even an unstoppable force could push down this immovable object." ("base", xpos="far_left", ypos="head")
        her "........" ("disgust", "narrow", "base", "R")
        her "Still, you should not have... It wasn't a part of the favour." ("soft", "base", "angry", "mid")
        her "I did not agree to be defiled like this!" ("disgust", "narrow", "base", "down")
        gen "I think I know where this is going..." ("base", xpos="far_left", ypos="head")

    her "I demand to be paid extra!" ("angry", "base", "angry", "mid")
    gen "Of course you do..." ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"You get one extra point.\"":
            $ states.her.mood += 20
            $ current_payout += 1

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "One extra point?" ("soft", "base", "angry", "stare")
            her "One meagre point for allowing you to defile me like this?" ("scream", "squint", "annoyed", "mid")
            her "Now, that is just insulting, [name_genie_hermione]!" ("soft", "base", "angry", "mid")
            gen "One extra point, [name_hermione_genie]. Take it or leave it." ("base", xpos="far_left", ypos="head")
            call her_chibi("sit_naked","on_desk","on_desk")

            her "............." ("annoyed", "narrow", "angry", "R")
            her "I'll take it." ("soft", "base", "angry", "mid")
            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You get ten extra points.\"":
            $ states.her.mood += 10
            $ current_payout += 10

            her "Ten extra points, [name_genie_hermione]?" ("soft", "base", "angry", "mid")
            her "But that is not even nearly enough!" ("soft", "base", "angry", "mid")
            gen "Ten extra points. Take it or leave it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            call her_chibi("sit_naked","on_desk","on_desk")

            her "..............." ("annoyed", "narrow", "angry", "R")
            her "Well, alright... Better than nothing I suppose..." ("soft", "base", "angry", "mid")

            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You get twenty-five extra points.\"":
            $ current_payout += 25

            call her_chibi("sit_naked","on_desk","on_desk")

            her "Yes, I believe this would be an appropriate amount." ("open", "closed", "base", "mid")
            gen "Are we good then?" ("base", xpos="far_left", ypos="head")
            her "Yes, [name_genie_hermione]... Thank you." ("open", "closed", "base", "mid")
            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You get fifty extra points.\"":
            $ current_payout += 50

            her "Seriously?!" ("angry", "wide", "base", "stare")
            call her_chibi("sit_naked","on_desk","on_desk")

            her "Oh... I don't know what to say..." ("open", "wide", "base", "stare")
            gen "I thoroughly enjoyed your performance, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Thank you [name_genie_hermione]..." ("grin", "narrow", "base", "mid_soft")
            gen "How could I resist, plastering your agile little body with cum..." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]......" ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "So, just allow me to show my appreciation out of it." ("base", xpos="far_left", ypos="head")
            gen "Fifty extra points, all well deserved, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Thank you very much, [name_genie_hermione]." ("silly", "happyCl", "worried", "mid", emote="sweat")
            call ctc

            show screen blkfade
            with d5
            $ hermione.wear("all")
            jump end_hg_pf_strip

        "\"You're not getting shit!\"":
            stop music fadeout 1.0
            her "What? Not even my usual pay?" ("shock", "wide", "base", "stare")

            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"Oh, no, you are still getting that.\"":
                    $ states.her.mood += 20
                    her "How generous of you, [name_genie_hermione]..." ("soft", "base", "angry", "mid")
                    call ctc

                    show screen blkfade
                    with d5
                    $ hermione.wear("all")
                    jump end_hg_pf_strip

                "\"No, not even that!\"":
                    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
                    her "!!!?" ("angry", "base", "base", "stare")
                    her "So, what you're saying, is that I danced for you..." ("soft", "happy", "base", "stare")
                    her "I degraded myself for your amusement..." ("soft", "happy", "base", "R")
                    her "I even let you cum on me..." ("open", "base", "base", "R")
                    her "And I get, {size=+5}NOTHING?!{/size}" ("clench", "base", "angry", "mid", emote="angry", trans=hpunch)
                    gen "You've got a shiny and glistening complexion out of it..." ("base", xpos="far_left", ypos="head")
                    her "Oh, this is a new low... Even for you, [name_genie_hermione]!" ("soft", "base", "angry", "mid")
                    gen "Dismissed." ("base", xpos="far_left", ypos="head")
                    her "{size=+5}*GROAN*!{/size}" ("clench", "base", "angry", "mid", emote="angry")
                    call ctc

                    show screen blkfade
                    with d5
                    $ hermione.wear("all")

                    call gen_chibi("sit_behind_desk")
                    call her_chibi("stand","desk","base")
                    hide screen blkfade
                    with d5

                    call her_walk(action="leave")

                    $ states.her.mood += 30

                    jump end_hermione_event
