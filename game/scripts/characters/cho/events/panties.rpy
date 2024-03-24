

### Tier 2 (pre Slytherin) ###

label cho_panties_response_T2:
    $ states.cho.ev.panty_thief.acquired = False
    play sound "sounds/door.ogg"
    call cho_chibi("stand","mid","base")
    with d3

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "Hello, [name_genie_cho]." ("soft", "narrow", "worried", "mid", xpos="right", ypos="base")
    gen "[name_cho_genie]..." ("base", xpos="far_left", ypos="head")
    cho "*Uhm*..." ("annoyed", "narrow", "worried", "R")
    cho @ cheeks blush "I forgot to take my underwear with me the last time I was here." ("soft", "narrow", "worried", "downR")

    if states.cho.ev.panty_thief.soaked:
        gen "Your panties! Of course, [name_cho_genie]!{w} I've got them right here..." ("grin", xpos="far_left", ypos="head")
        call cho_walk("desk", "base")
        pause .8

        call give_reward("You hand over the panties...", "interface/icons/panties_cum.webp")

        play sound "sounds/cloth_sound3.ogg"
        pause .4

        cho "(...)" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade) # Evil stare.
        gen "What?" ("base", xpos="far_left", ypos="head")
        cho "(...)" ("annoyed", "narrow", "angry", "R")
        gen "Anything wrong?" ("base", xpos="far_left", ypos="head")
        cho "They are covered in semen." ("soft", "narrow", "base", "R")
        gen "What was that?" ("base", xpos="far_left", ypos="head")
        cho "Semen, Sir!" ("scream", "narrow", "angry", "mid", trans=hpunch) # Scream
        cho "" ("annoyed", "narrow", "angry", "mid")
        gen "You are correct!{w} They are indeed covered in a thick load of filthy, nasty reeking semen!" ("angry", xpos="far_left", ypos="head")
        gen "Who could have done this?!" ("grin", xpos="far_left", ypos="head")
        cho "I don't know... why don't we inquire how they got here in the first place..." ("open", "base", "base", "R")
        cho "Didn't I take off my panties while I was stripping for you?" ("soft", "narrow", "base", "mid")
        gen "That is correct." ("base", xpos="far_left", ypos="head")
        cho "And you had my panties this whole time?" ("soft", "narrow", "raised", "mid")
        gen "Yup." ("base", xpos="far_left", ypos="head")
        cho "And you just gave them back to me covered in spunk..." ("annoyed", "narrow", "base", "mid")
        gen "That makes sense to me..." ("base", xpos="far_left", ypos="head")
        cho "So you admit that you did it?" ("soft", "narrow", "angry", "mid")
        gen "It's not my cum..." ("base", xpos="far_left", ypos="head")
        cho "*Argh*!" ("angry", "narrow", "angry", "mid", trans=hpunch)
        cho "Well whose is it then?{w} The house-elves?" ("soft", "narrow", "base", "mid")
        gen "*Uhm*...{w} Yes?" ("base", xpos="far_left", ypos="head")
        cho "It's disgusting!" ("annoyed", "narrow", "base", "down")
        cho "I better get them cleaned immediately..." ("angry", "narrow", "worried", "down")

        call cho_walk("door", "base")

        call bld
        gen "Where are you going?" ("base", xpos="far_left", ypos="head")

        call cho_chibi("leave")

        call bld
        gen "(...)" ("base", xpos="far_left", ypos="head")

        $ states.cho.mood += 6
        $ states.cho.busy = True

        $ states.cho.ev.panty_thief.soaked = False

        $ achievements.unlock("pantiesfapcho")

        call music_block
        jump main_room_menu

    else:
        gen "Your panties, that's right!{w} I've got them right here..." ("grin", xpos="far_left", ypos="head")

        play sound "sounds/sniff.ogg"
        nar "You bring the panties to your nose and give them one last sniff."

        gen "*Aaahhh*!{w} Wonderful!" ("angry", xpos="far_left", ypos="head")
        cho "(...)" ("annoyed", "narrow", "base", "mid")
        gen "There, take them..." ("base", xpos="far_left", ypos="head")

        call cho_walk("desk", "base")
        pause .8

        play sound "sounds/cloth_sound3.ogg"
        pause .4

        call cho_walk("mid", "base")
        call cho_chibi("stand", "mid", "base", flip=False)
        with d3
        pause .2

        cho "Thank you, Sir." ("base", "base", "base", "mid")
        gen "You're welcome..." ("base", xpos="far_left", ypos="head")

        jump cho_requests


### Tier 3 (pre Gryffindor) ###

label cho_panties_response_T3:
    $ states.cho.ev.panty_thief.acquired = False
    play sound "sounds/door.ogg"
    call cho_chibi("stand","mid","base")
    with d3

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho @ cheeks blush "Hello, [name_genie_cho]." ("base", "narrow", "base", "downR", xpos="right", ypos="base")
    gen "[name_cho_genie]..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I believe I left you something of mine..." ("open", "narrow", "base", "down")
    gen "Ah, yes... Your panties, I've got them right here." ("grin", xpos="far_left", ypos="head")
    cho "Great!" ("base", "base", "base", "mid")
    if states.cho.ev.panty_thief.soaked:

        call cho_walk("desk", "base")
        pause .8

        call give_reward("You hand over the panties...", "interface/icons/panties_cum.webp")

        cho @ cheeks blush "(...)" ("upset", "base", "base", "down", xpos="mid", ypos="base", trans=blackfade)
        gen "Something wrong?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "You came on them didn't you?" ("mad", "narrow", "base", "downR")
        gen "Of course, what did you think would happen when you left them here?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("annoyed", "narrow", "base", "down")
        cho @ cheeks blush "I suppose you're just a man after all, I would've been more shocked if you hadn't done it." ("open", "closed", "base", "mid")
        cho @ cheeks blush "I'll just have to make sure to clean them before I use them next time..." ("soft", "narrow", "base", "down")
        gen "Or you could put them on now..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("annoyed", "base", "base", "downR")
        cho @ cheeks blush "*Hmm*... No, I don't think so..." ("base", "narrow", "base", "mid")
        gen "Worth a shot..." ("base", xpos="far_left", ypos="head")
        gen "There, take them..." ("base", xpos="far_left", ypos="head")

        $ states.cho.ev.panty_thief.soaked = False

        $ achievements.unlock("pantiesfapcho")

    else:

        play sound "sounds/sniff.ogg"
        nar "You bring the panties to your nose and give them one last sniff."

        gen "*Aaahhh*!{w} Wonderful!" ("angry", xpos="far_left", ypos="head")
        cho "(...)" ("base", "narrow", "base", "down")
        gen "Here, come and take them..." ("base", xpos="far_left", ypos="head")

        call cho_walk("desk", "base")
        pause .8

    play sound "sounds/cloth_sound3.ogg"
    pause .4

    call cho_walk("mid", "base")
    call cho_chibi("stand", "mid", "base", flip=False)
    with d3
    pause .2

    cho "Thank you, Sir." ("base", "base", "base", "mid")
    gen "You're welcome..." ("base", xpos="far_left", ypos="head")

    jump cho_requests
