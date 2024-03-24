
### Make Out With A Girl ###

label start_hg_pr_kiss:

    # Setup
    $ current_payout = 45

    if not _events_completed_any:
        gen "{size=-4}(Tell her to go make out with one of her female classmates?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu
    return

label hg_pr_kiss:

    call start_hg_pr_kiss

    her "" (xpos="mid", ypos="base", trans=fade)

    #Intro.
    if not _events_completed_any:
        gen "Have you ever kissed another girl, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        
        if states.her.public_level < 9:
            $_event.cancel()
            jump too_much_public

        her "?!" ("normal", "squint", "angry", "mid")
        her "I am not a... lesbian, [name_genie_hermione]." ("open", "base", "base", "mid")
        gen "Silly girl... You don't need to be a lesbian to kiss girls." ("base", xpos="far_left", ypos="head")
        gen "I mean, I've done it, and that doesn't make me a lesbian." ("base", xpos="far_left", ypos="head")
        her "..............." ("angry", "base", "angry", "mid")
        her "[name_genie_hermione]--"
        gen "No, \"[name_genie_hermione]s\"! This is your task for today!" ("base", xpos="far_left", ypos="head")
        gen "Go find a cute little thing and plant a \"smooch\" on her!" ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione], but I am--" ("open", "base", "worried", "mid")
        gen "Dismissed, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]!......" ("normal", "squint", "angry", "mid")
        gen "I said you're dismissed." ("base", xpos="far_left", ypos="head")
        her "*Hmph*!..." ("annoyed", "squint", "angry", "mid")
    else:
        if states.her.tier >= 5:
            gen "[name_hermione_genie], {number=current_payout} house points are up for grabs today!" ("base", xpos="far_left", ypos="head")
            gen "Are you interested?" ("base", xpos="far_left", ypos="head")
            her "Sure, why not?" ("base", "base", "base", "mid")
            gen "Great." ("base", xpos="far_left", ypos="head")
            gen "I want you to make out with another girl today." ("base", xpos="far_left", ypos="head")
            her "Alright." ("soft", "base", "base", "R")
            her "I know a couple of girls who are starved for attention that wouldn't mind a little kiss." ("open", "closed", "base", "mid_soft")
            gen "Great... See you after your classes then." ("base", xpos="far_left", ypos="head")
        elif states.her.tier >= 4:
            gen "[name_hermione_genie], {number=current_payout} house points are up for grabs today!" ("base", xpos="far_left", ypos="head")
            gen "Are you interested?" ("base", xpos="far_left", ypos="head")
            her "I suppose..." ("annoyed", "narrow", "annoyed", "up")
            gen "Great. All you need to do is make out with a girl." ("base", xpos="far_left", ypos="head")
            her "I see..." ("annoyed", "narrow", "worried", "down")
            gen "Up for the task, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "I guess..." ("annoyed", "base", "worried", "R")
            gen "Great. See you after your classes then." ("base", xpos="far_left", ypos="head")
        else:
            gen "[name_hermione_genie], {number=current_payout} house points are up for grabs today!" ("base", xpos="far_left", ypos="head")
            gen "Are you interested?" ("base", xpos="far_left", ypos="head")
            her "It depends..." ("normal", "base", "base", "mid")
            her "Will I have to do something depraved again?" ("normal", "base", "base", "mid")
            gen "\"Depraved\"??! When did I ever--?" ("base", xpos="far_left", ypos="head")
            her "Really, [name_genie_hermione]?" ("open", "closed", "angry", "mid")
            gen "Fine, fine... But all I want you to do today is to make out with a girl." ("base", xpos="far_left", ypos="head")
            her "Oh, is that all..." ("angry", "base", "angry", "mid") # sarcastic
            gen "Yes... Pretty basic stuff for you, right?" ("base", xpos="far_left", ypos="head")
            gen "And you will be getting {number=current_payout} house points afterwards, of course." ("base", xpos="far_left", ypos="head")
            her "............." ("normal", "squint", "angry", "mid")
            gen "So...{w=0.4} Are you up for it?" ("base", xpos="far_left", ypos="head")
            her "I'll see what I can do, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
            gen "Great. See you after your classes then." ("base", xpos="far_left", ypos="head")
            her "................" ("annoyed", "narrow", "annoyed", "mid")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_kiss_fail:
    call start_hg_pr_kiss

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Today, I require you to get out there and kiss another girl." ("base", xpos="far_left", ypos="head")

    jump too_much_public

