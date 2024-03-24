

### Tier 2 ###

label hg_pf_grope_ass_T2:
    stop music fadeout 5.0
    call her_chibi_scene("grope_ass_front", trans=d7)

    her @ cheeks blush "[name_genie_hermione]!?" ("mad", "wide", "base", "stare", ypos="head", flip=False)
    gen "Relax, [name_hermione_genie]. It will be the easiest {number=current_payout} points you've ever made, I promise." ("base", xpos="far_left", ypos="head")
    gen "All I am going to do is squeeze your little butt a couple of times..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "No! I demand you to stop!" ("scream", "closed", "angry", "mid")

    call her_chibi_scene("behind_desk_front", trans=d5)

    her @ cheeks blush "This is inappropriate, [name_genie_hermione]................" ("angry", "closed", "angry", "mid")
    gen "Nobody needs to know how exactly you got the points..." ("base", xpos="far_left", ypos="head")
    her "But..." ("annoyed", "base", "angry", "mid")
    gen "Do it for {i}gravenboor{/i}..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "(These {number=current_payout} points could really make a difference...)" ("disgust", "narrow", "base", "down")
    her @ cheeks blush "(Darn it.....!)" ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "(...............................)" ("annoyed", "narrow", "angry", "R")

    her @ cheeks blush "Can I at least turn around then, Sir?" ("soft", "base", "angry", "mid")

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

        "\"Yes. Turn around, [name_hermione_genie].\"": # Can fail
            jump hg_pf_grope_ass_T2_back

        "\"No. Just stand still, [name_hermione_genie].\"": # Fails
            jump hg_pf_grope_ass_T2_front

label hg_pf_grope_ass_T2_front:
    call her_chibi_scene("behind_desk_front", trans=d7)

    her @ cheeks blush "(...)" ("disgust", "narrow", "worried", "down", ypos="head", flip=False)

    call her_chibi_scene("grope_ass_front", trans=d5)
    call ctc

    her @ cheeks blush "(...)" ("disgust", "narrow", "base", "down")
    her @ cheeks blush "I'm sorry, [name_genie_hermione]. But I can't do this!" ("soft", "narrow", "base", "down")

    call her_chibi_scene("behind_desk_front", trans=d7)
    gen "Can't do what, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "I can't do it when I can see you looking at me..." ("mad", "happyCl", "worried", "mid")
    gen "That's the whole point [name_hermione_genie], I want to look at you..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "............." ("annoyed", "base", "worried", "mid")

    show screen blkfade
    with d3

    nar "Hermione moves your hand away and rushes to the front of your desk."

    call her_chibi_scene("reset", "desk", "base")
    hide screen blkfade
    with d3

    gen "What's the problem [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It's demeaning!" ("angry", "closed", "angry", "mid")
    gen "Wouldn't it be worse if I didn't want to look at you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*ARGH* Whatever!!!" ("scream", "base", "angry", "mid")

    her @ cheeks blush "Good day, Sir." ("disgust", "narrow", "angry", "R")

    call her_walk(action="leave")

    $ states.her.mood += 4

    jump end_hermione_event

