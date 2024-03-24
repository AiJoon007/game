

### Luna Inspect Body ###

label ll_pf_inspect:

    if not _events_completed_any:
        gen "{size=-4}(I think a physical examination is in order...){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump luna_favor_menu
    return

label ll_pf_inspect_end:

    # Setup
    stop music fadeout 2.0
    call hide_characters

    call lun_chibi("stand", flip=False)
    call gen_chibi("sit_behind_desk")

    # Increase level
    if states.lun.tier == 2:
        if states.lun.level < 6:
            $ states.lun.level += 1

    elif states.lun.tier == 3:
        if states.lun.level < 9:
            $ states.lun.level += 1

    jump end_luna_event

### Tier 2 ###

label ll_pf_inspect_T2_E1_intro:

    call ll_pf_inspect

    gen "Ready for your physical, [name_luna_genie]?" ("grin", xpos="far_left", ypos="head")
    lun "My physical, [name_genie_luna]?" ("open", "base", "raised", "mid")
    gen "Your inspection!" ("grin", xpos="far_left", ypos="head")
    lun "Oooh...{w=0.3} The inspection!" ("grin", "base", "base", "mid")
    lun "Yes, I'm ready!" ("base", "base", "base", "mid")
    gen "Great...{w=0.4} Then you can begin undressing." ("base", xpos="far_left", ypos="head")
    lun "Alright, just give me a--" ("grin", "base", "base", "down")
    gen "Wait...{w=0.4} Before you do that." ("base", xpos="far_left", ypos="head")

    $ states.gen.masturbating = True
    $ states.gen.stats.masturbated_to_luna += 1
    hide luna_main
    nar "You take your cock out of your robes and begin stroking it..."
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause .8

    gen "There we go... Might as well." ("base", xpos="far_left", ypos="head")
    lun "Good thinking, [name_genie_luna]!" ("crooked_smile", "narrow", "base", "mid")
    gen "Right... Now to give you a full assessment of your goods...{w=0.4} *Err*...{w=0.4} Orifices." ("base", xpos="far_left", ypos="head")
    if luna.is_any_worn("robe", "accessory"):
        lun "Of course [name_genie_luna]... Let me just take this off..." ("base", "base", "base", "mid")

        play sound "sounds/cloth_sound3.ogg"
        $ luna.strip("robe", "accessory")
        with d3
        pause .5

        gen "Great." ("base", xpos="far_left", ypos="head")
    if luna.is_worn("top"):
        gen "Now then..." ("base", xpos="far_left", ypos="head")
        gen "Let's start with your breasts." ("base", xpos="far_left", ypos="head")
        gen "Take that top off for me, will you." ("base", xpos="far_left", ypos="head")
        lun "Of course, [name_genie_luna]." ("base", "base", "base", "mid")

        #Luna takes top off
        play sound "sounds/cloth_sound3.ogg"
        $ luna.strip("top")
        with d3
        pause .5

        gen "Excellent...{w=0.4} And such a lovely pair of breasts as well." ("base", xpos="far_left", ypos="head")

        $ states.lun.status.show_bra = True
    else:
        gen "Let's see what we got here..." ("base", xpos="far_left", ypos="head")
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        lun "Something wrong, [name_genie_luna]?" ("soft", "base", "raised", "mid")
        gen "Not at all, [name_luna_genie]!" ("base", xpos="far_left", ypos="head")
        gen "I'm just inspecting those lovely breasts of yours!" ("base", xpos="far_left", ypos="head")
    lun "*Ehm*...{w=0.3} Lovely, [name_genie_luna]?" ("soft", "base", "raised", "mid")
    gen "*Err*...{w=0.4} Healthy! They look very healthy!" ("base", xpos="far_left", ypos="head")
    lun "I see...{w=0.4} Thank you [name_genie_luna]!" ("grin", "base", "base", "mid")
    gen "But I still need a proper look, so you're going to have to take your bra off as well." ("base", xpos="far_left", ypos="head")
    lun "Certainly [name_genie_luna]." ("base", "base", "base", "mid")

    #Luna takes bra off (Not possible in wardrobe until next tier)
    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bra")
    with d3
    pause .5

    $ states.lun.status.show_tits = True

    gen "(Nice...)" ("base", xpos="far_left", ypos="head")

    nar "*Fap* *Fap* *Fap*..."

    lun "So...{w=0.4} Do you think this should work, [name_genie_luna]?" ("open", "base", "raised", "mid")
    gen "Oh...{w=0.4} It's working alright." ("grin", xpos="far_left", ypos="head")

    nar "Focusing your attention on the girl's breasts, you feel your cock harden more and more with each stroke..."

    lun "Great! So, what do I have to do to get the Wrackspurts out of them?" ("smile", "base", "base", "mid")
    gen "*Mmm*...{w=0.4} The what, sorry?" ("base", xpos="far_left", ypos="head")
    lun "The Wrackspurts, [name_genie_luna]..." ("open", "base", "raised", "mid")
    gen "*Ah*...{w=0.4} Those bloody things." ("base", xpos="far_left", ypos="head")
    gen "Let's see..." ("base", xpos="far_left", ypos="head")
    gen "Tell...{w=0.4} *Ngh*...{w=0.4} Tell me a bit about them..." ("base", xpos="far_left", ypos="head")
    lun "Well... As I said, they're invisible--" ("soft", "closed", "base", "mid")
    gen "Not the spurts! Your breasts, [name_luna_genie]!" ("base", xpos="far_left", ypos="head")
    lun "Ooooh...{w=0.2} What do you need to know about them, [name_genie_luna]?" ("mad", "base", "base", "mid")
    gen "(How much do they jiggle-- How hard can I pull on your-- What do they taste--)" ("grin", xpos="far_left", ypos="head")

    lun "" ("upset", "base", "raised", "mid") #Confused
    nar "*Fap* *Fap* *Fap*..."
    nar "You pick up the pace whilst staring at her tits... An expression of confusion spreading across Luna's face as she waits for a response..."

    lun "[name_genie_luna]?" ("open", "base", "raised", "mid")
    gen "What?!" ("angry", xpos="far_left", ypos="head")
    gen "Oh yes...{w=0.3} Your tits!" ("grin", xpos="far_left", ypos="head")
    gen "It appears the Spurts gather around sensitive areas..." ("base", xpos="far_left", ypos="head")
    gen "So with that in mind..." ("base", xpos="far_left", ypos="head")
    gen "Would you say that your breasts fit that description, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "*Hmm*...{w=0.4} Well, my nipples do get a bit hard and sensitive whenever they bothered me previously..." ("open", "narrow", "base", "downL")
    lun "Is that the kind of thing you meant, [name_genie_luna]?" ("soft", "base", "raised", "mid")
    gen "*Ah*... Yes, that's exactly it..." ("base", xpos="far_left", ypos="head")

    nar "You move your gaze and focus on Lunas erect nipples...{w=0.3} Your cock twitching slightly in your grasp."
    nar "*Fap* *Fap* *Fap*..."

    gen "*Hmm*...{w=0.4} They do look a bit hard actually..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "They do?" ("disgust", "base", "base", "mid")
    lun @ cheeks blush "I've been trying to suppress it the best I can, [name_genie_luna]!" ("clench", "closed", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "Well, that won't do." ("base", xpos="far_left", ypos="head")
    gen "Fighting it is what's been holding you...{w=0.4} *Err*...{w=0.4} Them back, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    gen "You need to allow that feeling to build up, or you--{w=0.2} *Ah*...{w=0.4} You won't be able to expel them." ("base", xpos="far_left", ypos="head")

    nar "You keep stroking your cock, thinking about what you'd do to those nipples..."

    lun @ cheeks blush "Wait...{w=0.4} So I've been doing it wrong the whole time!?" ("angry", "base", "base", "mid")
    gen "Yes...{w=0.4} *Nghh*...{w=0.4} It appears what you've been feeling is the Spurts trying to get out, you see..." ("base", xpos="far_left", ypos="head")
    lun "Ooooh..." ("open", "base", "base", "stare")
    lun "That makes so much sense!" ("grin", "wide", "base", "mid")
    lun @ cheeks blush "I can't believe I didn't think of that before!" ("angry", "base", "base", "down")

    nar "Looking up at Luna's face, you notice her expression has changed to that of excitement and lust..."
    nar "After a moment of silence, you finally speak up, in fear of not being able to finish in time."

    gen "*Ehm*...{w=0.4} So...{w=0.4}  Any other areas that you've noticed being unusually sensitive, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh, yes [name_genie_luna]!" ("mad", "base", "base", "mid")
    lun @ cheeks blush "There's this area down here!" ("angry", "base", "base", "down")

    call lun_walk("desk", "base", speed=1.75)
    pause .5
    call lun_chibi(flip=True)
    pause .5

    #Luna takes her Bottoms, panties and everything else off
    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("clothes")
    with d3
    pause .5

    $ states.lun.status.show_pussy = True
    $ states.lun.status.stripping = True

    gen "By the great--" ("angry", xpos="far_left", ypos="head")

    lun @ cheeks blush "Do you think I'll be able to expel them from here, [name_genie_luna]?" ("open", "base", "raised", "mid", flip=True)

    show CG lun_intro luna bendover naked as cg zorder 17:
        subpixel True
        zoom 0.5
        pos (0, 0)
        easein_quad 15.0 zoom 1.0 pos (-1040, -600)
    with fade

    gen "[name_luna_genie]!"
    lun "[name_genie_luna]?"
    gen "*Ahem*...{w=0.4} Yes, I'd say that area is definitely a contender."

    nar "With a full view of the girl's naked body, you feel your cock throbbing in your hand, and you begin stroking it even faster..."

    lun "I thought it might be...{w=0.4} It does get just as sensitive as my breasts...{w=0.4} Maybe more even!"

    nar "*Fap* *Fap* *Fap*..."

    gen "*Ah*, Yes...{w=0.4} both of those areas do appear to be very susceptible...{w=0.4} To spurts."
    lun "I knew it!"

    lun @ cheeks blush "" ("grin", "base", "base", "mid", flip=False)
    call hide_characters
    call lun_chibi(flip=False)
    hide cg
    with fade

    nar "Luna turns back around, and as you get a full view of her front, you feel yourself getting close to the edge."

    lun @ cheeks blush "So that's how you came up with the idea of rubbing your penis, [name_genie_luna]!" ("grin", "wink", "base", "mid", trans=dissolve)
    lun @ cheeks blush "To bait the Wrackspurts to one spot!" ("crooked_smile", "base", "base", "mid")
    lun @ cheeks blush "Since your penis is a sensitive area, rubbing it gets the Wrackspurts all excited..." ("smile", "closed", "base", "mid")

    nar "*Fap* *Fap* *Fap*..."

    lun @ cheeks blush "So when you do it, they all start gathering in there until there's nowhere else for them to go, and finally..." ("smile", "narrow", "base", "mid")
    lun @ cheeks blush "You expel them right out!" ("grin", "base", "annoyed", "mid")
    gen "*Ah*...{w=0.4} Yes...{w=0.4} That's it girl, you've cracked it!" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "That's geni--" ("crooked_smile", "base", "base", "mid")
    gen "{size=+5}I'm cumming!{/size}" ("angry", xpos="far_left", ypos="head")

    call gen_chibi("cum_behind_desk")
    call cum_block

    gen "{size=-5}*Argh*! YES!{/size}" ("angry", xpos="far_left", ypos="head")

    call cum_block

    lun @ cheeks blush "[name_genie_luna], you did it again!" ("grin", "base", "base", "stare")
    lun @ cheeks blush "I can't believe it!" ("grin", "base", "base", "mid")

    call cum_block
    pause .5
    call gen_chibi("cum_behind_desk_done")

    gen "*Ah*...{w=0.4}*Ah*...{w=0.4} What..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Cumming...{w=0.4} You came again!" ("base", "happyCl", "base", "mid")
    gen "*Ah*...{w=0.4} I sure did..." ("base", xpos="far_left", ypos="head")
    gen "Your naked body was enough for me to--" ("grin", xpos="far_left", ypos="head")
    lun @ cheeks blush "My naked body helped you release the spurts?" ("mad", "base", "base", "mid")
    gen "It...{w=0.4} *Ah*...{w=0.4} Yes, it appears so..." ("grin", xpos="far_left", ypos="head")
    lun @ cheeks blush "What did it feel like?" ("mad", "wide", "base", "mid")
    gen "Like the biggest relief--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Can I try it now?" ("smile", "wide", "base", "mid")

    menu:
        "\"Of course!\"":
            lun @ cheeks blush "Yay!" ("crooked_smile", "happyCl", "base", "mid")
            gen "Although..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Although?" ("mad", "narrow", "base", "mid")
            gen "Well, how would I be sure you're ready for it...{w=0.4} What if you hurt yourself?" ("base", xpos="far_left", ypos="head")

        "\"No!\"":
            lun @ cheeks blush "What?!" ("mad", "base", "base", "mid")
            lun @ cheeks blush "Why not!?" ("angry", "narrow", "annoyed", "mid")
            gen "*Err*...{w=0.5} Because it's dangerous!" ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "But [name_genie_luna]! You've done it yourself a couple of times already!" ("angry", "base", "base", "mid")
    gen "Actually..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "And it didn't look very complicated..." ("annoyed", "narrow", "annoyed", "mid")
    gen "Well. I can assure you..." ("base", xpos="far_left", ypos="head")
    gen "Tricking those spurts is not an easy task!" ("base", xpos="far_left", ypos="head")
    gen "As I said, you could end up with some severe burns!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "But didn't you just--" ("angry", "base", "base", "mid")
    gen "I am a master baiter, [name_luna_genie]!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("mad", "narrow", "base", "downL") #wide eyed
    gen "Nobody but I have successfully been able to bait those--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Then what am I supposed to do?!" ("angry", "base", "base", "mid")
    lun @ cheeks blush "If I don't expel them soon..." ("mad", "base", "base", "downL")
    lun @ cheeks blush "I'll go crazy!" ("clench", "wide", "base", "mid") #Crazy stare
    gen "..." ("angry", xpos="far_left", ypos="head")

    nar "Luna starts grinding her legs together uncomfortably..."

    gen "Well perhaps--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I know!" ("smile", "wide", "base", "mid")
    lun @ cheeks blush "[name_genie_luna]...{w=0.2} Why don't you teach me?" ("smile", "base", "base", "mid")
    gen "..." ("grin", xpos="far_left", ypos="head")
    gen "*Hmm*... I don't know, [name_luna_genie]..." ("grin", xpos="far_left", ypos="head")
    lun @ cheeks blush "[name_genie_luna], please!" ("mad", "narrow", "base", "mid")
    hide luna_main
    with d3

    #Luna teleports up to genie
    play sound "sounds/magic4.ogg"
    call lun_chibi("stand", 230, 455, flip=True)
    with flash

    gen "*Ghk*... How did you--" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "[name_genie_luna], if I can't do it myself, then you'll {size=+5}have{/size} to teach me!" ("clench", "wide", "base", "stare", xpos="mid", ypos="base", flip=True, trans=dissolve)
    gen "Teach you how to masturbate..." ("base", xpos="far_left", ypos="head")

    nar "Luna stares into your eyes as she unconsciously begins grinding her pussy on the edge of your desk."

    lun @ cheeks blush "Yes, teach me [name_genie_luna]!" ("angry", "wide", "base", "mid")
    lun @ cheeks blush "I want to be a master baiter too!" ("angry", "happyCl", "base", "mid")

    nar "Luna's cheeks burns with red as she keeps grinding on the edge of your desk."

    gen "(Poor girl is literally edging...)" ("base", xpos="far_left", ypos="head")
    gen "Alright, you have convinced me, [name_luna_genie]... I'll do it!" ("base", xpos="far_left", ypos="head")

    nar "Luna stops her grinding, and begins jumping happily on the spot. Her tits bouncing up and down as she does so."

    lun @ cheeks blush "Oh, thank you [name_genie_luna]!" ("grin", "narrow", "base", "mid")
    lun @ cheeks blush "I knew I could count on you!" ("grin", "closed", "base", "mid")
    gen "Certainly..." ("grin", xpos="far_left", ypos="head")
    gen "But first things first...{w=0.4} I need something from you, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Something from me?" ("soft", "narrow", "raised", "mid")
    gen "Yes, I need a promise." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh..." ("angry", "base", "base", "mid")
    lun @ cheeks blush "Alright then!" ("soft", "base", "base", "mid")
    gen "I haven't even told you what it is yet." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Don't worry [name_genie_luna], I trust you!" ("grin", "narrow", "base", "mid")
    gen "If we're to be able to have you expel these spurts successfully, then you're going to have to venture into an entirely new venue of magic..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "New venue of magic..." ("angry", "base", "raised", "mid")
    lun @ cheeks blush "I'm not sure I understand, [name_genie_luna]." ("soft", "narrow", "base", "mid")
    gen "As you know... These techniques are untested and go beyond the normal boundaries of magical conventions." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Right." ("soft", "narrow", "base", "downL")
    gen "It's not the type of magic where you'll have a use for a wand..." ("base", xpos="far_left", ypos="head")
    gen "(Unless it has a vibrate function.)" ("grin", xpos="far_left", ypos="head")
    lun @ cheeks blush "I understand..." ("open", "narrow", "base", "downL")
    gen "There will be no use for any incantations!" ("base", xpos="far_left", ypos="head")
    gen "Barring a safe word or two." ("base", xpos="far_left", ypos="head")
    gen "So you must promise not to tell anyone about what happens in this room, no matter what." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "But..." ("clench", "base", "base", "mid")

    nar "Luna rocks her pelvis awkwardly..."

    gen "That is my only requirement..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Nngh*...{w=0.4} Alright then." ("clench", "closed", "base", "downL")
    lun @ cheeks blush "I solemnly swear that I will tell no one what happens within these hallowed walls..." ("mad", "closed", "base", "mid")
    gen "Fantastic!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "So, can we please try your techniques, [name_genie_luna]?" ("angry", "narrow", "base", "mid")
    gen "Another time, [name_luna_genie]... I'll need to recharge--{w=0.4} *Err*...{w=0.4} Contain these spurts first." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "But [name_genie_luna]..." ("clench", "base", "base", "mid") #Looks down blushing
    gen "..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Alright..." ("upset", "base", "base", "downL")
    gen "Now- Now... This is a good thing, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    gen "Remember what we've learned... The more excited and sensitive you feel, the easier it'll be to spurt...{w=0.3} *Err*...{w=0.4} Expel the spurts!" ("base", xpos="far_left", ypos="head")
    lun "Oh, that is true!" ("soft", "base", "base", "mid")
    gen "Now, until next time... I want you to do your best to not suppress that feeling." ("base", xpos="far_left", ypos="head")
    gen "Embrace it...{w=0.4} Let it flow over you." ("base", xpos="far_left", ypos="head")
    lun "Yes, [name_genie_luna]." ("base", "base", "base", "mid")
    gen "Just make sure not to touch yourself." ("base", xpos="far_left", ypos="head")
    gen "That will have to wait until I can assist you." ("base", xpos="far_left", ypos="head")
    lun "Alright... I'll try..." ("mad", "narrow", "base", "downL")
    gen "Trying won't be enough, [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Don't...{w=0.4} Touch...{w=0.4} Yourself..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Okay, I won't!" ("angry", "base", "base", "mid")
    gen "Good...{w=0.3} Then I believe we're done here... For now at least." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh...{w=0.2} Of course." ("soft", "base", "base", "downL")

    show screen blkfade
    with d5

    play sound "sounds/cloth_sound.ogg"
    $ luna.wear("all")
    call lun_chibi("stand", "desk", "base")
    hide luna_main
    with fade
    pause 2

    hide screen blkfade
    with d5

    lun "" ("base", "base", "base", "mid", xpos="base", ypos="base", flip=False, trans=dissolve)
    pause .2

    if game.daytime:
        gen "You better head back to class, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        lun "Okay." ("open", "base", "base", "mid")
        lun "Good day then, [name_genie_luna]!" ("base", "base", "base", "mid")
    else:
        gen "Now, you better head off to bed." ("base", xpos="far_left", ypos="head")
        lun "Okay." ("open", "base", "base", "mid")
        lun "Good night, [name_genie_luna]!" ("base", "base", "base", "mid")
        gen "Good night, [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(Poor girl doesn't even know how to masturbate.)" ("base", xpos="far_left", ypos="head")
    gen "(How did this school even function without me...)" ("base", xpos="far_left", ypos="head")

    jump ll_pf_inspect_end

label ll_pf_inspect_T2_E2_intro:

    call ll_pf_inspect

    gen "Alright, time to give those spurts a run for their money..." ("base", xpos="far_left", ypos="head")
    lun "Finally!" ("clench", "narrow", "base", "down")
    gen "Now, are you sure you're ready for this--" ("base", xpos="far_left", ypos="head")

    if luna.is_any_worn("robe", "accessory"):
        play sound "sounds/cloth_sound3.ogg"
        $ luna.strip("robe", "accessory")
        with d3
        pause .5

        gen "*Err*..." ("base", xpos="far_left", ypos="head")
    if luna.is_worn("top"):
        play sound "sounds/cloth_sound3.ogg"
        $ luna.strip("top")
        with d3
        pause .5

        gen "Whoa!" ("angry", xpos="far_left", ypos="head")
    #Luna takes off Bra (Not possible in wardrobe until next tier)
    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bra")
    with d3
    pause .5

    gen "[name_luna_genie]!" ("base", xpos="far_left", ypos="head")
    lun "..." ("angry", "narrow", "base", "down") # looks up at genie
    gen "Now that's the kind of self-determination I've been looking for!" ("grin", xpos="far_left", ypos="head")
    gen "Check out those tits!" ("grin", xpos="far_left", ypos="head")

    if luna.is_worn("bottom"):
        play sound "sounds/cloth_sound3.ogg"
        $ luna.strip("bottom")
        with d3
        pause .5

    gen "*Hmm*... Those panties though...{w=0.4} I'd love to smell them..." ("grin", xpos="far_left", ypos="head")

    #Luna takes off Panties and everything else (Panty strip is not possible in wardrobe until next tier)
    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("clothes")
    with d3
    pause .5

    gen "And that pussy... What I'd do to stick my cock in--" ("grin", xpos="far_left", ypos="head")
    gen "*Err*..." ("angry", xpos="far_left", ypos="head")
    gen "I mean I can't wait to--" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "Please [name_genie_luna], they've been bothering me constantly..." ("angry", "narrow", "worried", "mid")
    gen "(Oh good, she wasn't listening...)" ("base", xpos="far_left", ypos="head")
    gen "Well, I hope you've followed my instructions, and that you haven't touched yourself..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I...{w=0.4} I haven't, [name_genie_luna]!" ("soft", "happyCl", "base", "mid")

    nar "Luna grinds her legs together once more, and you notice a wet streak beginning to run down her leg."

    gen "Good girl..." ("base", xpos="far_left", ypos="head")
    gen "Then come up to me, so we can deal with those spurts, once and for all." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Thank you [name_genie_luna]..." ("angry", "narrow", "base", "mid")

    #Luna quickly walks up towards desk, fades to black
    call lun_walk("desk", "base", speed=1.75)
    show screen blkfade
    with d5

    nar "Luna rushes up to your desk, and without any further instructions, plants her cheeks firmly in your lap, waiting for your next move expectantly."

    #Fades back to Luna in your lap
    call lun_chibi_scene("inspect_idle_naked")
    hide screen blkfade
    with d5

    nar "Before moving on, you can't help but pick up the sounds of her shallow breaths and the unusual warmth, despite her current state of undress, coming off her body."
    nar "You feel your cock harden slightly beneath your robes, almost at the verge of pressing up in between the girl's cheeks."
    gen "*Ahem*...{w=0.4} So...{w} The sensitive areas we discussed previously." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Mmm*..." ("soft", "closed", "low", "mid", xpos="mid", ypos="base", flip=True, trans=dissolve)
    gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "(His breath on the back of my neck... It's making me all tingly again...)" ("soft", "closed", "worried", "mid")
    gen "Luna?" ("base", xpos="far_left", ypos="head")
    gen "I guess we'll start with your breasts then..." ("grin", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_grope_breasts_naked")
    with d3
    pause 2
    call lun_chibi_scene("inspect_idle_naked")
    with d3

    lun @ cheeks blush "Ooooh!" ("open", "wide", "base", "stare")
    nar "You give Luna's breasts a light squeeze, which causes a shudder to go down her spine..."
    gen "How did that feel?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ehm*..." ("soft", "narrow", "base", "down")
    gen "Good?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I...{w=0.4} Yes...{w=0.4} I wasn't sure if good was the right word--" ("mad", "base", "base", "down")
    gen "Excellent...{w=0.4} Then focus on that feeling..." ("base", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_grope_breasts_naked")

    nar "You begin kneading Luna's breasts... Her nipples firmly locked between your fingers."

    lun @ cheeks blush "*Ah*..." ("open", "happyCl", "low", "mid")
    lun @ cheeks blush "[name_genie_luna]...{w=0.4} I think it's working...{w=0.4} I feel a lot more sensitive than before..." ("soft", "happyCl", "base", "mid")
    gen "Good...{w=0.4} That means the spurts are building up." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.4} Finally...{w=0.4} Keep going, [name_genie_luna]..." ("angry", "happyCl", "base", "stare")

    nar "As you continue, Luna tightens her thighs around your legs, and subconsciously pushes her ass back towards your abdomen."
    nar "Her cheeks lightly grace your hardening cock, and as they do, the tip of your cock manages to wiggle its way out of your robes."

    lun @ cheeks blush "*Mmm*...{w=0.4} [name_genie_luna]..." ("base", "closed", "base", "mid")
    gen "You're doing a great job [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Make sure to keep focusing on that feeling." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "But [name_genie_luna], I think I feel the wrackspurts--" ("mad", "closed", "annoyed", "mid")

    nar "You stop your kneading and give her another squeeze, just slightly harder than previously."

    lun @ cheeks blush "*Ah*..." ("grin", "closed", "base", "L")

    nar "And as you do, Luna clenches her butt-cheeks around the bottom of your shaft, the tip of your penis now sticking out of your robes right above her tailbone."

    lun @ cheeks blush "I--" ("soft", "closed", "base", "mid")

    nar "You run your fingers along the sides of her breasts, lightly brushing against her."

    lun @ cheeks blush "*Ah*...{w=0.4} Yes, it definitely feels a lot more intense than...{w=0.4} *Mmm*..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "But I'm not feeling that--{w=0.2} *Ah*...{w=0.4} Relief you mentioned..." ("mad", "closed", "base", "mid")
    lun @ cheeks blush "My body still feels as if--{w=0.2} *Ah*...{w=0.4} As if I'm on fire, [name_genie_luna]..." ("angry", "happyCl", "base", "mid")

    nar "Luna gives up to the sensation, and starts rubbing her ass against you... The tip of your cock sliding between her ass-cheeks with each thrust."

    gen "(If this keeps going, then this bitch in heat will make me bust before she does...)" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "I think something is happening...{w=0.4} I feel woozy, [name_genie_luna]..." ("angry", "happyCl", "low", "mid")

    call lun_chibi_scene("inspect_lean_grope_breasts_naked")
    nar "Luna slumps forward slightly...{w=0.4} Her ass-cheeks, now fully embracing the bottom of your shaft."

    lun @ cheeks blush "(Is...{w=0.4} Is that his...)" ("clench", "narrow", "base", "downL")

    call lun_chibi_scene("inspect_grope_breasts_naked")
    nar "Arching her back up again, Luna's cheeks slide over your cock once more, which is enough to bring you over the edge."

    gen "*ARGH*!!!" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "" ("clench", "narrow", "base", "stare") #surprised
    pause .5
    gen "(You've done it now slut!)" ("angry", xpos="far_left", ypos="head")
    gen "(Take this!)" ("angry", xpos="far_left", ypos="head")

    call cum_block

    call lun_chibi_scene("inspect_idle_naked")
    nar "With a rush of pleasure, you unload a torrent of semen across Lunas back, completely covering it with your seed."

    lun @ cheeks blush "(What's he--)" ("clench", "narrow", "base", "R") #Pleasure/confused

    gen "*Ah*!!!" ("angry", xpos="far_left", ypos="head")
    call cum_block

    nar "And with a soft groan, you let out a final spurt, emptying your entire sack on the girl..."
    nar "Your semen, which reached all the way up onto her hair, slowly begins sliding down her back."

    gen "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "[name_genie_luna], I think...{w=0.4} I feel a bit faint..." ("mad", "narrow", "low", "down")
    gen "*Ah*...{w=0.4} No, you just need to--{w=0.2} *Ah*...{w=0.4} To push through--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "No [name_genie_luna]...{w=0.4} It's as if a chill is going down my spine...{w=0.4} It doesn't feel right." ("clench", "wide", "base", "stare")
    lun @ cheeks blush "It's nowhere near the feeling of relief that you described..." ("disgust", "narrow", "base", "stare")
    gen "*Err*...{w=0.4} Well I--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I think I need to--" ("disgust", "narrow", "base", "down")
    gen "No, wait!" ("angry", xpos="far_left", ypos="head")

    show screen blkfade
    with d5

    nar "Luna, now shaking slightly, stands up and makes her way to the front of your desk, leaving a noticeable wet streak across your robes."
    nar "She begins dressing herself, keeping her eyes on the floor the entire time."
    $ luna.wear("all")
    hide luna_main

    call lun_chibi("stand", "desk", "base")
    call lun_chibi_scene("reset")
    hide screen blkfade
    with d5
    #Fade back to Luna in front of your desk.

    gen "*Ehm*...{w=0.4} So..." ("base", xpos="far_left", ypos="head")

    nar "Luna shuffles uncomfortably and then glances up at you, seemingly unable to find what to say..."

    gen "(Good job me...{w=0.4} I have royally fucked it up this time.)" ("base", xpos="far_left", ypos="head")
    gen "Look, accidents happen to the best of--" ("base", xpos="far_left", ypos="head")
    lun "I'm sorry [name_genie_luna]!" ("angry", "narrow", "worried", "mid", xpos="base", ypos="base", flip=False, trans=dissolve)
    gen "..." ("angry", xpos="far_left", ypos="head")
    lun "You were right..." ("upset", "narrow", "worried", "down")
    lun "I guess I wasn't ready..." ("open", "closed", "worried", "down")
    gen "What are you--" ("base", xpos="far_left", ypos="head")
    lun "I was so sure that we'd be able to do it..." ("angry", "narrow", "worried", "down")
    gen "*Err*...{w=0.3} Do \"it\", [name_luna_genie]?" ("base", xpos="far_left", ypos="head")

    lun "Cum, [name_genie_luna]..." ("soft", "narrow", "worried", "mid")
    gen "Oh!" ("base", xpos="far_left", ypos="head")
    gen "Well, it was your first time...{w=0.3} It's not that uncommon for it to end prematurely..." ("base", xpos="far_left", ypos="head")
    lun "It's not, [name_genie_luna]?" ("angry", "base", "worried", "stare")
    gen "Yes...{w=0.3} Actually it's very...{w=0.3} Very common..." ("base", xpos="far_left", ypos="head")
    gen "I wasn't expecting you to work it--{w=0.2} *Err*...{w=0.3} For it to work the first time!" ("base", xpos="far_left", ypos="head")
    gen "We'll just have to try it again some other time." ("base", xpos="far_left", ypos="head")
    lun "So you're not disappointed in me, [name_genie_luna]?" ("annoyed", "narrow", "worried", "mid") #Looks down
    gen "Of course not." ("base", xpos="far_left", ypos="head")
    gen "(Quite the opposite...)" ("base", xpos="far_left", ypos="head")
    lun "Oh...{w=0.3} Okay." ("normal", "narrow", "worried", "down") #Looks down
    lun "" ("base", "narrow", "worried", "down") #Looks down smile

    nar "Luna gives off a hopeful smile whilst still staring at her feet."
    nar "After a couple of seconds, she looks back up at you with a confused expression across her face."

    lun "[name_genie_luna]...{w=0.3} What was that cold feeling going down my spine?" ("upset", "narrow", "base", "mid")
    gen "Oh...{w=0.3} That." ("angry", xpos="far_left", ypos="head")
    gen "*Err*...{w=0.3} I wouldn't worry about that, [name_luna_genie]... It happens sometimes." ("angry", xpos="far_left", ypos="head")
    gen "Your body can do all sorts of things when you're moments away from spurting." ("angry", xpos="far_left", ypos="head")
    lun "So we actually almost did it, [name_genie_luna]?" ("clench", "narrow", "base", "mid")
    gen "We almost did \"it\" alright..." ("base", xpos="far_left", ypos="head")
    lun "*Aww*...{w=0.3} Blithering Humdinger..." ("upset", "narrow", "annoyed", "downL")
    gen "I'll give you some more pointers next time...{w=0.3} I'm sure we'll get there." ("base", xpos="far_left", ypos="head")
    lun "Okay...{w=0.3} Thank you [name_genie_luna]!" ("base", "narrow", "base", "mid") #looks at you smiling

    if game.daytime:
        lun "If I may, then I'll head back to class for today, [name_genie_luna]." ("soft", "base", "base", "R")
        gen "Certainly, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    else:
        gen "Now you best be off to bed." ("base", xpos="far_left", ypos="head")
        lun "Of course [name_genie_luna]." ("soft", "base", "base", "R")
        lun "Good night then..." ("base", "base", "base", "mid")
        gen "Good night [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_walk("door")
    lun @ cheeks blush "(Wait a second...{w=0.3} The thing I felt on my back...)" ("soft", "narrow", "base", "downL", xpos="base", ypos="base", flip=True, trans=dissolve)
    hide luna_main
    with d3

    #Luna turns to genie
    call lun_chibi(flip=False)


    gen "Yes...{w=0.3} Was there something else [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh...{w=0.3} No, that's all, [name_genie_luna]!" ("angry", "narrow", "base", "down", xpos="base", ypos="base", flip=False, trans=dissolve)


    hide luna_main
    with d3

    #Luna turns to door
    call lun_chibi(flip=True)

    gen "Off you go then..." ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "(Was me rubbing up against him enough to help with his--)" ("soft", "narrow", "base", "down", xpos="base", ypos="base", flip=True, trans=dissolve)
    lun @ cheeks blush "(Why am I suddenly so woozy again?)" ("angry", "narrow", "base", "downL")

    call lun_walk(action="leave")

    jump ll_pf_inspect_end

label ll_pf_inspect_T2_E3_intro:

    $ states.lun.ev.inspect_her_body.t2_e3_complete = True

    call ll_pf_inspect

    gen "Ready for another attempt?" ("base", xpos="far_left", ypos="head")
    lun "I...{w=0.3} Yes [name_genie_luna], I believe so..." ("open", "narrow", "base", "downL")

    #Luna walks towards desk and it fades to black
    call lun_walk("desk")
    show screen blkfade
    with d5

    nar "Luna absent-mindedly walks up and scoots in front of you."

    if luna.is_any_worn("top", "bottom", "robe"):
        call lun_chibi_scene("inspect_idle")
    else:
        call lun_chibi_scene("inspect_idle_naked")
    hide screen blkfade
    with d5

    gen "*Err*...{w=0.3} I think you've forgotten something [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "*Huh*?" ("soft", "narrow", "base", "mid", xpos="mid", ypos="base", flip=True, trans=dissolve)

    if luna.is_any_worn("top", "bottom", "robe"):
        gen "Your clothes..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Your underwear..." ("base", xpos="far_left", ypos="head")

    lun "Oh...{w=0.3} Right..." ("angry", "narrow", "base", "down")
    gen "You seem awfully distracted today." ("base", xpos="far_left", ypos="head")
    lun "*Ehm*...{w=0.3} To tell you the truth...{w=0.3} I'm a bit worried that it's not going to work again, [name_genie_luna]." ("open", "narrow", "base", "downL")
    gen "Now, I wouldn't worry about that...{w=0.3} I'm confident it will work this time." ("base", xpos="far_left", ypos="head")
    lun "But how can you be so sure, [name_genie_luna]?" ("mad", "narrow", "base", "mid")
    lun "Maybe it's different for us women, maybe we aren't able to expel the wrackspurts like you men do." ("angry", "narrow", "base", "mid")
    gen "I'm quite certain that the process isn't too dissimilar...{w=0.3} I'm confident that with my help--" ("base", xpos="far_left", ypos="head")
    lun "But {i}how{/i} do you know, [name_genie_luna]?" ("angry", "narrow", "base", "mid")
    gen "Just trust me on this one [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "*Hmm*..." ("upset", "narrow", "base", "downL")
    gen "(She doesn't seem convinced.)" ("base", xpos="far_left", ypos="head")
    gen "(Oh, wait...{w=0.3} I know!)" ("grin", xpos="far_left", ypos="head")

    gen "*Ahem*...{w=0.3} [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "Yes [name_genie_luna]?" ("upset", "base", "base", "mid")
    gen "Tell me...{w=0.3} How were those spratters described in your father's paper again?" ("base", xpos="far_left", ypos="head")
    lun "Let me think.{w=0.5} They're invisible creatures that enter inside your ears and make your brain go all fuzzy." ("angry", "base", "base", "mid")
    gen "And...{w=0.3} Wasn't there an instruction on how to expel them?" ("base", xpos="far_left", ypos="head")
    lun "Why yes, by thinking positively..." ("soft", "narrow", "base", "mid")
    lun "But that's not working, [name_genie_luna]...{w=0.3} It isn't my brain that's getting all fuzzy because of them..." ("clench", "narrow", "base", "mid")
    gen "Then tell me...{w=0.3} What else have we learned about them thus far?" ("base", xpos="far_left", ypos="head")
    lun "*Uhm*..." ("upset", "base", "base", "downR")
    lun "We have learned that you can lure them out to a particularly sensitive body area, through positive thoughts. Then, you need to rub that spot energetically to finally expel them..." ("angry", "narrow", "base", "down")
    lun "But we have already tried that [name_genie_luna], and it didn't work!" ("annoyed", "narrow", "base", "R")
    gen "I managed to do it by myself...{w=0.3} So you must have done something wrong..." ("base", xpos="far_left", ypos="head")
    lun "*Hmm*..." ("upset", "narrow", "base", "downL")
    gen "(Putting the pieces together...{w=0.3} And...)" ("base", xpos="far_left", ypos="head")
    lun "Oh! I know!" ("smile", "wide", "base", "stare")
    lun "I was possibly thinking too much about the wrackspurts, and how glad I'd be to finally get rid of them." ("mad", "wide", "base", "mid")
    lun "What I should have done instead was project positive thoughts onto the area itself!" ("smile", "narrow", "base", "down")
    gen "Exactly!" ("grin", xpos="far_left", ypos="head")
    gen "Ignore intrusive thoughts that may pop into your head, and just focus on your body, on how it feels..." ("base", xpos="far_left", ypos="head")
    gen "Let the sensations engulf you completely, until your mind is clear..." ("base", xpos="far_left", ypos="head")
    gen "Leave the rest to the fate..." ("base", xpos="far_left", ypos="head")
    lun "That's smart, [name_genie_luna], maybe I should try that." ("crooked_smile", "narrow", "base", "mid")
    gen "Now then... Ready for another try?" ("base", xpos="far_left", ypos="head")
    lun "Yes, I'm ready [name_genie_luna]!" ("base", "base", "base", "mid")

    if luna.is_any_worn("robe", "top", "bottom", "accessory"):
        gen "Let's get you out of those clothes first, shall we..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Now, let me help you get you out of those pesky undergarments..." ("base", xpos="far_left", ypos="head")

    #Fade to black
    show screen blkfade
    with d5

    if luna.is_any_worn("robe", "top", "bottom", "accessory"):
        nar "Luna shuffles around for a bit, attempting to get out of her clothing. The limited space between you and the desk is making it somewhat difficult."

        lun "It's a bit cramped in here, [name_genie_luna]...{w=0.4} Should I scoot out and--" ("base", "base", "base", "mid")
        gen "No, that won't be necessary, [name_luna_genie]...{w=0.4} Let me help you."

    if luna.is_worn("robe"):
        nar "You unclasp Luna's outerwear and let it drop to the ground behind her."

    if luna.is_worn("top"):
        nar "You swiftly pull Luna's top over her head...{w=0.4} Her breasts bounce a little, then settle still as the offending piece of clothing is taken off."
        play sound "sounds/boing02.ogg"
        pause .4

        lun "Whoa!" ("base", "base", "base", "mid")

    #Luna always wears underwear at this stage
    nar "You unhook Luna's bra with ease, and let it drop to the floor, right in front of her."
    nar "She glances back at you, her cheeks flushed, and a look of surprise painted across her face, caused by your unusual dexterity."

    lun "Have you done this before, [name_genie_luna]?" ("base", "base", "base", "mid")
    gen "Let's not make this about me, [name_luna_genie]. Free your mind of intrusive thoughts." ("base", xpos="far_left", ypos="head")
    lun "Okay, I'll try." ("soft", "base", "base", "mid")

    if luna.is_worn("bottom", "panties"):
        nar "Noticing Luna's ever-increasing excitement, you put your hands on either side of her hips, and pull both fabrics down, in one singular motion..."
        $ luna.strip("bottom", "panties")
    elif luna.is_worn("bottom"):
        nar "Noticing Luna's ever-increasing excitement, you put your hands on either side of her hips, and pull the fabric down swiftly..."
    elif luna.is_worn("panties"):
        nar "You oggle Luna's choice of underwear, before swiftly pulling them down right to her ankles..."

    lun @ cheeks blush "" ("clench", "narrow", "base", "downR")
    $ luna.strip("clothes")
    pause .2
    hide screen blkfade

    #Fade back to Naked Luna in front of genie
    call lun_chibi_scene("inspect_idle_naked")
    with d5

    lun @ cheeks blush "[name_genie_luna]!" ("clench", "narrow", "base", "downR")
    gen "Yes, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ehm*...{w=0.4} Never mind..." ("soft", "narrow", "base", "down")
    gen "Okay. In that case, let the exorcism commence--." ("base", xpos="far_left", ypos="head")
    gen "--*Err*, I mean the expulsion." ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("base", "narrow", "base", "down") #blush

    call lun_chibi_scene("inspect_grope_breasts_naked")
    nar "Without hesitation, you reach forward and grab and start fondling Luna's breasts."
    nar "As she feels your touch, any doubts in Luna's mind are washed away, letting the sensations overtake her."

    lun @ cheeks blush "*Ah*...{w=0.4} [name_genie_luna]..." ("soft", "closed", "base", "mid")

    nar "You move your attention towards Luna's sensitive areas... Gently sliding your fingers across her nipples, then across the sides of her breasts and back again."

    lun @ cheeks blush "*Mmm*..." ("normal", "closed", "base", "mid")

    nar "You continue massaging Luna's breasts and the silence is only broken by her moans as your fingers pass across her nipples."

    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Mmmm*..." ("soft", "closed", "base", "mid")

    nar "Luna, getting more and more excited by your touch, pushes her ass towards you once more."

    call lun_chibi_scene("inspect_lean_grope_breasts_naked")
    nar "As it graces your cock, you struggle not to get hard..."

    gen "(Nnnn-{w=0.2} Not today!)" ("angry", xpos="far_left", ypos="head")

    lun @ cheeks blush "" ("normal", "closed", "base", "mid")
    nar "Determined to keep your composure this time, you move your gaze down to see Luna rubbing her thighs together."

    gen "(Well then...{w=0.4} Looks like she's ready.)" ("grin", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_lean_idle_naked")
    lun @ cheeks blush "" ("soft", "narrow", "base", "R")
    nar "As you remove your hands from Luna's breasts, she opens her eyes, confused as to why you stopped."
    nar "Without saying anything, you place your hand across her pussy, and give it a gentle rub."

    lun @ cheeks blush "Ooooh!" ("crooked_smile", "wide", "base", "stare")

    call lun_chibi_scene("inspect_lean_grope_vagina_naked")
    nar "A shudder passes through Luna's body from your initial touch."
    nar "You then begin moving your forefinger up and down her slit with increasing ease, as her pussy becomes wetter and wetter."

    lun @ cheeks blush "*Ah*...{w=0.4} [name_genie_luna]...{w=0.4} This feels a lot different to you--{w=0.2} *Ah*...{w=0.4} Touching my breasts..." ("open", "wink", "base", "R")
    gen "(You ain't seen nothing yet...)" ("base", xpos="far_left", ypos="head")

    nar "As you continue rubbing her, the excitement in her voice gnaws at your steadily decreasing patience..."

    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..." ("soft", "narrow", "base", "up")
    gen "Ready, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "" ("soft", "narrow", "base", "up") #pleasure
    pause .8
    gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(Fuck it...)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/slick_02.ogg"
    with kissiris
    pause .5

    call lun_chibi_scene("inspect_lean_idle_naked")
    lun @ cheeks blush "..." ("scream", "wide", "base", "stare") #wide eyed
    lun @ cheeks blush "[name_genie_luna]!" ("scream", "base", "base", "mid")

    nar "As you penetrate Luna with your index finger, she clenches her legs together in surprise."

    lun @ cheeks blush "[name_genie_luna]...{w=0.4} Your finger slipped inside of me..." ("clench", "wide", "base", "mid")
    gen "I know..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "What do you--" ("clench", "narrow", "base", "mid")

    call lun_chibi_scene("inspect_lean_grope_vagina_naked")
    play background "sounds/slickloop.ogg" fadein 2
    nar "You begin moving your finger inside of Luna, slowly increasing the pace, her words soon replaced by the sounds of increasing pleasure."

    lun @ cheeks blush "*Ah*...{w=0.4} My word...{w=0.3} *Ah*...{w=0.4} I never...{w=0.3} *Ah*..." ("soft", "narrow", "base", "stare")
    gen "(*Hmm*...{w=0.4} Perhaps I shouldn't go so hard on her...)" ("base", xpos="far_left", ypos="head")

    stop background fadeout 2
    nar "You stop your movement for a second to give Luna some breathing room, but as you do, she starts moving her hips back and forth on her own."

    gen "(Never mind, then...)" ("grin", xpos="far_left", ypos="head")
    gen "*Tsk*... Such impatience with the youths these days..." ("grin", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("base", "narrow", "base", "up") #Looks back at you
    gen "Very well [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
    gen "In that case I won't hold back on you." ("base", xpos="far_left", ypos="head")

    play sound "sounds/slick_02.ogg"
    with kissiris

    lun @ cheeks blush "*Ah*!!!" ("scream", "wide", "base", "stare") #Wide eyed

    play background "sounds/slickloopfast.ogg"
    nar "You insert another finger and begin pumping them in and out, the walls of her pussy clinging onto your fingers with each insertion."

    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..." ("open", "happyCl", "base", "stare")

    nar "Luna, now completely lost in pleasure, begins shaking slightly, prompting you to pick up the pace even further."

    play background "sounds/slickloopveryfast.ogg"
    lun @ cheeks blush "[name_genie_luna]...{w=0.3} This...{w=0.3} is...{w=0.3} amazing...{w=0.3} I... {w=0.3} never...{w=0.3} thought--" ("soft", "happyCl", "base", "stare")
    gen "Then don't...{w=0.3} Focus on the feeling!" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.3} Yes...{w=0.3} [name_genie_luna]." ("soft", "closed", "base", "stare")
    lun @ cheeks blush "*N-n-ngh*!!!" ("grin", "closed", "base", "mid")

    nar "Not showing her any mercy, you continue pumping your fingers in and out of her rapidly."

    lun @ cheeks blush "*Ah*...{w=0.5} [name_genie_luna]...{w=0.4} I think this is it!" ("mad", "narrow", "base", "stare")
    lun @ cheeks blush "I'm...{w=0.3} *Ah*...{w=0.3} I'm--" ("open_tongue", "narrow", "base", "up")
    gen "Yes girl, let all of it out!" ("angry", xpos="far_left", ypos="head")

    nar "You insert your fingers one last time... As Luna's body finally gives in, her entire weight drops onto your hand and your fingers penetrates her down to the base."

    lun @ cheeks blush "I'm cumming!!" ("mad", "base", "base", "ahegao")
    lun @ cheeks blush "*Nngh*...{w=0.8}{nw}" ("clench", "base", "base", "ahegao")

    with kissiris
    stop background fadeout 2
    play sound "sounds/slick_01.ogg"
    lun @ cheeks blush "*Nngh*...{fast} *Ah*!" ("open_wide_tongue", "narrow", "base", "ahegao")


    call lun_chibi_scene("inspect_lean_idle_naked")
    gen "(By the great--)" ("angry", xpos="far_left", ypos="head")

    with kissiris

    play sound "sounds/slick_01.ogg"
    lun @ cheeks blush "*AAAAAH*!!!" ("crooked_smile", "narrow", "base", "ahegao")
    nar "Your fingers now locked inside of Luna, you feel her entire body spasms as wave after wave of pleasure passes through her body."
    lun @ cheeks blush "Wow...{w=0.5} That was--{w=0.8}{nw}" ("crooked_smile", "narrow", "base", "stare")

    with kissiris
    play sound "sounds/slick_01.ogg"
    lun @ cheeks blush "Wow... That was--{fast} *Ah*..." ("open", "narrow", "base", "ahegao")

    lun @ cheeks blush "*Mmm*...{w=0.4} You were right...{w=0.3} That...{w=0.3} That relief..." ("soft", "narrow", "base", "up")

    show screen blkfade
    with d5

    nar "Luna attempts to stand up, but her legs give way, and she slumps forward onto your desk, completely limp."
    nar "Luckily her grip around your fingers finally loosens enough for you to free yourself, and you swiftly pull them out, which causes her to shudder once more."

    play sound "sounds/slick_02.ogg"
    lun "*Ah*..."

    nar "Admiring your work, you watch as a streak of liquid runs down her leg before settling on the floor."

    lun @ cheeks blush "[name_genie_luna]..." ("base", "base", "base", "mid", xpos="base", ypos="base", flip=False, trans=dissolve)

    $ luna.wear("all")

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    call lun_chibi("stand", "desk", "base")
    call lun_chibi_scene("reset")
    hide screen blkfade
    with d5

    lun "[name_genie_luna], that was incredible!" ("base", "narrow", "base", "mid")
    lun "Did you see how many Wrackspurts I expelled?" ("crooked_smile", "base", "raised", "mid")
    gen "Very impressive indeed." ("base", xpos="far_left", ypos="head")
    lun "I can't believe we finally did it!" ("crooked_smile", "happyCl", "base", "mid")
    lun "Finally, a foolproof way of expelling Wrackspurts from other areas than your brain!" ("crooked_smile", "narrow", "base", "mid")
    gen "Quite the discovery! I'm sure we'll be able to help a lot of backed up people." ("grin", xpos="far_left", ypos="head")
    lun "Yes!" ("grin", "base", "base", "mid")
    lun "So, what next? We've solved it now, right?" ("grin", "base", "raised", "mid")
    gen "Solved--" ("angry", xpos="far_left", ypos="head")
    gen "Now I think you're getting a bit ahead of yourself [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "But--" ("angry", "base", "base", "mid")
    gen "Masturbation is only a temporary solution, so perfecting it is vital... Until I've come up with a more permanent solution, that is..." ("base", xpos="far_left", ypos="head")
    lun "Then I'll practice as soon as I get to my dorm!" ("smile", "narrow", "base", "mid")
    gen "No!" ("angry", xpos="far_left", ypos="head")
    gen "I need to watch--{w=0.2} *Err*...{w=0.4} Instruct you, so you can alleviate yourself properly and safely." ("base", xpos="far_left", ypos="head")
    lun "Oh, of course [name_genie_luna]!" ("mad", "base", "base", "mid")
    lun "Hopefully the Wrackspurts will leave me alone until then..." ("angry", "narrow", "base", "downL") #blush looking down
    gen "Hopefully..." ("base", xpos="far_left", ypos="head")
    gen "(Although I doubt it.)" ("base", xpos="far_left", ypos="head")

    if game.daytime:
        gen "Well then, you've got class to attend [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        gen "Off you go." ("base", xpos="far_left", ypos="head")
        lun "Yes [name_genie_luna], thank you [name_genie_luna]..." ("base", "wink", "base", "mid")
    else:
        gen "Well then, it's getting late so you best head to your dorm, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        gen "Off you go." ("base", xpos="far_left", ypos="head")
        lun "Yes [name_genie_luna]." ("base", "base", "base", "mid")
        lun "Good night, [name_genie_luna]." ("base", "wink", "base", "mid")
        gen "Good night [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    gen "(She sure is a eager one...)" ("base", xpos="far_left", ypos="head")
    nar "You look down and see something's caught onto your robes."
    gen "(*Hmm*... What's this?)" ("base", xpos="far_left", ypos="head")

    $ hair_luna_ITEM.owned = 1
    call give_reward("You found a string of blonde hair!", gift=hair_luna_ITEM)

    gen "(Looks like she's left me a parting gift.)" ("base", xpos="far_left", ypos="head")
    if states.map.snape_office.intro_e2:
        gen "Maybe I could use this for one of my potions..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Maybe I'll find some use for this later..." ("base", xpos="far_left", ypos="head")

    jump ll_pf_inspect_end

label ll_pf_inspect_T2_E4_repeat:

    call ll_pf_inspect

    gen "How are you feeling, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    gen "Have those spratters been bothering you any further?" ("base", xpos="far_left", ypos="head")
    lun "I'm feeling a little bit better, [name_genie_luna]." ("soft", "narrow", "low", "down")
    lun "Although I began feeling them move around again once I was on the way to my dorm, just thinking about our last session." ("upset", "narrow", "base", "downL")

    gen "Well, that's to be expected." ("base", xpos="far_left", ypos="head")
    gen "Until we've found a foolproof way to deal with them, I'm afraid this will have make do as a regular treatment." ("base", xpos="far_left", ypos="head")
    lun "Alright..." ("soft", "narrow", "base", "downL")
    lun "I suppose that's not too bad." ("base", "narrow", "base", "down")
    gen "Good to hear..." ("base", xpos="far_left", ypos="head")
    gen "Now then, ready for your treatment, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "Yes [name_genie_luna]..." ("grin", "base", "base", "mid")
    gen "Great, then come here, and we'll get started." ("base", xpos="far_left", ypos="head")

    #Luna walks towards desk and it fades to black
    call lun_walk("desk")
    show screen blkfade
    with d5

    $ luna.strip("clothes")

    #Fades back to Luna in your lap
    call lun_chibi_scene("inspect_idle_naked")
    hide screen blkfade
    with d5

    gen "Now then..." ("base", xpos="far_left", ypos="head")
    gen "Time to get these spratters worked up..." ("base", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_grope_breasts_naked")
    nar "You grab onto Luna's breasts and begin massaging them."

    lun "*Eeek*!!" ("clench", "wide", "base", "stare", xpos="mid", ypos="base", flip=True, trans=dissolve)
    gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "Oh...{w=0.2} Sorry, [name_genie_luna]!" ("angry", "happyCl", "base", "mid")
    lun "Your hands are a bit cold." ("angry", "narrow", "base", "stare")
    gen "Then let's get them warmed up, shall we?" ("base", xpos="far_left", ypos="head")
    nar "You spread your fingers apart and drag them across the sides of Luna's nipples, increasing your grip around them with each motion."
    lun @ cheeks blush "*Ah*..." ("soft", "closed", "base", "mid")
    gen "How's this, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    gen "Feeling any build up yet?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Mmm*...{w=0.4} Yes, [name_genie_luna]..." ("open", "closed", "base", "mid")
    gen "Good..." ("base", xpos="far_left", ypos="head")
    nar "You begin moving your hands in a circular motion, squeezing her breasts together and pulling them apart over and over..."
    lun @ cheeks blush "*Mmm*..." ("soft", "closed", "base", "mid")

    nar "Luna, whose thoughts are now enveloped by the sensations of your touch, pushes her crotch towards you once again, as if desperate to feel you inside of her..."

    call lun_chibi_scene("inspect_lean_idle_naked")
    with d3

    lun @ cheeks blush "" ("base", "closed", "base", "mid")
    gen "*Hmm*...{w=0.4} Looks like someone's eager..." ("base", xpos="far_left", ypos="head")
    gen "Very well then, [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_lean_grope_vagina_naked")
    lun @ cheeks blush "Ooooh..." ("grin", "narrow", "base", "up")
    nar "Luna shivers slightly as your hand graces her pussy..."
    nar "You notice that she's already wet, as your fingers slide across her with ease..."
    gen "Looks like someone's been looking forward to this..." ("base", xpos="far_left", ypos="head")
    gen "Better not let you wait any further then." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I--" ("base", "narrow", "base", "up")

    call lun_chibi_scene("inspect_lean_idle_naked")
    play sound "sounds/slick_02.ogg"

    with kissiris
    lun @ cheeks blush "{heart}*Ngh*{heart}..." ("crooked_smile", "narrow", "base", "up")
    gen "There we go..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "You're...{w=0.4} They're inside me again..." ("grin", "narrow", "base", "up")
    gen "Yes indeed [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
    gen "And two fingers already...{w=0.4} Looks like you're getting better at this..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh...{w=0.4} Thank--" ("soft", "narrow", "base", "stare")

    play background "sounds/slickloop.ogg" fadein 2
    call lun_chibi_scene("inspect_lean_grope_vagina_naked")

    nar "You begin pumping your fingers quickly into Luna's pussy..."
    lun @ cheeks blush "*Ah*!!!" ("clench", "base", "base", "stare")
    nar "Taken by surprise, Luna clenches her thighs, which only strengthens her grip around your fingers..."
    lun @ cheeks blush "*Ah*... [name_genie_luna]!" ("angry", "narrow", "base", "R")
    gen "That's it [name_luna_genie]...{w=0.4} Keep that grip steady, and this will be over before you know it..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} But [name_genie_luna]--" ("open", "happyCl", "base", "mid")
    nar "As you keep pumping your fingers repeatedly inside of Luna, you feel her grip loosen slightly..."
    lun @ cheeks blush "I...{w=0.4} I..." ("upset", "happyCl", "base", "mid")
    lun @ cheeks blush "{size=+5}I don't want it to be over!{/size}" ("scream", "narrow", "worried", "stare")
    gen "Too bad!" ("base", xpos="far_left", ypos="head")
    nar "Not showing any mercy on the girl, you keep pumping faster and faster in and out of her pussy."

    play background "sounds/slickloopfast.ogg"

    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} No..." ("clench", "narrow", "base", "stare")
    lun @ cheeks blush "Not yet!" ("mad", "happyCl", "base", "mid")

    play background "sounds/slickloopveryfast.ogg"

    nar "Luna, trying to keep that sensation going, tries to get a hold of herself as not to let herself cum."

    lun @ cheeks blush "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..." ("open", "happyCl", "base", "mid")

    nar "Taking it as a challenge, you insert your fingers all the way in, which proves to be enough for the girl."

    call lun_chibi_scene("inspect_lean_idle_naked")
    lun @ cheeks blush "*Ah*...{w=0.2} No...{w=0.3} I'm cumming!!" ("clench", "happyCl", "worried", "mid")

    with kissiris
    play sound "sounds/slick_01.ogg"

    lun @ cheeks blush "*AAAAAH*!!!" ("clench", "narrow", "base", "up")
    nar "Luna's thighs clench around you, as waves of pleasure washes over her."

    lun @ cheeks blush "*Ah*...{w=0.2} I'm...{w=0.2} I'm--" ("mad", "narrow", "base", "stare")

    with kissiris
    play sound "sounds/slick_01.ogg"
    stop background fadeout 2

    lun @ cheeks blush "*Ah*..." ("grin", "narrow", "base", "up")
    lun @ cheeks blush "*Mmm*..." ("base", "happyCl", "low", "up")

    show screen blkfade
    with d5

    $ luna.wear("all")

    nar "Luna, completely exhausted, slumps onto your desk once again."
    nar "You pull your chair back to give her some space."

    lun @ cheeks blush "*Mmm*..." ("base", "narrow", "base", "down", xpos="base", ypos="base", flip=False, trans=dissolve)

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    call lun_chibi("stand", "desk", "base")
    call lun_chibi_scene("reset")

    hide screen blkfade
    with d5

    gen "Well done, [name_luna_genie]!" ("base", xpos="far_left", ypos="head")
    gen "Looks like you managed to spurt even more than last time!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Mmm*...{w=0.4} Thank you, [name_genie_luna]." ("base", "closed", "base", "mid")
    gen "Holding them in for as long as possible was very clever!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh-- I...{w=0.3} Yes, thank you!" ("soft", "narrow", "base", "downR")
    gen "Are you okay, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh, yes [name_genie_luna]...{w=0.4} I'm...{w=0.3} I feel great!" ("crooked_smile", "narrow", "base", "mid")
    gen "You look exhausted, you better get some rest..." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        lun @ cheeks blush "*Ehm*...{w=0.4} I've still got classes..." ("soft", "narrow", "base", "R")
        gen "Right..." ("base", xpos="far_left", ypos="head")
        gen "Maybe I should go a bit easier on you during the--" ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "No, it's fine!" ("mad", "narrow", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "I mean... I'll be okay [name_genie_luna]..." ("soft", "narrow", "base", "mid")
        lun @ cheeks blush "Off I go then..." ("open", "narrow", "base", "R")
    else:
        gen "Off you go." ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "Alright." ("soft", "narrow", "base", "R")
        lun @ cheeks blush "Good night, [name_genie_luna]." ("base", "narrow", "base", "mid")
        gen "Good night [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    jump ll_pf_inspect_end

label ll_pf_inspect_T3_E1_repeat:

    call ll_pf_inspect

    gen "Would you like me to help you with--" ("base", xpos="far_left", ypos="head")
    lun "Yes please!" ("grin", "base", "base", "stare")

    #Luna walks towards desk and it fades to black
    call lun_walk("desk")
    show screen blkfade
    with d5

    $ luna.strip("clothes")

    #Fades back to Luna in your lap
    call lun_chibi_scene("inspect_idle_naked")
    hide screen blkfade
    with d5

    gen "You didn't even let me finish my sentence..." ("base", xpos="far_left", ypos="head")
    lun "Oh...{w=0.4} Was this not what you meant, [name_genie_luna]?" ("angry", "base", "base", "R", xpos="mid", ypos="base", flip=True, trans=dissolve)
    gen "That's not the...{w} Well I suppose..." ("base", xpos="far_left", ypos="head")
    lun "I hope I'm not too much of a bother, [name_genie_luna]..." ("soft", "narrow", "worried", "downL")
    lun "I know your time is valuable." ("open", "narrow", "base", "downL")
    gen "Assisting my students is part of my job, [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    if game.daytime:
        gen "Even if that meant treating you for an entire day, then so be it..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Even if that meant treating you all night, then so be it..." ("base", xpos="far_left", ypos="head")

    lun "Really? You'd do that?" ("clench", "base", "base", "mid")
    gen "If that's what is required of me..." ("base", xpos="far_left", ypos="head")
    lun "*Hmm*..." ("annoyed", "narrow", "base", "downL")
    gen "(Is she really considering it?)" ("base", xpos="far_left", ypos="head")
    lun "I wouldn't want you to feel obligated just because it's part of your job..." ("open", "narrow", "base", "mid")
    lun "I think I will still be fine with the amount of time we're spending on the treatment for now." ("base", "narrow", "base", "down")
    gen "Good to hear." ("base", xpos="far_left", ypos="head")
    gen "(I've got enough wankers cramp as it is...)" ("base", xpos="far_left", ypos="head")
    gen "So, are you ready to begin your treatment?" ("base", xpos="far_left", ypos="head")
    lun "Yes... Please go ahead [name_genie_luna]..." ("base", "base", "base", "mid")

    gen "Then just relax, and let me take care of it." ("base", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_grope_breasts_naked")

    nar "Grabbing onto Luna's breasts, you begin massaging them gently."
    lun "*Ah*..." ("open", "closed", "base", "mid")
    nar "Luna immediately shudders, and lets out a soft moan as a response to your touch."
    gen "(All day... Such a silly girl, I doubt she'd last an hour...)" ("base", xpos="far_left", ypos="head")
    nar "You let go of Luna's breasts and give her nipples a quick pinch."
    lun "Ouch!" ("mad", "wide", "base", "up")
    gen "Whops." ("base", xpos="far_left", ypos="head")
    menu:
        "-Pinch her again-":
            nar "You quickly pinch Luna's nipples again, and she jumps slightly by surprise."
            lun @ cheeks blush "Ow, Ow, Ow!!" ("clench", "happyCl", "base", "mid")
            lun @ cheeks blush "[name_genie_luna]!" ("mad", "narrow", "worried", "R")
            gen "Just give it a moment... It will feel better soon..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Are you--" ("angry", "closed", "base", "down")

            nar "You pinch her again, even harder this time, and Luna suddenly jerks her body forward."
            call lun_chibi_scene("inspect_lean_idle_naked")

            lun @ cheeks blush "Stop it [name_genie_luna]...{w=0.4} I can't..." ("mad", "happyCl", "worried", "mid")
            nar "As you let go of her tits, Luna's words trail off slightly..."
            gen "Can't what, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "That's odd..." ("mad", "narrow", "base", "down")
            lun @ cheeks blush "It feels kind of nice, after you let go of them." ("soft", "narrow", "base", "down")
            gen "More sensitive?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Yes..." ("soft", "narrow", "base", "mid")
            lun @ cheeks blush "Do it again [name_genie_luna]!" ("angry", "base", "base", "mid")
            gen "Again?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Yes, again!" ("angry", "base", "base", "R")
            gen "If you say so..." ("base", xpos="far_left", ypos="head")

            call lun_chibi_scene("inspect_lean_grope_breasts_naked")
            nar "You pinch Luna's nipples again, and being fully ready for it this time, you only hear a short intake of breath."
            lun @ cheeks blush "" ("soft", "base", "base", "up")
            nar "Releasing your grip on her nipples, you begin brushing your fingertips along the sides of her breasts, up and around her nipples."
            lun @ cheeks blush "*Ah*...{w=0.4} How...{w=0.4} How strange..." ("open", "closed", "base", "mid")
            nar "Luna, now enjoying the heightened sensitivity of her nipples, begins to relax, her breathing slowing down more and more."
            lun @ cheeks blush "..." ("base", "closed", "base", "mid")
            gen "(Am I just giving her a massage now?)" ("base", xpos="far_left", ypos="head")
        "-Don't-":
            lun @ cheeks blush "Please be careful [name_genie_luna]..." ("angry", "narrow", "base", "mid")

            nar "Trying not to give into the temptation, you resume massaging Luna's breasts."
            nar "Her breathing soon begins slowing down, and you feel her previously tense grip around your legs starting to relax."

            lun @ cheeks blush "..." ("base", "closed", "base", "mid")

            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            gen "(Am I just giving her a massage now?)" ("base", xpos="far_left", ypos="head")

            lun @ cheeks blush "*Ah*....." ("base", "closed", "base", "mid")
            nar "You suddenly feel her beginning to go limp in your hands, and realise that your grip is the only thing preventing her from slumping forward."
            call lun_chibi_scene("inspect_lean_grope_breasts_naked")
            with d3

    gen "*Err*... Are you--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Mmm*..." ("base", "closed", "base", "mid")
    gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("base", "closed", "base", "mid")
    gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")

    call lun_chibi_scene("inspect_lean_idle_naked")
    nar "You let go of Luna's breasts, and she goes stiff, opening her eyes in confusion."

    lun @ cheeks blush "*Huh*?" ("soft", "narrow", "base", "stare")
    gen "I believe our purpose here isn't for me to massage you until you fall asleep..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh... Right..." ("base", "narrow", "base", "downL")

    call lun_chibi_scene("inspect_lean_grope_vagina_naked")
    nar "You stick your hand down between Luna's legs, and begin rubbing your fingers along her slit."

    lun @ cheeks blush "*Ah*..." ("soft", "closed", "base", "mid")
    nar "As you brush up against her, you notice how wet she is already."
    gen "*Hmm*... Looks like that massage helped after all..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("open", "closed", "low", "mid")
    nar "Moving your forefinger up and down against Luna, you hear her breathing becoming more and more erratic, and you feel your cock twitch slightly against your robes."
    gen "(Time to bust this thing wide open...)" ("base", xpos="far_left", ypos="head")
    nar "You stop your movements, giving Luna just a brief moment of anticipation before you push a finger inside."

    call lun_chibi_scene("inspect_lean_idle_naked")
    play sound "sounds/slick_02.ogg"

    with kissiris
    lun @ cheeks blush "{heart}*Ngh*{heart}..." ("grin", "closed", "base", "stare")

    play background "sounds/slickloop.ogg" fadein 2
    call lun_chibi_scene("inspect_lean_grope_vagina_naked")

    nar "You begin moving your finger inside Luna's pussy, as if playfully searching for her weak spot."
    lun @ cheeks blush "*Ah*... What are... What are you doing [name_genie_luna]..." ("grin", "narrow", "base", "up")
    gen "Oh... You know... Just looking for something..." ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "*Ah*...{w=0.4} Looking...{w=0.4} *Ah*...{w=0.4} What are you--" ("grin", "narrow", "base", "up")

    gen "Why I'll never find it at this rate... Better get some of my friends to help." ("base", xpos="far_left", ypos="head")

    play sound "sounds/slick_02.ogg"
    play background "sounds/slickloopfast.ogg"
    nar "You push another finger inside her, and begin moving them around."

    lun @ cheeks blush "*Ah*...{w=0.4} [name_genie_luna]..." ("soft", "narrow", "base", "up")
    gen "*Hmm*... Some lousy friends they are... I still can't find it..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} Are you...{w=0.3} Are you sure..." ("base", "narrow", "base", "up")

    nar "You keep moving your fingers inside Luna, and as you do, you feel her clench around them slightly."

    gen "Yes...{w=0.3} Although maybe it's just hiding..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.3} It...{w=0.3} What is--" ("soft", "narrow", "base", "up")
    gen "Better call in an expert..." ("base", xpos="far_left", ypos="head")
    nar "Keeping your fingers moving inside Luna, you move your thumb and press it up against her clit."
    lun @ cheeks blush "*Oooooh*!!!" ("grin", "wide", "base", "up")
    gen "There it is!" ("base", xpos="far_left", ypos="head")

    play background "sounds/slickloopveryfast.ogg"
    nar "You start rubbing your thumb against Luna's clit as your fingers move rapidly inside her."
    lun @ cheeks blush "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..." ("grin", "base", "base", "up")
    nar "Luna's moans reverberates around your office, and you notice her legs beginning to shake slightly."
    nar "Luna's moans suddenly stops, and she clenches her thighs tight around your hand."

    call lun_chibi_scene("inspect_lean_idle_naked")
    lun @ cheeks blush "*Ah*...{w=0.2} I'm...{w=0.3} I'm cumming!!" ("grin", "happyCl", "base", "stare")

    with kissiris
    play sound "sounds/slick_01.ogg"

    lun @ cheeks blush "*AAAAAH*!!!" ("grin", "narrow", "base", "up")
    nar "Even with your hand locked firmly between her thighs, you still manage to keep your fingers going."

    lun @ cheeks blush "*Ah*...{w=0.2} I'm...{w=0.2} I'm--" ("grin", "narrow", "base", "stare")

    with kissiris
    play sound "sounds/slick_01.ogg"
    stop background fadeout 2

    lun @ cheeks blush "*Ah*..." ("grin", "narrow", "base", "up")
    lun @ cheeks blush "*Mmm*..." ("base", "closed", "low", "up")

    show screen blkfade
    with d5

    $ luna.wear("all")

    nar "Luna's legs buckle completely as she puts her full weight onto your desk."
    nar "You watch her body move up and down for a while, her legs twitching slightly every now and then as liquid runs down her legs."
    nar "After some time, she manages to push herself up and get off your desk."


    hide luna_main
    call lun_chibi("stand", "desk", "base")
    call lun_chibi_scene("reset")

    hide screen blkfade
    with d5

    gen "How was that, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "How did you do that, [name_genie_luna]?" ("mad", "base", "base", "mid", xpos="base", ypos="base", flip=False, trans=dissolve)
    gen "Do what?" ("base", xpos="far_left", ypos="head")
    lun "The thing you did with your thumb." ("angry", "base", "base", "mid")
    gen "Oh that...{w=0.4} Well I just called in an expert didn't I?" ("base", xpos="far_left", ypos="head")
    gen "Nice bloke to have at hand isn't he?" ("base", xpos="far_left", ypos="head")
    lun "Very..." ("base", "narrow", "base", "stare")
    gen "So, feeling better now?" ("base", xpos="far_left", ypos="head")
    lun "Yes, [name_genie_luna]...{w=0.4} Thank you..." ("base", "base", "base", "mid")

    if game.daytime:
        gen "Then you better make your way to class, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    else:
        gen "Then you best be off to bed, [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    lun "Okay..." ("soft", "base", "base", "R")
    lun "Let me know if you want to..." ("open", "narrow", "base", "mid")
    lun "*Ehm*... I mean, I'll let you know if I need any more assistance..." ("open", "base", "base", "down")
    gen "Certainly..." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    jump ll_pf_inspect_end
