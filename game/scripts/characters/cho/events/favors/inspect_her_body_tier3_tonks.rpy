
## Tier 3 - Summon Tonks ##

label cc_pf_strip_T3_tonks:

    # Setup
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    $ name_cho_tonks = renpy.random.choice( ("Sweetie", "babe", "Honey") )
    # All character's clothes get saved in case we need to change any.
    # Cho and Tonks won't change their clothes.

    $ cho_outfit_last.save() # Store current outfit.
    $ ton_outfit_last.save() # Store current outfit.
    $ her_outfit_last.save() # Store current outfit.

    #$ cho.equip(cho_outfit_default)
    #$ tonks.equip(ton_outfit_default)
    $ hermione.equip(her_outfit_default)

    call cho_chibi("stand", "desk", "base", flip=False)

    hide screen blkfade
    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=fade)

    # Intro
    if states.cho.ev.inspect_her_body.tonks_doppler_encounter == False and states.cho.ev.inspect_her_body.tonks_succubus_encounter == False: # First time only.
        gen "About your teacher, Professor Tonks..." ("base", xpos="far_left", ypos="head")
        gen "That ability she has, it's quite... interesting, don't you think?" ("base", xpos="far_left", ypos="head")
        cho "It is! And exceptionally rare as well!" ("grin", "happyCl", "base", "mid")
        cho "I only ever heard about this type of transfiguration ability once -- during one of Professor McGonagall's lessons..." ("open", "base", "raised", "mid")
        cho "She seemed kind of annoyed by the fact that there are people with natural abilities to change their appearance like that." ("annoyed", "base", "base", "R")
        gen "Well, not everyone can be as naturally handsome as me." ("grin", xpos="far_left", ypos="head")
        cho "That... is not what I meant." ("open", "closed", "angry", "mid")
        gen "I wonder if she's the only person here who has this \"Metamorphic\" ability..." ("base", xpos="far_left", ypos="head")
        cho "I hope so..." ("annoyed", "base", "base", "mid")
        gen "You do?" ("base", xpos="far_left", ypos="head")
        cho "You've seen the kind of thing she uses her ability for, haven't you?" ("open", "narrow", "base", "mid")
        cho "Surely when you decided to tell me her secret -- you considered what could happen if I told the other students about it?" ("open", "closed", "base", "mid")
        gen "I...{w=0.2} Of course!" ("angry", xpos="far_left", ypos="head")
        cho "Don't worry, I won't tell anyone..." ("open", "narrow", "base", "mid")
        cho "Though I'd suggest keeping it a secret from Granger at all cost!" ("mad", "narrow", "angry", "mid")
        cho "I'm confident she'd come up with some annoying rule to try and keep her teacher in check..." ("annoyed", "narrow", "angry", "mid")
        gen "Right..." ("base", xpos="far_left", ypos="head")
        cho "Well, I'm glad to know that you trust me with something like this, [name_genie_cho]." ("smile", "happyCl", "base", "mid")
        cho "It'd be quite difficult for her to pretend to be someone else, if everybody knew about it." ("annoyed", "base", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        cho "I sure am glad there isn't another student with her abilities..." ("annoyed", "narrow", "base", "R")
        gen "*Ha-ha*, yeah..." ("grin", xpos="far_left", ypos="head")
        gen "Another student -- preferably female -- with her abilities...{w=0.5} That would be horrible..." ("base", xpos="far_left", ypos="head")
        gen "(Not...)" ("grin", xpos="far_left", ypos="head")
        cho "Yes... If they somehow found out about Tonks, she'd surely receive all the blame." ("angry", "narrow", "raised", "mid")
        gen "..." ("angry", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "narrow", "base", "mid")
        gen "Let's just call her up here for now..." ("base", xpos="far_left", ypos="head")
        gen "I'm sure she'll make it well worth it for you to continue keeping her secret safe." ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "Yes, [name_genie_cho]..." ("smile", "narrow", "base", "mid") #glancing away #blush

    # Repeat
    else:
        gen "Let me summon her real quick." ("base", xpos="far_left", ypos="head")
        cho "Yes, [name_genie_cho]." ("base", "base", "base", "mid")

    stop music fadeout 1
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    # You summon Tonks.
    call cho_chibi("stand", "desk", "base", flip=True)
    with d3
    pause .8

    # Tonks enters.
    play sound "sounds/door.ogg"
    call ton_chibi("stand", "door", "base")
    with d3
    pause .5

    # Tonks walks next to Cho.
    call ton_walk(540, "base")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    cho @ cheeks blush "" ("base", "narrow", "worried", "L", xpos="left", ypos="base", flip=True)
    ton "Hello, Professor." ("soft", "narrow", "base", "mid", xpos="right", ypos="base", flip=False)
    ton "Miss Chang." ("base", "narrow", "raised", "L")

    # Intro
    if states.cho.ev.inspect_her_body.tonks_doppler_encounter == False and states.cho.ev.inspect_her_body.tonks_succubus_encounter == False: # First time only.
        gen "Didn't fancy taking the fireplace this time?" ("base", xpos="far_left", ypos="head")
        ton "Not today... I only use floo powder when I'm in a hurry." ("open", "base", "base", "mid")


    ## Tonks and Cho strip for you ##
    ton "So...{w=0.3} What do you have planned for us today, Professor?" ("base", "narrow", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Why don't you tell her what we're doing, Miss Chang?" ("grin", xpos="far_left", ypos="head")
    cho "You want me to--" ("open", "narrow", "base", "mid")
    gen "Don't see why not..." ("grin", xpos="far_left", ypos="head")
    cho "Of course, Sir." ("soft", "narrow", "base", "downR")

    if states.cho.ev.inspect_her_body.tonks_doppler_encounter == False and states.cho.ev.inspect_her_body.tonks_succubus_encounter == False: # First time only.
        cho @ cheeks blush "..." ("annoyed", "narrow", "worried", "down") # Embarrassed look down.
        cho @ cheeks blush "The headmaster wanted to see us strip for him again..." ("open", "narrow", "worried", "L")
        if cho.is_worn("robe") or ( cho.is_worn("top") and cho.is_worn("bottom") ):
            pass
        else: # Cho is in her underwear or naked.
            gen "Well... A bit of a show should do, seeing what your current state of undress is like..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "You're the one that requested it..." ("annoyed", "narrow", "angry", "down") # small text

        if tonks.is_worn("robe") or ( tonks.is_worn("top") and tonks.is_worn("bottom") ):
            pass
        else: #Tonks is in her underwear or naked.
            ton @ hair horny "*Hmm*...{w=0.3} Who needs clothing anyway?" ("horny", "narrow", "base", "L")
            ton @ hair horny "But I'll give you a show if that's what you want...{heart}" ("horny", "narrow", "base", "mid")
        gen "..." ("grin", xpos="far_left", ypos="head")

    else: # repeat
        cho @ cheeks blush "The headmaster wants us to strip for him again." ("base", "narrow", "base", "mid")
        ton @ hair horny "Does he now?" ("horny", "narrow", "base", "L")
        if cho.is_worn("robe") or ( cho.is_worn("top") and cho.is_worn("bottom") ):
            pass
        else:
            gen "Well, since you're not wearing much... I'd at least like a show..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "Very well..." ("annoyed", "narrow", "angry", "down") # small text

        if tonks.is_worn("robe") or ( tonks.is_worn("top") and tonks.is_worn("bottom") ):
            pass
        else: #Tonks in in her underwear or naked.
            ton @ hair horny "Stripping's out of the question for me that's for sure..." ("horny", "narrow", "base", "L")
            ton @ hair horny "But I'll give you a good view at the very least...{heart}" ("horny", "narrow", "base", "mid")

    ton @ hair horny "Well, in that case we shouldn't keep him waiting, should we?" ("horny", "narrow", "base", "L")
    ton @ hair horny "After you, [name_cho_tonks]." ("horny", "narrow", "base", "L")
    stop music fadeout 1

    # Cho and Tonks hop onto the desk.
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=False)
    with d3
    pause .1

    show screen blkfade
    with d5


    # Tonks chibi on desk next to Cho's. # Tonks is facing left
    call cho_chibi("stand", 314, 366, flip=True)
    call ton_chibi("stand", 370, 360, flip=False)

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    hide screen blkfade
    with d5
    pause .8

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    $ cho.zorder = 16 # in front of Tonks # Default is 15.
    $ tonks.zorder = 15 # reset to default.
    cho @ cheeks heavy_blush "" ("base", "narrow", "base", "L", xpos=280, ypos="base", flip=True)
    ton @ hair horny "..." ("base", "narrow", "raised", "L", xpos=345, ypos="base")

    ton @ hair horny "This feels quite familiar, doesn't it, Miss Chang?" ("crooked_smile", "narrow", "raised", "L")
    cho @ cheeks blush "..." ("horny", "narrow", "base", "mid")
    ton @ hair horny "Let's not waste any more time..." ("horny", "narrow", "base", "L")

    ton @ hair horny "Who of us would you like to start, Professor?" ("base", "narrow", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"Miss Chang will go first.\"":
            cho @ cheeks blush "..." ("horny", "narrow", "base", "down")
            $ cho_position = 1 # Cho's current positon is in the middle.

            jump cc_pf_strip_T3_tonks.strip_cho

        "\"You go first, Miss Tonks!\"":
            ton @ hair horny "*Hmm*..." ("base", "narrow", "base", "L")
            ton @ hair horny "Saving the best for last, are we?" ("base", "narrow", "raised", "mid")
            cho @ cheeks blush "..." ("horny", "narrow", "base", "downR")
            $ cho_position = 1 # Cho's current position is in the middle.

            jump cc_pf_strip_T3_tonks.strip_tonks

        #"\"How about Miss Granger?\"" if states.cho.ev.inspect_her_body.tonks_doppler_encounter == True and states.cho.ev.inspect_her_body.tonks_succubus_encounter == True:
            #jump cc_pf_strip_T3_tonks.strip_hermione



## Cho Strips ##
label .strip_cho:

    # Check their positions. If Cho stands to the right, she'll get moved to the middle.
    if cho_position == 2: # to the right.
        ton @ hair horny "Move between us, Cho." ("soft", "narrow", "shocked", "L")
        ton @ hair horny "That way the headmaster can see you better." ("base", "narrow", "base", "mid")
        cho @ cheeks blush "Yes, Professor." ("smile", "narrow", "base", "L")
        call hide_characters
        hide screen bld1
        with d5
        pause .2

        # Cho stands in the middle, between Genie and Tonks.
        $ cho_position = 1 # middle.
        $ cho.zorder = 16 # in front of Tonks # Default is 15.
        $ tonks.zorder = 15 # reset to default.
        call cho_chibi("stand", 314, 366, flip=True)
        call ton_chibi("stand", 370, 360, flip=False)
        cho @ cheeks blush "" ("base", "narrow", "base", "mid", xpos=280, ypos="base", flip=True)
        ton @ hair horny "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False)
        with d5
    call ctc


    # Cho is wearing at least one clothing piece:
    if cho.is_any_worn("robe", "top", "bottom", "bra", "panties"):
        pass
    else: # Cho is already naked.
        ton @ hair horny "Well, since you're not really wearing much already..." ("soft", "narrow", "base", "L")
        ton @ hair horny "There isn't that much more for me to help her take off, is there?" ("soft", "narrow", "base", "L")
        cho @ cheeks heavy_blush "..." ("base", "narrow", "base", "downR")
        pause .2
        $ cho.strip("clothes")
        with d3

        call cc_pf_strip_T3_tonks.spank_cho

        jump cc_pf_strip_T3_tonks.strip_check # label checks if both are nude.

    # Remove Top and Bottom.
    if cho.is_any_worn("robe", "top", "bottom"):
        ton @ hair horny "Let me help you get out of these clothes, Miss Chang." ("soft", "narrow", "base", "L")
        cho @ cheeks heavy_blush "Yes, Professor." ("base", "narrow", "base", "down")
        ton @ hair horny "" ("base", "narrow", "base", "down", xpos=300, ypos="base", flip=False, trans=d5) # moves closer to Cho.
        pause .2

        if cho.is_worn("robe"):
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("robe")
            with d3
            pause .5
            cho @ cheeks blush "" ("horny", "narrow", "raised", "down")
            call ctc
        if cho.is_worn("top"):
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("top")
            with d3
            pause .5
            cho @ cheeks blush "" ("horny", "narrow", "raised", "mid")
            pause .8
            nar "Tonks swiftly pulls the girl's top over her chiselled frame."
            pause .2
        if cho.is_worn("bottom"):
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("bottom")
            with d3
            pause .5
            cho @ cheeks blush "" ("horny", "narrow", "base", "down")
            pause .8
            nar "A quick tug by her teacher, and Cho's bottoms slips down her muscular thighs."
            call ctc

    # Remove Bra and Panties.
    if cho.is_any_worn("bra", "panties"):
        ton @ hair horny "I like your underwear Miss Chang... Very cute!" ("soft", "narrow", "base", "L")
        cho @ cheeks heavy_blush "" ("horny", "narrow", "base", "downR")
        ton @ hair horny "" ("soft", "narrow", "base", "L", xpos=300, ypos="base", flip=False, trans=d5) # moves closer to Cho.

        if cho.is_worn("bra"):
            ton @ hair horny "But...{w=0.3} That bra definitely has to come off." ("soft", "narrow", "angry", "down")
            pause .5
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("bra")
            with d3
            pause .5
            cho @ cheeks blush "" ("base", "narrow", "raised", "L")
            pause .8
            nar "Tonks effortlessly removes the bra of her student."
            pause .2
        if cho.is_worn("panties"):
            cho @ cheeks blush "..." ("mad", "narrow", "base", "down")
            ton @ hair horny "Wearing panties is so silly, let's take those off... {heart}" ("crooked_smile", "narrow", "angry", "down")
            pause .5
            play sound "sounds/cloth_sound3.ogg"
            $ cho.strip("panties")
            with d3
            pause .5
            cho @ cheeks heavy_blush "" ("horny", "narrow", "base", "down")
            pause .8
            nar "Eyes fixated onto Cho's lovely Snitch, Tonks slowly pulls the girl's panties down her thighs."
            pause .2


    # Remove all Cho clothes.
    $ cho.strip("clothes")
    with d3
    cho @ cheeks heavy_blush "" ("base", "narrow", "base", "mid")
    call ctc

    ton @ hair horny "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False) # Tonks moves to her original position.
    with d5

    random:
        block:
            ton @ hair horny "Look at all these muscles!" ("horny", "narrow", "raised", "down")
            ton @ hair horny "I mean... I could easily get some muscles as well, but not without cheating..." ("open", "closed", "base", "mid")
            ton @ hair horny "I'm quite impressed, Miss Chang." ("base", "narrow", "base", "L")
            cho @ cheeks blush "Thank you." ("soft", "narrow", "base", "L")
        block:
            ton @ hair horny "You look quite tasty, Miss Chang." ("horny", "narrow", "raised", "down")
            cho @ cheeks heavy_blush "*Ehm*..." ("clench", "narrow", "worried", "down")
            cho @ cheeks heavy_blush "Thanks?" ("soft", "narrow", "worried", "L")
        block:
            ton @ hair horny "Looks like we're done here, Professor." ("horny", "narrow", "raised", "mid")
            gen "Excellent!" ("base", xpos="far_left", ypos="head")
            gen "I do love watching you two." ("grin", xpos="far_left", ypos="head")

    call cc_pf_strip_T3_tonks.spank_cho

    jump cc_pf_strip_T3_tonks.strip_check


## Spank Cho ##
label .spank_cho:
    # Cho should stand next to Genie for this.
    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "-Spank her!-":
            pass
        "-Don't spank her...-":
            return

    call slap_her
    ton @ hair horny "" ("crooked_smile", "narrow", "raised", "L")
    cho @ cheeks heavy_blush "!!!" ("clench", "wide", "base", "mid") # shocked
    cho @ cheeks heavy_blush "Ouch... Professor!" ("silly", "happyCl", "worried", "mid")
    play sound "sounds/giggle2_loud.ogg"
    ton @ cheeks blush hair horny "*Giggles*... {heart}{heart}{heart}" ("silly", "happyCl", "base", "mid")
    ton @ hair horny "..." ("base", "narrow", "base", "mid")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "-Spank her again!-":
            call slap_her
            ton @ hair horny "" ("crooked_smile", "narrow", "base", "mid")
            cho @ cheeks heavy_blush "Professor!" ("clench", "wide", "raised", "mid")
            gen "What? I know you like it." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "I do not..." ("annoyed", "narrow", "angry", "mid")

            menu:
                "-Again!-":
                    pass
            call slap_her
            cho @ cheeks heavy_blush "Sir!" ("clench", "wide", "base", "mid")
            gen "I need to get these cushions ready for your next flight!" ("grin", xpos="far_left", ypos="head")
            gen "Spank them tender, so you're more comfortable on your broom-stick!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "I don't think that will be necessary." ("open", "happyCl", "angry", "mid")

            menu:
                "-Slap it hard!-":
                    pass
            call slap_her
            cho @ cheeks heavy_blush "" ("clench", "wide", "raised", "mid")
            ton @ cheeks blush hair horny "" ("grin", "narrow", "base", "mid")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .3
            call slap_her
            cho @ cheeks heavy_blush "*Owww*..." ("clench", "happyCl", "worried", "mid")
            cho @ cheeks blush "That's enough..." ("annoyed", "narrow", "angry", "mid")
            gen "You'd probably enjoy it more if your teacher were to spank you, wouldn't you?" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("annoyed", "narrow", "base", "L")
            ton @ hair horny "" ("base", "narrow", "base", "L")
            cho @ cheeks heavy_blush "*Ehm*..." ("annoyed", "narrow", "raised", "mid")
            play sound "sounds/giggle2_loud.ogg"
            ton @ cheeks heavy_blush hair horny "*Giggles*... {heart}{heart}{heart}" ("base", "happyCl", "base", "mid")
            ton @ hair horny "I won't be gentle on you either, Miss Chang." ("soft", "narrow", "base", "L")
            cho @ cheeks heavy_blush "..." ("horny", "narrow", "worried", "down")

            return

        "-Ask Tonks to spank her.-":
            gen "Miss Tonks, If you may..." ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "With pleasure!" ("grin", "narrow", "angry", "mid")
            cho @ cheeks heavy_blush "But-- Professor Tonks!" ("clench", "base", "worried", "L")
            ton @ hair horny "Don't worry, [name_cho_tonks]. You'll learn to love it! {heart}" ("horny", "narrow", "base", "L")
            cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "mid")
            ton @ hair horny "Now, turn around for me, please." ("soft", "narrow", "base", "L")
            cho @ cheeks heavy_blush "..." ("clench", "narrow", "worried", "down")
            pause .2

            # Cho turns around.
            call cho_chibi("stand", 325, 366, flip=False)
            call ton_chibi("stand", 360, 360, flip=False)
            ton @ hair horny "" ("base", "narrow", "base", "down", xpos=325, ypos="base", flip=False)
            cho @ cheeks blush "" ("disgust", "narrow", "worried", "down", xpos=235, ypos="base", flip=False, trans=d5)
            pause .5

            call slap_her
            cho @ cheeks blush "" ("normal", "happyCl", "worried", "mid")
            ton @ hair horny "Such a firm ass you have, Miss Chang!" ("horny", "narrow", "raised", "down")
            cho @ cheeks blush "" ("mad", "narrow", "worried", "downR")
            call ctc

            gen "..." ("base", xpos="far_left", ypos="head")
            ton @ hair horny "Lovely indeed... {heart}" ("grin", "narrow", "base", "down")
            gen ".........." ("base", xpos="far_left", ypos="head")
            gen "I don't hear any spanking." ("base", xpos="far_left", ypos="head")
            ton @ hair horny "Don't worry, Sir. I'll get to that eventually... {heart}" ("open", "narrow", "annoyed", "mid")
            gen "Building up the suspense are--" ("base", xpos="far_left", ypos="head")
            call slap_her
            cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "downR")
            ton @ hair horny "You should get a good feel of it first, before you--" ("crooked_smile", "narrow", "annoyed", "down")
            call slap_her
            cho @ cheeks heavy_blush "" ("mad", "wide", "base", "mid")
            ton @ hair angry "" ("horny", "narrow", "angry", "down")
            pause .6
            call slap_her
            pause .3
            call slap_her
            pause .4
            ton @ hair horny "" ("horny", "narrow", "angry", "down")
            cho @ cheeks heavy_blush "Please!" ("clench", "happyCl", "base", "mid")
            ton @ hair horny "What's wrong, Miss Chang?" ("open", "narrow", "angry", "mid")
            ton @ hair horny "You never get this flustered when you get hit by a bludger..." ("open", "narrow", "angry", "down")
            call slap_her
            ton @ hair horny "Surely a bit of a spanking isn't enough for you to..." ("horny", "narrow", "base", "mid")
            cho @ cheeks blush "..." ("clench", "narrow", "worried", "down")
            ton @ hair horny "Ask me nicely, and I'll do it again, [name_cho_tonks]." ("crooked_smile", "narrow", "base", "mid")
            gen "Go on, Cho... Ask your teacher to spank you." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "..." ("disgust", "narrow", "worried", "downR")
            cho @ cheeks heavy_blush "Please spank me again, Professor." ("soft", "narrow", "worried", "R")
            ton @ hair horny "Of course sweetie...{w=0.4} Since you're asking so nicely." ("base", "narrow", "base", "L")
            ton @ hair horny "" ("base", "narrow", "base", "down")
            call slap_her
            cho @ cheeks heavy_blush "" ("angry", "narrow", "worried", "up")
            pause .5
            call slap_her
            pause .4
            call slap_her
            cho @ cheeks heavy_blush "" ("horny", "happyCl", "worried", "mid")
            call ctc

            cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "R")
            ton @ hair horny "*Hmm*..." ("annoyed", "narrow", "shocked", "down")
            ton @ hair horny "A well-behaved girl like you should be rewarded. {heart}" ("crooked_smile", "narrow", "raised", "L")
            ton @ hair horny "Ten points for Ravenclaw, Miss Chang." ("soft", "narrow", "base", "L")
            $ ravenclaw += 10
            cho @ cheeks heavy_blush "Thank you I guess--" ("crooked_smile", "narrow", "worried", "R")
            ton @ hair horny "" ("horny", "narrow", "angry", "down")
            call slap_her
            cho @ cheeks heavy_blush "!!!" ("clench", "wide", "base", "mid")
            cho @ cheeks heavy_blush "Ouch..." ("horny", "narrow", "worried", "R")
            pause .2

            # Cho turns around.
            call cho_chibi("stand", 314, 366, flip=True)
            call ton_chibi("stand", 370, 360, flip=False)
            ton @ hair horny "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False)
            cho @ cheeks blush "" ("annoyed", "narrow", "base", "mid", xpos=280, ypos="base", flip=True, trans=d5)
            pause .8

            return

    return