label end_hg_pr_kiss:
    $ gryffindor += current_payout

    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if states.her.tier <= 3 and not _events_completed_any:

        her "(*Tsk*)" ("mad", "base", "angry", "R", ypos="base", xpos="base", flip=True, trans=d3)

    call her_chibi("leave")

    label .quick_end:

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    jump end_hermione_event

label hg_pr_kiss_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("open", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you succeed in completing your task?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*..."

    if _events_filtered_completed_all:
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_kiss

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("soft", "squint", "base", "R")
        her "Well... I..." ("soft", "base", "base", "R")
        gen "Don't be shy, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Did you, or did you not, kiss someone?" ("base", xpos="far_left", ypos="head")
    else:
        her "Yes, [name_genie_hermione]."
        gen "So, you kissed someone?" ("base", xpos="far_left", ypos="head")

    return

### Tier 3 ###

label hg_pr_kiss_T3_E1:

    call hg_pr_kiss_intro

    her "I..." ("open", "base", "worried", "mid")
    gen "I told you to make out with another girl..." ("base", xpos="far_left", ypos="head")
    gen "Did you do it or not?" ("base", xpos="far_left", ypos="head")
    her "I..." ("open", "base", "worried", "R")
    her "I tried, [name_genie_hermione]. I really did."
    gen "And?" ("base", xpos="far_left", ypos="head")
    her "Well..." ("annoyed", "base", "worried", "R")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "It was awkward and embarrassing..."
    gen "Did you do it or not?" ("base", xpos="far_left", ypos="head")
    her "... No, I did not, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    her "All I achieved was making a complete fool out of myself..."
    her "In front of the entire class..." ("angry", "base", "angry", "mid")
    gen "Tell me what happened, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "No, I will not, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    her "Not in a million years!"
    her "Why do I have to perform such ridiculous tasks anyway?!" ("shock", "happyCl", "worried", "mid")
    her "What is the point of all this?"
    her "I hate this!" ("scream", "closed", "angry", "mid")
    her "..............." ("annoyed", "narrow", "angry", "R")
    her "................."
    gen ".............." ("base", xpos="far_left", ypos="head")
    gen "You are not getting paid, you know that, right?" ("base", xpos="far_left", ypos="head")
    her "I don't care..." ("scream", "closed", "angry", "mid")

    $ states.her.mood += 5

    jump end_hg_pr_kiss.no_points

label hg_pr_kiss_T3_E2:

    call hg_pr_kiss_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I did, [name_genie_hermione]..." ("open", "closed", "base", "mid")
    gen "Good. Give me the details." ("base", xpos="far_left", ypos="head")
    her "Well, I kissed a girl. Just like you told me to, [name_genie_hermione]." ("annoyed", "squint", "base", "mid")
    gen "Seeing how it went last time, I presume it was embarrassing for you, girl?" ("base", xpos="far_left", ypos="head")
    her "Very much so, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    gen "Did you enjoy it at least?" ("base", xpos="far_left", ypos="head")
    her "*Hmph*!..." ("annoyed", "narrow", "annoyed", "mid")
    gen "So, you kissed a girl and you liked it?" ("base", xpos="far_left", ypos="head")
    her "Yes..." ("disgust", "narrow", "base", "mid_soft")
    gen "Did your tongues touch?" ("base", xpos="far_left", ypos="head")
    her "Yes..." ("disgust", "narrow", "base", "mid_soft")
    her "It was a proper kiss, if that's what you're asking..."
    her "Can I get my payment now?"
    her "Please, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    gen "Well, alright..." ("base", xpos="far_left", ypos="head")

    $ states.her.status.public_kissing = True

    jump end_hg_pr_kiss

label hg_pr_kiss_T3_E3:

    call hg_pr_kiss_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Yes, I did, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "Good. Tell me how it went." ("base", xpos="far_left", ypos="head")
    her "It went well, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "Great. Give me the details." ("base", xpos="far_left", ypos="head")
    her "What would you like to know, [name_genie_hermione]?" ("open", "closed", "angry", "mid")
    gen "Tell me everything! Was the girl pretty?" ("base", xpos="far_left", ypos="head")
    gen "Did she return your kiss?" ("base", xpos="far_left", ypos="head")
    her "She was relatively pretty, [name_genie_hermione]." ("open", "squint", "base", "mid")
    her "And she did return my kiss..."
    her "..........." ("annoyed", "closed", "base", "mid")
    her "Anything else, [name_genie_hermione]?" ("open", "squint", "base", "mid")
    gen "...." ("base", xpos="far_left", ypos="head")
    gen "Why are you being difficult, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "With all due respect, [name_genie_hermione]..." ("open", "closed", "angry", "mid")
    her "You told me to make out with another girl, and I did..."
    her "Now, I would like to get paid, if you would be so kind." ("normal", "base", "base", "mid")
    gen "......................" ("base", xpos="far_left", ypos="head")

    menu:
        "\"Fine. Here is your payment, girl.\"":
            pass

        "\"I don't appreciate your attitude, [name_hermione_genie].\"":
            her "Well, that is unfortunate, [name_genie_hermione]." ("open", "closed", "angry", "mid")
            gen "Sure is..." ("base", xpos="far_left", ypos="head")
            gen "Because you are not getting paid, you insolent little witch." ("base", xpos="far_left", ypos="head")

            stop music fadeout 1.0

            her "What?" ("normal", "base", "base", "mid")
            her "[name_genie_hermione], you can't do that!" ("open", "base", "worried", "mid")
            gen "Dismissed." ("base", xpos="far_left", ypos="head")
            her "B-but--" ("open", "base", "worried", "R")
            her "[name_genie_hermione], please!" ("open", "base", "worried", "mid")
            her "The girl was from Hufflepuff, and--"
            gen "It's far too late for that, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            gen "You are dismissed." ("base", xpos="far_left", ypos="head")
            her @ tears soft "......" ("angry", "base", "base", "mid")
            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            pause 1.0
            gen "*Tsk*" ("base", xpos="far_left", ypos="head")

            $ states.her.mood +=25
            jump end_hg_pr_kiss.quick_end

    jump end_hg_pr_kiss

### Tier 4 ###

label hg_pr_kiss_T4_E1:

    call hg_pr_kiss_intro

    her "I did, [name_genie_hermione]..." ("open", "closed", "base", "mid")
    gen "Well, don't just stand there. Give me the details." ("base", xpos="far_left", ypos="head")
    her "*Ehm*, alright..." ("open", "base", "base", "mid")
    her "The girl was from Ravenclaw..." ("open", "base", "base", "mid")
    her "I think she may have been an underclassman, but I did not ask..." ("soft", "base", "base", "R")
    her "We were grouped together for divination class, and once class finished, we kept talking, while making our way down the winding staircases."("soft", "base", "base", "R")
    her "Eventually we got to the subject of boys..." ("open", "base", "base", "R")
    gen "As you do." ("base", xpos="far_left", ypos="head")
    her "She told me that she had never kissed one..." ("open", "closed", "base", "mid")
    her "And that she was worried that she might be very bad at it..."
    her "So, I offered her my help..." ("soft", "base", "base", "mid")
    her "You had tasked me to kiss a girl after all, so I figured, if I can help this girl at the same time, then why--" ("open", "closed", "base", "mid")
    gen "Yes, yes... Very noble of you." ("base", xpos="far_left", ypos="head")
    gen "So, you taught this girl how to press her lips against yours?" ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Yes... We took a detour before lunch, and went into a stall in one of the girls' bathrooms, so I could teach her in private..."
    her "To my surprise, she caught on pretty quick..." ("open", "base", "base", "mid")
    her "And after some time, this overly affectionate attitude started emerging from her..." ("soft", "base", "base", "mid")
    her "She kept calling me \"Miss Hermione\" in a higher pitched, and adorably sounding voice..." ("open", "base", "base", "R")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "I don't recall sending you out with a task to confuse some poor girl, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "\"Confuse\"? [name_genie_hermione]--" ("angry", "narrow", "base", "mid_soft")
    her "I assure you that she was anything but confused..." ("disgust", "base", "angry", "mid")
    her "In fact, at the end of our \"Study session\", she started getting rather handsy..."
    her "That's when I realised, she had probably been taking advantage of me the entire time..." ("annoyed", "narrow", "base", "mid")
    gen "Oh... Well, in that case..." ("base", xpos="far_left", ypos="head")
    her "" ("soft", "base", "base", "R")

    $ states.her.status.public_kissing = True

    jump end_hg_pr_kiss

label hg_pr_kiss_T4_E2:

    call hg_pr_kiss_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I did, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "Tell me how it went." ("base", xpos="far_left", ypos="head")
    her "Well... *Ehm*..." ("open", "base", "base", "mid")
    her "There's this one girl who I had heard is into girls..." ("soft", "base", "base", "R")
    her "I figured, if I'm going to kiss a girl, then why not go for the ideal candidate..." ("soft", "base", "base", "R")
    her "So, when I spotted her, sitting on one of the benches in the courtyard, I went up and told her that I've been curious and wanted to know how she first figured it out..." ("open", "base", "base", "mid")
    her "She was taken a bit by surprise, so I went ahead and asked if we could go to some secluded spot to see if she could help \"spark my interest\"..." ("soft", "base", "base", "R")
    gen "Very direct [name_hermione_genie], I'm impressed..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you [name_genie_hermione]... Although unfortunately, that's when things went a bit outside of my control." ("angry", "base", "base", "mid")
    her @ cheeks blush "Rather than doing what I requested, she immediately jumped to her feet, and kissed me right there and then..." ("open", "base", "base", "mid")
    gen "Nice... Love a girl who's got her life figured out." ("base", xpos="far_left", ypos="head")
    gen "You kissed her back, I hope?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course I did!" ("annoyed", "closed", "base", "mid")
    her @ cheeks blush "I requested her help, after all, so it would've been weird if I hadn't!" ("angry", "base", "base", "mid")
    her "Although... Speaking of weird..." ("open", "base", "base", "mid")
    her "Things got weird really fast..." ("angry", "narrow", "base", "down")
    her "The way she kissed me..." ("angry", "narrow", "base", "down")
    her "She did it like a boy would, [name_genie_hermione]..." ("angry", "base", "base", "mid")
    her "Aggressively, yet filled with confidence..." ("angry", "narrow", "base", "down")
    her "And before I knew it, a small group of spectators had gathered around us..." ("upset", "closed", "base", "mid")
    her @ cheeks blush "Mostly boys, of course..." ("open", "narrow", "base", "down")
    her @ cheeks blush "Some of them even cheered us on..." ("open", "happyCl", "worried", "mid")
    her @ cheeks blush "....." ("base", "happyCl", "base", "mid")
    her @ cheeks blush "Anyway... The girl I kissed..." ("angry", "narrow", "base", "R")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "She's known as one of the unpopular girls..." ("open", "base", "base", "mid")
    her @ cheeks blush "In fact, I've heard some of the other students making fun of her before..." ("upset", "base", "base", "mid")
    her "But today changed that for her..." ("base", "squint", "base", "mid")
    her "I single-handedly turned that girl from a social outcast..."
    her "Into \"that bold lesbian girl who snagged a kiss from Hermione Granger\"!" ("grin", "closed", "base", "mid")
    gen "She went from unpopular to popular, just from kissing you?" ("base", xpos="far_left", ypos="head")
    her "That's right!" ("base", "narrow", "base", "mid_soft")
    her "I changed that poor girl's life..."
    gen "How heroic..." ("base", xpos="far_left", ypos="head")
    her "I suppose it is, [name_genie_hermione]..." ("grin", "closed", "base", "mid_soft")
    gen "You make it sound almost too good to be true." ("base", xpos="far_left", ypos="head")
    her "It is true!" ("angry", "base", "base", "mid_soft")
    gen "*Hmm*... I don't know [name_hermione_genie], I think you may have to bring me this girl and prove it for me." ("base", xpos="far_left", ypos="head")
    her "Don't get it twisted, I'm not a lesbian, [name_genie_hermione]... I already told you this." ("base", "narrow", "base", "mid_soft")
    gen "Of course [name_hermione_genie]... That much is already obvious..." ("base", xpos="far_left", ypos="head")
    her "Good, I'm glad you're finally listening--" ("grin", "closed", "base", "mid_soft")
    gen "It's of course fine for you to like any gender..." ("base", xpos="far_left", ypos="head")
    her "..." ("disgust", "narrow", "base", "mid")

    jump end_hg_pr_kiss

label hg_pr_kiss_T4_E3:

    call hg_pr_kiss_intro

    her "I did."
    her ".........." ("annoyed", "base", "base", "R")
    her "[name_genie_hermione]?" ("open", "closed", "base", "mid")
    gen "Yes, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "May I ask you a question?" ("open", "base", "base", "mid")
    gen "By all means." ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("annoyed", "narrow", "angry", "R")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "How come boys are so fascinated by girls kissing other girls?" ("disgust", "narrow", "base", "mid_soft")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Who knows? Boys are weird.\"":
            her "Yes, they are, aren't they...?" ("angry", "narrow", "base", "down")
            gen "Yes, yes..." ("base", xpos="far_left", ypos="head")
            gen "And that is why young girls such as yourself..." ("base", xpos="far_left", ypos="head")
            gen "Are often more interested in older gentlemen..." ("base", xpos="far_left", ypos="head")
            her "??!" ("angry", "base", "base", "mid")
            her "That is not what I meant, [name_genie_hermione]..." ("annoyed", "narrow", "annoyed", "mid")
        "\"You wouldn't understand, girl.\"":
            her "*Hmm*..." ("upset", "closed", "base", "mid")
            her "What about you, [name_genie_hermione]?" ("angry", "base", "base", "mid")
            her "Were you like that when you were younger?"
            gen "Are you asking if I enjoyed watching two girls going at it?" ("base", xpos="far_left", ypos="head")
            gen "Well, of course." ("base", xpos="far_left", ypos="head")
            gen "I still do..." ("base", xpos="far_left", ypos="head")
            her "Oh..." ("upset", "closed", "base", "mid")
        "\"Can't have too much of a good thing.\"":
            her "What do you mean by that, [name_genie_hermione]?" ("angry", "narrow", "base", "mid")
            gen "If you take one thing that you like, and then add another one, then put them together..." ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("annoyed", "narrow", "annoyed", "mid")
            gen "Think of it like this, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Watching a guy and a girl kissing is kinda gay, since there's a guy involved..." ("base", xpos="far_left", ypos="head")
            her "..." ("upset", "narrow", "worried", "mid")
            gen "But if you're watching two girls doing it, then it's--" ("base", xpos="far_left", ypos="head")
            her "That doesn't make any sense..." ("angry", "narrow", "worried", "mid")
            gen "Of course it does!" ("base", xpos="far_left", ypos="head")
            gen "Let me explain the maths..." ("base", xpos="far_left", ypos="head")
            gen "A guy and a girl kissing is fifty percent gay because there's a guy involved..." ("base", xpos="far_left", ypos="head")
            gen "So if there's two girls, and no guy, that makes it zero percent gay!" ("grin", xpos="far_left", ypos="head")
            gen "(Although...{w=0.4} That does make it lesbian...{w=0.4} Which is a hundred percent gay.)" ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]?" ("upset", "narrow", "worried", "mid")
            gen "*Hmm*...{w=0.4} Perhaps there isn't a straight answer to your question after all, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        "\"Where are you kissing exactly?!!\"":
            her "*Tsk*!......................" ("angry", "base", "angry", "mid", emote="angry")

    her "Well, I am only asking you this, [name_genie_hermione], because..." ("open", "narrow", "worried", "down")
    her "... It's sort of becoming a new trend at our school..." ("angry", "base", "base", "mid")
    her "Some of the girls are willing to do this, simply to catch the attention of some boy..."
    gen "Aren't you one of those girls, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "What do you mean by that, [name_genie_hermione]?" ("angry", "narrow", "base", "down")
    gen "You've got my undivided attention, any time you're telling me about kissing other girls... And speaking of..." ("base", xpos="far_left", ypos="head")
    her "I think you've got it a bit backwards, [name_genie_hermione]..." ("upset", "closed", "base", "mid")
    gen "Attention span... Slowly fading..." ("base", xpos="far_left", ypos="head")
    her "Right..." ("open", "narrow", "base", "mid")
    her "I suppose I'll tell you about the kissing booth I set up today." ("open", "narrow", "base", "mid")
    gen "A kissing booth? Now we're talking." ("grin", xpos="far_left", ypos="head")
    her "Well, as you know, I am quite popular..." ("base", "closed", "base", "mid")
    her "And I thought... Why should I approach a bunch of girls, if I could have them come to me..." ("base", "happyCl", "base", "mid")
    her "So, I set up a kissing both, and to nobody's surprise, I had half a dozen girls lining up instantly..." ("base", "base", "base", "mid")
    gen "Impressive..." ("base", xpos="far_left", ypos="head")
    gen "I presume you went through the line efficiently, yet still provided a service at the standard expected from a Gryffindor student?" ("base", xpos="far_left", ypos="head")
    her "That certainly was my intention, although that's not exactly what happened..." ("soft", "narrow", "base", "R")
    gen "Right?" ("base", xpos="far_left", ypos="head")
    gen "Don't tell me you forgot to use tongue?" ("base", xpos="far_left", ypos="head")
    her "Of course I did, [name_genie_hermione]... I used tongue and everything." ("annoyed", "base", "worried", "R")
    her "The problem is, I set up the booth with the intention of kissing as many girls as I could, in a single day--" ("annoyed", "base", "worried", "R")
    gen "Someone's started to get greedy..." ("base", xpos="far_left", ypos="head")
    her "--In the hopes that by doing so, I could earn myself some extra points..." ("annoyed", "base", "base", "mid")
    gen "That's what I meant to say." ("base", xpos="far_left", ypos="head")
    her "Anyway..." ("open", "narrow", "base", "R")
    her "It didn't exactly go to plan... In fact, I only had enough time to kiss a single girl, during that whole free period." ("open", "base", "base", "mid")
    gen "A single girl?" ("base", xpos="far_left", ypos="head")
    her "Yes [name_genie_hermione]... {b}One{/b} girl..." ("annoyed", "base", "worried", "R")
    her "We started with some light pecking on the lips, but then I made the mistake of giving her a little bit of tongue..." ("annoyed", "base", "worried", "R")
    her @ cheeks blush "She took that as an invitation to get serious, and promptly wrapped her tongue around mine." ("open", "base", "worried", "mid")
    her "The other girls in line didn't seem to like this, and their outcries brought the attention of a group of Slytherin boys." ("open", "base", "worried", "mid")
    her "Once the boys realised what was going on, they rushed up to watch... Pushing the girls who had been waiting their turn to the side." ("annoyed", "base", "worried", "mid")
    her "Of course, normally, I would've interjected, and given them a piece of my mind..." ("angry", "closed", "worried", "mid")
    her "But the girl who I was kissing, instead of breaking the kiss, basked in the attention and pulled me even closer towards her." ("angry", "base", "worried", "mid")
    her "And she kept going at it, right up until our classes were resuming." ("annoyed", "base", "base", "mid")
    her "So, due to her not letting go, and the Slytherin boys pushing away the other girls, I didn't manage to get more than one kiss today."
    gen "Sounds to me like your kissing booth idea was far too affective." ("base", xpos="far_left", ypos="head")
    her "Affective, [name_genie_hermione]? Don't you mean--{w=0.2} Oh...{w=0.4} Yes, perhaps you're right..." ("angry", "narrow", "base", "mid")
    gen "Either way... You've still done what I've asked of you today." ("base", xpos="far_left", ypos="head")
    gen "Nicely done [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "" ("base", "narrow", "base", "down")

    jump end_hg_pr_kiss

