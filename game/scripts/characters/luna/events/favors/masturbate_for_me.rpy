

### Luna Masturbate ###

label ll_pf_masturbate:


    if not _events_completed_any:
        gen "{size=-4}(*Hmm*... I wonder if I should ask Luna to masturbate in front of me...){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump luna_favor_menu

    # Start Event
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    $ lun_outfit_last.save() #Save Luna clothing
    $ luna.equip(lun_outfit_default) #Equip Luna Default clothing

    hide screen blkfade
    with d5

    return

label ll_pf_masturbate_end:

    # Setup
    stop music fadeout 2.0
    call hide_characters

    call gen_chibi("sit_behind_desk")

    # Reset Luna clothing.
    $ luna.equip(lun_outfit_last)

    if states.lun.tier == 3:
        if states.lun.level < 9:
            $ states.lun.level += 1

    elif states.lun.tier == 4:
        if states.lun.level < 16:
            $ states.lun.level += 1

    jump end_luna_event

### Tier 3 ###

##Genie teaches Luna how to touch herself. She lifts up and rubs herself under her skirt until cumming and is very pleased that she managed to do it.##

label ll_pf_masturbate_T3_E1_intro:

    call ll_pf_masturbate

    gen "So, have the wickerspats finally left you alone [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "Not at all, [name_genie_luna]... In fact... They've been worse than ever." ("angry", "narrow", "base", "downL", trans=dissolve)
    gen "Really?" ("base", xpos="far_left", ypos="head")
    nar "Luna shifts her thighs together uncomfortably."
    lun "Yes..." ("annoyed", "narrow", "base", "mid") #seductive
    gen "That's unfortunate..." ("base", xpos="far_left", ypos="head")
    gen "Well, in that case, I think it's time I teach you how to masturbate." ("base", xpos="far_left", ypos="head")
    lun "*Oooh*... I'm finally going to become a master baiter myself, [name_genie_luna]?" ("grin", "base", "raised", "mid")
    gen "That's right..." ("base", xpos="far_left", ypos="head")
    lun "Marvellous!" ("smile", "base", "base", "mid")
    lun "" ("crooked_smile", "narrow", "base", "mid")
    nar "Luna jumps happily on the spot, looking at you expectantly."
    gen "Let's get going then, shall we..." ("base", xpos="far_left", ypos="head")
    lun "Thank you so much!" ("crooked_smile", "happyCl", "base", "mid")
    gen "No need to thank me, [name_luna_genie], I'm simply doing what is necessary." ("base", xpos="far_left", ypos="head")
    gen "Now, come stand in front of my desk." ("base", xpos="far_left", ypos="head")

    hide luna_main
    with d3

    call lun_walk("desk", "base")

    $ luna.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")

    stop weather fadeout 4

    show CG luna as cg zorder 17:
        zoom 0.95
        pos (-975, -155)
    hide screen blkfade
    with fade

    show CG luna as cg zorder 17:
        zoom 0.95
        pos (-975, -155)
        easein_quad 5.0 zoom 0.5 pos (0, 0)

    lun "Is here okay?" ("soft", "narrow", "base", "mid")
    gen "Perfect."
    gen "I'll have to explain a few things before we get going, so pay attention..."
    lun "Yes, [name_genie_luna]..." ("base", "base", "base", "mid")
    nar "Luna stares at you intently."
    gen "Good... Now--"
    gen "Remember what we talked about... Locate the affected area, then focus positive thoughts onto it..."
    lun "Right." ("open", "narrow", "base", "down")
    gen "Have you found it?"
    lun "Yes..." ("base", "narrow", "base", "down")
    gen "Good..."
    gen "Now then..."
    gen "Let's try some self-applied massage to start with."
    lun @ cheeks blush "A--{w=0.2} Alright." ("soft", "narrow", "base", "down")
    gen "Don't worry, I'll be here to give you some guidance."
    lun @ cheeks blush "Thank you, [name_genie_luna]." ("base", "narrow", "base", "down")


    show screen blkfade
    with d3

    $ luna.set_pose("hand_on_pussy_and_breast")

    nar "Luna puts one of her hands on her nipple and the other one below her skirt, a slight moan escapes her as her fingers reaches the surface of her skin."

    hide screen blkfade
    with d3

    lun @ cheeks blush "*Ah*..." ("open", "narrow", "base", "up")
    gen "Is everything alright, [name_luna_genie]?"
    lun @ cheeks blush "*Ah*...{w=0.3} of course, [name_genie_luna]!" ("soft", "narrow", "base", "stare")
    lun @ cheeks blush "My fingers are just a bit cold..." ("normal", "narrow", "base", "mid")
    gen "That's fine... Just try rubbing yourself, and your fingers will warm up in just a moment."
    lun @ cheeks blush "*Ah*...{w=0.3} Yes [name_genie_luna]..." ("angry", "narrow", "low", "stare")
    gen "..."


    lun @ cheeks blush "*Ah*...{w=0.3} is this how it should be done?" ("soft", "base", "base", "mid")
    gen "As long as it's feeling good, then I'm sure it's working. Just keep going, and you'll soon be rid of those nasty Wickerspoons."
    lun @ cheeks blush "I'm glad..." ("base", "narrow", "base", "down")
    lun @ cheeks blush "Although it feels a bit different compared to when you helped me..." ("annoyed", "narrow", "base", "down")
    gen "That's to be expected... Another person's touch will always feel different to your own."
    lun @ cheeks blush "Okay..." ("upset", "base", "base", "down")

    nar "Luna moves her hand around beneath her skirt before stopping again."
    lun @ cheeks blush "It's just..." ("upset", "narrow", "base", "mid")
    lun @ cheeks blush "As nice as this massage feels..." ("soft", "narrow", "base", "mid")
    lun @ cheeks blush "It's not really scratching that same itch, [name_genie_luna]..." ("annoyed", "narrow", "base", "mid")
    gen "I guess I do have that slight magic touch..."
    gen "*Hmm*..."
    lun @ cheeks blush "Am I doing it wrong, [name_genie_luna]?" ("upset", "narrow", "base", "down")
    gen "Certainly not, but this might be trickier than I initially thought..."
    lun @ cheeks blush "Really?" ("soft", "base", "base", "mid")
    gen "It would seem that those nasty critters are trying to hide!"
    lun @ cheeks blush "Hide? But I thought touching myself would lure them--" ("mad", "narrow", "base", "down")
    gen "Don't worry [name_luna_genie]... As long as you're still feeling that itch, then they can't have gone far."
    gen "Although this means you'll have to chase them down."
    lun @ cheeks blush "Chase them down?" ("angry", "narrow", "base", "down")
    gen "I'll be here to guide you through it of course..."
    lun @ cheeks blush "Okay..." ("soft", "base", "base", "mid")
    gen "Ready?"
    lun @ cheeks blush "Yes." ("angry", "base", "base", "mid")
    gen "Close your eyes..."
    lun @ cheeks blush "" ("normal", "closed", "base", "mid") #eyes closed
    call ctc
    gen "Very good...{w} Now I want you to block out everything else."
    lun @ cheeks blush "Alright, [name_genie_luna]..." ("open", "closed", "base", "mid")
    gen "Imagine standing alone in your bedroom..."
    lun @ cheeks blush "" ("normal", "closed", "base", "mid")
    call ctc
    gen "Empty your mind of all intrusive thoughts..."
    lun @ cheeks blush "" ("normal", "closed", "annoyed", "mid")
    call ctc
    gen "Now... Focus on where the itch is coming from..."
    lun @ cheeks blush "" ("upset", "closed", "annoyed", "mid")
    call ctc
    gen "Then once you've found it, I want you to chase down that feeling with your fingers."
    lun @ cheeks blush "" ("annoyed", "closed", "annoyed", "mid")
    call ctc
    gen "And catch it!"

    lun @ cheeks blush "I-- I can't... I can't find it..." ("angry", "closed", "base", "mid")


    lun @ cheeks blush "It's like trying to grab rays of sunlight..." ("angry", "closed", "base", "mid")
    gen "Don't try to grab a hold of it, just brush against it with the tips of your fingers."
    lun @ cheeks blush "" ("soft", "closed", "annoyed", "mid")
    call ctc

    lun @ cheeks blush "" ("normal", "closed", "annoyed", "mid")
    call ctc

    nar "Luna desperately moves her hand around beneath her skirt."
    lun @ cheeks blush "I... I think I've lost them again, [name_genie_luna]..." ("angry", "closed", "base", "mid")
    gen "Try moving your hand up a bit more..."
    lun @ cheeks blush "Up a bit--" ("angry", "closed", "low", "mid")

    lun @ cheeks blush "*Ah*..." ("grin", "closed", "worried", "mid")
    lun @ cheeks blush "*Mmm*..." ("base", "closed", "base", "mid")
    nar "Luna gives off a soft moan under her breath."
    gen "(There we go...)"
    lun @ cheeks blush "This... This area is even more itchy, [name_genie_luna]..." ("base", "closed", "low", "mid")
    gen "Excellent... That means you've managed to chase them down."
    gen "Just keep your eyes closed and begin gently moving your fingers in a circular motion over the area."


    lun @ cheeks blush "Oooh! {heart}" ("grin", "closed", "base", "mid")
    lun @ cheeks blush "*Ah*...{w=0.3} Yes...{w=0.3} I think it's working, [name_genie_luna]!" ("grin", "closed", "annoyed", "mid")
    gen "*Shhh*...{w=0.3} Don't speak...{w=0.3} Just focus."
    lun @ cheeks blush "" ("grin", "closed", "base", "mid")
    gen "Empty your mind and only think about what makes you feel good..."
    lun @ cheeks blush "Okay..." ("base", "closed", "base", "mid")
    lun @ cheeks blush "" ("soft", "closed", "low", "mid")
    call ctc
    lun @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "[name_genie_luna]..." ("soft", "closed", "base", "mid")
    lun @ cheeks blush "*Ah*...{w=0.3} [name_genie_luna]..." ("soft", "closed", "base", "mid")
    lun @ cheeks blush "I think..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "I think I've almost..." ("soft", "closed", "base", "mid")
    gen "*Shhh*..."


    nar "You see Luna's hand move swiftly beneath her skirt."
    lun @ cheeks blush "*Mmmm*..." ("base", "closed", "base", "mid")
    lun @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "*A-ah*..." ("grin", "closed", "base", "mid")
    lun @ cheeks blush "Yes..." ("grin", "closed", "low", "mid")
    lun @ cheeks blush "*Ah*... *Ah*...{heart}" ("grin", "closed", "low", "mid")
    lun @ cheeks blush "{size=+4}*Mmm*...{w=0.3} Yes...{heart}{/size}" ("crooked_smile", "narrow", "base", "up")
    lun @ cheeks blush "{size=+8}*Ah*...{w=0.3} *Ah*...{/size}" ("crooked_smile", "narrow", "base", "up")
    gen "That's it--"


    nar "Luna now desperately trying to cum, moves her hand even faster."
    lun @ cheeks blush "*Ah*! I think they're attacking me, [name_genie_luna]!" ("crooked_smile", "base", "base", "up")
    lun @ cheeks blush "I... I can't stop moving my--" ("grin", "happyCl", "base", "mid")
    gen "Keep going, you're doing it!"
    lun @ cheeks blush "*Ah*...{w=0.4} Yes [name_genie_luna]...{heart}" ("crooked_smile", "happyCl", "base", "up")
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*...{w=0.4}" ("soft", "happyCl", "base", "up")
    lun @ cheeks blush "*Ngh*... It's...{w=0.3} I'm--" ("grin", "happyCl", "base", "mid")

    play sound "sounds/slick_01.ogg"
    with kissiris
    lun @ cheeks blush "*Ah*!" ("grin", "narrow", "base", "ahegao")

    lun @ cheeks blush "*Mmm*..." ("grin", "narrow", "base", "up")
    gen "Well done--"

    play sound "sounds/slick_01.ogg"
    with kissiris
    lun @ cheeks blush "*Ah*!" ("crooked_smile", "narrow", "base", "up")

    lun @ cheeks blush "..." ("soft", "narrow", "base", "stare")
    lun @ cheeks blush "{size=-5}*Sigh*...{/size}" ("base", "closed", "low", "mid")

    #end of masturbate section (Cuts to Normal office screen with blkfade)
    show screen blkfade
    with d3

    $ luna.set_pose(None)

    hide cg

    hide screen blkfade
    with d5

    call weather_sound

    gen "Well, will you look at that... You're a natural..." ("grin", xpos="far_left", ypos="head")
    gen "So, the {i}wickspots{/i} have left you alone now, I take it?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I...{w=0.4} I believe so, [name_genie_luna]..." ("open", "narrow", "base", "down", xpos="mid", ypos="base", trans=dissolve)
    lun @ cheeks blush "At least that nasty itch appears to have gone away." ("base", "narrow", "base", "down")
    gen "Excellent!" ("grin", xpos="far_left", ypos="head")
    gen "Then my work here is done!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Oh*..." ("soft", "base", "base", "mid")
    lun @ cheeks blush "You want me to leave already, [name_genie_luna]?" ("open", "base", "base", "mid")
    gen "If there's nothing else I can help you with?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ehm*...{w=0.4} Well, I was just wondering..." ("soft", "narrow", "base", "R")
    lun @ cheeks blush "What do I do if the feeling comes back, [name_genie_luna]?" ("angry", "narrow", "base", "mid")
    lun @ cheeks blush "Do I just get rid of them myself from now on?" ("soft", "narrow", "base", "mid")
    gen "Certainly not!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("base", "base", "base", "mid") #happy
    gen "I need to supervise every development until you've mastered the art of masturbation." ("base", xpos="far_left", ypos="head")
    gen "Preventing this outbreak is now my top priority." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Really? Thank you so much, [name_genie_luna]." ("base", "happyCl", "base", "mid")
    gen "Certainly." ("base", xpos="far_left", ypos="head")
    gen "Bestow shall I in you, my teaching of all, young padawan!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Sorry?" ("soft", "base", "base", "mid")
    lun @ cheeks blush "I'm not sure exactly what you mean, [name_genie_luna]." ("angry", "narrow", "base", "mid")
    gen "Yes, Indeed... You still have more to learn before reaching your true potential..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Huh*?" ("upset", "narrow", "base", "mid")
    gen "Once you've learned how to control the force, I shall bestow on you my saber of light." ("base", xpos="far_left", ypos="head")
    gen "And as my meta chlorines flow through your body--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "[name_genie_luna]?" ("angry", "base", "base", "mid")
    gen "Oh yeah, that's not canon anymore is it..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("annoyed", "base", "base", "mid") #Confused
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "That shall do for today, [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Okay..." ("base", "narrow", "base", "mid")
    gen "Off you pop." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Right." ("open", "base", "base", "mid")
    lun @ cheeks blush "Bye then..." ("base", "base", "base", "mid")

    call lun_walk(action="leave")

    $ states.lun.status.masturbating = True

    jump ll_pf_masturbate_end

