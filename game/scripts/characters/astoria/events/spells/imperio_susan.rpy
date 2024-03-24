

### Susan Imperio Events ###

label ag_se_imperio_sb:

    if not _events_completed_any:
        menu:
            gen "{size=-4}(Should I ask her to cast Imperio on Miss Bones?){/size}" ("base", xpos="far_left", ypos="head")

            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump astoria_favor_menu

    if states.sus.busy:
        gen "(Something tells me Susan is not available right now, perhaps I should try later...)" ("base", xpos="far_left", ypos="head")
        $ _event.cancel()
        jump astoria_favor_menu

    # Setup
    $ sus_outfit_last.save() # Store current outfit.
    $ ast_outfit_last.save() # Store current outfit.

    $ susan.equip(sus_outfit_default)
    $ astoria.equip(ast_outfit_default)

    $ astoria_chibi.zorder = 4 # In front of Susan.

    call ast_chibi("stand",530,"base") #Align with spell casting chibi

    return

label end_ag_se_imperio_sb:

    # Reset
    $ astoria_chibi.zorder = 3 # Default

    $ susan.equip(sus_outfit_last) # Equip player outfit.
    $ astoria.equip(ast_outfit_last) # Equip player outfit.

    $ states.ast.busy = True
    $ states.sus.busy = True

    # Increase level
    if not _events_filtered_completed_all:
        $ states.ast.level += 1

    $ states.ast.ev.imperio_with_susan.completed_once = True

    jump end_astoria_event