## Tonks Strips ##
label .strip_tonks:

    # Check their positions. If Tonks stands to the right, she'll get moved to the middle.
    if cho_position == 1: # middle.
        ton @ hair horny "Cho, would you mind if I stood between you two?" ("open", "narrow", "base", "L")
        ton @ hair horny "I'd like to give the headmaster a better view of my body." ("base", "narrow", "base", "mid")
        cho @ cheeks blush "Not at all, Professor." ("smile", "narrow", "base", "L")
        ton @ hair horny "Thank you, [name_cho_tonks]." ("soft", "narrow", "shocked", "L")
        call hide_characters
        hide screen bld1
        with d5
        pause .2

        # Tonks stands in the middle, between Genie and Cho.
        $ cho_position = 2 # to the right.
        $ tonks_chibi.zorder = 2 # default is 3
        $ cho.zorder = 15 # reset to default.
        $ tonks.zorder = 16 # in front of Cho # Default is 15.
        call cho_chibi("stand", 370, 360, flip=False)
        call ton_chibi("stand", 320, 360, flip=True)
        with d3
        pause .5

        cho @ cheeks blush "" ("base", "narrow", "base", "mid", xpos=315, ypos="base", flip=False)
        ton @ hair horny "" ("base", "narrow", "base", "mid", xpos=280, ypos="base", flip=True)
        with d5
    call ctc


    # Tonks is wearing at least one clothing piece:
    if tonks.is_worn("robe") or tonks.is_worn("top") or tonks.is_worn("bottom") or tonks.is_worn("bra") or tonks.is_worn("panties"):
        cho @ cheeks blush "..." ("horny", "narrow", "base", "L")
        if tonks.is_worn("top"):
            ton @ hair horny "You don't mind if Miss Chang helps me undress, do you, Professor?" ("horny", "wink", "base", "mid")
            gen "Of course not!" ("grin", xpos="far_left", ypos="head")
        else:
            ton @ hair horny "Just enjoy the show, Professor..." ("horny", "wink", "base", "mid")
        pass
    else: # Tonks is already naked.
        ton @ hair horny "Professor... It seems like I'm not wearing much..." ("soft", "narrow", "base", "L")
        ton @ hair horny "How shameful of me... Am I to get detention now?" ("horny", "narrow", "base", "mid")
        gen "Damn right you are!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks heavy_blush "..." ("base", "narrow", "base", "downR")
        pause .2
        $ tonks.strip("clothes")
        with d3

        call cc_pf_strip_T3_tonks.spank_tonks

        jump cc_pf_strip_T3_tonks.strip_check # label checks if both are nude.

    # Remove Top and Bottom.
    if tonks.is_worn("robe") or tonks.is_worn("top") or tonks.is_worn("bottom"):
        ton @ hair horny "Help me get out of these clothes, Miss Chang." ("soft", "narrow", "base", "L")
        cho @ cheeks blush "Yes, Professor." ("soft", "narrow", "base", "down")
        cho @ cheeks blush "" ("horny", "narrow", "base", "down", xpos=315, ypos="base", flip=False, trans=d5) # Cho moves closer to Tonks.
        pause .2

        if tonks.is_worn("robe"):
            play sound "sounds/cloth_sound3.ogg"
            $ tonks.strip("robe")
            with d3
            pause .5
            ton @ hair horny "" ("horny", "narrow", "raised", "down")
            call ctc
        if tonks.is_worn("top"):
            play sound "sounds/cloth_sound3.ogg"
            $ tonks.strip("top")
            with d3
            pause .5
            ton @ hair horny "" ("horny", "narrow", "raised", "mid")
            pause .8
            nar "Cho eagerly helps her teacher take off her top."
            pause .2
        if tonks.is_worn("bottom"):
            ton @ hair horny "Remember... Always take your time when undressing in front of somebody." ("soft", "narrow", "base", "L")
            ton @ hair horny "" ("base", "narrow", "base", "mid")
            nar "Slowly, and with gracile movements, Tonks takes off her bottom piece of clothing."
            play sound "sounds/cloth_sound3.ogg"
            $ tonks.strip("bottom")
            with hpunch
            pause .5
            ton @ cheeks blush hair horny "" ("horny", "narrow", "raised", "mid")
            pause .8
            nar "And then flicks it out of sight with one swift motion."
            call ctc

    # Remove Bra and Panties.
    if tonks.is_worn("bra") or tonks.is_worn("panties"):
        ton @ hair horny "*Hmm*... It's been a while since I had to remove underwear." ("annoyed", "narrow", "base", "down")
        ton @ hair horny "Help me take them off, [name_cho_tonks]." ("base", "narrow", "base", "down")
        cho @ cheeks blush "Of course..." ("smile", "narrow", "base", "down")
        cho @ cheeks blush "" ("horny", "narrow", "base", "down", xpos=315, ypos="base", flip=False, trans=d5) # Cho moves closer to Tonks.

        if tonks.is_worn("bra"):
            ton @ hair horny "Let's get these tits out already!" ("base", "narrow", "angry", "mid")
            pause .5
            play sound "sounds/cloth_sound3.ogg"
            $ tonks.strip("bra")
            with d3
            pause .5
            ton @ hair horny "" ("base", "narrow", "base", "mid")
            pause .8
            nar "Tonks bares her impressive bosom for you both."
            pause .2
        if tonks.is_worn("panties"):
            ton @ hair horny "Oh my... what happened to my panties..." ("soft", "narrow", "base", "down")
            ton @ hair horny "I can't believe how wet they got!" ("clench", "narrow", "shocked", "down")
            pause .5
            play sound "sounds/cloth_sound3.ogg"
            $ tonks.strip("panties")
            with d3
            pause .5
            ton @ hair horny "" ("horny", "narrow", "angry", "mid")
            pause .8
            nar "Without much hesitation, Tonks panties are swiftly flung out of sight and out of mind."
            pause .2

    # Remove all Cho clothes.
    ton @ hair horny "" ("base", "narrow", "base", "mid")
    $ tonks.strip("clothes")
    with d3
    call ctc

    cho @ cheeks blush "" ("base", "narrow", "base", "mid", xpos=315, ypos="base", flip=False) # Cho moves to her original position.
    with d5

    random:
        block:
            ton @ hair horny "How immoral for a teacher to do this sort of thing in front of a student..." ("open", "closed", "annoyed", "mid")
            ton @ hair horny "You aren't going to report me for my wanton behaviour, are you, Miss Chang?" ("soft", "narrow", "annoyed", "L")
            cho @ cheeks heavy_blush "No. Of course not, Professor." ("base", "narrow", "base", "L")
            ton @ hair horny "Good girl." ("horny", "narrow", "base", "L")
            cho @ cheeks blush "..." ("angry", "narrow", "base", "down")
        block:
            ton @ hair horny "Are you enjoying yourself, Professor?" ("open", "narrow", "raised", "mid")
            gen "With those tits in front of me? Always!" ("grin", xpos="far_left", ypos="head")
        block:
            ton @ hair horny "Did you like that, Professor?" ("horny", "narrow", "raised", "mid")
            gen "I bloody love it!" ("grin", xpos="far_left", ypos="head")

    call cc_pf_strip_T3_tonks.spank_tonks

    jump cc_pf_strip_T3_tonks.strip_check


