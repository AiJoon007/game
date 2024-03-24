### Cho Gryffindor Training ###
label cc_gt_start:

    gen "Alright then. Let's get you out there to smack some asses!" ("base", xpos="far_left", ypos="head")
    cho "Smack some asses, [name_genie_cho]?" ("angry", "base", "base", "mid")
    gen "You've heard me!" ("base", xpos="far_left", ypos="head")
    gen "It's not against the rules, is it?" ("base", xpos="far_left", ypos="head")
    cho "W--{w=0.2} Well... I suppose not, unless I do it with my elbows." ("soft", "narrow", "base", "R")
    gen "With your elbows...?" ("base", xpos="far_left", ypos="head")
    cho "Yeah, excessive use of elbows is against the rules." ("soft", "narrow", "base", "mid")
    gen "Sounds like something you made up..." ("base", xpos="far_left", ypos="head")
    cho "It's a real rule! Excessive use of elbows, otherwise known as cobbing--" ("mad", "narrow", "base", "mid")
    gen "Alright fine, no elbow touching." ("base", xpos="far_left", ypos="head")
    gen "You won't need them to turn some bums red." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "So that's what you meant by getting intimate? Smacking the Gryffindor's bums until they turn red?" ("disgust", "narrow", "base", "mid")
    gen "Yeah!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Isn't that a bit extreme?" ("angry", "narrow", "base", "mid")
    gen "A good ole love tap is hardly extreme." ("base", xpos="far_left", ypos="head")
    gen "If you do it well enough, then I'm sure Miss Granger will notice." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well enough, [name_genie_cho]?" ("angry", "narrow", "base", "mid")
    gen "Yeah, make those slaps echo across the pitch!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Hmm*... Alright then, I'll make sure of that..." ("open", "narrow", "base", "downR")
    gen "Great! Then get out there and spank some booty, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "On it, [name_genie_cho]!" ("angry", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ states.cho.ev.quidditch.in_progress = True
    $ states.cho.ev.quidditch.gryffindor_failed = True

    call gen_chibi("sit_behind_desk")
    with fade

    jump end_cho_event

