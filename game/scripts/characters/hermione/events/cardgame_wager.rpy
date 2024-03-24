label hg_wager_bj:
    gen "Well, if you want to avoid losing the points, you could come over here and get on your knees." ("grin", xpos="far_left", ypos="head")
    gen "And put my dick in your mouth!" ("grin", xpos="far_left", ypos="head")
    if not states.her.status.blowjob: #Hasn't sucked genie off.
        her "I don't want to lose those points, but that is asking way too much!" ("angry", "base", "angry", "mid")
        her "Isn't there anything else I could do?" ("open", "base", "base", "mid")
        gen "You're no fun!" ("angry", xpos="far_left", ypos="head")
        gen "In that chase, come over here and let me give your butt a squeeze, then I'll only deduct ten points from Gryffindor." ("grin", xpos="far_left", ypos="head")
        if states.her.tier < 3:
            her "No! what kind of girl do you take me for, [name_genie_hermione]!" ("scream", "base", "angry", "mid")
            gen "Fine... Twenty points, deducted from Gryffindor!" ("base", xpos="far_left", ypos="head")
            her "*Hmph*!" ("angry", "base", "angry", "mid")
            $ gryffindor -= 20
            pause.5
            call her_chibi("leave","door","base")
        else:
            her @ cheeks blush "Okay, I can do that..." ("open", "base", "base", "mid_soft")
            her "" ("base", "base", "base", "mid_soft")
            gen "Well then... Get over here!" ("grin", xpos="far_left", ypos="head")
            call her_walk("desk", "base", reduce=0.8)
            call blkfade
            her "Should I turn around, [name_genie_hermione]?" ("open", "happyCl", "worried", "mid")
            her "" ("upset", "base", "worried", "mid")
            gen "No, not this time." ("base", xpos="far_left", ypos="head")
            her "Okay then..." ("annoyed", "narrow", "base", "R_soft")
            call gen_chibi("hide")
            call her_chibi_scene("behind_desk_front")
            with d1

            call hide_blkfade
            call ctc
            call her_chibi_scene("grope_ass_front")
            with d1
            gen "Have you been working out, [name_hermione_genie]? This feels great!" ("base", xpos="far_left", ypos="head")
            her "Can we just get this over with?" ("annoyed", "narrow", "base", "mid_soft")
            her "{size=-5}All this, because of a stupid card game...{/size}" ("upset", "happyCl", "worried", "mid")
            gen "I know, we should definitely do this again." ("base", xpos="far_left", ypos="head")

            if states.her.status.stripping: #(snape has previously walked in, during stripping event)
                play music "music/Dark Fog.ogg" fadein 1 if_changed
                $ hermione_chibi.zorder = 2 #Under snape

                call sna_walk(action="enter", xpos="mid", ypos="base")

                sna "Hello Geni--" (face="snape_09")
                sna "What do we have here?!?" (face="snape_20")
                her "{size=+5}Professor Snape?!{/size}" ("shock", "wide", "worried", "shocked", xpos="left",ypos="base")
                her "It's not what it looks like!" ("scream", "wide", "base", "R")
                hide hermione_main
                sna "So you're not letting your headmaster feel you up?" (face="snape_05")
                sna "And thoroughly enjoying it... By the looks of it!" (face="snape_02")
                her @ cheeks blush "I knew playing another round of cards wasn't a good idea..." ("mad", "happyCl", "worried", "mid")
                her @ cheeks blush "..." ("annoyed", "narrow", "annoyed", "mid")
                her @ cheeks blush "Take your hands off me, now!!" ("scream", "closed", "angry", "mid")
                gen "Fine... Calm down, Miss Granger." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Don't tell me to calm down!!!" ("scream", "base", "angry", "mid")
                hide hermione_main
                sna "Don't feel as if you have to stop on my behalf." (face="snape_01")
                gen "Fine, I'll stop..." ("base", xpos="far_left", ypos="head")

                call her_chibi_scene("behind_desk_front")
                nar "You take your hands off Hermione."

                show screen blkfade
                with d5
                call gen_chibi("sit_behind_desk")
                call her_chibi("stand",410,"base", flip=True)
                hide screen blkfade
                with d5

                sna "Little Miss perfect... Letting her headmaster feel her up over a card game and some house points!" (face="snape_02")
                sna "How sweet..." (face="snape_03")
                her "May I leave now?" ("annoyed", "narrow", "worried", "down", flip=True)
                gen "You are excused, Miss Granger... But I will be taking twenty points from Gryffindor." ("base", xpos="far_left", ypos="head")
                $ gryffindor -= 20

                call her_walk(action="leave")

                sna "How did you talk her into that?" (face="snape_02")
                gen "We made a bet involving house points, and she lost... Why did you have to barge your way in like that?" ("base", xpos="far_left", ypos="head")
                gen "It was just getting good!" ("base", xpos="far_left", ypos="head")
                sna "You should hang a tie on the door or something!" (face="snape_03")
                sna "How was I supposed to know you were busy with the girl?" (face="snape_04")
                gen "Just knock next time!" ("angry", xpos="far_left", ypos="head")
                gen "Can't a mythical creature feel up a schoolgirl in peace around here?" ("angry", xpos="far_left", ypos="head")
                sna "Fine, I'll leave you to it... The less I have to see that girl, the better..." (face="snape_06")

                $ hermione_chibi.zorder = 3 #reset to default
                call sna_walk(action="leave")

            else : #If Snape hasn't walked in during stripping.
                her "Doing it to gain house points is one thing... But doing it to prevent losing them..." ("clench", "narrow", "angry", "R")
                gen "You don't enjoy it? Even a little?" ("base", xpos="far_left", ypos="head")
                her "I'm just doing this to solve the problem I created..." ("disgust", "narrow", "base", "mid_soft")
                gen "Well, to each their own..." ("base", xpos="far_left", ypos="head")
                her "Are you done yet?" ("disgust", "narrow", "base", "R_soft")
                gen "Fine, I'll let you go..." ("base", xpos="far_left", ypos="head")
                call her_chibi_scene("behind_desk_front")
                with d1
                gen "I'll only deduct ten points from Gryffindor, as we agreed." ("base", xpos="far_left", ypos="head")
                gen "Ten points deducted from Gryffindor!" ("base", xpos="far_left", ypos="head")
                $ gryffindor -= 10
                call blkfade
                call her_chibi("stand","mid","base")
                call gen_chibi("sit_behind_desk")
                call hide_blkfade
                her "Thank you, [name_genie_hermione]." ("open", "base", "base", "mid")
                hide hermione_main
                with d3

                call her_walk(action="leave")

    else: #If she's sucked Genie off.
        her "Gryffindor really can't afford to lose twenty points..." ("soft", "base", "worried", "mid")
        her "Okay then, I'll do it." ("open", "closed", "base", "mid")
        her @ cheeks blush "I mean, it's not like I haven't done it before..." ("base", "happy", "base", "mid_soft")
        gen "Get over here then!" ("base", xpos="far_left", ypos="head")

        call her_walk("desk", "base", reduce=0.8)
        call blkfade

        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
        hide hermione_main
        call her_chibi_scene("bj")

        hide screen blkfade
        with fade
        call ctc

        her "*Urk*, *Slurp*, *Gobble*" ("open_wide_tongue", "closed", "base", "mid", ypos="head", flip=False)
        gen "Very good, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "Now, put some work into it." ("angry", xpos="far_left", ypos="head")
        her "*Gulp*, *Gobble*, *Gltch*" ("open_wide_tongue", "narrow", "worried", "mid_soft")
        gen "Your mouth feels amazing, you're a natural!" ("base", xpos="far_left", ypos="head")
        call her_chibi_scene("bj_pause")
        her @ cheeks blush "I'm glad you're enjoying it, [name_genie_hermione]." ("open", "happy", "base", "mid")
        her @ cheeks blush "And for giving me an alternative to not lose those points..." ("open", "happy", "base", "mid")
        call her_chibi_scene("bj")
        her @ cheeks blush "*Gobble*, *Slurp*, *Gobble*" ("open_wide_tongue", "closed", "base", "mid")

        play music "music/Dark Fog.ogg" fadein 1 #Snape walks in if_changed

        call sna_walk(action="enter", xpos="mid", ypos="base")

        sna "" (face="snape_01", xpos="base", ypos="base")
        call ctc

        with hpunch
        sna "I want a rematch!" (face="snape_07")
        call her_chibi_scene("bj_pause")
        gen "{size=-5}Don't stop, [name_hermione_genie]...{/size}" ("base", xpos="far_left", ypos="head")
        gen "What do you mean, rematch? I beat you, fair and square!" ("angry", xpos="far_left", ypos="head")
        call her_chibi_scene("bj")
        her @ cheeks blush "*Slurp*, *Gulp*, *Urk*" ("open_wide_tongue", "happyCl", "worried", "mid", ypos="head", flip=False)
        sna "I'm certain you were cheating... My deck is way more powerful--" (face="snape_06")
        sna "Hold on... What's that noise?" (face="snape_03")
        gen "Probably ghosts...{w} This place must be haunted." ("base", xpos="far_left", ypos="head")
        gen "And why would it matter if your deck is more powerful... I'm better than you, just accept it." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "*Gulp*, *Gobble*, *Gltch*" ("open_wide_tongue", "happyCl", "worried", "mid")
        sna "{size=-5}That doesn't sound like any ghost I've ever heard...{/size}" (face="snape_01")
        sna "Are you sure?" (face="snape_05")
        her "*Slurp*, *Gobble*, *Urk*" ("open_wide_tongue", "happyCl", "worried", "mid")
        sna "There it is again!" (face="snape_25")
        gen "Yes, definitely ghosts..." ("base", xpos="far_left", ypos="head")
        gen "Are you changing the subject because you can't accept the fact I beat you at wizard cards?!" ("grin", xpos="far_left", ypos="head")
        gen "{size=-5}Get ready, [name_hermione_genie]!{/size}" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "*Gurk*, *Gulp*, *Gulp*" ("open_wide_tongue", "base", "worried", "mid")
        sna "Something is going on here... What are you doing?" (face="snape_07")
        gen "... Just standing at my desk." ("base", xpos="far_left", ypos="head")
        hide snape_main
        menu:
            gen "..." ("base", xpos="far_left", ypos="head")
            "-Tell him not to worry about it-":
                $ states.her.status.gokkun = True
                gen "There's nothing suspicious happening--{w=0.2} {size=-5}Ugh!{/size}" ("angry", xpos="far_left", ypos="head")
                pause.5
                call her_chibi_scene("bj_cum_in")
                call cum_block
                gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
                her "..." ("full", "wide", "worried", "stare")
                sna "..." (face="snape_25")
                gen "..." ("angry", xpos="far_left", ypos="head")
                sna "*Hmm*...{w=0.4} It appears that the weird noise has subsided..." (face="snape_04")
                gen "*Err*... Yes... Seems like it." ("base", xpos="far_left", ypos="head")
                sna "I bet it was Peeves again... He's been acting out a lot more than usual..." (face="snape_16")
                sna "I should probably try and find the bastard before he starts wreaking havoc elsewhere..." (face="snape_03")
                sna "Until next time..." (face="snape_03")
                her @ cheeks blush "..." ("full_cum", "narrow", "base", "down")

                call sna_walk("door", "base") #snape walks to the door, pauses on gulp sound

                play sound "sounds/gulp.ogg"
                her "{heart}*Gulp* {heart}" ("cum", "narrow", "annoyed", "up")
                sna "..." (face="snape_07", flip=True)
                pause.2

                show screen blkfade
                with d5
                play sound "sounds/07_run.ogg" #snape runs back and draws his wand
                hide snape_main
                $ snape_chibi.zorder = states.desk_chibi_zorder + 1
                call sna_chibi("wand_defend", "mid")
                pause 1
                hide screen blkfade
                with d5

                play music "music/Hitman.ogg" if_changed
                pause .6
                call her_chibi_scene("bj_pause")

                gen "...?!" ("angry", xpos="far_left", ypos="head")
                sna "Reveal yourself! I won't let you harm him!" (face="snape_10", wand=True, flip=False)
                gen "Severus, wait!" ("angry", xpos="far_left", ypos="head")
                sna "I knew something was wrong from the start! You can't hide from me! Now reveal yourself, or prepare to die!" (face="snape_30", wand=True)
                if not states.her.status.stripping: # Snape hasn't walked in on Hermione stripping.
                    gen "What are you doing, Severus?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "..." ("soft", "base", "worried", "mid")
                    gen "You're acting very strange..." ("base", xpos="far_left", ypos="head")
                    gen "I never knew you cared so much about my well-being..." ("grin", xpos="far_left", ypos="head")
                    sna "But... I swear I heard something..." (face="snape_14", wand=True)
                    gen "..." ("angry", xpos="far_left", ypos="head")
                    sna "I guess I must've imagined it... I'll just go then." (face="snape_14", wand=True)
                    call sna_chibi("stand","mid","base",flip=True) #snape turns and leaves
                    hide screen bld1
                    with d3
                    stop music fadeout 2

                else: # Snape has walked in on Hermione stripping.
                    gen "Wait!" ("angry", xpos="far_left", ypos="head")

                    show screen blkfade
                    with d3
                    call gen_chibi("dick_out", 260, 205+250)
                    call her_chibi("stand",220,"base", flip=True)
                    call sna_chibi("stand",460,"base")
                    stop music fadeout 2
                    sna "" (face="snape_14", wand=False)
                    hide screen blkfade
                    with d5

                    sna "Miss Granger?! But, I thought--{w=0.2} I..." (face="snape_14")
                    hide snape_main
                    play music "music/Dark Fog.ogg" if_changed
                    if states.her.level > 21:
                        her "Hello, Professor Snape." ("cum", "base", "base", "mid", xpos="left", ypos="base", flip=True)
                        her "I was just helping the headmaster with an \"itch\"." ("soft", "base", "base", "mid_soft", flip=True)
                        sna "I see... I was expecting a poor excuse, but your honesty is admirable..." (face="snape_02")
                        her @ cheeks blush "..." ("base", "base", "base", "mid_soft", flip=True)
                        sna "Well, in that case, I hope you don't mind giving me a scratch--" (face="snape_13")
                    else: #whoring of 21 or less
                        her @ cheeks blush "Oh, hello there Professor..." ("cum", "base", "worried", "mid", xpos="left", ypos="base", flip=True)
                        her @ cheeks blush "I was just helping the headmaster with some cleaning under his desk." ("open", "happyCl", "worried", "mid")
                        random:
                            sna "Sure... And I live a double life as a death eater..." (face="snape_02")
                            sna "Sure... And I'm the sheriff of Nottingham..." (face="snape_02")
                            sna "Sure... And my name is {i}Hans Gruber{/i}..." (face="snape_02")
                    gen "I believe that your work is done, Miss Granger... I'll refrain from deducting those points..." ("base", xpos="far_left", ypos="head")
                    sna "Avoiding house point deductions, are we? Is it that simple to get inside your panties, Miss Granger?" (face="snape_01")
                    sna "If I had known..." (face="snape_20")
                    her "In your dreams!" ("mad", "narrow", "annoyed", "mid")
                    sna "In any case... You're a lucky man... Albus." (face="snape_13")
                    sna "I'll leave you two to it..." (face="snape_02")

                    hide screen bld1
                    with d3

                pause.2

                call sna_walk(action="leave")
                $ snape_chibi.zorder = 3

                pause.2
                gen "Well, that was something..." ("base", xpos="far_left", ypos="head")

                if states.her.level < 22: #if she has lower whoring than 22
                    her "That was mortifying!" ("angry", "closed", "angry", "mid")
                    her "How could you make me keep going?!?" ("angry", "base", "angry", "mid")
                    gen "Well, you were down there already... So, why shouldn't you finish the job?" ("base", xpos="far_left", ypos="head")
                    her "I can't believe you..." ("angry", "closed", "angry", "mid")
                    her "I'm going now... Don't expect me to do anything for you any time soon!" ("clench", "base", "angry", "mid")
                    call gen_chibi("sit_behind_desk")
                    $ states.her.mood += 10
                else: # 22+
                    her @ cheeks blush "The old me would have been embarrassed by that..." ("clench", "narrow", "worried", "mid_soft")
                    her @ cheeks blush "But I must say... It was kind of exciting..." ("grin", "happy", "base", "mid_soft")
                    gen "You bet it was." ("grin", xpos="far_left", ypos="head")
                    her "I can't believe that just happened!" ("smile", "base", "base", "mid_soft")
                    gen "You did a great job [name_hermione_genie]... I'll try even harder to win next time!" ("base", xpos="far_left", ypos="head")
                    her "Thank you, [name_genie_hermione]... Anyway, I must be going..." ("open", "base", "base", "mid")

                    show screen blkfade
                    with d3
                    call her_chibi("stand","mid","base")
                    call gen_chibi("sit_behind_desk")
                    hide hermione_main
                    hide screen blkfade
                    with d5

                    if game.daytime:
                        her "Bye then..." ("smile", "base", "base", "mid", trans=dissolve, flip=False)
                        gen "Bye, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    else:
                        her "Good night..." ("open", "base", "base", "mid", trans=dissolve, flip=False)
                        gen "Good night, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            "-Tell him the ghost is gone-":
                gen "Hold it..." ("angry", xpos="far_left", ypos="head")
                her "*Glick*?" ("open_wide_tongue", "wide", "base", "R")
                gen "No, I think I should be able to exorcise these spirits myself..." ("base", xpos="far_left", ypos="head")
                sna "You can do that?" (face="snape_11")
                if states.her.level > 21:
                    her @ cheeks blush "*Slurp*, *Slurp*, *Gobble*" ("open_wide_tongue", "narrow", "annoyed", "up")
                    gen "*Ghh*, of--{w=0.3} of course I can..." ("angry", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Gltch*, *Slurp*, *Gobble*" ("open_wide_tongue", "squint", "worried", "up")
                    gen "I've exercised--" ("angry", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Gulp*, *Gulp*, *Gobble*" ("open_wide_tongue", "squint", "worried", "up")
                    gen "*ARGH*...{w=0.4} Plenty!" ("angry", xpos="far_left", ypos="head")
                    sna "Are you..." ("snape_05")
                    menu:
                        "-Try to get him to Leave-":
                            $ states.her.status.gokkun = True
                            gen "Fine? Yes, I just need some concentration...{w=0.4} It'd be easier if you left me to it, as the final expulsion could become quite messy..." ("angry", xpos="far_left", ypos="head")
                            her @ cheeks blush "...?" ("open_wide_tongue", "narrow", "base", "up")
                            sna "Truly? Now, I'd love to see that..." ("snape_02")
                            gen "No...{w=0.4} *Gngh*...{w=0.2} Trust me...{w=0.4} You don't...{w=0.4} Now, if you could just give me some--" ("angry", xpos="far_left", ypos="head")
                            sna "Fine... But you're going to have to teach me how to do that some other time..." ("snape_01")
                            gen "Well, I'm not sure if that's such a--" ("angry", xpos="far_left", ypos="head")
                            her "*Slurp*, *Slurp*, *Gobble*" ("open_wide_tongue", "squint", "worried", "up")
                            gen "Oh, Holy Spirit that resides in this place!" ("angry", xpos="far_left", ypos="head")
                            her @ cheeks blush "*Slurp*, *Slurp*, *Urk*" ("open_wide_tongue", "squint", "worried", "up")
                            gen "Please help me release this anguish--{w=0.4} I mean... Allow me to release you from this anguish." ("angry", xpos="far_left", ypos="head")
                            sna "Well, you seem to know what you're doing... I'll leave you to it." ("snape_05")
                            hide screen bld1
                            with d3
                            pause.2

                            call sna_walk(action="leave")

                            gen "{size=-5}And not a moment too soon...{w=0.4} Take this, you whore!{/size}" ("angry", xpos="far_left", ypos="head")
                            call her_chibi_scene("bj_cum_in")

                            call cum_block
                            pause 1
                            call her_chibi_scene("bj_pause")

                            her @ cheeks blush "*Mmmh*!!" ("full_cum", "wide", "base", "stare")

                            play sound "sounds/gulp.ogg"
                            her "*Gulp*!" ("cum", "happyCl", "worried", "mid")
                            her "*Gua-ha*..." ("open_wide_tongue", "narrow", "base", "stare")

                            gen "Who said you could continue sucking? Because it wasn't me." ("base", xpos="far_left", ypos="head")
                            her "You asked me to give you a blowjob, did you not?" ("soft", "base", "base", "mid_soft")
                            gen "..." ("base", xpos="far_left", ypos="head")
                            gen "Fine... I suppose I did... I won't deduct those points." ("base", xpos="far_left", ypos="head")
                            her "Thank you, [name_genie_hermione]..." ("smile", "base", "base", "mid")

                            call blkfade
                            call her_chibi("stand","mid","base")
                            call gen_chibi("sit_behind_desk")

                            nar "Hermione gets up, and walks to the front of your desk."

                            hide screen blkfade
                            with d5
                            call ctc

                            her "Alright then, if that's everything, then I better head off." ("smile", "happy", "base", "mid", ypos="base")
                            gen "..." ("base", xpos="far_left", ypos="head")
                            her "[name_genie_hermione]?" ("soft", "happy", "base", "mid", ypos="base")
                            gen "*Huh*? Oh, yes... You may leave, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                            her "Thank you..." ("base", "happy", "base", "mid", ypos="base")

                            call her_chibi("leave","door","base")

                            gen "That girl..." ("grin", xpos="far_left", ypos="head")
                        "-Let her keep going, and deal with any aftermaths-":
                            $ states.her.status.gokkun = True
                            gen "Yeah... I'm good." ("base", xpos="far_left", ypos="head")
                            her "*Slurp*, *Slurp*, *Gobble*" ("open_wide_tongue", "squint", "worried", "up")
                            sna "Is there anything I could assist you with?" ("snape_04")
                            with hpunch
                            gen "{size=+7}What?!?{/size}" ("angry", xpos="far_left", ypos="head")
                            her @ cheeks blush "...?" ("open_wide_tongue", "wide", "worried", "stare")
                            sna "With the exorcism..." (face="snape_05")
                            gen "Oh..." ("base", xpos="far_left", ypos="head")
                            her @ cheeks blush "*Slurp*, *Slurp*, *Slurp*" ("open_wide_tongue", "happyCl", "worried", "mid")
                            gen "No... It's all good... I can feel the ghostly presence being expelled as we speak..." ("base", xpos="far_left", ypos="head")
                            gen "Now take this, you whore!" ("angry", xpos="far_left", ypos="head")
                            call her_chibi_scene("bj_cum_in")
                            call cum_block
                            gen "..." ("angry", xpos="far_left", ypos="head")
                            sna "..." (face="snape_14")
                            her "........" ("full_cum", "narrow", "base", "dead")
                            play sound "sounds/gulp.ogg"
                            her "*Gulp*!" ("cum", "happyCl", "worried", "mid")
                            gen "..." ("base", xpos="far_left", ypos="head")
                            sna "I had no clue exorcism would be this..." (face="snape_03")
                            sna "Extreme..." ("snape_02")
                            gen "*Hah*, yeah...{w=0.3} But I've done this plenty of times..." ("grin", xpos="far_left", ypos="head")
                            gen "Actually... There's quite a bit of ghostly residue I have to deal with, so it might be best--" ("base", xpos="far_left", ypos="head")
                            sna "Whatever... I'd just leave it to the house elves..." ("snape_03")
                            gen "It's not as simple as it may seem... Warm water isn't going to cut it..." ("base", xpos="far_left", ypos="head")
                            sna "Fine, I'll see you some other time, in that case." ("snape_01")
                            hide screen bld1 #should go black
                            with d3
                            pause.2

                            call sna_walk(action="leave")

                            gen "He's gone now, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                            call her_chibi_scene("bj_pause")
                            her "I have disposed of the ghostly residue, [name_genie_hermione]..." ("open", "narrow", "worried", "mid_soft")
                            gen "I can't believe he bought it..." ("base", xpos="far_left", ypos="head")
                            her "What do you expect from the head of Slytherin?" ("crooked_smile", "narrow", "base", "R_soft")
                            gen "Well...{w=0.3} I think that's enough excitement for today." ("base", xpos="far_left", ypos="head")

                            call blkfade
                            call her_chibi("stand","mid","base")
                            call gen_chibi("sit_behind_desk")

                            nar "Hermione gets up, and walks to the front of your desk."

                            hide screen blkfade
                            with d5
                            call ctc

                            her "" ("base", "happy", "base", "mid_soft", ypos="base")
                            gen "You've done more than enough to save those points." ("base", xpos="far_left", ypos="head")
                            her "Thank you, [name_genie_hermione]." ("smile", "happy", "base", "mid_soft")
                            if game.daytime: #should play if day time
                                her "Bye then..." ("open", "base", "base", "mid")
                                gen "Bye, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                            else:
                                her "Good night." ("open", "base", "base", "mid")
                                gen "Good night, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                        "-Try something crazy- {image=interface/icons/small/cards.webp}":
                            gen "Oh yes, I'm--{w=0.2} *Ugh*...{w=0.3} fine..." ("base", xpos="far_left", ypos="head")
                            gen "But for some reason... I feel like playing some cards." ("base", xpos="far_left", ypos="head")
                            sna "During a moment like this?" (face="snape_02")
                            gen "Yes, I think the ghost may have been a gambler during their lifetime..." ("base", xpos="far_left", ypos="head")
                            jump bj_duel_game
                else: #whoring not higher than 21.
                    call her_chibi_scene("bj_pause")
                    her "*Mmphaa*..." ("open_tongue", "narrow", "annoyed", "up")
                    gen "Hold on...{w} Yes, I believe the ghostly presence has departed..." ("base", xpos="far_left", ypos="head")
                    sna "Already?" (face="snape_05")
                    gen "Yes, they must've felt how powerful my exorcism abilities were, and moved on somewhere else..." ("angry", xpos="far_left", ypos="head")
                    sna "Well, that's no fun... I was hoping to see it happen for myself." (face="snape_03")
                    gen "Trust me, there's not going to be any watching going on here..." ("base", xpos="far_left", ypos="head")
                    sna "..." (face="snape_05")
                    sna "Anyway... The reason I am here, was to see if you were up for another round of cards..." (face="snape_01")
                    sna "But I suppose you're looking quite spent, after that whole ordeal." (face="snape_02")
                    menu:
                        "\"*Hmm*... Actually...\" {image=interface/icons/small/cards.webp}":
                            gen "I don't see why not... I don't have anything else going on at the moment..." ("grin", xpos="far_left", ypos="head")
                            label bj_duel_game:
                            her "..." ("open_wide_tongue", "narrow", "annoyed", "mid")
                            call her_chibi_scene("bj")
                            her "*Slurp*, *Slurp*, *Gobble*" ("open_wide_tongue", "narrow", "annoyed", "mid")
                            gen "*Gngh*..." ("angry", xpos="far_left", ypos="head")
                            sna "In that case, let's begin..." (face="snape_02")
                            # Gamestart
                            call snape_special_duel
                            # After game
                            $ states.her.status.gokkun = True
                            call her_chibi_scene("bj_cum_in")
                            call cum_block
                            pause 3
                            if duel_response == "draw":
                                gen "I'm spent..." ("base", xpos="far_left", ypos="head")
                                sna "So, no rematch?" (face="snape_05")
                                gen "Yes, definitely not..." ("base", xpos="far_left", ypos="head")
                                gen "I'm not sure I could handle another one of those for at least thirty minutes..." ("base", xpos="far_left", ypos="head")
                                sna "That's oddly specific..." (face="snape_04")
                                gen "You're oddly specific..." ("base", xpos="far_left", ypos="head")
                                sna "..." (face="snape_03")
                                gen "I don't know what that means..." ("base", xpos="far_left", ypos="head")
                                sna "I feel as if my understanding of you is diminishing by the day...." (face="snape_01")

                                call sna_walk(action="leave")

                                call her_chibi_scene("bj_pause")
                                her "So, no rematch then?" ("crooked_smile", "narrow", "base", "mid_soft")
                                gen "Why would you start sucking again, like that?" ("base", xpos="far_left", ypos="head")
                                her "Why would you suddenly start playing cards, when I'm being so kind as to give you a blowjob?" ("annoyed", "narrow", "base", "mid_soft")
                                gen "That's fair..." ("base", xpos="far_left", ypos="head")
                                gen "Very well, as promised, I won't be deducting those points..." ("base", xpos="far_left", ypos="head")
                                if game.daytime:
                                    her "Great... Goodbye for now then, [name_genie_hermione]." ("base", "base", "base", "mid")
                                else:
                                    her "Great... Good night then, [name_genie_hermione]." ("base", "base", "base", "mid")
                                gen "{size=-8}That girl is crazy...{/size}" ("base", xpos="far_left", ypos="head")
                            elif duel_response == "loss" or duel_response == "Close":
                                sna "Yes! I knew I'd make you bust this time!" (face="snape_02")
                                gen "Trust me..." ("base", xpos="far_left", ypos="head")
                                gen "You did not \"make me bust\"." ("base", xpos="far_left", ypos="head")
                                sna "Sure I didn't...{w=0.4} So, how about you hand me a bottle of that fine wine to celebrate the occasion..." (face="snape_20")
                                label bj_duel_game_menu:
                                menu:
                                    "-Give him the bottle-" (style="disabled") if wine_ITEM.owned <= 0:
                                        nar "You don't have any bottles of wine left."
                                        jump bj_duel_game_menu
                                    "-Give him the bottle-" if wine_ITEM.owned > 0:
                                        $ wine_ITEM.owned -= 1
                                        gen "Fine..." ("angry", xpos="far_left", ypos="head")
                                        gen "I feel like I won in the end anyway..." ("grin", xpos="far_left", ypos="head")
                                        sna "That literally makes no sense..." (face="snape_04")
                                        sna "You clearly can't overcome the dreading feeling of such an explosive victory..." (face="snape_02")
                                        gen "Sure... Something like that..." ("base", xpos="far_left", ypos="head")
                                        gen "Just take the wine and leave..." ("base", xpos="far_left", ypos="head")
                                        gen "I need to reflect on my previous life decisions." ("base", xpos="far_left", ypos="head")

                                        call sna_walk(action="leave")

                                        gen "Get out of there... life decisions." ("base", xpos="far_left", ypos="head")
                                        call her_chibi_scene("bj_pause")
                                        her @ cheeks blush "Happy?" ("normal", "happyCl", "base", "mid")
                                        gen "I just lost the game and one of my bottles of wine..." ("base", xpos="far_left", ypos="head")
                                        her @ cheeks blush "And an above-average amount of two to five millilitres of ejaculate, by the looks of it..." ("open", "narrow", "worried", "down")
                                        gen "That is true..." ("grin", xpos="far_left", ypos="head")
                                        her @ cheeks blush "Are you still deducting those points, [name_genie_hermione]?" ("normal", "narrow", "base", "down")
                                    "-Don't give him anything-":
                                        gen "Get out..." ("base", xpos="far_left", ypos="head")
                                        sna "Someone's a sore loser..." (face="snape_13")
                                        gen "Aching..." ("base", xpos="far_left", ypos="head")
                                        gen "Now get out..." ("base", xpos="far_left", ypos="head")
                                        if states.sna.level >= 30:
                                            sna "Fine... But next time I'm playing you for one of those bottles..." (face="snape_03")
                                        else:
                                            sna "Fine..." (face="snape_03")

                                        call sna_walk(action="leave")

                                        call her_chibi_scene("bj_pause")
                                        her @ cheeks blush "Happy?" ("normal", "happyCl", "base", "mid")
                                        gen "What are you talking about? How could I be happy during a moment like this?" ("angry", xpos="far_left", ypos="head")
                                        her @ cheeks blush "But I just made you.--" ("open", "base", "worried", "mid")
                                        gen "I just lost that god-damn game because you made it impossible for me to concentrate!" ("angry", xpos="far_left", ypos="head")
                                        her @ cheeks blush "I just did what you asked of me!" ("mad", "narrow", "angry", "R")
                                        her @ cheeks blush "So I'd very much appreciate it if you could do your end of the bargain, and not deduct those points!" ("open", "closed", "angry", "mid")
                                menu:
                                    "-Only deduct the twenty points-":
                                        gen "You should be happy that I'm not deducting more!" ("angry", xpos="far_left", ypos="head")
                                        gen "Twenty points deduced from Gryffindor!" ("angry", xpos="far_left", ypos="head")
                                        $ gryffindor -= 20
                                        her "..." ("disgust", "base", "angry", "mid")
                                        her "Whatever..." ("open", "closed", "angry", "mid")
                                        $ states.her.mood += 15
                                    "-Deduct even more-":
                                        gen "Oh, don't you worry..." ("base", xpos="far_left", ypos="head")
                                        her "..."
                                        gen "Forty points deducted from Gryffindor!" ("angry", xpos="far_left", ypos="head")
                                        $ gryffindor -= 40
                                        her "What?! You can't do that!" ("shock", "wide", "worried", "stare")
                                        gen "Of course I can, I'm the headmaster!" ("angry", xpos="far_left", ypos="head")
                                        her "I can't believe you've done this..." ("mad", "base", "angry", "mid")
                                        gen "Suck it up..." ("base", xpos="far_left", ypos="head")
                                        her @ cheeks blush "{size=-5}That's what I did...{/size}" ("open", "narrow", "annoyed", "mid")
                                        gen "Excuse me?" ("base", xpos="far_left", ypos="head")
                                        her "Never mind..." ("clench", "narrow", "angry", "R")
                                        $ states.her.mood += 25
                                    "-Let her go-":
                                        gen "No, I feel like I've somehow reached a net gain during this whole exchange..." ("base", xpos="far_left", ypos="head")
                                        her "..." ("normal", "base", "base", "mid")
                                        gen "A net gain is when--" ("base", xpos="far_left", ypos="head")
                                        her "I know what it means..." ("open", "narrow", "base", "mid_soft")
                                        gen "Right." ("base", xpos="far_left", ypos="head")
                                        if game.daytime:
                                            her "good day to you then, [name_genie_hermione]." ("base", "base", "base", "mid")
                                        else:
                                            her "Good night then..." ("base", "base", "base", "mid")
                            else: #Win
                                sna "..." (face="snape_18")
                                gen "Did I say that aloud?" ("angry", xpos="far_left", ypos="head")
                                sna "Yes..." (face="snape_12")
                                gen "I meant to say bore..." ("base", xpos="far_left", ypos="head")
                                gen "Take that..." ("base", xpos="far_left", ypos="head")
                                sna "..." (face="snape_05")
                                gen "You bore..." ("base", xpos="far_left", ypos="head")
                                sna "..." (face="snape_05")
                                sna "What kind of trash talk is that... Seriously... You need to step up your game." (face="snape_06")
                                gen "No you..." ("base", xpos="far_left", ypos="head")
                                sna "That's fair..." (face="snape_03")
                                sna "I'll take my leave in that case..." (face="snape_01")

                                call sna_walk(action="leave")

                                call her_chibi_scene("bj_pause")
                                her "Did you just call me a...{nw}"
                                gen "Snape..." ("base", xpos="far_left", ypos="head")
                                # Easter egg start
                                $ tried_rollback = False
                                show screen rollback_check
                                $ renpy.block_rollback()
                                gen "If you {w=0.25}{b}{u}{i}scrolled back{/i}{/u}{/b}{w=0.25}, then you'd clearly see I was referring to Snape..." ("base", xpos="far_left", ypos="head") ####
                                #***Goes back to reality***
                                label hg_wager_bj_secret_end:
                                if not tried_rollback:
                                    hide screen rollback_check
                                    $ renpy.block_rollback()
                                    her "If I do what back?" ("annoyed", "narrow", "base", "mid_soft")
                                    gen "Never mind..." ("base", xpos="far_left", ypos="head")
                                else:
                                    $ achievements.unlock("flashback")
                                    her "........" ("annoyed", "narrow", "worried", "down")
                                gen "Right then... I believe we're done for today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                                her "What about the points..." ("annoyed", "narrow", "worried", "down")
                                gen "Points?" ("angry", xpos="far_left", ypos="head")
                                gen "Oh yes, the points!" ("grin", xpos="far_left", ypos="head")
                                gen "Twenty points to Gryffindor!" ("grin", xpos="far_left", ypos="head")
                                $ gryffindor += 20
                                her "That's not--" ("normal", "narrow", "base", "down")
                                her "Thank you, [name_genie_hermione]..." ("open", "closed", "base", "mid")
                                if game.daytime:
                                    her "Goodbye then..." ("base", "base", "base", "mid")
                                else:
                                    her "Good night then..." ("base", "base", "base", "mid")

                            call blkfade
                            call her_chibi("stand","mid","base")
                            call gen_chibi("sit_behind_desk")
                            hide screen blkfade
                            jump end_hermione_event
                        "\"I'll pass\"":
                            pass
                    #
                    #
                    gen "Yes, I think I better spend some time, re-evaluating why went down this path..." ("base", xpos="far_left", ypos="head")
                    sna "..." (face="snape_05")
                    sna "I'll just go then." (face="snape_01")
                    hide screen bld1
                    with d3
                    pause.2

                    call sna_walk(action="leave")

                    gen "..." ("base", xpos="far_left", ypos="head")
                    gen "... Why did you stop?" ("angry", xpos="far_left", ypos="head")
                    her "What?" ("annoyed", "narrow", "annoyed", "mid")
                    her "I thought you wanted me to..." ("clench", "narrow", "worried", "down")
                    gen "If I wanted you to stop, then I would've said so..." ("base", xpos="far_left", ypos="head")
                    her "I could resume, if you want me to..." ("soft", "base", "base", "mid_soft")
                    gen "No... The mood is already ruined..." ("base", xpos="far_left", ypos="head")
                    her "Are you still deducting those points?" ("open", "base", "base", "mid")
                    menu:
                        "-Don't deduct the points-":
                            gen "No, [name_hermione_genie]... You're excused." ("base", xpos="far_left", ypos="head")
                            her "Thank you professor..." ("smile", "happy", "base", "mid_soft")
                        "-Deduct the points-":
                            gen "Of course I am! You didn't finish the job!" ("angry", xpos="far_left", ypos="head")
                            her "..." ("annoyed", "wide", "base", "stare")
                            her "But, Snape was going to--" ("open", "happyCl", "worried", "mid")
                            her "..." ("upset", "narrow", "worried", "down")
                            her "Fine..." ("clench", "narrow", "annoyed", "mid")
                            gen "Twenty points deducted from Gryffindor!" ("base", xpos="far_left", ypos="head")
                            $ gryffindor -= 20
                            $ states.her.mood += 10

        $ states.her.status.blowjob = True
        $ achievements.unlock("headlib")
    call blkfade
    call her_chibi("stand","mid","base")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade

    jump end_hermione_event

label hg_wager_bj_secret:
    hide screen rollback_check
    hide hermione_main
    call blkfade
    $ renpy.block_rollback()
    call her_chibi_scene("bj")
    call sna_chibi("stand",460,"base")
    pause 1.0
    show screen hg_wager_bj_secret
    call hide_blkfade
    $ renpy.block_rollback()
    gen "Yeeeeees!{w=0.5}{nw}" ("grin", xpos="far_left", ypos="head")
    call cum_block
    gen "Go fuck yourself Snape, take that, you fucking whore!" ("angry", xpos="far_left", ypos="head")
    sna "..." (face="snape_11")
    gen "Yeah! What do you have to say about that!? Slut!" ("grin", xpos="far_left", ypos="head")
    sna "..." (face="snape_11")
    gen "Slam dunk!" ("grin", xpos="far_left", ypos="head")
    gen "Another victory in the bag! Eat my shit!" ("grin", xpos="far_left", ypos="head")

    call blkfade
    call her_chibi_scene("bj_pause")
    call sna_chibi("hide")
    hide snape_main
    hide screen hg_wager_bj_secret
    pause 1.0
    call hide_blkfade

    $ renpy.block_rollback()
    gen "And then I totally just shat all over the game board..." ("grin", xpos="far_left", ypos="head")

    jump hg_wager_bj_secret_end

screen hg_wager_bj_secret():
    zorder 4
    add im.MatrixColor("images/rooms/overlays/g_circular.webp", im.matrix.saturation(0.0)*im.matrix.brightness(0.7))

    text "Replay" pos (50, 50) size 40 color "#FFF" outlines [(5, "#000", 0, 0)] at blink

screen rollback_check():
    tag rollback_check
    if not tried_rollback:
        key "rollback" action [SetVariable("tried_rollback", True), Jump("hg_wager_bj_secret")]
