
### Flirt With Classmate ###

label hg_pr_flirt:

    # Setup
    $ current_payout = 5

    if not _events_completed_any:
        gen "{size=-4}(Ask her to go flirt with some boys from Slytherin?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    her "" (xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes?" ("soft", "base", "base", "mid")

    #Intro.
    if not _events_completed_any:
        gen "What is your opinion on the boys of the Slytherin house?" ("base", xpos="far_left", ypos="head")
        her "I detest them, [name_genie_hermione]." ("angry", "base", "angry", "mid")
        gen "Well, too bad. Because I want you to get really friendly with a few of them today." ("base", xpos="far_left", ypos="head")
        her "If I must..." ("soft", "base", "base", "R")
        her "Yes, I think I can manage to be civil with them for one day."
        gen "Yes, and when I say \"get friendly with them\"..." ("base", xpos="far_left", ypos="head")
        gen "I actually mean that I need you to flirt with them..." ("base", xpos="far_left", ypos="head")
        her "Flirt?!" ("shock", "wide", "base", "stare")
        her "[name_genie_hermione]!" ("angry", "base", "angry", "mid")
        her "I'm not even going to ask why you'd be interested in this, [name_genie_hermione]..." ("annoyed", "squint", "base", "mid")
        her "But why Slytherin?" ("open", "base", "worried", "mid")
        her "If you need me to be flirtatious today, I think I can manage that..."
        her "But, please, can't it be another house?"
        her "Gryffindor maybe?" ("upset", "wink", "base", "mid")
        gen "I am only trying to protect your reputation, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]?" ("soft", "base", "base", "mid")
        gen "Do you value the opinion the Slytherin students have of you?" ("base", xpos="far_left", ypos="head")
        her "I couldn't care less about the opinions of those Neanderthals." ("scream", "closed", "angry", "mid")
        gen "What about the students of the Gryffindor house?" ("base", xpos="far_left", ypos="head")
        her "Their opinion means the world to me--" ("annoyed", "base", "worried", "R")
        her "Oh, I see..." ("base", "base", "base", "mid")
        gen "Exactly... Just looking out for you [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "*Ehm*... Thank you [name_genie_hermione]..."
    else:
        if states.her.tier >= 3:
            gen "I need you to flirt with some boys from Slytherin today." ("base", xpos="far_left", ypos="head")
            her "Right... I'll see what I can do, [name_genie_hermione]." ("open", "base", "base", "R")
            gen "Great. I'll be expecting a report once your classes are done for the day." ("base", xpos="far_left", ypos="head")
            her "Okay then..." ("soft", "base", "base", "R")
        elif states.her.tier >= 2:
            gen "I need you to go make some new friends at the Slytherin house." ("base", xpos="far_left", ypos="head")
            her "You mean you need me to flirt with the Slytherin boys again [name_genie_hermione]?"
            her "Fine." ("upset", "base", "angry", "R")
            her "If I have to, [name_genie_hermione]..." ("normal", "squint", "angry", "mid")
        else:
            if _events_filtered_completed_any:
                gen "I need you to go make some new friends at the Slytherin house." ("base", xpos="far_left", ypos="head")
                her "You mean you need me to flirt with the Slytherin boys again, [name_genie_hermione]?"
                gen "That's exactly what I need you to do today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                gen "Just do it properly this time." ("base", xpos="far_left", ypos="head")
                her "Must I really do this [name_genie_hermione]?" ("open", "base", "base", "mid")
                gen "We have been through this, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                gen "Going to the Slytherin boys is in your best interest." ("base", xpos="far_left", ypos="head")
                her "Yes, I know, [name_genie_hermione]." ("open", "closed", "angry", "mid")
                her "But why must I do this at all?"
                gen "Nobody is forcing you, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her "You don't need to remind me of that, [name_genie_hermione]..." ("angry", "base", "angry", "mid")
                her "Alright, if I must... [name_genie_hermione]..." ("normal", "squint", "angry", "mid")
            else:
                gen "I need you to go make some new friends at the Slytherin house." ("base", xpos="far_left", ypos="head")
                her "You mean you need me to flirt with the Slytherin boys again, [name_genie_hermione]?"
                her "Must I really do this [name_genie_hermione]?" ("upset", "base", "worried", "mid")
                gen "This again?" ("base", xpos="far_left", ypos="head")
                her "Fine........." ("upset", "base", "angry", "R")
                her "If I must... [name_genie_hermione]..." ("normal", "squint", "angry", "mid")

    her "Well, I'd better go now. Classes are about to start..."
    call her_walk(action="leave")
    
    jump end_hermione_event

