label start_hg_pr_panty_thief:

    if not _events_completed_any:
        gen "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    return

label hg_pr_panty_thief_fail:
    jump end_hermione_event

### Fail Events ###
label hg_pr_panty_thief_T1_E1:

    call start_hg_pr_panty_thief

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Give me your panties!" ("base", xpos="far_left", ypos="head")
    her "Give you--" ("angry", "wide", "base", "stare")
    her "My panties!?!" ("angry", "wide", "worried", "mid")
    gen "That's right, I could really use a pair to--"
    her "I refuse!" ("open", "happyCl", "worried", "mid")
    gen "What? Why not?" ("base", xpos="far_left", ypos="head")
    her "Good day to you, Sir!" ("angry", "happyCl", "worried", "mid")

    call her_walk(action="leave")

    gen "(\"Good day\", she says...{w=0.4} If she really wanted me to have a good day, she would've given me her panties...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 8

    jump hg_pr_panty_thief_fail

label hg_pr_panty_thief_T2_E1:

    call start_hg_pr_panty_thief

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "I could really do with a pair of underwear today... How about you let me borrow yours?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You want to... Borrow my underwear?" ("soft", "wide", "base", "stare")
    gen "Your panties, specifically." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Why would you want to--" ("angry", "base", "base", "mid")
    her @ cheeks blush "What would you need panties for!?" ("disgust", "narrow", "base", "mid")
    gen "Lots of things..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
    her @ cheeks blush "I refuse..." ("annoyed", "narrow", "base", "mid")
    gen "(Figured...)" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Good day to you, Sir..." ("open", "narrow", "base", "R")

    call her_walk(action="leave")

    gen "(\"Good day\", she says...{w=0.4} If she really wanted me to have a good day, she would've let me borrow her panties...)" ("base", xpos="far_left", ypos="head")

    $ states.her.mood += 6

    jump hg_pr_panty_thief_fail

