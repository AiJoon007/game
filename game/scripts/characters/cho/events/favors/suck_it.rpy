

### Cho Blowjob ###

label cc_pf_blowjob:

    if not _events_completed_any:
        gen "{size=-4}(Should I ask her for a blowjob?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump cho_favor_menu.favors

    # Setup
    $ warned_her = False

    return

label end_cc_pf_blowjob:

    $ states.cho.status.blowjob = True
    $ cho.set_cum(None)

    if states.cho.tier == 3:
        if states.cho.level < 15: # Points till 15
            $ states.cho.level += 1

    jump end_cho_event

label cc_pf_blowjob_T3_intro_E1:

    call cc_pf_blowjob

    if states.cho.ev.suck_it.variant == None:
        gen "[name_cho_genie], ready to reward your coach for a job well done?" ("base", xpos="far_left", ypos="head")
        cho "Of course... A deal's a deal." ("open", "narrow", "base", "mid")
        gen "Great, in that case I think a blowjob is in order!" ("base", xpos="far_left", ypos="head")
        cho "A blowjob?!!" ("disgust", "wide", "base", "mid")
        gen "And some hand action as well of course!" ("base", xpos="far_left", ypos="head")
        cho "Sir, I didn't think it'd come to this... I already showed you my naked body and everything..." ("clench", "narrow", "base", "down")
        gen "There are other tactics you could use that aren't just about showing off your body in public, you know..." ("base", xpos="far_left", ypos="head")
        cho "Oh, yeah? Like what?" ("angry", "narrow", "raised", "mid")
        gen "Your dream is to become a professional, is it not?" ("base", xpos="far_left", ypos="head")
        cho "I... Yes... I suppose it is." ("soft", "narrow", "base", "R")
        gen "Then we should do our best to prepare you for what's out there!" ("base", xpos="far_left", ypos="head")

        label .introspection:

        if _in_replay:
            show screen blkfade
            with d5

            $ cho.equip(cho_outfit_default)
            $ cho.set_pose("default")
            $ cho.animation = None
            $ game.gold = 1984
            $ game.day = 124
            call room("main_room")

            call cho_chibi("stand", "desk", "base", flip=False)
            call gen_chibi("sit_behind_desk")

            cho "" ("soft", "narrow", "base", "R")

            hide screen blkfade
            with d5

        gen "I won't be your coach forever... Once you're looking for a proper team, you'll be in fierce competition with the other women athletes." ("base", xpos="far_left", ypos="head")
        gen "Women that will stop at nothing to get what they want." ("base", xpos="far_left", ypos="head")

        if _in_replay:
            show screen blkfade
            with d5
            return

        gen "So, as your coach, it's my responsibility to prepare you!" ("base", xpos="far_left", ypos="head")
        cho "And a blowjob is necessary for this?" ("angry", "narrow", "raised", "mid")

        if states.cho.ev.spy_on_girls.t3_e1_complete:
            gen "You've seen the girls on the Gryffindor team... You think they would hesitate with something as simple as a blowjob?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("disgust", "closed", "base", "down") #Pout
            gen "I see how it is..." ("base", xpos="far_left", ypos="head")
            gen "I sure didn't think a simple blowjob would dissuade you from pursuing your dreams." ("base", xpos="far_left", ypos="head")
        else:
            gen "Well, I can tell you this much... A woman looking to make it professionally should have enough confidence not to get stopped by something as simple as a blowjob." ("base", xpos="far_left", ypos="head")

        cho @ cheeks blush "..." ("normal", "narrow", "base", "downR") # angry
        cho @ cheeks blush "Alright, I'll do it..." ("open", "happyCl", "angry", "downR")
        gen "That's more like it!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "Don't get me wrong sir... I don't believe a word of what you just said is even remotely true." ("upset", "base", "base", "mid")
        cho @ cheeks blush "But you've helped me get this far..." ("annoyed", "narrow", "base", "down")
        cho @ cheeks blush "So if a blowjob is what it takes, then so be it..." ("soft", "base", "base", "downR")
        gen "That's the kind of determination I've been looking for..." ("grin", xpos="far_left", ypos="head")
        gen "Let's find out how a skilled Quidditch player handles this type of wood..." ("grin", xpos="far_left", ypos="head")
        cho "..." ("disgust", "narrow", "base", "mid") #smile #looks away
        cho @ cheeks blush "Okay, then... I'm ready." ("angry", "narrow", "base", "mid")
        gen "(At last!)" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/zipper.ogg"
        hide screen bld1
        hide cho_main
        call gen_chibi("jerk_off_behind_desk")
        with d5

        call cho_walk("desk_close", "base")
        pause 0.5

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("mid_shock")
        if game.daytime:
            $ camera.set_overlay("day_overlay")
        else:
            $ camera.set_overlay("night_overlay")
        $ camera.set(zoom=1.0, pos=(950, -750), initialize=True)
        show screen animatedCG
        with fade

        call gen_chibi("sit_behind_desk") # reset

        # Start CG with Cho kneeling in front of Genie.
        # Cho is dressed.

        # Note: Cho does not require posing here because it happens during the CG scene.
        $ renpy.choice_for_skipping()

        pause 0.5
        $ camera.set(pos=(0, -750), t=3.5, pause=True)
        $ camera.set(pos=(150, 400), t=2)

        if not states.cho.status.dick_seen:
            cho "By Merlin's beard!" #Wide eyed looking at dick #open mouth
            gen "Something wrong?"
            $ camera.set_image("mid_surprised")
            cho "N-No...{w=0.4} It's just...{w=0.4} This close...{w=0.4} It's so much larger than--" #Looking at dick
            gen "Good, then stop staring and put your hand on it..."
        else:
            cho "..." #Wide eyed looking at dick #open mouth
            gen "Go on... Stop staring, and put your hand on it."

        $ camera.set_image("mid_surprised_blush")
        cho "Okay..." #Blush #Normal mouth
        $ camera.set_imagepath("cho_bj/hj/")
        $ camera.set_image("up_worried")

        pause 0.6

        $ camera.set(zoom=0.5, pos=(100, 100), t=2.0)
        #Cho puts her hand on genies dick and looks up at him

        cho "..." #worried eyes
        gen "What? Don't tell me this is the first time you've done this..."
        $ camera.set_image("away_blush")
        cho "O-{w=0.3}of course I've done it before!"
        gen "Then get that arm moving, use those muscles!"
        $ camera.set_image("up")
        cho "..." # annoyed

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "Yes, that's it...{w=0.4} Stroke that cock, you little Ravenclaw slut..."

        $ camera.set_image("up_annoyed")

        cho "[name_genie_cho]!"# Stops moving hand #Annoyed #Looks up at genie
        gen "What?"
        gen "You're doing a great job [name_cho_genie], keep it going just like that..."

        $ camera.set_image("mid_annoyed")

        cho "*Hmph*..." #annoyed

        $ camera.set_image("away_blush")

        cho "Fine..."

        $ camera.set_image("cho_hj mid")

        call ctc

        gen "Such a firm grip..."
        gen "Must be from riding that broom so much..."
        gen "Although your rhythm could do with some work..."

        $ camera.set_image("cho_hj mid annoyed")

        cho "*Tsk*..." #Annoyed

        call ctc

        gen "That's better..."
        gen "Now then... Let's find out what you can do with that mouth of yours, shall we?"

        $ camera.set_image("up_wide")

        cho "Already?" #Wide eyed
        $ camera.set_image("up_worried")
        cho "Can't I just keep jerking you off?"
        gen "You agreed to a blowjob did you not?"
        $ camera.set_image("mid_worried")
        if not states.cho.status.dick_seen:
            cho "I...{w=0.4} Well, that was before you showed me your..." #Looks back down
        else:
            cho "Well, now that I'm seeing it again... I'm not so sure..." #Looks back down
        $ camera.set_image("away_blush")
        cho "How is this even..." #Cuts to dialog Menu choice

        $ states.cho.status.handjob = True
        $ states.cho.status.dick_seen = True
    else: # Alternate intro if first event has failed
        gen "Ready to continue with your training?" ("base", xpos="far_left", ypos="head")
        cho "Of course!" ("open", "base", "base", "mid")
        gen "Then you know what is required..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "You want me to touch your..." ("soft", "base", "base", "downR")
        cho @ cheeks blush "..." ("horny", "closed", "base", "mid")
        cho @ cheeks blush "Fine... I'll do it." ("angry", "base", "base", "mid")

        hide cho_main
        with d3

        call cho_walk("desk_close", "base")
        pause 1.0

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("mid_surprised")
        $ camera.set(zoom=1.0, pos=(0, -750), initialize=True)
        show screen animatedCG
        with fade

        $ camera.set(pos=(150, 400), t=2.0, pause=True)

        $ camera.set(zoom=0.5, pos=(100, 100), t=2.0)
        cho "Okay... I'm ready."
        $ camera.set_image("mid_surprised_blush")
        cho "..." #blush
        gen "Go on then, I don't have all day..."
        $ camera.set_image("mid_blush")
        cho "R-Right..." #Pout
        $ camera.set_imagepath("cho_bj/hj/")
        $ camera.set_image("mid_annoyed")
        cho "..." #annoyed
        gen "There you go... Much easier the second time, isn't it?"
        gen "Now, get those muscles moving..."

        $ camera.set_image("cho_hj mid")
        call ctc

        gen "That's it... You keep stroking, slut..."

        $ camera.set_image("cho_hj mid annoyed")
        cho "*Hmph*..." #Annoyed

        call ctc

        gen "Good..."
        gen "You're doing way better than last time... Perhaps you've had some time to think things over?"

        $ camera.set_image("cho_hj mid")

        call ctc

        cho "..."

        gen "I take that as a yes... So, let's put that mouth to good use then, shall we?"

        $ camera.set_imagepath("cho_bj/kneel/")
        $ camera.set_image("up_shock")

        cho "Already?"
        gen "No, tomorrow... Yes, of course now!"
        $ camera.set_image("mid_worried")
        cho "Can't I just keep jerking you off?" #pout
        gen "This again..."

    jump cc_pf_blowjob_1

