
### Give Classmate A Handjob ###

label start_hg_pr_handjob:

    # Setup
    $ current_payout = 55

    if not _events_completed_any:
        gen "{size=-4}(Tell her to give a handjob to one of her classmates?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu
    return

label hg_pr_handjob:

    call start_hg_pr_handjob

    her "" (xpos="mid", ypos="base", trans=fade)

    #Intro
    if not _events_completed_any:

        if states.her.public_level < 12:
            gen "[name_hermione_genie], I want you to do something different today..." ("base", xpos="far_left", ypos="head")
            her "...?" ("normal", "squint", "angry", "mid")
            gen "I want you to give a handjob to one of your classmates." ("base", xpos="far_left", ypos="head")

            $ _event.cancel()
            jump too_much_public

        gen "[name_hermione_genie], I want you to do something different today..." ("base", xpos="far_left", ypos="head")
        her "..........." ("soft", "base", "base", "mid")
        gen "I want you to go out there and have sex with one of your classmates." ("grin", xpos="far_left", ypos="head")

        stop music fadeout 0.5
        with hpunch

        her "{size=+5}What?!!{/size}" ("shock", "wide", "base", "stare")
        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
        her "Now you have done it, [name_genie_hermione]! You crossed the line!" ("angry", "base", "angry", "mid")
        her "I know I did sell you a couple of rather questionable favours in the past..."
        gen "{size=-4}*Heh* a couple she says...{/size}" ("base", xpos="far_left", ypos="head")
        with vpunch
        her "{size=+5}--But THIS?!{/size}" ("scream", "base", "angry", "mid", emote="angry")
        her "I cannot believe that you would ask one of your pupils to... to..."
        her "We are done here, [name_genie_hermione]!" ("angry", "base", "angry", "mid", emote="angry")
        gen "Alright, alright, calm down, would you?" ("base", xpos="far_left", ypos="head")
        her "I most certainly will not, [name_genie_hermione]! This is beyond inappropriate!" ("scream", "closed", "angry", "mid")
        gen "Alright, fine, maybe I really did cross some sort of line this time..." ("base", xpos="far_left", ypos="head")
        her "You think [name_genie_hermione]?! You think!!?" ("angry", "base", "angry", "mid")
        gen "Yes, I apologise..." ("base", xpos="far_left", ypos="head")
        her "........." ("annoyed", "narrow", "annoyed", "mid")
        gen "How about we try something less... engaging instead?" ("base", xpos="far_left", ypos="head")
        her "............" ("upset", "closed", "base", "mid")
        gen "I'll be willing to grant Gryffindor {number=current_payout} points." ("base", xpos="far_left", ypos="head")
        gen "All I ask in return is..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..........?" ("angry", "base", "angry", "mid")
        gen "... that you go out there and give some lucky boy a handjob..." ("base", xpos="far_left", ypos="head")
        her "!!!......" ("angry", "base", "angry", "mid")
        gen "Oh, come on... Just a harmless handjob." ("base", xpos="far_left", ypos="head")
        her "..." ("disgust", "narrow", "base", "mid_soft")
        gen "{number=current_payout} house points..." ("base", xpos="far_left", ypos="head")
        her ".............." ("annoyed", "narrow", "angry", "R")
        her "I am glad that you came to your senses, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
        gen "Oh, but of course. Thank you for keeping me in check." ("base", xpos="far_left", ypos="head")
        gen "Are you up for it then?" ("base", xpos="far_left", ypos="head")
        her "I am willing to give it a try..." ("annoyed", "narrow", "angry", "R")
        gen "Splendid... See you tonight then." ("base", xpos="far_left", ypos="head")
    else:
        if states.her.tier >= 6:
            gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "What do you think about going out there and giving a handjob to one of your classmates?" ("base", xpos="far_left", ypos="head")
            her "I don't mind, [name_genie_hermione]." ("open", "narrow", "base", "down")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            her "Yes... I mean, it's just a handjob..." ("soft", "base", "worried", "R")
            gen "Great. Go have fun then!" ("base", xpos="far_left", ypos="head")
            gen "And report back to me after your classes, as usual." ("base", xpos="far_left", ypos="head")
            her "Of course, [name_genie_hermione]." ("base", "happyCl", "base", "mid")
        elif states.her.tier >= 5:
            gen "Ready to go have sex with one of your classmates yet?" ("base", xpos="far_left", ypos="head")

            stop music fadeout 1.0

            her "What?" ("scream", "wide", "base", "mid")
            her "Of course not! I would never--" ("scream", "closed", "angry", "mid")
            gen "How about a handjob then?" ("base", xpos="far_left", ypos="head")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
            her "..............." ("annoyed", "narrow", "angry", "R")
            gen "Come on [name_hermione_genie]... You've given a handjob before." ("base", xpos="far_left", ypos="head")
            her "*Hmm*.........." ("annoyed", "narrow", "annoyed", "mid")
            her "{number=current_payout} house points?" ("annoyed", "narrow", "annoyed", "mid")
            gen "Naturally." ("base", xpos="far_left", ypos="head")
            her "Well, alright... I'll see what I can do..." ("angry", "narrow", "base", "down")
        else:
            gen "Alright then, [name_hermione_genie], for today's favour..." ("base", xpos="far_left", ypos="head")
            her "........." ("angry", "base", "base", "mid")
            gen "I require you to give a handjob to the boy of your choosing!" ("base", xpos="far_left", ypos="head")
            her "... Again?" ("angry", "narrow", "base", "down")
            gen "Sure, why not?" ("base", xpos="far_left", ypos="head")
            gen "You'll be receiving {number=current_payout} points for the Gryffindor house, of course." ("base", xpos="far_left", ypos="head")
            her ".........." ("annoyed", "base", "worried", "R")
            gen "So... Are you up for it, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "I will see what I can do..." ("annoyed", "narrow", "angry", "R")
            gen "Splendid!" ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_handjob_fail:
    call start_hg_pr_handjob

    gen "[name_hermione_genie], I was thinking..." ("base", xpos="far_left", ypos="head")
    her "Yes?" ("open", "squint", "base", "mid")
    gen "Wouldn't it be great, if you gave a handjob to one of your classmates?" ("base", xpos="far_left", ypos="head")

    jump too_much_public