label ag_se_imperio_sb_E1:

    call ag_se_imperio_sb

    gen "I think it's time for you to try that spell on another person." ("base", xpos="far_left", ypos="head")
    ast "Another person?" ("open", "narrow", "base", "mid", xpos="base", ypos="base", trans=dissolve)
    ast "But I thought professor Tonks--" ("annoyed", "narrow", "worried", "mid")
    gen "I've already spoken to your teacher, and we both think it'd be best if I took over the lessons for now." ("base", xpos="far_left", ypos="head")
    ast "Really?" ("open", "narrow", "worried", "mid")
    gen "*Err*...{w=0.4} Yes." ("base", xpos="far_left", ypos="head")
    ast "*Hmm*... Well, you're the headmaster so whatever you say..." ("base", "narrow", "base", "mid")
    gen "Good!" ("grin", xpos="far_left", ypos="head")
    gen "Then Let's have you try it on that Susan girl again..." ("base", xpos="far_left", ypos="head")
    ast "You want me to... What?!" ("open", "base", "base", "mid")
    ast "But I thought--" ("angry", "narrow", "worried", "mid")
    gen "Don't tell me you wouldn't have given in to the temptation anyway." ("base", xpos="far_left", ypos="head")
    ast "...{w} I mean..." ("annoyed", "narrow", "base", "down")
    gen "You got lucky last time, if you were to be caught again, then I don't think even I would be able to save you..." ("base", xpos="far_left", ypos="head")
    gen "This way, you'll get that anger of yours out of your system, and we can both move on with our lives." ("base", xpos="far_left", ypos="head")
    ast "No, thanks!" ("base", "closed", "angry", "mid")
    gen "What? How could you say no to this?" ("angry", xpos="far_left", ypos="head")
    ast "If I can't use it to embarrass her in front of the other students, then what's the point?" ("angry", "narrow", "base", "mid")
    gen "You don't think she'd be more embarrassed if you got her to do something in front of her headmaster?" ("base", xpos="far_left", ypos="head")
    ast "I suppose..." ("annoyed", "narrow", "worried", "R")
    ast "But don't you think she'll figure out that you're in on it? Surely, she'd just report--" ("angry", "narrow", "worried", "mid")
    gen "We'll just wipe her memory." ("base", xpos="far_left", ypos="head")
    gen "That should let you cast it on her as many times as you like..." ("base", xpos="far_left", ypos="head")
    ast "You can do that?" ("open", "narrow", "base", "mid")
    gen "Apparent--{w=0.4} Yes!" ("base", xpos="far_left", ypos="head")
    gen "They haven't taught you that one?" ("base", xpos="far_left", ypos="head")
    ast "You're the one in charge here...{w=0.4} It's the first time I've heard of it." ("annoyed", "narrow", "base", "mid")
    gen "(Maybe there's a good reason for it...)" ("base", xpos="far_left", ypos="head")
    ast "..." ("annoyed", "narrow", "base", "down")
    gen "So, what do you say?" ("grin", xpos="far_left", ypos="head")
    ast "..." ("annoyed", "closed", "base", "mid")
    ast "...{fast} Heck yes!" ("smile", "narrow", "base", "mid")
    gen "Great! Then let me just bring her up here..." ("grin", xpos="far_left", ypos="head")

    stop music fadeout 1
    hide astoria_main
    with d3
    pause .8

    nar "You summon Susan to your office."

    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"
    sus "*Uhm*... Professor Dumbledore, you wanted to see me?"
    gen "Yes Miss Bones, and that would require you to come in here..." ("base", xpos="far_left", ypos="head")
    sus "Oh... Right..."

    call sus_walk(action="enter")

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "Hey [name_susan_astoria]!" ("grin", "narrow", "base", "L", xpos="right", ypos="base")
    sus "Astoria? What are you doing here?" ("angry", "wide", "shocked", "left", xpos="base", ypos="base")
    ast "Oh, don't mind me..." ("base", "base", "base", "R")

    gen "Come up here for a moment, Miss Bones..." ("base", xpos="far_left", ypos="head")
    sus "Oh... Okay sir." ("soft", "base", "base", "mid")

    call sus_walk("desk")
    pause.2

    gen "Alright, so the reason--" ("base", xpos="far_left", ypos="head")

    call ast_chibi("wand",530,"base")
    ast "Is so that I could put a curse on you!" ("grin", "narrow", "angry", "mid", xpos="base", ypos="base")
    sus "P-Put a curse on me?!!" ("open", "wide", "shocked", "stare", xpos="right", ypos="base")

    call ast_chibi("wand_casting",530,"base")
    sus "No! Professor, do someth--" ("angry", "base", "base", "mid")

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide susan_main
    ast "IMPERIO!" ("scream", "base", "angry", "mid")

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
    sus "W-what{w=0.3} are{w=0.3} y{w=0.1}o{w=0.1}u--" ("soft", "base", "base", "stare")
    nar "Susan's eyes flicker and a blank expression spreads across her face."
    sus "..." ("soft", "narrow", "base", "stare")

    call ast_chibi("wand",530,"base")

    ast "Finally..." ("grin", "base", "angry", "mid")
    ast "So, what should we do now?" ("open", "base", "base", "R")
    ast "We could do whatever we want [name_genie_astoria]!" ("open", "base", "base", "R")
    gen "How about we have her take her clothes off?" ("base", xpos="far_left", ypos="head")
    ast "All of them?!" ("clench", "base", "worried", "mid")
    gen "What? Didn't that work last time?" ("base", xpos="far_left", ypos="head")
    gen "Let's find out if she really is a secret exhibitionist!" ("grin", xpos="far_left", ypos="head")
    ast "I only made her take her top off." ("open", "base", "base", "mid")
    gen "Then there you go!" ("grin", xpos="far_left", ypos="head")
    ast "Okay then..." ("smile", "base", "base", "L")
    ast "Susan, are you listening?" ("open", "closed", "base", "mid")
    sus "Yes..." ("normal", "narrow", "base", "stare")
    ast "Good, I want you to pay attention..." ("open", "base", "base", "L")
    sus "..." ("soft", "narrow", "base", "stare")
    ast "I want you to...{w} to..." ("open", "base", "base", "L")
    gen "Tell her to take off her top!" ("base", xpos="far_left", ypos="head")
    ast "Very well, [name_genie_astoria]..." ("clench", "base", "base", "L")
    ast "Susan, I want you to take off your...{w} your...{w} Take your top off!" ("clench", "base", "base", "L")
    sus @ cheeks blush "..." ("soft", "wide", "shocked", "stare")

    sus @ cheeks blush "..." ("soft", "narrow", "low", "stare")

    play sound "sounds/gulp.ogg"
    gen "*Gulp!*" ("angry", xpos="far_left", ypos="head")

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.strip("top")
    sus "" ("angry", "narrow", "base", "stare")
    pause.5

    gen "Oh no, Miss Bones!" ("base", xpos="far_left", ypos="head")
    gen "What are you doing?!" ("grin", xpos="far_left", ypos="head")
    hide screen bld1
    with d3
    pause.8

    call gen_chibi("jerk_off_behind_desk")
    pause.5

    sus @ cheeks blush "..." ("angry", "wide", "sad", "stare")
    ast "Speak, [name_susan_astoria]!" ("annoyed", "narrow", "base", "mid")
    sus @ cheeks blush "I-I-I'm sorry, Professor Dumbledore, I don't know what's come over me..." ("open", "wide", "sad", "stare")
    sus @ cheeks blush "I'm Sorry you have to see this..." ("angry", "narrow", "sad", "stare")
    ast "See what Suzy?" ("grin", "narrow", "angry", "mid")
    sus @ cheeks blush "My gross boobs..." ("open", "happy", "worried", "stare")
    ast "(I knew they were gross!)" ("grin", "base", "angry", "L")
    sus @ cheeks blush "Please Sir--" ("open", "narrow", "worried", "stare")
    sus @ cheeks blush "Don't think less of me..." ("soft", "narrow", "worried", "stare")
    ast "Now take them out!" ("angry", "narrow", "base", "L")
    sus @ cheeks blush "" ("soft", "narrow", "base", "stare")
    pause .8

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.strip("bra")
    sus @ cheeks blush "" ("soft", "narrow", "low", "stare")

    gen "{size=+10}Nice!{/size}" ("angry", xpos="far_left", ypos="head")
    ast "Sir!" ("base", "narrow", "angry", "mid")
    gen "What? You can't blame me for this!" ("base", xpos="far_left", ypos="head")
    ast "We're doing this, so I can cast the spell more successfully." ("clench", "narrow", "angry", "mid")
    gen "Don't you think her breasts are pretty?" ("base", xpos="far_left", ypos="head")
    ast "{b}No!{/b} they're huge and soft and squishy and, and, and... gross!" ("clench", "closed", "angry", "mid")
    gen "Well, you've got two out of three..." ("grin", xpos="far_left", ypos="head")
    gen "You're right about them being huge and soft." ("grin", xpos="far_left", ypos="head")
    ast "Sir!" ("clench", "narrow", "angry", "mid")
    sus @ cheeks blush "Did I do something wrong?" ("angry", "happy", "worried", "stare")
    ast "Your ugly tits are all wrong, they belong on a cow!" ("scream", "base", "angry", "L")
    sus @ cheeks blush "Cow!? W-why are you always being so mean to me?" ("angry", "wide", "sad", "stare")
    ast "*Pfft*... you know..." ("annoyed", "narrow", "angry", "R")
    sus @ cheeks blush "A-{w=0.3}Are you just going to let her say that, s-sir?" ("soft", "happy", "worried", "stare")
    ast "Shut up cow!" ("angry", "narrow", "angry", "R")
    sus @ cheeks blush "" ("upset", "happy", "sad", "stare")
    pause .8

    nar "You keep stroking your rock-hard cock whilst marvelling at Susan's heaving chest."
    gen "(So big...{w=0.4} Soft...{w=0.4} And squishy...)" ("angry", xpos="far_left", ypos="head")
    sus @ cheeks blush "..." ("upset", "happy", "sad", "stare")
    ast "Alright, I think you're enjoying this a little too much!" ("clench", "base", "angry", "mid")
    gen "Just give me a minute..." ("base", xpos="far_left", ypos="head")
    pause.2

    stop music fadeout 1
    call hide_characters
    call ast_chibi("reset",530,"base")
    hide screen bld1
    with fade
    pause.8

    ast "" ("annoyed", "base", "angry", "R")
    sus "W--{w=0.2} what..." ("angry", "narrow", "base", "stare")

    nar "Susan's eyes flicker once more as the spell lessens its hold."

    call gen_chibi("sit_behind_desk")
    with d3
    pause.1

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    gen "(Damn it! Why did she do that?)" ("angry", xpos="far_left", ypos="head")
    sus "..." ("soft", "narrow", "base", "stare")
    ast "Put your clothes on, Suzy." ("smile", "base", "base", "mid")
    sus "..." ("normal", "narrow", "base", "stare")

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.wear("bra", "top")
    sus "" ("soft", "narrow", "base", "stare")
    pause.5


    hide susan_main
    sus "" ("soft", "narrow", "base", "stare")
    pause.5
    nar "Susan dresses herself... Her eyes still looking quite unfocused and seemingly struggling to properly take in her surroundings."

    gen "*Aww*...{w=0.4} Why would you do that?" ("base", xpos="far_left", ypos="head")
    ast "You were getting too excited, old man." ("clench", "base", "angry", "mid")
    gen "So what?" ("base", xpos="far_left", ypos="head")
    ast "How am I going to get any better if you keep distracting me?" ("annoyed", "narrow", "angry", "R")
    gen "Couldn't you have made her dance, or something at least..." ("base", xpos="far_left", ypos="head")
    ast "I could have..." ("annoyed", "base", "base", "L")
    gen "Then why don't we?" ("base", xpos="far_left", ypos="head")
    ast "Because it's boring!" ("annoyed", "narrow", "base", "ahegao")
    ast "I want to do something fun!" ("open", "closed", "base", "mid")
    gen "*Ugh*... fine..." ("base", xpos="far_left", ypos="head")
    ast "But not today..." ("annoyed", "base", "base", "mid")
    ast "I should put Bessy here back in her barn before people start to notice." ("grin", "base", "angry", "L")
    sus "(*Hmm*...)" ("soft", "narrow", "base", "stare")
    gen "Alright..." ("base", xpos="far_left", ypos="head")
    ast "Just call me for the next practice session!" ("smile", "narrow", "base", "mid")
    gen "Will do." ("base", xpos="far_left", ypos="head")
    gen "Oh, please escort Miss Bones to professor Tonks to be obliterated..." ("base", xpos="far_left", ypos="head")
    ast "Obliviated?" ("base", "base", "worried", "mid")
    gen "Yeah, that!" ("base", xpos="far_left", ypos="head")
    ast "Can't you do it?" ("annoyed", "base", "base", "mid")
    nar "Susan's eyes shift and become a bit more focused as she begins to recognize where she is..."
    sus "Wait, where...{w=0.4} am..." ("soft", "narrow", "base", "downL")
    gen "My wand casting hand is a bit tired for some reason..." ("base", xpos="far_left", ypos="head")
    ast "Fine..." ("annoyed", "base", "worried", "R")
    gen "And hurry up will you?" ("base", xpos="far_left", ypos="head")
    ast "Yeah, yeah..." ("annoyed", "narrow", "base", "mid")

    call ast_walk("door","base")
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    ast "Come on Suzy, time to give professor Tonks a visit." ("open", "base", "base", "mid")
    sus "Professor...{w=0.4} Tonks?" ("soft", "narrow", "shocked", "downL")

    call sus_walk(680, "base")
    call sus_chibi("leave")


    call hide_characters
    call ast_chibi("stand","door","base", flip=True)
    pause .3
    call ast_chibi("leave")
    hide screen bld1
    with d3
    pause.5

    call bld
    gen "(*Hmm*... Looks like Miss Bones had more of a lingering effect than Tonks...)" ("base", xpos="far_left", ypos="head")
    gen "(Maybe leaving Tonks out of this was a bad idea...)" ("base", xpos="far_left", ypos="head")
    gen "(Nah...{w=0.3} She's had her fun...)" ("base", xpos="far_left", ypos="head")

    jump end_ag_se_imperio_sb