label .spank_tonks:
    # Tonks should stand next to Genie for this.
    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "-Spank her!-":
            pass
        "-Don't spank her...-":
            return

    call slap_her
    ton @ cheeks heavy_blush hair scared "!!!" ("clench", "shocked", "base", "stare") # shocked
    ton @ cheeks blush hair horny "*Mmm*... You're so naughty, Professor!" ("silly", "narrow", "angry", "mid")
    ton @ cheeks blush hair horny "Right in front of a student and everything..." ("base", "narrow", "base", "mid")
    call slap_her
    ton @ cheeks blush hair horny "Ouch... {heart}{heart}{heart}" ("silly", "happyCl", "base", "mid")
    cho @ cheeks blush "..." ("grin", "narrow", "base", "mid")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "-Spank her again!-":
            call slap_her
            ton @ cheeks heavy_blush hair horny "*Mmm*... Spank me, Professor!" ("horny", "narrow", "angry", "mid")

            menu:
                "-Again!-":
                    pass
            call slap_her
            ton @ cheeks heavy_blush hair horny "Not so rough, Sir! {heart}" ("soft", "narrow", "base", "mid")
            cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "down") # blushing #lip bite #looking away

            menu:
                "-Slap it hard!-":
                    pass
            call slap_her
            ton @ cheeks heavy_blush hair scared "" ("clench", "base", "shocked", "ahegao")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .3
            call slap_her
            cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "mid")
            ton @ cheeks heavy_blush hair horny "*Hngh*..." ("upset", "narrow", "base", "ahegao")
            ton @ cheeks heavy_blush hair horny "Thank you, Professor. {heart}{heart}{heart}" ("soft", "narrow", "worried", "mid")
            gen "You're welcome." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "downR")

            return

        "-Ask Cho to spank her.-":
            gen "Miss Chang, would you be so kind and slap your teacher's ass for me?" ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "" ("base", "narrow", "base", "mid")
            cho @ cheeks blush "Yes, Sir." ("open", "narrow", "angry", "mid")
            ton @ hair horny "Do it, [name_cho_tonks]!" ("base", "narrow", "base", "L")
            pause .2

            # Tonks turns around.
            call ton_chibi(flip=False)
            ton @ cheeks blush hair horny "" ("base", "base", "base", "mid", xpos=215, ypos="base", flip=False, trans=d5)
            pause .5

            ton @ cheeks blush hair horny "Slap this naughty teacher's ass!" ("crooked_smile", "narrow", "angry", "R")
            cho @ cheeks blush "..." ("base", "narrow", "angry", "down")
            call slap_her
            ton @ hair horny "Surely you can do better than that, Cho." ("soft", "narrow", "base", "downR")
            cho @ cheeks blush "" ("annoyed", "narrow", "angry", "down")
            call slap_her
            ton @ cheeks blush hair horny "*Hngh*..." ("crooked_smile", "narrow", "base", "mid")
            ton @ hair angry "Do I have to fetch a beaters bat, so you can hit it properly, Miss Chang?" ("open", "narrow", "annoyed", "downR")
            ton @ hair angry "I thought I asked you to slap it harder!" ("scream", "narrow", "angry", "downR")
            cho @ cheeks blush "" ("clench", "narrow", "angry", "down")
            call slap_her
            ton @ hair scared "" ("mad", "wide", "shocked", "stare")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .2
            call slap_her
            ton @ cheeks heavy_blush hair horny "!!!" ("clench", "narrow", "base", "ahegao")
            cho @ cheeks blush "Good enough for you, Professor?" ("open", "narrow", "angry", "L")
            ton @ hair horny "*Ah*...{w=0.4} Yes, [name_cho_tonks]... I'd say that was quite--" ("open", "narrow", "worried", "R")
            cho @ cheeks blush "" ("annoyed", "narrow", "angry", "down")
            call slap_her
            ton @ hair scared "" ("clench", "narrow", "base", "ahegao")
            pause .5
            call slap_her
            pause .3
            call slap_her
            pause .2
            call slap_her
            ton @ cheeks heavy_blush hair horny "" ("horny", "narrow", "base", "ahegao")
            call ctc

            gen "That's enough." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Oh wow, it's really red now..." ("grin", "narrow", "base", "down")
            ton @ cheeks heavy_blush hair horny "Very good, Miss Chang. {heart}" ("horny", "narrow", "worried", "R")
            pause .2

            # Tonks turns around.
            call ton_chibi(flip=True)
            ton @ cheeks heavy_blush hair horny "" ("base", "base", "base", "mid", xpos=280, ypos="base", flip=True, trans=dissolve)
            pause .8

            ton @ cheeks heavy_blush hair horny "Ten points for Ravenclaw." ("soft", "narrow", "base", "L")
            $ ravenclaw += 10
            ton @ cheeks heavy_blush hair horny "For this thorough ass spanking!" ("horny", "narrow", "base", "mid")
            cho "Thank you, Professor Tonks." ("crooked_smile", "narrow", "base", "down")

            return


