
label potion_breasts_make:

    call give_reward("You have successfully created a new potion!", breast_potion_ITEM)

    gen "There we go." ("base", xpos="far_left", ypos="head")
    play sound "sounds/sniff.ogg"
    pause .5
    gen "Smells pretty good!" ("base", xpos="far_left", ypos="head")
    gen "I bet Hermione will love this one." ("base", xpos="far_left", ypos="head")
    return

label her_potion_breasts_give:

    if hermione.is_worn("robe"):
        gen "Before we begin... Why don't you take those robes off and make yourself comfortable." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("soft", "squint", "base", "mid")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        with d3
        gen "Now then..." ("base", xpos="far_left", ypos="head")
    else:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")

    $ current_payout = 20

    gen "What would it take for you to drink this potion?" ("base", xpos="far_left", ypos="head")
    nar "You bring out the potion and hand it to Hermione."
    call her_chibi("hold_potion","mid","base")
    with d3

    if not states.her.ev.potions.breast_expand_drank:
        her "A potion?" ("open", "squint", "base", "mid")
        gen "Why yes... And it's one of the nicer smelling ones." ("base", xpos="far_left", ypos="head")

        if states.her.level < 19:
            her "*Hmm*... You really want me to drink this?" ("angry", "narrow", "base", "mid")
            gen "Of course! I'll give you twenty points for it." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "squint", "base", "R")

        her "Alright then..." ("soft", "base", "base", "R")
    else: #Drank
        call her_chibi("sniff_potion","mid","base")
        pause 0.2
        play sound "sounds/sniff.ogg"
        pause 0.6
        call her_chibi("hold_potion","mid","base")

        if states.her.ev.potions.breast_expand_known:
            her "*Sniff*" ("normal", "happy", "base", "mid")
            her "Another breast expansion potion?" ("open", "squint", "base", "mid") #Neutral face
            gen "Good guess!" ("base", xpos="far_left", ypos="head")
            her "It does have that distinctive smell to it..." ("open", "squint", "base", "R") #Neutral face

            if states.her.level < 19:
                her "I mean... I guess it wasn't so bad." ("open", "closed", "base", "mid") #neutral face
                her "I had my teeth shrunk at some point too, so I'm not overly against body modifications..." ("open", "base", "base", "mid")
                gen "You had your teeth shrunk?" ("base", xpos="far_left", ypos="head")
                her "Yes?" ("disgust", "base", "base", "mid")
                gen "Really?" ("base", xpos="far_left", ypos="head")
                her "Do you want me to drink the potion or not?" ("annoyed", "narrow", "base", "mid")

                menu:
                    "\"No, you fucking weirdo!\"":
                        her @ cheeks blush "What did you just call me?" ("angry", "narrow", "annoyed", "mid")
                        gen "Oh, sorry, did I say that out loud?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("annoyed", "narrow", "annoyed", "mid")
                        gen "You had your teeth shrunk?" ("base", xpos="far_left", ypos="head")
                        gen "Now that's too much even for me..." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "What!?! Why!" ("disgust", "squint", "annoyed", "mid")
                        gen "..." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "You're teasing me again aren't you?" ("annoyed", "narrow", "annoyed", "R")
                        gen "..." ("grin", xpos="far_left", ypos="head")
                        her @ cheeks blush "Very funny, [name_genie_hermione]..." ("soft", "narrow", "base", "mid")
                        her @ cheeks blush "..." ("angry", "narrow", "base", "R")
                        her @ cheeks blush "So you want me to drink it or--" ("open", "narrow", "base", "mid")
                        gen "Yes!" ("base", xpos="far_left", ypos="head")
                    "\"Does the Pope shit in the woods?\"":
                        her "Huh?" ("disgust", "base", "base", "mid")
                        gen "Figuratively speaking." ("base", xpos="far_left", ypos="head")
                        her "..." ("annoyed", "squint", "base", "mid") # Still confused
                        gen "... It means yes, I want you to drink the potion." ("base", xpos="far_left", ypos="head")
                        her "(Weirdo...)" ("angry", "narrow", "base", "R")
                    "\"Yes, just don't make it weird.\"":
                        her "Hey, I'm not the one asking people to drink random concoctions, am I?" ("angry", "narrow", "base", "mid")
                        gen "Fair point." ("base", xpos="far_left", ypos="head")
        else:
            her "*Sniff*" ("normal", "squint", "base", "mid")
            her "This smells familiar." ("open", "squint", "base", "mid") #Neutral face
            her "Is it that other potion you gave me that had no effect?" ("open", "squint", "base", "R")
            gen "Maybe." ("base", xpos="far_left", ypos="head")
            her "Okay, I can drink that one." ("open", "closed", "base", "mid") # Slight smile
            her "Whatever you put in it, it made me sleep like a baby." ("base", "closed", "base", "mid") # Averts gaze (she's lying)
            gen "Hopefully it works this time..." ("base", xpos="far_left", ypos="head")

            show screen blktone
            with d3

            if states.her.level < 19:
                her "(Please don't work, please don't work.)" ("normal", "narrow", "base", "down")
                her "(My breast ached so much I couldn't even sleep...)" ("angry", "narrow", "base", "down")
                her "(I can't give him the satisfaction!)" ("angry", "closed", "base", "mid")
            else:
                her "*Sigh*..." ("base", "narrow", "base", "down")

                her @ cheeks blush "(My breasts ached so much...{w=0.4} I can't believe even the smallest touch almost made me cum on the spot...)" ("base", "narrow", "base", "down")
                her @ cheeks blush "(If I spend another night relieving myself I'll start running out of excuses for why I'm missing the morning class...)" ("normal", "narrow", "base", "down")
                gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                her "(Although it sure was enjoyable...)" ("base", "narrow", "base", "down")

            hide screen blktone
            with d3

            gen "Something wrong, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "N-- No, it's nothing." ("angry", "narrow", "base", "mid")
            gen "If you say so." ("base", xpos="far_left", ypos="head")

    nar "Hermione takes one last look at the potion and then brings it up to her mouth."
    her "Well then...{w=0.3} bottoms up!" ("angry", "base", "base", "mid")


    call her_chibi("drink_potion","mid","base")
    pause 0.6
    play sound "sounds/gulp.ogg"
    pause 0.8
    call her_chibi("stand","mid","base")
    nar "Hermione swallows the potion in a series of gulps."


    her "*Ahhh*..." ("open", "closed", "base", "mid")
    call her_chibi("stand", "mid", "base")

    if not states.her.ev.potions.breast_expand_drank:
        her "*shakes head*" ("angry", "happyCl", "base", "mid")
        her "*Ugh*, the smell wasn't so bad, but the taste..." ("disgust", "squint", "base", "mid")
        her "It's like sour milk." ("disgust", "narrow", "base", "mid")
        gen "You'll be fine." ("base", xpos="far_left", ypos="head")
        her "I would hope so..." ("open", "squint", "base", "mid")

    her "Now what?" ("open", "squint", "base", "mid")

    # Send to class, or
    # Tell her to take out/show off her tits
    menu:
        "-Send her to class-":

            if states.her.level < 19:

                if not states.her.ev.potions.breast_expand_drank:
                    gen "*Hmm*...{w=0.4} It appears as if the potion may have been a failure or something should've happened." ("base", xpos="far_left", ypos="head")
                    her "Oh... So, what should I--" ("soft", "base", "base", "mid")

                    nar "You notice Hermione's breasts bounce slightly as the potion begins to take effect."

                    her "..." ("angry", "wide", "base", "stare") #surprised

                    gen "Something wrong [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    her "*Ehm*... No [name_genie_hermione]... I just thought I felt something for a moment." ("angry", "squint", "base", "mid")
                    gen "Right..." ("base", xpos="far_left", ypos="head")
                    gen "Well, since it didn't appear to work, you're free to go." ("base", xpos="far_left", ypos="head")
                else:

                    if states.her.ev.potions.breast_expand_known:
                        gen "Any moment now..." ("base", xpos="far_left", ypos="head")

                        nar "You notice Hermione's breasts bounce slightly as the potion begins to take effect."

                        her @ cheeks blush "*Ah*... I-- I think my breasts are--" ("angry", "narrow", "base", "down") # Slightly panting
                        gen "Itchy?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "No, that's not,{w=0.2} *Ah*...{w=0.4} it... It's hard to describe." ("open", "happyCl", "worried", "mid")
                        gen "In any case, you are free to leave and get back to class." ("base", xpos="far_left", ypos="head")
                        gen "Report back to me when you're done." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Y-- Yes [name_genie_hermione]..." ("angry", "squint", "base", "mid")
                        her "Can I have my points now?" ("angry", "base", "base", "R")
                    else:
                        gen "That's odd... Something should've happened." ("base", xpos="far_left", ypos="head")
                        her "Did you brew it right?" ("annoyed", "squint", "base", "mid")
                        gen "Of course I--" ("base", xpos="far_left", ypos="head")

                        nar "You notice Hermione's breasts bounce slightly as the potion begins to take effect."
                        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                        gen "I think you better head to class, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                        her "Of course, [name_genie_hermione]." ("open", "squint", "base", "mid")
                        her "Can I have my points then?" ("soft", "base", "base", "mid")

                    gen "Certainly." ("base", xpos="far_left", ypos="head")

                gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
                $ gryffindor += current_payout

                her "Thank you, [name_genie_hermione], I'll head to class then." ("open", "squint", "base", "mid")
            else: #19+

                if not states.her.ev.potions.breast_expand_drank:
                    gen "*Hmm*... Looks like a dud..." ("base", xpos="far_left", ypos="head")
                    her "A dud, [name_genie_hermione]?" ("annoyed", "squint", "base", "mid")
                    gen "Yes... Well then... You better head back to class for today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                    her "Already?" ("annoyed", "squint", "worried", "mid")
                    gen "Yes, I'll let you know once I've brewed another one of these." ("base", xpos="far_left", ypos="head")
                    her "Oh... Alright..." ("open", "narrow", "base", "down")
                else:

                    if states.her.ev.potions.breast_expand_known:
                        gen "Alright then, off to class you go..." ("base", xpos="far_left", ypos="head")
                        her "*Aww*... But I was hoping--" ("soft", "squint", "base", "R")
                        her "*Ahem*... I mean-- Alright..." ("open", "narrow", "base", "down")
                    else:
                        gen "Is it working, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                        her "It's difficult to say, I don't feel any different..." ("open", "squint", "base", "mid")
                        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                        gen "Then I maybe it's best you head back to class for today." ("base", xpos="far_left", ypos="head")
                        her "Oh... Okay." ("base", "squint", "base", "mid")
                        gen "Since you drank it, I suppose you've earned your points." ("base", xpos="far_left", ypos="head")

                gen "{number=current_payout} points to Gryffindor." ("base", xpos="far_left", ypos="head")
                $ gryffindor += current_payout
                her "Thank you, [name_genie_hermione]..." ("open", "base", "base", "mid") #annoyed #blush

            call her_walk("door")

            if states.her.status.public_stripping: ## Triggers public return event ##
                # Variant where she's used to flashing people.

                if not states.her.ev.potions.breast_expand_drank:

                    nar "As Hermione reaches the door, she stops and her body lurches slightly, the potion now beginning to spread through her body."
                    #Hermione turns around
                    call her_chibi(flip=False)
                    pause .5

                    her "[name_genie_hermione]..." ("angry", "squint", "base", "mid", trans=d3)
                    gen "Yes, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
                    her "Just out of curiosity... What was the potion supposed to do?" ("angry", "squint", "base", "mid")

                    menu:
                        "\"Oh... It was supposed to make your breasts bigger.\"":
                            if states.her.level < 19:
                                her @ cheeks blush "It was supposed to do what?" ("open", "base", "base", "stare") # Slightly shocked
                                gen "What? You didn't oppose to drinking this potion, did you?" ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "No, but I didn't--" ("angry", "squint", "base", "mid")
                                gen "It's not like you're not getting anything out of this, are you?" ("base", xpos="far_left", ypos="head")
                                her "That's true..." ("open", "squint", "base", "R")
                                her "Oh well, whatever, the potion obviously did not work, there's no point arguing about it." ("angry", "closed", "base", "mid")
                                gen "Exactly." ("grin", xpos="far_left", ypos="head")
                                gen "In any case, you better be off, or you'll miss class." ("base", xpos="far_left", ypos="head")

                            else:
                                her @ cheeks blush "It-- I thought you liked my--" ("angry", "narrow", "base", "down")
                                gen "I do, but there's something about a big pair of tits that I find captivating." ("base", xpos="far_left", ypos="head")
                                gen "Besides, wouldn't it be fun to try something different for a change?" ("base", xpos="far_left", ypos="head")
                                her @ cheeks blush "I guess..." ("upset", "narrow", "base", "R")
                                gen "Anyhow, back to class you go [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                                gen "Let me know if there are any developments." ("base", xpos="far_left", ypos="head")

                        "\"It's a secret.\"":
                            her "I see..." ("open", "squint", "base", "R")
                            gen "Yeah, too bad it didn't work." ("base", xpos="far_left", ypos="head")
                            her "*Ah*...{w=0.4} Right..." ("angry", "narrow", "base", "mid")
                            nar "You watch as Hermione shifts around uncomfortably."
                            her "I think I better head off then." ("angry", "narrow", "base", "mid")
                            gen "Certainly." ("base", xpos="far_left", ypos="head")
                            gen "Let me know if there's any... developments." ("base", xpos="far_left", ypos="head")
                            her "*Huh*?." ("angry", "squint", "base", "mid")
                            gen "Nevermind, just get back to class [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                    her "Alright." ("open", "base", "base", "R")
                else:
                    gen "[name_hermione_genie]." ("base", xpos="far_left", ypos="head")

                    #Hermione turns around
                    call her_chibi(flip=False)
                    her "Yes, [name_genie_hermione]?" ("soft", "base", "base", "mid", trans=d3)

                    if states.her.ev.potions.breast_expand_known:
                        gen "Have fun in class." ("grin", xpos="far_left", ypos="head")

                        if states.her.level < 19:
                            her @ cheeks blush "*Ah* You know I'm not doing it for fun--" ("open", "narrow", "base", "R")

                            nar "You watch as Hermione's breasts bounce again."

                            gen "*Heh*, sure. Whatever you say, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                        else: # 19+
                            her @ cheeks blush "*Ah* Maybe I will, [name_genie_hermione], maybe I will." ("soft", "narrow", "base", "R")
                            gen "That's my girl." ("base", xpos="far_left", ypos="head")

                        gen "Let me know how it went." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Yes [name_genie_hermione]." ("open", "closed", "base", "mid")
                        gen "Dismissed!" ("base", xpos="far_left", ypos="head")
                    else:
                        gen "Make sure to note if there's any... Developments, got it?" ("base", xpos="far_left", ypos="head")
                        her "*Ah* Yes, [name_genie_hermione]." ("soft", "squint", "base", "R")

                        nar "You watch as Hermione's breasts bounce again."

                        gen "In details!" ("grin", xpos="far_left", ypos="head")
                        gen "And If so, report to me as soon as you're done with your classes." ("base", xpos="far_left", ypos="head")
                        her "Of course, [name_genie_hermione]." ("open", "closed", "base", "mid")

                #Hermione leaves
                call her_walk(action="leave")

                # Set Return event
                $ breast_potion_ITEM.set_active("hermione")

                # Flags are not set to True here, instead they are set in the return event to not break the writing.

                jump end_hermione_event

            else: ## Doesn't trigger public return event ##

                pause 0.5
                call chibi_emote("thought", "hermione")

                pause 1.0

                nar "You watch Hermione suddenly stop right at the door."

                #Hermione turns around
                call her_chibi(flip=False)
                call ctc

                if not states.her.ev.potions.breast_expand_drank:
                    her "[name_genie_hermione]... This potion..." ("soft", "squint", "base", "mid")
                    gen "Yes?" ("base", xpos="far_left", ypos="head")
                    nar "Suddenly Hermione jumps slightly and a shocked expression spreads across her face."
                else:
                    if states.her.level < 19:
                        her "(Not this again...)" ("angry", "narrow", "base", "down")
                        her "(*Ah*... My breasts are starting to get sensitive.)" ("angry", "happyCl", "base", "mid")
                        her "(I can't go to classes like this, it would ruin my reputation...)" ("angry", "narrow", "base", "down")
                    else:
                        her "(By merlin's beard! It's happening again!)" ("angry", "narrow", "base", "down")
                        her @ cheeks blush "(What am I thinking... I can't go to classes like this, not if I get as horny as last time...)" ("angry", "narrow", "base", "down")
                        her "(Not to mention, it would affect my reputation...)" ("disgust", "closed", "base", "mid")

                her "*Ehm*..." ("angry", "narrow", "base", "mid")
                her "You know, *Ah*...{w=0.4} I don't feel that great, so I think I'll just head to my dorm for today." ("angry", "closed", "base", "mid")
                gen "Are you sure? It's not very like you to miss class, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Ah*...{w=0.4} Yes, I--{w=0.2} I'm sure..." ("open", "closed", "worried", "mid")
                gen "Very well [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "B-- Bye then!" ("angry", "squint", "base", "mid")

                #Hermione leaves
                call her_walk(action="leave")

                gen "(Looks like she isn't willing to risk going to class...)" ("base", xpos="far_left", ypos="head")
                gen "(Perhaps if I asked her to do some other stuff in public she'd be more susceptible to the idea.)" ("base", xpos="far_left", ypos="head")

                $ states.her.ev.potions.breast_expand_drank = True
                # We only need to set the 'drank' flag.

                jump end_hermione_event

        "-Tell her to take out her tits-" if hermione.is_any_worn("top", "bra"):

            gen "Get your tits out!" ("base", xpos="far_left", ypos="head")

        "-Tell her to display her titties-" if not hermione.is_worn("top", "bra"):

            gen "Give me a better look at those tits." ("base", xpos="far_left", ypos="head")

    if not states.her.ev.potions.breast_expand_drank:
        if states.her.level < 19:
            her "I don't think so [name_genie_hermione]... You're only paying me for drinking the potion." ("angry", "narrow", "base", "mid")
            if hermione.is_any_worn("top", "bra"):
                her "If you expected to see me without anything covering them, then you should've said so at the start." ("angry", "closed", "base", "mid")
                gen "Oh, I didn't think that would be necessary, is all." ("base", xpos="far_left", ypos="head")
                her "That's it then? Does it make me show you my breasts? Is it some sort of mind control potion?" ("open", "narrow", "base", "mid")
                gen "Mind control? Where's the fun in that? No, this is something much more entertaining." ("base", xpos="far_left", ypos="head")
                her "If not mind control, then what on earth--" ("open", "closed", "base", "mid")
                nar "You notice Hermione's clothes getting tighter as the potion begins to take effect."
                nar "Hermione unconsciously adjusts them as they get less and less comfortable by the minute."
                her "*Hmm*... Something better happen soon, or I'm out of here." ("angry", "narrow", "base", "R")
                gen "Looks to me as if something's already happened." ("base", xpos="far_left", ypos="head")
                her "Something--{w=0.2} What do you--{w=0.2} What's wrong with me?" ("angry", "squint", "base", "mid")
                gen "There's nothing wrong with you. Although I'd get those breasts out if I were you..." ("base", xpos="far_left", ypos="head")
            else:
                her "If you expected me to give you a better view, then you should've said so at the start." ("angry", "closed", "base", "mid")
                gen "If you say so... You won't really have much choice in a minute or two once that potion kicks in." ("base", xpos="far_left", ypos="head")
                her "What's that's supposed to mean?" ("open", "narrow", "base", "mid")
                gen "You'll just have to wait and find out, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her "Well whatever it is, it better happen soon, otherwise I'm going--" ("open", "closed", "base", "mid")
                nar "You notice Hermione's breasts jiggle slightly as the potion begins taking effect."
                nar "After a brief moment of confusion, Hermione then continues..."
                her "As I said, something better be happening soon, or I'm leaving." ("angry", "narrow", "base", "R")
                gen "I wouldn't worry about it, from the looks of it, something already happened." ("base", xpos="far_left", ypos="head")
                her "It-- Where? What's happened to me?" ("angry", "squint", "base", "mid")
                gen "Well, nothing major yet..." ("base", xpos="far_left", ypos="head")

            her "What do you--" ("angry", "base", "base", "mid")

            nar "Hermione starts checking herself, trying to find what you're referring to..."

            her "I don't see what you could possibly be--" ("open", "squint", "base", "mid")

            nar "Hermione looks down as her breast suddenly bounces on its own accord..."

            her "!!!" ("clench", "narrow", "base", "down")
            her "What's happening to my breasts?!" ("clench", "squint", "base", "mid")
            gen "About time you noticed..." ("base", xpos="far_left", ypos="head")
            her "Hold on... This means you have..." ("angry", "base", "base", "mid")

            show CG hermione as cg zorder 17:
                zoom 0.5
            with fade

            # Strip top/bra
            if hermione.is_any_worn("top", "bra", "accessory"):
                pause 1.5
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("top", "bra", "accessory")

            call ctc

            $ hermione.equip(her_chest_breasts1)
            play sound "sounds/boing02.ogg"
            with d3

            gen "You know what they say, can't have too much of a good thing!" ("grin", xpos="far_left", ypos="head")
            her "It's the other way around [name_genie_hermione]!" ("angry", "squint", "base", "mid")
            gen "It is? I prefer my version." ("base", xpos="far_left", ypos="head")
            her "So that's it then, the potion is meant to make my breasts a bit bigger?" ("angry", "wink", "base", "mid")
            gen "It was meant to make them {i}a lot{/i} bigger..." ("base", xpos="far_left", ypos="head")
            gen "Maybe it takes a while for it to take full effect." ("base", xpos="far_left", ypos="head")
            her "A lot bigger? How big are they supposed to--" ("clench", "squint", "base", "mid")

            $ hermione.equip(her_chest_breasts1)
            play sound "sounds/boing02.ogg"
            with d3

            her "Whoa! They're so full..." ("angry", "base", "base", "down")

        else: # 19+
            her @ cheeks blush "*Hmm*... Is this one of your games again?" ("soft", "narrow", "base", "mid")
            her @ cheeks blush "Am I supposed to pretend that I'm being mind controlled? I should've known the potion was a bit too odd tasting for a real potion..." ("grin", "closed", "base", "mid")
            gen "Yes... Your first order is to proudly display those titties for me!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright then... I hope you've got some extra points--" ("smile", "narrow", "base", "mid")

            if hermione.is_any_worn("top", "bra"):
                nar "You notice Hermione's uniform getting tighter as the potion begins to take effect."
            else:
                nar "You notice Hermione's breasts jiggle slightly as the potion begins to take effect."

            her @ cheeks blush "..." ("soft", "squint", "base", "stare")
            gen "Something wrong?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I-I don't know... I thought I felt something in my chest." ("angry", "squint", "base", "mid")
            gen "Looks like the potion is beginning to take effect." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It is? What's it doing?" ("angry", "base", "worried", "mid")

            nar "Hermione grabs her breasts to check them just as they give off another lurch."

            her @ cheeks blush "Oh my!" ("angry", "wide", "base", "mid")
            her @ cheeks blush "But this means..." ("soft", "wide", "base", "stare")

            show CG hermione as cg zorder 17:
                zoom 0.5
            with fade

            her @ cheeks blush "" ("soft", "wide", "base", "down")

            # Strip top/bra
            if hermione.is_any_worn("top", "bra", "accessory"):
                pause 1.5
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("top", "bra", "accessory")

            call ctc

            $ hermione.equip(her_chest_breasts1)
            play sound "sounds/boing02.ogg"
            with d3

            her @ cheeks blush "..." ("open", "wide", "base", "down")
            her @ cheeks blush "Of course you did..." ("angry", "base", "base", "mid") #blush
            gen "Did what?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "My breasts... Surely you knew that this potion would make them grow..." ("angry", "closed", "base", "mid")
            gen "Looks like your regular size to me [name_hermione_genie]..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... I thought my breasts were already a good enough size..." ("annoyed", "narrow", "base", "mid") #annoyed
            gen "Can't have too much of a good thing." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That's not--" ("open", "narrow", "base", "mid")

            $ hermione.equip(her_chest_breasts2)
            play sound "sounds/boing02.ogg"
            with d3

            her @ cheeks blush "Whoa, they grew even more!" ("open", "wide", "base", "down")
            her @ cheeks blush "And they're so... squishy?" ("soft", "base", "base", "down")

            nar "Hermione fondles her newly expanded breasts..."

            her @ cheeks blush "*Ah*... {w=0.4} And so sensitive too!" ("open", "closed", "worried", "mid")

        gen "*He-heh*..." ("grin", xpos="far_left", ypos="head")
        gen "Now then... Since the effects are already visible..." ("base", xpos="far_left", ypos="head")

    else:

        if states.her.level < 19:
            # She won't ask for points on level 19+
            her "Am I getting paid extra for this?" ("open", "squint", "base", "mid")

            menu:
                "\"No way!\"":
                    gen "Aren't you already getting enough?" ("base", xpos="far_left", ypos="head")
                    gen "Does your greed have no end?" ("base", xpos="far_left", ypos="head")
                    her "A simple \"no\" would've been enough..." ("annoyed", "narrow", "base", "R")
                "\"How about ten extra points?\"":
                    her "*Hmm*. That does sound fair." ("open", "closed", "base", "mid")

                    $ current_payout += 10

        if states.her.level < 21: #Under Sex level

            gen "Step up a bit closer as well..." ("base", xpos="far_left", ypos="head")
            gen "I want to see them in all their glory!" ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "base", "mid")

            hide hermione_main
            with d3
            call her_walk("desk")

            if hermione.is_any_worn("top", "bra", "accessory"):
                gen "Good... And now--" ("base", xpos="far_left", ypos="head")
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("top", "bra", "accessory")
                call ctc
                gen "..." ("grin", xpos="far_left", ypos="head")

            her @ cheeks blush "Alright then... Let's see if the potion is working or not..." ("angry", "narrow", "base", "down", trans=d3)

            gen "I'm sure it will..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("angry", "narrow", "base", "R")
            gen "Feeling anything yet?" ("base", xpos="far_left", ypos="head")
            her "No...{w=0.4} Are you sure you gave me the right potion--" ("angry", "narrow", "base", "down")
            her "**Eekh*!!!" ("clench", "wide", "base", "stare") #shocked

            nar "Hermione jumps as the potion begins to take effect, bouncing her bossom."

            gen "You were saying?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "This... It feels a bit strange..." ("angry", "base", "base", "mid")
            gen "Oh?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes...{w=0.4} There's a slight tingling sensation..." ("angry", "narrow", "base", "down")
            gen "(Some side effect perhaps?)" ("base", xpos="far_left", ypos="head")

            nar "Hermione's breasts expand as the potion spreads through her body."

            $ hermione.equip(her_chest_breasts1)
            play sound "sounds/boing02.ogg"
            with d3

            her @ cheeks blush "*Mmm*..." ("base", "narrow", "base", "stare") #showing some pleasure
            her @ cheeks blush "..." ("disgust", "narrow", "base", "R")
            gen "Looks like I've brewed it just right..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "happyCl", "base", "down") #Happy closed
            gen "Don't you want to look at your new breasts [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "... Oh, thank Merlin..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "I was readying myself for them to get even--" ("angry", "narrow", "worried", "down")

            $ hermione.equip(her_chest_breasts2)
            play sound "sounds/boing02.ogg"
            with d3
            pause .5

            her @ cheeks blush "Bigger..." ("disgust", "narrow", "base", "down")
            gen "You were saying?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "narrow", "base", "mid")
            gen "Now then..." ("base", xpos="far_left", ypos="head")

        else: # 21+

            her @ cheeks blush "Alright..." ("base", "squint", "base", "mid")
            gen "Excellent..." ("base", xpos="far_left", ypos="head")
            gen "Come a bit closer as well, will you?" ("base", xpos="far_left", ypos="head")

            hide hermione_main
            with d3
            call her_walk("desk")

            # Strip top/bra
            if hermione.is_any_worn("top", "bra", "accessory"):
                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("top", "bra", "accessory")
                call ctc

            her @ cheeks blush "There you go, how are they looking?" ("grin", "base", "base", "mid", trans=d3)
            gen "Looks great!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thanks you..." ("base", "narrow", "base", "mid")
            her @ cheeks blush "..." ("base", "narrow", "base", "mid")
            her @ cheeks blush "Nothing's happening..." ("upset", "narrow", "base", "down") #annoyed
            gen "Patience, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "narrow", "worried", "down")
            her @ cheeks blush "This potion is taking way too long--" ("annoyed", "narrow", "annoyed", "mid")

            call kiss_her

            her @ cheeks blush "*Ah*...." ("grin", "narrow", "base", "up") #pleasure

            nar "Hermione shivers as the potion begins to take effect."

            gen "There it is..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Is--{w=0.2} Is it normal for the potion to make them so sensitive?" ("grin", "narrow", "base", "stare")
            gen "Sounds like a side effect, but I'd call that better than advertised." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "*Mmm*...{w=0.4} What...{w=0.4} What's that supposed to mean?" ("smile", "narrow", "base", "stare")
            nar "Hermione's breasts bounce slightly as the potion spreads through her body."

            $ hermione.equip(her_chest_breasts1)
            play sound "sounds/boing02.ogg"
            with d3

            her @ cheeks blush "Whoa!" ("soft", "squint", "base", "stare")
            gen "*He-heh*..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "So heavy..." ("grin", "narrow", "base", "down")
            her @ cheeks blush "Although... Are they not supposed to get bigger?" ("open", "narrow", "base", "down")
            gen "Well..." ("base", xpos="far_left", ypos="head")

            $ hermione.equip(her_chest_breasts2)
            play sound "sounds/boing02.ogg"
            with d3

            her @ cheeks blush "*Ah*..." ("grin", "narrow", "base", "up")
            gen "There they go!" ("grin", xpos="far_left", ypos="head")
            gen "They don't call me the potions master for nothing..." ("grin", xpos="far_left", ypos="head")
            gen "Now then..." ("base", xpos="far_left", ypos="head")

    hide cg
    with fade

    ##Genie asks to touch her breasts##

    if states.her.level < 19:
        gen "Would you like to earn some additional points?" ("base", xpos="far_left", ypos="head")
    else:
        gen "How about we take it one step further?" ("base", xpos="far_left", ypos="head")

    if not states.her.ev.potions.breast_expand_groped:
        her @ cheeks blush "Depends what it is you want..." ("soft", "narrow", "base", "mid")
        gen "To weigh those melons, of course!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Sorry?" ("angry", "narrow", "base", "mid")
        gen "I want you to come here for a moment and let me have a feel." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh..." ("open", "squint", "base", "R")

        if states.her.level < 19:
            her @ cheeks blush "Of course you do." ("angry", "narrow", "base", "R")
            gen "So?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I want twenty extra points..." ("open", "closed", "base", "mid")
            gen "Certainly..." ("base", xpos="far_left", ypos="head")
            gen "Now get over here, so we can find out just how much bigger they got!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("angry", "narrow", "base", "R") #annoyed #glancing away #blush

            $ current_payout += 20

        else: #19+
            her @ cheeks blush "*Hmm*... Alright, I'll do it..." ("base", "narrow", "base", "mid")
            gen "Excellent..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Just...{w=0.4} Don't be too rough, okay?" ("soft", "squint", "base", "mid")
            her @ cheeks blush "They're sensitive..." ("angry", "narrow", "base", "down")

        #Hermione walks to desk (already there on repeat)
        call her_walk("desk")

    else: #Grope repeat
        her @ cheeks blush "You want to touch them again I assume..." ("soft", "narrow", "base", "mid")
        gen "That's right." ("base", xpos="far_left", ypos="head")

        if states.her.level < 19:
            her @ cheeks blush "In that case I want another twenty points like last time..." ("open", "closed", "base", "mid")
            gen "Twenty points again?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes." ("angry", "narrow", "base", "mid")
            gen "*Hmm*... I can give you an additional ten points at best." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "But..." ("mad", "squint", "worried", "mid")
            gen "If I were to give you the same amount of points every time, then why would you ever want to do something new." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "narrow", "base", "R")
            gen "No... Ten extra points should suffice." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Alright, fine... I'll do it..." ("open", "narrow", "base", "mid")

            $ current_payout += 10

        else: #19+
            her @ cheeks blush "I should've guessed..." ("base", "narrow", "base", "R") #smirk
            gen "Can't waste such an opportunity, can we?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "If touching my breasts is what you want then go ahead..." ("open", "closed", "base", "mid")
            her @ cheeks blush "I don't mind..." ("base", "closed", "base", "mid") # smirk

        gen "Great! Get up here [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")

    show screen blkfade

    nar "Hermione walks over to behind your desk, her breasts swaying rhythmically as she moves."
    pause .8

    hide hermione_main

    #Genie groping breast chibi animation nude top
    call her_chibi_scene("grope_tits")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    nar "With the two big globes presented in front of you, you reach out and grab one in each hand and begin massaging them."
    hide screen blkfade

    if not states.her.ev.potions.breast_expand_groped:
        her @ cheeks blush "!!!" ("angry", "narrow", "worried", "down", xpos="mid", ypos="base", trans=d3)
        her @ cheeks blush "Please be gentle [name_genie_hermione]... The potion made them even more sensitive than usual." ("angry", "squint", "base", "mid")
        gen "{i}Even more{/i}?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I mean--" ("clench", "squint", "base", "R")

        nar "Before she can finish, you start kneading her breasts even harder with your fingers."

        her @ cheeks blush "..." ("soft", "closed", "base", "mid")
        gen "They sure feel much more tender than usual." ("base", xpos="far_left", ypos="head")
        gen "On top of the extra cup size that is." ("base", xpos="far_left", ypos="head")

        nar "You continue massaging Hermione's breasts, loosening your grip and sliding your hands around them gently."

        her @ cheeks blush "W-- wait... I'm feeling something--" ("open", "squint", "base", "stare")

        # Note: Dissolve works better for the image, but vpunch is fine with the sound effect

        play sound "sounds/boing04.ogg"
        with vpunch

        $ hermione.equip(her_chest_breasts3)
        with d3


        if states.her.level < 19: #Under blowjob level
            her @ cheeks blush "*Ahhhh*!!!" ("scream", "wide", "base", "down")
            her @ cheeks blush "They've grown even bigger!" ("angry", "base", "base", "down")
            gen "Don't worry about it [name_hermione_genie], think about how you're helping your precious {i}Gryffindeer{/i}." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It's Gryffindor, [name_genie_hermione]!" ("open", "happyCl", "base", "mid")

            her @ cheeks blush "*Ah*..." ("soft", "happyCl", "base", "mid")

            her @ cheeks blush "J-- Just hurry up..." ("annoyed", "happyCl", "base", "mid")

        else:
            her @ cheeks blush "They... They've grown even bigger..." ("soft", "base", "base", "down")
            gen "Yes they have." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "And..." ("angry", "closed", "base", "down")

        her @ cheeks blush "They seem to have become even more sensitive..." ("open", "happyCl", "base", "mid")
        gen "Really?" ("base", xpos="far_left", ypos="head")

        nar "You take both nipples between your thumb and index finger and tug on them."

        her @ cheeks blush "*Ouch!*" ("angry", "wide", "base", "mid")
        gen "Yes... They do appear to be even more sensitive than before..." ("base", xpos="far_left", ypos="head")

    else:
        her @ cheeks blush "*Ah*..." ("open", "closed", "worried", "mid", xpos="mid", ypos="base", trans=d3)
        her @ cheeks blush "*Hnngh*..." ("clench", "closed", "base", "mid") #blushes


        play sound "sounds/boing04.ogg"
        with vpunch

        $ hermione.equip(her_chest_breasts3)
        her @ cheeks blush "Aaaah!!!" ("scream", "wide", "base", "stare")
        with d3

        gen "Now that's more like it!" ("base", xpos="far_left", ypos="head")
        gen "Real weighty these things aren't they?" ("base", xpos="far_left", ypos="head")

        if states.her.level < 19:
            her @ cheeks blush "[name_genie_hermione]... That's not--" ("angry", "squint", "base", "stare")
        else:
            her @ cheeks blush "Oh... Yes..." ("base", "closed", "base", "mid")

        gen "Are they just as sensitive as last time?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ehm*..." ("disgust", "narrow", "base", "R")

        nar "You tug on Hermione's nipples once more, making her yelp in surprise."

        her @ cheeks blush "*Ouch!!*" ("angry", "happyCl", "base", "mid")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "down") #blush
        gen "I suppose that answers that question..." ("base", xpos="far_left", ypos="head")

    if states.her.level < 21: ## Doesn't cum ##
        nar "You take Hermione's breasts back into your hands and continue massaging."

        gen "Now... Stay still, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        nar "You start rolling Hermione's nipples in between your fingers."

        her @ cheeks blush "What... What are you doing?" ("angry", "narrow", "base", "down") #blush
        gen "I'm touching your breasts [name_hermione_genie], wasn't that what we agreed on?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes but--" ("clench", "closed", "worried", "mid") #blush

        nar "You resume running your fingers across her breasts."

        if states.her.level < 19:
            gen "Those points aren't going to earn themselves, are they?" ("base", xpos="far_left", ypos="head")

        nar "You pinch Hermione's nipples, making her yelp in surprise."

        her @ cheeks blush "*Oohh*..." ("angry", "closed", "worried", "mid") #pleasure #still eyes closed
        gen "..." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("disgust", "narrow", "base", "down") #Wide eyed
        her @ cheeks blush "Don't pinch them, [name_genie_hermione]!" ("angry", "narrow", "base", "mid")
        gen "It looked like you enjoyed it though..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I did not!" ("angry", "narrow", "base", "R") #blush
        gen "Very well... I suppose that's it for today..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "But I'm still--{w=0.2} I mean...{w=0.4} Alright..." ("disgust", "squint", "base", "mid")

        show screen blkfade
        with d5

        call her_chibi("stand")
        call gen_chibi("sit_behind_desk")
        her "" ("annoyed", "squint", "base", "R", xpos="right", ypos="base", trans=d3)

        hide screen blkfade
        with d5

        gen "Good work, [name_hermione_genie]... {number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "{size=-4}I'm glad at least one of us got some gratification out of it...{/size}" ("normal", "narrow", "base", "down") # Annoyed that Genie cut it short

        if not states.her.ev.potions.breast_expand_drank:
            her @ cheeks blush "I'll be heading out now." ("open", "closed", "base", "mid")

            #Hermione walks to the door
            call her_walk("door")

            if states.her.level < 19:
                her @ cheeks blush "Wait!" ("angry", "narrow", "base", "stare", xpos="base", ypos="base", flip=True)
                her @ cheeks blush "I can't go out like this!" ("open", "squint", "base", "stare")
                gen "Why? What's the problem?" ("base", xpos="far_left", ypos="head")
            else:
                her @ cheeks blush "Hold on..." ("open", "narrow", "base", "down", xpos="base", ypos="base", flip=True)
                her @ cheeks blush "I almost forgot to put something on." ("base", "narrow", "base", "down")

            hide hermione_main
            with d3
            call her_chibi(flip=False)

        else:
            her @ cheeks blush "I'll head out as soon as the effects wear off." ("open", "closed", "base", "mid")

        if states.her.status.public_stripping:
            gen "It's not like you haven't gone topless in public before, have you?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes but--" ("angry", "narrow", "base", "mid", flip=False, trans=dissolve)

            if states.her.level < 19:

                if not states.her.ev.potions.ass_expand_public_complete:
                    gen "Haven't I given you your points already?" ("base", xpos="far_left", ypos="head")
                    gen "I'm certain you usually leave after that." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "Yes, but not like this..." ("soft", "narrow", "base", "down")
                    gen "I don't see any difference..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "..." ("angry", "narrow", "base", "mid")
                    her @ cheeks blush "Fine, I'm not going to argue with you..." ("open", "closed", "worried", "mid")
                    gen "Good girl." ("base", xpos="far_left", ypos="head")

                    call her_walk(action="leave")

                    gen "Now then... Back to being productive." ("base", xpos="far_left", ypos="head")
                else:
                    gen "As far as I remember we've already done {i}butts{/i}." ("grin", xpos="far_left", ypos="head")
                    her "*tsk*" ("normal", "narrow", "base", "R")
                    her "I'd rather leave than listen to your ass-jokes any longer." ("open", "narrow", "base", "mid")
                    gen "Jokes? I'm not sure why you're making such {i}ass{/i}-umptions all of a sudden--" ("base", xpos="far_left", ypos="head")

                    call her_walk(action="leave")

                    gen "..." ("base", xpos="far_left", ypos="head")
                    gen "She didn't even let me get to the good bit..." ("base", xpos="far_left", ypos="head")
                    gen "Oh well, back to being productive." ("base", xpos="far_left", ypos="head")

                jump .end

            else: # 19+
                gen "No buts." ("base", xpos="far_left", ypos="head")
                gen "Not this time at least." ("grin", xpos="far_left", ypos="head")
                her "*Sigh*... It's as if you are obsessed with all things sexual." ("base", "narrow", "base", "R")
                gen "Only when it's about you, my dear [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "*Hmm*..." ("base", "narrow", "base", "R") # Blushes
                her @ cheeks blush "I'll get going then..." ("open", "base", "base", "mid")
                gen "That you shall." ("base", xpos="far_left", ypos="head")
                gen "Good luck!" ("grin", xpos="far_left", ypos="head")

                call her_walk(action="leave")

                jump .end

        else:
            if not states.her.ev.potions.breast_expand_drank:
                gen "Can't you just avoid public places on your way out to your dormitory?" ("base", xpos="far_left", ypos="head")
                if states.her.level < 19:
                    her @ cheeks blush "The dormitory is a public place!" ("angry", "squint", "base", "mid", flip=False, trans=dissolve)
                    her "Even then, the castle is full of moving pictures, they're like surveillance..." ("angry", "base", "worried", "mid")
                else:
                    her "You want me to go out like this?" ("open", "narrow", "base", "down", flip=False, trans=d3)
                    her "*Hmm*...{w=0.3} No, I think I'd rather stay in here until I can put my top on..." ("base", "narrow", "base", "R")
                gen "Fine. I guess you can wait here until the effects wear off..." ("base", xpos="far_left", ypos="head")
                gen "I don't really mind either way." ("grin", xpos="far_left", ypos="head")
            else:
                gen "Fine by me." ("base", xpos="far_left", ypos="head")

        show screen blkfade
        with d3

        nar "You wait with Hermione until the effects of the potion wears off."
        nar "Shortly after, she decides to leave your office."

        call her_chibi("hide")
        call gen_chibi("sit_behind_desk")
        hide hermione_main

        hide screen blkfade
        with d3

    else: #21+ ##She cums##
        her @ cheeks blush "Please don't do anything sudden like that." ("open", "happyCl", "base", "down")
        gen "What, this?" ("grin", xpos="far_left", ypos="head")

        nar "You take both nipples between your thumb and index finger and tug on them."

        her @ cheeks blush "!!!" ("grin", "narrow", "base", "stare")
        her @ cheeks blush "Please...{w=0.4} It's as if my nipples are on fire!" ("soft", "narrow", "base", "stare")

        nar "You start rolling Hermione's nipples in-between your fingers."
        nar "As you continue, you catch Hermione shifting her legs uncomfortably."

        gen "Feeling a little aroused are we?" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("base", "narrow", "base", "stare")
        gen "Are you paying attention, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes?" ("angry", "squint", "base", "mid")

        nar "You pinch Hermione's nipples, making her yelp in surprise."

        her @ cheeks blush "*Oohh*..." ("grin", "narrow", "base", "stare")
        gen "(I wonder how far I could take this...)" ("base", xpos="far_left", ypos="head")

        nar "You resume running your fingers across her bountiful bosom."

        her @ cheeks blush "..." ("base", "narrow", "base", "stare")

        nar "As you continue rubbing her, you notice that Hermione's eyes are glazed over, numbingly staring into space."

        gen "Well, well, well... You sure are sensitive, aren't you?" ("base", xpos="far_left", ypos="head")
        #unfocused pupils from this point

        nar "You start alternating, pinching and pulling her nipples out as far as you can, then letting them go before grabbing them again."

        her @ cheeks blush "*Ah*..." ("open", "closed", "base", "mid")

        nar "Hermione lets out an involuntary moan, as the feeling of her increasingly sensitive nipples overwhelm her."

        her @ cheeks blush "*Mmm*..." ("base", "narrow", "base", "stare")
        gen "You little slut!" ("grin", xpos="far_left", ypos="head")

        nar "You resume pulling on her nipples, Hermione closes her eyes and starts breathing heavily..."

        her @ cheeks blush "*Ah*...{w=0.3} *Ah*...{w=0.3} *Ah*..." ("open", "closed", "worried", "mid")

        nar "Suddenly you feel Hermione begin to tense up, and you grab her breasts and squeeze her nipples hard between your fingers."

        her @ cheeks blush "*Ngh*--" ("angry", "happyCl", "base", "mid")

        play sound "sounds/slick_01.ogg"
        with kissiris

        her @ cheeks blush "*Ahhhh*!!!" ("grin", "narrow", "base", "stare")
        gen "Such a naughty girl..." ("base", xpos="far_left", ypos="head")

        show screen blkfade
        with d3
        nar "Hermione slumps to the floor, breathing heavily as she slowly regains her ability to stand."

        her @ cheeks blush "" ("base", "narrow", "base", "stare", xpos="right", ypos="base", trans=d3)
        call her_chibi("stand")
        call gen_chibi("sit_behind_desk")

        hide screen blkfade
        with d3

        #Hermione stands in front of desk

        gen "Fantastic work, [name_hermione_genie]... {number=current_payout} points to Gryffindor!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Thank you..." ("base", "narrow", "base", "mid") # Still dazed

        pause.2

        gen "Off you go." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Mhm*..." ("base", "narrow", "base", "down") # Affirmative murmur, still dazed

        #Hermione leaves
        call her_walk(action="leave")

        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Is it just me or did she forget to put her clothes back on...?" ("base", xpos="far_left", ypos="head")
        gen "*Heh*! That potion must've had a much stronger effect on her than I thought." ("grin", xpos="far_left", ypos="head")

    label .end:

    $ states.her.ev.potions.breast_expand_groped = True
    $ states.her.ev.potions.breast_expand_drank = True
    $ states.her.ev.potions.breast_expand_known = True
    $ hermione.unequip("chest")

    jump end_hermione_event