label cc_gt_return:
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"

    gen "Come in!" ("base", xpos="far_left", ypos="head")

    $ cho.equip(cho_outfit_quidditch_gryffindor)

    call cho_walk(xpos="mid", ypos="base", action="enter")

    gen "[name_cho_genie]!" ("base", xpos="far_left", ypos="head")
    gen "Had a fruitful day, smacking some peaches?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I did not!" ("disgust", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    gen "Too bad, I was so sure it would have worked." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Oh, it worked alright..." ("annoyed", "closed", "angry", "mid")
    gen "It did?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "In fact, it worked so well I'm not sure what was redder, Katie's bum, or Hermione's face..." ("angry", "narrow", "base", "R")
    cho @ cheeks blush "She was fuming!" ("base", "narrow", "angry", "mid")
    gen "Splendid! Then what's the problem?" ("base", xpos="far_left", ypos="head")
    cho "It's my broom..." ("angry", "closed", "worried", "R") # Sad
    cho "Those bloody Weasley twins, they destroyed my broom!" ("clench", "narrow", "angry", "mid")
    gen "They did what?!" ("base", xpos="far_left", ypos="head")
    gen "Sabotaging weasels!" ("base", xpos="far_left", ypos="head")
    gen "I'll get them expelled!!" ("base", xpos="far_left", ypos="head") # Double exclamation intentional
    cho "That would be great and all, but I don't have any proof..." ("disgust", "narrow", "angry", "mid")
    gen "What do you mean? Then how do you know it was them?" ("base", xpos="far_left", ypos="head")
    cho "Well, given the state my broom was in when I've found it, it couldn't have been anyone else." ("annoyed", "narrow", "angry", "mid")
    cho "My broom fell a victim to termites..." ("angry", "closed", "angry", "mid")
    cho "They must have put them on my broom while I was changing, after the practise." ("disgust", "narrow", "angry", "mid")
    gen "Can't you just borrow another broom from, I don't know, one of the cleaning cupboards?" ("base", xpos="far_left", ypos="head")
    cho "Cleaning cupboards--" ("angry", "wide", "base", "mid")
    cho "Please, [name_genie_cho], this isn't a joking matter." ("angry", "narrow", "base", "mid")
    cho "Being this close to the finals, I won't be able to purchase a proper professionally crafted broom in time." ("angry", "narrow", "base", "mid")
    gen "Why not?" ("base", xpos="far_left", ypos="head")
    cho "They're very expensive." ("disgust", "narrow", "base", "mid")
    gen "How expensive could a broom be--" ("base", xpos="far_left", ypos="head")

    # This will always display player gold + 1000, because why not.
    $ _gold = game.gold + 4000
    $ _gold = num_to_word(_gold)

    cho "[_gold]!" ("clench", "closed", "base", "mid")
    play sound "sounds/gulp.ogg"
    gen "*Gulp*..." ("angry", xpos="far_left", ypos="head")
    gen "Surely there must be some spare brooms around the castle." ("angry", xpos="far_left", ypos="head")
    cho "I assure you... Even the brooms provided for flying lessons are terrible." ("disgust", "narrow", "angry", "mid")
    gen "I'm sure they're fine..." ("base", xpos="far_left", ypos="head")
    gen "(Please don't make me buy a bloody broom, I'll go bankrupt...)" ("base", xpos="far_left", ypos="head")
    cho "Please, [name_genie_cho]..." ("soft", "narrow", "worried", "mid")
    gen "(Here we go...)" ("base", xpos="far_left", ypos="head")
    cho "Could you buy me a broom?" ("quiver", "narrow", "worried", "mid")
    gen "Hold on just a second... Termites? Are you just trying to get me to buy you a new broom again?" ("angry", xpos="far_left", ypos="head")
    cho "Of course not! You think I would lie about something like this?" ("clench", "narrow", "worried", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "Please believe me [name_genie_cho]!" ("scream", "closed", "worried", "mid")
    gen "A school supplied broom will have to suffice." ("base", xpos="far_left", ypos="head")
    cho "Why aren't you listening, [name_genie_cho]!" ("angry", "wide", "worried", "mid")

    # Used in Quidditch Outro
    label .introspection:

    if _in_replay:

        show screen blkfade
        with d5

        $ cho.equip(cho_outfit_quidditch_gryffindor)
        $ game.gold = 1984
        $ game.day = 665
        $ game.daytime = False
        $ game.weather = "clear"
        call room("main_room")
        call cho_chibi(xpos="mid", ypos="base")

        hide screen blkfade
        with d5

        play music "music/Music for Manatees.ogg" fadein 1 if_changed
    #

    cho "The school supplied brooms are ancient, there's no way I'd be able to win anything, flying on that rubbish!" ("scream", "narrow", "worried", "mid", xpos="mid")
    cho "Harry's firebolt--" ("angry", "closed", "worried", "mid")
    gen "A broom's a broom. I'm sure the expensive ones are just branding." ("base", xpos="far_left", ypos="head")
    cho "..." ("disgust", "narrow", "base", "mid")
    gen "Just try them out, I'm sure it'll be fine." ("base", xpos="far_left", ypos="head")
    cho "It's a waste of time, but if that's what it takes, then sure..." ("annoyed", "closed", "angry", "mid")
    cho "I'll meet you at the pitch tomorrow morning." ("open", "closed", "angry", "mid") #smirk
    gen "Excellent, I'll...{w=0.4} Wait, did you say tomorrow morning?" ("base", xpos="far_left", ypos="head")
    cho "Yes, and you better be there, [name_genie_cho]..." ("disgust", "narrow", "angry", "mid") #smiling
    gen "(The things a Coach has to do...{w=0.4} Wake up in the morning...)" ("base", xpos="far_left", ypos="head")
    gen "What else do you need from me? Shall I put together a cheerleading squad as well?" ("base", xpos="far_left", ypos="head")
    cho "Oh, yes please! That should help with riling up Hermione even more." ("smile", "narrow", "base", "mid")
    gen "(Does sarcasm not exist in this world?)" ("base", xpos="far_left", ypos="head")
    gen "Very well then, I'll get you your squad, and meet you at the pitch... *Eugh*... tomorrow morning..." ("base", xpos="far_left", ypos="head")

    #Cho walks to door
    call cho_walk(xpos="door")

    cho "(The school brooms, what's he thinking? I can't believe he doesn't realise they wouldn't be anywhere close to the speed of Harry's firebolt...)" ("disgust", "narrow", "base", "R", flip=True)
    cho "(What if he forces me to use one... There's no way I would be able to outspeed even their keeper...)" ("clench", "narrow", "base", "down")
    cho "(I have to win the finals, no matter what!)" ("angry", "closed", "base", "mid")
    cho "(But how...)" ("annoyed", "narrow", "base", "down")
    gen "[name_cho_genie]?" ("base", xpos="far_left", ypos="head")

    #Cho leaves.
    call cho_walk(action="leave")
    pause .8

    # Used in Quidditch Outro
    if _in_replay:
        return

    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

    $ cho.equip(cho_outfit_last) # Equip last worn clothes

    $ states.cho.ev.quidditch.gryffindor_stage = "ready"
    $ states.cho.ev.quidditch.gryffindor_training = True
    $ states.cho.ev.quidditch.lock_practice = True

    jump end_cho_event

label cc_gt_talk:

    cho "" (xpos="right", ypos="base", trans=fade)

    if states.cho.ev.quidditch.gryffindor_training:
        cho "Finals starting soon?" ("base", "base", "base", "mid")

        if not states.cho.ev.quidditch.e11_complete and not states.cho.ev.quidditch.e12_complete:
            # Didn't ask Luna to cheer and didn't get the broom
            gen "Not yet... I've got some things to take care of before then." ("base", xpos="far_left", ypos="head")
            cho "That's too bad, I want to crush those Gryffindors already!" ("base", "base", "base", "mid")
            gen "(I've still got to help her find a broom in the morning...)" ("base", xpos="far_left", ypos="head")
            gen "(And how am I supposed to get a cheerleading squad together...)" ("base", xpos="far_left", ypos="head")
            gen "(Perhaps there's some other Ravenclaw student I can ask...)" ("base", xpos="far_left", ypos="head")
        elif not states.cho.ev.quidditch.e11_complete:
            # Didn't ask Luna to cheer
            gen "No, I still need to get you your stupid cheerleading squad." ("base", xpos="far_left", ypos="head")
            cho "Stupid? Wasn't this your idea?" ("base", "base", "base", "mid")
            gen "I was being..." ("base", xpos="far_left", ypos="head")
            gen "Nevermind..." ("base", xpos="far_left", ypos="head")
            gen "(I wonder if there's someone from Ravenclaw that I could ask...)" ("base", xpos="far_left", ypos="head")
        elif not states.cho.ev.quidditch.e12_complete:
            # Didn't get the broom
            gen "Not until we have you pick out one of the school brooms to use." ("base", xpos="far_left", ypos="head")
            cho "You mean not until we find out how worthless they are, and you have to get me a proper broom." ("base", "base", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
        else: #Match ready
            gen "As long as you're ready." ("base", xpos="far_left", ypos="head")
            cho "I'm ready!" ("base", "base", "base", "mid")
    else:
        cho "Let's find the weakness of those Gryffindors!" ("base", "base", "base", "mid")
        gen "On it!" ("base", xpos="far_left", ypos="head")

    cho "" (xpos="base", ypos="base", trans=fade)

    jump cho_training.choices