# Check if Tonks and Cho are naked. Proceed to transformation section if they are.
label .strip_check:
    # Cho is wearing at least one clothing piece:
    if cho.is_any_worn("robe", "top", "bottom", "bra", "panties"):
        jump cc_pf_strip_T3_tonks.strip_cho
    # Tonks is wearing at least one clothing piece:
    elif tonks.is_any_worn("robe", "top", "bottom", "bra", "panties"):
        jump cc_pf_strip_T3_tonks.strip_tonks
    # Both are naked; Proceed with event.
    else:
        jump cc_pf_strip_T3_tonks.transformations



## Transformations ##
label .transformations:
    # Intro Event 1 - Doppler or Succubus choice.
    # Intro Event 2 - Doppler or Succubus choice.
    # Repeatable Event - Transformations.

    $ cho.zorder = 16 # in front of Tonks # Default is 15.
    $ tonks.zorder = 15 # reset to default.
    call cho_chibi("stand", 314, 366, flip=True)
    call ton_chibi("stand", 370, 360, flip=False)
    ton @ hair horny "" ("base", "narrow", "base", "L", xpos=345, ypos="base", flip=False)
    cho @ cheeks blush "" ("grin", "base", "base", "L", xpos=280, ypos="base", flip=True)
    with d5

    ## Intro Events 1 and 2:
    if states.cho.ev.inspect_her_body.tonks_doppler_encounter == False or states.cho.ev.inspect_her_body.tonks_succubus_encounter == False:

        # Ask Tonks if she's a Doppler or a Succubus.
        # After asking her both questions, the next time you do the event she'll do some tranformations.

        if states.cho.ev.inspect_her_body.tonks_doppler_encounter == True or states.cho.ev.inspect_her_body.tonks_succubus_encounter == True: # You have asked her if she was one of these before.
            ton "You're getting quite good at this, Miss Chang." ("base", "narrow", "base", "L")
            cho @ cheeks blush "Thank you, Professor." ("base", "narrow", "base", "L")
            gen "She's learning from the best." ("base", xpos="far_left", ypos="head")
            if states.cho.ev.inspect_her_body.tonks_succubus_encounter :
                gen "Who'd be better suited to teach her how to entice a man than a semen stealing she-devil!" ("base", xpos="far_left", ypos="head")
                ton "Please, Professor. I've already told you I'm not a Succubus..." ("open", "closed", "annoyed", "mid")
            else: # states.cho.ev.inspect_her_body.tonks_succubus_encounter
                gen "Who'd be better suited to teach her how to entice a man than a shapeshifter!" ("base", xpos="far_left", ypos="head")
                ton "Please, Professor. I've already told you I'm not this... doppler creature you spoke of." ("open", "closed", "annoyed", "mid")
            ton "" ("annoyed", "narrow", "annoyed", "mid")
            gen "You can never be a hundred percent sure..." ("base", xpos="far_left", ypos="head")
            cho "..." ("quiver", "narrow", "raised", "mid")
            gen "My theories have yet to be completely debunked!" ("grin", xpos="far_left", ypos="head")
            ton "Seriously?!" ("upset", "base", "raised", "mid")
            ton "Alright then... What do you want me to do to convince you this time?" ("soft", "narrow", "base", "mid")
            gen "Prove to me that you're not--" ("base", xpos="far_left", ypos="head")
            pass

        else:
            ton "*Hmm*... not so nervous around me anymore, are you, Cho?" ("crooked_smile", "narrow", "base", "L")
            cho @ cheeks blush "Oh, I guess not. It seems like I got used to it..." ("crooked_smile", "narrow", "worried", "R")
            cho @ cheeks blush "It's fun doing this sort of thing at school... I'm quite enjoying it." ("smile", "narrow", "base", "downR")
            ton @ hair horny "Well, there's somebody who enjoys it even more than we do, isn't that right, Professor?" ("horny", "base", "raised", "mid")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            ton "Professor?" ("soft", "narrow", "base", "mid")
            cho @ cheeks blush "" ("annoyed", "narrow", "base", "mid")
            ton "Something on your mind?" ("annoyed", "base", "raised", "mid")
            gen "Actually, there is..." ("base", xpos="far_left", ypos="head")
            gen "Since your abilities are so rare... Can we be certain that you are, in fact, human?" ("base", xpos="far_left", ypos="head")
            ton "Don't be silly..." ("clench", "base", "shocked", "mid")
            gen "You {b}are{/b} human, are you?" ("base", xpos="far_left", ypos="head")
            ton "Of course I am, Professor!" ("open", "closed", "annoyed", "mid")
            ton "What else am I supposed to be?" ("open", "narrow", "raised", "mid")
            pass

        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"A Doppler!\"" if states.cho.ev.inspect_her_body.tonks_doppler_encounter == False:
                jump .doppler_E1
            "\"A Succubus!\"" if states.cho.ev.inspect_her_body.tonks_succubus_encounter == False:
                jump .succubus_E1


    ## Repeatable ##
    else:
        pass

    call ctc

    gen "Tonks, would you mind showing us your little trick again?" ("grin", xpos="far_left", ypos="head")
    ton "Of course. What's it gonna be, Professor?" ("grin", "base", "base", "mid")
    ton "Remember, I can transform into anything... Or anyone." ("soft", "narrow", "base", "mid") # suggestive
    cho @ cheeks blush "..." ("horny", "narrow", "base", "down")
    gen "*Hmm*... Who do I want you to turn into... Let me think." ("base", xpos="far_left", ypos="head")

    menu:
        gen "Yes, I want you to shapeshift into--" ("grin", xpos="far_left", ypos="head")
        "\"Hermione!\"":
            jump cc_pf_strip_T3_tonks.hermione_E1
        "\"A Succubus!\"":
            jump cc_pf_strip_T3_tonks.succubus_E2



