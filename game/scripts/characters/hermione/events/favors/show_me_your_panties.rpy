

### Hermione Admire Panties ###

label start_hg_pf_admire_panties:

    if not _events_completed_any:

        gen "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 10
    
    return

label end_hg_pf_admire_panties:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    $ hermione.wear("all")

    hide screen blkfade
    if states.her.tier <= 2:
        her ".................." ("annoyed", "base", "base", "R", trans=fade)
    elif states.her.tier <= 3:
        her @ cheeks blush "" ("annoyed", "narrow", "base", "down", trans=fade)
    elif states.her.tier <= 5:
        her "" ("soft", "base", "base", "R", trans=fade)
    else:
        her "" ("smile", "narrow", "base", "mid_soft", trans=fade)

    # If Hermione is at tier 4+, she does not care about points.
    if states.her.tier < 4 and current_payout > 0:
        $ gryffindor += current_payout
        gen "{number=current_payout} points to Gryffindor, [name_hermione_genie]. Well done." ("base", xpos="far_left", ypos="head")

        if not _events_completed_any: # First time
            her "Another {number=current_payout} points..." ("base", "narrow", "worried", "down")
            her "I can't wait to tell the guys!" ("smile", "happyCl", "base", "mid")
            her "Except that I can't actually tell them about any of this..." ("annoyed", "narrow", "angry", "R")

    pause 1.0
    if game.daytime:
        her "Well, my classes are about to start..." ("open", "closed", "base", "mid")
    else:
        her "It's getting pretty late, [name_genie_hermione]..." ("open", "closed", "base", "mid")
    her "Will this be all?" ("open", "base", "base", "mid")
    gen "Yes, that shall do for now [name_hermione_genie], you may leave." ("base", xpos="far_left", ypos="head")

    # Hermione stops at the door
    call her_walk("door", "base")

    # If Hermione is at tier 4+, she does not care/forgets about points.
    if states.her.tier >= 6:
        her "(I feel like I've forgotten something...)" ("soft", "base", "worried", "stare", xpos="base", ypos="base", flip=True, trans=d3)
        her "(Oh well... I'm sure I'll remember if it was something important...)" ("base", "base", "base", "L")
    elif states.her.tier >= 5:
        her "(Hold on... I forgot about the points again...)" ("open", "base", "worried", "stare", xpos="base", ypos="base", flip=True, trans=d3)
        her "(*Eh*... I'm sure he'll remember the points next time...)" ("base", "base", "base", "R")
    elif states.her.tier >= 4:
        her "(Wait, what about my points...)" ("open", "base", "worried", "stare", xpos="base", ypos="base", flip=True, trans=d3)
        her "(I better remember to ask next time...)" ("annoyed", "base", "base", "L")

    # Hermione leaves
    call her_chibi("leave")

    # Increase level
    if states.her.tier == 1:
        if states.her.level < 3: # Points til 3
            $ states.her.level += 1

    elif states.her.tier == 2:
        if states.her.level < 9: # Points til 9
            $ states.her.level += 1

    elif states.her.tier == 3:
        if states.her.level < 12: # Points til 12
            $ states.her.level += 1

    elif states.her.tier == 4:
        if states.her.level < 18: # Points til 18
            $ states.her.level += 1

    jump end_hermione_event

### Tier 1 ###

# Hermione reluctantly lifts her skirt for you.
# Event 1 (i) - Hermione is shocked about your suggestion.
# Event 2 (r) - Hermione still can't believe what you ask her to do.

