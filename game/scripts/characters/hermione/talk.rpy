label hermione_talk:
    menu:
        ### Astoria ###
        "-Ask her to help Tonks-" (icon="interface/icons/small/tonks.webp") if states.ast.ev.intro.e1_complete and not states.ast.ev.intro.e3_complete:
            if states.ast.ev.intro.e2_ask_hermione:
                her "I'm still looking for that student, [name_genie_hermione]!" ("open", "closed", "base", "mid")
                her "Trust in me, I will find that Slytherin scum!" ("angry", "base", "angry", "mid")
                jump hermione_talk

            $ states.her.busy = True
            $ states.ast.ev.intro.e2_ask_hermione = True
            $ ag_event_pause = 2
            jump astoria_intro_E2_hermione


        ### Cho ###
        "-Solve the matter with Cho-" (icon="interface/icons/small/cho.webp", style="disabled") if states.cho.ev.intro.e2_complete and not states.sna.ev.hangouts.cho_e1:
            # Before talking to Snape.
            gen "(I should ask Snape what to do about that Cho girl first. Just to be safe.)" ("base", xpos="far_left", ypos="head")
            gen "(Might as well have a drink with him...)" ("base", xpos="far_left", ypos="head")
            jump hermione_talk

        "-Solve the matter with Cho-" (icon="interface/icons/small/cho.webp") if states.sna.ev.hangouts.cho_e1 and not states.cho.ev.intro.e4_complete:
            # After talking to Snape.
            jump cho_intro_E3

        "-Ask her to commentate the game-" (icon="interface/icons/small/quidditch.webp") if states.cho.tier == 1 and states.cho.ev.quidditch.e3_complete and not states.cho.ev.quidditch.e4_complete:
            jump cho_quid_E4

        "-Ask her to commentate the game-\n{size=-5}again...{/size}" (icon="interface/icons/small/quidditch.webp") if states.cho.tier == 2 and states.cho.ev.quidditch.e6_complete and not states.cho.ev.quidditch.e7_complete:
            jump cho_quid_E7

        # General.
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ name_genie_hermione = "Sir"
                    jump genie_change
                "-Dumbledore-":
                    $ name_genie_hermione = "Dumbledore"
                    jump genie_change
                "-Professor-":
                    $ name_genie_hermione = "Professor"
                    jump genie_change
                "-Old man-":
                    $ name_genie_hermione = "Old man"
                    jump genie_change
                "-Genie-":
                    if states.her.level >=5:
                        $ name_genie_hermione = "Genie"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-My Lord-":
                    if states.her.level >=7:
                        $ name_genie_hermione = "My Lord"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Darling-":
                    if states.her.level >=10:
                        $ name_genie_hermione = "Darling"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Lord Voldemort-":
                    if states.her.level >=15:
                        $ name_genie_hermione = "Lord Voldemort"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Daddy-":
                    if states.her.level >=19:
                        $ name_genie_hermione = "Daddy"
                        $ achievements.unlock("daddy")
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Master-":
                    if states.her.level >=20:
                        $ name_genie_hermione = "Master"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", name_genie_hermione, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump hermione_talk
                    if states.her.level >=20:
                        $ name_genie_hermione = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-From now on, I will refer to you as-":
            menu:
                "-Miss Granger-":
                    $ temp_name = "Miss Granger"
                    jump hermione_change
                "-Hermione-":
                    $ temp_name = "Hermione"
                    jump hermione_change
                "-Girl-":
                    $ temp_name = "Girl"
                    if states.her.level >=1:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Nerd-":
                    $ temp_name = "Nerd"
                    if states.her.level >=3:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Hottie-":
                    $ temp_name = "Hottie"
                    if states.her.level >=5:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Angel-":
                    $ temp_name = "Angel"
                    if states.her.level >=7:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Minx-":
                    $ temp_name = "Minx"
                    if states.her.level >=9:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Princess-":
                    $ temp_name = "Princess"
                    if states.her.level >=11:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Pet-":
                    $ temp_name = "Pet"
                    if states.her.level >=11:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Bitch-":
                    $ temp_name = "Bitch"
                    if states.her.level >=15:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slut-":
                    $ temp_name = "Slut"
                    if states.her.level >=19:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Cumslut-":
                    $ temp_name = "Cumslut"
                    if states.her.level >= 19:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slytherin Whore-":
                    $ temp_name = "Slytherin Whore"
                    if states.her.level >= 22:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Mudblood-":
                    $ temp_name = "Mudblood"
                    if states.her.level >= 22:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)", name_hermione_genie, ALLOWED_CHARACTERS, length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        jump hermione_talk
                    if states.her.level >=21:
                        $ name_hermione_genie = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-Give her the ball dress-" if states.her.ev.yule_ball.e4_complete and ball_outfit_ITEM.owned > 0 and not states.her.ev.yule_ball.gave_dress:
            jump ball_quest_E5

        "-Start the autumn ball-" if states.her.ev.yule_ball.gave_dress and not states.her.ev.yule_ball.started:
            jump ball_ending_start

        "-Never mind-":
            jump hermione_requests


