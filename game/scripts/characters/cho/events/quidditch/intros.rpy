
# Training Intro 1. (Hufflepuff)

label cho_quid_E1:
    # Genie should get into a drill sergeant mood here, but fails at the end.

    cho "" (xpos="mid", ypos="base", trans=fade)

    gen "Are you ready for your first training session?" ("base", xpos="far_left", ypos="head")
    cho "Of course, Professor!" ("smile", "base", "base", "mid")
    gen "Professor? Who are you calling Professor, girl?" ("angry", xpos="far_left", ypos="head")
    cho "I'm... sorry?" ("soft", "base", "worried", "mid")
    gen "From now on you will address me only as \"Sir\"!{w} Or..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"-Coach-\"":
            $ name_genie_cho = "Coach"
        "\"-Sergeant-\"":
            $ name_genie_cho = "Sergeant"
        "\"-Captain-\"":
            $ name_genie_cho = "Captain"
        "\"-Professor-\"":
            $ name_genie_cho = "Professor"
            gen "You know what, keep calling me Professor..." ("base", xpos="far_left", ypos="head")

    cho "Yes, [name_genie_cho]." ("base", "base", "angry", "mid")
    gen "And I will call you..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"-Cadet-\"":
            $ name_cho_genie = "Cadet"
        "\"-Pilot-\"":
            $ name_cho_genie = "Pilot"
        "\"-Maggot-\"":
            $ name_cho_genie = "Maggot"
            cho "(...)" ("quiver", "base", "worried", "R")
        "\"-Eagle One-\"":
            $ name_cho_genie = "Eagle One"
        "\"-Cho-\"":
            $ name_cho_genie = "Cho"
        "\"-Miss Chang-\"":
            $ name_cho_genie = "Miss Chang"
            cho "Don't you already call me that, [name_genie_cho]?" ("open", "base", "raised", "mid")
            gen "Never question your [name_genie_cho], [name_cho_genie]!" ("base", xpos="far_left", ypos="head")

    cho "Yes, [name_genie_cho]!" ("soft", "closed", "angry", "mid")
    gen "Let's start with your {i}Quiddesh{/i} training!" ("angry", xpos="far_left", ypos="head")
    cho "\"Quidditch\", Sir." ("annoyed", "narrow", "angry", "mid")
    gen "Let's start with your \"Quidditch\" training, [name_cho_genie]." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "!!!" ("smile", "happyCl", "base", "mid")
    cho "Shall I call the rest of my team up here?" ("open", "base", "base", "mid")
    gen "What? Why?" ("base", xpos="far_left", ypos="head")
    cho "So they can hear your expertise as well, of course." ("soft", "narrow", "base", "mid")
    gen "I don't think that will be necessary." ("base", xpos="far_left", ypos="head")
    gen "Let's focus on you, for the moment..." ("base", xpos="far_left", ypos="head")
    cho "Very well, [name_genie_cho]." ("soft", "base", "worried", "R")
    gen "Tell me, how do you usually play?{w} Is there a specific reason why you've been losing?" ("base", xpos="far_left", ypos="head")

    cho "Well, it sort of differs depending on which team we're playing against..." ("open", "narrow", "base", "R")
    gen "...{w} Let's start with whichever team you're playing against first." ("base", xpos="far_left", ypos="head")
    cho "That'd be Hufflepuff...{w=0.4} Most of their previous victories against us were achieved thanks to their seeker!" ("open", "base", "base", "mid")
    cho "He's always catching the snitch before me." ("quiver", "narrow", "worried", "down")
    cho "I don't know how he does it, to be honest. It always happens so quick..." ("open", "narrow", "worried", "mid")
    gen "And you are \"both\" looking for that thing? At the same time?" ("base", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]." ("soft", "base", "base", "mid")
    cho "I do my best flying around the pitch searching for it. But it's just so small and really tricky to see..." ("angry", "base", "worried", "down")
    gen "Why don't you look for it together? After all, there is only one." ("base", xpos="far_left", ypos="head")
    cho "*Hmm*?" ("annoyed", "base", "base", "mid")
    gen "You just need to grab that Snatch before he does." ("grin", xpos="far_left", ypos="head")
    cho "???" ("annoyed", "wide", "raised", "mid")
    cho "[name_genie_cho]! It's \"Snitch\"!" ("angry", "closed", "angry", "mid")
    gen "Potato {i}potato{/i}..." ("base", xpos="far_left", ypos="head")
    cho "You just said the same thing twice..." ("open", "base", "raised", "R")
    gen "Exactly..." ("base", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "mid")
    cho "Anyhow... As I said, I don't really have a chance once he's caught sight of it." ("open", "narrow", "base", "mid")
    gen "Caught sight of what?" ("base", xpos="far_left", ypos="head")
    cho "The snitch!" ("annoyed", "narrow", "base", "mid")
    gen "Oh, I see..." ("base", xpos="far_left", ypos="head")
    cho "There's no way for me to stop him, with how fast and determined he is..." ("open", "base", "base", "R")
    gen "Well, lucky for you, you have me!" ("grin", xpos="far_left", ypos="head")
    cho "" ("annoyed", "base", "raised", "mid")
    gen "I'm also very fast and determined!" ("grin", xpos="far_left", ypos="head")
    gen "And you just gave me a great idea." ("base", xpos="far_left", ypos="head")
    gen "We'll need to distract him!" ("base", xpos="far_left", ypos="head")
    gen "So you can get a hold of that Snatch before he does!" ("angry", xpos="far_left", ypos="head")
    cho "Please stop saying that, [name_genie_cho]!" ("angry", "closed", "angry", "mid")
    gen "Saying what?" ("base", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "mid")
    cho "{size=-4}\"Snatch.\"{/size}" ("soft", "narrow", "angry", "mid")
    gen "*He-he-he*...{w} Now you've said it!" ("grin", xpos="far_left", ypos="head")
    cho "Could we please just talk about your plan, [name_genie_cho]?" ("open", "narrow", "angry", "R")
    gen "Patience, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho "Tell me!" ("scream", "closed", "angry", "mid", trans=hpunch)
    cho "" ("annoyed", "narrow", "angry", "mid")

    gen "We'll hit him where he least expects it!" ("base", xpos="far_left", ypos="head")
    cho "And that would be?" ("soft", "base", "angry", "mid")
    gen "The balls!" ("base", xpos="far_left", ypos="head")
    cho "What?!?" ("mad", "wide", "raised", "mid")
    cho "Sir, surely you can't be--" ("clench", "base", "angry", "mid")
    gen "If we entice him during the game he'll lose focus..." ("base", xpos="far_left", ypos="head")
    cho "Entice...{w=0.4} what are you--" ("clench", "base", "base", "mid")

    cho "Sir, this is just ridiculous!" ("scream", "closed", "angry", "mid", trans=hpunch)
    cho "I thought a highly regarded wizard of your stature would know at least something that could help us at Quidditch." ("open", "narrow", "angry", "mid")
    cho "I didn't hold it against you that you seemingly know very little about the sport." ("open", "base", "angry", "R")
    gen "Which I proved you wrong, but who cares..." ("base", xpos="far_left", ypos="head")
    cho "But I thought it was at least worth a try.{w} Although after hearing your suggestion--" ("upset", "narrow", "angry", "mid")
    gen "Believe me when I say this..." ("base", xpos="far_left", ypos="head")
    gen "The only way you can keep a man from fulfilling his sought-out purpose, is by confronting him with his most primal instinct!" ("angry", xpos="far_left", ypos="head")
    cho "Which would be?" ("annoyed", "narrow", "angry", "mid")
    gen "The act of procreation!" ("grin", xpos="far_left", ypos="head")
    cho "Sir, are you suggesting I should have \"sex\" with him?!" ("soft", "wide", "base", "mid") # Shocked
    gen "What? I never said that..." ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "You have a really dirty mind, girl!" ("grin", xpos="far_left", ypos="head")
    cho "But you just said--" ("angry", "closed", "angry", "mid")
    gen "I merely want you to distract him with your body, during the match." ("base", xpos="far_left", ypos="head")
    gen "And then, when he can't keep his eyes off you..." ("grin", xpos="far_left", ypos="head")
    gen "You grab that Snatch!" ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "mid")
    cho "I'm sorry Sir, but I feel methods like those would get us nowhere!" ("open", "closed", "raised", "mid")
    cho "And it's very improper for a teacher to suggest such things! Not to mention right out vulgar!" ("open", "base", "angry", "R")
    cho "I'll be leaving now.{w=0.8} Please only call me should you decide to finally take things seriously..." ("soft", "narrow", "angry", "mid")
    gen "And you, think about using that petite body of yours to get closer to your dreams!" ("grin", xpos="far_left", ypos="head")
    cho "*Tzzzz*" ("angry", "closed", "angry", "mid")

    if game.daytime:
        cho "Good day, Sir..." ("soft", "narrow", "angry", "mid")
    else:
        cho "Good night, Sir..." ("soft", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call popup("You've lost the ability to train Cho in Quidditch.", "Congratulations!", "interface/icons/head/cho.webp")

    call bld
    gen "She'll get over it..." ("base", xpos="far_left", ypos="head")

    # Flags
    $ states.cho.mood += 9
    $ states.cho.ev.quidditch.e1_complete = True

    jump end_cho_event

label cho_quid_E2:
    # Genie regains ability to train Cho

    cho "" (xpos="mid",ypos="base", trans=fade)
    gen "So, have you considered going with my training methods?" ("base", xpos="far_left", ypos="head")
    cho "I... Yes..." ("soft", "closed", "angry", "mid")
    cho "I looked at other options, but seeing how little time we have left...{w} Well, I suppose I have no other choice." ("open", "narrow", "angry", "R")
    cho "If there's any chance your methods could help us win the cup this year, then I'm willing to try them, Sir." ("open", "narrow", "angry", "mid")
    gen "I'm glad you've come to your senses." ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "R")
    gen "Let's get this ball rolling--{w=0.4} *Ahem*... flying then shall we!" ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "base", "base", "mid")

    gen "Now, let me show you..." ("base", xpos="far_left", ypos="head")
    cho "" ("base", "base", "base", "mid")

    gen "First, get your flying thing ready!" ("base", xpos="far_left", ypos="head")
    cho "My broom?" ("soft", "base", "raised", "mid")
    gen "Broom... flying carpet... Whichever you prefer." ("base", xpos="far_left", ypos="head")
    cho "Only brooms are allowed in Quidditch, Sir." ("annoyed", "base", "base", "mid")
    gen "Good for you." ("base", xpos="far_left", ypos="head")
    gen "And put on your Quidditch gear while you're at it..." ("base", xpos="far_left", ypos="head")
    cho "Yes, Sir.{w} Let me just go and get it." ("smile", "base", "base", "mid")
    cho "I'll be right back." ("base", "base", "base", "mid")

    call cho_walk(action="leave", speed=1.5) # Cho moves, excitedly.

    call blkfade
    pause .8

    # Scene Setup
    call gen_chibi("stand", "desk", "base")
    call cho_chibi("stand", "right", "base")

    $ cho_outfit_last.save()
    $ cho.equip(cho_outfit_quidditch) # Equip quidditch set

    play sound "sounds/door.ogg"
    pause .5

    call hide_blkfade
    pause .8

    cho "Ready when you are, [name_genie_cho]!" ("smile", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    gen "Perfect, now get on that broom and follow my instructions..." ("base", xpos="far_left", ypos="head")
    hide cho_main
    with d3

    # Tutorial menu
    $ _selected = [False, False, False]
    $ menu_y = 0.8

    label .choices:

    if not all(x == True for x in _selected): # Has selected every position once? Loop if the answer is no.
        call bld
        menu:
            gen "Could you..." ("base", xpos="far_left", ypos="head")
            "\"Fly in front of me.\"" if not _selected[0]:
                $ _selected[0] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                call cho_walk("mid", "base")
                if cho_chibi.flip == False:
                    gen "Looking good, now turn away from me..." ("base", xpos="far_left", ypos="head")
                    call cho_chibi("fly", "mid", "base", flip=True)
                    with d5
                cho "Like this?" ("soft", "base", "base", "R", ypos="head", flip=False)
                gen "A bit higher maybe..." ("base", xpos="far_left", ypos="head")
                call cho_walk(550, 200+180)

                gen "Excellent!" ("base", xpos="far_left", ypos="head")

                jump cho_quid_E2.choices

            "\"Fly above me.\"" if not _selected[1]:
                $ _selected[1] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                gen "Move a bit higher." ("base", xpos="far_left", ypos="head")
                call cho_walk(600, 150+180)
                cho "Like this?" ("soft", "base", "base", "downR", ypos="head", flip=False)
                gen "Great, you've got some excellent control over that stick." ("base", xpos="far_left", ypos="head")

                jump cho_quid_E2.choices

            "\"Fly close to me.\"" if not _selected[2]:
                $ _selected[2] = True
                call bld("hide")

                if not cho_chibi.action == "fly":
                    call cho_chibi("fly", "mid", "base")
                    with d5

                cho "How close?" ("soft", "base", "raised", "mid", ypos="head", flip=False)
                gen "As close as you can get..." ("base", xpos="far_left", ypos="head")
                call cho_walk(450, 240+180)
                gen "Nice..." ("base", xpos="far_left", ypos="head")
                cho "..." ("soft", "narrow", "raised", "mid", ypos="head", flip=False)

                jump cho_quid_E2.choices
    else:
        pass

    gen "That should be enough..." ("base", xpos="far_left", ypos="head")
    gen "I presume you're able to hold these positions during movement?" ("base", xpos="far_left", ypos="head")
    cho "Of course." ("open", "closed", "raised", "mid", ypos="head", flip=False)
    gen "Great!" ("base", xpos="far_left", ypos="head")
    gen "You can come down now." ("base", xpos="far_left", ypos="head")
    cho "Okay." ("open", "base", "base", "mid", ypos="head", flip=False)

    #Cho flies down
    call cho_walk("mid", "base")
    call cho_chibi("stand", "right", "base")
    with fade


    gen "Great job, we should definitely use positioning to our advantage!" ("base", xpos="far_left", ypos="head")
    cho "Well, that much is true for any quidditch game..." ("open", "base", "raised", "mid")
    cho "So I'm not exactly sure what we've achieved here." ("soft", "base", "raised", "R")
    gen "All in due time, [name_cho_genie]..." ("base", xpos="far_left", ypos="head")
    gen "With my training methods you'll have the upper hand over those other teams, I'm sure of it." ("base", xpos="far_left", ypos="head")
    cho "I'll have to take you at your word then..." ("base", "base", "raised", "mid") #cautious smile
    cho "So, what's next?" ("open", "base", "raised", "mid")
    gen "That's all for today." ("base", xpos="far_left", ypos="head")
    cho "Already? I usually train for a couple of hours!" ("angry", "base", "raised", "mid")
    gen "Yes, I need to come up with a pl--{w=0.3}{nw}" ("base", xpos="far_left", ypos="head")
    gen "Yes, I need to come up with a pl--{fast} prepare for our next session!" ("grin", xpos="far_left", ypos="head")
    cho "Oh...{w=0.3} okay." ("soft", "base", "base", "down")
    cho "Bye then, [name_genie_cho]." ("base", "base", "base", "mid")
    gen "Bye for now, [name_cho_genie]." ("base", xpos="far_left", ypos="head")

    call cho_walk(action="leave")

    gen "(Now to find out what the boy's into and make sure she's prepared to do what it takes...)" ("base", xpos="far_left", ypos="head")
    call popup("You've unlocked Cho personal favours!", "Congratulations!", "interface/icons/head/cho.webp")

    # Flags
    $ cho.equip(cho_outfit_last)
    $ states.cho.ev.quidditch.e2_complete = True
    $ states.cho.favors_unlocked = True
    $ states.cho.ev.quidditch.lock_training = False

    call gen_chibi("sit_behind_desk")
    with fade

    jump end_cho_event

label cho_quid_E3:
    # Commentator disaster, Lee Jordan is unable to commentate.

    call cho_walk(action="enter", xpos="desk", ypos="base", speed=1.5)

    stop music fadeout 1

    cho "[name_genie_cho], there's been a disaster!" ("scream", "closed", "angry", "mid", xpos="mid", ypos="base", trans=hpunch)

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    gen "Off to a good start..." ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho], something terrible happened to Lee Jordan!" ("soft", "narrow", "worried", "mid")
    gen "Lee Jordan?{w=0.5} Is that a famous basketball player I'm not aware of?" ("base", xpos="far_left", ypos="head")
    cho "What?{w=0.5} No Sir, Lee is our quidditch commentator!" ("soft", "narrow", "base", "mid")
    cho "He got hit in the throat by a bludger!" ("disgust", "base", "raised", "down")
    cho "Madam Pomfrey says he'll be able to talk in a few days, but yelling is out of the picture for the rest of the season." ("soft", "closed", "worried", "mid")
    cho "What are we going to do?! We can't have a Quidditch Cup without a commentator!" ("soft", "base", "worried", "mid")
    gen "Can't you play without one?" ("base", xpos="far_left", ypos="head")
    cho "No... Someone has to announce the points after all." ("annoyed", "narrow", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")

    $ _selected = [False, False]

    label .choices:
    menu:
        gen "How about we ask..." ("base", xpos="far_left", ypos="head")
        "\"Hermione\"":
            pass

        "\"Astoria\"" if states.ast.unlocked and not _selected[0]:
            $ _selected[0] = True

            cho "That mischievous little..." ("clench", "wide", "raised", "mid")
            cho "Not a chance!" ("open", "closed", "angry", "mid")
            cho "Besides, [name_genie_cho]. Did you forget that she's a Slytherin?" ("open", "narrow", "angry", "mid")
            gen "Right. No Slytherins. Got it." ("base", xpos="far_left", ypos="head")
            gen "How about..." ("base", xpos="far_left", ypos="head")

            jump cho_quid_E3.choices

        "\"Luna\"" if states.lun.unlocked and not _selected[1]:
            $ _selected[1] = True

            cho "Luna? Luna Lovegood, [name_genie_cho]?" ("open", "narrow", "raised", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            cho "Surely{w=0.3}, nobody in their right mind would let Luna Lovegood commentate." ("grin", "happyCl", "base", "mid") # Book quote.
            #gen "I am of right mind, Miss Chang...{w} and don't call me Shirley..." ("base", xpos="far_left", ypos="head")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            cho "Knowing her, she'd probably commentate the grass as it's growing..." ("open", "base", "base", "R")
            cho "Trust me, [name_genie_cho]. Luna would be a terrible choice!" ("soft", "narrow", "base", "mid")
            gen "Fine. How about..." ("base", xpos="far_left", ypos="head")

            jump cho_quid_E3.choices

    cho "Hermione Granger?" ("scream", "wide", "raised", "mid")
    cho "She wouldn't know the first thing about quidditch!" ("clench", "narrow", "angry", "mid")
    cho "You can't pick her!" ("annoyed", "narrow", "angry", "mid")
    gen "Now, now... Don't underestimate Miss Granger..." ("base", xpos="far_left", ypos="head")
    gen "Why don't we just ask her first?" ("base", xpos="far_left", ypos="head")
    cho "Absolutely not! I won't talk to that Gryffindor skunk ever again!" ("scream", "closed", "angry", "mid")
    cho "Didn't I make it clear that I don't want her to {b}ever{/b} be involved in Quidditch again?" ("annoyed", "narrow", "angry", "mid")
    gen "Alright... are there any other students who know Quidditch rules well enough to take this... Jordan boy's place?" ("base", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "base", "base", "down")
    gen "Well?" ("base", xpos="far_left", ypos="head")
    cho "Well, most of them would already be on one of the Quidditch teams..." ("soft", "base", "raised", "R")
    cho "But Granger wouldn't know anything about Quidditch either!" ("annoyed", "narrow", "angry", "mid")
    gen "Do you know anybody else suited for the job?" ("base", xpos="far_left", ypos="head")
    cho "{size=-4}Probably anyone at this point...{/size}" ("annoyed", "base", "raised", "R")
    stop music fadeout 1
    cho "(Wait a minute...)" ("annoyed", "wide", "raised", "mid")
    play music "music/marty-gots-a-plan-by-kevin-macleod.ogg" fadein 1.0 if_changed
    cho "No..." ("smile", "base", "base", "mid") #Mischievous smile
    gen "I'll ask her... What's the worst that could happen..." ("grin", xpos="far_left", ypos="head")
    cho "Yeah, actually you're probably right..." ("grin", "narrow", "angry", "mid")
    gen "Don't worry she'll do a--" ("base", xpos="far_left", ypos="head")
    gen "Wait... what did you say?" ("angry", xpos="far_left", ypos="head")
    cho "I'm sure she'll do a heckin' good job!" ("smile", "narrow", "angry", "mid")
    cho "(She'll flub the whole thing and everyone will laugh at her.)" ("smile", "narrow", "angry", "R") #Mischievous smile
    gen "Well, great then. I'll ask her in that case!" ("grin", xpos="far_left", ypos="head")
    cho "(She'll be so humiliated! And no one will ever see her as anything but a show-off that knows nothing!)" ("grin", "narrow", "angry", "down")
    cho "(I can already picture it...{w=0.8} the whole school laughing...)" ("silly", "base", "raised", "up")
    gen "Miss Chang?" ("base", xpos="far_left", ypos="head")
    cho "Oh, thank you for handling it professor!" ("open", "base", "base", "mid")
    cho "Boy, you took a load off my mind..." ("silly", "happyCl", "base", "mid", trans=hpunch)
    gen "(...)" ("base", xpos="far_left", ypos="head")
    cho "I'll be heading back to class, if you don't mind." ("soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    gen "(...)" ("base", xpos="far_left", ypos="head")

    # Reset
    $ cho.equip(cho_outfit_last) # Equip last worn clothes
    $ states.cho.ev.quidditch.e3_complete = True
    $ states.cho.ev.quidditch.lock_practice = True

    jump end_cho_event

label cho_quid_E4:
    # Genie asks Hermione if she would agree to commentate the game.

    her "" (xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], how much do you know about Quidditch?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], I mean, I've taken flying lessons... they're mandatory." ("open", "base", "base", "R")
    gen "Ah, okay... and here I was hoping that you'd be able to commentate this year's Quidditch games..." ("base", xpos="far_left", ypos="head")
    her "Me, wasting time on something as stupid as--" ("base", "closed", "base", "mid")
    her "Wait...{w=0.3} What did you say?" ("open", "squint", "base", "mid")
    gen "I was going to ask you if you'd commentate this year's Quidditch games..." ("base", xpos="far_left", ypos="head")
    her "You want me... to commentate this year's Inter-House Quidditch cup?" ("open", "wide", "base", "mid")
    her "I'd be honoured, sir!" ("scream", "closed", "base", "mid", trans=hpunch)
    her "Quidditch has always been one of my passions, to be able to commentate it..." ("open", "base", "angry", "mid")
    her "Not to mention getting to make all the announcements..." ("smile", "base", "base", "R")
    her "The speeches..." ("grin", "happy", "base", "mid")

    if states.her.level < 18:
        her "The paper..." ("soft", "narrow", "annoyed", "up")
        her "The {heart}{b}preparation{/b}{heart}..." ("open_tongue", "narrow", "base", "up")
    else:
        her "Everybody will be focused on me..." ("soft", "narrow", "annoyed", "up")

    her "I accept!" ("scream", "closed", "angry", "mid", trans=hpunch)
    gen "I thought you just said you didn't--" ("angry", xpos="far_left", ypos="head")
    her "Cho will be so mad!" ("crooked_smile", "happy", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "Congratulations then, [name_hermione_genie]! You got the job." ("grin", xpos="far_left", ypos="head")
    her "Ah!!! I better start learning--{w=0.4} I mean, preparing my opening speech!" ("open", "wide", "base", "mid", trans=hpunch)

    call her_walk(action="leave", speed=1.5)

    call bld
    gen "Aaaa-nd, she's gone..." ("base", xpos="far_left", ypos="head")
    gen "I better tell Cho about the...{w=0.8} news." ("base", xpos="far_left", ypos="head")

    $ states.cho.ev.quidditch.e4_complete = True

    jump end_hermione_event # This is correct, it's Hermione talking!

label cho_quid_E5:
    # Slytherin Quidditch intro. Triggers after you summon Cho.

    stop music fadeout 6.0

    call cho_walk(action="enter")
    call cho_walk("mid", "base")

    if game.daytime:
        cho "Good morning, [name_genie_cho]..." ("annoyed", "narrow", "worried", "downR", xpos="right", ypos="base", trans=d3)
        gen "Mornin'." ("base", xpos="far_left", ypos="head")
    else:
        cho "Good evening, [name_genie_cho]..." ("annoyed", "narrow", "worried", "downR", xpos="right", ypos="base", trans=d3)
        gen "Evenin'." ("base", xpos="far_left", ypos="head")
    gen "[name_cho_genie], before we get back to our usual diversions, why don't we have a little chat about the recent happenings?" ("base", xpos="far_left", ypos="head")
    cho "Very well, [name_genie_cho]..." ("open", "narrow", "worried", "mid")
    gen "Cheer up, will you..." ("base", xpos="far_left", ypos="head")
    gen "Where did that high-spirit from your \"big win\" fly off to?" ("base", xpos="far_left", ypos="head")
    cho "Nowhere, [name_genie_cho]...{w=0.6} I'm still very happy we won the game, it's just..." ("open", "narrow", "worried", "down") # worried/sad
    cho "I'm a bit worried about the future." ("soft", "narrow", "worried", "mid") # sad/relieved
    gen "The future?" ("base", xpos="far_left", ypos="head")
    gen "You didn't get pregnant during your little celebration event, did you?" ("base", xpos="far_left", ypos="head")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho @ cheeks heavy_blush "WHAT?!" ("clench", "wide", "base", "mid")  # Upset/whatthefuck face
    cho @ cheeks blush "Sir, why would you even suggest that?!" ("angry", "narrow", "angry", "mid") # upset
    gen "Then what is it?" ("base", xpos="far_left", ypos="head")
    cho "It's about the upcoming quidditch match." ("annoyed", "narrow", "angry", "R") # annoyed - eyes R, mouth annoyed
    gen "Oh...{w=0.4} Of course..." ("base", xpos="far_left", ypos="head")
    gen "{size=-6}Always some stupid quest...{/size}" ("base", xpos="far_left", ypos="head")
    cho "Pardon?" ("annoyed", "narrow", "raised", "mid")
    gen "It's nothing,{w=0.5} please continue." ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho], I worry that we won't be able to beat Slytherin in the next match." ("annoyed", "narrow", "worried", "mid") # eyebrows sad, eyes mid, mouth pout
    gen "Slytherin is next?{w=0.6} Sweet!" ("grin", xpos="far_left", ypos="head")
    cho "They're an entirely different ballpark compared to Hufflepuff." ("open", "base", "worried", "mid")
    gen "Really? Why's that?" ("base", xpos="far_left", ypos="head")
    cho "They're brutal and ruthless!{w} And they think they can get away with anything..." ("open", "narrow", "angry", "mid") # eyebrows sad, eyes mid, mouth pout
    gen "Then we should do the same, shouldn't we?" ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "base", "mid")
    gen "We'll show those Slytherins what {b}we{/b} got -- no problem!" ("base", xpos="far_left", ypos="head")
    cho "..." ("base", "base", "base", "mid") # slight smile
    gen "(And show Snape who's boss.)" ("grin", xpos="far_left", ypos="head")
    gen "Trust me, our tactics have worked perfectly thus far, haven't they?" ("base", xpos="far_left", ypos="head")
    cho "I--{w=0.3} yes..." ("soft", "base", "raised", "downR")
    cho "You're right! Thank you, [name_genie_cho]." ("base", "base", "base", "mid") # happy

    $ states.cho.ev.quidditch.e5_complete = True
    $ states.cho.favors_unlocked = True

    jump cho_requests

label cho_quid_E6:
    # Hermione refuses to commentate Slytherin match.
    stop music fadeout 3.0

    pause 1.0

    call her_walk(action="enter")
    call chibi_emote("thought", "hermione")
    pause 2.0
    call chibi_emote("hide", "hermione")

    call bld
    gen "..." ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base")
    her "" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base") # annoyed
    pause .5
    her "I can't believe her..." ("clench", "closed", "angry", "mid", trans=hpunch) # angry
    gen "Good day to you too..." ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "That bitch has been walking around saying that I quit the commentator job." ("open", "base", "angry", "mid")
    gen "Who did?" ("base", xpos="far_left", ypos="head")
    her "Cho Chang." ("soft", "base", "angry", "mid")
    gen "..." ("angry", xpos="far_left", ypos="head")
    gen "Wait, so you didn't quit?" ("base", xpos="far_left", ypos="head")
    her "No! Why would I be here telling you this if I did?" ("angry", "base", "angry", "mid")
    gen "I guess you would've had to give me a two weeks notice..." ("base", xpos="far_left", ypos="head")
    her "You tell me, you're the one who appointed me." ("annoyed", "narrow", "annoyed", "mid")
    gen "Oh, right." ("base", xpos="far_left", ypos="head")
    her "And since I didn't sign anything..." ("soft", "closed", "base", "mid")
    her "I quit!" ("soft", "narrow", "base", "mid")
    gen "What?{w=0.5} You can't do that!" ("angry", xpos="far_left", ypos="head")
    her "Why not? After all, I'm terrible at it, aren't I?" ("clench", "base", "angry", "mid")
    her @ tears soft "I made such a fool out of myself during the Hufflepuff game..." ("upset", "base", "worried", "R") # Sad, tears
    her @ tears soft_blink "And now with the Slytherin team being next..." ("open", "happyCl", "worried", "mid")
    her @ tears soft "I won't just stand there and have them laugh at me..." ("open", "base", "worried", "mid")
    her @ tears soft "I'm not giving those Slytherins that satisfaction!" ("annoyed", "base", "worried", "R")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Tough luck, Miss Granger!\"":
            $ states.her.mood += 16

            her "Tough luck?!" ("clench", "wide", "base", "stare")
            gen "You agreed to do this, remember..." ("base", xpos="far_left", ypos="head")
            gen "May I remind you how many house points I gave you?" ("angry", xpos="far_left", ypos="head")
            her "No amount of house points was worth the humiliation I got!" ("angry", "base", "angry", "mid")
            gen "Well, *boo* --{w=0.3} bloody --{w=0.3} *hoo*..." ("base", xpos="far_left", ypos="head")
            her "*Tzzzs*!..." ("clench", "closed", "angry", "mid", emote="angry")
            her "Good luck finding somebody that is more willing to be the school's laughingstock!" ("open", "base", "angry", "mid")


        "\"We'll look for somebody more competent, then.\"":
            $ states.her.mood += 10

            her "More competent?!" ("clench", "base", "angry", "mid")
            gen "Surely we can find a replacement for you in no time." ("base", xpos="far_left", ypos="head")
            her "Well, if that's the case, it seems like I'm no longer needed..." ("open", "base", "angry", "mid")

        "\"All you need is a bit of practice...\"":
            if not states.her.status.sex:
                gen "(And a good fucking, but we'll get to that...)" ("grin", xpos="far_left", ypos="head")
            else:
                gen "(And a good fucking...)" ("grin", xpos="far_left", ypos="head")
            gen "You're a natural at this!" ("base", xpos="far_left", ypos="head")
            her @ tears soft "..." ("annoyed", "base", "worried", "mid")
            her @ tears soft "It doesn't matter..." ("soft", "base", "worried", "R")
            her @ tears soft_blink "Thanks to Cho, everybody now thinks I'm a fraud..." ("open", "happyCl", "worried", "mid")
            her @ tears soft "I don't understand why she feels the need to constantly spread rumours about me." ("annoyed", "base", "annoyed", "R")
            gen "(Look who's talking...)" ("base", xpos="far_left", ypos="head")

    her "You can tell that bitch to look for somebody else to commentate!" ("open", "base", "angry", "mid")
    her "Because I will not!" ("clench", "base", "angry", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    her "Good day, Sir." ("annoyed", "base", "annoyed", "R")

    #Hermione walks out
    call her_walk(action="leave")
    call bld

    gen "(What in the great desert sands do these women want from me...)" ("angry", xpos="far_left", ypos="head")
    gen "(Can't they get along like me and my ol' pal Snape?)" ("base", xpos="far_left", ypos="head")

    $ states.cho.ev.quidditch.e6_complete = True

    jump end_hermione_event

label cho_quid_E7:
    # Genie blackmails Hermione

    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "[name_hermione_genie], could I change your mind about your role in the Slytherin match?" ("base", xpos="far_left", ypos="head")
    her "My answer is still no, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "Come on!" ("angry", xpos="far_left", ypos="head")
    her "That's my final answer." ("annoyed", "narrow", "angry", "mid")
    gen "(This girl...)" ("base", xpos="far_left", ypos="head")
    gen "What if..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"I'll give you house points.\"":
            her "Not...{w=0.3} interested." ("annoyed", "narrow", "angry", "R")
            gen "But you're always eager for those points!" ("angry", xpos="far_left", ypos="head")
            her "No amount of points would be worth it." ("open", "base", "angry", "mid")
            gen "So, you don't even want to hear my offer?" ("base", xpos="far_left", ypos="head")
            her "I guess I don't..." ("open", "closed", "base", "mid") # upset
            gen "Your loss..." ("base", xpos="far_left", ypos="head")

        "\"You could make fun of those Slytherins.\"":
            if states.her.tier >= 5:
                her "I'm not that childish, [name_genie_hermione]." ("annoyed", "base", "base", "mid")
                gen "You're not?" ("base", xpos="far_left", ypos="head")
                gen "So what they're doing doesn't bother you? Calling you all sorts of names?" ("base", xpos="far_left", ypos="head")
                her "Not in the slightest..." ("soft", "narrow", "base", "mid")
                her @ cheeks blush "They can act like the usual dorks if they want to, that's no concern to me." ("soft", "base", "base", "R")
                her "But I have no reason to stoop down to their level." ("open", "closed", "base", "mid")
            else:
                her "And why would I want to do that? I'm not that foolish!" ("open", "base", "annoyed", "mid")
                her "Bad-mouthing their entire team would make me an even bigger target than I already am." ("annoyed", "base", "base", "R")
                her "Besides, I wouldn't really be able to mock them with a teacher present." ("open", "closed", "base", "mid")
                her "Madam Hooch would be unquestionably against that." ("open", "narrow", "base", "mid")

    gen "..." ("base", xpos="far_left", ypos="head")
    her "I won't step a foot on that podium, [name_genie_hermione]." ("open", "closed", "base", "mid")
    her "There's nothing you could tempt me with that would change my mind." ("soft", "narrow", "annoyed", "R")
    gen "Well then..." ("base", xpos="far_left", ypos="head")
    gen "No more mister nice guy..." ("angry", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("soft", "wink", "base", "mid")
    gen "[name_hermione_genie], you're going to commentate that match. Whether you like it or not." ("base", xpos="far_left", ypos="head")
    her "No! You can't change my mind on this!" ("annoyed", "base", "angry", "mid")
    gen "Are you sure about that?" ("grin", xpos="far_left", ypos="head")
    her "Why?" ("annoyed", "narrow", "angry", "mid") # suspicious

    menu:
        gen "[name_hermione_genie]..." ("grin", xpos="far_left", ypos="head")
        "\"I heard Cho has a crush on you!\"":
            $ d_flag_01 = True
            her "She has a--{w=0.5} What?" ("open", "wide", "base", "stare")

        "\"I heard you have a crush on Cho!\"":
            $ d_flag_01 = False
            her "But--{w=0.3} That's not true!" ("open", "wide", "base", "mid")

    her "That's a lie!" ("clench", "base", "angry", "mid") # angry
    her "Not even Cho would agree to this!" ("open", "base", "angry", "mid")
    gen "Why don't we ask her?" ("grin", xpos="far_left", ypos="head")
    her "What?" ("angry", "base", "base", "mid")
    her "[name_genie_hermione], you can't do this!" ("open", "base", "angry", "mid")
    gen "Sure I can." ("grin", xpos="far_left", ypos="head")

    call hide_characters
    nar "You telepathically call Cho into your office."

    if states.her.tier < 4: # Hermione changes into her school outfit
        nar "While Hermione hastily puts on some less revealing clothes."
        $ her_outfit_last.save()
        $ hermione.equip(her_outfit_default)
    else:
        $ hermione.wear("all")


    # Summon Cho.
    call cho_walk(action="enter")
    pause 1

    call cho_walk(680, "base")
    pause .2

    call her_walk("mid", "base")
    call chibi_emote("thought", "hermione")
    with d3
    pause .8
    call chibi_emote("hide", "hermione")
    with d3

    her "" ("annoyed", "base", "angry", "R", xpos=270, ypos="base", flip=True)
    cho "Hello, Sir." ("base", "base", "base", "mid", xpos="close", ypos="base")
    cho "Granger." ("soft", "narrow", "base", "L")
    her @ cheeks blush "..." ("annoyed", "base", "angry", "mid")
    cho "How can I be of help?" ("base", "base", "base", "mid")
    gen "I have some very good news for you, Miss Chang." ("base", xpos="far_left", ypos="head")
    gen "Miss Granger and I were just discussing who should commentate the next Squidditch game." ("base", xpos="far_left", ypos="head")
    cho "Oh, am I sensing a blackmail situation?" ("crooked_smile", "base", "base", "mid")
    her "Blackmailing?!{w=0.5} Me?" ("open", "wide", "base", "stare") # shocked
    cho "" ("annoyed", "narrow", "base", "L")
    gen "What other choice do we have? You're acting stubborn, Miss Granger." ("base", xpos="far_left", ypos="head")
    her "So that's what's going on here. You two are scheming against me!" ("angry", "base", "angry", "mid") # angry
    cho "Come on, Hermione. You can't be {b}that{/b} scared of those Slytherins..." ("open", "narrow", "raised", "L")
    cho "Don't be such a coward..." ("annoyed", "narrow", "angry", "L")
    her @ cheeks blush "I am not!" ("annoyed", "base", "angry", "R")
    cho "Please! We need somebody to commentate." ("upset", "narrow", "base", "L")
    her "I won't do it! And neither of you can change my mind on this!" ("angry", "base", "angry", "mid")
    gen "I bet she can!" ("grin", xpos="far_left", ypos="head")
    cho "Me? How so?" ("annoyed", "base", "raised", "mid")

    if d_flag_01: # Cho has crush
        gen "Miss Chang, I've heard rumours that you have a huge crush on Hermione..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "What? That's rubbish!" ("open", "narrow", "angry", "mid")
        her "..." ("annoyed", "base", "angry", "mid")

    else: # Hermione has crush
        gen "Miss Chang, I've heard rumours that Hermione secretly has a crush on you..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "She does?" ("soft", "base", "raised", "mid") # Surprised
        her "No, I don't!" ("clench", "happyCl", "angry", "mid")
        her "It's just made up rubbish..." ("open", "base", "angry", "mid")

    gen "Rubbish or not, I'm sure Miss Granger wouldn't want such rumours to make their rounds now, would she?" ("grin", xpos="far_left", ypos="head")
    cho "" ("annoyed", "base", "raised", "L")
    her "*Pfff*...{w=0.3} As if anybody would believe that..." ("annoyed", "base", "angry", "R")
    cho "Oh, I get it now!" ("base", "base", "base", "mid")
    her "" ("annoyed", "narrow", "angry", "L")
    cho "You can count on me, Sir!" ("crooked_smile", "base", "base", "mid")
    cho "I don't mind if my reputation gets a bit tarnished, from being associated with her." ("open", "narrow", "angry", "L")
    cho "For as long as it gets me closer to that cup..." ("base", "narrow", "base", "mid")
    her "You're such an idiot..." ("clench", "happyCl", "angry", "mid")
    her "I can't believe you'd stoop as low as blackmail for some stupid Quidditch Cup!" ("open", "narrow", "angry", "L")

    if d_flag_01: # Cho has crush
        cho "Don't be mean to me, Hermione." ("soft", "base", "base", "L")
        cho "After all, I really, really like you!" ("base", "narrow", "base", "L")
        her "..." ("annoyed", "narrow", "angry", "R") # looks away
        cho "I love your bushy hair, your cute little nose, your gorgeous eyes..." ("soft", "narrow", "raised", "L")
        cho "Your enormous rack!" ("grin", "narrow", "angry", "L")
        her @ cheeks blush "*Tzzzs*!" ("clench", "closed", "angry", "mid") # Starts to blush
        her @ cheeks blush "Stop lying!" ("open", "base", "angry", "L")
        cho @ cheeks blush "" ("horny", "narrow", "angry", "L")
        gen "She sounds pretty convincing to me..." ("base", xpos="far_left", ypos="head")
        cho "Everybody will know that I have a thing for you, Granger!" ("open", "narrow", "angry", "L")
        cho "And, sooner or later, I might even mix in some love potion into your pumpkin juice..." ("soft", "narrow", "raised", "L")
        her @ cheeks blush "You'd...{w=0.5} do what?" ("clench", "wide", "worried", "stare")
        gen "(Pumpkin juice? Sounds disgusting.)" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "You wouldn't want all of your friends to see us finally make out, would you?" ("horny", "narrow", "raised", "L")

    else: # Hermione has crush
        cho "Tell me, Granger..." ("soft", "narrow", "raised", "L")
        cho "What exactly do you like about me?" ("base", "narrow", "angry", "L")
        her "" ("annoyed", "narrow", "angry", "L")
        cho "Is it my hair? Or my strong legs? Or my abs?" ("open", "narrow", "base", "down")
        cho "Would you like me to show you my body again, right now?" ("grin", "narrow", "base", "L")
        her "No, thanks." ("normal", "closed", "base", "mid")
        cho "I should mix in some drops of Veritaserum into your pumpkin juice, and ask you again..." ("annoyed", "narrow", "base", "L")
        cho "Maybe then you'll speak the truth... How you really think of me." ("annoyed", "narrow", "raised", "mid")
        her @ cheeks blush "You wouldn't!" ("clench", "base", "angry", "L")
        cho "Yes I would!" ("base", "narrow", "base", "L")
        gen "(Pumpkin juice? Sounds disgusting...)" ("base", xpos="far_left", ypos="head")
        cho "And I'll make sure that all your friends hear about it. Maybe I'll even let them watch!" ("open", "narrow", "angry", "L")

    her @ cheeks blush "Professor! You can't have her do that. That's insane!" ("clench", "happyCl", "worried", "mid")
    cho "" ("annoyed", "narrow", "base", "up")
    gen "That's all up to you, Miss Granger." ("base", xpos="far_left", ypos="head")
    gen "All you have to do is agree to commentate again." ("grin", xpos="far_left", ypos="head")
    her "All the matches!" ("clench", "base", "angry", "mid")
    cho "" ("annoyed", "narrow", "base", "L")
    gen "What?" ("base", xpos="far_left", ypos="head")
    her "I will commentate all the matches, the Gryffindor match as well! The one after this one, should Ravenclaw even get that far..." ("open", "base", "angry", "mid")
    cho "Oh no, you won't! You'd be all in favour of Gryffindor!" ("clench", "base", "angry", "L")
    her "Yes I would. And I'll make sure that you lose." ("base", "narrow", "base", "L")
    gen "Great... Finally, we can get on with this..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Wait!--" ("clench", "happyCl", "worried", "mid")
    gen "Miss Granger, you better keep to your word this time..." ("base", xpos="far_left", ypos="head")
    her "" ("base", "base", "base", "mid")
    cho @ cheeks blush "(...)" ("annoyed", "narrow", "angry", "L")
    gen "If you don't show up I'll take a hundred points away from Gryffindor!" ("grin", xpos="far_left", ypos="head")
    her "That's just typical of you!" ("annoyed", "narrow", "base", "mid")
    gen "Make sure to be present..." ("base", xpos="far_left", ypos="head")
    her "I will." ("annoyed", "narrow", "base", "L")
    gen "You are both dismissed..." ("base", xpos="far_left", ypos="head")
    her "..." ("base", "base", "base", "mid")

    call her_walk(action="leave")
    pause .2

    show screen blkfade
    with d3

    call cho_chibi("stand","mid","base")
    hide screen blkfade
    cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)
    gen "I'd say that was a success." ("base", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "R")

    if game.daytime:
        cho "Good day, Sir." ("open", "narrow", "angry", "mid")
    else:
        cho "Good night, Sir." ("open", "narrow", "angry", "mid")

    call cho_walk(action="leave")

    pause 1.0
    gen "(Quest complete!)" ("grin", xpos="far_left", ypos="head")

    $ states.cho.mood = 0

    $ states.her.busy = True
    $ states.cho.busy = True

    $ states.cho.ev.quidditch.e7_complete = True

    if states.cho.ev.quidditch.slytherin_training: # Finished practice match?
        $ states.cho.ev.quidditch.lock_training = True

    # Reset
    if states.her.tier < 4:
        $ hermione.equip(her_outfit_last) # Equip player outfit.

    jump main_room_menu

label cho_quid_E8:
    # Genie hangouts with Tonks, asks her for help with the Slytherins.

    gen "I wanted to ask you for a favour..." ("base", xpos="far_left", ypos="head")
    ton "Me? Selling a favour to you?" ("grin", "closed", "base", "mid", ypos="head", flip=False)
    ton "You sure you can afford me?" ("base", "base", "raised", "mid") #Horny
    gen "Not that kind of favour." ("base", xpos="far_left", ypos="head")
    ton "*Aww*..." ("annoyed", "base", "raised", "down")

    # Tell Tonks about Cho.
    gen "You know this {i}Quiddish{/i} sport the students play here?" ("base", xpos="far_left", ypos="head")
    ton "Quidditch?" ("upset", "base", "raised", "mid")
    gen "Close enough." ("base", xpos="far_left", ypos="head")
    gen "The next match is coming up, and I require your help with something." ("base", xpos="far_left", ypos="head")
    ton "Of course. What is it?" ("base", "base", "base", "mid")
    gen "There's this Asian girl..." ("base", xpos="far_left", ypos="head")
    ton "Cho Chang?" ("open", "base", "raised", "mid")
    gen "How did you--" ("base", xpos="far_left", ypos="head")
    gen "(Is she the {i}token Asian{/i} girl in this school?)" ("base", xpos="far_left", ypos="head")
    gen "Yes, the little Ravenclaw minx, correct." ("base", xpos="far_left", ypos="head")
    ton "Well, I figured you'd be talking about her - if it has to do with Quidditch." ("open", "base", "base", "R")
    gen "She's one of the girls I buy favours from." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "No way!" ("open_wide", "shocked", "shocked", "mid")
    ton @ hair horny "You got that little hotty--" ("horny", "base", "raised", "R")
    ton "*Ehm*... hot-head to sell you favours?" ("mad", "base", "raised", "R")
    gen "Once or twice..." ("base", xpos="far_left", ypos="head")
    ton "Impressive." ("horny", "base", "raised", "mid")
    ton "Tell me everything!" ("horny", "base", "angry", "mid")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-Tell her everything-":
            gen "She's been stripping for me." ("base", xpos="far_left", ypos="head")
            ton "Cho?! And I'm supposed to believe that?" ("upset", "wide", "raised", "mid")
            gen "Oh, you better believe it!" ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "Holy shit!" ("upset", "wide", "shocked", "stare")
            ton "I'd pay so much gold to watch that girl take her clothes off..." ("base", "base", "raised", "R")
            ton @ hair angry "You need to invite me next time!" ("annoyed", "base", "angry", "mid") # angry
            gen "And how would I get her to agree to that?" ("base", xpos="far_left", ypos="head")
            ton @ hair horny "Well... *Ehm*..." ("upset", "base", "worried", "down")
            gen "It was difficult enough to get her to strip just for me..." ("base", xpos="far_left", ypos="head")
            gen "She only did it because I helped her win against Hufflepuff." ("base", xpos="far_left", ypos="head")
            ton "So that was your idea with the skirt? Very clever." ("horny", "base", "annoyed", "mid")
            gen "Maybe I could arrange something once we've beaten those Slytherins..." ("base", xpos="far_left", ypos="head")
            gen "For the two of you." ("base", xpos="far_left", ypos="head")
            ton "Or all three of us!" ("soft", "base", "raised", "mid")
            gen "Yes!" ("grin", xpos="far_left", ypos="head")
            gen "I'm sure that minx would love that!" ("grin", xpos="far_left", ypos="head")
            ton "I can't wait!" ("base", "happyCl", "base", "mid")

        "-Don't tell her-":
            gen "I don't think I should..." ("base", xpos="far_left", ypos="head")
            ton "What? Why not?" ("open", "base", "worried", "mid")
            gen "Miss Chang wouldn't like anybody to know." ("base", xpos="far_left", ypos="head")
            ton "I can keep a secret!" ("upset", "base", "worried", "R")
            gen "I really shouldn't..." ("base", xpos="far_left", ypos="head")
            ton @ hair angry "Tell me, or I'll jinx your balls off!" ("upset", "base", "angry", "mid")
            gen "*Ghzzz!* Alright! Alright!" ("angry", xpos="far_left", ypos="head")
            gen "You sure know how to get me to talk..." ("base", xpos="far_left", ypos="head")

    # Talk about Slytherin.
    gen "I'm currently helping her with this Quidditch thing in exchange for favours." ("base", xpos="far_left", ypos="head")
    gen "But to get any further with her, I'll have to help her beat the opposing team in the next match." ("base", xpos="far_left", ypos="head")
    ton "Slytherin? That shouldn't be too difficult." ("open", "base", "raised", "mid")
    gen "Really? How so?" ("base", xpos="far_left", ypos="head")
    ton "Their tactics revolve around strength, brute force, and manifesting their dominance on the field!" ("open", "closed", "angry", "mid")
    ton "A good strategy for when you're in bed with your partner, but not in Quidditch." ("base", "base", "angry", "mid")
    gen "You don't say..." ("base", xpos="far_left", ypos="head")
    gen "Wait, what?" ("angry", xpos="far_left", ypos="head")
    ton "I've seen them play a couple of times. They clearly aren't the brightest bunch..." ("upset", "base", "annoyed", "R")
    ton "What tactics are you gonna use against them?" ("base", "base", "raised", "mid")
    gen "I shouldn't ruin the surprise." ("grin", xpos="far_left", ypos="head")
    ton "Can't wait... If it's anything like the first game." ("base", "base", "raised", "R")
    gen "The main hurdle right now is that I have no way to try out our tactics on the Slytherins..." ("base", xpos="far_left", ypos="head")
    gen "They refuse to practice against Ravenclaw." ("base", xpos="far_left", ypos="head")
    ton "Well that's unfortunate..." ("upset", "base", "shocked", "L")
    ton "Perhaps you could ask Snape. He should be able to get those lazy gits back on the pitch..." ("open", "base", "base", "mid")

    if states.cho.ev.quidditch.e9_complete:
        gen "I already did. He isn't going to help me out..." ("base", xpos="far_left", ypos="head")
        ton "Well, that's just like him." ("open", "base", "angry", "R")
    else:
        gen "I guess I could..." ("base", xpos="far_left", ypos="head")
        ton "Yeah, maybe not..." ("open", "closed", "base", "mid")

    ton "Just leave it to me, Genie." ("base", "base", "angry", "mid")
    ton "I'll get those shits back on the grass..." ("mad", "base", "angry", "mid")
    gen "And how will you accomplish that?" ("base", xpos="far_left", ypos="head")
    ton "Oh, don't you worry..." ("silly", "happyCl", "base", "mid")
    ton "Perhaps I'll tell you my techniques some other time." ("base", "narrow", "angry", "mid")

    gen "..." ("base", xpos="far_left", ypos="head")
    if not states.cho.ev.quidditch.e7_complete:
        # Has NOT blackmailed Hermione

        gen "That's not all, though. There's something else I need your help with." ("base", xpos="far_left", ypos="head")
        ton "You can't expect me to fix all of your problems, Genie." ("annoyed", "base", "base", "mid")
        gen "It's about Hermione's role as a commentator..." ("base", xpos="far_left", ypos="head")
        ton "Really? What happened to Miss Granger?" ("upset", "base", "worried", "mid")
        gen "She quit..." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... That's too bad..." ("open", "base", "worried", "R")
        ton "But it's understandable... Seeing that she had to go through all that mocking, during the last game." ("open", "base", "worried", "mid")
        ton "Poor thing..." ("mad", "base", "worried", "L")
        ton "Have you tried talking to her?" ("open", "base", "raised", "mid")
        gen "Not yet..." ("base", xpos="far_left", ypos="head")
        ton "Well, if anyone could convince her, surely you'd be the one to be able to." ("base", "base", "base", "R")
        gen "..." ("base", xpos="far_left", ypos="head")
        ton "Why don't you tell her that a very special someone will be really disappointed if she doesn't show up." ("horny", "base", "base", "stare")
        gen "(So it's not just me who thinks she's into Cho!)" ("grin", xpos="far_left", ypos="head")
        ton "(She was so cute fumbling over her words...)" ("base", "happyCl", "base", "mid")
        ton "I'm sure you'll be able to change her mind." ("base", "base", "base", "mid")
    else:
        gen "Did you know Hermione wanted to quit her task as a commentator?" ("base", xpos="far_left", ypos="head")
        ton "Did she now? I thought she did well in the Hufflepuff game." ("upset", "base", "raised", "mid")
        ton "A bit wooden, but not bad for her first try." ("open", "base", "base", "R")
        ton "Speaking in front of such a large crowd and all." ("open", "base", "raised", "mid")
        ton "I thought it was rather cute listening to her fumble her words..." ("base", "happyCl", "base", "mid")
        ton "What changed her mind?" ("base", "base", "base", "mid")
        gen "Cho helped me convince her to do it." ("base", xpos="far_left", ypos="head")
        ton "Really? How?" ("open", "base", "raised", "mid")
        ton "I'd love to hear it." ("horny", "base", "angry", "mid")
        gen "*Hmm*... Maybe next time." ("base", xpos="far_left", ypos="head")
        ton "Very well..." ("upset", "base", "worried", "R")

    ton "In any case, I could join you in the commentator booth during the next game to help encourage Miss Granger." ("open", "base", "base", "mid")
    ton "If anything, I'll get a nice view from up there." ("grin", "happyCl", "base", "mid")
    ton "Since you already made sure Hufflepuff is out of the competition..." ("upset", "base", "raised", "R")
    ton "The best we can hope for now is to not get last..." ("open", "closed", "base", "mid")
    ton "It's always third or nothing with us Puffs." ("open", "base", "worried", "R")
    gen "(Puffs?)" ("base", xpos="far_left", ypos="head")

    gen "Well, I'd be happy to have you." ("grin", xpos="far_left", ypos="head")
    ton "*N'Aww*, you're so sweet!" ("base", "base", "worried", "mid")
    with hpunch
    play sound "sounds/hiccup_fem.ogg"
    ton "*Hick*!... whoopsie..." ("upset", "wide", "base", "mid")
    ton @ hair horny "Now, I better get going convincing those boys to play again..." ("open", "base", "raised", "R")

    if game.daytime:
        nar "You finish your drinks before calling it a day."
    else:
        nar "You finish your drinks before calling it a night."

    $ states.ton.busy = True
    $ states.cho.ev.quidditch.e8_complete = True
    $ states.cho.ev.quidditch.lock_practice = False
    $ states.cho.ev.quidditch.slytherin_prepared = True # Unlocks practice match

    jump end_tonks_hangout_points

label cho_quid_E9:
    # Ask Snape for help, but it backfires (optional)

    sna "Your precious Ravenclaw bird, made any breakthroughs with her yet?" ("snape_37", ypos="head")
    gen "The little Asian?" ("base", xpos="far_left", ypos="head")
    sna "Yes, Miss Chang." ("snape_40")
    gen "..." ("base", xpos="far_left", ypos="head")
    sna "I wish her best of luck against my team of Slytherins." ("snape_02")
    sna "She'll need it." ("snape_45")
    gen "What kind of game are you playing?" ("angry", xpos="far_left", ypos="head")
    sna "I'm sorry?" ("snape_38")
    gen "Your team didn't show up for practice against Ravenclaw!" ("base", xpos="far_left", ypos="head")
    sna "Well, there's no specific rule that forces the teams to practise against each other..." ("snape_05")
    gen "There's not?" ("base", xpos="far_left", ypos="head")
    gen "(Actually, that does make sense...)" ("base", xpos="far_left", ypos="head")
    sna "Of course not, but it is heavily encouraged for students that are looking to make it professionally." ("snape_09")
    gen "Do you have something to do with this?" ("base", xpos="far_left", ypos="head")
    sna "I don't know what you're talking about..." ("snape_47") #Smirk
    gen "You little weasel..." ("angry", xpos="far_left", ypos="head")
    sna "Ha! Do you have another trick up your sleeve?" ("snape_20")
    sna "What's it gonna be? An even shorter skirt? Prohibit her from wearing panties?" ("snape_13")
    sna "Well, we'll see during the game if it has any effect..." ("snape_46")
    gen "*Grrrrr*!..." ("angry", xpos="far_left", ypos="head")
    gen "Get your team back on that pitch, you coward!" ("angry", xpos="far_left", ypos="head")
    sna "No... I don't think I will..." ("snape_41")
    gen "Give me that wine!" ("angry", xpos="far_left", ypos="head")
    sna "You want some?" ("snape_20")
    play sound "sounds/spit.ogg" # Spits in the cup
    sna "..." ("snape_40")
    gen "I'm gonna win that bet. Then I'll have the last laugh!" ("base", xpos="far_left", ypos="head")
    sna "I wish you good fortune." ("snape_22")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Get your wine from some place else, you slacker." ("angry", xpos="far_left", ypos="head")
    sna "You won't win by making friends, isn't that right?" ("snape_18")
    gen "..." ("base", xpos="far_left", ypos="head")
    sna "*Hrhm*... Good riddance, then..." ("snape_12")
    play sound ["sounds/gulp.ogg"]*3
    nar "Snape empties the last drop of wine, before leaving."
    nar "You feel a sense of remorse shortly after he's gone, realizing that you're both just parts of the same coin."
    nar "Your friendship level with him has not changed...{w=0.5} Probably..."

    $ states.sna.busy = True
    $ ss_summon_pause = 5 # Snape can't be summoned for a couple of days. Can be set to 0 once you talked to Tonks.

    $ states.cho.ev.quidditch.e9_complete = True

    $ chair_OBJ.hidden = False

    jump end_snape_hangout_no_points

label cho_quid_E10:
    # Introduction to Gryffindor team.

    call cho_walk("mid", "base", action="enter")

    if game.daytime:
        cho "Good morning, [name_genie_cho]..." ("open", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
        gen "Good morning [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    else:
        cho "Good evening, [name_genie_cho]..." ("open", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
        gen "Good Evening [name_cho_genie]." ("base", xpos="far_left", ypos="head")

    gen "Ready to continue your training and take on those Griffins?" ("base", xpos="far_left", ypos="head")
    cho "Griffins, [name_genie_cho]?" ("soft", "base", "raised", "mid")
    gen "Yeah! Aren't they the next team we're up against?" ("base", xpos="far_left", ypos="head")
    cho "Oh, you mean the Gryffindor team." ("soft", "base", "base", "mid")
    gen "Yeah, the doors!" ("base", xpos="far_left", ypos="head")
    cho "*Sigh*." ("base", "narrow", "raised", "downR")
    gen "Ready to knock those doors down?" ("base", xpos="far_left", ypos="head")
    cho "Always, if it means I get to take that smug look off of Granger's face." ("smile", "base", "base", "mid")
    gen "Great, then tell me what you know about their team." ("base", xpos="far_left", ypos="head")
    cho "Sure thing, what would you like to know?" ("base", "base", "base", "mid")
    gen "What makes them different to the other teams? Can we expect similar tactics like with the Slytherbins?" ("base", xpos="far_left", ypos="head")
    cho "Oh, no... They're the polar opposite to the Slytherin team." ("soft", "base", "base", "mid")
    gen "Figures." ("base", xpos="far_left", ypos="head")
    gen "So what's their shtick then?" ("base", xpos="far_left", ypos="head")
    cho "They use tactics and coordination!" ("soft", "base", "base", "mid")
    gen "What?! There are tactics in this game?" ("angry", xpos="far_left", ypos="head")
    cho "They're also quite a bit more nimble than the Slytherin team, so they got hit by way fewer bludgers than we did." ("open", "base", "base", "mid")
    cho "Some of the hits they pulled off during the last game had my teammates covered in bruises for days!" ("soft", "narrow", "angry", "downR")
    cho "Would've been weeks if it wasn't for Madam Pomfrey." ("open", "closed", "angry", "mid")
    gen "*Hmm*... Well, hopefully we won't see that kind of meddling from Snape this time around." ("base", xpos="far_left", ypos="head")
    cho "Snape?! What has Professor Snape got to do with it?" ("angry", "base", "base", "mid")
    gen "He provided them with a felix potion... Thing, before the game." ("base", xpos="far_left", ypos="head")
    cho "Felix Felicis!?" ("clench", "wide", "base", "mid")
    gen "That's the one." ("base", xpos="far_left", ypos="head")
    cho "But that's against the rules!" ("disgust", "base", "angry", "mid")
    gen "It is?" ("base", xpos="far_left", ypos="head")
    cho "Of course it is..." ("angry", "base", "angry", "mid")
    cho "To think Professor Snape would go as far as giving them a luck potion!" ("angry", "narrow", "angry", "downR")
    gen "You won the match did you not? Even despite the fact they drank that thing." ("base", xpos="far_left", ypos="head")
    cho "If the department of magical games and sports heard about this, there's no way those Slytherins would have any chance at--" ("angry", "closed", "angry", "mid")
    gen "[name_cho_genie]..." ("base", xpos="far_left", ypos="head")
    cho "What? It's true!" ("clench", "narrow", "base", "mid")
    gen "Achieving true success isn't about bringing other people down, but to raise yourself above others." ("base", xpos="far_left", ypos="head")
    gen "(In her case, quite literally...)" ("base", xpos="far_left", ypos="head")
    cho "..." ("disgust", "base", "base", "mid")
    cho "No offence [name_genie_cho] but I must say I've never heard such nonsense in my life." ("disgust", "narrow", "angry", "mid")
    cho "I only care about reaching the top, no matter what!" ("open", "closed", "angry", "mid")
    gen "Very well [name_cho_genie]... If that's the case, then I'm not sure if I can help you any further." ("base", xpos="far_left", ypos="head")
    cho "What?!" ("angry", "base", "base", "mid")
    cho "But [name_genie_cho], I still want you-- I still need your help!" ("mad", "narrow", "base", "mid")
    gen "Then you shouldn't bite the hand that feeds you." ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho]?" ("disgust", "base", "base", "mid")
    gen "Do you think Severus and the Slytherins would be the only ones in trouble if you contacted some ministry employee?" ("base", xpos="far_left", ypos="head")
    cho "..." ("normal", "narrow", "base", "downR")
    gen "I thought that I was doing you a favour by coaching you... Some way to repay me for my time." ("base", xpos="far_left", ypos="head")
    cho "I--{w=0.4} I suppose I didn't think that far [name_genie_cho]..." ("clench", "narrow", "base", "downR")
    gen "For this to work and for you to receive my continued help, you need to remember who got you this far..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Right..." ("disgust", "narrow", "base", "down")
    gen "Well then, let's show them who the greatest snatch catcher is!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes [name_genie_cho]!" ("soft", "narrow", "base", "mid")

    #Unlock Personal favours (Public locked)
    $ states.cho.ev.quidditch.e10_complete = True
    $ states.cho.favors_unlocked = True

    jump cho_requests

label cho_quid_E11:
    # Ask Luna to cheer for Ravenclaw (She cheers for Gryffindor, the bimbo!)

    gen "[name_luna_genie], there's something I have been meaning to ask." ("base", xpos="far_left", ypos="head")
    lun "Yes, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "I require your assistance with something..." ("base", xpos="far_left", ypos="head")
    lun "Assistance? You need my help, [name_genie_luna]?" ("open", "base", "raised", "mid")
    gen "Yes, it's about the upcoming Quidditch finals." ("base", xpos="far_left", ypos="head")
    lun "Oh, right... Yes, that is an issue for sure." ("open", "narrow", "base", "down")
    gen "I haven't even told you what the problem is..." ("base", xpos="far_left", ypos="head")
    lun "Oh... Sorry, [name_genie_luna]... Go on." ("angry", "base", "base", "mid")
    gen "Well, I've been looking into setting up a cheerleading squad." ("base", xpos="far_left", ypos="head")
    lun "Cheerleading?" ("soft", "base", "base", "mid")
    gen "Yes I--" ("base", xpos="far_left", ypos="head")
    gen "Are you asking what it is, or just confirming what I just said?" ("base", xpos="far_left", ypos="head")
    lun "Oh, of course I know what it is! It's students who dress up and cheer for the players, right?" ("grin", "base", "base", "mid")
    gen "That's right..." ("base", xpos="far_left", ypos="head")
    lun "..." ("base", "base", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "So.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} Is that something you could help me with?" ("base", xpos="far_left", ypos="head")
    lun "Oh, you want me to cheer at the finals?!" ("mad", "base", "base", "mid")
    gen "Yes... And your friends as well." ("base", xpos="far_left", ypos="head")
    gen "{size=-8}If you have any to begin with...{/size}" ("base", xpos="far_left", ypos="head")
    lun "I could hear some mumbling, was that you [name_genie_luna]?" ("angry", "base", "base", "stare")
    gen "No, it was--" ("base", xpos="far_left", ypos="head")
    lun "A ghytrash? Maybe a phantom rat?" ("angry", "base", "base", "stare")
    gen "A phantom rat-- what--" ("base", xpos="far_left", ypos="head")
    gen "Girl, you're losing my patience..." ("angry", xpos="far_left", ypos="head")
    lun "I could prepare a skurge charm to--" ("mad", "base", "base", "mid")
    gen "I'll handle it, don't worry about it..." ("base", xpos="far_left", ypos="head")
    gen "I'd still like to ask you to cheer in the upcoming Quidditch match, would you agree?" ("base", xpos="far_left", ypos="head")
    lun "Oh, yes [name_genie_luna], I'd be happy to!" ("angry", "base", "base", "mid")
    gen "Are you sure?" ("base", xpos="far_left", ypos="head")
    lun "Of course, [name_genie_luna]!" ("grin", "base", "base", "mid")
    gen "Great. Then I'll look forward to seeing you cheering at the game!" ("base", xpos="far_left", ypos="head")

    $ states.cho.ev.quidditch.e11_complete = True

    call lun_walk(action="leave")

    pause 1.0

    # Normally we allow the player to pick favours, but Luna is being Luna.
    gen "... Did she just leave?" ("base", xpos="far_left", ypos="head")
    gen "I guess they don't call her Loony Luna for nothing..." ("base", xpos="far_left", ypos="head")

    jump end_luna_event

label cho_quid_E12:

    # Genie visits cho during her training as requested

    $ game.weather = "clear"

    gen "*Yawn*..." ("base", xpos="far_left", ypos="head")
    gen "I can't believe she made me wake up this early..." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", 225, "base")
    with d3

    pause .4
    call gen_walk(path=[(230, 470), (410, 470), (417, 426)])

    pause .4
    call gen_chibi("stand_alt", flip=False)
    with d3

    pause .4
    #Genie chibi either walks around desk or teleports next to bird facing the window

    play sound "sounds/MaleGasp.ogg"
    gen "What in the great desert sand is that!?" ("angry", xpos="far_left", ypos="head")

    gen "Oh wait... That's the sun... Never seen it this low before." ("base", xpos="far_left", ypos="head")
    gen "Alright then... Better go help her find a broom." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", flip=True)
    with d3
    pause .3

    #Genie leaves the office
    call gen_walk(action="leave")

    show screen blkfade
    with d5

    stop music fadeout 1
    play sound "sounds/steps_grass.ogg"
    nar "You make your way down to the pitch, catching a few stares on the way from some of the portraits. It appears the real Dumbledore may not have been a morning person either."

    #Pitch entrance, Cho is standing there
    call room("quidditch_pitch")
    play background "sounds/outskirts.ogg" fadein 2
    call gen_chibi("stand", "left", "base", flip=True)
    call cho_chibi("stand", "right", "base", flip=False)

    hide screen blkfade
    with d5

    call gen_walk(xpos="mid")

    gen "Alright then, let's find you a broom to use so we can finally be done--" ("base", xpos="far_left", ypos="head")
    cho "Where have you been?" ("disgust", "base", "angry", "mid", xpos=460, ypos="base", trans=d3)
    gen "*Err*...{w=0.4} In my office?" ("base", xpos="far_left", ypos="head")
    cho "It's ten AM! I've already been here for the past five hours!" ("soft", "base", "angry", "mid")
    gen "You've been here since six AM?" ("angry", xpos="far_left", ypos="head")
    cho "Five AM!" ("scream", "closed", "angry", "mid")
    gen "Then where are the brooms?" ("base", xpos="far_left", ypos="head")
    cho "I put them in the cleaning supply closet where they belong." ("disgust", "narrow", "angry", "mid")
    cho "They were all terrible, I tried every single one, and they're even worse than my family's bluebottle!" ("open", "narrow", "angry", "R")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "So the broom makes the player, does it?" ("base", xpos="far_left", ypos="head")
    cho "Yes!" ("mad", "narrow", "base", "mid")
    cho @ cheeks blush "I mean no!" ("clench", "narrow", "base", "mid")
    cho @ cheeks blush "But you still need a broom that is made to be used professionally." ("annoyed", "narrow", "base", "mid")
    gen "And they all just happen to cost a lot of money?" ("base", xpos="far_left", ypos="head")
    cho "That's Quidditch for you." ("open", "closed", "base", "mid")
    gen "Sounds like pay to win to me..." ("base", xpos="far_left", ypos="head")
    gen "Can't you just borrow a broom from one of the other players?" ("base", xpos="far_left", ypos="head")
    cho "...{w=0.4} What do you mean by \"other players\"?" ("disgust", "narrow", "base", "mid")
    gen "What about that greasy haired blond fella?" ("base", xpos="far_left", ypos="head")
    cho "Malfoy?" ("disgust", "wide", "base", "mid")
    gen "Yeah, him! Or that guy you dated?" ("base", xpos="far_left", ypos="head")
    cho "Are you seriously expecting that any of them would lend me their broom?" ("angry", "narrow", "base", "mid")
    cho "After the stunts I pulled to win the games against them?" ("angry", "base", "base", "mid")
    gen "What about the teachers then?" ("base", xpos="far_left", ypos="head")
    cho "Teachers..." ("open", "narrow", "base", "down")
    cho "The only teacher that would own a proper Quidditch approved broom is Madam Hooch, and she'll be using it during the game." ("open", "narrow", "base", "downR")
    gen "Madam Who?" ("base", xpos="far_left", ypos="head")
    cho "{size=+5}Madam Hooch!{/size}" ("open", "base", "base", "mid") #yelling
    femv "One moment!"

    hide cho_main
    hide screen bld1
    with d3

    #Hooch chibi comes down the commentator booth stairs (Or left stairs) and stands next to genie (Genie in the middle of the two girls)

    $ hooch_chibi.zoom = 0.38
    $ hooch_chibi.zorder = 4

    chibi hooch move(path=[(50, 460), (200, 520), (450, 500)])

    pause 1.5
    call gen_chibi(flip=False)
    with d3

    pause 1.0

    gen "(Mamma mia!)" ("grin", xpos="far_left", ypos="head")

    #Hooch theme
    play music "music/march-of-the-spoons-by-kevin-macleod-from-filmmusic-io.ogg" fadein 1 fadeout 1 if_changed

    #Hooch doll fades in
    hoo "Professor Dumbledore, Miss Chang, what can I do you for?" ("base", "base", "base", "L", xpos=100, ypos="base", flip=True, trans=d3) # "what can I do you for" is a form of a joke, fits next line perfectly.
    gen "Me..." ("base", xpos="far_left", ypos="head")
    hoo "Sorry?" ("open", "base", "base", "L")
    gen "Oh...{w=0.4} *Err*...{w=0.4} Miss Chang here is looking for a broom to use for the final Quidditch match." ("base", xpos="far_left", ypos="head")
    hoo "A broom eh?" ("normal", "base", "raised", "L")
    hoo "So that's why I saw you bobbing around on the school training brooms." ("grin", "shocked", "shocked", "L")
    hoo "We use those for cleaning you know." ("base", "narrow", "base", "L")
    cho "See! I told you, sir!" ("mad", "narrow", "base", "mid", trans=d3)
    gen "..." ("base", xpos="far_left", ypos="head")
    hoo "Certainly a good enough tool to teach students how to fly, but not much beyond that." ("base", "base", "base", "L")
    hoo "If you learn how to fly on one of those, you'll have no problem on a proper broomstick!" ("base", "base", "shocked", "mid")
    cho "" ("annoyed", "narrow", "base", "mid")
    gen "The motto for any public school when funds are involved." ("base", xpos="far_left", ypos="head")
    hoo @ cheeks blush "*Ahem*... Yes indeed, always the blunt one, Professor." ("open", "closed", "base", "mid")
    hoo "So, what's the situation then? Lost your broom?" ("normal", "base", "raised", "L")
    hoo "I thought you would've been taught accio by now, Miss Chang?" ("normal", "base", "shocked", "L")
    cho "No, that's not it... I've been able to summon my broom for a long time." ("angry", "closed", "base", "L")
    cho "The problem...{w=0.4} Is those stupid twins!" ("angry", "closed", "angry", "mid")
    hoo "Right?" ("open", "narrow", "raised", "L")
    cho "Can't even look away for a second...{w=0.4} To think they'd care so little about the sport--" ("clench", "narrow", "angry", "down")
    gen "{size=-6}*Ahem*... Apparently they put some kind of bug on her broom.{/size}" ("base", xpos="far_left", ypos="head") #small text whispering to hooch
    hoo "{size=-6}Espionage?{/size}" ("open", "shocked", "shocked", "mid") #small text
    gen "{size=-6}Termites...{/size}" ("base", xpos="far_left", ypos="head") #small text
    hoo "{size=-6}I see...{/size}" ("normal", "narrow", "base", "mid") #small text
    cho "The audacity! I couldn't believe--" ("angry", "closed", "angry", "mid")
    gen "{size=-6}And she's been quite the handful ever since...{/size}" ("base", xpos="far_left", ypos="head") #small text
    cho @ cheeks blush "They should be banned from ever participating--" ("upset", "closed", "angry", "mid")
    gen "{size=-6}More than usual that is...{/size}" ("base", xpos="far_left", ypos="head") #small text
    gen "Please... Help me..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Azkaban--" ("mad", "happyCl", "angry", "mid")
    hoo "Calm down Miss Chang." ("open", "shocked", "angry", "L")
    cho @ cheeks blush "I need a broom that is as fast as Harry's!" ("angry", "narrow", "angry", "downR")
    hoo "A firebolt? Now don't you think those expectations are a bit high, Miss--" ("open", "shocked", "shocked", "L")
    cho "Please professor, you're my only hope!" ("mad", "narrow", "base", "L")
    hoo "..." ("normal", "narrow", "base", "downR")
    hoo "Well, I'd normally be able to pull some strings, but I don't think even I would be able to procure you a firebolt, Miss Chang..." ("open", "base", "base", "down")
    hoo "There's only so many produced each season, and only a couple have been sold outside of professional--" ("normal", "base", "base", "down")
    cho "Pleaaaaaase!" ("soft", "narrow", "worried", "L")
    hoo "..." ("normal", "narrow", "worried", "downR")

    #Hooch turns to genie

    gen "{size=-6}Are you sure there's nothing you could do?{/size}" ("base", xpos="far_left", ypos="head") #small text
    hoo "{size=-6}*Hmm*...{/size}" ("normal", "narrow", "base", "down")  #small text
    hoo "{size=-6}Considering how she achieved her previous wins this season...{/size}" ("normal", "base", "raised", "down") #small text
    hoo "{size=-6}Maybe it's finally time to pass it down...{/size}" ("base", "base", "raised", "R")  #small text
    gen "{size=-6}Her previous--{/size}" ("base", xpos="far_left", ypos="head")  #small text

    #Hooch turns back to Cho

    hoo "Miss Chang." ("open", "base", "angry", "L")
    hoo "I think I've got just the broom for you." ("base", "shocked", "angry", "L")
    cho "Yes! Thank you, Professor!" ("crooked_smile", "base", "base", "L")
    hoo "A broom, that when used by the right person could be faster and even more agile than the firebolt." ("base", "shocked", "shocked", "L")
    cho "Thank you so--" ("smile", "closed", "base", "mid")
    cho "Wait...{w=0.4} Faster than the firebolt?! But that's the best broom out there!" ("disgust", "wide", "base", "mid")
    hoo "Yes girl, you heard me right." ("open", "shocked", "base", "L")
    hoo "Now, I'll give you this broom... But you're going to have to promise me..." ("base", "shocked", "base", "L")
    hoo "Promise me!" ("open", "shocked", "angry", "L")
    hoo "Don't ever tell a soul what I'm about to show you..." ("normal", "shocked", "base", "L")
    cho "Oh, of course, professor!" ("angry", "base", "base", "L")
    hoo "And that goes for you as well, Professor..." ("open", "base", "shocked", "mid")
    gen "Of course, but what exactly--" ("base", xpos="far_left", ypos="head")
    hoo "Alright then, one moment..." ("grin", "base", "base", "R")
    gen "Hold on, this isn't a broom from some black market brooms dealer, is it?" ("base", xpos="far_left", ypos="head")
    hoo "Don't be silly, of course not." ("base", "base", "base", "mid")
    hoo "You can inspect it if you like." ("base", "base", "base", "mid")
    hoo "{size=-6}Coach...{/size}" ("base", "wink", "raised", "mid") #small text #blush #smirkyface
    gen "{size=-6}How did you--{/size}" ("base", xpos="far_left", ypos="head") #Small text
    gen "{size=-6}Tonks...{/size}" ("base", xpos="far_left", ypos="head") #Small text
    hoo "Anyhow, one moment please..." ("base", "base", "base", "mid")

    #Hooch starts walking
    #Fades to black
    #Hooch Chibi gone
    #Fades back
    #Some time later
    #Hooch comes back holding broom (No dildo)

    chibi hooch move (path=[(450, 500), (200, 520), (50, 460)])

    hide screen bld1
    hide hooch_main
    hide cho_main
    with d3

    pause 1.0

    call gen_chibi(flip=True)
    with d3

    pause 0.5

    gen "Told you I'd get it sorted."
    cho "..."

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}A few moments later...{/color}{/size}"

    call gen_chibi(flip=False)
    hide screen blkfade
    with d5

    pause 0.5

    chibi hooch move (path=[(50, 460), (200, 520), (450, 500)])

    pause 1.0

    hoo "Sorry about that... Had to go through quite a few protective charms to take it out." ("base", "base", "base", "mid", trans=d3)
    hoo "Here we are..." ("base", "base", "base", "downR")
    cho "Ooooh!" ("open", "wide", "base", "L")
    cho "This...{w=0.4} This is the broom of The Masked Seeker!" ("angry", "wide", "base", "L")
    gen "The what?" ("base", xpos="far_left", ypos="head")
    gen "(I swear it looks the same as the broom she had moments ago...)" ("base", xpos="far_left", ypos="head")
    hoo "Ah, yes... It's been a while since somebody called me that..." ("base", "narrow", "shocked", "L")
    cho "I can't believe it... To think that our teacher was The Masked Seeker all this time!" ("open", "wide", "base", "L")
    cho "How do you not know about her, sir?" ("angry", "narrow", "base", "mid")
    menu:
        "-Throw the question back at her-":
            gen "{i}\"How do you not know about her, sir?\"{/i}" ("base", xpos="far_left", ypos="head")
            cho "What?" ("disgust", "narrow", "base", "mid")
            gen "Err... What I meant to say..." ("base", xpos="far_left", ypos="head")
            cho "*Rolls eyes*" ("soft", "narrow", "base", "R")
        "-Blame her-":
            gen "It's your fault my memory is so bad." ("base", xpos="far_left", ypos="head")
            cho "What?!" ("angry", "base", "base", "mid")
            cho "How does that make any sense..." ("disgust", "narrow", "angry", "mid")
            gen "Who are you again?" ("base", xpos="far_left", ypos="head")
            cho "..." ("disgust", "narrow", "base", "mid")
        "-Distract her-":
            gen "Look! A squirrel!" ("base", xpos="far_left", ypos="head")
            cho "... I'm not a dog, sir." ("disgust", "narrow", "base", "mid")
            cho "I know what you're trying to do." ("annoyed", "narrow", "angry", "mid")
            gen "... What was that mister squirrel? You want to know about the masked seeker?" ("base", xpos="far_left", ypos="head")
            cho "*Rolls eyes*" ("disgust", "narrow", "base", "R")
            gen "You heard the squirrel." ("base", xpos="far_left", ypos="head")
        "-Pretend like you misheard her-":
            gen "Oh, the masked seeker! I thought you said, the masked streaker... You should really learn how to speak up." ("base", xpos="far_left", ypos="head")
            cho "... You actually don't know, do you?" ("disgust", "narrow", "base", "mid")
            gen "Of course I do..." ("base", xpos="far_left", ypos="head")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Although a reminder wouldn't hurt." ("base", xpos="far_left", ypos="head")
        "-Blame the Quidditch guidebook-" if quidditchguide_ITEM.used:
            gen "Err..." ("base", xpos="far_left", ypos="head")
            gen "I must've missed that section in the Quidditch guide." ("base", xpos="far_left", ypos="head")
            cho "Her list of accomplishments required a whole book, it said so in the footnotes!" ("disgust", "narrow", "base", "mid")
            gen "People read those?" ("base", xpos="far_left", ypos="head")
    cho "She was a legendary seeker, the speed and precision of her flying was unmatched." ("angry", "closed", "base", "mid")
    cho "Nobody ever managed to figure out her identity or how she managed to fly so well." ("soft", "narrow", "base", "L")
    hoo "You sure know your Quidditch history Miss Chang, ten points to Ravenclaw." ("grin", "base", "base", "L")
    $ ravenclaw += 10
    cho "And then...{w=0.4} And then...{w=0.4} You disappeared, and became a teacher?" ("soft", "base", "raised", "L")
    hoo "Yes indeed." ("base", "shocked", "base", "L")
    cho "Wow...{w=0.4} I can't believe it." ("soft", "base", "base", "mid")
    cho "Why?" ("upset", "base", "raised", "L")
    hoo "Sorry?" ("open", "shocked", "raised", "L")
    cho "Why would you end in the middle of your Quidditch career?" ("angry", "narrow", "base", "L")
    hoo @ cheeks blush_heavy "Oh...{w=0.4} *Ehm*..." ("open", "narrow", "base", "downR")
    hoo @ cheeks blush_heavy "Well you know, better end it when you're at the peak...{w=0.4} The urge to experience Quidditch from a new angle... And to... *Ehm*..." ("open", "narrow", "base", "downL")
    gen "Teach?" ("base", xpos="far_left", ypos="head")
    hoo @ cheeks blush_heavy "Oh, yes! Teach!" ("open", "closed", "shocked", "stare")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "The masked seeker... Teaching the next generation of Quidditch players..." ("smile", "narrow", "base", "L")
    hoo @ cheeks blush_heavy "Oh, stop it now, Miss Chang, you're making me blush." ("grin", "base", "base", "downR")
    cho "But, you're a living legend! This broom... It's... It's..." ("smile", "narrow", "base", "L")
    gen "Looks like a normal broom to me." ("base", xpos="far_left", ypos="head")
    cho "Sir, how could you say that?! This surely must be her secret! Why else would she be giving it to me?" ("disgust", "narrow", "angry", "mid")
    hoo @ cheeks blush "Oh no... He's right. There's nothing special about this broom." ("base", "narrow", "base", "L")
    cho "What?!" ("angry", "wide", "base", "L")
    cho "But then how did you get it to fly at such speeds?" ("angry", "narrow", "base", "L")
    hoo @ cheeks blush "By utilising some very special techniques that I discovered." ("base", "wink", "raised", "L")
    gen "(Why is she still blushing?)" ("base", xpos="far_left", ypos="head")
    hoo @ cheeks blush "*Ahem*... Perhaps it'd be best if I explained the history behind it first." ("open", "narrow", "base", "downR")
    hoo @ cheeks blush "I'm sure you're well aware that caring for your broom means a great deal to how well it will behave during flight." ("open", "closed", "base", "mid")
    cho "You mean using things like broom polish and trimming it?" ("soft", "base", "raised", "L")
    hoo @ cheeks blush "Precisely." ("base", "base", "base", "L")
    hoo @ cheeks blush "It's always been believed, and I still teach our students that usage of such things helps with aerodynamics, speed and agility." ("open", "base", "shocked", "L")
    hoo @ cheeks blush_heavy "Except that's only a half-truth." ("open", "base", "base", "downL")
    hoo @ cheeks blush_heavy "How do I explain this..." ("normal", "narrow", "raised", "down")
    hoo @ cheeks blush "Remember your first flying lesson when you had to use a command word for the broom to jump into your hand?" ("open", "shocked", "shocked", "L")
    cho "Yes, of course!" ("smile", "narrow", "base", "L")
    hoo @ cheeks blush "Have you ever considered how this actually works? There's no wand being used in conjunction with the command word." ("open", "shocked", "shocked", "L")
    cho "..." ("soft", "narrow", "base", "down")
    cho "I honestly never thought about it..." ("soft", "narrow", "base", "downR")
    hoo @ cheeks blush "Yes, and I wouldn't blame you..." ("open", "closed", "base", "mid")
    hoo @ cheeks blush "The basic knowledge of creating brooms has been passed down for generations, the \"why's\" and \"how's\" is not something the average broom user cares about." ("open", "base", "shocked", "L")
    hoo @ cheeks blush "But me, on the other hand... Well, I got a bit obsessed trying to answer this question, and began researching heavily to try and figure out how it all worked..." ("base", "base", "base", "mid")
    cho "And you found the answer?" ("angry", "base", "base", "L")
    hoo @ cheeks blush "It took years of research... But yes, I did." ("grin", "shocked", "base", "L")
    cho "Years?!" ("clench", "wide", "base", "L")
    hoo @ cheeks blush "Indeed... I had to sift through and translate some very old tomes to find what I was searching for, as all my questions led me towards the very essence of enchanting." ("open", "shocked", "base", "L")
    cho @ cheeks blush "Wow..." ("smile", "base", "base", "L")
    hoo @ cheeks blush "Think of magic as a tree." ("open", "base", "base", "L")
    hoo @ cheeks blush "All magic in this world and others stems from the same source, each school of magic are just branches leading to it." ("base", "shocked", "base", "L")
    hoo @ cheeks blush "If the magic user has a higher understanding of the core fundamentals of that branch of magic, then they have a much easier time at manipulating it..." ("base", "base", "base", "L")
    hoo @ cheeks blush "As an example, creatures of old such as Djinns possess magical abilities that stretch as far as the roots of magic." ("base", "base", "base", "mid")
    hoo @ cheeks blush "Although their abilities are innate... We'd be so lucky to even get close to the source of each school of magic." ("base", "shocked", "base", "mid")
    gen "(Makes sense... I sort of just waved my fingers and shit happened...)" ("base", xpos="far_left", ypos="head")
    cho "Djinns?" ("soft", "base", "raised", "mid")
    hoo @ cheeks blush "Or Genies, whatever you prefer." ("open", "shocked", "base", "L")
    gen "Djinn is fine." ("base", xpos="far_left", ypos="head")
    cho "I see..." ("soft", "narrow", "base", "downR")
    hoo @ cheeks blush "Through my research, I found that when a magic user imbues an object with magic, we also leave a trace of ourselves inside of it." ("open", "shocked", "shocked", "L")
    hoo @ cheeks blush "It's a bit complicated to explain... In essence, it's something like our core instincts or character, mixed with all of the other elements that binds us magic users together." ("base", "base", "shocked", "L")
    hoo @ cheeks blush "Are you following?" ("base", "shocked", "raised", "L")
    gen "Makes perfect sense to me." ("base", xpos="far_left", ypos="head")
    cho "*Err*..." ("angry", "narrow", "base", "L")

    if states.map.snape_office.picture_examined:
        gen "That's why those portraits never keep quiet, isn't it?" ("base", xpos="far_left", ypos="head")
        hoo @ cheeks blush "Precisely... The portraits appear alive for this very reason." ("base", "base", "base", "mid")
        hoo @ cheeks blush "Every painting contains some characteristics from the artist who painted it." ("base", "shocked", "base", "L")

    hoo @ cheeks blush "That said, a bond can also be formed between a magic user and an object, much like the one we all have with our wands." ("base", "base", "base", "L")
    hoo @ cheeks blush "This is the reason why doing things like polishing our brooms is so important, it has nothing to do with the polish itself... That's all just corporate mumbo jumbo." ("base", "narrow", "base", "L")
    hoo @ cheeks blush "It's about forming that bond with the object." ("base", "shocked", "base", "mid")
    gen "I polish mine every day." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Wow..." ("smile", "narrow", "base", "L")
    hoo @ cheeks blush_heavy "Which leads me to my practical research in the subject, and how I finally became... The masked seeker." ("open", "closed", "shocked", "mid")
    cho "Oooh!" ("smile", "base", "base", "L")
    hoo @ cheeks blush "So... With this knowledge, I started working on figuring out new ways to care for your broom." ("base", "base", "base", "down")
    hoo @ cheeks blush "I tried sweeping with it, it's a broom after all, I thought maybe it would like that." ("open", "shocked", "raised", "R")
    hoo @ cheeks blush "But it didn't work... In fact, it made the broom slower... Which made sense, this broom was designed for flying after all..." ("normal", "base", "base", "mid")
    hoo @ cheeks blush "I tried talking to it... And that might've worked, albeit the fact that brooms don't have ears..." ("base", "shocked", "base", "L")
    hoo @ cheeks blush "I even tried using Fleetwood's High-Finish Handle Polish to see if it made any difference to the one I usually use, and lo and behold..." ("base", "base", "base", "downR")
    cho "" ("angry", "base", "base", "L") #expectant

    call ctc

    hoo @ cheeks blush "There was no difference." ("open", "base", "base", "L")
    cho "" ("annoyed", "base", "base", "mid") #disappointed
    hoo @ cheeks blush "After all these tests, I wasn't getting anywhere, and I was just feeling more and more frustrated...{w=0.4} So I had to do something to take the edge off." ("open", "closed", "base", "mid")
    hoo @ cheeks blush_heavy "And as it just so happened, there was a polished and stiff wooden object at hand right there..." ("open", "base", "base", "R")
    gen "..." ("grin", xpos="far_left", ypos="head")
    hoo @ cheeks blush_heavy "Let's just say that I rode that thing in ways I had never done before..." ("base", "narrow", "base", "down")
    cho "I do that when I'm stressed out too!" ("smile", "base", "base", "L")
    gen "I don't think she meant in the way you're thinking." ("grin", xpos="far_left", ypos="head")
    cho "What do you mean then professor--" ("soft", "base", "raised", "mid")
    cho @ cheeks blush "Ooooh..." ("soft", "narrow", "base", "L") #Blushing
    gen "So, this is what you meant when you said you had just the broom for Miss Chang..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("soft", "narrow", "base", "down") #Blushing
    hoo @ cheeks blush "Figured it out already have you?" ("base", "wink", "raised", "mid")
    hoo @ cheeks blush "Well, I can't say I'm surprised, you've always had a much broader view on magic than most, professor." ("base", "base", "base", "mid")
    cho @ cheeks blush "I'm confused..." ("disgust", "narrow", "base", "mid")
    hoo @ cheeks blush "Think about the things I've told you thus far, Miss Chang." ("base", "base", "base", "L")
    hoo @ cheeks blush "When you enchant an object, it takes on some of the enchanter's characteristics." ("base", "base", "shocked", "L")
    cho @ cheeks blush "Yes?" ("soft", "narrow", "base", "L")
    hoo @ cheeks blush "Well, Initially during practical testing I was trying to appeal to what I thought a broom would enjoy." ("base", "base", "base", "R")
    hoo @ cheeks blush_heavy "When I should've appealed to what I would enjoy..." ("base", "base", "base", "L")
    cho @ cheeks heavy_blush "Wait, so doing...{w=0.4} {i}\"That\"{/i} with your broom... Made the broom go faster? Using it to...{w=0.4} *Err*..." ("angry", "narrow", "base", "L")
    gen "Take off." ("base", xpos="far_left", ypos="head")
    hoo @ cheeks blush "Faster {b}and{/b} more agile... Although the effects faded quite quickly afterwards." ("base", "shocked", "base", "L")
    cho @ cheeks heavy_blush "Then how were you able to use this method during a game of Quidditch?" ("angry", "narrow", "base", "L")
    hoo @ cheeks blush "I'm glad you asked!" ("grin", "shocked", "base", "L")
    hoo @ cheeks blush "I used this..." ("grin", "base", "base", "L")

    #Dildo appears on broom
    hoo @ cheeks blush "" ("base", "base", "base", "downR")
    play sound "sounds/collar_click.ogg"
    $ hooch.equip(hoo_accessory_broom_dildo)
    with d3

    nar "Madam Hooch takes a phallic shaped object out of her pockets and attaches it to the broom."

    cho @ cheeks heavy_blush "Merlin's beard!" ("mad", "wide", "base", "L")
    gen "Merlin's cock!" ("grin", xpos="far_left", ypos="head")
    hoo @ cheeks blush "So, what say you, Miss Chang? You wanted a broom that rivals the firebolt, so here you have it!" ("grin", "shocked", "raised", "L")
    cho @ cheeks heavy_blush "Yes, but..." ("mad", "narrow", "base", "downR")
    hoo @ cheeks blush_heavy "When used by the right person, this broom could go even faster." ("grin", "shocked", "base", "L")
    cho @ cheeks heavy_blush "But, everyone will be there, watching..." ("angry", "narrow", "base", "L") #blushing
    hoo @ cheeks blush_heavy "I know...{w=0.4} Exciting thought, isn't it?" ("grin", "base", "shocked", "L")
    cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "downR")
    hoo @ cheeks blush "You don't need to pretend with me, Miss Chang. I have seen how much you enjoyed everybody gazing at you during the preliminaries..." ("grin", "wink", "base", "L")
    cho @ cheeks heavy_blush "You did?" ("angry", "narrow", "base", "L")
    hoo @ cheeks blush_heavy "Yes, and I assure you, I understand your feelings completely..." ("base", "narrow", "shocked", "L")
    hoo @ cheeks blush_heavy "As it happens... There's nothing that gets me more excited than a crowd..." ("base", "narrow", "base", "mid")

    # Used in Quidditch Outro
    label .introspection:

    if _in_replay:
        show screen blkfade
        with d5

        $ hooch.equip(hoo_outfit_default)
        $ hooch.equip(hoo_accessory_broom_dildo)
        $ cho.equip(cho_outfit_quidditch_gryffindor)
        $ game.gold = 1984
        $ game.day = 666
        $ game.daytime = True
        $ game.weather = "clear"
        $ hooch_chibi.zoom = 0.38
        $ hooch_chibi.zorder = 4
        call room("quidditch_pitch")
        call cho_chibi("stand", "right", "base", flip=False)
        call gen_chibi("stand", "mid", 470, flip=False)
        chibi hooch place ((450, 500))

        hoo @ cheeks blush "" ("base", "narrow", "base", "R", xpos=100, ypos="base", flip=True)
        cho @ cheeks heavy_blush "" ("horny", "narrow", "base", "mid", xpos=460, ypos="base", flip=False)

        play background "sounds/outskirts.ogg" fadein 2
        play music "music/march-of-the-spoons-by-kevin-macleod-from-filmmusic-io.ogg" fadein 1 fadeout 1 if_changed
        
        hide screen blkfade
        with d5

    hoo @ cheeks blush "And all those feelings are imbued into this very broom..." ("base", "narrow", "base", "R")
    hoo @ cheeks blush_heavy "I remember using it at the Quidditch world cup finals... Thousands of people watching..." ("grin", "closed", "worried", "mid")
    cho @ cheeks heavy_blush "" ("horny", "narrow", "base", "downR")
    hoo @ cheeks blush_heavy "I don't think any broom had ever reached such speeds before..." ("grin", "narrow", "base", "stare")
    hoo @ cheeks blush_heavy "When I caught the snitch... Why, I've never felt such a rush." ("grin", "closed", "shocked", "mid")
    cho @ cheeks heavy_blush "{size=-6}I'll do it...{/size}" ("disgust", "narrow", "base", "downR") #Small text

    # Used in Quidditch Outro
    if _in_replay:
        return

    if states.cho.ev.quidditch.given_thestral:
        gen "Wait, how come when I tried to give you a broom with a--" ("angry", xpos="far_left", ypos="head")
    else:
        gen "You will?" ("base", xpos="far_left", ypos="head")

    hoo @ cheeks blush "Fantastic news!" ("grin", "shocked", "shocked", "L")

    if states.cho.ev.quidditch.given_thestral:
        gen "..." ("base", xpos="far_left", ypos="head")

    cho @ cheeks heavy_blush "Just...{w=0.4} *Ahem*...{w=0.4} I have a question..." ("angry", "narrow", "base", "down")
    hoo @ cheeks blush "Yes?" ("base", "shocked", "raised", "L")
    cho @ cheeks heavy_blush "How did you manage to keep it--{w=0.2} I mean, it's so big...{w=0.4} How did nobody see?" ("angry", "narrow", "base", "L")
    hoo @ cheeks blush "A skirt and a small cut in your underwear and no one will be any wiser." ("base", "shocked", "base", "downL")
    cho @ cheeks heavy_blush "I see..." ("soft", "narrow", "base", "down")
    gen "To think that a \"PE\" teacher would have such a grasp of the fundamentals of magic..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Sir!" ("clench", "base", "base", "mid")
    gen "Oh sorry, did I say that out loud?" ("base", xpos="far_left", ypos="head")
    hoo "Yes, I'm a bit of a rogue bludger..." ("grin", "wink", "base", "mid")
    cho @ cheeks blush "" ("annoyed", "base", "base", "mid")
    gen "(I wonder if this is this why that carpet always appeared more energetic after getting whipped.)" ("base", xpos="far_left", ypos="head")
    gen "(Gross...)" ("base", xpos="far_left", ypos="head")
    gen "So, what do you call this invention of yours?" ("base", xpos="far_left", ypos="head")
    hoo "What do I call it?" ("open", "shocked", "raised", "mid")
    hoo "*Hmm*... Why, I've never really thought about giving it a name." ("normal", "base", "shocked", "down")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    gen "I thought women named all their toys." ("base", xpos="far_left", ypos="head")
    gen "How about..." ("base", xpos="far_left", ypos="head")

    menu:
        #Sets Cho's broom name for use during and after match (states.cho.ev.quidditch.broom_name)
        "\"The Schlickstick!\"":
            $ states.cho.ev.quidditch.broom_name = "Schlickstick"

            cho @ cheeks blush "The what?" ("angry", "wide", "base", "mid")
            gen "A fitting name for a fitted broom..." ("base", xpos="far_left", ypos="head")
            hoo "[states.cho.ev.quidditch.broom_name] eh? I like it!" ("base", "base", "base", "mid")
        "\"The Scoot-a-ride!\"":
            $ states.cho.ev.quidditch.broom_name = "Scoot-a-ride"

            gen "You know, cause you scoot around on it." ("base", xpos="far_left", ypos="head")
            cho "Very funny professor..." ("annoyed", "narrow", "base", "mid")
            hoo "Works for me." ("base", "base", "base", "mid")
        "\"The Speedblaster 2000!\"":
            $ states.cho.ev.quidditch.broom_name = "Speedblaster 2000"

            gen "Cause it'll get up to higher speeds when it blasts your--" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Sir!" ("angry", "base", "angry", "mid")
            gen "I know, a perfect name isn't it?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Professor Hooch, I'm so sorry about his--" ("angry", "closed", "angry", "mid")
            hoo "I like it!" ("base", "base", "base", "mid")
            cho @ cheeks blush "..." ("disgust", "base", "base", "L")
        "\"The Purple Rocket!\"":
            $ states.cho.ev.quidditch.broom_name = "Purple Rocket"

            cho @ cheeks blush "The broom isn't... Oh, I see..." ("disgust", "narrow", "base", "mid")
            hoo "Works for me." ("base", "base", "base", "mid")
            gen "*He-heh*..." ("grin", xpos="far_left", ypos="head")
        "\"The Cumet!!\"":
            $ states.cho.ev.quidditch.broom_name = "Cumet"

            hoo "There's already a broom called that, unfortunately." ("normal", "base", "shocked", "mid")
            gen "There is?" ("base", xpos="far_left", ypos="head")
            gen "Someone's stolen the pun before I could..." ("base", xpos="far_left", ypos="head")
            hoo "Oh, I see what you mean now." ("base", "base", "base", "mid")
            cho "Huh?" ("open", "base", "base", "L")
            hoo @ cheeks blush "Yeah, cumet suits it just fine..." ("grin", "base", "raised", "R")
        "\"The Nimble 2069!\"":
            $ states.cho.ev.quidditch.broom_name = "Nimble 2069"

            hoo "I see, since you're able to move more nimbly on it... Very clever." ("base", "base", "base", "mid")
            gen "(Heh-heh... Sixty-nine...)" ("base", xpos="far_left", ypos="head")
        "\"The Spurtstick 900!\"":
            $ states.cho.ev.quidditch.broom_name = "Spurtstick 900"

            hoo "It does go very fast once you get it going... I like it!" ("base", "shocked", "shocked", "mid")
            cho @ cheeks blush "I'm not sure that's why he wants to call it--" ("disgust", "narrow", "base", "L")
            gen "Great! Spurtstick 900 it is!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("disgust", "base", "base", "mid")

    gen "Very well then... You've got what you wanted, Miss Chang. I hope you're satisfied." ("base", xpos="far_left", ypos="head")
    gen "If not, I'm sure you will be, at the finals." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Sir!" ("angry", "base", "base", "mid")
    gen "When you win that cup, of course." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Oh..." ("upset", "base", "base", "downR")
    gen "Make sure you get lots of practice in until then." ("grin", xpos="far_left", ypos="head")
    cho "Yes sir." ("soft", "base", "base", "mid")
    cho "*Ehm*...{w=0.4} Thank you for your assistance, Professor." ("open", "base", "base", "L")
    hoo "Certainly, Miss Chang... Good luck." ("base", "base", "base", "L")

    #Fade to black
    show screen blkfade
    with d5

    nar "You leave Cho to her own devices...{w=0.4} And return to your office."

    $ states.cho.ev.quidditch.e12_complete = True

    # Reset hooch's chibi values
    $ hooch_chibi.zoom = 0.28
    $ hooch_chibi.zorder = 12
    $ hooch.equip(hoo_accessory_broom)

    stop background fadeout 0.5
    stop weather fadeout 0.5

    jump main_room

label cho_quid_E13:

    # Informs the player that all preparations are complete

    gen "(Cheerleading squad... Check... Broom... Check...)" ("base", xpos="far_left", ypos="head")
    gen "(Well then... That should be everything.)" ("base", xpos="far_left", ypos="head")
    gen "(Although perhaps I could leave her with that broom for a bit before arranging the finals...)" ("grin", xpos="far_left", ypos="head")

    $ states.cho.ev.quidditch.e13_complete = True

    jump main_room_menu

label cho_quid_E14:

    # Quidditch Outro

    call cho_walk("mid", "base", action="enter")

    cho "Hello Coach." ("base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    gen "Hello [name_cho_genie]...{w=0.4} So, I am still your coach after all?" ("base", xpos="far_left", ypos="head")
    cho "Of course you are!" ("smile", "base", "base", "mid")
    cho "Unless you would rather not be anymore?" ("upset", "narrow", "base", "mid")
    gen "Nonsense." ("base", xpos="far_left", ypos="head")
    gen "If you ever need me, I'll be there before you can even say snitch." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well, in that case...{w=0.3}{nw}" ("smile", "narrow", "base", "mid")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    cho @ cheeks blush "Well, in that case...{fast} {size=-2}Snitch...{/size}" ("smile", "narrow", "base", "mid")

    menu:
        "-Use Instant Transmission-": # Genie teleports to Cho

            play sound "sounds/kick.ogg"
            call gen_chibi("stand", 430, "base")
            call teleport(position="genie", effect=False)

            cho @ cheeks blush "Whoa! I didn't know you could apparate at Hogwarts!" ("angry", "narrow", "base", "mid")
            gen "Appa--{w=0.4} What?" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Apparate!" ("angry", "base", "base", "mid")
            gen "Isn't that the flying thing from Four Elements Tr--{w=0.2} I mean Avatar!" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "What?" ("upset", "base", "base", "mid")
            gen "*Err*...{w=0.2} Yeah, whatever you said." ("base", xpos="far_left", ypos="base")

        "\"Wait, right now?\"": # Genie walks to cho

            gen "Wait, now?" ("angry", xpos="far_left", ypos="head")
            cho @ cheeks blush "Isn't the coach supposed to make sure their pupil keeps up with their training?" ("base", "wink", "base", "mid")
            gen "*Hmm*... I suppose another examination of your physique would be in order." ("base", xpos="far_left", ypos="head")

            call gen_chibi("stand", 225, "base")
            with d3
            call gen_walk(path=[(230, 470), (410, 470), (430, "base")])

    gen "So, how about we start with examining your chest, and then move on to--" ("grin", xpos="far_left", ypos="base")
    cho @ cheeks blush "Actually, I was thinking of showing you how I take care of my most prized possession." ("smile", "narrow", "base", "down")
    gen "Your {i}most prized possession?{/i}" ("base", xpos="far_left", ypos="base")
    cho @ cheeks blush "That's right..." ("smile", "narrow", "base", "mid")
    cho @ cheeks blush "Can you guess what it is?" ("smile", "narrow", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="base")
    cho @ cheeks blush "Let me give you a hint... It's a piece of wood, that goes between my legs..." ("smile", "narrow", "base", "mid")
    gen "Piece of... Wood?" ("base", xpos="far_left", ypos="base")

    $ _aware = False
    $ _stressed = False

    menu:
        "-Let the intrusive thoughts win-":
            $ _stressed = True

            gen "(Last I checked, she didn't have any wood down there, we've even had sex!)" ("base", xpos="far_left", ypos="base")
            gen "(Have my dick gotten so worn down that I can't tell the difference between a pussy and an ass?)" ("base", xpos="far_left", ypos="base")
            gen "(Maybe she's a were-futa?!)" ("angry", xpos="far_left", ypos="base")
            cho @ cheeks blush "[name_genie_cho]?" ("soft", "base", "base", "mid")
            gen "(Nah... She would've shown symptoms much earlier if that were the case...)" ("base", xpos="far_left", ypos="base")
            gen "(Perhaps she's been under some sort of body concealment charm this entire time?)" ("base", xpos="far_left", ypos="base")
            gen "(No... That'd be ridiculous...{w=0.5} Although--)" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "[name_genie_cho], are you listening?" ("open", "base", "raised", "mid")
            gen "*Huh*?" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "If you don't mind... I'd like to show off my skills as a beater." ("smile", "narrow", "base", "mid") #beater is used deliberately instead of beating
            gen "(Quidditch... Of course that's what she meant...)" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Why are you looking at me like that?" ("soft", "base", "base", "mid")
            gen "Oh, I was just--{w=0.2} Well, I just thought you--" ("base", xpos="far_left", ypos="base")
            cho @ cheeks heavy_blush "Is it because I'm a girl?!" ("angry", "narrow", "raised", "mid")
            gen "What?!" ("angry", xpos="far_left", ypos="base")
            cho @ cheeks heavy_blush "You think I can't do it because I'm a girl?!" ("open", "narrow", "angry", "mid")
            gen "W--What, how are you implying--" ("angry", xpos="far_left", ypos="base")
            cho @ cheeks blush "Just because boys have it easier, it doesn't mean a girl like me can't do it!" ("upset", "narrow", "angry", "downR")
            gen "I wasn't saying--{w=0.2} I mean, do you even have the right equipment?" ("angry", xpos="far_left", ypos="base")
            cho @ cheeks blush "I have everything I need right here!" ("open", "closed", "angry", "mid")
            gen "Y-You do?" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Of course!" ("angry", "narrow", "base", "mid")
            cho @ cheeks blush "Just close your eyes for a moment, and I'll prove my worth to you." ("open", "closed", "angry", "mid")
            gen "Why would I need to--" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Close them!" ("angry", "narrow", "base", "mid")
            gen "(I hope I don't regret this...)" ("base", xpos="far_left", ypos="base")
        "\"Your broom?\"":
            cho @ cheeks blush "Close, but not quite." ("base", "narrow", "base", "mid")
            cho @ cheeks blush "If you don't mind... I'd like to show off my skills as a beater." ("smile", "narrow", "base", "mid") #beater is used deliberately instead of beating
            gen "(A beater's bat?)" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Just close your eyes for a moment, and you won't regret it." ("horny", "base", "base", "mid")
            gen "Why would I need to close--" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Just close them!" ("upset", "narrow", "angry", "mid")
            gen "..." ("angry", xpos="far_left", ypos="base")
        "\"You mean...\"":
            cho @ cheeks blush "If you don't mind... I'd like to show off my skills as a beater." ("smile", "narrow", "base", "mid") #beater is used deliberately instead of beating
            gen "(A beater's bat?)" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Just close your eyes for a moment, and you won't regret it." ("horny", "base", "base", "mid")
            gen "Why would I need to close--" ("base", xpos="far_left", ypos="base")
            cho @ cheeks blush "Just close them!" ("upset", "narrow", "angry", "mid")
            gen "..." ("angry", xpos="far_left", ypos="base")
        "\"It's my cock, isn't it.\"":
            $ _aware = True

            cho @ cheeks blush "*Err*--{w=0.4} No, it's--{w=0.4} *Ehm..." ("upset", "narrow", "angry", "mid")
            gen "*He-he*...{w=0.4} I knew it." ("grin", xpos="far_left", ypos="base")
            cho @ cheeks blush "J-Just close your eyes..." ("upset", "narrow", "angry", "mid")    

    show screen blkfade
    with d5

    stop weather fadeout 4
    $ game.weather = "clear"

    play sound "sounds/cloth_sound3.ogg"

    if _stressed:

        gen "What are you doing?"
        cho "One moment [name_genie_cho], I'm just having a little bit of trouble pulling it out..."
        gen "*Gulp*"

        play sound "sounds/cloth_sound3.ogg"

        gen "[name_cho_genie], is that...?"
        cho "One more second..."
        cho "Now, if I could just--"

        play sound "sounds/cloth_sound3.ogg"

    cho "There we go!"
    cho "You can open your eyes now."

    if game.daytime:
        show cho_handjob as cg zorder 16
    else:
        show cho_handjob as cg zorder 16 at color_temperature(1.0)

    hide screen blkfade
    with d5

    #Fade to CG, Cho has arm to her side, normal shirt (ingame shader for night variant)

    #Cho looks down at genie's soft cock
    call ctc

    if not _aware:
        gen "Whoa! You were talking about my cock!"

    #Cho looks up and smiles

    show cho_handjob cho_body_idle mouth_smile as cg with d3

    if not _aware:
        gen "But, I thought you said you wanted to show off your skills--"
        gen "Okay, I think I just caught up to what we're doing here..."
    else:
        gen "Are you going to jerk me off? You naughty little raven."

    show cho_handjob mouth_open eyes_open_right as cg with d3

    cho "I don't know what you're talking about, [name_genie_cho]... This is just yet another normal training session with one of your trainees."

    show cho_handjob mouth_base eyes_open_right as cg with d3

    gen "(Sounds like something I would say.)"
    gen "I must've rubbed off on you in more ways than one."

    show cho_handjob mouth_smile eyes_open_narrow_forward as cg with d3

    cho "What can I say, I'm very impressionable..."

    show cho_handjob mouth_lipbite eyes_open_forward eyebrows_raised as cg with d3

    cho "Speaking of rubbing... Would you like a demonstration of how I enchant my equipment?"

    if _stressed:
        gen "A few minutes ago, I would be hesitant, but now? Sure!"
    else:
        gen "Very much so."

    show cho_handjob mouth_neutral eyes_open_down as cg with d3

    cho "Although..."

    show cho_handjob eyebrows_worried as cg with d3

    cho "It looks like the equipment isn't quite ready yet."

    if _stressed:
        call ctc
        gen "The--"

        gen "(Floppy cock!!)"
        gen "(She got me all stressed out for a moment, but I cannot show weakness!)"

        menu:
            "\"It's cold in here!\"":
                gen "And I wasn't ready!"

            "\"I wasn't ready!\"":
                gen "And it's cold in here!"

        show cho_handjob mouth_base eyebrows_base eyes_open_narrow_down as cg with d3

        cho "No big deal, [name_genie_cho]... I learned how to deal with this sort of thing during one of my lessons."
        gen "(During her lessons...?)"
    else:
        show cho_handjob mouth_base eyebrows_base eyes_open_narrow_down as cg with d3

        cho "Let me try something I learnt during my lessons."

    gen "(During her lessons...?)"

    show cho_handjob cho_body_stroke_idle mouth_open eyes_open_down eyebrows_angry as cg with d3

    cho "{size=+5}Up!{/size}"

    show cho_handjob mouth_upset eyes_open_left eyebrows_worried as cg with d3

    cho "Hold on, that's for brooms, not for--"

    #Genie gets a boner
    play sound "sounds/boing05.ogg"
    show cho_handjob penis_hard mouth_open eyes_open_wide_down eyebrows_base as cg with vpunch
    pause .5

    cho "Oh, it worked!"

    show cho_handjob mouth_smile eyes_open_down as cg with d3

    cho "I mean, of course it worked!"

    show cho_handjob cho_body_idle eyes_open_forward as cg with d3

    cho "Well then... Let's start with the enchanting process..."

    #Cho takes genie's cock in her hand
    #Cho turn head down towards dick
    #Spit trailing from mouth towards dick
    #Spit on dick
    #Cho hand on dick, jacking it.
    #Shiny dick (spit)

    show cho_handjob cho_body_bending as cg with d6
    pause 0.75

    play sound "sounds/drooling.ogg"

    show cho_handjob effects_spitting as cg with d3
    pause 0.25
    show cho_handjob penis_hard_spit_on_tip as cg with d3
    pause 0.5

    gen "Whoa!"

    show cho_handjob eyes_open_down cho_body_stroke_idle -effects_spitting as cg with d3
    pause 0.5
    show cho_handjob eyebrows_raised cho_body_stroke_up as cg with d3
    pause 0.5
    show cho_handjob eyebrows_sad mouth_lipbite -effects_spitting as cg with d3

    cho "*Mmm*...{w=0.4} Nice and stiff..."
    gen "Stop teasing me and get to it already!"

    show cho_handjob cho_body_stroke_up eyebrows_base eyes_open_narrow_forward mouth_base as cg with d3

    cho "Patience, [name_genie_cho], this is just one of the steps I learned about enchanting."
    gen "Hold on, you're actually enchanting my cock? I didn't know you could do that!"

    show cho_handjob mouth_open eyes_open_forward as cg with d3

    cho "Your cock?"

    show cho_handjob mouth_smile eyes_open_narrow_forward as cg with d3

    cho "I'm not sure what you're talking about..."

    show cho_handjob mouth_base eyes_open_narrow_down as cg with d3

    cho "I'm merely creating a magical connection between myself and this magnificent piece of wood..."
    gen "Creating a connection... By using spit?"

    show cho_handjob mouth_open eyes_open_forward eyebrows_raised as cg with d3

    cho "Of course! You don't want friction--"

    show cho_handjob mouth_open eyes_open_right eyebrows_angry as cg with d3

    cho "*Ahem*...{w=0.4} I mean, you need the element of water to cast a successful enchantment!"

    show cho_handjob mouth_neutral eyes_open_right eyebrows_base as cg with d3

    gen "You're not trying to turn my penis into a water geyser, are you?"

    show cho_handjob eyes_closed eyebrows_sad as cg with d3

    cho "*Sigh*"

    show cho_handjob mouth_neutral eyes_open_forward as cg with d3

    gen "Alright, I'll listen..."

    show cho_handjob mouth_base as cg with d3

    gen "So, what's this magical spit rubbing called again?"

    show cho_handjob mouth_smile eyebrows_base as cg with d3

    cho "Imbuing."
    gen "Fascinating."

    show cho_handjob eyes_open_narrow_down as cg with d3

    cho "I'm basically channelling my magic into the element to create a connection between myself and this piece of wood."
    gen "Magic spit, *huh*..."

    show cho_handjob mouth_base eyes_open_down eyebrows_raised as cg with d3

    cho "Once the connection is established, it can then be strengthened and enforced in various ways, through stimulation."

    menu:
        "\"You're starting to sound like Hermione.\"":

            show cho_handjob mouth_annoyed eyes_open_forward eyebrows_angry as cg with d3

            cho "*Hmph*"
            gen "See? She *Hmphs* at me too!"

            show cho_handjob mouth_upset eyes_open_narrow_forward eyebrows_angry as cg with d3

            cho "Oh, stop it..."
            cho "We have nothing in common."
            gen "I would argue, that--"

            show cho_handjob mouth_angry eyes_open_wide_forward as cg with d3

            nar "Cho grips your hard wood tight."
            gen "*Gulp*... Maybe not... Please, continue..."

            show cho_handjob eyes_open_left mouth_upset as cg with d3
            cho "*Tsk*"

            show cho_handjob eyes_closed mouth_neutral as cg with d3
            cho "Where was I..."

            show cho_handjob eyes_closed eyebrows_base as cg with d3
            pause 1

            show cho_handjob eyes_open_right as cg with d3
            cho "Ah, right!"

            show cho_handjob eyes_open_forward mouth_base as cg with d3
            cho "The type of stimulation required depends on what the magic user has the strongest affinity for."

        "\"And the spit also helps with that, I assume?\"":

            show cho_handjob eyes_open_forward mouth_base as cg with d3
            cho "If it's physical stimulation, sure... The type of stimulation required depends on what the magic user has the strongest affinity for."

    gen "Right?"

    show cho_handjob eyes_open_narrow_forward as cg with d3

    cho "Some may require mental stimulation."

    show cho_handjob mouth_smile as cg with d3

    cho "But I personally prefer something more physical..."
    gen "Nice..."
    gen "Although, I still don't get what the fuck you're on about--"

    #Cho turn head down towards dick
    #Spit trailing from mouth towards dick

    show cho_handjob cho_body_bending as cg with d6
    pause 0.75

    play sound "sounds/drooling.ogg"

    show cho_handjob effects_spitting as cg with d3
    pause 0.25
    show cho_handjob penis_hard_spit_on_shaft as cg with d3

    gen "Although..."

    show cho_handjob mouth_base cho_body_stroke_down -effects_spitting as cg with d3
    pause 0.5
    show cho_handjob cho_body_stroke_up as cg with d3
    pause 0.5
    show cho_handjob cho_body_stroke_down as cg with d3
    pause 0.5
    show cho_handjob mouth_lipbite cho_body_stroke_up as cg with d3
    pause 0.5
    show cho_handjob eyebrows_raised cho_body_stroke_down as cg with d3

    #jerking slow
    play background "sounds/slickloop.ogg" fadein 2
    show cho_handjob speedlines_1 as cg with d3
    call ctc

    cho "You were saying?"
    gen "Never mind! I totally get it now!"

    show cho_handjob eyebrows_base mouth_smile eyes_shut as cg with d3

    cho "Good! Then we can proceed to the next step."

    gen "Damn, [name_cho_genie]! Since when did you get so good at giving handjobs?"

    show cho_handjob eyebrows_raised mouth_neutral eyes_open_right as cg with d3

    cho "I'm not sure what you mean by \"giving handjobs\", [name_genie_cho]."

    show cho_handjob eyebrows_base mouth_base eyes_open_forward as cg with d3

    cho "But what I can tell you is, to establish a strong connection, an enchanter must always use their full potential."
    gen "That Hooch lady's sure taught you a lot!"

    show cho_handjob eyebrows_base mouth_smile eyes_shut as cg with d3

    cho "*Giggles*"

    show cho_handjob eyebrows_raised mouth_base eyes_open_narrow_forward as cg with d3

    cho "Practice makes perfect... It's what she taught me."

    show cho_handjob eyebrows_base mouth_lipbite eyes_open_narrow_forward as cg with d3

    cho "I've practised enchanting on my own equipment countless times by now."

    show cho_handjob eyebrows_sad as cg with d3

    cho "My snitch absolutely glows with magic once I'm finished with it."
    gen "I bet..."

    show cho_handjob eyebrows_base eyes_open_right as cg with d3

    cho "Although I have to do it in secret, so I end up picking a time and place where I won't be bothered, like the changing rooms after practice."

    show cho_handjob eyebrows_base eyes_open_narrow_forward mouth_smile as cg with d3

    gen "Clever...{w=0.4} *Nghh*--{w=0.2} girl."

    show cho_handjob mouth_base as cg with d3

    gen "So, is experiencing the real deal any different from your practice?"

    show cho_handjob mouth_open eyes_open_left as cg with d3

    cho "It's somewhat similar, but..."

    stop background
    show cho_handjob eyebrows_raised eyes_open_forward mouth_smile -speedlines_1 as cg with d3
    cho "You know what... Why don't I tell you how I usually do it, and we could compare?"
    gen "Sounds like a plan!"

    show cho_handjob eyebrows_sad eyes_open_narrow_down mouth_base as cg with d3
    cho "Well then..."

    # CG of Cho masturbating in front of lockers shows inside a small though-bubble.
    show cho_masturbate_lockers cho_body_idle mouth_open eyes_narrow_down as cg2 zorder 15
    show cho_handjob as cg zorder 16

    show screen cho_dual_cg("cg2")

    #Cho puts fingers in mouth (masturbate)
    #Cho stops jacking (genie)
    #Cho turn head down towards dick (genie)
    #Spit trailing from mouth towards dick (genie)

    show cho_handjob eyes_open_right eyebrows_base mouth_base as cg with d3

    cho "First, I start by covering the surface with a good coat of spit-- I mean the magical conductor..."

    show cho_masturbate_lockers cho_body_sucking mouth_sucking as cg2
    show cho_handjob cho_body_bending as cg
    with d6
    pause 0.75

    play sound "sounds/drooling.ogg"

    show cho_handjob effects_spitting as cg with d3
    pause 0.25

    gen "Magical conductor, right."

    #Cho puts hand on clit (masturbate)
    #Cho normal head pose (genie)
    show cho_handjob eyes_open_down cho_body_stroke_idle -effects_spitting as cg with d3
    pause 0.5
    show cho_handjob eyebrows_raised cho_body_stroke_up as cg with d3
    pause 0.5

    show cho_masturbate_lockers cho_body_fingering_up mouth_open eyes_narrow_down as cg2
    show cho_handjob eyebrows_sad mouth_base eyes_open_right -effects_spitting as cg
    with d3

    cho "I then slowly begin fondling it gently with my fingers."

    #Cho starts jerking (genie)
    #Cho starts rubbing clit (masturbate)
    play background "sounds/slickloop.ogg" fadein 2
    show cho_masturbate_lockers cho_body_fingering_down mouth_base eyes_narrow_down as cg2
    show cho_handjob eyebrows_base eyes_open_narrow_down speedlines_1 as cg
    with d3
    cho "Rubbing it,{w=0.3} up and down,{w=0.3} up and down..."


    show cho_masturbate_lockers mouth_lipbite eyebrows_mad eyes_down as cg2
    show cho_handjob mouth_smile as cg
    with d3
    cho "Once the coating has been evenly distributed, I proceed to channel my magic into it."

    #jerking medium (genie)
    #rubbing medium (masturbate)
    play background "sounds/slickloopfast.ogg" fadein 2
    show cho_handjob speedlines_2 as cg
    show cho_masturbate_lockers mouth_lipbite eyebrows_mad eyes_down as cg2 with d3

    gen "*Ngh*... You're--{w=0.2} You're able to channel your own magic into your--"

    show cho_masturbate_lockers eyes_narrow_left mouth_open as cg2
    show cho_handjob eyes_open_right as cg
    with d3
    cho "Of course, any able-bodied witch should be able to do that."
    gen "I have so many questions, but... Please, continue..."

    show cho_masturbate_lockers eyes_narrow_forward mouth_open as cg2
    show cho_handjob eyes_open_right eyebrows_base mouth_base as cg
    with d3
    cho "So, I do my very best to keep the flow at a steady pace, until I start feeling tingly."

    show cho_masturbate_lockers eyebrows_raised eyes_narrow_down mouth_lipbite effects_hand_move as cg2
    show cho_handjob eyebrows_angry eyes_open_narrow_down mouth_smile as cg
    with d3
    cho "That's when I increase the speed--{w=0.2} I mean flow..."

    #jerking fast (genie)
    #rubbing fast (masturbate)
    play background "sounds/slickloopveryfast.ogg" fadein 2
    show cho_handjob speedlines_3 as cg
    gen "*Ngh*!!!"

    show cho_masturbate_lockers eyebrows_mad mouth_angry as cg2
    show cho_handjob eyes_open_down mouth_angry as cg
    with d3
    cho "And I pour every ounce of magic I've got into the process, until it's almost bursting with magic!"
    gen "*Aargh*!"

    #Cho stops jerking (genie)
    show screen blkfade
    hide screen cho_dual_cg
    hide cg
    hide cg2
    stop background
    play sound "sounds/pop01.ogg"

    cho "Then I stop, leaving it pulsing, and filled to the brim with magical energy."

    gen "*Ah*...{w=0.4} Why did you--"

    if game.daytime:
        show cho_handjob cho_body_idle mouth_neutral eyes_open_right penis_hard_spit_on_shaft as cg zorder 16
    else:
        show cho_handjob cho_body_idle mouth_neutral eyes_open_right penis_hard_spit_on_shaft as cg zorder 16 at color_temperature(1.0)

    hide screen blkfade
    with d5

    cho "Even though it might be tempting, one shouldn't overdo it, or they might have an accidental discharge."
    gen "Right... Who would want something like that to happen..."

    show cho_handjob eyebrows_sad eyes_open_narrow_down as cg with d3
    cho "Of course, sometimes you can't help it... I've left quite the mess inside the changing room a couple of times."
    gen "You know... I wouldn't mind it if you showed me what such a discharge may look like..."

    show cho_handjob eyebrows_base eyes_open_forward mouth_angry as cg with d3
    cho "*Huh*? Oh, I'm sorry [name_genie_cho]... I got a bit carried away..."

    show cho_handjob eyebrows_sad eyes_open_down mouth_open as cg with d3
    cho "Of course I'll demonstrate how a discharge could happen..."

    show cho_handjob eyebrows_sad eyes_open_narrow_down mouth_neutral as cg with d3
    cho "*Hmm*... I suppose I better--{w=0.2} *Ehm*..."

    show cho_handjob shirt_open as cg with d3
    call ctc

    gen "Nice, show me those titties!"

    show cho_handjob cho_body_stroke_idle eyebrows_raised eyes_open_narrow_down mouth_open as cg with d3
    cho "Okay then...{w=0.4} *Ehm*...{w=0.4} So..."

    show cho_handjob eyebrows_sad cho_body_idle eyes_closed mouth_neutral as cg with d3
    cho "I'm sorry, [name_genie_cho], I don't think I can keep this up..."
    gen "W--{w=0.2} What? No, you're doing a fantastic job keeping it up!"

    show cho_handjob eyes_open_narrow_forward mouth_open as cg with d3
    cho "I mean this role-playing thing."
    gen "(Role-playing? Is that what we're doing?)"

    show cho_handjob eyes_open_right mouth_open as cg with d3
    cho "There is... Something I need to talk to you about..."
    gen "Now?! What about the--"

    show cho_handjob eyes_open_forward mouth_neutral as cg with d3
    cho "..."
    gen "*Ahem*... Of course..."
    gen "(Do they not know of the concept of blue-balls in this world?)"

    show cho_handjob eyebrows_worried eyes_open_narrow_down as cg with d3
    cho "Well... It's just..."

    show cho_handjob eyes_closed mouth_open as cg with d3
    cho "I thought I could pretend it never happened, and that I could trick myself into thinking I'm just doing this to get better at Quidditch."

    show cho_handjob eyes_open_wide_forward mouth_angry as cg with d3
    cho "But I can't!"
    gen "..."

    show cho_handjob cho_body_idle eyes_closed as cg with d3
    cho "I mean, I won the cup already!"

    show cho_handjob eyebrows_worried eyes_shut mouth_neutral as cg with d3
    cho "So, I can't really fool myself that this is about Quidditch any more, can I?"
    gen "*Err*..."
    gen "We could pretend that it's to help you with Quidditch still, if it makes you feel better."
    gen "Training your body to help you reach for the cock-- I mean the snitch and all that."

    show cho_handjob eyebrows_base eyes_open_narrow_down as cg with d3
    cho "The... snitch?"
    gen "Snatch! Dammit... Now that whole bit is ruined..."

    show cho_handjob eyebrows_sad as cg with d3
    cho "..."
    gen "I know! We could compare wind resistance whenever you fly naked versus clothed."

    show cho_handjob eyes_open_down as cg with d3
    cho "..."
    gen "Still not convinced? *Hmm*..."
    gen "Then how about some sexual--{w=0.2} I mean, completely normal yoga!"

    show cho_handjob eyes_open_narrow_down mouth_open as cg with d3
    cho "It's okay, [name_genie_cho]..."

    show cho_handjob mouth_neutral as cg with d3
    cho "While I'm sure there are still a great number of things you could teach me that I could apply at the pitch--"

    show cho_handjob mouth_open eyes_open_forward as cg with d3
    cho "--It's clear that this is not about Quidditch any more, I just need to get to terms with it."
    gen "Why stick with one hobby when you can have many, that's what I always say!"

    show cho_handjob eyebrows_sad mouth_neutral eyes_open_right as cg with d3
    cho "Right...{w=0.4} Well, there's one more thing I wanted to...{w=0.4} *Ehm*..."
    gen "If you're asking me to assist with broadening your horizons, past holding a piece of wood in-between your legs, then my answer is--"

    show cho_handjob eyebrows_raised eyes_open_wide_forward mouth_angry as cg with d3
    cho "Wait!"
    gen "--Yes?"

    show cho_handjob eyebrows_sad eyes_open_narrow_forward mouth_angry as cg with d3
    cho "That's not it..."

    show cho_handjob eyebrows_worried mouth_neutral as cg with d3
    cho "Well, I think it would be best if we were fully honest with each other from now on."
    gen "Oh... *Err*..."

    show cho_handjob eyes_open_narrow_down as cg with d3
    cho "You had me do all those naughty things, and..."
    gen "..."

    show cho_handjob eyebrows_base mouth_open as cg with d3
    cho "Well, it took me a while, but I finally figured it out..."
    gen "You got me! I did it all, just for a chance to get my dick squeezed between your muscly thighs!"

    show cho_handjob cho_body_idle2 eyes_open_forward as cg with d3
    cho "My thighs?"
    gen "Yes?"

    show cho_handjob eyes_open_forward mouth_neutral as cg with d3
    cho "You know, you don't need to lie to me, [name_genie_cho]."
    cho "I understand now that the only reason why you had me do all those things, was to help me raise my confidence, despite my recklessness." # Important note
    gen "*Huh*?"

    show cho_handjob eyes_open_right mouth_open as cg with d3
    cho "I mean, the deal was that I'd sell you favours as a way to repay you for your coaching."

    show cho_handjob eyes_open_narrow_down mouth_neutral as cg with d3
    cho "But if it was sex that you were after, then surely you would've wanted us to go all the way before the finals."

    show cho_handjob eyebrows_sad mouth_open as cg with d3
    cho "But you didn't push me even once to cross that line... You only pushed me to the point where I was able to do what was necessary to win the cup."
    gen "(Probably a bad time to tell her that I just kind of forgot...)"

    show cho_handjob eyebrows_worried mouth_neutral as cg with d3
    cho "And that's why...{w=0.4} Well, there's something I need to--"

    show cho_handjob eyes_open_forward as cg with d3
    cho "I mean, you have spent so much of your time guiding and encouraging me..."

    show cho_handjob eyebrows_base eyes_open_wide_forward mouth_open as cg with d3
    cho "And you even gave me a luck potion, just so I could finally achieve my dreams!"
    gen "(Did I do that...?)"

    show cho_handjob eyes_closed mouth_neutral as cg with d3
    cho "But then I threw it all away, my urges for sexual gratification became too strong."

    show cho_handjob eyes_open_narrow_down as cg with d3
    cho "I ended up getting carried away..."
    gen "(Been there, done that...)"

    show cho_handjob eyebrows_raised eyes_open_down as cg with d3
    cho "I was sort of running on a high after winning the cup, thinking I could do anything I wanted--"
    gen "No need to apologise [name_cho_genie], you drank that luck potion after all, if there were any consequences I'm sure they would have happened by now."

    show cho_handjob eyebrows_base eyes_open_narrow_down mouth_open as cg with d3
    cho "*Ehm*..."

    show cho_handjob eyebrows_sad mouth_neutral as cg with d3
    cho "It's just--{w=0.2} Well, I thought I should...{w=0.4} Since we ended up having sex..."
    gen "Oh...{w=0.4} I understand what you're trying to say..."

    show cho_handjob eyebrows_sad eyes_open_narrow_forward mouth_angry as cg with d3
    cho "You do?"
    gen "Of course, and there's no need to worry, I've coached my swimmers to not accidentally get anyone pregnant."

    show cho_handjob eyebrows_worried eyes_open_wide_forward mouth_neutral as cg with d3
    cho "That's--{w=0.2} I wasn't even considering that..."
    gen "You weren't?!"

    show cho_handjob eyebrows_base eyes_open_narrow_down as cg with d3
    cho "Not really..."
    gen "So, what is bothering you then?"

    show cho_handjob eyebrows_sad eyes_open_right mouth_open as cg with d3
    cho "It's about the luck potion..."
    gen "Yeah?"

    show cho_handjob eyebrows_worried mouth_neutral as cg with d3

    cho "I never drank any of it."
    gen "I see..."

    stop music fadeout 1.0
    play sound "sounds/scratch.ogg"

    gen "{size=+8}Wait what?!{/size}" with vpunch
    gen "So, that means..."
    cho "*Sigh*... Yes, what actually happened, is--"

    #Cue flashback effect with woosh sound
    #Should we use the replay function that we do for mirror stories for this section? Would we change the day counter at all/set it to 0?
    #Editors note. Sections taken from original writing should not be adjusted, for obvious reasons.

    #Office evening, (Gryffindor practice return event)

    #TODO add cho chibi/doll position, night time etc

    $ renpy.call_replay("cho_quid_E14_retrospection")
    $ renpy.block_rollback() # Otherwise the player would have to replay the entire section if they rolled back here

    show screen blkfade with None

    show cho_handjob cho_body_idle2 penis_soft shirt_open mouth_neutral eyes_open_narrow_down as cg zorder 16

    hide screen blkfade
    with d5

    cho "And, well... You know the rest..."
    gen "*Huh*?"

    show cho_handjob eyebrows_sad mouth_neutral eyes_open_down as cg with d3
    cho "We...{w=0.4} had sex."
    gen "(I feel like I missed some sort of flashback happening.)"

    show cho_handjob cho_body_idle eyebrows_sad mouth_angry eyes_open_wide_forward as cg with d3
    cho "Please don't be mad at me, [name_genie_cho]... I know you had good intentions when you left me that potion."

    show cho_handjob eyebrows_worried eyes_open_narrow_down as cg with d3
    cho "But I just couldn't bear the thought, after all the hurdles that we've gone through, just to end up cheating for the finals."

    show cho_handjob eyes_open_right as cg with d3
    cho "Since I poured it out, I wasn't even going to tell you, but when they found the bottle...{w=0.2} I don't know what came over me."
    gen "So, What you're saying is..."

    show cho_handjob eyes_open_forward mouth_neutral as cg with d3
    gen "There was never any luck potion inside your system, pushing you towards doing all those naughty things?"

    show cho_handjob as cg with d3
    gen "Stripping, and getting off during the game, sucking my cock under the desk with all those teachers inside my office."

    show cho_handjob eyes_open_narrow_down as cg with d3
    cho "..."
    gen "And then riding my cock to your heart's content."
    gen "You did all those things, not due to some assurance from a potion?"
    gen "The potion was merely used as an excuse to make your desires a reality."

    show cho_handjob eyebrows_sad eyes_closed as cg with d3
    cho "..."
    gen "Am I getting that right?"

    show cho_handjob eyes_open_narrow_forward as cg with d3
    cho "Yes, you're completely right [name_genie_cho]..."
    cho "Even though I didn't drink it, I lied, and made you believe that I did... Just so I could fulfill my desires..."

    play sound "sounds/boing05.ogg"
    show cho_handjob penis_hard as cg with vpunch
    gen "{size=-2}Nice...{/size}"

    show cho_handjob eyebrows_worried as cg with d3
    cho "I'm no better than Professor Snape..."

    show cho_handjob mouth_angry as cg with d3
    cho "I'm sorry [name_genie_cho], I shouldn't have--"

    $ _no_shirt = False
    $ _facefuck = False
    menu:
        "-Rip her top off-":
            $ _no_shirt = True

            play sound "sounds/cloth_rip.ogg"

            show cho_handjob no_shirt as cg with d3
            pause .4

            show cho_handjob eyebrows_raised eyes_open_wide_forward mouth_angry as cg with d3
            cho "[name_genie_cho]!"

        "-Don't-":
            pass
    menu:
        "-Punish her throat with your cock-": #Deepthroat
            $ _facefuck = True #used for end variant

            play music "music/dark_trance.ogg" fadein 2 if_changed
            
            call cho_quid_E14_facefuck
            
        "-Finish the demonstration-": #Keep jerking off/masturbate until completion
            #Cho resumes jerking genie off, and you also see the scene of Cho orgasming inside the changing room.

            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

            gen "Put your hand back on that cock, young lady!"

            show cho_handjob eyes_open_forward mouth_angry as cg with d3
            cho "What?! But I thought--"
            gen "Finish the demonstration!"

            show cho_handjob eyebrows_base as cg with d3
            cho "Yes [name_genie_cho]!"

            #Cho starts jerking
            #Dual CG appears
            show cho_masturbate_lockers cho_body_fingering_up mouth_lipbite eyes_narrow_down as cg2 zorder 15
            show cho_handjob cho_body_stroke_idle eyes_open_narrow_down as cg zorder 16
            with d3

            show screen cho_dual_cg("cg2")

            gen "The magic spit!"

            show cho_masturbate_lockers eyebrows_raised mouth_angry eyes_left as cg2
            show cho_handjob eyes_open_down mouth_open as cg
            with d3
            cho "Oh, right!"

            show cho_masturbate_lockers eyebrows_base cho_body_sucking mouth_sucking as cg2
            show cho_handjob cho_body_bending as cg
            with d6
            pause 0.75

            play sound "sounds/drooling.ogg"

            show cho_handjob effects_spitting as cg with d3
            pause 0.25
            show cho_handjob penis_hard_spit_on_tip as cg with d3
            pause 0.5

            show cho_handjob eyes_open_down cho_body_stroke_idle -effects_spitting as cg with d3
            pause 0.5
            show cho_handjob eyebrows_raised cho_body_stroke_up as cg with d3
            pause 0.5

            show cho_handjob eyebrows_sad mouth_neutral eyes_open_right -effects_spitting as cg
            show cho_masturbate_lockers eyebrows_mad cho_body_fingering_up mouth_base eyes_narrow_down as cg2
            with d3

            $ _nude = False
            menu:
                "\"Now, undress!\"":
                    $ _nude = True

                    show cho_handjob cho_body_idle eyes_open_down mouth_angry as cg with d3
                    cho "Yes [name_genie_cho]!"
                    if not _no_shirt:
                        play sound "sounds/cloth_sound3.ogg"
                        show cho_handjob no_shirt as cg with d3
                        pause 0.8
                    play sound "sounds/cloth_sound3.ogg"
                    show cho_handjob no_skirt as cg with d3
                    pause 0.4
                    show cho_handjob cho_body_stroke_up eyes_open_forward as cg with d3

                "\"Now, get going!\"":
                    pass

            #Cho starts jerking (genie)
            #Cho starts fingering pussy (masturbate)
            play background "sounds/slickloop.ogg" fadein 2
            show cho_masturbate_lockers eyes_narrow_left eyebrows_sad as cg2
            show cho_handjob eyes_open_forward mouth_angry speedlines_1 as cg
            with d3
            cho "So, you're--{w=0.2} You're not mad at me?"
            gen "Mad? Are you kidding?"
            gen "I'm--"

            show cho_masturbate_lockers mouth_smile blush_heavy effects_wet as cg2
            show cho_handjob eyebrows_raised eyes_open_wide_forward mouth_open as cg
            with d3

            gen "Proud of you!"

            show cho_masturbate_lockers mouth_lipbite as cg2
            show cho_handjob eyebrows_base eyes_open_forward mouth_angry as cg
            with d3
            cho "You are?!"

            show cho_masturbate_lockers eyes_narrow_down as cg2
            show cho_handjob eyebrows_raised as cg with d3
            cho "But I lied to you, [name_genie_cho]."
            gen "So what?"

            show cho_masturbate_lockers eyes_narrow_left mouth_smile as cg2
            show cho_handjob eyebrows_sad eyes_open_narrow_forward as cg
            with d3
            cho "Are you--{w=0.2} What do you mean?"
            gen "Faster, [name_cho_genie]!"

            #jerking fast
            #Fingering fast
            play background "sounds/slickloopveryfast.ogg" fadein 2
            show cho_masturbate_lockers eyes_down mouth_base effects_hand_move as cg2
            show cho_handjob eyebrows_raised eyes_open_wide_down speedlines_3 as cg
            with d3
            call ctc

            show cho_masturbate_lockers eyes_left mouth_base as cg2
            show cho_handjob eyebrows_base eyes_open_narrow_down mouth_neutral as cg
            with d3
            cho "So...{w=0.4} You're not disappointed--"
            gen "Of course not! You did exactly what I taught you!"

            show cho_masturbate_lockers eyes_narrow_down as cg2
            show cho_handjob eyes_open_forward mouth_neutral as cg
            with d3
            gen "You utilized both your physical and mental capabilities to achieve your desired outcome!"
            gen "Now, if that isn't the true spirit of Ravenclaw, I don't know what is!"

            show cho_masturbate_lockers mouth_smile -effects_wet effects_very_wet as cg2
            show cho_handjob eyes_open_narrow_down mouth_base as cg
            with d3
            cho "Oh, well, I--"
            gen "More spit!"

            show cho_masturbate_lockers mouth_base eyes_narrow_left as cg2
            show cho_handjob eyebrows_base eyes_open_wide_forward mouth_angry as cg
            with d3
            cho "Yes, [name_genie_cho]!"

            stop background
            show cho_masturbate_lockers cho_body_sucking mouth_sucking -effects_hand_move -speedlines_3 as cg2
            show cho_handjob cho_body_bending as cg
            with d6
            pause 0.75

            play sound "sounds/drooling.ogg"

            show cho_handjob effects_spitting as cg with d3
            pause 0.25
            show cho_handjob penis_hard_spit_on_shaft as cg with d3

            gen "Good girl..."

            show cho_masturbate_lockers eyebrows_base eyes_left as cg2
            show cho_handjob cho_body_stroke_down eyes_open_narrow_down mouth_neutral -effects_spitting as cg with d3
            pause 0.5
            show cho_handjob cho_body_stroke_up as cg with d3
            pause 0.5
            show cho_handjob cho_body_stroke_down as cg with d3
            pause 0.5
            show cho_handjob mouth_base cho_body_stroke_up as cg with d3
            pause 0.5
            show cho_handjob eyebrows_raised cho_body_stroke_down as cg with d3

            play background "sounds/slickloopfast.ogg" fadein 2
            show cho_masturbate_lockers cho_body_fingering_up mouth_smile eyes_narrow_down as cg2 with d3
            show cho_handjob speedlines_2 as cg
            pause 0.5
            show cho_masturbate_lockers cho_body_fingering_up eyebrows_sad eyes_narrow_ahegao effects_hand_move as cg2
            show cho_handjob eyes_open_down as cg
            with d3
            cho "S--{w=0.2} So, you'll forgive me? You still want to--"
            gen "Forgive you?"
            gen "I'll...{w=0.2} I'll--"
            gen "Reward you!"

            show cho_handjob eyes_open_wide_down mouth_neutral as cg
            with d3
            call ctc

            show cho_masturbate_lockers cho_body_fingering_up mouth_lipbite as cg2 with d3
            gen "{size=+4}Aaaaah Yeeeees!{/size}"

            stop background
            show cho_handjob cum_precum eyebrows_raised eyes_open_wide_down mouth_angry -speedlines_2 as cg with d3
            cho "{size=+4}Wait!{/size}"

            # Genies cum shoots past Cho through time, space and reason onto the masturbating Cho CG
            #Masturbating Cho CG Cums
            show cho_masturbate_lockers cho_body_fingering_up eyes_narrow_ahegao mouth_ahegao effects_shaking -effects_hand_move as cg2 with d5
            show cho_handjob cum_cumshot as cg with d5
            show cho_masturbate_lockers cum_cumshot as cg2 with d5
            show cho_masturbate_lockers cum_head as cg2 with d5
            show cho_masturbate_lockers cum_torso cum_mouth_ahegao as cg2 with d5
            show cho_masturbate_lockers -cum_cumshot cum_stomach as cg2 with d5
            show cho_handjob -cum_cumshot cum_after as cg with d5
            show cho_masturbate_lockers -effects_shaking as cg2 with d5

            pause 0.5

            gen "*Ah*......."

            show cho_masturbate_lockers mouth_base -cum_mouth_ahegao cum_mouth_base as cg2
            cho "*Gulp*"

            show cho_masturbate_lockers cho_body_idle eyebrows_sad mouth_smile -cum_mouth_base as cg2
            show cho_handjob eyes_open_right as cg
            with d3
            cho "You--{w=0.2} your cum... It's..."
            gen "Looks like we need to work on your reflexes a bit more, [name_cho_genie]."

            show cho_handjob eyebrows_base eyes_open_forward mouth_open as cg with d3
            cho "Work on my--" ("base", "base", "base", "mid")
            gen "Unless you're ready to give up?"

            show cho_handjob cho_body_idle eyebrows_raised eyes_open_wide_forward mouth_angry as cg with d3
            cho "Of--{w=0.2} Of course not!"
            gen "Are you sure? It will be even more intense from now on."

            show cho_handjob mouth_smile as cg with d3
            cho "Yes! I can do it!"
            gen "Then to prove it, I want you to fly ten laps around the pitch..."
            gen "Completely naked!"

            show cho_masturbate_lockers eyes_left eyebrows_mad mouth_open as cg2
            show cho_handjob mouth_angry as cg
            with d3
            cho "Naked?!"
            gen "Did I hear a \"yes coach\"?!"

            show cho_handjob cho_body_idle eyes_open_down mouth_angry as cg with d3
            cho "Yes coach!"

            if not _nude:
                if not _no_shirt:
                    play sound "sounds/cloth_sound3.ogg"
                    show cho_handjob no_shirt as cg with d3
                    pause 0.8
                play sound "sounds/cloth_sound3.ogg"
                show cho_handjob no_skirt as cg with d3
                pause 0.4
                show cho_handjob cho_body_stroke_up eyes_open_forward as cg with d3

            show screen blkfade
            hide screen cho_dual_cg
            hide cg
            hide cg2

    if cho.is_any_worn("clothes"):
        hide cho_main
        $ cho.strip("clothes")

    hide screen blkfade
    with d5
    pause .8

    $ cho_chibi.zorder = 2

    call cho_walk(xpos=437, ypos=400)
    call gen_chibi(flip=False)

    $ cho.set_pose("wand")

    cho @ cheeks blush "Accio [states.cho.ev.quidditch.broom_name]!" ("scream", "base", "base", "L", trans=d3)
    gen "Hold on... Where did your wand just appear from?" ("base", xpos="far_left", ypos="base")
    cho @ cheeks heavy_blush "Oh... *Err*... See you in a bit!" ("angry", "base", "base", "mid")
    hide cho_main
    with d3
    pause .5

    play sound "sounds/boing05.ogg"
    call cho_chibi("hide")
    call gen_chibi("stand_alt", flip=False)
    with d3

    nar "Cho jumps out the window, landing onto her broom, plunging herself on the attached dildo."
    $ cho_chibi.zorder = 3
    
    play sound "sounds/slick_02.ogg"
    with kissiris
    cho "{heart}*Ah*...{heart}"
    gen "*Heh-heh*." ("grin", xpos="far_left", ypos="base")

    show screen blkfade
    with d3

    stop music fadeout 2.0
    call gen_chibi("sit_behind_desk")
    $ cho.set_pose(None)

    if _facefuck:
        nar "You walk up to the window and watch as Cho flies off towards the direction of the Gryffindor tower."
        nar "She returns within a couple of minutes and gives you a triumphant smile. She then takes her clothes and flies off again."
    else:
        play sound "sounds/steps_grass.ogg"
        nar "You grab Cho's clothing and start making your way down to the Quidditch pitch..."
        if game.daytime:
            nar "After catching a couple of glances from the students, you quickly tuck her underwear underneath her outer clothing..."
            nar "Once you reach the pitch, Cho is already circling around it at breakneck speeds..."
            nar "Rather than heading up to the tower, you decide it'd be best to keep a look-out from the entrance-way... Since you'd get a much better angle from below."
            nar "Once Cho finishes, you return her clothing, and then part ways."
        else:
            nar "After catching a couple of glances from the portraits, you quickly tuck her underwear underneath her outer clothing..."
            nar "Once you reach the pitch, you can already see the outline of Cho, circling around it at breakneck speeds..."
            nar "Rather than heading up to the tower, you decide it'd be best to keep a look-out from the entrance-way... Since you'd get a much better angle from below."
            nar "Once Cho finishes, you return her clothing, and then part ways."

    hide screen blkfade
    with d3

    $ states.cho.ev.quidditch.e14_complete = True

    jump end_cho_event

label cho_quid_E14_facefuck:

    gen "You have been very naughty, [name_cho_genie]!"

    show cho_handjob mouth_open as cg with d3
    cho "Yes, I know [name_genie_cho], I'm--"
    gen "You deserve to be punished!"

    show cho_handjob eyebrows_raised eyes_open_wide_forward mouth_angry as cg with d3
    cho "Punished?!"
    gen "Now, lubricate my wood!"

    show cho_handjob eyebrows_base eyes_open_narrow_forward mouth_open as cg with d3
    cho "You want me to--"
    gen "Do it!"

    show cho_handjob eyebrows_base eyes_open_forward mouth_angry as cg with d3
    cho "Yes, [name_genie_cho]!"

    show cho_handjob cho_body_bending as cg with d6
    pause 0.75

    play sound "sounds/drooling.ogg"

    show cho_handjob effects_spitting as cg with d3
    pause 0.25
    show cho_handjob penis_hard_spit_on_tip as cg with d3
    pause 0.5

    show cho_handjob eyes_open_down cho_body_stroke_idle -effects_spitting as cg with d3
    pause 0.5
    show cho_handjob eyebrows_raised cho_body_stroke_up as cg with d3
    pause 0.5
    show cho_handjob cho_body_stroke_down penis_hard_spit_on_shaft as cg with d3
    pause 0.5
    show cho_handjob cho_body_stroke_up as cg with d3
    pause 0.5
    show cho_handjob eyebrows_raised cho_body_stroke_down as cg with d3

    show cho_handjob eyebrows_sad mouth_neutral eyes_open_right as cg with d3

    cho "Alright, I've done it, but--"
    gen "Now, get that mouth over here!"

    #Fade to black (Throatfuck CG)
    show screen blkfade
    hide cg
    with d5

    play sound "sounds/cloth_sound4.ogg"
    pause .5

    cho "[name_genie_cho], what are you--{w=0.2}{nw}"

    play sound "sounds/gltch.ogg"
    with kissiris
    cho "[name_genie_cho], what are you--{fast} *Glick*!!"

    # Throatfuck CG:

    if game.daytime:
        if _no_shirt:
            show cho_facefuck up eyebrows_low eyes_narrow_down no_shirt as cg zorder 15
        else:
            show cho_facefuck up eyebrows_low eyes_narrow_down as cg zorder 15
    else:
        if _no_shirt:
            show cho_facefuck up eyebrows_low eyes_narrow_down no_shirt as cg zorder 15 at color_temperature(1.0)
        else:
            show cho_facefuck up eyebrows_low eyes_narrow_down as cg zorder 15 at color_temperature(1.0)

    hide screen blkfade
    with d5

    gen "I can't believe a pupil of mine would defy me like this!"

    show cho_facefuck eyebrows_worried eyes_narrow_stare as cg with d3 
    cho "*Mfff*!"
    gen "So, to set you straight, I'm going to pump some morals into you!"

    #Genie's dick, halfway down Cho's throat
    play sound "sounds/gag_03.ogg"
    show cho_facefuck mid eyes_shut cheekbulge spit_on_mouth as cg with d3
    cho "*Glck* *Cough*{nw}"

    show cho_facefuck  -cheekbulge as cg
    cho "*Glck* *Cough*{fast} *Cough*{nw}"

    show cho_facefuck cheekbulge as cg
    cho "*Glck* *Cough* *Cough*{fast}{w=0.2}{nw}"

    show cho_facefuck eyes_narrow_down -cheekbulge as cg
    cho "*Glck* *Cough* *Cough*{fast}"

    show cho_facefuck eyes_narrow_stare as cg with d3
    gen "Unfortunately it has to be delivered straight down your throat, but I'm sure you don't mind."
    gen "After all--"

    #Genie's dick three fourths down Cho's throat
    play sound "sounds/gag_04.ogg"
    show cho_facefuck down eyes_shut as cg with d3

    cho "*Gag*"

    show cho_facefuck eyebrows_angry cheekbulge as cg with d3
    cho "*Mmmmmf*!!!{w=0.2}{nw}"
    show cho_facefuck eyebrows_angry -cheekbulge as cg
    cho "*Mmmmmf*!!!{fast}"

    show cho_facefuck as cg with d3
    gen "You went to great lengths, lying to me like that."

    show cho_facefuck eyes_stare as cg with d3
    gen "So I'm sure you have--{w=0.2} *Ngh*--{w=0.2} no problem--"
    gen "With...{w=0.4} my..."

    #Genie's dick fully down Cho's throat
    play sound "sounds/squish_slap_01.ogg"
    show cho_facefuck deep eyes_down as cg with d3
    pause 0.3
    show cho_facefuck eyes_narrow_ahegao as cg with d3

    #Cho Ahegao

    gen "Great length!!!"

    play sound "sounds/gag_02.ogg"
    show cho_facefuck tears eyes_ahegao as cg with d3
    cho "*Glk-Gg-Khh*!"
    gen "There we go!"
    show cho_facefuck eyes_narrow_ahegao blush_heavy as cg with d3
    gen "Just think of this as an advanced version of washing your mouth out with--"
    gen "Oh right... I almost forgot the soap!"

    play sound "sounds/spit.ogg"
    show cho_facefuck spit_on_face as cg with d3
    pause 0.5
    show cho_facefuck eyebrows_worried eyes_ahegao as cg with d3
    gen "Much better... Don't you think?"
    show cho_facefuck eyes_narrow_ahegao blush_choking as cg with d8
    call ctc
    gen "[name_cho_genie]?"

    play sound "sounds/slick_01.ogg"
    show cho_facefuck mid eyes_ahegao -blush_choking as cg with d3
    pause 0.4
    show cho_facefuck mid eyebrows_low as cg with d3
    cho "*Mmmm*..."

    gen "I'm glad you agree..."

    show cho_facefuck eyes_up as cg with d3
    gen "You know... You're quite lucky that you told me about all this as soon as you did."
    gen "It's not healthy to base your whole existence around a lie..."

    show cho_facefuck eyes_stare as cg with d3
    cho "*Hmm*?"

    #Genie pumps down her throat once
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_01.ogg"
    show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
    #pause 0.1
    show cho_facefuck down eyes_ahegao as cg with d3
    #pause 0.1
    show cho_facefuck mid eyes_stare as cg with d3
    #pause 0.1
    show cho_facefuck up as cg with d3
    pause 0.5

    show cho_facefuck eyebrows_angry eyes_narrow_stare as cg with d3
    cho "*Mmmm*..."

    show cho_facefuck eyes_narrow_right as cg with d3
    call ctc
    gen "You know, perhaps I should be blaming myself..."

    show cho_facefuck eyes_narrow_stare as cg with d3
    gen "After all... I made the decision to help you achieve your goals."

    #Genie pumps down her throat once
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_01.ogg"
    show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck down eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_up as cg with d3
    #pause 0.3
    show cho_facefuck up eyes_stare as cg with d3
    #pause 0.5
    gen "I encouraged you..."

    #Genie pumps down her throat once
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_02.ogg"
    show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck down eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_up as cg with d3
    #pause 0.3
    show cho_facefuck up eyes_stare as cg with d3
    #pause 0.5
    gen "To do your very best..."

    show cho_facefuck eyebrows_angry eyes_narrow_down as cg with d3
    cho "*Mmmm*..."
    gen "And you did... You did everything that I asked of you, no matter what..."

    #Genie pumps down her throat once
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_01.ogg"
    show cho_facefuck deep eyebrows_worried eyes_shut as cg with d3
    #pause 0.3
    show cho_facefuck down as cg with d3
    #pause 0.3
    show cho_facefuck mid as cg with d3
    #pause 0.3
    show cho_facefuck up as cg with d3
    pause 0.5
    show cho_facefuck eyes_narrow_stare as cg with d3

    gen "You did all those things, so that you would have enough confidence to do what was necessary to win the cup..."

    show cho_facefuck eyes_narrow_down as cg with d3
    pause 0.8
    show cho_facefuck eyes_narrow_stare as cg with d3
    call ctc

    gen "You stood right here, while I jerked off behind the desk..."


    #Genie pumps once down her throat again
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_07.ogg"
    show cho_facefuck deep eyebrows_angry eyes_narrow_ahegao as cg with d3
    pause 0.3
    show cho_facefuck down eyebrows_worried eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_up as cg with d3
    #pause 0.3
    show cho_facefuck up eyes_stare as cg with d3
    pause 0.5

    gen "You took your clothes off... Giving me a full view of your naked body."

    #Genie pumps once down her throat again
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_04.ogg"
    show cho_facefuck deep eyebrows_angry eyes_narrow_ahegao as cg with d3
    pause 0.3
    show cho_facefuck down eyebrows_worried eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_up as cg with d3
    #pause 0.3
    show cho_facefuck up eyes_stare as cg with d3
    pause 0.5

    gen "And you sucked my cock, as if your life depended on it."

    #Genie pumps once down her throat again
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_01.ogg"
    show cho_facefuck deep eyebrows_angry eyes_narrow_ahegao as cg with d3
    pause 0.3
    show cho_facefuck down eyebrows_worried as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_narrow_up as cg with d3
    #pause 0.3
    show cho_facefuck up eyes_narrow_stare as cg with d3
    pause 0.5

    show cho_facefuck eyebrows_angry eyes_narrow_down as cg with d3
    cho "*Mmhhff*..."
    gen "A student, falling for their coach..."
    gen "It's so cliche it almost makes me--{w=0.4}{nw}"

    #Genie pumps once down her throat again
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_03.ogg"
    show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3

    gen "It's so cliche it almost makes me--{fast} puke!" with vpunch

    play sound "sounds/gag_06.ogg"
    show cho_facefuck deep eyes_shut cheekbulge as cg with d3
    cho "*Glk* *Cough *Cough*"

    show cho_facefuck deep -cheekbulge as cg with d3
    gen "You're lucky I'm into that stuff!"

    play sound "sounds/gag_08.ogg"
    show cho_facefuck deep eyes_down as cg with d3
    cho "*Mmmf*!!"

    show cho_facefuck down as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_narrow_stare as cg with d3
    #pause 0.3
    show cho_facefuck up as cg with d3
    #pause 0.5
    gen "Not puking...{w=0.4} Cliche things."

    show cho_facefuck eyebrows_low eyebrows_low eyes_narrow_down as cg with d3
    cho "*Mhmmm*...."
    gen "So... Here's something cliche, that I've always wanted to tell you..."
    gen "I--"

    #Genie pumps once down her throat again
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_02.ogg"
    show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck down eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_stare as cg with d3
    #pause 0.3
    show cho_facefuck up as cg with d3
    pause 0.5

    gen "Love--"

    #Genie pumps once down her throat again
    play sound "sounds/squish_slap_01.ogg"
    play sound2 "sounds/gag_01.ogg"
    show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck down eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_stare as cg with d3
    #pause 0.3
    show cho_facefuck up as cg with d3
    pause 0.5

    gen "Your throat!"

    play sound "sounds/slick_02.ogg"
    play sound2 "sounds/gag_03.ogg"
    show cho_facefuck deep eyebrows_angry eyes_ahegao as cg with d3
    cho "*Mmmmmfff*!!!" with vpunch

    gen "Sorry to make you disappointed, but I can't go around openly expressing love and affection towards my students."
    gen "I've been told it's highly inappropriate."

    play sound "sounds/gag_09.ogg"
    show cho_facefuck eyes_shut as cg with d3
    cho "*Nnng*!!!!"
    gen "I know, I know... Favouritism isn't that great either, but can you blame me?"
    gen "But that's one of the perks of being a headmaster, I get to break the rules."

    show cho_facefuck eyes_narrow_ahegao as cg with d8
    pause 0.2
    show cho_facefuck eyes_shut as cg with d5

    gen "The only thing they can do is whisper, \"there he goes, showing favouritism towards another student again\"."

    show cho_facefuck blush_choking as cg with d8
    call ctc

    gen "You look very cute when you blush, did anyone ever tell you?"

    play sound "sounds/slick_02.ogg"
    show cho_facefuck mid eyebrows_low eyes_narrow_ahegao as cg with d3
    pause 0.2
    show cho_facefuck eyes_narrow_down -blush_choking as cg with d8
    cho "*Mmmm*...."

    gen "Of course, I only break the rules, when it's for the benefit of my pupils."
    gen "So, when I saw that you had potential, I felt it was my duty to help you reach that potential."

    show cho_facefuck eyes_narrow_stare as cg with d3
    pause 0.5

    gen "But, what do I get in return?"

    show cho_facefuck eyebrows_worried eyes_narrow_down as cg with d3
    pause 0.5

    show cho_facefuck eyes_narrow_stare as cg with d3
    gen "My student, lying her red, raw, little cheeks off, tricking me into having sex with her!"

    show cho_facefuck eyebrows_worried eyes_shut as cg with d3
    pause 0.5
    gen "Wrapping me all around her finger, just so she could wrap her lips around my cock!"
    gen "I hope you're proud of yourself because now you're getting exactly what you asked for..."
    cho "..."
    gen "Look at me when I'm speaking to you!"

    show cho_facefuck eyes_narrow_down as cg with d3
    pause 0.5
    show cho_facefuck eyes_narrow_stare as cg with d3
    pause 0.5

    gen "Now, tell me...{w=0.4} How does it feel?"

    #Genie dick all way down
    play sound "sounds/slick_02.ogg"
    play sound2 "sounds/gag_03.ogg"
    show cho_facefuck down eyes_ahegao as cg with d3
    #pause 0.3
    show cho_facefuck deep eyebrows_worried eyes_ahegao as cg with d3
    call ctc

    gen "Is it how you imagined?"
    gen "Now that you finally got me, are you sure you're good enough to handle it?"

    #Cho face red
    show cho_facefuck blush_choking eyes_narrow_ahegao as cg with d8

    gen "I'm quite high maintenance, you know..."
    gen "It's either all..."

    #Cho head up, blush normal colour, eyes forward
    show cho_facefuck down as cg with d3
    #pause 0.3
    show cho_facefuck mid eyes_up as cg with d3
    #pause 0.3
    show cho_facefuck up eyes_stare -blush_choking as cg with d3
    #pause 0.5

    gen "Or nothing."
    show cho_facefuck eyebrows_low eyes_narrow_stare as cg with d3
    cho "{heart}*Mhhmmff*{heart}...{nw}"
    show cho_facefuck eyes_narrow_down as cg
    cho "{heart}*Mhhmmff*{heart}...{fast}{w=0.4}{nw}"
    show cho_facefuck eyes_narrow_stare as cg
    cho "{heart}*Mhhmmff*{heart}...{fast}"
    gen "So, what do you say?"
    gen "Can--"

    #genie dick half way down
    show cho_facefuck mid eyes_stare as cg with d3

    gen "You--"

    #Genie dick 3/4th way down
    show cho_facefuck down eyes_ahegao as cg with d3

    gen "Handle--"

    #Genie dick all way down
    play sound "sounds/slick_02.ogg"
    play sound2 "sounds/gag_02.ogg"
    show cho_facefuck deep eyes_narrow_ahegao as cg with d3
    pause 0.5
    play sound "sounds/gag_06.ogg"
    show cho_facefuck eyes_shut mouth_bubbles as cg with d3
    pause 0.2
    show cho_facefuck eyes_narrow_ahegao as cg with d3


    gen "Me!?"
    gen "One blink for no, two blinks for yes...{w=0.4} No take backsies."
    show cho_facefuck eyebrows_worried eyes_ahegao as cg with d3
    cho "..."
    gen "Think fast, seeker..."

    pause 0.8

    show cho_facefuck eyes_shut blush_heavy as cg with d3
    pause 0.4
    show cho_facefuck eyes_narrow_ahegao as cg with d8

    pause 0.8

    show cho_facefuck blush_choking as cg with d8

    pause 0.8

    show cho_facefuck eyes_shut as cg with d3
    pause 0.4
    show cho_facefuck eyes_narrow_ahegao as cg with d8
    pause 0.4

    gen "Excellent!"

    #Genie starts fucking her throat, loop/speedlines
    play background "sounds/slickloopfast.ogg" fadein 2
    show cho_facefuck effects_speedlines blush_heavy as cg with d3
    pause 0.4
    show cho_facefuck eyes_ahegao as cg with d3
    cho "*Glick* *Slurp* *Gobble*"
    gen "In that case, I won't just forgive you..."

    show cho_facefuck eyes_shut as cg with d3
    cho "*Slurp* *Slurp* *Gobble*"
    gen "I'll help you explore this side of you... As long as my cock gets to be involved."
    gen "Sounds good to you?"

    show cho_facefuck eyebrows_angry as cg with d3
    cho "{heart}*Gobble* *Glick* *Gobble*{heart}"
    gen "I'll take that open and welcoming throat as a positive response."

    show cho_facefuck eyes_narrow_stare as cg with d3
    cho "*Glick* *Glick* *Gobble*"

    menu:
        "-Teach her a life lesson-":
            gen "Now then..."
            gen "As your first lesson of the day, I must tell you..."

            show cho_facefuck eyebrows_low eyes_narrow_up as cg with d3
            pause 0.5
            gen "If you are looking to explore your sexual side, then that tough exterior you're putting on isn't doing you any favours..."

            show cho_facefuck eyebrows_angry eyes_narrow_left as cg with d3
            cho "*Slurp* *Glick* *Gobble*"
            gen "If you never allow people past your exterior, then nobody will ever get to experience..."

            show cho_facefuck eyebrows_low as cg with d3
            cho "*Gobble* *Slurp* *Gobble*"
            gen "Your very soft, and wet interior..."

            show cho_facefuck eyes_stare as cg with d3
            cho "*Slurp* *Slurp* *Gobble*"

            gen "But no need to worry [name_cho_genie]... I'll help soften you up a bit."
            gen "Starting with your throat!"

            show cho_facefuck eyes_narrow_down as cg with d3
            cho "*Mmmmm*..."

            show cho_facefuck eyebrows_worried eyes_up as cg with d3
            cho "*Mmmmmf*!!!"

            stop background

            show cho_facefuck down eyes_stare -effects_speedlines as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3
            #Genie thrust 3 times into throat

            play sound "sounds/squish_slap_01.ogg"
            play sound2 "sounds/gag_01.ogg"
            show cho_facefuck deep eyes_ahegao as cg with d3
            #pause 0.3
            show cho_facefuck down eyes_narrow_ahegao as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3

            play sound "sounds/squish_slap_01.ogg"
            play sound2 "sounds/gag_03.ogg"
            show cho_facefuck deep as cg with d3
            #pause 0.3
            show cho_facefuck down as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3

            play sound "sounds/slick_01.ogg"
            play sound2 "sounds/gag_02.ogg"
            show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
            play sound "sounds/slick_03.ogg"
            show cho_facefuck cumshot as cg with d3

            gen "*Ah*... Much better..."

            play sound2 "sounds/gag_06.ogg"
            show cho_facefuck eyebrows_angry eyes_shut cumshot2 as cg with d3
            cho "*Cough*"

            show cho_facefuck up throatpie as cg with d4

        "-Destroy her diet-":

            gen "Now then, how about we start this new venture by finding out just how much cum can be pumped down a seeker's throat?"

            play sound "sounds/gag_08.ogg"
            show cho_facefuck eyebrows_worried eyes_stare as cg with d3
            cho "*Mmmf*!!"

            gen "Don't--{w=0.2} *Ah*...{w=0.4} Don't worry [name_cho_genie]...{w=0.4} you've deserved a cheat day on your diet!"
            gen "Winner winner, here comes dinner!"

            show cho_facefuck eyes_up as cg with d3
            cho "*Mmmmmf*!!!"

            stop background

            show cho_facefuck down eyes_stare -effects_speedlines as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3
            #Genie thrust 3 times into throat

            play sound "sounds/squish_slap_01.ogg"
            play sound2 "sounds/gag_01.ogg"
            show cho_facefuck deep eyes_ahegao as cg with d3
            #pause 0.3
            show cho_facefuck down eyes_narrow_ahegao as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3

            play sound "sounds/squish_slap_01.ogg"
            play sound2 "sounds/gag_03.ogg"
            show cho_facefuck deep as cg with d3
            #pause 0.3
            show cho_facefuck down as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3

            play sound "sounds/slick_01.ogg"
            play sound2 "sounds/gag_02.ogg"
            show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
            play sound "sounds/slick_03.ogg"
            show cho_facefuck cumshot as cg with d3

            gen "*Ah*...{w=0.4} That hit the spot..."
            gen "Although with this amount...{w=0.4} perhaps we should call it a cheat week instead."

            play sound2 "sounds/gag_06.ogg"
            show cho_facefuck eyebrows_angry eyes_shut cumshot2 as cg with d3
            cho "*Cough*"

            show cho_facefuck up throatpie as cg with d4

        "-Claim her as your prize-":

            gen "To think that the cup wouldn't be enough of a prize for you...{w=0.4} You just had to claim your coach as well."

            show cho_facefuck eyebrows_low eyes_narrow_up as cg with d3
            cho "{heart}*Glick* *Mfff* *Slurp*{heart}"
            gen "Not that I'm complaining, you're quite the golden cup yourself."

            show cho_facefuck eyes_narrow_down as cg with d3
            cho "*Glick* *Slurp* *Slurp*"
            gen "In fact... Why don't we put you on display right here, as my trophy."

            show cho_facefuck eyes_stare as cg with d3
            pause 0.5

            gen "Right next to my desk, for both myself and others to admire."

            show cho_facefuck eyebrows_worried eyes_narrow_down as cg with d3
            cho "*Slurp* *Slurp* *Gulp*"
            gen "I have quite a few notable people coming through my office, you know."

            show cho_facefuck eyes_narrow_right as cg with d3
            cho "*Slurp* Gobble* *Slurp*"

            gen "And I'm sure even more would find their way here, once rumours start spreading."

            show cho_facefuck eyes_narrow_stare as cg with d3
            cho "*Slurp* *Gulp* *Slurp*"
            gen "Of course... Trophies aren't just good for admiring."

            show cho_facefuck eyebrows_low eyes_narrow_stare as cg with d3
            cho "*Slurp* *Gobble* *Slurp*"
            gen "You can also use them..."
            gen "As a vessel!"

            show cho_facefuck eyes_narrow_down as cg with d3
            cho "*Mmmmm*..."

            show cho_facefuck eyebrows_worried eyes_up as cg with d3
            cho "*Mmmmmf*!!!"

            stop background

            show cho_facefuck down eyes_stare -effects_speedlines as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3
            #Genie thrust 3 times into throat

            play sound "sounds/squish_slap_01.ogg"
            play sound2 "sounds/gag_01.ogg"
            show cho_facefuck deep eyes_ahegao as cg with d3
            #pause 0.3
            show cho_facefuck down eyes_narrow_ahegao as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3

            play sound "sounds/squish_slap_01.ogg"
            play sound2 "sounds/gag_03.ogg"
            show cho_facefuck deep as cg with d3
            #pause 0.3
            show cho_facefuck down as cg with d3
            #pause 0.3
            show cho_facefuck mid as cg with d3
            #pause 0.3
            show cho_facefuck up as cg with d3

            play sound "sounds/slick_01.ogg"
            play sound2 "sounds/gag_02.ogg"
            show cho_facefuck deep eyebrows_worried eyes_narrow_ahegao as cg with d3
            play sound "sounds/slick_03.ogg"
            show cho_facefuck cumshot as cg with d3

            gen "*Ah*...{w=0.8} Victory sure tastes sweet, doesn't it?"

            play sound2 "sounds/gag_06.ogg"
            show cho_facefuck eyebrows_angry eyes_shut cumshot2 as cg with d3
            cho "*Cough*"

            show cho_facefuck up throatpie as cg with d4

    stop music fadeout 1
    show screen blkfade
    with d5
    hide cg

    play sound "sounds/gltch.ogg"
    pause 0.4

    gen "On your feet, [name_cho_genie]!"
    cho "*Ah*...{w=0.4} Yes--{w=0.2} Yes, [name_genie_cho]..."
    cho "Let me just...{w=0.4} wipe my face..."

    play sound "sounds/cloth_sound3.ogg"
    pause 0.8

    if game.daytime:
        if _no_shirt:
            show cho_handjob no_shirt cho_body_idle eyebrows_base mouth_smile eyes_open_forward penis_soft as cg zorder 16
        else:
            show cho_handjob cho_body_idle eyebrows_base mouth_smile eyes_open_forward penis_soft as cg zorder 16
    else:
        if _no_shirt:
            show cho_handjob no_shirt cho_body_idle eyebrows_base mouth_smile eyes_open_forward penis_soft as cg zorder 16 at color_temperature(1.0)
        else:
            show cho_handjob cho_body_idle eyebrows_base mouth_smile eyes_open_forward penis_soft as cg zorder 16 at color_temperature(1.0)

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    hide screen blkfade
    with d5

    cho "That was...{w=0.4} Incredible..."

    show cho_handjob eyes_open_down mouth_neutral as cg with d3
    cho "I've always imagined...{w=0.4} But I never thought I'd be able to do that."
    gen "You wanted to explore new things... So I figured, why not start with your throat."

    show cho_handjob mouth_base as cg with d3
    cho "I...{w=0.4} I just never thought--"

    show cho_handjob eyes_open_wide_forward as cg with d3
    cho "How did you know it would fit?"
    gen "You never know until you try...{w=0.4} That's what I've always said."

    show cho_handjob eyebrows_raised eyes_open_forward as cg with d3
    cho "You've always said that, have you?"
    gen "Yep, it's a bit of a motto of mine at this--"
    gen "I mean...{w=0.4} I just knew! I've totally never and will never put my penis anywhere near somebody else's throat."

    show cho_handjob mouth_neutral as cg with d3
    cho "Really?"

    show cho_handjob eyebrows_sad eyes_open_narrow_down as cg with d3
    cho "That's disappointing..."

    show cho_handjob eyes_open_narrow_forward mouth_base as cg with d3
    cho "I don't think I could bear the thought that I'd be the only one to get my throat blessed by \"The great Albus Dumbledore\"."
    gen "In that case, I was just being sarcastic."

    show cho_handjob eyebrows_angry mouth_smile as cg with d3
    cho "Good!"

    show cho_handjob eyes_open_right as cg with d3
    cho "If not her throat, I think Hermione's ass could do with a blessing..."

    show cho_handjob eyes_closed as cg with d3
    cho "There's a stick in there that I believe only you'd be able to dislodge."
    gen "I'm sure you could do it if you tried hard enough."

    show cho_handjob eyebrows_worried as cg with d3
    cho "I wish..."
    gen "..."

    show cho_handjob eyes_open_down mouth_angry as cg with d3
    cho "I mean, I wish there was anything I could do about it!"
    gen "I'm sure the girl who just took a cock all the way down her throat would do it very easily."
    gen "Or are you telling me, you're not that girl?"

    show cho_handjob eyebrows_raised eyes_open_wide_forward as cg with d3
    cho "What do you mean? Of course I am!"
    gen "I don't know... That girl would've been up for a challenge like that, I'm sure of it."
    gen "So, where did she go?"

    show cho_handjob eyebrows_base eyes_open_narrow_forward as cg with d3
    cho "I am that girl! But even I know when--"
    gen "Really?"
    gen "Then prove it by flying ten laps around the Gryffindor tower, completely naked!"

    show cho_handjob eyebrows_raised eyes_open_wide_forward as cg with d3
    cho "Naked?!"
    cho "What's that supposed to achieve?"
    gen "Did I hear a \"yes coach\"?!"

    show cho_handjob cho_body_idle eyes_open_down mouth_angry as cg with d3
    cho "Yes coach!"

    if not _no_shirt:
        play sound "sounds/cloth_sound3.ogg"
        show cho_handjob no_shirt as cg with d3
        pause 0.8
    play sound "sounds/cloth_sound3.ogg"
    show cho_handjob no_skirt as cg with d3
    pause 0.4
    show cho_handjob eyes_open_forward as cg with d3

    $ states.cho.status.deepthroat = True
    $ states.cho.status.gokkun = True

    show screen blkfade
    with d5
    hide cg

    return
