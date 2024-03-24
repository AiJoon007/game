

### Hermione Handjob ###

label start_hg_pf_handjob:

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her for a handjob?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 45
    return

label hg_pf_handjob_fail:
    jump end_hermione_event

label end_hg_pf_handjob:

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
        her "" ("annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        her "" ("soft", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Points
    if states.her.tier <= 5:
        gen "Here you go, [name_hermione_genie]... {number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
        gen "You may leave now." ("base", xpos="far_left", ypos="head")
        $ gryffindor += current_payout
    else:
        gen "You may leave now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    her "Thank you, [name_genie_hermione]..." ("soft", "squint", "base", "R")

    # Hermione leaves
    call her_walk(action="leave")

    # Increase level
    if states.her.tier == 4:
        if states.her.level < 18: # Points til 18
            $ states.her.level += 1
    if states.her.tier == 5:
        if states.her.level < 21: # Points til 21
            $ states.her.level += 1

    jump end_hermione_event

### Fail Events ###

label hg_pf_handjob_T1_E1:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "How about you put your dainty little hands on my cock..." ("base", xpos="far_left", ypos="head")
    gen "And give it a rub." ("base", xpos="far_left", ypos="head")
    her "!!!" ("shock", "wide", "base", "stare")
    gen "[name_genie_hermione]?" ("base", xpos="far_left", ypos="head")
    gen "Hello?"
    her "*Gulp*" ("angry", "closed", "base", "mid")
    her "I'm sorry, [name_genie_hermione]... But I believe I must've misheard you." ("open", "closed", "base", "mid")
    her "I'm sure you didn't just request what I think you did." ("base", "base", "base", "mid")
    her "If you could please repeat your request, I'm sure we can work something out." ("base", "base", "base", "mid")
    gen "Oh, of course..." ("base", xpos="far_left", ypos="head")
    gen "One handjob please." ("base", xpos="far_left", ypos="head")
    her "!!!" ("shock", "wide", "base", "stare")
    her "I think I better leave." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(*Hmm*... Perhaps she's worried that her hand isn't big enough...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 10

    jump hg_pf_handjob_fail

label hg_pf_handjob_T2_E1:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Today, I require you to give me a hand--" ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]! Gryffindor could really do with some points right now!" ("base", "base", "base", "mid")
    gen "I appreciate the enthusiasm, but I wasn't done speaking..." ("base", xpos="far_left", ypos="head")
    her "Sorry, [name_genie_hermione]... What would you like me to give you a hand with?" ("angry", "base", "base", "mid")
    gen "I'd like you to use your hands... To rub my cock." ("base", xpos="far_left", ypos="head")
    her "Rub your--" ("shock", "wide", "base", "stare")
    gen "That's right..." ("base", xpos="far_left", ypos="head")
    gen "I'll be sure to award Gryffindor--" ("base", xpos="far_left", ypos="head")
    her "I think I better leave." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(Did she not just say that she needed the points?)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 8

    jump hg_pf_handjob_fail

label hg_pf_handjob_T3_E1:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "For today's favour... I need you to rub my cock." ("base", xpos="far_left", ypos="head")
    her "Your...{w=0.4} Cock!?!" ("angry", "base", "worried", "mid")
    gen "That's right..." ("base", xpos="far_left", ypos="head")
    her "You must be referring to your Phoenix, right?" ("angry", "base", "base", "mid")
    gen "If that's what you want to call my penis, sure!" ("base", xpos="far_left", ypos="head")
    her "That's not--{w=0.2} I think, I better leave..." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(*Hmm*... She must've gone to fetch some lubricant...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 6

    jump hg_pf_handjob_fail

### Tier 4 ###

# Event 1 (i) - Hermione wants 100 house points for it!
# Event 2 (i) - Reluctantly does it again.
# Event 3 (r) -

label hg_pf_handjob_T4_intro_E1:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Do you know what a \"handjob\" is?" ("base", xpos="far_left", ypos="head")
    her "Why?" ("annoyed", "narrow", "annoyed", "mid")
    gen "I feel like getting one..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]!" ("angry", "base", "angry", "mid")
    gen "It's just another favour... No big deal, right?" ("base", xpos="far_left", ypos="head")
    her "......" ("disgust", "narrow", "base", "mid_soft")
    her "{size=-7}I want a hundred house points for this...{/size}" ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "What was that?" ("base", xpos="far_left", ypos="head")
    her "I want a hundred house points for this!!!" ("scream", "happyCl", "worried", "mid")
    her "" ("clench", "happyCl", "worried", "mid")
    gen "A hundred house points, *huh*?" ("base", xpos="far_left", ypos="head")
    gen "And you will stroke my cock and everything?" ("base", xpos="far_left", ypos="head")
    her "{size=-7}Yes...{/size}" ("soft", "narrow", "angry", "down")
    gen "Sorry, I couldn't hear you..." ("base", xpos="far_left", ypos="head")
    her "Yes, I said yes! I will stroke your stupid cock, [name_genie_hermione]!" ("scream", "happyCl", "worried", "mid")
    her "" ("upset", "narrow", "angry", "R")

    $ _refused = False

    label .choices:

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"You will get fifteen house points.\"" if not _refused:
            $ _refused = True
            $ states.her.mood += 7
            her "For fifteen house points I suppose I could let you molest me a little, but that is all you'll be getting, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
            her "I will not stoop as low as to sell handjobs for fifteen house points."
            her "That is just insulting, [name_genie_hermione]."

            jump .choices

        "\"You will get forty-five house points.\"":
            $ states.her.mood += 3
            her "....." ("soft", "narrow", "angry", "R")
            her "{number=current_payout} house points...?" ("open", "happy", "worried", "R")
            her "This could put Gryffindor back in the lead..." ("open", "narrow", "worried", "down")
            gen "Is that a \"yes\"?" ("base", xpos="far_left", ypos="head")
            her "That's a yes, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
            gen "Great!" ("base", xpos="far_left", ypos="head")
            pass

        "\"You will get one hundred house points.\"":
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            $ current_payout = 100
            her "{number=current_payout} points?!" ("scream", "wide", "base", "mid")
            her "This will definitely put Gryffindor in the lead!"
            gen "Is that a \"yes\" then?" ("base", xpos="far_left", ypos="head")
            her "Of course!" ("smile", "happyCl", "base", "mid")
            her "If I could earn Gryffindor a hundred house points, then I don't mind touching your... Thing, a little." ("smile", "happyCl", "base", "mid", emote="happy")
            pass

    jump hg_pf_handjob_1

label hg_pf_handjob_T4_intro_E2:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Do you know what a \"handjob\" is?" ("base", xpos="far_left", ypos="head")
    her "You've asked me that already, [name_genie_hermione]." ("disgust", "narrow", "base", "mid_soft")
    gen "Ah, that's right." ("base", xpos="far_left", ypos="head")
    gen "Well, I want you to play with my cock again." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], you are being vulgar again..." ("upset", "closed", "base", "mid")
    gen "Fine, fine." ("base", xpos="far_left", ypos="head")
    gen "[name_hermione_genie], I would like to buy another favour from you today." ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    gen "The favour being, you, handling my penis!" ("grin", xpos="far_left", ypos="head")
    her ".............." ("disgust", "narrow", "base", "mid_soft")
    gen "Oh, come on [name_hermione_genie]... For the honour of Gryffindor?" ("base", xpos="far_left", ypos="head")
    her "............." ("angry", "base", "angry", "mid")
    gen "Play with my cock, for the honour of the Gryffindor house, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
    her "Stop saying that, [name_genie_hermione]..." ("scream", "base", "angry", "mid", emote="angry")
    gen "Come off it [name_hermione_genie], it's not like I'm asking you to do this for free." ("base", xpos="far_left", ypos="head")
    her "" ("normal", "narrow", "angry", "mid")
    gen "I'm sure the Slytherin girls have no issue doing it...{w=0.4} In fact, they're probably being showered in house points as we speak!" ("base", xpos="far_left", ypos="head")
    her "{size=-4}That is not the kind of shower that I'm worried about...{/size}" ("soft", "narrow", "angry", "R")
    gen "What was that?" ("base", xpos="far_left", ypos="head")
    her "Nothing, [name_genie_hermione]..." ("open", "narrow", "angry", "R")
    gen "So, what will it be [name_hermione_genie]? It's all up to you..." ("base", xpos="far_left", ypos="head")
    her "......{w=0.3}{nw}" ("annoyed", "narrow", "angry", "R")
    her "......{fast}...." ("disgust", "narrow", "angry", "down")

    jump hg_pf_handjob_1

label hg_pf_handjob_T4_repeat:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "How would you like to give me another handjob?" ("base", xpos="far_left", ypos="head")

    her "..............." ("upset", "base", "worried", "mid")
    her "Will I be getting paid for it, [name_genie_hermione]?" ("open", "base", "worried", "R")
    gen "Of course. {number=current_payout} points." ("base", xpos="far_left", ypos="head")
    her "...{w} Alright then." ("upset", "narrow", "angry", "R")

    jump hg_pf_handjob_1

### Tier 5 ###

# Event 1 (i) -
# Event 3 (r) -

label hg_pf_handjob_T5_intro_E1:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "You don't mind giving me another handjob, do you?" ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]... I don't mind." ("base", "squint", "base", "mid")
    her @ cheeks blush "I mean... As long as I am getting paid, of course." ("angry", "squint", "base", "stare")
    gen "Well, then... Time to earn those points." ("base", xpos="far_left", ypos="head")

    jump hg_pf_handjob_2

label hg_pf_handjob_T5_intro_E2:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "You don't mind giving me another handjob, do you?" ("base", xpos="far_left", ypos="head")
    her "I suppose I don't, [name_genie_hermione]..." ("soft", "narrow", "worried", "down")
    her "..................." ("clench", "narrow", "base", "down")
    gen "Great, then let's get started..." ("base", xpos="far_left", ypos="head")

    jump hg_pf_handjob_2

label hg_pf_handjob_T5_repeat:

    call start_hg_pf_handjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "I'd like another handjob, if you don't mind." ("base", xpos="far_left", ypos="head")
    her "Certainly, [name_genie_hermione]..." ("base", "base", "base", "R")

    jump hg_pf_handjob_2

### Tier 4 Handjob ###

label hg_pf_handjob_1:
    $ states.her.status.handjob = True
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand",560,"base")
    call gen_chibi("jerk_off",450,"base")

    hide screen blkfade
    with fade
    pause.8

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "..........." ("disgust", "narrow", "worried", "down", xpos="base", ypos="head", flip=False)
    gen "Whenever you're ready, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    if hermione.is_any_worn("robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")

    her "......................." ("disgust", "happyCl", "worried", "mid")
    pause.1

    call her_chibi_scene("hj_pause", trans=d9)
    pause.8

    nar "Hermione puts her slender hands on your cock..."

    gen "Good...{w=0.4} Now stroke it." ("base", xpos="far_left", ypos="head")
    her "Right..." ("angry", "happyCl", "worried", "mid", emote="sweat")

    call her_chibi_scene("hj", trans=d5)
    call ctc

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "Nice..." ("grin", xpos="far_left", ypos="head")

    if not _events_completed_any:
        her "!!!" ("shock", "wide", "base", "stare")
        her "Are you about to finish, [name_genie_hermione]?!" ("mad", "wide", "base", "stare")
        gen "About to finish?" ("base", xpos="far_left", ypos="head")
        gen "Don't be ridiculous [name_hermione_genie], we are just getting started." ("base", xpos="far_left", ypos="head")
        her "Oh..." ("angry", "happyCl", "worried", "mid", emote="sweat")
        her "......" ("angry", "happyCl", "worried", "mid")
        her "You will give me a warning, won't you, [name_genie_hermione]?" ("upset", "wink", "base", "mid")
    else:
        her "[name_genie_hermione]...?" ("angry", "happyCl", "worried", "mid", emote="sweat")
        gen "What is it?" ("base", xpos="far_left", ypos="head")
        her "Will you warn me before...{w=0.4} *Ehm*...{w=0.4} you know..." ("angry", "happyCl", "worried", "mid", emote="sweat")

    $ _promise = False #If TRUE Genie promised to warn her.

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Of course, I'll let you know when it's time.\"":
            $ _promise = True #Genie promised to warn her
            her "Thank you, [name_genie_hermione]." ("normal", "happyCl", "worried", "mid")
        "\"I myself don't always know when...\"":
            her "Really? But I thought..." ("disgust", "squint", "worried", "mid")
            her "Well, never mind then..." ("annoyed", "closed", "worried", "mid")

    her "........" ("open", "squint", "base", "R")
    gen "............." ("base", xpos="far_left", ypos="head")
    her "............." ("normal", "squint", "worried", "mid")
    her "*Ehm*...{w=0.4} [name_genie_hermione]?" ("open", "happy", "worried", "mid")
    gen "Yes, what is it?" ("base", xpos="far_left", ypos="head")
    her "How long do you think this will take?" ("angry", "base", "worried", "mid")
    gen "Why?" ("base", xpos="far_left", ypos="head")

    if game.daytime:
        her "Well, it's just that my classes are about to start..." ("upset", "wink", "base", "mid")
    else:
        her "Well, it's just that I have this paper that I need to finish..." ("upset", "wink", "base", "mid")
        her "It's due tomorrow, and it's getting pretty late..." ("upset", "wink", "base", "mid")

    gen "Then don't you think you should focus more on your task?" ("base", xpos="far_left", ypos="head")
    her "Right, [name_genie_hermione]! I'm sorry..." ("angry", "happyCl", "base", "mid")
    her "I will just keep on stroking it then..." ("angry", "happyCl", "base", "mid")
    gen "That said...{w=0.4} There is something you could do to accelerate the process..." ("base", xpos="far_left", ypos="head")
    her "Really? What is it [name_genie_hermione]?" ("soft", "squint", "base", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Tell me how much of a whore you are!\"":
            her "{size=+4}What?!?{/size}" ("clench", "base", "worried", "stare")
            her "I am not a whore!" ("angry", "base", "angry", "mid")
            menu:
                "\"That is not what I said.\"":
                    her "But, you--" ("disgust", "base", "angry", "mid")
                    gen "You asked me what would accelerate the process, and I gave you an--" ("base", xpos="far_left", ypos="head")
                    her "Hold on... You want me to make things up, and degrade myself?" ("angry", "narrow", "worried", "mid")
                    her "And that's supposed to assist... Calling myself a..." ("disgust", "base", "worried", "mid")
                    gen "That's right [name_hermione_genie]... If you want me to finish quicker, then I need you to degrade yourself." ("base", xpos="far_left", ypos="head")
                    her "..." ("disgust", "narrow", "base", "down")
                    gen "Go on, [name_hermione_genie]...{w=0.4} I'm sure you won't find it that difficult." ("base", xpos="far_left", ypos="head")
                "\"Well, that's up for debate.\"":
                    her "[name_genie_hermione]!" ("angry", "narrow", "angry", "mid")
                    gen "Either way, if you want to accelerate the process..." ("base", xpos="far_left", ypos="head")
                    gen "Then I want you to call yourself a \"whore\", or a \"slut\", you could also throw a \"harlot\" or two in there for good measure." ("base", xpos="far_left", ypos="head")
                    her "So, you want me to make up naughty and degrading things to say about myself?" ("annoyed", "base", "worried", "R")
                    gen "Sure, make things up..." ("base", xpos="far_left", ypos="head")
                "\"{size=-4}Whore says \"what?\"{/size}\"":
                    her "What?" ("angry", "base", "worried", "mid")
                    gen "*Heh-heh*..." ("base", xpos="far_left", ypos="head")
                    her "..." ("disgust", "happy", "base", "stare")
                    her "Why, I never..." ("annoyed", "narrow", "annoyed", "R")
                    gen "Come off it, [name_hermione_genie]... I'm not asking you to speak with honesty." ("base", xpos="far_left", ypos="head")
                    gen "Surely you've heard of dirty talk before..." ("base", xpos="far_left", ypos="head")
                    her "Dirty talk? That's what you want?" ("annoyed", "narrow", "annoyed", "mid")
                    gen "That's right... Just make things up, and have fun with it." ("base", xpos="far_left", ypos="head")
            her "*Hmph*...{w=0.4} Alright then...{w=0.4} I'll do it." ("normal", "narrow", "annoyed", "R")
            her "As long as you promise not to think of me differently, afterwards..." ("open", "closed", "annoyed", "R")
            gen "Certainly, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "Say it [name_genie_hermione], tell me that you promise!" ("angry", "narrow", "annoyed", "mid")
            gen "Alright, alright...{w=0.4} I promise I won't think of you differently." ("base", xpos="far_left", ypos="head")
            gen "(You'll always be a whore in my mind.)" ("base", xpos="far_left", ypos="head")
            her "Alright... Good..." ("base", "closed", "base", "mid")
            call ctc
            her @ cheeks blush "......." ("normal", "closed", "base", "mid")
            her @ cheeks blush "I--{w=0.2} I'm a whore..." ("open", "closed", "base", "mid")
            gen "Go on..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am a big whore..." ("open", "narrow", "annoyed", "down")
            gen "Yes, you are." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I am the biggest whore in the United Kingdom!" ("mad", "squint", "worried", "mid")
            her @ cheeks blush "I try to act innocent, but the truth is, all I think about... is cock!" ("angry", "narrow", "worried", "mid")
            gen "Yes, you do, you little slut!" ("base", xpos="far_left", ypos="head")
            her "Yes, that's right! I am a slut!" ("angry", "squint", "worried", "R")
            her "I crave cock...{w=0.4} {size=-4}All the time!{/size}" ("angry", "closed", "worried", "mid")
            gen "Very nice!" ("base", xpos="far_left", ypos="head")
            gen "But you don't have to be truthful, you can make things up." ("base", xpos="far_left", ypos="head")
            her "What?" ("shock", "wide", "base", "stare")
            her "[name_genie_hermione], those things I said aren't true!" ("disgust", "squint", "annoyed", "mid")
            her "You--{w=0.2} You promised you wouldn't--" ("disgust", "squint", "angry", "mid")
            gen "*He-Heh*... Don't worry [name_hermione_genie], I'm just messing with you." ("grin", xpos="far_left", ypos="head")
            her "[name_genie_hermione]!" ("angry", "narrow", "worried", "mid")
            gen "As a matter of fact, you are doing an excellent job... Keep at it, and we'll be done in no time!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "(*Hmph*... I'd rather finish this now...)" ("disgust", "narrow", "worried", "down")
            her @ cheeks blush "..." ("soft", "narrow", "worried", "down")
            her @ cheeks blush "I--{w=0.2} I love cock..." ("open", "narrow", "worried", "down")
            her @ cheeks blush "And I love...{w=0.4} Spunk..." ("clench", "narrow", "base", "down")
            her @ cheeks blush "And semen... And sperm..." ("clench", "narrow", "base", "down")
            gen "Those are all the same--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I love to drink sperm..." ("clench", "narrow", "base", "down")
            gen "Really?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I want you to feed me your sperm, [name_genie_hermione]!" ("open_tongue", "narrow", "base", "mid_soft")
            gen "You do?!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Or better yet, pump me full of it, [name_genie_hermione]!" ("open_wide_tongue", "happy", "worried", "mid_soft")
            gen "Of course I will!" ("angry", xpos="far_left", ypos="head")

        "\"Stick your tongue out, and look at me!\"":
            her "What?" ("clench", "happy", "base", "mid")
            gen "Just do it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "..." ("soft", "happy", "worried", "mid")
            her "*Ike Is*?" ("open_wide_tongue", "happy", "worried", "mid")
            gen "Yes, very good... Now, keep your tongue just like that, and look into my eyes..." ("base", xpos="far_left", ypos="head")
            her "....................." ("open_wide_tongue", "base", "worried", "mid")
            gen "Yes [name_hermione_genie]... Just like that..." ("base", xpos="far_left", ypos="head")
            her "..........." ("open_wide_tongue", "happy", "worried", "mid")
            her "..........." ("open_wide_tongue", "narrow", "worried", "down")
            her "I can't keep my mouth open for so long, [name_genie_hermione]... Or I'll end up drooling all over myself." ("disgust", "happy", "worried", "mid")
            gen "But I want you to drool all over yourself..." ("base", xpos="far_left", ypos="head")
            her "What? But I will look silly!" ("angry", "base", "worried", "stare")
            gen "That's the point, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her "......." ("disgust", "base", "worried", "mid")
            gen "Go on, [name_hermione_genie], or did you not want to speed things up after all?" ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "angry", "down") #Looks at Genie as if saying "fine"
            gen "Good...{w=0.4} Now, open your mouth, and let me see that tongue..." ("base", xpos="far_left", ypos="head")
            her "............" ("normal", "narrow", "worried", "mid")
            her "A-ha..." ("open_wide_tongue", "narrow", "worried", "mid")
            gen "Excellent..." ("base", xpos="far_left", ypos="head")
            her ".............." ("open_wide_tongue", "happy", "base", "mid")
            gen "Yes... Keep stroking, and drool over my cock." ("base", xpos="far_left", ypos="head")
            her ".................." ("open_wide_tongue", "happy", "worried", "R")
            gen "Oh, your tongue just makes me want to slide my cock into that wet hole of yours!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "................." ("open_wide_tongue", "narrow", "worried", "R")
            gen "No, keep on looking at me [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "....................." ("open_wide_tongue", "base", "worried", "R")
            her @ cheeks blush ".....................{fast}" ("open_wide_tongue", "base", "worried", "mid")
            gen "That's it, you little slut!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "......................" ("open_wide_tongue", "base", "angry", "stare")
            gen "Let me just--{w=0.2} *Ngh*...{w=0.4} Pump that gaping hole full of cum...{w=0.4} Until it overflows, and slides--{w=0.2} Down your neck!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "................" ("open_wide_tongue", "narrow", "angry", "mid")

    gen "But first, give my cock a kiss!" ("base", xpos="far_left", ypos="head")
    her "Excuse me?" ("angry", "base", "angry", "mid")
    gen "You know, just a little kiss, right on the tip." ("base", xpos="far_left", ypos="head")
    her "............." ("angry", "narrow", "angry", "mid")
    her "...{w=0.4} With my lips?" ("angry", "narrow", "annoyed", "down")
    gen "What else would you--" ("base", xpos="far_left", ypos="head")
    her "..." ("angry", "base", "worried", "mid")
    gen "I mean, sure! That will speed things up, I'm telling you!" ("base", xpos="far_left", ypos="head")
    her "*Sigh*.............." ("open", "narrow", "annoyed", "down")
    her "Well, if it will speed things up, I suppose I may as well try it..." ("soft", "narrow", "annoyed", "down")

    nar "Hermione bends forward, and gives the tip of your engorged cock a tender kiss."

    play sound "sounds/kiss.ogg"
    call her_chibi_scene("hj_kiss", trans=kissiris)
    pause 1

    if not states.her.ev.give_me_a_handy.cock_kiss:
        $ states.her.ev.give_me_a_handy.cock_kiss = True
        $ achievements.unlock("herkiss")

        if not states.her.status.public_kissing:
            her "(My first kiss ever, and I gave it away...{w=0.4} To a cock...)" ("soft", "closed", "worried", "down")
        else:
            her "(Our first kiss ever, and I gave it away...{w=0.4} To his cock...)" ("soft", "closed", "worried", "down")

    $ states.her.status.kissing = True
    pause 2

    call her_chibi_scene("hj", trans=d5)
    pause.5

    her "Like that?" ("open", "squint", "worried", "mid")
    gen "Of course I liked that!" ("grin", xpos="far_left", ypos="head")
    her "{size=-5}I was asking if I did it correctly...{/size}" ("angry", "narrow", "worried", "R")
    gen "Sorry?" ("base", xpos="far_left", ypos="head")
    her "Nothing, [name_genie_hermione]..." ("disgust", "narrow", "worried", "mid")
    gen "That wasn't so bad, was it?" ("base", xpos="far_left", ypos="head")
    her "No, I suppose it wasn't..." ("upset", "wink", "base", "mid")
    gen "So, could I ask you to do it again?" ("base", xpos="far_left", ypos="head")
    her "I--{w=0.2} I suppose..." ("normal", "happyCl", "worried", "mid")
    gen "Then please, do it again!" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, alright..." ("base", "narrow", "base", "down")

    play sound "sounds/kiss.ogg"
    call her_chibi_scene("hj_kiss", trans=kissiris)
    pause 3

    nar "Hermione gives your cock another kiss..."
    call ctc

    nar "This time she lingers a moment longer..."
    pause.5

    call her_chibi_scene("hj", trans=d5)
    pause.5

    gen "Good...{w=0.4} Now do it again, and stay there for a while." ("base", xpos="far_left", ypos="head")
    her "Stay there...{w=0.4} With my lips touching--" ("open", "base", "base", "stare")
    her "No, I will look stupid!" ("disgust", "happy", "angry", "R")
    menu:
        "\"That's the point!\"":
            gen "It will make me cum in no time!" ("base", xpos="far_left", ypos="head")
            her "......" ("annoyed", "narrow", "annoyed", "mid")
            gen "Now, don't be so silly, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Just put your lips back, and keep them there for me." ("base", xpos="far_left", ypos="head")
        "\"Nobody is watching...\"":
            her "You are, [name_genie_hermione]." ("angry", "narrow", "worried", "down")
            gen "That's true... And I'm letting you know right now, that if you did this for me, It'd make me cum in no time." ("base", xpos="far_left", ypos="head")
    her "......" ("annoyed", "narrow", "base", "down")
    gen "Go on...{w=0.4} You said you were in a hurry." ("base", xpos="far_left", ypos="head")
    her "..............." ("annoyed", "narrow", "angry", "R")
    if game.daytime:
        gen "Once we're done here, you can get out and head back to class." ("base", xpos="far_left", ypos="head")
    else:
        gen "Once we're done here, you can get back to working on your paper." ("base", xpos="far_left", ypos="head")
    her "............." ("disgust", "narrow", "base", "mid_soft")
    her "Well, alright then..." ("open", "narrow", "worried", "down")
    her "" ("open", "closed", "worried", "down")

    nar "Hermione shuts her eyes, puckers her lips, and bends forward again..."
    nar "A twitch runs down your shaft, as she plants her lips on the tip of your cock..."

    play sound "sounds/kiss.ogg"
    call her_chibi_scene("hj_kiss", trans=kissiris)
    call ctc

    gen "Very good, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Now touch it with your tongue." ("base", xpos="far_left", ypos="head")
    her "??!" ("open_tongue", "happyCl", "worried", "mid")
    gen "That's the last thing I will be asking of you today." ("base", xpos="far_left", ypos="head")
    her "............" ("open_tongue", "closed", "annoyed", "mid")
    her "............{fast}" ("open_wide_tongue", "closed", "worried", "mid")

    nar "You feel Hermione warily rub the tip of her tongue against the head of your cock..."

    gen "Yes...{w=0.4} Just--{w=0.2} *Ngh*...{w=0.4} Just like that..." ("base", xpos="far_left", ypos="head")
    nar "Looking as if she has no clue what to do in this situation, Hermione starts wiggling her tongue a little bit..."
    her "(*Hmm*... It tastes a bit weird...)" ("open_wide_tongue", "closed", "worried", "down")
    her "(Wait, why did I try to taste it?!)" ("open_tongue", "happyCl", "worried", "down")
    gen "Yes... Good job, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

    call her_chibi_scene("hj", trans=d5)
    pause.8

    her "So, did it work? Are you ready to--{w=0.4} *Ehm*...{w=0.4} Finish, [name_genie_hermione]?" ("angry", "narrow", "base", "down")
    gen "{size=-4}(Surprisingly, yes!){/size}" ("angry", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Give her a warning-":
            $ states.her.status.cumshot = True
            gen "Here it comes, [name_hermione_genie]! You better be ready!" ("angry", xpos="far_left", ypos="head")
            her "What? So soon?!" ("shock", "wide", "base", "stare")
            gen "{size=+5}Yeah, you did a great job!!!{/size}" ("angry", xpos="far_left", ypos="head")
            gen "{size=+5}You little whore!!!{/size}" ("angry", xpos="far_left", ypos="head")
            her "No, [name_genie_hermione], wait, I--" ("angry", "base", "base", "stare")
            gen "{size=+5}Too late for that, slut!{/size}" ("angry", xpos="far_left", ypos="head")
            her "*Whimper*" ("angry", "happyCl", "base", "stare")
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")
            her "!!!!!!!!!!!" ("shock", "happyCl", "base", "stare")

            stop music fadeout 1.0
            call her_chibi_scene("hj_cum_in_done", trans=d5)
            pause.5

            call cum_block
            play sound "sounds/slick_01.ogg"
            call her_chibi_scene("hj_cum_in", trans=d5)
            pause.8

            if hermione.is_worn("top"):
                nar "Hermione suddenly slides your already dripping cock under her top..."
            else:
                nar "Hermione suddenly slides your already dripping cock in-between her breasts, placing your tip mere inches from her chin..."
            gen "?!!" ("angry", xpos="far_left", ypos="head")
            nar "The sensation of her warm skin against your cock overwhelms you, and you begin to ejaculate like a mad-man."
            call ctc

            call her_chibi_scene("hj_cum_in_done", trans=d5)

            her "......................." ("angry", "wide", "base", "stare", xpos="right", ypos="base")
            gen "..........................." ("base", xpos="far_left", ypos="head")
            her "......................." ("angry", "wide", "base", "stare")
            gen "....................?" ("base", xpos="far_left", ypos="head")
            her "......................." ("angry", "narrow", "base", "down")
            gen "... What the fuck just happened?" ("base", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "I don't know...{w=0.4} I suppose I just panicked..." ("angry", "happyCl", "worried", "mid", emote="sweat")

            if game.daytime:
                if hermione.is_worn("top"):
                    her "My classes are about to start, and I didn't want to get it on top of my clothes, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
                    gen "So you'd rather go to class--" ("base", xpos="far_left", ypos="head")
                    gen "--With your top all soaked with sperm from the inside?" ("base", xpos="far_left", ypos="head")
                else:
                    her "My classes are about to start, and I didn't want you to ruin my face, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
                    gen "So you'd rather go to class--" ("base", xpos="far_left", ypos="head")
                    gen "--With sperm between your tits?" ("base", xpos="far_left", ypos="head")
                her "What other choice do I have?" ("angry", "narrow", "base", "down")
                her "I can't just skip class..." ("angry", "narrow", "base", "down")
            else:
                her "At this hour, the Gryffindor common room will be full of people..." ("angry", "happyCl", "worried", "mid", emote="sweat")
                her "And I didn't want to have to return there with my face all covered in your...{w=0.4} Spunk, [name_genie_hermione]." ("angry", "narrow", "worried", "mid")
                gen "So you'd rather enter your dorm--" ("base", xpos="far_left", ypos="head")

                if hermione.is_worn("top"):
                    gen "With your top all soaked with sperm from the inside?" ("base", xpos="far_left", ypos="head")
                else:
                    gen "With sperm, stuck between your tits?" ("base", xpos="far_left", ypos="head")

                her "What other choice do I have?" ("angry", "narrow", "base", "down")

            call hide_characters
            show screen blkfade
            with d5

            nar "Hermione releases your still pulsating cock."

            call her_chibi("stand","mid","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blkfade
            with fade
            pause.8

            her "*Eww*...{w=0.4} Your sperm, [name_genie_hermione]..." ("angry", "narrow", "base", "down")
            if hermione.is_worn("top"):
                her "It's sticking to the underside of my top..." ("disgust", "narrow", "base", "down")
            else:
                her "It's made my breasts all sticky..." ("angry", "base", "base", "mid")
            gen "Just put it in your mouth next time." ("base", xpos="far_left", ypos="head")
            her "*Hmph*..." ("disgust", "narrow", "worried", "down")
            her "I really need to go now, so may I have my payment?" ("open", "squint", "worried", "R")

        "-Just start cumming-":
            $ states.her.status.cumshot = True
            with hpunch
            gen "{size=+3}*Argh*!{/size}" ("angry", xpos="far_left", ypos="head")
            her "{size=+3}What?!{/size}" ("shock", "wide", "base", "stare")
            gen "Take this!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            call her_chibi_scene("hj_cum_on", trans=d9)
            pause.8

            call cum_block
            $ hermione.set_cum(face="light")
            call bld
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")
            pause 1.0
            $ hermione.set_cum(breasts="light", body="light")
            her "!!!!!!!!!!!" ("shock", "wide", "base", "stare")

            call her_chibi_scene("hj_cum_on_done", trans=d5)
            call ctc

            her "......................." ("angry", "wide", "base", "stare")
            gen "Finally...{w=0.4} I Feel so much better now..." ("base", xpos="far_left", ypos="head")
            call hide_characters
            show screen blkfade
            with d5

            call her_chibi("stand","mid","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blkfade
            with fade
            pause.8

            her @ tears soft ".................." ("disgust", "narrow", "worried", "down", ypos="base")
            gen "Well, I think that's about it for today [name_hermione_genie], so why don't--" ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]! What have you done?!" ("scream", "happyCl", "worried", "mid", trans=hpunch)
            gen "What?" ("base", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.

            if _promise: # Promised to warn her
                $ states.her.mood += 11

                her "You promised to give me a warning, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
                gen "Oh, that's right...{w=0.4} My bad." ("base", xpos="far_left", ypos="head")
            if hermione.is_worn("top"):
                her "My clothes are ruined!" ("annoyed", "narrow", "angry", "R")
            else:
                her "My face... It's been defiled..." ("annoyed", "narrow", "angry", "R")
            if game.daytime:
                her "How could you do this to me?" ("angry", "narrow", "worried", "down")
                her "Classes are about to start, I can't go out looking like this!" ("open", "narrow", "worried", "down")
                gen "Of course you can." ("base", xpos="far_left", ypos="head")
            else:
                her "Am I supposed to return to the Gryffindor common room, looking like this?!" ("angry", "narrow", "worried", "down")
                gen "Why not? You look great!" ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]!!!" ("annoyed", "narrow", "annoyed", "mid")
            gen "Alright, alright... Just wipe it off or something." ("base", xpos="far_left", ypos="head")
            gen "Nobody will even notice." ("base", xpos="far_left", ypos="head")
            her "...{w=0.4} I would like to get paid now." ("disgust", "narrow", "annoyed", "mid")

    jump end_hg_pf_handjob

### Tier 5 Handjob ###

label hg_pf_handjob_2:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand",560,"base")
    call gen_chibi("jerk_off",450,"base")

    hide screen blkfade
    with fade
    pause.8

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her @ cheeks blush "..........." ("soft", "narrow", "base", "down", xpos="base", ypos="head", flip=False)

    if hermione.is_any_worn("robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")

    her "......................." ("base", "narrow", "base", "down")
    pause.1

    call her_chibi_scene("hj_pause", trans=d9)
    pause.8

    nar "Hermione puts her hands on your cock without so much as a nod from you..."

    her @ cheeks blush "You know... It does fit quite neatly in my hands..." ("base", "narrow", "worried", "down", emote="sweat")

    call her_chibi_scene("hj", trans=d5)
    call ctc

    gen "*Mmm*... Yes, indeed..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Do you like it when I pull on it like this, [name_genie_hermione]?" ("soft", "squint", "base", "mid")
    gen "Certainly... You're doing very well, [name_hermione_genie]..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you [name_genie_hermione]... I suppose practice does make perfect." ("base", "closed", "base", "mid")

    nar "Hermione quickens her pace slightly, while keeping a steady rhythm."

    gen "Yes, just like that..." ("base", xpos="far_left", ypos="head")
    gen "You are getting worryingly good at this..." ("base", xpos="far_left", ypos="head")
    her "Worryingly good, [name_genie_hermione]?" ("angry", "squint", "base", "mid")
    gen "Yes, if you continue on this path, then I'll never be able to get off if I ever have to do it myself." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Truly?" ("soft", "base", "base", "stare")
    gen "Undoubtedly..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, I'm not sure if I'm supposed to feel flattered or worried about that." ("soft", "squint", "base", "R")
    gen "That said... I can't help but notice that your mouth isn't partaking in this..." ("base", xpos="far_left", ypos="head")
    if states.her.status.blowjob:
        her @ cheeks blush "My mouth?" ("soft", "base", "base", "mid")
        her @ cheeks blush "Are you saying that I should suck on it, instead?" ("open", "squint", "base", "R")
        gen "That's not it, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Then what--" ("annoyed", "base", "base", "mid")
    else:
        her "What do you--" ("annoyed", "base", "base", "mid")
    gen "Surely you should know what is required by now..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh! You'd like me to talk dirty, [name_genie_hermione]?" ("angry", "wink", "base", "mid")
    gen "That's right, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Alright, so what would you like me to do?" ("soft", "base", "base", "mid")


    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Tell me what you think of my cock.\"":
            her @ cheeks blush "Your--" ("angry", "happy", "base", "stare")
            her @ cheeks blush "You want me to compliment your penis, [name_genie_hermione]?" ("angry", "wink", "base", "mid", emote="sweat")
            gen "Well, you don't have to, but--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ahem*... Let me be honest with you, [name_genie_hermione]..." ("upset", "closed", "base", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You've got the biggest penis I have ever seen!" ("grin", "closed", "annoyed", "mid")
            gen "Really? Well, perhaps you've not seen that--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm not done yet, [name_genie_hermione]!" ("scream", "closed", "angry", "mid")
            gen "My apologies..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Your penis is so big, it's almost frightening!" ("open", "closed", "annoyed", "down")
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Nevertheless, I have been captivated by it since the first time I saw it." ("angry", "closed", "annoyed", "down")
            gen "... You sure have a way with words, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Please [name_genie_hermione], I have to say this!" ("scream", "closed", "angry", "mid")
            gen "By all means..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I think your magnificent cock is a blessing to this world!" ("scream", "closed", "annoyed", "mid")
            gen "Well, I wouldn't go that--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "From this day forward, it shall be my lifelong goal to erect a statue dedicated to your magnificent phallus in every city!" ("scream", "closed", "base", "mid")
            her "As it would be a disservice to the world if not everyone had the chance to experience the sheer might of your penis!" ("scream", "closed", "angry", "mid")
            gen "Alright [name_hermione_genie], I think I've heard enough..." ("base", xpos="far_left", ypos="head")
            her "And shall a female giant decide to--" ("scream", "closed", "angry", "mid")
            gen "For crying out loud, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
            her "*Huh*?" ("angry", "wink", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "Did I go too far?" ("annoyed", "squint", "base", "mid")
            gen "Yeah, just a bit..." ("base", xpos="far_left", ypos="head")
            her "Sorry..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "No worries... I'll be more careful when I ask you to speak truthfully next time." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "squint", "base", "R") #smirk
            gen "Just keep stroking it for now." ("base", xpos="far_left", ypos="head")
            her "Yes, [name_genie_hermione]..." ("soft", "closed", "annoyed", "up")

            nar "Hermione keeps on stroking your cock in silence."
            nar "Oddly enough, her enthusiasm appears to have increased, and you can tell that she's really trying her best to make you finish."

            gen "Yes... Very good..." ("base", xpos="far_left", ypos="head")

        "\"Call yourself a whore!\"":
            her @ cheeks blush "Call myself a--" ("angry", "base", "base", "stare")
            her @ cheeks blush "Oh, that's right! Degrading myself will allow you to finish quicker?" ("soft", "wink", "base", "mid")
            gen "Most certainly... Although you if you'd rather take your time, then I won't--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That's alright [name_genie_hermione], I don't mind..." ("open", "closed", "base", "mid")
            her @ cheeks blush "I am nothing but a whore, after all!" ("open", "closed", "worried", "mid")
            gen "That's right, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Now, why don't you to repeat after me..." ("base", xpos="far_left", ypos="head")

            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"I am a worthless slut!\"":
                    her @ cheeks blush "Of course, [name_genie_hermione]." ("angry", "closed", "worried", "mid")
                    her @ cheeks blush "I am... A worthless slut." ("soft", "closed", "worried", "up")
                    gen "*Mmm*..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "A dirty, worthless little slut, that's what I am!" ("base", "closed", "worried", "up")
                    gen "Yes! Good! Now--" ("base", xpos="far_left", ypos="head")
                "\"I live to suck cock!\"":
                    her @ cheeks blush "*Ehm*..." ("angry", "wink", "base", "mid")
                    her @ cheeks blush "I live to suck penis--{w=0.2} I mean cock..." ("angry", "narrow", "worried", "R")
                    gen "Really? Then why aren't you begging to suck on this one, right now?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "[name_genie_hermione], I am just repeating what you said..." ("angry", "happy", "base", "mid")
                    gen "Really? I swear, I heard some honesty in your words...." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "...................." ("annoyed", "narrow", "base", "R")
                    gen "Speaking of honesty... I think you're doing an outstanding job with those hands, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                "\"I love to swallow my headmaster's cum!\"":
                    her @ cheeks blush "I...{w} I love to swallow my--{w=0.2} *Ehm*...{w=0.2} headmaster's cum." ("angry", "closed", "base", "mid")
                    gen "You hesitated there for a moment." ("base", xpos="far_left", ypos="head")
                    if not states.her.status.gokkun:
                        her @ cheeks blush "Well, I haven't really swallowed..." ("angry", "wink", "base", "mid")
                        her @ cheeks blush "*Ahem*..." ("angry", "wink", "base", "mid")
                    else:
                        her @ cheeks blush "Yes, I know..." ("angry", "narrow", "base", "down")
                    her @ cheeks blush "Let me try again..." ("open", "closed", "worried", "mid")
                    her @ cheeks blush "I love to swallow my headmaster's cum!" ("grin", "squint", "worried", "mid")
                    her @ cheeks blush "It is truly the best cum in the world!" ("smile", "narrow", "base", "down")
                    her @ cheeks blush "And I can't get enough of it!" ("smile", "closed", "base", "mid")
                    her @ cheeks blush "..................................." ("grin", "narrow", "base", "dead")
                    her @ cheeks blush "*Ahem*...{w=0.4} How was that, [name_genie_hermione]?" ("soft", "squint", "base", "mid")
                    gen "Perfect... Now just--" ("base", xpos="far_left", ypos="head")

        "\"Tell me how you got so good at giving handjobs.\"":
            her @ cheeks blush "Oh...{w=0.4} Well, I recently overheard a discussion between a group of female students." ("open", "closed", "base", "R")
            gen "A discussion about handjobs?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That's right..." ("soft", "happy", "base", "mid")
            gen "Interesting... You'd think that students wouldn't be discussing such things out in the open... Especially in your presence." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes, I was certainly surprised when I heard--" ("angry", "squint", "base", "R", emote="happy")
            her @ cheeks blush "Wait, what did you mean by that?" ("disgust", "narrow", "angry", "mid")
            gen "Nothing..." ("base", xpos="far_left", ypos="head")
            gen "So, about these students... What was it that you overheard, exactly?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "They were talking about all the handjobs they have given, obviously..." ("open", "closed", "annoyed", "R")
            gen "Really... That's very interesting..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Most of their techniques were already familiar to me, of course... The ones I didn't know sounded unlikely to have any real effect." ("open", "closed", "base", "mid")
            gen "(Is she trying to undermine these students?...)" ("base", xpos="far_left", ypos="head")
            her "So, since you were wondering... The reason why I got so good, is because after hearing their awful techniques, I started coming up with my own--" ("open", "closed", "base", "mid")
            gen "If you're so confident, then why don't we find out if what you overheard is as infective as you think..." ("base", xpos="far_left", ypos="head")
            her "Oh... Well, I suppose..." ("soft", "narrow", "annoyed", "R")
            her "From what I can vaguely remember... You would just need to adjust your grip slightly, like this..." ("open", "narrow", "angry", "down")
            her "And then you--" ("soft", "narrow", "annoyed", "down")
            gen "*Ngh*--{w=0.2} Holy mother of--{w=0.2} That feels incredible!" ("angry", xpos="far_left", ypos="head")
            her "Really? It actually works?!" ("mad", "base", "worried", "down")
            her "*Hmph*... I suppose if anyone has practised giving handjobs enough, it'd be those Slytherin--" ("angry", "narrow", "annoyed", "down")
            gen "What did you just say?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, *Ehm*...{w=0.4} Did I not mention that they were Slytherin students?" ("angry", "squint", "worried", "R")
            gen "You did not." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ahem*...{w=0.4} Well, I guess it wasn't really that important..." ("open", "closed", "base", "R")
            gen "I'd beg to differ... I'd like a list of their names, if you don't--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You can also shift your pressure across each finger, and that's supposed to feel really good!" ("angry", "squint", "base", "stare")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course! I came up with that one myself, not some Slytherin Harlot!" ("grin", "squint", "worried", "mid")
            gen "I see... Go on, then..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, you actually want me to--" ("angry", "squint", "worried", "stare")
            her @ cheeks blush "I mean... Alright then!" ("grin", "squint", "worried", "mid")

            nar "Hermione shifts the pressure from one side of each hand, to the other..."
            nar "It doesn't make much difference..."

            gen "*Hmm*... I don't feel anything..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Really?" ("disgust", "squint", "base", "mid")
            her @ cheeks blush "Oh! Silly me, I need to do it continuously! That's why!" ("grin", "happyCl", "worried", "down")

            nar "Hermione shifts the pressure back and forth repeatedly... You still can't really tell much difference..."
            her @ cheeks blush "Is it working-- I mean, it feels good, right?" ("mad", "squint", "base", "mid")

            gen "*Err*... Yeah, of course!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Really? I mean--{w=0.2} That's good!" ("smile", "happyCl", "base", "mid", emote="happy")
            her @ cheeks blush "What if I go a bit faster, and then--" ("smile", "narrow", "base", "down")
            gen "[name_hermione_genie], you are killing me!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Really? Really?!" ("smile", "happyCl", "base", "mid", emote="happy")
            her @ cheeks blush "(I guess I'm better at this than I thought!)" ("smile", "happyCl", "base", "mid", emote="happy")
            gen "*Ah*... Yes... You just keep massaging that spot..." ("grin", xpos="far_left", ypos="head")
            gen "Make your house proud..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, yes! For my house, of course!" ("smile", "happyCl", "worried", "down")

    gen "Keep stroking it--{w=0.2} *Ngh*...{w=0.4} Just like that, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush ".............." ("base", "narrow", "base", "down")

    if not _events_completed_any:
        jump hg_pf_handjob_2_cumming
    else:
        jump hg_pf_handjob_2_continue


label hg_pf_handjob_2_continue:
    call her_chibi_scene("hj", trans=d5)
    call ctc

    gen "Now I want you to say..." ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-4}\"I fantasise about being touched by my father.\"{/size}":
            $ states.her.mood += 11
            her "I do not!" ("angry", "base", "angry", "mid")
            gen "I know... Just say it." ("base", xpos="far_left", ypos="head")
            her "How could I say something like that about my own father? That's disgusting, [name_genie_hermione]!" ("angry", "narrow", "annoyed", "mid", emote="angry")
            gen "Humour me." ("base", xpos="far_left", ypos="head")
            her "..........." ("annoyed", "narrow", "annoyed", "mid")
            her "Fine... If I really have to..." ("open", "closed", "annoyed", "down")
            gen "Go on..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("disgust", "closed", "annoyed", "down")
            her @ cheeks blush "Sometimes I--{w=0.2} *Ugh*...{w=0.4} Fantasise about my father..." ("open", "closed", "annoyed", "down")
            her @ cheeks blush "......." ("normal", "closed", "worried", "down")
            gen "I see... And in those fantasies of yours..." ("base", xpos="far_left", ypos="head")
            gen "He is touching you, right?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Touching--" ("angry", "wide", "base", "stare")
            gen "Yes... You're enjoying the thought of it, aren't you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "No! If that happened, I'd cry and beg for him to stop!" ("angry", "happyCl", "base", "down")
            gen "Very well, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "That wasn't so hard, was it--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'd scream for my mommy, even though I know she is still at work..." ("angry", "closed", "worried", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Then my daddy would bring me to my room..." ("soft", "closed", "base", "mid")
            her @ cheeks blush "And throw me on my bed..." ("normal", "closed", "worried", "mid")
            her @ cheeks blush "I'd cry-- \"No, daddy, please, I'm still a virgin\"!" ("scream", "happyCl", "worried", "mid")

            call her_chibi_scene("hj_pause", trans=d5)
            pause.5

            her "But he wouldn't listen, and he'd rip my panties off!" ("grin", "narrow", "base", "dead")
            her "I'd beg him to stop! I'd scream, and I'd cry!" ("angry", "narrow", "base", "dead")
            gen "*Err*... [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("angry", "base", "base", "stare")
            gen "You stopped stroking my cock a while ago..." ("base", xpos="far_left", ypos="head")
            her "Oh, I'm sorry, [name_genie_hermione]." ("grin", "happyCl", "worried", "mid", emote="sweat")
            her "I just got so focused on the story..." ("grin", "happyCl", "worried", "mid", emote="sweat")

            call her_chibi_scene("hj", trans=d5)
            pause.5

            her "I hope you enjoyed my little fabrication!" ("base", "squint", "worried", "mid")
            her "I never have fantasies like that myself, of course!" ("open", "closed", "base", "mid")
            gen "Right." ("base", xpos="far_left", ypos="head")

        "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
            her "What?!" ("angry", "wide", "base", "stare")
            her "That's disgusting!" ("annoyed", "squint", "annoyed", "mid")
            her "Dogs carry {size=+5}STD{/size}s, [name_genie_hermione]." ("open", "closed", "base", "mid")
            gen "Actually, human and canine {size=+5}STD{/size}s are species-specific..." ("base", xpos="far_left", ypos="head")
            gen "Meaning... They can only be spread to the same species." ("base", xpos="far_left", ypos="head")
            gen "Surely you would know this... It's basic biology." ("base", xpos="far_left", ypos="head")
            her "I... I mean, if it's basic knowledge...{size=-6} Then I suppose I did know that...{/size}" ("angry", "squint", "base", "R")
            gen "Then surely you must also know that many women enjoy getting \"knotted\" ?" ("base", xpos="far_left", ypos="head")
            her "Is this also basic biology?" ("normal", "squint", "worried", "mid")
            gen "*Err*... Sure is..." ("base", xpos="far_left", ypos="head")
            her "Then how come I've never heard of this \"getting knotted\" thing?" ("annoyed", "narrow", "worried", "mid")
            gen "*Ehm*... Well..." ("base", xpos="far_left", ypos="head")
            gen "You know what... It doesn't matter." ("base", xpos="far_left", ypos="head")
            gen "Just say the thing!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine..." ("annoyed", "narrow", "annoyed", "mid")
            her @ cheeks blush "Sometimes I get lonely... And let my dog... m--{w=0.2} mount me." ("angry", "narrow", "base", "mid")
            gen "That sounded so fake..." ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("hj_pause", trans=d5)
            pause.5

            her "Because I don't even own a dog!" ("annoyed", "squint", "angry", "mid")

            gen "Fine, whatever, let's just move on..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "squint", "angry", "R")

            call her_chibi_scene("hj", trans=d5)
            pause.5


        "{size=-4}\"-Manual user input-\"{/size}" if not renpy.android:

            # The phrase in the brackets is the text that the game will display to prompt
            # the player to enter the name they've chosen.

            $ tmp_name = renpy.input("(Use keyboard to enter the phrase.)")
            $ tmp_name = tmp_name.strip()

            # The .strip() instruction removes any extra spaces the player may have typed by accident.
            #  If the player can't be bothered to choose a name, then we
            #  choose a suitable one for them:
            if tmp_name == "":
                $ tmp_name="I'm a whore"
                gen "(...)" ("base", xpos="far_left", ypos="head")
                her "I could just call myself a \"whore\"..." ("annoyed", "base", "worried", "R")
                gen "Yes. A great suggestion." ("base", xpos="far_left", ypos="head")
                her "..............." ("annoyed", "base", "base", "R")
                her "[tmp_name]." ("base", "base", "base", "mid")
                gen "A bit louder..." ("base", xpos="far_left", ypos="head")
                her "[tmp_name]!!!" ("scream", "closed", "angry", "mid")
            else:
                random:
                    block:
                        her "I don't want to say that..." ("annoyed", "base", "worried", "R")
                        gen "Oh, just do it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                        her "..........." ("annoyed", "base", "worried", "R")
                        her "[tmp_name]." ("scream", "closed", "angry", "mid")
                    block:
                        her "*Huh*?" ("annoyed", "base", "worried", "R")
                        her "What does that have to do with anything?" ("annoyed", "base", "worried", "R")
                        gen "Just say it." ("base", xpos="far_left", ypos="head")
                        her "......" ("annoyed", "base", "worried", "R")
                        gen "Come on, humour me." ("base", xpos="far_left", ypos="head")
                        her "[tmp_name]." ("scream", "closed", "angry", "mid")
                    block:
                        her "..........." ("annoyed", "base", "worried", "R")
                        her "Do I really have to?" ("annoyed", "base", "worried", "R")
                        gen "Just say it." ("base", xpos="far_left", ypos="head")
                        her "[tmp_name]." ("scream", "closed", "angry", "mid")
            gen "*He-he*..." ("grin", xpos="far_left", ypos="head")

        "{size=-4}\"-Manual user input-\"{/size}" if renpy.android:

            random:
                block:
                    her "I don't want to say that..." ("annoyed", "base", "worried", "R")
                    gen "Oh, just do it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    her "..........." ("annoyed", "base", "worried", "R")
                    her "Manual user input..." ("scream", "closed", "angry", "mid")
                block:
                    her "*Huh*?" ("annoyed", "base", "worried", "R")
                    her "What does That have to do with anything?" ("annoyed", "base", "worried", "R")
                    gen "Just say it." ("base", xpos="far_left", ypos="head")
                    her "......" ("annoyed", "base", "worried", "R")
                    gen "Come on, humour me." ("base", xpos="far_left", ypos="head")
                    her "... Manual user input." ("scream", "closed", "angry", "mid")
                block:
                    her "..........." ("annoyed", "base", "worried", "R")
                    her "Do I really have to?" ("annoyed", "base", "worried", "R")
                    gen "Just say it." ("base", xpos="far_left", ypos="head")
                    her "Manual user input." ("scream", "closed", "angry", "mid")
            gen "*He-heh*..." ("grin", xpos="far_left", ypos="head")

    jump hg_pf_handjob_2_cumming

label hg_pf_handjob_2_cumming:
    call her_chibi_scene("hj", trans=d5)
    pause.8

    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "I love that thing you're doing with the palm of your hand..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You noticed...?" ("soft", "squint", "base", "mid")
    her @ cheeks blush "Then I suppose I better do it some more..." ("base", "narrow", "base", "down")

    nar "Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently..."
    gen "Oh, yes!!!" ("grin", xpos="far_left", ypos="head")

    stop music fadeout 1.0
    gen "{size=-5}(I think this is it!){/size}" ("grin", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"-Warn her!-\"":
            gen "I think I'm about to--" ("angry", xpos="far_left", ypos="head")
            call her_chibi_scene("hj_cum_in_done", trans=d5)
            pause.8

            if hermione.is_worn("top"):
                nar "Hermione swiftly pulls her top up..."
                nar "She then pushes your already dribbling cock against her belly and covers it up, placing your cock a bit higher than you would have expected..."
            else:
                nar "She pushes your already dribbling cock against her belly, placing your cock a bit higher than you would have expected..."
            nar "You can feel her incredibly soft tits rubbing against the tip of your cock..."

            call cum_block
            $ hermione.set_cum(breasts="light")
            call her_chibi_scene("hj_cum_in", trans=d5)
            pause.8

            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "!!!!!!!!!!!" ("grin", "happyCl", "base", "stare", xpos="right", ypos="base", cheeks="blush", flip=False)
            call ctc

            call cum_block
            $ hermione.set_cum(body="light")
            gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")
            nar "The sensation of her skin against your engorged cock almost makes you light-headed..."
            her "Yes, [name_genie_hermione]! Just let it out!" ("grin", "narrow", "worried", "down")
            gen "*Argh*! You got it, you fucking slut!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            call her_chibi_scene("hj_cum_in", trans=d5)
            pause.8
            $ hermione.set_cum(breasts="heavy")

            her "Ah!! It's so hot!" ("soft", "closed", "base", "mid_soft")
            her "And it's getting everywhere! There's so much of it!" ("soft", "closed", "worried", "up")
            gen "*Argh*!!!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            call her_chibi_scene("hj_cum_in", trans=d5)
            pause.8
            $ hermione.set_cum(body="heavy")

            call her_chibi_scene("hj_cum_in_done", trans=d5)
            pause.8

            gen "*Ah*... That... That was great..." ("base", xpos="far_left", ypos="head")
            her "You've finished, [name_genie_hermione]?" ("soft", "wink", "base", "mid")
            gen "Yes...{w=0.4} *Ngh*--{w=0.2} Yes, I believe so..." ("base", xpos="far_left", ypos="head")
            her "Alright..." ("base", "squint", "worried", "R")
            her ".............." ("base", "narrow", "worried", "down")
            call ctc

            call hide_characters
            show screen blkfade
            with d5

            nar "Hermione lets go of your still pulsating cock, and you go to sit back down at your desk."

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blkfade
            with fade
            pause.8

            if game.daytime:
                her "Well, I think I'd better go now...{w=0.4} My classes are about to start." ("open", "base", "base", "R", xpos="right", ypos="base")
            else:
                her "Well, I think I'd better go now...{w=0.4} It's getting late." ("open", "base", "base", "R", xpos="right", ypos="base")

            if hermione.is_worn("top"):
                gen "Will you be alright in those clothes?" ("base", xpos="far_left", ypos="head")
            else:
                gen "Will you be alright with this much cum on you?" ("base", xpos="far_left", ypos="head")
            her "What?" ("angry", "narrow", "base", "down")
            her @ cheeks blush "Oh... Well, I suppose I better clean myself a little bit first..." ("angry", "closed", "base", "R")
            gen "*Hmm*... You know... You could just put it in your mouth and swallow next time..." ("base", xpos="far_left", ypos="head")
            if hermione.is_worn("top"):
                gen "That would surely keep your clothes clean." ("base", xpos="far_left", ypos="head")
            else:
                gen "That would surely avoid making such a mess." ("base", xpos="far_left", ypos="head")

            if not states.her.status.gokkun: #Hasn't swallowed.
                her "With all due respect [name_genie_hermione]..." ("open", "closed", "base", "mid")
                her "I believe that isn't a part of this type of favour..." ("base", "wink", "base", "mid")
                her "Speaking of which... May I receive my payment now, please?" ("base", "base", "base", "mid")
            else:
                her "Maybe next time..." ("base", "narrow", "base", "down")
                her "May I receive my payment now, please?" ("base", "closed", "base", "mid", cheeks="none")
            gen "Of course..." ("base", xpos="far_left", ypos="head")

        "\"-Too late, ejaculate!-\"":
            gen "Take this, whore!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            $ hermione.set_cum(face="light")
            call her_chibi_scene("hj_cum_on", trans=d5)
            pause.8
            gen "*ARGH*!" ("angry", xpos="far_left", ypos="head")
            $ hermione.set_cum(breasts="light", body="light")

            her "WHAT?!" ("shock", "wide", "base", "stare", xpos="right", ypos="base", cheeks="blush", flip=False)
            gen "Take this!" ("angry", xpos="far_left", ypos="head")

            call cum_block
            $ hermione.set_cum(breasts="heavy")
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "!!!!!!!!!!!" ("angry", "happyCl", "base", "stare")
            hide screen bld1
            call ctc

            her "......................." ("angry", "narrow", "base", "down")

            call her_chibi_scene("hj_cum_on_done", trans=d5)
            pause.8

            gen "*Ah*... Much better..." ("base", xpos="far_left", ypos="head")

            her @ cheeks blush ".............." ("base", "narrow", "worried", "down")
            call ctc

            call hide_characters
            show screen blkfade
            with d5

            nar "Hermione lets go of your still pulsating cock, and you go to sit back down at your desk."

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")
            hide screen bld1
            hide screen blkfade
            with fade
            pause.8

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            her "[name_genie_hermione]! Why did you do that?" ("angry", "closed", "worried", "mid") #Not angry
            gen "What?" ("base", xpos="far_left", ypos="head")
            her "You... You came all over me, [name_genie_hermione]..." ("grin", "closed", "worried", "mid")
            her "Such a state you've put me in..." ("base", "closed", "base", "down")
            her "You really should have warned me..." ("base", "narrow", "base", "down")
            gen "It's your fault, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her "My fault?!" ("angry", "base", "base", "mid")
            gen "Yes! The handjob was too good!" ("base", xpos="far_left", ypos="head")
            gen "You made me forget about everything else!" ("base", xpos="far_left", ypos="head")
            her "Oh... That's what you meant..." ("disgust", "narrow", "base", "down")
            her "Well, then I suppose there was nothing that could be done about this mess..." ("angry", "closed", "base", "mid")
            her "I will just wipe it off the best I can before I go, and hope that nobody will notice..." ("grin", "narrow", "base", "dead")
            gen "Don't forget your payment..." ("base", xpos="far_left", ypos="head")
            her "Oh, and my payment! May I receive that, as well?" ("angry", "squint", "base", "mid", cheeks="none")
            gen "Of course, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

        "-Cum in her mouth!-" if states.her.status.gokkun: # Has swallowed cum before.
            gen "Open your mouth, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her "What?!" ("open", "wide", "base", "stare", ypos="head", cheeks="blush", flip=False)
            if hermione.is_worn("top"):
                gen "Open your mouth, or I'll coat your clothes!" ("angry", xpos="far_left", ypos="head")
            else:
                gen "Open your mouth, or I'll coat your tits!" ("angry", xpos="far_left", ypos="head")
            her "....................." ("angry", "squint", "base", "stare")

            call her_chibi_scene("hj_kiss", trans=kissiris)
            pause.8

            nar "Hermione swiftly puts the tip of your cock against her lips..."
            nar "The simple gesture makes your dick practically explode with pleasure, and waves of cum suddenly burst from the tip."

            call cum_block
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "*Gulp!-Gulp!-Gulp*!" ("full", "happyCl", "base", "stare")

            call cum_block
            gen "*Argh*! You little whore!" ("angry", xpos="far_left", ypos="head")
            gen "Yes, you slut! Drink my cum! Drink all of it!" ("angry", xpos="far_left", ypos="head")
            her "*Gulp!-Gulp!-Gulp*!" ("full_cum", "narrow", "worried", "up")
            gen "*Argh*... Yes!" ("angry", xpos="far_left", ypos="head")
            nar "You notice Hermione's eyes rolling back, as she can barely keep up with the sheer amount of cum that your cock is pumping into her mouth."
            her "*Gulp!-Gulp!-Gulp*!" ("full_cum", "narrow", "worried", "up")
            gen "*Ah-ah*..." ("angry", xpos="far_left", ypos="head")
            gen "This feels great..." ("angry", xpos="far_left", ypos="head")
            her "*Gulp*! *Gulp*! *Gulp*!" ("full_cum", "squint", "worried", "ahegao")
            gen "I think that's it, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "You can let go now..." ("base", xpos="far_left", ypos="head")
            gen "... [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

            call her_chibi("stand","desk","base")
            call gen_chibi("sit_behind_desk")

            her "" ("full_cum", "narrow", "base", "dead", xpos="right", ypos="base", trans=fade)
            call ctc

            her "........................................." ("full_cum", "closed", "annoyed", "dead")
            play sound "sounds/gulp.ogg"
            her "*GULP*!!!" ("cum", "happyCl", "worried", "mid")
            her "*Gu-ah-a*..." ("open_wide_tongue", "narrow", "base", "dead")
            her "I swallowed it all, [name_genie_hermione]!" ("grin", "narrow", "base", "dead")
            gen "Good girl..." ("base", xpos="far_left", ypos="head")
            her "Although, at one point I thought I was going to choke..." ("grin", "narrow", "worried", "dead")
            her "There was so much of it..." ("soft", "narrow", "base", "dead")
            gen "Well, the deed is done, and you're perfectly clean." ("base", xpos="far_left", ypos="head")
            her "Yes! I know! It's so much easier this way!" ("grin", "closed", "worried", "down")

            if game.daytime:
                her "I can just go to classes now as if nothing ever happened." ("grin", "squint", "base", "mid")
            else:
                her "I can just go and spend some time with the guys in the common room now and nobody will know..." ("base", "narrow", "worried", "down")

            gen "Yes... With your belly full of semen..." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]!" ("angry", "base", "base", "mid")
            her "... I'll have my payment now, if you please..." ("angry", "squint", "base", "R")
            gen "Of course... Can't keep your classmates waiting..." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "base", "base", "mid", cheeks="none")

    jump end_hg_pf_handjob
