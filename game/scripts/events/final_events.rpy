
default her_ev_yule_ball_e4 = Event(id="her_ev_yule_ball_e4", wait=2, label="ball_quest_E4", priority=15, req="game.daytime", repeat=False)
default her_ev_yule_ball_e3 = Event(id="her_ev_yule_ball_e3", wait=4, label="ball_quest_E3", priority=15, req="game.daytime", repeat=False, subevents=["her_ev_yule_ball_e4"])
default her_ev_yule_ball_e2 = Event(id="her_ev_yule_ball_e2", wait=1, label="ball_quest_E2", priority=15, req="game.daytime", repeat=False, subevents=["her_ev_yule_ball_e3"])
default her_ev_yule_ball_e1 = Event(id="her_ev_yule_ball_e1", label="ball_quest_E1", priority=15, req="states.her.tier >= 6 and game.daytime and not states.her.busy and not states.her.ev.yule_ball.e1_complete", autoenqueue=True, repeat=False, subevents=["her_ev_yule_ball_e2"])

#hermione asks genie about who will be in-charge of the ball
label ball_quest_E1:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="mid", ypos="base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "[name_genie_hermione]?" ("soft", "base", "base", "mid", xpos="right", ypos="base")
    gen "[name_hermione_genie], how can I help you?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], have you made your decision yet on who will be in charge of the \"ABOC\" this year?" ("open", "base", "base", "mid")
    gen "\"ABOC\"?" ("base", xpos="far_left", ypos="head")
    her "The \"Autumn Ball Organization Committee\", [name_genie_hermione]..." ("open", "closed", "base", "mid")
    gen "*Ehm*... Sure..." ("base", xpos="far_left", ypos="head")
    her "Please excuse me if I am being too direct with this, [name_genie_hermione]..." ("normal", "squint", "angry", "mid")
    her "But I think you should put {b}me{/b} in charge." ("open", "closed", "angry", "mid")
    her "I did it last year, and it was the best organised \"autumn ball\" Hogwarts has had in years." ("open", "closed", "base", "mid")
    her "You said so yourself, [name_genie_hermione]. Do you remember?" ("normal", "base", "base", "mid")
    gen "Right, of course..." ("base", xpos="far_left", ypos="head")
    her "So, is this a yes?" ("base", "base", "base", "mid")
    her "Does this mean I will be in charge again this year?" ("base", "base", "base", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"You shall be in charge, [name_hermione_genie].\"":
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")

        "\"No. Professor Snape shall be in charge!\"":
            her "Professor Snape, [name_genie_hermione]?" ("open", "squint", "angry", "mid")
            her "But, traditionally organizing and hosting the ball is the responsibility of the students..." ("normal", "base", "angry", "mid")
            her "Teachers are only present as the guests of honour..." ("open", "closed", "angry", "mid")
            gen "Of course...{w=0.4} I was just kidding." ("base", xpos="far_left", ypos="head")
            gen "You shall be in charge, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

    gen "There is one condition, though..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("normal", "squint", "angry", "mid")

    $ d_flag_01 = False
    $ d_flag_02 = False # Have sex with me
    $ d_flag_03 = False # Masturbation flag

    label .choices:

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Take some of those clothes off.\"" if hermione.is_any_worn("top", "bottom", "bra", "panties"):
            $ states.her.mood += 5
            $ d_flag_01 = True

        "\"Just stand right there for a moment.\"" if not hermione.is_worn("top", "bottom", "bra", "panties"):
            if hermione.is_any_worn("clothes"):
                gen "And take off those things you're wearing." ("base", xpos="far_left", ypos="head")
                her "Alright..." ("open", "squint", "base", "R")
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("clothes")
            else:
                her "Just stand right here?" ("base", "base", "base", "R")
                gen "Yes, just stand right there for me..." ("base", xpos="far_left", ypos="head")
            her "..." ("base", "base", "base", "mid")
            her "Is that all?" ("open", "squint", "base", "mid")
            jump ball_quest_E1.after_strip

        "\"You will have to sleep with me.\"" if not d_flag_02 and not states.her.status.sex:
            $ states.her.mood += 10
            $ d_flag_02 = True

            her "I will have to--{w=0.2} Sleep...?" ("angry", "wide", "base", "mid")
            her @ cheeks blush "..................." ("angry", "base", "angry", "mid")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her @ cheeks blush "I am not stupid, [name_genie_hermione]... Quite the opposite in fact." ("angry", "closed", "angry", "mid")
            her @ cheeks blush "And I understand that the nature of the favours I have been selling you lately..." ("open", "base", "angry", "R")
            her @ cheeks blush "... Might have led you to believe that I would be willing to..." ("open", "squint", "angry", "mid")
            her @ cheeks blush "... To let you have your way with me eventually, [name_genie_hermione]..." ("disgust", "squint", "angry", "L_soft")
            gen "Whaaa--? I would never--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Please, let me finish, [name_genie_hermione]." ("scream", "base", "angry", "mid",emote="angry")
            gen "Right..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I know that you are a rather wise man yourself, [name_genie_hermione]." ("angry", "base", "angry", "mid")
            her @ cheeks blush "So, please... Understand this..." ("disgust", "narrow", "base", "L_soft")
            her @ cheeks blush "I may be willing to sacrifice my pride and even my dignity for the sake of my house..." ("open", "closed", "angry", "mid")
            her @ cheeks blush "But sleeping with my headmaster?" ("open", "squint", "annoyed", "mid")
            her @ cheeks blush "That is where I draw the line, [name_genie_hermione]." ("angry", "base", "angry", "mid")
            gen "Fine... In that case..." ("base", xpos="far_left", ypos="head")

            jump ball_quest_E1.choices

        "\"Never mind. the Position is yours.\"":
            $ states.her.mood = 0

            her "Really?" ("smile", "base", "base", "mid")
            gen "Yes." ("base", xpos="far_left", ypos="head")

            jump ball_quest_E1.end

    if d_flag_02:
        her @ cheeks blush "Do I have to?" ("annoyed", "base", "annoyed", "R")
        gen "No [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "You don't have to take any clothes off..." ("base", xpos="far_left", ypos="head")
        her "Finally you're being reasonable." ("open", "closed", "base", "mid")
        if hermione.is_worn("panties"):
            gen "I only need you to pull those panties aside for easy access." ("grin", xpos="far_left", ypos="head")
        else:
            gen "I only need you to bend over my desk for easy access." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]! I thought I established this already... I'm not going to sleep with you!" ("angry", "narrow", "angry", "mid")
        gen "Then the answer is yes..." ("base", xpos="far_left", ypos="head")
        gen "If you want to be in charge of my balls--" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "The \"Autumn Ball\", [name_genie_hermione]..." ("upset", "squint", "annoyed", "mid")
        her "But this isn't a favour... this is THE Autumn Ball we're talking about..." ("open", "squint", "angry", "mid")
        gen "Then would you say the job of organizing it is... an honour?" ("base", xpos="far_left", ypos="head")
        her "It is!" ("open", "closed", "base", "mid")
        gen "And you believe that you should be the one to do it?" ("base", xpos="far_left", ypos="head")
        her "I do!" ("open", "base", "base", "mid")
        gen "Well then..." ("base", xpos="far_left", ypos="head")
        gen "Show me what you're prepared to do for the privilege!" ("base", xpos="far_left", ypos="head")
    else:
        her "What?!" ("open", "base", "base", "mid")
        gen "What?" ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]!" ("angry", "base", "angry", "mid")
        gen "What?" ("base", xpos="far_left", ypos="head")
        her "You are abusing your power, [name_genie_hermione]. Again!" ("disgust", "narrow", "base", "mid_soft")
        gen "Seriously? After all those favours you sold me?" ("base", xpos="far_left", ypos="head")
        her "Those were for the sake of my house, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
        gen "Well this one is for the sake of the \"Autumn prom\"." ("base", xpos="far_left", ypos="head")
        her "It's the \"Autumn Ball\", [name_genie_hermione]..." ("upset", "closed", "base", "mid")
        gen "Oh, come on..." ("base", xpos="far_left", ypos="head")
        gen "Entrusting the thing to somebody else would be a crime, you know that." ("base", xpos="far_left", ypos="head")
        her ".........." ("annoyed", "narrow", "angry", "R")
        gen "Don't you care about your classmates at all?" ("base", xpos="far_left", ypos="head")
        her "What?" ("open", "base", "base", "mid")
        gen "Put your selfishness aside for once, would you?" ("base", xpos="far_left", ypos="head")
        her "My... Selfishness?" ("annoyed", "base", "worried", "R")
        gen "Your classmates deserve the best organised ball possible!" ("base", xpos="far_left", ypos="head")
        gen "And only {size=+5}YOU{/size} can give them that!" ("base", xpos="far_left", ypos="head")
        her "... That is true actually." ("angry", "narrow", "base", "down")
        gen "People depend on you, girl!" ("base", xpos="far_left", ypos="head")
        her "You... Maybe you're right, [name_genie_hermione]." ("open", "narrow", "worried", "down")
        her "I must do this... Everyone depends on me." ("upset", "closed", "base", "mid")

    her "Just give me a second please." ("annoyed", "narrow", "base", "R")
    hide hermione_main
    with d5

    gen "............" ("base", xpos="far_left", ypos="head")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    hide screen bld1
    hide hermione_main
    with d5

    #Walks to the door
    call her_walk("door", "base")

    #Locks the door
    pause.5
    call chibi_emote("thought","hermione")
    pause.5

    call chibi_emote("hide", "hermione")
    play sound "sounds/09_lock.ogg"
    pause 1.5

    #Returns from the door
    gen "......?" ("base", xpos="far_left", ypos="head")

    call her_walk("mid", "base")
    pause.2

    her @ cheeks blush "Just in case..." ("annoyed", "narrow", "angry", "R")

    $ d_flag_01 = False
    $ d_flag_02 = False

    gen ".........................." ("base", xpos="far_left", ypos="head")
    her "Okay then... what would you have me do?" ("normal", "base", "worried", "mid")

    label .choices2:

    if d_flag_01 and d_flag_02:
        if hermione.is_any_worn("clothes"):
            gen "Now take off everything else you're wearing." ("base", xpos="far_left", ypos="head")
            $ hermione.strip("clothes")

        jump ball_quest_E1.after_strip

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Take your top off.\"" if not d_flag_01:
            $ d_flag_01 = True

            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

            if not hermione.is_worn("top"):
                her "Take off my what? I'm not exactly clothed, you know!" ("angry", "base", "annoyed", "R")
                if not hermione.is_worn("bra"):
                    her "Can't you see that my breasts are already on display?" ("annoyed", "squint", "angry", "mid")
                    gen "Right..." ("base", xpos="far_left", ypos="head")

                    jump ball_quest_E1.choices2
                else:
                    gen "You are still wearing a bra, aren't you?" ("base", xpos="far_left", ypos="head")

                    jump ball_quest_E1.bra

            her @ cheeks blush "............" ("annoyed", "base", "worried", "R_soft")

            pause.3

            # TODO Animation doesn't work if this option is chosen second.
            # The standing chibi will reflect clothing state (once we have a topless chibi, that is)
            # call her_chibi("lift_top","mid","base")
            # with d3
            # pause 2.0
            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("robe", "accessory")
            $ hermione.strip("top")

            call ctc

            if hermione.is_worn("bra"):
                pause 2.0
                gen "And your bra..." ("base", xpos="far_left", ypos="head")

                label .bra:

                her @ cheeks blush "..." ("annoyed", "base", "angry", "R_soft")
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("bra")
                pause.5

            her @ cheeks blush "" ("soft", "base", "base", "R_soft")
            call ctc

            gen "Very good [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Your ample tits are always a welcome sight..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...................." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "" ("normal", "base", "worried", "R_soft")

            jump ball_quest_E1.choices2

        "\"Take your bottoms off.\"" if not d_flag_02:
            $ d_flag_02 = True

            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
            $ hermione.strip("robe", "accessory")
            if not hermione.is_worn("bottom"):
                her "I would if you'd let me wear any!" ("angry", "base", "angry", "mid")
                if not hermione.is_worn("panties"):
                    her "You have no idea how cold Hogwarts can be this time of year!" ("annoyed", "base", "worried", "R")
                    gen "......." ("base", xpos="far_left", ypos="head")

                    jump ball_quest_E1.choices2
                else:
                    gen "You don't need any, in fact, you don't need your panties either!" ("grin", xpos="far_left", ypos="head")
                    gen "Take them off..." ("base", xpos="far_left", ypos="head")

                    jump ball_quest_E1.panties

            pause.3

            # TODO Animation doesn't work if this option is chosen second. Just use the standing chibi (ie. remove the commented code)
            # call her_chibi("lift_skirt","mid","base")
            # with d3
            # pause 2.0

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bottom")

            call ctc

            if hermione.is_worn("panties"):
                pause 2.0
                gen "And your panties..." ("base", xpos="far_left", ypos="head")

                label .panties:

                her @ cheeks blush "..." ("normal", "base", "low", "R_soft")
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("panties")
                pause.5

            her @ cheeks blush "" ("annoyed", "base", "base", "R_soft")
            call ctc

            her @ cheeks blush ".............................." ("annoyed", "base", "angry", "R_soft")

            gen "What are you doing, girl?!" ("angry", xpos="far_left", ypos="head") with hpunch
            gen "I am your headmaster! Do you have no shame?!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "What?! But--" ("angry", "base", "angry", "mid")
            gen "*He-he*... Relax, [name_hermione_genie]. I'm just kidding." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione], that was just mean." ("scream", "happyCl", "angry", "mid")
            gen "*Heh-he*..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "....................................." ("annoyed", "base", "worried", "R_soft")
            gen "I do like your cute little pussy though..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..... Thank you, [name_genie_hermione]." ("disgust", "base", "angry", "R_soft")

            jump ball_quest_E1.choices2

        "\"Never mind. The position is yours.\"" if d_flag_01 or d_flag_02:
            her "Really?" ("smile", "base", "base", "mid")

            jump ball_quest_E1.end

    label .after_strip:

    call her_chibi("stand")
    with d5
    pause 1.0

    gen "Looking good [name_hermione_genie]..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Happy now?" ("annoyed", "base", "worried", "R")
    her "Will you let me have the \"privilege\" of being in charge of the \"ABOC\" this year?" ("normal", "base", "worried", "mid")

    menu:
        "\"Of course... the Position is yours.\"":
            her "Really?" ("smile", "base", "base", "mid")

            jump ball_quest_E1.end

        "\"Touch yourself for me first...\"":
            $ states.her.status.masturbating = True
            $ d_flag_03 = True
            $ states.her.mood += 5

            her "You want me to..." ("shock", "wide", "base", "stare")
            gen "Flick the bean..." ("base", xpos="far_left", ypos="head")
            gen "Fondle those puppies..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I..." ("angry", "wide", "worried", "mid")
            gen "Or did you not want to be in charge?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of--{w=0.2} Of course I do!" ("angry", "base", "worried", "down")
            gen "Then get on with it..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "happyCl", "worried", "down")
            her @ cheeks blush "Fine..." ("disgust", "squint", "worried", "down")

            show screen blkfade
            with d5
            play sound "sounds/slick_02.ogg"
            with hpunch
            with kissiris
            $ hermione.set_pose("hand_on_pussy")
            her "" ("open", "squint", "worried", "mid", xpos=270)
            hide screen blkfade
            with d5

            pause 0.5

            her @ cheeks blush "*Ah*..." ("open", "squint", "worried", "R")
            gen "Ni-i-i-ce!" ("grin", xpos="far_left", ypos="head")
            play background "sounds/slickloop.ogg" fadein 2
            her @ cheeks blush "*mmmh*..." ("open", "happyCl", "worried", "R")
            pause 0.4
            her @ cheeks blush "" ("soft", "closed", "base", "R")
            pause 0.4
            call ctc
            her @ cheeks blush tears soft "*Sob*!" ("soft", "squint", "worried", "R_soft")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Oh, please,{w=0.4} don't mind me, [name_genie_hermione]." ("open", "base", "base", "R")
            her @ cheeks blush tears soft "Just enjoy the... {w=0.5}The view..." ("upset", "happy", "base", "R")
            gen "Are you... Crying?" ("base", xpos="far_left", ypos="head")
            stop background

            # Hand down
            $ hermione.set_pose(None)

            her @ cheeks blush tears crying_blink "*Sob*! No, [name_genie_hermione]... *Sob*!..." ("angry", "happyCl", "worried", "mid")
            her @ cheeks blush tears crying "I... I enjoy touching myself...{w=0.5} In front of my headmaster, *SOB*!" ("angry", "squint", "worried", "R_soft")

            # Hands on pussy, breast
            $ hermione.set_pose("hand_on_pussy_and_breast")

            play background "sounds/slickloop.ogg" fadein 2
            her @ cheeks blush "*Ah*..." ("open", "squint", "worried", "R")
            her @ cheeks blush tears messy "These...{w=0.4} *Ah*...{w=0.5} Are happy tears, [name_genie_hermione]." ("open", "narrow", "low", "R")
            her @ cheeks blush tears messy "I...{w=0.5} *Ah*...{w=0.5}... I'm sorry...{w=0.5} I can't help it! *Sob*!" ("angry", "happyCl", "worried", "mid_soft")
            gen "Are you sure that you are okay with this?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "Yes...{w=0.4} *Ah*...{w=0.5} Yes, sir, please.... *Sob*!" ("soft", "squint", "worried", "mid")
            her @ cheeks blush tears messy "Please keep looking as I...{w=0.3} Pleasure myself, *Sob*!" ("open", "narrow", "base", "mid_soft")
            her @ cheeks blush tears messy "" ("open", "narrow", "angry", "stare_soft")
            pause.2

            gen "(What the--)" ("angry", xpos="far_left", ypos="head")
            with hpunch
            her @ cheeks blush tears messy "[name_genie_hermione], I am begging you!" ("soft", "narrow", "angry", "mid")
            gen "Kind of sounds like an order--" ("base", xpos="far_left", ypos="head")
            play background "sounds/slickloopfast.ogg"
            her @ cheeks blush tears messy "I need it!" ("open", "narrow", "worried", "up_soft")
            her @ cheeks blush tears messy "... I need to shamelessly present my naked body before you like this!" ("soft", "narrow", "base", "up_soft")
            with hpunch
            gen ".............?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "I need to feel this embarrassment and humiliation! *SOB*!" ("silly", "narrow", "angry", "dead")
            play background "sounds/slickloopveryfast.ogg"
            her @ cheeks blush tears messy "The fate of the \"Autumn ball\" depends on this..." ("silly", "base", "worried", "mid_soft")
            her "So... [name_genie_hermione], please..."
            her @ cheeks blush tears messy "Keep looking at my naked breasts, and my pussy..." ("silly", "narrow", "worried", "mid")
            her "Look at me, as I get wet for you..."
            her @ cheeks blush tears messy "*mmmh*..." ("open", "happyCl", "worried", "R") #disgusted #blushing
            call ctc


            with hpunch
            her @ cheeks blush tears messy "*Ah*...{w=0.5} Yes! Make my skin burn with shame, [name_genie_hermione]... *Sob*!" ("open", "narrow", "base", "up")
            gen "*Ehm*... Right... Okay..." ("base", xpos="far_left", ypos="head")
            gen "Listen, I think this will do..." ("base", xpos="far_left", ypos="head")

            play background "sounds/slickloop.ogg" fadein 2
            her @ cheeks blush tears messy "*Ah*...{w=0.5} Are you sure, [name_genie_hermione]?" ("open", "narrow", "base", "mid")
            her @ cheeks blush tears messy "Are you sure that you've humiliated me enough, [name_genie_hermione]?" ("base", "narrow", "worried", "mid_soft")
            gen "...................." ("base", xpos="far_left", ypos="head")
            gen "(Is she getting off from this, or is she being sarcastic? I don't get it...)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "*Mmmh*............" ("open", "happyCl", "worried", "R")
            call ctc

            gen "That's enough..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "" ("annoyed", "base", "base", "mid")
            gen "Just put your clothes back on, [name_hermione_genie]. You're making me feel uncomfortable." ("base", xpos="far_left", ypos="head")
            stop background fadeout 4
            her "..."

            # Reset pose
            $ hermione.set_pose(None)
            $ hermione.strip("clothes")

            her @ cheeks blush tears messy "As you wish, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")

            stop music fadeout 3.0

    label .end:

    show screen blkfade
    with d5
    call her_chibi("stand","mid","base")
    her "" ("base", "happyCl", "base", "mid", xpos="right", ypos="base")
    $ hermione.wear("all")
    pause 2.0
    hide screen blkfade
    with d5

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "So... Does this mean I'm officially in charge of this year's \"Autumn Ball Organization Committee\" now?" ("base", "happyCl", "base", "mid", xpos="right", ypos="base")
    gen "That you are." ("base", xpos="far_left", ypos="head")
    her "Thank you [name_genie_hermione]! You will not regret this, I promise!"
    if d_flag_03:
        gen "(That was weird... She sure changed her mood quick.)" ("base", xpos="far_left", ypos="head")
        gen "(Maybe she gets off from being humiliated...)" ("base", xpos="far_left", ypos="head")
        gen "(Guess I'll have to find out.)" ("base", xpos="far_left", ypos="head")
    else:
        gen "{size=-4}(Why would I?){/size}" ("base", xpos="far_left", ypos="head")
        gen "{size=-4}(I couldn't care less about the whole thing...){/size}" ("base", xpos="far_left", ypos="head")
    her "Well, I'd better go now. I have so many arrangements to make!" ("grin", "base", "base", "R")
    gen "By all means, [name_hermione_genie]. Have a nice day." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")
    pause.5

    call bld
    gen "........................................" ("base", xpos="far_left", ypos="head")
    gen "A ball, *huh*?" ("base", xpos="far_left", ypos="head")
    gen "I wonder if I will have to show up for that..." ("base", xpos="far_left", ypos="head")

    $ states.her.ev.yule_ball.e1_complete = True

    $ states.her.busy = True
    $ ss_event_pause += 2 # Next event happens in 2 days.

    jump end_hermione_event