## Doppler Event 1 ##
label cc_pf_strip_T3_tonks.doppler_E1:
    if states.cho.ev.inspect_her_body.tonks_doppler_encounter == False:
        # Intro
        ton "*Hmmm?*... What's a \"doppler\"?" ("upset", "base", "base", "mid")
        gen "What do you mean, what's a doppler?!" ("base", xpos="far_left", ypos="head")
        gen "Aren't you part of the magical animal control... or whatever." ("angry", xpos="far_left", ypos="head")
        ton "The Auror division does a lot more than \"animal control\"..." ("open", "narrow", "base", "mid")
        gen "But you're incapable of identifying a doppler?" ("angry", xpos="far_left", ypos="head")
        ton "I guess... This is the first time I'm hearing of such a creature." ("annoyed", "base", "raised", "mid")
        cho "I haven't heard of them either, Sir." ("soft", "narrow", "base", "mid")
        gen "What sort of magic school are we running here? Aren't you getting taught any Witcher lore?" ("base", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "base", "base", "mid")
        ton "Very well, Professor. Why don't you tell us about them?" ("upset", "narrow", "base", "mid")
        gen "Oh, there's nobody better suited to do that than me, I'll have you know!" ("grin", xpos="far_left", ypos="head")
        gen "After all, I know a lot about the Witcher just from playing the games alone!" ("grin", xpos="far_left", ypos="head")
        gen "(Truth be told, I skipped the first two, but they don't need to know that...)" ("base", xpos="far_left", ypos="head")
        cho "What kind of \"games\" is he talking about, Professor?" ("soft", "base", "worried", "L") # looking at Tonks. Small text
        ton "I haven't the foggiest..." ("mad", "base", "raised", "L") # looking back. Small text

    $ states.cho.ev.inspect_her_body.tonks_doppler_encounter = True
    gen "Dopplers are hideous creatures, you see... Both in character, and in appearance." ("angry", xpos="far_left", ypos="head")
    cho "" ("annoyed", "base", "base", "mid")
    ton "" ("upset", "narrow", "base", "mid")
    gen "They often abuse their ability for selfish gains, and manipulate people into thinking they're somebody else entirely." ("base", xpos="far_left", ypos="head")
    cho "That does sound quite suspicious, Professor..." ("open", "narrow", "angry", "mid")
    cho @ cheeks blush "After all, she's been abusing her powers to flaunt my bum at people!" ("annoyed", "narrow", "angry", "mid")
    gen "That's true!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Surely you can't blame me for that... As I said, it wasn't anything they hadn't seen before." ("soft", "base", "base", "R")
    cho @ cheeks heavy_blush "But-- Professor!" ("annoyed", "narrow", "angry", "L")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush hair horny "I'm not doing anything harmful, I promise." ("upset", "happyCl", "worried", "mid")
    cho @ cheeks blush "..." ("annoyed", "narrow", "angry", "mid") # annoyed

    ton @ hair horny "So, what other \"Evidence\" do you have to further prove this theory?" ("soft", "narrow", "base", "mid") #Amused
    gen "Well, there's a big reason why Dopplers indulge themselves when they get the chance to." ("base", xpos="far_left", ypos="head")
    gen "Since they're incredibly ugly creatures, it wouldn't surprise me in the slightest that they'd change their appearance into a highly attractive woman when given the chance." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("annoyed", "base", "base", "L")
    ton @ hair horny "" ("annoyed", "base", "base", "mid")
    gen "Miss Tonks, your appearance, it's almost too perfect..." ("base", xpos="far_left", ypos="head")
    gen "You didn't find some smoking hot woman in a magazine, did you?" ("base", xpos="far_left", ypos="head")
    gen "We all know those are highly edited..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "So I'm smoking hot, huh?" ("horny", "narrow", "base", "mid")
    ton @ hair horny "You flatter me, but no... I've always looked like this." ("base", "happyCl", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("annoyed", "base", "base", "mid") # blushing

    gen "You can count yourself lucky that I haven't seen any bounties for a Doppler..." ("base", xpos="far_left", ypos="head")
    gen "So, doppler or not..." ("base", xpos="far_left", ypos="head")
    gen "You're off the hook for now." ("base", xpos="far_left", ypos="head")
    ton "Well, I'm glad we cleared that up..." ("base", "narrow", "base", "mid")
    cho @ cheeks blush "" ("annoyed", "base", "base", "mid")
    ton "My ability is perfectly harmless, Professor." ("crooked_smile", "base", "base", "mid")
    gen "You may say that, but we all know shape-shifting is the source of all kinds of evil sorcery!" ("angry", xpos="far_left", ypos="head")
    ton "No it's not..." ("open", "closed", "annoyed", "mid")
    gen "The last thing we need at this school is a rogue shapeshifter -- abusive of its powers..." ("angry", xpos="far_left", ypos="head")
    ton @ hair horny "..." ("upset", "base", "base", "mid")

    gen "Anyway... Promise me you won't start murdering people and steal their identities." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("angry", "base", "raised", "mid")
    ton @ hair scared "What?! How could you even suggest that I would--" ("clench", "shocked", "shocked", "mid") # shocked
    gen "Identity theft is not a joke, Tonks! Millions of families suffer every year!" ("angry", xpos="far_left", ypos="head")
    ton "Yikes! Of course I won't do that, Professor!" ("clench", "happyCl", "base", "mid")
    gen "Good." ("base", xpos="far_left", ypos="head")
    ton "..." ("upset", "base", "worried", "mid")
    cho "" ("annoyed", "base", "base", "mid")
    gen "How come you're the only one that can shapeshift?" ("base", xpos="far_left", ypos="head")
    ton "It's just very uncommon." ("open", "narrow", "raised", "down")
    ton "You can't fault me for having it... I was born with it." ("annoyed", "base", "base", "mid")
    gen "Very well then, I shall believe that you're not a doppler..." ("base", xpos="far_left", ypos="head")
    gen "(For now...)" ("base", xpos="far_left", ypos="head")
    ton "Glad to hear it." ("mad", "base", "base", "mid")
    cho "..." ("soft", "narrow", "worried", "L")
    ton "Anyhow, it's getting quite late, Professor." ("soft", "narrow", "base", "L")

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event


## Succubus Event 1 ##
label cc_pf_strip_T3_tonks.succubus_E1:
    if states.cho.ev.inspect_her_body.tonks_succubus_encounter == False:
        # Intro
        ton "*snort!*... For real?" ("crooked_smile", "happyCl", "shocked", "mid")
        cho "Oh, I've heard of those, Professor!" ("grin", "happyCl", "base", "mid")
        cho "They're demons in female form, that can visit you in your dreams and murder you!" ("soft", "narrow", "angry", "mid")
        ton "Very good, Miss Chang..." ("crooked_smile", "base", "base", "L")
        ton "Ten points for Ravenclaw!" ("soft", "narrow", "base", "L")
        $ ravenclaw += 10
        cho @ cheeks blush "Thank you." ("smile", "narrow", "base", "downR") # happy

    $ states.cho.ev.inspect_her_body.tonks_succubus_encounter = True
    ton "I mean... I'm quite flattered, Professor..." ("open", "narrow", "raised", "mid")
    ton @ hair horny "Who doesn't want to be compared to a demonic, sex-driven temptress!" ("soft", "narrow", "base", "mid")
    cho @ cheeks blush "" ("annoyed", "base", "base", "mid")
    gen "I knew it! You're a Succubus!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("annoyed", "base", "raised", "L")
    ton "No I'm not, silly!" ("open", "closed", "base", "mid")
    ton @ hair horny "..." ("annoyed", "base", "shocked", "L") # thinks
    ton @ hair horny "Well, I do have similar shapeshifting abilities, that's true..." ("soft", "base", "base", "down")
    ton @ hair horny "And share some of their more raunchy characteristics..." ("crooked_smile", "happyCl", "base", "mid")
    gen "Not to mention a banger body!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Obviously." ("soft", "narrow", "base", "mid")
    cho @ cheeks blush "..." ("horny", "narrow", "base", "L") # blushing
    ton @ hair horny "I may also act like one on the occasion..." ("open", "base", "base", "R")

    # TODO: v v v Added this bit of writing. Needs review
    gen "But you're still denying that you're an alluring sex-demon, even after that last demonstration?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "I might have some unusual talents, that's all..." ("open", "base", "base", "R")
    ton @ hair horny "Why are you so scared of them anyway?" ("open", "narrow", "base", "mid")
    ton @ hair horny "What's the worst a succubus could do to you?" ("horny", "narrow", "base", "mid")
    gen "Do I really have to tell the two of you of what they do?" ("angry", xpos="far_left", ypos="head")
    gen "I won't let any demon suck the life-blood out of my penis!" ("angry", xpos="far_left", ypos="head")
    ton @ hair horny "" ("normal", "base", "base", "mid")
    cho "What?!" ("clench", "base", "base", "mid") # bit shocked.
    ton @ hair horny "Well, if I was one, I promise you I wouldn't do that..." ("mad", "narrow", "base", "mid")
    ton @ hair horny "Not as long as there's plenty of other essence to be gathered." ("horny", "narrow", "angry", "mid")
    cho "Professors?!" ("mad", "narrow", "base", "downR") # uncomfortable
    gen "Then I better not run out of essence!" ("grin", xpos="far_left", ypos="head")
    cho "..." ("disgust", "narrow", "base", "mid")
    gen "Thought you could trick me, you semen loving sex-demon!" ("grin", xpos="far_left", ypos="head")
    # TODO: ^ ^ ^ Added this bit of writing. Needs review

    ton @ hair horny "I'm still human, and not a sex-demon...{w=0.5} Believe it or not." ("open", "narrow", "raised", "mid")
    gen "If you say so..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "If you'd met one before, you'd know the difference between me and a succubus right away..." ("base", "narrow", "base", "mid")
    ton @ hair horny "They are quite relentless when it comes to sex, you know. -- Even more so than I am!" ("horny", "narrow", "annoyed", "mid")
    cho "You have met a Succubus, Professor? But I thought they're extremely dangerous." ("mad", "base", "base", "mid")
    ton @ hair horny "Oh yes! You have to be extremely cautious around them..." ("soft", "base", "base", "L")
    gen "Don't tell me you--" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "Who do you think you're talking to, Professor.{w=0.5} Of course I did." ("base", "narrow", "base", "mid") # horny, confident
    cho @ cheeks heavy_blush "No way!" ("horny", "base", "base", "L")
    ton @ hair horny "It was part of an auror job, obviously. Maybe I'll tell you about it some time." ("crooked_smile", "base", "base", "mid")
    cho "Yes! I want to hear it!" ("grin", "base", "base", "mid")
    ton @ hair horny "Are you sure you'd want that, honey?" ("soft", "narrow", "base", "L")
    ton @ hair horny "It's quite the filthy story... You don't walk away from a Succubus unscarred unless you can impress her!" ("horny", "narrow", "raised", "mid") # horny
    cho @ cheeks heavy_blush "*Uhm*..." ("disgust", "narrow", "worried", "downR")
    play sound "sounds/gulp.ogg"
    gen "*gulp*..." ("angry", xpos="far_left", ypos="head") # sound
    ton @ hair horny "Of course I could tone it down for you guys." ("base", "happyCl", "base", "mid")
    gen "No, please. We'd love to hear the full story!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("horny", "narrow", "base", "mid")
    ton "Next time. I promise." ("base", "narrow", "base", "mid")
    ton "Anyhow, it's getting quite late, Professor." ("soft", "narrow", "base", "L")

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event


## Succubus Event 2 ##
label .succubus_E2:
    ton "You want me to shape-shift into a Succubus?" ("base", "narrow", "base", "mid")
    cho "" ("horny", "narrow", "base", "L")
    gen "Hell yeah! I do love me some cosplay!" ("grin", xpos="far_left", ypos="head")
    ton "It's not..." ("open", "base", "shocked", "R")
    ton "Very well then..." ("open", "closed", "base", "mid")

    # Tonks transforms into a Succubus
    stop music fadeout 0.5
    cho "" ("mad", "narrow", "base", "down", xpos=265, ypos="base", flip=True) # bit more to the left
    ton "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False) # bit more to the right
    with fade
    pause .5

    play sound "sounds/magic3.ogg"
    $ tonks.equip(ton_outfit_succubus)
    ton "" ("horny", "narrow", "base", "mid", trans=flash)
    call ctc

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    ton "{heart}{heart}{heart}"
    gen "Marvellous!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("horny", "narrow", "raised", "down") # blush
    ton @ hair horny "*Giggles*" ("horny", "narrow", "raised", "L") #sound
    ton @ hair horny "What do you think?" ("grin", "narrow", "base", "mid")
    ton @ hair horny "Do you like it?" ("horny", "narrow", "annoyed", "down")
    cho @ cheeks blush "..." ("horny", "narrow", "worried", "down")
    pause .8
    ton @ hair horny "Miss Chang?" ("soft", "narrow", "base", "L")
    cho @ cheeks heavy_blush "Oh! Yes... Very impressive, Professor!" ("soft", "narrow", "worried", "L")
    ton @ hair horny "I don't think my skin tone is quite right... I believe they're usually more devilish looking." ("upset", "narrow", "base", "down")
    gen "I can already feel my balls retract by fear." ("angry", xpos="far_left", ypos="head")
    ton @ hair horny "" ("base", "narrow", "base", "mid")
    cho "Your... What, Sir?" ("clench", "wide", "base", "mid") #wide eyed
    ton @ hair horny "Don't worry, Miss Chang... Unless you're in a state of high arousal then you have nothing to worry about." ("crooked_smile", "narrow", "base", "L")
    cho @ cheeks blush "*Ehm*... If you say so, Professor." ("normal", "happyCl", "worried", "mid")
    ton @ hair angry "Now the Professor on the other hand..." ("mad", "narrow", "angry", "mid")
    cho @ cheeks blush "" ("mad", "base", "raised", "mid")
    ton @ hair angry "He can call himself very lucky that I'm not a real Succubus." ("soft", "narrow", "base", "mid")
    gen "I'm not ruling out the possibility..." ("base", xpos="far_left", ypos="head")
    ton @ hair angry "*Tsk*..." ("upset", "narrow", "base", "mid")
    gen "Though I must say you're much more attractive than the last demon who visited me..." ("base", xpos="far_left", ypos="head")
    ton @ hair angry "" ("annoyed", "narrow", "raised", "mid")
    cho "You were visited by a demon, Professor?" ("soft", "narrow", "base", "mid")
    gen "Yes... Although, it was just your regular sleep paralysis demon." ("base", xpos="far_left", ypos="head")
    ton @ hair angry "" ("base", "narrow", "base", "mid")
    cho "Oh..." ("disgust", "narrow", "base", "down")
    gen "A rather horrifying looking one at that... Not sexy in the slightest!" ("angry", xpos="far_left", ypos="head")
    gen "Mating with it proved itself to be quite difficult..." ("grin", xpos="far_left", ypos="head")
    ton @ hair angry "Of course you did..." ("horny", "narrow", "angry", "mid")
    cho "You... Wait, did you say {b}it{/b}, Sir?" ("open", "base", "base", "mid") #wide eyed
    gen "*Ahem*... So, how does one summon a Succubus anyway?" ("base", xpos="far_left", ypos="head")
    gen "I'm sure you're an expert in the subject, Miss Tonks." ("grin", xpos="far_left", ypos="head")
    cho "{b}It{/b}, sir?!" ("mad", "narrow", "raised", "mid")
    ton "*Hmm*... I wouldn't call myself an expert..." ("base", "narrow", "base", "mid")
    cho "But what about your Auror Training professor?" ("annoyed", "narrow", "base", "L") #annoyed pout
    ton "" ("base", "narrow", "base", "L") #Glances at Cho
    cho @ cheeks blush "..." ("base", "narrow", "base", "L") #embarrased
    ton "Now I know I'm your Teacher, Miss Chang, but that doesn't mean I'm at an expert level of every subject before doing proper research..." ("open", "narrow", "raised", "L")
    cho @ cheeks blush "Oh... Of course, Professor... I didn't mean to--" ("mad", "narrow", "worried", "down")
    ton "Whilst we did cover Succubi during our training, the subject of summoning wasn't very in depth..." ("soft", "narrow", "raised", "L")
    cho @ cheeks blush "" ("base", "narrow", "worried", "L")
    ton "We mostly learned how to easily recognize and how to... Deal with various magical beings." ("open", "closed", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    ton "That said..." ("grin", "narrow", "base", "mid")
    ton "What I do know is that they usually come off as quite erratic and spontaneous." ("soft", "narrow", "shocked", "mid")
    ton "In most cases you'd only encounter them if {b}they{/b} want you to..." ("base", "narrow", "base", "mid")
    ton "So summoning one would be quite difficult." ("base", "narrow", "base", "L")
    gen "Well... Luckily, I have the ability to summon you any time I want!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmmm*... Be careful what you wish for, Professor..." ("horny", "narrow", "base", "mid")
    ton @ hair angry "I can be just as dangerous and seductive... {heart}" ("horny", "narrow", "angry", "mid")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "mid")
    gen "See that hungry look in her eyes, Cho?" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "L")
    gen "This Succubus is out to steal all my semen!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Oh, don't tempt me, Professor..." ("crooked_smile", "narrow", "angry", "mid")
    cho @ cheeks blush "..." ("base", "narrow", "worried", "down") # embarrassed

    #Tonks succubus encounter story
    cho @ cheeks blush "*Ehm*...{w=0.5} So, did you actually confront a real Succubus, Professor?" ("soft", "narrow", "base", "L")
    ton @ hair horny "Oh, Yes indeed, Miss Chang!" ("base", "happyCl", "base", "mid")
    ton "It happened during my first year of Auror training, when I was still a complete novice." ("open", "narrow", "raised", "L")
    ton "We were tracked down by one during a scouting mission... Unbeknownst to us, of course." ("crooked_smile", "narrow", "base", "mid")
    cho @ cheeks blush "She tracked you down?" ("mad", "base", "raised", "L")
    ton "Yes... They can sense the arousal of humans from miles away... Even further, if they haven't had any relief for some time." ("base", "narrow", "base", "L")
    gen "Well, who can blame your partner with you around?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "*Giggles*" ("base", "happyCl", "base", "mid") #sound
    ton @ hair horny "Oh silly... She was after me, of course!" ("soft", "narrow", "base", "mid")
    cho @ cheeks blush "No way!?" ("horny", "narrow", "raised", "L")
    ton @ hair horny "I know what you're going to say, Professor... And yes... They don't usually go after females." ("open", "closed", "base", "mid")
    cho @ cheeks blush "But she still came after you?" ("soft", "narrow", "raised", "L")
    cho @ cheeks blush "When did you and your partner notice her?" ("mad", "narrow", "base", "L")
    ton @ hair horny "Well... My partner didn't notice her exactly... I might've wandered a bit further away from our camp than I should have..." ("soft", "narrow", "base", "downR")
    ton @ cheeks blush hair horny "You know... To get some privacy." ("crooked_smile", "narrow", "base", "mid")
    ton @ hair horny "She must've taken some great caution to be able to sneak up on me, but after a while of... *Ehm*..." ("clench", "narrow", "base", "L")
    ton @ hair horny "After some time, I noticed her movements among the bushes." ("open", "closed", "base", "mid")
    ton @ hair horny "Once I noticed her presence, there was no doubt in my mind why she had sneaked up on me..." ("grin", "narrow", "base", "mid")
    gen "Let me guess... She was--" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "She was going full force, pleasuring herself... Not even noticing that I had stopped and spotted her!" ("grin", "narrow", "angry", "mid")
    cho "Stopped what?" ("annoyed", "base", "raised", "mid")
    gen "Shush, Miss Chang... Don't interrupt the story!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Of course I had to be a hundred percent sure what creature she was, so I went to take out my wand to make some light, but..." ("base", "narrow", "base", "L")
    ton @ hair angry "Before I knew it, she had flown right up next to me, grabbing my wrists." ("open", "narrow", "angry", "mid")
    cho "And then you used your auror training to fight her!" ("grin", "narrow", "angry", "L")
    play sound "sounds/giggle2_loud.ogg"
    ton @ hair horny "*Giggles*...{w=0.4} No, we made out instead." ("horny", "narrow", "raised", "L") #sound
    cho "You...{w} Made out with her!?" ("clench", "wide", "base", "L")
    ton @ hair horny "Of course! She couldn't get enough of me!" ("grin", "happyCl", "base", "mid")
    ton @ hair horny "After all... I'm quite skilled with my tongue." ("horny", "narrow", "base", "mid")
    cho @ cheeks blush "Your--" ("soft", "narrow", "worried", "L")
    gen "Tongue!" ("grin", xpos="far_left", ypos="head")
    play sound "sounds/giggle2_loud.ogg"
    ton @ hair horny "*Giggles*" ("base", "happyCl", "base", "mid")
    ton @ hair horny "Yes indeed... Would you like a demonstration?" ("crooked_smile", "narrow", "base", "mid")

    menu:
        gen "!!!" ("grin", xpos="far_left", ypos="head")
        "\"Yes please!\"":
            ton @ hair horny "Yeah, I bet you'd like that, Professor. {heart}" ("horny", "narrow", "base", "mid")
            ton @ hair horny "Maybe some other time." ("soft", "narrow", "base", "mid")
            cho @ cheeks blush "..." ("clench", "narrow", "worried", "down") # curious look

        "\"What do you say, Miss Chang?\"":
            cho @ cheeks heavy_blush "With m-me?" ("clench", "wide", "raised", "mid")
            ton @ hair horny "No, silly... Well, not today at least. {heart}" ("soft", "narrow", "base", "L")
            cho @ cheeks blush "..." ("clench", "narrow", "worried", "down") # blushing

    # Tonks shows her tongue.
    ton @ hair horny "You'll have to settle for a peek for now..." ("horny", "narrow", "base", "mid")
    cho @ cheeks blush "..." ("horny", "narrow", "base", "L") #blush
    gen "*Hmm?*..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "*Ahh*..." ("open_wide", "narrow", "base", "down")
    cho @ cheeks blush "" ("horny", "base", "raised", "L")
    ton @ hair horny "*Ahhhhhhh*........." ("open_wide_tongue", "narrow", "angry", "down") # Tonks shows her tongue.
    cho @ cheeks blush "Wow!" ("open", "base", "raised", "L")
    gen "..." ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Ae I chahn mhehk i ash ong ashh I whan..." ("open_wide_tongue", "narrow", "angry", "mid")
    ton @ hair horny "... shee!" ("open_wide_tongue2", "narrow", "angry", "down") # Tongue all the way out.
    cho @ cheeks heavy_blush "By Merlin's beard!" ("clench", "narrow", "worried", "L") #blush
    gen "Nice..." ("grin", xpos="far_left", ypos="head")
    gen "Although with a succubus, I highly doubt there was just kissing going on..." ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmm*... Yesh, thaht little devil..." ("open_wide_tongue", "narrow", "angry", "mid")
    ton @ hair horny "She was very quick to lock my head in place between her thighs, and then impaled herself on my tongue." ("open_wide_tongue", "narrow", "raised", "mid")
    ton @ hair horny "Rode my tongue for a good hour, that freak..." ("horny", "narrow", "angry", "mid")

    #gen "You're calling her a freak? Your tongue is longer than my dick!" ("angry", xpos="far_left", ypos="head")
    #cho "Professor?"
    #ton "Oh, sweetie... My dick could be longer than your dick..."
    #cho "What?!"
    #ton "Not that I have one currently..."
    #ton "But I could make it as long as I wanted!"
    #cho "..." #looking at the floor
    #gen "What else? Does it vibrate too? How are you even supposed to compete with that?" ("angry", xpos="far_left", ypos="head")
    #ton "*Giggles*" #sound
    #ton "I haven't tried that, actually... That's not a bad idea."
    #cho "" #blush
    #gen "..." ("base", xpos="far_left", ypos="head")
    #ton "Don't you worry professor... There's always the need for that masculine touch..."

    gen "(Like you didn't enjoy every minute of it...)" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Pleasuring her was quite exhausting to say the least..." ("soft", "narrow", "base", "L")
    ton @ hair angry "I licked her inside out until my whole face was covered in her devilish love-juices... {heart}" ("horny", "narrow", "angry", "mid")
    cho @ cheeks heavy_blush "" ("clench", "narrow", "worried", "down") #Horny #looks at tonks
    call ctc

    ton @ hair horny "Although... I did almost drown..." ("upset", "base", "raised", "up") # thinking back
    ton @ hair horny "Her thighs, practically glued to my cheeks meant there was no other way for her juices to flow than into my mouth..." ("open", "narrow", "annoyed", "mid")
    ton @ hair horny "Her essence becoming too much for me to handle as it eventually ran up my nose." ("horny", "narrow", "base", "down")
    gen "Holy shit." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "I had no other choice but to swallow all of it..." ("grin", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "" ("normal", "happyCl", "worried", "mid")
    play sound "sounds/gulp.ogg"
    gen "*gulp*" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "L")
    ton @ hair horny "That little demon must've come at least twenty times that night. {heart}" ("open_wide_tongue", "narrow", "raised", "L")
    ton @ cheeks heavy_blush hair horny "I could give you a ride on this as well if you'd like, Miss Chang." ("open_wide_tongue2", "narrow", "angry", "L") # tongue out
    cho @ cheeks heavy_blush "Professor--" ("soft", "narrow", "worried", "mid") # embarrassed #looks at you
    gen "Tonks, not before--" ("base", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush hair angry "Yes, yes... Not before you win that silly Quidditch cup." ("mad", "closed", "angry", "mid")
    cho @ cheeks blush "It's not silly!" ("annoyed", "narrow", "angry", "L")
    ton @ cheeks heavy_blush hair horny "Winning that cup won't feel as good as having my tongue inside you, Miss Chang... I can promise you that much." ("annoyed", "narrow", "angry", "L")
    cho @ cheeks heavy_blush "..." ("clench", "happyCl", "worried", "mid") #Pout #blush
    ton @ hair horny "Well then... I hope you two liked my little story. {heart}" ("open", "closed", "base", "mid")
    ton @ hair horny "And my new outfit, of course..." ("crooked_smile", "narrow", "base", "down")

    # Unlock outfit message. Should only appear once.
    if not ton_outfit_succubus.unlocked:
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_succubus)

    cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "L")
    ton @ hair horny "Maybe I could dress as a Succubus for Halloween. I'm sure the boys would love it..." ("base", "narrow", "base", "mid")
    gen "With or without the tits out?" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmm*... Haven't decided yet." ("upset", "narrow", "raised", "down")
    cho @ cheeks blush "..." ("clench", "narrow", "worried", "mid")
    ton @ hair horny "Well then... Off we go Miss Chang..." ("soft", "narrow", "base", "L")

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event



