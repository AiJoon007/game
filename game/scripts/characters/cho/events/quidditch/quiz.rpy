
### Quidditch Quiz ###

label cho_quiz:
    cho "" (xpos="mid",ypos="base", trans=fade)

    $ states.cho.ev.quiz.correct_answers = 0

    if states.cho.ev.quiz.checkpoint:
        gen "I'm ready to show you what I know about Quidditch..." ("base", xpos="far_left", ypos="head")
        cho "Great!" ("base", "base", "base", "L")
        cho "Let's begin..." ("open", "wide", "raised", "mid")
        jump cho_quiz_checkpoint

    # Intro
    if not states.cho.ev.quiz.e1_complete:
        $ states.cho.ev.quiz.e1_complete = True
        gen "It's time to start our first lesson, Miss Chang." ("base", xpos="far_left", ypos="head")
        cho "Okay then, where do we begin?" ("smile", "base", "base", "mid")
        gen "Well, first we'll need to discuss what you'll do for me in this arrangement of ours..." ("base", xpos="far_left", ypos="head")
        cho "You need me to do something for your assistance, professor?" ("soft", "base", "base", "mid")
        gen "Yes, my time is quite a commodity these days, so I want to make sure that the ones I spend it on are actually prepared to do what it takes to achieve their goals." ("base", xpos="far_left", ypos="head")
        cho "Right... I suppose that's fair." ("open", "closed", "base", "mid")
        gen "Great! Then I'd like you to start selling favours to me for my service." ("base", xpos="far_left", ypos="head")
        cho "Favours? What kind of favours?" ("annoyed", "narrow", "raised", "mid")
        gen "Nothing that Miss Granger hasn't had any issues with." ("base", xpos="far_left", ypos="head")

        if states.her.public_level < 16:
            cho "(So nothing sexual, at the very least...)" ("grin", "base", "base", "R")
        else:
            cho "(I hope it's nothing sexual. I've heard some rumours about Granger...)" ("quiver", "base", "worried", "R")

        cho "Well... if Granger could do it, so can I!" ("open", "closed", "base", "mid")
        cho "And better!" ("soft", "narrow", "base", "mid")
        gen "Great!" ("base", xpos="far_left", ypos="head")
        cho "And longer!" ("smile", "narrow", "base", "mid")
        gen "Longer?" ("base", xpos="far_left", ypos="head")
        cho "And harder!" ("angry", "narrow", "angry", "mid", trans=hpunch)
        gen "(Oh my...)" ("base", xpos="far_left", ypos="head")
        cho "But..." ("soft", "closed", "base", "mid")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        cho "I'll only do it if we actually win!" ("soft", "narrow", "raised", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "(Damn it! Always a catch...)" ("angry", xpos="far_left", ypos="head")
        gen "Fine..." ("base", xpos="far_left", ypos="head")
        gen "Okay, so...{w} I'll help you win quidditch matches, and in return, you'll sell me favours..." ("base", xpos="far_left", ypos="head")
        gen "Sounds good?" ("base", xpos="far_left", ypos="head")
        cho "Yes, that's the deal." ("smile", "base", "base", "mid")
        cho "Although..." ("annoyed", "base", "worried", "down")
        gen "Although?" ("base", xpos="far_left", ypos="head")
        cho "Well, how do I know that you actually know anything about the game?" ("open", "base", "base", "mid")
        cho "I mean...{w} I never really saw you showing too much interest before..." ("soft", "narrow", "base", "mid")
        gen "About what?" ("base", xpos="far_left", ypos="head")
        cho "Quidditch!" ("angry", "closed", "angry", "mid", trans=hpunch)
        gen "Ah, yes... Quidditch.{w} It's like the Wizards' version of Basketball, right?" ("grin", xpos="far_left", ypos="head")
        cho "Basketball?!" ("clench", "base", "raised", "mid")
        cho "Is that the muggle sport nobody cares about?" ("soft", "narrow", "raised", "L")
        gen "Nobody cares?{w} What are you...{w} Haven't you seen \"Space Jam\"?" ("angry", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "base", "raised", "mid")
        gen "Come on." ("angry", xpos="far_left", ypos="head")
        gen "Well..." ("base", xpos="far_left", ypos="head")

    # Repeat
    else:
        gen "I'm ready to make my case on how Quidditch is a knock-off of basketball..." ("base", xpos="far_left", ypos="head")
        cho "Really sir... again?" ("open", "narrow", "angry", "L")
        gen "Of course, it's an important subject for your education..." ("base", xpos="far_left", ypos="head")
        cho "I can't really see how, but I'm sure you know what you're talking about..." ("open", "base", "base", "mid")
        gen "Alright, so..." ("base", xpos="far_left", ypos="head")

    play music "music/ominous_music.ogg" if_changed
    stop weather

    $ confidence_meter = 50
    show screen meter(confidence_meter)

    # Question 1
    menu:
        "-There are five players on each team...-":
            gen "Two teams with each one having five players on the court at one time..." ("base", xpos="far_left", ypos="head")
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            cho "Whilst Quidditch does have two teams...{w=0.5} there are seven players on each..." ("annoyed", "narrow", "raised", "mid")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(1.0)
            play sound "sounds/kung-fu-punch.ogg"
            gen "Ah,{w=0.4} well..." ("angry", xpos="far_left", ypos="head")

        "-[states.cho.ev.quiz.hint]At the start of the game the ball gets thrown in the air...-":
            $ states.cho.ev.quiz.correct_answers += 1

            gen "You start the game by the referee throwing the ball into the air..." ("base", xpos="far_left", ypos="head")
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(0.5)
            play sound "sounds/hmm1.ogg"
            $ renpy.block_rollback()
            cho "I guess that's kind of similar..." ("smile", "base", "raised", "mid")
            $ renpy.music.set_volume(1.0)
            gen "It is? I mean, yes... and also..." ("grin", xpos="far_left", ypos="head")


    # Question 2
    menu:
        "-It's played on a rectangular court...-":
            gen "The game is played on a rectangular court..." ("base", xpos="far_left", ypos="head")
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            cho "Well, that's not similar at all then. The Quidditch pitch is oval-shaped..." ("annoyed", "narrow", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(1.0)
            play sound "sounds/kung-fu-punch.ogg"
            gen "Of course!{w=0.4}... and in basketball..." ("angry", xpos="far_left", ypos="head")

        "-[states.cho.ev.quiz.hint]You may not go out of bounds with the ball...-":
            $ states.cho.ev.quiz.correct_answers += 1

            gen "You're not allowed outside the bounds whilst holding the ball, or you'll have to hand it over to the opponent team..." ("base", xpos="far_left", ypos="head")
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            play sound "sounds/hmm1.ogg"
            cho "I guess that's pretty much the same as in Quidditch..." ("base", "base", "raised", "L")
            $ renpy.music.set_volume(1.0)
            gen "Great! I mean, obviously! And..." ("base", xpos="far_left", ypos="head")


    # Question 3
    menu:
        "-[states.cho.ev.quiz.hint]Each player takes a certain position...-":
            $ states.cho.ev.quiz.correct_answers += 1

            gen "Each player takes a certain position." ("base", xpos="far_left", ypos="head")
            gen "There are defensive positions..." ("base", xpos="far_left", ypos="head")
            gen "And offensive positions..." ("base", xpos="far_left", ypos="head")
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            play sound "sounds/hmm2.ogg"
            cho "I guess Quidditch has something like that..." ("base", "narrow", "base", "R")
            $ renpy.music.set_volume(1.0)
            gen "Exactly, which is obviously why I brought it up, and lastly..." ("grin", xpos="far_left", ypos="head")

        "-You can't run with the ball unless you dribble or pass...-":
            gen "You can't run whilst holding the ball,{w=0.4} you need to pass it or dribble..." ("base", xpos="far_left", ypos="head")
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            cho "Well, you can move with the ball freely without passing in Quidditch, that's why we have the beaters..." ("annoyed", "narrow", "raised", "mid")
            cho "To make the opponents drop the ball." ("open", "narrow", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(1.0)
            play sound "sounds/kung-fu-punch.ogg"
            gen "Ah!{w=0.4} Well, I guess that is different... Lastly though..." ("angry", xpos="far_left", ypos="head")


    # Question 4
    menu:
        "-You can't touch your opponent...-":
            gen "You're not allowed to touch your opponent, or it would be counted as a foul..." ("base", xpos="far_left", ypos="head")
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            cho "Well, that's definitely not the case in Quidditch..." ("open", "closed", "raised", "mid")
            cho "Except for excessive use of elbows..." ("annoyed", "narrow", "base", "L")
            with hpunch
            show screen swear_bubble(random.randint(0, 4))
            with d1
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            gen "Well...{w=0.4}" ("angry", xpos="far_left", ypos="head")
            gen "Fine..." ("base", xpos="far_left", ypos="head")

        "-[states.cho.ev.quiz.hint]You score by getting the ball through a hoop...-":
            $ states.cho.ev.quiz.correct_answers += 1

            gen "The way you score is by getting the ball through a hoop." ("base", xpos="far_left", ypos="head")
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            $ renpy.music.set_volume(0.5)
            $ renpy.block_rollback()
            play sound "sounds/hmm3.ogg"
            cho "*Hmm*... Well, that's the same as in Quidditch, I suppose." ("smile", "base", "base", "mid")
            gen "Naturally..." ("grin", xpos="far_left", ypos="head")


    pause 1.0
    hide screen meter
    with d3

    $ renpy.music.set_volume(1.0)

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    call weather_sound

    $ renpy.block_rollback()

    # Failed
    if states.cho.ev.quiz.correct_answers <= 1: # 0-1 answers correct?
        gen "Well, I'm sure that the winning conditions are pretty similar at least..." ("base", xpos="far_left", ypos="head")
        cho "And what are the winning conditions?" ("base", "base", "base", "mid")
        gen "You win by having the most number of points when the time is over." ("base", xpos="far_left", ypos="head")
        cho "Well, in Quidditch the game doesn't end until the snitch is caught, so it could technically go on forever." ("open", "narrow", "raised", "mid")
        cho "So in short... nothing like basketball." ("annoyed", "closed", "base")
        gen "The game doesn't end until the snitch is caught?" ("base", xpos="far_left", ypos="head")
        cho "Yes..." ("base", "base", "base", "mid")
        gen "Well, that is stupid..." ("base", xpos="far_left", ypos="head")
        cho "Yes, that bit is kind of stupid..." ("annoyed", "base", "worried", "down")
        cho "Anyway..." ("base", "closed", "base")
        cho "I didn't come here to listen to you talk about basketball..." ("annoyed", "base", "base", "downR")
        gen "Right..." ("base", xpos="far_left", ypos="head")
        cho "I came for you to tutor me..." ("annoyed", "narrow", "angry", "L")
        gen "(Perhaps it might be worth trying to learn a bit more about Quidditch before I ruin this whole thing...)" ("base", xpos="far_left", ypos="head")
        gen "Oh, well... look at the time!" ("grin", xpos="far_left", ypos="head")
        cho "What?" ("open", "wide", "raised", "mid")
        gen "You've made me go on about basketball for such a long time, so we're already at the end of today's session." ("grin", xpos="far_left", ypos="head")
        cho "But we didn't even get to any tutoring..." ("annoyed", "narrow", "base", "mid")
        gen "We'll get there, don't you worry... next time..." ("base", xpos="far_left", ypos="head")
        cho "...{w=0.4}Fine." ("annoyed", "base", "base", "mid")
        cho "Bye then professor..." ("annoyed", "base", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        gen "(What am I supposed to do now... I clearly know fuck-all about Quidditch...)" ("angry", xpos="far_left", ypos="head")
        gen "(I'd rather not ask Snape... but unless there's someone else that I could ask without sounding like a complete dumb-ass it might have to do...)" ("base", xpos="far_left", ypos="head")

        $ states.cho.ev.quiz.lost = True

        if quidditchguide_ITEM.used:
            gen "(Why didn't I just follow the book? Serves me right...)" ("base", xpos="far_left", ypos="head")
        elif quidditchguide_ITEM.owned > 0:
            gen "(Maybe I should read the book I bought...)" ("base", xpos="far_left", ypos="head")
        elif item_store_intro_done:
            gen "(Actually, perhaps the twins might be a better idea...)" ("base", xpos="far_left", ypos="head")


    # Success! Or did you?
    elif states.cho.ev.quiz.correct_answers == 4:

        $ states.cho.ev.quiz.correct_answers = 0

        show screen meter(confidence_meter)
        gen "So, as you can see, Basketball and Quidditch are pretty much the same game..." ("base", xpos="far_left", ypos="head")
        cho "I'm sure that can't be right..." ("annoyed", "base", "base", "mid")
        cho "I'll have to look up this \"Space Jamming\"...{w=1.0} thing." ("open", "narrow", "base", "mid")
        gen "You should! It has Bugs Bunny in it!" ("grin", xpos="far_left", ypos="head")
        cho "And now you stopped making sense again..." ("annoyed", "base", "raised", "L")
        cho "Also, I'm still quite unsure if you actually know Quidditch or are just trying to confuse me with Basketball terms..." ("annoyed", "narrow", "raised", "mid")
        show screen meter(75)
        pause .3
        call bld
        gen "(Fuck, she's onto me!)" ("angry", xpos="far_left", ypos="head")
        gen "Of course I'm not... I'll prove it to you!" ("grin", xpos="far_left", ypos="head")
        show screen meter(50)
        pause .5
        call bld
        gen "(Wait, why did I say that?)" ("angry", xpos="far_left", ypos="head")
        cho "..." ("smile", "base", "raised", "mid")
        cho "Okay then, show me what you know..." ("smile", "base", "raised", "mid")

        jump cho_quiz_checkpoint

    # Failed
    else: # 2-3 answers correct.
        cho "I guess it has some similarities..." ("annoyed", "narrow", "worried", "mid")
        gen "Pretty much the same game I'd say..." ("base", xpos="far_left", ypos="head")
        cho "I wouldn't say that... You fly for one in quidditch..." ("open", "base", "base", "mid")
        gen "You do?!?" ("angry", xpos="far_left", ypos="head")
        cho "Very funny professor, of course you do..." ("annoyed", "base", "raised", "down")
        cho "Anyway, weren't you supposed to tutor me?..." ("annoyed", "narrow", "base", "L")
        gen "Oh, right..." ("base", xpos="far_left", ypos="head")
        gen "(Perhaps it might be worth trying to learn a bit more about Quidditch before I ruin this whole thing...)" ("base", xpos="far_left", ypos="head")
        gen "Oh, well... look at the time!" ("grin", xpos="far_left", ypos="head")
        cho "What?" ("upset", "closed", "worried")
        gen "You've made me go about basketball for such a long time, so we're already at the end of today's session." ("grin", xpos="far_left", ypos="head")
        cho "But we didn't even get to any tutoring..." ("annoyed", "narrow", "angry", "mid")
        gen "We'll get there, don't you worry... next time..." ("base", xpos="far_left", ypos="head")
        cho "...{w=0.4}Fine." ("annoyed", "narrow", "base", "mid")
        cho "Bye then professor..." ("annoyed", "base", "base", "R")

        # Cho leaves.
        call cho_walk(action="leave")

        gen "(The fuck am I supposed to do now... I feel like that must've been a fluke, I know nothing about Quidditch...)" ("angry", xpos="far_left", ypos="head")
        gen "(I'd rather not ask Snape... but unless there's someone else that I could ask without sounding like a complete dumb-ass it might have to do...)" ("base", xpos="far_left", ypos="head")

        $ states.cho.ev.quiz.lost = True

        # Read the book.
        if quidditchguide_ITEM.used:
            gen "(Why didn't I just follow the book?{w} Serves me right...)" ("base", xpos="far_left", ypos="head")

        # Got the book but not read.
        elif quidditchguide_ITEM.owned > 0:
            gen "(Maybe I should read the book I bought...)" ("base", xpos="far_left", ypos="head")

        # Visited their shop before.
        elif item_store_intro_done:
            gen "(Actually, perhaps the twins might be a better idea...)" ("base", xpos="far_left", ypos="head")

    $ states.cho.busy = True

    jump main_room_menu



### Quiz - Part 2 ###

label cho_quiz_checkpoint:
    $ confidence_meter = 50
    show screen meter(confidence_meter)

    play music "music/determined_pursuit_loop.ogg" if_changed
    stop weather

    # Intro
    if not states.cho.ev.quiz.e2_complete:
        $ states.cho.ev.quiz.e2_complete = True
        cho "You do seem to know some basic things, but do you know anything about the balls?" ("open", "narrow", "base", "mid")
        gen "I could probably teach you quite a lot..." ("base", xpos="far_left", ypos="head")
        gen "You should never neglect the balls." ("grin", xpos="far_left", ypos="head")
        cho "In that case..." ("base", "base", "base", "mid")

    cho "My position on the team is seeker, it is my job to catch the \"Blank\" to end the game and score our team 150 points." ("open", "base", "base", "L")
    show screen meter(confidence_meter)

    # Question 1
    menu:
        "-Stitch-":
            gen "Stitch?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "No..." ("open", "narrow", "angry", "mid")
            gen "Oh wait, that's that blue alien thing, isn't it?" ("angry", xpos="far_left", ypos="head")
            cho "I don't know what a stitch is, sorry sir..." ("soft", "narrow", "worried", "R")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "Next question..." ("open", "base", "raised", "down")

        "-Lich-":
            gen "Lich?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "A Lich? Like those undead skeletal creatures?" ("open", "narrow", "raised", "mid")
            gen "Oh, that's what I said?" ("angry", xpos="far_left", ypos="head")
            gen "I must've had a PTSD flashback from my tomb raiding days..." ("base", xpos="far_left", ypos="head")
            cho "You've been tomb raiding?" ("soft", "base", "raised", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            gen "Of course not..." ("base", xpos="far_left", ypos="head")
            cho "Next question..." ("open", "base", "raised", "down")

        "-[states.cho.ev.quiz.hint]Snitch-":
            gen "Snitch?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            play sound "sounds/gasp.ogg"
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            cho "Yes!" ("smile", "wide", "base", "mid")
            gen "Well then, surely that should show you how superi--" ("grin", xpos="far_left", ypos="head")
            cho "Next question..." ("open", "closed", "base", "down")
            $ states.cho.ev.quiz.correct_answers += 1

    cho "Apart from the snitch, there are two other types of balls on the pitch, what are they called?" ("open", "base", "angry", "mid")

    # Question 2
    menu:
        "-Butter and Waffles-":
            gen "Butter and Waffles?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "Sir?" ("annoyed", "narrow", "raised", "mid")
            gen "Sorry, I didn't have any lunch..." ("base", xpos="far_left", ypos="head")
            gen "Actually, I can't even remember the last time I ate..." ("angry", xpos="far_left", ypos="head")
            cho "Well, you're obviously wrong..." ("soft", "narrow", "raised", "R")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "Next question..." ("open", "base", "raised", "down")

        "-[states.cho.ev.quiz.hint]Bludger and Quaffle-":
            gen "Bludger and Quaffle?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            play sound "sounds/gasp.ogg"
            cho "Yes!" ("smile", "wide", "base", "mid")
            gen "Great! Then let's get started with the--" ("grin", xpos="far_left", ypos="head")
            cho "Next question..." ("open", "base", "raised", "down")
            $ states.cho.ev.quiz.correct_answers += 1

        "-Quabble and Bluffer-":
            gen "Quabble and bluffer?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "I think you got some letters mixed up there..." ("soft", "narrow", "raised", "R")
            gen "Quibble and Blodger?" ("base", xpos="far_left", ypos="head")
            cho "No, that's also not--" ("annoyed", "base", "base", "up")
            gen "Qacker and Blugger?" ("base", xpos="far_left", ypos="head")
            cho "Professor..." ("annoyed", "narrow", "angry", "mid")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "Next question..." ("open", "base", "raised", "down")

    cho "Let's do some history..." ("base", "base", "base", "mid")
    gen "I am made out of history, this should be a breeze..." ("grin", xpos="far_left", ypos="head")
    cho "Okay then..." ("smile", "base", "raised", "mid")
    cho "A game of Quidditch doesn't finish until the Snitch is caught; therefore it could go on forever..." ("open", "base", "base", "down")
    cho "In the longest ever match played, they had to constantly bring on substitutes to let the players get some sleep..." ("open", "base", "base", "mid")
    cho "For how long did the game go on for?" ("base", "narrow", "raised", "mid")

    # Question 3
    menu:
        "-[states.cho.ev.quiz.hint]Three Months-":
            gen "Three months?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            play sound "sounds/gasp.ogg"
            cho "Yes!" ("smile", "wide", "base", "mid")
            cho "That's impressive, how did you know that one?" ("grin", "happyCl", "base", "mid")
            gen "I feel like there weren't that many realistic options available this time..." ("base", xpos="far_left", ypos="head")
            cho "Okay... I'm not sure what that means..." ("soft", "narrow", "worried", "mid")
            cho "Anyway, final question..." ("open", "base", "raised", "down")
            $ states.cho.ev.quiz.correct_answers += 1

        "-Seven Years-":
            gen "Seven years?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "How long?! That's the same amount of time a student stays at Hogwarts!" ("clench", "wide", "base", "mid")
            gen "Oh right, I don't know what I was thinking..." ("base", xpos="far_left", ypos="head")
            gen "Seven just seems like the magical right answer most of the time..." ("base", xpos="far_left", ypos="head")
            cho "Not in this case..." ("annoyed", "narrow", "angry", "mid")
            cho "Anyway, final question..." ("open", "base", "raised", "down")

        "-Two Minutes-":
            gen "Two minutes?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "What?" ("angry", "base", "raised", "mid")
            gen "What?" ("angry", xpos="far_left", ypos="head")
            cho "Sir, what sport lasts only two minutes?" ("soft", "narrow", "angry", "mid")
            gen "A Splurge race?" ("base", xpos="far_left", ypos="head")
            cho "Never heard of it, is it anything like that basketball thing?" ("annoyed", "narrow", "base", "mid")
            gen "Well, balls have a big role in it..." ("grin", xpos="far_left", ypos="head")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "I'll have to take your word on that one..." ("soft", "narrow", "angry", "R")
            cho "Anyway... final question..." ("open", "base", "raised", "down")

    cho "As you know, you may not go outside the bounds with the ball during the game, or you'd have to hand it over to the opposition..." ("open", "base", "base", "down")
    cho "But what is the penalty if the defensive goes out of bounds?" ("smile", "narrow", "angry", "mid")

    # Question 4
    menu:
        "-Three Months-":
            gen "Three months?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "Three months, what?" ("annoyed", "narrow", "angry", "mid")
            gen "Three months...{w=0.5} in prison?" ("base", xpos="far_left", ypos="head")
            cho "Professor, you're not going to get a prison sentence unless you do something that's actually illegal..." ("open", "narrow", "angry", "L")
            gen "What if the Quidditch pitch was in prison?" ("base", xpos="far_left", ypos="head")
            gen "And you flew outside the prison boundaries..." ("base", xpos="far_left", ypos="head")
            gen "Did you consider that?" ("grin", xpos="far_left", ypos="head")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "I think you're going off track a bit..." ("annoyed", "narrow", "raised", "mid")
            gen "Or off the pitch..." ("grin", xpos="far_left", ypos="head")

        "-A free shot at the goal-":
            gen "Free goal shot?" ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            cho "No, that's not right..." ("soft", "narrow", "raised", "L")
            gen "Then what is it?" ("base", xpos="far_left", ypos="head")
            cho "Well, I don't know..." ("angry", "narrow", "worried", "down")
            gen "How am I supposed to then?" ("angry", xpos="far_left", ypos="head")
            $ confidence_meter -= 12
            show screen meter(confidence_meter)
            play sound "sounds/kung-fu-punch.ogg"
            cho "I'm not sure what else to tell you..." ("open", "closed", "base", "mid")

        "-[states.cho.ev.quiz.hint]I don't know...-":
            gen "Uh... I don't know..." ("base", xpos="far_left", ypos="head")
            $ renpy.block_rollback()
            $ confidence_meter += 12
            show screen meter(confidence_meter)
            play sound "sounds/gasp.ogg"
            cho "That's right!" ("smile", "wide", "base", "mid")
            gen "What?" ("angry", xpos="far_left", ypos="head")
            cho "Nobody knows what happens! There isn't any rule for it..." ("open", "wide", "raised", "L")
            gen "Why wouldn't there be a rule for it?" ("angry", xpos="far_left", ypos="head")
            cho "Why would the defensive leave the pitch... they'd just leave the goal open..." ("soft", "base", "worried", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            $ states.cho.ev.quiz.correct_answers += 1

    pause 1.0
    hide screen meter
    with d3

    $ renpy.music.set_volume(1.0)

    call music_block

    call weather_sound

    $ renpy.block_rollback()

    # Success
    if states.cho.ev.quiz.correct_answers >= 4:
        cho "Well Sir, I thought for a minute that you only cared about basketball, but it looks like I was wrong..." ("smile", "base", "base", "mid")
        gen "Of course, I am well versed in all sports. I just thought I'd teach you a thing or two." ("base", xpos="far_left", ypos="head")
        gen "So, will you let me train you then?" ("base", xpos="far_left", ypos="head")
        cho "I suppose..." ("soft", "base", "raised", "R")
        gen "{size=-4}(Fuck yeah, here we go!){/size}" ("grin", xpos="far_left", ypos="head")
        cho "And I will stay true to my word... I'll sell you favours...{w} For wins..." ("soft", "closed", "base", "mid")
        gen "(Hell yes!)" ("angry", xpos="far_left", ypos="head")
        cho "But keep it civil. I won't do anything those Slytherin skanks do!" ("angry", "narrow", "worried", "R")
        cho "And should you not be able to help me and my team beat Hufflepuff, this will be over before you can even say Snitch!" ("scream", "closed", "base", "mid")
        gen "..." ("angry", xpos="far_left", ypos="head")

        if game.daytime:
            cho "Anyway, got to go now, or I'll be late for class." ("smile", "base", "base", "mid")
            cho "But I should have some time this evening if you'd like to get started with the training." ("soft", "base", "base", "down")
            gen "{size=-4}Oh, you bet I do...{/size}" ("base", xpos="far_left", ypos="head")
        else:
            cho "Anyway, it's getting late. I should better head to my dorms." ("soft", "base", "base", "R")
            cho "I'll be ready for training by tomorrow morning." ("soft", "base", "base", "down")
            gen "{size=-4}Oh, I'm not so sure you'll be that prepared...{/size}" ("base", xpos="far_left", ypos="head")
        cho "Until then, Sir." ("smile", "base", "base", "mid")
        gen "Looking forward to it." ("base", xpos="far_left", ypos="head")

        # Cho leaves.
        call cho_walk(action="leave")

        $ states.cho.ev.quiz.complete = True

        call popup("You've unlocked the ability to train Cho in Quidditch.", "Congratulations!", "interface/icons/head/cho.webp")

    # Failed
    else:
        cho "You seem to care a lot about basketball Sir, but I'm not sure if you know that much about Quidditch..." ("open", "narrow", "worried", "mid")
        gen "Or were you asking the wrong questions?" ("base", xpos="far_left", ypos="head")
        cho "Sorry?" ("soft", "narrow", "raised", "mid")
        gen "Time is just relative... what is the difference between a month or a few minutes, really..." ("grin", xpos="far_left", ypos="head")
        cho "Sir, you got a bunch of the questions wrong..." ("annoyed", "narrow", "angry", "mid")
        gen "The truth lies in the eyes of the beholder, Miss Chang..." ("base", xpos="far_left", ypos="head")
        cho "I don't...{nw=1.0}" ("annoyed", "base", "worried", "mid")
        gen "You'll see... I'll show you the real truth..." ("base", xpos="far_left", ypos="head")
        gen "The true truth!" ("base", xpos="far_left", ypos="head")
        gen "(Once I can figure out what the fuck I'm doing...)" ("base", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "base", "raised", "mid")
        gen "Next time..." ("grin", xpos="far_left", ypos="head")
        cho "Oh..." ("soft", "narrow", "base", "down")
        cho "Well, goodbye then, Sir..." ("soft", "base", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        gen "(What am I supposed to do now... I clearly don't know enough about Quidditch...)" ("angry", xpos="far_left", ypos="head")
        gen "(I'd rather not ask Snape... but unless there's someone else that I could ask without sounding like a complete dumb-ass it might have to do...)" ("base", xpos="far_left", ypos="head")

        $ states.cho.ev.quiz.lost = True

        # Read the book.
        if quidditchguide_ITEM.used:
            gen "(Why didn't I just follow the book?{w} Serves me right...)" ("base", xpos="far_left", ypos="head")

        # Got the book but not read.
        elif quidditchguide_ITEM.owned > 0:
            gen "(Maybe I should read the book I bought...)" ("base", xpos="far_left", ypos="head")

        # Visited their shop before.
        elif item_store_intro_done:
            gen "(Actually, perhaps the twins might be a better idea...)" ("base", xpos="far_left", ypos="head")

    jump main_room_menu



# Ask Snape for Quidditch help.
label ss_he_cho_E2:

    call bld
    gen "So It looks like I might need some information about Quidditch..." ("base", xpos="far_left", ypos="head")
    sna "I see, I guess it was only a matter of time before you got yourself involved..." ("snape_01", ypos="head")
    gen "Oh, I don't care much about the sport..." ("base", xpos="far_left", ypos="head")
    sna "Worried you will lose the bet?" ("snape_03")
    gen "No?{w} Let's say it's more of a plot device to push the narrative forward..." ("base", xpos="far_left", ypos="head")
    sna "Of course you can't teach the girl Quidditch if you know nothing about it..." ("snape_09")
    sna "Did she call your bluff?" ("snape_13")
    gen "Of course not..." ("base", xpos="far_left", ypos="head")
    sna "Well, whilst I could drone on for hours about Quidditch rules..." ("snape_06")
    sna "I'd rather not spend my time on such a topic." ("snape_03")
    gen "Where am I supposed to learn the basics then?" ("base", xpos="far_left", ypos="head")
    sna "Why do you think I care where you'd learn it from?" ("snape_09")
    gen "Because keeping me occupied is within your best interests?" ("base", xpos="far_left", ypos="head")
    sna "..." ("snape_04")
    sna "Good point..." ("snape_06")
    sna "Well, I guess it wouldn't be too harmful if you made yourself to the Weasley Twins..." ("snape_05")

    if item_store_intro_done:
        gen "And how would they be able to help me?" ("base", xpos="far_left", ypos="head")
        sna "Well, they're both on the Gryffindor team..." ("snape_03")
        sna "And as much as it pains me to say this..." ("snape_06")
        sna "They're very discrete business minded individuals..." ("snape_02")
        gen "I take it you've had a fair deal of business with them yourself?" ("base", xpos="far_left", ypos="head")
        sna "No comment..." ("snape_03")

    else:
        gen "The Twins? Have you been keeping twins from me now as well?" ("base", xpos="far_left", ypos="head")
        sna "I mean, if two very irritating ginger boys is your type, I'm not going to judge..." ("snape_03")
        gen "..." ("base", xpos="far_left", ypos="head")
        sna "Fred and George Weasley runs a secret shop in the school..." ("snape_01")
        gen "Doesn't sound very secret if you know about it..." ("base", xpos="far_left", ypos="head")
        sna "Their rates are good, plus it means I don't have to leave the castle unless absolutely necessary..." ("snape_09")
        gen "Ah, a basement dweller... charmed." ("base", xpos="far_left", ypos="head")
        sna "In any case, about your inquiry..." ("snape_03")
        sna "The boys are sure to have the means of providing what you need." ("snape_01")
        gen "Sweet, looking forward to meeting them..." ("base", xpos="far_left", ypos="head")
        sna "Aren't you going to ask for directions?" ("snape_05")
        gen "I'm sure I'll manage..." ("base", xpos="far_left", ypos="head")
        sna "Try not to wander too far from your office..." ("snape_09")
        gen "Yes... dad..." ("base", xpos="far_left", ypos="head")
        sna "..." ("snape_08") #[angry]

    # Ending

    nar "You spend the rest of the evening in Snape's company once again talking about Cho's remarkable legs."


    $ states.sna.ev.hangouts.cho_e2 = True

    jump end_snape_hangout_points