label hg_pr_panty_thief_e1:

    call start_hg_pr_panty_thief

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "I am listening, [name_genie_hermione]." ("open", "base", "base", "mid")
    gen "I will need your panties..." ("base", xpos="far_left", ypos="head")

    if not states.her.status.stripping:
        her "My panties?!" ("open", "base", "worried", "mid")
        gen "That's right..." ("base", xpos="far_left", ypos="head")
        her "But then... I won't have anything to--" ("angry", "base", "worried", "R")
        her "And you..." ("open", "base", "worried", "mid")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her "I'm sorry, [name_genie_hermione]... But you're asking too much..." ("open", "closed", "worried", "mid")

        call her_walk(action="leave")

        $ states.her.mood += 6

        $ _event.cancel()
        jump end_hermione_event

    elif not _events_completed_any:
        stop music fadeout 10.0

        her "W-what?" ("open", "base", "worried", "mid")
        her "My... panties...?"
        her "[name_genie_hermione], this is--"
        gen "This is the favour I will be buying from you today, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "If you are not interested, then you are more than welcome to leave." ("base", xpos="far_left", ypos="head")
        her "No, I am interested... It's just--"
        her "You need my..."

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

        her "... Panties, [name_genie_hermione]?" ("angry", "base", "base", "mid")
        gen "Yes I do..." ("base", xpos="far_left", ypos="head")
        her "May I ask what you are planning to do with them...?" ("disgust", "narrow", "base", "mid_soft")
        gen "*Ehm*... I'm conducting research..." ("base", xpos="far_left", ypos="head")
        if states.her.tier < 5:
            her "But this is kind of inappropriate, don't you think?"
            gen "You wanted to get ahead of Slytherin, did you not?" ("base", xpos="far_left", ypos="head")
            her "Yes, I do!" ("angry", "base", "angry", "mid")
            gen "Right..." ("base", xpos="far_left", ypos="head")
            gen "Tell me, [name_hermione_genie], do you believe that the Slytherin girls would refuse to hand out their panties for points?" ("base", xpos="far_left", ypos="head")
            her "They wouldn't even hesitate... Those Slytherin tramps have no dignity." ("annoyed", "narrow", "angry", "R")
            gen "Well, there you go then!" ("base", xpos="far_left", ypos="head")
            her "*Huh*?" ("disgust", "narrow", "base", "mid_soft")
            gen "If they wouldn't even hesitate..." ("base", xpos="far_left", ypos="head")
            her "..." ("open", "base", "base", "mid")
            gen "Don't you think they'll eventually come out on top and win the cup?" ("base", xpos="far_left", ypos="head")
            her "But--" ("angry", "wide", "base", "mid")
            gen "So, if you truly want your house to win, then you'll have to beat them at their own game!" ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]... Can't you just--" ("open", "base", "worried", "mid")
            gen "Sorry, [name_hermione_genie]... As the headmaster, I cannot play favourites..." ("base", xpos="far_left", ypos="head")
            gen "I wish I could just increase the amount of points I give you for the simple favours, but I have to honour the system..." ("base", xpos="far_left", ypos="head")
            hide hermione_main
            with d3

            if hermione.is_worn("panties"):
                $ hermione.strip("robe", "accessory")
                $ hermione.strip("panties")
                nar "Suddenly Hermione bends forward and takes off her panties."
            else:
                if hermione.is_any_worn("robe", "top", "bottom"):
                    nar "Suddenly Hermione reaches inside one of her hidden pockets."
                else:
                    nar "Suddenly Hermione reaches inside--"
                    nar "Wait, she's not exactly clothed...{w=0.4} Well then..."
                    nar "By some kind of magic, a pair of panties suddenly appears in her hand."

            nar "She extends her arm to you, clutching a little piece of fabric in her fist."
            gen "??!" ("base", xpos="far_left", ypos="head")
            her @ tears soft "Just take them, [name_genie_hermione]..." ("mad", "base", "worried", "mid")
            nar "Slightly surprised, you take the panties from her hand."
            gen "What? When did you?" ("base", xpos="far_left", ypos="head")
            her "Your speech was so moving..."
            her "You are so right, [name_genie_hermione]! I shall beat them at their own game!"
            her "My classes are about to start, so I should probably go now..."
            her @ tears soft "..........." ("normal", "base", "base", "R")
            her "I hope nobody will notice that I have no underwear on today..." ("annoyed", "base", "worried", "R")
            her "Oh, and I will be back tonight to pick them up, [name_genie_hermione]." ("open", "base", "base", "mid")
            gen "Of course. Your panties will be right here on my desk, waiting for you..." ("base", xpos="far_left", ypos="head")
            her "............." ("angry", "happyCl", "worried", "mid")
        else:
            her @ cheeks blush "I see..." ("soft", "base", "base", "mid")
            hide hermione_main
            with d3

            if hermione.is_worn("panties"):
                $ hermione.strip("robe", "accessory")
                $ hermione.strip("panties")
                nar "Suddenly Hermione bends forward and takes off her panties."
            else:
                if hermione.is_any_worn("robe", "top", "bottom"):
                    nar "Suddenly Hermione reaches inside one of her hidden pockets."
                else:
                    nar "Suddenly Hermione reaches inside--"
                    nar "Wait, she's not exactly clothed...{w=0.4} Well then..."
                    nar "By some kind of magic, a pair of panties suddenly appears in her hand."
            nar "She then throws the panties over your desk, and they land in your lap."
            her @ cheeks blush "Here you are." ("open", "closed", "base", "mid")
            gen "(That was easy.)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Anything else?" ("open", "base", "base", "mid")
            gen "That shall do for now [name_hermione_genie]... Feel free to come and collect your panties, later tonight." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright..." ("open", "narrow", "base", "R")

    else:
        if _events_completed_any:
            her "Again, [name_genie_hermione]?"
            gen "Yes, again..." ("base", xpos="far_left", ypos="head")

        her "Here..."

        if states.her.tier > 4:
            hide hermione_main
            with d3

            if hermione.is_worn("panties"):
                $ hermione.strip("robe", "accessory")
                $ hermione.strip("panties")
                nar "Suddenly Hermione bends forward and takes off her panties."
            else:
                if hermione.is_any_worn("top", "bottom"):
                    nar "Hermione pulls her panties out of her pocket."
                else:
                    nar "Suddenly Hermione reaches inside--"
                    nar "Wait, she's not exactly clothed...{w=0.4} Well then..."
                    nar "By some kind of magic, a pair of panties suddenly appears in her hand."

            nar "She casually throws them on your desk."

            gen "What?" ("base", xpos="far_left", ypos="head")
            her "Yes, I had a feeling that you might ask for these today, [name_genie_hermione]." ("base", "base", "base", "mid")
            gen "A feeling?" ("base", xpos="far_left", ypos="head")
            her "Well, to be completely honest I just do not bother to wear them much anymore..." ("grin", "base", "base", "R")

            if hermione.is_equipped("panties"):
                her "Unless I'm asked to, that is..."

        else:
            hide hermione_main
            with d3

            if hermione.is_worn("panties"):
                $ hermione.strip("robe", "accessory")
                $ hermione.strip("panties")
                nar "Hermione takes off her panties without hesitation."
            else:
                if hermione.is_any_worn("top", "bottom"):
                    nar "Suddenly Hermione reaches inside one of her hidden pockets."
                else:
                    nar "Suddenly Hermione reaches inside--"
                    nar "Wait, she's not exactly clothed...{w=0.4} Well..."
                    nar "Magically, a pair of panties suddenly appears in her hand."

            nar "She casually throws the offending underwear on your desk."

        her "Classes are about to start, so I'd better go now..." ("soft", "base", "base", "mid")

    call her_walk(action="leave")

    $ states.her.ev.panty_thief.acquired = True
    call give_reward("You have acquired Hermione's panties!", "interface/icons/panties.webp")

    jump end_hermione_event

