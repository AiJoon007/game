

### Hermione Titjob ###

label start_hg_pf_titjob:

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her for a titjob?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 45
    return

label hg_pf_titjob_fail:
    jump end_hermione_event

label end_hg_pf_titjob:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    $ hermione.set_cum(None)
    $ hermione.wear("all")
    $ hermione.zorder = 15 # Reset sprite zorder (affected by CGs)

    hide cg

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if states.her.mood != 0:
        her "" ("annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    # Points
    if states.her.tier <= 5:
        gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
        $ gryffindor += current_payout
    else:
        gen "You may leave now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    her "Thank you, [name_genie_hermione]..." ("soft", "base", "base", "R")

    if game.daytime:
        her "Classes are about to start..."
    else:
        her "It's getting late..."
    her "I'd better go now..."


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

    jump end_hermione_event

### Fail Events ###

label hg_pf_titjob_T1_E1:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "I noticed how much your tits jiggle when you walk, so I figured they'd be a perfect fit for my cock!" ("base", xpos="far_left", ypos="head")
    her "They'd be, what?!" ("angry", "wide", "worried", "mid")
    gen "A perfect--" ("base", xpos="far_left", ypos="head")
    her "I'm out of here!" ("angry", "happyCl", "angry", "mid")

    call her_walk(action="leave")

    gen "(*Hmm*... Perhaps she thought I wanted to try and fuck her nipple...)" ("base", xpos="far_left", ypos="head")
    gen "(Yes...{w=0.4} That must be it.)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 12

    jump hg_pf_titjob_fail

label hg_pf_titjob_T2_E1:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Get those fat titties out and wrap them around my cock, will you?" ("base", xpos="far_left", ypos="head")
    her "What?! Why would you say something like that?" ("angry", "base", "worried", "mid")
    gen "It's a compliment!" ("base", xpos="far_left", ypos="head")
    her "I'm leaving!" ("angry", "happyCl", "angry", "mid")

    call her_walk(action="leave")

    gen "(Women... Can't even take a compliment these days...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 10

    jump hg_pf_titjob_fail

label hg_pf_titjob_T3_E1:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "How about you get your tits out, and wrap them around my cock?" ("base", xpos="far_left", ypos="head")
    her "You want me to--{w=0.2} What?!" ("angry", "base", "worried", "mid")
    gen "Wrap those titties of yours, around my cock!" ("base", xpos="far_left", ypos="head")
    her "I'm leaving!" ("angry", "happyCl", "angry", "mid")

    call her_walk(action="leave")

    gen "(*Hmm*... Perhaps she's not confident enough that she'll do a good enough job...)" ("base", xpos="far_left", ypos="head")
    gen "(Yes...{w=0.4} That must be it.)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 8

    jump hg_pf_titjob_fail

label hg_pf_titjob_T4_E1:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "How do you feel about giving someone a titjob?" ("base", xpos="far_left", ypos="head")
    her "A what?!" ("angry", "wide", "base", "mid")
    gen "A titjob...{w=0.4} It's when you--" ("base", xpos="far_left", ypos="head")
    her "I'm leaving..." ("angry", "happyCl", "worried", "mid")
    gen "No wait, I was talking about myself, not--" ("base", xpos="far_left", ypos="head")
    her "*Hmph*!" ("annoyed", "happyCl", "angry", "mid")

    call her_walk(action="leave")

    gen "(...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 6

    jump hg_pf_titjob_fail

### Tier 5 ###

# Event 1 (i) - Hermione wants 100 house points for it!
# Event 2 (r) - Reluctantly does it again.

label hg_pf_titjob_T5_intro_E1:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Alright then...{w=0.4} [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Have you ever given someone a \"titjob\"?" ("base", xpos="far_left", ypos="head")
    her "A \"titjob\"?" ("annoyed", "squint", "base", "mid")
    gen "It's when you wrap some {i}fat tits{/i} around a cock..." ("base", xpos="far_left", ypos="head")
    gen "And then shake them up and down, until--" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "base", "mid")
    gen "Is that a yes?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..............." ("disgust", "narrow", "base", "mid_soft")
    her @ cheeks blush "{size=-7}No...{/size}" ("soft", "closed", "worried", "mid", emote="sweat")
    gen "*Hmm*?... What was that?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course I haven't..." ("angry", "narrow", "base", "mid")
    gen "Well then, today is your lucky day!" ("grin", xpos="far_left", ypos="head")
    gen "It's not every day that you get to learn something new." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "It's not? Do I not get taught new things during class every day?" ("annoyed", "squint", "base", "mid")
    gen "I'm talking about things that actually matter." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Right... I suppose I haven't learned the very {i}important{/i} and {i}essential{/i} skills of \"Giving titjobs\" in any of my classes..." ("angry", "narrow", "base", "R")
    gen "Yes, it certainly is a flaw with our education system..." ("base", xpos="far_left", ypos="head")
    gen "You should consider yourself very fortunate to have the opportunity to learn these vital life skills from me." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "If you say so, [name_genie_hermione]..." ("open", "narrow", "base", "down")
    if states.her.status.blowjob:
        gen "You're sounding unsure about this, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Didn't you say you were glad to be able to help your house before giving me a blowjob?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh... Well, that's a bit different..." ("angry", "narrow", "base", "down")
        gen "It is?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well, I was mentally prepared for that, I had never even heard of a titjob before today." ("angry", "closed", "base", "mid")
        gen "So, that's all that it takes?" ("base", xpos="far_left", ypos="head")
        gen "Well then, I suppose I'll give you a moment to consider it..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Thank you, [name_genie_hermione]..." ("angry", "narrow", "base", "down")
        her @ cheeks blush "......" ("angry", "narrow", "base", "down") #Thinking
        her @ cheeks blush "........." ("soft", "narrow", "base", "down")
        her @ cheeks blush "So, I would just need to put your penis in-between my breasts and then move them up and down to stimulate it?" ("open", "wink", "base", "mid")
        gen "Move them up and down, with enthusiasm." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh, of course..." ("angry", "base", "base", "mid")
        gen "Think you could do that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Certainly [name_genie_hermione]... No doubts about it." ("base", "squint", "base", "mid")
    else:
        gen "I'm hearing some uncertainty in your voice... Surely, you don't believe that you're incapable--" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Of course not... I am confident that my breasts are large enough." ("open", "closed", "base", "mid")
    gen "Well then, in that case, I expect nothing but the best from your performance today..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Naturally..." ("open", "closed", "base", "mid")
    gen "And, providing you are doing enough to meet expectations..." ("base", xpos="far_left", ypos="head")


    label back_to_titjob_choices:
    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"I'll give you fifteen house points.\"" if states.her.mood == 0:
            $ states.her.mood += 1
            her "Only--" ("angry", "wide", "angry", "stare")
            her "*Ahem*..." ("angry", "closed", "base", "mid")
            her "I mean... I was expecting a bit more than fifteen points for something like this, [name_genie_hermione]..." ("soft", "squint", "base", "R")
            gen "Then how about twenty? Does that sound fair?" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Well I suppose..." ("annoyed", "base", "base", "down")
            gen "(She doesn't sound too happy about that...)" ("base", xpos="far_left", ypos="head")
            gen "Alright, [name_hermione_genie], forget what I said..." ("base", xpos="far_left", ypos="head")
            jump back_to_titjob_choices

        "\"I'll give you forty-five house points.\"":
            her "{number=current_payout} house points...?" ("open", "wink", "base", "mid")
            her "This could put Gryffindor back in the lead..." ("soft", "narrow", "base", "down")
            gen "So... Is that a yes?" ("base", xpos="far_left", ypos="head")
            her "It's a yes, [name_genie_hermione]..." ("open", "closed", "base", "mid")
            her "{number=current_payout} points sounds like a fair amount for--" ("open", "base", "base", "R")
            gen "For a titjob!" ("grin", xpos="far_left", ypos="head")
            her "(...)" ("base", "narrow", "base", "down")

        "\"I'll give you one hundred house points!\"":
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            $ current_payout = 100
            her "{number=current_payout} house points?!" ("scream", "wide", "base", "stare")
            her "This might be enough to put Gryffindor in the lead!" ("smile", "wide", "base", "stare")
            gen "So... Is that a yes?" ("base", xpos="far_left", ypos="head")
            her "Yes, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid")
            her "I shall do my best..." ("smile", "wink", "base", "mid_soft", emote="happy")

    jump hg_pf_titjob_1