label ag_se_imperio_sb_E2:

    call ag_se_imperio_sb

    ast "Let's try something else this time!" ("grin", "narrow", "base", "mid", xpos="close", ypos="base", trans=fade)
    gen "Of course!" ("grin", xpos="far_left", ypos="head")
    ast "Great, I can't wait to see the look on Susan's dumb face..." ("grin", "closed", "base", "mid")
    gen "Let me just bring her up here." ("base", xpos="far_left", ypos="head")

    stop music fadeout 1
    gen "..." ("base", xpos="far_left", ypos="head")
    ast "..." ("annoyed", "base", "base", "R")

    call hide_characters
    hide screen bld1
    with d3
    call sus_walk(action="enter")
    pause.2

    sus "You wanted to see me, sir?" ("soft", "base", "base", "mid", xpos="base", ypos="base")
    sus "Astoria? Why are you here?" ("angry", "wide", "base", "left")

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "Oh... no reason..." ("annoyed", "base", "base", "down", xpos="right", ypos="base")
    gen "Come up here for a moment Miss Bones..." ("base", xpos="far_left", ypos="head")
    sus "Okay..." ("open", "base", "base", "mid")

    call hide_characters
    with d3

    call sus_walk("desk")
    pause.2

    sus "Is there something wrong, Professor?" ("open", "happy", "base", "left", xpos="right", ypos="base")
    gen "As a matter of fact there is..." ("base", xpos="far_left", ypos="head")
    sus "R-really? Is this about me returning my books to the library a day late?" ("angry", "happy", "base", "mid")
    sus "I swear it won't happen again!" ("angry", "happy", "worried", "mid")
    gen "What? No, I'm afraid there's an issue with your uniform..." ("base", xpos="far_left", ypos="head")
    sus "Oh... Is it because I'm not wearing the school robe?" ("soft", "happy", "base", "mid")
    sus "I can wear it from now on if you like!" ("soft", "wide", "sad", "mid")
    gen "Actually, Wearing too many clothes is the problem." ("base", xpos="far_left", ypos="head")
    sus "W-w-what???" ("angry", "wide", "base", "mid")
    sus "You can't be serious, sir!" ("clench", "wide", "base", "mid")
    gen "I am, Miss Bones..." ("base", xpos="far_left", ypos="head")
    gen "Hiding away those glorious milk duds of yours is a serious offence!" ("grin", xpos="far_left", ypos="head")
    ast "(*Pffft*, gloriously gross...)" ("annoyed", "base", "angry", "R", xpos="base", ypos="base")
    sus @ cheeks blush "P-professor Dumbledore! Why would you say s-something like that!" ("angry", "wide", "sad", "stare", trans=hpunch) #Perhaps she should be a bit intrigued =Blush

    call ast_chibi("wand",530,"base")
    sus @ cheeks blush "I think I better go..." ("disgust", "base", "sad", "right")
    call ast_chibi("wand_casting",530,"base")
    ast "" ("grin", "base", "angry", "L")
    pause.5

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide susan_main
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
    sus "..." ("soft", "happy", "shocked", "stare")
    ast "*ha-ha-ha-ha!*" ("grin", "closed", "base", "mid")
    ast "Her face was priceless when you said milk duds..." ("grin", "base", "base", "L")
    gen "You liked that?" ("base", xpos="far_left", ypos="head")
    ast "Of course! Anything to bring Bessy here down a peg." ("smile", "base", "base", "L")

    call ast_chibi("wand",530,"base")
    ast "So what should we make her do today, [name_genie_astoria]?" ("smile", "base", "base", "mid")
    gen "Something fun, perhaps?" ("base", xpos="far_left", ypos="head")
    ast "*Hmm*..." ("annoyed", "narrow", "base", "R")
    gen "Maybe something a little more... adventurous?" ("base", xpos="far_left", ypos="head")
    ast "You mean like making her show you her milk duds?" ("upset", "narrow", "base", "mid")
    gen "Well, if you insist..." ("base", xpos="far_left", ypos="head")
    ast "*Ugh*... You're such a filthy pervert!" ("clench", "narrow", "angry", "mid")
    gen "We can do something else if you--" ("base", xpos="far_left", ypos="head")
    ast "I didn't say no..." ("upset", "closed", "base", "mid")
    gen "Oh... Then how about you make it so--" ("base", xpos="far_left", ypos="head")
    ast "I get to choose, [name_genie_astoria]!" ("scream", "closed", "angry", "mid")
    gen "What? Why?" ("base", xpos="far_left", ypos="head")
    ast "Because it's my spell and my wand!" ("open", "narrow", "angry", "mid")
    ast "Not to mention, you'd probably do something over the top and gross..." ("open", "narrow", "angry", "R")
    gen "Probably..." ("base", xpos="far_left", ypos="head")
    gen "So, what's your plan?" ("base", xpos="far_left", ypos="head")
    ast "Just wait and see, old man!" ("clench", "narrow", "angry", "mid")
    ast "Susan, can you hear me?" ("open", "closed", "base", "L")
    sus "Yes..." ("open", "happy", "base", "stare")
    ast "You now have an uncontrollable urge to take your top off, okay?" ("open", "closed", "base", "mid")
    sus "Okay..." ("soft", "happy", "base", "stare")
    ast "Awesome! Now act like you normally would, [name_susan_astoria]!" ("grin", "base", "angry", "L")
    sus "..." ("normal", "base", "base", "stare")

    nar "The blank expression slowly fades from Susan's eyes..."
    sus "*Ugh*..." ("angry", "narrow", "low", "down")
    sus "What happened?" ("angry", "narrow", "base", "mid")
    ast "Nothing, Suzy... Dumbledore was just explaining how your uniform wasn't up to scratch." ("grin", "base", "base", "mid")
    sus "My uniform... You're right... Too many clothes..." ("disgust", "happy", "sad", "downL")
    sus "I need to take off my top..." ("soft", "narrow", "low", "down")
    ast "*Mhmm*, that's right, Suzy... Why don't you show the old man here your gross boobs... Don't you think he's old?" ("grin", "base", "angry", "mid")
    sus "I... I suppose..." ("open", "happy", "low", "downL")
    ast "That's right... Only a nasty slut would show her boobs to such a wrinkly old man..." ("grin", "narrow", "angry", "L")
    gen "Hey!" ("base", xpos="far_left", ypos="head")
    ast "Quiet sir... don't ruin my fun!" ("clench", "narrow", "angry", "mid")
    gen "Fine..." ("base", xpos="far_left", ypos="head")
    sus "I-I'm not a slut..." ("angry", "happyCl", "base", "down")
    ast "Well, I'm sure you'll be able to keep your top on then, [name_susan_astoria]." ("open", "closed", "base", "mid")
    sus @ cheeks blush "I... There's something wrong, sir!" ("angry", "happyCl", "low", "mid")
    sus @ cheeks blush "I can't help it..." ("angry", "happy", "worried", "down")
    ast "" ("grin", "base", "angry", "L")
    pause.2

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.strip("top", "bra")
    sus @ cheeks blush "" ("angry", "wide", "shocked", "down")
    call ctc

    gen "Nice!" ("angry", xpos="far_left", ypos="head")
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("jerk_off_behind_desk")
    pause.8

    ast "[name_genie_astoria]! Are you touching yourself?" ("scream", "base", "base", "mid")
    gen "*Ugh*... can you blame me?" ("base", xpos="far_left", ypos="head")
    gen "It's not every day you get to see a rack like this..." ("angry", xpos="far_left", ypos="head")
    ast "Well, stop it! It's gross!" ("clench", "narrow", "angry", "mid")
    gen "Alri--" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "Please sir... it's too much!" ("angry", "happy", "worried", "downR")
    sus @ cheeks blush "It's bad enough that I can't help showing you my breasts..." ("disgust", "happyCl", "worried", "mid")
    ast "Wait..." ("smile", "base", "base", "mid")
    ast "Keep going, sir!" ("clench", "narrow", "angry", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "What?" ("angry", "wide", "sad", "right")
    ast "Well if Bessy here hates it... Then I love it!" ("clench", "narrow", "angry", "L")
    ast "Besides, it's not like I can see through the desk." ("open", "closed", "base", "mid")
    sus @ cheeks blush "(...)" ("annoyed", "happy", "sad", "right")
    gen "So you're okay with this?" ("base", xpos="far_left", ypos="head")
    ast "*Mhmm*... Just don't expect me to touch it, old man!" ("upset", "narrow", "angry", "mid")
    sus @ cheeks blush "W-why is this happening!" ("angry", "closed", "worried", "mid")
    ast "No one asked you, slut!" ("clench", "narrow", "angry", "L")
    sus @ cheeks blush "I am not a slut!" ("angry", "happy", "low", "stare")
    ast "Ha! You're standing here, letting old man dumbledore ogle your fat tits while he jerks his wrinkly old cock!" ("open", "closed", "base", "mid")
    ast "If that's not a slut, then I don't know what is!" ("clench", "narrow", "angry", "L")
    gen "(There's no way Tonks would allow this, perhaps this was a good idea after all...)" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "I-- don't know why I'm doing this..." ("angry", "narrow", "base", "down")
    sus @ cheeks blush "You probably cursed me!" ("angry", "base", "sad", "downR")
    ast "Duh!" ("grin", "narrow", "angry", "L")
    sus @ cheeks blush "Well stop it!" ("angry", "narrow", "base", "right")
    ast "*Nuh-uh*!" ("open", "closed", "base", "mid")
    sus @ cheeks blush "Please Astoria..." ("angry", "narrow", "shocked", "right")

    nar "You start to zone out as the two girls argue, focusing on Susan's heaving bosom."
    gen "Yeah... that's it..." ("angry", xpos="far_left", ypos="head")
    ast "You can leave once Dumbledore here's done." ("open", "closed", "base", "mid")
    sus @ cheeks blush "What? you mean I have to wait until he..." ("angry", "wide", "worried", "mid")
    sus @ cheeks blush "This is unbelievable!" ("angry", "wide", "sad", "mid")
    sus @ cheeks blush "I'm going to report both of you to the ministry of magic!" ("upset", "happyCl", "annoyed", "mid")
    sus @ cheeks blush "My aunt is the head of the department of magical law enforcement, I'll have you know!" ("angry", "narrow", "annoyed", "mid")
    ast "yeah... I've met your creepy old aunt." ("annoyed", "narrow", "base", "L")
    sus @ cheeks blush "What? Did you curse her too, you evil little witch?" ("open", "base", "angry", "right")
    ast "I wish..." ("base", "narrow", "base", "R")
    sus @ cheeks blush "Well, she's going to lock both of you away in Azkaban!" ("annoyed", "closed", "angry", "mid")
    sus @ cheeks blush "You'll never see me or anyone else again..." ("base", "closed", "annoyed", "mid")
    ast "Yeah, sure!" ("grin", "base", "angry", "L")
    sus @ cheeks blush "*Ugh*! You're both sick!" ("disgust", "narrow", "annoyed", "stare")
    ast "Says the slut baring her chest for the headmaster." ("smile", "base", "base", "L")
    gen "*Mmmm*... Keep shaking those tits of yours..." ("angry", xpos="far_left", ypos="head")
    sus @ cheeks blush "I am not a {size=+10}slut!{/size}" ("angry", "base", "angry", "stare")
    nar "As Susan yells at the top of her voice, the effort causes her gigantic tits to rise and slap back together."

    gen "{size=+10}HERE IT COMES!{/size}" ("angry", xpos="far_left", ypos="head")
    sus @ cheeks blush "" ("clench", "wide", "shocked", "stare")
    hide screen bld1
    with d3
    pause.1
    call gen_chibi("cum_behind_desk")
    call cum_block
    gen "{size=+10}AHHH... YESS!!!!{/size}" ("angry", xpos="far_left", ypos="head")
    call gen_chibi("cum_behind_desk_done")
    pause.5
    ast "Woah... I didn't think you'd have that much in you, sir..." ("clench", "base", "base", "mid")

    sus @ cheeks blush "{size=+10}*Hmph*! I hope you Enjoy Azkaban, perverts!{/size}" ("angry", "base", "angry", "mid")

    ast "" ("annoyed", "narrow", "base", "R")

    nar "As you finish shooting your massive load, Susan's leg twitches slightly..."

    ast "Can't have that, can we... Let's delve deeper." ("grin", "narrow", "angry", "L")

    # chibi spell animation.
    play sound "sounds/magic2.ogg"
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    sus "" ("soft", "happy", "shocked", "stare")
    gen "W-what?" ("base", xpos="far_left", ypos="head")
    nar "You watch as a colourful mist spreads from the tip of Astoria's wand and seeps into Susan's nostrils..."
    ast "Suzy, you can still hear me, right?" ("open", "base", "base", "L")
    sus "Yes..." ("open", "happy", "base", "stare")

    call ast_chibi("wand",530,"base")
    ast "She's just so easy to put under the spell..." ("base", "narrow", "worried")
    ast "Nothing like Tonks, there's something wrong here..." (eyes="base", pupils="R")
    gen "W-what do you mean?" ("base", xpos="far_left", ypos="head")
    ast "Quiet!" ("clench", "base", "base", "mid")
    gen "..." ("angry", xpos="far_left", ypos="head")
    ast "Suzy, I want you to speak the truth and nothing but the truth, okay?" ("open", "base", "base", "L")
    sus "Okay..." ("soft", "narrow", "base", "stare")
    gen "What are you--" ("base", xpos="far_left", ypos="head")
    ast "..." ("upset", "base", "base", "mid") # Stares at you
    gen "..." ("angry", xpos="far_left", ypos="head")
    ast "Suzy, do you like baring your chest to the headmaster?" ("open", "base", "base", "L")
    ast "Just like all those other closeted sluts?" ("clench", "narrow")
    gen "(Oh shit...)" ("base", xpos="far_left", ypos="head")
    sus @ cheeks blush "I... I..." ("angry", "narrow", "base", "stare")
    ast "Tell me!" ("scream")
    ast "" ("clench")
    sus @ cheeks blush "I...{w=0.8} I do!" ("smile", "wink", "worried", "stare")
    ast "I knew it!" ("scream", "narrow", "angry") # Angry
    sus @ cheeks blush "" ("base", "narrow", "worried", "stare")
    ast "Where's the fun if she's enjoying it!" ("clench", pupils="mid")
    gen "*Errr-*" ("base", xpos="far_left", ypos="head")
    ast "I want to humiliate this cow, but she's just another slut!" ("scream")
    gen "A closeted slut..." ("base", xpos="far_left", ypos="head")
    ast "Excuse me?" (mouth="open", eyebrows="worried")
    ast "" (mouth="upset")
    gen "Miss Greengrass... Are there any other Hufflepuff students you know of selling favours?" ("base", xpos="far_left", ypos="head")
    ast "Why would I know or care what the Hufflepuffs are doing?" (mouth="clench")
    gen "Just because she enjoys it doesn't mean it's not humiliating for her..." ("base", xpos="far_left", ypos="head")
    gen "What would the other Hufflepuffs think of her if she knew what you have her do?" ("base", xpos="far_left", ypos="head")
    ast "What do you mean?" ("upset", "base", "base")
    gen "Ask her the right questions..." ("base", xpos="far_left", ypos="head")
    ast "..." (eyes="closed")
    ast "Suzy!" ("open", "narrow", "base", "L")
    ast "" ("base")
    sus @ cheeks blush "..." ("normal", "narrow", "raised", "stare")
    ast "Are you ashamed of what you've done?" ("open", "base")
    ast "" ("base")
    sus @ cheeks blush "...{w=0.4} Yes." ("soft", "narrow", "worried", "stare")
    ast "Would your house think less of you if they knew what you're doing here?" ("grin")
    sus @ cheeks blush "They would..." ("open", "narrow", "worried", "stare")
    gen "Well, there you go!" ("base", xpos="far_left", ypos="head")
    ast "*Ha-ha-ha*!" ("smile")
    gen "(Nailed it...)" ("base", xpos="far_left", ypos="head")
    gen "So, are we continuing with the training?" ("base", xpos="far_left", ypos="head")
    ast "Of course we are!" ("smile", "base", "base", "L")
    gen "Great!" ("base", xpos="far_left", ypos="head")


    ast "Suzy, put your clothes back on." ("grin", "base", "base", "L")

    sus "" ("normal", "narrow", "sad", "down")
    pause.5
    nar "Susan begins dressing herself in silence..."

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.wear("top", "bra")
    pause 1

    stop music fadeout 1
    call hide_characters
    call ast_chibi("reset",530,"base")
    pause .5
    call ast_walk("door","base")
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "Come on Suzy, time to give professor Tonks another visit." ("open", "base", "base", "L")
    sus "*Hmm*... Another visit..." ("soft", "narrow", "sad", "downL")

    call sus_walk(action="leave")

    if game.daytime:
        ast "See you, [name_genie_astoria]!" ("grin", "closed", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
    else:
        ast "Smell yah later, [name_genie_astoria]!" ("grin", "closed", "base", "mid")
        gen "Good night." ("base", xpos="far_left", ypos="head")

    play sound "sounds/door.ogg"
    call hide_characters
    call ast_chibi("hide")
    call gen_chibi("sit_behind_desk")
    hide screen bld1
    with d3
    pause.5

    jump end_ag_se_imperio_sb

label ag_se_imperio_sb_E3:

    call ag_se_imperio_sb

    ast "" ("smile", "base", "base", "mid",xpos="close",ypos="base",trans=fade)
    gen "Ready for another go with the curse?" ("base", xpos="far_left", ypos="head")
    ast "You bet [name_genie_astoria]! I can't wait to see the look on Suzy's stupid face!" ("grin", "narrow", "angry", "down")
    gen "Shall I bring her up here?" ("base", xpos="far_left", ypos="head")
    ast "Do you even need to ask?" ("smile", "narrow", "base", "mid")
    gen "I suppose not..." ("base", xpos="far_left", ypos="head")

    stop music fadeout 1

    call hide_characters
    with d3
    call sus_walk(action="enter")
    pause.2

    sus "You wanted to see me sir?" ("base", "base", "base", "mid", xpos="base", ypos="base")
    sus "Astoria?" ("angry", "wide", "shocked", "left")
    sus "What are you doing here?" ("open", "base", "sad", "left")

    gen "Come up here for a moment, Miss Bones..." ("base", xpos="far_left", ypos="head")
    sus "Okay..." ("soft", "happy", "low", "mid")

    call sus_walk("desk")
    pause.2

    gen "..." ("base", xpos="far_left", ypos="head")
    sus "*Ehm*... Can I help you with--" ("soft", "narrow", "base", "downL", xpos="right", ypos="base")

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    call ast_chibi("wand",530,"base")
    ast "Blah, blah, blah..." ("open", "base", "base", "R", xpos="base", ypos="base")

    call ast_chibi("wand_casting",530,"base")
    sus "I'm not in trouble for anything am--" ("angry", "happy", "base", "mid", xpos="right", ypos="base")

    # Astoria casts imperio.
    stop music fadeout 2.0
    hide susan_main
    ast "IMPERIO!{w=0.8}{nw}" ("scream", "base", "angry", "mid", trans=hpunch)

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
    sus "Wait, what--" ("soft", "base", "base", "stare")
    sus "" ("soft", "narrow", "base", "stare")
    gen "Couldn't even wait this time?" ("base", xpos="far_left", ypos="head")
    ast "Quiet old man." ("open", "narrow", "angry", "mid")
    call ast_chibi("wand",530,"base")
    ast "Susan, I want you to keep listening to my commands and act as if nothing out of the ordinary is happening." ("open", "narrow", "base", "L")
    ast "Is that clear?" ("smile", "narrow", "angry", "L")
    sus "Yes..." ("open", "narrow", "base", "stare")
    ast "Great!{w} Now take your top off!" ("grin", "base", "angry", "L")
    gen "!!!" ("angry", xpos="far_left", ypos="head")
    pause .8

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.strip("top")
    sus "" ("base", "base", "base", "mid")
    pause.5

    nar "Susan's arms, now seemingly with a mind of their own, removes her top as she resumes speaking where she left off."
    sus "Was this about the l-library books that I returned a day late s-sir?" ("open", "happy", "sad", "mid")
    sus "I promise it won't happen again..." ("soft", "closed", "sad", "mid")
    gen "Don't you worry about the books, Ms Bones!" ("grin", xpos="far_left", ypos="head")
    sus "I--{w=0.4} I'm a bit confused sir, for what reason have you--" ("soft", "base", "low", "mid")
    ast "Get those milk bags out Suzy!" ("clench", "narrow", "angry", "L")
    sus "Of course..." ("open", "base", "low", "mid")
    pause .8

    hide susan_main
    play sound "sounds/cloth_sound3.ogg"
    $ susan.strip("bra")
    sus "" ("base", "base", "base", "mid")
    pause.5

    gen "Miss Bones!" ("angry", xpos="far_left", ypos="head")
    sus "Sir?" ("soft", "base", "raised", "mid")
    sus "Have I done something wrong?" ("open", "base", "raised", "mid")
    ast "Maybe it's because of you, showing off your gross boobs?" ("grin", "base", "angry", "L")
    sus "Astoria! H-how can you say something so rude! I'd never..." ("soft", "happy", "annoyed", "right")
    ast "Oh yeah?{w} Susan, I want you to look down and take in what you've been doing this whole time." ("open", "base", "angry", "L")
    sus "" ("soft", "base", "base", "downL")
    pause.8

    nar "Susan's eyes drift down to her exposed chest."
    sus "WHAT?!?!?" ("angry", "wide", "shocked", "down", trans=hpunch)
    sus @ cheeks blush "I'm so sorry, professor Dumbledore!" ("open", "wide", "worried", "stare")
    sus @ cheeks blush "I don't know what's come over me!" ("angry", "happyCl", "sad", "mid")
    ast "Maybe it's just because you're a nasty slut!" ("annoyed", "base", "base", "L")
    sus @ cheeks blush "I am not a {size=+10}slut{/size}, Astoria!" ("angry", "happyCl", "annoyed", "mid")
    ast "*Pfft*... We both know that's not true... You love showing your headmaster those oversized bean bags of yours." ("annoyed", "base", "base", "R")
    sus @ cheeks blush "I-- don't know why this is happening..." ("open", "happyCl", "annoyed", "down")
    sus @ cheeks blush "You must have cursed me!" ("angry", "happy", "shocked", "stare")
    ast "Bingo!" ("grin", "base", "angry", "L")
    sus @ cheeks blush "Professor! You h-have to stop her!" ("open", "happy", "sad", "left")
    gen "*Ugh*...{w=0.3} I'm afraid I can't do that, Miss Bones..." ("base", xpos="far_left", ypos="head")
    ast "" ("grin", "narrow", "angry", "L")
    sus @ cheeks blush "WHAT?!" ("angry", "wide", "low", "mid")
    sus @ cheeks blush "W-w-w-well, my aunt will just send you--" ("angry", "happyCl", "annoyed", "mid")

    ast "Quiet!" ("scream", "base", "angry", "L")
    nar "Astoria strengthens her grip on her wand, and focuses on maintaining the spell, increasing its effect on Susan."

    sus "To...{w=0.5} Azkaban..." ("soft", "narrow", "annoyed", "stare")
    sus "..." ("soft", "narrow", "base", "stare")
    ast "Alright... that'll shut her up...{w} what should we make her do this time, [name_genie_astoria]?" ("open", "closed", "base", "mid")
    gen "*Hmm*... Are you actually going to let me choose this time, or are you just asking to be annoying?" ("base", xpos="far_left", ypos="head")
    ast "Hey! I am not annoying!" ("scream", "narrow", "angry", "mid", trans=vpunch)
    gen "So, are you going to let me pick then?" ("base", xpos="far_left", ypos="head")
    ast "Fine... Just nothing too disgusting!" ("clench", "narrow", "base", "mid")
    ast "Or boring... that'd be even worse!" ("upset", "narrow", "angry", "mid")

    gen "Alright... Well, first things first..." ("base", xpos="far_left", ypos="head") #I'll add a menu here with more options once art assets are drawn for them

    pause.1
    call gen_chibi("jerk_off_behind_desk")
    pause.8

    nar "Your hands sneak under your desk and around your engorged cock."
    gen "That's better..." ("grin", xpos="far_left", ypos="head")
    ast "(...)" ("annoyed", "narrow", "angry", "R")
    gen "What?" ("base", xpos="far_left", ypos="head")
    ast "I told you not to be boring! We already did this last time!" ("open", "closed", "base", "mid")
    gen "If this is too boring, why don't you get her to suck me off?" ("grin", xpos="far_left", ypos="head")
    ast "Sir! I said it shouldn't be something disgusting..." ("clench", "base", "base", "mid")
    ast "I don't wanna have to see your nasty old cock!" ("clench", "narrow", "angry", "R")
    gen "*Ugh*... Fine... What do you want to do then?" ("base", xpos="far_left", ypos="head")
    ast "Well seeing as how you asked..." ("open", "closed", "base", "mid")
    ast "Suzy, are you listening?" ("open", "narrow", "base", "L")

    sus "yes..." ("soft", "narrow", "base", "stare")
    ast "I want you to crawl under the headmaster's desk." ("grin", "base", "base", "L")
    gen "I thought you didn't want her to suck me off?" ("base", xpos="far_left", ypos="head")
    ast "Shut it, and stop being so disgusting!" ("scream", "closed", "angry", "mid")
    sus "..." ("base", "base", "base", "mid")
    ast "Now go, [name_susan_astoria]!" ("grin", "narrow", "angry", "mid")

    call hide_characters
    call sus_chibi("hide")
    show screen blkfade
    with d3

    nar "Susan slowly makes her way around your desk before obediently crawling under."
    pause.5
    hide screen blkfade
    with d3

    ast "" ("smile", "base", "base", "down",xpos="mid",ypos="base",trans=fade)
    hide screen bld1
    call ctc

    ast "And you're not allowed to come out until I say so." ("open", "closed", "base", "mid")
    sus "yes..."
    ast "And if you actually are just a slut, then I want you to let that slut out! Show us that you really love it!" ("clench", "narrow", "base", "down")
    sus "...{w=0.4} Love it?"
    sus "I love it..."
    ast "Good!" ("clench", "base", "angry", "L")
    gen "Isn't that a little much?" ("base", xpos="far_left", ypos="head")
    ast "*Pfft*! That's rich coming from you, sir!" ("annoyed", "narrow", "base", "mid")
    ast "If it was up to me, she'd be clucking like a chicken right now!" ("annoyed", "narrow", "angry", "R")
    ast "Not doing nasties with her mouth!" ("clench", "narrow", "base", "down")
    gen "Fair enough..." ("base", xpos="far_left", ypos="head")
    gen "Although it sounds to me as if you're enjoying this as--" ("base", xpos="far_left", ypos="head")
    ast "But you've helped me, so take this as a reward..." ("open", "closed", "base", "mid")
    ast "Now, make sure to give Susan a reward for being so obedient as well..." ("smile", "base", "angry", "mid")
    gen "You don't have to tell me twice!" ("base", xpos="far_left", ypos="head")
    nar "You renew your efforts, encouraged by the image of the well-endowed redhead hidden under your desk."
    ast "And Suzy..." ("open", "narrow", "base", "down")
    sus "Yes..."
    ast "Time for you to wake up..." ("grin", "narrow", "angry", "down")
    sus "..."

    play music "music/teddy-bear-waltz-by-kevin-macleod.ogg" fadein 1 if_changed
    hide screen blktone
    hide screen bld1
    with d3
    pause.5
    show screen bld1
    with hpunch
    sus "W-w-what's happening?"
    play sound "sounds/kick.ogg"
    with vpunch
    pause.2
    sus "Ouch..."
    pause.5
    sus "Where am I?"
    ast "Don't you remember crawling under your headmaster's desk, begging him to jerk his nasty old cock for you?" ("open", "closed", "base", "mid")
    with hpunch
    sus "WHAT?"
    sus "I'd never do something like that!"
    ast "Really? Because it sure looks like you did..." ("grin", "base", "base", "R")
    sus "I--{w} I don't know why..."
    ast "If you don't like it down there, why don't you just hop out then?" ("annoyed", "base", "base", "R")
    sus "I can't!"
    ast "Really? why's that, Suzy?" ("grin", "narrow", "base", "down")
    sus "I don't know... I just can't!"
    ast "*Hmm*... it must be because you're such a nasty little slut then..." ("open", "closed", "base", "mid")
    with hpunch
    sus "I-- I am not!"
    ast "Are you sure?" ("grin", "base", "angry", "down")
    sus "I... Y-yes..."
    ast "because it sure doesn't look like that..." ("open", "narrow", "base", "down")
    ast "In fact, it looks like you're the nastiest little slut this school has ever seen!" ("grin", "closed", "base", "mid")
    gen "That's it, Astoria..." ("angry", xpos="far_left", ypos="head")
    sus "Professor... {b}please...{/b}"
    ast "Please what, Susan?" ("open", "closed", "base", "mid")
    ast "Please stop?" ("open", "narrow", "base", "down")
    ast "Or please coat me in cum?" ("clench", "narrow", "angry", "down")
    with hpunch
    sus "ASTORIA!"
    ast "Answer the question, Suzy..." ("open", "base", "base", "mid")
    sus "..."
    sus "Please sir..."
    sus "{size=-3}Coat{/size} {size=-3}me{/size} {size=-3}in{/size} {size=-3}your{/size} {size=-3}cum...{/size}"
    ast "I knew it!" ("scream", "base", "angry", "L")
    ast "You're a dirty little slut after all, aren't you!" ("clench", "narrow", "angry", "down")
    sus "I am not! I don't know why I'm down here!"
    ast "Alright then... if you're such a good girl..." ("open", "closed", "base", "mid")
    ast "Why don't you tell me what it's like down there?" ("smile", "narrow", "base", "down")
    sus "Down here?"
    sus "Under professor Dumbledore's desk?"
    ast "*Mhmm*... I bet it's nasty down there..." ("clench", "narrow", "angry", "down")
    ast "It probably smells gross with all the yucky cum he shoots against that desk of his..." ("open", "base", "base", "R")
    ast "Not to mention his big, smelly old cock..." ("annoyed", "narrow", "base", "ahegao")
    gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
    ast "Quiet, sir!" ("clench", "narrow", "angry", "mid")
    ast "So go on, Suzy... tell me what it's like..." ("open", "closed", "base", "mid")

    sus "It... It's--"
    nar "you hear Susan take a deep breath before she begins to speak."
    sus "{size=+10}It's incredible!{/size}"
    ast "" ("grin", "narrow", "angry", "mid")
    sus "Everything about it is fantastic!"
    ast "" ("smile", "base", "base", "mid")
    sus "The cum stains on the back of the desk..."
    ast "" ("clench", "narrow", "base", "mid")
    sus "The thick smell of semen in the air..."
    ast "" ("clench", "narrow", "base", "R")
    sus "The way Professor Dumbledore's stroking his {b}cock{/b}..."
    ast "" ("smile", "narrow", "angry", "R")
    sus "I just want to--"
    ast "(*Eeeegh*...)" ("scream", "closed", "angry", "mid",trans=hpunch)

    sus "..."
    nar "You hear Susan's words trail off into nothingness, as she takes another breath..."
    sus "I wish I could live down here! Is that what you wanted to hear, you evil witch?!"
    ast "Almost..." ("grin", "narrow", "base", "down")
    ast "I want you to tell me the truth... say you're a slut..." ("grin", "base", "angry", "mid")
    ast "Then I'll let you go..." ("open", "closed", "base", "mid")
    sus "Really?"
    sus "Alright..."
    sus "{size=-5}I'm a...{/size} {size=-3}slut...{/size}"
    ast "*Hmm*... I'm not sure I heard anything. What about you, sir?" ("annoyed", "base", "base", "R")
    gen "*Ah*...{w=0.3} almost..." ("base", xpos="far_left", ypos="head")
    ast "Go on Suzy... one more time..." ("smile", "narrow", "base", "down")
    with hpunch
    sus "I'm a slut, OK!"
    gen "*Ah*... YES..." ("angry", xpos="far_left", ypos="head")
    sus "I'm a nasty slut who crawled under her headmaster's desk and--"

    gen "HERE IT COMES SLUT!" ("angry", xpos="far_left", ypos="head")
    hide screen bld1
    call gen_chibi("cum_behind_desk")
    call cum_block
    sus "No wait! Astoria, you said I could go--"
    call cum_block
    gen "*ARGHHHH*!!!" ("angry", xpos="far_left", ypos="head")
    nar "Susan's sudden yelps prove too much for you as your cock begins to fire off an immense load onto Susan's face..."
    gen "HERE IT IS SLUT!!!" ("angry", xpos="far_left", ypos="head")
    call cum_block
    sus "..."

    ast "That's it, [name_genie_astoria]! Make sure you get it all out..." ("grin", "narrow", "angry", "mid")
    gen "*Ahhh*... don't worry about that..." ("angry", xpos="far_left", ypos="head")
    nar "You give your cock a few final pumps, working out the last of your load onto Susan's waiting face..."

    call gen_chibi("cum_behind_desk_done")
    pause.5
    gen "There we go..." ("angry", xpos="far_left", ypos="head")
    ast "Nice work, [name_genie_astoria]..." ("open", "closed", "base", "mid")
    ast "You can come out now, Suzy..." ("smile", "narrow", "base", "down")
    sus "..."

    stop music fadeout 1
    hide astoria_main
    show screen blkfade
    with d3

    nar "Susan slowly crawls out from under your desk..."

    call sus_chibi("stand","desk","base")
    $ susan.set_cum(face="heavy")
    hide screen blkfade
    with d5

    sus @ cheeks blush "..." ("soft", "narrow", "low", "mid", xpos="right", ypos="base", trans=fade)

    play music "music/KMcL_OpenThoseBrightEyes.ogg" fadein 1 if_changed
    ast "Oh my god! He absolutely covered you!" ("scream", "base", "base", "mid",xpos="base",ypos="base")
    sus @ cheeks blush "..." ("annoyed", "closed", "annoyed", "right")
    ast "I didn't know you had it in you, sir!" ("clench", "base", "base", "mid")
    ast "Nice work!" ("smile", "base", "base", "mid")
    gen "Thanks..." ("base", xpos="far_left", ypos="head")
    ast "And Suzy... that look suits you." ("grin", "narrow", "angry", "L")
    sus @ cheeks blush "Are you done, Astoria?" ("soft", "narrow", "annoyed", "right")
    ast "Yes, you can get dressed." ("smile", "narrow", "base", "L")

    show screen blkfade
    with d3

    nar "Susan slowly wipes the cum from her face as she begins getting dressed."

    hide susan_main
    $ susan.set_cum(None)
    sus @ cheeks blush "I hope you two are happy..." ("soft", "happy", "annoyed", "down")

    play sound "sounds/cloth_sound3.ogg"
    $ susan.wear("top", "bra")
    hide screen blkfade
    with d5
    pause .8

    sus @ cheeks blush "Now, if you'll excuse me, I've got--" ("open", "closed", "annoyed", "right")

    # chibi spell animation.
    play sound "sounds/magic2.ogg"
    call ast_chibi("wand_imperio",530,"base")
    with hpunch
    pause.8

    nar "You watch as a colourful mist spreads from the tip of Astoria's wand and seeps into Susan's nostrils once again..."
    ast "I don't think so..." ("smile", "narrow", "base", "L")


    call ast_chibi("reset",530,"base")
    sus "..." ("soft", "narrow", "base", "stare")
    gen "..." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        ast "We're going to be late for classes, Suzy!" ("annoyed", "narrow", "base", "R")
        ast "Let's head to Tonks' study, shall we." ("smile", "narrow", "base", "R")
        sus "Yes..." ("open", "narrow", "base", "stare")
        gen "..." ("base", xpos="far_left", ypos="head")
        ast "Until next time, [name_genie_astoria]!" ("grin", "closed", "base", "mid")
    else:
        ast "It's getting a bit late Suzy, let's head to Tonks' study..." ("annoyed", "narrow", "base", "R")
        sus "Yes..." ("open", "narrow", "base", "stare")
        gen "..." ("base", xpos="far_left", ypos="head")
        ast "Good night, [name_genie_astoria]!" ("grin", "closed", "base", "mid")


    stop music fadeout 1
    call hide_characters
    pause .5
    call ast_walk("door","base")
    pause.2
    call ast_chibi("stand","door","base", flip=False)
    with d3
    pause.5

    ast "Come on then..." ("angry", "narrow", "base", "R")
    sus "Okay..." ("open", "narrow", "base", "stare")

    call sus_walk(action="leave")

    call hide_characters
    call ast_chibi("leave")
    hide screen bld1
    with d3
    pause.5

    call gen_chibi("sit_behind_desk")

    call bld
    gen "(*Hmm*... Miss Bones still seemed affected even after she lessened her hold of the spell...)" ("base", xpos="far_left", ypos="head")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    if states.ast.level < 24:
        $ states.ast.level = 24
        $ states.sus.level = 24
        $ states.sus.wardrobe_unlocked = True

        call end_of_content

    jump end_ag_se_imperio_sb
