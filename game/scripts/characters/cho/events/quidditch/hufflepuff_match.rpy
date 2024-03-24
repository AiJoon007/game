
# Ravenclaw vs. Hufflepuff

label start_hufflepuff_match:
    # Chat with Cho the day before the match

    cho "" (xpos="mid", ypos="base", trans=fade)
    gen "[name_cho_genie], what do you say... ready for your first game of the season?" ("base", xpos="far_left", ypos="head")
    cho "To be honest, [name_genie_cho], I'm feeling quite nervous." ("soft", "base", "worried", "R")
    gen "Don't worry. I believe you are ready..." ("base", xpos="far_left", ypos="head")
    gen "When are you going to play against Hufflepuff?" ("base", xpos="far_left", ypos="head")
    cho "That's up to you, [name_genie_cho]. As headmaster, you decide when the games will be held..." ("open", "base", "base", "mid")
    gen "So if I were to say tomorrow, it will happen tomorrow?" ("base", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]." ("base", "base", "base", "mid")
    gen "Well then, tomorrow it is!" ("grin", xpos="far_left", ypos="head")

    if game.weather in {"rain", "storm"}:
        cho "Sounds great, [name_genie_cho]. I just hope it stops raining before then." ("soft", "base", "base", "R")
    elif game.weather in {"snow", "blizzard"}:
        cho "Sounds great, [name_genie_cho]. I just hope it stops snowing before then." ("soft", "base", "base", "R")
    elif game.weather == "overcast":
        cho "Sounds great, [name_genie_cho]. I just hope the weather doesn't get worse." ("soft", "base", "base", "R")
    else:
        cho "Sounds great, [name_genie_cho]. I just hope the weather stays like it is." ("soft", "base", "base", "R")

    gen "With our tactics, this will be a piece of cake!" ("base", xpos="far_left", ypos="head")
    cho "I hope you're right, [name_genie_cho]." ("base", "base", "base", "mid")
    cho "Anyhow, I need to prepare for the game." ("soft", "base", "base", "R")
    cho "See you then, [name_genie_cho]!" ("smile", "base", "base", "mid")
    gen "Good luck!" ("base", xpos="far_left", ypos="head")

    call cho_walk(action="leave")

    $ states.cho.ev.quidditch.lock_training = True
    $ states.cho.ev.quidditch.lock_practice = True

    $ cc_event_pause  += 1 # Event starts on the next day
    $ cc_summon_pause += 1 # Can't be summoned until next event

    $ states.cho.busy = True

    $ states.cho.ev.quidditch.hufflepuff_stage = "start"

    jump end_cho_event