label hg_pf_titjob_T5_repeat:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], would you like to earn some house points today?" ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]..." ("base", "base", "base", "mid")
    her "What would you require me to do?" ("open", "base", "base", "R")
    gen "Nothing you aren't already experienced with!" ("grin", xpos="far_left", ypos="head")
    gen "I'm just going to rub my cock between those precious tits of yours..." ("base", xpos="far_left", ypos="head")
    gen "{number=current_payout} house points, as always..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Very well, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "..............." ("grin", xpos="far_left", ypos="head")

    jump hg_pf_titjob_1

### Tier 6 ###

# Event 1 (i) - Event with a couple of choices.
# Event 2 (i) - Some new interactions.
# Event 3 (r) - Repeat.

label hg_pf_titjob_T6_intro_E1:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("soft", "base", "base", "mid")
    if not states.her.status.titjob:
        gen "Do you know what a \"titjob\" is?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*... Can't say that I've ever heard the term before... But I would assume it's like a handjob or a blowjob, except..." ("soft", "squint", "base", "R")
        gen "Go on..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Except... You'd put the penis in-between your breasts, rather than in your hand or mouth?" ("normal", "happy", "base", "mid")
        gen "That's right..." ("base", xpos="far_left", ypos="head")
        gen "Although, not everyone are lucky enough to be able to provide a titjob..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Really?" ("open", "base", "base", "mid")
        gen "Yes... The tits needs to be plump and big enough for it to work." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh... Right..." ("base", "narrow", "base", "down")
        her @ cheeks blush "Well, I suppose my breasts are big enough..." ("open", "closed", "base", "mid")
        her @ cheeks blush "Alright then... I'll do it, [name_genie_hermione]... I'll give you a titjob..." ("open", "squint", "base", "mid")
        gen "How nice of you to offer, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "What do you--" ("angry", "base", "base", "mid")
        gen "I only asked if you knew what a titjob is... Not if you could give me one." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "But--{w=0.2} You were going to ask, right?" ("angry", "wink", "base", "mid")
        gen "Well, I suppose we'll never know..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "down") #happyCl
        gen "Now, get those big plump titties over here." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes, [name_genie_hermione]..." ("open", "narrow", "base", "down")
    else:
        gen "How do you feel about wrapping those nice tits of yours around my cock again?" ("base", xpos="far_left", ypos="head")
        her "Only nice?" ("upset", "closed", "base", "mid")
        gen "How do you feel about wrapping those {b}perfect{/b} tits of yours around my cock again?" ("base", xpos="far_left", ypos="head")
        her "Alright then, [name_genie_hermione]... Since you're putting it like that..." ("base", "narrow", "base", "mid_soft")

    jump hg_pf_titjob_2

label hg_pf_titjob_T6_intro_E2:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "I would very much like to see those perfect fun-bags of yours again..." ("base", xpos="far_left", ypos="head")
    gen "Wrapped around my cock!" ("grin", xpos="far_left", ypos="head")
    her "Again?" ("base", "narrow", "worried", "down")
    gen "Yes, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "(...)" ("annoyed", "base", "base", "R")
    her "Very well..." ("base", "closed", "base", "mid")
    gen "Splendid!" ("grin", xpos="far_left", ypos="head")

    jump hg_pf_titjob_2

label hg_pf_titjob_T6_repeat:

    call start_hg_pf_titjob

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], what do you think about wrapping those perfect tits of yours around my cock again?" ("base", xpos="far_left", ypos="head")
    her "Sure thing, [name_genie_hermione]..." ("soft", "happy", "base", "R")
    her "{heart}{heart}{heart}" ("base", "closed", "base", "mid")

    jump hg_pf_titjob_2

### Tier 5 Titjob ###