label hg_pr_panty_thief_e1_reactions:
    # Hermione responds the cum on her panties

    $ states.her.ev.panty_thief.acquired = False
    call give_reward("You hand over the panties...", "interface/icons/panties_cum.webp")

    if states.her.tier == 3:
        her "*Hmm*....?" ("annoyed", "narrow", "worried", "down")
        her "[name_genie_hermione]? What is this?" ("angry", "base", "angry", "mid")
        her "What have you done to them?"
        her "They are covered in something slimy..." ("normal", "squint", "angry", "mid")

        menu:
            "\"An experiment went wrong!\"":
                her "An experiment went wrong, [name_genie_hermione]?" ("open", "base", "base", "mid")
                gen "Yes... Or maybe I should rather say..." ("base", xpos="far_left", ypos="head")
                gen "\"An experiment went very right\"? *He-he*..." ("grin", xpos="far_left", ypos="head")
                her ".....................?" ("normal", "squint", "angry", "mid")
                her "What kind of experiment was it?"
                gen "What? Oh..." ("base", xpos="far_left", ypos="head")
                gen "Some top secret research I'm conducting." ("base", xpos="far_left", ypos="head")
                gen "I can't discuss it with a student." ("base", xpos="far_left", ypos="head")
                her "................................" ("angry", "base", "angry", "mid")
            "\"You gave them to me like this!\"":
                her "I most certainly did not, [name_genie_hermione]!"
                her ".........................."

        her "Well, these will require some serious cleaning before I can put them on again..." ("annoyed", "narrow", "worried", "down")
        gen "Or you could put them on now." ("base", xpos="far_left", ypos="head")
        her "What?" ("open", "base", "base", "mid")
        her "I really would rather not, [name_genie_hermione]..." ("disgust", "base", "base", "R")

        menu:
            "\"Put them on or lose the points!\"":
                $ states.her.mood +=7
                her "What?" ("scream", "wide", "base", "mid")
                her "[name_genie_hermione], you are joking, right?"
                gen "I am not..." ("base", xpos="far_left", ypos="head")
                her "B-but..." ("open", "base", "base", "mid")
                her "........................................" ("normal", "happyCl", "worried", "mid")
                her "{size=-5}Must you always have your way, [name_genie_hermione]?{/size}" ("angry", "base", "angry", "mid")
                gen "What was that, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her "It's nothing, [name_genie_hermione]." ("scream", "closed", "angry", "mid")
                her "Putting my panties back on!"
                hide hermione_main
                nar "Hermione hesitantly puts on her panties."

                if hermione.is_equipped("panties"):
                    $ hermione.wear("panties")
                else:
                    $ hermione.equip(her_panties_base1)

                nar "A tiny stream of cum trickles down her leg."
                nar "Hermione looks very uncomfortable."
                her "......................" ("angry", "happyCl", "worried", "mid")

            "\"Well, suit yourself...\"":
                pass

        her "And my payment?" ("annoyed", "base", "base", "mid")

    elif states.her.tier == 4:
        her "My panties..." ("annoyed", "narrow", "worried", "down")
        her "What happened to them, [name_genie_hermione]?" ("annoyed", "narrow", "worried", "down")

        menu:
            "\"An experiment went wrong.\"":
                her "*Hmm*..."
                her "I see..."

            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."

        hide hermione_main
        nar "Hermione gives her cum-soaked underwear a quizzical look."
        her "Seems like these will require some serious cleaning before I can put them on again..." ("open", "narrow", "worried", "down")
        gen "Why not put them on now?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*...?" ("annoyed", "squint", "base", "mid")
        her "Well, I suppose I could wear them one more time before putting them into laundry..." ("annoyed", "narrow", "worried", "down")
        hide hermione_main
        nar "Hermione puts on the panties."

        if hermione.is_equipped("panties"):
            $ hermione.wear("panties")
        else:
            $ hermione.equip(her_panties_base1)

        gen "You can go now." ("base", xpos="far_left", ypos="head")
        her "What about my points?" ("angry", "base", "base", "mid")
        gen "You still want points after I just gave you a gift?" ("base", xpos="far_left", ypos="head")
        her "What gift?" ("angry", "base", "annoyed", "mid")
        gen "You're wearing it." ("base", xpos="far_left", ypos="head")
        her "What, soaked panties?"
        gen "If you preferred receiving points, then you shouldn't have put them on." ("base", xpos="far_left", ypos="head")
        her "Then why didn't you tell me before!" ("annoyed", "base", "worried", "R")
        gen "Good girls say \"thank you\" when they receive a gift." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]...{w=0.3} for the gift." ("annoyed", "squint", "base", "mid")
        gen "You can go now." ("base", xpos="far_left", ypos="head")
        her "Alright... Good night then, [name_genie_hermione]."

    elif states.her.tier == 5:
        her "My panties..." ("annoyed", "narrow", "worried", "down")
        her "They are covered in something slimy..."
        her "And they smell funny..."
        her "*Hmm*... That smell..." ("annoyed", "base", "worried", "R")
        her "What exactly did you do to them, [name_genie_hermione]?" ("open", "base", "base", "mid")

        menu:
            "\"An experiment went wrong\"":
                her "An experiment, *huh*?"
                her "Of what nature?"
                her "No, don't answer that... I think I know..." ("disgust", "base", "base", "R")

            "\"You gave them to me like this!\"":
                her "I don't think so, [name_genie_hermione]."
                her "But it's alright if you don't want to tell me, [name_genie_hermione]..."
                her "I already know exactly what happened to them..."

            "\"I came all over them!\"":
                her "I knew it..." ("disgust", "narrow", "base", "mid_soft")
                her "They reek of semen!"

        her "*Hmm*..." ("annoyed", "base", "base", "R")
        her "Seems like these will require some serious cleaning before I can put them on..."
        her "Unless you require me to put them on now, [name_genie_hermione]...?" ("soft", "narrow", "base", "R")

        menu:
            "\"Yes! Put them on now, [name_hermione_genie]!\"":
                her "Well, if I must..."
                her "I am only doing it to give my house a fair chance at winning the cup this year..." ("base", "happyCl", "base", "mid")

            "\"I don't care. Do what you want.\"":
                her "Well, I suppose I shouldn't be walking around without underwear, unless you've asked me to..."

        gen "Right..." ("base", xpos="far_left", ypos="head")
        hide hermione_main
        nar "Hermione swiftly slides into her drenched panties..."

        if hermione.is_equipped("panties"):
            $ hermione.wear("panties")
        else:
            $ hermione.equip(her_panties_base1)

        her "(This feels funny...)" ("angry", "closed", "worried", "mid")
        gen "Alright then... Off you go." ("base", xpos="far_left", ypos="head")
        her "But what about...{w=0.4} Okay then...{w=0.4} Good night, [name_genie_hermione]." ("angry", "base", "worried", "mid")

    elif states.her.tier >= 6:
        her "My panties..." ("base", "narrow", "base", "up")
        her "You came all over them..."
        her "*Hmm*..." ("grin", "base", "base", "R")
        her "These will require some serious cleaning before I can put them on..."
        her "Unless you want me to put them on now, [name_genie_hermione]...?" ("soft", "narrow", "base", "R")

        menu:
            "\"Yes! Put them on now, [name_hermione_genie]!\"":
                her "Of course, I'd prefer not to do it, [name_genie_hermione]..."
                her "But for the honour of house Gryffindor." ("soft", "closed", "base", "mid")
                her "I'll do it... I'll... Even though it's gross..." ("base", "narrow", "base", "up")
                gen "Right..." ("base", xpos="far_left", ypos="head")
                hide hermione_main
                nar "Hermione swiftly slides her drenched panties on..."

                if hermione.is_equipped("panties"):
                    $ hermione.wear("panties")
                else:
                    $ hermione.equip(her_panties_base1)

                her "..." ("soft", "narrow", "annoyed", "up")
            "\"Why don't you clean them now, instead?\"":
                her "Of course, [name_genie_hermione]... Let me just get my wand." ("open", "base", "base", "mid")
                gen "Not by using your wand, [name_hermione_genie]... Using your mouth." ("base", xpos="far_left", ypos="head")
                her "My mouth?!" ("scream", "wide", "base", "mid")
                gen "What's the big deal? You've done more than that, before." ("base", xpos="far_left", ypos="head")
                her "It's a bit different! I wore these panties before I gave them to you." ("scream", "closed", "angry", "mid")
                her "Not to mention that your cum is all cold and slimy..." ("scream", "happyCl", "worried", "mid")
                gen "Well in that case, hand them back." ("base", xpos="far_left", ypos="head")
                her "What? Can't I just put them on?" ("angry", "wink", "base", "mid")
                gen "I'm afraid not... Either you clean them, or you hand them back." ("base", xpos="far_left", ypos="head")
                her "{size=-4}Fine...{/size}" ("angry", "narrow", "base", "down")
                gen "What was that?" ("base", xpos="far_left", ypos="head")
                her "I said I'll clean them, okay!?" ("shock", "happyCl", "worried", "mid")
                gen "Well..." ("base", xpos="far_left", ypos="head")
                her "..." ("angry", "narrow", "base", "down")
                nar "Hermione reluctantly puts her cum-soaked panties in her mouth."
                play sound "sounds/gltch.ogg"
                her "*Mmmmhhhhh*!" ("full_panties", "slit", "worried", "ahegao")
                gen "That's it [name_hermione_genie]... Not as bad as you thought, is it?" ("base", xpos="far_left", ypos="head")
                her "..." ("full_panties", "slit", "low", "stare")
                gen "Make sure you get them nice and clean now..." ("base", xpos="far_left", ypos="head")
                play sound "sounds/gulp.ogg"
                her @ cheeks blush "*Gulp*" ("full_panties", "narrow", "worried", "down")
                gen "That's it... Do you think they're clean yet?" ("base", xpos="far_left", ypos="head")
                her "*Mmmhhhmmm*" ("full_panties", "narrow", "base", "dead")
                gen "Open your mouth, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                play sound "sounds/gltch.ogg"
                her "*Ahhhhh*" ("open_wide_tongue_panties", "narrow", "annoyed", "up")
                gen "That's a good girl... Nice and clean." ("base", xpos="far_left", ypos="head")
                gen "You can take them out now." ("base", xpos="far_left", ypos="head")
                her "........" ("angry", "happyCl", "worried", "up")

        gen "Alright then, you may go..." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]..." ("angry", "narrow", "base", "down")
        gen "After you say \"thank you\"..." ("base", xpos="far_left", ypos="head")
        her "Thank you for what?" ("angry", "wink", "base", "mid")
        gen "For my cum." ("base", xpos="far_left", ypos="head")
        her "..." ("base", "narrow", "worried", "down")
        her "Thank you for your cum, [name_genie_hermione]..." ("grin", "narrow", "base", "down")
        gen "Good... You may leave." ("base", xpos="far_left", ypos="head")
        her "Good night, [name_genie_hermione]." ("open", "happy", "base", "mid")

    $ achievements.unlock("pantiesfap")
    jump hg_pr_panty_thief_e1_return.end