##Luna takes off her skirt and later on, her top. She fingers herself for the first time
##She doesn't squirt in this event, but will, druing the third event.

label ll_pf_masturbate_T3_E2_intro:

    call ll_pf_masturbate

    gen "[name_luna_genie], tell me how you've been." ("base", xpos="far_left", ypos="head")
    lun "I've been okay [name_genie_luna]... But it appears the wrackspurts have come back again..." ("open", "narrow", "base", "down", trans=dissolve)
    gen "Oh no... Such a shame!" ("base", xpos="far_left", ypos="head")
    lun "Every time I think about the things we've done in here..." ("soft", "narrow", "base", "down")
    lun "It just makes them feel so much... Stronger..." ("angry", "narrow", "base", "mid")
    gen "They must be afraid of my powerful techniques..." ("base", xpos="far_left", ypos="head")
    lun "You believe so?" ("angry", "base", "raised", "mid")
    gen "I do..." ("base", xpos="far_left", ypos="head")
    gen "Why else would they attack you when you're thinking about ridding yourself of them?" ("base", xpos="far_left", ypos="head")
    lun "That's true..." ("soft", "narrow", "base", "down")
    gen "This just means we need to fight back even harder!" ("base", xpos="far_left", ypos="head")
    lun "Harder?" ("mad", "base", "base", "mid")
    gen "Yes, and better!" ("base", xpos="far_left", ypos="head")
    lun "Better, but last time I--" ("angry", "narrow", "base", "stare")
    gen "Faster! Stronger!" ("base", xpos="far_left", ypos="head")
    lun "Oh my... Are you sure I'm ready, [name_genie_luna]?" ("angry", "narrow", "base", "mid")
    gen "Of course... Why, you've already experienced it before..." ("base", xpos="far_left", ypos="head")
    lun "You don't mean..." ("angry", "wide", "base", "mid") #horny
    nar "Luna starts grinding her thighs together."
    lun @ cheeks blush "But what if I don't do it right, [name_genie_luna]?" ("upset", "closed", "base", "down")
    lun @ cheeks blush "I wouldn't want to hurt myself..." ("angry", "narrow", "base", "down")
    gen "*Hmm*... In that case, why don't you take your bottoms off this time?" ("base", xpos="far_left", ypos="head")
    gen "That way I can see what you're doing a lot easier, and make sure you don't hurt yourself." ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "" ("soft", "base", "base", "mid")
    nar "Luna gives you a look of excitement from your proposition..."

    lun @ cheeks blush "Well, I do feel inclined to take you up on that offer." ("soft", "base", "base", "down")
    gen "It's not an offer, [name_luna_genie]. If we are to make any progress, then I require you to take off your bottoms. so I can watch you masturbate." ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "" ("base", "narrow", "base", "down")
    nar "Luna's body twitches slightly, looking at her face, you get the feeling she's pondering on something."

    lun @ cheeks blush "My body appears to think it's the right decision, [name_genie_luna]." ("open", "base", "base", "mid")
    gen "Your body?" ("base", xpos="far_left", ypos="head")
    gen "(What is she on about now?)" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Yes, my body appears to have reacted to your proposition..." ("base", "base", "base", "down")
    gen "Your body is reacting to--" ("base", xpos="far_left", ypos="head")
    gen "I mean, yes! That makes perfect sense... Your body does tell you when you're hungry, so why wouldn't it try and help you get rid of those spurts too." ("grin", xpos="far_left", ypos="head")
    gen "Ten points to Ravenclaw." ("base", xpos="far_left", ypos="head")
    $ ravenclaw += 10
    lun @ cheeks blush "Thank you [name_genie_luna]." ("grin", "closed", "base", "mid")
    gen "Very well then, let's give your body what it needs... Take your bottoms off--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("base", "narrow", "base", "mid") #Horny
    lun @ cheeks blush "Yes, [name_genie_luna]." ("base", "base", "base", "mid")
    gen "And do come a bit closer, so I can get a proper look..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Okay." ("open", "base", "base", "mid")

    #Luna chibi walks to desk

    call lun_walk("desk", "base")

    stop weather fadeout 4

    hide screen blkfade
    show CG luna as cg zorder 17:
        zoom 0.5
    with fade

    #start of masturbation section (in front of desk CG)
    gen "Begin when you're ready, [name_luna_genie]."

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bottom")
    $ luna.set_cum(pussy="wet")
    with d3

    lun @ cheeks blush "Finally..." ("angry", "narrow", "base", "down")
    gen "You seem relieved."
    gen "(And rather wet...)"

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bottom", "panties")
    with d3

    call ctc

    $ luna.set_pose("hand_on_pussy_and_breast")
    $ luna.strip("bottom", "panties")

    lun @ cheeks blush "*Ah*..." ("grin", "narrow", "base", "up")
    lun @ cheeks blush "I've not been able to stop thinking about this since last time..." ("grin", "narrow", "base", "stare")
    lun @ cheeks blush "I worry those slimy wrackspurts have infested the dormitories, because I'm having trouble sleeping as well..." ("angry", "narrow", "base", "down")
    gen "That's quite possible..."
    lun @ cheeks blush "It's--{w=0.2} *Ah*...{w=0.3} It's weird...{w=0.3} I almost feel glad I've got them..." ("angry", "closed", "base", "mid")
    lun @ cheeks blush "Getting rid of them feels...{w=0.4} so...{w=0.3} so...{w=0.3}{nw}" ("angry", "closed", "low", "mid")
    lun @ cheeks blush "Getting rid of them feels... so... so...{fast} good..." ("grin", "narrow", "base", "stare")
    gen "The positive feelings must be your body telling you that you're doing the right thing, by expelling them..."
    lun @ cheeks blush "*Ah*..." ("grin", "narrow", "base", "up")
    lun @ cheeks blush "I must be...{w=0.3} *Ah*...{w=0.3} Expelling a lot of them then..." ("base", "narrow", "base", "stare")
    lun @ cheeks blush "*Ah*... [name_genie_luna], I'm feeling hot all over..." ("angry", "happyCl", "base", "mid")
    lun @ cheeks blush "And that itch... It's all over my--" ("angry", "narrow", "base", "down")
    lun @ cheeks blush "*Ah*..." ("soft", "happyCl", "base", "down")
    gen "That means your body is ready for the next step..."
    lun @ cheeks blush "[name_genie_luna]...{w=0.3} *Ah*... I'm not sure I'm ready..." ("angry", "happyCl", "base", "mid")
    gen "Nonsense..."
    gen "Just take it slow and gently push a finger in..."
    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} Alright..." ("open", "happyCl", "base", "mid")
    nar "Luna begins rubbing a finger across her slit... Still a little apprehensive about putting it inside..."
    lun @ cheeks blush "*Ah*...{w=0.3} [name_genie_luna]..." ("soft", "happyCl", "base", "mid")
    gen "Gently..."
    lun @ cheeks blush "Gently...{w=0.4} Okay..." ("angry", "closed", "base", "mid")
    lun @ cheeks blush "*Nnnngh*..." ("clench", "happyCl", "base", "mid")

    #Finger inserted
    play sound "sounds/slick_02.ogg"
    with kissiris

    lun @ cheeks blush "*Ah*..." ("base", "narrow", "base", "up")
    lun @ cheeks blush "I...{w=0.3} I did it, [name_genie_luna]..." ("grin", "narrow", "base", "up")
    gen "How does it feel?"
    lun @ cheeks blush "It...{w=0.3} Good...{w=0.5} Just a bit strange..." ("soft", "narrow", "base", "stare")
    gen "Try moving it in and out."
    lun @ cheeks blush "Alright..." ("soft", "narrow", "base", "down")

    play background "sounds/slickloop.ogg" fadein 2
    #Luna fingering

    nar "Luna starts pushing her fingers in and out, the sounds of her moaning becoming more and more shallow as she goes on."
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "How--{w=0.2} *Ah*...{w=0.4} How is it looking?" ("soft", "closed", "base", "up")
    gen "Very good [name_luna_genie]... You're very pretty..."
    lun @ cheeks blush "*Ah*...{w=0.3} I'm--{w=0.2} *Ah*...{w=0.4} I'm pretty, [name_genie_luna]?" ("angry", "narrow", "base", "stare")
    gen "Why yes, [name_luna_genie]. Your body is very nice..."
    lun @ cheeks blush "[name_genie_luna]--{w=0.2} *Ah*...{w=0.4} That's not what I--{w=0.4}{nw}" ("angry", "narrow", "base", "mid")
    lun @ cheeks blush "[name_genie_luna]-- *Ah*... That's not what I--{fast} *Ah*..." ("angry", "closed", "base", "mid")
    lun @ cheeks blush "I merely wanted to know if I was doing it right..." ("soft", "closed", "base", "mid")
    gen "I know."
    lun @ cheeks blush "*Ah*...{w=0.3} [name_genie_luna]?" ("soft", "narrow", "base", "stare")
    gen "Take your top off for me will you..."
    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} Okay..." ("open", "narrow", "base", "up")

    #Luna takes out finger
    stop background fadeout 2
    lun @ cheeks blush "" ("base", "narrow", "base", "stare")
    $ luna.set_pose("default")
    pause 1

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("top", "bra")
    with d5

    lun @ cheeks blush "" ("grin", "narrow", "base", "down")
    pause 1
    lun @ cheeks blush "" ("grin", "narrow", "base", "mid")
    call ctc

    gen "Now keep going, [name_luna_genie]..."
    lun @ cheeks blush "Yes [name_genie_luna]..." ("grin", "narrow", "base", "mid")

    $ luna.set_pose("hand_on_pussy_and_breast")

    #Luna rubs herself again

    lun @ cheeks blush "*Mmm*..." ("base", "closed", "base", "mid")

    gen "That's it... Keep rubbing that cute slit of yours..."
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4}*Ah*..." ("soft", "closed", "base", "down")
    gen "Look at me [name_luna_genie]."
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("soft", "narrow", "base", "mid")
    gen "Show me your tongue..."
    lun @ cheeks blush "*Ah*...{w=0.4} My...{w=0.4} My tongue?" ("angry", "base", "base", "mid")
    lun @ cheeks blush "Is this part of our research?" ("angry", "base", "base", "R")
    gen "Yes... Open your mouth as wide as you can please."
    lun @ cheeks blush "But--" ("open", "base", "base", "mid")
    gen "Say \"Aaaa\"..."
    lun @ cheeks blush "*Aaaa*...{w=0.1}{nw}" ("open", "closed", "base", "mid")
    lun @ cheeks blush "*Aaaa*...{fast}{w=0.1}{nw}" ("open_tongue", "closed", "base", "mid")
    lun @ cheeks blush "*Aaaa*...{fast}" ("open_wide_tongue", "closed", "base", "mid")
    gen "Good..."
    gen "I want you to know how much I appreciate that you chose to come to me with this problem of yours [name_luna_genie]..."

    #Luna stops

    lun @ cheeks blush "" ("soft", "narrow", "base", "mid")
    call ctc
    lun @ cheeks blush "[name_genie_luna] I--" ("angry", "narrow", "base", "mid")
    gen "Keep going... Put a finger in again..."
    lun @ cheeks blush "Yes [name_genie_luna]..." ("angry", "narrow", "base", "down")

    #Luna puts finger in again
    play sound "sounds/slick_02.ogg"
    with kissiris

    lun @ cheeks blush "*Mmm*..." ("soft", "narrow", "base", "up")
    gen "Good girl... Now get it moving... Get those spurts out..."
    lun @ cheeks blush "" ("base", "narrow", "base", "up")
    call ctc

    play background "sounds/slickloop.ogg" fadein 2
    #Luna fingering

    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "[name_genie_luna]... *Ah*...{w=0.3} I feel them building up again..." ("soft", "closed", "base", "mid")
    gen "Good girl, then try going a bit faster..."
    lun @ cheeks blush "Oh-- Okay..." ("soft", "closed", "base", "mid")

    play background "sounds/slickloopfast.ogg"

    lun @ cheeks blush "*Ah*...{w=0.2}*Ah*...{w=0.2}*Ah*..." ("open", "narrow", "base", "up")
    lun @ cheeks blush "I think...{w=0.3} *Ah*...{w=0.3} I'm about to...{w=0.3} *Ah*..." ("angry", "narrow", "base", "up")
    gen "Oh, are you cumming already?"
    lun @ cheeks blush "*Ah*... Yes, I'm--" ("angry", "narrow", "base", "stare")
    lun @ cheeks blush "*Ah*...{w=0.3} I'm cumming [name_genie_luna]!!{heart}{heart}" ("grin", "happyCl", "base", "up")

    play sound "sounds/slick_01.ogg"
    with kissiris

    lun @ cheeks blush "*Ah*!{heart}" ("grin", "narrow", "base", "up")

    nar "You see a flush of red roll over Luna's face as her body twitches from the throes of her orgasm."

    play sound "sounds/slick_01.ogg"
    with kissiris

    $ luna.set_cum(pussy="squirt_post")
    lun @ cheeks blush "*Ah*...{heart}" ("open_tongue", "narrow", "base", "ahegao")
    nar "Despite this, her fingers remain a flurry of movement until a final wave of pleasure washes over her."

    play sound "sounds/slick_01.ogg"
    with kissiris
    stop background fadeout 2
    #Finger stops moving

    lun @ cheeks blush "*Mmm*...{heart}" ("base", "happyCl", "base", "mid")

    hide cg
    show screen blkfade
    with d5

    nar "Luna slowly pulls her finger out and shudders slightly..."
    nar "She looks at her fingers, which glisten in the light, with a relieved expression on her face..."

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    # End of masturbate section

    $ luna.set_pose(None)
    $ luna.wear("all")
    $ luna.set_cum(None)
    hide screen blkfade
    with d5

    call weather_sound

    gen "It seems those Wickedspots have been giving you a fair bit of grief, haven't they?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ah*...{w=0.3} {heart}yes{heart}..." ("base", "narrow", "base", "down", xpos="mid", ypos="base", trans=dissolve)
    gen "Don't worry, that should sort them out for now..." ("base", xpos="far_left", ypos="head")
    gen "Feeling better?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Yes... I'm feeling much better now... Thank you [name_genie_luna]." ("base", "base", "base", "mid")
    gen "I take it my words of encouragement were effective?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I...{w=0.4} Yes [name_genie_luna]..." ("soft", "narrow", "base", "R")
    gen "Excellent." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ehm*..." ("soft", "narrow", "base", "down")
    lun @ cheeks blush "So the things you said..." ("open", "narrow", "base", "down")
    lun @ cheeks blush "About me being pretty..." ("normal", "narrow", "base", "down")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Was that just to help me with..." ("soft", "narrow", "base", "downL")
    lun @ cheeks blush "Actually... Forget I asked [name_genie_luna]..." ("angry", "narrow", "base", "downL")
    lun @ cheeks blush "I... I'll just head back to my dorms now..." ("angry", "base", "base", "R")
    gen "Of course, good job today--" ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    gen "(What an odd girl...)" ("base", xpos="far_left", ypos="head")

    jump ll_pf_masturbate_end