## Hermione Transformation ##
label .hermione_E1:
    # Pink Hair: $ hermione.get_equipped("hair").set_color([[255, 87, 171, 255], [255, 210, 227, 255], [230, 141, 32, 255]])
    # Brown Hair: $ hermione.get_equipped("hair").set_color([[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]])
    ton "Hermione again, *Hmm*?" ("base", "base", "base", "mid")
    ton "Seems to me like she's a bit of a favourite, isn't she?" ("soft", "narrow", "raised", "mid")
    gen "What can I say, she's got the best tits in the house!" ("grin", xpos="far_left", ypos="head")
    cho "Hey! That's not true!" ("annoyed", "narrow", "base", "mid")
    gen "It isn't? Then whose tits are better, Miss Chang?" ("base", xpos="far_left", ypos="head")
    gen "Do tell me, I'd love to know!" ("grin", xpos="far_left", ypos="head")
    cho "Just forget I said anything..." ("annoyed", "narrow", "base", "L")
    ton "Well... I, for one, am not going to disagree with you, Professor." ("crooked_smile", "narrow", "base", "mid")
    ton @ hair horny "Miss Granger's tits are quite nice indeed..." ("horny", "narrow", "angry", "mid")
    cho "..." ("normal", "narrow", "base", "up")
    ton "I mean we could do something else if you'd like, Miss--" ("open", "base", "base", "L")
    gen "No, No-- Do the thing!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("annoyed", "narrow", "base", "L")
    ton "Certainly... With pleasure." ("base", "happyCl", "base", "mid")
    stop music
    pause .8

    # Save custom Hermione name
    $ temp_name = name_hermione_genie
    $ name_hermione_genie = "Tonks"

    # Transforms into Hermione
    play sound "sounds/magic4.ogg"
    hide tonks_main
    $ hermione.strip("clothes")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ hermione_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("hide")
    call her_chibi("stand", 370, 360, flip=False)
    her "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=morph)
    pause .2

    cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "L")
    call ctc

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    her "Well then, here she is..." ("smile", "narrow", "angry", "mid")
    her "Feel free to touch me, Cho." ("base", "narrow", "annoyed", "R")
    her "Unlike Hermione, I won't bite you... Probably. {heart}" ("smile", "narrow", "annoyed", "down")
    cho @ cheeks blush "..." ("mad", "narrow", "worried", "down") # blush
    her "I simply love getting groped..." ("soft", "narrow", "angry", "up")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "L")
    gen "That reminds me... Let's talk about how well you did during the last quidditch match..." ("grin", xpos="far_left", ypos="head")
    gen "You did quite a good job pretending to be Hermione." ("base", xpos="far_left", ypos="head")
    gen "Wouldn't you say she did a good job commentating, Miss Chang?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Oh... Well, I wouldn't know since I was more focused on playing, Sir..." ("soft", "base", "base", "mid")
    cho @ cheeks heavy_blush "But from what I could gather, you did quite well, *uhm*... Professor." ("silly", "narrow", "worried", "L")
    gen "Yes... She put so much effort into it... you must have been completely exhausted by the end..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "L")
    her @ cheeks blush "... {heart}" ("base", "happy", "base", "mid_soft") # blushing
    cho @ cheeks blush "You were?" ("smile", "narrow", "base", "L")
    gen "Indeed... Addressing the entire school is no easy task, Miss Chang..." ("base", xpos="far_left", ypos="head")
    her "..." ("crooked_smile", "happyCl", "base", "mid") #Horny #Starts touching breasts (If Cho isn't looking)

    show screen blkfade
    with d5
    play sound "sounds/slick_02.ogg"
    with hpunch
    with kissiris
    $ hermione.set_pose("hand_on_pussy")
    her "" ("base", "narrow", "worried", "stare")
    hide screen blkfade
    with d5

    gen "You have to stay completely focused when you're tasked with commentating on everything that's happening." ("base", xpos="far_left", ypos="head")
    cho "Surely commentating doesn't even come close to the amount of focus you need to spot the snitch..." ("soft", "narrow", "raised", "mid")
    cho "Or how would Granger be able to do it?" ("annoyed", "narrow", "base", "R")
    gen "Depends on how easily you get distracted, I suppose..." ("base", xpos="far_left", ypos="head")
    gen "Would you say that you're easily distracted... Miss Granger?" ("base", xpos="far_left", ypos="head")
    her "*Mmm*..." ("base", "narrow", "base", "stare_soft")
    gen "Miss Granger?" ("base", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "narrow", "base", "L") #annoyed
    her "*Mmm*... Just thinking about it gets me all riled up again..." ("open", "narrow", "worried", "mid")
    cho @ cheeks blush "Professor, what are you..." ("disgust", "narrow", "base", "L") #Looks at Tonks/Hermione
    her "*Hmm*... Sorry, what did you say?" ("open_tongue", "narrow", "base", "L")
    cho @ cheeks blush "What are you doing?" ("mad", "happyCl", "base", "mid")
    play sound "sounds/giggle2_loud.ogg"
    her @ cheeks blush "*Giggles*" ("base", "narrow", "base", "mid") #sound
    her "What does it look like?" ("grin", "narrow", "base", "L")
    cho @ cheeks blush "You're touching your... Her--" ("clench", "narrow", "raised", "down")
    her "Yes... How could I not?" ("base", "narrow", "base", "mid")
    her "These breasts are just so..." ("soft", "narrow", "base", "down")

    # Hands on pussy, breast
    $ hermione.set_pose("hand_on_pussy_and_breast")
    play background "sounds/slickloop.ogg" fadein 2

    her "*Mmmh*... So soft..." ("base", "closed", "base", "mid")
    her "And her nipples..." ("soft", "narrow", "base", "down")
    her "*Ah*..." ("open_tongue", "narrow", "base", "stare_soft")
    her "So sensitive..." ("base", "narrow", "base", "up")
    cho @ cheeks heavy_blush "*Ehm*..." ("horny", "narrow", "worried", "down")
    her "*Mhmm*... And I bet her nipples aren't the only--" ("open", "narrow", "base", "down")
    her "" ("grin", "closed", "worried", "mid") #Hand in front of pussy
    pause .8
    play sound "sounds/slick_02.ogg"
    her "*Ah*..." ("open_tongue", "narrow", "base", "up") #Hand on pussy
    cho @ cheeks heavy_blush "Tonks!" ("mad", "narrow", "worried", "R")

    play background "sounds/slickloop.ogg" fadein 2 #Continuous masturbate loop
    her "*Mmmm*..." ("base", "narrow", "base", "up")
    pause 1
    her "*Hmm?*... Not even a peek?" ("soft", "narrow", "base", "L")
    her @ cheeks blush "Don't you want to see what Hermione looks like when--{w=0.2} *Ah*...{w=0.4} She masturbates?" ("grin", "narrow", "worried", "down")
    her @ cheeks blush "Are you sure you--{w=0.2} *Ah*...{w=0.4} want to miss this?" ("open", "closed", "base", "mid")
    cho @ cheeks heavy_blush "..." ("clench", "narrow", "worried", "down") #glances at her
    her "*Ah*...{w=0.3} That's it, Cho..." ("smile", "narrow", "base", "L")
    her "I knew you couldn't resist..." ("soft", "narrow", "base", "up")
    cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "down") #Horny
    call ctc

    her @ cheeks blush "*Ah*...{w=0.3} Look at me as I rub Granger's cute little slit." ("open_wide_tongue", "narrow", "angry", "up")
    her @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..." ("open_wide_tongue", "narrow", "worried", "up")
    cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "downR") #looks away
    call ctc

    her "No! Keep watching me!" ("annoyed", "narrow", "angry", "L")
    play background "sounds/slickloopfast.ogg"
    $ hermione.set_cum(pussy="wet")
    her @ cheeks blush "*Ah*...{w=0.3} I'm getting close!" ("soft", "narrow", "base", "up")
    play background "sounds/slickloopveryfast.ogg"
    cho @ cheeks heavy_blush "" ("mad", "narrow", "base", "down") #still looking away
    her @ cheeks blush "Watch me!" ("open_wide_tongue", "narrow", "angry", "up")
    cho @ cheeks heavy_blush "" ("horny", "narrow", "raised", "down") #still looking away
    her @ cheeks blush "Watch as Hermione cums for you!" ("angry", "narrow", "base", "up")
    cho @ cheeks heavy_blush "" ("smile", "narrow", "base", "down") #embarrased #Looks at Tonks
    play sound "sounds/slick_01.ogg"
    her @ cheeks blush "*Nngh*...{w=0.4} *Aaah*!!!" ("clench", "happy", "base", "ahegao")

    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    $ hermione.set_cum(pussy="squirt")
    pause .8

    $ hermione.set_cum(pussy="squirt_post")

    cho @ cheeks heavy_blush "" ("horny", "base", "raised", "down") #wide eyed

    her @ cheeks blush "*Ah*!" ("open_wide_tongue", "happy", "angry", "ahegao")

    with kissiris
    with hpunch
    play sound "sounds/slick_01.ogg"
    $ hermione.set_cum(pussy="squirt_transition")
    pause .8

    $ hermione.set_cum(pussy="squirt_post")

    stop background fadeout 2
    stop music fadeout 1
    her @ cheeks blush "*Mmmh*..." ("clench", "narrow", "base", "squint")
    cho @ cheeks heavy_blush "..." ("smile", "narrow", "base", "L")
    her @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.5} *Ah*...{w=0.6} Good...{w=0.3} Good girl..." ("open_tongue", "narrow", "base", "up")

    # Reset pose
    $ hermione.set_pose(None)
    $ hermione.strip("clothes")
    with d5

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    her "*Mmmh*... How I love masturbating in a body that I'm not quite familiar with..." ("smile", "happyCl", "base", "mid")
    her "It's like flying a new broom... There's nothing quite like the first test ride..." ("base", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "..." ("grin", "narrow", "base", "downR")
    play sound "sounds/giggle2_loud.ogg"
    her @ cheeks blush "*Giggles*" ("base", "happyCl", "base", "mid") #Looks at cho

    # Tonks transforms back.
    play sound "sounds/magic4.ogg"
    hide hermione_main
    $ hermione.set_cum(None)
    call her_chibi("hide")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ tonks_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("stand", 370, 360, flip=False)
    ton "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=morph)
    pause .2

    cho @ cheeks heavy_blush "" ("horny", "base", "base", "L")
    call ctc

    ton "Miss Granger's clit is quite sensitive... Who could have guessed?" ("grin", "narrow", "raised", "mid")
    gen "Noted." ("grin", xpos="far_left", ypos="head")
    ton "You'll do good to memorize this as well, Miss Chang. That knowledge might come in handy in the future." ("soft", "narrow", "base", "L")
    cho @ cheeks heavy_blush "..." ("smile", "narrow", "base", "down") # blushing
    ton "Well then... this should be enough to last me for the day... Hopefully..." ("grin", "narrow", "base", "mid")

    # Reset
    $ name_hermione_genie = temp_name

    # End Event.
    jump cc_pf_strip_T3_tonks.end_event

## End Event ##
label .end_event:

    # Fade to black.
    stop music fadeout 1
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    # The girls get dressed and wait at the door.
    $ cho.wear("all")
    $ tonks.wear("all")
    $ hermione.wear("all")

    # Reset zorder.
    $ cho.zorder = 15 # reset to default.
    $ tonks.zorder = 15 # reset to default.
    $ hermione.zorder = 15 # reset to default.
    $ cho_chibi.zorder = 3 # reset to default.
    $ tonks_chibi.zorder = 3 # reset to default.
    $ hermione_chibi.zorder = 3 # reset to default.
    hide screen cho_cloth_pile

    call cho_chibi("stand", 690, "base", flip=False)
    call ton_chibi("stand", "door", "base", flip=False)

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    hide screen blkfade
    with d5
    pause .5

    call bld
    if game.daytime:
        ton "We should get going, Miss Chang. Classes are about to start..." ("open", "base", "base", "L", ypos="head", flip=False)
        cho "Until next time, Professor." ("grin", "base", "base", "mid", ypos="head", flip=False)
    else:
        ton "Let me escort you back to your dormitories, Miss Chang." ("open", "base", "base", "L", ypos="head", flip=False)
        cho "Good night, Professor." ("grin", "base", "base", "mid", ypos="head", flip=False)

    call bld("hide")
    pause .1

    # They both leave.
    call cho_chibi(flip=True)
    pause .3
    call ton_chibi(flip=True)
    with d3
    pause .2

    play sound "sounds/door.ogg"
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    pause .5

    # Reset clothing.
    $ cho.equip(cho_outfit_last)
    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)

    $ states.ton.busy = True

    # End event.
    jump end_cho_strip_event
