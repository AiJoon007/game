

### Hermione Masturbate ###

### Tier 4 (Intro) ###

label hg_pf_strip_T4_fingering:
    if not states.her.status.masturbating:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
        gen "Do you ever touch yourself?" ("base", xpos="far_left", ypos="head")
        her "What? Why are you asking me that?" ("upset", "wink", "base", "mid")
        gen "It's a simple question..." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]!" ("angry", "happyCl", "worried", "mid")
        gen "And I'd like you to answer it, truthfully..." ("base", xpos="far_left", ypos="head")
        her "......" ("normal", "happyCl", "worried", "mid")
        gen "Well, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "{size=-5}I suppose I do...{/size}" ("angry", "happyCl", "worried", "mid", emote="sweat")
        gen "*Huh*? What was that?" ("base", xpos="far_left", ypos="head")
        her "I said that I do, alright!!?" ("scream", "happyCl", "worried", "mid")
        gen "*Hmm*... I'm not sure I believe you." ("base", xpos="far_left", ypos="head")
        her "What? Why would I lie about something like this?" ("clench", "happy", "worried", "mid")
        gen "Well, you never know... Perhaps you believe it's what I want you to say..." ("base", xpos="far_left", ypos="head")
        her "That doesn't make any--" ("annoyed", "base", "angry", "mid")
        gen "But don't worry... I'm sure a quick little demonstration will erase any doubts." ("base", xpos="far_left", ypos="head")
        her "So that's what you're after......" ("annoyed", "narrow", "angry", "R")
        her "Don't you think this is going a bit too far?......" ("annoyed", "narrow", "angry", "R")
        if states.her.status.handjob:
            her "I mean, aren't these favours supposed to be for your benefit?" ("annoyed", "narrow", "worried", "R")
            gen "Truly? Why I don't remember receiving any points for my house..." ("base", xpos="far_left", ypos="head")
            her "That's not what I meant..." ("disgust", "narrow", "worried", "mid")
            her "I just--" ("angry", "narrow", "worried", "down")
            her "Are you sure you wouldn't prefer another handjob, [name_genie_hermione]?" ("annoyed", "narrow", "worried", "mid")
            gen "I suppose, if you'd like to attempt getting us both off at the same time, you could try..." ("grin", xpos="far_left", ypos="head")
            her "Getting us both--" ("clench", "base", "worried", "stare")
            her "No-no-no... You're not--" ("angry", "base", "worried", "mid")
            gen "...." ("grin", xpos="far_left", ypos="head")
            her "..." ("annoyed", "base", "worried", "mid")
            her "Please, stop doing that, [name_genie_hermione]." ("disgust", "happy", "worried", "mid")
            gen "Stop doing what?" ("base", xpos="far_left", ypos="head")
            her "Telling me to do something even more difficult, just so that I agree to what you actually want me to do..." ("annoyed", "narrow", "worried", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her "......" ("disgust", "base", "worried", "mid")
        else:
            gen "I'm only asking what is necessary, so that Gryffindor may get ahead of the other houses." ("base", xpos="far_left", ypos="head")
            gen "You want to win the cup, don't you?" ("base", xpos="far_left", ypos="head")
            her "Of course [name_genie_hermione], but--" ("disgust", "narrow", "angry", "mid")
            gen "Well, the choice is literally in your hands..." ("base", xpos="far_left", ypos="head")
            her "......" ("annoyed", "narrow", "worried", "down")
        her "*Sigh*...{w=0.4} I suppose I could...{w=0.4} Touch myself...{w=0.4} In front of you." ("open", "narrow", "worried", "down")
        her "But you better keep your hands to yourself..." ("angry", "narrow", "worried", "mid")
        gen "Witcher's promise." ("base", xpos="far_left", ypos="head")
        her "......" ("annoyed", "squint", "base", "mid")
    else: # Repeat
        gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Why don't you give that lovely pussy of yours a little rub for me?" ("grin", xpos="far_left", ypos="head")
        her "Again?" ("annoyed", "narrow", "base", "mid")
        gen "Again, and again, until it feels really good." ("base", xpos="far_left", ypos="head")
        her "..." ("disgust", "narrow", "base", "down")
        her "Fine... Just keep your hands to yourself..." ("open", "squint", "base", "R")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "..........." ("upset", "base", "base", "mid")
    her "*Ehm*... Let me know when you'd like me to--{w=0.4} start..." ("soft", "wink", "base", "mid")

    if hermione.is_any_worn("clothes"):
        gen "You may start once you're completely naked..." ("base", xpos="far_left", ypos="head")
        if hermione.is_worn("panties"):
            gen "Those panties of yours would get in the way otherwise..." ("base", xpos="far_left", ypos="head")
            her "Right." ("disgust", "narrow", "base", "down")
            pause 1.0
            play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("clothes")
        pause 1.0
    else:
        gen "When you're ready..." ("base", xpos="far_left", ypos="head")

    her "(I never would've imagined...{w=0.4} Doing this in front of my headmaster...{w=0.4} Of all people...)" ("normal", "happyCl", "worried", "mid")

    $ hermione.set_pose("hand_on_pussy")
    her "" ("soft", "closed", "worried", "mid", trans=d3)

    play sound "sounds/slick_02.ogg"
    with hpunch
    pause 1.0
    play background "sounds/slickloop.ogg" fadein 2
    call ctc

    gen "Excellent..." ("grin", xpos="far_left", ypos="head")
    her "........" ("upset", "wink", "base", "mid")
    gen "............." ("base", xpos="far_left", ypos="head")
    her "............." ("normal", "happyCl", "worried", "mid")

    stop background

    her "*Ehm*... [name_genie_hermione]?" ("angry", "narrow", "worried", "mid")
    gen "Yes [name_hermione_genie], what is it?" ("base", xpos="far_left", ypos="head")
    if not states.her.status.masturbating:
        her "For how long did you want me to do this?" ("open", "base", "worried", "mid")
        gen "Until you finish, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

        if game.daytime:
            her "But my classes are about to start, [name_genie_hermione]..." ("annoyed", "base", "worried", "mid")
        else:
            her "But it's getting late, [name_genie_hermione]..." ("annoyed", "base", "worried", "mid")
            gen "So?" ("base", xpos="far_left", ypos="head")
            her "Won't I miss curfew?" ("soft", "base", "worried", "mid")
            gen "There's still some time left before curfew..." ("base", xpos="far_left", ypos="head")
            gen "(I think...)" ("base", xpos="far_left", ypos="head")
    else:
        her "I presume that you're expecting me to do this until--" ("open", "base", "worried", "mid")
        gen "Until you finish, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

        if game.daytime:
            her "But, what if I don't make it back to class in time, [name_genie_hermione]..." ("annoyed", "base", "worried", "mid")
        else:
            her "Right... I Just thought... Well, it's getting a bit late, [name_genie_hermione]..." ("annoyed", "base", "worried", "mid")
            gen "Right?" ("base", xpos="far_left", ypos="head")
            her "I don't want to miss curfew, that's all..." ("soft", "base", "worried", "mid")
            gen "Well, then it's up to you to ensure you don't miss it..." ("base", xpos="far_left", ypos="head")

    her "It's just...{w=0.4} I'm not sure if I'll be able to--" ("disgust", "narrow", "base", "down")
    gen "Focus less on the talking and more on the doing, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "You want those points, don't you?" ("base", xpos="far_left", ypos="head")
    her "I do, [name_genie_hermione]! I'm sorry..." ("open", "narrow", "worried", "down")
    her "I'll keep going then..." ("disgust", "narrow", "base", "down")
    play background "sounds/slickloop.ogg" fadein 2
    gen "(*Hmm*... Perhaps I should encourage her a little.)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"That's it... Keep going, slut.\"":
            her "[name_genie_hermione]!!!" ("angry", "base", "angry", "mid")
            her "How...{w=0.4} How dare you!" ("upset", "base", "angry", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her "I hardly think that kind of--{w=0.2} *Ah*...{w=0.4} Language is appropriate." ("open", "happyCl", "base", "mid")
            gen "And masturbating in front of your headmaster is?" ("base", xpos="far_left", ypos="head")
            her "Well...{w=0.4} This--{w=0.2} This is different." ("open", "narrow", "worried", "down")
            her "I'm doing this for the honour of Gryffindor..."
            her "To help my--{w=0.2} *Ah*..." ("open", "closed", "worried", "down")

            play background "sounds/slickloopfast.ogg"
            nar "You notice Hermione beginning to move her fingers a little faster."
            $ hermione.set_cum(pussy="wet")

            her "*Ah*...{heart}{heart}{heart}" ("soft", "narrow", "annoyed", "up")
            her "Help my house, win the cup..." ("angry", "wink", "base", "mid")
            gen "Surely that can't be the only reason..." ("grin", xpos="far_left", ypos="head")
            her "I--{w=0.2} *Ah*...{w=0.4} Of course it--" ("normal", "happyCl", "worried", "mid")

            $ hermione.set_pose("hand_on_pussy_and_breast")

            her "*Ah-a*{heart}..." ("open", "happyCl", "worried", "mid")
            her "What--{w=0.2} *Ah*...{w=0.4} Other reason would there be for me to--" ("angry", "happyCl", "base", "down")
            gen "I don't know... From where I'm sitting, it looks as if you might be enjoying this a little too much..." ("base", xpos="far_left", ypos="head")
            her "I am not, [name_genie_hermione]!" ("open", "happyCl", "worried", "mid")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            her "......................" ("normal", "happyCl", "worried", "mid")
            gen "Then why are your fingers moving so fast, slut?" ("base", xpos="far_left", ypos="head")
            call ctc

            her "*Ah*...{heart}" ("open", "happyCl", "worried", "mid")
            gen "Just admit it... You do enjoy being called a slut!" ("base", xpos="far_left", ypos="head")
            her "I do not!" ("normal", "happyCl", "worried", "mid")
            her "I'm just thinking about--{w=0.2} *Ah*...{w=0.4} How happy everyone will be when we win!" ("shock", "happyCl", "worried", "mid")
            gen "And what if they find out how you earned the points?" ("base", xpos="far_left", ypos="head")
            stop background
            her "What?!" ("shock", "wide", "base", "stare")
            gen "If that happened, then surely everyone would be degrading you..." ("base", xpos="far_left", ypos="head")
            play background "sounds/slickloop.ogg"
            her "..." ("soft", "closed", "base", "R")
            gen "The entire school would let you know exactly what they think about your ways of gaining house points." ("base", xpos="far_left", ypos="head")
            play background "sounds/slickloopfast.ogg"
            her @ cheeks blush "The entire-- *Ah*...{heart}" ("silly", "narrow", "base", "dead")
            gen "That's right... Every...{w=0.4} Single...{w=0.4} Student." ("base", xpos="far_left", ypos="head")
            play background "sounds/slickloopveryfast.ogg"
            her @ cheeks blush "*Ah*...{heart}{heart}{heart}" ("grin", "narrow", "annoyed", "up")
            her @ cheeks blush "[name_genie_hermione], please... {w=0.4}*Mmmh*...{w=0.4} Don't tell anyone..." ("soft", "narrow", "base", "mid_soft")
            nar "Hermione continues to rub herself with renewed effort..."
            her @ cheeks blush "They can't--{w=0.2} *Ah*...{w=0.4} They can't find out..." ("soft", "narrow", "base", "R_soft")
            her @ cheeks blush "If Harry and Ron knew..." ("open", "narrow", "base", "down")
            her @ cheeks blush "I'd--{w=0.2} *Ah*...{heart}" ("soft", "closed", "annoyed", "up")
            gen "You'd what, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'd..." ("open", "closed", "worried", "mid")
            her @ cheeks blush "I'd...{heart}" ("silly", "closed", "worried", "mid")
            her @ cheeks blush "I...{heart}{heart}{heart}" ("grin", "narrow", "annoyed", "up")

        "\"Now, play with your breast.\"":
            her "My breast..." ("open", "narrow", "worried", "down")
            her "I'm not sure if I should--" ("open", "narrow", "base", "down")
            gen "Did you want to finish in time, or not?" ("base", xpos="far_left", ypos="head")
            her "Yes, but--" ("angry", "narrow", "base", "down")
            gen "Then do what I say." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "narrow", "base", "mid")
            gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
            gen "What I meant to say, is that there could be another ten points for you, at the finish-line..." ("base", xpos="far_left", ypos="head")
            $ current_payout += 10
            her "..." ("normal", "happy", "base", "R")
            her "......" ("soft", "happy", "base", "R")

            $ hermione.set_pose("hand_on_pussy_and_breast")

            her "*Ah*...{heart}" ("open", "closed", "base", "R")
            gen "There... Isn't that better?" ("base", xpos="far_left", ypos="head")
            her "*Ah*... I--{w=0.2} I don't know..." ("open", "wink", "worried", "mid")
            her "It feels kind of weird..." ("normal", "happyCl", "base", "mid")
            gen "Really? I thought you'd be used to it by now..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*...{w=0.4} Why would you think that I'd be used to it......{w=0.4} [name_genie_hermione]?" ("angry", "narrow", "base", "mid")
            gen "You've already done a lot of things for me inside this office..." ("base", xpos="far_left", ypos="head")
            gen "If it weren't for the points, you'd be considered quite the slut." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Why would you say something like--" ("soft", "narrow", "base", "L")
            gen "I'm just telling you how I see it..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Please [name_genie_hermione]... I'm not twisted, like those Slytherin harlots..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "I'm not a--{w=0.2} *Ah*..." ("open", "happyCl", "base", "mid")
            gen "Not a what, Miss Granger?" ("base", xpos="far_left", ypos="head")

            her @ cheeks blush "{size=-3}A Slut...{/size}" ("soft", "narrow", "base", "down")
            gen "Miss Granger!" ("base", xpos="far_left", ypos="head")
            gen "How very unbecoming of you to use such foul language..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "But--{w=0.2} *Ah*...{w=0.4} I just repeated what you--" ("angry", "narrow", "base", "mid")

            $ hermione.set_cum(pussy="wet")

            her "*Ah*...{heart}{heart}" ("open", "closed", "annoyed", "mid")
            gen "What would your parents think if they heard you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "My parents...{heart}" ("open", "narrow", "worried", "up")
            play background "sounds/slickloopfast.ogg"
            her @ cheeks blush "*Ah*...{heart} I don't know..." ("soft", "closed", "base", "up")
            her @ cheeks blush "Although, to be perfectly honest [name_genie_hermione]... I don't think I care...{heart}{heart}{heart}" ("silly", "narrow", "base", "up")
            gen "Really?" ("base", xpos="far_left", ypos="head")

            her @ cheeks blush "Yes...{heart}" ("grin", "happyCl", "base", "mid")
            her @ cheeks blush "It's not for them to--{w=0.2} *Ah*...{w=0.4} Decide how I speak." ("grin", "closed", "base", "mid")
            gen "Is that so..." ("base", xpos="far_left", ypos="head")
            gen "And what if they saw you like this?..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I--{w=0.2} *Mmmh*...{w=0.4} Surely that would never--" ("angry", "closed", "worried", "mid")
            gen "What if they burst through that door, and saw their little girl masturbating in front of the headmaster." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*...{w=0.4} They wouldn't...{w=0.4} You'd never allow..." ("normal", "happyCl", "worried", "mid")
            gen "I bet if they appeared right now, you wouldn't even stop touching yourself, you filthy slut." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*...{heart}" ("open_tongue", "narrow", "base", "up")
            gen "Look at you... You're nothing but a disgrace to your family..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*...{w=0.4} I'm-{heart}" ("open", "happyCl", "worried", "mid")
            her @ cheeks blush "I'm--{heart}{heart}{heart}" ("grin", "narrow", "annoyed", "up")

        "\"Spread em!\"":
            gen "And make sure to give me a nice view of that wet pussy!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione]!" ("open", "base", "angry", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")

            her @ cheeks blush "It's not {size=-5}wet...{/size}" ("annoyed", "narrow", "worried", "R")
            gen "Are you sure?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It--{w=0.2} I'm just getting a little sweaty, that's all..." ("angry", "narrow", "worried", "R")
            gen "I suppose that could be it..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..............." ("base", "closed", "base", "mid")
            gen "Only a slut would get wet that quickly." ("base", xpos="far_left", ypos="head")
            play background "sounds/slickloopfast.ogg"
            $ hermione.set_cum(pussy="wet")
            her @ cheeks blush "{heart}{heart}{heart}" ("grin", "narrow", "base", "up_soft")
            gen "Wow... Looks like you're getting quite the work-out, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Ah*... Yes, I--" ("angry", "narrow", "base", "up_soft")
            gen "Had I not known it was sweat, I would've thought that you enjoyed being called a slut." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione]...{w=0.4} Please..." ("open", "happyCl", "base", "stare")

            $ hermione.set_pose("hand_on_pussy_and_breast")
            her @ cheeks blush "" ("soft", "happyCl", "base", "mid")

            play background "sounds/slickloopveryfast.ogg"
            nar "Hermione starts fingering herself even faster."
            gen "Look at those fingers go..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...{heart}" ("grin", "closed", "worried", "mid")
            her @ cheeks blush "*Ah*...{heart}" ("open_tongue", "narrow", "base", "up")
            gen "That's it, push those fingers deep inside, just like all those other sluts..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("open_tongue", "narrow", "base", "up")
            her @ cheeks blush "...{heart}" ("open", "happyCl", "worried", "mid")

    play background "sounds/slickloop.ogg"
    her @ cheeks blush "(Wait, what am I doing...)" ("angry", "narrow", "worried", "stare")
    her @ cheeks blush "*Ah*..." ("soft", "narrow", "base", "R")
    gen "Almost there [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "A-almost..." ("annoyed", "base", "worried", "L")
    her "I just need a bit longer..."
    gen "Well, you better hurry..." ("base", xpos="far_left", ypos="head")
    her "*Ah*...{w=0.3} I know, [name_genie_hermione]." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "..........." ("normal", "closed", "base", "R")
    gen "Is everything alright?" ("base", xpos="far_left", ypos="head")
    play background "sounds/slickloopfast.ogg"
    her @ cheeks blush tears sweat "................" ("annoyed", "narrow", "base", "down")
    gen "Why are you being so quiet, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    play background "sounds/slickloop.ogg"
    her @ cheeks blush "......" ("annoyed", "base", "worried", "R_soft")
    her @ cheeks blush "[name_genie_hermione]... I don't think I can..." ("soft", "base", "worried", "down")
    gen "What?" ("base", xpos="far_left", ypos="head")
    stop background
    her @ cheeks blush tears soft "...{w=0.3} Finish..." ("angry", "happyCl", "base", "down")
    gen "Really? Even after all my encouragement?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Your...{w=0.2} {size=-4}(So that's why he said all those things...){/size}" ("angry", "narrow", "base", "down")

    menu:
        "-Chastise her-":
            gen "Well then, I suppose Slytherin will end up winning the house cup this year." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears soft "B-but--" ("disgust", "narrow", "worried", "mid")
            gen "Now, now [name_hermione_genie]... A deal's a deal." ("base", xpos="far_left", ypos="head")
            her @ tears crying "But, I really tried, [name_genie_hermione]!" ("upset", "narrow", "worried", "down")
            gen "You should've tried harder..." ("base", xpos="far_left", ypos="head")
            play background "sounds/slickloopveryfast.ogg"
            her @ tears tears_soft_sweat "" (eyes="happyCl")
            nar "Hermione starts grinding furiously against her hand."

            # Reset pose
            $ hermione.set_pose(None)
            $ hermione.strip("clothes")

            stop background
            her @ cheeks blush tears messy "*SOB*!{w=0.3} I can't..." ("angry", "happyCl", "base", "down")
            gen "Well then... Zero points to Gryffindor." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "{size=-5}After everything I...{/size} Really [name_genie_hermione]?" ("open", "base", "worried", "stare")
            her @ cheeks blush tears messy "After I stood here and..." ("scream", "base", "angry", "mid")
            her @ cheeks blush tears messy ".........." ("angry", "squint", "base", "mid")

            call blkfade
            hide hermione_main
            call her_chibi("stand", "desk", "base")
            $ hermione.wear("all")
            stop music fadeout 2.0

            call hide_blkfade

            her @ cheeks blush tears mascara "I am not going to sell you a single favour anymore, [name_genie_hermione]!" ("scream", "base", "low", "mid")

            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            $ states.her.mood += 15

            pause 1.0
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "We'll see about that." ("base", xpos="far_left", ypos="head")

            $ states.her.status.masturbating = True
            jump end_hermione_event

        "-Forgive her-":
            gen "It's alright, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears crying "Really?" ("open", "narrow", "worried", "mid")
            gen "I'm sure you're just a little nervous." ("base", xpos="far_left", ypos="head")

            # Reset pose
            $ hermione.set_pose(None)
            $ hermione.strip("clothes")

            her @ cheeks blush tears soft "Thank you [name_genie_hermione]." ("base", "base", "worried", "mid")
            her @ cheeks blush "I promise to try harder next time." ("base", "happyCl", "worried", "mid")

    $ states.her.status.masturbating = True
    jump end_hg_pf_strip

### Tier 5 ###

label hg_pf_strip_T5_fingering:
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "I hope you're feeling horny." ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("angry", "narrow", "base", "mid", cheeks="blush")
    gen "Go on...{w=0.4} I can tell when you're not being honest." ("base", xpos="far_left", ypos="head")
    her "I suppose I...{w=0.4} Maybe just a little..." ("angry", "narrow", "base", "mid")
    gen "Good... Then we better do something about that." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "wink", "worried", "mid")
    gen "Why don't you give that lovely pussy of yours a little rub." ("grin", xpos="far_left", ypos="head")
    if not states.her.status.masturbating:
        her "You want me to... Masturbate?" ("angry", "squint", "base", "mid")
        gen "Did you not say you were feeling horny?" ("base", xpos="far_left", ypos="head")
        her "..." ("angry", "narrow", "base", "down")
        gen "You have masturbated before, haven't you?" ("base", xpos="far_left", ypos="head")
        her "Oh--{w=0.2} Of course, I have!" ("angry", "squint", "worried", "mid")
        her "It's just...{w=0.4} Never during circumstances such as this..." ("angry", "narrow", "base", "down")
        gen "Well, that's about to change..." ("base", xpos="far_left", ypos="head")
    her "{heart}{heart}{heart}" ("soft", "narrow", "worried", "down")
    her "............." ("base", "narrow", "worried", "down")
    her "Alright...{w=0.4} if that's what you want..." ("open", "narrow", "base", "down")
    if not states.her.status.masturbating:
        her "(I can't believe I'm agreeing to do this...)" ("soft", "narrow", "base", "down")
    else:
        her "(I can't believe I'm agreeing to do this...{w=0.4} again...)" ("soft", "narrow", "base", "down")

    if hermione.is_worn("panties"):
        nar "Hermione bends over and takes off her panties."
        pause 1.0
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("panties")
        pause 1.0

    if hermione.is_any_worn("clothes"):
        gen "Now take off the rest." ("base", xpos="far_left", ypos="head")
        $ hermione.strip("clothes")

    her "(Okay then, here I go...)" ("normal", "closed", "worried", "mid")

    show screen blkfade
    with d5
    $ hermione.set_pose("hand_on_pussy")

    her "" ("soft", "closed", "worried", "mid", trans=d3)
    play sound "sounds/slick_02.ogg"
    with hpunch
    with kissiris
    her "*Ah*..." ("open", "closed", "worried", "mid")
    call ctc
    hide screen blkfade
    with d5

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "Nice..." ("grin", xpos="far_left", ypos="head")

    play background "sounds/slickloop.ogg" fadein 2
    her "*Mmhh*... {heart}" ("soft", "happyCl", "worried", "mid")
    her "*Ah*...{w=0.4} {heart}-aha..." ("open", "happyCl", "worried", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "*Ah-ah*..." ("open", "happyCl", "worried", "mid")
    gen "......................" ("base", xpos="far_left", ypos="head")
    her "*Ah*...{w=0.4} *Ah*...{heart}" ("open", "happyCl", "worried", "mid")
    her "*Ah*...{w=0.4} [name_genie_hermione]?" ("soft", "wink", "base", "mid")
    gen "What is it?" ("base", xpos="far_left", ypos="head")
    her "Do you....{w=0.4}*Ah*...{w=0.4} like this?" ("angry", "narrow", "base", "R")
    gen "Do I like watching \"you\" finger your cute little pussy?" ("base", xpos="far_left", ypos="head")
    gen "Of course, [name_hermione_genie]... How is that even a question?" ("base", xpos="far_left", ypos="head")
    her "{heart}{heart}{heart}" ("angry", "happyCl", "worried", "mid")
    her "*Ah*... It's just... Well, you were being so quiet..." ("open", "happyCl", "worried", "mid")
    gen "Need some encouragement, do you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Ah*...{w=0.4} I...{w=0.4} I suppose....{heart}" ("angry", "closed", "worried", "down")
    gen "*Tch*... Such a dirty whore..." ("base", xpos="far_left", ypos="head")
    play background "sounds/slickloopfast.ogg"
    $ hermione.set_cum(pussy="wet")
    her "[name_genie_hermione], *Ah*...{heart}" ("grin", "narrow", "base", "up")
    her "Please...{w=0.4} *Ah*...{heart}" ("grin", "narrow", "worried", "stare")
    gen "You deserve to be punished for being such a filthy slut!" ("angry", xpos="far_left", ypos="head")
    her "You shouldn't--{w=0.2} *Ah*...{w=0.4} Say such--{w=0.2} *Ah*...{w=0.4} Things..." ("angry", "happyCl", "base", "mid")
    her "To a student..." ("angry", "happyCl", "base", "up")
    play background "sounds/slickloopveryfast.ogg"
    gen "No?" ("base", xpos="far_left", ypos="head")
    her "*Ah*...{w=0.4} {heart}It's not...{w=0.4} *Ah*...{w=0.4}{heart} Appropriate..." ("soft", "happyCl", "worried", "dead")
    gen "Asking your headmaster to lie isn't appropriate either, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "*Ah-a*...{heart} Yessss..." ("silly", "narrow", "base", "up")
    gen "Yes, you've been a very naughty girl..." ("base", xpos="far_left", ypos="head")
    gen "Now cum for me, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")

    her "{heart}{heart}{heart}!!!{heart}{heart}{heart}" ("grin", "narrow", "annoyed", "up")
    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    $ hermione.set_cum(pussy="squirt")
    pause .8

    $ hermione.set_cum(pussy="squirt_post")
    her @ cheeks blush "*Ah*...{heart}...{heart}" ("grin", "narrow", "annoyed", "up")
    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    $ hermione.set_cum(pussy="squirt_transition")
    pause .8

    $ hermione.set_cum(pussy="squirt_post")
    her "*Ah*... *Ah*...{heart}" ("silly", "base", "base", "ahegao")
    play background "sounds/slickloopfast.ogg"
    her "..." ("open_tongue", "closed", "base", "up")
    her "...{heart}{heart}{heart}" ("grin", "narrow", "annoyed", "dead")
    her "*Gah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("open_tongue", "narrow", "worried", "dead")
    play background "sounds/slickloop.ogg"
    her "[name_genie_hermione]...{heart}{heart}{heart}" ("angry", "narrow", "worried", "mid")
    her "............." ("grin", "closed", "worried", "up", cheeks="none")
    stop background
    nar "Hermione takes a minute to collect herself."

    # Reset pose
    $ hermione.set_pose(None)
    $ states.her.status.masturbating = True
    jump end_hg_pf_strip