### Tier 5 ###

label hg_pr_kiss_T5_E1:

    call hg_pr_kiss_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I did, [name_genie_hermione]." ("soft", "base", "base", "mid")
    gen "I'm all ears..." ("base", xpos="far_left", ypos="head")
    her "Well, I kissed that annoying blond girl from Slytherin..." ("annoyed", "squint", "base", "mid")
    gen "*Hmm*... \"annoying\", *Huh*?" ("base", xpos="far_left", ypos="head")
    gen "Because she happens to be from Slytherin." ("base", xpos="far_left", ypos="head")
    her "Precisely so, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Don't you think you're being a little prejudiced there?" ("base", xpos="far_left", ypos="head")
    gen "Or shall I say that you are being a \"housist\"?" ("base", xpos="far_left", ypos="head")
    her "... A \"housist\", [name_genie_hermione]?" ("annoyed", "narrow", "annoyed", "mid")
    gen "Well, you know... It's like \"sexist\" or \"ageist\"..." ("base", xpos="far_left", ypos="head")
    gen "You just put an \"ist\" after something, and it automatically becomes a bad thing..." ("base", xpos="far_left", ypos="head")
    her "\"housist\" is not an actual word, [name_genie_hermione]..." ("soft", "base", "base", "R")
    gen "It's not? Well, give it time..." ("base", xpos="far_left", ypos="head")
    her ".............?" ("annoyed", "narrow", "annoyed", "mid")
    gen "\"Housophobic\"...?" ("base", xpos="far_left", ypos="head")
    gen "No, wait, I got it!" ("base", xpos="far_left", ypos="head")
    gen "\"Housophobe\"!" ("base", xpos="far_left", ypos="head")
    her "Stop it, [name_genie_hermione]. I am not any of those weird words..." ("normal", "squint", "angry", "mid")
    her "Slytherins are evil and annoying. Nobody likes them, and that is a fact!" ("normal", "squint", "angry", "mid")
    gen "Fine, whatever... Back to the \"girl-kissing\", then." ("base", xpos="far_left", ypos="head")
    her "..............." ("annoyed", "base", "worried", "R")
    her "As I was saying..." ("open", "closed", "worried", "R")
    her "I kissed that... girl... from Slytherin." ("open", "narrow", "worried", "R")
    her "Normally I would never do it, of course..." ("annoyed", "narrow", "angry", "R")
    her "Not with someone from that wretched house..." ("annoyed", "narrow", "angry", "R")
    her "But she approached me first, and practically begged me for a kiss..." ("annoyed", "narrow", "annoyed", "mid")
    gen "She... begged you?" ("base", xpos="far_left", ypos="head")
    her "She did... And to be perfectly honest..." ("annoyed", "narrow", "angry", "R")
    her "The way she begged me... It did make me feel quite good about myself..." ("annoyed", "narrow", "annoyed", "mid")
    her "That doesn't change what I think about Slytherin, though..." ("upset", "closed", "base", "mid")
    gen "Why would she beg you for a kiss, exactly?" ("base", xpos="far_left", ypos="head")
    her "I did not ask her why... But she was begging so desperately, even I started feeling bad for her..." ("open", "closed", "base", "mid")
    her "Thinking back on it, she was probably just trying to boost her own popularity at my expense..." ("open", "closed", "base", "mid")
    her "Even so, I figured since I was tasked with this today..." ("open", "closed", "base", "mid")
    her "Hold on..." ("open", "base", "base", "stare")
    her "Do you think that someone from the school staff may have bought this favour from her?" ("angry", "base", "base", "mid")
    her @ cheeks blush "The same time you bought the favour from me, [name_genie_hermione]..." ("angry", "squint", "worried", "mid")
    gen "(Did Snape somehow--)" ("base", xpos="far_left", ypos="head")
    her "If that is the case, I am certain that it was professor Snape!" ("angry", "closed", "angry", "mid")
    gen "Whaaat... He would never..." ("base", xpos="far_left", ypos="head")
    her "Then, who else--" ("annoyed", "narrow", "annoyed", "mid_soft")
    gen "Enough about that... Just tell me what happened next, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Fine..." ("annoyed", "narrow", "base", "down")
    her "Well, we made out for a while..." ("open", "closed", "worried", "down")
    her @ cheeks blush "She was very... passionate." ("angry", "narrow", "base", "down")
    her @ cheeks blush "For a Slytherin, that is!" ("annoyed", "closed", "annoyed", "down")
    gen "..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Anyway... She decided it was a good idea to for us to \"snowball\"..." ("angry", "narrow", "base", "R")
    gen "I'm sorry... She decided, what?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "To \"snowball\", [name_genie_hermione]." ("angry", "narrow", "base", "mid")
    her @ cheeks blush "It's when you kiss and move a ball of spit, between each other's mouths..." ("soft", "narrow", "base", "mid_soft")
    her @ cheeks blush "Undoubtedly, Snape had made this requirement for her..." ("annoyed", "closed", "angry", "mid_soft")
    gen "(Sounds like a classic Snape request, alright...)" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "So... She spat into my mouth..." ("open", "closed", "base", "mid")
    her @ cheeks blush "And then by reflex, I spat it back into hers..." ("angry", "narrow", "worried", "down")
    her @ cheeks blush "Of course, if I had been ready for it, I would have spat it back in her face!" ("angry", "base", "angry", "mid")
    her @ cheeks blush "Then she broke off the kiss, and smirked at me... And I really had to fight the urge to slap her smug face..." ("angry", "narrow", "angry", "R")
    her @ cheeks blush "But I figured you wouldn't have appreciated that..." ("upset", "closed", "base", "mid")
    gen "(Sounds kind of hot, to be honest...)" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "After that, she just left me standing there..." ("annoyed", "narrow", "angry", "down")
    gen "You didn't even try to chase after her?" ("base", xpos="far_left", ypos="head")
    her "I didn't have the chance, as she left just as class was about to start..." ("angry", "narrow", "angry", "R")
    gen "That's unlucky..." ("base", xpos="far_left", ypos="head")
    her "(She must've sensed that a punch was about to come her way...)" ("annoyed", "narrow", "annoyed", "R")
    gen "*Sigh*... The things girls experience during their schooldays..." ("base", xpos="far_left", ypos="head")
    gen "Assignments... Classes..." ("base", xpos="far_left", ypos="head")
    gen "\"Snowballing\" with other girls..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "[name_genie_hermione], I--" ("angry", "narrow", "worried", "mid")
    gen "Well done, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "...{w=0.4} Thanks." ("annoyed", "base", "base", "R")

    $ states.her.status.public_kissing = True

    jump end_hg_pr_kiss