label hg_pf_titjob_1:
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
    her "..........." ("soft", "narrow", "base", "down")
    if not states.her.status.titjob:
        her @ cheeks blush "(It's so big... Am I really going to put this between my--)" ("soft", "narrow", "base", "down")
    gen "Get to it, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Right..." ("angry", "squint", "base", "mid", emote="sweat")
    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        pause 1.0

    if hermione.is_any_worn("top", "bra"):
        her "Just need to--" ("angry", "narrow", "base", "down")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top", "bra")
        pause 1.0
        her "There we go..." ("angry", "narrow", "base", "down")

    if not states.her.status.titjob:
        her "(You can do this, Hermione... You're a Gryffindor!)" ("angry", "narrow", "base", "down")
        her "(Gryffindor students can do anything they put their mind to...)" ("angry", "narrow", "base", "down")
        if states.her.status.blowjob:
            her "(The process surely can't be too dissimilar to that of a blowjob...)" ("angry", "narrow", "base", "down")
            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "Sorry, [name_genie_hermione]! Here I go then!" ("mad", "squint", "base", "mid")

    her "" ("soft", "narrow", "base", "down")
    pause.5

    # Setup
    show her_titjob_personal h5 as cg zorder 17
    $ hermione.zorder = -1
    hide hermione_main

    hide hermione_main
    with d3
    nar "Hermione awkwardly wraps her tits around your cock..."

    call her_chibi_scene("tj_pause", trans=d5)
    call ctc
    #pause.8

    gen "Great...{w=0.4} Now, move your tits up and down along the shaft..." ("base", xpos="far_left", ypos="head")
    her "Alright..." ("angry", "happyCl", "worried", "mid", emote="sweat", ypos="head", flip=False)

    call her_chibi_scene("tj", trans=d5)
    call ctc

    gen "*Mmmm*..." ("grin", xpos="far_left", ypos="head")
    show her_titjob_personal h6 as cg
    her "..." ("soft", "narrow", "base", "down")
    her "Does it...{w=0.4} feel good?" ("base", "happy", "base", "mid")
    gen "Of course not!" ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h8 as cg
    her "..." ("angry", "happy", "base", "mid")
    gen "It feels amazing." ("grin", xpos="far_left", ypos="head")
    show her_titjob_personal h6 as cg
    her "Oh..." ("base", "happy", "base", "mid")
    her "......" ("base", "happy", "base", "mid")
    show her_titjob_personal h10 as cg
    her "Thank you, [name_genie_hermione]." ("base", "base", "base", "R")
    show her_titjob_personal h7 as cg
    her "*Ehm*..." ("annoyed", "narrow", "worried", "down")
    her "[name_genie_hermione]." ("soft", "base", "base", "mid")
    gen "What is it?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Are you planning on finishing in my mouth?" ("soft", "narrow", "base", "up")

    $ _mouth = False #Says he'll cum in mouth.
    $ _tits = False #Says he'll cum between tits.
    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"I certainly was considering it...\"":
            $ _mouth = True
            her @ cheeks blush "I see..." ("open", "closed", "base", "mid")
            if states.her.status.gokkun:
                gen "Will that be a problem?"
                show her_titjob_personal h6 as cg
                her @ cheeks blush "Oh, of course not, [name_genie_hermione]..." ("open", "closed", "base", "mid")
            else:
                show her_titjob_personal h6 as cg
                her @ cheeks blush "(Ejaculate... in my mouth...)" ("base", "narrow", "base", "down")
                her @ cheeks blush "(I suppose it was only a matter of time...)" ("base", "narrow", "base", "down")
        "\"That's what your tits are for, [name_hermione_genie].\"":
            $ _tits = True
            show her_titjob_personal h8 as cg
            her "Right..." ("soft", "narrow", "base", "down")

    show her_titjob_personal h5 as cg
    her "............." ("soft", "narrow", "worried", "down")
    gen "............." ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h8 as cg
    her "............." ("normal", "happyCl", "worried", "mid")
    show her_titjob_personal h5 as cg
    her "*Ehm*...{w=0.4} [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Yes, what is it, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Are you almost...{w=0.3} there?" ("open", "base", "base", "mid")
    gen "Almost there? Why you've only just started, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h7 as cg
    if game.daytime:
        her "Well, it's just that...{w=0.3} my classes are about to start..." ("upset", "wink", "base", "mid")
    else:
        her "Well, it's just that...{w=0.3} I promised I would meet up with a friend tonight..." ("upset", "wink", "base", "mid")
        her "They're already pretty upset with how much time I'm spending outside the dormitory..." ("upset", "wink", "base", "mid")
    gen "If your performance is satisfactory, then you will have ample time for less important activities." ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h8 as cg
    her "{size=-5}Less important...{/size}" ("soft", "narrow", "worried", "down")
    gen "Besides... If you want to earn those points..." ("base", xpos="far_left", ypos="head")
    her "Then I should meet the expectations..." ("grin", "happyCl", "worried", "mid")
    gen "That's right..." ("base", xpos="far_left", ypos="head")
    gen "That said... There are always ways to finish things up a bit faster..." ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h7 as cg
    her @ cheeks blush "I see... Then, what would you like me to do, [name_genie_hermione]?" ("soft", "base", "base", "R")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Tell me what people think of your tits!\"":
            show her_titjob_personal h5 as cg
            her "What?" ("upset", "wink", "base", "mid")
            show her_titjob_personal h8 as cg
            her @ cheeks blush "My breasts?" ("disgust", "narrow", "worried", "down")
            gen "That's right..." ("base", xpos="far_left", ypos="head")
            gen "Surely you've had plenty of unique experiences, thanks to them..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h7 as cg
            her @ cheeks blush "I... Well..." ("soft", "narrow", "worried", "down")
            gen "Tell me... Have you ever caught someone staring at them?" ("base", xpos="far_left", ypos="head")
            her "I suppose..." ("base", "narrow", "base", "down")
            gen "Go on..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h5 as cg
            her @ cheeks blush "Well...{w=0.4} There was this one time in the library..." ("open", "base", "base", "R")
            her @ cheeks blush "I was the only one there, apart from this other person sitting right across from me..." ("base", "base", "base", "R")
            gen "Go on..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h7 as cg
            her "It was a very hot day...{w=0.4} and even I was struggling not to give in, and head off to the lake..." ("angry", "happy", "base", "mid")
            her "Nevertheless, the heat soon became unbearable, and I decided to remove my vest..." ("angry", "happy", "base", "mid")
            gen "And somehow that made you even hotter!" ("grin", xpos="far_left", ypos="head")
            show her_titjob_personal h8 as cg
            her "[name_genie_hermione]..." ("open", "base", "base", "R")
            gen "So, I assume this other person noticed this sudden change?" ("grin", xpos="far_left", ypos="head")
            show her_titjob_personal h7 as cg
            her "They certainly did... Any time I looked down at my book, I could tell that they were peeking at my chest..." ("base", "base", "base", "R")
            show her_titjob_personal h5 as cg
            her "Unfortunately, removing my vest was not enough, so I decided to undo a couple of buttons as well...." ("base", "narrow", "base", "mid_soft")
            gen "*Hmm*... Yes, very unfortunate..." ("grin", xpos="far_left", ypos="head")
            show her_titjob_personal h7 as cg
            her "And by the second button, they weren't just sneaking a peek, they were barely taking their eyes off me...." ("base", "narrow", "worried", "down")
            her "Once I reached for the third, I could swear I could see their hand move under the desk...." ("base", "narrow", "worried", "down")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            her "Yes... I even thought I could hear the sound of them at one point....{w=0.3} The sound of them \"doing it\"..." ("base", "narrow", "base", "up")
            gen "I suppose that's to be expected when you start stripping in front of someone." ("grin", xpos="far_left", ypos="head")
            show her_titjob_personal h8 as cg
            her "[name_genie_hermione]! I wasn't stripping, I was merely trying to cool off..." ("base", "narrow", "worried", "down")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "Well, I guess I was technically stripping..." ("base", "narrow", "base", "mid_soft")
            show her_titjob_personal h7 as cg
            her "Anyway... By the third button, they had a clear view of the upper part of my bra...." ("base", "narrow", "base", "mid_soft")
            show her_titjob_personal h6 as cg
            her "As well as the entirety of my cleavage..." ("base", "base", "base", "mid")
            show her_titjob_personal h7 as cg
            her "At that point, they didn't even try to cover up what they were doing, and their attention was completely focused on my chest..." ("base", "base", "base", "mid")
            her "That's when I suddenly felt something wet doing down my legs!" ("open_tongue", "narrow", "annoyed", "up")
            gen "!!!" ("angry", xpos="far_left", ypos="head")
            if _tits:
                her "Come on, [name_genie_hermione]! Cum for me already! Cover my breasts in it!" ("grin", "base", "angry", "mid")
            else:
                her "Come on, [name_genie_hermione]! Give it to me already!" ("grin", "base", "angry", "mid")

        "\"Stick out your tongue!\"":
            show her_titjob_personal h7 as cg
            her "[name_genie_hermione]?" ("open", "wink", "base", "mid")
            gen "Just do it, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
            show her_titjob_personal h11 as cg
            her "*Ehm*...{w=0.4} *Ike* *ees*?" ("open_wide_tongue", "narrow", "worried", "down")
            gen "Yes, good..." ("base", xpos="far_left", ypos="head")
            gen "Now tilt your head down a bit... As far as it'll go." ("base", xpos="far_left", ypos="head")
            her "....................." ("open_wide_tongue", "base", "base", "mid")
            gen "Yes...{w=0.3} Good..." ("base", xpos="far_left", ypos="head")
            her "..........." ("open_wide_tongue", "base", "base", "mid")
            her "..........."
            show her_titjob_personal h9 as cg
            her "I *khant* *eef* *ay* *outh* *oen*..." ("open_tongue", "base", "base", "mid")
            her "I *eel* *ool*..." ("open_wide_tongue", "narrow", "worried", "down")
            gen "Yes! Drool all over those perfect tits of yours!" ("angry", xpos="far_left", ypos="head")
            her "*Erth-ect*?" ("open_tongue", "base", "base", "mid")
            gen "As perfect as any mortal, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h11 as cg
            her "......." ("base", "narrow", "base", "up")
            gen "Try to get it as close to the tip of my cock as you can..." ("base", xpos="far_left", ypos="head")
            her "............" ("normal", "happyCl", "worried", "mid")
            her "A-ha..." ("open_wide_tongue", "base", "base", "mid")
            gen "Good, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her ".............." ("open_wide_tongue", "base", "base", "mid")
            gen "Yes, and keep stroking my cock with your tits!" ("base", xpos="far_left", ypos="head")

            nar "As Hermione lets her saliva land between your cock and her tits, the friction between them gets less and less."

            her ".................." ("open_wide_tongue", "base", "base", "mid")
            gen "That's good..." ("angry", xpos="far_left", ypos="head")
            her "................." ("open_wide_tongue", "base", "base", "mid")
            pause.2

            call her_chibi_scene("tj_mouth", trans=d5)
            call ctc

            nar "Hermione's movements become increasingly aggressive thanks to the lack of friction, and you feel yourself getting closer to finishing by the second."

            gen "That's it, slut! Taste it!" ("angry", xpos="far_left", ypos="head")
            her "....................." ("open_wide_tongue", "wide", "angry", "stare")
            gen "Yes, keep going, you big-titted whore!" ("angry", xpos="far_left", ypos="head")
            her "......................" ("open_wide_tongue", "happyCl", "angry", "mid")
            her "................" ("open_wide_tongue", "narrow", "worried", "up")

    with hpunch
    gen "{size=-4}(Here it comes!){/size}" ("angry", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Fill her mouth up!-":
            gen "Get ready, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
            show her_titjob_personal h13 as cg

            call her_chibi_scene("tj_pause", trans=d5)

            her "What? already?!" ("angry", "wide", "base", "stare")
            gen "{size=+5}Yeah, your tits felt great!!!{/size}" ("angry", xpos="far_left", ypos="head")
            gen "{size=+5}Open wide, you big-titted whore!!{/size}" ("angry", xpos="far_left", ypos="head")
            if _mouth:
                her "Wait, I need to--" ("angry", "wide", "base", "stare")
            else:
                her "Wait, I thought you said--" ("angry", "wide", "base", "stare")

            nar "You grab the back of Hermione's head, and force your cock into her open mouth..."
            show her_titjob_personal h12 as cg

            stop music fadeout 1.0
            call cum_block
            call her_chibi_scene("tj_cum_in", trans=d5)
            pause.8

            her "!!!" ("open_wide_tongue", "wide", "base", "stare")
            call cum_block

            $ hermione.set_cum(breasts="light")

            gen "{size=+5}*ARGH*! YES!!! Take it!{/size}" ("angry", xpos="far_left", ypos="head")
            her "....................." ("open_wide_tongue_cum", "happyCl", "worried", "mid")
            call bld("hide")
            call ctc

            call her_chibi_scene("tj_cum_in_done", trans=d5)

            her @ cheeks blush "......................." ("full_cum", "narrow", "worried", "down")
            gen "*Mmm*... That felt great..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "......................." ("full_cum", "narrow", "worried", "down")
            gen "How are you feeling?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "......................." ("full_cum", "narrow", "worried", "down")
            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            pause.2

            call her_chibi_scene("tj_pause", trans=d5)
            pause.5

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            show her_titjob_personal h15 as cg
            her "*Ptui*..." ("open_wide_tongue_cum", "base", "angry", "mid", trans=hpunch)

            $ hermione.set_cum(face="light")

            show her_titjob_personal h16 as cg
            her "Why on earth did you pull my head like that?" ("angry", "happyCl", "worried", "mid", emote="sweat")
            pause.2

            show her_titjob_personal h17 as cg

            call her_chibi_scene("tj_cum_on_done", trans=d5)
            pause.5

            nar "Hermione lets go of your still pulsating cock..."

            her "*Ugh*...{w=0.4} You came so much!" ("angry", "happyCl", "worried", "mid", emote="sweat")
            her "You should've warned me sooner... That way I would've been able to reposition--" ("soft", "narrow", "base", "down", emote="sweat")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "I mean, with my head being pulled--{w=0.2} *Ahem*...{w=0.4} It meant I couldn't swallow all of it..." ("soft", "narrow", "base", "down", emote="sweat")
            her "I suppose, it may have been my fault... I should've realised." ("soft", "narrow", "base", "down", emote="sweat")
            if states.her.status.gokkun:
                gen "Well, you tried and that's all that matters." ("grin", xpos="far_left", ypos="head")
                her "I suppose..." ("soft", "narrow", "base", "down", emote="sweat")
                gen "You still did an excellent job, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
                gen "I'm impressed..." ("grin", xpos="far_left", ypos="head")
                her "Thank you, [name_genie_hermione]..." ("open", "narrow", "base", "R", emote="sweat")
            else:
                gen "..." ("grin", xpos="far_left", ypos="head")
                her "..." ("soft", "happy", "base", "base", emote="sweat")
                gen "For someone who's never swallowed before, I'd say you went well above exceeding my expectations." ("grin", xpos="far_left", ypos="head")
                her "Well above..." ("soft", "narrow", "base", "down", emote="sweat")
                gen "Indeed! You did an \"outstanding\" job, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
                her "Well, I don't know about that..." ("soft", "narrow", "base", "down", emote="sweat")
                gen "(Is she setting her own expectations now?)" ("base", xpos="far_left", ypos="head")
                gen "Well, I for one, am certainly impressed..." ("base", xpos="far_left", ypos="head")
                her "Thank you, [name_genie_hermione]..." ("open", "narrow", "base", "R", emote="sweat")
            her "But that doesn't change the fact that I still failed..." ("annoyed", "narrow", "base", "R", emote="sweat")
            gen "(She sounds like she's just failed a test...)" ("base", xpos="far_left", ypos="head")
            her "I mean, the most optimal thing would've been to swallow it all." ("base", "narrow", "base", "down", emote="sweat")
            if game.daytime:
                her "That way, I don't have to go to class, smelling like semen..." ("open", "closed", "base", "mid", emote="sweat")
            else:
                her "That way, I don't have to go through the common-room, smelling like semen..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "I see... You're really taking things seriously." ("base", xpos="far_left", ypos="head")
            her "Of course, [name_genie_hermione]... I always strive to achieve the highest level of excellence in any task I am given." ("open", "closed", "base", "mid")
            gen "Well, I'm sure you'll do better next time..." ("base", xpos="far_left", ypos="head")
            her "Most certainly..." ("soft", "narrow", "base", "down")
            if game.daytime:
                her "{size=-2}Maybe if I skip breakfast... Or practice relaxing my throat...{/size}" ("base", "narrow", "base", "down")
            else:
                her "{size=-2}Maybe if I skip dinner... Or practice relaxing my throat...{/size}" ("base", "narrow", "base", "down")
            her "Perhaps I could--" ("base", "narrow", "base", "down")
            gen "Sounds like some good ideas... Now let me sit down and I'll give you the points you've earned today." ("base", xpos="far_left", ypos="head")
            her "My reward! I almost forgot!" ("soft", "happy", "base", "mid")

            $ states.her.status.gokkun = True

        "-Cover her tits!-":
            with hpunch
            call bld
            gen "{size=+2}*Argh*!{/size}" ("angry", xpos="far_left", ypos="head")
            show her_titjob_personal h13 as cg

            call her_chibi_scene("tj_pause", trans=d5)

            her "{size=+2}What?!{/size}" ("shock", "wide", "base", "stare")
            gen "Take this, slut!" ("angry", xpos="far_left", ypos="head")

            stop music fadeout 1.0
            call cum_block
            call her_chibi_scene("tj_cum_on", trans=d5)
            pause.8

            $ hermione.set_cum(breasts="light")

            call bld
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")

            her "...................." ("shock", "happyCl", "worried", "mid")
            call cum_block
            $ hermione.set_cum(body="light", breasts="heavy")
            show her_titjob_personal h18 as cg
            call ctc

            call her_chibi_scene("tj_cum_on_done", trans=d5)

            her "......................." ("angry", "wide", "base", "stare")
            gen "Well, I think that's about it..." ("base", xpos="far_left", ypos="head")
            her ".........." ("soft", "base", "base", "mid")

            show her_titjob_personal h17 as cg
            if _mouth:
                her "[name_genie_hermione], I thought you said you were going to finish in my mouth..." ("angry", "happyCl", "worried", "mid")
                gen "Disappointed are you, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Oh, of course not...{w=0.4} It's just..." ("angry", "happyCl", "worried", "mid")
            else:
                her "[name_genie_hermione]! How could you cum this much?!" ("angry", "happyCl", "worried", "mid")
                her "(It's like he dumped a bucket all over my chest...)" ("disgust", "narrow", "base", "down")
                gen "That's what happens when you meet expectations, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Right..." ("disgust", "narrow", "base", "down")
                her @ cheeks blush "Still..." ("annoyed", "narrow", "base", "down")

            if game.daytime:
                her "I can't exactly attend classes looking like this..." ("angry", "happyCl", "worried", "down")
            else:
                her "How am I supposed to go back to the Gryffindor common-room, looking like this?!" ("angry", "happyCl", "worried", "mid")
            gen "You could just wipe it off..." ("base", xpos="far_left", ypos="head")
            her "I suppose..." ("angry", "narrow", "worried", "down")
            her "May I get paid now, [name_genie_hermione]?" ("soft", "happy", "base", "R")
            gen "Certainly..." ("base", xpos="far_left", ypos="head")

    $ achievements.unlock("hertits")
    $ states.her.status.titjob = True

    jump end_hg_pf_titjob

### Tier 6 Titjob ###

label hg_pf_titjob_2:
    stop music fadeout 4.0
    call hide_characters
    show screen blkfade
    with d3

    # Setup
    show her_titjob_personal h6 as cg
    $ hermione.zorder = -1
    hide hermione_main

    show her_titjob_personal h20 as cg
    $ hermione.strip("robe", "accessory")

    if hermione.is_any_worn("top", "bra"):
        her "Let me get undressed first..." ("disgust", "base", "worried", "down")
        $ hermione.strip("top", "bra")
        pause 1.0

    nar "Hermione wraps her plump tits around your cock..."

    call her_chibi_scene("tj", trans=fade)
    call ctc

    nar "She then starts moving her breasts, alternating her speed every now and  then."
    her "Do you enjoy it when I move them like this, [name_genie_hermione]?" ("grin", "base", "base", "R", ypos="head", flip=False)
    gen "Oh, yes... Very much!" ("grin", xpos="far_left", ypos="head")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "..." ("base", "narrow", "base", "mid_soft")
    gen "Yes, just like that..." ("base", xpos="far_left", ypos="head")
    gen "*Hmm*... You're getting pretty good at this." ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h21 as cg
    her "Thank you, [name_genie_hermione]..." ("base", "happyCl", "base", "mid")
    her "I do believe that my proficiency in identifying your preferred interests has advanced to a satisfactory level..." ("base", "closed", "base", "mid")
    gen "I love it when you speak dirty to me like that..." ("base", xpos="far_left", ypos="head")
    her "*Huh*?" ("soft", "base", "base", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"What do you think of my cock?\"":
            show her_titjob_personal h22 as cg
            her "*Huh*?" ("open", "base", "base", "mid")
            her "Your cock?" ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "Yes, my--" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h23 as cg
            her "Oh!" ("angry", "base", "base", "mid")
            her "It's magnificent!" ("angry", "closed", "base", "mid")
            gen "Very good... Go on..." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione], If I have the perfect breasts..." ("soft", "narrow", "annoyed", "up")
            nar "She squeezes her tits around your cock."
            show her_titjob_personal h22 as cg
            her "Then this has to be the perfect cock for them!" ("grin", "narrow", "base", "dead")
            gen "The perfect cock... For your tits?" ("grin", xpos="far_left", ypos="head")
            her "The size..." ("soft", "narrow", "worried", "down")
            her "The shape..." ("base", "narrow", "worried", "down")
            her "It just fits perfectly between my breasts..." ("base", "narrow", "base", "mid_soft")
            show her_titjob_personal h24 as cg
            nar "Hermione opens her mouth and lets some saliva drip onto the tip of your dick."
            her "..........." ("open_tongue", "narrow", "annoyed", "up")
            show her_titjob_personal h23 as cg
            her "And now it will slide between them perfectly, as well..." ("soft", "narrow", "annoyed", "up")
            gen "Nice... And what else--" ("grin", xpos="far_left", ypos="head")
            show her_titjob_personal h25 as cg
            her "We should share this magnificent cock with everyone around the school!" ("scream", "closed", "angry", "mid")
            gen "Well, I wouldn't go that far--" ("base", xpos="far_left", ypos="head")
            her "Listen to me, [name_genie_hermione]!" ("angry", "closed", "angry", "mid")
            her "Worshipping your penis should be a part of the school curriculum!" ("soft", "narrow", "annoyed", "up")
            show her_titjob_personal h24 as cg
            her "Girls will be required to come to your office once a day, and give it one suck, all the way down to the hilt--" ("open_tongue", "narrow", "annoyed", "up")
            gen "Alright... I think I've heard enough." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h21 as cg

            call her_chibi_scene("tj_pause", trans=d5)
            pause.8

            her "Too much?" ("angry", "wink", "base", "mid")
            gen "Too little... One suck wouldn't be nearly enough..." ("base", xpos="far_left", ypos="head")
            her "Sorry, [name_genie_hermione]... Let me make it up to you..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            gen "Just do your best, massaging my cock with those big tits of yours, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Yes, [name_genie_hermione]..." ("angry", "narrow", "base", "down", emote="sweat")

            call her_chibi_scene("tj", trans=d5)
            pause.8

            her "................." ("soft", "narrow", "annoyed", "up")
            nar "Hermione keeps stroking your cock, making sure to push her breasts up and down as far as she can."
            show her_titjob_personal h24 as cg
            nar "Occasionally, she lets some saliva dribble from her mouth to help lubricate it."
            show her_titjob_personal h21 as cg
            gen "Yes...{w=0.3} That's it, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")

        "\"Call yourself a big-titted whore!\"":
            show her_titjob_personal h22 as cg
            her "Call myself a--" ("open", "base", "base", "mid")
            show her_titjob_personal h23 as cg
            her "*Hmm*...{w=0.5} Yes, I am a big-titted whore!" ("soft", "narrow", "annoyed", "up")
            gen "Very good..." ("base", xpos="far_left", ypos="head")
            gen "Now I want you to say..." ("base", xpos="far_left", ypos="head")

            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"I'm a shameless cumslut!\"":
                    show her_titjob_personal h22 as cg
                    her "Of course..." ("base", "narrow", "worried", "down")
                    show her_titjob_personal h24 as cg
                    her "I'm a shameless cumslut..." ("soft", "narrow", "annoyed", "up")
                    show her_titjob_personal h21 as cg
                    her "A dirty little slut who's addicted to the taste of my headmaster's cum..." ("grin", "narrow", "base", "dead")
                    gen "Yes! Good!" ("base", xpos="far_left", ypos="head")
                "\"I love being covered in cum!\"":
                    show her_titjob_personal h24 as cg
                    her "I love being covered in cum!" ("soft", "narrow", "annoyed", "up")
                    her "Hot..." ("soft", "narrow", "annoyed", "up")
                    her "Sticky..." ("soft", "narrow", "annoyed", "up")
                    her "Messy..." ("soft", "narrow", "annoyed", "up")
                    her "Cum..." ("soft", "narrow", "annoyed", "up")
                    show her_titjob_personal h23 as cg
                    her "..................................." ("grin", "narrow", "base", "dead")
                    show her_titjob_personal h21 as cg
                    her "How was that, [name_genie_hermione]?" ("angry", "wink", "base", "mid")
                    gen "Perfect..." ("base", xpos="far_left", ypos="head")

        "\"So, you haven't been practising or anything?\"" if states.her.status.titjob: #Since she should do it once to then practice it more.
            show her_titjob_personal h22 as cg
            her "*Hmm*..." ("base", "happyCl", "base", "mid")
            show her_titjob_personal h21 as cg
            her "Well, I suppose I sort of--{w=0.3} But it wasn't on another cock..." ("angry", "wink", "base", "mid")
            gen "Then what was it?" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "Well... It'd require some explaining..." ("angry", "wink", "base", "mid")
            gen "Then explain..." ("base", xpos="far_left", ypos="head")
            her "Well... I was taking a shower the other day, when I overheard some of the other girls comparing the size of their breasts..." ("soft", "base", "base", "R")
            gen "*Gasp*!" ("base", xpos="far_left", ypos="head")
            her "I know! I couldn't believe it!" ("soft", "base", "base", "R")
            her "Of course, I pretended not to notice, but then they started making fun of mine, and I had to say something about it." ("annoyed", "base", "base", "R")
            gen "*Even louder gasp*" ("base", xpos="far_left", ypos="head")
            her "Yes, They were calling them small! Can you believe that?" ("annoyed", "base", "base", "R")
            gen "One side of me wants to lie, just to hear your reaction... But I don't think I'd be able to make it sound convincing." ("base", xpos="far_left", ypos="head")
            her "Yes, their words didn't sound very convincing either... But still... The fact that they even dared to utter them is astounding." ("base", "narrow", "base", "R")
            show her_titjob_personal h21 as cg
            gen "So, what did you say to them?" ("base", xpos="far_left", ypos="head")
            her "I told them that their tits are so small, they can't even fit a dick between them!" ("base", "happy", "base", "mid")
            gen "Really? You said that to them?" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "Of course I did! They were making fun of me!" ("smile", "base", "base", "R")
            show her_titjob_personal h23 as cg
            her "Although I didn't expect what would come next..." ("angry", "wink", "base", "mid")
            gen "One of them told you to prove that you could fit a dick between your tits by having you wrap them around their arm?" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h25 as cg
            her "How did you know?!" ("angry", "happyCl", "worried", "mid", emote="sweat")
            show her_titjob_personal h22 as cg
            gen "...{w=0.4} They were obviously baiting you to do it..." ("base", xpos="far_left", ypos="head")
            her "They were--" ("angry", "base", "worried", "mid", emote="sweat")
            show her_titjob_personal h23 as cg
            her "Oh..." ("base", "narrow", "worried", "down")
            her "So they must've known I was listening in, the entire time..." ("base", "narrow", "worried", "down")
            gen "Did you lather them up with soap first?" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h21 as cg
            her "*Huh*?" ("base", "narrow", "base", "up")
            gen "Did you put soap on your tits, before you wrapped them--" ("grin", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "[name_genie_hermione]!" ("base", "happyCl", "base", "mid")
            show her_titjob_personal h23 as cg
            gen "Sorry... Perhaps I shouldn't have--" ("base", xpos="far_left", ypos="head")
            her "Of course I used soap! How else would I have been able to move them up and down?" ("base", "closed", "base", "mid")
            gen "Nice... I bet she loved that..." ("base", xpos="far_left", ypos="head")
            her "She most certainly did..." ("open", "narrow", "worried", "down")
            show her_titjob_personal h22 as cg
            her "Maybe a little too much..." ("soft", "happy", "base", "R")
            gen "How so?" ("base", xpos="far_left", ypos="head")
            her "Well..." ("soft", "happy", "base", "R")
            her "She might have started..." ("soft", "happy", "base", "R")
            show her_titjob_personal h23 as cg
            her "Grinding on my leg..." ("grin", "narrow", "annoyed", "up")
            with hpunch
            gen "She did?!" ("angry", xpos="far_left", ypos="head")
            her "Yes... Although I was too busy to notice, at first..." ("open", "base", "base", "R")
            gen "So, when did you notice?" ("base", xpos="far_left", ypos="head")
            her "I noticed when she... She..." ("open", "base", "base", "R")
            show her_titjob_personal h24 as cg
            her "Orgasmed..." ("soft", "narrow", "annoyed", "up")
            gen "On your leg?!" ("angry", xpos="far_left", ypos="head")
            show her_titjob_personal h23 as cg
            her "Yes..." ("soft", "narrow", "annoyed", "up")
            gen "You little slut!" ("base", xpos="far_left", ypos="head")
            her "How was I supposed to know she would start--" ("grin", "happyCl", "worried", "mid", emote="sweat")
            her "*Err*... I mean..." ("angry", "wink", "base", "mid")
            show her_titjob_personal h21 as cg
            her "I didn't notice she was doing it, so I don't see why that would make me a slut!" ("angry", "narrow", "base", "down")
            gen "I was obviously referring to the girl..." ("base", xpos="far_left", ypos="head")
            her "Oh..." ("angry", "narrow", "base", "down")
            gen "Even then... I find it highly unlikely for you not to notice a girl rubbing up on your leg..." ("base", xpos="far_left", ypos="head")
            gen "Surely, you wouldn't embellish the truth to hide your sluttishness?" ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "base", "down")
            gen "Either way...{w=0.4} I think I've heard enough about your \"accidental\" lesbian escapades..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h24 as cg
            her "Of course, [name_genie_hermione]..............." ("base", "narrow", "worried", "down")
            nar "Hermione opens her mouth and lets her saliva dribble down on your cock."

    if not _events_completed_any:
        jump hg_pf_titjob_2_cumming
    else: # Repeat
        jump hg_pf_titjob_2_continue

