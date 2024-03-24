

### Spell Training ###

### Astoria Imperio Training ###

label ag_st_imperio:

    if not _events_completed_any:
        menu:
            gen "{size=-4}(Should I ask her to cast Imperio on Tonks?){/size}" ("base", xpos="far_left", ypos="head")

            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump astoria_favor_menu

    if states.ton.busy:
        gen "(Something tells me Tonks is not available right now, perhaps I should try later...)" ("base", xpos="far_left", ypos="head")
        $ _event.cancel()
        jump astoria_favor_menu

    if not _events_completed_any: # Intro for 1st event.
        ast "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
        gen "Ready for your first day of detention?" ("base", xpos="far_left", ypos="head")
        ast "No..." ("annoyed", "base", "base", "R")
        ast "Do I really have to go?" ("clench", "base", "base", "mid")
        gen "I could have you scrub the toilets instead..." ("grin", xpos="far_left", ypos="head")
        ast "Please don't, [name_genie_astoria]!" ("clench", "base", "worried", "mid")
        gen "Professor Tonks has some interesting lessons planned for you!{w=0.8} I'm sure you'll enjoy them." ("base", xpos="far_left", ypos="head")
        ast "Oh yeah?" ("open", "base", "base", "mid")
        ast "Well, I doubt it..." ("annoyed", "narrow", "angry", "R")
        ast "At least it's not gonna be boring, if it's her." ("open", "closed", "base", "mid")
        ast "I once had to spend an entire day, listening to McGonagall prattle on about the importance of some transfiguration spell." ("annoyed", "narrow", "angry", "R")
        ast "When all it did was turn a stupid rat yellow!" ("annoyed", "base", "base", "ahegao")
        ast "I wanna learn something that's actually fun!" ("annoyed", "narrow", "base", "down")
        gen "Like an unforgivable curse?" ("base", xpos="far_left", ypos="head")
        ast "Yes." ("annoyed", "base", "base", "mid")
        gen "Good. Because your teacher has offered to teach one of them to you, properly." ("base", xpos="far_left", ypos="head")
        ast "She offered to--{w=0.2} What?" ("clench", "base", "base", "mid")
        gen "That's what I said!" ("base", xpos="far_left", ypos="head")
        ast "I thought this was meant to be a punishment?" ("smile", "base", "base", "L")
        ast "That's wicked!" ("smile", "narrow", "angry", "down")
        gen "Off you go then. She's waiting for you..." ("base", xpos="far_left", ypos="head")
        gen "Return here with Professor Tonks for a progress report once you're done for the day." ("base", xpos="far_left", ypos="head")
        ast "Of course!" ("smile", "closed", "base", "mid")
        ast "See ya later!" ("smile", "base", "base", "mid") #smell ya later newbie! - gary oak

    # TODO: This is problematic to implement, perhaps it could be done differently once we got to workinbg on Astoria's storyline.
    # elif ag_st_imperio.points == 3: # Intro for 4th event.
    #     ast "" ("annoyed", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
    #     gen "Time for another lesson, don't you think?" ("base", xpos="far_left", ypos="head")
    #     ast "Do I really have to?" ("open", "narrow", "base", "R")
    #     ast "I'd rather not spend the day, getting yelled at..." ("annoyed", "narrow", "base", "down")
    #     gen "Nobody's gonna yell at you." ("base", xpos="far_left", ypos="head")
    #     ast "If you say so, [name_genie_astoria]." ("annoyed", "base", "base", "mid")
    #     gen "Return here after your lesson." ("base", xpos="far_left", ypos="head")
    #     ast "..." ("annoyed", "base", "base", "R")

    else:
        ast "" ("grin", "base", "base", "mid", xpos="right", ypos="base", trans=fade)
        random:
            gen "Ready for another lesson-- I mean detention?" ("base", xpos="far_left", ypos="head")
            gen "Looking forward to curse your teacher again?" ("base", xpos="far_left", ypos="head")
            gen "Ready to go see Professor Tonks?" ("base", xpos="far_left", ypos="head")
        ast "Yes, [name_genie_astoria]." ("smile", "base", "base", "mid")
        gen "I'm eager to see another demonstration of your progress!" ("grin", xpos="far_left", ypos="head")
        gen "Return to my office with your teacher afterwards." ("base", xpos="far_left", ypos="head")
        ast "Until then, [name_genie_astoria]!" ("smile", "base", "base", "R")

    play sound "sounds/door.ogg"
    call hide_characters
    call ast_walk(action="leave")
    hide screen bld1
    with d3

    # Setup
    $ ton_outfit_last.save() # Store current outfit.
    $ ast_outfit_last.save() # Store current outfit.

    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)

    $ states.ast.busy = True
    $ states.ton.busy = True

    jump end_astoria_event

label end_ag_st_imperio:
    call hide_characters
    hide screen bld1
    with d3

    $ tonks.equip(ton_outfit_last) # Equip player outfit.
    $ astoria.equip(ast_outfit_last) # Equip player outfit.

    # Increase level
    if not _events_filtered_completed_all:
        $ states.ast.level += 1

    $ states.ast.ev.imperio_with_tonks.completed_once = True

    jump end_astoria_event