#Snape confronts genie about his ABOC decision

label ball_quest_E2:
    stop music fadeout 1.0

    call sna_walk(action="enter", xpos="mid", ypos="base")
    pause.2

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    sna "Are you bloody insane?!" ("snape_01", xpos="base", ypos="base")
    gen "You know, sometimes I think I may be..." ("base", xpos="far_left", ypos="head")

    sna "You appointed {b}that{/b} girl as the head of the \"Autumn Ball Organization Committee\"?!!" ("snape_01")
    gen "I'm guessing that's bad?" ("base", xpos="far_left", ypos="head")
    sna "Bad?{w} {size=+5}BAD?!{/size}" ("snape_10")
    sna "{size=+5}That's a catastrophe!{/size}" ("snape_15")
    sna "Last year's ball was completely horrible!" ("snape_16")
    gen "Was it? I heard differently..." ("base", xpos="far_left", ypos="head")
    sna "Oh really? And who told you that?" ("snape_10")
    gen "Not a very reliable source apparently..." ("base", xpos="far_left", ypos="head")
    sna "Dammit... Dammit all to hell..." ("snape_08")
    sna "I had big plans for the thing..." ("snape_07")
    gen "Really? Like what?" ("base", xpos="far_left", ypos="head")
    sna "Oh, that doesn't matter now..." ("snape_06")
    sna "Now the girl will use the prefects or the ghosts to keep an eye on me throughout entire thing..."
    gen "Right, that reminds me..." ("base", xpos="far_left", ypos="head")
    gen "Am I supposed to show up as well?" ("base", xpos="far_left", ypos="head")
    sna "Show up?" ("snape_03")
    sna "You are expected to host the bloody thing!"
    sna "But don't you worry! I'll figure something out!" ("snape_09")
    sna "*Hmm*... I'll Probably have to host the ball instead..." ("snape_06")
    gen "............" ("base", xpos="far_left", ypos="head")
    sna "Well, the Autumn ball is about to happen and Hermione Granger is in charge..." ("snape_09")
    sna "There is no changing it now..."
    sna "Sorry for the outburst..." ("snape_05")
    sna "That girl brings out the worst in me..." ("snape_16")
    gen "Don't sweat it..." ("base", xpos="far_left", ypos="head")
    sna "You know what...?" ("snape_06")
    sna "I don't feel like working today..."
    sna "Do we still have any of Dumbledore's wine left?" ("snape_05")
    gen "I believe so..." ("base", xpos="far_left", ypos="head")
    sna "Great! Pour me some..." ("snape_02")
    gen "Seriously? You're just gonna bail on your class like that?" ("base", xpos="far_left", ypos="head")
    sna "Yeah, big news -- I hate my job." ("snape_03")
    sna "And since you are my boss..."
    sna "I don't know why I even bother teaching those so-called students..." ("snape_06")
    gen "To maintain the charade?" ("base", xpos="far_left", ypos="head")
    sna "Right..." ("snape_05")
    sna "But you know what else could endanger our little enterprise?"
    sna "Me losing it during class, and strangling a couple of Gryffindor maggots with my bare hands..." ("snape_07")
    gen "*Hmm*... I see your point..." ("base", xpos="far_left", ypos="head")
    sna "Seriously, man... I need a drink..." ("snape_06")

    hide snape_main
    call blkfade

    call gen_chibi("hide")
    show screen with_snape(ani=False)
    $ chair_OBJ.hidden = True

    $ states.fireplace_started = True
    $ fireplace_OBJ.foreground = "fireplace_fire"
    call sna_chibi("hide")
    hide screen bld1
    call hide_blkfade

    call bld
    nar "Professor Snape spends the day in your chamber, drinking the stress away."

    if states.sna.level < 100:
        nar "Your relationship with him has improved."
        $ states.sna.level +=1

    $ ss_event_pause += 2
    $ hg_event_pause += 1

    $ states.her.ev.yule_ball.e2_complete = True
    $ chair_OBJ.hidden = False
    $ fireplace_OBJ.foreground = None

    jump end_snape_hangout_no_points