label hg_pr_panty_thief_e1_return:
    # Hermione returns to get her panties back

    $ hermione.strip("panties")

    call her_walk(action="enter", xpos="mid", ypos="base")

    her "Good evening, [name_genie_hermione]..." ("base", "base", "base", "mid",xpos="right",ypos="base", trans=d5)
    her "I came to retrieve what's mine..." ("open", "base", "base", "mid",xpos="right",ypos="base", trans=d5)
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    menu:
        "\"Here are your panties.\"":
            if states.her.ev.panty_thief.soaked:
                jump hg_pr_panty_thief_e1_reactions
            else:
                her "And my payment?"

        "\"How was your day, [name_hermione_genie]?\"":
            if states.her.tier == 3:
                her "Oh..." ("soft", "base", "base", "mid")
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And I conducted a short \"MRM\" meeting after that..."
                her "I gave a rather short speech on how we could level out the playing-field, so that the men could earn more house points..." ("open", "closed", "base", "mid")
                her "Although I felt a bit uncomfortable, doing it without any underwear on..." ("annoyed", "narrow", "angry", "R")
                her "I couldn't help but worry that somebody would notice somehow..." ("soft", "base", "base", "R")
                menu:
                    "\"You little hypocrite!\"":
                        $ states.her.mood +=5
                        her "[name_genie_hermione]?" ("open", "base", "base", "mid")
                        gen "You're taking part in the favour trading, by lending me your panties this morning..." ("base", xpos="far_left", ypos="head")
                        gen "Then a couple of hours later, you're giving a speech about how it's unfair..." ("base", xpos="far_left", ypos="head")
                        her "I'll have to do this, until the boys get to be more included!" ("annoyed", "narrow", "angry", "R")
                        gen "If you want them to be included, then why not just ask them to come watch you earn the points." ("base", xpos="far_left", ypos="head")
                        her "...{w=0.4} Can I have my payment now please?" ("disgust", "narrow", "base", "mid_soft")
                        gen "What about your panties?" ("base", xpos="far_left", ypos="head")
                        her "Oh, them too of course..." ("angry", "happyCl", "worried", "mid")
                        if states.her.ev.panty_thief.soaked:
                            jump hg_pr_panty_thief_e1_reactions

                    "\"It's for the greater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so unfair..."
                        her "I shall remain a symbol of righteousness to my peers, no matter what!" ("open", "closed", "base", "mid")
                        her "Can I have my panties back now, please?" ("open", "base", "base", "mid")
                        gen "Certainly..." ("base", xpos="far_left", ypos="head")
                        if states.her.ev.panty_thief.soaked:
                            jump hg_pr_panty_thief_e1_reactions
                        else:
                            nar "You give Hermione her panties back."
                            her "And my payment."
            elif states.her.tier == 4:
                her "It was fine..." ("open", "closed", "base", "mid")
                gen "Just fine?" ("base", xpos="far_left", ypos="head")
                her "Well, as fine it could be... When you have to walk around without any underwear on, all day."
                gen "Great, I'm glad you enjoyed it." ("base", xpos="far_left", ypos="head")
                her "That's not--" ("annoyed", "base", "worried", "R")
                her "..."
                her "Can I have my panties back now, please?" ("open", "base", "base", "mid")
                gen "Of course..." ("base", xpos="far_left", ypos="head")
                if states.her.ev.panty_thief.soaked:
                    jump hg_pr_panty_thief_e1_reactions
                else:
                    nar "You give Hermione her panties back."
                    her "And my payment?" ("base", "base", "base", "mid")
            elif states.her.tier == 5:
                her "Another ordinary day at Hogwarts..." ("open", "closed", "base", "mid")
                her "Nothing worth mentioning happened today..."
                her "Although I have to admit..." ("annoyed", "base", "worried", "R")
                her "It was oddly empowering to spend the day, without any underwear on..."
                her "*Hmm*..."
                her "Can I have my panties back now please?" ("base", "base", "base", "mid")
                gen "Of course..." ("base", xpos="far_left", ypos="head")
                if states.her.ev.panty_thief.soaked:
                    jump hg_pr_panty_thief_e1_reactions
                else:
                    nar "You give Hermione her panties back."
                    her "And my payment?" ("base", "base", "base", "mid")
            elif states.her.tier >= 6:
                her "It was good, nothing out of the ordinary really..." ("open", "closed", "base", "mid")
                gen "Did it not feel strange, walking around without any panties all day?" ("base", xpos="far_left", ypos="head")
                her "*Hmm*... No, not really..." ("base", "closed", "base", "mid")
                gen "In that case, I assume you wouldn't mind if I kept them?" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "I didn't say that..." ("base", "base", "base", "R")
                gen "Oh well..." ("base", xpos="far_left", ypos="head")
                if states.her.ev.panty_thief.soaked:
                    jump hg_pr_panty_thief_e1_reactions
                else:
                    nar "You give Hermione her panties back."
                    her "And my payment?" ("base", "base", "base", "mid")

    label .end:

    if not states.her.ev.panty_thief.soaked or states.her.tier < 4:
        gen "Yes, yes..." ("base", xpos="far_left", ypos="head")
        $ gryffindor +=15
        gen "Fifteen points to Gryffindor, [name_hermione_genie]... Well deserved." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]..." ("soft", "base", "base", "R")
        gen "You can go now." ("base", xpos="far_left", ypos="head")

    her "Good night, [name_genie_hermione]." ("base", "base", "base", "mid")
    gen "Yes, good night..." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")
    $ states.her.ev.panty_thief.soaked = False

    jump end_hermione_event
