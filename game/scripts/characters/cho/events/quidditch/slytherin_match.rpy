
# Ravenclaw vs. Slytherin

label start_slytherin_match:
    # Chat with Cho the day before the match

    cho "" (xpos="mid", ypos="base", trans=fade)
    gen "Alright, [name_cho_genie]. Let's do this!" ("grin", xpos="far_left", ypos="head")
    gen "Tomorrow we shall wipe the floor with those Slytherins, and bathe in their salty tears!" ("angry", xpos="far_left", ypos="head")
    gen "(Snape's tears in particular, after I get a hold of all of his gold!)" ("grin", xpos="far_left", ypos="head")
    cho "I'll do my best, Sir." ("soft", "base", "angry", "mid")
    gen "Are you ready?" ("base", xpos="far_left", ypos="head")
    cho "I am!" ("base", "base", "angry", "mid")
    menu:
        "\"Then show me the money.\"":
            cho "What?" ("upset", "base", "raised", "mid")
            gen "Say it with me, [name_cho_genie]!{w} Show me the money!" ("grin", xpos="far_left", ypos="head")
            cho "I don't have any on me, Sir." ("angry", "narrow", "worried", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            cho "Show me the money?" ("open", "narrow", "raised", "mid")
            gen "Yes! Say it like you mean it, brother!" ("grin", xpos="far_left", ypos="head")
            cho "What?" ("angry", "wide", "base", "mid")
            with hpunch
            gen "{size=+5}Show me the money!{/size}" ("angry", xpos="far_left", ypos="head") # loud
            cho "(He knows I'm a girl... why would he say that?)" ("annoyed", "narrow", "angry", "mid")
            with hpunch
            cho "Sir, Are you all right?" ("soft", "narrow", "worried", "mid")
            gen "What you gonna do, [name_cho_genie]?" ("grin", xpos="far_left", ypos="head")
            cho "Get the nurse?" ("upset", "narrow", "angry", "mid")
            gen "You're gonna win that match tomorrow, that's what!" ("base", xpos="far_left", ypos="head")
        "\"Show me what you got!\"":
            cho "Of course sir, always!" ("soft", "base", "base", "R")
            gen "Show me what you got!" ("grin", xpos="far_left", ypos="head")
            cho "sir?" ("upset", "base", "raised", "mid")
            gen "Show me what you got, I want to see what you got!" ("grin", xpos="far_left", ypos="head")
            cho "Sir, are you okay?" ("open", "narrow", "raised", "mid")
            gen "Show me--" ("base", xpos="far_left", ypos="head")
        "\"Show me your tits!\"":
            cho "What?" ("upset", "base", "raised", "mid")
            gen "For luck!" ("grin", xpos="far_left", ypos="head")
            cho "Sir, I don't have time for this..." ("soft", "narrow", "worried", "mid")
    cho "If we're going to play tomorrow, I'll first have to prepare my gear, and charm my Quidditch goggles..." ("soft", "base", "base", "R")
    cho "Or they'll just fog-up and not dispel the rain properly..." ("soft", "narrow", "base", "mid")
    gen "Hold up!{w=0.3} It's going to rain tomorrow?" ("base", xpos="far_left", ypos="head")
    cho "Most likely..." ("annoyed", "base", "worried", "mid")
    gen "(This might be just what we need!)" ("angry", xpos="far_left", ypos="head")
    cho "Professor Trelawney told us to wear our robes tomorrow." ("soft", "base", "base", "R")
    cho "According to her, there are some heavy rain clouds approaching..." ("open", "narrow", "raised", "mid")
    cho "But that's just Trelawney... She can be a bit inconsistent with her weather forecasts..." ("soft", "base", "worried", "down")
    cho "Well, she's quite inconsistent with everything, if I'm honest..." ("annoyed", "narrow", "base", "R")
    gen "Let's hope she's right this time!" ("grin", xpos="far_left", ypos="head")
    cho "But, Sir! Wouldn't this put us at a huge disadvantage?" ("open", "narrow", "worried", "mid")
    gen "Nonsense..." ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho], I'm gonna get soaked without my coat on!" ("soft", "base", "worried", "mid")
    gen "Counting on it!" ("grin", xpos="far_left", ypos="head")
    gen "I, for one, am quite looking forward to the possibility of you getting wet." ("grin", xpos="far_left", ypos="head")
    cho "Let's just hope for the best..." ("upset", "narrow", "worried", "down")
    gen "That we shall." ("grin", xpos="far_left", ypos="head")
    gen "Off you go then. And good luck." ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "R")
    cho "See you tomorrow, [name_genie_cho]." ("soft", "narrow", "worried", "mid")

    call cho_walk(action="leave")

    $ states.cho.busy = True
    $ cc_event_pause  += 1 # Event starts on the next day
    $ cc_summon_pause += 1 # Can't be summoned until next event

    $ states.cho.ev.quidditch.lock_training = True
    $ states.cho.ev.quidditch.lock_practice = True

    $ states.cho.ev.quidditch.slytherin_stage = "start"

    jump end_cho_event