label ball_quest_E3:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="mid", ypos="base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her @ tears soft "My parents sent me the wrong dress!" ("angry", "base", "base", "mid", xpos="right", ypos="base")
    gen "Are You kidding me!?" ("base", xpos="far_left", ypos="head")
    her @ tears soft "They sent me the dress I wore to the ball last year..." ("angry", "base", "base", "mid")
    gen "Those inconsiderate bastards!" ("base", xpos="far_left", ypos="head")
    her @ tears soft "Are you making fun of me [name_genie_hermione]?" ("mad", "base", "worried", "mid")
    gen "Can you blame me?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "I will become the laughingstock of Hogwarts! *Sob*!" ("clench", "base", "worried", "mid")
    her @ cheeks blush tears crying "My reputation is as good as ruined! *Sob*!" ("angry", "narrow", "base", "dead")
    gen "Seriously? After all the favours you've sold me, you care about a thing like this?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears crying "Wearing the same dress to the \"Autumn Ball\" for two years in a row would be more humiliating than any favour I sold you so far, [name_genie_hermione]." ("shock", "narrow", "base", "down")
    with hpunch
    gen "You've gotta be kidding me..." ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "Oh, you wouldn't understand..." ("angry", "squint", "base", "mid")
    her @ cheeks blush tears messy "You're just like my father!" ("scream", "base", "angry", "mid")
    gen "I beg your pardon?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "I mean... *Ehm*..." ("open", "wide", "worried", "stare")
    her "Forgive me [name_genie_hermione]..."
    her @ cheeks blush tears crying "I don't know why I am telling you all of this..." ("shock", "narrow", "base", "down")
    gen "................" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears crying "......................*sob*!" ("angry", "narrow", "base", "dead")
    her @ cheeks blush tears messy "I think I'd better go now...*sob*" ("angry", "squint", "base", "mid")
    gen "Well, don't let me keep you a moment longer, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

    call her_walk("door", "base")
    pause.3

    her @ cheeks blush tears messy "(My life is ruined...)" ("angry", "squint", "base", "mid", flip=True)
    pause.1

    call her_chibi("leave")

    call bld
    gen "*Hmm*... I don't remember ever seeing the girl this desperate..." ("base", xpos="far_left", ypos="head")
    gen "And that says a lot, all things considered..." ("base", xpos="far_left", ypos="head")
    gen "I suppose Whoring herself out for house points is a significantly smaller problem than not having a proper prom dress..." ("base", xpos="far_left", ypos="head")
    gen ".............." ("base", xpos="far_left", ypos="head")
    gen "Schoolgirls..." ("base", xpos="far_left", ypos="head")

    $ states.her.busy = True
    $ hg_event_pause += 1
    $ states.her.mood += 5

    $ states.her.ev.yule_ball.e3_complete = True

    jump end_hermione_event