### Tier 6 ###

label hg_pf_strip_T6_fingering:

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("soft", "base", "base", "mid")
    gen "How often do you pleasure yourself?" ("base", xpos="far_left", ypos="head")
    her "Oh... *Ehm*... Well, I'm not sure how to answer that question, [name_genie_hermione]..." ("open", "narrow", "base", "down", cheeks="blush")
    gen "Truthfully, of course." ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]... Although that's not exactly what I meant..." ("soft", "closed", "base", "down")
    gen "Then let me be more specific... How many times have you masturbated this past week?" ("base", xpos="far_left", ypos="head")
    her "Oh, well... That's easier to answer... I've done it two times--" ("open", "narrow", "base", "down")
    gen "This week?" ("base", xpos="far_left", ypos="head")
    her "Today..." ("open", "base", "base", "R")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    her "Yes... How many times I do it each week varies, depending on whether or not I am spending time in here." ("open", "closed", "base", "mid")
    gen "You don't say..." ("base", xpos="far_left", ypos="head")
    gen "Then what's your record?" ("base", xpos="far_left", ypos="head")
    her "My what, sorry?" ("angry", "base", "base", "mid")
    gen "Your record, [name_hermione_genie]... Go on... Everyone has one..." ("base", xpos="far_left", ypos="head")
    her "Well, I'm not sure if I've ever noted down..." ("annoyed", "squint", "base", "R")
    gen "Please... You're telling me that \"the Hermione Granger\", is not keeping track of everything that she does? And here I thought--" ("base", xpos="far_left", ypos="head")
    her "Five times in one day!" ("open", "happyCl", "base", "mid")
    gen "Shut the front door... Surely, you must be lying!" ("base", xpos="far_left", ypos="head")
    gen "(Wait, is she talking about orgasms in one session, or how many sessions?)" ("base", xpos="far_left", ypos="head")
    her "Of course I'm not lying, [name_genie_hermione]... Schoolwork requires a clear state of mind." ("annoyed", "wink", "base", "mid")
    her "I spend an average of twelve minutes per session, so any more than five a day would be detrimental." ("open", "closed", "worried", "mid")
    gen "Detrimental to what? Your well-being?" ("base", xpos="far_left", ypos="head")
    gen "(Should I be worried?)" ("base", xpos="far_left", ypos="head")
    her  "Not my well-being, [name_genie_hermione]... If I did it any more, I would miss my classes." ("angry", "squint", "base", "mid")
    gen "Oh, good thing I didn't swap places with some student..." ("base", xpos="far_left", ypos="head")
    her "Swap places?" ("soft", "base", "base", "mid")
    gen "So... Twelve minutes per session, you say... Well, that won't do..." ("base", xpos="far_left", ypos="head")
    if not states.her.status.masturbating:
        gen "Perhaps you better show me how you do it, and we could bring that number down to five minutes..." ("base", xpos="far_left", ypos="head")
        her "I suppose I could do that..." ("soft", "narrow", "base", "down")
        gen "Great, then show me how you do it... And the timer starts... Now!" ("base", xpos="far_left", ypos="head")
    else:
        gen "Perhaps if you showed me how you do it again, then we could bring that number down to five minutes..." ("base", xpos="far_left", ypos="head")
        her "*Hmm*... I suppose that's not too bad of an idea..." ("soft", "narrow", "base", "down")
        gen "Great! Timer starts... Now!" ("grin", xpos="far_left", ypos="head")

    $ _start_time = datetime.datetime.now()

    her  "..." ("base", "narrow", "base", "down")
    if hermione.is_worn("panties"):
        nar "Hermione hastily takes off her panties."
        pause 1.0
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("panties")
        pause 1.0

    if hermione.is_any_worn("clothes"):
        gen "Now take off the rest." ("base", xpos="far_left", ypos="head")
        $ hermione.strip("clothes")

    her "(...)" ("base", "happyCl", "worried", "mid")

    show screen blkfade
    with d5
    $ hermione.set_pose("hand_on_pussy")
    her "" ("soft", "closed", "worried", "mid", trans=d3)
    play sound "sounds/slick_02.ogg"
    with hpunch
    with kissiris
    her "*Ah*..." ("open", "squint", "worried", "R")
    call ctc
    hide screen blkfade
    with d5


    stop music fadeout 3.0
    play background "sounds/slickloop.ogg" fadein 2

    her "*Mmmh*...{heart}" ("base", "narrow", "base", "down")
    her "[name_genie_hermione]...{w=0.4} What do you think, when I do it like this?" ("grin", "narrow", "base", "down")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.

    gen "Pleasurable to look at, but I'm sure you can do better..." ("base", xpos="far_left", ypos="head")
    gen "When you're in a hurry, you should try going a little deeper with your fingers." ("base", xpos="far_left", ypos="head")
    her "Alright, [name_genie_hermione]..." ("base", "happyCl", "base", "mid")
    play background "sounds/slickloopfast.ogg"
    her "*Ah*...{w=0.4} *Ah*...{w=0.4}{heart}" ("open", "happyCl", "worried", "mid")
    $ hermione.set_cum(pussy="wet")
    her "*Ah*...{w=0.6} [name_genie_hermione]...{heart}" ("open", "happyCl", "worried", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Tell me what you're thinking about.\"":
            her "*Huh*?" ("open", "wink", "worried", "mid")
            her "Oh, *umm*... Nothing..." ("soft", "happyCl", "worried", "mid")
            gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione],{w=0.4} it's a bit weird..." ("disgust", "narrow", "base", "down")
            gen "Even more reason to tell me." ("angry", xpos="far_left", ypos="head")
            her "......" ("annoyed", "narrow", "annoyed", "mid")
            her "Fine..." ("open", "base", "base", "R")
            her "If you must know...{w=0.4} I was thinking about the time I corrected professor Snape on the ingredients of a \"Hiccoughing Solution\"." ("open", "narrow", "worried", "down")
            gen "....." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{heart}" ("soft", "narrow", "annoyed", "up")
            her "It was--{w=0.2} *Ah*...{w=0.4} {heart} in front of the entire class as well." ("soft", "narrow", "annoyed", "up")
            her "He refused to let me answer any questions for a week after that." ("base", "narrow", "worried", "down")
            her "But it was worth it..." ("soft", "happy", "base", "R")
            her "The look on his face when he realised he was wrong...{heart}" ("soft", "narrow", "annoyed", "up")
            her "*A-ah*...{heart}"
            her "It just felt so good!{heart}" ("grin", "narrow", "base", "dead")
            gen "This is what you're thinking of when masturbating?" ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "dead")
            her "Is that too weird?" ("upset", "narrow", "base", "mid")
            gen "(No wonder why she's being such a know-it-all... She's getting off from it.)" ("base", xpos="far_left", ypos="head")
            gen "Let's just get back to business, shall we?" ("base", xpos="far_left", ypos="head")
            her "................." ("base", "closed", "worried", "up")
            nar "Hermione goes quiet for a moment to enjoy herself, now fully focused on moving her fingers."

        "\"You really are a shameless slut, aren't you?\"":
            her "*Ah*...{w=0.4} [name_genie_hermione].{heart}" ("angry", "narrow", "base", "dead")
            gen "Go on, [name_hermione_genie]... Time's ticking..." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{w=0.4} Right..." ("soft", "closed", "worried", "dead")
            her "Yes, maybe I am a slut after all, [name_genie_hermione]..." ("angry", "narrow", "base", "dead")
            her "Perhaps the time that I spent with you, made me this way...{heart}" ("angry", "narrow", "worried", "dead")
            her "Or perhaps I've always been like this...{heart}" ("disgust", "narrow", "base", "down")
            her "..." ("base", "closed", "worried", "down")
            gen "Very good, [name_hermione_genie]... Keep talking like that, and you'll get there a lot sooner..." ("base", xpos="far_left", ypos="head")
            her "Yes... {heart} {w=0.4}*Ah*...{w=0.4} {heart}I...{w=0.4} I'm a slut, [name_genie_hermione]...{heart}" ("soft", "closed", "annoyed", "up")
            play background "sounds/slickloopfast.ogg"
            her "A shameless, naughty slut..." ("grin", "narrow", "base", "up")
            her "Who doesn't mind pleasuring herself...{heart} {w=0.4}*Ah*..." ("soft", "narrow", "worried", "up")
            her "If it makes her headmaster happy..." ("grin", "narrow", "base", "dead")
            gen "Really now..." ("base", xpos="far_left", ypos="head")
            her "Yes, [name_genie_hermione]..." ("base", "narrow", "worried", "down")
            her "Please enjoy yourself while I'm--" ("soft", "narrow", "base", "down")
            her "*Ah*...{heart}" ("open_wide_tongue", "narrow", "worried", "up")
            her "Fingering my pussy..." ("grin", "narrow", "worried", "up")
            her "It makes me--{w=0.2} *Ah*...{w=0.4} Happy..." ("silly", "closed", "base", "up")
            her "*Ah*...{w=0.4} *Ah*...{heart}" ("grin", "narrow", "annoyed", "up")
            her "*Ah*...{w=0.4} Do you.... like this, [name_genie_hermione]?" ("shock", "happyCl", "worried", "mid")
            her "Watching me--{w=0.4}*Ah*...{w=0.4}{heart} degrade myself?" ("angry", "narrow", "base", "dead")
            gen "Very much, [name_hermione_genie]... Just keep going..." ("base", xpos="far_left", ypos="head")
            her "{heart}{heart}{heart}" ("soft", "narrow", "base", "dead")

        "\"Play with your tits!\"":
            her "*Hmm*?" ("soft", "narrow", "worried", "up")
            her "Okay...{w=0.4} If you think that will help..." ("base", "narrow", "base", "up")

            stop background
            $ hermione.set_pose("hand_on_breast")

            her "*Ah*...{heart}" ("grin", "narrow", "base", "dead")
            gen "Now pinch your nipple." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]..." ("angry", "narrow", "base", "down")
            gen "Do it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "..." ("base", "narrow", "base", "down")
            play sound "sounds/gasp2.ogg"
            her "*Ah*..." ("grin", "narrow", "base", "up")
            gen "..." ("grin", xpos="far_left", ypos="head")
            nar "You gaze at Hermione's breasts, as she runs the tips of her fingers across her nipple..."
            her "*Ah*..." ("silly", "narrow", "base", "dead")
            gen "So, you do like playing with those big tits of yours..." ("grin", xpos="far_left", ypos="head")
            her "Well, I--{w=0.2} *Ah*...{heart}" ("soft", "narrow", "annoyed", "up")
            her "I don't know why..." ("base", "narrow", "base", "dead")
            her "But it feels really good...{heart}{heart}" ("open", "closed", "worried", "down")
            gen "You nasty slut!" ("base", xpos="far_left", ypos="head")
            her "*Ah*...{w=0.4}{heart} *Ah-a*...{heart}" ("open_tongue", "narrow", "annoyed", "up")
            gen "Go on, [name_hermione_genie]... Say it!" ("base", xpos="far_left", ypos="head")
            her "I... I am..." ("angry", "narrow", "annoyed", "up")
            her "A slut...{w=0.4} *Ah*...{heart}" ("grin", "narrow", "base", "dead")
            gen "You are a disgrace, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her "*Ah-ah*...{heart}{heart}{heart}" ("open_wide_tongue", "narrow", "worried", "up")

    gen "Why don't you come down, and I'll help you finish?" ("base", xpos="far_left", ypos="head")
    her "..." ("base", "narrow", "base", "stare")

    # Hermione climbs off your desk.
    show screen blkfade
    with d5
    hide hermione_main
    play sound "sounds/08_hop_on_desk.ogg"
    stop background
    nar "Hermione gingerly climbs down from the desk, and stands in front of you."
    pause.5

    # Reset pose
    $ hermione.set_pose(None)
    $ hermione.strip("clothes")

    call her_chibi_scene("behind_desk_front")

    hide screen blkfade
    with d5
    call ctc

    her ".............." ("base", "narrow", "base", "up", trans=d3)

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Grab her tits-":
            nar "You reach forward and grab a hold of Hermione's tits."

            call her_chibi_scene("grope_tits")

            her "[name_genie_hermione]!" ("angry", "happyCl", "worried", "mid")
            her "How is this going to help me finish faster?" ("open", "narrow", "worried", "mid")
            her "I was almost there..." ("annoyed", "narrow", "worried", "R")
            gen "Would you rather not trade speed for a stronger orgasm, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            gen "This way, you won't need to do it as many times today..." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{w=0.4} Truly? Well, I suppose--{w=0.2} *Ngh*...{w=0.4} I suppose you're the expert..." ("open", "closed", "base", "up")
            her "But it--{w=0.2} *Ah*...{w=0.4}{heart} better work..." ("open", "narrow", "base", "up")
            nar "You give her tits a couple of firm squeezes..."
            gen "Now tell me how much you love this." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{w=0.4} Fine...{heart}" ("open", "happyCl", "worried", "mid")
            her "{size=-5}I like it...{/size}" ("soft", "narrow", "worried", "down")
            gen "What was that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "......." ("normal", "narrow", "annoyed", "up")
            her "I love it..." ("annoyed", "closed", "worried", "dead")
            gen "What do you love?" ("base", xpos="far_left", ypos="head")
            her "Standing here... All exposed..." ("base", "narrow", "worried", "down_soft")
            her "*Ah*...{w=0.4} While you play with me...{heart}" ("soft", "closed", "worried", "up")
            gen "*Heh*... Nice." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{heart}" ("open", "narrow", "base", "up")
            her "I sometimes wish I could spend all day in here..." ("open", "narrow", "worried", "dead")
            gen "Perhaps we could arrange that some time..." ("base", xpos="far_left", ypos="head")
            nar "You keep on massaging the girl's breasts..."
            her "......." ("grin", "narrow", "angry", "dead")
            her "[name_genie_hermione]... I...{w=0.4} Please...{w=0.4} I was so close..." ("open", "narrow", "worried", "up")
            her "*Ah*...{heart}" ("angry", "narrow", "worried", "up")
            her "Please...{w=0.4} You're just teasing me..." ("angry", "narrow", "base", "up")
            gen "What was that, [name_hermione_genie]? You'll have to speak up." ("base", xpos="far_left", ypos="head")
            her "Please, [name_genie_hermione]...{w=0.4} Let me finish..." ("open", "narrow", "base", "up")
            gen "Why, I believe I'm the one in control at this current time, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "*Ah*...{heart} {size=+5}Then, please finger my pussy!{/size}" ("scream", "happyCl", "base", "up")
            gen "As you wish..." ("base", xpos="far_left", ypos="head")
            call her_chibi_scene("grope_ass_front")
            with vpunch
            play sound "sounds/slick_02.ogg"
            play background "sounds/slickloopfast.ogg"
            nar "As you put your fingers against Hermione's slit, she suddenly pounds herself down to the base of your fingers."

        "-Finger her-":

            call her_chibi_scene("grope_ass_front")

            nar "You run your hands up and down Hermione's legs..."
            her "..." ("base", "narrow", "worried", "dead")
            nar "And then slowly move your them towards her pussy..."
            her "................." ("grin", "narrow", "base", "up")
            gen "That's it, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "{size=-7}[name_genie_hermione]...{/size}" ("soft", "narrow", "worried", "up")
            gen "Good girl." ("base", xpos="far_left", ypos="head")
            her "...................." ("base", "narrow", "base", "up")
            gen "Don't talk... Just focus on my touch..." ("base", xpos="far_left", ypos="head")
            nar "You stroke the inside of Hermione's thighs..."
            nar "While gently kneading her, you move ever so closer to her wet pussy..."
            nar "As you're just about to touch it, you suddenly move your hands around her back and squeeze her ass..."
            her "" ("angry", "wide", "annoyed", "dead")
            gen "I love your big... firm, ass..." ("base", xpos="far_left", ypos="head")
            her "....................." ("annoyed", "base", "annoyed", "dead")
            gen "Your loins..." ("base", xpos="far_left", ypos="head")
            nar "You slide your fingers along the side of her legs, and then gently begin rubbing your forefinger just above her clit."
            her ".....................{size=-8} [name_genie_hermione]...{/size}" ("silly", "narrow", "base", "dead")
            gen "What was that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "....................." ("angry", "narrow", "base", "dead")
            her "... I...{w=0.4} {size=-5}... I need you...{w=0.4} inside of me...{/size}" ("angry", "narrow", "base", "up")
            gen "You'll have to speak up if you expect me to hear you..." ("base", xpos="far_left", ypos="head")
            her "I...{w=0.4} *Ah*...{w=0.4}{heart} need..." ("open", "narrow", "base", "up")
            nar "You swiftly plunge two fingers into her drenched pussy."
            play sound "sounds/slick_02.ogg"
            her "!!!{heart}{heart}" ("grin", "narrow", "worried", "up")
            nar "You start pumping your fingers inside her before she can do more than gasp."
            play background "sounds/slickloop.ogg"
            her "{size=+10}{heart}{heart}!!!{heart}{heart}{/size}" ("silly", "narrow", "base", "dead")
            gen "That's it, [name_hermione_genie]... You've deserved this..." ("base", xpos="far_left", ypos="head")
            her ".................................................." ("base", "narrow", "base", "up")
            gen "Tell me... Do you like this?" ("base", xpos="far_left", ypos="head")
            gen "Do you like it when I finger your pussy?" ("base", xpos="far_left", ypos="head")
            her "I..." ("angry", "narrow", "base", "dead")
            stop background
            nar "You suddenly pull your fingers out of Hermione..."
            her @ cheeks blush "Please don't stop, [name_genie_hermione]!{heart}{w=0.4} I...{w=0.4} I love it! I love your fingers inside my pussy!!{heart}" ("angry", "happyCl", "worried", "up")
            gen "Well, I don't know, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her "{size=+10}Please [name_genie_hermione]!!!{/size}" ("open", "happyCl", "worried", "up")
            with vpunch
            play sound "sounds/slick_02.ogg"
            play background "sounds/slickloopfast.ogg"
            nar "As you put your fingers back against Hermione's slit, she suddenly pounds herself down to the base of your fingers."

    her "*Ah*...{heart}{w=0.4} please...{w=0.4}{heart} keep...{heart}" ("silly", "narrow", "base", "dead")
    her "Fingering my pussy!{heart}{heart}" ("silly", "narrow", "annoyed", "up")
    gen "You naughty girl!" ("grin", xpos="far_left", ypos="head")
    nar "You begin fingering Hermione with renewed effort..."
    play sound "sounds/slick_02.ogg"
    play background "sounds/slickloopveryfast.ogg"
    her "*Ah*...{w=0.4} yes! {heart}iloveitiloveitiloveit!{heart}" ("scream", "wide", "worried", "dead")
    gen "What do you love, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Ah!!{heart} I love your fingers inside my pussy, [name_genie_hermione]!{heart}" ("open_wide_tongue", "narrow", "worried", "up")
    nar "Hermione's legs begin to shake slightly as you push your fingers down to the hilt."
    gen "Are you about to--" ("base", xpos="far_left", ypos="head")
    her "*Ah*...{heart} Yes!!" ("mad", "narrow", "annoyed", "dead")
    her "I'm gonna cum, [name_genie_hermione]!!{heart}" ("grin", "narrow", "base", "dead")
    her "From being fucked by your fingers!!{heart}{heart}" ("open_tongue", "base", "base", "ahegao")
    her "*Ah*...{w=0.4} Yes...{w=0.4}*Ah*..." ("smile", "narrow", "base", "up")
    her "[name_genie_hermione]{heart}... I'm--{w=0.2} *Ah*...{w=0.4} I'm cumming!{heart}" ("silly", "narrow", "annoyed", "dead")

    her @ cheeks blush "{heart}{heart}{heart}!!!{heart}{heart}{heart}" ("silly", "narrow", "base", "dead")
    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    $ hermione.set_cum(pussy="squirt")
    pause .8

    $ hermione.set_cum(pussy="squirt_post")

    her @ cheeks blush "*Ah*...{w=0.4}{heart}...{heart}" ("grin", "squint", "worried", "ahegao")
    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    $ hermione.set_cum(pussy="squirt_transition")
    pause .8

    $ hermione.set_cum(pussy="squirt_post")

    her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{heart}" ("silly", "narrow", "annoyed", "dead")
    $ hermione.set_cum(pussy="squirt_transition")
    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    pause .8

    $ hermione.set_cum(pussy="squirt_post")

    her @ cheeks blush "*Mmmmmmh*!!!" ("grin", "narrow", "annoyed", "up")
    her @ cheeks blush "........................" ("grin", "narrow", "worried", "up")
    stop background

    nar "You take your hands off Hermione pussy and then wipe her love-juices across the side of her leg."

    call her_chibi_scene("behind_desk_front")

    $ _end_time = datetime.datetime.now()
    $ _time_difference = (_end_time - _start_time).total_seconds()

    if _time_difference < 60:
        gen "I'm not sure how you did it, but you finished in less than a minute." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} Really?" ("grin", "narrow", "base", "mid")
        gen "Yes... If I didn't see it happen myself, I would've thought you cheated somehow..." ("base", xpos="far_left", ypos="head")
    elif _time_difference < 360:
        gen "You finished in under six minutes... Very impressive." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} Thank you..." ("base", "narrow", "base", "down")
    elif _time_difference < 720:
        gen "Looks like you finished under your average time... Congratulations." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} Thank you..." ("base", "narrow", "base", "down")
    elif _time_difference < 3600:
        gen "Good girl..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} Thank you, [name_genie_hermione]..." ("base", "narrow", "base", "mid")
        gen "That said... it appears you didn't beat your average time..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh..." ("base", "narrow", "base", "down")
        gen "No worries...{w=0.4} There's always next time." ("base", xpos="far_left", ypos="head")
    else:
        gen "I'm not exactly sure how this happened..." ("base", xpos="far_left", ypos="head")
        gen "But you were masturbating for over an hour..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} But--{w=0.2} *Ah*...{w=0.4} How is that even possible?" ("base", "narrow", "base", "mid")
        gen "I'm not sure... Maybe the player just left for a bit..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*...{w=0.4} Who--{w=0.2} Who are you talking about, [name_genie_hermione]?" ("soft", "narrow", "base", "mid")
        gen "Don't worry about it..." ("base", xpos="far_left", ypos="head")

    gen "Alright then, [name_hermione_genie]... If you're finished..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Ah*...{w=0.4} *Ah*...{heart}" ("grin", "narrow", "worried", "dead")
    her @ cheeks blush "Yes...{w=0.4} yes, [name_genie_hermione]...{w=0.4} Just give me a moment...{heart}" ("base", "narrow", "base", "up")
    her @ cheeks blush "(How will I ever be able to achieve this... on my own...{heart})" ("soft", "narrow", "base", "down")
    her "" ("soft", "narrow", "base", "down", cheeks="none")

    $ states.her.status.masturbating = True

    jump end_hg_pf_strip
