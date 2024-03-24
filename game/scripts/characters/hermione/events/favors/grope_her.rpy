

### Hermione Groping ###

label start_hg_pf_grope:

    if not _events_completed_any:
        gen "{size=-4}(I will grope her a little. Pretty harmless stuff.){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 15
    return

label hg_pf_grope_fail:
    jump end_hermione_event

label end_hg_pf_grope:

    # Setup
    stop music fadeout 1.0
    call hide_characters
    show screen blkfade
    with d3

    nar "You let go of Hermione..."

    $ hermione.wear("all")
    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    if states.her.mood != 0:
        her "" ("annoyed", "base", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    else:
        her "" ("soft", "narrow", "base", "R", xpos="mid", ypos="base", trans=fade)

    gen "This will do for now." ("base", xpos="far_left", ypos="head")
    if states.her.tier <= 3:
        her @ cheeks blush "................" ("annoyed", "narrow", "angry", "R")
    else:
        her @ cheeks blush "................" ("soft", "narrow", "base", "R")


    # Points
    if states.her.tier <= 5:
        $ gryffindor += current_payout
        gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    else:
        gen "You may leave now, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    if states.her.tier <= 2:
        her ".................." ("annoyed", "base", "worried", "R")
        her "Thank you, [name_genie_hermione]..."
    elif states.her.tier <= 4:
        her ".................." ("base", "base", "base", "R")
        her "Thank you, [name_genie_hermione]..." ("soft", "base", "base", "mid")
    else:
        her ".................." ("soft", "narrow", "annoyed", "up")
        her "Thank you, [name_genie_hermione]..." ("soft", "narrow", "base", "mid_soft")

    if game.daytime:
        her "Now, if you don't mind, I'd better go. My classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."

    # Hermione leaves
    call her_walk("door", "base")

    if states.her.tier > 5:
        her @ cheeks blush "(What about my points?)" ("disgust", "narrow", "base", "down", xpos="base", flip=True)
        if states.her.level < 24:
            her "(I'll just ask him about it next time...)" ("annoyed", "narrow", "angry", "R")
        else:
            her @ cheeks blush "(Eh, who cares...)" ("base", "narrow", "base", "up")
        pause.5

    call her_chibi("leave")


    # Increase level
    if states.her.tier == 2:
        if states.her.level < 9: # Points til 9
            $ states.her.level += 1

    if states.her.tier == 3:
        if states.her.level < 12: # Points til 12
            $ states.her.level += 1

    jump end_hermione_event

### Tier 1 - Events Fail ###

# Those events still prgress, but Hermione will run off and get mad.
# The heart icons for these events are 'black'

label hg_pf_grope_T1_E1:

    call start_hg_pf_grope

    if not _event_completed_failed:
        gen "[name_hermione_genie], would you mind if I play with your tits a little?" ("base", xpos="far_left", ypos="head")
        her "Play with...?" ("shock", "wide", "base", "stare")
        her "My tits?!" ("angry", "wide", "base", "mid")
        gen "Or your butt! I haven't fully decided yet!" ("grin", xpos="far_left", ypos="head")
        her "[name_genie_hermione]??!" ("shock", "wide", "base", "stare")
        her "How could you ask for such a thing!?" ("angry", "wide", "base", "stare")
        her "I think I better leave." ("angry", "happyCl", "worried", "mid")
    else:
        gen "[name_hermione_genie], I'd like to grope you a little!" ("grin", xpos="far_left", ypos="head")
        her "This again...?" ("angry", "base", "angry", "mid")
        her "I've told you before, [name_genie_hermione], absolutely not!!" ("scream", "closed", "angry", "mid")
        her "By Merlin's beard..." ("angry", "base", "angry", "mid")
        gen "Please?" ("base", xpos="far_left", ypos="head")
        her "I'm leaving! Good day, Sir!" ("soft", "closed", "base", "mid")

    call her_walk(action="leave")

    $ states.her.mood += 6

    jump hg_pf_grope_fail

### Tier 2 ###

# Event 1 (i) - Hermione is shocked about you groping her.
# Event 2 (i) - Hermione is still shocked.

label hg_pf_grope_T2_intro_E1:
    stop music fadeout 2.0
    gen "Come closer [name_hermione_genie]... Hop around my desk..." ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Very well, [name_genie_hermione]." ("disgust", "narrow", "base", "down")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    her "[name_genie_hermione].....?" ("annoyed", "base", "worried", "R", ypos="head", flip=False)
    gen "..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna molest your tits now.\"":
            her "What? What do you mean, [name_genie_hermione]--" ("soft", "wide", "base", "stare")
            if hermione.is_worn("top"):
                nar "You reach out swiftly and grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly and grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly and grab both of her tits..." #Fallback, she'd usually wear a bra on this level.

            jump hg_pf_grope_breasts_T2

        "\"I'm gonna play with your butt a little.\"":
            nar "You reach out and place your hand on her butt cheeks..."

            jump hg_pf_grope_ass_T2

label hg_pf_grope_T2_E1:
    stop music fadeout 2.0
    gen "Come closer [name_hermione_genie]... Hop around my desk..." ("base", xpos="far_left", ypos="head")
    her "..............." ("annoyed", "base", "angry", "mid")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    her "[name_genie_hermione].....?" ("annoyed", "narrow", "angry", "R", ypos="head", flip=False)
    gen "..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna molest your tits now.\"":
            her "!!!" ("soft", "wide", "worried", "shocked")
            her "S-Sir?!" ("disgust", "happyCl", "worried", "mid")
            if hermione.is_worn("top"):
                nar "You reach out swiftly and grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly and grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly and grab both of her tits..." #Fallback, she'd usually wear a bra on this level.

            jump hg_pf_grope_breasts_T2

        "\"I'm gonna play with your butt a little.\"":
            nar "You reach out and place your hand on her butt cheeks..."

            jump hg_pf_grope_ass_T2

### Tier 3 ###

# Event 1 (i) - Hermione tries to talk you out of it.
# Event 2 (i) - Hermione is indignant.

label hg_pf_grope_T3_intro_E1:
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "How would you like to earn some house points today?" ("base", xpos="far_left", ypos="head")
    her "And what would I need to do to earn them?" ("annoyed", "narrow", "annoyed", "mid")
    gen "Oh, nothing too out of the ordinary." ("base", xpos="far_left", ypos="head")
    gen "You'd just have to stand here, while I grope you for a bit..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]... I'd prefer it if you wouldn't make me such offers..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Why? Too hard to resist?" ("base", xpos="far_left", ypos="head")
    her "Nothing of the sort, [name_genie_hermione]."
    gen "Well, that's my offer, so how about you come closer and bare your tits for me...?" ("base", xpos="far_left", ypos="head")
    gen "I feel like playing with them a little..." ("grin", xpos="far_left", ypos="head")
    her "!!!" ("open", "base", "base", "mid")
    gen "Or your butt..." ("base", xpos="far_left", ypos="head")
    gen "I'd like to give it a good squeeze." ("grin", xpos="far_left", ypos="head")

    her "[name_genie_hermione]! Don't you think this is too much?" ("disgust", "narrow", "base", "mid_soft")
    gen "You think?" ("base", xpos="far_left", ypos="head")
    her "I am not one of those harlots from Slytherin, you know..."
    gen "I know... You are from {i}Gryfonmon{/i}... Or something..." ("base", xpos="far_left", ypos="head") #<- GRYFFINDOR MISSPELLED ON PURPOSE
    her "So if I don't feel like it, then I don't have to sell you a single favour, [name_genie_hermione]!" ("annoyed", "base", "worried", "R")
    gen "Of course..." ("base", xpos="far_left", ypos="head")
    her "..................." ("annoyed", "narrow", "angry", "R")
    gen "So, I'd like to award {number=current_payout} house points to Gryffindor... If you \"feel\" like earning any more points from me, that is." ("base", xpos="far_left", ypos="head")
    her "......................." ("disgust", "narrow", "base", "mid_soft")
    her "Is watching me not enough, [name_genie_hermione]?"
    gen "Why watch, when I could touch..." ("base", xpos="far_left", ypos="head")
    her "...................................."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause .5

    her "[name_genie_hermione].....?" ("annoyed", "narrow", "angry", "R", ypos="head", flip=False)
    gen "..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna play with your tits now.\"":
            if hermione.is_worn("top"):
                nar "You reach out swiftly to grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly to grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly to grab both of her tits..." #Fallback, she'd usually wear a bra on this level.

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt a little.\"":
            nar "You reach out and place your hand on her butt cheeks..."

            jump hg_pf_grope_ass_T3

label hg_pf_grope_T3_E1:
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "How would you like to earn some house points today?" ("base", xpos="far_left", ypos="head")
    her "And what would I need to do to earn them?" ("annoyed", "narrow", "annoyed", "mid")
    gen "Get squeezed!" ("grin", xpos="far_left", ypos="head")
    her "Squeezed......?" ("annoyed", "narrow", "angry", "R")
    gen "Come here, and I'll show you." ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "angry", "down")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    her "[name_genie_hermione].....?" ("annoyed", "narrow", "angry", "R", ypos="head", flip=False)
    gen "..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna molest your tits now.\"":
            if hermione.is_worn("top"):
                nar "You reach out swiftly and grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly and grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly and grab both of her tits..." #Fallback, she'd usually wear a bra on this level.

            jump hg_pf_grope_breasts_T3

        "\"I'm gonna play with your butt a little.\"":
            nar "You reach out and place your hand on her butt cheeks..."

            jump hg_pf_grope_ass_T3