label ball_quest_E4:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="mid", ypos="base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    call bld
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Sorry to disturb you [name_genie_hermione]..." ("open", "base", "worried", "mid", xpos="right", ypos="base")
    her "I came to apologise for my..." ("open", "base", "worried", "R")
    her "... My hysterical behaviour the other day."
    gen "Sure thing, don't worry about it." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]." ("open", "base", "base", "mid")
    her "Still, I cannot help but feel awful for causing a scene..." ("open", "closed", "angry", "mid")
    gen "So the issue has been resolved then?" ("base", xpos="far_left", ypos="head")
    her "Not really..." ("open", "base", "worried", "mid")
    her "Not at all actually..." ("annoyed", "narrow", "angry", "R")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    her "But it is not really a big deal..." ("annoyed", "narrow", "worried", "down")
    her "I'm just overreacting..."

    play music "music/Despair_by_erenik.ogg" fadein 1 if_changed
    her "I won't be able to attend the ball this year... so what?" ("annoyed", "narrow", "worried", "down")
    her "I spent countless hours organising the event..." ("normal", "happyCl", "worried", "mid")
    her @ tears soft "I worked so hard... And..." ("open", "base", "worried", "mid")
    her @ cheeks blush tears soft "And now I will not even be able to...{w=0.3} To...{w=0.4} *Sob*!" ("shock", "base", "base", "R")
    her @ cheeks blush tears crying "To... *SOB*!" ("shock", "narrow", "base", "down")
    her @ cheeks blush tears messy "Excuse me [name_genie_hermione]!" ("angry", "squint", "base", "mid")
    hide hermione_main
    hide screen bld1
    with d3
    call gen_chibi("sit_behind_desk")
    with d1

    call her_walk(action="run", xpos="door", speed=2, reduce=True)
    call her_chibi("leave")

    gen "......................................." ("base", xpos="far_left", ypos="head")
    gen "(*Hmm*...)" ("base", xpos="far_left", ypos="head")

    if clothing_store_intro_done:
        gen "(Maybe I should pay Madam Mafkin a visit and ask for a dress...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "(Maybe I should look around the castle and see if I can procure a dress for her.)" ("base", xpos="far_left", ypos="head")

    $ states.her.busy = True
    $ hg_event_pause += 1
    $ states.her.mood += 5

    $ states.her.ev.yule_ball.e4_complete = True
    $ her_outfit_ball.price = 1000 # Unlocks it in the store

    jump end_hermione_event