label hg_pf_grope_ass_T2_back:
    call her_chibi_scene("behind_desk_front", trans=d7)

    her @ cheeks blush "As you say, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")

    call her_chibi_scene("behind_desk_back", trans=d5)
    call ctc

    her @ cheeks blush "............." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "..........................." ("annoyed", "base", "angry", "mid")
    her @ cheeks blush "[name_genie_hermione], I would like to be done with this sooner rather than later..." ("soft", "closed", "angry", "mid")
    gen "Don't rush me [name_hermione_genie]... Let me savour the moment..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "............................." ("annoyed", "narrow", "angry", "R")

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "-Give her butt a squeeze-":
            jump hg_pf_grope_ass_T2_continue

        "-Give her butt a slap-":
            $ states.her.mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    her @ cheeks blush "!!!!!!!!!!!!!" ("scream", "wide", "base", "stare")
    her @ cheeks blush "[name_genie_hermione]!!?" ("scream", "wide", "base", "stare")

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            her @ cheeks blush "......................." ("annoyed", "narrow", "angry", "R")

            jump hg_pf_grope_ass_T2_continue

        "-Give her butt another slap-":
            $ states.her.mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    her @ cheeks blush "!!!!!!!!!!!!!" ("scream", "wide", "base", "stare")
    her @ cheeks blush "[name_genie_hermione], what are you doing!?" ("angry", "closed", "angry", "mid")
    her @ cheeks blush "You said all you were going to do is touch!" ("angry", "base", "angry", "mid")

    menu:
        "\"Alright, alright... stop making a scene....\"":
            her @ cheeks blush "......................." ("annoyed", "narrow", "angry", "R")

            jump hg_pf_grope_ass_T2_continue

        "-Give her butt another slap-":
            $ states.her.mood += 2
            pass

    # Slap her!
    call slap_her #Calls slapping sound and visual.
    her @ cheeks blush "Ouch! It hurts!" ("angry", "closed", "angry", "mid")
    her @ cheeks blush "This is so demeaning!" ("angry", "base", "angry", "mid")
    her @ cheeks blush "You said all you were going to do is touch..." ("angry", "base", "angry", "mid")
    gen "Just stand still, [name_hermione_genie]!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "I don't think so, [name_genie_hermione]!" ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "No amount of points is worth this humiliation!" ("scream", "base", "angry", "mid",emote="angry")
    her @ cheeks blush "You are abusing your power, [name_genie_hermione]!" ("scream", "base", "angry", "mid",emote="angry")
    gen "What?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "I'm leaving!" ("angry", "happyCl", "worried", "mid", ypos="head", flip=False)

    call her_chibi_scene("reset", "desk", "base", trans=fade)

    # Hermione gets mad
    menu:
        gen "*Tsk*..." ("angry", xpos="far_left", ypos="head")
        "\"I... I apologise...\"":
            gen "...... It's not my fault......" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "An apology won't be enough, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
            gen "What else do you want? More points?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes, I believe I'm owed at least that much!" ("angry", "base", "angry", "mid")
            gen "{number=current_payout} is what we agreed on. You won't get any more than that." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Tzzh*... Fine!" ("clench", "closed", "angry", "mid")
            her @ cheeks blush "Keep your points." ("angry", "base", "angry", "mid")
            her @ cheeks blush "All of them! I don't even want them anymore." ("scream", "closed", "angry", "mid")
            gen "Are you sure about that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm leaving. Good day, Sir." ("angry", "base", "angry", "mid")

            call her_walk(action="leave")

            gen "(Whatever...)" ("base", xpos="far_left", ypos="head")

            $ states.her.mood += 15

            jump end_hermione_event

        "\"You are not getting any points for this!\"":
            her @ cheeks blush "Hah! See if I care, [name_genie_hermione]!" ("angry", "base", "angry", "mid")

            call her_walk(action="leave")

            gen "*Tsk!* (You brat!)" ("angry", xpos="far_left", ypos="head")

            $ states.her.mood += 20

            jump end_hermione_event

        "\"I'm subtracting points from you then!\"":
            her @ cheeks blush "You can't be serious!?" ("scream", "wide", "base", "stare")
            gen "The Gryffindor house, minus ten points!" ("angry", xpos="far_left", ypos="head")
            gen "There! It's done!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "*Grr*..........." ("angry", "base", "angry", "mid")
            her @ cheeks blush "........................" ("angry", "base", "angry", "mid")
            her @ cheeks blush tears messy "This is not fair..." ("angry", "squint", "base", "mid")
            gen "What? Hey, wait, don't you start crying on me..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush tears messy "I hate you, [name_genie_hermione]! I hate you!" ("scream", "happyCl", "worried", "mid")

            # Hermione runs out of the room.
            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            gen "(..............)" ("base", xpos="far_left", ypos="head")

            menu:
                "\"Dammit. Now I feel like crap...\"":
                    gen "(But who could resist slapping that little behind of hers?)" ("grin", xpos="far_left", ypos="head")
                "\"She made me do this!\"":
                    gen "(Acting all wounded now...)" ("base", xpos="far_left", ypos="head")
                    gen "(I bet she actually enjoyed the slapping and just won't admit it...)" ("grin", xpos="far_left", ypos="head")

            $ gryffindor -=10
            $ states.her.mood += 30

            jump end_hermione_event

label hg_pf_grope_ass_T2_continue:
    call her_chibi_scene("grope_ass_back")
    with d7
    call ctc

    her @ cheeks blush ".............." ("annoyed", "narrow", "angry", "R")
    nar "*Squeeze* *Squeeze* *Squeeze*..."

    her @ cheeks blush "........................." ("annoyed", "base", "angry", "mid")
    her @ cheeks blush "(I can't believe this is really happening...)" ("disgust", "happyCl", "worried", "mid")
    her @ cheeks blush "If you don't mind, Sir..." ("soft", "happyCl", "worried", "mid")
    her @ cheeks blush "I'd like you to unhand me now..." ("disgust", "base", "worried", "mid")
    gen "What? Already?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes! This has been demeaning enough!" ("annoyed", "base", "angry", "mid")
    her @ cheeks blush "Please let go of me, Sir." ("soft", "base", "angry", "mid")
    gen "Fine..." ("base", xpos="far_left", ypos="head")
    nar "You give her butt one last squeeze..."
    her @ cheeks blush "..................." ("annoyed", "narrow", "angry", "R")

    jump end_hg_pf_grope