label ag_st_imperio_E1:
    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)
    stop music fadeout 1.0
    play sound "sounds/door.ogg"
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",530,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with fade
    pause.8

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ast "" ("annoyed", "base", "base", "mid", xpos="base", ypos="base")
    ton "Good evening, Professor." ("base", "happyCl", "base", "mid", xpos="right", ypos="base")
    gen "Finally, you're back." ("base", xpos="far_left", ypos="head")
    ton "Yes we are." ("base", "wink", "base", "mid")
    ton "" ("soft", "base", "base", "mid")
    ast "......................" ("annoyed", "narrow", "base", "L") # embarrassed
    gen "Astoria!{w} How was your training? *Err*... I mean detention!" ("grin", xpos="far_left", ypos="head")
    ast "................................" ("annoyed", "narrow", "base", "R")
    ton "It went very well, I'd say." ("crooked_smile", "happyCl", "base", "mid")
    ton "I instructed her on how to cast the curse - properly." ("base", "closed", "base", "mid")
    ton "The proper wand movement... The correct pronunciation..." ("open", "wide", "base", "R")
    ton "There's a lot to it!" ("grin", "wide", "base", "mid")
    ton "One mishap with those - and the curse might backfire!" ("normal", "shocked", "shocked", "mid")
    ton "Sending you straight to St. Mungo's hospital - quacking like a duck!" ("annoyed", "shocked", "base", "mid")
    gen "..........." ("base", xpos="far_left", ypos="head")
    ton "I'd say she was very lucky, when using it on Miss Bones..." ("mad", "base", "base", "mid")
    ast "I knew what I was doing..." ("base", "closed", "angry", "mid")
    ast "" ("clench", "narrow", "base", "mid")
    ton "Of course you did, princess." ("soft", "narrow", "base", "L") # Happy
    ast "................................." ("annoyed", "narrow", "angry", "R") # annoyed

    ton "Now, shall we get started?" ("soft", "base", "base", "mid")
    ast "Get started - with what?" ("open", "narrow", "base", "R")
    ton "The next step of your training, of course!" ("soft", "base", "base", "R")
    ton "I'd like you to cast the Imperius curse now... On another person." ("base", "base", "angry", "L")
    ast "Wait, what?" ("angry", "base", "base", "mid")
    ast "I thought I wasn't allowed to ever use it again?" ("annoyed", "base", "worried", "L")
    ton "You aren't... That is correct." ("open", "closed", "base", "mid")
    ton "However, you are hereby given special permission!" ("grin", "base", "base", "R")
    ast "Really?" ("smile", "narrow", "base", "down") # happy
    ton "Yes, dear!" ("base", "base", "base", "R")
    ton "I believe our Professor would have no objection to that..." ("open", "closed", "base", "mid")
    ton "Would you, Professor?" ("base", "base", "angry", "mid")
    ast "Please, Professor!" ("smile", "base", "base", "mid")
    gen "*Uhm*...{w=0.4} Sure...{w=0.6} Go ahead." ("base", xpos="far_left", ypos="head")
    ton "Splendid!" ("silly", "happyCl", "base", "mid")
    ast "Yes!" ("smile", "base", "angry", "L")

    ton "You can cast it, as long as it's under the supervision of a teacher..." ("open", "base", "raised", "down")
    ton "And only within the walls of this room!" ("normal", "base", "base", "downR") # stern
    ast "Right here? In front of Professor Dumbledore?" ("open", "base", "base", "mid")
    ton "Naturally!" ("base", "closed", "base", "mid")
    ast "But who do I cast it on? Susan?" ("smile", "base", "base", "R")
    ton @ cheeks blush "Not this time, sweetheart." ("upset", "narrow", "base", "down")
    ton @ cheeks blush "Today, I'd like you to cast it on me, if you don't mind..." ("open", "closed", "base", "mid")
    ast "Wicked!" ("grin", "narrow", "worried", "down")
    ton "Let's give this old man a quick demonstration of your talents, shall we..." ("grin", "base", "shocked", "mid")

    call ast_chibi("wand",530,"base")
    with d3

    ast "" ("grin", "narrow", "base", "mid")
    gen ".............................." ("base", xpos="far_left", ypos="head")
    ton "Just like we practised..." ("open", "closed", "base", "mid")
    ton "Do the movement with your wand, and then you say--" ("open", "base", "base", "R")
    ast "Imperio!" ("angry", "narrow", "angry", "mid") # angry scream
    ast "" ("clench", "narrow", "angry", "mid")
    pause .8

    call ast_chibi("wand_casting",530,"base")
    with d3

    ton "Yes..." ("mad", "narrow", "base", "mid")
    ton "...................." ("annoyed", "narrow", "shocked", "stare")
    ton "You don't have to scream the words, darling." ("open", "closed", "raised", "L")
    ton "What's crucial is that your mind is focused and--" ("normal", "closed", "base", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    ast "IMPERIO!{w=0.8}{nw}" ("scream", "base", "angry", "mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    play sound "sounds/magic2.ogg"
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    ast "" ("clench", "base", "angry", "L", xpos="base", ypos="base")
    ton @ hair scared "........................." ("mad", "wide", "shocked", "ahegao", xpos="right", ypos="base") # shock
    ton @ hair horny "*Aaaaaah*..." ("horny", "base", "base", "ahegao") # inhales
    ast "......................" ("clench", "base", "worried", "L") # clenched teeth
    gen "What's happening to her?" ("base", xpos="far_left", ypos="head")
    ast "I just cast the spell on her..." ("open", "closed", "base", "mid")
    ast "Now she's under my command!" ("smile", "base", "base", "mid")
    gen "You don't say?" ("grin", xpos="far_left", ypos="head")
    gen "I love magic!" ("grin", xpos="far_left", ypos="head")
    call ast_chibi("wand",530,"base")
    with d3
    ast "What shall I do now, Professor?" ("clench", "base", "base", "L")
    gen "I don't know...{w=0.4} Why are you asking me?" ("base", xpos="far_left", ypos="head")
    gen "Did you two not discuss it beforehand?" ("base", xpos="far_left", ypos="head")
    ast "No. All we did was some theoretical practice of the spell..." ("open", "base", "base", "down")
    ast "I need to tell her to do something... or..." ("open", "base", "worried", "mid")
    ast "I don't know... Maybe say something?" ("clench", "base", "base", "L")
    ton "*Hmm*... Something..." ("base", "base", "worried", "up")
    ast "!!!" ("smile", "base", "base", "L")
    gen "What?" ("base", xpos="far_left", ypos="head")
    ast "She did it!" ("smile", "base", "base", "L")
    gen "Something what?" ("angry", xpos="far_left", ypos="head")
    ast "No, she just said what I asked her to say!" ("smile", "base", "base", "mid")
    gen "Oh..." ("base", xpos="far_left", ypos="head")
    ast "I believe it's working!" ("smile", "closed", "base", "mid")

    ast "*Uhm*... Professor Tonks, you can now speak freely!" ("horny", "base", "base", "L")
    ton "............................" ("base", "closed", "base", "stare")
    ton "Oh... Can I?..." ("open", "base", "base", "stare")
    ton "Thank you..." ("soft", "wide", "base", "stare")
    ast "She can hear me!" ("smile", "base", "base", "mid")
    ton "You have a really cute voice..." ("horny", "wide", "shocked", "stare")
    ast "................" ("annoyed", "base", "worried", "R")
    gen "Try something else now." ("base", xpos="far_left", ypos="head")
    ast "" ("annoyed", "base", "base", "L")
    ton @ hair horny "I feel so good!" ("soft", "wide", "shocked", "stare")
    ton @ cheeks blush "What is happening to me?" ("mad", "base", "raised", "stare")
    ton @ cheeks blush "Are you playing with me?" ("open", "base", "worried", "stare")
    ton "I want you to play with me!" ("open_wide_tongue", "narrow", "shocked", "stare") # horny
    gen "I think she's tripping..." ("base", xpos="far_left", ypos="head")
    ast "No!{w=0.6} Keep{w=0.4} - standing{w=0.4} - still!" ("clench", "closed", "worried", "mid")
    ton "Okay........." ("soft", "base", "base", "stare")
    gen "This is quite funny to watch!" ("grin", xpos="far_left", ypos="head")
    gen "Can you make her *oink*?" ("grin", xpos="far_left", ypos="head")
    ast "*Oink*?" ("open", "wink", "base", "mid")
    gen "You know, like a pig..." ("base", xpos="far_left", ypos="head")
    ast "Yes, we can try that!" ("clench", "base", "base", "mid")
    ast "Professor Tonks, I demand that you *oink*!" ("open", "base", "base", "L")
    ton "*Huh*?..." ("open", "wide", "base", "stare")
    ast "*Oink*!" ("open", "base", "angry", "L")
    ton @ cheeks blush "..................." ("normal", "wide", "base", "stare")
    ast "Do it already!" ("angry", "base", "angry", "L")
    ast "*Oink!*{w=0.8}-*oink*!{w=0.8}-*oink*!" ("clench", "closed", "angry", "mid") # Angry
    gen "*He-he-he!*" ("grin", xpos="far_left", ypos="head")
    ast "*Oink*...{w=0.8} you pig!" ("scream", "base", "angry", "L", trans=hpunch) # Screaming
    ast "" ("clench", "narrow", "angry", "L")
    gen "I don't believe she's going to do it..." ("base", xpos="far_left", ypos="head")
    ast "But!" ("clench", "closed", "base", "mid")
    gen "It's pointless, girl..." ("base", xpos="far_left", ypos="head")
    gen "You can stop now..." ("base", xpos="far_left", ypos="head")
    ast "Fine..." ("annoyed", "base", "angry", "down")

    # Tonks reverts back.
    pause.2
    call hide_characters
    call ast_chibi("reset",530,"base")
    hide screen bld1
    with fade
    pause.8

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton @ cheeks blush "" ("soft", "base", "worried", "down", xpos="right", ypos="base", trans=dissolve)
    ast "" ("annoyed", "base", "angry", "mid", xpos="base", ypos="base", trans=dissolve)
    ton @ cheeks blush "Oh my..." ("soft", "base", "worried", "down", xpos="right", ypos="base")
    ton @ cheeks blush "Well that was fun!" ("base", "happyCl", "base", "down") # Happy
    ast "No it wasn't!" ("clench", "narrow", "angry", "mid")
    ast "Why weren't you doing pig noises!?" ("scream", "closed", "angry", "mid", trans=hpunch)
    ast "You refused to do what I demanded!" ("annoyed", "narrow", "angry", "R")
    ton "Yes I did!" ("soft", "base", "base", "R")
    ton "It was quite easy, actually." ("normal", "base", "raised", "down")
    ast "*Hnghhh*!" ("clench", "narrow", "angry", "down")
    ton "Don't worry. You'll have better luck next time..." ("base", "base", "shocked", "R")
    ton "Just try a bit harder." ("base", "wink", "base", "mid")
    ton "" ("soft", "base", "base", "mid")
    ast "..................................." ("annoyed", "narrow", "angry", "down")
    ton "Thank you for your assistance, Professor." ("open", "base", "base", "mid")
    ton "Let Astoria know when to visit me again for our next training session..." ("base", "base", "base", "mid")
    gen "Very well." ("base", xpos="far_left", ypos="head")
    ast "........................" ("annoyed", "base", "angry", "R")
    ton "Have a good night, Professor." ("base", "wink", "base", "mid")

    call ton_walk("door", "base")
    call ton_chibi("stand","door","base", flip=False)
    with d3
    pause.2

    ton "Come on, Astoria. I shall escort you back to your dormitory..." ("soft", "base", "base", "L", ypos="head")
    ast "................................................." ("annoyed", "base", "base", "down", ypos="head")

    # They both leave.
    call ast_walk(680, "base")

    play sound "sounds/door.ogg"
    call ast_chibi("hide")
    call ton_chibi("hide")
    with d3

    jump end_ag_st_imperio

label ag_st_imperio_E2:
    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)
    stop music fadeout 1.0
    play sound "sounds/door.ogg"
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",530,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with fade
    pause.8

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ast "" ("upset", "base", "base", "mid", xpos="base", ypos="base")
    ton "Hello, Professor." ("base", "happyCl", "base", "mid", xpos="right", ypos="base")
    ast "........................." ("upset", "base", "base", "L")
    gen "Back already?" ("base", xpos="far_left", ypos="head")
    ton "Yes, I gave Astoria a couple more pointers on how to improve the persuasiveness of the curse..." ("open", "wide", "base", "L")
    ton "The trick is to not lose your temper after casting it!" ("soft", "closed", "base", "mid")
    call ast_chibi("wand",530,"base")
    ast "........................." ("annoyed", "base", "base", "down")
    ton "This should be fun!" ("grin", "happyCl", "base", "mid")
    gen "Very good." ("base", xpos="far_left", ypos="head")

    ton "Now, Astoria, just as last time - you will cast the Imperius curse on me..." ("soft", "base", "base", "L")
    ton "And I'll do my best to resist--" ("open", "closed", "base", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    ast "IMPERIO!{w=0.8}{nw}" ("scream", "base", "angry", "mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    play sound "sounds/magic2.ogg"
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    ast "" ("clench", "base", "angry", "L")
    ton "........................." ("mad", "wide", "shocked", "ahegao") # shock

    gen "Damn it, girl!" ("grin", xpos="far_left", ypos="head")
    gen "Give me a warning next time. You scared the crap out of me..." ("base", xpos="far_left", ypos="head")
    ast "Sorry Professor!" ("smile", "base", "base", "mid") # Cute face

    ton ".........................." ("normal", "wide", "base", "stare")
    ton "*uhhhh*... I looooooove this!" ("soft", "base", "base", "stare")
    ton "It's like - I'm floating..." ("open", "wide", "shocked", "stare")
    ton "It feels... sooooooooooooo... goooooooooooood!" ("open_wide_tongue", "base", "base", "ahegao")
    ton "" ("mad", "base", "base", "ahegao")
    call ast_chibi("wand",530,"base")
    gen "(Is she getting off on this?)" ("base", xpos="far_left", ypos="head")

    ast "What shall I have her do, Professor?" ("clench", "wink", "base", "mid")

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

        "-Have her turn around-":
            ast "Yes, that's a good idea!" ("smile", "base", "base", "mid")
            ton "................................" ("normal", "wide", "base", "stare")
            ast "Professor Tonks, I command you to turn around." ("open", "base", "base", "L")
            ton "*Huh*?" ("open", "wide", "raised", "stare")
            ast "Turn around!" ("clench", "base", "angry", "L")
            gen "Remember what she said about your temper, Astoria..." ("base", xpos="far_left", ypos="head")
            ast "Oh... yes Sir! Of course..." ("smile", "closed", "base", "mid")
            ast "Turn around." ("open", "narrow", "base", "L")
            ton "......................" ("soft", "wide", "base", "stare")

            # Tonks turns around. (mirror sprite)
            call ton_chibi("stand","desk","base", flip=True)
            ton "" ("normal", "base", "base", "stare",  flip=True, trans=dissolve)
            pause.8

        "-Ask her to remove her coat-":
            ast "Yes, that should be easy." ("smile", "base", "base", "mid")
            ton "................................" ("normal", "wide", "base", "stare")
            ast "Tonks, I command you to remove your coat." ("open", "closed", "base", "mid")
            ton "*Huh*?" ("open", "wide", "raised", "stare")
            ast "Come on, do it!" ("annoyed", "base", "angry", "L")
            gen "Try saying the magic word..." ("base", xpos="far_left", ypos="head")
            ast "Imperio? But I already did--" ("open", "wink", "base", "mid")
            gen "No... Ask her politely..." ("base", xpos="far_left", ypos="head")
            ast "Oh! I got it!" ("smile", "closed", "base", "mid")
            ast "Professor Tonks, please remove your coat for me..." ("open", "base", "base", "L")
            ton "*Hmm*... okay..." ("soft", "wide", "base", "stare")

            # Tonks removes her coat.
            play sound "sounds/cloth_sound3.ogg"
            $ tonks.strip("robe")

            call ctc

            ton @ cheeks blush "" ("normal", "wide", "base", "stare", flip=False)
            pause.8

    ast "Yes, she did it!" ("smile", "base", "base", "L")
    ast "What shall I have her do next?" ("base", "base", "base", "mid")
    gen "*Hmm*................." ("base", xpos="far_left", ypos="head")

    $ d_flag_01 = False

    label .choices:

    menu:
        gen "Make her..." ("base", xpos="far_left", ypos="head")

        "\"Do pig noises again!\"" if d_flag_01 == False: # Jumps back to choices.
            $ d_flag_01 = True

            ast "Do a pig noise?" ("open", "base", "worried", "mid")
            ton "*oink*!" ("open_wide", "happyCl", "base", "stare")
            ast "She did it!" ("smile", "closed", "base", "mid")
            ton "" ("normal", "happyCl", "base", "mid")
            gen "Well done!" ("grin", xpos="far_left", ypos="head")
            ast "Do it again!" ("smile", "base", "angry", "L")
            ton @ cheeks blush "*oink*!" ("open_wide", "shocked", "worried", "stare")
            ast "*hi-hi-hi-hi*!" ("smile", "closed", "base", "mid")
            ton @ cheeks blush "" ("normal", "wide", "worried", "stare")
            gen "I believe that's enough--" ("base", xpos="far_left", ypos="head")
            ast "Do it again piggy! Ten times!" ("clench", "narrow", "angry", "L") # Angry
            ton @ cheeks blush "*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*{w=0.2}-*oink*!" ("open_wide_tongue", "wide", "base", "ahegao")
            gen "......................." ("base", xpos="far_left", ypos="head")
            ast "Agai--" ("scream", "closed", "angry", "mid", trans=hpunch)
            gen "That's enough, Astoria!" ("angry", xpos="far_left", ypos="head")
            ast "Fine..." ("annoyed", "narrow", "angry", "R")

            # Tonks returns to normal
            call hide_characters
            call ton_chibi("stand","desk","base", flip=False)
            call ast_chibi("reset",530,"base")
            with fade
            pause.8

            play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
            ast "" ("open", "base", "base", "down")
            ton @ cheeks blush "Oh wow..." ("mad", "base", "shocked", "down", flip=False)
            ton @ cheeks blush "You made me squeal like a pig!" ("mad", "happyCl", "base", "mid")
            ton "You've made quite some progress, well done Astoria!" ("grin", "narrow", "shocked", "R")
            ast "Thank you!" ("smile", "base", "base", "L")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "I have to say, I'm not that impressed..." ("base", xpos="far_left", ypos="head")
            ton "You aren't?" ("open", "wide", "shocked", "mid")
            ast "But, Professor!" ("clench", "base", "worried", "mid")
            gen "Tonks, would you please make the noise again..." ("base", xpos="far_left", ypos="head")
            ton "The noise, Professor?" ("soft", "base", "raised", "mid")
            gen "Yes. Squeal for me." ("base", xpos="far_left", ypos="head")
            ton "Very well..." ("open", "narrow", "shocked", "down")
            ton "*Oink*-*oink*!" ("open", "happyCl", "base", "mid")
            gen "See, I don't even have to use magic to make her do it!" ("grin", xpos="far_left", ypos="head")
            ton "Very funny, Sir..." ("soft", "narrow", "base", "downR")
            gen "I'd like us to try this again..." ("base", xpos="far_left", ypos="head")
            ton "Right now? Are you sure?" ("soft", "wide", "raised", "mid")
            gen "(I want to see some tits - damn it! Or hear her talk dirty...)" ("angry", xpos="far_left", ypos="head")
            gen "Yes, cast that spell again, Astoria..." ("base", xpos="far_left", ypos="head")
            call ast_chibi("wand",530,"base")
            ast "Very well, Sir..." ("smile", "closed", "base", "mid")

            # Astoria casts imperio.
            stop music fadeout 2.0
            ast "IMPERIO!{w=0.8}{nw}" ("scream", "base", "angry", "mid", trans=hpunch) # Screams it even louder

            call hide_characters
            hide screen bld1
            with d3
            pause.2

            # chibi spell animation.
            play sound "sounds/magic2.ogg"
            call ast_chibi("wand_imperio",530,"base")
            with hpunch
            pause.8

            play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
            ast "" ("clench", "base", "angry", "L")
            ton "*Hmm*............." ("base", "base", "base", "ahegao")
            call ast_chibi("wand",530,"base")
            ast "And now?" ("open", "base", "base", "mid")

            jump .choices

        "\"Say something naughty!\"": # Fails
            ast "*Huh*?..." ("open", "base", "worried", "mid")
            gen "Wouldn't you like to hear your teacher say something shameful?" ("grin", xpos="far_left", ypos="head")
            ast "Yes!" ("smile", "base", "angry", "L")
            ast "And what exactly?" ("clench", "base", "base", "mid")
            gen "I don't know... You should think of something..." ("base", xpos="far_left", ypos="head")
            gen "You're the one with the magic stick, after all..." ("base", xpos="far_left", ypos="head")
            ton "......................." ("normal", "wide", "base", "stare")
            ast "Okay... Professor Tonks..." ("open", "base", "worried", "L")
            ast "I want you to repeat after me..." ("open", "closed", "base", "mid")
            ton "..................................." ("horny", "wide", "base", "stare")
            ast "I... am... a..." ("open", "base", "worried", "L")
            ton "I am a--" ("soft", "wide", "base", "stare")
            ast "dirty!{w} filthy!{w} pig!" ("open", "narrow", "base", "L")
            ton @ cheeks blush "..................................." ("soft", "base", "base", "stare")
            ast "Go on, say it!" ("clench", "narrow", "base", "L")
            ast "I'm a dirty... Filthy... Pig!" ("open", "closed", "base", "mid")
            ton @ cheeks blush "*Hi-hi*!..." ("base", "happyCl", "shocked", "mid")
            ast "SAY IT!" ("scream", "base", "angry", "L") # Scream
            gen "Time-out!" ("angry", xpos="far_left", ypos="head")
            ast "No! She has to do what she's told!" ("clench", "narrow", "angry", "mid")
            gen "She clearly isn't going to..." ("base", xpos="far_left", ypos="head")
            gen "We should take a break here..." ("base", xpos="far_left", ypos="head")
            ast "......................." ("annoyed", "narrow", "angry", "mid")

            # Tonks returns to normal.
            pause.2
            call hide_characters
            call ton_chibi("stand","desk","base", flip=False)
            call ast_chibi("reset",530,"base")
            hide screen bld1
            with fade
            pause.8

            play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
            ast "" ("annoyed", "base", "angry", "mid")
            ton "*huh*..." ("disgust", "base", "base", "down", flip=False)
            ton "Well that was something, wasn't it?" ("soft", "closed", "base", "mid")
            ast ".................................." ("annoyed", "narrow", "angry", "L")
            gen "You resisted her curse again." ("base", xpos="far_left", ypos="head")
            ton "Yes..." ("upset", "base", "base", "L")
            ton "I'm sorry, honey!" ("annoyed", "narrow", "worried", "R")
            ast ".................................." ("annoyed", "narrow", "angry", "down")
            ton "You can't expect to succeed right away now, can you?" ("normal", "closed", "raised", "mid")
            ton "To master a spell it takes time - and regular practising..." ("normal", "narrow", "base", "R")
            ton "Or else anyone could do it." ("open", "closed", "shocked", "mid")
            ton "We'll try again next time..." ("base", "narrow", "raised", "R")
            ast "............................" ("upset", "narrow", "base", "down")
            ton "Have a good night, Professor." ("soft", "base", "base", "mid")

            call ton_walk("door", "base")
            call ton_chibi("stand","door","base", flip=False)
            with d3
            pause.2

            ton "After you, Astoria." ("open", "base", "base", "L", ypos="head")
            ast "..........................." ("upset", "base", "base", "L", ypos="head")

            # They both leave.
            call ast_walk(680, "base")

            play sound "sounds/door.ogg"
            call ast_chibi("hide")
            call ton_chibi("hide")
            with d3

            $ states.ast.mood += 12

            # Event fails.

            gen "(I don't think we made much progress here...)" ("base", xpos="far_left", ypos="head")

            $ tonks.equip(ton_outfit_last) # Equip player outfit.
            $ astoria.equip(ast_outfit_last) # Equip player outfit.

            call music_block

            # Event resets. (No progress)
            $ _event.cancel()

            jump main_room_menu

        "\"Show us those tits!\"": # Succeeds
            pass

    ast "What?" ("clench", "base", "base", "mid")
    gen "Have her show us her breasts!" ("grin", xpos="far_left", ypos="head")
    ast "Professor?!" ("open", "closed", "worried", "mid")
    gen "You did the same to Miss bones, did you not?" ("base", xpos="far_left", ypos="head")
    ast "Yes, but..." ("open", "narrow", "worried", "mid")
    ast "I doubt Professor Tonks would be okay with that, she'll just refuse like she did before!" ("clench", "narrow", "base", "L")
    gen "Did you have those concerns with Susan as well?" ("base", xpos="far_left", ypos="head")
    ast "Susan didn't require much convincing, her boobs were already falling out of her--" ("clench", "narrow", "base", "L")
    gen "Just try it." ("base", xpos="far_left", ypos="head")
    gen "She can refuse to do it if she really doesn't want to..." ("base", xpos="far_left", ypos="head")
    ast "Fine... But it's a waste of time." ("annoyed", "base", "base", "L")
    ast "Professor Tonks, I'd like you to show us your..." ("open", "base", "base", "mid")
    ast "*Uhm*..." ("upset", "base", "base", "down")
    ast "Your breasts!" ("clench", "closed", "base", "mid") # embarrassed
    ton "Oh..." ("open", "wide", "shocked", "up")
    ton "............................" ("soft", "wide", "worried", "stare")
    gen "(Fingers crossed!)" ("angry", xpos="far_left", ypos="head")
    ton "............................" ("clench", "narrow", "base", "stare") # Clenched teeth
    ast "What the--{w=0.4} I think she's struggling!" ("smile", "base", "base", "L")
    gen "Very good, girl!" ("angry", xpos="far_left", ypos="head")
    gen "Pressure her more! I want to see those puppies!" ("angry", xpos="far_left", ypos="head")
    ast "Professor Tonks, show us your breasts! Now!" ("open", "base", "angry", "L")
    gen "(It was easier for her to resist doing pig noises...)" ("base", xpos="far_left", ypos="head")
    gen "(Could it be that she {b}wants{/b} to show them to us?{w} And is resisting that inner urge?)" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "................................" ("mad", "wide", "worried", "stare") # Really struggling!
    gen "(What a slut!)" ("angry", xpos="far_left", ypos="head") # Small text
    ast "Come on, do it!" ("clench", "narrow", "angry", "L")
    ton @ hair horny "*Hnnnngh*!..." ("mad", "wide", "worried", "ahegao")
    call cum_block
    ton @ cheeks blush "*Aaaaahhh*..." ("open_wide_tongue", "base", "worried", "ahegao") # Relieved
    gen "(Did she just--)" ("angry", xpos="far_left", ypos="head")
    ton @ cheeks blush "" ("open", "narrow", "worried", "stare")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Girl, I think your teacher is done for..." ("base", xpos="far_left", ypos="head")
    ast "What?" ("clench", "base", "worried", "mid")
    ton @ cheeks blush "" ("normal", "closed", "worried", "stare")
    gen "She \"broke the curse.\" You can stop now..." ("base", xpos="far_left", ypos="head")
    ast "*Aww*..." ("upset", "narrow", "base", "down")
    ast "If you say so, Professor..." ("annoyed", "base", "base", "mid")

    # Tonks returns to normal.
    pause.2
    call hide_characters
    call ast_chibi("reset",530,"base")
    hide screen bld1
    with fade
    pause.8

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "" ("annoyed", "base", "base", "mid")
    ton @ cheeks blush "*Ouch*... That was painful!" ("mad", "closed", "base", "mid", flip=False)
    ton @ cheeks blush "You nearly got me there." ("disgust", "base", "shocked", "R")
    ast "Did I really?" ("smile", "base", "base", "mid")
    ton @ cheeks blush "Yes, well done, Astoria!" ("open", "base", "base", "down")
    ast "Thank you!" ("smile", "closed", "base", "mid")
    gen "Was it really such a struggle for you to not get your breasts out?" ("base", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush "*Uhm*..." ("mad", "base", "base", "down")
    gen "*He-he-he*!" ("grin", xpos="far_left", ypos="head")
    ton @ cheeks blush "Shall we wrap it up for today?" ("upset", "base", "shocked", "downR")
    ton "I'm sure you'll do even better next time, Astoria." ("soft", "base", "shocked", "R")
    ast "{size=-4}Yes... Finally I shall release my unlimited power...{/size}" ("smile", "narrow", "base", "L")

    play sound "sounds/thunder_2.ogg"
    pause .5

    if game.weather in {"clear", "cloudy"}:
        gen "Where the hell did that thunder come from?" ("base", xpos="far_left", ypos="head")
    else:
        gen "What the--" ("base", xpos="far_left", ypos="head")

    #Astoria walks to door but waits for Tonks.
    call ast_walk(680, "base")
    call ast_chibi("stand", 680, "base", flip=False)
    with d3

    ton "Have a good night, Professor!" ("base", "happyCl", "base", "mid")
    gen "Until next time..." ("base", xpos="far_left", ypos="head")

    # Tonks walks to door and they both leave
    call ton_walk("door", "base")

    hide tonks_main
    call ton_chibi("leave")
    hide astoria_main
    call ast_chibi("stand", 680, "base", flip=True)
    pause .3
    call ast_chibi("leave")
    with d3

    gen "(And they say I'm the big, bad pervert...)" ("base", xpos="far_left", ypos="head")

    jump end_ag_st_imperio

label ag_st_imperio_E3:
    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)
    stop music fadeout 1.0
    play sound "sounds/door.ogg"
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",500,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with fade
    pause.8

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ast "" ("annoyed", "base", "base", "mid", xpos="base", ypos="base")
    ton "Well, Professor." ("open", "closed", "base", "mid", xpos="right", ypos="base")
    ton "We're back..." ("soft", "wink", "base", "mid")
    ast "..." ("annoyed", "base", "base", "L")
    gen "Did you make any progress today?" ("base", xpos="far_left", ypos="head")
    ton "Most certainly!" ("base", "wide", "base", "mid")
    ton "Professor, you aren't questioning my abilities as a teacher, are you?" ("base", "closed", "annoyed", "mid")
    gen "Of course not..." ("base", xpos="far_left", ypos="head")
    gen "You're very skilled at what you do!" ("grin", xpos="far_left", ypos="head")
    gen "You've shown me, many times." ("grin", xpos="far_left", ypos="head")
    ton "Thank you! {heart}" ("base", "narrow", "base", "mid")
    ast "*Ugh*..." ("clench", "narrow", "base", "down") # Disgusted from the flirting?

    call ast_chibi("wand",530,"base")
    with d3
    ton "I could teach you a thing or two as well, Professor." ("base", "base", "shocked", "down")

    call ast_chibi("wand_casting",530,"base")
    with d3
    ton "Even the great Albus Dumbledore doesn't know everything about--" ("soft", "closed", "angry", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    ast "IMPERIO!{w=0.8}{nw}" ("scream", "base", "angry", "mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    play sound "sounds/magic2.ogg"
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    ast "" ("clench", "base", "angry", "L")
    ton "*Hngh*!..." ("mad", "wide", "shocked", "ahegao") # shock
    ton @ hair horny "*Hmm*..." ("base", "base", "base", "ahegao")

    call ast_chibi("wand",530,"base")
    with d3
    ast "Sir, I'm not here to listen to you two banter..." ("angry", "closed", "angry", "mid")
    gen "That's fair." ("base", xpos="far_left", ypos="head")
    gen "Time is precious, after all..." ("base", xpos="far_left", ypos="head")
    ton "..." ("normal", "wide", "base", "stare")
    ast "I've spent enough of my time today, getting lectured..." ("annoyed", "base", "angry", "L")
    gen "Isn't she supposed to do that? Lecture you?" ("base", xpos="far_left", ypos="head")
    ast "I don't need to be taught!" ("annoyed", "narrow", "angry", "mid")
    ast "I clearly already know how to cast the spell." ("clench", "base", "angry", "mid")
    gen "Surely there's always room for improvement." ("base", xpos="far_left", ypos="head")

    ast "Professor Tonks, take off that coat!" ("open", "closed", "base", "mid")
    ton "..." ("soft", "wide", "worried", "stare")
    ton "...{fast}..." ("base", "wide", "worried", "stare")

    # Remove coat.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("robe")

    call ctc

    ton @ cheeks blush "" ("base", "base", "base", "stare")
    pause.8

    ast "See, I told you I could do it!" ("smile", "narrow", "base", "mid")
    gen "Great... Don't get cocky..." ("base", xpos="far_left", ypos="head")
    ast "Don't you see, Professor?" ("annoyed", "narrow", "base", "mid")
    ast "I can make her do whatever I want!" ("smile", "narrow", "base", "mid")
    ast "I'm the greatest witch of all time!" ("clench", "base", "angry", "L")
    ton "..." ("normal", "base", "raised", "stare")
    ast "If I can pull off the Imperius curse on Professor Tonks..." ("open", "closed", "base", "mid")
    ast "Any of the other girls will be easy game for me!" ("smile", "narrow", "angry", "down") # Game as in "prey".
    ast "I'll make them rue the day they ever made fun of me!" ("clench", "closed", "angry", "mid")
    ton @ hair upset "..................................................." ("annoyed", "wide", "shocked", "stare") # Angry at Astoria
    gen "......................." ("base", xpos="far_left", ypos="head")
    ast "Tomorrow, I shall have Susan walk through school - parading those ridiculous udders of hers for all to see! That'll show her!" ("angry", "narrow", "angry", "R")
    ton @ hair angry "!!!" ("upset", "wide", "shocked", "stare") # Very angry
    ast "And then shove her into our common room - and all the boys will laugh at her cow udders!" ("smile", "closed", "angry", "R")
    gen "And she'll love every second of it!" ("grin", xpos="far_left", ypos="head")
    ast "And she'll--" ("smile", "closed", "angry", "R")
    ton @ hair angry "*Tzzzzz*!..." ("upset", "closed", "annoyed", "mid", emote="angry")
    ton "That's enough!" ("scream", "base", "angry", "R", trans=hpunch)

    # Tonks returns to normal, and puts her clothes back on.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.wear("all")
    ton "" ("mad", "base", "angry", "down")
    pause.8

    call ast_chibi("reset",530,"base")
    ast "What?" ("clench", "base", "worried", "L")
    ton "Astoria, you are dismissed!" ("open", "closed", "angry", "mid")
    ast "No! I still wanted to--" ("angry", "base", "angry", "mid")
    ton "Dismissed!" ("normal", "closed", "angry", "mid")
    ast "........................" ("annoyed", "narrow", "angry", "R")
    ast "*Tzzz!*..." ("clench", "base", "angry", "mid")

    # Astoria leaves.
    call ast_walk(action="leave")

    ton @ hair angry "The nerve of that girl, I can't believe it!" ("open", "base", "angry", "R", xpos="mid", ypos="base")
    ton "I'm beginning to think teaching her an \"unforgivable curse\" might've been a bad idea after all..." ("normal", "closed", "annoyed", "mid")
    gen "How so?" ("base", xpos="far_left", ypos="head")
    ton "Didn't you hear her?" ("open", "base", "angry", "mid")
    ton "She's disregarding all of our advice!... Or at least planning to..." ("mad", "base", "angry", "R")
    ton "She's been ignoring my instructions all day!" ("annoyed", "closed", "base", "mid")
    ton "She's such a cute and stubborn girl..." ("soft", "closed", "angry", "mid")
    ton "We can't have her roaming the school - cursing people as she pleases!" ("annoyed", "base", "annoyed", "mid")

    gen "So, should we stop?" ("base", xpos="far_left", ypos="head")
    ton @ hair neutral ".................." ("annoyed", "closed", "annoyed", "mid")
    ton "Only if she refuses to follow our rules..." ("open", "narrow", "annoyed", "downR")
    ton "As long as what we're doing stays within these walls, it shouldn't be too bad." ("normal", "base", "annoyed", "R")
    ton "And besides, Imperio isn't the worst curse you could be a target of, all things considered..." ("upset", "base", "annoyed", "down")
    gen "I thought it was dangerous?" ("base", xpos="far_left", ypos="head")
    ton "Only if you use the right commands." ("open", "narrow", "annoyed", "down")
    gen "Such as asking one of their horny teachers to--" ("base", xpos="far_left", ypos="head")
    ton "The curse itself is quite harmless." ("annoyed", "closed", "base", "mid")
    ton "And it feels really good when you're under its effect..." ("soft", "base", "base", "R")
    gen "It does?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "*Mhmm*... yeah..." ("horny", "base", "annoyed", "up")
    ton "It's so goood! {heart}" ("soft", "narrow", "worried", "ahegao")
    gen "I think you're enjoying this a bit too much!" ("grin", xpos="far_left", ypos="head")
    gen "What would your students think if they knew their teacher gets off on being mind controlled?" ("grin", xpos="far_left", ypos="head")
    ton "It's not mind control..." ("annoyed", "wide", "annoyed", "up")
    gen "Suggestion... Mind control, same thing... Doesn't change the fact that you're getting off from it." ("grin", xpos="far_left", ypos="head")
    ton "................................" ("upset", "wide", "worried", "stare")
    ton "Is it that obvious?" ("disgust", "base", "worried", "L")
    gen "Can't fool a genie..." ("grin", xpos="far_left", ypos="head")
    gen "I'm a genius, it's in the name." ("base", xpos="far_left", ypos="head")
    gen "G{w=0.3} E{w=0.3} N{w=0.5} I{w=0.5} U...{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
    gen "G E N I U...{fast} hold on a second..." ("angry", xpos="far_left", ypos="head") #This makes the line change expression mid sentence
    ton "Anyway..." ("normal", "base", "base", "down")
    ton "I'll have to talk some sense into that girl before we can continue, that's for certain..." ("annoyed", "wide", "annoyed", "downR")
    gen "Of course..." ("base", xpos="far_left", ypos="head")

    ton "I'm sorry I let this situation get out of hand..." ("open", "closed", "worried", "mid")
    ton "It won't happen again, I promise." ("disgust", "base", "worried", "mid")
    gen "You did great..." ("base", xpos="far_left", ypos="head")
    gen "But next time, I'd like to see some tits!" ("grin", xpos="far_left", ypos="head")
    ton "Of course you would." ("base", "base", "annoyed", "R")
    ton "You love 'em - don't you?" ("base", "wide", "annoyed", "mid")
    gen "That I do!" ("grin", xpos="far_left", ypos="head")
    ton "I should get going. It's getting late..." ("normal", "base", "shocked", "down")
    gen "Until next time..." ("base", xpos="far_left", ypos="head")
    ton "Have a good night, [name_genie_tonks]." ("soft", "base", "base", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(G{w=0.3} E{w=0.3} N{w=0.5} I--)" ("angry", xpos="far_left", ypos="head")
    gen "(Fuck it...)" ("base", xpos="far_left", ypos="head")

    $ states.ast.mood += 12

    jump end_ag_st_imperio

label ag_st_imperio_E4:
    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)
    stop music fadeout 1.0

    call ton_walk(action="enter",xpos="desk",ypos="base")
    pause.5

    call ton_chibi("stand","desk","base", flip=True)
    with d3
    pause.1

    ton "Astoria, would you come in here please..." ("open", "closed", "base", "mid", ypos="head")
    ast "Do I have to?"
    ton "Yes, we already talked about this..." ("open", "base", "base", "R")
    ast "Fine, whatever..."
    hide screen bld1
    with d3
    pause.1

    #Astoria enters
    call ast_walk(action="enter",xpos=530,ypos="base") # Make sure it's slightly to the left of Tonks' chibi.
    pause.1

    call ton_chibi("stand","desk","base", flip=False)
    with d3
    pause.5

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "" ("base", "base", "base", "L", xpos="right", ypos="base")
    ast "..." ("annoyed", "narrow", "base", "down", xpos="base", ypos="base")

    ton "Astoria... isn't there something you'd like to say to our Headmaster?" ("soft", "base", "shocked", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ast "Yes..." ("open", "narrow", "base", "down")
    ton "" ("base", "base", "base", "R")
    ast "Sir, I'm sorry about my behaviour during our last training session." ("annoyed", "base", "base", "L")
    gen "Sure, no big deal--" ("base", xpos="far_left", ypos="head")
    ast "It was wrong of me to scream at Professor Tonks like that, or scream at you..." ("open", "narrow", "base", "L")
    gen "Fine. Let's just get to--" ("base", xpos="far_left", ypos="head")
    ton "And what else?" ("open", "closed", "base", "mid")
    ton "" ("base", "base", "base", "L")
    ast "I was disrespectful, selfish, and mean." ("open", "closed", "base", "mid")
    ast "And I should be thankful that you are granting me this opportunity." ("open", "base", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ast "I'm well aware of what is at stake here, and I shall follow the rules from now on." ("clench", "narrow", "base", "down")
    ast "..." ("annoyed", "narrow", "base", "down") # Looks away
    gen "*Ahem* Could we please just get started?" ("base", xpos="far_left", ypos="head")
    gen "(I'm dying to see some tits!)" ("angry", xpos="far_left", ypos="head")
    ast "........................" ("annoyed", "base", "base", "R")
    ton "Very good, Astoria." ("base", "happyCl", "base", "mid")
    ton "I'm proud of you. {heart}" ("grin", "base", "base", "R")
    ast "........................." ("annoyed", "base", "base", "down") # embarrassed
    gen "......................." ("base", xpos="far_left", ypos="head")

    ton "So, let's begin..." ("base", "wide", "base", "mid")
    call ast_chibi("wand",530,"base")
    with d3
    ton "Astoria, try and focus on what we went through today..." ("open", "base", "base", "down")
    ton "Keep good track of your emotions after channelling the spell..." ("open", "closed", "base", "mid")
    ton "Anger and rage will cause you to lose control - and eventually break the connection with the target..." ("normal", "base", "annoyed", "L")
    ton "Do your best to be as thoughtful, nice, and endearing as you possibly can towards your target..." ("base", "base", "base", "L")
    ast "" ("annoyed", "base", "base", "R")
    ton "The stronger the emotional bond - the better." ("open", "closed", "base", "mid")
    ton "So try to charm them a bit while you're at it!" ("soft", "base", "base", "L")
    ton "It is called a charm for a reason, after all!" ("base", "happyCl", "base", "mid")
    ast "....................." ("annoyed", "base", "worried", "down")
    gen "...................." ("base", xpos="far_left", ypos="head")
    ton "Not a very good joke - I gather..." ("annoyed", "wide", "raised", "mid")
    gen "I'm sorry. I was only half paying attention..." ("base", xpos="far_left", ypos="head")
    ton "Very well..." ("upset", "base", "shocked", "L")

    ton "Now then, let's get on with it, shall we?" ("base", "wink", "annoyed", "mid")
    ast "..." ("annoyed", "base", "base", "mid")
    call ast_chibi("wand_casting",530,"base")
    with d3
    ton "Astoria, as soon as I'm ready, I'd like you to--" ("open", "closed", "base", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    ast "IMPERIO!{w=0.8}{nw}" ("scream", "base", "angry", "mid", trans=hpunch) # Screams it even louder

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    play sound "sounds/magic2.ogg"
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    ast "" ("annoyed", "base", "base", "L")
    ton @ hair horny "........................." ("mad", "wide", "shocked", "ahegao") # shock

    gen "......................" ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush hair horny "*Aaaaah*..." ("open", "base", "shocked", "ahegao")
    call ast_chibi("wand",530,"base")
    with d3
    ast "I'm getting really good at this!" ("smile", "base", "angry", "L")
    ton "......................." ("normal", "wide", "base", "stare")
    ast "What shall I have her do, Professor?" ("smile", "base", "base", "mid")

    gen "*Hmm*... How about..." ("base", xpos="far_left", ypos="head")
    menu:
        "\"Make her turn around!\"": # She's facing Astoria
            ast "Very well, Sir." ("base", "base", "worried", "mid")
            ast "Professor, please turn around for me..." ("open", "base", "base", "L")
            ton "*Hmm*... Yes!" ("base", "base", "worried", "stare")

            # Tonks turns around
            call hide_characters
            hide screen bld1
            with d3
            pause.1

            call ton_chibi("stand","desk","base", flip=True)
            with d3
            pause.5

            ast "" ("clench", "wink", "worried", "mid")
            ton "" ("base", "base", "base", "L", flip=True)
            pause.8

            ton "........................" ("horny", "wide", "base", "stare")
            ast "*Uhm*..." ("clench", "narrow", "worried", "R") # Astoria is uncomfortable

        "\"Let her face me!\"":
            ast "Very well..." ("open", "base", "base", "mid")

    ast "And now?" ("base", "base", "base", "mid")
    gen "Her coat! Tell her to take it off!" ("grin", xpos="far_left", ypos="head")
    ast "Professor Tonks, please remove your coat for me." ("open", "base", "worried", "L")
    ton "..." ("base", "base", "base", "stare")

    # Remove coat.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("robe")
    ton "" ("base", "base", "base", "ahegao")
    pause.8

    gen "You're doing great, Astoria!" ("grin", xpos="far_left", ypos="head")
    gen "It's like watching you teach a puppy new tricks..." ("grin", xpos="far_left", ypos="head")
    ton ".........................." ("soft", "narrow", "base", "ahegao") # ahegao
    ast "If you say so, Sir." ("clench", "base", "base", "down")
    gen "Let's move on to the next trick, shall we?" ("base", xpos="far_left", ypos="head")
    gen "Ask her to get those tits out!" ("grin", xpos="far_left", ypos="head")
    ast "Her what?!" ("clench", "base", "base", "mid")
    gen "Her breasts, girl..." ("base", xpos="far_left", ypos="head")
    gen "Tell her to remove her top." ("base", xpos="far_left", ypos="head")
    ast "Right now?" ("open", "wink", "base", "mid")
    ast "But..." ("clench", "base", "base", "mid")

    if tonks.xzoom == -1: # Facing Astoria
        ast "Can I at least tell her to turn around again?" ("clench", "base", "worried", "R")
        gen "Why? Scared of your teacher's enormous rack?" ("base", xpos="far_left", ypos="head")
        ast "What?{w} As if!" ("annoyed", "narrow", "angry", "R")
        gen "I doubt she'd like to show them to you anyway..." ("grin", xpos="far_left", ypos="head")
        ton @ hair horny "......................" ("soft", "base", "base", "ahegao") # Ahegao
        ast "............" ("annoyed", "base", "worried", "mid")
        gen "Go on..." ("base", xpos="far_left", ypos="head")

    else: # Facing Genie
        ast "I'm not sure if she'd be okay with that." ("open", "base", "worried", "mid")
        gen "This again?" ("base", xpos="far_left", ypos="head")
        ast "You'd have to close your eyes first, Professor!" ("open", "closed", "base", "mid")
        gen "What?" ("base", xpos="far_left", ypos="head")
        gen "Are you giving orders to me now as well, girl?" ("base", xpos="far_left", ypos="head")
        ast "Close your eyes!" ("angry", "narrow", "angry", "mid")
        gen "Not a chance!" ("base", xpos="far_left", ypos="head")
        ast "......................." ("annoyed", "base", "angry", "R")
        ast "It won't be my fault if she gets mad at you later!" ("open", "narrow", "base", "down")
        gen "Sure, whatever..." ("base", xpos="far_left", ypos="head")
        gen "Go on already!" ("base", xpos="far_left", ypos="head")

    gen "Let's get those tits out!" ("grin", xpos="far_left", ypos="head")
    ast "Professor Tonks, I need you to remove your..." ("open", "base", "worried", "R")
    ast "Your shirt..." ("clench", "base", "base", "down")
    ton "................" ("normal", "base", "shocked", "stare")
    gen "!!!" ("grin", xpos="far_left", ypos="head")

    # Remove top.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("top")
    if tonks.is_worn("bra"): # Remove bra if True
        ast "and your bra..." ("clench", "base", "base", "down")
        play sound "sounds/cloth_sound3.ogg"
        $ tonks.strip("bra")
    ton @ cheeks blush "" ("base", "wide", "shocked", "ahegao")
    ast "" ("annoyed", "closed", "base", "mid")
    call ctc

    if tonks.xzoom == -1: # Facing Astoria
        ast "Is she... is she doing it?" ("clench", "closed", "worried", "mid") # closed eyes
        ton @ cheeks blush "............." ("grin", "wink", "base", "mid") # horny
        gen "Why don't you see for yourself?" ("grin", xpos="far_left", ypos="head")
        gen "Open your eyes, girl!" ("grin", xpos="far_left", ypos="head")
        ast "I don't want to..." ("open", "closed", "worried", "mid")
        gen "Why not?" ("base", xpos="far_left", ypos="head")
        ast "Why would I want to look at her--" ("open", "closed", "worried", "mid")
        gen "Now, now... Don't be rude to your teacher..." ("base", xpos="far_left", ypos="head")
        gen "It seems to me like she would really like to show you!" ("grin", xpos="far_left", ypos="head")
        ast "...................." ("clench", "closed", "base", "mid") # eyes still closed
        ton @ cheeks blush "" ("base", "wide", "base", "stare")
        ast "..." ("clench", "wink", "base", "mid")
        ast "...................." ("annoyed", "narrow", "worried", "R")
        gen "That wasn't too bad now, was it?" ("grin", xpos="far_left", ypos="head")
        ton @ cheeks blush hair horny "......................." ("base", "base", "base", "ahegao") # ahegao

    else:
        gen "Now would you look at that!" ("grin", xpos="far_left", ypos="head")
        ton "................" ("soft", "wide", "shocked", "stare") # horny
        gen "Those are some great breasts your teacher has there!" ("base", xpos="far_left", ypos="head")
        ton @ hair horny "................" ("soft", "wide", "base", "stare") # ahegao
        ast "I asked you not to look, Professor!" ("open", "closed", "angry", "mid")
        gen "I don't believe she minds, does she?" ("grin", xpos="far_left", ypos="head")
        ast "" ("clench", "narrow", "worried", "R")
        ton @ cheeks blush "................" ("horny", "wide", "base", "stare") # ahegao

    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "We might be able to push her even further!" ("base", xpos="far_left", ypos="head")
    ast "Further, Sir? How?" ("annoyed", "wink", "base", "mid")
    gen "By getting her to remove the rest of her clothing, of course!" ("grin", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush hair horny ".............." ("horny", "base", "shocked", "ahegao") # angry/horny expression
    gen "What do you think? Want to give it a try?" ("grin", xpos="far_left", ypos="head")
    ast "Would that really be necessary, Sir?" ("open", "base", "base", "R")
    gen "Yes.{w=0.3} it.{w=0.3} would." ("base", xpos="far_left", ypos="head")
    ast "We--{w=0.5} we could try again next time, Professor..." ("clench", "narrow", "base", "down")
    gen "Next time?" ("base", xpos="far_left", ypos="head")
    gen "Where did your enthusiasm go all of a sudden?" ("base", xpos="far_left", ypos="head")
    gen "Weren't you so eager to practise this spell?" ("base", xpos="far_left", ypos="head")
    ast "Yes, but..." ("annoyed", "narrow", "base", "down")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    ast "I don't have to explain myself to you!" ("annoyed", "narrow", "angry", "down")
    ton @ cheeks blush "" ("annoyed", "wide", "shocked", "ahegao")
    ast "..." ("annoyed", "narrow", "angry", "R")

    stop music fadeout 2.0
    gen "..." ("base", xpos="far_left", ypos="head")
    ast "I should go to bed..." ("open", "narrow", "base", "R")
    gen "Is that so..." ("base", xpos="far_left", ypos="head")
    ast "I-- *Uhm*...{w=0.5} I'm tired, Sir." ("open", "narrow", "base", "mid")
    ast "*Yaaaaawn*!..." ("open", "closed", "worried", "mid")
    ast "See?" ("annoyed", "base", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Very well..." ("base", xpos="far_left", ypos="head")
    gen "You are dismissed." ("base", xpos="far_left", ypos="head")
    ast "..." ("clench", "narrow", "worried", "down") #embarrased

    # Astoria leaves and spell fades
    call hide_characters
    hide screen bld1
    with d3
    pause.5

    call ast_chibi("reset",530,"base", flip=True)
    with d3
    pause.2

    call ast_walk(action="leave")
    pause.5

    call ton_chibi("stand","desk","base", flip=False)
    with d3
    pause.8

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton @ hair neutral "Well, that was interesting..." ("annoyed", "wide", "base", "downR", xpos="mid", ypos="base", flip=False, trans=dissolve)
    gen "Do you have any idea why she wanted to leave so abruptly?" ("base", xpos="far_left", ypos="head")
    ton "I have a couple of theories, actually..." ("soft", "closed", "base", "mid")
    gen "*Mhmm*... That curse thing, is it?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny ".................." ("soft", "wide", "base", "down") # horny stare
    ton "Would you like me to put my clothes back on?" ("grin", "narrow", "raised", "mid")
    gen "Don't feel pressured!" ("grin", xpos="far_left", ypos="head")
    ton "Very well, then..." ("base", "narrow", "base", "mid")

    # screenshake
    with hpunch
    nar "Tonks gives her breasts a quick shake for you."

    gen "Sweet!" ("grin", xpos="far_left", ypos="head")
    ton "..............." ("horny", "wink", "base", "L")
    ton "She made some good progress today, unlike last time..." ("base", "base", "shocked", "L")
    ton "And she was very polite!" ("base", "happyCl", "base", "mid")
    ton "But she isn't quite there yet..." ("upset", "base", "shocked", "down")

    gen "Does she require more training?" ("base", xpos="far_left", ypos="head")
    ton "Yes, actually..." ("soft", "narrow", "shocked", "downR")
    ton "She'll need a lot more training to pull off the Imperius curse properly..." ("open", "closed", "base", "R")
    ton "And, as you could see... It doesn't have much of an effect on me." ("soft", "base", "shocked", "down")
    ton "I could have easily avoided doing everything she's told me today, if I wanted to..." ("open", "closed", "base", "mid")
    gen "But you didn't!" ("grin", xpos="far_left", ypos="head")
    ton "It wasn't my intention to break her spirit again... She was really trying!" ("upset", "closed", "worried", "R")
    ton "Now, as you know, I'm a trained Auror..." ("normal", "wide", "shocked", "mid")
    gen "A very \"talented\" one at that!" ("base", xpos="far_left", ypos="head")
    ton "Are you just praising my tits, Sir?" ("soft", "narrow", "annoyed", "mid")
    gen "Every part of your body is worthy of praise!" ("grin", xpos="far_left", ypos="head")
    ton "Well... thank you, [name_genie_tonks]." ("base", "happyCl", "shocked", "mid")

    # Screenshake
    with hpunch
    ton "" ("horny", "narrow", "shocked", "mid")
    nar "Tonks gives her breasts another quick shake for you."

    call ctc

    ton "I suggest we do one more training session, and then call it from there..." ("base", "wide", "base", "mid")
    gen "Sounds good to me..." ("base", xpos="far_left", ypos="head")
    ton "Believe me, it's gonna be a great one!" ("soft", "wink", "base", "mid")
    gen "Are we going to see more of your... talents?" ("grin", xpos="far_left", ypos="head")
    ton "How would you like to see {b}all{/b} this Auror has to offer?" ("horny", "closed", "annoyed", "mid") # horny
    gen "Looking forward to it!" ("grin", xpos="far_left", ypos="head")
    ton "Have a good night, [name_genie_tonks]!" ("base", "base", "angry", "mid")

    # Tonks leaves.
    call ton_walk(action="leave")

    gen "(I hope she's planned something big!)" ("grin", xpos="far_left", ypos="head")

    jump end_ag_st_imperio

label ag_st_imperio_E5:
    $ tonks.equip(ton_outfit_default)
    $ astoria.equip(ast_outfit_default)
    stop music fadeout 1.0
    play sound "sounds/door.ogg"
    call ton_chibi("stand","desk","base")
    call ast_chibi("stand",530,"base") # Make sure it's slightly to the left of Tonks' chibi.
    with fade
    pause.8

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "" ("smile", "base", "base", "mid", xpos="base", ypos="base")
    ton "Hi, Professor!" ("base", "wide", "base", "mid", xpos="right", ypos="base")

    ast "Hello!" ("smile", "closed", "base", "mid", emote="happy") # Happy
    gen "All cheered up today, Astoria?" ("base", xpos="far_left", ypos="head")
    ast "Yes, Sir." ("grin", "base", "base", "mid")
    ton "She should be. We made some real progress today." ("grin", "narrow", "base", "R")
    ton "I'm very impressed with her, I've got to say!" ("base", "base", "base", "mid")
    ton "She's very close to mastering it!" ("base", "happyCl", "base", "mid")
    ast "Really?!" ("smile", "base", "base", "R")
    gen "Is that so?" ("grin", xpos="far_left", ypos="head")
    gen "Care for a demonstration?" ("grin", xpos="far_left", ypos="head")
    ast "" ("smile", "base", "base", "mid")
    ton "Of course." ("base", "base", "base", "mid")
    ton @ hair horny "I'm confident she'll be able to make me do {b}anything{/b} you want today." ("horny", "base", "base", "R") # Horny stare
    gen "Counting on it!" ("grin", xpos="far_left", ypos="head")
    ton "Make sure to give her some good suggestions, Professor!" ("open", "base", "angry", "mid")
    gen "Absolutely!" ("grin", xpos="far_left", ypos="head")
    ton "And Astoria..." ("open", "base", "raised", "L")
    ton "Today we are going to try to push me to the limit." ("base", "base", "base", "L")
    ton "You will have me do whatever Professor Dumbledore commands, without question!" ("soft", "wide", "annoyed", "L")
    ton "We will only stop with today's training once I'm able to... resist, am I clear?" ("open", "closed", "base", "L")
    ast "I suppose..." ("annoyed", "base", "base", "down")
    ton "What was that?" ("soft", "base", "base", "R")
    ast "Yes, Professor..." ("annoyed", "base", "base", "R")

    ton "Great, then you may start, Astoria..." ("base", "narrow", "base", "L")
    call ast_chibi("wand",530,"base")
    with d3
    ton "..................." ("base", "closed", "base", "mid")
    call ast_chibi("wand_casting",530,"base")
    with d3
    ast "..................." ("annoyed", "base", "base", "down")
    ton "Astoria? Would you cast the curse - please?" ("open", "base", "base", "L")
    ast "..................." ("clench", "base", "base", "down")

    # Astoria casts imperio.
    stop music fadeout 2.0
    ast "Imperio...{w=0.8}{nw}" ("open", "closed", "base", "mid")

    call hide_characters
    hide screen bld1
    with d3
    pause.2

    # chibi spell animation.
    call ast_chibi("wand_imperio",530,"base")
    play sound "sounds/magic2.ogg"
    with hpunch
    pause.8

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    ast "" ("base", "base", "base", "L")
    ton @ hair horny "*Hmm*............" ("soft", "base", "worried", "ahegao")

    gen "(Here we go!)" ("grin", xpos="far_left", ypos="head")
    ast ".............." ("grin", "base", "base", "L")
    call ast_chibi("wand",530,"base")
    with d3
    ast "What should we start with, Professor?" ("open", "base", "worried", "mid")
    gen "Let's just try the same things as last time..." ("base", xpos="far_left", ypos="head")
    gen "Ask her to take that coat off first." ("base", xpos="far_left", ypos="head")
    ast "Very well..." ("base", "base", "base", "mid")
    ast "Professor, would you please take off your coat?" ("open", "base", "base", "L")
    ton "*Hmm*... My coat?..." ("open", "base", "worried", "stare")
    ton "..............." ("normal", "wide", "base", "stare")
    ton "Sure...{heart}" ("silly", "happyCl", "base", "mid")

    # Remove coat.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("robe")
    ton "" ("base", "base", "base", "ahegao")
    pause.8

    ast "Yay!" ("smile", "narrow", "base", "mid")
    ast "Her shirt was next, right?" ("base", "base", "angry", "mid")
    gen "That is correct." ("base", xpos="far_left", ypos="head")
    ast "Yes! Take off your shirt, Professor!" ("clench", "base", "angry", "L") # menacing
    ton @ cheeks blush "*Ahhh*................" ("soft", "base", "base", "ahegao")

    # Remove top.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("top")
    $ tonks.strip("bra")
    ton @ cheeks blush "" ("base", "base", "base", "ahegao")
    pause.8

    ast @ cheeks blush "She did it!" ("smile", "base", "base", "mid")
    gen "Well{w=0.5} {i}fucking{/i}{w=0.7} done!" ("grin", xpos="far_left", ypos="head")
    gen "Next, I'd like you to--" ("base", xpos="far_left", ypos="head")
    ast "Ask her to take off her trousers!" ("grin", "base", "angry", "L")
    gen "Yes please!" ("grin", xpos="far_left", ypos="head")
    ast "Professor, please take off your trousers..." ("open", "closed", "base", "mid")
    ton @ cheeks blush "*hngh*..." ("mad", "closed", "base", "ahegao")

    # Remove bottom.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("bottom")
    $ tonks.strip("panties")
    ton "" ("base", "base", "worried", "ahegao")
    pause.5
    ast "" ("annoyed", "narrow", "angry", "down")
    pause.8
    ton @ cheeks blush "" ("horny", "wide", "shocked", "ahegao")
    call ctc

    ast "Oh wow..." ("angry", "base", "base", "down")
    ton @ cheeks blush "..................." ("horny", "base", "base", "ahegao")
    ast "Professor, how can it be that you're not wearing any underwear?!" ("angry", "base", "worried", "down") # angry embarrassed
    gen "Yes, Miss Tonks." ("base", xpos="far_left", ypos="head")
    gen "Explain yourself!" ("grin", xpos="far_left", ypos="head")
    ton @ cheeks blush "*Hmm*......." ("normal", "base", "worried", "stare")
    ast "Answer us!" ("clench", "closed", "angry", "mid")
    ton @ cheeks blush hair sad "I don't like to wear them..." ("open", "wide", "worried", "stare")
    ast "Why?!" ("open", "narrow", "angry", "L") # angry
    ton @ hair horny "I feel so much better without a bra on... or panties..." ("soft", "wide", "base", "stare")
    ast "You're a teacher! This is disgusting!" ("clench", "closed", "angry", "mid", emote="angry")
    gen "Dis-{w=0.8}gusting!" ("angry", xpos="far_left", ypos="head")

    with hpunch
    ton @ cheeks blush "{heart} {heart} {heart}" ("soft", "happyCl", "worried", "ahegao")
    ast "I can't believe my teacher is such a slut!" ("angry", "narrow", "angry", "L")
    gen "Des-{w=0.8}picable!" ("angry", xpos="far_left", ypos="head")
    ast "Are you a slut, Professor?" ("open", "narrow", "angry", "L")
    ton @ cheeks blush "..............." ("normal", "shocked", "worried", "stare") # ahegao
    ast "Are you?!" ("clench", "base", "angry", "L")
    ton @ cheeks blush hair horny "I am! {heart}" ("soft", "base", "worried", "ahegao")
    ast "I knew it!" ("smile", "narrow", "angry", "L")
    ast "That's why she has such difficulty resisting our commands!" ("open", "base", "worried", "mid")
    gen "Yes. She's clearly trying her hardest..." ("base", xpos="far_left", ypos="head")

    ton @ cheeks blush hair horny "" ("normal", "base", "shocked", "ahegao")
    ast "Professor Dumbledore, you knew exactly what her weakness would be!" ("smile", "base", "base", "mid")
    gen "I did?" ("base", xpos="far_left", ypos="head")
    gen "*Ahem*... I mean, of course I did!" ("base", xpos="far_left", ypos="head")
    ast "We're taking off her clothes, because that's what she enjoys! But could never do in school!" ("angry", "narrow", "angry", "L")
    ast "Which makes it easier for me to channel the Imperius curse..." ("grin", "base", "angry", "mid")
    ast "Because she's nothing but a weak-minded slut!" ("open", "narrow", "angry", "L") # angry
    ton @ cheeks blush hair horny "................" ("soft", "narrow", "shocked", "ahegao") # ahegao
    gen "You're on point!" ("base", xpos="far_left", ypos="head")

    ast "Take off the rest of your clothes!" ("clench", "base", "angry", "L") # angry
    gen "Yes!" ("grin", xpos="far_left", ypos="head")
    ast "Take them off, you slut!" ("scream", "closed", "angry", "mid", trans=hpunch) # scream
    ton @ cheeks blush "........{heart}" ("normal", "wide", "shocked", "stare")

    # Strip naked. Removes clothes and stockings.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("clothes")
    ton @ cheeks blush hair horny "" ("grin", "base", "base", "ahegao")
    ast "(She did it...)" ("horny", "narrow", "angry", "L")
    call ctc

    ast "Look, Professor!" ("smile", "narrow", "angry", "L")
    ast "I got her to be completely naked!" ("smile", "base", "angry", "mid")
    gen "Excellent work, [name_astoria_genie]!" ("grin", xpos="far_left", ypos="head")
    ast "Thank you, Sir!" ("smile", "closed", "base", "mid")
    ton @ cheeks blush "............." ("silly", "happyCl", "base", "stare")

    #screenshake
    with hpunch
    nar "Tonks gives her tits a little sway..."

    gen "*Argh*! (I can't take it anymore!)" ("angry", xpos="far_left", ypos="head")

    gen "..." ("angry", xpos="far_left", ypos="head")
    menu:
        "-Start masturbating!-":
            $ states.gen.masturbating = True
            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call gen_chibi("jerk_off_behind_desk")
            with d5
            pause.8

            nar "You take out your cock and start jacking off."

    ton @ cheeks blush "" ("horny", "narrow", "raised", "L")
    ast "What shall I have her do now?" ("open", "base", "base", "L")
    "*fap-fap-fap*"
    ton @ cheeks blush hair horny "" ("soft", "narrow", "shocked", "L")
    ast "Professor?" ("annoyed", "narrow", "angry", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    gen "Oh..." ("base", xpos="far_left", ypos="head")
    gen "Get her to climb my desk!" ("grin", xpos="far_left", ypos="head")
    gen "Have her do a little dance for us." ("grin", xpos="far_left", ypos="head")
    ast "Did you hear him, Professor?" ("smile", "closed", "base", "mid")
    ast "Get on that desk, and start dancing!" ("open", "narrow", "angry", "L")
    ton @ hair horny "Yes...{heart}" ("grin", "wink", "base", "mid")

    # Climb desk and dance.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    nar "After giving you a playful wink, Tonks suggestively climbs on top of your desk, getting a good glimpse of your rock-hard cock..."
    pause 1

    call ast_chibi("wand","desk","base") # Still in wand pose.
    call ton_chibi("stand","on_desk","on_desk")
    hide screen blkfade
    with d5
    call ctc

    gen "(This is getting better and better...)" ("grin", xpos="far_left", ypos="head")
    "*fap-fap-fap*"
    ton "" ("horny", "base", "raised", "down", xpos="mid", ypos="base")

    ast "Move your hips!" ("open", "narrow", "base", "L")
    call hide_characters
    hide screen bld1
    with d3
    pause.1

    # Tonks dances.
    call ton_chibi("stand","on_desk","on_desk", flip=True)
    with d3
    pause.8
    call ton_chibi("stand","on_desk","on_desk", flip=False)
    with d3
    pause.5

    ast "" ("horny", "base", "angry", "L")
    ton "............" ("grin", "base", "base", "mid")
    ast "She's really doing everything I tell her!" ("smile", "base", "angry", "mid")
    ast "Look how easy it is, Professor!" ("smile", "closed", "base", "mid", emote="hearts",trans=hpunch)

    nar "Astoria joyfully jumps up and down on the spot, making a happy squeal..."
    call hide_characters
    hide screen bld1
    with d3
    pause.1

    show screen astoria_wand_drop
    call ast_chibi("reset","desk","base") # No wand pose.
    pause.355
    play sound "sounds/wand_drop.ogg"
    pause.5

    show screen bld1
    nar "Unknowingly dropping her wand..."

    ton "" ("upset", "base", "base", "R")
    gen "*Uhm*..." ("base", xpos="far_left", ypos="head")
    ast "What's next, Professor?" ("smile", "narrow", "angry", "mid")
    gen "Next?" ("base", xpos="far_left", ypos="head")
    ast "Yes, just look at her... She's loving this!" ("clench", "narrow", "angry", "L")
    ast "Can I walk her around school like this?" ("grin", "narrow", "worried", "L")
    gen "What?" ("base", xpos="far_left", ypos="head")
    gen "Are you serious?" ("base", xpos="far_left", ypos="head")
    ast "Please!" ("upset", "base", "base", "mid")
    ton ".............." ("soft", "base", "raised", "down")
    gen "(That might be a good idea for another time...)" ("base", xpos="far_left", ypos="head")
    gen "Not today, I'm afraid..." ("base", xpos="far_left", ypos="head")
    ton "" ("annoyed", "closed", "base", "mid")
    ast "*Aww*..." ("annoyed", "narrow", "base", "down")
    gen "Don't worry, I have an even better idea!" ("grin", xpos="far_left", ypos="head")
    gen "Could you ask her to get under my table?" ("grin", xpos="far_left", ypos="head")
    ast "*Huh*?... To do what?" ("open", "base", "worried", "mid")
    ton "To give him a blowjob..." ("open", "closed", "shocked", "mid") # Tonks answers for Genie
    ast "Professor Tonks!{w} Are you serious?" ("scream", "base", "base", "L") # shocked
    ast "Why would she want to do that? That's disgusting!!!" ("clench", "base", "worried", "mid")
    gen "That-- *Uhm*..." ("base", xpos="far_left", ypos="head")
    gen "That wasn't what I would have suggested, but..." ("base", xpos="far_left", ypos="head")
    gen "I'm willing to give her a chance to try..." ("base", xpos="far_left", ypos="head")
    gen "Try to resist that urge, I mean..." ("base", xpos="far_left", ypos="head")
    ast "Are you sure it's okay...{w=0.4} I mean, As long as I don't have to look at it!" ("angry", "narrow", "base", "R")
    ast "Professor Tonks, you can get under Professor Dumbledore's desk... and..." ("open", "closed", "base", "mid")
    ast "Do \"that\" thing..." ("angry", "base", "worried", "R")
    ast "..." ("horny", "base", "worried", "mid")
    ton "............." ("base", "base", "shocked", "down", emote="hearts")

    call hide_characters
    hide screen bld1
    with d3
    #show screen blkfade
    #with d5
    pause.2

    play sound "sounds/door.ogg"
    pause.8

    call sna_chibi("stand","door","base")

    hide screen blkfade
    with d5

    # Snape enters...
    sna "Genie, I was wondering if you could help me with--" ("snape_35", ypos="head")
    stop music fadeout 2.0
    play sound "sounds/scratch.ogg"
    sna "!!!" ("snape_11", ypos="head")
    hide screen bld1
    with d3
    pause.1
    call ton_chibi("stand","on_desk","on_desk", flip=True)
    with d3
    pause.5

    ton @ hair upset "Shit!" ("mad", "base", "angry", "L", xpos="left", flip=True)
    hide tonks_main
    hide screen bld1
    with d3
    pause.1
    call ast_chibi("stand","desk","base", flip=True)
    with d3
    pause.5

    ast "*Huh*?!" ("annoyed", "narrow", "worried", "L", xpos="mid", flip=True)
    ast "*Aaaaaaaaaah*!!!......................." ("scream", "base", "base", "L", emote="shocked", trans=hpunch) # Screams
    hide astoria_main
    hide screen bld1
    with d3
    pause.1

    play sound "sounds/run_03.ogg"
    call ast_chibi("hide")
    call teleport("astoria", effect=False)
    call ast_chibi("stand",210,275+180, flip=True) # Next to Genie's chair.
    hide screen bld1
    with d3
    pause.1

    call gen_chibi("sit_behind_desk")
    with d3
    pause.5

    nar "You quickly put away your priorly liberated cock."
    gen "What's going on?" ("angry", xpos="far_left", ypos="head")
    sna "Yes! I'd like to know that as well!" ("snape_43")
    gen "Snape?!" ("angry", xpos="far_left", ypos="head")
    if states.her.status.stripping == True: # Snape saw Hermione strip
        gen "Damn it, not you again!" ("angry", xpos="far_left", ypos="head")
        gen "(You walking cock-block!)" ("angry", xpos="far_left", ypos="head")

    else:
        gen "Damn it, what are you doing here?" ("angry", xpos="far_left", ypos="head")

    call sna_walk(620,"base")
    pause.2

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    sna "What on Earth is going on here?!" ("snape_08", xpos=580 ,ypos="base")
    sna "You two better explain to me what I just witnessed!" ("snape_32")
    ton @ hair angry "Stop being such a wuss, Severus!" ("mad", "base", "angry", "L", xpos="mid", flip=True)
    ton @ hair upset "We were just practising some spells with Miss Greengrass." ("annoyed", "base", "base", "R")
    sna "And that required you to be undressed? In front of a student?" ("snape_10")
    ton @ cheeks blush "Well... she was the cause of it..." ("clench", "base", "base", "down")
    sna "Caused you to strip?" ("snape_34")
    sna "Which spells are you teaching that girl?!" ("snape_25")
    sna "Don't tell me you--" ("snape_36") # Shocked
    ton @ cheeks blush "The Imperius Curse." ("soft", "closed", "base", "mid")
    sna "I can't believe you two..." ("snape_08")
    ast "Am I in trouble now, Professor?" ("annoyed", "base", "base", "L", xpos=10) # Asking Snape
    sna "Keep quiet, girl!" ("snape_34")
    sna "............" ("snape_04") # Snape sees the wand.

    sna "Is that your wand lying on the ground, Miss Greengrass?" ("snape_03")
    ast "My wand?" ("annoyed", "base", "base", "down")
    ast "Oh no, I must have dropped it when you came in, Sir." ("clench", "closed", "worried", "mid")
    sna "Well, pick it back up!" ("snape_32")
    sna "A Slytherin takes better care of her equipment..." ("snape_10")
    ast "Yes. I'm sorry, Professor." ("clench", "closed", "angry", "mid", emote="sweat")

    call ast_walk(path=[(270, 290+180), (370,290+180), ("desk","base")])
    call ast_chibi("stand","desk","base", flip=False)
    with d3
    pause.1
    play sound "sounds/09_lock.ogg"
    hide screen astoria_wand_drop
    pause.5

    sna "You may leave, Astoria." ("snape_09", ypos="head")
    ast "..." ("clench", "base", "base", "down", ypos="head", flip=True)
    sna "Miss Greengrass..." ("snape_04")
    ast "Yes sir." ("annoyed", "base", "base", "down")

    #astoria leaves
    $ snape_chibi.zorder = 3
    $ astoria_chibi.zorder = 2

    call sna_chibi("stand",620,"base") # Updates Zorder.
    call ast_walk(action="leave")

    $ snape_chibi.zorder = 2 # Reset to default.

    # Tonks hops off your desk and walks closer to Snape.
    play sound "sounds/08_hop_on_desk.ogg"
    show screen blkfade
    with d5
    pause 1

    call ton_chibi("stand","desk","base", flip=True)
    hide screen blkfade
    with d5
    pause.5

    call ton_walk(550,"base")
    pause.8

    ton "" ("annoyed", "base", "annoyed", "L", xpos=275, ypos="base", flip=True)
    sna "........................." ("snape_05", xpos=580 ,ypos="base")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton @ hair horny "Like what you see?" ("upset", "base", "raised", "L") # Bit flirty, maybe just to calm Snape down.
    sna "............................." ("snape_12") # blushing
    gen "You couldn't have picked a worse time to burst in here..." ("angry", xpos="far_left", ypos="head")
    sna "I can imagine that..." ("snape_18")

    sna "So, Nymphadora..." ("snape_04")
    ton @ hair angry "*Tzzzzs*!......" ("annoyed", "closed", "annoyed", "mid")
    sna "Would you mind explaining to me why you were naked in the headmaster's office - with a student present?" ("snape_03")
    sna "One of my students - at that." ("snape_10")
    ton @ hair horny "Are you jealous?" ("soft", "narrow", "base", "L")
    sna "............" ("snape_14")

    sna "The question..." ("snape_18")
    ton @ cheeks blush "It's this Astoria girl..." ("soft", "base", "annoyed", "R")
    ton "There's something wrong with her..." ("open", "narrow", "base", "down")
    ton "She's cursed you see!" ("open", "wide", "worried", "L")
    ton "A blood curse... very unfortunate." ("mad", "base", "worried", "down")
    sna "A blood curse you say?" ("snape_09") #incredulous
    sna "Now that sounds serious..." ("snape_05")
    ton "Yes, very serious!" ("clench", "wide", "worried", "down")
    ton "Been in her family for generations even." ("disgust", "wide", "base", "mid")
    sna "And what are the effects of this \"Blood curse\" exactly?" ("snape_04")
    ton "Well... I believe that this curse has rendered her practically asexual!" ("clench", "base", "worried", "L")
    sna "What nonsense..." ("snape_07")
    gen "........................." ("base", xpos="far_left", ypos="head")
    ton "How dare you!" ("mad", "closed", "angry", "L")
    ton "I can recognise someone that's under a curse!" ("open", "narrow", "angry", "down")
    ton "I've been an auror for three years now, I'll have you know!" ("mad", "base", "angry", "R")
    sna "Working at that precious ministry of yours has really rubbed off on you, hasn't it?" ("snape_02")
    gen "That's enough, Severus." ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_35")
    gen "What business is conducted in this office is none of your concern." ("base", xpos="far_left", ypos="head")
    gen "You're excused..." ("base", xpos="far_left", ypos="head")
    sna ".................." ("snape_04")
    sna "Very well..." ("snape_03")
    sna "Genie...{w} Nymphadora..." ("snape_09")
    ton @ hair angry ".................." ("mad", "base", "angry", "L") # Angry stare

    #Snape leaves
    call sna_walk(action="leave")

    call ton_chibi("stand","mid","base", flip=False)
    with d3
    pause.2
    call ton_walk("desk","base")
    pause.5

    ton @ hair neutral "Thank you..." ("normal", "base", "worried", "mid", xpos="mid", ypos="base", flip=False)
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Now..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Prompt her to be honest with herself-":
            gen "I think it's time for some honesty." ("base", xpos="far_left", ypos="head")
            ton "Regarding?" ("soft", "base", "shocked", "downR")
            gen "Everything that we've been doing with the Astoria girl." ("base", xpos="far_left", ypos="head")
            ton "Oh..." ("upset", "base", "worried", "down")
            ton @ cheeks blush "Well, we've been helping her haven't we?" ("open", "base", "shocked", "down")
            ton @ cheeks blush "She's such an uptight and oppressed cute little...{w=0.4} girl." ("upset", "closed", "raised", "down")
            ton @ cheeks blush "..." ("mad", "narrow", "base", "downR")
            ton @ cheeks blush "How can I not help her, even if she's a Slytherin." ("upset", "closed", "base", "mid")
            gen "[name_tonks_genie]... You aren't convincing anyone." ("base", xpos="far_left", ypos="head")
            ton @ cheeks blush "To think such an innocent girl could be the victim of such an--" ("open", "closed", "base", "down")
            gen "Tonks!" ("base", xpos="far_left", ypos="head")
            ton "Alright..." ("annoyed", "base", "annoyed", "down") #exasperated
            ton "The blood curse may have been a little white lie on my part." ("annoyed", "narrow", "base", "down")
            gen "And?" ("base", xpos="far_left", ypos="head")
            ton "And the imperio training with Astoria may have been for my own benefit." ("soft", "narrow", "annoyed", "downR")
            gen "..." ("base", xpos="far_left", ypos="head")
            ton @ cheeks blush "Having her cast it on me was exclusively for my own personal enjoyment." ("annoyed", "base", "base", "down")
            gen "(What a surprise...)" ("base", xpos="far_left", ypos="head")
            gen "Why weren't you honest with me?" ("base", xpos="far_left", ypos="head")
            ton "*Sigh*..." ("open", "narrow", "base", "R")
            ton @ cheeks blush "Perhaps I've been taking this favour business... thing a bit too lightly." ("open", "narrow", "raised", "down")
            ton "I've been telling myself that it's as much for the students' benefit as it is my own." ("upset", "closed", "worried", "mid")
            ton "\"I'll help them explore their sexuality\"." ("annoyed", "closed", "base", "mid")
            ton "\"It'll do them good\"." ("annoyed", "closed", "base", "mid")
            gen "We both know that is not the reason why we're doing this." ("base", xpos="far_left", ypos="head")
            ton "Yes..." ("upset", "base", "base", "down")
            ton "A small voice in my head knows it..." ("annoyed", "base", "base", "mid")
            ton @ hair angry "And I can't help that I'm just so god...{w=0.4} damn...{w=0.3} horny!" ("open_wide", "closed", "angry", "mid")
            ton @ hair horny "All the bloody time!" ("open_wide_tongue", "base", "base", "ahegao")
            ton @ hair horny "See!" ("annoyed", "base", "annoyed", "up")
            nar "You notice the bright pink colour of her hair - once again..."
            gen "You should stop lying to yourself, it's not healthy..." ("base", xpos="far_left", ypos="head")
            gen "I'm immortal - and even I know that!" ("base", xpos="far_left", ypos="head")
            gen "Embrace why you chose to be a part of this, you've got a pretty good gig here." ("base", xpos="far_left", ypos="head")
            ton "Yes, you're right." ("soft", "narrow", "base", "L")
            gen "You're doing this for yourself, it's okay to be selfish." ("base", xpos="far_left", ypos="head")
            gen "Think about how much you've endured at that ministry." ("angry", xpos="far_left", ypos="head")
            ton "..." ("upset", "closed", "annoyed", "ahegao")
            gen "Think of it as your reward! The students should be happy to have such a loving teacher as you." ("grin", xpos="far_left", ypos="head")
            ton "Thank you... sir." ("soft", "closed", "base", "mid")

        "-Call her out on her bullshit-":
            gen "I think there's someone who hasn't been very honest here..." ("base", xpos="far_left", ypos="head")
            ton "Sorry?" ("upset", "base", "worried", "mid")

            #Music changes and darker overlay on screen
            play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
            show screen blktone
            with d3

            gen "You seem to think you're above what we're doing here." ("base", xpos="far_left", ypos="head")
            gen "That you're doing the students a favour rather than accepting it's for your benefit." ("base", xpos="far_left", ypos="head")
            gen "Do you know what I think?" ("base", xpos="far_left", ypos="head")
            ton "N-no..." ("upset", "wide", "worried", "R")
            gen "I think that you've been fabricating this curse, to get what you really wanted - all along." ("base", xpos="far_left", ypos="head")
            gen "Not for the good of Miss Greengrass..." ("base", xpos="far_left", ypos="head")
            ton @ hair upset "..." ("mad", "base", "worried", "R")
            gen "Someone's been a naughty girl... Acting all innocent with the ones that welcomed her into their scheme..." ("angry", xpos="far_left", ypos="head")
            gen "Or perhaps you've been trying to justify your actions... to yourself?" ("base", xpos="far_left", ypos="head")
            gen "Is that right?" ("base", xpos="far_left", ypos="head")
            ton @ hair scared "That's..." ("upset", "closed", "worried", "mid")
            gen "I think we both know what this means, don't we?" ("base", xpos="far_left", ypos="head")
            gen "Miss Tonks..." ("base", xpos="far_left", ypos="head")
            gen "What this means is that you're no different than Snape and I." ("base", xpos="far_left", ypos="head")
            gen "But you have yet to accept it..." ("base", xpos="far_left", ypos="head")
            gen "And if you're unable to... Well, in that case..." ("base", xpos="far_left", ypos="head")
            ton "I can! I have!" ("open_wide", "closed", "worried", "mid")
            gen "Are you sure? Because if you're not in on this one hundred percent. Perhaps this may have been a mistake." ("base", xpos="far_left", ypos="head")
            ton "I..." ("open", "base", "worried", "down")
            gen "Say it!" ("angry", xpos="far_left", ypos="head")

            $ menu_y = 0.7
            menu:
                "\"You're a selfish slut!\"":
                    ton @ hair horny "Yes!" ("mad", "wide", "shocked", "stare")
                    ton @ hair horny "I'm a selfish slut!" ("open_wide_tongue", "closed", "worried", "mid")
                "\"You're a filthy pervert!\"":
                    ton @ hair horny "Yes!" ("mad", "base", "worried", "mid")
                    ton @ hair horny "I'm a filthy,{w=0.6} {b}fucking{/b}{w=0.4} pervert!" ("open_wide_tongue", "closed", "worried", "mid")
                "\"You're nothing more than a whore!\"":
                    ton @ hair horny "Yes!" ("mad", "base", "worried", "mid")
                    ton @ hair horny "I'm nothing but a cheap,{w=0.6} {b}fucking{/b}{w=0.4} whore!" ("open_wide_tongue", "closed", "worried", "mid")
            call reset_menu_position

            ton "... {w}This is what I want!" ("mad", "wide", "annoyed", "down")
            gen "Good, you're doing this for yourself, and nobody else..." ("base", xpos="far_left", ypos="head")
            gen "You'd do good to remember that." ("base", xpos="far_left", ypos="head")
            ton @ cheeks blush "Yes, Sir." ("base", "happyCl", "shocked", "mid")

            #Overlay goes away and music returns to normal
            play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
            hide screen blktone
            with d3

    ton "So... *Ehm*... How long did you know?" ("open", "narrow", "annoyed", "R")
    gen "From the very start." ("base", xpos="far_left", ypos="head")
    ton "Really?!" ("clench", "base", "base", "mid")
    gen "Yes... The way she was looking at you just now merely confirmed it..." ("base", xpos="far_left", ypos="head")
    ton "Was it that obvious..." ("annoyed", "narrow", "base", "down")
    gen "Now, with that out of the way..." ("base", xpos="far_left", ypos="head")
    gen "Are you ready to take this to the next step?" ("base", xpos="far_left", ypos="head")
    gen "Have you considered letting miss Greengrass cast the curse on a more susceptible target?" ("base", xpos="far_left", ypos="head")
    ton "..." ("annoyed", "wide", "base", "R")
    gen "Miss Tonks..." ("base", xpos="far_left", ypos="head")
    ton "Fine, let's do it!" ("mad", "closed", "annoyed", "down")
    gen "Good." ("grin", xpos="far_left", ypos="head")
    gen "Do you have a student in mind... Someone with similar... Inhibitions, perhaps?" ("base", xpos="far_left", ypos="head")
    gen "That Susan girl... How about her?" ("grin", xpos="far_left", ypos="head")

    ton "Susan Bones?" ("open", "wide", "shocked", "stare")
    ton @ hair sad "But, she's a Hufflepuff...{w=0.8} I used to be..." ("open", "base", "worried", "up") # Tonks looks concerned (Blue)
    gen "I don't see how that makes any difference..." ("base", xpos="far_left", ypos="head")
    gen "Remember why we're doing this, you want Miss Greengrass to be able to curse you properly, correct?" ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "Yes..." ("soft", "base", "worried", "downR")
    gen "This Susan girl sounds like the perfect target then." ("base", xpos="far_left", ypos="head")
    gen "Maybe we could even hit two birds with one stone." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "*Huh*?" ("soft", "base", "worried", "mid")
    gen "Perhaps I could learn a thing or two about this Susan girl is what I meant..." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "Right." ("open", "base", "worried", "mid")
    gen "Any objections?" ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush hair neutral "No sir..." ("open", "base", "base", "down")
    gen "But for now... Just make sure to obliterate her afterwards." ("base", xpos="far_left", ypos="head")
    ton "Erase her memory?" ("open", "base", "base", "mid")
    gen "That's what I said." ("base", xpos="far_left", ypos="head")
    gen "Well then, I believe we're done here..." ("base", xpos="far_left", ypos="head")
    ton "Alright..." ("annoyed", "base", "base", "down")
    ton @ hair horny "I'm going to require some \"me\" time now..." ("open", "closed", "base", "ahegao")
    ton @ hair horny "If you know what I mean..." ("grin", "narrow", "raised", "down")
    ton "I suppose I should wish you good luck with the training..." ("soft", "base", "shocked", "L")
    gen "Have a good night." ("grin", xpos="far_left", ypos="head")
    ton "Oh - I will, [name_genie_tonks]!" ("base", "base", "raised", "R")
    ton "I sure will!" ("horny", "base", "raised", "downR")

    call ton_walk(action="leave")

    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(Snape...)" ("base", xpos="far_left", ypos="head")
    gen "(That guy deprived me of a blowjob...)" ("base", xpos="far_left", ypos="head")
    gen "(He owes me one!)" ("angry", xpos="far_left", ypos="head")

    nar "Astoria has \"mastered\" the imperio curse!"

    $ states.sna.busy = True
    $ states.ton.busy = True
    $ states.ast.busy = True

    $ tonks.wear("all") # Wear all stripped clothing

    jump end_ag_st_imperio

# astoria wand drop animation screen
screen astoria_wand_drop():
    tag wand
    zorder 2

    add "characters/astoria/chibis/wand.webp":
        at transform:
            zoom 0.35
            rotate -25
            xanchor 0
            yoffset -60
            xpos 530-90
            ypos 400

            easeout_cubic 0.5 yoffset 0 rotate 0
            linear 0.15 rotate 5 yoffset -5
            linear 0.15 rotate 10 yoffset 10
            linear 0.15 rotate 15 yoffset 5
            linear 0.15 rotate 25 yoffset 15