label hufflepuff_match:
    # Quidditch match: Ravenclaw vs. Hufflepuff

    $ cho_outfit_last.save()
    $ her_outfit_last.save()

    $ cho.equip(cho_outfit_quidditch)
    $ hermione.equip(her_outfit_default)

    stop music fadeout 1

    # Start in the office
    call sna_walk(action="enter", xpos="mid", ypos="base")
    pause .5

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    sna "Are you ready to go?" ("snape_03", xpos="base", ypos="base")
    gen "Can't you bloody knock?!" ("angry", xpos="far_left", ypos="head")
    sna "Should I?{w=0.3} I was sure you were already waiting for me..." ("snape_05")
    gen "For what?" ("base", xpos="far_left", ypos="head")
    sna "We have to head out for the pitch. The whole school is waiting on you." ("snape_24")
    gen "Didn't you nag me earlier not to leave this room unless absolutely necessary?" ("base", xpos="far_left", ypos="head")
    sna "A rule which I'm sure you have disregarded a great many times already..." ("snape_29")
    sna "You'll have to join me on this one. As headmaster, you are expected to attend the Quidditch matches." ("snape_06")
    gen "And that's today?" ("base", xpos="far_left", ypos="head")
    sna "Indeed." ("snape_03")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "Wouldn't the other teachers see me if I went?" ("base", xpos="far_left", ypos="head")
    sna "Don't worry. I've arranged to have us moved from the teachers' seats to the commentator booth." ("snape_24")
    sna "Just the two of us..." ("snape_23")
    gen "And Miss Granger?" ("base", xpos="far_left", ypos="head")
    sna "Granger..." ("snape_08")
    sna "Well, that's very displeasing to say the least..." ("snape_07")
    sna "In any case, you won't be seen up close by any of the other teachers." ("snape_09")
    gen "Sounds like a snore. Can't I stay here, and you'll tell them I'm ill or something?" ("base", xpos="far_left", ypos="head")
    sna "No." ("snape_04")
    sna "That would just prompt the nurse to examine you closely..." ("snape_03")
    gen "Well... I wouldn't mind that." ("base", xpos="far_left", ypos="head")
    sna "I'm sure you wouldn't..." ("snape_06")
    sna "Good thing though is that we'll be able to bring a little something to keep us occupied." ("snape_20")
    call hide_characters
    with d3

    # Show wine
    call give_reward(text=">Not grape-juice.", gift="interface/icons/wine.webp")

    gen "That's all the persuasion I needed, my friend!" ("base", xpos="far_left", ypos="head")
    hide screen bld1
    with d3
    pause .2

    # Teleport to door
    play sound "sounds/kick.ogg"
    call gen_chibi("hide")
    with d3

    call gen_chibi("stand", "door", "base")
    call teleport(position="genie", effect=False)
    pause .5

    call gen_chibi("stand", "door", "base", flip=False)
    with d3
    pause .2

    call bld
    gen "What are we waiting for. Let's go!" ("base", xpos="far_left", ypos="head")

    call sna_chibi("stand", "mid", "base", flip=True)
    with d3
    pause .2

    sna "(When did he?...)" ("snape_05", ypos="head")
    sna "After you..." ("snape_09", ypos="head")
    pause .8

    gen "Actually, I have no idea where we're going." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", "door", "base")
    with d3
    pause .2

    call bld
    gen "You should lead the way..." ("base", xpos="far_left", ypos="head")
    sna "Right you are. Time to get smashed!" ("snape_02", ypos="head")

    call sna_walk(700, "base")

    # Blackfade
    stop music fadeout 2
    stop background fadeout 2
    play sound "sounds/door.ogg"
    call blkfade
    pause 2

    nar "You make your way towards the pitch with Snape, pondering if this was such a good idea."
    play sound "sounds/steps_grass.ogg"
    nar "After walking for a while across the school grounds, a huge oval-shaped pitch with massive towers around it looms before you."
    nar "Amazed by...{w=0.6}{nw}"
    gen "Agrabah towers are larger..." ("base", xpos="far_left", ypos="head")
    nar "Amazed... by the sight, Snape then leads you to the base of one of the towers."

    # Pitch entrance
    centered "{size=+7}{color=#cbcbcb}At the Quidditch pitch...{/color}{/size}"

    call room("quidditch_pitch")
    play background "sounds/outskirts.ogg" fadein 2
    call sna_chibi("stand", "right", "base")
    call gen_chibi("stand", "mid", "base", flip=True)
    call hide_blkfade
    pause .8

    call bld
    gen "So, this is it? This is where the quidditch is played?" ("base", xpos="far_left", ypos="head")
    sna "Of course, did you expect something else?" ("snape_05", ypos="head")
    gen "I mean... What's the point of the grass and sand? Isn't it played in the air?" ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_25", ypos="head")
    gen "Wouldn't it make more sense to have the ground be something soft if they fall?" ("base", xpos="far_left", ypos="head")
    gen "Like...{w=0.3} magic marshmallow or something..." ("grin", xpos="far_left", ypos="head")
    sna "You think there's a spell for everything?" ("snape_35", ypos="head")
    gen "From previous experiences with this world so far...{w} yes, pretty much." ("base", xpos="far_left", ypos="head")
    sna "Anyhow... time to get moving.{w=0.6} This place will be filled with teachers and students any minute now." ("snape_03", ypos="head")
    sna "After me..." ("snape_02", ypos="head")

    call sna_walk(path=[("stairs_base", "base"),("stairs_up", "stairs_up")])
    call gen_walk(650)
    call chibi_emote("exclaim", "genie")
    pause 0.3

    call chibi_emote("hide", "genie")
    call gen_chibi("stand_alt")
    with d3
    pause 0.5

    call bld
    gen "(*He-heh*... \"Snape sux\"...)" ("grin", xpos="far_left", ypos="head")
    call gen_chibi("stand")
    call gen_walk(path=[("stairs_base", "base"),("stairs_up", "stairs_up")])

    call blkfade

    # Sound check
    if get_volume_preference('music') < 0.1 or get_volume_preference('sfx') < 0.1:
        nar "This section of the game is best played with the sound turned on. Go to preferences to set the volume."

    pause 1

    # Quidditch stands
    call room("quidditch_stands")
    call quidditch_stands(crowd=crowd_mid)

    ### Snape Chibi Postions ###
    # First Step R:     call sna_chibi("stand", flip=True, 25, 234)
    # Second Step R:    call sna_chibi("stand", flip=True, 85, 260)
    # Third Step R:     call sna_chibi("stand", 120, 295, flip=True)
    # Fourth Step R:    call sna_chibi("stand", flip=True, 160, 330)

    ### Genie Postions ###
    ## Sprite:          call gen_main(face="base", base="base", xpos=-10, ypos=140)
    # First Step Mid:   call gen_chibi("stand", flip=True, -20, 270)
    # Second Step L:    call gen_chibi("stand", flip=True, -20, 320)
    # Second Step Mid:  call gen_chibi("stand", flip=True, 0, 360)
    # Third Step L:     call gen_chibi("stand", 20, 365, flip=True)
    # Third Step Mid:   call gen_chibi("stand", 65, 340, flip=True)
    # Floor Mid:        call gen_chibi("stand", flip=True, 170, 400)
    # Podium:           call gen_chibi("stand", 280, 400, flip=True)

    ### Hermione Postions ###
    ## Sprite:          her "" (flip=True, xpos=290, ypos="base")
    # Second Step Mid:  call her_chibi("stand", 40, 295, flip=True)
    # Floor Mid:        call her_chibi("stand", flip=True, 180, 400)
    # Podium:           call her_chibi("stand", 300, 400, flip=True)
    # Podium Sidestep:  call her_chibi("stand", 260, 460, flip=True)

    ### Tonks Positions ###
    # 1st Step R:       call ton_chibi("stand", flip=True, 55, 235)
    # 4th Step R:       call ton_chibi("stand", flip=True, 180, 340)
    # Floor mid:        call ton_chibi("stand", flip=True, 180, 400)
    # Floor R:          call ton_chibi("stand", flip=True, 230, 370)
    # Podium:           call ton_chibi("stand", flip=True, 300, 400)
    # Sitting:          call ton_chibi("sit", flip=True, xpos=-140, ypos=125)

    ### Cho Positions ###
    ## Flying Sprite:   call cho_main(xpos=580, ypos=-200)
    # Flying Chibi:     call cho_chibi("fly", 530, 360)

    $ snape_chibi.zorder = 2
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 4

    # Match starts
    play background "sounds/crowd.ogg" fadein 2
    call hide_blkfade
    pause 1

    play sound "sounds/footsteps.ogg"
    pause .8

    call sna_chibi("stand", 120, 295, flip=True)
    with d3
    pause .8
    call sna_chibi("stand", flip=False)
    with d3

    sna "Careful at the top. Don't hit your head." ("snape_35", ypos="head")
    play sound "sounds/kick.ogg"
    with hpunch
    pause .6
    gen "Bloody hell!" ("angry", xpos="far_left", ypos="head")
    play sound "sounds/footsteps.ogg"
    pause .8
    call gen_chibi("stand", 20, 365, flip=True)
    with d3
    pause .5
    call sna_chibi("stand", flip=True)
    with d3
    sna "Well, here we are..." ("snape_09")
    sna "Now we are only waiting for--" ("snape_03")
    play sound "sounds/footsteps.ogg"
    call her_chibi("stand", 40, 295, flip=True)
    with d3
    pause .5
    call sna_chibi("stand", flip=False)
    with d3
    pause .2
    her "Professors." ("open", "closed", "base", "mid", ypos="head", flip=True)
    sna "Granger..." ("snape_35")
    call sna_chibi("stand", flip=True)
    with d3
    pause .2

    call her_walk(path=[(180, 400),(300, 400)])
    call her_chibi("stand", 300, 400, flip=True) # Temp Bugfix
    pause .5

    her "Good Morning everyone, and welcome to the i-inaugural--" ("soft", "base", "worried", "mid", flip=True, xpos=290, ypos="base", trans=d3)
    her "" ("normal", "base", "worried", "mid")
    sna "Speak up girl! And would it kill you to enunciate?!" ("snape_03", ypos="head")
    her "*Grrr*" ("mad", "narrow", "angry", "R")
    her "" ("open", "closed", "angry", "mid")
    her "Welcome to the first Quidditch game of the season...{fast}" ("open", "base", "worried", "mid")

    call quidditch_stands(crowd=crowd_full)
    with d5
    sna "Better... You've advanced from Troll to Dreadful..." ("snape_09", ypos="head")
    her "" ("normal", "closed", "base", "mid")
    gen "{size=-4}Troll?{/size}" ("base", xpos="far_left", ypos="head")
    sna "{size=-4}Those are grades we give out to our students, for decidedly poor performances, like Granger's...{/size}" ("snape_01", ypos="head")
    her "..." ("mad", "base", "angry", "mid")
    with hpunch

    stop background fadeout 4

    her "{size=+5}Quiet Please!{/size}" ("scream", "base", "angry", "mid")
    her "..." ("normal", "closed", "angry", "mid")

    play background "sounds/crowd_low.ogg" fadein 2

    her "Thank you..." ("open", "happy", "base", "mid_soft")
    her "L-let's begin!" ("base", "base", "base", "mid")

    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    her "Hufflepuff versus Ravenclaw!" ("smile", "base", "base", "mid_soft")

    call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])
    with d3

    play sound "sounds/crowd_cheer.ogg"
    nar "A loud cheer roars from the grandstands."

    # Speech
    her "And now, to say a few words and declare the games open, Professor Dumbledore!" ("open", "closed", "base", "mid")
    her "" ("base", "base", "base", "mid_soft")
    call ctc

    hide hermione_main
    with d3

    gen "{size=-4}What? Isn't that me?{/size}" ("base", xpos="far_left", ypos="head")
    sna "It is." ("snape_02", ypos="head")

    call quidditch_stands(crowd_react=[None, "emo7", "emo8"])
    with d3

    gen "Why did no one warn me about this?" ("base", xpos="far_left", ypos="head")

    call quidditch_stands(crowd_react=[None, None, "emo8"])
    with d3

    sna "I've been looking forward to watching you bumble your way through this..." ("snape_22", ypos="head")

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    sna "Besides, you only have to give some trivial speech about team spirit, gesticulate wildly and say \"let the games begin\". A child could manage it." ("snape_24", ypos="head")
    sna "Now get up there!" ("snape_10", ypos="head")

    stop background fadeout 4
    stop music fadeout 2

    $ hermione_chibi.zorder = 4
    $ genie_chibi.zorder = 3
    #call her_chibi("stand",350,185+186, flip=True)
    call her_chibi("stand", 260, 460, flip=True)
    with d3
    pause .5

    call gen_chibi("stand", 65, 340, flip=True)
    with d3

    call gen_walk(path=[(170, 400),(280, 400)])
    call gen_chibi("stand", 280, 400, flip=True) # Temp Bugfix
    with d3
    pause .5

    $ states.gen.image.zorder = 15

    show screen blktone
    with d5
    pause 1.0
    gen "" ("base", xpos=0, ypos="base")
    show genie zorder states.gen.image.zorder
    with d3
    pause 2.0

    gen "" ("angry")

    menu:
        "(Shit, what do I even talk about?)"
        "-Miracles-":
            play background "music/fanfare.ogg" fadein 1.0
            gen "Great moments are born from great opportunity." ("base")
            nar "A reverent hush falls over the crowd..."
            gen "And that's what you have here tonight--" ("base")
            gen "That's what you've earned here tonight!" ("base")

            pause .8
            play sound "sounds/killswitch_on.ogg"
            hide screen blktone
            call quidditch_stands(spotlight=True)
            with d1
            pause .8

            show genie zorder states.gen.image.zorder
            with d3
            gen "One game..." ("base")
            gen "Tonight, WE are the greatest hockey team in the world!" ("base")
            gen "You were born to be hockey players..." ("base")
            gen "Every one of you..." ("base")

            call quidditch_stands(crowd_react=["emoq", None, None])
            with d3

            gen "And you were meant to be here tonight!" ("base")
            gen "This is your time..." ("base")

            gen "Their time is done, it's over! I'm sick and tired of hearing what a great hockey team the soviets have!" ("base")

            call quidditch_stands(crowd_react=["emoq", "qu", None])
            with d3
            pause 1.5

            mal "I think Dumbledore has finally started to lose his marbles..."
            mal2 "I think you might be right."
            play background "sounds/wind_long_loop.ogg" fadein 2 fadeout 2

            call quidditch_stands(crowd_react=["sur", None, None])
            with d3

            gen "Screw it! This is our time..." ("base")

            call quidditch_stands(crowd_react=["sal", None, None])
            with d3

            mal "..."
            play sound "sounds/cough_male.ogg"
            call quidditch_stands(crowd_react=["sal", "sal", None])
            with d3

            mal2 "..."
            call quidditch_stands(crowd_react=[None, None, None], spotlight=False)
            with d1

            play sound "sounds/killswitch_off.ogg"
            gen "Now let the games begin!" ("base")

        "-Freedom-":
            play background "music/fanfare.ogg" fadein 1.0
            gen "Sons of Scotland!" ("base")

            pause .8
            play sound "sounds/killswitch_on.ogg"
            hide screen blktone
            call quidditch_stands(spotlight=True)
            with d1
            pause .8

            gen "I am William Wallace..." ("base")

            call quidditch_stands(crowd_react=["qu", None, None])
            with d3

            nar "A confused murmur falls over the crowd."
            sna "{size=-4}William Wallace?{/size}" ("snape_05", ypos="head")
            gen "{size=-4}That's not your line...{/size}" ("angry")
            gen "Yes... I am William Wallace!" ("grin")
            gen "And I see a whole army of my countrymen, here in the defiance of tyranny..." ("grin")
            gen "You have come to fight as free men, and free men you are. What would you do with that freedom? Will you fight?" ("grin")

            play sound "sounds/murmur.ogg"
            call quidditch_stands(crowd_react=["qu", "emoq", None])
            with d3

            nar "The sound of confused murmuring increases even further..."
            mal "Fight? Against what?"
            gen "{size=-4}See, that guy knows his lines...{/size}" ("base")
            sna "..." ("snape_03")
            gen "Aye... fight, and you may die." ("base")

            call sna_chibi("stand", 230, 400, flip=True)
            with d3
            pause .2

            sna "I think it's time for you to step down from the..." ("snape_01")
            gen "No, I'm just about to get to the best part!" ("angry")
            play sound "sounds/cloth_sound.ogg"
            stop background fadeout 2.0

            hide genie
            call sna_chibi("stand", 210, 400, flip=True)
            call gen_chibi("stand", 260, 400, flip=True)
            with d3

            nar "Snape then begins to drag you away from the podium."
            play background "sounds/wind_long_loop.ogg"

            show genie zorder states.gen.image.zorder
            with d3
            gen "This is our chance... they may take away our microphones...{w=1.0} But they...{nw}{w=0.3}" ("angry")
            play sound "sounds/microphone_feedback.ogg"

            call sna_chibi("stand", 230, 400, flip=True)
            call gen_chibi("stand", 280, 400, flip=True)
            with d3

            gen "This is our chance... they may take away our microphones...{w=1.0} But they... {fast}But they...{w=0.5}{nw}" ("angry")

            call sna_chibi("stand", 190, 400, flip=True)
            call gen_chibi("stand", 240, 400, flip=True)
            with d3

            gen "But they'll never take away our freedom!" ("angry")

            hide genie
            call quidditch_stands(crowd_react=[None, None, None], spotlight=False)
            with d3

            play sound "sounds/killswitch_off.ogg"

            $ snape_chibi.zorder = 3
            $ genie_chibi.zorder = 2
            call sna_chibi("stand", 170, 400, flip=True)
            call gen_chibi("stand", 240, 400, flip=False)
            with d3

        "-Nam-":
            play background "sounds/wind_long_loop.ogg"

            pause .8
            play sound "sounds/killswitch_on.ogg"
            hide screen blktone
            call quidditch_stands(spotlight=True)
            with d1
            pause .8

            gen "{cps=7}Goooooooood{/cps}  morning,{w=0.1} Vietnam!" ("grin")
            gen "Hey, this is not a test... This is rock and roll!" ("grin")
            gen "Time to rock it from the delta to the DMZ!" ("grin")
            gen "Is that me, or does that sound like an Elvis Presley movie?" ("grin")

            call quidditch_stands(crowd_react=["sal", "emoq", None])
            with d3

            nar "A confused murmur falls over the crowd."
            gen "Ugh..." ("base")

            play sound "sounds/microphone_feedback.ogg"
            gen "Is this thing on?" ("base")

            call quidditch_stands(crowd_react=["sal", "sal", None])
            with d3
            play sound "sounds/cough_male.ogg"
            mal "..."

            call quidditch_stands(crowd_react=["emoq", "qu", None])
            with d3

            gen "It's O six hundred, what does the O stand for?" ("grin")
            gen "Ooooh my god it's early!" ("grin")

            play sound "sounds/murmur.ogg"
            nar "The sound of confused murmuring increases even further..."
            mal "What's he on about? Is the fire lit but the cauldron empty?"
            mal2 "Looks like it..."

            call quidditch_stands(crowd_react=[None, None, None], spotlight=False)
            with d1

            play sound "sounds/killswitch_off.ogg"

            gen "Tough crowd... Anyway, let the games begin!" ("base")

    hide genie
    with d3

    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    play background "sounds/crowd_low.ogg" fadein 3 fadeout 2
    play sound "sounds/crowd_cheer.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])
    with d3

    nar "After a moment of confusion, the crowd cheers excitedly, eager to see the match kick-off."

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    call gen_walk(path=[(170, 400),(65, 340)])

    $ snape_chibi.zorder = 2
    $ genie_chibi.zorder = 3
    call gen_chibi("stand", 20, 365, flip=True)
    call sna_chibi("stand", 120, 295, flip=True)
    with d5
    pause .2

    # Hermione commentates again
    $ hermione_chibi.zorder = 3
    call her_chibi("stand", 300, 400, flip=True)
    with d3
    pause .8

    her "Ugh... thank you for that, professor Dumbledore..." ("soft", "narrow", "base", "R_soft", flip=True, xpos=290, ypos="base", trans=d3)
    her "Now, to get this game underway!" ("open", "closed", "base", "mid")

    # Player introduction
    her "First, let's welcome everyone's favourite underdogs, Ravenclaw!" ("base", "happy", "base", "R")
    play sound "sounds/crowd_stomping.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", None])
    with d3

    her "" ("base", "base", "base", "mid")
    nar "The blue grandstand shakes violently with enthusiasm."
    sna "At least try to sound like you're awake, Miss Granger." ("snape_03", ypos="head")
    her @ cheeks blush "..." ("normal", "closed", "angry", "mid")

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    her @ cheeks blush "And coming onto the field to face them are the equally impressive, Hufflepuff!" ("open", "base", "base", "mid")
    play sound "sounds/crowd_cheer2.ogg"

    call quidditch_stands(crowd_react=[None, None, "emo8"])
    with d3

    her @ cheeks blush "" ("base", "base", "base", "mid")
    nar "The yellow grandstand bursts into a mix of applause and whistles."
    hide hermione_main
    with d3
    sna "Back down to Troll..." ("snape_09", ypos="head")

    call her_chibi("stand", flip=False)
    with d3
    pause .1

    her "*grrrrr*"

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    call her_chibi("stand", flip=True)
    with d3
    pause .1

    her "It appears we've got an interesting game ahead of us." ("open", "base", "base", "mid", flip=True, xpos=290, ypos="base", trans=d3)
    her "If I'm not mistaken, there's some history between our seekers, Cho Chang and Cedric Diggory..." ("crooked_smile", "closed", "base", "mid")
    her "" ("smile", "happy", "base", "mid_soft")
    nar "Even though they are far down below on the pitch, you can clearly see Cho and Cedric glaring up at Hermione."
    her "Given how essential the seeker's role is in Quidditch, their complex past might cost one of them the game..." ("open", "base", "base", "mid_soft")
    sna "Complex past..." ("snape_01", ypos="head")
    her "" ("base", "closed", "base", "mid")
    sna "I practically caught them chewing each other's tongues off at one point." ("snape_02", ypos="head")
    her "But before we begin, I just realised that as the inaugural game, I should cover the rules of the game for any first-years watching." ("open", "happy", "base", "R")

    # Reading the rules
    stop music fadeout 4
    stop background fadeout 2
    hide hermione_main
    with d3
    nar "Hermione heaves a heavy rulebook{nw}"
    play sound "sounds/punch01.ogg"
    nar "Hermione heaves a heavy rulebook{fast} from under the table and begins to monotonously recite it to the crowd."
    play sound "sounds/sniff.ogg"
    her "..."
    play background "sounds/wind_long_loop.ogg" fadein 2
    her "The capturing of the snitch is worth 150 points--" ("open", "narrow", "base", "down", flip=True, xpos=290, ypos="base", trans=d3)

    call quidditch_stands(crowd_react=["th", None, None])
    with d3
    play sound "sounds/murmur.ogg"

    her "The game may not conclude until it has been caught, or an agreement is made between both capt--" ("open", "base", "base", "mid")

    call quidditch_stands(crowd_react=["th", "an", None])
    with d3
    play background "sounds/crowd.ogg" fadein 8 fadeout 2
    hide hermione_main
    with d3

    mal "Just get on with it already you big-titted slag!"

    call quidditch_stands(crowd_react=["th", "an", "excl"])
    with d3

    mal2 "Yeah! Start the game!"
    qcr "START THE GAME! START THE GAME!"
    nar "Hermione's voice eventually gets drowned out by the growing restlessness of the crowd."
    her "" ("normal", "base", "base", "mid", xpos=290, ypos="base", flip=True)
    her "Ugh, fine...{w=0.3} If everyone wants us to begin play without knowing {b}a single thing{/b}...{w=0.8} then that's {b}OK!{/b}" ("annoyed", "narrow", "annoyed", "R", trans=d3)
    her "A good commentator knows when to accommodate for a crowd's impatience!" ("soft", "closed", "base", "mid")
    hide hermione_main
    with d3
    sna "{size=-4}This should be good.{/size}" ("snape_02", ypos="head") # Small text.

    play sound "sounds/crowd_cheer.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])
    with d3

    nar "With that, the snitch and bludgers are released and fly off into the air."

    call quidditch_stands(crowd_react=[None, None, None])
    with d3
    play background "sounds/crowd_low.ogg" fadein 0.5 fadeout 0.5
    her @ cheeks blush "Now then..." ("open", "closed", "base", "mid", flip=True, xpos=290, ypos="base", trans=d3)
    her @ cheeks blush "Let's begin!" ("base", "happy", "base", "mid_soft")
    hide hermione_main
    with d3
    pause .1

    # Start of the game
    play sound "sounds/referee.ogg"
    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    nar "A fit looking woman then throws the quaffle into the air -- which signals the start of the match -- and the players quickly take off!"

    her "Oh, wow... They're going quite f-fast..." ("normal", "wide", "worried", "shocked", flip=True, xpos=290, ypos="base", trans=d3)
    her "" ("normal", "happyCl", "base", "mid")
    sna "Great commentary there girl... You might want to let them know the colour of the grass next..." ("snape_10", ypos="head")
    play sound "sounds/ball_hit.ogg"
    her "*Umm*, I'm not sure if anyone's scored yet..." ("normal", "happy", "base", "mid")
    her "Wait, that guy has the quaffle... I think..." ("open", "squint", "base", "mid")
    her "Scratch that last bit, he has a stick, so he must be a beater!" ("mad", "happy", "base", "mid")
    sna "{size=-4}Good grief...{/size}" ("snape_05", ypos="head")

    pause .5

    her "Higher up, Cho seems to have caught an eye on the snitch and is chasing after it, directly followed by Cedric who..." ("open", "slit", "low", "stare", flip=True)
    her "Hold on a minute... Is Cho wearing a skirt?" ("scream", "wide", "worried", "stare")

    show image "CG quidditch cho_flashing" as cg zorder 17
    with fade

    play sound "sounds/crowd_gasp.ogg"
    call quidditch_stands(crowd_react=["emo02", "excl", "sur"])
    with d3

    call ctc

    her @ cheeks blush "" ("open", "wide", "worried", "shocked")
    qcr "!!!" # [screenshake?]
    play background "sounds/crowd.ogg" fadein 2
    mal "..."
    play sound "sounds/murmur.ogg"
    her @ cheeks blush "" ("open", "happyCl", "base", "mid")
    mal "She totally is!"
    play sound "sounds/giggle2_loud.ogg"
    hide hermione_main
    with d3
    fem "What a slut!"
    call ctc

    # Pack to stands.
    hide image cg
    with fade
    pause .1

    call her_chibi("stand", flip=False)
    with d3
    pause .3

    her "Professor, why won't you say something?{w=0.8} She's clearly breaking the very basics of Quidditch rules!" ("clench", "narrow", "angry", "mid", ypos="head", flip=False)
    gen "I fail to see anything wrong with the way she's dressed." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But... she's wearing a skirt!" ("clench", "wide", "base", "stare")
    her "Surely that must be against some kind of regulation..." ("annoyed", "narrow", "angry", "mid")
    gen "You tell me Miss Granger, you've got the rulebook right there..." ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_13", ypos="head")
    her "Perhaps I could get Madam Hooch to pause the game..." ("open", "closed", "annoyed", "mid")
    pause .1

    call her_chibi("stand", flip=True)
    with d3
    pause .3

    sna "Knowing her, she's probably enjoying the sight of the Ravenclaw seeker rushing past her." ("snape_20", ypos="head")
    sna "{size=-4}Odds are she's already tried to take a peek.{/size}" ("snape_20", ypos="head")
    gen "{size=-4}Who's Madam Hooch?{/size}" ("base", xpos="far_left", ypos="head")
    sna "{size=-4}It's that fit lady on the pitch who is seemingly unable to take her eyes off the underside of miss Chang's... undergarments.{/size}" ("snape_09", ypos="head")
    sna "{size=-4}Great idea with the skirt, if I might add.{/size}" ("snape_13", ypos="head")
    gen "{size=-4}You're welcome.{/size}" ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_12", ypos="head")
    play sound "sounds/ball_hit.ogg"
    sna "{size=-4}She is wearing something underneath I assume?{/size}" ("snape_13", ypos="head")
    gen "For now..." ("base", xpos="far_left", ypos="head")
    sna "Excellent..." ("snape_22", ypos="head")

    play sound "sounds/wolf_whistle.ogg"

    call quidditch_stands(crowd_react=["emo8", "excl", "sur"])
    with d3

    mal "Cho, show us your panties!"

    play sound "sounds/giggle2_loud.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "sur"])
    with d3

    fem "We want to see them!"

    play sound "sounds/crowd_cheer.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])
    with d3

    # Back to commentating
    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    play background "sounds/crowd_low.ogg" fadein 0.5 fadeout 0.5
    her "..." ("normal", "squint", "angry", "mid", flip=True, xpos=290, ypos="base", trans=d3)
    her "Oh, apparently Ravenclaw scored during that... \"captivating\" bit of distraction..." ("open", "narrow", "annoyed", "mid")
    gen "Sarcasm much?" ("grin", xpos="far_left", ypos="head")
    her "" ("normal", "closed", "base", "mid")
    sna "..." ("snape_13", ypos="head")
    her "I think it's 10-20!" ("open", "happy", "base", "mid")
    her "Or is that 20-10... I'm not sure, aren't they both home teams...?" ("annoyed", "squint", "base", "mid")
    sna "Surely you must have learnt how to read by now, Miss Granger?" ("snape_03", ypos="head")

    play sound "sounds/ball_hit.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", None])
    with d3

    her "Hey! I have excellent reading skills, I'll have you know..." ("mad", "narrow", "angry", "R")
    play sound "sounds/crowd_cheer2.ogg"

    her "..." ("normal", "closed", "angry", "mid")

    call quidditch_stands(crowd_react=["emo8", None, None])
    with d3

    her "Wait, now it's... 20-30... I think..." ("annoyed", "happy", "base", "mid")
    play sound "sounds/murmur.ogg"
    call quidditch_stands(crowd_react=["th", None, None])
    with d3

    mal "Has this girl ever commentated even once in her life?"

    call quidditch_stands(crowd_react=["th", "th", None])
    with d3

    mal2 "She can't help herself answering questions in class..."
    mal2 "I suppose the rulebook was more for her benefit than ours."

    #call quidditch_stands(crowd_react=["th", "th", "emo3"]) # emo3 image is missing?
    call quidditch_stands(crowd_react=["th", "th", None]) # Temp fix, use above line.
    with d3

    her "" ("annoyed", "closed", "base", "mid")
    mal "Then how'd she get the role over Lee Jordan?"
    mal2 "I heard he had an accident with a rogue bludger."
    play sound "sounds/cough_male.ogg"
    mal "..."
    her "Wow... that snitch is darting around like nobody's business--" ("base", "base", "base", "mid")

    call quidditch_stands(crowd_react=[None, None, None])
    with d3
    hide hermione_main
    with d3
    pause .1

    # Genie and Snape get drunk
    sna "Fancy a glass of wine then?" ("snape_02", ypos="head")
    gen "Don't mind if I do... Something to distract me from this... bizarre game..." ("base", xpos="far_left", ypos="head")
    pause .5
    play sound "sounds/bottle.ogg"
    pause .8

    sna "{size=-4}I don't care much for the game myself...{/size}" ("snape_09", ypos="head")
    sna "{size=-4}Although, there is a special place in my heart for watching the bludgers catch a student...{/size}" ("snape_02", ypos="head")
    gen "{size=-4}Blubbers?{/size}" ("base", xpos="far_left", ypos="head")
    play sound "sounds/ball_hit.ogg"
    sna "{size=-4}Bludgers... See those cannonball looking things whizzing around?{/size}" ("snape_03", ypos="head")
    gen "{size=-4}Oh... The ones those boys are whacking at?{/size}" ("base", xpos="far_left", ypos="head")
    sna "{size=-4}Right... Well, we enchant them to go after the students while they play.{/size}" ("snape_23", ypos="head")
    gen "{size=-4}I see... {/size}{w}{nw}" ("base", xpos="far_left", ypos="head")
    gen "{size=-4}I see... {fast}Wait, Really? Why?{/size}" ("angry", xpos="far_left", ypos="head")
    sna "{size=-4}Makes things more interesting doesn't it!{/size}" ("snape_02", ypos="head")
    gen "{size=-4}So what happens when they hit their target?{/size}" ("base", xpos="far_left", ypos="head")
    sna "{size=-4}Generally it's just a concussion... Though sometimes they fall pretty far, that's always entertaining.{/size}" ("snape_20", ypos="head")

    with hpunch
    play sound "sounds/punch02.ogg"
    her "..." ("normal", "wide", "base", "stare", flip=True, xpos=290, ypos="base", trans=d1)

    play sound "sounds/crowd_ouch.ogg"
    call quidditch_stands(crowd_react=["sur", "emo02", "excl"])
    with d3

    her "Oh no!" ("clench", "happyCl", "worried", "mid")
    sna "{size=+4}HA-HA-HA-HA!!{/size}" ("snape_28", ypos="head")
    her "Somebody on the Ravenclaw team just got hit by a bludger!" ("open", "base", "worried", "L")
    gen "What an amazing turn of events!" ("grin", xpos="far_left", ypos="head")
    sna "See, I told you!" ("snape_22", ypos="head")
    hide hermione_main
    with d3
    pause .1

    call her_chibi("stand", flip=False)
    with d3
    pause .1

    call quidditch_stands(crowd_react=["sur", "emo02", None])
    with d3

    her "Professors, could you please keep it down a little?" ("normal", "base", "angry", "mid", ypos="head", flip=False)
    sna "Why? It's not like we're interrupting anything important." ("snape_18", ypos="head")

    call quidditch_stands(crowd_react=["sur", None, None])
    with d3

    her "I'm trying to commentate the game!" ("mad", "squint", "angry", "mid")

    play sound "sounds/ball_hit.ogg"
    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    sna "Yes, and I was starting to enjoy it. You are missing most of it, by the way..." ("snape_20", ypos="head")
    her "As a result of your yelling!" ("scream", "closed", "angry", "mid")
    her "" ("normal", "closed", "angry", "mid")
    sna "Eyes forward... girl." ("snape_13", ypos="head")
    her "*Grrrrr*" ("clench", "narrow", "angry", "mid")
    pause .1

    call her_chibi("stand", flip=True)
    with d3
    pause .1

    nar "Hermione's eyes briefly meet with yours as if she can't believe you're letting Snape talk to her that way."
    sna "{size=-4}As I was saying... They're the only reason I watch the bloody thing. Now, mind if I top that one off for you?{/size}" ("snape_20", ypos="head")

    play sound "sounds/crowd_cheer.ogg" fadein 3
    call quidditch_stands(crowd_react=["th", None, "emo8"])
    with d3

    her "So, I think... that Hufflepuff just scored another goal? They might even be unstoppable at this point!" ("open", "base", "base", "L", flip=True, xpos=290, ypos="base", trans=d3)

    # Fade to black
    stop background fadeout 4
    stop music fadeout 4
    show screen blkfade
    with d5
    pause .3

    hide hermione_main
    call quidditch_stands(crowd_react=[None, None, None])
    nar "You and Snape lean back and watch the game, frequently shifting your focus to Cho, as she darts past the stands..."
    nar "Only Occasionally pausing to refill your wine, while Snape keeps ridiculing Hermione's commentary..."

    # End of game
    play background "sounds/crowd_low.ogg" fadein 2
    play sound "sounds/referee.ogg"
    pause 1.0
    her "What was that?{w=0.5} Did somebody do a foul?" # intentional 'do'
    pause .5

    call hide_blkfade
    pause .1

    #"You see Cho flying over to the commentator booth glaring at Hermione with a look of pure hatred."

    # Transition to Cho on her broom
    $ cho.set_pose("broom")
    $ cho.animation = sprite_fly_idle

    call cho_chibi("fly", 1100, 140)
    call cho_walk(530, 360, speed=2)
    pause 1.5

    her "" ("annoyed", "base", "annoyed", "L", flip=True, xpos=290, ypos="base")
    cho "Hey, Granger!" ("open", "narrow", "angry", "L", xpos=580, ypos=-200, trans=d3)
    her "What do you want?{w=0.6} Shouldn't you be busy with,{w=0.8} I don't know..." ("open", "base", "angry", "mid", trans=d3)
    cho "" ("annoyed", "narrow", "raised", "L")
    her "playing the game?" ("smile", "closed", "base", "mid")
    cho "The game is over, you dipstick!" ("scream", "narrow", "angry", "L")
    cho "" ("mad", "narrow", "angry", "L")
    her "What? Already?" ("shock", "wide", "worried", "stare")
    her "But who caught the Snitch?" ("open", "wide", "base", "stare")
    cho "" ("upset", "narrow", "angry", "L")

    #TODO: Draw the arm.

    #$ cho.set_body(armright="snitch")
    with d3
    nar "Cho waves the snitch in front of her."
    her "" ("mad", "wide", "worried", "shocked")
    #$ cho.set_body(armright="down")

    cho "My first ever win this season, and you didn't even notice it!" ("clench", "closed", "angry", "mid")
    cho "No one did, thanks to your dreadful commentating!" ("scream", "narrow", "angry", "L")
    cho "" ("mad", "narrow", "angry", "L")
    her "Oh..." ("normal", "wide", "worried", "shocked")
    her "So, should I announce it now?" ("open", "happyCl", "worried", "mid")
    sna "Obviously--" ("snape_12", ypos="head")
    cho "{size=+10}YES!{/size}" ("scream", "closed", "angry", "mid", trans=vpunch)
    her "" ("normal", "base", "annoyed", "L")
    cho "{size=+6}WHAT ARE YOU EVEN WAITING FOR?{/size}" ("clench", "narrow", "angry", "L", trans=hpunch)
    her "Don't scream at me like that, {b}bitch!{/b}" ("scream", "base", "angry", "mid", trans=hpunch)
    her "" ("normal", "base", "angry", "mid")
    cho "{size=+6}WHAT DID YOU JUST CALL ME?!!!{/size}" ("scream", "wide", "angry", "L", trans=vpunch)
    cho "" ("clench", "wide", "angry", "L")
    her "Everyone, Ravenclaw wins!" ("grin", "happy", "base", "mid_soft")
    cho "" ("annoyed", "narrow", "angry", "L")
    her "Cho Chang managed to catch the snitch..." ("smile", "happyCl", "base", "mid")
    her "With the help of her ridiculously short skirt!" ("crooked_smile", "base", "angry", "mid")
    #cho "{size=+10}!!!{/size}" ("clench", "closed", "angry", "mid")
    hide hermione_main
    with d3
    cho @ cheeks heavy_blush "" ("normal", "wide", "base", "L")

    play background "sounds/crowd.ogg" fadein 1 fadeout 1
    play sound "sounds/crowd_applause.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo7"])
    hide hermione_main
    hide screen bld2
    with d3
    call ctc

    cho @ cheeks blush "" ("quiver", "base", "worried", "downR")
    nar "Hermione's commentating is drowned out by the sound of the Ravenclaw grandstand cheering."
    cho @ cheeks blush "{size=+6}You are done, Granger!{/size}" ("scream", "closed", "angry", "L")
    hide cho_main
    with d3
    pause .1

    call cho_walk(1200, 500+180, speed=2)
    pause 2
    $ cho.animation = None
    $ cho.set_pose(None)
    call cho_chibi("reset")

    # Outro
    gen "This isn't such a bad game after all." ("base", xpos="far_left", ypos="head")
    sna "I--{w=0.2} *hick*...{w=0.2} told you so..." ("snape_22", ypos="head")
    gen "Just bring more wine next time!" ("base", xpos="far_left", ypos="head")
    sna "M-More?!" ("snape_20", ypos="head")
    gen "Or at least share more of it with me!" ("base", xpos="far_left", ypos="head")
    play sound "sounds/glass_shatter.ogg"
    sna "Get your own, magic man!" ("snape_21", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")

    # Blackfade
    stop background fadeout 4
    show screen blkfade
    with d5

    nar "Snape wanders off in a drunken stupor..."
    pause .5
    play sound "sounds/steps_grass.ogg"
    nar "You hurry back to your office before giving anyone a chance to talk to you."

    $ game.daytime = False
    call room("main_room")
    call gen_chibi("hide")
    call hide_blkfade
    pause 1.0

    play sound "sounds/door.ogg"
    call gen_chibi("stand", "door", "base", flip=False)
    with d3
    pause 0.3

    call bld
    gen "I'm hom--" ("base", xpos="far_left", ypos="head")
    gen "Dammit, I almost said that!" ("angry", xpos="far_left", ypos="head")
    gen "Anyway, I'm beat, time to hit the hay." ("base", xpos="far_left", ypos="head")

    call gen_walk("desk", "base")
    with d3
    #pause .5

    # Fade to black
    show screen blkfade
    with d9
    pause .5

    call gen_chibi("sit_behind_desk")
    with fade

    # Reset
    $ hermione.equip(her_outfit_last) # Equip player outfit.
    $ cho.equip(cho_outfit_last) # Equip player outfit.

    jump hufflepuff_match_return


label hufflepuff_match_return:
    # Cho returns after winning the Quidditch match.
    # She's outraged about Hermione.
    # Demands that you will find somebody to replace her.

    # The office, evening after the game
    $ game.daytime = False

    stop music fadeout 1
    call room("main_room")

    $ cho_outfit_last.save()

    $ cho.equip(cho_outfit_quidditch)

    call music_block
    hide screen blkfade
    with d9
    pause 0.8

    call bld
    play sound "sounds/snore1.ogg"
    gen "*Snore*{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    pause 1.0
    play sound "sounds/snore3.ogg"
    gen "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    pause 1.0
    play sound "sounds/snore2.ogg"
    gen "......{w=0.5}*Snore*{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
    stop music fadeout 6.0
    call cho_walk("desk", "base", action="enter")

    play sound "sounds/punch01.ogg"
    cho "We beat Hufflepuff!!!" ("silly", "happyCl", "base", "mid", xpos="mid", ypos="base", trans=hpunch)
    play sound "sounds/MaleGasp.ogg"
    gen "{size=+10}IT WASN'T ME!{/size}" ("angry", xpos="far_left", ypos="head")
    gen "..........." ("base", xpos="far_left", ypos="head")
    cho "*Huh*?{w=0.5} Are you okay, [name_genie_cho]?" ("soft", "narrow", "base", "mid")
    gen "Wha--" ("base", xpos="far_left", ypos="head")
    gen "Of course I am!" ("angry", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "narrow", "raised", "R")
    cho "If you say so..." ("annoyed", "narrow", "base", "mid")
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "I can't believe that we've broken our six year dry streak and won a real game!" ("smile", "happyCl", "base", "mid")
    cho "We could actually win the cup!" ("open", "wide", "base", "mid")
    gen "And you weren't embarrassed?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I was a little at the start of the game..." ("quiver", "narrow", "worried", "downR")
    cho "But once I realised how much it was affecting those slack-jawed Hufflepuffs..." ("smile", "narrow", "angry", "R")
    cho "It was like having my own personal weapon of mass distraction!" ("smile", "wide", "angry", "mid")
    cho @ cheeks blush "I don't think Cedric even knew where the snitch was, most of the time!" ("horny", "base", "base", "downR")
    cho @ cheeks blush "All he seemed to do was follow me around..." ("horny", "narrow", "worried", "down")
    cho @ cheeks heavy_blush "Him {size=-2}and {size=-2}half {size=-2}the {size=-2}team...{/size}{/size}{/size}{/size}" ("quiver", "narrow", "worried", "downR")
    cho "This might be the first real chance Ravenclaw has ever had to win the cup." ("open", "closed", "worried", "mid")
    gen "I'm sure this must mean a lot to you..." ("base", xpos="far_left", ypos="head")
    cho "It does... I might even get picked up by a pro team!" ("smile", "base", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "*Ahh*{w=0.3} I can't wait!" ("silly", "happyCl", "base", "mid")
    cho "I better go celebrate with the team now!" ("clench", "wide", "base", "mid")
    gen "Well, off you go then." ("base", xpos="far_left", ypos="head")
    cho "Thank you [name_genie_cho]..." ("smile", "wink", "base", "mid")
    #
    # TODO: Add panty flash in form of a reward/tease
    #
    # cho "But before I go..." # blushes
    # (flashes panties)
    # gen "!!!" ("angry", xpos="far_left", ypos="head")
    # (equips skirt again)
    # cho "I gotta go."
    # starts walking out of the office
    # gen "Hey but I ha--" ("base", xpos="far_left", ypos="head")
    # (cho leaves)
    # gen "Oh well.. At least I caught a glimpse of the goodies." ("base", xpos="far_left", ypos="head")

    call cho_walk(action="leave")

    stop music fadeout 1.0
    call unlock_clothing(text="New clothing items for Cho have been unlocked!", item=cho_outfit_cheerleader)
    call popup("New favours for Cho have been unlocked!", "Congratulations!", "interface/icons/head/cho.webp")

    $ states.her.busy = True
    $ states.sna.busy = True

    # Reset Cho
    $ cho.equip(cho_outfit_last)

    $ states.cho.tier = 2
    $ states.cho.favors_unlocked = False
    $ states.cho.requests_unlocked = False
    $ states.cho.ev.quidditch.lock_training = False
    $ states.cho.ev.quidditch.lock_practice = True
    $ states.cho.ev.quidditch.lock_tactic   = False
    $ states.cho.ev.quidditch.hufflepuff_stage = "completed"

    jump end_cho_event