### Tier 3 ###

label hg_pf_grope_ass_T3:
    call her_chibi_scene("behind_desk_front", trans=d7)

    her @ cheeks blush "Do you want me to turn around then, [name_genie_hermione]?" ("base", "base", "base", "R", ypos="head", flip=False)

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "\"Yes. Turn around, [name_hermione_genie].\"":
            her @ cheeks blush "As you say, [name_genie_hermione]..." ("base", "base", "base", "R")

            jump hg_pf_grope_ass_T3_back

        "\"No. Just stand still, [name_hermione_genie].\"":
            her @ cheeks blush "As you say, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")

            jump hg_pf_grope_ass_T3_front

label hg_pf_grope_ass_T3_front:
    call her_chibi_scene("behind_desk_front")
    with d7
    call ctc

    her @ cheeks blush "[name_genie_hermione], please hurry up, before someone discovers us like this..." ("soft", "base", "base", "R", ypos="head", flip=False)
    gen "What's the problem, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    gen "You're just doing something to help your house." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I do know." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "But not everyone would see it that way..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "So let us be done with this as quickly as possible..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "Please..." ("open", "base", "base", "R")
    gen "Well, if you insist..." ("base", xpos="far_left", ypos="head")

    call her_chibi_scene("grope_ass_front")
    with d7

    her @ cheeks blush "!!!" ("mad", "wide", "base", "stare")
    gen "What is it?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "N-nothing, [name_genie_hermione]. Your hands are cold, that's all..." ("open", "base", "base", "R")

    nar "You run your hands up and down Hermione's legs..."
    her @ cheeks blush "........................." ("annoyed", "narrow", "angry", "R")

    nar "And give her Ass a good squeeze..."
    her @ cheeks blush "................." ("angry", "happyCl", "worried", "mid")
    gen "Don't look away, girl. I want you to look into my eyes." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I would rather not, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Fine. Just keep on standing still then.\"":
            her @ cheeks blush "Thank you, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", ypos="head", flip=False)

            nar "You massage her ass-cheeks lightly..."
            her @ cheeks blush "...................." ("angry", "happyCl", "worried", "mid")

            nar "And keep enjoying the sensation of her butt under your hands..."
            her @ cheeks blush "....................." ("angry", "happyCl", "worried", "mid")

            nar "Then You give Hermione's butt one last squeeze."
            her @ cheeks blush "....................." ("angry", "happyCl", "worried", "mid")

            jump end_hg_pf_grope

        "\"Open your eyes, or you'll lose the points!\"":
            $ states.her.mood += 10

            her @ cheeks blush "*Tsk*! {size=-5}(You wretched old--){/size}" ("angry", "happyCl", "worried", "mid", ypos="head", flip=False)
            gen "Did you say something, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "It's nothing, [name_genie_hermione]." ("angry", "base", "angry", "mid")

            nar "You massage her ass-cheeks lightly..."
            nar "Hermione maintains eye contact, doing as she's been told..."

            her "...................." ("angry", "base", "angry", "mid")
            her @ cheeks blush "..............................." ("annoyed", "narrow", "angry", "R")
            gen "What did I tell you about looking away?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes, I remember..." ("angry", "happyCl", "worried", "mid")
            her "................................." ("angry", "base", "angry", "mid")
            her @ cheeks blush "..................................." ("annoyed", "narrow", "angry", "R")
            her @ cheeks blush ".................................................." ("annoyed", "narrow", "angry", "R")

            nar "You keep enjoying the sensation of her soft buttocks under your fingertips..."
            her "....................." ("angry", "base", "angry", "mid")

            nar "Then You give Hermione's butt one last squeeze."
            her @ cheeks blush "....................." ("annoyed", "base", "angry", "mid")

            jump end_hg_pf_grope

label hg_pf_grope_ass_T3_back:
    call her_chibi_scene("behind_desk_back", trans=d7)
    call ctc

    her @ cheeks blush "............." ("base", "narrow", "base", "up")

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "-Give her butt a squeeze-":
            jump hg_pf_grope_ass_T3_continue

        "-Give her butt a slap-":
            call slap_her
            her @ cheeks blush "!!!!!!!!!!!!!" ("scream", "wide", "base", "stare")
            her @ cheeks blush "[name_genie_hermione]....?" ("angry", "base", "base", "R")

            pass

    menu:
        "\"Fine, fine... I just couldn't resist....\"":
            her @ cheeks blush "It's okay..." ("base", "base", "base", "R")

            jump hg_pf_grope_ass_T3_continue

        "-Give her butt another slap-":
            call slap_her
            her @ cheeks blush "!!!!!!!!!!!!!" ("scream", "wide", "base", "stare")
            her @ cheeks blush "[name_genie_hermione], what are you doing!?" ("angry", "base", "base", "R")
            her @ cheeks blush "You said that all you were going to do is touch!" ("open", "narrow", "base", "R")

            pass

    menu:
        "\"Alright, alright...\"":
            her @ cheeks blush "It's not a big deal..." ("base", "base", "base", "R")

            jump hg_pf_grope_ass_T3_continue

        "-Give her butt yet another slap-":
            call slap_her

            her @ cheeks blush "[name_genie_hermione], not so loudly, please..." ("silly", "narrow", "base", "up")
            her @ cheeks blush "What if somebody hears us?" ("silly", "narrow", "base", "up")
            gen "Alright, alright... proceeding with groping then..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "................" ("base", "narrow", "base", "stare")

            jump hg_pf_grope_ass_T3_continue

