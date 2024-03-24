
label start_hg_pr_cumslut:
    # Public shaming: Wear cum
    # TODO: Some events need to be rewritten so they follow cum layers limitations and actual game progression.
    # Additionally, they should be converted into the event class.

    $ current_payout = 50

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her to walk around with my cum on her?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu
    return

label hg_pr_cumslut_fail:

    call start_hg_pr_cumslut

    her "" (xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]." ("open", "base", "base", "mid")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    gen "Today I have another small favour to ask of you." ("base", xpos="far_left", ypos="head")
    her "What is it?" ("soft", "base", "base", "mid")
    gen "I'd like you to attend class..." ("base", xpos="far_left", ypos="head")
    her "Of course, not a problem..." ("base", "happyCl", "base", "mid")
    gen "Glazed with my cum!" ("grin", xpos="far_left", ypos="head")

    jump too_much_public

label hg_pr_cumslut_e1:

    call start_hg_pr_cumslut

    her "" (xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks base "Yes, [name_genie_hermione]." ("base", "base", "base", "mid")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    gen "Today I have another small favour to ask of you." ("base", xpos="far_left", ypos="head")
    her "What is it?" ("soft", "base", "base", "mid")
    gen "I'd like you to attend class..." ("base", xpos="far_left", ypos="head")
    her "Of course, not a problem..." ("base", "happyCl", "base", "mid")
    gen "Glazed with my cum!" ("grin", xpos="far_left", ypos="head")
    her "What?!?" ("shock", "wide", "base", "stare")
    her "You can't be serious!" ("angry", "base", "angry", "mid")
    her "It's bad enough that I let you cum on me in the first place!" ("annoyed", "narrow", "annoyed", "mid")
    her "But in public?" ("angry", "narrow", "annoyed", "mid", emote="angry")
    her "I think I better leave..." ("annoyed", "base", "angry", "mid")
    gen "Wait!" ("base", xpos="far_left", ypos="head")
    gen "What if nobody could see it?" ("base", xpos="far_left", ypos="head")
    her "You mean like a spell?" ("soft", "narrow", "annoyed", "mid")
    gen "That, or I could dump my load somewhere discreet." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well... I suppose that would be alright..." ("annoyed", "narrow", "annoyed", "R")
    her "But what's the point of it all?" ("annoyed", "base", "worried", "R")
    gen "You'll know it's there, and so will I." ("grin", xpos="far_left", ypos="head")
    her "*Hmm*..." ("annoyed", "narrow", "angry", "L")
    her "How much would I be paid for this?" ("annoyed", "squint", "base", "mid")
    gen "Thirty points." ("base", xpos="far_left", ypos="head")
    her "Thirty?! I expect at least seventy for such a filthy act!" ("angry", "happyCl", "worried", "mid")
    gen "Forty." ("base", xpos="far_left", ypos="head")
    her "Sixty!" ("open", "closed", "angry", "mid")
    gen "Fifty points, my final offer." ("base", xpos="far_left", ypos="head")
    her "Okay, I'll do it." ("annoyed", "base", "worried", "R")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "If nobody can see it then I guess it's okay..." ("annoyed", "narrow", "angry", "R")
    gen "Splendid. Care to lend me a hand?" ("base", xpos="far_left", ypos="head")
    her "*sigh*..." ("soft", "narrow", "worried", "down")

    hide hermione_main
    call blkfade

    call her_chibi_scene("hj", "desk", "base")

    call hide_blkfade
    call ctc

    her "Why are you making me do this, [name_genie_hermione]?" ("angry", "base", "worried", "mid", ypos="head", flip=False)
    gen "What do you mean?" ("base", xpos="far_left", ypos="head")
    her "Why are you making me jerk you off..." ("angry", "narrow", "base", "down")
    gen "You know why..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Are you trying to mark me as yours?" ("normal", "narrow", "annoyed", "mid")
    her @ cheeks blush "Like some common beast?" ("normal", "narrow", "worried", "mid")
    gen "I'm not doing anything, my hands are right here." ("grin", xpos="far_left", ypos="head")
    her "That may be so, but if I stop, Gryffindor will lose the house cup." ("annoyed", "narrow", "worried", "mid")
    gen "And?" ("base", xpos="far_left", ypos="head")
    her "Harry and Ron will be so disappointed..." ("annoyed", "base", "worried", "mid")
    gen "So that's why you are doing this? For those two boys?" ("base", xpos="far_left", ypos="head")
    her "Sort of... I'm not sure that they'd be too upset, though." ("annoyed", "base", "worried", "R")
    gen "Are you sure that's the only reason?" ("base", xpos="far_left", ypos="head")
    her "What?" ("upset", "wink", "base", "mid")
    gen "I mean, you're answering all my summon requests--" ("base", xpos="far_left", ypos="head")
    gen "--Doing whatever I tell you to do, whenever I tell you." ("base", xpos="far_left", ypos="head")
    gen "Performing in front of your peers, because I ask of you." ("base", xpos="far_left", ypos="head")
    her "..." ("disgust", "narrow", "base", "down")
    gen "Tell you what, I'll give you a choice." ("base", xpos="far_left", ypos="head")
    gen "So long as I cum on you, and you parade around school smelling like a slut today, Gryffindor will get fifty points." ("base", xpos="far_left", ypos="head")
    her "How is that any different from what we've already agreed on?" ("disgust", "narrow", "base", "mid_soft")
    gen "Because I'll let you choose where to take my load." ("base", xpos="far_left", ypos="head")
    nar "You feel her hands tense around your cock."
    her "You're letting me choose?" ("open", "base", "base", "mid")
    gen "Yep." ("base", xpos="far_left", ypos="head")
    gen "As long as you let me cum on you. You can even choose your feet for all I care." ("base", xpos="far_left", ypos="head")
    her "Okay..." ("crooked_smile", "narrow", "base", "mid")
    gen "Well, hurry up then, [name_hermione_genie], classes will start soon." ("base", xpos="far_left", ypos="head")
    nar "She starts jerking your cock with renewed vigour."
    gen "So, what will be your choice?" ("base", xpos="far_left", ypos="head")
    her "I'm not sure." ("upset", "wink", "base", "mid")
    her "I'm trying to think of a place no one will be able to see..." ("angry", "base", "base", "mid")
    gen "You better think of something soon!" ("base", xpos="far_left", ypos="head")
    her "Why's that?" ("open", "wink", "worried", "mid")
    gen "Because I'm about to cum!" ("grin", xpos="far_left", ypos="head")
    her "Already?! But I still haven't--" ("angry", "wide", "base", "stare")

    menu:
        #"-Stay Silent-": # TODO: rewrite so it doesn't require to be "under" shirt, but on top of the existing cloth (if any at all)
            # Cum under shirt
            #$ _cum_location = 1

            #nar "Hermione swiftly pulls her shirt up..."
            #nar "You can feel her incredibly soft tits rubbing against the tip of your cock, making you cum!"
            #gen "{size=+5}*ARGH*! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")

            #call her_chibi_scene("hj_cum_in")
            #call cum_block

            # TODO Cum under shirt layer

            #her "!!!!!!!!!!!" ("shock", "wide", "base", "stare", xpos="right", ypos="base")

            #call her_chibi_scene("hj_cum_in_done")
            #call ctc

            #her "Well, this shouldn't be too bad..." ("upset", "wink", "base", "mid")
            #gen "I'm sure no one will notice." ("base", xpos="far_left", ypos="head")
            #her "They better not." ("angry", "base", "angry", "mid")

        "\"Just keep on jerking, [name_hermione_genie]!\"":
            # Cum on skirt
            $ _cum_location = "bottom"

            nar "Hermione keeps jerking your cock, her gaze wandering about her own body."
            gen "Get ready, you whore, here it comes!!!" ("angry", xpos="far_left", ypos="head")
            her "Wait, I need more time--" ("shock", "wide", "worried", "mid")
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("grin", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(crotch="light")

            her "!!!!!!!!!!!" ("shock", "wide", "base", "stare", xpos="right", ypos="base")

            $ hermione.set_cum(crotch="heavy")

            gen "That's it! All over you, slut!" ("angry", xpos="far_left", ypos="head")
            her "..." ("shock", "base", "worried", "down")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

            her "Y-you came all over my bottom half..." ("angry", "narrow", "worried", "mid")

            her "Will that be all, [name_genie_hermione]?" ("angry", "narrow", "worried", "mid")
            gen "I don't suppose you could kiss it for good luck?" ("base", xpos="far_left", ypos="head")
            her "I don't think so." ("annoyed", "narrow", "angry", "R")
            gen "Well then that should be all, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        "\"Use your head, slut!\"":
            # Cum on head
            $ _cum_location = "face"

            nar "Hermione bends down and holds your cock in front of her face."
            gen "Oh? Interesting! Get ready, here it comes!" ("base", xpos="far_left", ypos="head")
            her "W-wait I--" ("scream", "wide", "base", "mid")
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("grin", xpos="far_left", ypos="head")
            her "--I can't!" ("open", "wide", "worried", "mid")

            nar "Hermione moves your cock away from her face at the last second."
            nar "You erupt all over the top of her head, covering her hair in your spunk."

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(hair="light")

            her "!!!!!!!!!!!" ("shock", "wide", "base", "stare", xpos="right", ypos="base")

            $ hermione.set_cum(hair="heavy")

            gen "Yes! I Feel so much better now..." ("grin", xpos="far_left", ypos="head")
            her ".............." ("normal", "happyCl", "worried", "mid")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

            her @ tears soft_blink "H-How could you!?" ("scream", "happyCl", "worried", "mid")
            gen "How could I? What do you mean?" ("base", xpos="far_left", ypos="head")
            her @ tears soft "You told me to use my head!" ("scream", "base", "angry", "mid")
            gen "I did." ("base", xpos="far_left", ypos="head")
            her @ tears soft_blink "Why would you do something like that then!?" ("mad", "happyCl", "worried", "mid")
            gen "Sorry, what wrongdoing did I do?" ("base", xpos="far_left", ypos="head")
            her @ tears soft "If I hadn't moved at the last second, my face would be covered!" ("angry", "base", "base", "mid")
            gen "Don't blame me, that was your move, not mine." ("base", xpos="far_left", ypos="head")
            her "What?" ("open", "base", "angry", "mid")
            gen "I only said that you should use your head to think." ("base", xpos="far_left", ypos="head")
            gen "I didn't mean it in a literal sense..." ("base", xpos="far_left", ypos="head")
            her "You mean I didn't have to..." ("angry", "base", "worried", "R")
            gen "Not at all." ("base", xpos="far_left", ypos="head")
            gen "I thought you of all people would know what an idiom is." ("grin", xpos="far_left", ypos="head")
            her "........." ("disgust", "narrow", "worried", "mid")

    hide hermione_main
    call blkfade

    nar "You tuck your cock back into your robe."

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    call hide_blkfade
    pause.2

    call bld
    gen "Oh, and one last thing before you head to class..." ("base", xpos="far_left", ypos="head")
    her "What is it?" ("annoyed", "narrow", "annoyed", "mid")
    gen "If you happen to report to me after class, with no traces of cum on you, Slytherin will get two hundred points." ("base", xpos="far_left", ypos="head")
    her "{size=+10}Two hundred!? That is not fair!{/size}" ("shock", "wide", "base", "stare")
    gen "It's unfair only if you cheat, and try washing it off." ("grin", xpos="far_left", ypos="head")
    her "*tsk*!..." ("angry", "base", "angry", "mid")

    call her_walk(action="leave")

    gen "See you soon..." ("grin", xpos="far_left", ypos="head")

    jump end_hermione_event

label hg_pr_cumslut_e2:

    call start_hg_pr_cumslut

    her "" (xpos="mid", ypos="base", trans=fade)

    her "Again?" ("angry", "wide", "base", "stare")
    her "You cannot be serious!?" ("angry", "base", "angry", "mid")
    her @ cheeks blush "I already let you do this to me once, isn't that enough?" ("annoyed", "narrow", "annoyed", "mid")
    gen "It's enough when I say it's enough." ("base", xpos="far_left", ypos="head")
    gen "Besides, was it really so bad the last time?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well I guess not..." ("annoyed", "base", "angry", "R")
    her "But will it still be hidden this time?" ("annoyed", "base", "worried", "mid")
    gen "That's up to you." ("base", xpos="far_left", ypos="head")
    her "*Hmm*..." ("annoyed", "narrow", "angry", "R")

    her "How much will I be paid this time then?" ("open", "squint", "base", "mid")
    gen "Twenty points." ("base", xpos="far_left", ypos="head")
    her "Twenty!? we agreed on fifty last time!" ("clench", "base", "angry", "mid")
    gen "Forty." ("base", xpos="far_left", ypos="head")
    her "Seventy!" ("scream", "closed", "angry", "mid")
    gen "Fifty points then, final offer." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Eighty and I'll let people see it." ("grin", "narrow", "base", "mid_soft")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "As long as it isn't too obvious..." ("base", "narrow", "worried", "down")
    gen "Deal!" ("grin", xpos="far_left", ypos="head")
    her "..." ("soft", "narrow", "worried", "down")

    hide hermione_main
    call blkfade

    call her_chibi_scene("hj", "desk", "base")
    call hide_blkfade
    call ctc

    her "Why are we doing this again, [name_genie_hermione]?" ("annoyed", "base", "base", "mid", ypos="head", flip=False)
    gen "Let me answer your question with one of my own." ("base", xpos="far_left", ypos="head")
    her "Okay..." ("open", "base", "base", "mid")
    gen "Why are you jerking me off, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Because you asked me to..." ("soft", "narrow", "annoyed", "mid")
    gen "And that's all there is to it?" ("base", xpos="far_left", ypos="head")
    her "Yes... I think?" ("open", "wink", "worried", "mid")
    gen "Are you sure?" ("base", xpos="far_left", ypos="head")
    her "I don't know..." ("open", "base", "worried", "R")
    gen "What is your other reason?" ("base", xpos="far_left", ypos="head")
    her "if I don't do this, Gryffindor will lose the house cup." ("angry", "happyCl", "worried", "mid")
    gen "You said the same thing the last time, but I still don't buy it." ("base", xpos="far_left", ypos="head")
    her "It's not a lie..." ("angry", "base", "worried", "mid")
    gen "No, it's not, but it's not a complete truth either." ("base", xpos="far_left", ypos="head")
    gen "If you had to choose, would you rather win the house cup, or--" ("base", xpos="far_left", ypos="head")
    gen "Would you rather make me a happy man." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Can't I do both?" ("annoyed", "base", "worried", "R")
    gen "You certainly can... But I want you to be honest." ("base", xpos="far_left", ypos="head")
    gen "I'm going to give you another choice--" ("base", xpos="far_left", ypos="head")
    gen "You can stop jerking me off right now, leave the room and I'll give you a hundred points. However, I'll be very upset." ("base", xpos="far_left", ypos="head")
    her "..." ("open", "base", "base", "mid")
    her "What's the other option?" ("soft", "base", "worried", "mid")
    gen "Or, you can continue what you're doing, take my load on you, but you'll get no points whatsoever." ("base", xpos="far_left", ypos="head")
    her "..." ("shock", "wide", "base", "mid")
    her "NO POINTS?" ("angry", "wide", "worried", "mid")
    gen "None. However, you will make me very happy." ("base", xpos="far_left", ypos="head")
    her "But that's... Can't you just pay me like usual--" ("angry", "base", "worried", "mid", emote="sweat")
    gen "No, I cannot." ("base", xpos="far_left", ypos="head")
    gen "The choice is yours however." ("base", xpos="far_left", ypos="head")
    nar "You feel Hermione's hand tense around your cock."
    her "You're making me choose? Between getting a hundred points for doing nothing--" ("angry", "happyCl", "angry", "mid")
    her "--Or getting paid nothing for being treated like some cumrag from slytherin?" ("angry", "narrow", "annoyed", "mid", emote="angry")
    gen "I would've phrased it differently, but yes, these are your choices, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")
    her "{size=-5}Some choices they are...{/size}" ("disgust", "narrow", "base", "R")
    gen "You might wish to make up your mind soon, your classes are about to start." ("base", xpos="far_left", ypos="head")
    nar "Hermione ponders for a minute, you study her face in great detail, wondering what's going through her head."
    nar "You can see the wheels turning as she contemplates her choices, as ridiculous as they may be."
    nar "Her face is beet red, eyes unfocused. You nod to yourself, you think you know the answer."
    nar "She starts jerking your cock with renewed vigour."
    her @ cheeks blush "..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "You better appreciate this..." ("open", "narrow", "angry", "R")
    gen "Oh, trust me, I am feeling {b}very{/b} happy!" ("grin", xpos="far_left", ypos="head")
    her "Really?" ("open", "base", "base", "mid")
    gen "You're about to see how much I'm appreciating this!" ("grin", xpos="far_left", ypos="head")
    her "What, Already? Where should I--" ("angry", "wide", "base", "stare")

    menu:
        "-Stay Silent-":
            # Cum on legs
            $ _cum_location = "legs"

            nar "Hermione tries to think, but her mind is too distracted to think quick enough."
            gen "Get ready slut, here it comes!" ("angry", xpos="far_left", ypos="head")
            her "Wait, where am I supposed to--" ("shock", "wide", "worried", "mid")
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("grin", xpos="far_left", ypos="head")
            nar "Hermione aims your cock lower, aiming it at her legs."

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(legs="light")

            her "!!!!!!!!!!!" ("shock", "wide", "base", "stare", xpos="right", ypos="base")

            $ hermione.set_cum(legs="heavy")

            gen "That's it, all over your milky thighs." ("angry", xpos="far_left", ypos="head")
            her "..." ("shock", "narrow", "worried", "down")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

            her "Are you happy now?" ("soft", "narrow", "annoyed", "mid")
            gen "I've never been happier, but..." ("base", xpos="far_left", ypos="head")
            her "...but?" ("normal", "wink", "annoyed", "mid")
            gen "I don't suppose you could give it a kiss, you know, for good luck?" ("base", xpos="far_left", ypos="head")
            her "......*sigh*" ("soft", "closed", "base", "up")

            hide hermione_main
            call her_chibi_scene("hj_kiss")
            play sound "sounds/kiss.ogg"
            with kissiris
            call ctc

            $ states.her.ev.give_me_a_handy.cock_kiss = True

            call her_chibi_scene("hj_cum_on_done")
            gen "Good girl." ("base", xpos="far_left", ypos="head")

        "\"Just keep on jerking, [name_hermione_genie]!\"":
            # Cum on shirt
            $ _cum_location = "chest"

            nar "Hermione keeps jerking your cock, her eyes focused intently on it."
            gen "Get ready slut, here I come!" ("angry", xpos="far_left", ypos="head")
            her "Please not on my--" ("shock", "base", "worried", "mid")
            gen "{size=+5}*ARGH*! YES!!! RIGHT ON THOSE TITS!{/size}" ("grin", xpos="far_left", ypos="head")

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(breasts="light", body="light")

            her "!!!!!!!!!!!" ("shock", "wide", "base", "stare", xpos="right", ypos="base")

            $ hermione.set_cum(breasts="heavy")

            gen "That's it! Let it soak, slut!" ("grin", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "worried", "down")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

            her "It's all over me..." ("angry", "narrow", "worried", "mid")
            gen "Not quite, but good enough." ("base", xpos="far_left", ypos="head")
            her "I think I should go now..." ("annoyed", "narrow", "worried", "down")

        "\"Take it on your face slut!\"":
            # Cum on face
            $ _cum_location = "face"

            nar "Hermione bends down and holds your cock in front of her face."
            gen "Get ready, here it comes!" ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "happyCl", "base", "mid")
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("grin", xpos="far_left", ypos="head")
            her "..." ("angry", "happyCl", "angry", "down")
            nar "You erupt onto her face, dousing her in your seemingly infinite spunk."

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(face="light")

            her "!!!!!!!!!!!" ("shock", "happyCl", "base", "stare", xpos="right", ypos="base")

            $ hermione.set_cum(face="heavy", hair="light")

            gen "I Feel so much lighter now..." ("grin", xpos="far_left", ypos="head")
            her ".............." ("normal", "happyCl", "worried", "mid")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

            her "[name_genie_hermione]!!!" ("scream", "happyCl", "worried", "mid")
            her "You came all over my face!" ("scream", "closed", "angry", "mid")
            gen "That's very perceptive of you." ("base", xpos="far_left", ypos="head")
            her @ tears soft_blink "Why would you ask me to do that!?" ("mad", "happyCl", "worried", "mid")
            her @ tears soft "I'm completely covered in your cum!" ("angry", "base", "base", "mid")
            gen "You didn't have to listen to me." ("base", xpos="far_left", ypos="head")
            her "..." ("angry", "base", "worried", "mid")
            her "You told me to do it though..." ("annoyed", "base", "worried", "R")

    hide hermione_main
    call blkfade

    nar "You tuck your cock back into your robe."

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")

    hide screen blktone
    hide screen bld1
    call hide_blkfade
    pause.2

    call bld
    gen "Oh and one last thing before you head to class." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, I know... Don't wash it off before reporting in..." ("annoyed", "narrow", "annoyed", "R", xpos="right", ypos="base")
    gen "Good, you learn quick." ("Grin", xpos="far_left", ypos="head")
    her "........." ("annoyed", "narrow", "base", "R")
    gen "Have fun! Tell your friends that Dumbledork sends his regards." ("grin", xpos="far_left", ypos="head")
    her "Very funny..." ("disgust", "narrow", "worried", "mid")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_cumslut_e3:

    call start_hg_pr_cumslut

    her "" (xpos="mid", ypos="base", trans=fade)

    her "Again? I just took a shower not too long ago..." ("open", "base", "worried", "mid")
    gen "No worries, [name_hermione_genie], I'll give you another shower." ("grin", xpos="far_left", ypos="head")
    her "I'm not sure we're talking about the same thing..." ("disgust", "narrow", "base", "mid")
    gen "Only one way to find out." ("base", xpos="far_left", ypos="head")
    her "*sigh*... I hope I don't regret it..." ("soft", "narrow", "base", "R")

    hide hermione_main
    call blkfade

    call her_chibi_scene("hj", "desk", "base")

    call hide_blkfade
    call ctc

    call bld
    gen "Gods, you're good at this, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her "Thank you... I've been thinking about what you asked me the last time..." ("angry", "wink", "base", "mid", ypos="head", flip=False)
    gen "Oh?" ("base", xpos="far_left", ypos="head")
    her "You asked me for the reason why I do all this... Why I sell you all these favours..." ("open", "base", "angry", "mid")
    her "I think it's time for me to come clean..." ("open", "closed", "worried", "mid")
    gen "(*heh*)" ("grin", xpos="far_left", ypos="head")
    gen "(I'm itching to make a joke, but perhaps it'd be wiser to let her speak.)" ("base", xpos="far_left", ypos="head")
    her "I didn't lie when I said it was just to get more house points, so that gryffindor could win the house cup..." ("angry", "wink", "worried", "mid")
    her @ cheeks blush "At first. But lately..." ("base", "narrow", "worried", "down")
    her @ cheeks blush "I think...{w=0.5} I think I'm starting to enjoy it, [name_genie_hermione]." ("soft", "narrow", "base", "mid_soft")
    her @ cheeks blush "Because seeing you happy, makes me happy..." ("base", "happyCl", "base", "mid")
    gen "That's great... But what would really make me happy right now is you focusing a little more on the task at hand..." ("base", xpos="far_left", ypos="head")
    her "Oh! Of course, [name_genie_hermione]... Silly me!" ("angry", "happy", "worried", "mid")
    her "I need to learn how to multitask." ("annoyed", "narrow", "base", "stare")
    her "it would come in handy." ("open", "squint", "base", "down")
    gen "(*heh-heh*)" ("grin", xpos="far_left", ypos="head")
    her "I think something's wrong with me, [name_genie_hermione]." ("open", "narrow", "worried", "mid")
    her "Ever since you asked me to parade with your cum in public, I think--" ("open", "narrow", "annoyed", "up")
    her "--I think something changed in me." ("grin", "narrow", "base", "dead")
    her "I thought I hated it but the truth is..." ("grin", "narrow", "base", "dead")
    her "I'm kind of enjoying it." ("soft", "narrow", "annoyed", "up")
    her "Is it weird? Does that make me a slut, [name_genie_hermione]?" ("soft", "narrow", "worried", "mid")

    if "slut" in name_hermione_genie.lower():
        gen "Is that a rhetorical question, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her "Right... I guess it was..." ("silly", "narrow", "annoyed", "up")
    else:
        gen "No, [name_hermione_genie], it does not." ("base", xpos="far_left", ypos="head")
        her "Really? I'm relie--" ("base", "closed", "base", "up")
        gen "--It makes you a {b}cumslut{/b}." ("grin", xpos="far_left", ypos="head")
        her "I'm a what?" ("open", "squint", "annoyed", "mid")
        gen "A cumslut. A cum-loving jizz guzzler." ("grin", xpos="far_left", ypos="head")
        her "...So there's something wrong with me after all..." ("angry", "narrow", "annoyed", "down")
        gen "I didn't say that." ("grin", xpos="far_left", ypos="head")
        her "...?" ("soft", "wink", "worried", "mid")
        gen "You may be a cumslut, but you're also {b}my{/b} cumslut, first and foremost." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ah*{heart} Y-Your cumslut...?" ("disgust", "squint", "worried", "mid")
        gen "Yes, you're my favourite cum receptacle, the smartest cumslut on the block." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "I'm your favourite... The smartest...{heart}{heart}" ("silly", "narrow", "base", "dead")
        her @ cheeks blush "In that case..." ("base", "narrow", "low", "mid")

    her "Would you be so kind and douse your favourite cumslut with a fresh layer of your nasty jizz?" ("open_wide_tongue", "narrow", "annoyed", "up")
    gen "Oh that did it, you filthy slut!" ("grin", xpos="far_left", ypos="head")
    gen "HERE IT COMES!!!" ("angry", xpos="far_left", ypos="head")
    her "Shoot it wherever you want [name_genie_hermione]..." ("open_wide_tongue", "narrow", "worried", "mid")

    menu:
        "\"Take it on your tits!\"":
            # Cum on shirt
            $ _cum_location = "chest"
            her "Please cover my tits with your sticky semen! I need it, [name_genie_hermione]!" ("silly", "narrow", "annoyed", "up", ypos="head", flip=False)
            nar "Hermione keeps jerking your cock with a smile."
            gen "Get ready whore, here comes your reward!" ("angry", xpos="far_left", ypos="head")
            her "...{heart}" ("silly", "narrow", "base", "dead")
            nar "Hermione leans back, protruding her chest to give you a better target."

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(breasts="light", body="light")

            her "{heart}{heart}{heart}" ("silly", "narrow", "worried", "down", xpos="right", ypos="base")
            gen "{size=+5}*ARGH*! YES!!! RIGHT between your TITS!{/size}" ("grin", xpos="far_left", ypos="head")

            $ hermione.set_cum(breasts="heavy")

            gen "That's it! All over your tits!" ("base", xpos="far_left", ypos="head")
            her "......" ("soft", "narrow", "annoyed", "up")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

            her "It's so warm...{heart}" ("grin", "narrow", "base", "dead")
            gen "That it is." ("base", xpos="far_left", ypos="head")

        "\"Take it on your face, slut!\"":
            # Cum on face
            $ _cum_location = "face"
            nar "Hermione bends down and holds your cock in front of her face."
            gen "Get ready cumslut, I'm going to paint your pretty face white!" ("angry", xpos="far_left", ypos="head")
            her "Please do! I need it, [name_genie_hermione]!" ("grin", "narrow", "annoyed", "up", ypos="head", flip=False)
            gen "{size=+5}*ARGH*! YES!!!{/size}" ("grin", xpos="far_left", ypos="head")
            her "..." ("open_wide_tongue", "narrow", "annoyed", "up")
            nar "You erupt onto her, dousing her entire face in thick layers of spunk."

            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
            call her_chibi_scene("hj_cum_on")
            call cum_block

            $ hermione.set_cum(face="light")

            her "*Ahhh* {i}it'shhh sho warm and shticky{/i}.{heart}{heart}{heart}" ("open_wide_tongue", "narrow", "annoyed", "up",xpos="right",ypos="base")

            $ hermione.set_cum(face="heavy", hair="light")

            gen "Yes... I Feel so much better now..." ("grin", xpos="far_left", ypos="head")
            her "{size=-2}Me too...{/size}" ("silly", "narrow", "worried", "dead")

            call her_chibi_scene("hj_cum_on_done")
            call ctc

    gen "You did great, [name_hermione_genie], excellent performance!" ("grin", xpos="far_left", ypos="head")
    gen "But I think it's time for your classes." ("base", xpos="far_left", ypos="head")
    her "*Huh*? Classes?" ("silly", "happyCl", "worried", "mid")
    her "Oh no, what have I done!!" ("normal", "wide", "worried", "mid")

    if _cum_location == "face":
        her "I can't attend classes with your cum on my face!" ("shock", "happyCl", "worried", "mid")
    elif _cum_location == "chest":
        her "I can't attend classes with your cum on my chest!" ("angry", "happyCl", "worried", "mid")

    gen "Not with that attitude." ("base", xpos="far_left", ypos="head")
    gen "I chose where to cum, but it was you who gave me the choice." ("base", xpos="far_left", ypos="head")
    gen "Learn to live with the consequences of your actions, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "But..." ("angry", "narrow", "worried", "mid")
    gen "You're smart, you'll figure something out." ("base", xpos="far_left", ypos="head")
    her "(......am I really, though?)" ("angry", "narrow", "worried", "down")

    show screen blkfade
    with d3

    nar "You tuck your cock back into your robe."

    call her_chibi("stand", "desk", "base")
    call gen_chibi("sit_behind_desk")
    with d3
    pause.2

    hide screen blkfade
    with d3

    call bld
    gen "I'll see you after classes. You know the drill." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "... Yes, [name_genie_hermione]..." ("soft", "narrow", "annoyed", "down", xpos="right", ypos="base")

    call her_walk("door")

    her "(What am I going to do now?...)" ("annoyed", "happyCl", "low", "dead")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_cumslut_e1_return:

    call her_walk(action="enter", xpos="mid", ypos="base")

    #if _cum_location == 1: # TODO: No can do. Requires rewrite.
        # Cum under shirt
        #her "... I did it, [name_genie_hermione]." ("base", "happy", "base", "mid",xpos="right",ypos="base")
        #her "I kept your cum on me all day." ("base", "base", "base", "R")

        #menu:
            #"\"Fifty points to Gryffindor!\"":
                #$ gryffindor += 50
                #her "Thank you [name_genie_hermione], will that be all?" ("soft", "base", "base", "mid")
                #gen "Yes [name_hermione_genie], you may leave now." ("base", xpos="far_left", ypos="head")

            #"\"Tell me about your day.\"":
                #her "It was a pretty normal day, I had potions class and then transfiguration." ("open", "closed", "base", "mid")
                #gen "And do you think that anyone noticed?" ("base", xpos="far_left", ypos="head")
                #her "I don't think so [name_genie_hermione]. Ginny Weasley asked me about it during transfiguration class though." ("soft", "base", "base", "mid")
                #gen "And what did you tell her?" ("base", xpos="far_left", ypos="head")
                #her "I just said that I spilled some {i}Wiggenweld potion{/i} on myself in potions class." ("open", "base", "base", "mid")
                #gen "Very cunning of you. Fifty points to Gryffindor." ("base", xpos="far_left", ypos="head")
                #$ gryffindor += 50
                #her "Thank you [name_genie_hermione], if that's all I might head to bed." ("soft", "base", "base", "mid")
                #gen "Very well, goodnight [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                #her "Good night [name_genie_hermione]." ("base", "base", "base", "mid")

    if _cum_location == "bottom":
        # Cum on skirt

        $ hermione.set_cum(crotch="heavy")

        her "... I did it [name_genie_hermione]." ("normal", "happyCl", "worried", "mid", xpos="mid", ypos="base", trans=fade)
        her "I kept your cum on me all day!" ("angry", "happyCl", "worried", "mid",emote="sweat")
        gen "(*Heh*, I would have never expected her to say that out loud...)" ("base", xpos="far_left", ypos="head")

        if _events_filtered_completed_all:
            menu:
                "\"Fifty points to Gryffindor!\"":
                    $ gryffindor += current_payout
                    her "Thank you [name_genie_hermione], will that be all?" ("annoyed", "base", "worried", "R")
                    gen "Yes [name_hermione_genie], you may leave now." ("base", xpos="far_left", ypos="head")

                    jump hg_pr_cumslut_e1_return.end

                "\"Tell me about your day.\"":
                    pass
        else:
            gen "Tell me about your day, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        her "It was a pretty normal day at first. For starters I had potions class and then transfiguration...--" ("open", "base", "worried", "R")
        gen "I want you tell me about the deed, not your boring classes." ("base", xpos="far_left", ypos="head")
        gen "Did anyone notice the gift I left on you?" ("base", xpos="far_left", ypos="head")
        her "Oh..." ("soft", "base", "worried", "mid")
        her "I think some people did, [name_genie_hermione]." ("angry", "happyCl", "worried", "mid")
        her "I could hear The first years all whispering as I walked past." ("angry", "base", "worried", "down")
        gen "And how did you feel?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Ashamed, but also a little excited. I just wish that they knew why I was doing this." ("angry", "narrow", "worried", "R")
        gen "Speaking of which, fifty points to Gryffindor!" ("base", xpos="far_left", ypos="head")
        $ gryffindor += current_payout
        her "Oh, right the points, thank you [name_genie_hermione]." ("open", "narrow", "worried", "mid")
        her "if that's all I might head to bed." ("normal", "narrow", "worried", "R")
        gen "Very well, goodnight [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "Good night [name_genie_hermione]." ("upset", "base", "worried", "mid")

    else:
        # Cum on hair

        $ hermione.set_cum(hair="heavy")

        her @ tears mascara "... I did it [name_genie_hermione]." ("upset", "narrow", "base", "dead", xpos="mid", ypos="base", trans=fade)
        her @ tears mascara_soft_blink "I kept your cum on me all day." ("upset", "happyCl", "worried", "mid")

        if _events_filtered_completed_all:
            menu:
                "\"Fifty points to Gryffindor!\"":
                    $ gryffindor += 50
                    $ states.her.mood += 5
                    her @ tears mascara_soft "..." ("annoyed", "narrow", "annoyed", "mid")
                    gen "Well [name_hermione_genie], you may leave now." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "*Hmph*..." ("angry", "narrow", "annoyed", "mid", emote="angry")

                    jump hg_pr_cumslut_e1_return.end

                "\"Tell me about your day.\"":
                    pass
        else:
            gen "Tell me about your day, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        $ states.her.mood += 10
        her @ tears mascara_soft_blink "My day..." ("normal", "happyCl", "worried", "mid")
        her @ tears mascara_soft_blink "I've never been so ashamed!" ("angry", "happyCl", "worried", "mid",emote="sweat")
        gen "Oh? Did your friends treat you poorly?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara_soft_blink "No! That's the worst part!" ("scream", "closed", "angry", "mid")
        her @ tears mascara_soft_blink "I expected to be an outcast, to sit by myself and not have Ginny or Luna talk to me." ("annoyed", "base", "worried", "R")
        her @ tears mascara "But they didn't even acknowledge the fact that I was covered in cum!" ("annoyed", "narrow", "angry", "R")
        her @ tears mascara_soft_blink "They acted as if nothing was wrong." ("mad", "happyCl", "worried", "mid")
        her @ tears mascara_soft_blink "Well... Maybe except for Luna, she was looking at me odd..." ("mad", "happyCl", "worried", "mid")
        her @ tears mascara_soft_blink "At one point, she even tried to take a whiff at me... but Ginny..." ("mad", "happyCl", "worried", "mid")
        her @ tears mascara_soft "I tried to provoke a response from Ginny by asking her what she thought of my hair!" ("angry", "base", "base", "mid")
        gen "And what was her reaction?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara_soft_blink "She said that it suited me!" ("upset", "happyCl", "worried", "mid")
        gen "Maybe they're just used to you acting like this." ("base", xpos="far_left", ypos="head")
        her @ tears mascara_soft "That's the problem! They think that this slutty persona is who I am now!" ("angry", "base", "worried", "mid")
        gen "Would it really be so bad if you let go for once? Take example from your friends." ("base", xpos="far_left", ypos="head")
        her @ tears mascara "Let go... You tell me to--" ("angry", "wide", "worried", "mid")
        her @ tears mascara "I'm leaving, [name_genie_hermione]." ("upset", "base", "angry", "R")

    label .end:

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_cumslut_e2_return:

    call her_walk(action="enter", xpos="mid", ypos="base")

    if _cum_location == "legs":
        # Cum on legs

        $ hermione.set_cum(legs="heavy")

        her "... I did it, [name_genie_hermione]." ("annoyed", "happy", "base", "mid", xpos="mid", ypos="base", trans=fade)
        her "I kept your cum on me all day." ("normal", "base", "base", "R")

        if _events_filtered_completed_all:
            menu:
                "\"Good Work!\"":
                    her "Thank you [name_genie_hermione], will that be all?" ("soft", "base", "base", "mid")
                    gen "Yes [name_hermione_genie], you may leave now." ("base", xpos="far_left", ypos="head")

                    jump hg_pr_cumslut_e2_return.end

                "\"Tell me about your day.\"":
                    pass

        gen "Tell me how your day went." ("base", xpos="far_left", ypos="head")
        her "It was a pretty normal day, well, except for Luna..." ("open", "closed", "worried", "mid")
        gen "What happened with Miss Lovegood?" ("base", xpos="far_left", ypos="head")
        her "She kept trying to tell me that a Cornish pixie had left me a 'present'." ("annoyed", "narrow", "angry", "R")
        gen "I have been called many things, but a cornish pixie? That's a first." ("base", xpos="far_left", ypos="head")
        her "I didn't know what she was talking about at first. Cornish pixies are nasty little things that would never do anything nice." ("disgust", "narrow", "base", "mid_soft")
        gen "(I've walked into that one...)" ("base", xpos="far_left", ypos="head")
        gen "Well, what happened afterwards?" ("base", xpos="far_left", ypos="head")
        her "I asked her to explain herself, and then she ran a finger up my leg, scooping up some of your cum!" ("angry", "base", "base", "mid_soft")
        gen "Really?" ("base", xpos="far_left", ypos="head")
        her "That's not all--" ("angry", "narrow", "base", "mid_soft")
        her "She then put the slimy finger in her mouth, and gave it a taste!" ("open_tongue", "narrow", "base", "mid_soft")
        gen "I don't believe you." ("base", xpos="far_left", ypos="head")
        her "Oh believe me, I was just as shocked as you are right now." ("open", "closed", "base", "mid")
        gen "I'll say this, you certainly have made this old man very happy." ("grin", xpos="far_left", ypos="head")
        her "I'm glad, [name_genie_hermione]..." ("soft", "narrow", "worried", "L")

    elif _cum_location == "chest":
        # Cum on shirt

        $ hermione.set_cum(breasts="heavy", body="light")

        her "... I did it, [name_genie_hermione]." ("normal", "happyCl", "worried", "mid", xpos="mid", ypos="base", trans=fade)
        her "I kept your cum on me all day." ("angry", "happyCl", "worried", "mid",emote="sweat")

        if _events_filtered_completed_all:
            menu:
                "\"Good Work!\"":
                    her "Thank you [name_genie_hermione], will that be all?" ("annoyed", "base", "worried", "R")
                    gen "Yes [name_hermione_genie], you may leave now." ("base", xpos="far_left", ypos="head")

                    jump hg_pr_cumslut_e2_return.end

                "\"Tell me about your day.\"":
                    pass

        gen "Tell me how your day was." ("base", xpos="far_left", ypos="head")
        her "I had Defence against the dark arts class and then Herbology." ("annoyed", "base", "worried", "R")
        gen "..." ("base", xpos="far_left", ypos="head")
        her "R-right... I'll get to the point." ("grin", "happyCl", "worried", "mid")
        her "I think most people noticed the stains, [name_genie_hermione]. I'm not sure if they all knew it was cum, though." ("open", "narrow", "worried", "down")
        gen "How did that make you feel?" ("base", xpos="far_left", ypos="head")
        her "Cheap... Facing everyone pointing out the stains and me trying to explain them was hard..." ("disgust", "narrow", "worried", "L")
        gen "Was it as difficult as making the choice to skip on free points?" ("base", xpos="far_left", ypos="head")
        her "I suppose not... As long as it makes you happy." ("open", "narrow", "worried", "mid")
        gen "I'm glad to hear it. You are dismissed." ("base", xpos="far_left", ypos="head")

    else:
        # Cum on face

        $ hermione.set_cum(face="heavy", hair="light")

        her @ tears mascara "... I did it, [name_genie_hermione]." ("normal", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
        her @ tears mascara "I kept your cum on my face...{w=0.8} all day." ("soft", "narrow", "low", "mid")

        if _events_filtered_completed_all:
            menu:
                "\"Good Work!\"":
                    her @ tears mascara "..." ("annoyed", "narrow", "base", "dead")
                    gen "Well [name_hermione_genie], you may leave now." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "Did I at least make you happy?" ("open", "narrow", "annoyed", "mid")
                    gen "You did." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "I'm glad..." ("annoyed", "closed", "base", "mid")

                    jump hg_pr_cumslut_e2_return.end

                "\"Tell me about your day.\"":
                    pass

        gen "Are you alright?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara "What do you think.." ("angry", "narrow", "worried", "mid")
        gen "......Could you tell me what happened?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara "You want to know what happened...?" ("angry", "happy", "angry", "mid")
        her @ tears mascara "Oh, you know, it was a completely normal day!" ("angry", "narrow", "angry", "mid")
        gen "Really? Nothing strange happened at all?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara "No. Everyone treated me how I deserved to be treated." ("scream", "closed", "angry", "mid")
        gen "And how's that?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara "Like a slut..." ("disgust", "base", "angry", "mid")
        her @ tears mascara "Boys catcalled me..." ("annoyed", "narrow", "angry", "R")
        her @ tears mascara "Girls have mocked me... Put me down..." ("mad", "closed", "worried", "mid")
        her @ tears mascara_soft "Snape made me stand in front of others during one of his classes." ("angry", "base", "base", "mid")
        gen "What for? Did he ask you to do something?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara_soft_blink "No, he asked nothing of me... He just made me stood there, with everyone looking at me..." ("angry", "happyCl", "worried", "mid")
        gen "Did your friends say anything?" ("base", xpos="far_left", ypos="head")
        her @ tears mascara_soft "That's the worst part. They said nothing." ("angry", "base", "worried", "mid")
        her @ tears mascara_soft_blink "It's like they don't even care what I'm doing for them." ("angry", "happyCl", "worried", "mid")
        gen "......" ("base", xpos="far_left", ypos="head")
        her @ tears mascara "......" ("annoyed", "closed", "worried", "mid")
        her @ tears mascara_soft "Did I...{w=0.5} make you happy at least?" ("soft", "narrow", "worried", "mid")
        gen "You did more than that, you've made me very proud." ("base", xpos="far_left", ypos="head")
        her "Really?" ("base", "narrow", "worried", "mid", tears="mascara")
        gen "Truly." ("base", xpos="far_left", ypos="head")

    her "(............)" ("soft", "narrow", "worried", "mid")
    gen "Do you have something more to say?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "N-no, have a goodnight, [name_genie_hermione]." ("open", "narrow", "worried", "R")
    gen "Goodnight, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    $ hermione.set_face(tears=False)

    label .end:

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_cumslut_e3_return:

    call her_walk(action="enter", xpos="mid", ypos="base")

    if _cum_location == "chest":
        # Cum on shirt

        $ hermione.set_cum(breasts="heavy")

        nar "Hermione returns to your office, her breasts still stained with the remains of your mighty load."
        her "......[name_genie_hermione]." ("annoyed", "squint", "angry", "R", xpos="mid", ypos="base", trans=fade)
        gen "Oh, did you finish your task--" ("base", xpos="far_left", ypos="head")
        her "What do you think?!" ("angry", "happyCl", "worried", "mid", emote="sweat")
        gen "(*Hmm*)" ("base", xpos="far_left", ypos="head")

        if _events_filtered_completed_all:
            menu:
                "\"Good Work!\"":
                    her "......" ("base", "base", "base", "mid")
                    gen "You may leave now." ("base", xpos="far_left", ypos="head")

                    jump hg_pr_cumslut_e3_return.end

                "\"Tell me about your day.\"":
                    pass
                
        gen "Tell me what's up." ("base", xpos="far_left", ypos="head")
        her "Your school sucks, that's what is up!" ("annoyed", "narrow", "angry", "R")
        gen "I guess school sucks for some more, while others do the sucking." ("grin", xpos="far_left", ypos="head")
        her "...*glares*..." ("annoyed", "narrow", "annoyed", "mid")
        gen "*Ahem* Please, go on." ("base", xpos="far_left", ypos="head")
        her "After I left your office, I was close to having a panic attack, so I rushed towards the bathrooms." ("annoyed", "narrow", "angry", "R")
        her "Unfortunately for me, the bathrooms were occupied by a bunch of sluts from Slytherin..." ("open", "narrow", "angry", "R")
        gen "Interesting." ("base", xpos="far_left", ypos="head")
        her "So, as soon as I entered, they noticed my state of disarray... And the white stains on my chest." ("angry", "narrow", "angry", "down")
        her "I tried to hide it, and rush inside one of the stalls, but as soon as tried to go past them--" ("open", "narrow", "angry", "R")
        her "--one of them grabbed me by the arm, and asked me if I blew a Gallopogriff, because, here I quote--" ("open", "narrow", "worried", "L")
        her "\"nobody cums that much\"..." ("annoyed", "narrow", "angry", "mid")
        gen "(Little do they know...)" ("base", xpos="far_left", ypos="head")
        gen "What happened then?" ("base", xpos="far_left", ypos="head")
        her "You won't believe it..." ("angry", "narrow", "angry", "R")
        gen "Try me." ("base", xpos="far_left", ypos="head")
        her "She... She started a conversation with me." ("upset", "narrow", "angry", "mid")
        gen "That's all? She just wanted to have a chat with you?" ("base", xpos="far_left", ypos="head")
        her "What do you mean 'that's all'?" ("open", "happy", "angry", "mid")
        her "Me, a Gryffindor, chit-chatting with the enemy?!" ("angry", "happy", "angry", "mid")
        gen "I think you're exaggerating a little..." ("base", xpos="far_left", ypos="head")
        gen "She's still one of my students, you know." ("base", xpos="far_left", ypos="head")
        her "True... But still..." ("annoyed", "narrow", "angry", "R")
        gen "Anyway, what happened next?" ("base", xpos="far_left", ypos="head")
        her "Well... I was so shooked that I didn't really know what to do so..." ("open", "narrow", "angry", "mid")
        her @ cheeks blush "I went with the flow, and skipped class." ("annoyed", "narrow", "angry", "R")
        gen "You \"went with the flow\", *huh*?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Y-yes, that's one of the expressions I learned from our interaction." ("annoyed", "narrow", "low", "R")
        gen "Sounds to me like you've had a positive interaction with one of the Slytherins." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "That may be true, but she's still a Slytherin, and one good egg doesn't make the others smell any less!" ("angry", "narrow", "angry", "R")
        gen "It looks like you're deflecting the fact that not all Slytherins are bad, but if you say so." ("base", xpos="far_left", ypos="head")
        her "*Hmph*..." ("annoyed", "narrow", "angry", "R")
        gen "I think I've heard enough for now." ("base", xpos="far_left", ypos="head")
        gen "Dismissed." ("base", xpos="far_left", ypos="head")

    else:
        # Cum on face

        $ hermione.set_cum(face="heavy", hair="light")

        nar "Hermione returns to your office, her face caked with patches of cum."
        her @ cheeks blush "I did it, [name_genie_hermione]." ("angry", "happy", "base", "down", xpos="mid", ypos="base", trans=fade)
        her @ cheeks blush "I kept your cum on me all day." ("open", "narrow", "base", "R")

        if _events_filtered_completed_all:

            menu:
                "\"Good Work!\"":
                    her "Thank you, [name_genie_hermione]. Is that everything?" ("soft", "happy", "base", "R")
                    gen "Yes [name_hermione_genie], you can go clean up now." ("base", xpos="far_left", ypos="head")

                    jump hg_pr_cumslut_e3_return.end

                "\"Tell me about your day.\"":
                    pass

        her @ cheeks blush "As for my day..." ("upset", "happy", "base", "R")
        her @ cheeks blush "It was a normal day [name_genie_hermione]. Well. Whatever the new normal is for me now." ("soft", "narrow", "annoyed", "R")
        her @ cheeks blush "I got called names again, and some of the boys asked me if I wanted \"a refill\"." ("open", "narrow", "base", "L")
        her @ cheeks blush "Cho Chang has caught a glimpse of me before class, and started laughing..." ("angry", "narrow", "worried", "down")
        gen "And how did that make you feel?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Embarrased..." ("disgust", "narrow", "base", "mid")
        gen "Would it help knowing she went through the same thing?" ("base", xpos="far_left", ypos="head")
        her "D-did she?" ("shock", "base", "worried", "mid")
        gen "You know me. What do you think?" ("base", xpos="far_left", ypos="head")
        her "... I guess that's a yes." ("grin", "narrow", "annoyed", "mid")
        her "I'll throw it at her face the next time I see her! The slut will never see it coming!" ("grin", "narrow", "annoyed", "up")
        gen "(I hope a little competition between them doesn't hurt...)" ("base", xpos="far_left", ypos="head")
        gen "I think we're done here. Good work, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]." ("grin", "happy", "worried", "mid")

    label .end:

    call her_walk(action="leave")

    jump end_hermione_event