label hg_pf_titjob_2_continue:
    call her_chibi_scene("tj", trans=d5)

    call bld
    gen "*Mmm*... Keep stroking it." ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h23 as cg
    her ".............." ("angry", "wink", "base", "mid", ypos="head", flip=False)
    gen "Now I want you to say..." ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-4}\"I love teasing my father with my big tits.\"{/size}":
            show her_titjob_personal h25 as cg
            her "Teasing my--{w=0.2} But, [name_genie_hermione]..." ("angry", "narrow", "base", "down", ypos="head", flip=False)
            gen "Just say it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "*Hmph*...{w=0.4} What do you want me to say, exactly?" ("soft", "narrow", "annoyed", "up")
            gen "Just make something up, and include those big tits of yours..." ("base", xpos="far_left", ypos="head")
            her "..........." ("angry", "wink", "base", "mid")
            her "Alright..." ("open", "narrow", "worried", "down")
            show her_titjob_personal h21 as cg
            her "Sometimes... When I hug..." ("open", "narrow", "worried", "down")
            her "......." ("open", "narrow", "worried", "down")
            gen "Go on, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "Sometimes when I hug my father..." ("open", "narrow", "worried", "down")
            her "I press my tits against him...{w=0.2} Just to see his reaction..." ("soft", "narrow", "annoyed", "up")
            gen "Nice...{w=0.2} So, do you think he enjoys it?" ("base", xpos="far_left", ypos="head")
            her "I'm not sure..." ("annoyed", "base", "base", "mid")
            her "But I'd like to think he does..." ("soft", "happy", "base", "R")
            show her_titjob_personal h23 as cg
            her "I mean... He always runs off, covering his crotch afterwards..." ("base", "closed", "base", "mid")
            her "About ten minutes later... He reminds me that I'm too old for hugs..." ("annoyed", "closed", "base", "mid")
            her "But I don't care...{w=0.2} I always make sure to give him a big one, every night before I go to bed!" ("annoyed", "closed", "base", "mid")
            her "I tell myself that I do it, just because I love him... But deep down, I know it's because I want him to think about me..." ("base", "narrow", "worried", "down")
            her "And how good my tits felt..." ("grin", "narrow", "base", "dead")
            show her_titjob_personal h24 as cg
            her "I figured, if I do it before bed... Then perhaps he'll dream about it..." ("soft", "narrow", "annoyed", "up")
            gen "Who wouldn't..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "Maybe if I give him a kiss on his forehead..." ("soft", "happy", "base", "R")
            show her_titjob_personal h23 as cg
            her "I could let him get a peek at my chest..." ("grin", "happyCl", "worried", "mid", emote="sweat")
            her "{heart}{heart}{heart}" ("grin", "happyCl", "worried", "mid", emote="sweat")
            show her_titjob_personal h25 as cg
            her "*Ahem*...{w=0.4} Did you like that, [name_genie_hermione]?" ("angry", "base", "worried", "mid")
            show her_titjob_personal h22 as cg
            her "Did you like my little story?" ("soft", "base", "base", "mid")
            gen "Yes... Very good, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

        "{size=-4}\"I love teasing my classmates with my perfect tits.\"{/size}":
            show her_titjob_personal h23 as cg
            her "I...{w=0.4} I love teasing my classmates...{w=0.4} With my perfect tits..." ("soft", "narrow", "annoyed", "up", ypos="head", flip=False)
            gen "Of course you do..." ("base", xpos="far_left", ypos="head")
            her "I love the jealous looks from the other girls..." ("base", "narrow", "worried", "down")
            gen "Yes, and they should be jealous..." ("base", xpos="far_left", ypos="head")
            her "And that's about--" ("base", "narrow", "worried", "down")
            gen "And your friends... Tell me about your friends..." ("base", xpos="far_left", ypos="head")
            her "My friends?!" ("angry", "narrow", "worried", "mid")
            gen "Yes, [name_genie_hermione], your friends... Tell me how you use those tits to tease them..." ("base", xpos="far_left", ypos="head")
            her "But..." ("angry", "narrow", "worried", "mid")
            gen "Anything... Just say anything that you can think of..." ("base", xpos="far_left", ypos="head")
            her "Alright... Give me a moment to think..." ("angry", "narrow", "worried", "mid")
            gen "Fine... Just make it sound believable..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h21 as cg
            her "I... I love teasing my friends during breakfast..." ("base", "narrow", "base", "mid_soft")
            gen "Good... Yes, breakfast is something we all eat..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "Especially during a hot day, I'll just so happen to forget to button-up my shirt properly..." ("base", "squint", "base", "mid")
            gen "Naturally..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h23 as cg
            her "Other times I'll just wear it, with nothing underneath... Allowing my nipples to poke through..." ("base", "squint", "base", "mid")
            gen "Yes... And how does that make you feel?" ("base", xpos="far_left", ypos="head")
            her "Very naughty..." ("angry", "narrow", "base", "down")
            gen "And what else have you done, using those titties?" ("base", xpos="far_left", ypos="head")
            her "You want me to say even more?" ("angry", "narrow", "base", "down")
            her "Alright then..." ("angry", "narrow", "base", "down")
            her "*Ehm*... This one time, when walking back from your office at night, I forgot to cover them up..." ("angry", "wink", "base", "mid")
            her "And as I rounded a corner--" ("soft", "narrow", "annoyed", "up")
            show her_titjob_personal h23 as cg
            her "A Ravenclaw boy ran head first into them..." ("grin", "narrow", "annoyed", "up")
            gen "Head first into your first class tits?" ("base", xpos="far_left", ypos="head")
            her "Yes... All I could see was the top of his head..." ("grin", "narrow", "base", "dead")
            gen "A short king, I see..." ("base", xpos="far_left", ypos="head")
            her "He immediately attempted to pull away, of course..." ("grin", "narrow", "base", "dead")
            gen "Attempted?" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "Well...{w=0.4} I may have held him there..." ("base", "narrow", "base", "mid_soft")
            her "Only for a little bit..." ("base", "narrow", "worried", "down")
            show her_titjob_personal h23 as cg
            her "Just long enough so that it still looked like an accident..." ("base", "squint", "base", "mid")
            gen "This really did happen, didn't it?" ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h22 as cg
            her "*Ehm*..." ("soft", "squint", "base", "mid")
            her "Then he started masturbating!" ("base", "narrow", "worried", "down")
            show her_titjob_personal h21 as cg
            gen "Really? Just like that?" ("base", xpos="far_left", ypos="head")
            her "Of course! I mean, why wouldn't he!" ("soft", "narrow", "annoyed", "up")
            gen "*Hmm*... Yes, I suppose that could've happened..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h23 as cg

    gen "Now... Why don't you spit on my dick, so we can wrap this up?" ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]..." ("soft", "narrow", "annoyed", "up")
    show her_titjob_personal h24 as cg
    nar "Hermione lets her saliva dribble down on your cock, and then starts rubbing her tits with renewed effort."

    jump hg_pf_titjob_2_cumming