label hg_pf_grope_ass_T3_continue:
    call her_chibi_scene("grope_ass_back")
    with d7
    call ctc

    her @ cheeks blush "..................." ("base", "base", "base", "R", ypos="head", flip=False)
    gen "You are being awfully quiet today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Am I...?" ("base", "base", "base", "R")

    if states.her.tier <= 5:
        her @ cheeks blush "Well, you know me, [name_genie_hermione]..." ("base", "narrow", "base", "up")
        her @ cheeks blush "I'm just happy to be able to do my part for the Gryffindor house..." ("base", "narrow", "base", "up")
    else:
        her @ cheeks blush "Please don't mind it and continue..." ("base", "narrow", "base", "up")
        her @ cheeks blush "(... to grope me...)" ("base", "narrow", "base", "mid_soft")

    nar "You keep on playing with Hermione's ass..."
    nar "And continue sliding your hands up and down her inner thighs..."

    her @ cheeks blush "................" ("base", "base", "base", "R")

    her @ cheeks blush "!!!!!!?" ("mad", "wide", "base", "stare", ypos="head", flip=False)
    gen "What is it, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It's nothing [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "It's just..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "This is so... inappropriate..." ("angry", "happyCl", "worried", "mid")
    gen "Relax, [name_hermione_genie]. It's not like you are enjoying this..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What? Of course not! This is depraved..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "I am making this sacrifice for the honour of my house..." ("angry", "happyCl", "worried", "mid")
    gen "Yes, concentrate on that..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "...................." ("angry", "base", "angry", "mid")
    call ctc

    her @ cheeks blush "But, [name_genie_hermione]..." ("open", "base", "base", "R")
    her @ cheeks blush "Why are {size=+7}you{/size} doing this?" ("open", "base", "base", "R")

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "\"I have my reasons...\"":
            her @ cheeks blush "Oh..." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "*Hmm*..." ("annoyed", "narrow", "angry", "R")

        "\"In the name of science of course!\"":
            her "Really?!" ("soft", "wide", "base", "stare")
            her "Is this research of some kind?" ("soft", "wide", "base", "stare")
            gen "Yeah, sure, I'm researching... *Err*..." ("base", xpos="far_left", ypos="head")
            gen "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..." ("base", xpos="far_left", ypos="head")
            her "I see..." ("soft", "wide", "base", "stare")
            her "Well, if it is for research, then I am glad to be of help..." ("annoyed", "narrow", "angry", "R")

        "-Just squeeze her butt cheeks tighter-":
            nar "You give Hermione's butt cheeks a couple of extra firm squeezes."
            her @ cheeks blush "...................." ("open", "base", "base", "R")
            her @ cheeks blush "(Shall I just be quiet, then.....?)" ("disgust", "narrow", "base", "down")

    nar "You keep on playing with Hermione's buttocks..."
    nar "You slide your hands up and down her inner thighs..."
    her @ cheeks blush "................" ("angry", "happyCl", "worried", "mid")

    menu:
        "-Slide your hands under her panties-" if hermione.is_worn("panties"):
            nar "You slowly slide one of your hands under the fabric of the girl's panties..."
            her @ cheeks blush "[name_genie_hermione]... What are you...?" ("mad", "wide", "base", "stare", ypos="head", flip=False)
            gen "That's alright, just think about those {number=current_payout} points your house is about to receive..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "............." ("disgust", "narrow", "base", "down")

            pass

        "-Slide your hands across her pussy-" if not hermione.is_worn("panties"):
            nar "You slowly slide one of your hands across her pussy..."
            her @ cheeks blush "[name_genie_hermione]... What are you...?" ("mad", "wide", "base", "stare", ypos="head", flip=False)
            gen "That's alright, just think about those {number=current_payout} points your house is about to receive..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "............." ("disgust", "narrow", "base", "down")

            pass

        "-That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    menu:
        "-Prod her pussy with one of your fingers-":
            nar "You slide one of your fingers down and place it against the girl's slit..."
            her @ cheeks blush "[name_genie_hermione]? No! What are you...?" ("mad", "wide", "base", "stare")
            nar "Hermione tries to pull away from you..."
            $ states.her.mood += 3

            menu:
                "-Force your finger into her pussy!-":
                    nar "You force one of your fingers into her pussy..."
                    nar "It's very tight and warm..."
                    nar "It is also relatively dry... Doesn't look like Hermione's taking much pleasure in this..."

                    jump hg_pf_grope_ass_T3_mad

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Prod her butthole instead-":
            nar "You place one of your thumbs against the girl's butthole..."
            her @ cheeks blush "[name_genie_hermione]? No! What are you doing!?" ("mad", "wide", "base", "stare")
            $ states.her.mood += 3

            menu:
                "-Force your thumb into her butthole-":
                    nar "You force one of your thumbs into her little butthole..."
                    with hpunch
                    her "!!?" ("angry", "wide", "base", "stare")
                    nar "It's very tight and warm inside..."

                    jump hg_pf_grope_ass_T3_mad

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Stop pushing your luck. Dismiss the girl-":
            jump end_hg_pf_grope