label cc_pf_blowjob_1:
    menu:
        "-A deal's a deal...-": # FAIL
            gen "That's not what we agreed on."
            gen "Get those lips on there..."

            if states.cho.ev.suck_it.variant == None:
                $ camera.set_image("up_wide")
            else:
                $ camera.set_image("up_worried")

            cho "[name_genie_cho]!" #shocked
            gen "It's time to push those limits [name_cho_genie]... We've been over this."
            gen "Open up..."

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("mid_annoyed")

            cho "But... it's... How is it even going to fit?!"
            $ camera.set_image("mid")
            gen "It will fit... You're the most flexible girl in the castle."
            gen "If anyone could do it, it's you..."
            cho "..."
            gen "Now, put your hand back..."
            $ camera.set_image("mid_worried")
            cho "..."
            cho "Al-Alright...!"
            $ camera.set_imagepath("cho_bj/hj/")
            $ camera.set_image("up_worried")
            #Cho puts her hand back on
            gen "Good... Now put your lips around the tip..."

            $ camera.set_image("away_blush")
            cho "Oh-okay..."
            cho "(You can do this... Push your boundaries!)"
            cho "He-here I go..."

            #Cho opens her mouth and moves in towards genies cock #Genie cock twitches
            #She moves in closer and closes her eyes with her mouth wide open and just as she barely touches it, she jumps back
            $ camera.set_image("cho_bj lick fail")
            pause 1 # Pauses at last frame.
            cho "No, I can't... I can't do it!"

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("mid_annoyed")

            if states.cho.ev.suck_it.variant == "failed":
                cho "It still won't fit!"
                gen "[name_cho_genie]... You're here to push your limits, stop with the whining!"
                $ camera.set_image("up_worried")
                cho "I-I'm sorry [name_genie_cho]..."
                cho "I... I can't...{w=0.4} It's all happening too fast!"
                gen "[name_cho_genie]..."
                $ camera.set_image("mid_worried")
                cho "I'm sorry!" #blush, looking away
                $ states.cho.mood += 3 # Annoyed that you failed it again, sucker
            else:
                cho "It won't fit!"
                gen "[name_cho_genie]... You're here to push your limits."
                $ camera.set_image("up_worried")
                cho "I-I'm sorry [name_genie_cho]..."
                cho "I... Need some time to think..."
                gen "[name_cho_genie]..."
                $ camera.set_image("mid_worried")
                cho "I'm sorry!" #blush, looking away

            # Genie standing with his dick out, all alone, blue balled, all aloooooooone
            call gen_chibi("dick_out", 230, "base")

            hide screen animatedCG
            with fade

            #Cuts to Office and Cho walks quickly out of the room
            call cho_walk(action="leave")

            gen "(Damn...{w=0.4} Am I that type of coach that keeps pushing their pupils too hard?)" ("base", xpos="far_left", ypos="head")
            gen "(Speaking of hard, this thing isn't going to go away by itself...)" ("base", xpos="far_left", ypos="head")
            gen "(Well... if there's anything I got good at in that lamp...)" ("base", xpos="far_left", ypos="head")
            if states.cho.ev.suck_it.variant == "failed":
                gen "(Perhaps I should go a bit easier on her next time...)" ("base", xpos="far_left", ypos="head")

            $ states.cho.ev.suck_it.variant = "failed"

            call gen_chibi("sit_behind_desk")
            with fade

            # Event resets. (No progress)
            $ _event.cancel()

            jump end_cho_event

        "-Take it slow...-": #Cho strokes and licks genie then goes back to stroking until climax
            gen "Okay... Just keep stroking it for now..."

            if states.cho.ev.suck_it.variant == None:
                $ camera.set_imagepath("cho_bj/hj/")
                $ camera.set_image("up_wide")
                cho "Oh... Okay, I can do that..."
                gen "But you better put some work into it!"
                $ camera.set_image("mid")
            else:
                $ camera.set_imagepath("cho_bj/kneel/")
                $ camera.set_image("up")
                cho "Oh... Okay, I can do that..."
                gen "But you better put some work into it, show me that stamina of yours!"
                $ camera.set_image("mid")

            cho "Of course!"
            $ camera.set_imagepath("cho_bj/hj/")
            $ camera.set_image("mid_blush")
            cho "(I'll show you my stamina, alright!)" #Blushing

            $ camera.set_image("cho_hj mid")

            call ctc

            gen "*Ah*...{w=0.3} That's it... You're finally getting the hang of this."
            gen "You should've told me Quidditch players were this good at handjobs sooner."

            $ camera.set_image("cho_hj up blush")
            cho "..." #Looks up at genie #Blushes

            call ctc

            gen "And... Look at you... Stroking your coach's cock..."

            $ camera.set_image("cho_hj mid blush")

            cho "..."#Looks back down at cock #still stroking

            call ctc

            gen "Willing to do anything to win that cup..."

            $ camera.set_image("cho_hj mid")

            gen "Begging to receive her coach's cum."
            gen "Now, put your mouth on it [name_cho_genie]..."
            $ camera.set_image("up_wide")
            #Cho stops handjob
            cho "But I thought..."
            gen "If you want to outdo your competition then you need to push through your limits [name_cho_genie]..."
            $ camera.set_image("up_worried")
            gen "Give it a little lick, I promise it won't bite."
            cho "..." #Annoyed
            $ camera.set_image("away_blush")
            cho "Fine..." #Blushes #Annoyed
            $ camera.set_image("cho_bj lick success")
            pause 1.5
            gen "See? That wasn't bad, was it?"
            $ camera.set_image("up_annoyed")
            cho "I--..." # Grim look at Genie
            $ camera.set_image("mid")
            cho "(I guess not...)" #Looks back on cock
            gen "Go on..."
            $ camera.set_image("mid_annoyed")
            cho "Fine!" #annoyed
            $ camera.set_image("mid_worried")
            cho "..." #Worried
            $ camera.set_image("cho_bj lick start")
            pause .7
            $ camera.set_image("cho_bj lick")
            cho "*Lick-slurp-lick*"

            call ctc

            gen "*Ah*...{w=0.5} Good job [name_cho_genie]."
            gen "I suppose that will be enough for n--"
            $ camera.set_image("up_annoyed", trans=d3)
            cho "No! I want--"
            $ camera.set_image("away_blush")
            cho "I mean...{w=0.5} You deserve your reward, [name_genie_cho]."
            cho "At least let me finish you off with my hand..."
            $ camera.set_image("mid_blush")
            gen "That's what I wanted to hear [name_cho_genie], you're learning..."
            gen "Get going then..."

            $ camera.set_image("cho_hj mid blush")

            call ctc

            gen "*Hmm*...{w=0.4} That's it, grip it firmly just like that..."

            call ctc

            gen "*Ah*...{w=0.4} Not bad...{w=0.4} Not bad at all..."
            gen "Now... A little bit faster, [name_cho_genie]..."
            gen "I think you too deserve a reward..."

            $ camera.set_image("cho_hj mid blush fast")

            cho "Okay..." #Blush

            $ camera.set_image("cho_hj up blush")
            cho "[name_genie_cho]...{w=0.4} Will you tell me when--"
            gen "Faster [name_cho_genie]!"
            cho "Oh...{w=0.4} Of course!"

            $ camera.set_image("cho_hj mid blush fast")
            call ctc

            gen "(Now that's my [name_cho_genie]!)"
            gen "(I'm at my limit, should I warn her?)"

            menu:
                "-Warn her-":
                    $ warned_her = True

                    gen "That's it, almost there...!"

                    call ctc

                    gen "Get ready for your reward, [name_cho_genie]!"
                    menu:
                        "-Cum on her face-":
                            $ camera.set(zoom=0.45, pos=(150, 70), t=2.0)
                            gen "*ARGH*!"

                            with vpunch
                            $ camera.set_image("cho_hj cum face")
                            pause 1.42
                            $ camera.set_image("cum") # Still image

                            call ctc

                            gen "*Ah*..."
                            cho "Are...{w=0.5} Are you done?"
                            gen "*Ah*...{w=0.4} Yes, you can open your eyes now..."

                            $ camera.set_image("cum_eye")

                            cho "..." #Opens eyes

                            $ camera.set_image("cum_eye_blush")

                            cho "So...{w=0.4} much..." #blush

                            $ camera.set_imagepath("cho_bj/kneel/")
                            $ camera.set_image("cum_eye")

                            #Cho takes hand off penis and puts to her side
                            cho "And so sticky..." #blush

                            $ camera.set(zoom=0.6, pos=(220, 180), t=5.0, pause=True)

                            # Set cum on doll
                            $ cho.set_cum(face="heavy", hair="light")

                            $ states.cho.status.cumshot = True

                        "-Cum on her tits-":
                            gen "Get back a little, quick!"

                            $ camera.set_image("away", trans=d3)
                            $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)

                            gen "*ARGH!* Here it comes, you slut!"

                            with vpunch
                            $ camera.set_image("cho_hj cum tits")

                            pause 2
                            $ camera.set_image("cum_tits")

                            call ctc

                            gen "*Ah*..."

                            $ camera.set_image("look_cum_tits")

                            cho "You..." #Looks down on breasts
                            cho "My breasts..."

                            $ camera.set_image("look_blush_cum_tits")

                            cho "So much..." #blush

                            gen "That...{w=0.4} was...{w=0.4} amazing!"
                            gen "That is some talent you have there [name_cho_genie]..."

                            $ camera.set_image("dreamy_cum_tits")

                            cho "...{heart}{heart}" #blush #looking at penis
                            gen "[name_cho_genie]?"

                            $ camera.set_image("dreamy_up_cum_tits")

                            cho "Oh... Thank you [name_genie_cho]." #looks up at genie
                            gen "Now, get on your feet and let me have a proper look at you..."

                            $ camera.set(zoom=0.6, pos=(220, 180), t=5.0, pause=True)
                            #Cuts back to office screen  (sound of cloth etc as genie puts dick away and Cho moves)
                            # Set cum on doll
                            $ cho.set_cum(breasts="heavy")

                            $ states.cho.status.cumshot = True

                "-Don't-":
                    $ warned_her = False
                    $ states.cho.mood += 4

                    gen "(You better be ready slut...)"

                    $ camera.set_image("cho_hj up blush")

                    cho "[name_genie_cho], are you about to--"

                    gen "*ARGH*!"

                    $ camera.set_image("cho_hj mid")
                    $ camera.set(zoom=0.45, pos=(150, 70), t=2.0)
                    cho "*Huh*?!" #Wide eyed

                    with vpunch
                    $ camera.set_image("cho_hj cum face tits")
                    pause 0.9
                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("cum_face_tits")

                    call ctc

                    gen "*Ah*..."
                    cho "..." # Wide eyed
                    cho "M--{w=0.3} My face!" #Angry
                    cho "You just came on my face!"
                    gen "*Ahh*... At last..."

                    $ camera.set_image("cum_face_tits_glance", trans=d3)

                    $ camera.set(zoom=0.6, pos=(220, 180), t=5.0, pause=True)

                    #Cuts back to office screen (sound of cloth etc as genie puts dick away and Cho moves)
                    # Set cum on doll
                    $ cho.set_cum(face="heavy", hair="light", breasts="heavy")

                    $ states.cho.status.cumshot = True

    hide screen animatedCG
    with fade

    # After CG, in the office.

    if warned_her:
        gen "Well done [name_cho_genie], you've started pushing those limits on your own." ("base", xpos="far_left", ypos="head")
        gen "Also, You've got a little something right there..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Very funny [name_genie_cho]..." ("clench", "narrow", "base", "mid", trans=d3)
        gen "Your confidence is showing itself more and more every day." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I...{w=0.5} You deserved it [name_genie_cho]...{w=0.5} For helping me this far..." ("upset", "narrow", "base", "downR")
        cho @ cheeks blush "For teaching me... all this stuff..." ("angry", "closed", "base", "mid") #Blush
        gen "(I'm a bloody saint, I've waited that long...)" ("base", xpos="far_left", ypos="head")
        gen "You're very welcome." ("base", xpos="far_left", ypos="head")
    else:
        gen "That...{w=0.4} was...{w=0.4} amazing!"
        cho "Why didn't you warn me?!" ("clench", "base", "angry", "down", trans=d3) #Angry
        # cho "My clothes are all ruined now too..." ("angry", "closed", "angry", "mid")
        # cho "There's cum all over them!" ("mad", "narrow", "angry", "down")
        cho @ cheeks blush "I can't believe you just came all over me like that..." ("annoyed", "base", "angry", "downR") #pout
        gen "Should have put it in your mouth then..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("disgust", "narrow", "base", "mid") #pout

    cho @ cheeks blush "Is this what you do to Hermione as well?" ("upset", "narrow", "base", "down")

    if states.her.status.blowjob:
        gen "Maybe." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I knew it..." ("smile", "wide", "base", "mid")
        if states.her.status.gokkun:
            gen "Miss Granger knows how to properly dispose--" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "{size=+7}She swallows?!?{/size}" ("clench", "wide", "base", "mid")
            cho @ cheeks blush "I mean..." ("disgust", "base", "base", "downR")
            cho @ cheeks blush "{size=-4}Of course she does...{/size}" ("angry", "base", "base", "down")
    else:
        gen "Of course not..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I knew--" ("smile", "happyCl", "base", "mid")
        cho @ cheeks blush "Wait, she doesn't do stuff like that?" ("clench", "narrow", "base", "mid")
        gen "No." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "So I am your first?" ("smile", "narrow", "base", "downR") # blush
        gen "In one way or the other." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "What's that supposed to mean?!" ("upset", "base", "angry", "mid") # angry
        cho @ cheeks blush "Whatever..." ("annoyed", "base", "angry", "R") # pout

    cho @ cheeks blush "Are you...{w=0.4} Are we done?" ("open", "narrow", "base", "downR") #Blush
    gen "Yes, for now..." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        cho "Alright... In that case, I better head back to class." ("open", "base", "base", "R")
    else:
        cho "Alright... I'll head off to bed then." ("open", "base", "base", "R")
    gen "Until next time." ("base", xpos="far_left", ypos="head")

    call cho_walk(action="leave")

    gen "[name_cho_genie]!" ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(Probably should've asked her to clean herself first...)" ("base", xpos="far_left", ypos="head")
    gen "(Oh well, she'll find out one way or another.)" ("base", xpos="far_left", ypos="head")

    jump end_cc_pf_blowjob

label cc_pf_blowjob_T3_E2:

    call cc_pf_blowjob

    gen "Ready for an oral exam [name_cho_genie]?" ("base", xpos="far_left", ypos="head")
    cho "A what?" ("open", "base", "raised", "mid")
    gen "Time to put that mouth to good use..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "My mouth to--" ("horny", "base", "base", "downR") #Blush
    gen "Any problems?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No... of course not [name_genie_cho]..." ("normal", "base", "base", "mid")
    gen "Excellent!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Just...{w=0.4} tell me what to do [name_genie_cho]..." ("open", "base", "base", "R")

    call cho_walk("desk_close", "base")
    pause 1.0

    # Start CG with Cho kneeling in front of Genie.
    # Cho is dressed.

    # Note: Cho does not require posing here because it happens during the CG scene.

    $ camera.set_imagepath("cho_bj/kneel/")
    $ camera.set_image("mid")
    if game.daytime:
        $ camera.set_overlay("day_overlay")
    else:
        $ camera.set_overlay("night_overlay")
    $ camera.set(zoom=1.0, pos=(150, 400), initialize=True)
    show screen animatedCG
    with fade

    $ camera.set(zoom=0.5, pos=(100, 100), t=2.0)

    gen "..."
    cho "..." #looking at dick
    gen "Go on then..."

    $ camera.set_image("mid_blush")

    cho "Of course..." #Blush
    #Cho puts hand on genies dick

    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("mid_blush")

    gen "Just start with some stroking like you did before..."

    $ camera.set_image("up_blush")

    cho "Yes, [name_genie_cho]..."

    $ camera.set_image("cho_hj mid")

    call ctc

    gen "That's it... Stroke your coach's cock..."
    gen "Good...{w=0.5} Back and forth...{w=0.5} just like I taught you..."

    $ camera.set_image("cho_hj mid blush")

    cho "(He's so big...)" #Blushes

    gen "Very good... Now take that shirt off for me, will you..."

    $ camera.set_image("away_blush")

    cho "Okay..." #Blushes #moves back to base position
    #Takes off shirt

    play sound "sounds/cloth_sound3.ogg"
    $ camera.set_image("topless_mid", trans=Fade(0.5, 2.0, 0.5))

    gen "Excellent... Now continue stroking, [name_cho_genie]."

    $ camera.set_image("topless_up")

    cho "Alright..."
    #Resumes handjob

    $ camera.set_image("cho_hj topless mid")

    call ctc

    cho "......."
    cho "(I'm actually doing this...)"
    cho "(I'm stroking my coach's hard cock, just so I can win the quidditch cup...)"
    cho "(But...{w=0.4} If this is what it takes...{w=0.3} Then so be it!)"
    cho "(It won't be long until I have that cup in my hands...)"

    $ camera.set_image("cho_hj topless mid smile")

    cho "(I can already taste the victory!)"

    gen "You're being awfully quiet [name_cho_genie]... It's very unlike you..."

    $ camera.set_image("topless_away_blush")

    cho "S-Sorry [name_genie_cho]..."

    $ camera.set_image("topless_up_worried")

    cho "It's just...{w=0.4} I just keep thinking...{w=0.4} how without your help I would've been out of the competition by now..."
    gen "(And without your help I'd be sitting here with a limp dick right about now.)"

    $ camera.set_image("topless_away_blush")

    cho "I...{w=0.4} I'm sorry I doubted your methods at first [name_genie_cho]..."
    gen "I knew you'd come around..."

    $ camera.set_image("topless_up_blush")

    cho "{heart}"

    $ camera.set_image("topless_mid_blush")

    cho "I'm just glad that there was some small way for me to repay you..." #looks at genies dick

    $ camera.set_image("cho_hj topless mid smile")

    gen "*Ah*... Yes, of course... It's nothing really."

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "Oh please..."
    cho "Pleasuring you is little to nothing compared to what you've done for me so far..."

    $ camera.set_image("cho_hj topless mid smile")

    cho "Giving you a bit of a reward is the least I could do..." #Blush

    $ camera.set_image("cho_hj topless mid smile fast")

    gen "(*Argh*...{w=0.4} At this rate, she'll make me bust!)"

    call ctc

    gen "Now you're getting into it..."
    gen "Speaking of...{w=0.2} Time to put that mouth to work..."

    $ camera.set_image("topless_up_worried")

    cho "Already?"
    gen "Not this again."
    gen "Didn't you say you wanted to {i}reward{/i} me a second ago?"

    $ camera.set_image("topless_away_blush")

    cho "Sorry, you're right [name_genie_cho]..."
    cho "Just...{w=0.4} Tell me what to do..." #blush

    $ camera.set_image("topless_mid")

    gen "Start by putting those lips around the tip, then slowly work your mouth further down the shaft..."

    $ camera.set_image("topless_up")

    cho "I...{w=0.4} Yes, [name_genie_cho]..." #Looks at genie

    $ camera.set_image("topless_mid_blush")

    cho "..." #blush
    cho "Here it goes..."

    #$ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless suck closed success")
    pause 5.1

    #Cho closes her eyes as she moves in, her mouth spreading open as she works it around the tip of genies penis
    #Once her mouth worked past the tip she pulls out and open her eyes, looking up at genie

    $ camera.set_image("topless_up")

    cho "How...{w=0.4} how was that [name_genie_cho]?"
    gen "Good start, but you shouldn't close your eyes...{w=0.4} And you should keep going until you find your limit, then hold it there for a bit..."
    gen "The further down the better..."

    $ camera.set_image("topless_mid")

    cho "Okay..."

    $ camera.set_image("cho_bj topless suck closed fail")
    pause 0.5

    gen "Eyes open, [name_cho_genie]..."

    $ camera.set_image("cho_bj topless suck closed fail exit")
    cho "Oh!{w=0.4} Sorry [name_genie_cho]!"

    $ camera.set_image("topless_up_blush")

    #Cho opens her eyes and looks at Genies penis."
    cho "I'll keep them open..." #small text

    $ camera.set_image("cho_bj topless suck start")
    pause 0.8
    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("topless_suck_up")

    cho "*Khow ish dhat*?"

    #Cho goes in again with her eyes open this time, her mouth spreading open as it slowly goes over the tip."
    #As her mouth continues past the tip she stops and looks up at genie for some approval but he stays silent, her eyes closes slightly as she resumes by slowly going down further
    gen "*Ah*...{w=0.5} That's it...{w=0.5} Keep going, [name_cho_genie]!" #This line should auto play as she goes further down
    #As she continues further down, her pupils move up a bit more until she hits her gag reflex (slow zoom in effect)
    #Quickly retracting she moves her head back and her eyes open again (Loop going backwards fast if animated, zoom effect quickly goes back to normal)

    $ camera.set_image("cho_bj topless suck medium up")
    call ctc
    $ camera.set_image("cho_bj topless suck closed exit")
    pause 3

    cho "*Gah*...{w=0.4}{nw}"

    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("topless_cough")

    cho "*Cough*{w=0.2} *Cough*"

    $ camera.set_image("topless_mid")

    gen "Easy there girl..."

    $ camera.set_image("topless_up")

    cho "Was...{w=0.4} Was that better, [name_genie_cho]?" #Cho looks up at genie
    gen "Excellent!{w=0.3} Although... maybe a bit too far... You barely held it there for a second."

    $ camera.set_image("topless_away_blush")

    cho "Oh...{w=0.5} Yes, I thought it might've been..."
    gen "(This girl is like an on and off switch...)"
    gen "In any case... I think you got it..."
    gen "So... Let's get that head bobbing, [name_cho_genie]!"

    $ camera.set_image("topless_away_pout")

    #Cho looks back down at dick
    cho "Are...{w=0.4} are you going to cum on me again [name_genie_cho]?"
    gen "I wouldn't worry about that yet... Just focus on your task..."

    $ camera.set_image("topless_mid")

    cho "... {w=0.5}Okay then..."
    #Cho starts jerking genie off again

    $ camera.set_image("cho_hj topless mid")
    call ctc

    gen "You'll have to do more than just--"

    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless suck start")
    cho "*oomph*{w=1.0}{nw}"
    $ camera.set_image("cho_bj topless suck")

    #Cho moves in and starts sucking genie off properly (Not as deep as she attempted)

    call ctc

    gen "That's more like it... Work that tongue..."

    # Cho looks up
    $ camera.set_image("cho_bj topless suck medium up")
    call ctc

    gen "Fuck yes... You naughty girl..."

    #Cho pulls out and starts jerking genie off slowly
    $ camera.set_image("cho_bj topless suck closed exit")
    pause 3.0
    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("cho_hj topless up blush")
    call ctc

    cho "Am I doing it right, [name_genie_cho]?"
    gen "Yes, It feels--"

    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless lick start")
    pause 0.65
    $ camera.set_image("cho_bj topless lick")

    #Cho starts licking the tip a couple of times #looking at dick
    gen "Whoa!"

    call ctc

    cho "(*Huh*...{w=0.5} This is just like Quidditch, all I have to do is find a good tactic against him. {heart})" #looks up at genie still licking
    cho "(Guess he's not immune to his own tricks... {heart})"

    $ camera.set_image("cho_bj topless lick exit")
    pause 0.9
    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("topless_up_blush")

    #Cho pulls back and smiles
    cho "I can't believe you're making your student suck your cock..."
    cho "Surely that's not something a coach should be doing..."
    gen "Well, I--"

    $ camera.set_imagepath("cho_bj/bj/")
    $ camera.set_image("cho_bj topless suck start")
    pause 2.85
    $ camera.set_image("cho_bj topless suck medium up")

    #Blowjob starts again
    gen "(Fuck me, this girl is a natural!)"

    call ctc

    gen "You--{w=0.4} You're a fast learner, [name_cho_genie]..."

    $ camera.set_image("cho_bj topless suck deep")

    #Faster Blowjob
    cho "{heart}{heart}{heart}"

    gen "[name_cho_genie], if you do that--{w=0.2} Oh fuck!"

    menu:
        "-Warn her-":
            gen "[name_cho_genie]... I think..."
            gen "There's....{w=0.5} one more thing...{w=0.5} I could teach you today..."

            $ camera.set_image("cho_bj topless suck medium up")
            cho ".............?"

            gen "Time to make your coach proud... Get ready!"

            call ctc

            menu:
                "\"I'll even give you some house points!\"":
                    $ states.cho.ev.suck_it.variant = "points"
                    #Cho pulls back

                    $ camera.set_image("cho_bj topless suck medium")

                    cho "(House points!?)" # angry #Wide eyed #Big text


                    $ camera.set_image("cho_bj topless suck closed exit")
                    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
                    gen "{cps=5}Fuuuuuuuuu{/cps}--{w=0.5}{nw}"

                    with vpunch
                    $ camera.set_image("cho_hj topless cum face tits")
                    gen "Fuuuuuuuuu{fast}uck!"

                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("topless_mid_angry_cum_face_tits")

                    call ctc

                    show screen blkfade
                    with d5

                    cho "My eye!" #Big text
                    cho "I got some in my eye!" #Big text
                    gen "*Ah*...{w=0.4} Why'd you pull back!"

                    # Set cum on doll and strip her
                    $ cho.set_cum(face="heavy", hair="light", breasts="heavy")
                    $ cho.strip("robe", "top", "bra")

                    hide screen animatedCG
                    hide screen blkfade
                    with fade

                    #Office screen (Cho has cum on her face and tits)

                    cho @ cheeks blush "\"House points\", really?!" ("angry", "base", "angry", "mid", trans=d3)
                    cho @ cheeks blush "You want me to swallow your semen for house points?!" ("mad", "base", "angry", "mid")
                    gen "The points were just going to be a bonus." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "A bonus on top of?" ("open", "base", "angry", "mid")
                    gen "Not having to clean up..." ("base", xpos="far_left", ypos="head")
                    gen "Although I guess you didn't see it that way since you--" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "..." ("clench", "closed", "angry", "mid") #Angry
                    gen "Pulled...{w=0.5} back..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "I'm not selling my body for points!" ("scream", "base", "angry", "mid")
                    gen "Of course..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "I can't believe you..." ("disgust", "base", "angry", "down") #Small text

                    call cho_walk("door", "base")

                    cho @ cheeks blush "{size=-3}Who does he think I am?{w=0.4} I'm not Hermione!{/size}" ("annoyed", "closed", "angry", "mid", flip=True, trans=d3)
                    gen "[name_cho_genie]." ("base", xpos="far_left", ypos="head")

                    call cho_chibi("stand", "door", flip=False)
                    cho @ cheeks blush "I don't want to hear any of your excuses [name_genie_cho]!" ("scream", "narrow", "angry", "mid", flip=False, trans=d3)
                    call cho_chibi("stand", "door", flip=True)
                    hide cho_main
                    with d5
                    gen "At least let me--" ("base", xpos="far_left", ypos="head")

                    call cho_walk(action="leave")
                    play sound "sounds/door_down.ogg"
                    with hpunch

                    pause 1.0
                    gen "..." ("base", xpos="far_left", ypos="head")
                    pause 0.5

                    call cho_walk(action="enter")
                    with d5

                    pause 1.0

                    gen "Don't say I didn't try to--" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Shut... up!" ("angry", "base", "angry", "mid", trans=d3)
                    play sound "sounds/cloth_sound2.ogg"
                    $ cho.wear("all")
                    with fade

                    pause 1.0
                    call cho_walk("door", "base")
                    call cho_walk(action="leave")
                    play sound "sounds/door_down.ogg"
                    with hpunch

                    gen "..." ("base", xpos="far_left", ypos="head")
                    gen "(She'll get over it...)" ("base", xpos="far_left", ypos="head")
                    gen "(I think.)" ("base", xpos="far_left", ypos="head")

                    $ states.cho.mood += 12

                "\"Taste that cum in your mouth!\"":
                    $ states.cho.ev.suck_it.variant = "taste"

                    cho "(T-taste?! But... We never discussed this!)"

                    $ camera.set_image("cho_bj topless suck medium up")
                    cho "*Mhmmmm Mmhmmmm*!"

                    #Cho stops for a second to consider and then starts going again
                    call ctc

                    gen "*Ngh*--{w=0.2} That's it [name_cho_genie]!"

                    $ camera.set_image("cho_bj topless suck closed")

                    cho "(Oh god...)" #blush
                    gen "Here it comes!"

                    $ camera.set_image("cho_bj topless suck medium")

                    cho "(No, wait!)"
                    cho "*Mmmmmhmmm*!!!"
                    gen "{size=+4}*ARGH!*{/size}"

                    with vpunch
                    $ camera.set_image("cho_bj topless cum mouth")

                    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
                    pause 2

                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("topless_mid_cum_mouth")

                    call ctc

                    $ camera.set_image("topless_mid_surprised_cum_mouth")

                    #Cho opens her mouth and lets the cum dribble out
                    cho "*Sho*...{w=0.4} *Sho mush*...."

                    $ camera.set_image("topless_away_blush_cum_mouth")

                    cho "(Although...{w=0.4} it doesn't taste as bad as I--)"
                    gen "Nicely done [name_cho_genie], I knew you'd have it in you!"

                    # Make her lisp the name, if the name is unsupported fallback and replace 's' occurrences with 'sh'
                    $ _replacement_names = {
                        "master": "mashter",
                        "daddy": "dhadhy",
                        "old man": "oldh mhan",
                        "professor": "phrofeshor",
                        "coach": "choach"
                        }

                    $ _name = name_genie_cho.replace(name_genie_cho, _replacement_names.get(name_genie_cho, name_genie_cho.replace("s", "sh")))

                    $ camera.set_image("topless_up_cum_mouth")

                    cho "*Phank you, [_name]*"
                    gen "Didn't your parents teach you to not speak with your mouth full?"

                    $ camera.set_image("topless_away_blush_cum_mouth")

                    cho "............"
                    gen "Now, get on your feet, so I can have a look at you..."

                    # Set cum on doll and strip her
                    $ cho.set_cum(face="light")
                    $ cho.strip("robe", "top", "bra")

                    hide screen animatedCG
                    with fade

                    # TODO: Add Cho doll flip when at door etc, cum layers
                    #Cho has no shirt, cum on her face and down her tits

                    gen "Well, will you look at that...{w=0.4} You look great with a fresh coat of paint!" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Did you have to cum this much..." ("disgust", "narrow", "base", "down", trans=d3)
                    gen "I can't exactly control it..." ("base", xpos="far_left", ypos="head")
                    gen "If you don't swallow, you'll have to deal with the mess." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Swallow [name_genie_cho]'s--" ("upset", "base", "base", "downR") #Blush
                    cho @ cheeks blush "I don't know..." ("soft", "narrow", "base", "downR") #Blush
                    gen "In any case, you've excelled today [name_cho_genie]." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "I think I need to lie down for a bit..." ("open", "narrow", "base", "down")
                    cho @ cheeks blush "This was exhausting...{w=0.4} Even for me." ("open", "narrow", "base", "mid")
                    if states.her.status.blowjob:
                        cho "I don't know how Granger could do this, without getting exhausted." ("soft", "narrow", "base", "down")
                        gen "(*Heh*, practice makes perfect...)" ("grin", xpos="far_left", ypos="head")

                    if game.daytime:
                        gen "No time for a lie down I'm afraid..." ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "What, don't tell me you're already--" ("clench", "wide", "base", "mid")
                        gen "You've got class to get to." ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "Oh...{w=0.4} Right..." ("open", "base", "base", "down")
                        cho @ cheeks blush "Good day then..." ("soft", "base", "base", "mid")
                    else:
                        gen "A lie down you say..." ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "Don't you get any ideas..." ("disgust", "narrow", "base", "mid")
                        gen "I most certainly was not!" ("base", xpos="far_left", ypos="head")
                        cho @ cheeks blush "Yeah right." ("annoyed", "base", "base", "R")
                        gen "{size=-4}Pervert...{/size}" ("base", xpos="far_left", ypos="head")
                        gen "Well, you've earnt a lie down I suppose..." ("base", xpos="far_left", ypos="head")
                        cho "Good night then..." ("open", "narrow", "base", "mid")
                        gen "Good night, [name_cho_genie]." ("base", xpos="far_left", ypos="head")

                    call cho_walk("mid", "base")
                    gen "[name_cho_genie]!" ("base", xpos="far_left", ypos="head")

                    call cho_chibi("stand", "mid", "base", flip=False)

                    cho "Yes [name_genie_cho]?" ("open", "base", "raised", "mid", trans=d3)
                    gen "Your top..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Oh... Of course!" ("clench", "happyCl", "base", "mid") #Blush

                    play sound "sounds/cloth_sound2.ogg"
                    $ cho.wear("all")
                    with fade

                    cho @ cheeks blush "..." ("soft", "base", "base", "down") #Cho puts on top
                    cho @ cheeks blush "Thank you, [name_genie_cho]..." ("open", "base", "base", "downR")

                    call cho_walk(action="leave")

                    gen "...{w=0.5}Silly girl." ("base", xpos="far_left", ypos="head")
                    #Cho leaves
                    #End Scene #Marks at completed

                "\"Swallow that cum!\"":
                    $ states.cho.ev.suck_it.variant = "swallow"

                    $ camera.set_image("cho_bj topless suck closed exit")
                    pause 3
                    $ camera.set_imagepath("cho_bj/hj/")
                    $ camera.set_image("topless_up_cringe")

                    #Cho's eyes goes wide and pulls out
                    cho "But [name_genie_cho]--" #Big text
                    gen "*Aargh*! Get back there at once, or forget about your stupid Quidditch cup!"

                    $ camera.set_image("topless_away_pout")

                    cho "Y-yes, sir!"
                    $ camera.set_image("topless_mid_angry")
                    cho "(I'll show this stupid cock... You're not the boss of me!)"

                    $ camera.set_imagepath("cho_bj/bj/")
                    $ camera.set_image("cho_bj topless suck deep start")
                    pause 2.0
                    $ camera.set_image("cho_bj topless suck deep")

                    gen "Yeeees, you fucking slut!"
                    cho "*Mmmmhh* {heart}{heart}"

                    call ctc

                    gen "Get ready, I'm almost--"

                    $ camera.set_image("cho_bj topless suck medium")

                    cho "*Mhmhm*?!-- (Now?!--)"

                    gen "{size=+4}*ARGH*!{/size}"

                    with vpunch
                    $ camera.set_image("cho_bj topless cum swallow")
                    pause 1
                    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
                    pause 1
                    $ camera.set_imagepath("cho_bj/kneel/")
                    $ camera.set_image("topless_mid_cum_swallow")

                    call ctc

                    $ camera.set_image("topless_mid_surprised_cum_swallow")

                    cho "I...{w=0.4} I just swallowed..."
                    cho "My coach's cum..."
                    gen "Well done, [name_cho_genie], you sucked me dry."

                    $ camera.set_image("topless_away_cum_swallow")

                    cho "I...{w=0.4} Thanks... I guess."

                    # Strip doll (no cum necessary it seems)
                    $ cho.strip("top", "bra", "robe")

                    hide screen animatedCG
                    with fade

                    gen "Now this is the kind of initiative I'm talking about!" ("grin", xpos="far_left", ypos="head")
                    cho @ cheeks blush "..." ("disgust", "narrow", "base", "down", trans=d3) #blank stare
                    gen "[name_cho_genie]?" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Yes...{w=0.5} Sorry...{w=0.5} Thank you [name_genie_cho]." ("angry", "base", "base", "downR")
                    cho @ cheeks blush "Is that all?" ("soft", "narrow", "base", "down")
                    if game.daytime:
                        gen "That will be all for today..." ("base", xpos="far_left", ypos="head")
                    else:
                        gen "That will be all for tonight..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Okay, good..." ("angry", "narrow", "base", "down")
                    #Cho walks out the door, still without shirt on
                    call cho_walk(action="leave")
                    gen "[name_cho_genie]!" ("base", xpos="far_left", ypos="head")
                    #Cho comes back through the door
                    call cho_walk(action="enter")
                    with d5

                    cho @ cheeks blush "Yes [name_genie_cho]?" ("soft", "base", "base", "mid", trans=d3)
                    gen "..." ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Oh, of course!" ("clench", "base", "base", "down") #Wide eyed

                    #Cho puts on her shirt
                    play sound "sounds/cloth_sound2.ogg"
                    $ cho.wear("all")
                    with fade

                    if game.daytime:
                        cho @ cheeks blush "Bye then!" ("open", "happyCl", "base", "downR")
                    else:
                        cho "Good night then!" ("base", "base", "base", "mid")

                    call cho_walk(action="leave")

                    gen "(Heh. She's silly... but adorable.)" ("base", xpos="far_left", ypos="head")
                    gen "(Not the worst of combinations.)" ("base", xpos="far_left", ypos="head")
                    #Cho leaves
                    #End Scene #Marks at completed
                    $ states.cho.status.gokkun = True

        "-Just cum down her throat-":
            $ states.cho.ev.suck_it.variant = "throat"
            gen "That did it, you slut!"

            $ camera.set_image("cho_bj topless suck medium up")

            cho "*Hmmf*?" #looks at genie
            gen "{size=+4}*ARGH*!{/size}"

            with vpunch
            $ camera.set_image("cho_bj topless cum swallow")

            cho "*Mphhhh*!!!{w=1.0}{nw}"

            $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)

            gen "*Ahhh*... I needed that..."

            $ camera.set_imagepath("cho_bj/kneel/")
            $ camera.set_image("topless_mid_cough_cum_swallow")

            cho "*Cough*-*Cough*-...*Ah*...{w=0.4}*Ah*..."
            gen "That was awesome... Great job--"

            $ camera.set_image("topless_up_angry_cum_swallow")

            cho "What...{w=0.4} the hell...{w=0.4} is wrong with you?!?!" #screen shake
            gen "What do you--"

            $ camera.set_image("topless_up_angry2_cum_swallow")

            cho "Why didn't you warn me! I almost choked!"
            cho "I never agreed to this--"
            gen "It's sort of expected with a blowjob..."

            $ camera.set_image("topless_closed_angry_cum_swallow")

            $ camera.set(zoom=0.6, pos=(220, 180), t=5.0)

            cho "You asshole!"

            show screen blkfade
            with d5

            cho "For a first blowjob?! It is not!"
            gen "I mean...{w=0.4} Wait did you say first... Does that mean you still want to--"
            $ cho.wear("all")
            play sound "sounds/cloth_sound2.ogg"
            cho "I can't believe you..."

            hide screen animatedCG
            hide screen blkfade
            with fade

            #Cut to office screen #Cho has put on her top
            gen "As I said, it's kind of expected from the whole blowjob thing..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "You...{w=0.4} You're joking, right?" ("clench", "narrow", "angry", "mid", trans=d3)
            gen "Deadly serious..." ("base", xpos="far_left", ypos="head")
            gen "Unless I fancy covering your face that is..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Unless you--" ("soft", "wide", "angry", "mid") #disgust
            cho @ cheeks blush "*Humph*!" ("upset", "base", "angry", "mid")

            # Gets upset
            $ states.cho.mood += 12

            cho @ cheeks blush "I'm going to go take a shower now if you don't mind!" ("mad", "base", "angry", "mid")
            gen "You're dismissed [name_cho_genie]." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Good!" ("annoyed", "base", "angry", "mid")
            call cho_walk("door", "base")
            cho @ cheeks heavy_blush "{size=-4}Seriously... Just ask first...{/size}" ("disgust", "base", "angry", "down", flip=True, trans=d3) #Small text #Pout #Blush

            call cho_walk(action="leave")
            $ states.cho.status.gokkun = True

    jump end_cc_pf_blowjob