label hg_pf_titjob_2_cumming:
    call her_chibi_scene("tj", trans=d5)

    gen "*Mmm*..." ("base", xpos="far_left", ypos="head")
    gen "I love your perfect tits!" ("base", xpos="far_left", ypos="head")
    show her_titjob_personal h22 as cg
    her "Thank you, [name_genie_hermione]." ("soft", "narrow", "annoyed", "up", ypos="head", flip=False)
    show her_titjob_personal h23 as cg
    her "Shall I rub them a bit faster?" ("soft", "narrow", "annoyed", "up")
    gen "Rub away, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    nar "Hermione presses her tits together against your cock and begins rubbing it rapidly..."
    gen "Oh, yes!!!" ("base", xpos="far_left", ypos="head")
    stop music fadeout 1.0
    gen "{size=-5}(Almost there! Ready or not...){/size}" ("angry", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Cum in her mouth-":
            gen "Take this, whore!" ("angry", xpos="far_left", ypos="head")
            show her_titjob_personal h25 as cg
            her "What are you--" ("angry", "wink", "base", "mid", ypos="head", flip=False)

            call her_chibi_scene("tj_mouth", trans=d5)
            pause.8

            nar "You pull Hermione's head onto your cock, and the sensation of her wet mouth drives you over the edge."
            call cum_block
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            show her_titjob_personal h26 as cg

            call her_chibi_scene("tj_cum_in", trans=d5)
            pause.8

            her "!!!!!!!!!!!" ("full", "wide", "base", "stare")
            gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")
            her "{heart}{heart}{heart}" ("full_cum", "narrow", "base", "dead")
            call cum_block

            gen "*Argh*! You big-titted slut! Take it all!" ("angry", xpos="far_left", ypos="head")
            her "..............." ("full_cum", "narrow", "base", "dead")
            gen "............" ("base", xpos="far_left", ypos="head")

            call her_chibi_scene("tj_cum_in_done", trans=d5)
            pause.8

            gen "There... Every, last, drop..." ("base", xpos="far_left", ypos="head")
            her ".............." ("full_cum", "narrow", "base", "dead")
            her "........" ("full_cum", "narrow", "base", "dead")
            her "..." ("full_cum", "narrow", "base", "dead")

            play sound "sounds/gulp.ogg" #Sound of gulping down a liquid.
            show her_titjob_personal h27 as cg
            her "*GULP*" ("cum", "happyCl", "worried", "mid") #play noise here

            call her_chibi_scene("tj_idle", trans=d5)
            pause.8

            call bld
            nar "Hermione releases your cock from between her tits."

            if game.daytime:
                her "Well then, I think I'd better go... My classes are about to begin." ("base", "base", "base", "mid")
            else:
                her "Well then, I think I'd better go... It's getting late." ("base", "base", "base", "mid")
            gen "Hold on, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "Yes?" ("open", "narrow", "worried", "down")
            gen "You forgot to thank me..." ("base", xpos="far_left", ypos="head")
            her "Thank you--" ("open", "narrow", "worried", "down")
            gen "For the meal..." ("base", xpos="far_left", ypos="head")
            her "Oh...{w=0.4} Thank you for the meal, [name_genie_hermione]..." ("grin", "base", "base", "R")
            her "(Now that I think about it... I suppose it doesn't taste that bad...)" ("soft", "narrow", "base", "down")
            gen "*Hmm*... Or perhaps you would've preferred to walk outside with cum all over you?" ("base", xpos="far_left", ypos="head")
            her "(It's less wasteful... I don't need to eat as much food... And I don't have to clean up afterwards...)" ("base", "narrow", "base", "down")
            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "*Huh*... Yes?" ("soft", "happy", "base", "R")
            gen "I knew it..." ("base", xpos="far_left", ypos="head")
            her "Oh... Are we done already, [name_genie_hermione]?" ("base", "base", "base", "mid")
            gen "Yes, we're done [name_hermione_genie]... And don't worry... I'll make sure to give you what you want some other time..." ("base", xpos="far_left", ypos="head")
            her "???" ("soft", "base", "base", "mid")

            $ states.her.status.gokkun = True

        "-Cum on her tits-":
            call her_chibi_scene("tj_pause", trans=d5)

            gen "Take this, you big-titted whore!" ("angry", xpos="far_left", ypos="head")
            with hpunch
            gen "*ARGH*!" ("angry", xpos="far_left", ypos="head")
            show her_titjob_personal h25 as cg
            her "What? Already?!" ("angry", "wide", "base", "stare", ypos="head", flip=False)
            gen "Aaah, yes!" ("angry", xpos="far_left", ypos="head")
            call cum_block

            call her_chibi_scene("tj_cum_on", trans=d9)
            pause.8

            show her_titjob_personal h30 as cg
            $ hermione.set_cum(breasts="light")

            call bld
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")

            $ hermione.set_cum(breasts="heavy")

            her "!!!!!!!!!!!" ("shock", "wide", "base", "stare")

            show her_titjob_personal h31 as cg
            her "......................." ("angry", "wide", "base", "stare")

            show her_titjob_personal h32 as cg
            call her_chibi_scene("tj_cum_on_done", trans=d9)
            pause.8

            gen "*Ah*... I feel like I've lost five pounds..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h33 as cg
            her "......................." ("base", "narrow", "base", "down")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
            show her_titjob_personal h35 as cg
            her "[name_genie_hermione]!" ("open", "happyCl", "worried", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her "You've covered my chest in cum..." ("angry", "happyCl", "worried", "mid")
            show her_titjob_personal h34 as cg
            her "There's so much..." ("open", "base", "base", "R")
            gen "It's your fault, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her "My fault?" ("angry", "base", "base", "mid")
            gen "It's those perfect tits of yours!" ("base", xpos="far_left", ypos="head")
            gen "They just felt too good..." ("base", xpos="far_left", ypos="head")
            show her_titjob_personal h36 as cg
            her "*Hmm*... I suppose you're right..." ("soft", "narrow", "base", "down")
            show her_titjob_personal h37 as cg
            her "Oh well... I'll just wipe it off the best I can, and hope that nobody will notice..." ("upset", "closed", "base", "mid")
            gen "You could lick them clean..." ("base", xpos="far_left", ypos="head")
            her "You want me to lick your cum off my tits?" ("soft", "narrow", "annoyed", "up")
            gen "Oh, yes..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... Well, I don't think I'd be able to reach..." ("soft", "narrow", "annoyed", "up")
            gen "That's too bad..." ("base", xpos="far_left", ypos="head")
            her "Will that be all, [name_genie_hermione]?" ("base", "closed", "base", "mid")
            gen "Yes, that shall do for now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    $ states.her.status.titjob = True
    jump end_hg_pf_titjob