label hg_pf_grope_ass_T3_mad:
    her @ cheeks blush "Stop that at once!" ("angry", "happyCl", "worried", "mid", ypos="head")
    nar "Hermione gives you an unexpectedly strong shove..."

    call her_chibi_scene("behind_desk_front", trans=hpunch)

    her @ cheeks blush "This is not what we agreed on, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid")
    gen "More points is it?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "More..." ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "{size=+7}Points?!{/size}" ("scream", "happyCl", "worried", "mid", trans=hpunch)
    gen "That's not it?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "No, it's definitely not because of the points!" ("scream", "happyCl", "worried", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "So I assume you don't want any extra points before leaving then?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("mad", "base", "worried", "R")
    her @ cheeks blush "I'll have twenty--" ("angry", "base", "angry", "mid")
    gen "Alright, twenty it--" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "No, a hundred extra house points!" ("angry", "base", "angry", "mid")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Alright, alright... One hundred points it is...\"":
            $ gryffindor += 100
            $ states.her.mood += 9

            gen "One hundred points to Gryffindor!" ("base", xpos="far_left", ypos="head")
            gen "There, it is done..." ("base", xpos="far_left", ypos="head")
            gen "Not about the points, you say... You make me--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Shut up!" ("scream", "happyCl", "worried", "mid", ypos="head")
            her @ cheeks blush "{size=+7}The terms should've been stated before commencing the--{/size}" ("scream", "happyCl", "worried", "mid", trans=hpunch)
            gen "Commencing--" ("base", xpos="far_left", ypos="head")
            gen "Oh, snap out of it [name_hermione_genie], You got paid didn't you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("mad", "happyCl", "worried", "mid")
            gen "Don't act like you're not benefiting from this..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Whatever..." ("angry", "base", "base", "R")

        "\"Surely you can't be serious, [name_hermione_genie]!\"":
            $ states.her.mood += 27

            her @ cheeks blush "Yes... I Am!" ("scream", "happyCl", "worried", "mid", ypos="head")
            gen "By the great desert..." ("angry", xpos="far_left", ypos="head")
            gen "You get no points!" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "*Grr*... Fine!" ("scream", "happyCl", "worried", "mid")

    call her_chibi_scene("reset","desk","base", trans=fade)

    call her_walk("door", "base")

    her @ cheeks blush "..........................." ("disgust", "narrow", "base", "down", ypos="head", flip=False)

    call her_chibi("leave")

    jump end_hermione_event

### Tier 4 ###

label hg_pf_grope_ass_T4:
    call her_chibi_scene("behind_desk_front", trans=d7)

    her @ cheeks blush "Do you want me to turn around then, [name_genie_hermione]?" ("base", "base", "base", "R", ypos="head", flip=False)

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "\"Yes. Turn around, [name_hermione_genie].\"":
            her @ cheeks blush "As you say, [name_genie_hermione]..." ("base", "base", "base", "R")
            jump hg_pf_grope_ass_T4_back

        "\"No. Just stand still, [name_hermione_genie].\"":
            her @ cheeks blush "As you say, [name_genie_hermione]..." ("soft", "base", "base", "mid", ypos="head", flip=False)
            jump hg_pf_grope_ass_T4_front