label slytherin_match:
    # Quidditch match: Ravenclaw vs. Slytherin
    $ game.weather = "clear"

    $ cho_outfit_last.save()
    $ her_outfit_last.save()
    $ ton_outfit_last.save()

    $ cho.equip(cho_outfit_quidditch)
    $ hermione.equip(her_outfit_default)
    $ tonks.equip(ton_outfit_default)

    stop music fadeout 1

    # Start in the office
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Who is it?\"":
            call bld
            ton "Tonks, Sir."
            gen "First and last name, please." ("base", xpos="far_left", ypos="head")
            with hpunch
            ton "What?!"
            gen "Tell me your first and last name, and you may enter." ("grin", xpos="far_left", ypos="head")
            ton "Are you fucking with me right now?"
            gen "No. Unless that's on the table..." ("base", xpos="far_left", ypos="head")
            gen "Or desk." ("grin", xpos="far_left", ypos="head")
            ton "Bloody hell..."
            gen "Full name please." ("base", xpos="far_left", ypos="head")
            ton "Nymphadora Tonks...{w=0.3} Can I come in now?"
            gen "Of course..." ("grin", xpos="far_left", ypos="head")
        "\"Come in...\"":
            pass

    call ton_walk("desk", "base", action="enter")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "Hi, [name_genie_tonks]." ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=d3)
    gen "Tonks... A pleasure as always." ("base", xpos="far_left", ypos="head")
    ton "Pleasure's all mine..." ("soft", "base", "base", "mid")
    ton "I was afraid you might've forgotten about today's--" ("open", "base", "raised", "mid")
    gen "Quidditch match?" ("grin", xpos="far_left", ypos="head")
    ton "So you didn't forget!" ("grin", "wide", "shocked", "mid")
    gen "How could I? The previous match was a great show!" ("grin", xpos="far_left", ypos="head")
    ton "It sure was..." ("horny", "base", "raised", "R")
    ton "So, is Miss Granger going to show up as well?" ("soft", "wide", "shocked", "mid")
    gen "Who knows with her, honestly..." ("base", xpos="far_left", ypos="head")
    ton "Fingers crossed then." ("base", "base", "base", "mid")
    ton "I'd love to be able to watch her--{w} The game from the commentator booth." ("clench", "narrow", "raised", "R")
    ton "So... *Ahem*... May I be allowed to accompany you on the way to the pitch?" ("base", "base", "base", "mid") #sad
    gen "Of course! I'd be delighted to have you!" ("grin", xpos="far_left", ypos="head")
    ton @ hair happy "Thank you, [name_genie_tonks].{heart}" ("base", "happyCl", "base", "mid")
    ton @ hair neutral "Are we to expect another great performance this time around?" ("horny", "narrow", "base", "downR")
    gen "Oh, you'll see..." ("grin", xpos="far_left", ypos="head")
    ton "Great, shall we?" ("base", "wink", "shocked", "mid")
    gen "We certainly shall!" ("grin", xpos="far_left", ypos="head")

    stop music fadeout 1
    call hide_characters
    hide screen bld1
    with d3

    # Teleport to door
    play sound "sounds/kick.ogg"
    call gen_chibi("hide")
    with d3

    call gen_chibi("stand", "door", "base")
    call teleport(position="genie", effect=False)
    pause .2

    call ton_chibi("stand", "desk", "base", flip=True)
    with d3
    pause .2

    call gen_chibi("stand", "door", "base", flip=False)
    with d3
    pause .3

    ton "*Huh*?... (When did he?)" ("upset", "shocked", "raised", "L", ypos="base", flip=True)
    ton "(Impressive. I wonder if his stamina can keep up with that speed...)" ("mad", "narrow", "raised", "R")
    gen "Ladies first." ("grin", xpos="base", ypos="base", flip=True)
    ton "What a gentleman." ("base", "happyCl", "base", "mid")

    call ton_walk("door", "base", speed=1.25)

    play sound "sounds/door.ogg"
    call ton_chibi("hide")
    with d3
    pause .2

    call gen_chibi("stand", "door", "base")
    with d3
    pause .5

    play sound "sounds/door.ogg"
    call gen_chibi("hide")
    with d3
    pause .8

    # Black screen
    stop music fadeout 2
    stop background fadeout 2
    stop music fadeout 1
    show screen blkfade
    with d5
    pause 2


    play sound "sounds/steps_grass.ogg"
    nar "You and Tonks make your way across the castle grounds."
    nar "You find Snape waiting for you at the entrance of the Quidditch pitch towers."

    # Pitch entrance
    #centered "{size=+7}{color=#cbcbcb}At the Quidditch pitch...{/color}{/size}"

    #TODO Weather effects:
    # Scene Cloudy/rainy pitch
    # Sounds slightly windy/rain (Might need a new sound we'll see... It shouldn't overpower things)

    call room("quidditch_pitch")
    play background "sounds/outskirts.ogg" fadein 2
    call sna_chibi("stand", "right", "base")
    call ton_chibi("stand", "mid", "base", flip=True)
    call gen_chibi("stand", "left", "base", flip=True)
    call hide_blkfade
    pause .8

    sna "Miss Tonks..." ("snape_03", ypos="head")
    sna "Geni--" ("snape_03")
    sna "*Ahem*... Albus, Glad you made it in time, I was about to call for you." ("snape_09")
    ton "I know who he is, Snape. There's no need for the pretence." ("open", "closed", "base", "L", ypos="head", flip=True)
    sna "Of course there is. We're outside the headmaster's office, after all." ("snape_16")
    sna "We have to keep up the act in front of the students..." ("snape_01")
    ton "*Hmm*... Good point..." ("base", "base", "base", "R")
    gen "I'm standing right here." ("base", xpos="far_left", ypos="head", flip=False)
    sna "I would've gone and fetched him myself but..." ("snape_03")
    sna "I had some... business to attend to." ("snape_35")
    ton "Business, *huh*?" ("horny", "wide", "raised", "L")

    sna "You will be accompanying us, I presume?" ("snape_04")
    ton "If that's okay with you?" ("base", "happyCl", "base", "mid")
    with None

    show screen blktone
    with d5
    gen "(Why aren't they paying attention to me?)" ("base", xpos="far_left", ypos="head")
    hide screen blktone
    with d5

    sna "I suppose..." ("snape_05")
    ton "Great!" ("grin", "base", "raised", "L")

    ton "So, are we going?" ("base", "base", "shocked", "L")
    sna "*Ahem*, yes... I suppose." ("snape_12") #throat clear in the middle of the sentence for extra awkwardness
    gen "I may be immortal, but I'm afraid I'll die from this awkwardness..." ("base", xpos="far_left", ypos="head")
    gen "I'd take a hundred years in the lamp over this." ("base", xpos="far_left", ypos="head")

    play sound "sounds/giggle2_loud.ogg"
    ton "*Giggles*" ("base", "happyCl", "base", "mid")
    sna "..." ("snape_14")
    sna "After me then..." ("snape_12")

    call sna_walk(path=[("stairs_base", "base"),("stairs_up", "stairs_up")], speed=1.5)
    call ton_walk(path=[("stairs_base", "base"),("stairs_up", "stairs_up")], speed=1.5)
    call gen_walk(650, "base", speed=1.5)
    call gen_chibi("stand", 650, "base")
    with d3
    call chibi_emote("exclaim", "genie")
    pause 0.3

    call chibi_emote("hide", "genie")
    call gen_chibi("stand_alt")
    with d3
    pause 0.5

    call bld
    gen "(*He-heh*... \"Snape sux\"...)" ("grin", xpos="far_left", ypos="head")
    gen "(Oh right. I already saw that...)" ("base", xpos="far_left", ypos="head")
    gen "(Still funny.)" ("grin", xpos="far_left", ypos="head")
    call gen_chibi("stand")
    call gen_walk(path=[("stairs_base", "base"),("stairs_up", "stairs_up")], speed=1.5)

    stop background fadeout 2
    call blkfade

    # Sound check
    if get_volume_preference('music') < 0.1 or get_volume_preference('sfx') < 0.1:
        nar "This section of the game is best played with the sound turned on. Go to preferences to set the volume."

    pause 1

    # Quidditch stands
    call room("quidditch_stands")
    call quidditch_stands(weather="sun_high")

    ### Snape Chibi Postions ###
    # 1st Step R:       call sna_chibi("stand", flip=True, 25, 234)
    # 2nd Step R:       call sna_chibi("stand", flip=True, 85, 260)
    # 3rd Step R:       call sna_chibi("stand", 120, 295, flip=True)

    ### Genie Postions ###
    ## Sprite:          call gen_main(face="base", base="base", xpos=-10, ypos=140)
    # 1st Step Mid:     call gen_chibi("stand", flip=True, -20, 270)
    # 2nd Step L:       call gen_chibi("stand", flip=True, -20, 320)
    # 2nd Step Mid:     call gen_chibi("stand", flip=True, 0, 360)
    # 3rd Step L:       call gen_chibi("stand", 20, 365, flip=True)
    # 3rd Step Mid:     call gen_chibi("stand", flip=True, 65, 340)
    # Floor Mid:        call gen_chibi("stand", 170, 400, flip=True)
    # Podium:           call gen_chibi("stand", flip=True, 280, 400)

    ### Hermione Postions ###
    ## Sprite:          her "" (flip=True, xpos=290, ypos="base")
    # 2nd Step Mid:     call her_chibi("stand", 40, 295, flip=True)
    # Floor Mid:        call her_chibi("stand", flip=True, 180, 400)
    # Podium:           call her_chibi("stand", 300, 400, flip=True)
    # Podium Sidestep:  call her_chibi("stand", flip=True, 260, 460)

    ### Tonks Positions ###
    # 1st Step R:       call ton_chibi("stand", flip=True, 55, 235)
    # 4th Step R:       call ton_chibi("stand", 180, 340, flip=True)
    # Floor mid:        call ton_chibi("stand", flip=True, 180, 400)
    # Floor R:          call ton_chibi("stand", flip=True, 230, 370)
    # Podium:           call ton_chibi("stand", flip=True, 300, 400)
    # Sitting:          call ton_chibi("sit", flip=True, xpos=-140, ypos=125)

    ### Cho Positions ###
    ## Flying Sprite:   call cho_main(xpos=580, ypos=-200)
    # Flying Chibi:     call cho_chibi("fly", 530, 360)

    $ snape_chibi.zorder = 1
    $ tonks_chibi.zorder = 2
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 4

    # Match starts
    play weather "sounds/outskirts_tower.ogg" fadein 3
    call hide_blkfade
    pause 1

    play sound "sounds/footsteps.ogg"
    pause .8

    call sna_chibi("stand", 120, 295, flip=True)
    with d3
    pause .5

    call ton_chibi("stand", 180, 340, flip=True)
    with d3
    pause .2
    call ton_chibi("stand", flip=False)
    with d3

    ton "Mind your head!" ("open", "shocked", "shocked", "down", ypos="head", flip=False)

    play sound "sounds/kick.ogg"
    with hpunch
    pause .6
    gen "Bloody bleachers!" ("angry", xpos="far_left", ypos="head")
    sna "..." ("snape_45", ypos="head")
    pause .2

    play sound "sounds/footsteps.ogg"
    pause .8
    call gen_chibi("stand", 20, 365, flip=True)
    with d3
    pause .2
    call ton_chibi(flip=True)
    with d3
    pause .2

    play background "sounds/crowd_very_low.ogg" fadein 10
    call quidditch_stands(crowd=crowd_few)
    with d3
    pause 1

    ton "Oh, what a view! Much better than the one from the Hufflepuff stands!" ("grin", "wide", "base", "L", ypos="head", flip=True)

    gen "Nice weather too." ("base", xpos="far_left", ypos="head")
    ton "Indeed!" ("base", "wide", "base", "mid")

    play sound "sounds/thunder.ogg"
    call quidditch_stands(weather="overcast", tree_fire=True, rain=True, puddles=True)
    with flashbulb
    play weather "sounds/storm.ogg" fadeout 1.0 fadein 3.0
    $ game.weather = "rain"

    pause 1.0
    sna "Indeed!" ("snape_02", ypos="head")

    ton "You jinxed it..." ("upset", "closed", "worried", "mid", ypos="head", flip=True)
    gen "Hey!{w=0.4} That wasn't--" ("angry", xpos="far_left", ypos="head")

    # Hermione walks up to the podium
    play sound "sounds/footsteps.ogg"
    call her_chibi("stand", 40, 295, flip=True)
    with d3
    pause .3
    call her_walk(path=[(180, 400),(300, 400)])
    call her_chibi("stand", 300, 400, flip=True) # Temp Bugfix
    pause .5

    call her_chibi(flip=False)
    with d3
    pause .1

    her "Oh, hello, Professor Tonks!" ("soft", "base", "base", "L", ypos="head", flip=False)
    pause 1.0
    play sound "sounds/MaleClearThroat.ogg"
    sna "*Ahem*" ("snape_09", ypos="head")
    pause 2.0
    call chibi_emote("thought", "snape")
    pause 2.0
    call chibi_emote("hide", "snape")

    #show screen blktone
    #with d5
    #gen "(I feel you buddy...)" ("base", xpos="far_left", ypos="head")
    #hide screen blktone
    #with d5

    ton "{size=-4}Do I hear some jealousy back there?{/size}" ("grin", "narrow", "raised", "R", ypos="head", flip=True)
    sna "{size=-4}Of course not... just a cough,{w=0.3} {cps=15}Nymphadora{/cps}.{/size}" ("snape_03", ypos="head")
    ton @ hair angry "{size=-2}That's Tonks to you...{w=0.3} {i}dungeon dweller.{/i}{/size}" ("open", "wide", "angry", "R")
    sna "Dungeon dw--" ("snape_32", ypos="head")
    sna "I'll give you a dungeon dweller in a minute you--" ("snape_08", ypos="head")

    her "Professor Tonks, your hair!" ("soft", "base", "base", "L", ypos="head", flip=False)
    ton @ hair neutral "Whoopsie...{w=0.5} Miss Granger, so glad to see you!" ("base", "happyCl", "base", "L", ypos="head", flip=True)
    sna "{size=-2}*Hmph*{/size}" ("snape_31", ypos="head")
    her "Of course... As you know, I take my responsibilities seriously!" ("open", "base", "angry", "L")

    call quidditch_stands(crowd=crowd_mid)
    with d3

    #TODO Crowd sound goes up
    sna "{size=-4}Unfortunately...{/size}" ("snape_31") #small text
    ton "I'm here if you need me!" ("base", "happyCl", "base", "mid")
    her "I appreciate the thought, Professor... but I'll be fine." ("open", "closed", "base", "mid")
    her "I'd be made fun of even more if you had to take over..." ("open", "narrow", "angry", "L")
    ton "Whatever you want, sweetie." ("horny", "narrow", "base", "L") #smile
    her @ cheeks blush "..." ("clench", "happyCl", "worried", "mid") #smiles and blushes
    pause .2

    play background "sounds/crowd_low.ogg" fadeout 5.0 fadein 3.0
    call quidditch_stands(crowd=crowd_full)
    with d3
    pause .5

    sna "The crowd is waiting, Miss Granger..." ("snape_31")
    her "Sorry!" ("clench", "happyCl", "worried", "mid", emote="sweat")

    call her_chibi(flip=True)
    with d3
    pause .5

    her "" ("open", "base", "worried", "mid", flip=True, xpos=290, ypos="base", trans=d5)
    pause .8

    play sound "sounds/microphone_feedback.ogg"
    play background "sounds/crowd_very_low.ogg" fadeout 1.0 fadein 5.0
    her "*Ahem*" ("open", "happyCl", "base", "mid")
    her "Welcome back to the second match of the season!" ("base", "happyCl", "base", "mid")

    play background "sounds/crowd_low.ogg" fadeout 1.0 fadein 3.0

    call quidditch_stands(crowd_react=[None, "emo8", None])
    sly1 "{size=+5}Not the Gryffindor slut again!{/size}"

    sly2 "{size=+8}Get off the podium, Mudblood!{/size}"
    sly1 "{size=+15}Boooo!{/size}"
    her "*Hmph*!" ("annoyed", "narrow", "angry", "mid")

    call hide_characters
    with d3
    pause .2
    call her_chibi(flip=False)
    with d3
    pause .3

    her "Sir, I'm trying to do my job here, and those Slytherin boys just can't keep their filthy mouths shut!" ("soft", "narrow", "angry", "mid", ypos="head", flip=False)
    sna "Surely you've been called worse Miss Granger..." ("snape_05")

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    ton "Just ignore them sweetie, you're doing great." ("base", "happyCl", "base", "mid")

    if states.ton.level > states.sna.level:
        gen "What she said." ("base", xpos="far_left", ypos="head")
    elif states.ton.level == states.sna.level:
        gen "What they said." ("base", xpos="far_left", ypos="head")
    else:
        gen "What he said." ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "angry", "down")
    her "Fine..." ("soft", "base", "base", "R")

    pause .2
    call her_chibi(flip=True)
    with d3
    pause .5

    her "I know the weather might not be optimal, but the games must go on." ("soft", "closed", "base", "mid", flip=True, xpos=290, ypos="base", trans=d3)
    her "Therefore, let me now welcome onto the pitch..." ("open", "base", "base", "down")
    her "The team known for their technical prowess and... lately... unconventional tactics..." ("disgust", "base", "worried", "down")
    her "Team Ravenclaw!" ("open", "base", "base", "mid")

    play sound "sounds/crowd_cheer.ogg"
    call quidditch_stands(crowd_react=["emo8", None, "emo8"])
    with d3

    nar "A loud cheer roars from the grandstands."

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    #TODO Crowd sounds
    her "And their opponents..." ("soft", "closed", "base", "mid")
    her "The team known for their..." ("open", "narrow", "angry", "down")
    her "Their..." ("open", "narrow", "angry", "L")

    call quidditch_stands(crowd_react=[None, "emo8", None])
    with d3

    sly1 "{size=+5}Got a cock down your throat?{w=0.8} Get on with it!{/size}"
    sly2 "{size=+8}Yeah!{w=0.5} Get on with it!{/size}"
    her "..." ("annoyed", "closed", "angry", "mid")

    play background "sounds/crowd.ogg" fadeout 1.0 fadein 3.0
    call quidditch_stands(crowd_react=["emo8", None, "emo7"])
    with d3
    with hpunch
    qcr "{size=+15}Get on with it!{/size}"

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    play sound "sounds/microphone_feedback.ogg"
    her "The team known for their thick skin... or should I say, thick skulls..." ("angry", "base", "angry", "mid", emote="angry")
    her "Team Slytherin!" ("annoyed", "narrow", "angry", "mid")

    play sound "sounds/crowd_stomping.ogg"
    hide hermione_main
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo7"])
    with d3

    #her "" ("base", "base", "base", "mid")
    nar "The green grandstand shakes violently with enthusiasm."

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    gen "..." ("grin", xpos="far_left", ypos="head")
    sna "..." ("snape_38")
    her "And now, if both teams have managed to find their way to their starting positions..." ("open", "closed", "base", "mid", trans=d3)
    her "Madam Hooch, if you please!" ("soft", "base", "base", "L")

    hide hermione_main
    with d3

    pause .5

    play background "sounds/crowd_low.ogg" fadeout 1.0 fadein 3.0
    play sound "sounds/referee.ogg"
    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    nar "Madam Hooch glances up at the podium, and gives Hermione a wink as she throws the quaffle into the air."

    her "And we're off!" ("base", "happyCl", "base", "mid", trans=d3)
    nar "Looking up, you can see Cho giving Malfoy a quick smirk as she darts off towards the Slytherin half of the pitch."
    her "Ravenclaw chaser and team captain Roger Davies immediately goes for the quaffle..." ("open", "base", "angry", "L")
    her "The Slytherin captain Graham Montague not far behind." ("open", "base", "angry", "up")
    her "Oh! Davies catches it and passes to Bradley..." ("smile", "base", "angry", "up")
    ton "She's pretty cute when she's excited, isn't she." ("soft", "narrow", "base", "L")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "I feel like we've got the best seats in the house, right behind the podium..." ("horny", "narrow", "raised", "L")
    her "" ("open", "base", "angry", "up")
    ton "Who cares about the match if you've got a view like that..." ("horny", "base", "angry", "L")
    play sound "sounds/ball_hit.ogg"
    her "" ("open", "base", "angry", "up")

    sna "Well, some of us bet quite a fortune on the outcome." ("snape_09")
    if game.gold >= 2000:
        gen "Fuck{w=0.3}, I forgot he was here..." ("angry", xpos="far_left", ypos="head")
    else:
        gen "Oh shit{w=0.3}, the bet..." ("angry", xpos="far_left", ypos="head")

    sna "You aren't going to chicken out now, are you?" ("snape_03")
    gen "No... of course not..." ("base", xpos="far_left", ypos="head")
    if game.gold >= 2000:
        gen "(Why did I bet so much gold on this?!)" ("angry", xpos="far_left", ypos="head")
    else:
        gen "(How in the hell would I get two thousand gold?!)" ("angry", xpos="far_left", ypos="head")
        gen "(It's not like I can conjure gold out of the thin air, can I...)" ("base", xpos="far_left", ypos="head")

    her "The Slytherin beaters, Crabbe and Goyle, are now focusing their efforts on beating the bludgers as hard as they can towards the enemy chasers!" ("open", "base", "angry", "R")
    play sound "sounds/ball_hit.ogg"
    her "Crabbe just whacked the bludger straight towards Davis' broom--" ("open", "base", "angry", "up")
    her "Scratch that, he hit the quaffle out of his hand!" ("clench", "base", "worried", "up")
    her "That's crazy lucky!" ("open", "base", "angry", "up")
    her "Where's the quaffle?{w} Oh, Pucey's got it!" ("soft", "base", "base", "L")
    her "And he's already flown past the beaters!" ("smile", "base", "angry", "L")
    gen "..." ("angry", xpos="far_left", ypos="head")
    her "But can he get through the keeper?" ("soft", "base", "base", "up")

    play sound ["sounds/card_punch4.ogg", "sounds/crowd_ouch.ogg"]
    with hpunch

    pause 0.5
    call quidditch_stands(crowd_react=["sur", "emo02", "excl"])


    her "Another bludger hit by Crabbe -- going straight into the stomach of the Ravenclaw keeper!" ("clench", "base", "worried", "up")

    call quidditch_stands(crowd_react=[None, None, None])
    with d3

    her "Pucey passes the quaffle to Warrington, who scores another goal for team Slytherin!" ("annoyed", "base", "angry", "up")

    hide hermione_main
    call quidditch_stands(crowd_bj=True) # Blowjob Silhouette
    with d3

    gen "That's insane, how the hell did he hit that?" ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_45")
    gen "He was on the other side of the pitch!" ("angry", xpos="far_left", ypos="head")
    sna "That's my boys!" ("snape_37")
    sna "Thick as porridge, but built like a brick shithouse." ("snape_28")
    play sound "sounds/ball_hit.ogg"
    ton @ hair horny "They're so strong... I've never seen a bludger hit its target from that far before..." ("horny", "base", "base", "up") #horny
    ton @ cheeks blush "Is it me or is it getting a bit hot in here?" ("normal", "closed", "raised", "downR")
    sna "Something to cool you down perhaps?" ("snape_02")
    ton "Good idea, did you bring any of that firewhisky, Professor Dumbledore?" ("soft", "wink", "raised", "mid")
    gen "Err..." ("base", xpos="far_left", ypos="head")
    sna "Firewhisky? For such a special day as today, I've brought some of my finest wine." ("snape_20")
    gen "(Yeah, right... It's probably one of mine...)" ("base", xpos="far_left", ypos="head")
    sna "Now, if I may, Miss Tonks?" ("snape_13")
    ton "*Hmm*... I tend not to drink wine too often..." ("annoyed", "narrow", "raised", "down")
    ton "Oh what the heck, go on then. I'll have a glass." ("base", "base", "annoyed", "down")
    nar "You sit down with Snape and Tonks to enjoy the match -- drinking some of the finest wine you've tasted."
    nar "Tonks' cheeks turning redder as the game continues."
    her "" ("annoyed", "base", "base", "up")
    gen "Doesn't look great..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "What do you mean?" ("open", "base", "base", "L")
    ton @ hair horny "Only thing that would make this better would be those firm cheeks on my lap!" ("horny", "narrow", "annoyed", "L")
    sna "He's talking about the game..." ("snape_09")
    ton "Game? What game..." ("open", "wide", "raised", "L")
    ton "Oh, Quidditch! Of course!" ("clench", "wide", "base", "mid")

    her "And we're now sixty-nil to Slytherin as their onslaught continues, the seekers not yet having spotted the snitch." ("open", "base", "angry", "L")
    her "If it wasn't for those foul tactics... from the brutes on the Slytherin team..." ("angry", "base", "angry", "L")
    play sound "sounds/ball_hit.ogg"
    her "Ravenclaw would have no issues beating the ever living sh--{w=2.0}{nw}" ("angry", "narrow", "angry", "L")

    call hide_characters
    with d3
    pause .2

    # Hermione gets hit in the face by a bludger
    show screen bludger_flying((530, -100), (-50, 1000))
    pause .18
    play sound ["sounds/card_punch4.ogg", "sounds/microphone_feedback.ogg"]
    show screen gfx_effect(359, 226, img="glow_effect", zoom=0.7, duration=0.3)
    call her_chibi("hit_head", flip=True)
    with vpunch

    hide screen gfx_effect
    show screen gfx_effect(295, 475, img="smoke", zoom=0.5)
    play sound "sounds/kick.ogg"
    call quidditch_stands(hole=True)
    with None

    stop background fadeout 1.5
    stop music fadeout 1.5
    pause 0.5
    play sound "sounds/crowd_gasp.ogg"
    call ton_chibi("stand_shocked", flip=True)#, 200, 50+180, flip=True)
    call gen_chibi("stand_shocked")#, 130, 10+250)
    call sna_chibi("stand_shocked", flip=True)#, 210, -40+250, flip=True)
    pause 1.0
    play background "sounds/dizzy.ogg"
    pause 2.0
    sna "*Pfffffffffff*--" ("snape_14") #TODO Custom image? Snape has wine gushing out of his nose
    sna "{size=+5}Ha-ha-HA-HA!{/size}" ("snape_42")
    stop background fadeout 1

    play music "music/silly_fun_loop.ogg" fadein 1 if_changed
    stop weather fadeout 0.5
    show screen blkfade
    with d1

    centered "{size=+7}{color=#cbcbcb}-\{Intermission\}-{/color}{/size}\n{size=-2}{color=#686868}Please stand by{/color}{/size}{w=5.0}{nw}"

    stop music fadeout 1
    pause .5

    call hide_characters
    $ snape_chibi.zorder = 1
    $ hermione_chibi.zorder = 3
    $ tonks_chibi.zorder = 2
    $ genie_chibi.zorder = 4

    call her_chibi("lying", 295, 360) #, 330, 160+186)
    call ton_chibi("stand",330, 360, flip=False) # ,395,110+180, flip=False)
    call sna_chibi("stand", 185, 375, flip=True) # ,260,250, flip=True)
    call gen_chibi("stand_alt", 155, 420) #,210,40+250)
    with d3

    $ game.weather = "overcast"
    play background "sounds/wind_long_loop.ogg" fadein 5 fadeout 2
    call weather_sound
    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    call quidditch_stands(rain=False, crowd_bj=False, tree_fire=False) # Disable Blowjob Silhouette
    hide screen blkfade
    with d5
    pause .8

    sna "I'm surprised she didn't swallow that one... with how wide she was blabbing her mouth." ("snape_42", ypos="head")
    sna "To think that liquid luck--" ("snape_45")
    ton @ cheeks blush hair neutral "{size=+5}What?{/size}" ("scream", "shocked", "base", "stare", ypos="head", flip=True, trans=vpunch)
    gen "What the fuck is liquid luck?" ("angry", xpos="far_left", ypos="head")
    ton @ cheeks blush hair angry "You gave those brutes a luck potion?!" ("mad", "base", "angry", "L")
    sna "Well..." ("snape_14")
    ton @ cheeks blush "I can't believe you, Snape...{w=0.5} look what they've done to her face!" ("mad", "base", "worried", "down")
    ton @ cheeks blush hair sad "Her beautiful face..." ("upset", "base", "worried", "down")
    sna "Looks like an improvement to me." ("snape_46")

    menu:
        "\"Way to go Snape...\"":
            gen "You knew you couldn't win, so you decided to use one of your dirty tricks..." ("base", xpos="far_left", ypos="head")
            gen "And now I need to find me a new commentator, thanks to you!" ("angry", xpos="far_left", ypos="head")
            sna "A bit hypocritical of you don't you think--" ("snape_32")
        "\"You owe me one, Snape...\"":
            sna "I {i}owe you{/i} one? What are you talking about?" ("snape_10")
            gen "She won't be able to blow me any time soon, thanks to you." ("base", xpos="far_left", ypos="head")
            gen "So yes, I think you owe me." ("base", xpos="far_left", ypos="head")
            sna "Surely you can't be--" ("snape_14")
        "\"10 points to Gryffindor!\"":
            ton @ hair angry "Are you mad?" ("scream", "base", "angry", "R")
            gen "What? I'm just joking, I'm sure she'll be fine..." ("base", xpos="far_left", ypos="head")
            sna "{size=-4}10 points to Slytherin.{/size}" ("snape_38")
            gen "Did you say something--" ("base", xpos="far_left", ypos="head")
            $ gryffindor += 10
            $ slytherin += 10


    ton @ hair angry "Quiet!" ("mad", "base", "angry", "L")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton @ hair neutral "I'm taking her to the hospital wing..." ("open", "base", "angry", "down")
    gen "What about the game...?" ("base", xpos="far_left", ypos="head")
    ton "Leave it to me..." ("open", "base", "angry", "mid")
    gen "What?" ("angry", xpos="far_left", ypos="head")

    call hide_characters
    call ton_chibi(flip=True)
    with d3
    pause .1

    call ton_walk(380, 360)

    pause .5

    play sound "sounds/referee.ogg"
    nar "Tonks signals Hooch, who then sounds her whistle to signify a short break."
    nar "A murmur erupts across the crowd, some not realizing what has gone down."

    call ton_chibi(flip=False)
    with d3

    call ton_walk(330, 360)
    pause .5

    play sound "sounds/footsteps.ogg"
    show screen blkfade
    with d5
    pause .8

    $ genie_chibi.zorder = 2

    hide screen hermione_lying
    call ton_chibi("hide")
    call her_chibi("hide")
    call gen_chibi("stand", 300, 365, flip=False)
    call sna_chibi("stand", 215, 360, flip=False)
    with d3

    hide screen blkfade
    with d5
    pause .3

    gen "She sure sobered up quickly..." ("base", xpos="far_left", ypos="head")

    with hpunch
    play sound "sounds/falling_stairs.ogg"
    pause 1

    ton "Bloody stairs!"
    gen "Never mind..." ("base", xpos="far_left", ypos="head")
    sna "This isn't good." ("snape_03")
    gen "You tell me, her face is fucked, and not in the fun way." ("angry", xpos="far_left", ypos="head")
    call sna_chibi(flip=True)
    with d3
    call gen_chibi("stand_alt", flip=False)
    with d3
    sna "I'm talking about the crowd... Granger will be out of it for now, but should be fine by the end of the day." ("snape_09")
    sna "Unfortunately..." ("snape_35")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    pause .5

    # Blackfade
    show screen blkfade
    with d5
    pause .2

    nar "A couple of minutes goes by, and there's no sign of Tonks..."

    play sound "sounds/murmur.ogg"
    # Crowd reactions aren't visible during blackfade
    # call quidditch_stands(crowd_react=[None, "emoq", None])
    # with d3

    nar "The crowd is now whispering even more, some beginning to notice the empty podium."

    # call quidditch_stands(crowd_react=[None, None, None])
    # with d3

    call gen_chibi("stand_alt", 240, 365, flip=False)
    call sna_chibi("stand", 120, 295, flip=True)

    hide screen blkfade
    with d5
    pause .5

    sna "You'd better get up there and do something." ("snape_03")
    gen "What do you want me to do? You already made me do a speech last time..." ("base", xpos="far_left", ypos="head")
    gen "I'm out of material." ("angry", xpos="far_left", ypos="head")
    gen "Also, doesn't this feel a bit like rehashing content?" ("base", xpos="far_left", ypos="head")
    sna "Fine, in that case. I'll just go up and give a motivational--" ("snape_01")

    # Genie walks past Snape, who stops
    call gen_chibi("stand", flip=True)
    with d3
    pause .5
    gen "No..." ("base", xpos="far_left", ypos="head")
    pause .3

    call gen_walk(280, 400)
    pause .8

    stop music fadeout 3.0
    $ states.gen.image.zorder = 15
    show screen blktone
    with d5
    pause 1.0
    gen "" (face="base", base="base", xpos=-10, ypos=140)
    with d3

    gen "I've got this..." ("base", xpos="far_left", ypos="base") # Genie gets into character for his speech

    play sound "sounds/microphone_feedback.ogg"
    hide screen blktone
    with d3
    pause .2
    gen "Ladies and gentlemen..." (face="open")

    gen "An intermission if you will...{w} for some motivation...{w} for both teams..." (face="base")

    menu:
        "(Let's give them what they came for...)"
        "-Independence!-":
            # Independence day
            play background "music/fanfare.ogg" fadeout 3 fadein 1.0

            hide screen genie_main
            with d3
            pause .8
            play sound "sounds/killswitch_on.ogg"
            hide screen blktone
            call quidditch_stands(spotlight=True)
            with d1
            pause 1.5

            gen "Good morning..." (face="base", trans=d3)

            call quidditch_stands(crowd_react=[None, "emoq", None])
            with d3

            gen "In less than an hour, aircraft from here will join others from around the world. And you will be launching the largest aerial battle in the history of mankind." (face="open")
            gen "" (face="base")
            sna "Not again..." ("snape_17")
            gen "Mankind...{w=0.3} that word should have new meaning for all of us today." (face="open")

            call quidditch_stands(crowd_react=[None, "emoq", "qu"])
            with d3

            gen "We can't be consumed by our petty differences anymore." (face="base")
            gen "We will be united in our common interests." (face="open")
            gen "Perhaps it's fate that today is the Fourth of July, and you will once again be fighting for our freedom, not from tyranny, oppression, or persecution... but from annihilation." (face="open")
            gen "We're fighting for our right to live, to exist." (face="angry")
            gen "And should we win the day, the Fourth of July will no longer be known as an American holiday, but as the day when the world declared in one voice." (face="open")
            gen "We will not go quietly into the night!" (face="base")
            gen "We will not vanish without a fight!" (face="open")
            gen "We're going to live on!{w=0.5} We're going to survive!" (face="angry")

            play sound "sounds/microphone_feedback.ogg"
            stop background fadeout 5.5

        "-Sunshine and rainbows-":
            # Rocky
            stop background fadeout 3.0
            play music "music/BattleThemeB.ogg" fadein 3.0 if_changed
            gen "The world ain't all sunshine and rainbows..." (face="base")
            gen "It is a very mean and nasty place, and it will beat you to your knees and keep you there permanently if you let it." (face="base")

            call quidditch_stands(crowd_react=[None, "emo8", None])
            with d3
            mal "An inspirational speech in the middle of the game?"
            call quidditch_stands(crowd_react=[None, None, None])
            with d3

            gen "You, me, or nobody is gonna hit as hard as life." (face="base")
            sna "Ain't that true..." ("snape_09")
            with None

            hide screen genie_main
            with d3
            pause .8
            play sound "sounds/killswitch_on.ogg"
            hide screen blktone
            call quidditch_stands(spotlight=True)
            with d1
            pause .8

            gen "But it ain't how hard you hit...{w=0.5} it's about how hard you can get hit, and keep moving forward." (face="angry", trans=d3)

            call quidditch_stands(crowd_react=[None, None, "emo8"])
            with d3
            cra "{size=-4}Bullshit!{/size}"
            call quidditch_stands(crowd_react=[None, None, None])
            with d3

            gen "How much you can take, and keep moving forward. That's how winning is done." (face="open")
            gen "Now, if you know what you're worth, then go out and get what you're worth." (face="open")
            gen "But you gotta be willing to take the hit, and not pointing fingers saying you ain't where you are because of him, or her, or anybody." (face="angry")
            gen "Cowards do that and that ain't you. You're better than that!" (face="angry")
            stop music fadeout 10

            play sound "sounds/crowd_cheer.ogg"
            call quidditch_stands(spotlight=False, crowd_react=["emo8", "emo7", "emo8"])
            with d3

            gen "..." (face="grin")
            gen "Nailed it." (face="grin")

        "-Be winners!-": #"\"Don't care about the scoreboard\"":
            # Hoosier
            stop background fadeout 3.0
            play music "music/victory1.ogg" fadeout 3 fadein 1.0 if_changed
            gen "There's a tradition in tournament play to not talk about the next step until you've climbed the one in front of you." (face="base")
            gen "I'm sure going to the state finals is beyond your wildest dreams, so let's just keep it right there." (face="base")

            call quidditch_stands(crowd_react=[None, None, "emoq"])
            with d3
            cho "(State finals?!?)"
            call quidditch_stands(crowd_react=[None, None, None])
            with d3

            hide screen genie_main
            with d3
            pause .8
            play sound "sounds/killswitch_on.ogg"
            hide screen blktone
            call quidditch_stands(spotlight=True)
            with d1
            pause .8

            gen "Forget about the crowds, the size of the school, their fancy uniforms, and remember what got you here." (face="angry", trans=d3)
            gen "Focus on the fundamentals that we've gone over time and time again." (face="open")
            gen "And most important, don't get caught up thinking about winning or losing this game." (face="base")
            gen "If you put your effort and concentration into playing to your potential, to be the best that you can be, I don't care what the scoreboard says at the end of the game..." (face="open")
            gen "In my book we're gonna be winners!" (face="open")
            gen "{size=+5}Okay?!!{/size}" (face="angry") #Large text

            play sound "sounds/crowd_cheer2.ogg"
            call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])
            with d3

            stop music fadeout 10
            gen "{size=+8}Alright!!{/size}" (face="open")
            gen "{size=+10}Let's go!!{/size}" (face="angry")
            gen "{size=+10}Let's go!!{/size}" (face="angry")
            play sound "sounds/microphone_feedback.ogg"
            gen "{size=+10}Let me hear it!!!{/size}" (face="angry")

    call quidditch_stands(spotlight=False, crowd_react=[None, None, None])
    with d3

    #TODO Spotlights Off, pause, genie leaves podium

    play sound "sounds/footsteps.ogg"
    call hide_characters
    with d3
    pause .5

    $ snape_chibi.zorder = 1
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 2

    call her_chibi("stand", 40, 295, flip=True)
    #call her_chibi("stand", 160, 70+186, flip=True)
    with d3
    pause .5
    call gen_chibi("stand_alt", flip=False)
    with d3
    pause .2

    call her_walk(180, 400)
    pause .3

    play background "sounds/crowd_low.ogg" fadein 3 fadeout 2

    her @ cheeks blush "I'm back!" ("soft", "base", "worried", "L", ypos="head", flip=True) #whispering #Blushing from this point forward
    sna "Miss Granger?" ("snape_05", ypos="head")
    her @ cheeks blush "It's--" ("disgust", "base", "worried", "down")

    call gen_chibi("stand", 300, 365, flip=False)
    with d3
    pause .2

    gen "Get up there, the crowd has started to suspect something..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh...{w=0.5} of course!" ("soft", "narrow", "worried", "mid")

    call her_walk(300, 400)
    pause .1
    call gen_chibi("hide")
    with d3
    call gen_chibi("stand", 20, 365, flip=True)
    with d3
    pause .5

    play sound "sounds/microphone_feedback.ogg"
    her "*Ahem*..." ("base", "base", "base", "mid", xpos=290, ypos="base", flip=True, trans=dissolve)
    her @ cheeks blush "{size=-4}Oh, these boobs are so heavy...{/size}" ("disgust", "base", "worried", "down")
    her @ cheeks blush "{size=-4}And why is this shirt so hot...{/size}" ("soft", "base", "base", "down")

    play sound "sounds/cloth_sound.ogg"
    $ hermione.equip(her_outfit_default_no_vest)
    with d3
    pause .5
    call quidditch_stands(crowd_react=[None, "emoq", None])
    with d3
    pause .3

    gen "..." ("angry", xpos="far_left", ypos="head")
    play sound "sounds/cloth_sound3.ogg"
    $ hermione.equip(her_outfit_default_no_tie_open_shirt)
    with d3
    pause 1.0

    her @ cheeks blush "{size=-4}That's better.{/size}" ("base", "base", "base", "down")
    her "So, after that short... intermission and removing that... streaker from the pitch..." ("open", "base", "base", "L")
    gen "There was a streaker on the pitch? WHEN!?!" ("angry", xpos="far_left", ypos="head")
    sna "She's deflecting the attention from the podium..." ("snape_09")
    gen "Oh, of course..." ("base", xpos="far_left", ypos="head")

    her "Now, back to your positions..." ("open", "base", "base", "mid")
    her @ cheeks blush "{size=-4}How nice, I'm not used to being listened to this easily!{/size}" ("base", "happyCl", "base", "mid")

    call quidditch_stands(crowd_react=[None, "emo7", None])
    with hpunch

    sly1 "{size=+8}Oh, shut up slut... or I'll make you!{/size}"
    her "Looking forward to it!" ("base", "base", "angry", "L")

    call quidditch_stands(crowd_react=[None, "emoq", "emoq"])
    with d3

    sly1 "..."
    gen "What's wrong with her, did she get hit too hard?" ("base", xpos="far_left", ypos="head")
    her "Hooch, give that whistle a good blow for me, will you?" ("soft", "base", "angry", "L")
    call quidditch_stands(crowd_react=[None, None, None])
    with d3
    pause 0.5

    play sound "sounds/referee.ogg"
    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    pause 1.5
    hide hermione_main
    with d3
    sna "..." ("snape_04")
    sna "*Hmm*... wouldn't be the first time a student's personality changed from a bludger hit..." ("snape_35")
    sna "Perhaps Madam Pomfrey's healing drafts aren't being distilled properly..." ("snape_09")
    gen "If you say so..." ("base", xpos="far_left", ypos="head")

    her "With those strong and muscular Slytherins in a firm lead, we're now back in the game." ("open", "base", "base", "L", trans=d3)
    play sound "sounds/ball_hit.ogg"
    her "Look at those bats swing!" ("angry", "base", "angry", "L")
    her "I wouldn't mind being hit by one of those, if you know what I'm saying." ("grin", "narrow", "angry", "L")
    her "And watch those Ravenclaws go, such finesse and style is a rare sight..." ("open", "base", "base", "L")
    her "Miss Chang sure knows how to handle that broom between her thighs." ("crooked_smile", "narrow", "angry", "L")
    cho "{size=+7}{b}!!!{/b}{/size}"

    # Section where genie goes up and touches Hermione (Tonks) under her skirt
    show screen blktone
    call hide_characters
    with d3

    sna "{size=-4}You know... Tonks isn't here right now...{/size}" ("snape_05")
    gen "{size=-4}So?{/size}" ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_37")
    gen "{size=-4}Oh...{w=0.3} I see what you mean...{/size}" ("grin", xpos="far_left", ypos="head")
    hide screen blktone
    with d3

    call gen_chibi("stand", 65, 340)
    with d5
    call gen_walk(path=[(170, 400),(210, 400)])
    call gen_chibi("hide")
    call her_chibi_scene("grope_on_podium_idle")
    with d3
    pause .5

    # Genie starts sneaking up behind Hermione (Tonks)
    her "Cute brunette passes to handsome blonde boy..." ("base", "happyCl", "base", "mid", trans=d3)
    hide hermione_main
    with d3
    pause 1.0
    call her_chibi_scene("grope_on_podium")
    with d3
    pause 2.0
    her @ cheeks blush "Whoa!" ("soft", "wide", "base", "stare", trans=d3)
    hide hermione_main
    with d3
    call quidditch_stands(crowd_react=[None, None, "emoq"])
    with d3
    call ctc

    gen "..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "No worries, ladies and gentlemen...{w=0.5} Just had a bit of a slip." ("grin", "happyCl", "worried", "mid", trans=d3)
    her @ cheeks blush "It's very...{w=0.3} very wet up here." ("soft", "narrow", "base", "mid")
    gen "(And it will be getting even wetter in a minute...)" ("grin", xpos="far_left", ypos="head")
    call her_chibi_scene("grope_on_podium_horny")
    hide hermione_main

    nar "You move your hands gently up and down underneath Hermione's skirt, massaging her butt and thighs."

    her @ cheeks blush "*Hmm*...{w=0.3} Those boys are going--{w=0.2} *Ahh*...{w=0.4} going way too fast!{w} This game might be over before we know it." ("soft", "narrow", "base", "up", trans=d3)
    gen "(Let's slow down a bit then, shall we...)" ("grin", xpos="far_left", ypos="head")
    hide hermione_main

    nar "As you continue touching Hermione, she's finding it more and more difficult to focus on the game."

    her @ cheeks blush "*Ahh*--{w=0.2} Still...{w=0.4} Still no--{w=0.2} *Ahh*...{w=0.3} Sign of the golden snitch..." ("silly", "narrow", "base", "up", trans=d3)
    gen "(It's right here...{w=0.4} I'm rubbing it for good luck...)" ("base", xpos="far_left", ypos="head")
    her "*Mmmm*...{w=0.4} Those boys sure are doing well..." ("soft", "narrow", "base", "R") #Thrill big text
    her "I've never...{w=0.3} *Hnngh*...{w=0.5} Experienced such a...{w=0.5} Such a...{w=0.6} {b}Thrill{/b} before!" ("base", "narrow", "base", "up")
    gen "(Time to get some of my own liquid luck!)" ("grin", xpos="far_left", ypos="head")
    hide hermione_main

    nar "You keep touching Hermione, moving your hand further and further underneath her skirt."
    nar "And as you begin rubbing her vagina with increased pressure, you feel a bit of a wet spot forming across her panties."

    her @ cheeks blush "Oh! That's naughty!" ("soft", "narrow", "base", "up", trans=d3)

    pause 1.0
    play sound "sounds/kick.ogg"
    with hpunch
    pause 1.0

    her @ cheeks blush "*Ahh*...{w=0.3} One of the Slytherin beaters just went head on and smashed their elbow into an opposing player..." ("grin", "narrow", "base", "L")
    hide hermione_main

    nar "Noticing Hermione's breathing becoming more and more erratic, you pick up the pace, moving your middle finger back and forth across the underside of her wet panties."

    her @ cheeks blush "And we all know...{w=0.3} *Ahh*{w=0.3} No excessive use of elbows...{w=0.3} *Ahh*{w=0.3} Permitted..." ("open", "narrow", "base", "R", trans=d3)
    her @ cheeks blush "But it seems to have done the trick!" ("base", "closed", "base", "mid")
    her @ cheeks blush "The Slytherin chasers are...{w=0.3} *Ahh*...{w=0.5} Edging ever closer... to the goal posts!" ("grin", "narrow", "base", "up")

    call her_chibi_scene("grope_on_podium_close")
    hide hermione_main

    nar "As the quaffle is thrown towards one of the hoops, you give Hermione one last rub across her panties, bringing her over the edge."
    hide screen blktone
    play sound "sounds/crowd_applause.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])
    with d3

    her @ cheeks blush "{size=+8}Goooaaal!!!{/size}" ("scream", "narrow", "angry", "up", trans=hpunch)
    hide hermione_main
    with d3
    pause 0.5

    call cum_block
    call her_chibi_scene("grope_on_podium_cum")
    pause 0.7

    nar "Hermione's legs tremble as her knees buckle, the words of her orgasm drowned out by the cheers of the crowd."
    call ctc

    # Hermione (Tonks) falls to her knees
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 2
    hide hermione_main
    call her_chibi("kneel_pant", 250, 410)
    call gen_chibi("stand", 170, 400, flip=True)
    with d5
    pause .8

    nar "As Hermione collapses to the ground, you give her a last quick look before swiftly heading back to your seat."

    call gen_chibi("stand", 20, 365, flip=True)
    call quidditch_stands(crowd_react=[None, None, None])
    with fade
    pause .6

    nar "With her legs still shaking slightly, she tries fruitlessly to stand up and compose herself."

    her @ cheeks blush "*Ahh*...{w=0.3} *Ahh*...{w=0.5} Sir...{w=0.6} that was...{w=0.6} *Ahh*..." ("open_tongue", "narrow", "worried", "up", ypos="head", flip=False)

    # Start prediction
    $ renpy.start_predict("images/CG/cho_quidditch/*.*")

    gen "{size=-4}Now, where were we?{/size}" ("grin", xpos="far_left", ypos="head")
    sna "{size=-4}Another goal for Slytherin... Although you might've missed it...{/size}" ("snape_37") #Small text
    nar "You smirk and look back at Hermione who's still on the floor trying to catch her breath."
    sna "You can wipe that smile off your face now..." ("snape_01")
    sna "Whatever your plan is, I doubt you'll succeed..." ("snape_03") #smirk
    sna "Another couple of goals and you won't win even if Miss Chang manages to catch the snitch." ("snape_45")
    sna "Ravenclaw has no chance, We've got this game in the bag." ("snape_01")
    gen "You say that..." ("grin", xpos="far_left", ypos="head")

    nar "Cho, now with her eyes fixed behind one of the goalposts -- seemingly having spotted the snitch -- gives you a quick glance and a smile as she flies up to Crabbe and Goyle."

    # Cho CG
    show cho_cg quidditch pose1 open as cg zorder 17:
        zoom 1.0
        pos (-1300, -600)
    with fade

    $ renpy.choice_for_skipping()

    cho "Hey boys, check this out..."
    cra "What do you want, slut?"
    show cho_cg quidditch pose1 base as cg zorder 17:
        zoom 1.0
        pos (-1300, -600)
        easein_quad 3.5 zoom 0.5 pos (-500, -550)
    pause 3.0
    show cho_cg quidditch pose2 smirk as cg zorder 17:
        zoom 0.5
        pos (-500, -550)
        pause 2.0
        easein_quad 3.5 zoom 0.3 pos (-60, -130)
    with d5
    nar "Cho spins around, flaunts her butt and gives them a quick wink."
    show cho_cg quidditch pose2 smirk as cg zorder 17:
        pos (-60, -130)
        zoom 0.3

    call ctc

    cra "She's showing us her ass! That luck potion Snape gave us really is working!"

    if states.cho.ev.manipulate_boys.t2_e4_complete:
        goy "Looks like this little Ravenclaw slut has come back for more, Crabbe."
        cra "Of course she has Goyle, they've got nothing but wimps in that house of hers."
        cho "Oh yes, let me see those muscly arms of yours..."

        call slap_her
        show cho_cg quidditch pose2 slap_left as cg zorder 17:
            pos (-60, -130)
            zoom 0.3

        goy "Shut up bitch."
        cho "*Mmm*..."
        cra "What the hell... Is she enjoying it?!"

        call slap_her
        show cho_cg quidditch pose2 slap_right as cg zorder 17:
            pos (-60, -130)
            zoom 0.3

        cho "Oh, thank you, please spank me more."

        nar "Cho tightens her butt cheeks and flutters her eyelashes in a way that -- to anyone except Crabbe and Goyle -- would be an obvious distraction tactic."
    else:
        goy "Or maybe this little Ravenclaw slut has finally come to her senses, Crabbe."
        goy "No surprise there... Those Ravenclaw cucks got nothing even close to our sheer strength!" #have is correct grammar here but Crabbe and Goyle are dumb shits so

        show cho_cg quidditch pose2 open as cg zorder 17:
            pos (-60, -130)
            zoom 0.3
        nar "Cho tightens her butt cheeks and flutters her eyelashes in a way that -- to anyone except Crabbe and Goyle -- would be an obvious distraction tactic."

        show cho_cg quidditch pose2 smirk as cg zorder 17:
            pos (-60, -130)
            zoom 0.3
    play sound "sounds/crowd_cheer.ogg"

    her "And there's a goal for Ravenclaw, ladies and gentlemen!"
    her "Look at those cuties go!{w=0.5} Those clothes must be completely stuck to their skin after that heavy downpour!"

    call ctc

    show cho_cg quidditch pose1 base as cg zorder 17:
        pos (-60, -130)
        zoom 0.3
    with d5

    nar "Malfoy suddenly turns around, surprised that a goal was let in, and then angrily flies up to Crabbe and Goyle."
    malf "What the hell are you guys doing?{w=0.4} Have those bludgers been hitting you too hard?"
    malf "You're supposed to be blocking the goal until that Ravenclaw girl spots the snitch!"

    show cho_cg quidditch pose1 run as cg zorder 17:
        pos (-60, -130)
        zoom 0.3

    cra "Well, about that..."
    malf "How dare you speak over me, I'm not done with you!"
    cra "But Draco--"
    malf "What?!?"
    cra "She's going after the Snitch!"

    nar "Malfoy spins his head around, and as he finally spots Cho who is currently chasing the snitch in the distance, he quickly darts after her."
    malf "You fucking idiots!"


    # End of Cho CG

    call her_chibi("stand", 300, 400, flip=True)
    hide cg
    with fade

    # Stop Prediction
    $ renpy.stop_predict("images/CG/cho_quidditch/*.*")

    her "Oh... it looks like things are heating up!{w=0.5} Malfoy has finally realised Chang is going for the Snitch..." ("open", "base", "angry", "L", flip=True, xpos=290, ypos="base", trans=d3)

    play sound "sounds/giggle2_loud.ogg"
    her "*Giggles* Look at that girl fly! I didn't think you could grip a broom so tightly... maybe I could learn a thing or two from her." ("grin", "base", "angry", "L")
    sna "I see we've been playing different games..." ("snape_37")
    gen "Quite..." ("grin", xpos="far_left", ypos="head")
    her "Chang, now only inches away, can almost taste that ball..." ("grin", "base", "angry", "up")
    her "Malfoy on his superior broom edging ever closer..." ("open", "base", "angry", "L")
    sna "Well, congratulations... You've got me beat..." ("snape_37")
    sna "Sure as hell is a better view than last season..." ("snape_20")

    play background "sounds/crowd.ogg" fadein 1 fadeout 1
    play sound "sounds/crowd_applause.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo7"])
    with d3

    her "And she's caught it!{w=0.5} Ravenclaw wins and makes it to the finals against Gryffindor!" ("smile", "base", "angry", "L")
    sna "I was looking forward to seeing that cup in my office again this year... Oh, well..." ("snape_41")
    her "And what a well-deserved victory as well!" ("soft", "narrow", "base", "mid")
    gen "You put the cup in your office?" ("base", xpos="far_left", ypos="head")

    # Fade to black
    call hide_characters
    show screen blkfade
    with d5
    pause .8

    call her_chibi("hide") # Hermione is already gone.
    call gen_chibi("stand_alt", 300, 365, flip=False)
    call sna_chibi("stand", 215, 360, flip=True)

    call quidditch_stands(crowd=[], crowd_react=[None, None, None])

    stop background fadeout 4
    stop music fadeout 2

    centered "{size=+7}{color=#cbcbcb}After the game...{/color}{/size}"

    hide screen blkfade
    with d5
    pause .5

    play background "sounds/wind_long_loop.ogg" fadein 2 fadeout 2

    sna "Well, that was good..." ("snape_03")
    sna "And to my dismay the commentary was... acceptable." ("snape_09")
    gen "What?!" ("base", xpos="far_left", ypos="head")
    gen "I thought that you didn't like miss Granger..." ("base", xpos="far_left", ypos="head")
    gen "Where's that Slytherin pride you're so adamant about?" ("grin", xpos="far_left", ypos="head")
    sna "*Hmph*... I'm sure you can find your own way back to your office..." ("snape_05")
    gen "What about our bet?" ("base", xpos="far_left", ypos="head")
    sna "The bet?" ("snape_38")
    gen "I beat you!{w=0.3} Slytherin is out of the competition!" ("base", xpos="far_left", ypos="head")
    gen "Show me the money!" ("grin", xpos="far_left", ypos="head")
    sna "..." ("snape_23")
    sna "The Bet was for Slytherin or Ravenclaw {i}winning the cup{/i}." ("snape_02")
    sna "You'll get your money if Ravenclaw beats Gryffindor in the finals." ("snape_45")
    gen "Balls..." ("angry", xpos="far_left", ypos="head")
    sna "Who would've foreseen it would be in my best interest for Gryffindor to win the cup..." ("snape_47")

    # Fade to black
    show screen blkfade
    with d9
    pause .5

    stop background fadeout 4

    play sound "sounds/steps_grass.ogg"
    nar "You make your way back to your office, wondering how the real old man could stand all these stairs..."
    nar "No wonder he always stayed in there..."

    # Reset
    $ tonks.equip(ton_outfit_last) # Equip player outfit.
    $ hermione.equip(her_outfit_last) # Equip player outfit.
    $ cho.equip(cho_outfit_last) # Equip player outfit.

    $ snape_chibi.zorder = 3
    $ tonks_chibi.zorder = 3
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 3

    jump slytherin_match_return