label genie_change:
    her "Okay, from now on I'll call you [name_genie_hermione]." ("base", "base", "base", "mid")
    jump hermione_talk

label genie_change_fail:
    her "I'm not calling you that!" ("scream", "closed", "angry", "mid")
    jump hermione_talk

label hermione_change:
    if temp_name == "Miss Granger":
        if states.her.level <=0:
            her "Sure, [name_genie_hermione]." ("base", "base", "base", "mid")
        else:
            her "You don't have to be so formal, [name_genie_hermione], you know?" ("base", "closed", "base", "mid")
            her "" ("base", "base", "base", "mid")
    elif temp_name == "Hermione":
        her "Of course [name_genie_hermione]." ("base", "base", "base", "mid")
    elif temp_name == "Girl":
        if states.her.level >=1 and states.her.level < 3:
            her "This girl thing again?" ("annoyed", "happy", "base", "mid")
            her "*sigh*..." ("soft", "happy", "base", "R")
        elif states.her.level >=3:
            her "Fine... I don't mind." ("soft", "base", "base", "R")
    elif temp_name == "Nerd":
        if states.her.level >=3 and states.her.level < 5:
            her "*sigh* I just enjoy books, that's all." ("annoyed", "narrow", "worried", "down")
            gen "I'm sure you'll find other things to enjoy soon enough..." ("base", xpos="far_left", ypos="head")
            her "Like what exactly?" ("normal", "narrow", "base", "mid_soft")
            gen "Nothing to worry about, things will work out..." ("base", xpos="far_left", ypos="head")
            gen "Nerd..." ("grin", xpos="far_left", ypos="head")
            her "*tsk* ..." ("soft", "narrow", "base", "R_soft")
            her "" ("normal", "narrow", "base", "R_soft")
        elif states.her.level >= 5 and states.her.level < 19:
            her "I can be a bit nerdy sometimes I suppose..." ("angry", "happyCl", "base", "mid", emote="sweat")
            her "" ("base", "base", "base", "mid")
        elif states.her.level >= 19:
            her "I don't read as much as I used to anymore." ("grin", "narrow", "base", "R_soft", emote="sweat")
            her "" ("base", "narrow", "base", "mid_soft")
    elif temp_name == "Hottie":
        if states.her.level >=5 and states.her.level < 7:
            her @ cheeks blush "[name_genie_hermione]?!" ("angry", "wide", "angry", "mid")
            gen "What? That's true, you're hot." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That's inappropriate." ("annoyed", "base", "worried", "R")
            her "But I'll let it slide, I guess."
        elif states.her.level >=7 and states.her.level < 19:
            her "Thank you, [name_genie_hermione]." ("soft", "wink", "base", "mid")
            her "" ("normal", "base", "base", "mid")
        elif states.her.level >=19:
            her @ cheeks blush "... Glad you think so." ("smile", "wink", "base", "mid")
            her @ cheeks blush "" ("base","happy", "base", "mid")
    elif temp_name == "Good Girl":
        if states.her.level >=5 and states.her.level < 7:
            her "Well, I do try my best, [name_genie_hermione]." ("base", "closed", "base", "mid")
            her "" ("base", "base", "base", "mid")
        elif states.her.level >=7 and states.her.level < 19:
            her "I'm not sure if I'd qualify, but fine." ("annoyed", "wink", "base", "mid")
            her "" ("normal", "base", "base", "mid")
        elif states.her.level >=19:
            her @ cheeks blush "I could act like a good girl if you really want me to..." ("smile", "wink", "base", "mid")
            her @ cheeks blush "" ("base","happy", "base", "mid")
    elif temp_name == "Angel":
        if states.her.level >=7 and states.her.level < 9:
            her "What's going on with these silly nicknames of yours all of a sudden?" ("normal", "squint", "angry", "mid")
            gen "What do you mean by silly?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Ugh, forget I said anything..." ("open", "narrow", "base", "down")
            her @ cheeks blush "" ("normal", "base", "base", "R")
        elif states.her.level >=9 and states.her.level < 19:
            her @ cheeks blush "I like it..." ("soft", "narrow", "base", "R_soft")
            her @ cheeks blush "" ("base", "narrow", "base", "R_soft")
        elif states.her.level >= 19:
            her @ cheeks blush "I'm surprised I didn't grow wings yet." ("base", "narrow", "worried", "mid_soft")
    elif temp_name == "Little Girl":
        if states.her.level >=7 and states.her.level < 9:
            her "What's going on with these silly nicknames of yours all of a sudden?" ("normal", "squint", "angry", "mid")
            gen "What do you mean by silly?" ("base", xpos="far_left", ypos="head")
            her "It makes it sound as if I'm your..." ("soft", "base", "worried", "R")
            her @ cheeks blush "Ugh, forget I said anything..." ("open", "narrow", "base", "down")
            her @ cheeks blush "" ("normal", "base", "base", "R")
        elif states.her.level >=9 and states.her.level < 19:
            her "Bit of an odd request but..." ("normal", "narrow", "base", "down")
            her @ cheeks blush "I like it..." ("soft", "narrow", "base", "R_soft")
            her @ cheeks blush "" ("base", "narrow", "base", "R_soft")
        elif states.her.level >= 19:
            her @ cheeks blush "Yes, [name_genie_hermione]." ("base", "narrow", "worried", "mid_soft")
    elif temp_name == "Bad Girl":
        if states.her.level >=9 and states.her.level < 11:
            her "I guess I am a bit." ("soft", "narrow", "worried", "down")
            her "I did fail that test after all..." ("disgust", "narrow", "base", "down")
            her "" ("normal", "narrow", "worried", "mid_soft")
            her "" ("normal", "base", "base", "mid")
        elif states.her.level >=11 and states.her.level < 17:
            her @ cheeks blush "I may be a little bit naughty at times." ("base", "happy", "base", "R")
        elif states.her.level >=17:
            her @ cheeks blush "I may be a little bit naughty at times." ("base", "happy", "base", "R")
            her @ cheeks blush "" ("base", "base", "base", "mid")
    elif temp_name == "Minx":
        if states.her.level >=9 and states.her.level < 11:
            her "I guess I am a bit." ("soft", "narrow", "worried", "down")
            her "" ("normal", "narrow", "worried", "mid_soft")
        elif states.her.level >=11 and states.her.level < 17:
            her @ cheeks blush "I may be a little bit naughty at times." ("base", "happy", "base", "R")
        elif states.her.level >=17:
            her @ cheeks blush "I may be a little bit naughty at times." ("base", "happy", "base", "R")
            her @ cheeks blush "" ("base", "base", "base", "mid")
    elif temp_name == "Princess":
        if states.her.level >= 11 and states.her.level < 13:
            her @ cheeks blush "That would make you my prince wouldn't it?" ("open", "base", "base", "R")
            her @ cheeks blush "" ("base", "base", "base", "mid")
        elif states.her.level >= 13:
            her "Yes... My prince." ("smile","happy", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "I-I mean, [name_genie_hermione]." ("smile", "happyCl", "base", "mid", emote="sweat")
            her "" ("base", "base", "base", "mid")
    elif temp_name == "Pet":
        if states.her.level >= 11 and states.her.level < 13:
            her "You want to call me....{w=0.5} a pet?" ("normal", "squint", "angry", "mid")
            gen "Yes." ("base", xpos="far_left", ypos="head")
            her ".... {w=0.5}.... {w=0.5}.... {w=0.5}...." ("normal", "happy", "base", "mid")
            her "" ("normal", "squint", "base", "mid")
            gen ".... {w=0.5}.... {w=0.5}...." ("base", xpos="far_left", ypos="head")
            her "May I at least know why?" ("open", "squint", "base", "mid")
            gen "No." ("base", xpos="far_left", ypos="head")
            her "...." ("annoyed", "base", "worried", "mid")
        elif states.her.level >= 13:
            her "*Meow*" ("smile","happyCl", "base", "mid")
            her "" ("smile","happy", "base", "mid")
            gen "Don't do that..." ("base", xpos="far_left", ypos="head")
            her "Such a party pooper." ("annoyed","happyCl", "base", "mid")
            her "" ("base", "base", "base", "mid")
    elif temp_name == "Bitch":
        if states.her.level >=13 and states.her.level < 15:
            her "Isn't this a bit inappropriate [name_genie_hermione]?" ("mad", "narrow", "worried", "down")
            gen "And doing favours for house points isn't?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine..." ("base", "narrow", "base", "down")
        elif states.her.level >= 15 and states.her.level < 17:
            her @ cheeks blush "..." ("normal", "narrow", "worried", "down")
            gen "Any objections?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("soft", "base", "worried", "R")
            gen "Okay then..." ("grin", xpos="far_left", ypos="head")
        elif states.her.level >= 17:
            her @ cheeks blush "Alright." ("base", "happyCl", "base", "mid")
            her @ cheeks blush "" ("base","happy", "base", "mid")
    elif temp_name == "Slut":
        if states.her.level >=15 and states.her.level < 17:
            her "[name_genie_hermione]?!" ("shock", "wide", "worried", "stare")
            her "You can't just call someone that!" ("mad", "wide", "base", "stare")
            gen "It'll just be between us..." ("base", xpos="far_left", ypos="head")
            her "..." ("disgust", "squint", "base", "mid")
            gen "Nothing to add?" ("base", xpos="far_left", ypos="head")
            her "" ("clench", "closed", "base", "mid", emote="angry")
            gen "So you'll let me call you that or not?" ("base", xpos="far_left", ypos="head")
            her "{size=+5}FINE!{/size}" ("clench", "closed", "angry", "mid", emote="angry")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "" ("normal", "narrow", "angry", "R")
        elif states.her.level >= 17:
            her @ cheeks blush "I guess if you have to call me that, sure..." ("base", "narrow", "base", "down")
        elif states.her.level >= 19:
            her @ cheeks blush "I don't mind..." ("smile", "happyCl", "base", "mid")
    elif temp_name == "Cumslut":
        if states.her.level >= 17 and states.her.level < 19:
            her "A cumslut?!" ("open", "wide", "worried", "stare")
            gen "Something wrong?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You have to even ask?" ("soft", "narrow", "worried", "down")
            her @ cheeks blush "This is so degrading..." ("normal", "narrow", "base", "down")
            her @ cheeks blush "(But I kinda am a slut begging for cum aren't I...)" ("base", "happyCl", "base", "mid")
        elif states.her.level >= 19:
            her "..." ("soft", "narrow", "base", "up")
            her @ cheeks blush "(When did I start enjoying it so much...)" ("open", "narrow", "base", "up")
            her @ cheeks blush "(That taste, the texture...)" ("open", "narrow", "annoyed", "up")
            her @ cheeks blush "(So warm, sticky, and--)" ("silly", "narrow", "base", "up")
            gen "Are you okay there, [temp_name]?" ("base", xpos="far_left", ypos="head")
            her "Wha--" ("mad", "wide", "base", "stare")
            her @ cheeks blush "Of course I am!" ("smile", "base", "base", "R")
    elif temp_name == "Slytherin Whore":
        if states.her.level >=19 and states.her.level < 21:
            her "Do you really have to call me that, [name_genie_hermione]?" ("disgust", "base", "worried", "mid")
            her @ cheeks blush "Referring to me as a bitch or a slut for your own amusement is one thing..." ("mad", "narrow", "worried", "down")
            her "You're aware of how much I loathe Slytherin." ("open", "narrow", "worried", "mid_soft")
            her "And I'm definitely not a whore..." ("soft", "closed", "base", "mid")
            her "I refuse!"
            menu:
                "-Say it's fine-":
                    gen "Fine, I won't call you that..." ("base", xpos="far_left", ypos="head")
                    her "You won't?" ("open", "base", "base", "mid")
                    her "" ("soft", "base", "base", "mid")
                    gen "Of course..." ("base", xpos="far_left", ypos="head")
                    her "I am glad we're on the same page on this one, [name_genie_hermione]." ("open", "closed", "base", "mid")
                    her "" ("base", "closed", "base", "mid")
                    gen "In fact, from this point forward you don't have to call me [name_genie_hermione] or exchange any favours..." ("base", xpos="far_left", ypos="head")
                    her "" ("soft", "base", "base", "mid", emote="confused")
                    gen "Let's just void this whole... deal of yours, shall we?" ("base", xpos="far_left", ypos="head")
                    her "B-but, [name_genie_hermione]?!" ("mad", "wide", "base", "mid", emote="shocked")
                    her "" ("mad", "wide", "base", "mid")
                    gen "I must apologise {b}Miss Granger{/b}, I thought we had come to some kind of agreeable arrangement by now..." ("base", xpos="far_left", ypos="head")
                    her "But I--" ("mad", "wide", "worried", "stare")
                    gen "I should have known better to believe that this sort of thing would work out..." ("base", xpos="far_left", ypos="head")
                    her "Maybe I coul--" ("clench","happyCl", "worried", "stare")
                    gen "I thought we both had what we wanted..." ("base", xpos="far_left", ypos="head")
                    her "Liste--" ("soft", "narrow", "worried", "down")
                    her "" ("normal", "closed", "angry", "mid")
                    gen "Might as well hand in my resignation with the ministry and--" ("base", xpos="far_left", ypos="head")
                    with hpunch
                    her @ cheeks blush "{size=+10}I AM A SLYTHERIN WHORE!!!{/size}" ("scream", "closed", "angry", "mid")
                    her "" ("normal", "closed", "base", "mid")
                    gen "..." ("base", xpos="far_left", ypos="head")
                    her "Now please, [name_genie_hermione]... Let's just forget this conversation ever happened." ("disgust", "base", "worried", "mid")
                    gen "Are you sure that's what you want, [temp_name]?" ("base", xpos="far_left", ypos="head")
                    her "... Yes." ("disgust", "narrow", "worried", "down", emote="sweat")
                    gen "(This girl really is beyond redemption...)" ("base", xpos="far_left", ypos="head")
                    her "" ("base", "narrow", "worried", "down")
                "-Threaten her-":
                    gen "Either accept my offer or Gryffindor lose five hundred points..." ("angry", xpos="far_left", ypos="head")
                    with hpunch
                    her "FIVE HUNDRED?!" ("shock", "wide", "base", "stare")
                    her "[name_genie_hermione]... This is blackmailing!" ("scream", "closed", "angry", "mid")
                    her "" ("mad", "closed", "angry", "mid")
                    gen "It is?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "What else would it be?" ("mad", "base", "angry", "mid")
                    gen "Negotiations..." ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "You..." ("clench", "closed", "angry", "mid")
                    gen "That's not an answer..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "{size=-10}Okay...{/size}" ("soft", "narrow", "angry", "R")
                    gen "What was that? I didn't hear you." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I said yes, you can call me a Slytherin whore... or whatever." ("normal", "narrow", "annoyed", "mid")
                    her @ cheeks blush "Happy now?!" ("open", "closed", "angry", "mid")
                    gen "Very." ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "{size=-6}You are the worst.{/size}" ("normal", "narrow", "base", "R_soft")
                    $ states.her.mood += 15
        elif states.her.level >= 21:
            her "Please, [name_genie_hermione], couldn't you call me something else instead?" ("open", "base", "worried", "mid")
            gen "But where's the fun in that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Why do I even bother... *sigh*" ("soft", "narrow", "base", "R_soft")
    elif temp_name == "Mudblood":
        if states.her.level >= 21 and states.her.status.sex:
            her "A{w=0.5}...{w=0.5} {size=+6}{b}{cps=20}mud{w=0.5}blood{/cps}{/b}?!{/size}" ("shock", "wide", "base", "stare")
            her "Did I hear you right, [name_genie_hermione]?!" ("normal", "wide", "base", "mid")
            menu:
                "-Confirm-":
                    pass
                "-!!!{b}ABORT ABORT ABORT{/b}!!!-{#LINT_IGNORE}":
                    gen "What? Of course not!" ("angry", xpos="far_left", ypos="head")
                    gen "I said..." ("base", xpos="far_left", ypos="head")
                    gen "(I have to think fast)" ("angry", xpos="far_left", ypos="head")
                    menu:
                        "-Mass flood-":
                            gen "I said mass flood!" ("angry", xpos="far_left", ypos="head")
                            her "Mass flood?" ("soft", "base", "base", "mid")
                            gen "Are you deaf or something?" ("base", xpos="far_left", ypos="head")
                            if game.weather == "rain":
                                her "I was pretty sure you said--" ("open", "base", "base", "mid")
                                her "" ("normal", "base", "base", "R")
                                gen "Look outside the window, it's raining is it not?" ("base", xpos="far_left", ypos="head")
                                her "I{w=0.5}...{w=0.5} Yes, you are right [name_genie_hermione]." ("normal", "closed", "base", "mid")
                                gen "Of course I am." ("base", xpos="far_left", ypos="head")
                                her "So what did you want to talk about?" ("base", "base", "base", "mid")
                            else:
                                her "[name_genie_hermione], but it's not raining..." ("normal", "closed", "base", "mid")
                                her @ cheeks blush "" ("disgust", "narrow", "base", "down")
                                gen "Last time I had my dick in you, it felt like a mass flood." ("grin", xpos="far_left", ypos="head")
                                her @ cheeks blush "[name_genie_hermione]..." ("disgust", "closed", "base", "mid")
                                gen "What? It's true, I swear!" ("grin", xpos="far_left", ypos="head")
                                her @ cheeks blush "..." ("soft", "narrow", "worried", "down")
                        "-Mad stud-":
                            gen "I said mad stud!" ("angry", xpos="far_left", ypos="head")
                            her "Mad stud?" ("soft", "base", "base", "mid")
                            gen "My dick, your ass, bud." ("grin", xpos="far_left", ypos="head")
                            her @ cheeks blush "Really..." ("disgust", "narrow", "base", "mid_soft")
                            her @ cheeks blush "You can be so childish sometimes, [name_genie_hermione]..." ("annoyed", "narrow", "base", "R_soft")
                    jump hermione_talk
            her "Why would you even suggest calling me such a thing..." ("scream", "squint", "angry", "mid")
            her @ tears soft "It's like the most offensive thing you could call someone like..." ("shock", "squint", "angry", "mid")
            her @ tears soft_blink "Like..." ("open", "happyCl", "worried", "mid")
            her @ tears mascara_crying "Someone like..." ("open", "narrow", "worried", "down")
            her @ tears mascara_soft "Me..." ("disgust", "narrow", "worried", "down")
            her @ tears mascara "" ("disgust", "happyCl", "worried", "mid")
            menu:
                "-Try to calm her down-":
                    her @ tears mascara "" ("disgust", "narrow", "worried", "mid_soft")
                    gen "Now, now, there's no need to cry." ("base", xpos="far_left", ypos="head")
                    gen "Do you know why I call you these things, Miss Granger?" ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "... No?" ("disgust", "narrow", "worried", "mid_soft")
                    gen "It's so that you'll come to know that words are just words, and they only hurt if you let them." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "..." ("normal", "narrow", "worried", "mid_soft")
                    gen "Once you truly understand that nothing will hold you back." ("base", xpos="far_left", ypos="head")
                    gen "And you'll be at your utmost potential." ("grin", xpos="far_left", ypos="head")
                    her @ tears mascara "You really think so?" ("open", "narrow", "worried", "mid_soft")
                    her @ tears mascara "" ("normal", "narrow", "worried", "mid_soft")
                    gen "Yes, in fact I do." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "Thank you, [name_genie_hermione]." ("normal", "closed", "base", "mid")
                    her @ tears mascara "I can do it, I know I can." ("base", "narrow", "worried", "mid_soft")
                "-Tell her she deserves it-":
                    gen "You deserve to be called a slut, a whore and a mudblood... Just look at you." ("angry", xpos="far_left", ypos="head")
                    her @ tears mascara_soft_blink "..." ("scream", "happyCl", "worried", "mid")
                    her @ tears mascara_soft "" ("disgust", "happyCl", "worried", "mid")
                    gen "You walk into my office and sell your body for the sole reason that it will make Gryffindor happy to win the house cup." ("angry", xpos="far_left", ypos="head")
                    her @ tears mascara_soft_blink "..." ("open", "happyCl", "worried", "mid")
                    her @ tears mascara_soft "" ("disgust", "happyCl", "worried", "mid")
                    gen "Bending over onto my desk and let yourself be taken like a some common harlot..." ("angry", xpos="far_left", ypos="head")
                    her @ tears mascara_soft "I..." ("disgust", "narrow", "worried", "mid_soft")
                    gen "Letting your headmaster thrust himself upon you, and taking my load like your life depended on it..." ("angry", xpos="far_left", ypos="head")
                    her @ tears mascara_soft "..." ("normal", "happyCl", "worried", "mid")
                    her @ tears mascara "" ("normal", "narrow", "worried", "mid_soft")
                    gen "I bet you don't even care about the points anymore..." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "I..." ("normal", "narrow", "worried", "down")
                    her @ tears mascara "" ("normal", "narrow", "annoyed", "up")
                    gen "You are nothing more than a whore..." ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "" ("annoyed", "narrow", "annoyed", "up")
                    gen "{size=+4}{b}MY{/b}{/size} whore!" ("grin", xpos="far_left", ypos="head")
                    her @ tears mascara "" ("disgust", "narrow", "base", "up")
                    gen "And I {b}will{/b} call you however I want!" ("base", xpos="far_left", ypos="head")
                    her @ tears mascara "...." ("angry", "narrow", "base", "up")
    else: #Custom/fallback
        her "That's a bit odd... But sure, you can call me that." ("soft", "squint", "base", "mid")

    $ name_hermione_genie = temp_name
    jump hermione_talk

label hermione_change_fail:
    if temp_name == "Girl":
        her "I would prefer if we kept using our formal names and titles, [name_genie_hermione]." ("open", "closed", "base", "mid")
        her "" ("normal", "base", "base", "mid")
    elif temp_name == "Nerd":
        her "I would prefer if you didn't, [name_genie_hermione]." ("open", "closed", "angry", "mid")
        her "{size=-4}And I'm not a nerd...{/size}" ("annoyed", "base", "worried", "mid")
        if states.her.level >= 1:
            her "(I think...)" ("annoyed", "base", "worried", "R")
    elif temp_name == "Good Girl":
        her "I'm not letting you call me that, [name_genie_hermione]!" ("open", "closed", "angry", "mid")
        if states.her.level >= 3:
            her "(Although it's kinda cute he said that...)" ("base", "base", "base", "R")
    elif temp_name == "Little Girl":
        her "I won't let you call me that, [name_genie_hermione]!" ("open", "closed", "angry", "mid")
        if states.her.level >= 5:
            her "(I hope they'd grow out more...)" ("disgust", "narrow", "worried", "down")
            her "*sigh*" ("annoyed", "closed", "base", "mid")
            her "" ("normal", "base", "base", "R")
    elif temp_name == "Bad Girl":
        her "I am not a [temp_name]!" ("open", "base", "angry", "mid")
        if states.her.level >= 7:
            her "(Or am I...?)" ("disgust", "base", "base", "R")
            her "" ("normal", "base", "base", "R")
    elif temp_name == "Princess":
        her "This is inappropriate, [name_genie_hermione]!" ("open", "base", "angry", "mid")
        if states.her.level >= 9:
            her "(It sounds nice though...)" ("base", "base", "base", "R")
    elif temp_name == "Pet":
        her "Are you joking, [name_genie_hermione]?" ("open", "base", "worried", "mid")
        if states.her.level >= 11:
            her "(Why would he even suggest that?)" ("annoyed", "base", "base", "R")
    else:
        her "I won't let you call me that!" ("shock", "closed", "angry", "mid")
        her "" ("normal", "base", "angry", "mid")
    jump hermione_talk