label hg_pf_grope_ass_T4_front:
    call her_chibi_scene("behind_desk_front", trans=d7)
    pause.8

    her @ cheeks blush "..................." ("base", "base", "base", "R", ypos="head", flip=False)
    gen "You seem more relaxed this time." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..................." ("base", "narrow", "worried", "down")
    gen "Could it be that you're enjoying this?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I..." ("soft", "narrow", "worried", "down")
    her @ cheeks blush "I'm doing this to earn points for my house, it has nothing to do with personal enjoyment..." ("soft", "narrow", "worried", "down") #looks down
    gen "Is that so?" ("base", xpos="far_left", ypos="head")
    gen "Then why aren't you looking into my eyes when you say that..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I..." ("disgust", "base", "base", "mid") # looks back up

    call her_chibi_scene("grope_ass_front", trans=d7)
    pause.8

    her @ cheeks blush "!!!" ("mad", "wide", "base", "stare")
    gen "..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "........" ("annoyed", "base", "angry", "mid")

    nar "You run your hands up and down Hermione's legs..."
    her @ cheeks blush "........................." ("upset", "happyCl", "worried", "mid")

    nar "And give her ass a good squeeze..."
    her @ cheeks blush "................." ("soft", "base", "base", "mid")
    gen "There you go, a bit of eye-contact for once..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Isn't that what you wanted, [name_genie_hermione]..." ("open", "base", "worried", "mid")

    nar "You give her butt another firm squeeze as you gently move to massage her inner leg..."
    her @ cheeks blush "I'll take that as a yes..." ("base", "narrow", "annoyed", "mid")

    if hermione.is_worn("panties"):
        nar "You continue to massage her inner thigh and occasionally gently brush against her panties..."
    else:
        nar "You continue to massage her inner thigh and occasionally gently brush against her pussy..."
    her @ cheeks blush "*Ah*..." ("soft", "narrow", "annoyed", "up")
    her @ cheeks blush "..." ("clench", "narrow", "annoyed", "up")
    gen "..." ("grin", xpos="far_left", ypos="head")

    nar "Maintaining eye contact, you move your hand down. A split second of disappointment is seen on Hermione's face..."
    gen "Enjoying yourself?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "W-What..." ("disgust", "narrow", "worried", "down")
    gen "The massage... You seem less tense than last time." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh... I suppose it is quite nice..." ("clench", "base", "base", "R")

    nar "You continue rubbing her inner thighs, Hermione's chest moving up and down faster and faster..."
    her @ cheeks blush "......." ("clench", "narrow", "base", "down")
    gen "Enjoying a bit too much perhaps?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("base", "narrow", "base", "mid_soft")
    her @ cheeks blush "What do you--" ("soft", "narrow", "base", "mid_soft")

    call her_chibi_scene("behind_desk_front", trans=d7)
    pause.8

    nar "You bring your hands out from between Hermione's legs and hold them up in front of her..."
    gen "What would you call this then, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

    nar "Hermione embarrassingly looks at you, as you present her with a sticky substance gleaming across your upper hand..."
    her @ cheeks blush "Oh..." ("disgust", "narrow", "base", "down")
    her @ cheeks blush "Well, your hands were moving so close and--" ("soft", "narrow", "worried", "down")

    call her_chibi_scene("grope_ass_front", trans=d7)
    pause.8

    nar "Before she can finish her sentence, you put your hand back in place..."
    her @ cheeks blush "..." ("clench", "wide", "base", "stare")

    nar "You slowly brush your fingertips across her legs, and move your hands to rest on her firm cheeks..."
    her @ cheeks blush "..." ("soft", "narrow", "annoyed", "up")

    nar "Hermione begins to relax once more as you softly massage them with your hands..."
    her @ cheeks blush "..." ("base", "narrow", "base", "down")
    gen "I thought I asked you to look at me." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh, sorry..." ("base", "narrow", "base", "mid_soft")

    menu:
        "-Slide your hands under her panties-" if hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_front", trans=d7)

        "-Slide your hands across her pussy-" if not hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_front", trans=d7)

        "-That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    jump hg_pf_grope_ass_T4_continue