label ball_quest_E5:
    hide hermione_main
    with d5

    stop music fadeout 1.0
    gen "Here... This is for you..." ("base", xpos="far_left", ypos="head")

    call give_reward("You give the ball dress to Hermione...","interface/icons/box_red_1.webp")

    her "*Hmm*...? What is this?" ("base", "base", "base", "mid")
    her "{size=+7}A DRESS?!{/size}" ("angry", "wide", "base", "stare")
    with hpunch
    gen "I thought that you--" ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her @ tears soft "[name_genie_hermione]!" ("angry", "base", "base", "mid")
    gen "What? What happened? Don't tell me it's the wrong colour or something!" ("angry", xpos="far_left", ypos="head")
    her @ tears soft "It's perfect, [name_genie_hermione]...*sob*!" ("angry", "base", "base", "mid")
    her "It's perfect... *Sob*!... I love it."
    gen "You sure don't look like it..." ("base", xpos="far_left", ypos="head")
    her "I am sorry, [name_genie_hermione]... *Sob*!"
    her @ cheeks blush tears soft "I... I am just..." ("clench", "base", "worried", "mid")
    her @ cheeks blush tears crying "I am so happy..." ("shock", "narrow", "base", "down")
    her "Thank you, [name_genie_hermione]. Thank you so much."
    her @ cheeks blush tears messy "I cannot believe that you would do something like that for me..." ("angry", "squint", "base", "mid")
    gen "Well, I did... Now stop crying." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "I can't, [name_genie_hermione]. I am so happy and so grateful..." ("scream", "happyCl", "worried", "mid")
    her @ cheeks blush tears messy "Do you want me to suck your cock, [name_genie_hermione]?" ("open", "wide", "worried", "stare")
    gen "What?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "Because I will do it!" ("open", "wide", "worried", "stare")
    her "And I will swallow and everything!"
    her @ cheeks blush tears crying "And you wouldn't have to pay me a single house point!" ("shock", "narrow", "base", "down")
    gen "*Uhm*... Maybe some other time..." ("base", xpos="far_left", ypos="head")
    gen "This is not the type of crying I find arousing..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "I'm sorry, [name_genie_hermione]. I'm such a mess..." ("angry", "squint", "base", "mid")
    her @ cheeks blush tears crying "But this is so unexpected..." ("shock", "narrow", "base", "down")
    her "You made me so happy, [name_genie_hermione]... *sob*!"
    her @ cheeks blush tears messy "Thank you [name_genie_hermione]! *SOB*! Thank you! *SOB*!" ("angry", "squint", "base", "mid")
    gen "Well... *Err*... There, there..." ("base", xpos="far_left", ypos="head")
    gen "Better stop crying before you stain that new dress of yours..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "My new dress! *SOB*!" ("scream", "happyCl", "worried", "mid")
    gen "Alright, you know what? Just get out of my office." ("base", xpos="far_left", ypos="head")
    gen "Just take your dress and leave." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "Of course... I am sorry, [name_genie_hermione]!" ("angry", "squint", "base", "mid")
    hide hermione_main
    hide screen bld1
    with d3
    pause.1

    call her_chibi("stand","mid","base")
    pause.3
    call her_chibi("stand","mid","base",flip=True)
    pause.2

    call her_walk(action="leave")

    call bld
    gen "......................" ("base", xpos="far_left", ypos="head")
    gen "Women..." ("base", xpos="far_left", ypos="head")

    $ hg_event_pause += 2

    $ states.her.ev.yule_ball.gave_dress = True
    $ ball_outfit_ITEM.used = True

    jump end_hermione_event
