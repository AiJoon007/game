
### Cho Quidditch Tactics ###

label cho_training:

    # Automatic-Events

    # Quiz.
    if not states.cho.ev.quiz.complete:
        jump cho_quiz

    # Training Intro 1.
    # Event fails. Cho will get mad and leaves.
    if not states.cho.ev.quidditch.e1_complete:
        jump cho_quid_E1

    # Training Intro 2.
    if not states.cho.ev.quidditch.e2_complete:
        jump cho_quid_E2

    # Setup

    show screen blkfade
    call hide_characters
    with d5

    $ cho_outfit_last.save()
    $ cho.equip(cho_outfit_quidditch) # Equip quidditch set

    call cho_chibi("stand", "right", "base")

    call gen_chibi("stand", "desk", "base")

    hide screen bld1
    hide screen blkfade
    with d5
    pause .8

    # Menu
    label .choices:

    menu:
        "-Discuss Quidditch Training-":
            if states.cho.tier == 1:
                # Hufflepuff
                jump cc_ht_talk
            elif states.cho.tier == 2:
                # Slytherin
                jump cc_st_talk
            elif states.cho.tier == 3:
                # Gryffindor
                jump cc_gt_talk

            jump cho_training.choices

        "-Discuss Tactics-" if not states.cho.ev.quidditch.lock_tactic:

            if states.cho.tier == 1:
                if not states.cho.ev.talk_to_me.t1_e3_complete:
                    gen "(I don't know enough about the enemy team.)" ("base", xpos="far_left", ypos="head")
                    gen "(I should {b}talk to her{/b} more before proceeding.)" ("base", xpos="far_left", ypos="head")

                    jump .choices

                # Hufflepuff
                # Clothes:  Skirt, Robes
                if not states.cho.ev.quidditch.hufflepuff_stage == "intro_done":
                    $ states.cho.ev.quidditch.hufflepuff_stage = "intro_done"

                    gen "I got it!" ("base", xpos="far_left", ypos="head")
                    cho "Got what?" ("soft", "base", "base", "mid")
                    gen "I know how to get you that win against those Badgers!" ("base", xpos="far_left", ypos="head")
                    cho "Really? How?" ("soft", "base", "raised", "mid")
                    gen "You told me how, yourself." ("base", xpos="far_left", ypos="head")
                    gen "Panties are the key!" ("base", xpos="far_left", ypos="head")
                    cho "Panties? What do panties have to do with Quidditch?" ("soft", "wide", "raised", "mid")
                    gen "Everything, girl!{w} For some they are the meaning of life!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "What are you suggesting exactly?" ("clench", "base", "base", "mid")
                    gen "My plan is that we use Cedric's obsession with panties to distract him during the game." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "I don't really see how that would be--" ("annoyed", "base", "base", "downR")
                    gen "You'll have to wear a skirt of course." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks heavy_blush "A skirt?" ("clench", "wide", "base", "mid") #shocked
                    gen "Of course!" ("grin", xpos="far_left", ypos="head")
                    gen "If he's too focused on your panties, then there's no way he'll catch that snatch!" ("grin", xpos="far_left", ypos="head")
                else:
                    # Repeated intro
                    gen "So about that tactic..." ("base", xpos="far_left", ypos="head")
                    if states.cho.level < 3:
                        # Fail
                        cho "Got a better plan? One that doesn't involve showing off my panties?" ("annoyed", "base", "base", "mid")
                        gen "..." ("base", xpos="far_left", ypos="head")
                        cho "Didn't think so..." ("open", "narrow", "raised", "mid")
                        gen "(Damn... maybe I need to work on her confidence a bit...)" ("base", xpos="far_left", ypos="head")
                        gen "(Some more favours should surely do it...)" ("grin", xpos="far_left", ypos="head")

                        jump cho_training.choices

                if states.cho.level >= 3:
                    $ states.cho.ev.quidditch.lock_practice = False

                    cho @ cheeks blush "..." ("normal", "narrow", "base", "downR")
                    cho @ cheeks blush "You actually think that will work?" ("open", "closed", "angry", "mid")
                    gen "If what you're telling me about him is true then I'm sure of it." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "..." ("clench", "closed", "base", "mid")
                    cho @ cheeks blush "But what if it doesn't?" ("annoyed", "base", "base", "down")
                    cho @ cheeks blush "I need to win the game to make it to the finals!" ("open", "base", "angry", "mid")
                    gen "Then let's put this theory into practice..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "You want me to try it out during next practice against them?" ("upset", "base", "raised", "mid")
                    gen "You do practice matches against the other...{w=0.5} actually, that's a great idea!" ("base", xpos="far_left", ypos="head")
                    gen "That way we'll know it works for sure!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "..." ("disgust", "base", "base", "down")
                    cho @ cheeks blush "Fine, but I'm not changing any of my other clothes, I'd rather not have anyone else staring at my panties..." ("annoyed", "base", "angry", "mid")
                    gen "Okay then..." ("base", xpos="far_left", ypos="head")
                    gen "Get your broom and Quidditch-gear... and put that skirt on!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Alright..." ("annoyed", "base", "base", "mid")

                    #Cho returns with the Hufflepuff clothing combination
                    $ cho.equip(cho_outfit_quidditch_hufflepuff)
                    $ cho_outfit_quidditch.save()
                    cho "Okay then, now what?" ("upset", "base", "base", "R", trans=fade)

                    gen "Now let's try some flying positions..." ("base", xpos="far_left", ypos="head")
                    gen "Get on that broom, [name_cho_genie]." ("base", xpos="far_left", ypos="head")

                    call cho_chibi("fly", "mid", "base")
                    hide cho_main
                    with fade

                    gen "Excellent..." ("base", xpos="far_left", ypos="head")

                    jump cho_tactics
                else:
                    # Fail

                    cho "I will do nothing of the sort!" ("mad", "base", "angry", "mid")
                    gen "Sorry?" ("base", xpos="far_left", ypos="head")
                    cho "You want me to wear a skirt during quidditch?" ("mad", "narrow", "angry", "mid")
                    cho "The whole school will be there!" ("clench", "wide", "base", "mid")
                    gen "Don't focus on them, Cedric is your target!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "But they'll see my panties!" ("mad", "base", "base", "down")
                    cho @ cheeks blush "No, I will not be going through with this plan of yours..." ("open", "base", "angry", "mid")
                    cho @ cheeks blush "You better come up with something else!" ("soft", "base", "angry", "mid")

                    # Cho gets upset and leaves
                    $ states.cho.mood += 6
                    call cho_walk(action="leave")

                    gen "(Damn... maybe I need to work on her confidence a bit...)" ("base", xpos="far_left", ypos="head")
                    gen "(Some more favours should surely do it...)" ("grin", xpos="far_left", ypos="head")

                    $ cho.equip(cho_outfit_last)

                    call gen_chibi("sit_behind_desk")
                    with fade

                    jump end_cho_event

            elif states.cho.tier == 2:
                if not states.cho.ev.talk_to_me.t2_e3_complete:
                    gen "(I don't know enough about the enemy team.)" ("base", xpos="far_left", ypos="head")
                    gen "(I should {b}talk to her{/b} more before proceeding.)" ("base", xpos="far_left", ypos="head")

                    jump .choices

                # Slytherin
                # Clothes: Trousers, Pullover
                if not states.cho.ev.quidditch.slytherin_stage == "intro_done":
                    $ states.cho.ev.quidditch.slytherin_stage = "intro_done"

                    gen "I got it!" ("base", xpos="far_left", ypos="head")
                    gen "I've got the perfect idea on how to beat those snakes!" ("base", xpos="far_left", ypos="head")
                    cho "..." ("normal", "narrow", "raised", "mid")
                    gen "Do we even say \"phrasing\" anymore?" ("base", xpos="far_left", ypos="head")
                    cho "Just tell me your plan." ("open", "narrow", "raised", "mid")
                    gen "It's all about the ass!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "The ass?" ("upset", "base", "raised", "mid") #shocked
                    gen "Yes, you told me how those brutes love a good ass spanking, now that's an ass fetish if I ever heard one!" ("base", xpos="far_left", ypos="head")
                    gen "So this time we'll have those Slytherins get a good view of your ass!" ("base", xpos="far_left", ypos="head")
                else:
                    # Repeated intro
                    gen "So about that tactic..." ("base", xpos="far_left", ypos="head")
                    if states.cho.level < 9:
                        # Fail
                        cho "Got a better plan? One that doesn't involve flaunting my ass to those Slytherins?" ("annoyed", "base", "base", "mid")
                        gen "..." ("base", xpos="far_left", ypos="head")
                        cho "Didn't think so..." ("open", "narrow", "raised", "mid")
                        gen "(Damn...)" ("base", xpos="far_left", ypos="head")
                        gen "(Looks like she isn't confident enough yet...)" ("base", xpos="far_left", ypos="head")
                        gen "(Some more favours should do the trick.)" ("base", xpos="far_left", ypos="head")

                        jump cho_training.choices

                if states.cho.level >= 9 and states.cho.ev.inspect_her_body.T2_E3_complete:
                    $ states.cho.ev.quidditch.lock_practice = False

                    cho "..." ("soft", "base", "raised", "mid")
                    gen "And yes, before you ask, I'm sure this will ensure the win." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Fine..." ("upset", "base", "base", "R")
                    cho @ cheeks blush "I can't believe I'm saying this..." ("soft", "happyCl", "base", "mid")
                    cho @ cheeks blush "I'll flaunt my ass... to those Slytherins." ("clench", "narrow", "base", "mid")
                    gen "Excellent, then let's discuss some tactics..." ("base", xpos="far_left", ypos="head")
                    gen "I'd like you to put on some trousers this time." ("base", xpos="far_left", ypos="head")
                    gen "And get rid of your robes, they'll cover it too much." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks heavy_blush "Get rid of my--" ("open", "wide", "angry", "mid") #Shocked
                    gen "You can put on something else, just something that doesn't cover the goods." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Alright...{w=0.5} give me a minute to fetch my gear..." ("angry", "closed", "base", "mid")

                    #Cho returns with the Slytherin clothing combination
                    $ cho.equip(cho_outfit_quidditch_slytherin)
                    $ cho_outfit_quidditch.save()
                    cho "Okay then, tell me what to do." ("base", "base", "base", "mid", trans=fade)

                    gen "Get on that broom, [name_cho_genie]." ("base", xpos="far_left", ypos="head")

                    call cho_chibi("fly", "mid", "base")
                    hide cho_main
                    with fade

                    gen "Great." ("base", xpos="far_left", ypos="head")

                    jump cho_tactics

                else:
                    # Fail

                    cho "But, they're Slytherins!" ("clench", "base", "angry", "mid")
                    gen "And?" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks heavy_blush "You expect me to flaunt my ass to those brutes?" ("mad", "base", "angry", "mid")
                    gen "Are you telling me you don't think it will work?" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Of course it will work, they're dumb as hell." ("open", "base", "angry", "R")
                    cho "But everyone will be able to see my butt!" ("quiver", "base", "raised", "down")
                    gen "That's the point." ("angry", xpos="far_left", ypos="head")
                    cho "But, but, but!" ("open", "closed", "worried", "mid")
                    gen "That's probably what the crowd will be chanting..." ("grin", xpos="far_left", ypos="head")
                    cho "Teasing Cedric is one thing... but the Slytherins..." ("mad", "happyCl", "worried", "down")
                    cho "I can't see myself doing...{w=0.4} this..." ("base", "base", "base", "mid")
                    gen "Well, that's your loss I guess..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "..." ("normal", "happyCl", "base", "mid")
                    cho @ cheeks blush "If that's all you have then I think I'm done here." ("open", "base", "worried", "down")

                    # Cho gets upset and leaves
                    $ states.cho.mood += 3
                    call cho_walk(action="leave")

                    gen "(Damn...)" ("base", xpos="far_left", ypos="head")
                    gen "(Looks like she isn't confident enough yet...)" ("base", xpos="far_left", ypos="head")
                    gen "(Some more favours should do the trick.)" ("base", xpos="far_left", ypos="head")

                    $ cho.equip(cho_outfit_last)

                    call gen_chibi("sit_behind_desk")
                    with fade

                    jump end_cho_event

            elif states.cho.tier == 3:
                if not states.cho.ev.talk_to_me.t3_e3_complete:
                    gen "(I don't know enough about the enemy team.)" ("base", xpos="far_left", ypos="head")
                    gen "(I should {b}talk to her{/b} more before proceeding.)" ("base", xpos="far_left", ypos="head")

                    jump .choices

                # Gryffindor:
                # Clothes: No clothes decided on yet
                if not states.cho.ev.quidditch.gryffindor_stage == "intro_done":
                    $ states.cho.ev.quidditch.gryffindor_stage = "intro_done"

                    gen "I have got it!" ("base", xpos="far_left", ypos="head")
                    cho "Finally..." ("soft", "base", "raised", "R")
                    cho "So, what's the plan?" ("open", "base", "raised", "mid")
                    gen "It's time to get intimate!" ("base", xpos="far_left", ypos="head")
                    cho "Intimate?" ("upset", "base", "raised", "mid")
                    gen "Yes, {i}touchy-touchy{/i}!" ("base", xpos="far_left", ypos="head")
                else:
                    # Repeated intro
                    gen "So about our tactics..." ("base", xpos="far_left", ypos="head")

                    if not states.cho.ev.inspect_her_body.T3_E3_complete or not states.cho.ev.suck_it.T3_E3_complete:
                        # Fail
                        cho "Got a better plan that doesn't involve me getting groped?" ("annoyed", "base", "base", "mid")
                        gen "..." ("base", xpos="far_left", ypos="head")
                        cho "Didn't think so..." ("open", "narrow", "raised", "mid")
                        gen "(She doesn't seem fully convinced just yet...)" ("base", xpos="far_left", ypos="head")
                        gen "(Maybe a few personal lessons would make her more open-minded.)" ("base", xpos="far_left", ypos="head")

                        jump cho_training.choices

                if states.cho.ev.inspect_her_body.T3_E3_complete and states.cho.ev.suck_it.T3_E3_complete:
                    $ states.cho.ev.quidditch.lock_practice = False

                    cho @ cheeks blush "What is this plan of yours based on?" ("soft", "narrow", "base", "down")

                    if states.cho.ev.manipulate_girls.t3_e4_complete: # has completed "Manipulate the girls!" public request?
                        gen "The girls on the Gryffindor team sure seem fond of you. If you could get close to them, then I'm sure they'll lose focus on the game." ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "Maybe so, but that doesn't solve one important issue..." ("open", "base", "raised", "mid")
                    else:
                        gen "It's obvious isn't it..." ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "No?" ("annoyed", "base", "raised", "mid")
                        gen "Girls doing naughty things together..." ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "What are you getting at?" ("angry", "base", "raised", "mid")
                        gen "If you get close to them, they will lose focus on the game!" ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "..." ("normal", "closed", "base", "mid") #worried
                        cho @ cheeks blush "What about the boys?" ("mad", "base", "raised", "mid")
                        gen "What about them?" ("base", xpos="far_left", ypos="head")

                    cho "Shouldn't their seeker, Harry, be our priority?" ("annoyed", "narrow", "raised", "R") #annoyed
                    gen "Similar tactic could work on him too." ("base", xpos="far_left", ypos="head")
                    gen "Imagine Miss Granger's reaction if you get close to him." ("grin", xpos="far_left", ypos="head")
                    cho "Now that's a plan!" ("smile", "base", "base", "mid")
                    gen "Great! it's settled then." ("base", xpos="far_left", ypos="head")

                    cho "What should I be wearing?" ("open", "base", "raised", "mid")
                    gen "What do you mean?" ("base", xpos="far_left", ypos="head")
                    cho "Well, previously, you've made me wear some silly combination of clothes." ("soft", "base", "base", "mid")
                    gen "You can wear whatever you like, fashion is too complicated for me." ("base", xpos="far_left", ypos="head")
                    cho "I see..." ("base", "narrow", "base", "mid")
                    cho "In that case--" ("open", "base", "base", "R")
                    #

                    cho "--Let me fetch my gear, and we can jump straight to training." ("crooked_smile", "base", "base", "mid")

                    #Cho returns with the Gryffindor clothing combination
                    $ cho.equip(cho_outfit_quidditch_gryffindor)
                    $ cho_outfit_quidditch.save()

                    call cho_chibi("fly", "mid", "base")

                    cho "Okay then, tell me what to do." ("base", "base", "base", "mid", trans=fade)

                    hide cho_main
                    with d3

                    jump cho_tactics
                else:
                    # Fail

                    cho @ cheeks blush "You want them to feel me up?!" ("mad", "base", "raised", "mid")
                    gen "Absolutely!" ("base", xpos="far_left", ypos="head")
                    gen "You may also touch them a bit as well while you're at it!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "No way!" ("soft", "wide", "base", "mid")
                    gen "Why not?" ("angry", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Teasing them is one thing but touching as well?" ("angry", "base", "base", "mid")
                    cho @ cheeks heavy_blush "With everyone watching." ("horny", "happyCl", "base", "mid") #blushes but imagining it
                    gen "..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "No, I won't do it..." ("horny", "base", "base", "downR")
                    gen "But what if--" ("base", xpos="far_left", ypos="head")

                    # Cho gets upset and leaves
                    $ states.cho.mood += 6
                    call cho_walk(action="leave")

                    gen "(She doesn't seem fully convinced just yet...)" ("base", xpos="far_left", ypos="head")
                    gen "(Maybe a few personal lessons would make her more open-minded.)" ("base", xpos="far_left", ypos="head")

                    $ cho.equip(cho_outfit_last)

                    call gen_chibi("sit_behind_desk")
                    with fade

                    jump end_cho_event

        "-Discuss tactics-" (style="disabled") if states.cho.ev.quidditch.lock_tactic:
            gen "(We've already established a tactic for the next match)" ("base", xpos="far_left", ypos="head")

            jump cho_training.choices

        "-Start Practice Match-" if game.daytime and not states.cho.ev.quidditch.lock_practice:
            if states.cho.tier == 1:
                # Hufflepuff
                jump cc_ht_start
            elif states.cho.tier == 2:
                # Slytherin
                jump cc_st_start
            elif states.cho.tier == 3:
                # Gryffindor
                jump cc_gt_start

        "-Start Practice Match-" (style="disabled") if not game.daytime or states.cho.ev.quidditch.lock_practice:
            if states.cho.ev.quidditch.lock_practice:
                if (states.cho.tier == 1 and states.cho.ev.quidditch.hufflepuff_training) or (states.cho.tier == 2 and states.cho.ev.quidditch.slytherin_training) or (states.cho.tier == 3 and states.cho.ev.quidditch.gryffindor_training):
                    gen "(She doesn't need any more practice.)" ("base", xpos="far_left", ypos="head")
                else:
                    nar "Cho isn't ready for practice yet."
            else:
                nar "You can only do that during the day."

            jump cho_training.choices

        "-Back-":
            cho "Very well, [name_genie_cho]." ("open", "base", "base", "mid", ypos="head", flip=False)

            hide cho_main
            show screen blkfade
            with d3

            $ cho.equip(cho_outfit_last)

            call cho_chibi("stand", "mid", "base")
            call gen_chibi("sit_behind_desk")

            call reset_menu_position

            hide screen blkfade
            cho "" ("base", "base", "base", "mid", xpos="base", ypos="base", trans=fade)
            jump cho_requests

### Quidditch Tactics ###

label cho_tactics:

    # Menu
    label .choices:

    call hide_characters
    call bld

    $ menu_y = 0.74

    menu:
        gen "(What directions should I give her?)" ("base", xpos="far_left", ypos="head")
        "\"Fly in front of me.\"" if states.cho.ev.quidditch.position != "front":
            jump cho_tactics.change_front
        "\"Fly in front of me.\" {size=-6}(selected){/size}" if states.cho.ev.quidditch.position == "front":
            pass

        "\"Fly above me.\"" if states.cho.ev.quidditch.position != "above":
            jump cho_tactics.change_above
        "\"Fly above me.\" {size=-6}(selected){/size}" if states.cho.ev.quidditch.position == "above":
            pass

        "\"Fly close to me.\"" if states.cho.ev.quidditch.position != "close":
            jump cho_tactics.change_close
        "\"Fly close to me.\" {size=-6}(selected){/size}" if states.cho.ev.quidditch.position == "close":
            pass

    gen "(No, that probably won't work...)" ("base", xpos="far_left", ypos="head")

    jump cho_tactics.choices

    # Change Tactic
    #TODO This plays once cho has agreed to the tactic/clothing and during the first intro
    # Once you pick the right option, the practice match option unlocks (Maybe we should have it say Try out tactic?)
    # The various options should go away once you've tried it once

    label .change_front:
        # The *ASS* position!
        $ states.cho.ev.quidditch.position = "front"

        if states.cho.tier == 1:
            # Hufflepuff

            call cho_walk(600, 150+180)

            cho "Is this good?" ("open", "base", "raised", "mid", ypos="head", flip=False)
            gen "*Hmm*... No, that robe is in the way... I can't seem to get a good view from this angle..." ("base", xpos="far_left", ypos="head")
            cho "Good! Then the crowd shouldn't either!" ("smile", "base", "base", "down", ypos="head", flip=False)
            gen "Yes, probably..." ("base", xpos="far_left", ypos="head")
            gen "How about instead you..." ("base", xpos="far_left", ypos="head")

        elif states.cho.tier == 2:
            # Slytherin

            call cho_walk(600, 150+180)

            cho "How's this?" ("open", "base", "raised", "mid", ypos="head", flip=False)
            gen "Excellent, I told you getting rid of that coat would do it!" ("base", xpos="far_left", ypos="head")
            gen "And those trousers sure emphasise the shape of your--" ("base", xpos="far_left", ypos="head")

            # Cho turns towards you

            cho @ cheeks blush "Good, then it's settled!" ("soft", "base", "base", "down", ypos="head", flip=False)
            gen "But I didn't get a proper look yet!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("clench", "base", "base", "mid", ypos="head", flip=False)
            gen "Alright, you can come down then..." ("base", xpos="far_left", ypos="head")

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide cho_main
            with fade

            gen "We'll test the tactics during the next practice like usual." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Do we have to? I'm sure it will work even without trying it." ("clench", "base", "raised", "mid")
            gen "Of course we do! You're the one who was so adamant last time..." ("base", xpos="far_left", ypos="head")
            gen "So let's see those results!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Yeah... Great, just let me know when..." ("normal", "closed", "base", "mid")
            gen "I certainly shall." ("grin", xpos="far_left", ypos="head")
            gen "But this will do for today, [name_cho_genie]." ("base", xpos="far_left", ypos="head")

            if game.daytime:
                cho "I'll head back to class then." ("open", "base", "base", "R")
            else:
                cho "I'll head back to my dorm then." ("open", "base", "base", "R")

            gen "Until next time." ("grin", xpos="far_left", ypos="head")

            call cho_walk(action="leave")

            $ states.cho.ev.quidditch.lock_practice = False
            $ states.cho.ev.quidditch.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's practice matches have been unlocked.", "Congratulations!", "interface/icons/head/cho.webp")

            call gen_chibi("sit_behind_desk")
            with fade

            jump end_cho_event

        elif states.cho.tier == 3:
            # Gryffindor

            call cho_walk(600, 150+180)

            gen "No, this won't do, you're way too far away from me." ("base", xpos="far_left", ypos="head")
            cho "What should I do then?" ("annoyed", "base", "raised", "mid", ypos="head", flip=False)
            gen "Let's see..." ("base", xpos="far_left", ypos="head")

        jump cho_tactics.choices

    label .change_above:
        # The ~Panties~ position!
        $ states.cho.ev.quidditch.position = "above"

        if states.cho.tier == 1:
            # Hufflepuff

            gen "Now, start with getting in front of me..." ("base", xpos="far_left", ypos="head")

            call cho_walk(550, 200+180)

            cho "Like this?" ("soft", "base", "base", "downR", ypos="head", flip=False)
            with hpunch
            gen "Yes, and now...{w=0.4} Higher!" ("angry", xpos="far_left", ypos="head")
            cho "Is this not high enough to see my--" ("annoyed", "base", "raised", "mid", ypos="head", flip=False)
            gen "Fly right above my head!" ("angry", xpos="far_left", ypos="head")
            gen "Show me those panties!" ("angry", xpos="far_left", ypos="head")
            cho @ cheeks blush "Of course, [name_genie_cho]..." ("base", "base", "base", "downR", ypos="head", flip=False)

            call cho_walk(500, 100+180)

            cho @ cheeks blush "How is this?" ("soft", "base", "base", "down", ypos="head", flip=False)

            # TODO: Panty shot CG?

            # Genie looks up.
            call gen_chibi("stand_alt", "desk", "base")
            show screen bld1
            with d3

            gen "Yes, fantastic!" ("angry", xpos="far_left", ypos="head")
            gen "You have very cute panties, girl!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Ehm*...{w=0.5} Thank you, [name_genie_cho]." ("annoyed", "base", "base", "down", ypos="head", flip=False)
            gen "(I have created the ultimate up-skirt!)" ("base", xpos="far_left", ypos="head")
            gen "(Nothing can stop us now...)" ("base", xpos="far_left", ypos="head")
            cho "Can I come down now?" ("soft", "base", "base", "downR", ypos="head", flip=False)
            gen "Give me another minute." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Tsk*" ("normal", "base", "raised", "L", ypos="head", flip=False)
            gen "Okay, you can come down now." ("base", xpos="far_left", ypos="head")

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide cho_main
            with fade

            cho @ cheeks blush "Enjoyed the view?" ("upset", "base", "angry", "mid") #angry/annoyed
            gen "Very much so." ("base", xpos="far_left", ypos="head")
            cho "Good!" ("smile", "base", "base", "mid")
            cho "Then I'm sure Cedric will like it too..." ("base", "closed", "base", "mid")
            gen "Who?" ("base", xpos="far_left", ypos="head")
            gen "Oh yeah, that guy!" ("base", xpos="far_left", ypos="head")
            gen "Yes, we should definitely try this during your next practice match against them." ("base", xpos="far_left", ypos="head")
            cho "..." ("normal", "base", "raised", "mid") #annoyed
            gen "When is that again?" ("base", xpos="far_left", ypos="head")
            cho "*Sigh* Just let me know when and I'll set one up with their captain." ("open", "narrow", "base", "R")
            gen "Excellent." ("base", xpos="far_left", ypos="head")

            if game.daytime:
                cho "If that is all, I'll head back to class." ("open", "base", "base", "mid")
                gen "Yes, that shall do for today." ("base", xpos="far_left", ypos="head")
                cho "Good day then, Sir..." ("soft", "narrow", "base", "mid")
            else:
                cho "If that is all, I'll head back to my dorm." ("open", "base", "base", "mid")
                gen "Yes, that shall do for today." ("base", xpos="far_left", ypos="head")
                cho "Good night then, Sir..." ("soft", "narrow", "base", "mid")

            call cho_walk(action="leave")

            $ states.cho.ev.quidditch.lock_practice = False
            $ states.cho.ev.quidditch.lock_tactic = True
            $ states.cho.ev.quidditch.hufflepuff_prepared = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's practice matches have been unlocked.", "Congratulations!", "interface/icons/head/cho.webp")

            call gen_chibi("sit_behind_desk")
            with fade

            jump end_cho_event

        elif states.cho.tier == 2:
            # Slytherin

            cho "Above you, [name_genie_cho]?" ("annoyed", "base", "raised", "mid", ypos="head", flip=False)
            gen "Yes, above..." ("base", xpos="far_left", ypos="head")
            cho "Okay..." ("upset", "base", "base", "mid", ypos="head", flip=False)

            call cho_walk(500, 100+180)

            gen "Hold on, that's a bit too high I think..." ("base", xpos="far_left", ypos="head")
            cho "You think?" ("angry", "base", "raised", "mid", ypos="head", flip=False) #annoyed
            gen "Yeah, how about instead you..." ("base", xpos="far_left", ypos="head")

        elif states.cho.tier == 3:
            #Gryffindor

            cho "You want me to fly... above you?" ("clench", "base", "raised", "mid", ypos="head", flip=False)
            gen "You've heard me..." ("base", xpos="far_left", ypos="head")
            cho "Okay then..." ("upset", "base", "base", "mid", ypos="head", flip=False)

            call cho_walk(500, 100+180)

            gen "Hey, how am I supposed to reach you from up there?" ("angry", xpos="far_left", ypos="head")
            gen "That's not how you get intimate!" ("base", xpos="far_left", ypos="head")
            cho "Why did you tell me to fly above you then?" ("annoyed", "base", "base", "down", ypos="head", flip=False)
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Sorry, I can't hear you from all the way down here." ("base", xpos="far_left", ypos="head")
            gen "I think it might be better if you..." ("base", xpos="far_left", ypos="head")

        jump cho_tactics.choices

    label .change_close:
        # The ~intimate~ position!
        $ states.cho.ev.quidditch.position = "close"

        if states.cho.tier == 1:
            # Hufflepuff

            cho "Close? How would you be able to see my--" ("annoyed", "base", "base", "mid", ypos="head", flip=False)
            gen "Come closer!" ("base", xpos="far_left", ypos="head")

            call cho_walk(450, 240+180)

            gen "Wait a second, I can't see your panties at all from this angle..." ("base", xpos="far_left", ypos="head")
            cho "No shi--" ("open", "narrow", "base", "mid", ypos="head", flip=False)
            gen "Let's try this instead..." ("base", xpos="far_left", ypos="head")

        elif states.cho.tier == 2:
            # Slytherin

            cho "Close?" ("annoyed", "base", "base", "mid", ypos="head", flip=False)
            gen "Yes close... did I stutter?" ("base", xpos="far_left", ypos="head")

            call cho_walk(450, 240+180)

            gen "You smell nice..." ("base", xpos="far_left", ypos="head")
            cho "Yeah, this is not going to work..." ("disgust", "narrow", "base", "mid", ypos="head", flip=False)
            gen "Fine, let's have you..." ("base", xpos="far_left", ypos="head")

        elif states.cho.tier == 3:
            # Gryffindor

            gen "Come as close to me as you can..." ("base", xpos="far_left", ypos="head")
            cho "Yes, [name_genie_cho]." ("soft", "base", "base", "R", ypos="head", flip=False)

            call cho_walk(450, 240+180)

            cho @ cheeks blush "How's this? Too close?" ("soft", "wink", "raised", "mid", ypos="head", flip=False)
            gen "No! It's the perfect distance!" ("base", xpos="far_left", ypos="head")
            gen "They would be able to smell you if you got any closer!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I hope not!" ("quiver", "closed", "worried", "mid", ypos="head", flip=False)
            gen "Why? You smell lovely, girl!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Ehm*...{w=0.5} Thank you, [name_genie_cho]." ("soft", "base", "worried", "mid", ypos="head", flip=False)
            cho @ cheeks blush "Can I come down now?" ("soft", "narrow", "base", "mid", ypos="head", flip=False)
            gen "Of course." ("base", xpos="far_left", ypos="head")

            #Cho flies down
            #Black screen
            call gen_chibi("stand", "desk", "base")
            call cho_chibi("stand", "mid", "base")
            hide cho_main
            with fade

            gen "You'll definitely distract those girls with this kind of move!" ("base", xpos="far_left", ypos="head")
            cho "And boys..." ("open", "base", "raised", "R")
            gen "Oh yeah, them to!" ("base", xpos="far_left", ypos="head")
            cho "Just let me know when to try it out against them." ("normal", "base", "raised", "mid")
            gen "Certainly... Oh, and keep wearing that scent, whatever it is." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "It's just deodorant..." ("clench", "base", "raised", "mid")
            gen "Yes, that! Keep wearing it!" ("base", xpos="far_left", ypos="head")

            if game.daytime:
                cho "If that is all, I'll head back to class." ("base", "narrow", "base", "R")
                gen "Yes, that shall do for today." ("base", xpos="far_left", ypos="head")
                cho "Good day to you, [name_genie_cho]..." ("soft", "narrow", "base", "mid")
            else:
                cho "If that is all, I'll head back to my dorm." ("base", "narrow", "base", "R")
                gen "Yes, that shall do for today." ("base", xpos="far_left", ypos="head")
                cho "Goodnight, [name_genie_cho]..." ("soft", "narrow", "base", "mid")


            call cho_walk(action="leave")

            $ states.cho.ev.quidditch.lock_practice = False
            $ states.cho.ev.quidditch.lock_tactic = True
            $ cho.equip(cho_outfit_last)

            call popup("Cho's practice matches have been unlocked.", "Congratulations!", "interface/icons/head/cho.webp")

            call gen_chibi("sit_behind_desk")
            with fade

            jump end_cho_event

        jump cho_tactics.choices