label hg_pf_grope_ass_T4_back:
    call her_chibi_scene("behind_desk_back", trans=d7)
    pause.8

    her @ cheeks blush "..." ("base", "narrow", "annoyed", "up", ypos="head", flip=False)
    gen "How does it feel?" ("base", xpos="far_left", ypos="head")
    her "How does what feel?" ("open", "narrow", "base", "mid_soft")
    gen "How does it feel to be presenting your butt to your headmaster?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I don't know how to answer that, [name_genie_hermione]..." ("clench", "narrow", "base", "down")
    her @ cheeks blush "Do I have to give you a response?" ("open", "base", "base", "mid")
    gen "Well, you don't have to..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It feels weird...{w} but..." ("disgust", "narrow", "worried", "down")
    gen "Butt?" ("grin", xpos="far_left", ypos="head") #fucks sake

    call her_chibi_scene("grope_ass_back", trans=d7)
    pause.8

    her @ cheeks blush "!!!" ("mad", "wide", "base", "stare")
    her @ cheeks blush "[name_genie_hermione]!" ("clench", "base", "angry", "mid")
    gen "Sorry..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "You should've warned me..." ("soft", "narrow", "angry", "R")

    nar "Hermione goes quiet as you begin massaging her butt cheeks..."
    her @ cheeks blush "..." ("base", "closed", "base", "mid")

    nar "You take your thumbs and move them gently from side to side as her soft butt cheeks open and close with every move..."
    gen "Does this feel better?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It..." ("clench", "narrow", "worried", "down")
    her @ cheeks blush "It feels fine..." ("soft", "narrow", "worried", "down")
    gen "I meant not having to look at me..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh...{w} it doesn't matter to me how you want it..." ("soft", "base", "base", "R")
    gen "Is that so?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of cours--" ("soft", "closed", "base", "mid")

    menu:
        "-Give her butt a squeeze-":
            nar "You spread your hands out and then suddenly tighten them firmly around Hermione's Butt cheeks..."
            her @ cheeks blush "!!!" ("clench", "wide", "base", "stare")
            gen "Be careful what you wish for, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Giving me free rein might show you just how greedy I can be..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("angry", "narrow", "base", "R")
            gen "Although perhaps if you're lucky enough, you could also receive some of my well-known generosity..." ("base", xpos="far_left", ypos="head")
            nar "Lessening your grip on her cheeks slightly, you then move down towards her inner thighs, and gently begin massaging her with your thumbs..."

        "-Give her butt a slap-":
            call slap_her
            her @ cheeks blush "!!!!!!!!!!!!!" ("angry", "wide", "base", "stare")
            her @ cheeks blush "[name_genie_hermione]!" ("clench", "narrow", "base", "R")

            gen "Did you not just say that it didn't matter to you how I wanted it?" ("base", xpos="far_left", ypos="head")

            her @ cheeks blush "Yes... But--" ("disgust", "narrow", "base", "R")
            gen "{size=+5}BUTT!{/size}" ("base", xpos="far_left", ypos="head")

            call slap_her

            her @ cheeks blush "{size=+3}*Ah*!{/size}" ("angry", "narrow", "base", "up")
            her @ cheeks blush "..." ("disgust", "narrow", "base", "down")

            gen "*Heh-heh*..." ("grin", xpos="far_left", ypos="head")
            nar "You put your hands back on her butt, and then start moving them down towards her inner thighs..."
            nar "As you move your palms further and further up, you feel a slight wetness between her legs..."

            gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Y-Yes... [name_genie_hermione]?" ("angry", "narrow", "base", "R")
            gen "Are you...{w} *Hmm*... Never mind..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("angry", "narrow", "base", "down")
            nar "You gently begin massaging her with your thumbs..."

    her @ cheeks blush "..." ("soft", "narrow", "annoyed", "up")

    if hermione.is_worn("panties"):
        nar "Moving your hands gently up and down, Hermione begins to relax as they occasionally brush against her panties..."
    else:
        nar "Moving your hands gently up and down, Hermione begins to relax as they occasionally brush against her pussy..."
    her @ cheeks blush "*Ah*..." ("open", "narrow", "annoyed", "up")
    her @ cheeks blush "..." ("base", "narrow", "annoyed", "up")
    gen "..." ("grin", xpos="far_left", ypos="head")

    nar "You continue in silence, and notice that Hermione's chest has begun moving up and down, even faster than before..."

    menu:
        "-Slide your hands under her panties-" if hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_back", trans=d7)

        "-Slide your hands across her pussy-" if not hermione.is_worn("panties"):
            call her_chibi_scene("grope_ass_back", trans=d7)

        "-That's enough for today. Dismiss her-":
            jump end_hg_pf_grope

    jump hg_pf_grope_ass_T4_continue