label hg_pr_kiss_T5_E2:

    call hg_pr_kiss_intro

    her "I did, [name_genie_hermione]." ("open", "closed", "base", "mid")
    her @ cheeks blush "*Ehm*... [name_genie_hermione]..." ("soft", "base", "base", "R")
    gen "Yes, What is it, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well... There's this girl..." ("soft", "narrow", "base", "down")
    her @ cheeks blush "And... *Ehm*..." ("angry", "base", "base", "R")
    her @ cheeks blush "I'm not sure how to say this..." ("open", "closed", "base", "mid")
    gen "Just say it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, we decided to skip potions class..." ("open", "narrow", "base", "down")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "And study for the upcoming Herbology test instead..." ("open", "closed", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "While this girl and I were studying..." ("open", "base", "base", "R")
    her @ cheeks blush "We started talking about boys..." ("soft", "narrow", "base", "mid")
    gen "Naturally..." ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her @ cheeks blush "And then I sort of kissed her..." ("angry", "base", "base", "mid")
    her @ cheeks blush "And she returned my kiss with such passion..." ("angry", "narrow", "base", "down")
    her @ cheeks blush "That we sort of ended up doing more than just kissing..." ("angry", "narrow", "base", "mid_soft")
    gen "You had a pillow fight, wearing only lingerie?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "*Err*... No..." ("open", "happy", "base", "mid")
    gen "What did you do then?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I am not telling you, [name_genie_hermione]." ("annoyed", "narrow", "base", "R") # :)
    her @ cheeks blush "You sent me out to kiss a girl..." ("open", "closed", "worried", "R")
    her @ cheeks blush "And I did just that." ("base", "closed", "base", "R")
    her @ cheeks blush "The rest shall remain private." ("base", "narrow", "base", "mid")
    gen "Now you are just being cruel, you little witch." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "My points please." ("smile", "narrow", "base", "mid_soft")
    gen "Fine..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_kiss