# End Event
label end_hg_pr_flirt:

    $ states.her.ev.flirt_with_students.done_before = True

    $ gryffindor += current_payout

    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if states.her.tier <= 1 and not _events_completed_any:

        her "(........)" ("disgust", "base", "worried", "down", ypos="base", xpos="base", flip=True, trans=d3)
        her "(I'll need to read about this whole \"flirting\" thing...)" ("annoyed", "base", "angry", "L")

    call her_chibi("leave")

    label .quick_end:

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    jump end_hermione_event

label hg_pr_flirt_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("open", "closed", "base", "mid", xpos="mid", ypos="base", trans=fade)
    her "" ("normal", "base", "base", "mid")
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you complete your task?" ("base", xpos="far_left", ypos="head")
    her "I did as you asked, [name_genie_hermione]..." ("open", "base", "base", "R")
    her "" ("normal", "base", "base", "R")

    if _events_filtered_completed_all:
        menu:
            "\"Great. You earned your points.\"":
                jump end_hg_pr_flirt

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("annoyed", "narrow", "angry", "R")
        her "So...{w=0.4} *Ehm*." ("soft", "base", "base", "R")

    gen "How many boys did you flirt with today, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")

    return

### Tier 1 - LVL 0-3 ###

label hg_pr_flirt_T1_E1:

    call hg_pr_flirt_intro

    her "Well..." ("open", "base", "worried", "R")
    her "There was this one freshman boy..."
    her "........."
    gen "I'm listening..." ("base", xpos="far_left", ypos="head")
    her "So... I went to him and I said \"Hey, handsome!\"."
    gen "And?" ("base", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "He stuck out his tongue and ran off, [name_genie_hermione]." ("normal", "squint", "angry", "mid")
    gen "Did you try to lure him in with a lollipop?" ("base", xpos="far_left", ypos="head")
    her "I did not, [name_genie_hermione]..." ("open", "base", "worried", "R")
    her "The thought never crossed my mind, but--"
    gen "That was a joke, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "............." ("annoyed", "squint", "angry", "mid")
    gen "I told you to flirt with boys {size=+5}your{/size} age!" ("base", xpos="far_left", ypos="head")
    her "I wanted to at first, but..." ("normal", "squint", "angry", "mid")
    her "I guess I got scared..." ("annoyed", "narrow", "angry", "R")
    her "I mean, I despise those Slytherins way too much to flirt with them, [name_genie_hermione]!"
    her "I would have to fight my gag-reflex the entire time!" ("angry", "base", "angry", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Fine. Just try harder next time.\"":
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            her "I will, I promise!"

        "\"Favour failed! No points for you!\"":
            stop music fadeout 1.0

            her "I understand..." ("normal", "squint", "angry", "mid")
            gen "Get out of my sight..." ("base", xpos="far_left", ypos="head")
            her "Yes, [name_genie_hermione]... Sorry, [name_genie_hermione]..." ("annoyed", "squint", "angry", "mid")

            jump end_hg_pr_flirt.no_points

    jump end_hg_pr_flirt

label hg_pr_flirt_T1_E2:

    call hg_pr_flirt_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Well, I tried to compliment an upperclassman..." ("open", "base", "worried", "R")
    gen "Did he appreciate it?" ("base", xpos="far_left", ypos="head")
    her "He called me a \"Gryffindor whore\", [name_genie_hermione]!" ("angry", "base", "angry", "mid", emote="angry")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "What did you do then?" ("base", xpos="far_left", ypos="head")
    her "Well, that was not the proper way to address a fellow \"Hogwarts\" student..." ("open", "closed", "angry", "mid")
    her "So I told him that I would report him."
    gen "A truly captivating story..." ("base", xpos="far_left", ypos="head")
    gen "Anything else?" ("base", xpos="far_left", ypos="head")
    her "Yes, there was also this one student at the library..." ("annoyed", "squint", "angry", "mid")
    her "He was obviously struggling with a problem..."
    her "So I offered my help..."
    gen "And?" ("base", xpos="far_left", ypos="head")
    her "He called me a \"Patronising Gryffindor Whore\", [name_genie_hermione]..." ("angry", "base", "angry", "mid", emote="angry")
    gen "Did you threaten to report him as well?" ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]." ("open", "closed", "angry", "mid")
    gen "*Sigh*" ("base", xpos="far_left", ypos="head")
    gen "Anything else?" ("base", xpos="far_left", ypos="head")
    her "Well, there was one more incident but the outcome was pretty much the same..." ("annoyed", "squint", "angry", "mid")
    gen "\"Gryffindor whore\"?" ("base", xpos="far_left", ypos="head")
    her "......... yes, [name_genie_hermione]." ("disgust", "narrow", "base", "mid_soft")
    gen "You are doing it all wrong, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I am sorry, [name_genie_hermione]. I thought this would be easy..." ("annoyed", "narrow", "angry", "R")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Well, at least you are trying.\"":
            her "I truly am..." ("angry", "happyCl", "worried", "mid")
            her "But Apparently flirting is not my forte..." ("angry", "base", "worried", "down", emote="sweat")
            her "" ("base", "base", "worried", "mid")

        "\"Favour failed! No points for you!\"":
            stop music fadeout 1.0
            her "You are not going to pay me, [name_genie_hermione]?" ("open", "base", "worried", "mid")
            her @ tears soft "But, you promised!" ("angry", "base", "base", "mid")
            gen "And you promised to flirt with the boys, not get bullied." ("base", xpos="far_left", ypos="head")
            her @ tears soft_blink "................" ("mad", "happyCl", "worried", "mid")
            call her_walk(action="run", xpos="door", speed=2, reduce=True)
            call her_chibi("leave")

            pause 1.0

            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Now I feel bad for saying that..." ("base", xpos="far_left", ypos="head")

            $ states.her.mood += 10
            jump end_hg_pr_flirt.quick_end

    jump end_hg_pr_flirt

label hg_pr_flirt_T1_E3:

    call hg_pr_flirt_intro

    her "Well, the Slytherin quidditch team was practising in the stadium today..." ("open", "base", "worried", "R")
    gen "(Quidish... Team?)" ("base", xpos="far_left", ypos="head")
    her "I thought I could sneak into the bleachers and cheer them on..."
    her "But..." ("annoyed", "narrow", "angry", "R")
    gen "Yes?" ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music

    her "A whole flock of those Slytherin harlots was already there, [name_genie_hermione]." ("angry", "base", "angry", "mid")
    her "They were cheering and yelling..."
    her "And one of them even exposed herself inappropriately to the players, [name_genie_hermione]..." ("angry", "base", "angry", "mid")
    her "I cannot believe our school accepts such behaviour..."
    gen "So... how did this captivating drama end?" ("base", xpos="far_left", ypos="head")
    her "I just left, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        "\"Well, here are your points.\"":
            gen "Maybe you didn't do exactly as was asked of you, you at least tried." ("base", xpos="far_left", ypos="head")
            her "" ("base", "closed", "base", "mid")

            jump end_hg_pr_flirt

        "\"Favour failed! No points for you!\"":
            stop music fadeout 1.0
            her "I don't feel like I deserved any this time anyway..." ("annoyed", "happyCl", "worried", "R")
            her "Can I leave now, [name_genie_hermione]?" ("annoyed", "base", "worried", "mid")
            gen "Dismissed!" ("base", xpos="far_left", ypos="head")
            call her_walk(action="leave")

            jump end_hermione_event

### Tier 2 - LVL 3-6 ###

label hg_pr_flirt_T2_E1:

    call hg_pr_flirt_intro

    her "Well, there was this one guy at the library..." ("open", "base", "worried", "R")
    her "He was obviously struggling with some assignment, so I offered my help..."
    gen "And?" ("base", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Well, to my surprise he accepted it..." ("smile", "happyCl", "base", "mid")
    her "He let me finish the assignment for him..."
    her "While I was working he made a couple of inappropriate comments, but I just smiled in response..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "So, basically, he was the one doing the flirting..." ("base", xpos="far_left", ypos="head")
    her "Well... I guess." ("grin", "happyCl", "worried", "mid", emote="sweat")
    her "But, despite my better judgment, I did encourage his improper behaviour..." ("base", "base", "base", "mid")
    gen "By being quiet?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..."
    her "I mean, this does amount to something, right?"
    gen "*Meh*..." ("base", xpos="far_left", ypos="head")
    gen "What else do you have for me?" ("base", xpos="far_left", ypos="head")
    her "Right..." ("annoyed", "narrow", "angry", "R")
    her "Later in a corridor, these two other guys complimented my appearance in a very vulgar manner..."
    her "But I just smiled at them..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "You were on the receiving end again, then..." ("base", xpos="far_left", ypos="head")
    gen "This is not what I ordered you to do, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I know, [name_genie_hermione]!" ("angry", "happyCl", "worried", "mid", emote="sweat")
    her "But I am so busy. Between the \"MRM\" meetings and the classes..." ("annoyed", "narrow", "angry", "R")
    her "I barely have any time--"
    gen "Is this all you got for me this time then?" ("base", xpos="far_left", ypos="head")
    her "No, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    her "On my way here I ran into Draco Malfoy, [name_genie_hermione]."
    gen "No way!!! (No idea who that is...)" ("base", xpos="far_left", ypos="head")
    her "I forced myself to be friendly with him, and..."
    her "We ended up having a decent conversation for a change." ("base", "happyCl", "base", "mid")
    gen "I see... That \"Dark-oh\" guy..." ("base", xpos="far_left", ypos="head")
    gen "Was he looking at your legs at all?" ("base", xpos="far_left", ypos="head")
    her "What?" ("open", "base", "base", "mid")
    gen "Did he stare at your legs or not, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... He might have..." ("upset", "wink", "base", "mid")
    gen "What about your tits?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]!!!" ("angry", "base", "angry", "mid")
    gen "Fine. You get your points. Keep up the good work." ("base", xpos="far_left", ypos="head")
    her "" ("annoyed", "base", "worried", "R")

    jump end_hg_pr_flirt


label hg_pr_flirt_T2_E2:

    call hg_pr_flirt_intro

    her "Well..." ("open", "base", "worried", "R")
    her "This morning I did flirt with this one guy..."
    her "Then after the second period, there was this other guy..." ("soft", "base", "base", "R")
    her "And then something bizarre happened..." ("angry", "base", "worried", "mid")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "This angry-looking guy from Slytherin came up to me and asked me out on a date..."
    her "I told him \"no\" at first, but we ended up taking a walk together." ("soft", "base", "base", "R")
    gen "Did you enjoy yourself, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "I think I did, [name_genie_hermione]... To my own astonishment..." ("open", "base", "base", "mid")
    her "There was something about his \"devil-may-care\" attitude..." ("base", "base", "base", "mid")
    her "He was so confident and calm, and..." ("base", "happyCl", "base", "mid")
    her "I still loathe the Slytherin house of course!" ("angry", "happyCl", "worried", "mid", emote="sweat")
    her "But..." ("annoyed", "narrow", "worried", "down")
    her "Maybe some of the students got there by mistake?"
    her "Could the \"sorting hat\" make... Miscalculations?" ("open", "base", "worried", "R")

    menu:
        "\"Just take your points and go!\"":
            her "................" ("normal", "squint", "angry", "mid")

        "\"The almighty hat is never wrong!\"":
            her "Yes, of course... Everybody knows that..." ("soft", "base", "base", "R")
            gen "(What hat again? I have no fucking clue what she's blabbing about.)" ("base", xpos="far_left", ypos="head")
            gen "(Doesn't hurt playing along...)" ("base", xpos="far_left", ypos="head")

        "\"Could what make what?\"":
            her "Oh, never mind me, [name_genie_hermione]." ("soft", "base", "base", "R")
            her "Everyone knows that the \"Sorting Hat\" is never wrong."

    jump end_hg_pr_flirt


label hg_pr_flirt_T2_E3:

    call hg_pr_flirt_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Five guys, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    her "Yes!" ("base", "happyCl", "base", "mid")
    her "This one guy this morning." ("base", "happyCl", "base", "mid")
    her "Then another two right after the first period."
    her "And then another one before the third period."
    her "And after that, I had a surprisingly pleasant conversation with one more." ("grin", "base", "base", "R")
    her "That last one was quite smart and well-mannered too." ("base", "happyCl", "base", "mid")
    her "............................"
    her "................"
    her "But I still refuse to change my opinion about the Slytherin house, [name_genie_hermione]." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "I'm not asking you to, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I am only doing this to help my own house!"
    her "The proud house of {b}Gryffindor{/b}!" ("scream", "happyCl", "worried", "mid")
    gen "Alright, alright... Calm down, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "" ("base", "happyCl", "base", "mid")

    jump end_hg_pr_flirt

### Tier 3 - LVL 6-X ###

label hg_pr_flirt_T3_E1:

    call hg_pr_flirt_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Eleven boys, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid")
    gen "Eleven? Really? Your personal best, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Yes." ("base", "happyCl", "base", "mid")
    her "Let's see..." ("grin", "base", "base", "R")
    her "Those two handsome guys right before the first period started..."
    her "Then I exchanged a few rather inappropriate messages with this other guy, during the first period." ("smile", "narrow", "base", "mid_soft")
    her "After that there was this one other guy..." ("grin", "base", "base", "R")
    her "Then those three guys..." ("annoyed", "narrow", "worried", "down")
    her "Then one more right before the last period..." ("base", "happyCl", "base", "mid")
    her "And finally this last guy that walked me right to your tower, [name_genie_hermione]..." ("smile", "happyCl", "base", "mid")
    gen "So, eleven, then?" ("base", xpos="far_left", ypos="head")
    gen "Those Slytherin boys are really starting to like you, *huh*?" ("base", xpos="far_left", ypos="head")
    her "I suppose so..." ("base", "happyCl", "base", "mid")
    her "Well, not all of them were nice to me at first..." ("annoyed", "narrow", "worried", "down")
    her "But I used this one trick to \"tame\" them." ("smile", "narrow", "base", "mid_soft")
    gen "A trick, you say?" ("base", xpos="far_left", ypos="head")
    her "Yes... Whenever a boy from Slytherin is being mean to me, or calls me names..." ("open", "base", "base", "R")
    her "I just swallow my pride and smile in response." ("base", "happyCl", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "So, if for example, somebody were to call you a \"whore\" you would just smile at them?" ("base", xpos="far_left", ypos="head")
    her "Well, yes, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "Yeah, I'm sure that wins them over." ("base", xpos="far_left", ypos="head")
    gen "Great job, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "" ("grin", "base", "base", "R")

    jump end_hg_pr_flirt

label hg_pr_flirt_T3_E2:

    call hg_pr_flirt_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I had two dates, and seven quite pleasant conversations..." ("smile", "happyCl", "base", "mid")

    if states.her.status.public_kissing:
        her @ cheeks blush "I even let this one guy kiss me on the lips..." ("soft", "base", "base", "R")
    else:
        her "I even let this one guy kiss me on the cheek..." ("grin", "base", "base", "R")

    gen "Quite impressive, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I think so too, [name_genie_hermione]. Thank you." ("base", "happyCl", "base", "mid")
    her "Oh, and there was also this freshman boy..." ("smile", "happyCl", "base", "mid")
    her "I tried to flirt with him too, but we ended up just chatting..."
    her "He kept calling me \"Miss Hermione\"..." ("base", "happyCl", "base", "mid")
    her "So adorable..."
    gen "I didn't instruct you to harass people, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I didn't harass--" ("disgust", "narrow", "base", "mid_soft")
    her "[name_genie_hermione]! Seven flirts and two dates amount to something, don't they?" ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "Oh, absolutely." ("base", xpos="far_left", ypos="head")
    her "Then I would like to receive my payment now..." ("scream", "closed", "angry", "mid")
    her "" ("normal", "happyCl", "worried", "mid")

    jump end_hg_pr_flirt

label hg_pr_flirt_T3_E3:

    call hg_pr_flirt_intro

    her "[name_genie_hermione], I am sorry, but..." ("normal", "happyCl", "worried", "mid")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I hate those Slytherin tramps, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
    gen "Tell me what happened." ("base", xpos="far_left", ypos="head")
    her "I don't want to talk about it..." ("annoyed", "narrow", "angry", "R")
    gen "Tell me what happened, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    her "I don't want to talk about it, [name_genie_hermione]." ("angry", "base", "angry", "mid", emote="angry")
    her "Please don't make me..." ("annoyed", "narrow", "angry", "R")

    menu:
        "\"Fine. I'll let it go for today.\"":
            her "Thank you, [name_genie_hermione]." ("normal", "happyCl", "worried", "mid")
            gen "No luck with the flirting today then?" ("base", xpos="far_left", ypos="head")
            her "Oh, quite the opposite, [name_genie_hermione]." ("angry", "happyCl", "worried", "mid", emote="sweat")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
            her "One of the boys actually brought me to an empty classroom room today..."
            her "And there were at least a dozen more of them there..." ("normal", "base", "base", "mid")
            her "All of them knew who I was for some reason..." ("open", "closed", "angry", "mid")
            her "And I was the centre of attention..."
            her "I must say, it felt sort of wonderful..." ("base", "narrow", "base", "up")
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
            her "But then a bunch of those Slytherin harlots stumbled in, and..." ("disgust", "narrow", "base", "mid_soft")
            gen "And?" ("base", xpos="far_left", ypos="head")
            her "Well, they started saying stuff and doing things..." ("annoyed", "narrow", "angry", "R")
            gen "\"Stuff and things\"? What kind of things?" ("grin", xpos="far_left", ypos="head")
            her "I'm not sure I should--{w=0.2} Either way, I had to leave..."
            gen "I see..." ("base", xpos="far_left", ypos="head")
            gen "Well, I say you deserve your points anyway, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "" ("base", "happyCl", "base", "mid")

        "\"Tell me now, or lose the points!\"":
            her "[name_genie_hermione], please, I don't want to discuss this with you, [name_genie_hermione]." ("disgust", "narrow", "base", "mid_soft")
            gen "No one is forcing you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            gen "You are free to leave." ("base", xpos="far_left", ypos="head")
            her "{size=-4}(Stubborn old man!){/size}" ("angry", "base", "angry", "mid")

            $ states.her.mood += 10
            jump end_hg_pr_flirt.no_points
    jump end_hg_pr_flirt