label hg_pf_grope_ass_T4_continue:

    if hermione.is_worn("panties"):
        nar "You slowly slide one of your hands under the fabric of the girl's panties..."
    else:
        nar "You slowly slide one of your hands across her pussy.."
    her @ cheeks blush "[name_genie_hermione]... What are you...?" ("open", "base", "base", "R", ypos="head", flip=False)

    if states.her.tier <= 5:
        gen "It's alright, just think about those {number=current_payout} points your house is about to receive..." ("base", xpos="far_left", ypos="head")
    else:
        gen "It's alright, just try to relax and enjoy yourself." ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "As you say..." ("open", "base", "base", "R")

    menu:
        "-Prod her pussy with one of your fingers-":
            nar "You slide one of your fingers down and place it against the girl's little slit..."
            her @ cheeks blush "[name_genie_hermione]?" ("base", "base", "base", "R")

            menu:
                "-Force your finger into her pussy!-":
                    play sound "sounds/slick_02.ogg"

                    nar "You force one of your fingers into her little pussy..."
                    nar "It's very tight and warm..."
                    nar "It's quite wet as well... Seems like Hermione's taking pleasure in this..."

                    her @ cheeks blush "*Ah*..." ("silly", "narrow", "base", "mid_soft")
                    her @ cheeks blush "It's inside of me..." ("disgust", "narrow", "worried", "down")
                    her @ cheeks blush "No, [name_genie_hermione], you must stop now..." ("disgust", "base", "base", "mid_soft")
                    gen "Why? You don't like it?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "It doesn't matter whether I like this or not, [name_genie_hermione]." ("soft", "narrow", "base", "mid_soft")
                    nar "You take your fingers out, and brush them across her slit..."
                    her @ cheeks blush "You know why I'm doing this..." ("clench", "narrow", "worried", "down")
                    her @ cheeks blush "...." ("disgust", "narrow", "worried", "down")
                    her @ cheeks blush "And it's wrong for me to let you do this to me for a meagre {number=current_payout} points..." ("base", "narrow", "base", "mid_soft")
                    gen "*Heh*... I see..." ("base", xpos="far_left", ypos="head")

                    menu:
                        "-Continue rubbing her-":
                            nar "As you continue rubbing her, Hermione closes her eyes and goes silent..."
                            her @ cheeks blush "......" ("clench", "happyCl", "worried", "mid")
                            her @ cheeks blush "*Ah*..." ("silly", "happyCl", "worried", "mid")
                            nar "With no more objections, you move your index finger across her clit and begin rubbing it gently..."
                            her @ cheeks blush "..." ("soft", "closed", "base", "mid")
                            nar "Completely lost in the moment, Hermione's body reacts, and she grinds on your fingers slightly, as you massage her."
                            nar "In response to her movement, you start rubbing her faster, and as you do so, she squeals and lets out a gentle moan."
                            her @ cheeks blush "*Hnnngh*" ("clench", "happyCl", "worried", "mid") #still has eyes closed
                            her @ cheeks blush "...." ("disgust", "wide", "base", "stare") #Opens her eyes wide
                            gen "Did you just--" ("base", xpos="far_left", ypos="head")
                            if states.her.tier <= 5:
                                her @ cheeks blush "No..." ("angry", "happyCl", "worried", "mid")
                                gen "Well it sure looks like you just--" ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "I think we're done here!" ("soft", "happyCl", "worried", "mid", emote="angry")
                                gen "I see..." ("base", xpos="far_left", ypos="head")
                                gen "Well, in that case..." ("base", xpos="far_left", ypos="head")
                            else:
                                her @ cheeks blush "Yes..." ("angry", "narrow", "annoyed", "up")
                                her @ cheeks blush "That felt really good!" ("soft", "narrow", "base", "mid_soft")
                                gen "Any time, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
                                her @ cheeks blush "Thank you, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")

                            jump end_hg_pf_grope

                        "-Let the girl go...-":
                            jump end_hg_pf_grope

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Prod her butthole instead-":
            nar "You place one of your thumbs against the girl's little butthole..."
            her @ cheeks blush "[name_genie_hermione]? What are you doing?" ("base", "base", "base", "R")

            menu:
                "-Force your thumb into her butthole-":
                    play sound "sounds/slick_02.ogg"

                    nar "You force one of your thumbs into her little butthole..."
                    with hpunch
                    her @ cheeks blush tears soft "*Ah*... Your finger is up my..." ("silly", "base", "worried", "stare")
                    nar "It's very tight and warm inside..."
                    her @ cheeks blush "*Ah*..." ("silly", "narrow", "base", "mid_soft")
                    her @ cheeks blush "It's inside of me..." ("angry", "narrow", "base", "mid_soft")
                    her @ cheeks blush "No, [name_genie_hermione], you must stop now..." ("base", "narrow", "base", "mid_soft")
                    gen "Why? You don't like it?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "It doesn't matter whether I like this or not, [name_genie_hermione]." ("soft", "narrow", "base", "mid_soft")
                    her @ cheeks blush "You know why I'm doing this..." ("clench", "narrow", "worried", "down")
                    her @ cheeks blush "And it's wrong for me to let you do this to me for a meagre {number=current_payout} points..."("base", "narrow", "base", "mid_soft")

                    play sound "sounds/slick_pop.ogg"
                    nar "Hermione pulls away from you..."
                    gen "*Heh*... I see..." ("base", xpos="far_left", ypos="head")
                    gen "Well, in that case..." ("base", xpos="far_left", ypos="head")

                    jump end_hg_pf_grope

                "-Let the girl go...-":
                    jump end_hg_pf_grope

        "-Stop pushing your luck. Dismiss the girl-":
            jump end_hg_pf_grope
