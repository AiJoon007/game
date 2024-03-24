
label potion_luna_make:

    call give_reward("You have successfully created a new potion!", luna_potion_ITEM)

    play sound "sounds/sniff.ogg"
    gen "It does have a distinctive smell of grass, among other things..." ("base", xpos="far_left", ypos="head")
    gen "I wonder if Hermione will be able to tell whose DNA contributed to it." ("base", xpos="far_left", ypos="head")
    return

label her_potion_luna_give:

    $ lun_outfit_last.save() #Save Luna clothing
    $ luna.equip(lun_outfit_default) #Equip Luna Default clothing

    if hermione.is_worn("robe"):
        gen "Before we begin... Why don't you take those robes off and make yourself comfortable." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("soft", "squint", "base", "mid")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        with d3
        gen "Now then..." ("base", xpos="far_left", ypos="head")

    gen "Might I offer you a drink?" ("base", xpos="far_left", ypos="head")

    if states.her.level < 19:
        her "Are you sure it's wise to be giving me alcohol, [name_genie_hermione]?" ("soft", "squint", "base", "mid")
        gen "It's not alcohol, [name_hermione_genie]... Just a harmless little potion." ("base", xpos="far_left", ypos="head")
    else:
        her "Trying to get me drunk, are you?" ("soft", "narrow", "base", "mid")
        gen "Nothing of the sort, just a harmless little potion." ("base", xpos="far_left", ypos="head")

    nar "You hand Hermione the potion bottle."
    call her_chibi("hold_potion","mid","base")
    with d3

    if not states.her.ev.potions.polyjuice_drank:
        $ states.her.ev.potions.polyjuice_drank = True

        if states.her.level < 19:
            her "Let me guess, you're not going to tell me what it does." ("angry", "narrow", "base", "mid")
            gen "Of course not, where would the fun be in that..." ("base", xpos="far_left", ypos="head")
            her "Typical..." ("angry", "narrow", "base", "down")
            gen "Just imagine all the points you'll earn for Gryffindor." ("base", xpos="far_left", ypos="head")
            her "That's true... I can't let Gryffindor down." ("angry", "squint", "base", "mid")
        else:
            her "I see..." ("open", "base", "base", "mid")
            her "So what does this potion do exactly?" ("soft", "base", "base", "mid")
            gen "It makes your breath smell like strawberries." ("base", xpos="far_left", ypos="head")
            her "Does it--" ("grin", "base", "base", "mid")
            her "Of course it doesn't..." ("angry", "narrow", "base", "R")
            gen "You'll just have to drink it to find out, I suppose." ("base", xpos="far_left", ypos="head")
            her "Let's see if I can guess what is first..." ("base", "narrow", "base", "down")

        call her_chibi("sniff_potion","mid","base")
        pause 0.2
        play sound "sounds/sniff.ogg"
        pause 0.6
        call her_chibi("hold_potion","mid","base")
        nar "Hermione takes a quick sniff of the potion."

        her "*Hmm*... It smells weirdly familiar, like freshly cut grass, or--" ("base", "narrow", "base", "down")
        gen "Weed!" ("grin", xpos="far_left", ypos="head")
        her "Weeds? I suppose that is similar to grass." ("open", "squint", "base", "mid")
        her "It also kind of reminds me of Mr Xenoph--" ("open", "closed", "base", "mid")
        gen "Shush, let's not spoil the fun with all the guessing." ("base", xpos="far_left", ypos="head")
        her "... Fine." ("base", "base", "base", "mid")

    else:
        her "Is this..." ("angry", "narrow", "base", "down")
        gen "Yep, another Polyjuice potion." ("base", xpos="far_left", ypos="head")
        her "Do I really have to drink this again?" ("angry", "base", "base", "mid")
        gen "If you'd like to continue our favour trading, it would certainly be in your best interest, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        if states.her.level < 19:
            her "..." ("normal", "narrow", "base", "mid")
        else:
            her @ cheeks blush "Now, there's no need to go to such extremes..." ("open", "squint", "base", "R")

        her "Can you at least tell me what you've put in it?" ("angry", "base", "base", "mid")
        gen "Where's fun in that? You're going to have to drink it and find out..." ("base", xpos="far_left", ypos="head")

        if states.her.ev.potions.polyjuice_cat_drank:
            her "One of the last potions you gave me before tasted like wet puss..." ("disgust", "base", "base", "mid")
            gen "And it turned you into one as well!" ("grin", xpos="far_left", ypos="head")
            her "*Tsk!*" ("angry", "narrow", "base", "R")

        her "..." ("disgust", "narrow", "base", "down")
        gen "Bottoms up, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "... I hope this is one of the ones that goes down okay." ("angry", "narrow", "base", "down")

    call her_chibi("drink_potion","mid","base")
    pause 0.6
    play sound "sounds/gulp.ogg"
    pause 0.8
    call her_chibi("stand","mid","base")
    nar "Hermione downs the golden-hued potion."

    her "*Smacks lips*" ("grin", "closed", "base", "mid")

    if not states.her.ev.potions.polyjuice_luna_drank:
        her "It didn't taste so bad actually... Kind of sweet and sour." ("grin", "base", "base", "mid")
        gen "As long as you keep it down, you'll earn Gryffindor a great deal of points." ("base", xpos="far_left", ypos="head")
        her "I will." ("open", "closed", "base", "mid")
        her "So... What now?" ("base", "base", "base", "mid")
        gen "Let's wait and see if the potion is going to work." ("base", xpos="far_left", ypos="head")
        gen "For now, why don't you tell me a bit about how you've been." ("base", xpos="far_left", ypos="head")
        her "Alright." ("open", "base", "base", "mid")
        her "Well, ever since I started my \"Extracurricular activities\" with you, my attendance and grades started slipping." ("open", "closed", "base", "mid")

        menu:
            "\"Troubling indeed...\"":
                if states.her.level < 16:
                    her "It is! [name_genie_hermione], I used to be at the top of the class. My scores were impeccable." ("angry", "squint", "worried", "mid")
                    gen "And how are your scores now?" ("base", xpos="far_left", ypos="head")
                    her "I'm still at the top... Just not by much." ("open", "closed", "base", "mid")
                    gen "Well, there are times when academic excellence shouldn't be your primary concern." ("base", xpos="far_left", ypos="head")
                    her "*Hmph*... And what \"should\" be my primary concern, then?" ("angry", "narrow", "base", "mid")
                    gen "Currently. I'd say your face is pretty high on the list." ("base", xpos="far_left", ypos="head")
                    her "Excuse me? This is hardly appropriate--" ("angry", "narrow", "annoyed", "mid")
                elif states.her.level < 22:
                    her "That said... We have been earning a lot of points for Gryffindor." ("base", "squint", "base", "R")
                    gen "You have, you mean." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "I suppose..." ("base", "narrow", "base", "down")
                    her "Although it's easier just to say \"we\" as I can't tell them where the majority of those points came from." ("open", "closed", "base", "mid")
                    gen "That is true... If you told them, they probably wouldn't be able to be able to look at you the same way." ("base", xpos="far_left", ypos="head")
                    her "Yeah..." ("open", "narrow", "base", "down")
                    gen "I mean... Soon enough, you won't even look the same!" ("base", xpos="far_left", ypos="head")
                    her "What do you mean?" ("angry", "base", "worried", "mid")
                    her "I'm still the same person am I not--" ("annoyed", "squint", "worried", "mid")
                else:
                    her @ cheeks blush "Well... I suppose it's not the worst thing in the world..." ("soft", "narrow", "base", "down")
                    her @ cheeks blush "Grades aren't everything." ("angry", "closed", "base", "mid")
                    gen "Is that so?" ("base", xpos="far_left", ypos="head")
                    her "Well... I'm sure if I wanted to, I could get a ministry job by recommendation." ("base", "wink", "base", "mid")
                    gen "..." ("base", xpos="far_left", ypos="head")
                    her "Right?..." ("angry", "squint", "base", "mid")
                    gen "I suppose you could try persuading Miss Tonks to give you one." ("base", xpos="far_left", ypos="head")
                    her "Oh... I was thinking perhaps you could... *Ehm*..." ("angry", "squint", "base", "R")
                    gen "Me? And willingly hand over my favourite little slut to some bureaucrats?" ("base", xpos="far_left", ypos="head")
                    gen "No way!" ("base", xpos="far_left", ypos="head")
                    her "But [name_genie_hermione]!" ("clench", "base", "worried", "mid")
                    gen "Don't give me that face..." ("base", xpos="far_left", ypos="head")
                    her "But--" ("angry", "base", "worried", "mid")

            "\"I bet you'd get the top grade in dick sucking class!\"":
                if states.her.status.blowjob:
                    her @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "base", "mid")
                    gen "Oh, don't be so modest. If sucking dick was a class, you'd be {i}Magna Cum Laude{/i}." ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I'm not sure if that's appropriate, but thanks, I suppose..." ("angry", "narrow", "base", "R")
                    her @ cheeks blush "You know... There's still time to earn some house points before class. If you're feeling generous, I could..." ("open", "narrow", "base", "down")
                    gen "I'd have to know on whose face I'll be cumming on, though." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "What do you mean? My face of course--" ("angry", "squint", "base", "mid")
                elif states.her.level < 16:
                    her "[name_genie_hermione]!" ("angry", "base", "worried", "mid")
                    her "I can't believe you'd say such a thing!" ("clench", "squint", "worried", "mid")
                    gen "Well, you'll never know if you don't try." ("base", xpos="far_left", ypos="head")
                    her "*Hmph*" ("annoyed", "squint", "annoyed", "R")
                    gen "In any case, that's not why you're here today." ("base", xpos="far_left", ypos="head")
                    her "Then why am I here? What's this potion supposed to do anyway?" ("angry", "closed", "annoyed", "mid")
                    gen "I'm sure we'll find out any--" ("base", xpos="far_left", ypos="head")
                else:
                    her @ cheeks blush "How dare you even suggest such a thing." ("angry", "base", "base", "mid")
                    gen "Oh come on, it's not like you haven't thought about it." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Well, maybe, but I have never done such a thing before..." ("annoyed", "closed", "base", "mid")
                    gen "We could change that right now if you'd like'." ("grin", xpos="far_left", ypos="head")
                    gen "I'd have to know on whose face I'll be cumming on, though." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "What do you mean whose face you will be--" ("clench", "base", "base", "mid")

        play sound "sounds/burp.ogg"
        her "*Burp*" ("full", "happyCl", "worried", "mid")
        her "...{w=0.5}{nw}" ("mad", "happyCl", "base", "mid")
        her "...{fast}" ("mad", "base", "base", "mid")
        her @ cheeks blush "I beg your pardon, I'm not sure where that came from--" ("mad", "squint", "base", "mid")

        # Sets Luna's initial facial expression to the ones Hermione had just a moment ago (more or less)
        $ luna.set_face(mouth="mad", eyes="narrow", eyebrows="base", pupils="mid")
    else:
        her "Not bad. So, what now?" ("base", "squint", "base", "mid")
        gen "Just wait here for a moment until the potion starts taking effect." ("base", xpos="far_left", ypos="head")
        her "Okay." ("open", "squint", "base", "R")
        gen "Until then, why don't you tell me a little bit about how your day's been going." ("base", xpos="far_left", ypos="head")
        her "Alright." ("base", "base", "base", "mid")

        if states.her.level < 16:
            her "There's not much to tell you that you don't already know." ("open", "closed", "base", "mid")
            her "Lately I've been questioning my previous outlook on life in general." ("open", "narrow", "base", "R")
            gen "In what way exactly?" ("base", xpos="far_left", ypos="head")
            her "Well, since we started our... mutually beneficial... agreement, or whatever we call this..." ("disgust", "narrow", "base", "R")
            her "The general atmosphere in our common room has been at an all-time high because of how many house points we're racking in." ("open", "narrow", "base", "down")
            gen "That's good, you must feel a great sense of pride and accomplishment." ("base", xpos="far_left", ypos="head")
            her "Of course! The only issue is that I would never be able to tell them I'm the one to thank for it..." ("angry", "narrow", "base", "mid")
            her "If they just got one look at my face, then they'd be able to tell what was up." ("disgust", "base", "base", "mid")
            gen "Speaking of..." ("base", xpos="far_left", ypos="head")

            # Sets Luna's initial facial expression to the ones Hermione had just a moment ago
            $ luna.set_face(mouth="disgust", eyes="base", eyebrows="base", pupils="mid")
        elif states.her.level < 19:
            her "It's been pretty good, thanks for asking." ("base", "closed", "base", "mid")
            her "The morale has never been higher in the common room." ("grin", "base", "base", "mid")
            her "I feel like we might actually have a chance at winning this year." ("smile", "base", "base", "mid")
            gen "All thanks to you, I'm sure." ("base", xpos="far_left", ypos="head")
            gen "(You're lucky you've got me instead of the real old man, I bet he'd never rig the points like this...)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well... You've also kindly allowed me to earn these points..." ("open", "closed", "base", "mid")
            gen "That I have." ("base", xpos="far_left", ypos="head")
            gen "Although who knows... I might get confused and award the point to some other house in a minute." ("base", xpos="far_left", ypos="head")
            her "*Hmm*... So, the potion is not going to turn me into another Gryffindor--" ("angry", "narrow", "base", "down")

            # Sets Luna's initial facial expression to the ones Hermione had just a moment ago
            $ luna.set_face(mouth="angry", eyes="narrow", eyebrows="base", pupils="down")
        else:
            her "Well, generally it's been quite dull, until now." ("open", "closed", "base", "mid")
            her "I would be lying if I said I wasn't a little bit excited when you called on me." ("grin", "narrow", "base", "R")
            gen "Oh, you'll be getting your fair share of excitement soon enough, well, at least the {i}new you{/i} will." ("grin", xpos="far_left", ypos="head")
            her "What do you mean by that--" ("angry", "base", "base", "mid")

            # Sets Luna's initial facial expression to the ones Hermione had just a moment ago
            $ luna.set_face(mouth="angry", eyes="base", eyebrows="base", pupils="mid")

    stop music fadeout 2
    hide hermione_main
    with d3

    pause 2

    play sound "sounds/magic4.ogg"
    show screen gfx_effect(584, 340, img="smoke", zoom=0.85)
    call her_chibi("hide")
    call lun_chibi(xpos="mid", ypos="base")

    $ luna_name_old = name_luna_genie
    $ name_luna_genie = "Hermione?"

    pause 2

    play music "music/wallpaper-by-kevin-macleod.ogg" fadein 1 if_changed

    show CG luna as cg zorder 17:
        zoom 0.5

    $ luna.set_face(mouth="disgust", eyes="closed", eyebrows="base", pupils="mid")
    hide screen blkfade
    with fade

    pause 1

    if not states.her.ev.potions.polyjuice_luna_drank:
        lun "*Ughhh*... My head..."
        lun "I feel like I'm going to throw up!" ("mad", "narrow", "base", "mid")
        gen "Well you look fine to me!" ("grin", xpos="far_left", ypos="head")

        nar "Hermione starts examining herself, feeling out her new assets and pausing at her breasts."

        lun "*Hmm*... That's a Polyjuice potion, alright..." ("angry", "narrow", "base", "down")
        lun "And apparently I'm still a girl... Someone from Ravenclaw?" ("open", "base", "raised", "mid")
        gen "Keen observation, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        nar "Hermione examines her new hair."
        lun "Definitely a blonde... She sure could use a comb." ("angry", "narrow", "raised", "downR")
        lun "*Hmm*..." ("normal", "narrow", "low", "down")

        nar "Something suddenly dawns on Hermione."

        lun "You turned me into Loony--{w=0.4} I mean Luna Lovegood?!" ("clench", "wide", "base", "mid")
        gen "Very astute, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "And now if you don't mind, I'd like you to bare your--, her chest for me..." ("base", xpos="far_left", ypos="head")
        lun "What?!" ("disgust", "wide", "base", "mid")

        if states.her.level < 16:
            lun @ cheeks blush "I can't believe what you're suggesting, you're asking me to show off another student's breasts?" ("disgust", "base", "annoyed", "mid")
            gen "Well, what else would you have me do? Look at your face?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "I...{w=0.4} Yes?" ("annoyed", "narrow", "raised", "mid")
            gen "Come on... You've drank the potion... Don't you think it'd be a bit of a waste?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "But [name_genie_hermione]." ("clench", "base", "base", "mid")
            gen "I'm sure it's fine... It's not like I would tell her anyway." ("base", xpos="far_left", ypos="head")
            gen "Don't you want those points?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "..." ("upset", "narrow", "base", "downR")
            lun @ cheeks blush "Fine..." ("open", "narrow", "base", "down")

        else:
            lun "You can't possibly be interested in that... That girl's paltry breasts." ("annoyed", "narrow", "annoyed", "mid")
            gen "Currently they're yours. And they don't look so paltry from where I'm sitting [name_hermione_genie]. Do I detect a hint of jealousy?" ("base", xpos="far_left", ypos="head")
            lun "Not at all... I suppose it is only natural that someone of your advanced age has trouble with their--" ("open", "closed", "base", "mid")
            gen "Their what [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Nothing..." ("annoyed", "narrow", "base", "R")
            gen "Eyesight?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "*Ehm*... No, what I was going to say--" ("angry", "narrow", "base", "mid")
            gen "Is that any way to talk to your elders, [name_hermione_genie]? Perhaps you need a good spanking to remind you of your manners." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "I... I apologize, [name_genie_hermione]. I don't know what came over me." ("open", "narrow", "base", "mid")
            gen "Apology accepted. I'm sure they can't hold a candle to the brilliance of your own." ("base", xpos="far_left", ypos="head")
            lun "I'd like to think I'm more than just a pair of breasts... but thank you [name_genie_hermione]. That was flattering... In a way." ("angry", "closed", "base", "mid")
            gen "If you want to dispel all doubt, we could compare. Why don't you lift your shirt and show me what you... *Err*... She's got under that sweater." ("base", xpos="far_left", ypos="head")
            lun "I'm still not entirely comfortable with this..." ("angry", "narrow", "base", "down")

    else:
        lun "*Urgh*... Every time..." ("disgust", "narrow", "base", "stare", trans=d3)
        lun "Did it work?" ("angry", "narrow", "raised", "mid")
        gen "Perfectly..." ("base", xpos="far_left", ypos="head")

        nar "Hermione starts examining herself, feeling out her outfit and pausing at her breasts."

        lun "*Hmm*... At least I still appear to be a girl... A Ravenclaw." ("upset", "narrow", "raised", "down")
        gen "I'm surprised you expected something different." ("base", xpos="far_left", ypos="head")

        if states.her.ev.potions.polyjuice_cat_drank:
            lun "Well... Seeing that you've previously tried to turn me into a cat." ("open", "narrow", "base", "mid")
            gen "A cat-girl actually..." ("base", xpos="far_left", ypos="head")
            lun "..." ("disgust", "narrow", "base", "mid")

        nar "Hermione examines her new hair."

        lun "*Hmm*... A blonde... that narrows things down. Not a good sign..." ("normal", "narrow", "base", "downR")
        gen "And why might that be?" ("base", xpos="far_left", ypos="head")
        lun "Well... Unless I'm completely mistaken..." ("open", "closed", "base", "mid")
        lun "You've turned me into Luna Lovegood. Again." ("angry", "narrow", "base", "mid")
        gen "Yeah!" ("base", xpos="far_left", ypos="head")
        lun "What is your obsession with this crazy blonde girl?" ("upset", "narrow", "annoyed", "mid")
        gen "Now-now... You're the one looking like her, remember." ("base", xpos="far_left", ypos="head")
        gen "Unless you're referring to yourself, there's nothing wrong with the way she looks." ("base", xpos="far_left", ypos="head")
        lun "..." ("annoyed", "narrow", "base", "R")
        gen "Now, I'd like to see those great assets of hers..." ("base", xpos="far_left", ypos="head")

        if states.her.level <= 16:
            lun "This again? It was already bad enough that I agreed to do it before..." ("disgust", "narrow", "base", "mid")
            gen "There weren't any repercussions, were there?" ("base", xpos="far_left", ypos="head")
            lun "..." ("annoyed", "narrow", "base", "down")
            lun "I suppose not..." ("angry", "narrow", "base", "down")
            gen "Then get those puppies out for me." ("base", xpos="far_left", ypos="head")

        lun "Alright." ("open", "narrow", "base", "mid")

    nar "Hermione quickly strips off her Ravenclaw top."

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("top")

    pause .8
    lun @ cheeks blush "..." ("normal", "narrow", "base", "down")
    gen "Go on then..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bra")

    if not states.her.ev.potions.polyjuice_luna_drank:
        if states.her.level < 16:
            lun @ cheeks blush "..." ("normal", "narrow", "base", "down")
            lun @ cheeks blush "This feels wrong..." ("open", "narrow", "low", "down")
            gen "Feels pretty right to me!" ("grin", xpos="far_left", ypos="head")
            gen "Although I could do with a closer look." ("grin", xpos="far_left", ypos="head")
            lun @ cheeks blush "You're not going to touch her--" ("clench", "narrow", "base", "mid")
            gen "Just come up to the front of my desk, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "...{w} Alright." ("mad", "base", "base", "mid")

        else:
            pause .5
            lun @ cheeks blush "There, see... Perfectly ordinary breasts." ("open", "closed", "annoyed", "mid")
            lun @ cheeks blush "Absolutely no need to keep looking at them." ("soft", "narrow", "annoyed", "downR")
            gen "I'm not quite convinced, the soft pale skin, the cute pink nipples... They look like quite a handful..." ("base", xpos="far_left", ypos="head")
            gen "I think you might have some serious competition here [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            lun "You can't be serious! They're saggy and couldn't even fill your palm!" ("angry", "narrow", "annoyed", "mid")
            gen "*Hmm*... Well, I sure wouldn't use the word \"saggy\"... Perhaps a closer examination is required." ("base", xpos="far_left", ypos="head")
            lun "Surely you can see from there how--" ("angry", "narrow", "annoyed", "down")
            gen "No, I think I'd need a closer look [name_hermione_genie]... Seeing that my eyesight is so terrible and all..." ("base", xpos="far_left", ypos="head")
            lun "..." ("angry", "narrow", "annoyed", "down")
            gen "Come closer, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    else:
        pause .5
        lun @ cheeks blush "I assume you'd like a closer look like the last time?" ("open", "closed", "base", "mid")
        gen "Of course!" ("base", xpos="far_left", ypos="head")
        gen "Get those cute pink nipples up here." ("base", xpos="far_left", ypos="head")

    hide luna_main
    with d3

    call lun_walk(xpos="desk")

    nar "In a huff, Hermione walks over and presents her new set of breasts."
    lun @ cheeks blush "" ("annoyed", "base", "base", "R", trans=dissolve)
    call ctc

    if not states.her.ev.potions.polyjuice_luna_drank:
        if states.her.level < 16:
            gen "Very good." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "..." ("upset", "narrow", "base", "down")
            lun @ cheeks blush "Am I done here?" ("open", "closed", "base", "mid")
        else:
            gen "Yes... Upon closer inspection, I must say those are some magnificent tits..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "base", "mid")
            gen "But Hermione's will always remain my favourite." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "I'm glad you've come to your senses... Well, if you're completely satisfied, I'll cover up these... things." ("open", "closed", "base", "mid")
    else:
        gen "You look a bit flustered [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        lun @ cheeks blush "You're staring directly at my, well, her chest, [name_genie_hermione], and I can't help but feel a bit undefined as it's not my own..." ("angry", "narrow", "base", "mid")
        lun @ cheeks blush "Am I free to go now?" ("open", "narrow", "base", "mid")

    menu:
        "-Tell her to take the rest off.-":
            gen "Not yet." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "*Hmm*?" ("annoyed", "narrow", "base", "mid")
            gen "You haven't bared it all just yet." ("grin", xpos="far_left", ypos="head")

            if not states.her.ev.potions.polyjuice_luna_nude:
                $ states.her.ev.potions.polyjuice_luna_nude = True

                if states.her.level < 16:
                    lun @ cheeks blush "You want me to strip naked?" ("clench", "base", "base", "mid")
                    gen "Of course!" ("grin", xpos="far_left", ypos="head")
                    lun @ cheeks blush "Why?" ("upset", "narrow", "annoyed", "mid")
                    gen "To give you a chance to earn some extra points, obviously." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "That's not really the answer I was looking for..." ("upset", "narrow", "base", "R")
                    lun @ cheeks blush "..." ("upset", "narrow", "base", "down")
                    lun @ cheeks blush "{size=-4}I'm sorry, Luna...{/size}" ("normal", "happyCl", "base", "mid")
                    lun @ cheeks blush "I want fifty points." ("scream", "happyCl", "base", "mid")
                    gen "That's a bit much, don't you think?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "You're asking me to take the clothes off another student without their permission..." ("mad", "narrow", "base", "mid")
                    gen "Well technically--" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "..." ("angry", "narrow", "annoyed", "mid")

                    menu:
                        "-Give her the points.-":
                            gen "Alright, fifty points it is..." ("base", xpos="far_left", ypos="head")
                            $ current_payout = 50

                        "-Finish for today.-":
                            gen "No, In that case it will have to do for--" ("base", xpos="far_left", ypos="head")
                            lun @ cheeks blush "Thirty points!" ("clench", "happyCl", "base", "mid")
                            gen "..." ("base", xpos="far_left", ypos="head")
                            gen "Now who's being quick, selling out their fellow students body..." ("base", xpos="far_left", ypos="head")
                            lun @ cheeks blush "...Are you done?" ("upset", "narrow", "annoyed", "L")
                            gen "Quite, but not quite." ("grin", xpos="far_left", ypos="head")

                            gen "Thirty points it is..." ("base", xpos="far_left", ypos="head")
                            $ current_payout = 30

                    lun @ cheeks blush "..." ("normal", "narrow", "base", "down")
                    gen "Go on then..." ("base", xpos="far_left", ypos="head")

                    play sound "sounds/cloth_sound3.ogg"
                    $ luna.strip("bottom", "panties")
                    call ctc

                    lun @ cheeks blush "" ("normal", "narrow", "base", "mid")
                    gen "Very good..." ("grin", xpos="far_left", ypos="head")
                    gen "Now, let me just get my--" ("grin", xpos="far_left", ypos="head")

                    # Hide early to show chibi
                    hide screen animatedCG
                    with fade

                    pause 0.5

                    play sound "sounds/zipper.ogg"
                    call gen_chibi("jerk_off_behind_desk")
                    with d3

                    pause 1

                    lun @ cheeks blush "No!" ("clench", "wide", "base", "mid", trans=hpunch)

                    call gen_chibi("jerk_off_behind_desk_pause")
                    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I can't let you... That's... That's enough..." ("mad", "happyCl", "base", "mid")

                    play sound "sounds/zipper.ogg"
                    call gen_chibi("sit_behind_desk")
                    with d3
                    gen "Fine..." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "..." ("angry", "narrow", "base", "mid")

                    jump .end
                else:
                    $ current_payout = 20

                    lun @ cheeks blush "What?" ("mad", "base", "base", "mid")
                    gen "How am I supposed to get a good comparison if you're still wearing clothes." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "You were supposed to compare our breasts!" ("scream", "narrow", "annoyed", "mid")
                    gen "Well..." ("base", xpos="far_left", ypos="head")
                    gen "There's always more things worth comparing, don't you think?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "*Hmph*..." ("angry", "narrow", "annoyed", "R")
                    gen "Now-now [name_hermione_genie]... There are some points in it for you if you do it." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I don't care about the points..." ("angry", "base", "annoyed", "mid")
                    gen "You don't?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I mean... I do... But it's not about that!" ("annoyed", "base", "annoyed", "mid")
                    gen "You know your tits will always be my favourite, there's no need to be jealous." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I am not jealous!" ("angry", "base", "base", "mid")
                    gen "What is it then, are you afraid her delicate flower will be prettier than yours?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I am not afraid!" ("scream", "closed", "annoyed", "mid")
                    gen "Then prove it!" ("base", xpos="far_left", ypos="head")

                    play sound "sounds/cloth_sound3.ogg"
                    $ luna.strip("bottom", "panties")
                    call ctc

                    gen "Perfect!" ("grin", xpos="far_left", ypos="head")
                    lun @ cheeks blush "..." ("annoyed", "narrow", "annoyed", "mid")
                    gen "I mean... Adequate!" ("base", xpos="far_left", ypos="head")
                    gen "Of course I can't really tell for sure unless you were stood side by side..." ("base", xpos="far_left", ypos="head")
                    gen "Maybe some other time." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "..." ("angry", "narrow", "base", "mid")

            else: # Hermione stripped completely as Luna before
                lun @ cheeks blush "Right..." ("disgust", "narrow", "base", "down")

                if states.her.level < 16:

                    lun @ cheeks blush "And how many points would I--" ("angry", "base", "base", "mid")
                    gen "Thirty points." ("base", xpos="far_left", ypos="head")
                    $ current_payout = 30

                    lun @ cheeks blush "Alright then..." ("open", "narrow", "base", "mid")

                    play sound "sounds/cloth_sound3.ogg"
                    $ luna.strip("bottom", "panties")
                    pause .8
                    lun @ cheeks blush "" ("normal", "narrow", "base", "down")
                    call ctc

                    gen "You didn't even hesitate this time." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "Oh... Well, you've seen it already haven't you?" ("open", "narrow", "base", "mid")
                    gen "Yes... Although, I'd think you'd at least be a bit more hesitant about showing off another student's privates." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "*Hmm*... Honestly, after spending some more time around her, I do think you're right about her not caring about it that much..." ("open", "narrow", "base", "downR")
                    gen "Good enough for me." ("base", xpos="far_left", ypos="head")
                    gen "Then I suppose you don't mind if I--" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "No!" ("clench", "wide", "base", "mid")
                    gen "You didn't even let me finish..." ("base", xpos="far_left", ypos="head")
                    gen "Didn't you just say that Miss Lovegood wouldn't really care?" ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I..." ("disgust", "narrow", "base", "mid")
                    lun @ cheeks blush "Well, maybe she would care about this, stripping is one thing!" ("angry", "closed", "raised", "mid")
                    gen "Alright then [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                else:
                    $ current_payout = 20

                    lun @ cheeks blush "..." ("normal", "narrow", "base", "down")

                    play sound "sounds/cloth_sound3.ogg"
                    $ luna.strip("bottom", "panties")
                    call ctc

                    gen "Nice..." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "..." ("normal", "narrow", "base", "mid")
                    gen "Not as nice as your own, obviously..." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "Obviously..." ("open", "closed", "base", "mid")
                    gen "Although surely even you could admit..." ("base", xpos="far_left", ypos="head")
                    gen "Her nipples are pretty cute." ("base", xpos="far_left", ypos="head")
                    lun @ cheeks blush "I guess I could..." ("open", "narrow", "base", "R")
                    gen "*Heh-heh*." ("grin", xpos="far_left", ypos="head")
                    lun @ cheeks blush "Is that all?" ("angry", "narrow", "base", "mid")
                    gen "Yes, that shall do for today." ("base", xpos="far_left", ypos="head")

        "-Finish for today.-":
            gen "Yes, this will do for today..." ("base", xpos="far_left", ypos="head")

    label .end:

    show screen blkfade
    with d5
    pause .8
    $ luna.wear("all")
    hide cg
    hide luna_main
    hide screen blkfade
    with d5

    $ gryffindor += current_payout
    gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")

    lun "Thank you, [name_genie_hermione]..." ("open", "closed", "base", "mid", trans=dissolve)

    if not states.her.ev.potions.polyjuice_luna_drank:
        lun "I think I better head off to class now." ("angry", "base", "base", "R")
        gen "You're going to class looking like Miss Lovegood?" ("base", xpos="far_left", ypos="head")
        lun "Why not." ("base", "narrow", "base", "mid")
        lun "I can just pretend to be her, and who knows... Maybe I'll even improve her test scores." ("base", "narrow", "base", "mid")
        lun "You'll notify the teachers I can't attend class, right?" ("open", "base", "base", "mid")
        gen "Certainly. Just one more thing..." ("base", xpos="far_left", ypos="head")
        lun "Yes?" ("soft", "base", "raised", "mid")
        gen "What if you bump into her?" ("base", xpos="far_left", ypos="head")
        lun "Oh I wouldn't worry about that, [name_genie_hermione]..." ("grin", "narrow", "base", "R")
        lun "She will probably think I'm some kind of wrackspurts-induced hallucination or something." ("open", "closed", "base", "mid")
        gen "True." ("base", xpos="far_left", ypos="head")
        gen "Off you go then." ("base", xpos="far_left", ypos="head")
        lun "Good day, [name_genie_hermione]." ("base", "base", "base", "mid")
    else:
        lun "I'm off to class." ("open", "narrow", "base", "R")
        gen "Don't get up to any mischief will you?" ("base", xpos="far_left", ypos="head")
        lun "I would never..." ("smile", "narrow", "base", "mid")

    call lun_walk(action="leave")

    $ luna.equip(lun_outfit_last)
    $ name_luna_genie = luna_name_old
    $ states.her.ev.potions.polyjuice_luna_drank = True

    jump end_hermione_event
