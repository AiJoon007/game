

### Luna Intro ###

### Event 1 ###

label luna_intro_E1:

    # Setup
    $ states.lun.ev.intro.e1_complete = True
    $ name_luna_genie = "???"
    $ d_flag_01 = False
    $ d_flag_02 = [False, False, False, False, False]

    # Chibi Z Order. Default 3, (manual reset after event)
    $ hermione_chibi.zorder = 2
    $ luna_chibi.zorder = 2

    # Outfit Equips
    $ luna.equip(lun_outfit_default) # Sets this outfit as Luna's default.

    $ lun_outfit_last.save()
    $ her_outfit_last.save()
    $ ton_outfit_last.save()

    $ luna.equip(lun_outfit_pajama)
    $ hermione.equip(her_outfit_pajama)
    $ tonks.equip(ton_outfit_dressing_gown)

    stop music fadeout 1
    show screen blktone
    with d3

    pause .5
    play sound "sounds/snore1.ogg"

    gen "*Snore*{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    gen "Yes..." ("base", xpos="far_left", ypos="head")

    pause 1.0
    play sound "sounds/snore3.ogg"

    gen "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    gen "Let's weigh those melons then shall we..." ("base", xpos="far_left", ypos="head")

    pause 1.0
    play sound "sounds/snore2.ogg"

    gen "......{w=0.5}*Snore*{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
    gen "Can't find the scales... will have to use my hands..." ("grin", xpos="far_left", ypos="head")

    stop music fadeout 8.0
    hide screen blktone
    with d3
    pause .2

    call lun_walk(action="enter")
    call chibi_emote("thought", "luna")
    pause 1
    call chibi_emote("hide", "luna")
    call lun_walk("410", speed=0.7)
    play sound "sounds/kick.ogg"
    show screen gfx_effect(428, 365, img="smoke", zoom=0.25)
    with hpunch

    pause 0.5

    play sound "sounds/MaleGasp.ogg"
    call bld
    gen "M-My cabbages!" ("angry", xpos="far_left", ypos="head")

    $ luna.set_face(mouth="soft", eyes="closed", eyebrows="low", pupils="mid")
    show CG luna as cg zorder 17:
        align (0.5, 0.5)
        pos (-520, -300)
    with fade

    gen "Who is--"
    show CG luna as cg zorder 17:
        align (0.5, 0.5)
        pos (-520, -300)
        easein_quad 5.0 pos (-520, 150)

    gen "... A girl?"
    lun "*Mmh*"

    show CG luna as cg zorder 17:
        zoom 1.0
        align (0.5, 0.5)
        pos (-520, 150)
        easein_quad 3.0 align (0.0, 0.0) pos (0, 0) zoom 0.5

    gen "What are you doing in my office?"
    gen "Did Snape send you here? Surely--"
    lun "I can't find them, daddy..." ("open", "closed", "worried", "mid")
    gen "Daddy?!"
    lun "My glasses..." ("soft", "closed", "low", "mid")
    gen "You're...{w=0.4} looking for your glasses?"
    gen "Why would your glasses be in here?"
    gen "Hold on..."

    $ luna.hide()
    hide cg
    call gen_chibi("stand", 225, "base")
    with fade

    pause 0.5

    call gen_walk(path=[(230, 470), (440, 470), (450, 430)])
    call gen_chibi("stand", 450, "base", flip=False)
    with d3

    pause 0.5

    #Genie walks over behind Luna who doesn't turn around
    gen "(Is this girl sleepwalking?)" ("base", xpos="far_left", ypos="head")

    play music "music/wallpaper-by-kevin-macleod.ogg" fadein 5 if_changed
    lun "" ("soft", "closed", "low", "mid", xpos="mid", ypos="base", trans=dissolve)
    gen "Whoa,{w=0.2} check out these melons!" ("grin", xpos="far_left", ypos="head")
    gen "(Shit.... I said that out loud.)" ("angry", xpos="far_left", ypos="head")
    gen "(Guess she really must be sleepwalking...)" ("base", xpos="far_left", ypos="head")
    gen "(Although, maybe I could test it somehow just to be sure...)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "(What kind of {i}examination{/i} should I perform?)" ("base", xpos="far_left", ypos="head")
        "-Oral examination-":
            $ d_flag_01 = True
            gen "So... What's your name?" ("base", xpos="far_left", ypos="head")
            lun "...{w=0.8}Wrackspurts..." ("open", "closed", "low", "mid")
            gen "Charming..." ("base", xpos="far_left", ypos="head")
            gen "(I suppose that is a plausible name in this world...)" ("base", xpos="far_left", ypos="head")
            $ name_luna_genie = "Miss Backspurts?"

        "-Hands-on examination-":
            pause 0.5
            $ mouse_slap()
            lun "No!" ("angry", "happyCl", "low", "mid")
            gen "..." ("angry", xpos="far_left", ypos="head")
            lun "The Nargles..." ("open", "happyCl", "low", "mid")
            gen "The what now?" ("base", xpos="far_left", ypos="head")
            lun "*Inaudible mumbling*..." ("upset", "closed", "low", "mid")
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

        "-Shock therapy-":

            call blkfade
            call gen_chibi("dick_out", 450, "base", flip=False)
            hide luna_main
            pause 1
            call hide_blkfade
            gen "What do you think about this?" ("grin", xpos="far_left", ypos="head")
            lun "...Crumple-Horned Snorkack..." ("disgust", "closed", "low", "mid", trans=dissolve)
            gen "...Well, that's just rude..." ("base", xpos="far_left", ypos="head")
            pause 0.5
            with d3

    # Genie walks back to his chair and sits down
    gen "(What a strange girl...)" ("base", xpos="far_left", ypos="head")
    gen "(Although the crazies usually give the best blowjobs...)" ("base", xpos="far_left", ypos="head")
    gen "(Well, now I'm hard...)" ("base", xpos="far_left", ypos="head")

    menu:
        "-Jerk off-":
            gen "(Even after thousands of years, this is a new one even for me...)" ("base", xpos="far_left", ypos="head")

            call blkfade
            call gen_chibi("jerk_off", 450, "base", flip=False)
            lun "" ("soft", "closed", "low", "mid")
            pause 1
            nar "*Fap* *Fap* *Fap*"
            call hide_blkfade

            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Hey, you could at least talk dirty or something." ("base", xpos="far_left", ypos="head")
            lun "I feel...{w} tingling..." ("open", "closed", "low", "mid")
            gen "Nice..." ("grin", xpos="far_left", ypos="head")
            lun "Crawling on my skin..." ("normal", "closed", "low", "mid")

            call gen_chibi("dick_out", 450, "base", flip=False)
            gen "..." ("angry", xpos="far_left", ypos="head")
            gen "(Yeah, this is not going to work...)" ("base", xpos="far_left", ypos="head")
            call blkfade
            call gen_chibi("stand", 450, "base", flip=False)
            pause 1
            hide luna_main
            call hide_blkfade
            gen "(Better let someone else deal with this one...)" ("base", xpos="far_left", ypos="head")

        "-Don't-":
            call blkfade
            call gen_chibi("stand", 450, "base", flip=False)
            hide luna_main
            call hide_blkfade
            pause 1
            gen "(This is so weird, she's just standing there...)" ("base", xpos="far_left", ypos="head")
            gen "(I better get someone to deal with this...)" ("base", xpos="far_left", ypos="head")

    call gen_chibi("sit_behind_desk")
    with fade

    label luna_intro_E1.choices:

    menu:
        "-Summon Snape-" if not d_flag_02[0]:
            $ d_flag_02[0] = True
            nar "You put your palms on your temples, attempting to summon Snape, but nothing happens." # X-Man reference
            gen "*Hmm*... He must be dead..." ("base", xpos="far_left", ypos="head")
            gen "Dead drunk..." ("angry", xpos="far_left", ypos="head")

            jump .choices

        "-Summon Tonks-" if not d_flag_02[1]:
            $ d_flag_02[1] = True
            nar "You try to summon Tonks."
            pause 0.2
            play sound "sounds/magic3.ogg"
            nar "The spell fizzles."
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            gen "(Don't think that worked... Is she sleeping?)" ("base", xpos="far_left", ypos="head")

            jump .choices

        "-Summon God-" if not d_flag_02[2]:
            $ d_flag_02[2] = True
            nar "Nothing happened."
            gen "Figures..." ("base", xpos="far_left", ypos="head")

            jump .choices

        "-Summon Satan-" if not d_flag_02[3]:
            $ d_flag_02[3] = True

            gen "I summon thee... Satan." ("base", xpos="far_left", ypos="head")
            pause 1
            gen "*heh*... Just as I exp--" ("base", xpos="far_left", ypos="head")
            play sound "sounds/attack_snape2.ogg"
            show pentogram onlayer screens at Position(xpos=690, ypos=250, xanchor="center", yanchor="center")
            with d5

            pause 0.5
            gen "Uh-oh..." ("base", xpos="far_left", ypos="head")
            call blkfade
            hide pentogram onlayer screens
            centered "{size=+7}{color=#cbcbcb}20 minutes later...{/color}{/size}"

            gen "*Ha-ha*... Good one! Alright, talk to you later, Beelzebub!" ("grin", xpos="far_left", ypos="head")
            "Beelzebub" "Ah, don't be so formal, just call me Bub."
            "Beelzebub" "If you ever need some latest {i}hot{/i} news, I'm your guy."
            call give_reward("Satan's phone number has been added to your contacts list.", "interface/icons/phone.webp")
            gen "Thanks Bub, will do!" ("grin", xpos="far_left", ypos="head")

            "Bub" "Take care!"
            play sound "sounds/attack_snape2.ogg"

            call hide_blkfade

            gen "..." ("base", xpos="far_left", ypos="head")
            gen "He's such a nice guy, I don't understand why people hate him so much." ("base", xpos="far_left", ypos="head")

            if d_flag_02[2]:
                gen "(And he at least answered the call, unlike the guy upstairs...)" ("base", xpos="far_left", ypos="head")
                play sound "sounds/thunder.ogg"
                with flash
                gen "!!!" ("angry", xpos="far_left", ypos="head")
                gen "...Sorry." ("base", xpos="far_left", ypos="head")

            gen "Anyway... What was I doing?" ("base", xpos="far_left", ypos="head")

            lun "*Snore*..." ("soft", "closed", "low", "mid", trans=dissolve)
            gen "Right..." ("base", xpos="far_left", ypos="head")

            jump .choices

        "-Summon Hermione-":
            pass

        "-Summon Jafar-" if not d_flag_02[4]:
            $ d_flag_02[4] = True
            gen "Who the fuck made this an option?!" ("angry", xpos="far_left", ypos="head")

            jump .choices

    call blkfade
    hide luna_main
    nar "You summon Hermione to your office."
    call hide_blkfade

    call her_walk("mid", action="enter")

    gen "Ah, Miss Granger..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]... do you know what time it--" ("normal", "happyCl", "base", "down", xpos=500, ypos="base", trans=dissolve)
    her "..." ("normal", "narrow", "base", "L")
    her "Luna? what are you doing here?!?" ("angry", "base", "worried", "L") #shocked

    if d_flag_01:
        gen "(Didn't she say her name was backspurts or something?)" ("base", xpos="far_left", ypos="head")

    $ name_luna_genie = "Miss Luna?"

    her "Don't tell me--" ("clench", "happy", "worried", "mid")
    gen "Quiet, girl." ("base", xpos="far_left", ypos="head")
    gen "She's sleepwalking..." ("base", xpos="far_left", ypos="head")
    her "She's...{w=0.4} Oh, I see..." ("open", "squint", "base", "L")
    lun "So warm..." ("open", "closed", "base", "mid", trans=dissolve)
    her @ cheeks blush "..." ("disgust", "squint", "base", "L") #weirded out
    gen "Can you do something?" ("base", xpos="far_left", ypos="head")
    her "Do what exactly? I thought you weren't supposed to wake somebody up when they're sleepwalking..." ("angry", "squint", "base", "mid")
    gen "Then just escort her back to her bed..." ("base", xpos="far_left", ypos="head")
    her "She's from Ravenclaw, I don't have access to their dormitory, so why me?" ("angry", "narrow", "base", "mid")

    if d_flag_02.count(True) == 0:
        # Selected Hermione as the first pick
        gen "You were the obvious choice, Miss Granger." ("base", xpos="far_left", ypos="head")
    elif d_flag_02[3]:
        # Selected Satan (Other choices don't matter)
        gen "Nobody else seemed to be picking up my calls..." ("base", xpos="far_left", ypos="head")
        gen "Well, except..." ("base", xpos="far_left", ypos="head")
        her "Except?" ("upset", "squint", "base", "mid")
        gen "Satan." ("base", xpos="far_left", ypos="head")
        her "Satan...?" ("clench", "base", "worried", "mid")
        gen "Never mind." ("base", xpos="far_left", ypos="head")
        her "..........." ("clench", "base", "base", "mid")
    else:
        gen "Nobody else seemed to be picking up my calls..." ("base", xpos="far_left", ypos="head")

    gen "Anyway,{w=0.2} how am I supposed to know that?" ("base", xpos="far_left", ypos="head")
    gen "She's not wearing her school uniform, is she?" ("base", xpos="far_left", ypos="head")
    her "I thought our headmaster was supposed to know all of our students..." ("upset", "squint", "base", "mid")
    gen "Even my immense knowledge has its limits, dear..." ("base", xpos="far_left", ypos="head")
    her "(Clearly there's more important things occupying your mind...)" ("normal", "narrow", "base", "R") # Rolls eyes
    her "How come you haven't escorted her back yourself, professor?" ("angry", "narrow", "annoyed", "mid")

    menu:
        "\"I just told you, I didn't know which house she's in.\"":
            her "Well... Now you know, so you can take her." ("angry", "closed", "angry", "mid")
            gen "I'd never take a lady in such a state, that's too far even for me." ("base", xpos="far_left", ypos="head")
            her "What are you--" ("disgust", "narrow", "annoyed", "mid")
            gen "Just take this weirdo... And get out of here, will you?" ("base", xpos="far_left", ypos="head")
        "\"I don't know where this Ravenglove dormitory is...\"":
            her "It's Ravenclaw, [name_genie_hermione]..." ("disgust", "narrow", "annoyed", "mid")
            gen "Yes, that's what I said..." ("base", xpos="far_left", ypos="head")
            her "You said--" ("angry", "closed", "angry", "mid")
            her "What do you mean you don't know where their dormitory is?" ("clench", "squint", "base", "mid")
            gen "Girl, I'm starting to lose my patience..." ("base", xpos="far_left", ypos="head")
            gen "Just get this weirdo out of here, will you?" ("base", xpos="far_left", ypos="head")
        "-Dismiss the question-":
            gen "Just get this weirdo out of here, please." ("base", xpos="far_left", ypos="head")

    her "[name_genie_hermione]!" ("angry", "narrow", "worried", "mid") # Gasp
    lun "It tickles..." ("grin", "closed", "worried", "mid")
    her "......" ("disgust", "squint", "base", "L") # Looks at Luna, puzzled.
    her "She...{w=0.4} She's not a weirdo... She's just a bit... Loony..." ("disgust", "squint", "base", "mid")
    gen "I don't care what you call it, just escort miss {i}Loony{/i} back to her bed...." ("base", xpos="far_left", ypos="head")
    her "I can't!" ("clench", "squint", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "As I've already said, professor... I'm not allowed in their dormitory." ("open", "squint", "base", "L")
    gen "Bloody hell, there's always {i}something{/i}..." ("angry", xpos="far_left", ypos="head")

    if d_flag_02[1]:
        # tonks enters (wearing something sexy)
        call ton_walk("mid", 460, action="enter")

        ton "*Yawn* Sorry I'm late, [name_genie_tonks]." ("annoyed", "narrow", "shocked", "L", xpos="base", ypos="base", trans=dissolve)
        gen "You took your damn time." ("base", xpos="far_left", ypos="head")
        ton "I was in the middle of... something important." ("horny", "narrow", "base", "R")
        gen "Important, *hmm*..." ("base", xpos="far_left", ypos="head")
    else:
        her "I suggest you should summon a teacher to escort her back." ("open", "closed", "base", "mid")
        gen "Very well... I will summon--" ("base", xpos="far_left", ypos="head")
        her "Anyone but Snape!" ("clench", "narrow", "base", "mid")
        lun "*Sniff*..." ("soft", "closed", "base", "mid")
        her "Shush now... It's okay Luna, professor Snape is not allowed here." ("open", "squint", "base", "L")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Fine. I'll just get Professor Tonks up here..." ("base", xpos="far_left", ypos="head")

        call blkfade
        nar "You attempt to summon Tonks to your office."
        hide hermione_main
        hide luna_main
        call hide_blkfade

        call ton_walk("mid", 460, action="enter")
        ton "You called..." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=dissolve)

    her @ cheeks blush "Professor!" ("clench", "squint", "worried", "L", flip=True, trans=dissolve) #Wide eyed
    ton "*Oooooh* What's this? A slumber party?" ("horny", "narrow", "base", "down")
    gen "It is now!" ("grin", xpos="far_left", ypos="head")
    gen "Let me search for my bathrobe real quick." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "P-Professor, that's not why we asked her here." ("angry", "narrow", "base", "mid")
    gen "Right...{w=0.3} Miss Tonks, we may require your assistance here..." ("base", xpos="far_left", ypos="head")
    ton "Assistance? With what--" ("open", "base", "raised", "mid")
    lun "Wrackspurts!"
    ton "Ah... Miss Lovegood." ("base", "narrow", "raised", "L")

    if d_flag_01:
        gen "Luna Love-good... *heh*, that's funny." ("grin", xpos="far_left", ypos="head")
        ton "What's funny?" ("base", "base", "base", "mid")
        gen "Love...{w=0.4} Good...{w=0.6} Get it?" ("base", xpos="far_left", ypos="head")
        ton "..." ("base", "base", "base", "mid")
        gen "Anyway..." ("base", xpos="far_left", ypos="head")

    $ name_luna_genie = "Miss Lovegood"

    gen "This so-called Miss {i}Lovegood{/i} sleep-walked in here." ("base", xpos="far_left", ypos="head")
    ton "How am I not surprised." ("base", "closed", "base", "mid")
    her @ cheeks blush "P-Professor, what are you wearing?!" ("angry", "narrow", "base", "down")
    gen "Yes, Miss Tonks. What in the great desert sands are you wearing?" ("angry", xpos="far_left", ypos="head")
    gen "Is this a school or a brothel?" ("grin", xpos="far_left", ypos="head")

    ton @ hair horny "It's my nightgown... You don't like it?" ("horny", "narrow", "raised", "L") # Flirtatious
    # Fun option
    menu:

        "\"I love it!\"":
            gen "You look like a slut!" ("grin", xpos="far_left", ypos="head")

        "\"You look like a slut!\"":
            gen "I love it!" ("grin", xpos="far_left", ypos="head")

    her @ cheeks blush "Professor!" ("mad", "base", "base", "mid")
    her @ cheeks blush "How could you say such a thing!?" ("open", "happyCl", "base", "mid")
    ton @ hair horny "Yes... Such a rude thing to say to your staff. {heart}" ("soft", "narrow", "annoyed", "mid")
    gen "I'm a man of simple truths, I'm only stating the obvious." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "So my current attire is too slutty for you, *huh*?" ("base", "narrow", "base", "L")
    gen "I didn't say that, Miss Tonks..." ("grin", xpos="far_left", ypos="head")
    gen "I said you look like a slut... There's a difference." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "What if a student saw you professor?! You can't walk around the castle wearing... This!" ("angry", "narrow", "base", "down")
    ton "Quit worrying. Nobody is going to see me this late at night." ("open", "narrow", "base", "R")
    ton "After all, it's already past curfew..." ("open", "base", "base", "mid")
    ton "Students should be in their beds, including you, Miss Granger." ("soft", "base", "raised", "L")
    her @ cheeks blush "But professor Dumbledore asked me to--" ("clench", "squint", "base", "mid")
    ton "You just head back to bed, and I'll make sure Miss Lovegood gets back safe and sound to her dormitory..." ("base", "narrow", "base", "L")
    her @ cheeks blush "Okay..." ("disgust", "narrow", "base", "down") #annoyed
    ton "Good girl." ("horny", "narrow", "base", "L")

    call her_walk("door")

    her @ cheeks blush "Good night then..." ("normal", "squint", "base", "R", xpos="base", ypos="base") #annoyed, flipped
    ton "Sleep tight, Miss Granger..." ("horny", "narrow", "base", "R", xpos=400, ypos="base", trans=dissolve) # Tongue in cheek

    call her_walk(action="leave")

    # Tonks should maybe talk to Genie about the situation some more here.

    ton "Very well then..." ("soft", "narrow", "raised", "L", xpos="base", ypos="base", trans=dissolve)
    ton "Come on, Miss Lovegood, let's get you back to bed..." ("open", "narrow", "base", "L")

    #Tonks walks to the door

    lun "But I'm not tired mummy..." ("annoyed", "closed", "base", "mid", trans=dissolve)
    ton @ cheeks blush hair horny "..." ("disgust", "shocked", "base", "mid") #wide eyed
    gen "What a weirdo..." ("base", xpos="far_left", ypos="head")
    ton "Just...{w=0.4} be a good girl and follow me back to bed..." ("upset", "narrow", "worried", "L")
    lun "Yes, mummy..." ("base", "closed", "base", "mid")

    call lun_walk("door")

    ton "Don't worry about her, she'll be fine." ("annoyed", "narrow", "base", "downR")
    gen "I won't." ("base", xpos="far_left", ypos="head")

    call ton_walk("door", action="leave")
    call lun_walk(action="leave")

    gen "(This place never ceases to amaze me...)" ("base", xpos="far_left", ypos="head")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(At least that weirdo isn't my problem anymore...)" ("base", xpos="far_left", ypos="head")
    gen "(Time to get back to sleep.)" ("base", xpos="far_left", ypos="head")

    # Reset
    $ luna.equip(lun_outfit_last) # Equip player outfit.
    $ tonks.equip(ton_outfit_last) # Equip player outfit.
    $ hermione.equip(her_outfit_last) # Equip player outfit.

    $ hermione_chibi.zorder = 3
    $ luna_chibi.zorder = 3

    call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_dressing_gown)
    call unlock_clothing(text="New clothing items for Hermione have been unlocked!", item=her_outfit_pajama)

    jump day_start