label slytherin_match_return:

    # The office, evening after the game
    $ game.daytime = False

    stop music fadeout 1
    #show screen blkfade
    call room("main_room")
    call gen_chibi("hide")

    $ cho_outfit_last.save()
    $ her_outfit_last.save()
    $ ton_outfit_last.save()
    $ ast_outfit_last.save()

    $ cho.equip(cho_outfit_quidditch)
    $ hermione.equip(her_outfit_default)
    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)

    $ tonks.strip("clothes")

    hide screen blkfade
    with d9
    pause 1.0

    play sound "sounds/door.ogg"
    call gen_chibi("stand", "door", "base", flip=False)
    with d3
    pause .3

    call bld
    gen "(What a day...)" ("base", xpos="far_left", ypos="head")
    gen "(Although all things considered...)" ("base", xpos="far_left", ypos="head")
    gen "(I'd say it went down rather well!)" ("grin", xpos="far_left", ypos="head")

    call gen_walk("mid", "base")

    play music "music/Music for Manatees.ogg" fadein 1 if_changed
    call gen_chibi("sit_behind_desk")
    with fade
    pause .8

    call bld
    gen "(Even though I didn't get any of the gold Snape promised me...)" ("base", xpos="far_left", ypos="head")
    gen "(Oral contracts are the worst...)" ("base", xpos="far_left", ypos="head")
    gen "(At least I got to drink some of his wine for a change...)" ("base", xpos="far_left", ypos="head")
    gen "(And getting to feel up Miss Granger's juicy ass is always worth the price of admission!)" ("grin", xpos="far_left", ypos="head")
    call bld("hide")

    # Hermione (Tonks) walks in
    play sound "sounds/door.ogg"
    call her_chibi("stand", "door", "base", flip=False)
    with d3
    pause .8

    call bld
    gen "(Speak of the devil...)" ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "That{w=0.5} was{w=0.8} amazing!" ("smile", "happy", "base", "mid", xpos="mid", ypos="base", flip=False, trans=d3)
    gen "What was?{w=0.5} Getting hit in the face?" ("base", xpos="far_left", ypos="head")
    her "I've never experienced such a thrill before..." ("base", "narrow", "base", "L")
    her "Trying to keep it together when you groped me down there..." ("soft", "narrow", "worried", "down")
    her "While everyone was watching the game..." ("base", "narrow", "base", "L")
    gen "Well, I'm glad you enjoyed it!" ("grin", xpos="far_left", ypos="head")
    her "*Hmm*...{w=0.5} I think someone deserves a reward..." ("soft", "narrow", "base", "mid") #Horny
    pause .2

    # Hermione (Tonks) starts stripping
    play sound "sounds/cloth_sound.ogg"
    $ hermione.strip("robe", "accessory", "top")
    with d5
    pause .8

    gen "Miss Granger?" ("angry", xpos="far_left", ypos="head")
    her "Be quiet you, just enjoy it!" ("base", "narrow", "base", "mid")
    gen "!!!" ("grin", xpos="far_left", ypos="head")

    play sound "sounds/cloth_sound.ogg"
    $ hermione.strip("bottom")
    with d5
    pause .8

    her "*Hmm*... You like these cute panties?" ("soft", "narrow", "base", "down")

    play sound "sounds/giggle2_loud.ogg"
    her "*Hi-Hi-Hi*" ("grin", "happyCl", "base", "mid")
    gen "..." ("angry", xpos="far_left", ypos="head")
    her "Or these little puppies..." ("base", "narrow", "angry", "mid")

    play sound "sounds/cloth_sound.ogg"
    $ hermione.strip("bra")
    with d5
    pause .8

    with hpunch
    nar "Hermione playfully shakes her breasts at you."
    her "Much better without the bra, don't you think?" ("soft", "narrow", "base", "mid")
    gen "I..." ("base", xpos="far_left", ypos="head")
    her "Don't you just love this body?" ("base", "narrow", "base", "down")
    gen "I do!" ("angry", xpos="far_left", ypos="head")
    her "I knew you did, I could feel your eyes in the back of my neck when I was up there..." ("open", "narrow", "angry", "mid")
    gen "Who wouldn't, with a body like that..." ("grin", xpos="far_left", ypos="head")
    her "*Mmmm*... Damn right..." ("angry", "narrow", "angry", "down")
    her "And since you love this butt so much..." ("base", "narrow", "base", "down")

    pause .5
    call her_chibi(flip=True)
    her "" (flip=True, trans=d3)
    pause .8

    play sound "sounds/cloth_sound.ogg"
    $ hermione.strip("panties")
    with d5
    pause .8

    her "..." ("base", "narrow", "base", "mid")
    her "What do you think?" ("soft", "narrow", "base", "mid")
    her "Do you like your student's lusciously-shaped arse, Professor?" ("soft", "closed", "base", "mid")
    gen "Your...{w=0.4} arse?" ("base", xpos="far_left", ypos="head")
    gen "I mean--{w=0.3} Of course!{w=0.5} how could I not!" ("grin", xpos="far_left", ypos="head")
    gen "Your arse looks great, Miss--" ("grin", xpos="far_left", ypos="head")

    # Cho enters
    stop music fadeout 1
    call hide_characters
    hide screen bld1
    with d3

    play sound "sounds/door.ogg"
    call cho_chibi("stand", "door", "base")
    with d3
    pause .8

    call bld
    gen "Chang?" ("angry", xpos="far_left", ypos="head")
    cho "I did it! We won the--" ("smile", "closed", "base", "mid", xpos="base", ypos="base", flip=False, trans=d3)
    her "" ("upset", "base", "base", "L", ypos="base", flip=True, trans=d3)
    cho "!!!" ("annoyed", "wide", "base", "L", trans=hpunch) #Shocked face

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "Oh, hello there, Miss Chang..." ("grin", "narrow", "angry", "L")
    her "Like what you see?" ("soft", "narrow", "base", "L")
    cho @ cheeks blush "I..." ("angry", "wide", "base", "L")

    play sound "sounds/giggle2_loud.ogg"
    her "*Hi-Hi-Hi*" ("base", "happyCl", "base", "mid")
    her "What's wrong sweetie?" ("soft", "narrow", "base", "L")
    her "Want to find out if Gryffindors taste the same as Ravenclaws?" ("smile", "narrow", "base", "L")
    cho @ cheeks heavy_blush "..." ("angry", "base", "worried", "down") #Blushes
    cho @ cheeks blush "*Hmph*!" ("annoyed", "narrow", "angry", "L")

    # Cho walks out and slams the door
    stop music fadeout 1
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi("stand", "door", "base", flip=True)
    with d3
    pause .5

    play sound "sounds/kick.ogg"
    call cho_chibi("hide")
    with hpunch
    pause .5

    call her_chibi("stand", "desk", "base", flip=False)
    with d3
    pause .5

    her "Suit yourself..." ("open", "closed", "base", "mid", xpos="mid", ypos="base", flip=False) #Shruggs it off
    gen "What the hell are you doing, Granger?" ("base", xpos="far_left", ypos="head")
    her "Granger?" ("soft", "wink", "worried", "mid") #confused

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    her "What are you talking about, genie?" ("base", "narrow", "base", "mid")
    pause .8

    # Tonks turns back into herself
    #TODO Should the naked version only happen if you've done Imperio Training maybe?
    play sound "sounds/magic4.ogg"
    call hide_characters
    call her_chibi("hide")
    call ton_chibi("stand", "desk", "base", flip=False)
    ton "" ("base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)
    call ctc

    gen "Whoa!" ("angry", xpos="far_left", ypos="head")
    ton "Oh, silly me... I'm still naked..." ("upset", "base", "base", "down")
    pause .5

    play sound "sounds/cloth_sound.ogg"
    hide tonks_main
    $ tonks.wear("all")
    ton "" ("horny", "base", "base", "mid", trans=d5)
    pause .8

    if states.gen.ev.tonks.metamorphmagi_aware: #This wont be used if we make it so you learn it first time here and hangouts unlock after this
        gen "It all makes sense now." ("base", xpos="far_left", ypos="head")
        ton "Hello sweet cheeks!" ("base", "base", "base", "mid")
        ton "Thought I was about to lose focus there for a second when you started going at it!" ("open", "base", "base", "R")
        gen "You should've told me it was you..." ("base", xpos="far_left", ypos="head")
        ton "I tried to!" ("upset", "base", "worried", "mid")
        ton "You pretty much pushed me onto the podium when I got back..." ("open", "base", "worried", "mid")
        gen "Oh, yeah..." ("base", xpos="far_left", ypos="head")
        gen "So this is the ability you were speaking of?" ("base", xpos="far_left", ypos="head")
        ton "Impressive, isn't it?" ("horny", "base", "base", "mid")

    else:
        $ states.gen.ev.tonks.metamorphmagi_aware = True
        gen "You were Miss Granger the whole time?" ("angry", xpos="far_left", ypos="head")
        gen "Plot twist of the fucking century." ("base", xpos="far_left", ypos="head")
        ton "Of course not, don't be silly..." ("open", "closed", "base", "mid")
        ton "I'm a metamorphmagus..." ("soft", "base", "raised", "mid")
        gen "A meta what?" ("base", xpos="far_left", ypos="head")
        gen "(I thought I was the only one allowed to be meta in this game...)" ("base", xpos="far_left", ypos="head")

    ton "I can change my appearance to whatever I want." ("open", "base", "base", "R")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    ton "Of course!" ("base", "wide", "annoyed", "mid")

    # Tonks turns into cho
    play sound "sounds/magic4.ogg"
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    call hide_characters
    call ton_chibi("hide")
    call cho_chibi("stand", "desk", "base", flip=False)
    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)
    pause .5

    cho "Hi professor!" ("smile", "base", "base", "mid")
    cho "Want to give this snatch a little lick?" ("soft", "narrow", "base", "mid")
    gen "!!!" ("angry", xpos="far_left", ypos="head")

    if states.ast.unlocked:
        # Tonks turns into Astoria
        play sound "sounds/magic4.ogg"
        play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
        call hide_characters
        call cho_chibi("hide")
        call ast_chibi("stand", "desk", "base", flip=False)
        ast "How about giving this little butt a spanking?" ("smile", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)

        play sound "sounds/magic4.ogg"
        play music "music/teddy-bear-waltz-by-kevin-macleod.ogg" fadein 1 if_changed
        call hide_characters
        call cho_chibi("hide")
        call ast_chibi("hide")
        call sus_chibi("stand", "desk", "base", flip=False)
        sus @ cheeks blush "You want to s-spank me? W-Why would you want to sp-spank me, professor? Did I do something wrong?" ("angry", "wide", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)

        sus @ cheeks blush "Are you going to punish me for flaunting these massive pair of--" ("horny", "wink", "base", "mid")
        sus @ cheeks blush "Wow... They really are big, aren't they... And they feel so soft..." ("smile", "base", "base", "down")
        sus @ cheeks blush "(I'll give you two the attention you deserve tonight...)" ("grin", "narrow", "base", "down")
        gen "Tonks?" ("base", xpos="far_left", ypos="head")
        sus "Oh right...{w=0.3} Where was I?" ("smile", "happy", "low", "downL")

    elif states.sus.unlocked:
        # Tonks Turns into Susan
        play sound "sounds/magic4.ogg"
        play music "music/teddy-bear-waltz-by-kevin-macleod.ogg" fadein 1 if_changed
        call hide_characters
        call cho_chibi("hide")
        call ast_chibi("hide")
        call sus_chibi("stand", "desk", "base", flip=False)
        sus "Did I do something wrong, Sir?" ("base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)

        sus "Are you going to punish me for having these massive pair of tits--" ("base", "base", "base", "mid")
        sus "Wow. They really are big... And they feel so soft..." ("base", "base", "base", "mid")
        sus "(I think I'm gonna play with them later for a little...)" ("base", "base", "base", "mid")
        gen "Tonks?" ("base", xpos="far_left", ypos="head")
        sus "Oh right... Where was I?" ("base", "base", "base", "mid")

    if states.lun.unlocked:
        #Tonks turns into Luna
        gen "Now do Luna!" ("grin", xpos="far_left", ypos="head")

        play sound "sounds/magic4.ogg"
        play music "music/wallpaper-by-kevin-macleod.ogg" fadein 1 if_changed
        call hide_characters
        call cho_chibi("hide")
        call ast_chibi("hide")
        call sus_chibi("hide")
        call lun_chibi("stand", "desk", "base", flip=False)
        lun "Professor Dumbledore, watch out for that jigglypuff on your shoulder..." ("soft", "wink", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)

        lun "Let me lick it off for you!" ("open_wide_tongue", "wink", "base", "mid") #lmao nice
        play sound "sounds/giggle2_loud.ogg"
        lun "*Hi-Hi-Hi*" ("smile", "happyCl", "base", "mid")

    # Tonks turns into snape
    gen "Nice, now do--" ("grin", xpos="far_left", ypos="head")

    play sound "sounds/magic4.ogg"
    play music "music/Dark Fog.ogg" fadein 1 if_changed
    call hide_characters
    call cho_chibi("hide")
    call ast_chibi("hide")
    call sus_chibi("hide")
    call lun_chibi("hide")
    call sna_chibi("stand",410,177+250, flip=False)
    sna "Want some of this, Genie?" ("snape_clown", xpos=320, ypos="base", flip=False, trans=morph)

    play sound "sounds/MaleGasp.ogg"
    with hpunch
    gen "*Aaaah*!" ("angry", xpos="far_left", ypos="head")
    sna "Mind if I...{w=0.4} Slithered in?" ("snape_clown")
    gen "..." ("angry", xpos="far_left", ypos="head")
    play sound "sounds/giggle2_loud.ogg"
    sna "*Hi-Hi-Hi*" ("snape_clown")

    # Tonks turns into herself
    play sound "sounds/magic4.ogg"
    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    call hide_characters
    call sna_chibi("hide")
    call ton_chibi("stand", "desk", "base", flip=False)
    ton "" ("base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=morph)
    call ctc

    ton "I'm especially proud of that last one..." ("grin", "happyCl", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "So...{w=0.2} Can all wizards do this?" ("base", xpos="far_left", ypos="head")
    ton "Nah, I was born with it." ("horny", "base", "base", "R")
    gen "This world, I swear there's something new every day..." ("base", xpos="far_left", ypos="head")
    gen "What next?{w=0.2} Can you time travel?" ("base", xpos="far_left", ypos="head")
    ton "I wish! The ministry won't let me do it..." ("open", "base", "annoyed", "mid")
    ton "If I could, I'd just go back to kill baby \"you know who\"..." ("upset", "closed", "angry", "mid")
    gen "(Why is that always the first thing people consider when talking about time travel...)" ("base", xpos="far_left", ypos="head")
    gen "(So predictable...)" ("base", xpos="far_left", ypos="head")

    gen "So... when Miss Granger got hit by that bludger..." ("base", xpos="far_left", ypos="head")
    ton "I took her to the hospital wing..." ("open", "base", "base", "mid")
    ton "And I replaced her, so she wouldn't get picked on for leaving." ("annoyed", "base", "base", "down")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "And she--" ("base", xpos="far_left", ypos="head")
    ton "She's fine..." ("open", "base", "raised", "R")
    #TODO If we had the hospital wing drawn she could offer to take you there at this line
    ton "Your face is cute when you worry, you know that?" ("base", "narrow", "worried", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "So, won't people find out you replaced her?" ("base", xpos="far_left", ypos="head")
    ton "I wouldn't worry about that." ("base", "base", "base", "R")
    ton "I can lie if I want! Who would they believe, a teacher or a bunch of delinquents?" ("silly", "happyCl", "base", "mid")
    gen "Good point..." ("base", xpos="far_left", ypos="head")
    ton "Anyway..." ("open", "base", "base", "R")
    ton "I doubt Miss Granger would tell anyone, unless she has a really good reason to do so..." ("base", "base", "angry", "mid")
    ton "*Urgh*... My head hurts." ("upset", "base", "worried", "up")
    ton "I'm gonna go sleep off whatever this is..." ("open", "base", "worried", "mid")
    ton "Too-da-loo!" ("base", "happyCl", "base", "mid")

    call ton_walk(action="leave")
    stop music fadeout 11.0

    gen "(Damn, that witch is impressive!)" ("base", xpos="far_left", ypos="head")
    gen "(She reminds me of one of those ancient, semen-stealing succubi..)" ("base", xpos="far_left", ypos="head")
    gen "(Corrupting... Enticing...)" ("angry", xpos="far_left", ypos="head")
    gen "(I'd let her suck my life force any day.)" ("grin", xpos="far_left", ypos="head")

    $ states.ton.busy = True
    $ states.sna.busy = True
    $ states.her.busy = True
    $ states.cho.busy = True

    $ states.cho.mood += 9
    $ states.cho.tier = 3
    $ states.cho.favors_unlocked = False
    $ states.cho.requests_unlocked = False
    $ states.cho.ev.quidditch.lock_training = False
    $ states.cho.ev.quidditch.lock_practice = True
    $ states.cho.ev.quidditch.lock_tactic   = False
    $ states.cho.ev.quidditch.slytherin_stage = "completed" # Prevents this event from repeating.

    # Reset
    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)
    $ cho.equip(cho_outfit_last)
    $ astoria.equip(ast_outfit_last)

    call music_block
    jump main_room_menu
