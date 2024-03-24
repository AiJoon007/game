
label cc_pf_strip_T2_E3_hermione:

    # Equip Hermione default clothing.
    $ her_outfit_last.save() # Store current outfit.
    $ hermione.equip(her_outfit_default)    #Equip Hermione default clothing.

    # Summon Hermione.
    play sound "sounds/door.ogg"
    call her_chibi("stand", "door", "base")
    with d3
    pause .5

    her "You wanted to see me, Sir?" ("soft", "closed", "base", "mid", xpos="base", ypos="base", flip=False, trans=d3)

    her "...{w=0.4}{nw}" ("soft", "base", "worried", "L")
    her "...{fast}Cho?!" ("clench", "wide", "worried", "shocked")

    play music "music/deadly-roulette-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    cho "Hey there, Granger!" ("horny", "narrow", "angry", "mid") # Grinning
    her "What? Why are you--" ("disgust", "wide", "worried", "shocked")

    call her_walk(660, "base")

    cho "" ("smile", "narrow", "angry", "L", xpos="mid", ypos="base", flip=True)
    her "What the bloody hell is going on here?!" ("scream", "closed", "base", "mid", xpos="right", ypos="base", trans=hpunch) # Scream
    her "" ("angry", "base", "angry", "mid")

    cho "You know, just the usual..." ("soft", "base", "base", "L")
    cho "Like stripping for our dear headmaster!" ("smile", "narrow", "angry", "L")
    cho "I trust that you're more than familiar with it..." ("soft", "closed", "base", "L")
    her "You've told her?" ("clench", "base", "angry", "mid")
    cho "So you really {b}did{/b} do it!" ("open", "wide", "base", "L")
    her "It's none of your business what I do at this school! You slut!" ("angry", "narrow", "angry", "R")
    cho "Are you sure about that?{w=0.6} I believe there are some people that would think otherwise..." ("grin", "narrow", "base", "mid")
    cho "Your friends...{w} the other students...{w} our teachers..." ("soft", "narrow", "angry", "L")
    cho "Maybe even the ministry?" ("smile", "narrow", "angry", "L")
    her "You wouldn't dare!!!" ("upset", "happy", "base", "mid")
    cho "Indeed, I wouldn't." ("soft", "closed", "base", "mid")
    cho "And neither would you!" ("smile", "narrow", "angry", "L")
    cho "Which is why we brought you here..." ("open", "base", "base", "mid")
    cho "To have some fun!" ("base", "narrow", "angry", "mid")

    her "Sir, I demand that you stop this nonsense!" ("open", "base", "angry", "mid")
    cho "I don't think that's very likely to happen, Granger..." ("soft", "narrow", "angry", "mid")
    cho "We both know what he would prefer..." ("soft", "closed", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "And who he prefers..." ("smile", "narrow", "angry", "mid")
    her "You think that he prefers you over me?{w} Please..." ("soft", "narrow", "angry", "R")
    cho "Why don't we just ask him?" ("base", "narrow", "base", "mid")
    cho "Tell us, sir..." ("soft", "narrow", "base", "R")
    cho "How do you like the athletic, immaculate, nude body of your favourite student?" ("smile", "narrow", "angry", "mid")
    cho "It's so much better than Miss Granger's, isn't it?" ("base", "narrow", "angry", "mid")
    call ctc

    $ d_flag_01 = False # Cho not on desk

    call cc_pf_strip_T2_E3_hermione_choices

    return

label cc_pf_strip_T2_E3_hermione_choices:

    menu:
        "\"Definitely!\"":
            $ states.her.mood += 10
            her "What?!" ("open", "wide", "base", "stare")
            cho "See, I told you!{w=0.6} How could he pick a walking bush on legs over this!" ("smile", "narrow", "angry", "L")
            her "" ("angry", "base", "angry", "mid")
            cho "Now tell her. Tell her why my body is superior compared to hers." ("soft", "closed", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Well, you're more flexible for one..." ("base", xpos="far_left", ypos="head")
            cho "That's right, I am!" ("soft", "wide", "base", "mid")
            her "*Humph*..." ("annoyed", "narrow", "angry", "R")
            cho "And? What else?" ("smile", "narrow", "base", "L")
            gen "And Cho's thighs are probably the most impressive ones I've seen in the last hund-- decade or more!" ("angry", xpos="far_left", ypos="head")
            her "Well, in that case..." ("soft", "closed", "base", "mid")
            her "In that case, I'll give you a great opportunity to stare at them indefinitely." ("angry", "base", "angry", "mid")
            cho "What are you talking about, Granger?" ("soft", "narrow", "raised", "L")

            # Hermione walks towards the desk to pick up Cho's clothing.
            call her_walk("desk", "base", speed=1.5)
            pause .2
            if not d_flag_01: # Cho not on desk
                call cho_chibi("stand",570,"base", flip=False) # Facing the desk.
                with d3
            pause .6

            cho "What are you doing?" ("soft", "narrow", "base", "L", ypos="head", flip=False)

            # Hermione picks them up and runs off.
            call bld("hide")
            pause .2
            play sound "sounds/cloth_sound.ogg"
            hide screen cho_cloth_pile
            pause .5

            cho "My clothes!" ("open", "wide", "base", "L")

            play sound "sounds/run_03.ogg"
            call her_walk("door", "base", speed=2)
            call her_chibi(flip=False)
            with d3
            pause .1
            call cho_chibi(flip=True)
            with d3

            her "Hey seeker, looks like someone will have to seek their way to their dorm without any clothes tonight." ("open", "base", "angry", "mid", ypos="head", flip=False)
            cho "Hey!" ("clench", "narrow", "angry", "L", ypos="head", flip=True)

            # Hermione leaves out of the door.
            hide screen bld1
            call her_chibi("stand", "door", "base", flip=True)
            with d3
            pause .2

            call her_chibi("leave")

            # Cho runs out the door.
            if d_flag_01: # On desk
                play sound "sounds/08_hop_on_desk.ogg"
                show screen blkfade
                with d3
                pause 1

                hide screen bld1
                hide screen blkfade
                call cho_chibi("stand", "desk", "base", flip=True)
                with d3

            else:
                hide screen bld1
                call cho_chibi("stand",570,"base", flip=True) # Facing the door.
                with d3

            pause .2

            cho "{size=+4}Give them back, you bitch!{/size}" ("scream", "narrow", "angry", "L", ypos="head", flip=True, trans=hpunch)

            play sound "sounds/run_03.ogg"
            call cho_walk(action="leave", speed=2)

            call bld
            gen "Did she just?" ("base", xpos="far_left", ypos="head")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            gen "I don't think she's coming back..." ("base", xpos="far_left", ypos="head")

            call bld
            gen "Nice, I still got her panties!" ("grin", xpos="far_left", ypos="head")

            # Panties acquired message!
            call give_reward("You have acquired Cho's panties!", "interface/icons/panties.webp")

        "\"Not even close.\"":
            $ states.cho.mood += 15
            cho "Not even clo--" ("soft", "wide", "base", "mid")
            her "" ("smile", "base", "base", "R")
            cho "Sir, could you please repeat that for me?" ("clench", "closed", "angry", "mid")
            gen "Hermione's body is superior." ("base", xpos="far_left", ypos="head")
            her "No surprise there..." ("base", "base", "base", "R")
            cho "No!{w} It clearly isn't!" ("scream", "narrow", "angry", "mid", trans=hpunch)
            cho "Are you mad, old man?" ("angry", "narrow", "angry", "mid")
            her "Don't use that tone with the headmaster..." ("soft", "closed", "base", "mid")
            cho "Nobody asked you!" ("mad", "narrow", "angry", "L")
            her "He's the wisest wizard at our school...{w} Surely his word should be final..." ("smile", "narrow", "base", "mid_soft")
            gen "I'd use the word astute, but I'll take wise..." ("base", xpos="far_left", ypos="head")
            cho "Why are you siding with her all of a sudden?" ("annoyed", "narrow", "angry", "mid")
            gen "Good question." ("base", xpos="far_left", ypos="head")
            gen "Miss Granger, why don't you show Miss Chang why your body is superior to hers..." ("base", xpos="far_left", ypos="head")
            gen "Share with us your two most compelling arguments..." ("grin", xpos="far_left", ypos="head")
            her "Sir?" ("soft", "wink", "base", "mid")
            cho @ cheeks blush "He's talking about your {b}tits,{/b} you dimwit!" ("angry", "closed", "angry", "mid")
            her @ cheeks blush "(...)" ("clench", "narrow", "base", "down") # Embarrassed
            cho "" ("annoyed", "narrow", "angry", "mid")
            gen "Yes Miss Granger!{w=0.5} Your very round{w=0.5}, handsomely spheroid{w=0.5}, perfectly sized{w=0.5}, very voluptuous and--" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I got it, Professor!" ("clench", "happyCl", "worried", "mid")
            cho @ cheeks blush "(Cow tits...)" ("annoyed", "narrow", "angry", "R")
            $ hermione.strip("robe", "accessory")
            her "Here..." ("base", "narrow", "base", "mid_soft")

            # Hermione shows her breasts.
            # play sound "sounds/boing02.ogg"
            $ hermione.strip("top", "bra")
            with d3
            pause .5

            her @ cheeks blush "" ("base", "narrow", "base", "mid_soft")
            call ctc

            her "Have a good look." ("soft", "narrow", "base", "mid_soft")
            cho @ cheeks blush "(...)" ("annoyed", "narrow", "angry", "downR") # Tries to look away.
            her "And you'd better take in what a {b}real pair{/b} looks like, slut." ("smile", "narrow", "angry", "R")
            cho "I'd rather not, or I might barf..." ("soft", "narrow", "angry", "R") #
            gen "Very nice, Miss Granger!" ("grin", xpos="far_left", ypos="head")

            menu:
                "\"Ten points to Gryffindor!\"":
                    $ gryffindor += 10
                    cho "(...)" ("annoyed", "narrow", "angry", "mid")
                    her "Thank you." ("soft", "narrow", "base", "mid_soft")

                "\"Fifty points to Gryffindor!\"":
                    $ states.cho.mood += 10
                    $ gryffindor += 50
                    cho "(Fifty?!)" ("soft", "wide", "base", "mid") # Shocked
                    her "Thank you." ("soft", "narrow", "base", "mid_soft")
                    cho @ cheeks heavy_blush "" ("clench", "closed", "angry", "mid")

            gen "For exposing those magnificent breasts." ("grin", xpos="far_left", ypos="head")

            # play sound "sounds/cloth_sound3.ogg"
            $ hermione.wear("all")
            with d3
            pause .5

            her "Any time, Professor." ("soft", "narrow", "base", "mid_soft")
            cho @ cheeks heavy_blush "(I bloody hate her!)" ("angry", "narrow", "angry", "L")

            her "If you don't mind, Sir." ("open", "base", "base", "R")
            her "I'd like to leave now." ("soft", "base", "base", "mid")
            cho "By all means, just go already." ("soft", "narrow", "angry", "R")
            her "Did something not go as you expected?" ("smile", "base", "base", "R")
            her "Did you think having me here when you exposed yourself would make me jealous..." ("soft", "closed", "base", "mid")
            cho @ cheeks blush "(...)" ("annoyed", "narrow", "angry", "L")
            her "Thank you for inviting me, Professor." ("soft", "narrow", "base", "mid_soft")
            her "I {b}did{/b} enjoy this little obscene \"freak-show\" you arranged for me..." ("grin", "narrow", "base", "mid_soft")
            cho @ cheeks heavy_blush "You'll regret this, Granger!" ("clench", "narrow", "angry", "L")

            if game.daytime:
                her "Have a nice day, Professor." ("soft", "closed", "base", "mid")
            else:
                her "Have a good night, Professor." ("soft", "closed", "base", "mid")

            gen "(...)" ("base", xpos="far_left", ypos="head")
            her "See you in class, Chang!" ("grin", "narrow", "base", "R_soft")
            cho @ cheeks blush "*Tzzzz*!" ("angry", "closed", "angry", "mid")
            cho @ cheeks heavy_blush "Cow..." ("annoyed", "narrow", "angry", "R")

            # Hermione leaves.
            call her_walk(action="leave")

            # Cho stands close to your desk.
            call hide_characters
            show screen blkfade
            call cho_chibi("stand", "desk", "base", flip=True)
            with d3

            pause .5
            hide screen blkfade
            with d3

            pause .8
            call cho_chibi("stand", "desk", "base", flip=False)

            cho "I thought you were on my side, Sir!" ("soft", "narrow", "angry", "mid", xpos="mid", ypos="base", flip=False)
            gen "I'm on nobody's side, because nobody is on my side..." ("base", xpos="far_left", ypos="head")
            cho "You were supposed to have my back! Not Granger's!" ("angry", "closed", "angry", "mid")
            cho "That {b}whore{/b} doesn't deserve your praise!" ("soft", "narrow", "angry", "mid")
            gen "She made some good arguments..." ("base", xpos="far_left", ypos="head")
            gen "\"A couple\" of good arguments, to be precise!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "They're barely larger than mine..." ("annoyed", "narrow", "base", "downR")
            cho "You'll see, Sir.{w} I'm better than her.{w} And I'll prove it to you..." ("soft", "narrow", "angry", "mid")
            gen "Well, that is yet to be seen." ("grin", xpos="far_left", ypos="head")

            # Cho gets dressed.
            play sound "sounds/cloth_sound.ogg"
            show screen blkfade
            with d5
            $ cho.wear("all")
            hide screen cho_cloth_pile
            hide screen blkfade

            cho @ cheeks blush "Sir, my *Ehm*...{w} my panties..." ("open", "narrow", "angry", "R", xpos="mid", ypos="base", trans=fade)
            gen "Oh, of course..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "" ("annoyed", "narrow", "angry", "mid")
            pause .5
            gen "Give me just a moment..." ("base", xpos="far_left", ypos="head")
            play sound "sounds/sniff.ogg"
            nar "You give Cho's panties one last sniff before handing them back to the girl."
            gen "There." ("angry", xpos="far_left", ypos="head")
            cho @ cheeks blush "(Pervert...)" ("annoyed", "narrow", "angry", "R")
            cho "I think it's time for me to go now." ("soft", "closed", "angry", "mid")
            cho "Until next time, [name_genie_cho]." ("soft", "narrow", "angry", "mid")

            # Cho leaves.
            call cho_walk(action="leave")

            call bld
            gen "Damn!" ("angry", xpos="far_left", ypos="head")
            gen "For somebody who does a lot of exercising, she smells really nice!" ("grin", xpos="far_left", ypos="head")
            gen "Maybe I should be a bit nicer to her next time..." ("base", xpos="far_left", ypos="head")

            $ states.cho.ev.panty_thief.acquired = False


        "\"Let Hermione assess you, Cho.\"":
            $ states.her.mood += 6
            cho "Her?" ("soft", "wide", "base", "mid")
            her "I couldn't care less about the way she looks!" ("soft", "base", "angry", "mid")
            cho "(...)" ("annoyed", "narrow", "angry", "L")
            gen "Are you sure about that? I've seen you staring..." ("base", xpos="far_left", ypos="head")
            cho "" ("base", "narrow", "angry", "L")
            her "Because she just so happens to be standing there, butt naked!{w} In your office!" ("angry", "closed", "angry", "mid")
            gen "I'd like you to rate Miss Chang's figure, truthfully, and to the best of your ability." ("base", xpos="far_left", ypos="head")
            her "Really? Do I have to?" ("annoyed", "base", "base", "mid")
            gen "You do! I'd really like to hear your opinion on Miss Chang's shamelessly exposed body!" ("grin", xpos="far_left", ypos="head")
            cho "*Mhmm*" ("base", "closed", "base", "mid") # Self assured.
            her "Fine..." ("soft", "narrow", "angry", "R")
            her "\"Poor\", I'd say..." ("soft", "closed", "base", "mid")
            cho "How dare you!{w=0.6} You snobby skunk!" ("scream", "narrow", "angry", "L", trans=hpunch)
            her "" ("base", "base", "base", "R")
            gen "(Is that better or worse than \"troll?\")" ("base", xpos="far_left", ypos="head") # Snape explained school ratings during the match.
            cho "Our Professor asked you to rate my body truthfully!" ("mad", "narrow", "angry", "L")
            her "Which I did!{w} And it's at \"dreadful\" now!" ("soft", "closed", "base", "mid")
            cho "\"Dreadful\"?!" ("soft", "wide", "base", "mid")
            cho @ cheeks blush "You're a {b}lying bitch,{/b} Granger!" ("angry", "closed", "angry", "mid")
            her "Sir, you can't let her talk to me like that!" ("angry", "base", "angry", "mid")
            gen "Bitch isn't even a proper curse word." ("base", xpos="far_left", ypos="head")
            gen "You can say that on TV..." ("base", xpos="far_left", ypos="head")
            cho "Granger, why don't you tell us which part of my immaculate body deserves such a poor rating?" ("soft", "narrow", "angry", "L")
            her "Very well..." ("soft", "closed", "base", "mid")
            her "For one, you are a {b}narcissistic bitch!{/b}{w} That makes the presumption her body is superior to all others..." ("open", "base", "angry", "L")
            cho "Because it is." ("smile", "narrow", "angry", "mid")
            her "Not to mention that you have even fewer curves than some of the boys I know..." ("grin", "base", "angry", "mid")
            cho @ cheeks blush "" ("annoyed", "narrow", "angry", "mid")
            her "Maybe once your Quidditch endeavours all fail, you can apply for a profession to model male underwear..." ("soft", "closed", "base", "mid")
            cho "I wonder where you're getting {b}your{/b} undergarments from..." ("soft", "closed", "base", "mid")
            cho "Stealing them from Madam Pomfrey, are you?" ("smile", "narrow", "angry", "mid")
            her "I do not!!!" ("open", "wide", "base", "stare")
            gen "Girls, we all know what really counts is how we appear on the inside." ("base", xpos="far_left", ypos="head")
            her "" ("angry", "closed", "angry", "mid")
            cho "Oh, shut up!" ("angry", "narrow", "angry", "mid")
            her "Professor, you're the one who continuously asks us to expose ourselves!" ("soft", "base", "angry", "mid")
            gen "Well yes. I also never claimed that {b}I{/b} was pretty on the inside." ("base", xpos="far_left", ypos="head")
            gen "You of all people should know better by now..." ("base", xpos="far_left", ypos="head")
            her "Despicable..." ("angry", "narrow", "angry", "R")
            cho "Don't worry, Granger!" ("soft", "narrow", "angry", "L")
            cho "If you were to start doing hourly exercises, our Professor might even be attracted to you by the end of the year..." ("soft", "closed", "raised", "mid")
            her "Hourly exercises?" ("soft", "wide", "base", "stare") # Shocked
            cho "But I wouldn't say all hope is lost!" ("smile", "narrow", "angry", "L")
            cho "While your figure might be a bit repulsive to the eyes..." ("soft", "closed", "base", "mid")
            cho @ cheeks blush "I don't mind looking at those {b}huge melons{/b} of yours." ("soft", "narrow", "base", "L")
            her "How dare you speak of them like that!" ("angry", "narrow", "angry", "R")
            gen "*Heh*... Melons..." ("grin", xpos="far_left", ypos="head")
            her "Sir, I'd like to leave now." ("open", "base", "angry", "mid")

            cho "Already missing your books, are you?" ("annoyed", "narrow", "base", "L")
            her "I am not.{w} And I don't appreciate being made fun of!" ("angry", "closed", "angry", "mid")

            if game.daytime:
                her "Good day, Sir." ("soft", "base", "angry", "mid")
                cho "See ya around, Granger..." ("smile", "narrow", "angry", "L")
                her "*Hmpf*" ("annoyed", "narrow", "angry", "R")

            else:
                her "Good night, Sir." ("soft", "base", "angry", "mid")
                cho "Nighty-night, Granger..." ("soft", "narrow", "angry", "L")
                her "*Tzzzzzh*!" ("annoyed", "narrow", "angry", "R")

            # Hermione leaves.
            call her_walk(action="leave")

            show screen blkfade
            call cho_chibi("stand", "desk", "base", flip=False)
            with d3

            hide screen blkfade
            cho "I have to say, [name_genie_cho], doing these favours is fun!" ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", flip=False, trans=fade)
            gen "I'm glad you're enjoying yourself." ("base", xpos="far_left", ypos="head")
            cho "Believe me, Sir. I am." ("smile", "narrow", "angry", "mid")
            cho "" ("horny", "narrow", "angry", "mid")
            pause .4

            # Cho gets dressed.
            play sound "sounds/cloth_sound.ogg"
            $ cho.wear("all")
            hide screen cho_cloth_pile
            with d3
            pause .5

            cho "Now, if you excuse me..." ("soft", "base", "base", "mid")

            if game.daytime:
                cho "I have to head back to classes." ("soft", "base", "base", "R")
                gen "I still got your--" ("base", xpos="far_left", ypos="head")
                cho "See ya next time, [name_genie_cho]!" ("smile", "narrow", "angry", "mid")
            else:
                cho "I have to head back to my dorms." ("soft", "base", "base", "R")
                gen "Don't you want your--" ("base", xpos="far_left", ypos="head")
                cho "Sweet dreams, [name_genie_cho]!" ("smile", "narrow", "angry", "mid")

            call cho_walk(action="leave")

            call bld
            gen "Nice, I still got her panties!" ("grin", xpos="far_left", ypos="head")

            call give_reward("You have acquired Cho's panties!", "interface/icons/panties.webp")
            $ states.cho.ev.panty_thief.acquired = True

    # Reset Hermione clothing.
    $ hermione.equip(her_outfit_last)

    return

label cc_pf_strip_T2_E3_hermione_repeat:
    # Equip Hermione default clothing.
    $ her_outfit_last.save() # Store current outfit.
    $ hermione.equip(her_outfit_default)    #Equip Hermione default clothing.

    # Hermione enters.
    play sound "sounds/door.ogg"
    call her_chibi("stand", "door", "base")
    with d3
    pause .5

    call chibi_emote("thought", "hermione")
    pause .8

    call her_walk(660, "base")

    cho "" ("horny", "narrow", "angry", "L", xpos="mid", ypos="base", flip=True)
    her "You wanted to see me, Professor?" ("soft", "closed", "base", "mid", xpos="base", ypos="base")
    gen "Yes, but I wasn't the only one." ("grin", xpos="far_left", ypos="head")
    her "(...)" ("annoyed", "narrow", "angry", "R")
    cho "Hi, Granger!" ("smile", "narrow", "angry", "L")
    her "Let me guess, we are here to marvel at your insecurity again?" ("soft", "closed", "base", "mid")
    cho "Granger, instead of spitting out insults, why don't you join me and have some fun for once?" ("soft", "base", "raised", "L")
    cho "Strip down for your headmaster as well, like you usually do..." ("smile", "narrow", "angry", "L")
    cho "Or would it bother you too much, now that I'm here?" ("horny", "narrow", "base", "L")
    her "*glare*" ("angry", "base", "angry", "mid")
    cho "Maybe then you'd have a chance to win against me!{w} And earn some useless Gryffindor points while you're at it." ("soft", "base", "base", "L")
    her "I don't think that will be necessary..." ("soft", "closed", "base", "mid")
    cho "Well, we all already know how this is going to turn out don't we, [name_genie_cho]?" ("soft", "base", "base", "mid")
    cho "My body is still better than Miss Granger's, isn't it?" ("smile", "narrow", "angry", "L")
    her "" ("annoyed", "base", "angry", "mid")
    call ctc

    call cc_pf_strip_T2_E3_hermione_choices

    return