label end_hg_pr_handjob:
    $ gryffindor += current_payout #55
    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if states.her.tier <= 4 and not _events_completed_any:
        her ".........." ("upset", "narrow", "angry", "R", ypos="base", xpos="base", flip=True, trans=d3)
        her "(Do I really have to do this?)" ("upset", "closed", "angry", "mid")
        her "*Sigh*" ("soft", "closed", "angry", "mid")

    $ states.her.status.public_handjob = True

    call her_chibi("leave")

    label .quick_end:

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    jump end_hermione_event

label hg_pr_handjob_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("open", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you lend a hand to the needy?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..."

    if _events_filtered_completed_all:
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_handjob

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("annoyed", "narrow", "angry", "R")
        gen ".............." ("base", xpos="far_left", ypos="head")

    gen "Then tell me, how did it go?" ("base", xpos="far_left", ypos="head")

    return

### Tier 4 ###

label hg_pr_handjob_T4_E1:

    call hg_pr_handjob_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Quite awful... Of course..." ("annoyed", "squint", "angry", "mid")
    gen "Just tell me what happened, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "I made a complete fool out of myself, that's what happened, [name_genie_hermione]." ("disgust", "narrow", "base", "mid_soft")
    her "....."
    gen "..." ("base", xpos="far_left", ypos="head")
    her ".........." ("annoyed", "base", "worried", "R")
    her "I don't want to talk about it..." ("annoyed", "narrow", "angry", "R")
    her "You told me to go and touch a student's penis, and I did just that, [name_genie_hermione]."
    her "Please, just let me have my points now, [name_genie_hermione]..." ("open", "base", "base", "mid")
    gen "I did not tell you to \"go and touch a student's penis\", [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "I told you to give one of your classmates a handjob." ("base", xpos="far_left", ypos="head")
    her "Well, yes... That's what I meant, of course..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Did you make him cum, then?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Did his \"wee-wee\" shoot white stuff at you, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Well..." ("annoyed", "base", "worried", "R")
    her "No, it did not..." ("normal", "happyCl", "worried", "mid")
    gen "Poor guy... Must've blue-balled him." ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"In that case, it doesn't count.\"":
            stop music fadeout 4.0
            her "What?" ("angry", "wide", "base", "stare")
            her "But, [name_genie_hermione], I..."
            gen "If you didn't make him cum, then it wasn't a proper handjob. Period." ("base", xpos="far_left", ypos="head")
            her "But... But what was it then...?" ("angry", "base", "base", "mid")
            gen "How should I know? A cock massage?" ("base", xpos="far_left", ypos="head")
            her "*Aww*..." ("angry", "narrow", "base", "down")
            her "But I really tried my best..."
            gen "No handjob - no payment, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "....." ("angry", "base", "base", "mid")
            gen "You are free to go." ("base", xpos="far_left", ypos="head")
            her "........." ("annoyed", "narrow", "angry", "R")

            $ states.her.mood +=9
            jump end_hg_pr_handjob.no_points

        "\"You shall only get half the payment.\"":
            $ current_payout = int(current_payout/2)

            her "Oh...?" ("open", "base", "base", "mid")
            gen "Is that a problem, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "N-No [name_genie_hermione]... It's only fair, I suppose..." ("angry", "narrow", "base", "down")
            gen "Of course it is!" ("base", xpos="far_left", ypos="head")

        "\"Well, you did try. Here are your points.\"":
            her "Really?" ("angry", "base", "base", "mid")
            her "Thank you, [name_genie_hermione]!" ("open", "narrow", "worried", "down")
            her "I promise, I will try harder next time!" ("base", "base", "base", "mid")
            her "*Ehm*... Should you request a similar favour in the future, I mean..." ("upset", "wink", "base", "mid")

    jump end_hg_pr_handjob

label hg_pr_handjob_T4_E2:

    call hg_pr_handjob_intro

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "It went well, [name_genie_hermione]..." ("open", "base", "base", "mid")
    her "I asked one of the Gryffindor boys to let me do \"it\" for him..."
    her @ cheeks blush "To my surprise, he agreed eagerly." ("open", "base", "base", "mid")
    gen "Shocker..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "So we hid behind one of those huge tapestries in the east wing..." ("open", "closed", "base", "mid")
    her @ cheeks blush "And I... Wanked him until he came..." ("annoyed", "narrow", "angry", "R")
    her "........."
    her @ cheeks blush "After he finished, I asked him to keep the whole thing a secret of course... Although..." ("angry", "base", "base", "mid")
    gen "What's the matter, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    gen "Doubting the honesty of your fellow Gryffindor?" ("base", xpos="far_left", ypos="head")
    her "Of course not, [name_genie_hermione]." ("upset", "closed", "base", "mid")
    her @ cheeks blush "..........................." ("angry", "narrow", "base", "down")
    her @ cheeks blush "Still... Performing this sort of task could really damage my reputation..." ("angry", "base", "base", "mid")
    gen "Is this your way of asking for a raise, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    gen "As it stands, {number=current_payout} points is as high as I can go." ("base", xpos="far_left", ypos="head")
    her "Oh... I see..." ("angry", "narrow", "base", "down")
    gen "Unless, you've changed your mind about having sex with one of your classmates?" ("base", xpos="far_left", ypos="head")
    her "What?" ("shock", "wide", "base", "stare")
    her @ cheeks blush "[name_genie_hermione], I am not a prostitute!" ("angry", "narrow", "base", "down")
    gen "Well, in that case..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_handjob

label hg_pr_handjob_T4_E3:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    gen "[name_hermione_genie], how did it--" ("base", xpos="far_left", ypos="head")
    $ hermione.set_cum(hair="light")
    her "" ("angry", "narrow", "angry", "R", xpos="mid", ypos="base", trans=d3)
    gen "-- Go..." ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Awful, [name_genie_hermione]. Simply awful..." ("scream", "happyCl", "worried", "mid")
    gen "You've got something, right there... In your hair..." ("base", xpos="far_left", ypos="head")
    her "In my--" ("open", "base", "angry", "mid")
    her @ cheeks blush "Oh, no! I thought I got it all off!" ("angry", "happyCl", "base", "mid")
    her "One moment..."

    show screen blkfade
    with d3
    pause.5
    $ hermione.set_cum(None)
    her "" ("upset", "closed", "base", "mid")
    hide screen blkfade
    with d3

    gen "*Hmm*... So, I suppose you have completed your task?" ("base", xpos="far_left", ypos="head")
    her "I did, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    gen "What's the problem, then?" ("base", xpos="far_left", ypos="head")
    her "Boys are jerks, all of them! That is the problem, [name_genie_hermione]!" ("scream", "closed", "angry", "mid")
    her "I was kind enough to offer this one boy a handjob." ("open", "narrow", "angry", "down")
    her "And do you know how he thanked me?" ("angry", "narrow", "angry", "mid")
    her "By ejaculating all over me!" ("scream", "base", "angry", "mid", emote="angry")
    her "And he did that on purpose... I know he did!" ("scream", "closed", "angry", "mid")
    her "Nasty, good for nothing, Ravenclaw..." ("annoyed", "base", "angry", "R")
    gen "He probably just wanted to reward you for a job well done." ("base", xpos="far_left", ypos="head")
    her "What did you say?" ("angry", "base", "worried", "mid")
    gen "I say, job well done, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her "Oh... I see." ("normal", "base", "worried", "mid")

    $ states.her.status.public_cumshot = True

    jump end_hg_pr_handjob

### Tier 5 ###

label hg_pr_handjob_T5_E1:

    call hg_pr_handjob_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "*Ehm*..." ("open", "base", "base", "mid")
    her "Not that good to be honest, [name_genie_hermione]..." ("open", "base", "base", "mid")
    gen "Oh?" ("base", xpos="far_left", ypos="head")
    her "Yes... Let me explain myself, [name_genie_hermione]..." ("annoyed", "base", "worried", "R")
    her "*Ehm*... Well..." ("open", "base", "base", "mid")
    her "So, I was jerking this one boy off, in one of the empty classrooms..." ("open", "base", "base", "mid")
    her "And that nasty ghost Peeves walked in..." ("open", "base", "base", "mid")
    her "Or rather flew in on us..." ("annoyed", "base", "worried", "R")
    her "And as soon as he realised what I was doing to the boy..." ("open", "base", "base", "mid")
    her "He started shouting obscenities at us..." ("open", "base", "base", "mid")
    her "So we had to leave in a hurry..." ("open", "base", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    her "That is not all, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    gen "Go on..." ("base", xpos="far_left", ypos="head")
    her "Well, after that happened, I sort of made a promise to the boy..." ("open", "narrow", "worried", "down")
    her "I promised to meet him after my classes, and..." ("open", "narrow", "worried", "down")
    her "... and finish what I have started..." ("annoyed", "narrow", "annoyed", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "So, did you?" ("base", xpos="far_left", ypos="head")
    her "No, [name_genie_hermione]... Not yet at least..." ("angry", "base", "base", "mid")
    her "I am supposed to meet him around the time I'd be done here, [name_genie_hermione]." ("angry", "base", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    her "So, if you would kindly give me those points in advance..." ("angry", "narrow", "base", "down")
    her "Then I will go meet with the boy right away, and--" ("angry", "narrow", "base", "down")
    her @ cheeks blush "And finish him... I mean, finish what I started." ("open", "base", "base", "R")

    menu:
        "\"No... You failed this favour, [name_hermione_genie].\"":
            stop music fadeout 3.0

            her @ cheeks blush "B-but..." ("open", "base", "base", "mid")
            her "But I gave him my word..." ("angry", "wide", "base", "stare")
            her "I swore on Godric Gryffindor's name..." ("angry", "wide", "base", "stare")
            her "And now I will have to give him a wank no matter what..." ("angry", "narrow", "base", "down")
            gen "Well, I didn't force you to give him that promise, did I?" ("base", xpos="far_left", ypos="head")
            her "......" ("angry", "base", "base", "mid")
            her "This is just not fair!" ("scream", "happyCl", "worried", "mid")

            $ states.her.mood += 20
            jump end_hg_pr_handjob.no_points

        "\"Alright, I'll make an exception, this one time.\"":
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            her "I knew you would understand." ("base", "base", "base", "mid")
            gen "Just make sure you finish your \"job\" properly this time." ("base", xpos="far_left", ypos="head")
            her "Of course, [name_genie_hermione]! I will give him the wank of his life! I promise!" ("base", "happyCl", "base", "mid")

    jump end_hg_pr_handjob

label hg_pr_handjob_T5_E2:

    call hg_pr_handjob_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Fine, I suppose..." ("open", "closed", "base", "mid")
    her "Although I am still not sure how I feel about all of this..." ("annoyed", "base", "worried", "R")
    gen "Your personal feelings are of no concern to me, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "Just tell me more about how it went." ("base", xpos="far_left", ypos="head")
    her "Well, there is not much to tell, [name_genie_hermione]..." ("open", "base", "base", "mid")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Today I gave another handjob to one of my classmates..." ("open", "base", "base", "mid")
    her "Me, Hermione Granger..." ("open", "narrow", "worried", "down")
    her "Giving free handjobs in one of the school's restrooms..." ("angry", "narrow", "base", "down")
    gen "Wait... What do you mean by \"free\"?" ("base", xpos="far_left", ypos="head")
    her "Oh, of course... I do get paid with house points for this..." ("angry", "base", "base", "mid")
    her "But nobody knows about that..." ("angry", "base", "base", "mid")
    her "And to everyone else this just looks like some harlot, doing it for fun..." ("angry", "base", "base", "mid")
    her ".............." ("clench", "narrow", "base", "down")
    her @ cheeks blush "Do you think I'm a slut, [name_genie_hermione]?" ("open", "happy", "base", "mid")

    menu:
        gen "(*Hmm*...)" ("base", xpos="far_left", ypos="head")
        "\"What? Of course not, [name_hermione_genie]!\"":
            her @ cheeks blush ".............." ("base", "base", "base", "R")
            her "You are right, [name_genie_hermione]..." ("base", "narrow", "worried", "down")
            her "I am making this sacrifice for the glory of the Gryffindor house." ("base", "narrow", "worried", "down")
            her "I am not taking pleasure in this sort of activity..." ("soft", "narrow", "annoyed", "up")
            her "Because if I would..." ("annoyed", "narrow", "angry", "R")
            her "That would mean I really am a slut..." ("annoyed", "narrow", "angry", "R")
            her "And I am not..." ("angry", "narrow", "base", "down")
            her "......" ("angry", "narrow", "base", "down")
            her "I am not a slut..." ("angry", "narrow", "base", "down")

        "\"A slut? No... Not yet.\"":
            her "\"Not yet\"??!" ("angry", "base", "base", "mid")
            her ".........." ("angry", "narrow", "base", "down")
            her "Well, of course!" ("scream", "wide", "base", "mid")
            her "You are right, as usual, [name_genie_hermione]!" ("soft", "base", "base", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
            her "I have done a few... naughty things..." ("open", "base", "base", "mid")
            her "But that does not mean anything!" ("open", "base", "base", "mid")
            her "..........." ("annoyed", "narrow", "angry", "R")

        "\"Yes, that's exactly what you are.\"":
            her @ tears soft_blink "I was afraid that you would say that, [name_genie_hermione]..." ("mad", "happyCl", "worried", "mid")
            her "But you are wrong, [name_genie_hermione]." ("mad", "happyCl", "worried", "mid")
            her @ tears soft "You of all people should understand that I take no pleasure in this..." ("angry", "base", "base", "mid")
            her @ tears soft "I just do what needs to be done..." ("normal", "base", "base", "R")
            $ states.her.mood = 10

    her "[name_genie_hermione], can I just get paid now, please?" ("soft", "base", "base", "R")
    gen "Get paid? But you didn't tell me how it went yet." ("base", xpos="far_left", ypos="head")
    her "I didn't?" ("soft", "base", "base", "R")
    her @ cheeks blush "[name_genie_hermione], I gave a handjob to one of my classmates in one of the school's restroom stalls..." ("open", "base", "base", "mid")
    her "I wanked his cock until he came..." ("open", "base", "base", "mid")
    her "Is that not what you told me to do?" ("disgust", "narrow", "base", "mid_soft")
    gen "That's exactly what I told you to do, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Then I would like to get paid now, please." ("annoyed", "closed", "base", "mid")
    gen "........" ("base", xpos="far_left", ypos="head")
    gen "Fine..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_handjob

label hg_pr_handjob_T5_E3:

    call hg_pr_handjob_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Pretty well, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "Great... Tell me more." ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Well, today was a rather busy day..." ("open", "base", "base", "mid")
    her "And I had to catch up on some studying..." ("open", "base", "base", "mid")
    her "So, unfortunately I really had no time to plan things out properly, like I normally would..." ("open", "base", "base", "mid")
    her "Since it was nearing the end of the day, I pretty much just approached the first boy I saw..." ("open", "base", "base", "mid")
    her "And asked him if he wanted me to jerk him off." ("annoyed", "narrow", "angry", "R")
    her "A couple of minutes later I was already stroking him, inside one of the restroom stalls..." ("annoyed", "narrow", "angry", "R")
    gen "How very efficient of you..." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
    her "So, as I was saying..." ("annoyed", "narrow", "angry", "R")
    her "I stroked him until he came..." ("annoyed", "narrow", "angry", "R")
    her "Even though I did this for him, out of the kindness of my heart..." ("annoyed", "narrow", "angry", "R")
    her "The only thing he said before leaving was \"Good job, slut\"..." ("disgust", "narrow", "base", "mid_soft")
    her "Isn't that such a mean thing to say?" ("annoyed", "narrow", "angry", "R")
    her "I thought I was being efficient, but instead it left me feeling cheap... and used." ("upset", "closed", "base", "mid")
    her "But it gets worse..." ("upset", "closed", "base", "mid")
    her "......." ("upset", "closed", "base", "mid")
    her "I think on some level it also made me feel good somehow..." ("angry", "narrow", "base", "down")
    her "All these favours I have been selling to you lately, [name_genie_hermione]..." ("angry", "narrow", "base", "down")
    her "... It's starting to affect me." ("angry", "base", "base", "mid")
    her "[name_genie_hermione], what is happening to me?" ("angry", "base", "base", "mid")

    menu:
        "\"This is nothing... Stop over-thinking it!\"":
            her @ cheeks blush "......." ("open", "happy", "base", "mid")
            her @ cheeks blush "You are probably right, [name_genie_hermione]... As usual." ("base", "base", "base", "R")
            her "This does not have to mean anything..." ("base", "base", "base", "R")

        "\"That is just a natural response...\"":
            her @ cheeks blush "It is?" ("open", "happy", "base", "mid")
            gen "Of course." ("base", xpos="far_left", ypos="head")
            gen "You are a girl, and he is a boy..." ("base", xpos="far_left", ypos="head")
            gen "You got excited, and it made you feel good..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*..." ("base", "base", "base", "R")
            gen "Now, if you were to give a handjob and feel completely indifferent about it..." ("base", xpos="far_left", ypos="head")
            gen "... That would be... unnatural." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I think you are right, [name_genie_hermione]." ("open", "happy", "base", "mid")
            her @ cheeks blush "As usual." ("base", "base", "base", "R") # :)

        "\"Yes! It's all going according to plan!\"":
            her "What?" ("angry", "wide", "base", "stare")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione], did you just say \"It's all going according to plan\"?" ("angry", "base", "angry", "mid")
            gen "Did I?" ("base", xpos="far_left", ypos="head")
            gen "Oh, yes, of course." ("base", xpos="far_left", ypos="head")
            gen "Ensuring that Gryffindor gets the house cup this year." ("base", xpos="far_left", ypos="head")
            gen "That's the plan... And thanks to your hard work, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "It's all going according to my-- I mean, our plan..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("upset", "closed", "base", "mid")

            $ states.her.mood += 5

    jump end_hg_pr_handjob

### Tier 6 ###

label hg_pr_handjob_T6_intro_E1:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    $ hermione.set_cum(hair="light")

    her "[name_genie_hermione]..." ("open", "base", "worried", "mid", xpos="mid", ypos="base", trans=d3)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "I did a bad thing today, [name_genie_hermione]..." ("open", "base", "worried", "R")
    gen "Did you now? Do tell..." ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Yes, I did a bad thing... A very bad thing..."
    her "A very bad and foolish thing..." ("annoyed", "squint", "angry", "mid")
    her "..."
    gen "...................." ("base", xpos="far_left", ypos="head")
    her "......................"
    her "It all started when I decided to wank of two boys at the same time..." ("angry", "closed", "base", "mid")
    gen "Interesting..." ("base", xpos="far_left", ypos="head")
    her @ tears soft "It seemed like such a great idea at first..." ("open", "narrow", "base", "down")
    her @ tears soft "But now I'm worried that they might start boasting about it..." ("angry", "base", "base", "mid")
    gen "Boasting about a handjob? Is that really something to boast about?" ("base", xpos="far_left", ypos="head")
    her @ tears soft "[name_genie_hermione]!" ("annoyed", "base", "worried", "mid")
    gen "There is something in your hair, by the way..." ("base", xpos="far_left", ypos="head")
    her @ tears soft "What? But I swallowed it all... *Err*..." ("soft", "base", "base", "mid")
    her @ cheeks blush tears soft "I mean..." ("clench", "base", "worried", "mid")
    her @ cheeks blush tears soft "*Sigh*" ("open", "base", "base", "R")
    her @ cheeks blush "The reason why I thought they may boast... Is because I sucked them off, [name_genie_hermione]." ("angry", "closed", "base", "R")
    her @ cheeks blush "I did not plan to... But..." ("angry", "base", "base", "R")
    her @ cheeks blush tears soft "They were being so grateful, and--" ("clench", "base", "worried", "mid")
    her @ cheeks blush tears crying "Well, I made them promise not to tell anyone about the handjob, but--" ("angry", "narrow", "base", "down")
    her @ tears crying cheeks blush "I forgot to make them promise about the blowjob!" ("angry", "base", "base", "mid")
    her @ tears crying_blink cheeks blush "They'll tell people for sure, [name_genie_hermione]!" ("angry", "happyCl", "base", "mid")
    her @ cheeks blush tears crying "\"Hermione Granger gave us both a blowjob\"! That's what they'll say!" ("shock", "narrow", "base", "down")
    her @ cheeks blush tears crying_blink "No, no, no... How will I ever face my classmates after this...?" ("angry", "happyCl", "base", "down")
    gen "Calm down, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "I assure you that there's not a single man who would boast to anyone, as long as they think they might get another go with a girl in the future." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "You think so?" ("clench", "base", "worried", "mid")
    gen "I know so, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ tears soft "*Hmm*..." ("normal", "base", "base", "R")
    her @ tears soft "You are probably right, [name_genie_hermione]..." ("soft", "base", "base", "mid")
    her "I suppose if they felt the urge to talk about it, they could still talk to each other..." ("open", "base", "worried", "R")
    her ".........." ("soft", "base", "base", "R")
    her "Thank you for calming me down, [name_genie_hermione]..." ("open", "base", "base", "R")
    gen "Any time..." ("base", xpos="far_left", ypos="head")
    her "Will I get paid for this, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Of course." ("base", xpos="far_left", ypos="head")

    $ states.her.status.public_blowjob = True

    jump end_hg_pr_handjob

label hg_pr_handjob_T6_E2:

    call hg_pr_handjob_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "It went... Particularly well..." ("base", "squint", "base", "mid")
    her "I even did it more than once today, actually..."
    gen "More than once?" ("base", xpos="far_left", ypos="head")
    her "Yes, I believe I did it five times, [name_genie_hermione]..." ("base", "narrow", "base", "mid_soft")
    her "I... got carried away a little I suppose..."
    gen "What do you mean \"five times\", [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    gen "Like... at once?" ("base", xpos="far_left", ypos="head")
    her "No, silly... I mean I wanked off five boys today in total, [name_genie_hermione]." ("base", "squint", "base", "mid")
    gen "I see... That's still an impressive feat, I suppose..." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
    gen "You don't expect me to multiply your payment by five or anything, do you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course not, [name_genie_hermione]." ("base", "base", "base", "R")
    gen "Then why did you do it? Five times, no less!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, it sort of just happened..." ("open", "happy", "base", "mid")
    her "I was jerking off this one boy..."
    her "And another boy walked in on us..."
    her "He called his friends..."
    her @ cheeks blush "One thing led to another..." ("open", "narrow", "base", "down")
    gen "And you ended up jerking off five cocks..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "... yes." ("soft", "closed", "worried", "up")
    gen "One after another?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Mhmm*!" ("base", "closed", "worried", "mid_soft")
    gen "Well done, [name_hermione_genie], absolutely fantastic!" ("grin", xpos="far_left", ypos="head")
    her "" ("base", "narrow", "base", "mid_soft")

    jump end_hg_pr_handjob

label hg_pr_handjob_T6_E3:

    call hg_pr_handjob_intro

    her "It went well, [name_genie_hermione]." ("soft", "base", "base", "mid")
    her "But, *Ehm*..." ("open", "base", "worried", "mid")
    gen "...?" ("base", xpos="far_left", ypos="head")
    her "Well, I..." ("open", "narrow", "base", "down")
    her "..............." ("disgust", "narrow", "base", "down")
    gen "Did you give a classmate to a handjob... I mean, did you give a handjob to a classmate, or what?" ("base", xpos="far_left", ypos="head")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music

    her "I did... And I sort of did it... During class." ("open", "narrow", "worried", "down")
    gen "During class? Now that's impressive..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], you don't understand.... At least give me the oportynity to try and justify myself!" ("angry", "narrow", "base", "mid")
    gen "Go on..." ("base", xpos="far_left", ypos="head")
    her "I was stressing about the task you had given me during our last class for the day... And... Well, I don't even know what came over me..." ("angry", "narrow", "base", "down")
    her @ cheeks blush "But, I suddenly had this incredible urge to do it, right there, during Professor Snape's class." ("angry", "narrow", "worried", "R")
    her "At first, it was just one boy... So, I could at least use my other hand to take notes..."
    her "But then the boy on my other side, noticed it and had me wrap my hand around his cock too."
    gen "You gave two boys handjobs at the same time?!" ("base", xpos="far_left", ypos="head")
    gen "During class?!" ("base", xpos="far_left", ypos="head")
    gen "Snape's class, no less?!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, [name_genie_hermione]..." ("angry", "wink", "base", "mid")
    her @ cheeks blush "I think the boys may have been excited about getting away with it..." ("soft", "narrow", "base", "down")
    her @ cheeks blush "Because what they did, surely can't be described as a regular ejaculation..." ("angry", "closed", "worried", "down")
    her @ cheeks blush "Their cocks simply exploded, and it went everywhere." ("angry", "narrow", "worried", "up")
    gen "You enjoyed it as well, didn't you?" ("base", xpos="far_left", ypos="head")
    her "Well...To be completely honest with you, [name_genie_hermione]... I did." ("soft", "narrow", "base", "down")
    her "Since Professor Snape wasn't realising what I was doing... Well, I don't think I've ever been so excited in my life..." ("smile", "happyCl", "worried", "mid")
    her "God, there was so much cum... My hands looked as if a candle had dripped hot wax all over them." ("grin", "narrow", "base", "up")
    her "Of course, once I realised what kind of situation I had put myself in... I didn't know what to do." ("soft", "narrow", "base", "mid")
    her "I couldn't just go about the rest of class with huge globs of cum all over my hands." ("angry", "narrow", "base", "down")
    her "So I decided to rub it all over the inside of my socks to keep it from staining the outside of my clothes."
    her @ cheeks blush "But even then... That didn't hide the smell of cum, emerging from between my legs." ("angry", "closed", "worried", "up")
    gen "That's quite an exciting story, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Mmm*... Yes... Very exciting..." ("base", "closed", "worried", "mid")
    gen "........" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Mmm* I can still picture those two huge cocks......." ("grin", "closed", "worried", "up")
    gen "*Ehm*....." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh god, I'm sorry [name_genie_hermione]... I'm not sure what came over me." ("angry", "wide", "base", "stare")
    gen "Two huge cocks apparently..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("angry", "narrow", "base", "down")

    jump end_hg_pr_handjob