### Event 2 ###

label luna_intro_E2:

    # Setup
    $ lun_outfit_last.save()

    $ luna.equip(lun_outfit_default_quirky)

    #Next morning
    #Luna knocks on door
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"

    gen "Who is it?" ("base", xpos="far_left", ypos="head")
    lun "Luna."
    gen "Who?" ("base", xpos="far_left", ypos="head")
    lun "Luna Lovegood, Sir."
    gen "Love... good?" ("base", xpos="far_left", ypos="head")
    lun "Yes!"
    gen "(I don't remember ordering any foreign prostitutes...)" ("base", xpos="far_left", ypos="head")
    gen "(Maybe Snape has finally sent one of his Slytherin whores.)" ("grin", xpos="far_left", ypos="head")

    menu:
        "-Invite them in-":
            $ states.lun.ev.intro.e2_complete = True
            gen "Enter!" ("grin", xpos="far_left", ypos="head")

        "\"I'm busy!\"":
            gen "Come back tomorrow." ("base", xpos="far_left", ypos="head")
            lun "Oh, okay."
            lun "I'll come back tomorrow then."
            $ ll_event_pause += 1

            jump end_luna_event

    call lun_walk(action="enter")
    pause 0.5

    gen "{size=-4}Oh... It's miss Loony.{/size}" ("base", xpos="far_left", ypos="head")
    play music "music/wallpaper-by-kevin-macleod.ogg" fadein 1 if_changed

    call lun_walk("desk")

    lun "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    pause 1

    gen "(Whoa!)" ("angry", xpos="far_left", ypos="head")
    gen "(Finally someone who knows how to wear a uniform properly!)" ("grin", xpos="far_left", ypos="head")
    gen "(Look at those thighs!)" ("grin", xpos="far_left", ypos="head")

    menu:
        "-Jerk off-":
            gen "(*Argh*... Screw it...)" ("base", xpos="far_left", ypos="head")
            call gen_chibi("jerk_off_behind_desk")
            with d3
            nar "You drop down your pants and start jerking off."
            $ states.gen.masturbating = True

        "-Behave-":
            $ states.gen.masturbating = False

    if states.gen.masturbating:
        gen "Miss-- *Ah*... Love-good. What can I do you for?" ("grin", xpos="far_left", ypos="head")
    else:
        gen "Miss Lovegood... What can I help you with?" ("base", xpos="far_left", ypos="head")

    lun "*Hmm*..." ("soft", "narrow", "raised", "downL")

    if states.gen.masturbating:
        nar "*fap-fap-fap*!"
        gen "(Look at the tits on this girl, such a lovely profile!)" ("angry", xpos="far_left", ypos="head")
        gen "(And that lush blonde hair! I'd love to wrap it around my dick!)" ("grin", xpos="far_left", ypos="head")
    else:
        gen "Miss Lovegood?" ("base", xpos="far_left", ypos="head")

    call lun_walk(600, 460)
    call lun_chibi(flip=True)
    nar "Luna absent-mindedly starts looking around your office."

    if not states.gen.masturbating:
        gen "*Uhh* Hello?" ("base", xpos="far_left", ypos="head")

    call lun_walk("mid", "base")

    gen "(What's wrong with this girl?)" ("base", xpos="far_left", ypos="head")

    if states.gen.masturbating:
        gen "(Whatever. As long as I can beat my meat in peace.)" ("grin", xpos="far_left", ypos="head")
        nar "*fap-fap-fap*"

    call lun_walk("desk", "base")
    pause 0.25
    call lun_chibi(flip=True)
    with d3

    show CG lun_intro luna bendover as cg zorder 17:
        zoom 0.5
    with fade

    nar "Luna turns around and bends down slightly, examining the floor tiles, giving you an eyeful of her round butt without realising."

    if states.gen.masturbating:
        show CG lun_intro luna bendover as cg zorder 17:
            subpixel True
            zoom 0.5
            pos (0, 0)
            easein_quad 2.0 zoom 1.0 pos (-1040, -600)

        gen "(Holy shit... That ass!)"
        nar "{size=+3}*{b}fap{/b}-fap-{b}fap{/b}*{/size}"
        gen "*Ugh*... (I'm getting close.)"

        show CG lun_intro luna bendover as cg zorder 17:
            subpixel True
            zoom 1.0
            pos (-1040, -600)
            easein_quad 5.0 zoom 0.5 pos (0, 0)

        lun "There's such a strange aura in here..."
        gen "(Yes! It's the aura of me going crazy for you, you fucking slut!)"
        nar "{size=+3}*{b}fap{/b}-fap-{b}fap{/b}*{/size}"
    else:
        lun "There's such a strange aura in here..."
        lun "It's like a big hollow tree..."
        gen "(Oh, good...{w=0.4} She's a hippie.)" ("base", xpos="far_left", ypos="head")

    call lun_chibi(flip=False)

    nar "Luna finally turns to face you."

    hide cg
    with fade


    if states.gen.masturbating:
        gen "(Yes, yes! You little slut! Here it comes!)" ("angry", xpos="far_left", ypos="head")
        call gen_chibi("cum_behind_desk")
        call cum_block
        lun "Whoa!" ("open", "wide", "base", "downL", trans=dissolve)
        call cum_block
        lun "There's so much!" ("soft", "wide", "base", "downL")
        gen "*Argh*... (And it's all yours...)" ("angry", xpos="far_left", ypos="head")
        lun "They're flying everywhere! How impressive!" ("grin", "wide", "base", "stare")
        gen "Yes! (All because of you, you silly-hot bimbo!)" ("angry", xpos="far_left", ypos="head")
        call cum_block
        gen "*Argh*-- {size=-4}fuck!{/size} *heavy panting*" ("angry", xpos="far_left", ypos="head")
        call gen_chibi("cum_behind_desk_done")
        with d3
    else:
        lun "Whoa!" ("open", "wide", "base", "downL", trans=dissolve)
        gen "What? Is there something on my face?" ("base", xpos="far_left", ypos="head")
        gen "Actually, first of all... What are you even wearing?" ("base", xpos="far_left", ypos="head") # Luna ignores him.
        pause 1
        lun "This room is full of them!" ("angry", "wide", "base", "L")
        gen "(She ignored my question...)" ("base", xpos="far_left", ypos="head")
        gen "Full of what?" ("base", xpos="far_left", ypos="head")
        lun "Wrackspurts!" ("soft", "wide", "base", "mid")
        gen "Not this again..." ("base", xpos="far_left", ypos="head")

    lun "Why, I've never seen anything like this before, and never so clear..." ("soft", "base", "base", "mid")

    if states.gen.masturbating:
        gen "There's more where that came from." ("grin", xpos="far_left", ypos="head")
        lun "So you can see {i}them{/i} too, Professor?" ("angry", "wide", "base", "mid")
        gen "See what?" ("base", xpos="far_left", ypos="head")
        lun "*sigh* Just as expected." ("upset", "narrow", "base", "down")
        lun "You could see them if you had one of these." ("grin", "base", "base", "mid")
    else:
        gen "I can't see anything." ("base", xpos="far_left", ypos="head")
        lun "Of course you can't, Professor." ("grin", "closed", "base", "mid")
        lun "Because you don't have these!" ("grin", "wink", "base", "mid")

    nar "Luna points to the oddly shaped glasses on her nose."
    gen "Those goofy looking glasses?" ("base", xpos="far_left", ypos="head")
    gen "Are you planning on winning a masquerade ball or something?" ("base", xpos="far_left", ypos="head")
    lun "Don't be fooled by their look, professor... These glasses are infused with magic." ("grin", "closed", "base", "mid")
    lun "They are called {i}Spectrespecs{/i}!" ("base", "wink", "base", "mid")

    menu:
        "\"Spectre-- what?\"":
            lun "Spectrespecs!" ("crooked_smile", "happyCl", "base", "mid")
            lun "They allow the wearer to see things that are there, but hidden." ("grin", "base", "base", "mid")
            gen "And that vaporware thing on your nose is supposed to help you with that?" ("base", xpos="far_left", ypos="head")
            lun "*Uh-huh!*" ("grin", "wink", "base", "mid")
            gen "Great..." ("base", xpos="far_left", ypos="head")

        "\"Spectres as in ghosts?\"":
            gen "*G-G-Ghe* Ghosts!" ("angry", xpos="far_left", ypos="head")
            lun "Well, I don't know about ghosts--" ("open", "base", "base", "down")
            gen "Quick, I need to call someone..." ("base", xpos="far_left", ypos="head")
            lun "Oh, who you gonna call?" ("soft", "base", "base", "R")
            gen "Luigi, he's clearly the superior choice when it comes to fighting ghosts." ("grin", xpos="far_left", ypos="head")
            lun "Who, sir?" ("open", "narrow", "raised", "mid")
            gen "Who... How do you not know... the inventor of the Luigi board?" ("angry", xpos="far_left", ypos="head")
            lun "*Huh*?" ("angry", "base", "worried", "mid")
            gen "Never mind." ("base", xpos="far_left", ypos="head")
            gen "If not ghosts..." ("base", xpos="far_left", ypos="head")

        "\"The theory of the parable fourth dimensional tuples.\"":
            lun "I'm sorry, sir?" ("upset", "narrow", "base", "mid")
            gen "*Sigh* I'm talking about the four-dimensional space, {size=-1}a mathematical{/size} {size=-2}extension of the concept{/size} {size=-3}of three-dimensional or 3D space.{/size} {size=-5}Three-dimensional space{/size}{size=-7} is the simplest possible abstraction of the observation that one only needs three numbers, called dimensions, to describe the sizes or locations of objects in the everyday world.{/size}{size=-10}For example, the volume of a rectangular box is found by measuring and multiplying its length, width, and height (often labeled x, y, and z)...{/size}" ("base", xpos="far_left", ypos="head")
            call blkfade
            centered "{size=+7}{color=#cbcbcb}5 minutes later...{/color}{/size}"
            call hide_blkfade
            gen "...and this is how your glasses work, right?" ("base", xpos="far_left", ypos="head")
            lun "I... Maybe?" ("angry", "narrow", "base", "down") # Puzzled
            gen "Don't they teach you basic physics in this school?" ("base", xpos="far_left", ypos="head")
            gen "No matter." ("base", xpos="far_left", ypos="head")

    gen "What are you seeing in this room exactly?" ("base", xpos="far_left", ypos="head")
    lun "Wrackspurts, sir, and lots of them too!" ("soft", "narrow", "base", "mid")
    gen "Brackspurts?" ("base", xpos="far_left", ypos="head")
    lun "Wrackspurt sir..." ("open", "base", "base", "L")
    gen "I see...{w=0.2} *Err*, I mean I don't." ("base", xpos="far_left", ypos="head")
    gen "(Is she making all this shit up, or am I supposed to know about these things?)" ("base", xpos="far_left", ypos="head")
    gen "Well, I can't say I've ever come across these whackspurs you speak of." ("base", xpos="far_left", ypos="head")
    lun "There's a whole section dedicated to them in {i}the quibbler{/i}, it's a quite fascinating read you know." ("grin", "wink", "base", "mid")
    gen "Pretend that I don't know..." ("base", xpos="far_left", ypos="head")
    lun "{i}The quibbler{/i} is my daddy's magazine, sir." ("grin", "base", "base", "mid")
    gen "So is that why you're here?" ("base", xpos="far_left", ypos="head")
    gen "To advertise your father's magazine?" ("base", xpos="far_left", ypos="head")
    gen "Now I must say that's quite bold for a student to just waltz into their headmasters office and shill their--" ("base", xpos="far_left", ypos="head")
    lun "Oh... No sir!" ("mad", "narrow", "base", "downL")
    lun "I'm just worried that we might have an infestation on our hands and--" ("angry", "closed", "base", "mid")
    lun "..." ("angry", "narrow", "base", "down")
    #Luna eyes down
    pause .5
    nar "Luna gives you an uncomfortable look and then turns her gaze to the floor."
    gen "An infestation?" ("base", xpos="far_left", ypos="head")
    lun "Yes sir. I've come across several swarms of them in a fair few places recently." ("mad", "base", "base", "mid")
    lun "They appeared quite docile at first, but recently, they've started to become quite problematic..." ("angry", "narrow", "base", "down")
    gen "Well, I sure would love to be able to help Miss Lovegood, but as I said this is the first time I even heard about these things..." ("base", xpos="far_left", ypos="head")
    lun "Oh... But you can help, sir!" ("soft", "wide", "base", "mid")
    lun "You're the most powerful wizard there is, so if anyone could deal with them, it'd be you..." ("grin", "narrow", "base", "mid")
    gen "Well... I'm not usually the person to brag but..." ("base", xpos="far_left", ypos="head")
    gen "I am known to have slung some seriously powerful spells around back in the day..." ("grin", xpos="far_left", ypos="head")
    lun "Oh, thank you sir, I knew you'd be able to help!" ("grin", "happyCl", "base", "mid")
    gen "Why of course, anything for a student in--" ("base", xpos="far_left", ypos="head")
    gen "Hold on, I didn't actually say yes yet!" ("angry", xpos="far_left", ypos="head")
    lun "So I think what would be best is if you'd read my daddy's magazine..." ("grin", "narrow", "base", "downL")
    gen "(Is she even listening?)" ("base", xpos="far_left", ypos="head")
    lun "I'm sure once you've read through all of it you'll be able to use your immense knowledge to find a solution..." ("grin", "base", "base", "mid")
    gen "Of course!" ("grin", xpos="far_left", ypos="head")
    gen "I am all knowing after all!" ("grin", xpos="far_left", ypos="head")
    gen "(Or am I? I don't even know anymore...)" ("base", xpos="far_left", ypos="head")
    gen "(Wait... She did it again!)" ("angry", xpos="far_left", ypos="head")
    lun "Thank you sir..." ("base", "base", "base", "mid")
    gen "Now hold on for a second..." ("base", xpos="far_left", ypos="head")
    lun "Please let me know what you think of the paper once you've read it!" ("grin", "wink", "base", "mid")
    gen "What paper?" ("base", xpos="far_left", ypos="head")
    lun "The quibbler!" ("soft", "base", "base", "mid")
    gen "Oh... right..." ("base", xpos="far_left", ypos="head")
    lun "I'll leave you to it then." ("grin", "base", "base", "mid")
    gen "You do that..." ("base", xpos="far_left", ypos="head")

    call lun_walk("door", "base")
    call lun_chibi(flip=False)
    with d3

    lun "See you later, sir." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=dissolve)

    call lun_walk(action="leave")

    gen "(No wonder Miss Granger called her Loony... Her mind might as well be in another dimension...)" ("base", xpos="far_left", ypos="head")
    gen "(Where am I even supposed to get that bloody magazine from?)" ("base", xpos="far_left", ypos="head")

    if not item_store_intro_done:
        gen "(*Hmm*... I'm sure someone's bound to have it.)" ("base", xpos="far_left", ypos="head")
        gen "(Maybe it's time to look around the castle a bit more...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "(Well... Hopefully the twins have it in stock...)" ("base", xpos="far_left", ypos="head")

    stop music fadeout 1.0

    $ states.lun.unlocked = True
    $ achievements.unlock("unlocklun", True)
    call popup("{size=-4}You can now summon Luna into your office.{/size}", "Character unlocked!", "interface/icons/head/luna.webp")

    # Reset
    $ luna.equip(lun_outfit_last) # Equip player outfit.
    call gen_chibi("sit_behind_desk")

    jump end_luna_event
