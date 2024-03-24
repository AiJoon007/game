
label potion_cat_make:

    call give_reward("You have successfully created a new potion!", cat_potion_ITEM)

    play sound "sounds/sniff.ogg"
    gen "Yep..." ("base", xpos="far_left", ypos="head")
    gen "Smells like a wet pussy, all right..." ("base", xpos="far_left", ypos="head")
    gen "Not the kind I'd like to drink from, though." ("base", xpos="far_left", ypos="head")
    return

label her_potion_cat_give:

    if hermione.is_worn("robe"):
        gen "Before we begin... Why don't you take those robes off and make yourself comfortable." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("soft", "squint", "base", "mid")
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        with d3
        gen "Now then..." ("base", xpos="far_left", ypos="head")

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid")

    if not states.her.ev.potions.polyjuice_drank:
        $ states.her.ev.potions.polyjuice_drank = True

        gen "I've got a potion here that I'd like you to try..." ("base", xpos="far_left", ypos="head")
        nar "You bring out the thick potion and hand it to Hermione."
        call her_chibi("hold_potion","mid","base")
        with d3

        if states.her.level < 16:
            her "A potion? What kind of potion is it? It looks gross..." ("disgust", "happy", "base", "mid")
            gen "Wouldn't it spoil half of the enjoyment if I told you?" ("base", xpos="far_left", ypos="head")
            her "Depends on whose enjoyment you're talking about..." ("angry", "narrow", "base", "mid")
            gen "Twenty points." ("base", xpos="far_left", ypos="head")
            her "*Hmm*...{w=0.4} Can't you tell me what kind of potion it is?" ("annoyed", "wink", "base", "mid")
            her "Polyjuice? Babbling Beverage? Shrinking solution?" ("open", "squint", "base", "mid")
            gen "That's going to have to stay a secret, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "base", "down")
            gen "Well [name_hermione_genie], what do you say? Will you drink a harmless little potion?" ("base", xpos="far_left", ypos="head")
            gen "For Gryffindor?" ("base", xpos="far_left", ypos="head")
            her "Fine..." ("open", "narrow", "base", "down")

        else:
            her "You want me to drink this? It doesn't look that appealing..." ("angry", "narrow", "base", "down")
            gen "I'm sure it'll be worth it." ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "squint", "base", "mid")
            her "Alright then..." ("base", "base", "base", "mid")

        call her_chibi("sniff_potion","mid","base")
        pause 0.2
        play sound "sounds/sniff.ogg"
        pause 0.6
        call her_chibi("hold_potion","mid","base")
        nar "Hermione takes a quick sniff of the potion."

        her "It smells disgusting. Like mud and wet dog fur." ("angry", "happyCl", "base", "mid")
        gen "I suggest blocking your nose if the smell is too much." ("base", xpos="far_left", ypos="head")
        her "Alright..." ("disgust", "happy", "base", "mid")
        her "For Gryffindor!" ("open", "happyCl", "worried", "mid")

    else:
        gen "Ready to try another potion?" ("base", xpos="far_left", ypos="head")
        nar "You bring out the thick potion and swirl it in front of Hermione."
        her "Is this another Polyjuice potion?" ("open", "squint", "base", "mid")
        gen "...{w=0.5}no?" ("base", xpos="far_left", ypos="head")
        her "You're lying..." ("open", "closed", "base", "mid")

        if states.her.level < 16:
            her "Do I have to?" ("angry", "narrow", "base", "mid")
            gen "You don't have to do anything [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "But if you do decide to, it would make me very happy...." ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "squint", "base", "mid")
            gen "And there are some points in it for you as well..." ("base", xpos="far_left", ypos="head")

        else:
            her "But I'll drink it if you really want me to." ("base", "base", "base", "mid")
            gen "Great, here you go!" ("base", xpos="far_left", ypos="head")

        nar "Hermione grabs the potion and brings it up to her mouth."
        her "Here we go then..." ("angry", "squint", "base", "mid")


    call her_chibi("drink_potion","mid","base")
    pause 0.6
    play sound "sounds/gulp.ogg"
    pause 0.8
    call her_chibi("stand","mid","base")
    nar "Hermione downs the thick potion."


    her "*Bleugh*." ("open_tongue", "happyCl", "base", "mid")
    gen "Well done." ("base", xpos="far_left", ypos="head")

    if not states.her.ev.potions.polyjuice_cat_drank:
        her "I did it..." ("angry", "happy", "base", "mid")
        her "Now will you at least tell me what this potion does?" ("disgust", "base", "base", "mid")

        if states.her.ev.potions.breast_expand_drank:
            her "Is it supposed to make my breasts bigger? They don't feel any bigger." ("open", "base", "base", "mid")
            gen "That's not it... Maybe you should just head back to class in that case... I could've sworn I did it right..." ("base", xpos="far_left", ypos="head")

        else:
            gen "It should be noticeable any second now..." ("base", xpos="far_left", ypos="head")
            gen "Aaaany second..." ("base", xpos="far_left", ypos="head")
            gen "Unless..." ("base", xpos="far_left", ypos="head")
            her "Unless?" ("angry", "base", "base", "mid")
            gen "Well, maybe one of the ingredients..." ("base", xpos="far_left", ypos="head")
            gen "Never mind..." ("base", xpos="far_left", ypos="head")
            her "What was it supposed to do?" ("angry", "happy", "base", "mid")
            gen "There's no point in telling you now. It was going to be a surprise." ("base", xpos="far_left", ypos="head")
            gen "You may head back to class, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

        her "Oh, okay then." ("soft", "happy", "base", "mid")

        gen "Twenty points to Gryffindor." ("base", xpos="far_left", ypos="head")
        $ gryffindor += 20
        her "Thank you [name_genie_hermione]." ("base", "base", "base", "mid")
    else:
        her "Here we go again I suppose..." ("angry", "narrow", "base", "down")
        her "Nothing's happening..." ("disgust", "narrow", "base", "down")
        gen "You'll just have to wait for a bit, remember?" ("base", xpos="far_left", ypos="head")
        gen "So you best head back to class for now." ("base", xpos="far_left", ypos="head")

        if states.her.public_level < 15: #Before she'd enjoy having her look like a cat in class
            her @ cheeks blush "Great... Can't wait for the effects to kick in... It was bad enough the first time..." ("angry", "narrow", "base", "mid")
            gen "I'm sure ten extra points should make it worth it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

            gen "Thirty points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 30
            her "... Thank you [name_genie_hermione]." ("open", "squint", "base", "mid")

        else: #When she'd enjoy showing herself off as a cat in class
            her @ cheeks blush "Okay then..." ("open", "narrow", "base", "down")
            her @ cheeks blush "I wonder what they'll think when they see me like this again..." ("base", "narrow", "base", "R")
            gen "I'm sure they'll enjoy it." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm sure..." ("open", "narrow", "base", "R")
            gen "Oh, before I forget." ("base", xpos="far_left", ypos="head")

            gen "Twenty points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 20
            her "Thank you [name_genie_hermione]." ("open", "squint", "base", "mid")

    call her_walk(action="leave")
    $ cat_potion_ITEM.set_active("hermione")
    jump end_hermione_event