### Tier 4 ###

# Event 1 (i) - Hermione enjoys it.
# Event 2 (i) - Hermione asks if you are going to grope her tits or her ass.
# Event 2 (i) - Hermione enjoys it.

label hg_pf_grope_T4_intro_E1:
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "Would you like to join me again?" ("base", xpos="far_left", ypos="head")
    gen "Behind my desk." ("grin", xpos="far_left", ypos="head")
    her "Are you going to grope me again, [name_genie_hermione]?" ("soft", "narrow", "base", "mid_soft")
    gen "You just read my mind!" ("grin", xpos="far_left", ypos="head")
    her "..................." ("disgust", "narrow", "base", "down")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    her "[name_genie_hermione].....?" ("base", "narrow", "worried", "down", ypos="head", flip=False)
    gen "..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna molest your tits now.\"":
            if hermione.is_worn("top"):
                nar "You reach out swiftly to grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly to grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly and grab both of her tits..."

            jump hg_pf_grope_breasts_T4

        "\"I'm gonna play with your butt a little.\"":
            nar "You reach out and place your hand on her butt cheeks..."
            jump hg_pf_grope_ass_T4

label hg_pf_grope_T4_intro_E2:
    gen "[name_hermione_genie]. Come here and join me..." ("base", xpos="far_left", ypos="head")
    gen "I feel like playing with you a little." ("grin", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..." ("soft", "base", "base", "R")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    her "[name_genie_hermione].....?" ("soft", "narrow", "worried", "down", ypos="head", flip=False)
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    her "Are you going to grope my breasts again?" ("soft", "base", "base", "mid")
    her "Or my bum?...." ("soft", "narrow", "base", "mid_soft")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna play with your tits today.\"":
            her "Of course, [name_genie_hermione]." ("base", "narrow", "worried", "down")

            if hermione.is_worn("top"):
                nar "You reach out swiftly to grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly to grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly and grab both of her tits..."

            jump hg_pf_grope_breasts_T4

        "\"I'm gonna play with your butt today.\"":
            her "Of course, [name_genie_hermione]." ("base", "narrow", "worried", "down")
            nar "You reach out and place your hand on her butt cheeks..."
            jump hg_pf_grope_ass_T4

label hg_pf_grope_T4_E2:
    gen "[name_hermione_genie]. Come here and let me grope you!" ("grin", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]..." ("soft", "narrow", "base", "mid_soft")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe")

    call her_chibi_scene("behind_desk_front", trans=fade)
    pause.5

    her "Are you going to grope my breasts today, [name_genie_hermione]?" ("soft", "narrow", "base", "R_soft", ypos="head", flip=False)
    her "Or my bum?...." ("soft", "narrow", "base", "mid_soft")

    gen "*Hmm*... What would you like?" ("base", xpos="far_left", ypos="head")

    random:
        her "I wouldn't mind it if you massaged my breasts a little..." ("soft", "narrow", "base", "R_soft")
        her "I wouldn't mind it if you caressed my bum a bit, [name_genie_hermione]..." ("soft", "narrow", "worried", "down")
        her "I wouldn't mind either today, [name_genie_hermione]." ("soft", "narrow", "base", "R_soft")

    gen "Very well then..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'm gonna molest your tits now.\"":
            her "Yes, [name_genie_hermione]." ("base", "narrow", "annoyed", "up")

            if hermione.is_worn("top"):
                nar "You reach out swiftly to grab both of her tits through her clothes..."
            elif hermione.is_worn("bra"):
                nar "You reach out swiftly to grab both of her tits through her bra..."
            else:
                nar "You reach out swiftly and grab both of her tits..."

            jump hg_pf_grope_breasts_T4

        "\"I'm gonna play with your butt now.\"":
            her "Yes, [name_genie_hermione]." ("open", "narrow", "annoyed", "down")
            nar "You reach out and place your hand on her butt cheeks..."

            jump hg_pf_grope_ass_T4