##Send Hermione to class breast expand Return event##
label her_potion_breasts_return:

    stop music fadeout 1
    #Hermione enters the office, and walks to the front the of desk
    call her_walk("desk", "base", action="enter")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    if states.her.public_level < 19:
        if not states.her.ev.potions.breast_expand_public_low_complete:

            $ states.her.ev.potions.breast_expand_public_low_complete = True

            ### TODO: add CG once it's finished

            her @ cheeks blush "I can't believe you made me do that!" ("angry", "base", "base", "mid")
            gen "Do what?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Making me attend a class looking like that!" ("annoyed", "squint", "base", "mid")
            her @ cheeks blush "On the day we have potion lessons on the schedule no less." ("disgust", "squint", "base", "mid")
            gen "So I take it you caught some of the students' attention?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Some? I would be surprised if all of them weren't staring at me at some point..." ("clench", "narrow", "base", "R")
            her @ cheeks blush "And that includes Professor Snape!" ("disgust", "closed", "base", "mid")
            gen "(I'd be more surprised if they didn't stare...)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "And if the stares weren't enough, my breasts just kept growing..." ("angry", "narrow", "base", "down")
            gen "They did? Now that's unfortunate!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "That was the worst class of my life, I've never felt more humiliated!" ("angry", "happyCl", "base", "mid")
            her @ cheeks blush "The Slytherin students kept pointing and laughing at me as I was trying to prepare my concoctions..." ("open", "squint", "base", "mid")
            her @ cheeks blush "Asking me if \"I had dipped my fat udders in a swelling solution\"..." ("disgust", "narrow", "annoyed", "R")
            her @ cheeks blush "*Ugh!* The nerve of these guys!" ("disgust", "narrow", "annoyed", "mid")
            gen "Surely the ridicule of some Slytherin students isn't enough for you to lose your focus, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            gen "I thought a top student such as yourself would be able to keep your composure." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "The Slytherin students' snide remarks is not what bothers me, [name_genie_hermione]." ("angry", "narrow", "base", "R")
            her @ cheeks blush "But it's hard to focus on the precision needed for potion brewing when everyone in the room is staring at you." ("angry", "closed", "base", "mid")
            her @ cheeks blush "I could barely see the cutting board as I was preparing my ingredients..." ("angry", "narrow", "base", "down")
            gen "(Even then, I bet she was the most focused of all of them...)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Have you ever tried picking up Ashwinder's Egg with two beach balls attached to your chest?" ("open", "narrow", "annoyed", "mid")
            gen "Can't say that I have." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "--Once I had finally managed to finish my potion, I accidentally knocked it off and smashed it onto the floor..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "If it wasn't for the fact that Professor Snape chose to have me stay and clean it up after class, I'm sure I would've lost a lot of points then..." ("disgust", "narrow", "base", "R")
            gen "That doesn't sound too bad." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "He made me scrub the entire floor!" ("open", "squint", "annoyed", "mid") #screen shake
            gen "Can't a little spell take care of that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Without using magic!" ("scream", "closed", "annoyed", "mid") #screen shake
            gen "Ah... I see..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I could feel him gawking at my breasts as I was down there on my knees..." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "I should've known... The only times he doesn't dock points from me is when there's something he could get out of it." ("disgust", "narrow", "annoyed", "mid")
            gen "{size=-3}As if you wouldn't just come here and earn them back afterwards...{/size}" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "What did you say?" ("angry", "base", "base", "mid")
            gen "Nothing..." ("base", xpos="far_left", ypos="head")
            gen "Very well then, [name_hermione_genie]. You've done what I asked of you..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("annoyed", "narrow", "base", "R")
            gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "...{w=0.4} Thank you, [name_genie_hermione]." ("annoyed", "closed", "base", "mid")
            her @ cheeks blush "That will be all then, yes?" ("normal", "closed", "base", "mid")
            gen "Yes, that shall do for now... Unless..." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "base", "mid")
            gen "On second thought, I'll let you rest...{w=0.4} Off you go!" ("base", xpos="far_left", ypos="head")
            her "Thank you, [name_genie_hermione]..." ("open", "closed", "base", "mid")
        else: #Repeat
            gen "[name_hermione_genie]... Had a fun day in class?" ("base", xpos="far_left", ypos="head")
            her "How did you manage to convince me to do this again..." ("angry", "narrow", "base", "mid", trans=d3)
            gen "Convince you to do what?" ("base", xpos="far_left", ypos="head")
            her "Go to class like that!" ("annoyed", "narrow", "worried", "mid")
            gen "There was convincing involved?" ("base", xpos="far_left", ypos="head")
            her "*Hmph*..." ("annoyed", "narrow", "base", "R")
            gen "So... It didn't go that well, I take it?" ("base", xpos="far_left", ypos="head")
            her "No..." ("open", "narrow", "worried", "mid")

            show her_potion_public_expand_breasts_c1 as cg zorder 17:
                zoom 0.26
                pos (0, 0)
                anchor (0.05, 0)

                parallel:
                    subpixel True
                    transform_anchor True
                    linear 180.0 zoom 0.6 offset (0, 135) anchor (0.0, 0.4)
            with fade

            her "Even though I was ready for it and I knew what to expect, it didn't go much better than last time..." ("open", "squint", "worried", "R")
            her "Any optimism I had after leaving your office went out the window once I remembered we had potions class today." ("disgust", "narrow", "base", "down")
            her "When making my way there, I was hoping that the effects wouldn't be as prevalent as last time..." ("open", "squint", "worried", "mid")
            her "But I didn't even get all the way down the grand staircase before my breasts started growing rapidly." ("angry", "squint", "worried", "mid")
            her "I must've had at least a dozen portraits stare at me walking through the corridors on the way there." ("disgust", "narrow", "worried", "R")
            gen "Portraits aren't real, you know."
            her "I know that... But having all these famous witches and wizards stare at you..." ("angry", "squint", "worried", "mid")
            her @ cheeks blush "Well... It's embarrassing... Many of them are role models of mine." ("angry", "narrow", "base", "R")
            gen "But... They're paintings..."
            her @ cheeks blush "I don't understand how those other girls do it." ("annoyed", "narrow", "base", "down")
            gen "Other girls?"
            her @ cheeks blush "Oh... I meant the ones with... *Ehm*..." ("angry", "squint", "worried", "mid")
            gen "Giant tits?"
            her @ cheeks blush "[name_genie_hermione]!" ("angry", "happyCl", "base", "mid")
            gen "..."
            her @ cheeks blush "Yes... That." ("angry", "narrow", "base", "down")
            her "Surely they must be getting stared at constantly." ("clench", "closed", "base", "mid")
            gen "You've had your breasts out in public before, I don't get why you're making such a big deal out of it."
            her @ cheeks blush "That's different!" ("angry", "squint", "worried", "mid")
            gen "How is it different?"
            her @ cheeks blush "Flashing my breast to one person and sitting through a whole lesson with your breasts as big as melons are two completely different things!" ("angry", "narrow", "annoyed", "R")
            her @ cheeks blush "When I'm in class, I'm forced to just let the other students stare at me the entire time until the effect goes away." ("angry", "narrow", "annoyed", "down")
            gen "Other students and Snape."
            her @ cheeks blush "Don't even let me get started on Professor Snape." ("angry", "squint", "annoyed", "mid")
            gen "{size=-4}Oh boy, what have I done...{/size}"
            her @ cheeks blush "Brewing was the least of my worries..." ("angry", "narrow", "annoyed", "mid")
            her @ cheeks blush "Even more of the students took notice of my condition this time around." ("open", "narrow", "annoyed", "R")
            her @ cheeks blush "I pretty much gave up trying to grind up my shrivel figs after realising how it was making my breasts jiggle." ("open", "narrow", "annoyed", "down")
            gen "Giving up during a lecture? That doesn't sound very much like you, [name_hermione_genie]..."
            her @ cheeks blush "One of the Slytherin boys watching me was masturbating for crying out loud!" ("scream", "closed", "annoyed", "mid")
            gen "Really?"
            her @ cheeks blush "Yes!" ("angry", "base", "annoyed", "mid")
            gen "(A man of my own heart...)"
            gen "I mean, Who could blame him..."
            gen "You'd be surprised what people do when they think nobody is looking."
            her @ cheeks blush "Oh, He knew I saw him doing it!" ("mad", "narrow", "annoyed", "mid")
            her @ cheeks blush "But of course everyone else's eyes were on me, so he got away with it..." ("open", "closed", "annoyed", "mid")
            her @ cheeks blush "I couldn't believe it... He was barely every trying to conceal it." ("angry", "narrow", "annoyed", "mid")
            gen "Are you sure he wasn't just scratching--"
            her @ cheeks blush "No [name_genie_hermione]... It was out!" ("open", "base", "annoyed", "mid")
            her @ cheeks blush "If I was stood any closer to him, I'm sure he could've hit me with it." ("open", "narrow", "annoyed", "R")
            gen "(Amateur...)"
            gen "Wait, when you say \"it\"..."
            her @ cheeks blush "You know exactly what I mean..." ("disgust", "narrow", "annoyed", "R")
            her @ cheeks blush "If seeing him do that wasn't bad enough, I was also forced to clean it off the floor afterwards." ("disgust", "narrow", "annoyed", "down")
            gen "Very admirable of you [name_hermione_genie]... Boys will be boys, after all, you know how messy they can be."
            her @ cheeks blush "I didn't volunteer! Snape-- I mean... Professor Snape made me do it." ("angry", "squint", "base", "mid")
            gen "I'm sure he didn't know... He probably just thought someone spilled their potion again."
            her "I'm sure..." ("annoyed", "narrow", "annoyed", "R")
            her "A more plausible theory would be that he has always been looking for any excuse to torment me..." ("open", "narrow", "annoyed", "R")
            her "According to him, I had been purposely disrupting the class." ("open", "closed", "annoyed", "mid")
            gen "*Hmm*... That's a pretty vague reason... He should work on that."
            her "As if it's not bad enough that he's favouring students of his own house." ("angry", "narrow", "annoyed", "R")
            her "Maybe that's it... He probably saw the boy doing it, and revelled in the thought of making me stay and--" ("disgust", "squint", "annoyed", "R")
            gen "[name_hermione_genie]..."
            gen "I think I've heard enough..."

            hide cg
            with fade

            her @ cheeks blush "..." ("angry", "narrow", "worried", "R")
            her @ cheeks blush "So, am I free to go, [name_genie_hermione]?" ("angry", "narrow", "base", "mid")
            gen "Yes, you may leave for today..." ("base", xpos="far_left", ypos="head")
            gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "... Thanks." ("open", "narrow", "worried", "R")
    else: # 19+
        if not states.her.ev.potions.breast_expand_public_high_complete:

            $ states.her.ev.potions.breast_expand_public_high_complete = True

            her @ cheeks blush "Hello [name_genie_hermione]..." ("open", "base", "base", "mid")
            gen "*Mmm*... What?" ("base", xpos="far_left", ypos="head")
            gen "Oh it's you, [name_hermione_genie]... Forgive me, I was just... meditating." ("base", xpos="far_left", ypos="head")
            gen "So... Got anything to tell me?" ("base", xpos="far_left", ypos="head")
            gen "I hope your lessons went well." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "It went as well as can be expected given that I've got these things to try and work around..." ("open", "narrow", "base", "R") #blush, looking away
            gen "Details [name_hermione_genie]... I want to hear everything about your day." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("base", "narrow", "base", "down")
            her @ cheeks blush "Well, I left your office--" ("open", "narrow", "base", "down")

            show her_potion_public_expand_breasts_d1 as cg zorder 17:
                zoom 0.26
                pos (0, 0)
                anchor (0.05, 0)

                parallel:
                    subpixel True
                    transform_anchor True
                    linear 180.0 zoom 0.6 offset (500, 135) anchor (0.35, 0.4)
            with fade

            her @ cheeks blush "And I was making my way to my next class when I suddenly bumped into another student." ("open", "squint", "base", "R")
            gen "Poor guy probably didn't even know what hit him."
            her @ cheeks blush "I didn't mean it in a literal sense. {size=-4}Unfortunately...{/size}" ("base", "narrow", "base", "down")
            her @ cheeks blush "Although he wasn't exactly looking where he was going and ended up walking right into one of the suits of armour..." ("open", "squint", "base", "mid")
            her @ cheeks blush "Which did boost my confidence quite handsomely..." ("grin", "narrow", "base", "mid") #smile #glance away
            gen "I'm glad that our little experiment could give you such a boost in self-esteem."

            if states.her.public_level < 22:
                her @ cheeks blush "Me too..." ("base", "squint", "base", "mid")
                her "Not that I had much time to enjoy it." ("open", "narrow", "base", "R")
            else:
                her @ cheeks blush "Me too! When I walked past him, I noticed he had grown a boner! Although I didn't get a chance to help him out..." ("base", "squint", "base", "mid")

            gen "How so? What happened?"
            her "Well..." ("disgust", "narrow", "base", "R")
            her "I suddenly noticed Professor Snape watching us and as I did, he made sure I followed him to class." ("angry", "narrow", "base", "mid")
            her @ cheeks blush "He must've seen the whole thing because he really made the lesson even more difficult for me than usual." ("open", "narrow", "annoyed", "R")
            gen "Severus? I'm sure that whatever he did, he meant well... He is here to help you learn after all."
            her @ cheeks blush "Some help he is... He went out of his way to degrade me in front of the entire class!" ("soft", "narrow", "annoyed", "mid")
            gen "Surely you must be exaggerating, [name_hermione_genie]."
            gen "Professor Snape is an esteemed {i}Witcher{/i}--"
            gen "--Or a Lich, he does seem kind of pale..."
            her @ cheeks blush "I'll admit, it wasn't bad at first..." ("open", "closed", "annoyed", "mid")
            her @ cheeks blush "Chopping ingredients proved a bit difficult, my breasts kept pushing them off of the board, spilling onto the floor in front of me..." ("open", "base", "base", "mid")
            her @ cheeks blush "But that was manageable until Professor Snape noticed it and loudly told me off and to pick them up..." ("angry", "narrow", "annoyed", "mid")
            her @ cheeks blush "So it didn't take very long for all the students to notice what was going on..." ("open", "narrow", "base", "R")
            her @ cheeks blush "At first, it was just those Slytherin delinquents..." ("angry", "narrow", "base", "mid")
            her @ cheeks blush "And I can deal with them no problem, as you already know--" ("open", "closed", "base", "mid")
            her @ cheeks blush "But then boys from Gryffindor and other houses joined in and began making remarks about my chest too." ("annoyed", "narrow", "base", "down")
            gen "What about the girls? Did any of them notice?"
            her @ cheeks blush "Of course they did! One particular girl from Ravenclaw was saying that I'd done this to try and catch the eye of Professor Snape..." ("open", "narrow", "annoyed", "mid")
            her @ cheeks blush "As if!" ("open", "narrow", "annoyed", "mid") # annoyed, looking away
            gen "I'm sure they were merely jealous of your newfound assets."
            her @ cheeks blush "You know what, you may be right." ("grin", "narrow", "annoyed", "mid")
            her @ cheeks blush "Her friend kept staring at me the entire time, but whenever our eyes met she averted her gaze." ("base", "narrow", "annoyed", "mid")
            gen "Sounds like she was checking you out."
            her @ cheeks blush "She was--" ("angry", "base", "base", "mid")
            gen "What happened next?"
            her @ cheeks blush "*Ahem*... Well, the lesson was almost over... But that's when {i}it{/i} happened..." ("angry", "narrow", "base", "mid")
            gen "{i}It{/i}? [name_hermione_genie]?"
            her @ cheeks blush "Yes... I was doing my best to follow the potion recipe, but I must have got something wrong." ("angry", "narrow", "base", "down")
            her @ cheeks blush "Maybe I was distracted... Or maybe I dropped something important..." ("angry", "narrow", "base", "down")
            gen "Maybe you just were horny!"
            her @ cheeks blush "Or maybe... I just couldn't see all the instructions because your concoction gave me those massive things..." ("annoyed", "narrow", "base", "mid")
            gen "Well... Whatever the case..."

            show her_potions_public_expand_breasts_a1 as cg:
                pos (0, 0)
                anchor (0, 0)
                offset (-600, -200)
                zoom 0.65

                parallel:
                    ease_quad 10.0 zoom 0.25 offset (0, 0)
            with fade

            with hpunch
            her @ cheeks blush "The mixture exploded and knocked me right off my feet and onto the floor." ("open", "closed", "worried", "mid")
            her @ cheeks blush "It was supposed to be a simple antidote! They're not supposed to explode!" ("angry", "base", "base", "mid")
            gen "Yeah, tell me about it..."
            her @ cheeks blush "I was completely covered in the remains of my potion, face blackened by soot, and there was a knot of goosegrass in my hair." ("disgust", "squint", "base", "mid")
            her @ cheeks blush "And the explosion had also destroyed the only thing keeping my dignity intact--" ("angry", "narrow", "base", "down")
            gen "Was it your twisted sense of justice?"
            her @ cheeks blush "No, [name_genie_hermione], it was my vest! Which caused my breasts to flop out, giving the entire class a full view..." ("angry", "narrow", "base", "mid")
            her @ cheeks blush "I must have looked ridiculous!" ("open", "closed", "annoyed", "mid")
            gen "Don't be too hard on yourself, I am partially to blame for your breasts being seen in public, I admit--"
            her @ cheeks blush "I'm talking about the soot on my face, [name_genie_hermione]." ("open", "narrow", "annoyed", "mid")
            gen "Oh..."

            show her_potions_public_expand_breasts_a2 as cg

            her @ cheeks blush "Luckily one of the boys there was nice enough to use his handkerchief to clean up my face." ("open", "squint", "base", "mid")
            her @ cheeks blush "Of course he insisted I had gotten some on my breasts and that he had to help me clean that off as well..." ("base", "narrow", "base", "R")
            gen "*He-Heh*... Clever boy."
            her @ cheeks blush "Then a fellow Gryffindor took a pity on me, and let me borrow her vest so that I had something to cover up with." ("open", "squint", "base", "mid")
            her @ cheeks blush "I promised to give it back to her once I'd had time to shower and get changed, but she said I can keep it if I tell her where I got the swelling solution from." ("grin", "closed", "base", "mid")
            gen "Well, did you?"
            her @ cheeks blush "I said that the brewer would like to remain anonymous, as to not expose our arrangement." ("open", "squint", "base", "R")
            gen "I see... I suppose that's for the best."
            her @ cheeks blush "Professor Snape, of course, took this as a chance to lecture the others on the dangers of swelling solutions." ("angry", "narrow", "base", "R")
            her @ cheeks blush "Saying that I had obviously been more concerned with getting everyone's attention than following his directions!" ("disgust", "base", "base", "mid")
            her @ cheeks blush "Even going so far as implying that I had deliberately caused the accident so that I could show off my chest!" ("angry", "narrow", "annoyed", "mid")
            her @ cheeks blush "The very idea makes me fume with anger!" ("clench", "closed", "annoyed", "mid")
            gen "Well, you did just tell me at the beginning that you enjoyed having that boy pay more attention to you than where he was going."

            hide cg
            with fade

            her @ cheeks blush "That's... That's different!!" ("angry", "squint", "worried", "mid")
            gen "How is it different?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That was one boy... Not an entire classroom." ("open", "squint", "worried", "mid")
            gen "What about that Ravenclaw girl, the one that has been staring at you the entire time?" ("base", xpos="far_left", ypos="head")
            gen "You're saying you didn't enjoy that?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "W-- Well maybe, but I'm not--" ("angry", "base", "worried", "down")
            gen "Just admit it, [name_hermione_genie], you enjoyed being seen in public, you just didn't like the circumstances in which it has happened." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("angry", "narrow", "base", "R")
            her @ cheeks blush "You are not wrong. Still, what Professor Snape did was unnecessary..." ("annoyed", "closed", "base", "mid")
            gen "I suppose I shall have to talk to Snape about this. I can't have him degrading my star pupil in front of all her classmates." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "You will?" ("angry", "base", "base", "mid")
            gen "Don't worry, I will explain to him that the mistake was my own doing. It won't happen again, I assure you." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "*Ehm*... There's no need to go that far [name_genie_hermione]." ("open", "squint", "base", "mid")
            her @ cheeks blush "I'm fine, really!" ("angry", "squint", "worried", "mid")
            gen "No, no... This one's on me [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "I never should have asked you to take that concoction and head to class." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I assure you it is--" ("mad", "base", "worried", "mid")
            gen "Professor Snape is the potions master after all, if he thinks these types of potions are dangerous--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Professor Dumbledore!" ("scream", "happyCl", "base", "mid") #closed #yelling #blush
            her @ cheeks blush "I-I mean, [name_genie_hermione]..." ("angry", "narrow", "base", "down") # apologetic
            gen "Oh alright, if you don't want me to interfere, then I guess I won't." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you." ("open", "squint", "base", "R") # smile :)
            gen "I guess we're done here." ("base", xpos="far_left", ypos="head")
            gen "Well done [name_hermione_genie], {number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "May I please be excused?" ("angry", "closed", "base", "mid")
            gen "Somewhere you need to be?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes... I need to... *Ehm*..." ("disgust", "squint", "base", "R")
            gen "I see... Some time alone in your bed is what you need, I think." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "That's--" ("angry", "base", "base", "mid")
            gen "We both know I'm right, there's no point hiding it." ("base", xpos="far_left", ypos="head")
            gen "Talk to you later, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Good night then [name_genie_hermione]..." ("angry", "narrow", "base", "R") # blushing
        else: #Repeat
            her "Hello [name_genie_hermione]..." ("open", "squint", "base", "R")
            gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "How's your day been?" ("base", xpos="far_left", ypos="head")
            her "Pretty good, thanks." ("open", "closed", "base", "mid")
            her "Can't complain, you know." ("base", "narrow", "base", "down")
            gen "Good to hear, anything unusual happen?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Well, I caught the eye of more students than usual... Thanks to the potion you gave me." ("open", "squint", "base", "R")
            gen "I'm glad you're getting good use out of it." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes... {size=-4}Shame that it's not permanent...{/size}" ("base", "closed", "base", "mid")
            her @ cheeks blush "Being gawked over by the boys, or being stared at jealously by the girls is quite the confidence boost." ("open", "squint", "base", "mid")
            her @ cheeks blush "Although I think it's worth considering putting some sort of countermeasures up to prevent people from walking into things as much." ("base", "narrow", "base", "R")
            her @ cheeks blush "If a big pair of breasts is enough to have students knock over suits of armours or smash into walls, it's only a matter of time until someone seriously hurts themselves." ("soft", "squint", "base", "R")
            gen "That's easier said than done [name_hermione_genie]... I'm not sure if you noticed, but this castle is made from stone." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course I have, I'm just saying..." ("annoyed", "narrow", "base", "mid")
            her @ cheeks blush "At least if we put some cushioning charms down it wouldn't be as bad." ("open", "closed", "base", "mid")
            gen "Or perhaps if you didn't entrance people with those big titties then they would pay attention to where they were going." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Perhaps..." ("base", "narrow", "base", "R")
            gen "Anyway... Enough about outdated safety standards." ("base", xpos="far_left", ypos="head")
            gen "What lessons did you have today?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... We had double potions today, [name_genie_hermione]." ("open", "squint", "base", "mid")
            gen "Good... I mean, alright." ("base", xpos="far_left", ypos="head")
            gen "So how did that go?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmm*... Fine I suppose..." ("open", "narrow", "base", "down") #annoyed
            gen "Is that so? You don't sound very convincing." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmph*... I thought I was getting better at handling these things." ("angry", "closed", "base", "mid")
            her @ cheeks blush "The vest helps a ton, I'm sure if I wasn't wearing it, it'd be a difficult task not to burst any of the buttons." ("open", "closed", "base", "mid")
            gen "(Note to self... Remove vest from school uniform...)" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I only had a couple of vital steps left before finishing it up when one of the Slytherin students knocked the contents of my cauldron over me." ("soft", "narrow", "base", "down")
            gen "Oh, dear... Are you alright?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm fine... The only thing that was hurt was my pride..." ("open", "narrow", "base", "R")

            show her_potions_public_expand_breasts_b1 as cg zorder 17:
                pos (0, 0)
                anchor (0, 0)
                offset (-600, -600)
                zoom 0.65

                parallel:
                    ease_quad 10.0 zoom 0.25 offset (0, 0)
            with fade

            her @ cheeks blush "I must admit... That Slytherin boy was more clever than I'd give any of them credit for." ("annoyed", "narrow", "worried", "R")
            her @ cheeks blush "I got completely covered in that horribly sticky mess..." ("disgust", "closed", "worried", "mid")
            if not states.her.status.cumshot:
                gen "I'm sure you'll get used to it..."
            else:
                gen "You'd think you'd be used to that sort of thing."
            her @ cheeks blush "Sorry?" ("soft", "narrow", "base", "down")
            gen "Nothing... Please continue..."
            her @ cheeks blush "In any case... That unfinished potion nearly destroyed my clothing." ("disgust", "closed", "worried", "mid")
            her @ cheeks blush "So yet again I ended up giving the whole class a good view of those bloody things." ("soft", "narrow", "base", "down")
            gen "I'm sure they didn't mind."
            her @ cheeks blush "I'm sure..." ("soft", "narrow", "base", "R")

            show her_potions_public_expand_breasts_b2 as cg

            her @ cheeks blush "The Slytherins, even though they were howling with laughter, were all staring me down as I sat there getting rid of that sticky potion..." ("disgust", "narrow", "base", "mid")
            her @ cheeks blush "Even the Gryffindors didn't even pretend to avert their gaze." ("annoyed", "wink", "base", "mid")
            gen "Well, you're an attractive girl, It'd be an insult if they did."
            her @ cheeks blush "And Professor Snape, yet again, made sure to bring me up in front of the class to give some long-winded lecture on how important it is to let the stabilizing agent take effect before transferring your potion." ("angry", "narrow", "base", "mid")
            her @ cheeks blush "Trying to embarrass me, no doubt..." ("annoyed", "narrow", "base", "R")
            gen "Safety first."
            her @ cheeks blush "..." ("annoyed", "narrow", "base", "mid")

            hide cg
            with fade

            gen "Sounds to me like you've earned yourself some points today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh... Yes, the points..." ("grin", "narrow", "base", "down")
            gen "{number=current_payout} points to Gryffindor!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you [name_genie_hermione]..." ("grin", "closed", "base", "mid")
            gen "Before you leave... Just out of curiosity..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Yes [name_genie_hermione]?" ("open", "squint", "base", "mid")
            gen "What happened to that top of yours?" ("base", xpos="far_left", ypos="head")
            her "Oh... Well, apparently potion damage is quite common, so I was able to procure a new set." ("open", "squint", "base", "mid")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            her "Yes, I was told this was the fourth time this week!" ("open", "squint", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "(Better not mention that in my report...)" ("base", xpos="far_left", ypos="head")
            gen "Very well [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "That will do for today." ("base", xpos="far_left", ypos="head")
            her "Alright, good night then [name_genie_hermione]." ("base", "base", "base", "mid")
            gen "Good night [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    $ states.her.ev.potions.breast_expand_drank = True
    $ states.her.ev.potions.breast_expand_known = True

    jump end_hermione_event