label hg_pf_admire_panties_T1_intro_E1:

    call start_hg_pf_admire_panties

    gen "Nothing drastic, really..." ("base", xpos="far_left", ypos="head")
    gen "I just want you to show me your panties." ("base", xpos="far_left", ypos="head")
    her "My... Panties...?" ("open", "base", "base", "mid")
    her "[name_genie_hermione]!" ("angry", "base", "angry", "mid")
    gen "I know, I know, this is a little weird..." ("base", xpos="far_left", ypos="head")
    her "{size=+7}A little !?{/size}" ("shock", "wide", "base", "stare")
    her "This is completely inappropriate!"
    gen "Listen, we need to go through this phase before we get to the good stuff, alright?" ("base", xpos="far_left", ypos="head")
    her "The \"good stuff\"? [name_genie_hermione], I don't understand..." ("angry", "base", "base", "mid")
    gen "What don't you understand, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    gen "Do you need these points or not?" ("base", xpos="far_left", ypos="head")
    her "I do..." ("disgust", "base", "base", "down")
    gen "Get up here and show them to me then..." ("base", xpos="far_left", ypos="head")
    her "............." ("angry", "base", "angry", "mid")

    call hg_pf_admire_panties_T1

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T1_E1:

    call start_hg_pf_admire_panties

    gen "Nothing drastic, really..." ("base", xpos="far_left", ypos="head")
    gen "I just want you to show me your panties." ("base", xpos="far_left", ypos="head")
    her "This again?" ("angry", "base", "angry", "mid")
    gen "Yes. Show them to me..." ("base", xpos="far_left", ypos="head")
    her "............." ("angry", "base", "angry", "mid")

    call hg_pf_admire_panties_T1

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T1: # Call label

    $ states.her.status.show_panties = True

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if hermione.is_worn("bottom"):
        $ hermione.strip("bottom")
        call her_chibi("lift_skirt","desk","base")
        with d3
        call ctc
    else:
        call her_chibi("stand", "desk", "base")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
    her "....................." ("angry", "base", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    call ctc

    menu:
        "-Stare at her face-":
            nar "You study Hermione's face--"
            nar "Wondering what's going through her mind right now."
            her "......................." ("angry", "narrow", "annoyed", "mid", emote="angry")

        "-Stare at her panties-":
            nar "It's plain girlish underwear, nothing that an ordinary girl wouldn't wear."

    if not _events_completed_any:
        her "......................." ("angry", "narrow", "annoyed", "mid", emote="angry")
    else:
        her "......................." ("angry", "narrow", "base", "R", emote="angry")

    call ctc
    return

### Tier 2 ###

# Hermione lifts her skirt for you.
# Event 1 (i) - Hermione is embarrassed about what she's about to do.
# Event 2 (r) - Hermione is still not happy.

label hg_pf_admire_panties_T2_intro_E1:

    call start_hg_pf_admire_panties

    her "So, what will it be, [name_genie_hermione]?"
    gen "Nothing drastic, really..." ("base", xpos="far_left", ypos="head")
    gen "I just want you to show me your panties." ("base", xpos="far_left", ypos="head")

    if not _events_completed_any:
        her "My Panties?!" ("clench", "base", "worried", "mid")
    else:
        her "Oh... again?" ("annoyed", "base", "worried", "R")

    gen "Just do it..." ("base", xpos="far_left", ypos="head")
    her ".................." ("annoyed", "base", "worried", "mid")

    call hg_pf_admire_panties_T2

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T2_E1:

    call start_hg_pf_admire_panties

    her "What will it be, [name_genie_hermione]?"
    gen "I'd like you to show me your panties again." ("base", xpos="far_left", ypos="head")
    her ".................." ("annoyed", "base", "worried", "R")
    her "Alright..." ("open", "base", "worried", "R")

    call hg_pf_admire_panties_T2

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T2: # Call label

    $ states.her.status.show_panties = True

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if hermione.is_worn("bottom"):
        $ hermione.strip("bottom")
        call her_chibi("lift_skirt","desk","base")
        with d3
        call ctc
    else:
        call her_chibi("stand", "desk", "base")


    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
    her "Here, [name_genie_hermione]..." ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=d3)
    call ctc

    menu:
        "\"You don't look too embarrassed...\"":
            her "That's not true..." ("base", "happy", "base", "mid")
            her "But it is a small price to pay if it means the Gryffindor house keeps the cup this year." ("base", "base", "base", "R")
            her "I know everyone will be so happy..."

        "\"I like your panties...\"":
            her "Thank you, [name_genie_hermione]..." ("base", "happy", "base", "mid")

        "-Keep looking into her eyes-":
            her ".............................." ("soft", "base", "base", "mid")
            her "...........................?"
            her "................................" ("grin", "base", "base", "R")
            her "[name_genie_hermione], please... You are embarrassing me." ("grin", "happyCl", "worried", "mid",emote="sweat")
    call ctc
    return