label her_potion_cat_return:
    #Scene where Hermione comes back after class, angry and confused at being given cat ears and a tail.

    stop music fadeout 1
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_cat1, remove_old=False)
    $ hermione.strip("robe")

    call her_walk(action="enter", xpos="mid", ypos="base")

    if not states.her.ev.potions.polyjuice_cat_drank:
        $ states.her.ev.potions.polyjuice_cat_drank = True

        her "" ("annoyed", "squint", "annoyed", "mid")
        call ctc

        gen "Nice ears..." ("base", xpos="far_left", ypos="head")
        her "How could you do this to me [name_genie_hermione]?" ("open", "squint", "annoyed", "mid")

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

        her "I can't believe you'd try and turn me into a cat in the middle of class!" ("upset", "squint", "annoyed", "mid")
        gen "I didn't try to turn you into a cat, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "Then why do I have ears and a tail?" ("disgust", "base", "annoyed", "mid")

        menu:
            "\"I thought you'd look cute as a pussy.\"":

                her "Really?" ("disgust", "happy", "worried", "mid")
                gen "Yep... And I must say..." ("grin", xpos="far_left", ypos="head")
                her "..." ("normal", "base", "worried", "mid") #Hopeful
                gen "I've really shown how immense my brewing knowledge is today." ("grin", xpos="far_left", ypos="head")
                her "..." ("annoyed", "narrow", "base", "mid") #Annoyed
                gen "That {i}Polio-juice{/i} turned out exactly how I imagined it." ("grin", xpos="far_left", ypos="head") # intentional

            "\"-Lie-\"":
                gen "I have no idea... The potion I gave you was supposed to turn you into a different girl." ("base", xpos="far_left", ypos="head")
                her "Really?" ("angry", "base", "base", "mid")
                gen "*Err*... Yes?" ("base", xpos="far_left", ypos="head")
                her "*Hmm*... Figured you must've made a mistake." ("open", "closed", "base", "mid")

        her "Polyjuice potions are not meant to be used like this..." ("open", "closed", "annoyed", "mid")
        her "At least I know that it will wear off by morning." ("open", "squint", "base", "R")
        gen "Shame that, indeed..." ("base", xpos="far_left", ypos="head")
        her "May I go now?" ("open", "base", "base", "mid")

    else:
        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

        her @ cheeks blush "I can't believe you had me drink another one of these potions..." ("disgust", "squint", "base", "down", trans=d3)
        gen "What's the problem? I think you look cute..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I'm a Cat! Polyjuice isn't supposed to be used this way!" ("angry", "base", "base", "mid")

        if states.her.public_level < 15: #Before she'd enjoy to have her look like a cat in class
            her @ cheeks blush "People kept making fun of me and pulling my tail in class!" ("angry", "narrow", "base", "mid")
            gen "And how did that make you feel?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Humiliated!" ("angry", "happyCl", "base", "mid")
            her @ cheeks blush "They kept asking if I had been a good kitty and if I wanted scratches..." ("disgust", "squint", "base", "mid")
            her @ cheeks blush "And you know the worst thing?" ("angry", "base", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "The darn potion made me want the scratches..." ("angry", "narrow", "worried", "R")
            gen "I see...{w=0.5} then we at least learnt something new here today." ("base", xpos="far_left", ypos="head")
        else: #High
            her @ cheeks blush "My classmates sure seemed to enjoy it though..." ("angry", "narrow", "base", "down")
            her @ cheeks blush "One of the boys was entranced by the motion of my tail..." ("open", "closed", "base", "mid")
            her @ cheeks blush "It seemed to have its own mind..." ("angry", "closed", "base", "mid")
            gen "And how did that make you feel?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I'm not sure..." ("normal", "squint", "base", "mid")

        her @ cheeks blush "Are we done here?" ("open", "squint", "base", "R")

    label .choices:

    menu:
        "-Let her go-":
            gen "Very well, [name_hermione_genie]. You've done what I've asked of you, so be a good kitty and go to bed." ("base", xpos="far_left", ypos="head")
            her "..." ("annoyed", "narrow", "base", "mid")
            gen "Unless there was anything else?" ("base", xpos="far_left", ypos="head")
            her "No..." ("open", "closed", "base", "mid")
            her "Goodnight then, [name_genie_hermione]..." ("open", "base", "base", "mid")

            call her_walk(action="leave")
            $ hermione.equip(her_outfit_last)
            jump end_hermione_event

        "-Have her drink another one-" if cat_potion_ITEM.owned < 1:
            gen "(I don't have any more of that potion.)" ("base", xpos="far_left", ypos="head")
            jump .choices

        "-Have her drink another one-" if cat_potion_ITEM.owned > 1:

            gen "Not yet." ("base", xpos="far_left", ypos="head")
            gen "I do believe we could do better than this." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione]?" ("angry", "base", "base", "mid")
            nar "You bring out another polyjuice potion and swirl it in front of Hermione."
            if not states.her.ev.potions.polyjuice_cat_furry: #Not turned her into more of a cat
                $ states.her.ev.potions.polyjuice_cat_furry = True
                $ cat_potion_ITEM.owned -= 1

                her "You're joking, right?" ("disgust", "narrow", "base", "mid")
                gen "Surely you must be curious what another one would do?" ("base", xpos="far_left", ypos="head")
                her "But what if it turns me completely into a cat?" ("clench", "squint", "base", "mid")
                gen "I suppose I might have to hide the bird..." ("base", xpos="far_left", ypos="head")
                her "That's not what I'm worried about..." ("disgust", "narrow", "base", "mid")
                gen "Come on now, what's another harmless little potion going to do?" ("base", xpos="far_left", ypos="head")
                her "*Hmm*..." ("annoyed", "narrow", "base", "down")
                gen "I'll give you thirty more points..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "..." ("angry", "narrow", "base", "down")
                her "Are you really sure it's safe?" ("open", "squint", "base", "mid")
                gen "Of course! You're not doubting my brewing abilities, are you?" ("base", xpos="far_left", ypos="head")
                her "I... I suppose not..." ("angry", "narrow", "base", "down")
                her "Alright then..." ("angry", "base", "base", "mid")

                nar "Hermione grabs the potion and brings and readies herself to drink it."
                call her_chibi("hold_potion","mid","base")

                her "Here I go..." ("open", "happyCl", "base", "down")

                call her_chibi("drink_potion","mid","base")
                pause 0.6
                play sound "sounds/gulp.ogg"
                pause 0.8
                call her_chibi("stand","mid","base")

                her "Yuck..." ("open_tongue", "happyCl", "base", "mid")

                gen "Good kitty..." ("base", xpos="far_left", ypos="head")
                her "..." ("disgust", "base", "base", "mid")
                her "What now? It took some time for the first one to--" ("open", "base", "base", "mid")

                play sound "sounds/magic4.ogg"
                show screen gfx_effect(584, 340, img="smoke", zoom=0.85)
                $ hermione.equip(her_outfit_cat2, remove_old=False)

                her "Work..." ("normal", "base", "base", "mid")
                her "" ("normal", "base", "base", "down")
                call ctc
                her "Oh my god!" ("angry", "wide", "base", "down")
                gen "*Pfff*--" ("base", xpos="far_left", ypos="head")
                gen "*Ha-ha-Hah*!" ("grin", xpos="far_left", ypos="head")
                her "My--{w=0.2} I've got paws!" ("angry", "base", "annoyed", "down")
                gen "I know! *Ha-Ha-Ha*!" ("grin", xpos="far_left", ypos="head")
                if hermione.is_worn("bottom"):
                    her "And my legs are so... Itchy!" ("clench", "narrow", "base", "down")

                    play sound "sounds/cloth_sound3.ogg"
                    $ hermione.strip("bottom")
                call ctc
                pause .5
                her "My legs!" ("angry", "wide", "base", "down")
                gen "{size=+2}*HA-HA-HA*!!{/size}" ("grin", xpos="far_left", ypos="head")
                her "[name_genie_hermione]! Would you stop laughing?" ("disgust", "squint", "annoyed", "mid")
                menu:
                    "-Tease her-":
                        gen "*Ha-hah*! Or what? Going to scratch me?" ("grin", xpos="far_left", ypos="head")
                    "-Calm yourself-":
                        gen "*Ah-ha-ha*...{w=0.4} Ah...{w=0.4} That was funny..." ("grin", xpos="far_left", ypos="head")
                        her "Are you done?" ("disgust", "narrow", "annoyed", "mid")
                        gen "I--{w=0.2} *Heh*...{w=0.4} Yes, I think so..." ("grin", xpos="far_left", ypos="head")
                        her "Why did I drink another one... How am I supposed to face the other--" ("clench", "narrow", "worried", "down")
                        gen "*Hah-Hah* Your face! You should've seen the look on your--" ("grin", xpos="far_left", ypos="head")

                play sound "sounds/hiss_girl.ogg"
                her "..." ("mad", "base", "angry", "mid") #Hissing
                her @ cheeks blush "..." ("disgust", "wide", "base", "down") #Wide eyed
                gen "{size=+5}*Pwah-Ha-Ha-Hah*!{/size}" ("grin", xpos="far_left", ypos="head")
                her @ cheeks blush "I can't believe you!" ("scream", "base", "annoyed", "mid")

                call her_walk(action="leave")

                $ states.her.mood += 15
                #Hermione never gets the extra points
                $ hermione.equip(her_outfit_last)

                gen "Even if she stays mad forever, it was worth it." ("grin", xpos="far_left", ypos="head")

                jump end_hermione_event
            else:
                her "Are you serious? You know what happened last time!" ("clench", "base", "base", "mid")
                gen "More the reason to do it again!" ("grin", xpos="far_left", ypos="head")

                if states.her.level < 22: #Fail
                    her "No, I am not humiliating myself like this again..." ("disgust", "narrow", "base", "mid")

                    gen "(I guess she isn't ready for another dose yet, maybe I should train her more first...)" ("base", xpos="far_left", ypos="head")

                    gen "Fine..." ("base", xpos="far_left", ypos="head")
                    gen "In that case..." ("base", xpos="far_left", ypos="head")

                    jump .choices

                else: #Success
                    $ cat_potion_ITEM.owned -= 1

                    her @ cheeks blush "Fine... I'll do it..." ("disgust", "narrow", "base", "down") #blushing
                    gen "You will?" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "Yes..." ("open", "closed", "base", "mid")
                    her @ cheeks blush "Just hand me the potion..." ("open", "narrow", "base", "mid")

                    nar "Hermione grabs the potion and brings and readies herself to drink it."
                    call her_chibi("hold_potion","mid","base")

                    call her_chibi("drink_potion","mid","base")
                    pause 0.6
                    play sound "sounds/gulp.ogg"
                    pause 0.8
                    call her_chibi("stand","mid","base")

                    her "*Ah*..." ("open_tongue", "happyCl", "base", "mid")

                    gen "You did it!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "Did you not want me to?" ("annoyed", "squint", "base", "mid")
                    gen "Yes, although I was sure you'd refuse to do it again..." ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "*Hmph*... Well, I just thought--" ("open", "narrow", "base", "R")
                    gen "Did you enjoy those paws last time perhaps?" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "What do you--" ("clench", "base", "base", "mid")

                    play sound "sounds/magic4.ogg"
                    show screen gfx_effect(584, 340, img="smoke", zoom=0.85)
                    $ hermione.equip(her_outfit_cat3, remove_old=False)

                    her @ cheeks blush "" ("clench", "narrow", "base", "down")
                    gen "*Hah-ha-Hah*!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "There, I've drunk it..." ("angry", "base", "base", "mid")
                    her "[name_genie_hermione]!"
                    gen "*Ha-Ha-Ha*!" ("grin", xpos="far_left", ypos="head")
                    gen "Your face!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "My... What's wrong with my--" ("angry", "narrow", "base", "down")
                    her @ cheeks blush "I've got whiskers!" ("scream", "wide", "base", "mid")
                    gen "And a cute little nose too!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "Breathe Hermione..." ("angry", "closed", "base", "mid")
                    her @ cheeks blush "It's just polyjuice, it's only temporary..." ("normal", "closed", "base", "mid")
                    gen "Now, do the thing again!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "What thing?" ("angry", "squint", "worried", "mid")
                    gen "The hissing thing, it was hilarious!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I-- I can't!" ("clench", "happyCl", "base", "mid")
                    her @ cheeks blush "I didn't do it on purpose!" ("angry", "narrow", "annoyed", "mid")
                    gen "Come on now! Just try it!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I... Fine!" ("disgust", "narrow", "base", "mid")
                    nar "Hermione readies herself to hiss."
                    her @ cheeks blush "*Ahem*..." ("angry", "squint", "base", "mid")

                    play sound "sounds/hiss_girl_fail.ogg"
                    her @ cheeks blush "*Snort*...{w=0.4}{nw}" ("shock", "squint", "base", "mid")
                    her @ cheeks blush "*Snort*...{fast}" ("disgust", "squint", "base", "mid")

                    gen "*Pwha-ha-ha*!!!" ("grin", xpos="far_left", ypos="head")
                    gen "That was so bad!" ("grin", xpos="far_left", ypos="head")
                    gen "Come on, do it for real this time!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I was trying to!" ("angry", "happyCl", "annoyed", "mid")
                    gen "*Ha-Hah-Ha*!" ("grin", xpos="far_left", ypos="head")
                    gen "You sounded like an angry badger!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "It's not funny!" ("clench", "squint", "worried", "mid")
                    gen "*Ha-ha-ha*!" ("grin", xpos="far_left", ypos="head")
                    her @ cheeks blush "I can't believe you!" ("angry", "happyCl", "base", "mid")

                    call her_walk("door", "base")
                    gen "Watch the--" ("base", xpos="far_left", ypos="head")
                    call her_chibi("leave")

                    play sound "sounds/kick.ogg"

                    pause .5
                    play sound "sounds/cat_scream.ogg"
                    pause .8
                    gen "Tail..." ("base", xpos="far_left", ypos="head")
                    $ states.her.mood += 15
                    $ hermione.equip(her_outfit_last)
                    jump end_hermione_event

        "-Ask her for a blowjob-":
            pass

    gen "I suppose..." ("base", xpos="far_left", ypos="head")
    gen "Although I thought perhaps you'd like to do something to earn yourself some additional points first." ("base", xpos="far_left", ypos="head")
    her "By doing what?" ("open", "happy", "base", "mid")
    gen "By putting that mouth around my cock." ("base", xpos="far_left", ypos="head")

    if not states.her.ev.potions.polyjuice_cat_blowjob:

        if not states.her.status.blowjob: #Fail
            her "You want me to--" ("angry", "base", "base", "mid")
            her @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "annoyed", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")

            if states.her.level < 19:
                her @ cheeks blush "I can't believe you'd ask such a thing!" ("angry", "base", "angry", "mid")
                gen "Surely we can't waste this opportunity!" ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Yes we can!" ("angry", "narrow", "angry", "mid")
                $ states.her.mood += 15
            else:
                her "I am not doing that when looking like this!" ("angry", "base", "annoyed", "mid")
                gen "But it'd be such a wasted opportunity!" ("base", xpos="far_left", ypos="head")
                her "..." ("annoyed", "narrow", "annoyed", "mid")

            gen "(Perhaps if she had already given me a blowjob in her normal form, she'd be more willing to agree.)" ("base", xpos="far_left", ypos="head")
            gen "Fine..." ("base", xpos="far_left", ypos="head")
            gen "You may leave." ("base", xpos="far_left", ypos="head")

            call her_walk(action="leave")
            $ hermione.equip(her_outfit_last)

            jump end_hermione_event

        else: #Success
            her "Right now? I look like a cat! Why would you ask me at a time like this?" ("angry", "squint", "base", "mid")
            her "You're not some sort of pervert who likes animals, are you?" ("disgust", "narrow", "base", "mid")
            gen "Of course not, I just think that you have a very unique look at the moment and that it would be a shame not to do anything with it." ("base", xpos="far_left", ypos="head")
            gen "I'll give you Twenty extra points..." ("base", xpos="far_left", ypos="head")
            her "Fine... Just promise me you aren't going to do anything weird." ("disgust", "narrow", "base", "down")
            gen "Blowjobs are already kind of weird if you think about it." ("base", xpos="far_left", ypos="head")
            her "You know what I meant..." ("disgust", "narrow", "base", "mid")
            if hermione.is_any_worn("top", "bra", "bottom", "panties", "stockings"):
                gen "Now, take your clothes off for me..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "Alright..." ("open", "wink", "base", "mid")

    else: #Sucked him off as a cat before

        her "Again?" ("angry", "happy", "base", "mid")
        her "I thought you found my tongue was too rough in this state?" ("open", "happy", "base", "mid")
        gen "Well, the purring certainly made well up for that aspect." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Okay then..." ("open", "base", "base", "mid")
        if hermione.is_any_worn("top", "bra", "bottom", "panties", "stockings"):
            her @ cheeks blush "Let me just take this off..." ("base", "narrow", "base", "down")

    if hermione.is_any_worn("top", "bra", "bottom", "panties", "stockings"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("top", "bottom", "bra", "panties", "stockings")

    pause .8
    her @ cheeks blush "" ("base", "narrow", "base", "mid")
    call ctc
    gen "Purrfect... Now get that tail over here." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, [name_genie_hermione]." ("open", "squint", "base", "mid")

    #Chibi walks over and fade to black

    stop music fadeout 2.0
    call her_walk("desk", "base", reduce=0.8)
    pause .2

    call hide_characters
    show screen blkfade
    with d3

    call her_chibi_scene("bj_pause", trans=d9)
    pause.8

    gen "Good girl." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("base", "narrow", "base", "L", ypos="head", flip=False)
    nar "Hermione, now kneeling in front of you, takes you into her mouth."

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    call her_chibi_scene("bj", trans=d9)
    call ctc

    hide screen blkfade
    with d3

    if not states.her.ev.potions.polyjuice_cat_blowjob:
        her "*Slurp*! *Gulp*! *Gltch*!" ("open_wide_tongue", "closed", "base", "mid")
        gen "Good god what is with your tongue?!" ("angry", xpos="far_left", ypos="head")

        call her_chibi_scene("bj_pause", trans=d3)

        her @ cheeks blush "*Ah*..." ("open", "squint", "base", "mid")
        her "What do you mean, [name_genie_hermione]?" ("angry", "squint", "base", "mid")
        gen "It felt like Velcro!" ("angry", xpos="far_left", ypos="head")
        her "You're the one who asked me to do this... A cat's tongue is a lot rougher than a human." ("mad", "narrow", "base", "mid")
        her "Do you want me to stop?" ("open", "wink", "base", "mid")
        gen "No, keep going, just try not to move that tongue too much." ("base", xpos="far_left", ypos="head")
        her "Okay." ("angry", "narrow", "base", "R")

        call her_chibi_scene("bj", trans=d3)

        nar "Hermione swallows your cock again, taking care not to apply too much pressure with her tongue."
    else:
        her "*Slurp*! *Gulp*! *Gltch*!" ("open_wide_tongue", "closed", "worried", "mid")
        gen "There's that tongue again...{w} could you try using your throat a bit more?" ("angry", xpos="far_left", ypos="head")
        her "*Slurp*..." ("open_wide_tongue", "narrow", "base", "R") #Annoyed

    her "*Slurp*...{w=0.4} *Slurp*...{w=0.4} *Slurp*..." ("open_wide_tongue", "closed", "worried", "mid")
    gen "That's it... Nice kitty..." ("grin", xpos="far_left", ypos="head")
    her "*Slurp*...{w=0.4} *Gltch*...{w=0.4} *Gulp*..." ("open_wide_tongue", "closed", "base", "mid")
    gen "So, you still went to all your classes?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Mhm*..." ("open_wide_tongue", "closed", "base", "mid")
    her @ cheeks blush "*Slurp*...{w=0.4} *Slurp*...{w=0.4} *Slurp*..." ("open_wide_tongue", "closed", "worried", "mid")

    if not states.her.ev.potions.polyjuice_cat_blowjob:
        gen "Even looking like this?" ("base", xpos="far_left", ypos="head")
        gen "*Hmm*... You'd think they question why you'd turn up looking like a cat..." ("base", xpos="far_left", ypos="head")
        gen "Did they just assume you were under an evil Slytherin spell?" ("base", xpos="far_left", ypos="head")
        if states.her.public_level > 15:
            gen "Or would they just think that slutty little Miss Granger is begging for attention?" ("base", xpos="far_left", ypos="head")
        nar "You go to place your hand on the back of her head, but her new ears block the way."
        gen "These are quite soft." ("base", xpos="far_left", ypos="head")
        nar "You start feeling and patting the ears."
        nar "Hermione's eyes widen as she starts purring involuntarily."
        her @ cheeks blush "" ("open_wide_tongue", "base", "base", "up_soft")
        gen "Oh, good heavens!" ("base", xpos="far_left", ypos="head")
        gen "It's like your whole mouth has become a vibrator." ("base", xpos="far_left", ypos="head")

        call her_chibi_scene("bj_pause", trans=d3)

        her @ cheeks blush "I can't help it [name_genie_hermione], whenever anything touches my ears I just purr." ("angry", "squint", "base", "mid")
        gen "It feels amazing! Now cock back in the mouth, girl." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Yes [name_genie_hermione]." ("angry", "narrow", "base", "mid")

        call her_chibi_scene("bj", trans=d3)

        nar "You immediately put your hand back on her ears and start stroking them as she sucks you."
    else:
        call her_chibi_scene("bj_pause", trans=d3)

        her @ cheeks blush "*Ah*....{w=0.4} Well, You had me do it before..." ("open", "narrow", "base", "R")
        her @ cheeks blush "At least I knew what to expect this time." ("angry", "narrow", "base", "mid")
        gen "Such a good student you are..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Thank--" ("soft", "base", "base", "mid")
        gen "Now resume sucking." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("open", "narrow", "base", "down")

        call her_chibi_scene("bj", trans=d3)

        gen "Slutty little Miss Granger... I bet you loved the attention..." ("base", xpos="far_left", ypos="head")
        nar "You place your hand on her ears once again and give them a soft patting."
        nar "Hermione starts purring as her eyes widen and look into yours."
        gen "There it is!" ("base", xpos="far_left", ypos="head")
        gen "Keep going girl, this feels amazing..." ("base", xpos="far_left", ypos="head")
        nar "Closing your eyes, you momentarily stop patting her and Hermione's purring stops."
        gen "Don't stop!" ("base", xpos="far_left", ypos="head")

        call her_chibi_scene("bj_pause", trans=d3)

        her @ cheeks blush "You stopped patting me!" ("angry", "squint", "base", "mid")
        gen "Oh, Right..." ("base", xpos="far_left", ypos="head")
        nar "You gently stroke the back of Hermione's ears as she begins purring once more."

        call her_chibi_scene("bj", trans=d3)

    her "*Slurp!* *Purr* *Slurp!*" ("open_wide_tongue", "narrow", "base", "up_soft")
    gen "Oh god yes. This is Fantastic." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Purr* *Slurp!* *Purr*" ("open_wide_tongue", "narrow", "base", "up_soft")
    gen "Get ready girl... Here it comes." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Purr* *Purr* *Purr*" ("open_wide_tongue", "narrow", "base", "mid_soft")
    nar "Hermione pushes forward and the tip of your cock rests on her purring throat."
    gen "{size=+10}*ARGH*!!!!!!!!!!!!!!!!{/size}" ("angry", xpos="far_left", ypos="head")
    her "*Purr* *Purr* *Purr*" ("open_wide_tongue", "narrow", "base", "up_soft")

    nar "The vibrations prove too much, and you shoot your load directly down her throat."

    call cum_block
    call her_chibi_scene("bj_cum_in", trans=d5)
    pause.8

    call cum_block
    call bld
    gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
    her "*Purr!-Gulp!-Gulp*!" ("open_wide_tongue_cum", "narrow", "base", "up_soft")
    with hpunch
    gen "Take my milk!" ("angry", xpos="far_left", ypos="head")
    her "*Gulp*! *Gulp*! *Gulp*!" ("open_wide_tongue_cum", "happy", "base", "up_soft")
    call bld("hide")
    call ctc

    call her_chibi_scene("bj_pause", trans=d5)
    pause.8

    nar "Hermione pulls your cock out of her purring mouth."
    gen "*Ah*... That was amazing..." ("base", xpos="far_left", ypos="head")

    her "...{w=0.6}{nw}" ("full_cum", "happy", "base", "mid_soft")
    play sound "sounds/gulp.ogg"
    her @ cheeks blush "... *Gulp*{fast}{w=0.6}{nw}" ("cum", "happy", "base", "mid")
    her @ cheeks blush "*Gulp*{fast} *Ah*..." ("open", "narrow", "base", "mid")

    her @ cheeks blush "*Mmm*... That tasted so much better than the potion..." ("base", "closed", "base", "mid")

    show screen blkfade
    with d3

    $ hermione.set_cum(None)
    $ hermione.wear("all")

    call her_chibi("stand","desk","base", flip=False)
    call gen_chibi("sit_behind_desk")

    nar "Hermione walks back to the front of your desk, her tail swaying playfully."

    hide screen blkfade
    with d5

    gen "Well, you've certainly earned your points." ("base", xpos="far_left", ypos="head")
    gen "Forty points to Gryffindor." ("base", xpos="far_left", ypos="head")
    $ gryffindor += 40
    her "Thank you [name_genie_hermione]... Will that be all?" ("base", "happy", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    gen "Yes, that will do for today..." ("base", xpos="far_left", ypos="head")
    her "Okay, Goodnight then..." ("soft", "base", "base", "mid")
    call her_walk("door", "base")

    gen "Actually... One last thing..." ("base", xpos="far_left", ypos="head")

    call her_chibi("stand", "door", "base", flip=False)
    her "Yes [name_genie_hermione]?" ("open", "base", "base", "mid", xpos="base", ypos="base")
    gen "Who's a good kitty?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush ".........." ("angry", "happy", "base", "mid")
    her @ cheeks blush "I am..." ("base", "narrow", "base", "down")

    call her_walk(action="leave")
    $ hermione.equip(her_outfit_last)
    $ states.her.ev.potions.polyjuice_cat_blowjob = True

    jump end_hermione_event