label cc_pf_blowjob_T3_E3:

    call cc_pf_blowjob

    $ states.cho.ev.suck_it.T3_E3_complete = True

    gen "Let's see what that mouth can do." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "You want to...{w=0.4} use my mouth again [name_genie_cho]?" ("soft", "narrow", "base", "downR")
    cho @ cheeks blush "I suppose I could..." ("open", "narrow", "base", "down") #Blush #Horny

    if states.cho.ev.suck_it.variant == "points":
        gen "And this time I won't make the mistake of offering house points..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "You better not." ("annoyed", "narrow", "base", "downR")
        gen "But my expectations are still the same..." ("base", xpos="far_left", ypos="head")
        gen "For you to push your limits on your own..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "So you want me to..." ("soft", "base", "base", "downR")
    elif states.cho.ev.suck_it.variant == "taste":
        gen "And if you don't want those clothes dirty, you better swallow this time..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("annoyed", "narrow", "base", "downR") #blush
    elif states.cho.ev.suck_it.variant == "swallow":
        cho @ cheeks blush "You expect me to swallow again?" ("open", "base", "base", "downR")
        gen "Of course, that's part of the deal..." ("base", xpos="far_left", ypos="head")
    else: # states.cho.ev.suck_it.variant == throat - Using `else` as a fallback for degenerates that use cheats
        cho @ cheeks blush "Will you warn me this time?" ("annoyed", "narrow", "base", "downR")
        gen "Of course..." ("base", xpos="far_left", ypos="head")

    cho @ cheeks blush "Fine..." ("base", "narrow", "base", "R")
    gen "Good! And one more thing..." ("base", xpos="far_left", ypos="head")
    gen "I expect some dirty talk this time." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Dirty talk, [name_genie_cho]?" ("upset", "base", "raised", "mid") #pout
    cho @ cheeks blush "I... If that's what you want..." ("soft", "base", "base", "downR") #Blush
    gen "Good, then get over here..." ("base", xpos="far_left", ypos="head")

    call cho_walk("desk_close", "base")
    pause 1.0

    # Start CG with Cho kneeling in front of Genie.
    # Cho is dressed.

    $ camera.set_imagepath("cho_bj/kneel/")
    $ camera.set_image("mid")
    if game.daytime:
        $ camera.set_overlay("day_overlay")
    else:
        $ camera.set_overlay("night_overlay")
    $ camera.set(zoom=0.5, pos=(100, 100), initialize=True)

    show screen animatedCG
    with fade

    pause 1

    $ camera.set_image("up_neutral")

    cho "Did you want me to take my top off again [name_genie_cho]?"
    gen "Taking initiative, *huh*? I like it."

    $ camera.set_image("up_smile")

    cho "In that case...{w=0.4} Just relax [name_genie_cho] and I'll take care of you..."

    play sound "sounds/cloth_sound3.ogg"
    $ camera.set_image("topless_mid_dreamy", trans=Fade(0.5, 2.0, 0.5))

    #Cho moves up closer
    cho "..."
    cho "Your--{w=0.4} Your cock is so big [name_genie_cho]!"
    gen "That's it [name_cho_genie], keep talking just like that..."
    gen "Put your hand on it and tell me how it feels..."

    $ camera.set_imagepath("cho_bj/hj/")
    $ camera.set_image("topless_mid_dreamy")

    #Cho grabs genies dick
    cho "It...{w=0.4} it feels like I'm holding a beater's bat!"
    cho "I can't believe how hard it is..."

    #Cho starts jacking genie off #Looking at dick
    $ camera.set_image("cho_hj topless mid smile")

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "Do you like it when I stroke your cock, [name_genie_cho]?" #Looks at genie
    gen "Very much so!"
    cho "*Mhmmm* Good answer. {heart}"

    $ camera.set_image("cho_hj topless mid smile")

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "Although this is far too slow, let's pick up the pace a little..."#Looks at genie

    $ camera.set_image("cho_hj topless mid smile fast")

    gen "*Ahh* You make me proud, [name_cho_genie]...{w=0.3} I've taught you well."

    $ camera.set_image("cho_hj topless up blush")

    cho "Thank you, [name_genie_cho]... It's my pleasure. {heart}" #Worried #Looks at dick

    $ camera.set_image("cho_hj topless mid smile fast")

    gen "*Ahh*...{w=0.3} Pleasure's all mine, [name_cho_genie]."

    call ctc

    $ camera.set_image("cho_hj topless up blush")

    cho "You've been such a help to me, [name_genie_cho]."

    $ camera.set_image("cho_hj topless up blush")
    cho "I would never have been able to get this far without you..."

    gen "That's it, [name_cho_genie], keep talking..."

    $ camera.set_image("cho_hj topless mid smile")

    cho "I love how your cock barely fits in my hand..."
    cho "And the feeling as it goes in and out of my mouth..."

    $ camera.set_image("cho_hj topless up blush")

    cho "And when it twitches happily... It makes me glad, knowing I am making you feel good..."

    $ camera.set_image("cho_hj topless mid smile")

    cho "The look of pleasure on your face once you cum in my mouth..."
    if states.cho.ev.suck_it.variant in ("swallow", "throat"):
        cho "The sensation of your jizz going down my throat, is so..." #Looks at dick

        $ camera.set_image("cho_bj topless lick success")
        pause 1
        $ camera.set_image("topless_mid_dreamy")

        "addicting! {heart}{heart}"
    elif states.cho.ev.suck_it.variant == "points":
        cho "To finally feel your jizz slide down my throat, I..."

        $ camera.set_image("cho_bj topless lick success")
        pause 1
        $ camera.set_image("topless_mid_dreamy")

        "can't wait! {heart}{heart}"

    else:
        cho "And the taste of your jizz is so..."

        $ camera.set_image("cho_bj topless lick success")
        pause 1
        $ camera.set_image("topless_mid_dreamy")

        "delicious! {heart}{heart}"

    gen "(If she keeps going like this, I'll blow before the actual blowjob...)"

    $ camera.set_image("topless_up_blush2")

    cho "Will you let me put my lips around it now, [name_genie_cho]?" #Looks at genie
    gen "Perhaps..."

    $ camera.set_image("topless_up_worried")

    cho "... Perhaps?"  #Looks at genie
    gen "Tell me you want it..."

    $ camera.set_image("topless_up_blush2")

    cho "[name_genie_cho]?"
    gen "Tell me how badly you want--{w=0.2} No, how badly you {i}need{/i} cock in your mouth."

    $ camera.set_image("topless_up_cringe")

    cho "How badly I n-need...!?"

    $ camera.set_image("topless_away_pout")

    cho "......"
    cho "(I-I don't need his cock... I think...)"

    $ camera.set_image("topless_away_blush")

    cho "(But...)"

    $ camera.set_image("topless_mid_dreamy")

    cho "(*Ah*{heart}{heart}{heart})"
    gen "Well then?"

    $ camera.set_image("topless_up_wide")

    #Cho stops stroking but still holding genies cock #looking at cock
    cho "I...{w=0.4} I want..."

    $ camera.set_image("topless_away_blush")

    cho "I need..."

    $ camera.set_image("topless_mid_dreamy")

    gen "Go on..."

    $ camera.set_image("topless_up_blush2")

    cho "I need your cock in my mouth...{w=0.2} And I need to feel your cum going down my throat..."
    gen "(She sure is a quick learner...)"
    gen "That's it [name_cho_genie]... Now work that mouth of yours for your reward..."

    $ camera.set_image("topless_mid_dreamy")

    cho "*Ah* Thank you, [name_genie_cho]..." #Blushes

    $ camera.set_image("cho_bj topless suck medium start")
    pause 2
    $ camera.set_image("cho_bj topless suck medium")

    call ctc

    gen "*Mhm*... Suck that cock like it's the only thing between you and winning that cup..."
    #Cho looks up at genie as she's sucking and starts going faster.

    $ camera.set_image("cho_bj topless suck medium up")

    gen "Your coach will soon reward you for all of your efforts..."

    $ camera.set_image("cho_bj topless suck deep")

    cho "*glick* *glick* *glick*" #Looks back down on cock
    gen "*Argh*! You slut, I'm almost there..."

    call ctc

    $ camera.set_image("cho_bj topless suck closed exit")
    gen "What--{w=1.0}{nw}"
    pause 2.0

    #Cho suddenly pulls out
    $ camera.set_image("cho_hj topless up")

    gen "I didn't say you could--"
    cho "Cum for me [name_genie_cho]!"

    $ camera.set_image("cho_hj topless up blush")

    cho "I need to taste your delicious cum down my throat!"
    cho "I need to swallow it all!"

    $ camera.set_image("cho_bj topless suck deep start")
    pause 1
    $ camera.set_image("cho_bj topless suck deep")

    call ctc

    gen "That's it [name_cho_genie], get ready for your reward!"

    $ camera.set_image("cho_bj topless suck medium")

    call ctc

    $ camera.set_image("cho_bj topless suck medium up")

    gen "Open up [name_cho_genie], here it comes!" #large text
    gen "*ARGH!*"

    with vpunch
    $ camera.set_image("cho_bj topless cum mouth")
    pause 0.5
    $ camera.set(zoom=0.45, pos=(150, 70), t=1.0)
    pause 1.5
    $ camera.set_imagepath("cho_bj/kneel/")
    $ camera.set_image("topless_mid_cum_mouth")

    pause 1

    gen "*Ah*..." #Genie pulls out

    call ctc

    $ camera.set_image("topless_mid_full_worried2")

    gen "Don't swallow yet!"

    cho "*Mfff*..." #Mouth full
    gen "Good...{w=0.4} Now play with it with your tongue."

    $ camera.set_image("topless_mid_full_worried")
    cho "....{w}......{w}....."
    gen "Now you can swallow."
    pause 1

    $ camera.set_image("topless_mid_full_angry")

    pause 1
    play sound "sounds/gulp.ogg"
    $ camera.set_image("topless_mid_full_swallowed2", trans=d5)
    pause 1.5
    $ camera.set_image("topless_mid_full_swallowed")

    gen "I hope you liked your reward."
    gen "On your feet, [name_cho_genie]."

    $ camera.set(zoom=1.0, pos=(300, 400), t=5.0, pause=True)

    # Set cum on doll and strip her
    $ cho.set_cum(face="light")
    $ cho.strip("robe", "top", "bra")

    hide screen animatedCG
    with fade

    if states.cho.ev.suck_it.variant in ("taste", "points"):
        cho @ cheeks blush "I...{w=0.4} I did it...{w=0.4} I swallowed your cum [name_genie_cho]." ("base", "happyCl", "base", "mid", trans=d3)
        gen "As expected." ("base", xpos="far_left", ypos="head")
        gen "But an improvement from last time nevertheless..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Thank you [name_genie_cho]..." ("base", "narrow", "base", "down")
    elif states.cho.ev.suck_it.variant == "swallow":
        cho @ cheeks blush "I...{w=0.4} I hope you liked it [name_genie_cho]." ("base", "narrow", "base", "down", trans=d3)
    else: # states.cho.ev.suck_it.variant == throat - Using `else` as a fallback for degenerates that use cheats
        cho @ cheeks blush "I...{w=0.4} I did it..." ("base", "narrow", "base", "down", trans=d3)
        gen "And without my help this time." ("base", xpos="far_left", ypos="head")

    cho @ cheeks blush "Your...{w=0.4} Your cum...{w=0.4} was delicious [name_genie_cho]..." ("soft", "closed", "base", "mid")
    gen "That's right [name_cho_genie]... and if you keep doing such a good job there's even more where that came from..." ("grin", xpos="far_left", ypos="head")
    gen "You can stop talking dirty now." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "I wasn't--" ("open", "narrow", "base", "down") #blush, looking right
    cho @ cheeks heavy_blush "Yes, [name_genie_cho]..." ("upset", "narrow", "base", "R")
    cho @ cheeks blush "So...{w=0.4} Is that all?" ("soft", "narrow", "base", "R")
    gen "For now..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Okay then..." ("soft", "base", "base", "mid")

    play sound "sounds/cloth_sound2.ogg"
    $ cho.wear("all")
    $ cho.set_cum(None)
    with fade

    if game.daytime:
        cho @ cheeks blush "In that case, I'll head back to class." ("open", "base", "base", "R")
    else:
        cho "I'll head back to my dorms then..." ("base", "base", "base", "mid")
    gen "Of course...{w=0.4} you better be ready for next time..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Next...{w=0.4} Yes [name_genie_cho]..." ("horny", "narrow", "base", "down")
    call cho_walk("door", "base")
    cho @ cheeks heavy_blush "(He's so commanding...)" ("horny", "narrow", "base", "R", flip=True, trans=d3) # horny
    if states.her.status.blowjob:
        cho @ cheeks heavy_blush "(No wonder why Hermione is doing this...)" ("horny", "closed", "base", "mid")
    gen "[name_cho_genie]." ("base", xpos="far_left", ypos="head")

    call cho_chibi("stand", "door", "base", flip=False)
    cho "" (flip=False, trans=d5)

    cho @ cheeks heavy_blush "Yes... Sorry!" ("mad", "base", "base", "L") #Heavy Blush
    cho @ cheeks heavy_blush "Bye then!" ("soft", "happyCl", "base", "mid") #Heavy Blush

    call cho_walk(action="leave")

    pause 1

    gen "(Turns out I'm a better coach than I gave myself credit for.)" ("base", xpos="far_left", ypos="head")
    gen "(Time for the next step!)" ("grin", xpos="far_left", ypos="head")

    $ states.cho.status.gokkun = True

    jump end_cc_pf_blowjob