### Tier 3 ###
# Event 1 (i) - Ask her to take off her panties, she agrees to flash you quickly + variation if she has stripped.
# Event 2 (r) - Ask her to take off her panties, you make her stand for longer + variation if she has stripped.

label hg_pf_admire_panties_T3_intro_E1:

    call start_hg_pf_admire_panties

    $ states.her.status.show_pussy = True

    if not _events_completed_any:
        gen "[name_hermione_genie], could you show me your panties?" ("base", xpos="far_left", ypos="head")
        if not states.her.status.stripping:
            her "My panties?" ("open", "narrow", "base", "mid")
            gen "If it's not too much trouble..." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... I suppose not..." ("angry", "squint", "base", "R")
        else:
            her "I suppose... If it's just my panties..." ("angry", "squint", "base", "R")
            gen "(You'd be so lucky...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "[name_hermione_genie], I think it's time I took another look at your panties." ("base", xpos="far_left", ypos="head")
        if not states.her.status.stripping:
            her "Again?" ("open", "narrow", "base", "mid")
            gen "Yes, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Okay." ("angry", "squint", "base", "R")
        else:
            her "Just my panties, right?" ("open", "squint", "base", "mid")
            gen "We'll see..." ("base", xpos="far_left", ypos="head")
            her "Right..." ("angry", "narrow", "base", "down")

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if hermione.is_worn("bottom"):
        $ hermione.strip("bottom")
        call her_chibi("lift_skirt","desk","base")
        with d3
        call ctc
    else:
        call her_chibi("stand", "desk", "base")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
    her "There you go." ("base", "squint", "base", "mid", xpos="mid", ypos="base", trans=dissolve)

    gen "Very good, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    menu:
        "\"How are you feeling?\"":
            her "[name_genie_hermione]?" ("soft", "squint", "base", "mid")
            gen "How does it feel, knowing you're earning your house a lot of points." ("base", xpos="far_left", ypos="head")
            her "*Ehm*... Good?" ("angry", "happy", "base", "mid")
            her @ cheeks blush "I mean, as good as you could feel when you're showing the headmaster your panties." ("angry", "squint", "base", "R")
            gen "Glad to hear it." ("base", xpos="far_left", ypos="head")
        "-Stare at her face-":
            gen "You've got a very pretty face, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]?" ("angry", "base", "base", "mid")
            her "I thought you were supposed to be looking at my panties." ("angry", "narrow", "base", "mid")
            gen "Does it matter where I'm looking?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*...{w=0.4} Well as long as you're still paying me..." ("angry", "narrow", "base", "R")
        "-Stare at her panties-":
            her "..." ("base", "squint", "base", "mid")
            her "...{fast}..." ("normal", "squint", "base", "mid")
            her @ cheeks blush "[name_genie_hermione]?" ("open", "squint", "base", "mid")
            gen "Yes, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You're staring very intently..." ("angry", "narrow", "base", "R")
            gen "Of course, I'm savouring every moment." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Right..." ("open", "narrow", "base", "down")
            her @ cheeks blush "" ("normal", "narrow", "base", "down")
            call ctc

    her @ cheeks blush "Are we done?" ("open", "base", "base", "mid")
    gen "Not quite." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "[name_genie_hermione]?" ("angry", "base", "base", "mid")
    gen "First I'd like you to take those panties off." ("base", xpos="far_left", ypos="head")

    if not states.her.status.stripping:
        her @ cheeks blush "You want me to--" ("clench", "squint", "base", "mid")
        gen "Take them off for me, yes." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
        gen "For Gryffindor, obviously." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "So, I will get extra points for this?" ("open", "closed", "worried", "mid")
        gen "Of course, you shall receive twenty extra points..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Hmm*..." ("annoyed", "narrow", "worried", "R")
        her @ cheeks blush "For how long?" ("open", "narrow", "base", "mid")
        gen "Just a quick peek shall suffice." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Alright then..." ("open", "closed", "base", "mid")

        $ current_payout += 20
    else:
        her @ cheeks blush "I thought you just wanted me to show you my panties..." ("angry", "narrow", "base", "mid")
        gen "Yes, and now I want to see them slide off your legs." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "down")
        gen "You'll get paid extra, obviously..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "...{w=0.4} How much extra?" ("open", "narrow", "base", "R")
        gen "Ten points." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Just ten?" ("clench", "narrow", "base", "mid")
        gen "Is ten points not good enough for a quick glance of what's under those panties?" ("base", xpos="far_left", ypos="head")
        gen "It's not like I haven't gotten a good look already..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("annoyed", "narrow", "base", "down")
        her @ cheeks blush "I suppose...{w=0.4} If it's just a quick glance..." ("open", "narrow", "base", "down")

        $ current_payout += 10

    her @ cheeks blush "..." ("normal", "narrow", "base", "down")

    play sound "sounds/cloth_sound3.ogg"
    $ hermione.strip("panties")
    with d3

    her @ cheeks blush "" ("normal", "narrow", "base", "down")
    pause 4
    her @ cheeks blush "" ("angry", "narrow", "base", "mid")
    pause 3

    her @ cheeks blush "Okay, that's{nw}" ("open", "squint", "base", "mid")
    play sound "sounds/cloth_sound3.ogg"
    $ hermione.wear("panties")
    her "Okay, that's{fast} enough..."

    gen "Very well, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T3_E1:

    call start_hg_pf_admire_panties

    gen "[name_hermione_genie], I think it's time I took another look at your panties." ("base", xpos="far_left", ypos="head")
    her "Just my panties?" ("open", "narrow", "base", "mid")
    gen "*Hmm*... We'll see..." ("base", xpos="far_left", ypos="head")
    her "Alright..." ("open", "squint", "base", "mid")

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if hermione.is_worn("bottom"):
        $ hermione.strip("bottom")
        call her_chibi("lift_skirt","desk","base")
        with d3
        call ctc
    else:
        call her_chibi("stand", "desk", "base")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
    her "Here you go." ("base", "squint", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    call ctc

    gen "Excellent." ("base", xpos="far_left", ypos="head")

    menu:
        "\"You look pretty comfortable...\"":
            her "I guess..." ("open", "squint", "base", "R")
            her "It's not really that different from wearing bikini bottoms..." ("open", "closed", "base", "mid")
            her "I can just pretend that I'm at the lake." ("base", "closed", "base", "mid")
            gen "Right..." ("base", xpos="far_left", ypos="head")
            gen "(Then why not just pretend you're in the shower and bare it all.)" ("base", xpos="far_left", ypos="head")
        "\"Do you like showing off your panties?\"":
            her "Like, [name_genie_hermione]?" ("open", "squint", "base", "mid")
            gen "Yes [name_hermione_genie]... Do you enjoy it?" ("base", xpos="far_left", ypos="head")
            her "*Hmm*... I don't mind it, I guess..." ("open", "squint", "base", "R")
            her "As long as it makes my house happy." ("base", "base", "base", "mid")
            gen "I'm sure it does." ("base", xpos="far_left", ypos="head")
        "-Stare at her panties-":
            her "..." ("base", "squint", "base", "mid")
            her "......" ("normal", "squint", "base", "mid")
            her "[name_genie_hermione]?" ("open", "squint", "base", "mid")
            gen "Yes, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her "Do you have to stare so intently at them?" ("angry", "squint", "base", "mid")
            gen "I don't." ("base", xpos="far_left", ypos="head")
            gen "..." ("base", xpos="far_left", ypos="head")
            her "You're still staring..." ("annoyed", "narrow", "base", "mid")
            gen "I don't have to... But I want to." ("base", xpos="far_left", ypos="head")
            her "Right..." ("angry", "narrow", "base", "R")

    menu:
        "\"Now take them off.\"":
            her @ cheeks blush "[name_genie_hermione]!" ("angry", "narrow", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            gen "Surely you knew this was coming..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmph*... I suppose..." ("clench", "narrow", "base", "R")
            gen "So?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Just a flash, right?" ("annoyed", "narrow", "base", "mid")
            gen "Right." ("base", xpos="far_left", ypos="head")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("panties")
            with d3

            her @ cheeks blush "" ("normal", "narrow", "base", "down")
            pause 4
            her @ cheeks blush "" ("angry", "narrow", "base", "mid")
            pause 3

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("panties")
            her @ cheeks blush "Okay, that's--" ("clench", "narrow", "base", "down")
            gen "Wait!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "[name_genie_hermione]?" ("angry", "squint", "base", "mid")
            gen "I'm not done yet." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "But you said...{w} *Ugh*...{w=0.4} Fine...{nw}" ("angry", "narrow", "worried", "down")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("panties")

            her "But you said... *Ugh*... Fine...{fast}"
            her @ cheeks blush "Happy?" ("angry", "narrow", "base", "mid") #Looks away
            nar "You stare intently at Hermione's exposed pussy."
            her @ cheeks blush "Are you--" ("angry", "narrow", "base", "R") #Looks at genie
            gen "Quiet." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "closed", "base", "mid")
            call ctc
            gen "Okay, I'm done..." ("base", xpos="far_left", ypos="head")
        "-Let her go-":
            gen "Alright then, that shall do for now." ("base", xpos="far_left", ypos="head")

    jump end_hg_pf_admire_panties

### Tier 4 ###

# Event 1 (i) - Hermione is not wearing her panties.
# Event 2 (r) - No panties. You get to call her a slut.
# Event 3 (r) - Panties may or may not be equipped. Hermione asks to remove them or keep them on.

## Can unequip underwear in wardrobe at this stage ##
label hg_pf_admire_panties_T4_intro_E1:

    call start_hg_pf_admire_panties

    if not _events_completed_any:
        gen "[name_hermione_genie], I'd like you to show me your panties, if that's not too much trouble." ("base", xpos="far_left", ypos="head")
    else:
        gen "[name_hermione_genie], I'd like you to show me your panties again, if that's not too much trouble." ("base", xpos="far_left", ypos="head")
    her "My panties?" ("open", "narrow", "worried", "down")
    gen "Yes [name_hermione_genie]... Get up here will you..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh, Okay..." ("base", "narrow", "base", "down")

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if not hermione.is_worn("bottom") and hermione.is_worn("panties"):
        call her_chibi("stand", "desk", "base")
        her @ cheeks blush "*Hmm*... You know what..." ("normal", "narrow", "base", "R", xpos="mid", ypos="base")
        $ hermione.strip("panties")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4
        her @ cheeks blush "" ("base", "narrow", "base", "mid")
        call ctc

        gen "Trying to get some extra points, are you?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Perhaps..." ("base", "narrow", "worried", "down")
    else:
        if hermione.is_any_worn("bottom", "panties"):
            if hermione.is_worn("bottom", "panties"):
                call her_chibi("lift_skirt","desk","base")
            else:
                call her_chibi("stand", "desk", "base")
            $ hermione.strip("bottom", "panties")
            with d3
            pause.8

            her @ cheeks blush ".........................." ("base", "base", "base", "R", xpos="mid", ypos="base")
            gen "!!?" ("angry", xpos="far_left", ypos="head")

            her @ cheeks blush "" ("base", "narrow", "base", "mid_soft")
            call ctc

            # No Panties!
            gen "Where are your panties, [name_hermione_genie]?" ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, lately I just don't feel like wearing them..." ("base", "narrow", "worried", "down")
            gen "So, you're not doing it in the hopes of earning some extra point?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course not..." ("base", "narrow", "worried", "down")
        else:
            call her_chibi("stand", "desk", "base")

            her @ cheeks blush "*Ehm*..." ("open", "squint", "base", "R", xpos="mid", ypos="base")
            her @ cheeks blush "You asked me not to wear any panties, [name_genie_hermione]..." ("base", "narrow", "worried", "down")
            gen "Oh... So I did..." ("base", xpos="far_left", ypos="head")
            gen "I just wanted to make sure you followed my instructions..." ("base", xpos="far_left", ypos="head")
            gen "Well done [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you [name_genie_hermione]..." ("base", "narrow", "worried", "mid")

    menu:
        "\"You little slut!\"":
            her "*Hmm*..."
            her "So, am I receiving any extra points for not wearing any panties?" ("base", "narrow", "base", "mid_soft")

            menu:
                "\"Absolutely!\"":
                    gen "Ten additional points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                    her "Thank you, [name_genie_hermione]!" ("base", "happyCl", "worried", "mid")

                    $ gryffindor+= 10

                    call ctc

                "\"Absolutely not!\"":
                    her "Why not!?" ("scream", "closed", "angry", "mid")
                    gen "Sluts don't get paid." ("base", xpos="far_left", ypos="head")
                    gen "That's what makes them sluts." ("base", xpos="far_left", ypos="head")
                    her "Will you at least pay me the {number=current_payout} points?" ("annoyed", "base", "angry", "mid")
                    gen "Are you a slut or are you a prostitute?" ("base", xpos="far_left", ypos="head")
                    her "[name_genie_hermione]?!" ("angry", "base", "worried", "mid")
                    gen "It's a simple question... Sluts don't get paid, so you're a prostitute then?" ("base", xpos="far_left", ypos="head")
                    her "{size=-4}I'm not a prostitute...{/size}" ("disgust", "base", "worried", "mid")
                    gen "Then, what are you, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    her "Do I really have to--" ("disgust", "narrow", "worried", "mid")
                    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I'm...{w=0.4} {size=-4}... A slut. {/size}" ("open", "narrow", "worried", "down")
                    gen "Good girl." ("base", xpos="far_left", ypos="head")

                    $ current_payout = 0
                    $ states.her.mood +=5

                    call ctc

        "\"Good! {number=current_payout} points!\"":
            pass

    jump end_hg_pf_admire_panties

label hg_pf_admire_panties_T4_E1:

    call start_hg_pf_admire_panties

    gen "[name_hermione_genie], I'd like you to show me your panties again, if possible." ("base", xpos="far_left", ypos="head")
    her "Oh..." ("open", "narrow", "worried", "down")
    her @ cheeks blush "Well, that might be an issue..." ("base", "narrow", "base", "down")

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if not hermione.is_worn("bottom") and hermione.is_worn("panties"):
        call her_chibi("stand", "desk", "base")
        her @ cheeks blush "I don't really feel like wearing them right now..." ("base", "narrow", "base", "R", xpos="mid", ypos="base")
        $ hermione.strip("panties")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4
        her @ cheeks blush "" ("base", "narrow", "base", "mid")
        call ctc

        gen "Is that so?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes..." ("base", "narrow", "base", "mid")
    else:
        if hermione.is_any_worn("bottom", "panties"):
            if hermione.is_worn("bottom", "panties"):
                call her_chibi("lift_skirt","desk","base")
            else:
                call her_chibi("stand", "desk", "base")
            $ hermione.strip("bottom", "panties")
            with d3
            pause.8

            her "" ("base", "narrow", "base", "mid_soft", xpos="mid", ypos="base", trans=d3)
            call ctc

            # No Panties!
            gen "No panties again, [name_hermione_genie]?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I figured there was no point in wearing any, since you're asking me to undress all the time..." ("base", "narrow", "worried", "down")
        else:
            call her_chibi("stand", "desk", "base")

            her @ cheeks blush "I'm not wearing any panties right now..." ("base", "narrow", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
            her @ cheeks blush "Was I supposed to? I'm sure you asked me not to wear them..." ("open", "narrow", "worried", "down")
            gen "So I did... Good job [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            gen "I'm glad that I can count on you to do what I ask of you." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Thank you [name_genie_hermione]." ("base", "narrow", "worried", "mid")

    menu:
        "\"You little slut!\"":
            her "*Hmm*..."
            her "Do I get extra points this time?" ("open", "narrow", "base", "mid_soft")

            menu:
                "\"Absolutely!\"":
                    gen "Absolutely!" ("base", xpos="far_left", ypos="head")
                    gen "Ten additional points to Gryffindor!" ("base", xpos="far_left", ypos="head")
                    her "Thank you, [name_genie_hermione]!" ("base", "happyCl", "worried", "mid")

                    $ gryffindor+= 10

                    call ctc

                "\"Absolutely not!\"":

                    her "Why not!?" ("scream", "closed", "angry", "mid")
                    gen "Sluts doesn't get paid." ("base", xpos="far_left", ypos="head")
                    gen "That's what makes them sluts." ("base", xpos="far_left", ypos="head")
                    her "Will you at least pay me the {number=current_payout} points?" ("annoyed", "base", "angry", "mid")
                    gen "Are you a slut or are you a prostitute?" ("base", xpos="far_left", ypos="head")
                    her "[name_genie_hermione]?!" ("angry", "base", "worried", "mid")
                    gen "It's a simple question... Sluts doesn't get paid, so you're a prostitute then?" ("base", xpos="far_left", ypos="head")
                    her "{size=-4}I'm not a prostitute...{/size}" ("disgust", "base", "worried", "mid")
                    gen "Then, what are you, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    her "Do I really have to--" ("disgust", "narrow", "worried", "mid")
                    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I'm...{w=0.4} {size=-4}... A slut. {/size}" ("open", "narrow", "worried", "down")
                    gen "Good girl." ("base", xpos="far_left", ypos="head")

                    $ current_payout = 0
                    $ states.her.mood +=5

                    call ctc

        "\"Good! {number=current_payout} points!\"":
            pass


    her "I could put my panties back on for you, if you'd like that, [name_genie_hermione]?" ("open", "base", "base", "mid")

    menu:
        "\"Yes, put them back on!\"":
            her "Alright, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
            hide hermione_main
            with d3
            nar "Hermione puts on her panties."

            if not hermione.is_equipped("panties"):
                $ hermione.equip(her_panties_base1)
            else:
                $ hermione.wear("panties")

            her "" ("base", "narrow", "base", "mid_soft")
            call ctc

            her "I hope you like them..." ("soft", "base", "base", "R")

        "\"No, keep them off!\"":
            her "Of course, [name_genie_hermione]." ("soft", "narrow", "base", "mid")
            $ hermione.unequip("panties")
            call ctc

    jump end_hg_pf_admire_panties


label hg_pf_admire_panties_T4_E2:

    call start_hg_pf_admire_panties

    gen "[name_hermione_genie], show me those cute panties of yours again." ("base", xpos="far_left", ypos="head")
    her "Oh..." ("open", "narrow", "worried", "down")
    her @ cheeks blush "Okay..." ("base", "narrow", "base", "down")

    call hide_characters
    with d3

    if hermione.is_any_worn("robe", "accessory"):
        $ hermione.strip("robe", "accessory")
        play sound "sounds/cloth_sound3.ogg"
        pause 1.4

    call her_walk("desk", "base", reduce=0.8)
    pause .7

    if hermione.is_worn("bottom"):
        $ hermione.strip("bottom")
        call her_chibi("lift_skirt","desk","base")
        with d3
        call ctc
    else:
        call her_chibi("stand", "desk", "base")

    her "" ("base", "narrow", "base", "mid_soft", xpos="mid", ypos="base", trans=d3)
    call ctc

    # No Panties.
    if not hermione.is_worn("panties"):
        gen "Where are your panties, [name_hermione_genie]?" ("grin", xpos="far_left", ypos="head")
        her "You asked me not to wear any..." ("open", "squint", "base", "mid")
        gen "Oh right..." ("base", xpos="far_left", ypos="head")
        call ctc

        her "If you'd like, [name_genie_hermione], I could put my panties back on for you." ("soft", "narrow", "base", "mid_soft")

        menu:
            "\"Yes, put them back on!\"":
                her "Alright, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
                hide hermione_main
                with d3
                nar "Hermione puts on her panties."

                if not hermione.is_equipped("panties"):
                    $ hermione.equip(her_panties_base1)
                else:
                    $ hermione.wear("panties")

                her "" ("base", "narrow", "base", "mid_soft")
                call ctc

                her "I hope you like them..." ("soft", "base", "base", "mid")

            "\"No, keep them off!\"":
                her "Of course, [name_genie_hermione]." ("soft", "narrow", "annoyed", "up")
                $ hermione.unequip("panties")
                call ctc

    else:
        her "Do you like them, [name_genie_hermione]?" ("base", "narrow", "base", "mid_soft")
        gen "Indeed I do, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        call ctc

        her "I could take them off, if you'd like that, [name_genie_hermione]." ("open", "base", "base", "R")

        menu:
            "\"Yes, Take them off!\"":
                her "Alright, [name_genie_hermione]." ("soft", "narrow", "annoyed", "up")
                gen "And keep them off from now on!" ("base", xpos="far_left", ypos="head")
                her "Whatever you want, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
                hide hermione_main
                with d3
                nar "Hermione takes off her panties."

                $ hermione.unequip("panties")

                her "" ("base", "narrow", "base", "mid_soft")
                call ctc

                her "I hope you like it, [name_genie_hermione]..." ("angry", "wink", "base", "mid")

            "\"No, keep them on!\"":
                her "Of course, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
                call ctc

    jump end_hg_pf_admire_panties