##Luna masturbates for Genie, naked and squirts##
label ll_pf_masturbate_T3_E3_intro:

    $ states.lun.ev.play_with_yourself.t3_e3_complete = True

    call ll_pf_masturbate

    gen "Alright then, time for you to--" ("base", xpos="far_left", ypos="head")
    lun "Finally..." ("mad", "base", "base", "mid", trans=dissolve)

    call lun_walk("desk", "base")
    pause .3

    show screen blkfade
    with d3

    #Start of masturbate section

    nar "Luna quickly whips her clothes off and begins touching herself."

    $ luna.set_pose("hand_on_pussy_and_breast")
    $ luna.set_cum(pussy="wet")
    $ luna.strip("clothes")

    lun @ cheeks blush "" ("grin", "narrow", "base", "mid")

    stop weather fadeout 4

    hide screen blkfade
    show CG luna as cg zorder 17:
        zoom 0.5
    with fade

    # hand moving slow

    lun @ cheeks blush "*Ah*... {heart} Yes..." ("grin", "narrow", "base", "up")
    gen "By the great desert sands! You're sopping wet!"
    lun @ cheeks blush "I'm sorry [name_genie_luna]... I just...{w=0.3} Need this really bad...{heart}" ("mad", "happyCl", "base", "stare")
    lun @ cheeks blush "These Wrackspurts...{w=0.4} *Ah*..." ("upset", "happyCl", "base", "mid")
    lun @ cheeks blush "They've been very tiresome..." ("angry", "narrow", "base", "up")

    nar "Without being prompted, Luna pushes a finger inside her and starts fingering herself."

    #Luna inserts finger
    play sound "sounds/slick_02.ogg"
    with kissiris

    lun @ cheeks blush "*Ah*...{heart}" ("grin", "narrow", "base", "up")

    #Luna fingering
    play background "sounds/slickloop.ogg" fadein 2

    lun @ cheeks blush "" ("grin", "closed", "base", "mid")
    gen "You're becoming quite the expert at this..."
    lun @ cheeks blush "*Ah*...{w=0.4} I'm just doing--{w=0.2} *Ah*...{w=0.4} What you've taught me [name_genie_luna]..." ("soft", "closed", "base", "mid")
    gen "Don't be so modest [name_luna_genie]... It takes a lot of willpower and determination to get to where you are."
    lun @ cheeks blush "*Ah*... Really?" ("soft", "narrow", "base", "stare")
    gen "Absolutely...{w=0.4} You're a natural!"
    gen "I'd even go as far to say that you were born to do this."
    lun @ cheeks blush "*Mmm*..." ("base", "narrow", "base", "stare")

    lun @ cheeks blush "Well, I'm not so sure about that..." ("base", "closed", "base", "mid")
    lun @ cheeks blush "Although I must say...{w=0.4} *Ah*...{w=0.4} I've been enjoying these sessions a fair bit, [name_genie_luna]..." ("open", "closed", "base", "mid")
    lun @ cheeks blush "They are starting to become all I can think about..." ("base", "closed", "base", "mid")
    gen "*Hmm*...{w=0.3} Do you think that's a bad thing?"
    lun @ cheeks blush "*Ah*...{w=0.3} of course not!" ("grin", "closed", "base", "mid")
    lun @ cheeks blush "It just...*Hngh*{w=0.3} means that it's working..." ("grin", "happyCl", "base", "mid")
    lun @ cheeks blush "If only I could spend all day up here..." ("base", "narrow", "base", "up")
    gen "Do you think a full day of treatment would get rid of them?"
    lun @ cheeks blush "*Ah*..." ("soft", "narrow", "base", "up")
    lun @ cheeks blush "I don't know..." ("open", "narrow", "base", "up")
    lun @ cheeks blush "But..." ("upset", "narrow", "base", "up")
    lun @ cheeks blush "I think It'd probably feel--{w=0.2} *Ah*..." ("soft", "narrow", "base", "up")
    lun @ cheeks blush "Nice...{heart}{heart}{heart}" ("base", "narrow", "base", "stare")
    nar "Luna moans softly under her breath."
    lun @ cheeks blush "{heart}{heart}{heart}" ("base", "closed", "base", "mid")
    lun @ cheeks blush "You, watching me while I do this... For some reason--" ("grin", "narrow", "base", "mid")
    gen "*Shhh*... Focus [name_luna_genie]..."
    lun @ cheeks blush "Yes [name_genie_luna]..." ("base", "narrow", "base", "down")
    lun @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..." ("base", "closed", "base", "mid")
    lun @ cheeks blush "I think..." ("grin", "closed", "base", "stare")
    lun @ cheeks blush "*Ah*..." ("grin", "narrow", "base", "up")
    lun @ cheeks blush "I think I've almost got them, [name_genie_luna]..." ("crooked_smile", "narrow", "base", "up")
    gen "(Already? She's faster than I am!)"
    lun @ cheeks blush "[name_genie_luna]... Please..." ("crooked_smile", "narrow", "base", "up")

    play background "sounds/slickloopfast.ogg"

    lun @ cheeks blush "*Ah*...{w=0.3} Tell me...{w=0.3} Tell me I'm pretty." ("mad", "closed", "base", "stare")
    gen "What?"

    label .choice:

    menu:
        "-Tell her-":
            gen "You're very pretty, [name_luna_genie]."
            lun @ cheeks blush "*Mmm*..." ("base", "narrow", "base", "up")
        "-Don't-":

            random:
                lun @ cheeks blush "Hurry...{w=0.3} I'm...{w=0.3} I'm almost there..." ("grin", "happyCl", "base", "up")
                block:
                    gen "You're going to need to learn how to do this without my help [name_luna_genie]..."
                    lun @ cheeks blush "Please, [name_genie_luna]..." ("angry", "happyCl", "base", "mid")
                block:
                    gen "Tell you..."
                    lun @ cheeks blush "Tell me I'm pretty, [name_genie_luna]..." ("grin", "narrow", "base", "up")

            # Menu opens again until you've told her she's pretty
            jump ll_pf_masturbate_T3_E3_intro.choice

    play background "sounds/slickloopveryfast.ogg"

    lun @ cheeks blush "" ("grin", "closed", "base", "up")
    nar "Luna, revelling in your praise, closes her eyes and begins furiously pumping her fingers in and out."
    lun @ cheeks blush "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..." ("grin", "closed", "base", "mid") #Eyes closed
    lun @ cheeks blush "{size=+4}*Mmm*...{w=0.4}{/size}{nw}" ("base", "closed", "base", "mid")
    lun @ cheeks blush "{size=+4}*Mmm*...{fast} Yes...{heart}{/size}" ("crooked_smile", "closed", "base", "mid")
    lun @ cheeks blush "*Ah*...{w=0.3}{nw}" ("crooked_smile", "closed", "base", "mid")
    lun @ cheeks blush "*Ah*...{fast} [name_genie_luna], I think I'm..." ("crooked_smile", "narrow", "base", "stare")
    nar "Luna's fingers move in a flurry, as she continues pumping them into her needy slit."

    lun @ cheeks blush "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*...{heart}" ("crooked_smile", "narrow", "base", "up")
    gen "Good girl...{w=0.3} Now--"
    lun @ cheeks blush "*AAAAH*!!!" ("scream", "happyCl", "base", "up")

    play sound "sounds/slick_01.ogg"
    #Luna Squirts
    lun @ cheeks blush "" ("scream", "wide", "base", "up")
    $ luna.set_cum(pussy="squirt")
    with kissiris
    pause .8
    #Non luna squirt
    $ luna.set_cum(pussy="squirt_post")
    lun @ cheeks blush "" ("grin", "wide", "base", "up")

    gen "By the great--"
    lun @ cheeks blush "{size=+4}*Nnngh*--{/size}" ("angry", "narrow", "base", "up")

    play sound "sounds/slick_01.ogg"
    stop background fadeout 2
    #Luna Squirts
    with kissiris
    $ luna.set_cum(pussy="squirt")
    lun @ cheeks blush "{size=+4}*Nnngh*--{fast} *AH*!!{heart}{/size}{w=0.3}{nw}" ("scream", "narrow", "base", "ahegao")
    #Non luna squirt
    $ luna.set_cum(pussy="squirt_post")
    lun @ cheeks blush "{size=+4}*Nnngh*--{fast} *AH*!!{heart}{/size}{fast}" ("scream", "narrow", "base", "ahegao")

    lun @ cheeks blush "*Ah*..." ("base", "narrow", "base", "up")
    lun @ cheeks blush "Thank you, [name_genie_luna]..." ("base", "closed", "base", "mid")

    hide cg
    show screen blkfade
    with d5

    nar "Luna takes her fingers out, and looks up at you with a happy smile spread across her face..."
    gen "Well done [name_luna_genie]."

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    # End of masturbate section

    $ luna.set_pose(None)
    $ luna.wear("all")
    $ luna.set_cum(None)
    hide screen blkfade
    with d5

    call weather_sound

    gen "Now I didn't take you for a squirter, [name_luna_genie]..." ("grin", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("soft", "base", "base", "down", xpos="mid", ypos="base", trans=dissolve)
    gen "Is everything okay?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Look at all these wrackspurts!" ("mad", "base", "base", "down")
    gen "..." ("base", xpos="far_left", ypos="head")
    lun "I didn't think I'd be able to release this many at once." ("smile", "narrow", "base", "down")
    gen "Sure took me by surprise..." ("grin", xpos="far_left", ypos="head")

    lun "Am I a master baiter now?" ("crooked_smile", "base", "base", "mid")
    gen "Why yes indeed, [name_luna_genie]." ("grin", xpos="far_left", ypos="head")
    gen "I hereby grant you the title of a {i}masturbater{/i}!" ("grin", xpos="far_left", ypos="head")
    lun "Yay!" ("crooked_smile", "happyCl", "base", "mid")

    lun "Alright then, off I--" ("crooked_smile", "base", "base", "R")
    lun "Hold on..." ("angry", "wide", "base", "mid")
    lun "I just realised something, [name_genie_luna]!" ("disgust", "base", "base", "mid")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    lun "What you said earlier about you believing I was born to do this." ("grin", "base", "base", "mid")
    gen "Do what?" ("base", xpos="far_left", ypos="head")
    lun "Master bait." ("crooked_smile", "narrow", "base", "mid")
    gen "Oh... What of it?" ("base", xpos="far_left", ypos="head")
    lun "I wonder if...{w=0.4} It might be my destiny!" ("smile", "wide", "base", "mid")
    gen "(What is she on about now...)" ("base", xpos="far_left", ypos="head")
    gen "Why do you ask?" ("base", xpos="far_left", ypos="head")
    lun "Professor Trelawney told me during our latest reading!" ("smile", "base", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "(I suppose I'll humour her...)" ("base", xpos="far_left", ypos="head")
    lun "She said that I'll soon find something new within me that will propel me forward on the path towards my destiny." ("grin", "base", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    lun "Don't you think she meant my fingers, [name_genie_luna]?" ("grin", "base", "base", "mid")
    gen "*Err*..." ("base", xpos="far_left", ypos="head")
    lun "Hold on... That can't be it... My fingers aren't new... I've had them for as long as I can remember." ("angry", "narrow", "base", "downL")
    lun "What do you think it is, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "(Something new within her... Why does future telling always have to be so vague...)" ("base", xpos="far_left", ypos="head")
    gen "*Hmm*... Well, I can't say that I..." ("base", xpos="far_left", ypos="head")
    gen "(Hold on...)" ("grin", xpos="far_left", ypos="head")
    lun "*Huh*? Did you have a revelation, [name_genie_hermione]?" ("grin", "base", "raised", "mid")
    gen "You've just given me a great idea!" ("grin", xpos="far_left", ypos="head")
    lun "Oooh! What is it? Is it a new method of dealing with the Wrackspurts?" ("crooked_smile", "base", "base", "mid")
    gen "Why yes indeed, [name_luna_genie]!" ("base", xpos="far_left", ypos="head")
    lun "Marvellous!" ("smile", "happyCl", "base", "mid")
    gen "Although it might be a hard one, so I hope you're ready to take it on, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "Of course, as long as you're there to guide me..." ("grin", "wink", "base", "mid")
    gen "{size=-4}I'll be guiding something alright...{/size}" ("grin", xpos="far_left", ypos="head")
    lun "[name_genie_luna]?" ("soft", "narrow", "base", "mid")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    gen "*Ahem*... I'll let you know once I'm ready to begin our next set of tests." ("base", xpos="far_left", ypos="head")
    lun "Great!" ("base", "base", "base", "mid")
    lun "Until next time then, [name_genie_luna]..." ("grin", "base", "base", "mid")

    call lun_walk(action="leave")

    jump ll_pf_masturbate_end


label ll_pf_masturbate_T3_E4_repeat:

    call ll_pf_masturbate

    gen "Ready to avert the spurts?" ("base", xpos="far_left", ypos="head")
    lun "Avert them, [name_genie_luna]?" ("soft", "base", "base", "mid", trans=dissolve)
    gen "Ready to insert until you spurt and squirt?" ("base", xpos="far_left", ypos="head")
    lun "Oh!{w=0.4} Yes, I am ready!" ("base", "base", "base", "mid")
    gen "Great, then show me how it's done, master baiter!" ("base", xpos="far_left", ypos="head")

    #Luna chibi walks to desk
    call lun_walk("desk", "base")

    $ luna.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
    stop weather fadeout 4

    hide screen blkfade
    show CG luna as cg zorder 17:
        zoom 0.5
    with fade
    #start of masturbation section (in front of desk CG)

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("top", "bra")
    with d3

    gen "*Mmm*... Impressive..."
    lun "[name_genie_luna]?" ("soft", "base", "raised", "mid")
    gen "Your nipples, [name_luna_genie]... Are they always this perked up?"
    lun "Oh...{w=0.4} *Ehm*...{w=0.4} Kind of?" ("angry", "base", "base", "down")
    gen "Very impressive indeed..."
    gen "Why don't you give one a bit of a tweak and tell me how it feels?"
    lun "Oh...{w=0.4} Okay..." ("base", "base", "base", "mid")

    #Luna hand on nipple.
    $ luna.set_pose("hand_on_pussy_and_breast")
    $ luna.strip("top", "bra")

    lun "Like this?" ("soft", "base", "base", "mid")
    gen "Yes, that's it... Now pinch it with your fingers--"
    lun "Ouch!" ("mad", "base", "base", "stare")
    gen "... carefully..."
    gen "Patience, [name_luna_genie]..."
    lun "Sorry [name_genie_luna]..." ("disgust", "narrow", "base", "down")
    gen "So, how does it feel now? Any different?"
    lun "*Ehm*... It feels a bit harder than before..." ("soft", "narrow", "base", "down")
    gen "That's good, now try it a bit more gently and tell me if anything changes..."
    lun "Alright..." ("soft", "base", "base", "down")
    nar "Luna pinches her nipple more carefully this time, and an involuntary moan escapes her lips."
    lun "*Ah*..." ("open", "narrow", "base", "up")
    gen "So?"
    lun "It...{w=0.4} It's more sensitive than before." ("angry", "narrow", "base", "stare")
    gen "Excellent."
    nar "Luna pinches her nipple again, and tries to stifle another moan."
    lun "But--{w=0.2} *Ah*...{w=0.4} I must say it felt a lot better when you did it..." ("normal", "closed", "base", "stare")
    gen "You still seem to be enjoying yourself."
    lun "Yes... But--" ("annoyed", "closed", "base", "mid")
    gen "Aren't we here so that you can find ways to deal with this issue without me, [name_luna_genie]?"
    lun "We are?" ("disgust", "narrow", "base", "stare")
    gen "As a temporary measure that is... We'll still need to work together to find a way of ridding ourselves of them for good."
    lun "Oh... That's what you meant..." ("base", "closed", "base", "down")
    lun "I do feel a little bit guilty doing this though..." ("soft", "narrow", "base", "mid")
    gen "Guilty, in what way?"
    lun "Me doing this on my own in front of you feels a bit selfish now that I know how to do it..." ("open", "narrow", "base", "down")
    gen "Oh, I wouldn't worry about that, [name_luna_genie]..."
    gen "I'm thoroughly enjoying watching you touch yourself..."
    lun "You--{w=0.2} You are, [name_genie_luna]?" ("angry", "narrow", "base", "mid")
    gen "Of course!"
    gen "Didn't you enjoy watching me?"
    lun "Oh...{w=0.4} I suppose I did." ("base", "narrow", "base", "down")
    gen "Now undress for me, so I can watch you relieve yourself properly..."
    lun "Yes, [name_genie_luna]..." ("base", "base", "base", "mid")

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("clothes")
    with d3

    lun @ cheeks blush "" ("base", "closed", "base", "mid")
    nar "Luna slides the rest of her clothes off and begins rubbing herself."

    #Hand on pussy

    gen "That's better, don't you think?"
    lun "Much better...{w=0.4} Although they've been building up quite a bit since I started." ("soft", "narrow", "base", "down")
    gen "That's a good thing... Now just keep going as you've done before..."
    lun "Yes [name_genie_luna]..." ("base", "narrow", "base", "mid")

    nar "Luna moves her finger across her slit and then gently begins pushing it inside."

    play sound "sounds/slick_02.ogg"
    with kissiris
    lun @ cheeks blush "*Ah*..." ("base", "narrow", "base", "up")

    #Luna fingering
    play background "sounds/slickloop.ogg" fadein 2

    lun @ cheeks blush "*Mmm*..." ("base", "closed", "base", "mid")
    gen "Good..."
    gen "You sure seem to have found a way to keep yourself focused on the task, [name_luna_genie]..."
    lun @ cheeks blush "*Mmm*... Yes, [name_genie_luna]..." ("open", "closed", "base", "mid")
    gen "You should feel very proud of your accomplishments."
    lun @ cheeks blush "*Ah*...{w=0.4} Yes...{w=0.4} I feel it inside of me [name_genie_luna]..." ("soft", "closed", "base", "mid")

    play background "sounds/slickloopfast.ogg"
    lun @ cheeks blush "" ("soft", "narrow", "base", "mid")
    nar "Luna begins moving her fingers faster inside her as she stares at you intently."


    gen "I was very impressed with how quickly you got there last time..."
    gen "You've got to tell me your tricks, did you think of something in particular?"
    $ luna.set_cum(pussy="wet")
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} [name_genie_luna]..." ("base", "narrow", "base", "stare")
    gen "My apologies, I'll let you get on with it..."

    nar "You watch in silence as Luna fingers herself... Her heavy breathing, now being the only thing filling your chambers."
    lun @ cheeks blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*...{w=0.4}" ("grin", "narrow", "base", "up")
    gen "(Look at those fingers go... Now that's a girl with purpose.)"

    play background "sounds/slickloopveryfast.ogg"
    lun @ cheeks blush "" ("grin", "narrow", "base", "mid")
    nar "Looking at you once again, Luna starts moving her fingers even faster..."

    lun @ cheeks blush "*Ah*...{w=0.2} *Ah*...{w=0.2} [name_genie_luna]..." ("grin", "narrow", "base", "mid")
    gen "Yes, [name_luna_genie]?"

    lun @ cheeks blush "*Aaaah*!!!" ("crooked_smile", "narrow", "base", "up")

    play sound "sounds/slick_01.ogg"
    with kissiris
    #Luna Squirts

    $ luna.set_cum(pussy="squirt")
    pause .6
    #Non luna squirt
    $ luna.set_cum(pussy="squirt_post")

    play sound "sounds/slick_01.ogg"
    with kissiris
    #Luna Squirts
    $ luna.set_cum(pussy="squirt")
    pause .6
    #Non luna squirt
    $ luna.set_cum(pussy="squirt_post")

    lun @ cheeks blush "*[name_genie_luna]*!!{heart}" ("scream", "narrow", "base", "up")

    play sound "sounds/slick_01.ogg"
    stop background fadeout 2
    with kissiris
    #Luna Squirts
    $ luna.set_cum(pussy="squirt")
    pause .6
    #Non luna squirt
    $ luna.set_cum(pussy="squirt_post")
    lun @ cheeks blush "" ("crooked_smile", "narrow", "base", "stare")

    lun @ cheeks blush "*Ah*...{heart}" ("grin", "narrow", "base", "up")

    $ luna.set_pose(None)
    $ luna.strip("clothes")
    #Luna normal doll pose

    lun @ cheeks blush "*Mmm*..." ("base", "closed", "base", "mid")
    lun @ cheeks blush "Did I do good, [name_genie_luna]?" ("soft", "narrow", "base", "up")
    gen "Very good, [name_luna_genie]..."
    lun @ cheeks blush "*Ah*...{w=0.4} I'm glad..." ("base", "narrow", "base", "up")
    lun @ cheeks blush "..." ("base", "narrow", "base", "down") #More focused
    lun @ cheeks blush "Oh, no! Look at what has happened to your floor!" ("mad", "narrow", "base", "down")
    gen "I'm sure it's fine, it has seen worse I'm--"

    show CG lun_intro luna bendover naked as cg zorder 17:
        zoom 0.5
        easein_quad 10.0 zoom 1.0 pos (-1040, -600)
    #Luna naked bent over pose

    lun "Now where did I put my spectrespecs..." ("base", "base", "base", "mid")
    nar "Luna bends down and begins checking around the floor for her glasses."

    gen "Very fine indeed..."
    lun "Do you remember if I brought them or not, [name_genie_luna]?" ("base", "base", "base", "mid")
    lun "[name_genie_luna]?" ("angry", "narrow", "base", "mid")
    gen "*Huh*?"
    lun "My glasses... I can't see them without my glasses." ("base", "base", "base", "mid")
    gen "Jinkies..."
    lun "Blidgering humdinger...{w=0.4} I was hoping to see if they looked any different up close compared to yours..." ("base", "base", "base", "mid")
    gen "Don't worry about them [name_luna_genie], I'm sure you can get a closer look some other time..."
    lun "Alright..." ("base", "base", "base", "mid")

    hide cg
    show screen blkfade
    with d5

    nar "Luna turns around to face you and gives you a smile, seemingly still pleased with herself, even though she couldn't get a proper look through her glasses..."

    # End of masturbate section

    $ luna.set_pose(None)
    $ luna.strip("clothes")
    hide screen blkfade
    with d5

    call weather_sound

    #Luna normal pose
    #End of masturbate section (office screen)
    #Luna is still naked

    gen "So... How are you feeling?" ("base", xpos="far_left", ypos="head")
    lun "As if my mind has been cleared of a thick fog." ("base", "closed", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    gen "Ah yes... The post-nut clarity..." ("base", xpos="far_left", ypos="head")
    lun "The what? sorry?" ("soft", "base", "base", "mid")
    gen "The perfect time to make the big life decisions..." ("base", xpos="far_left", ypos="head")
    lun "I'm not sure I understand what you mean, [name_genie_luna]." ("upset", "base", "base", "mid")
    gen "It only gets more difficult at this point, now that you've mastered the art of masturbation [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "Mastered master baiting?" ("annoyed", "base", "raised", "mid") #confused
    gen "If we want to get rid of those spurts for good, then we need to keep trying new methods." ("base", xpos="far_left", ypos="head")
    lun "Oh! Well, I'm willing to do anything that it takes to save the school [name_genie_luna]!" ("grin", "narrow", "base", "mid")
    gen "That's what I like to hear." ("base", xpos="far_left", ypos="head")
    gen "Then that shall be all for today." ("base", xpos="far_left", ypos="head")
    lun "Okay, thank you [name_genie_luna]." ("base", "base", "base", "mid")

    hide luna_main
    with d3

    #Luna turns to door
    call lun_chibi(flip=True)
    pause .5

    gen "[name_luna_genie]." ("base", xpos="far_left", ypos="head")
    gen "Has the post nut clarity already worn off?" ("base", xpos="far_left", ypos="head")

    call lun_chibi(flip=False)
    pause .5

    lun "[name_genie_luna]?" ("soft", "base", "raised", "mid", trans=dissolve)
    gen "Your clothes..." ("base", xpos="far_left", ypos="head")
    lun "Oh!" ("mad", "narrow", "base", "down") #blush

    $ luna.wear("all")
    play sound "sounds/cloth_sound.ogg"
    $ luna.set_cum(None)
    with d3
    pause .5

    lun "There we go." ("grin", "narrow", "base", "mid")
    lun "I'm so used to walking around naked at home, so I didn't even realise..." ("grin", "happyCl", "base", "mid")
    gen "You walk around naked at home?" ("base", xpos="far_left", ypos="head")
    lun "Yes?" ("base", "base", "raised", "mid")
    gen "(No wonder she didn't look phased by taking her clothes off...)" ("base", xpos="far_left", ypos="head")
    gen "How very progressive..." ("base", xpos="far_left", ypos="head")
    lun "That way, there are fewer places for the Nargles to hide." ("grin", "base", "base", "mid")
    gen "I see..." ("grin", xpos="far_left", ypos="head")
    gen "(Just smile and nod...)" ("grin", xpos="far_left", ypos="head")
    gen "Well then... I'll let you know when our next session will be [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "Of course... Thank you [name_genie_luna]." ("base", "base", "base", "mid")
    if game.daytime:
        gen "Now, you best head back to class." ("base", xpos="far_left", ypos="head")
    else:
        gen "Now, you best head back to your dorm." ("base", xpos="far_left", ypos="head")
    lun "Yes [name_genie_luna]." ("grin", "base", "base", "mid")
    lun "Until next time..." ("base", "base", "base", "mid")

    call lun_walk(action="leave")

    if states.lun.level < 24:
        $ states.lun.level = 24
        call end_of_content

    jump ll_pf_masturbate_end
