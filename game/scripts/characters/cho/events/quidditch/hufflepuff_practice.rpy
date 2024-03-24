

# Started first training match against Hufflepuff

label cc_ht_start:

    cho "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    # First Hufflepuff match.
    gen "Ready to show off your panties to those badgering badgers?" ("base", xpos="far_left", ypos="head")

    if game.weather in ("blizzard", "storm", "snow", "rain"):
        cho "In this weather? But I'll freeze my legs off if I'm to wear a skirt..." ("clench", "base", "base", "R")
        cho "I'd rather not catch a cold during practice..." ("open", "base", "worried", "mid")
        gen "Alright." ("base", xpos="far_left", ypos="head")

        jump cho_training.choices

    cho "Ready as I'll ever be." ("open", "narrow", "base", "R")
    gen "Great. Get your team ready cause you are going to play today." ("base", xpos="far_left", ypos="head")
    cho "I'll give their team captain a heads-up during classes then." ("soft", "narrow", "base", "mid")
    gen "Good, let me know how it went once practice finishes." ("base", xpos="far_left", ypos="head")
    cho "I will, [name_genie_cho]. Wish me luck." ("soft", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ states.cho.ev.quidditch.in_progress = True

    call gen_chibi("sit_behind_desk")
    with fade

    jump end_cho_event

label cc_ht_return:
    # Cho enters.

    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"

    menu:
        "\"Come in!\"":
            cho "Yes, [name_genie_cho]..."
        "\"Who is it?\"":
            cho "Cho Chang, [name_genie_cho]."
            gen "Come on in, [name_cho_genie]!" ("base", xpos="far_left", ypos="head")
            cho "..."

    $ cho.equip(cho_outfit_quidditch)

    call cho_walk(xpos="mid", ypos="base", action="enter")

    cho "(...)" ("annoyed", "narrow", "angry", "R", xpos="mid", ypos="base", trans=d3)
    gen "You seem a little on edge..." ("base", xpos="far_left", ypos="head")
    cho "On edge?" ("scream", "wide", "angry", "mid")
    cho "Of course I'm on edge! I've never felt so humiliated in my life!" ("angry", "wide", "angry", "mid")
    cho "You had to have me do this on the day half of Hufflepuff shows up to watch us practise, didn't you!" ("annoyed", "narrow", "angry", "R")
    cho "I bet you were probably in on it..." ("upset", "narrow", "angry", "mid")
    gen "Now now, you know I'd never resort to any sort of foul play like that..." ("base", xpos="far_left", ypos="head")
    gen "More importantly, how did the game go?" ("base", xpos="far_left", ypos="head")
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "{size=+10}I got it!!!{/size}" ("scream", "base", "base", "mid")
    cho "I caught the snitch!" ("smile", "happyCl", "base", "mid")
    gen "Congratulations..." ("base", xpos="far_left", ypos="head")
    cho "That blockhead Cedric didn't stand a chance against me!" ("open", "base", "angry", "R")
    cho "Usually I'm never fast enough to beat him with my crummy old nimbus..." ("annoyed", "narrow", "angry", "downR")
    cho "But today, I flew above him as we both raced after the snitch, just like you said I should." ("smile", "base", "base", "mid")
    gen "Sounds like somebody should get a reward for their efforts!" ("grin", xpos="far_left", ypos="head")
    cho "I can't believe I was able to finally catch it!" ("grin", "happyCl", "base", "mid")
    gen "Is this the first time you've caught one?" ("base", xpos="far_left", ypos="head")
    cho "*Mhmm*...{w=0.3} This is the first game of quidditch Ravenclaw has won in over six years!" ("smile", "base", "base", "mid")
    gen "Wasn't this just a practice game?" ("base", xpos="far_left", ypos="head")
    cho "I was including the practices, [name_genie_cho]..." ("annoyed", "narrow", "worried", "downR")
    gen "Oh..." ("base", xpos="far_left", ypos="head")
    cho "Ravenclaw...{w} isn't very good..." ("annoyed", "narrow", "worried", "down")
    cho "But I have a feeling that's going to change this year!" ("base", "happyCl", "base", "mid")
    gen "And I am happy to be of help!" ("grin", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]! Thank you so much!" ("smile", "narrow", "base", "mid")
    cho "If there is any way I can return the favour...?" ("horny", "base", "raised", "mid")
    gen "Yes, but we can discuss that after you've won the game." ("base", xpos="far_left", ypos="head")
    gen "And have you do some more {b}advanced{/b} favours for me." ("grin", xpos="far_left", ypos="head")
    cho "More advanced... Sir?" ("soft", "narrow", "worried", "mid")
    #gen "Would you say you've had enough practice to play against them in a tourney game?" ("base", xpos="far_left", ypos="head")
    #cho "Absolutely! The next time we will confront Hufflepuff, they will be crushed!" ("smile", "narrow", "angry", "mid")
    #cho "This should be an easy win for Ravenclaw." ("base", "closed", "base", "mid")
    cho "*Ehm*... [name_genie_cho]..." ("horny", "base", "worried", "mid")
    cho "The whole house is celebrating our win at the moment..." ("soft", "narrow", "worried", "mid")
    cho "And I'd rather not miss spending some time with--" ("horny", "base", "worried", "R")
    gen "You did well today, [name_cho_genie]." ("angry", xpos="far_left", ypos="head")
    cho "" ("horny", "base", "base", "mid")
    gen "Go and party! You've earned it." ("grin", xpos="far_left", ypos="head")
    cho "Thank you, [name_genie_cho]... For everything." ("base", "narrow", "base", "mid")
    cho "Have a good night!" ("smile", "base", "base", "mid")
    gen "You too..." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    $ cho.equip(cho_outfit_last) # Equip last worn clothes
    $ states.cho.ev.quidditch.hufflepuff_training = True # Mark as complete

    jump end_cho_event

### Cho Talk ###

label cc_ht_talk:

    cho "" (xpos="right", ypos="base", trans=fade)

    if not states.cho.ev.quidditch.e1_complete:
        gen "Ready to start training?" ("base", xpos="far_left", ypos="head")
        cho "Of course, just let me know when." ("smile", "base", "raised", "mid")
    elif not states.cho.ev.quidditch.e2_complete:
        gen "So, are you sure you don't want my help?" ("base", xpos="far_left", ypos="head")
        cho "I... I don't know..." ("upset", "base", "raised", "downR")
    elif states.cho.ev.quidditch.e3_complete and not states.cho.ev.quidditch.e4_complete:
        cho "Have you asked Hermione to be our commentator yet?" ("soft", "base", "base", "mid")
        gen "Not yet." ("base", xpos="far_left", ypos="head")
        cho "We can't play if we don't have a commentator." ("soft", "base", "worried", "R")
        cho "Please ask her, Sir." ("annoyed", "base", "worried", "mid")
    elif states.cho.ev.quidditch.e4_complete and states.cho.ev.quidditch.lock_practice: # mandatory
        gen "I've got great news for you! I found us a new commentator!" ("grin", xpos="far_left", ypos="head")
        cho "Is it Hermione?" ("soft", "narrow", "base", "mid")
        gen "Yes! Very good guess!" ("grin", xpos="far_left", ypos="head")
        cho "It wasn't a guess, [name_genie_cho]. We've discussed this already." ("annoyed", "narrow", "angry", "mid")
        gen "Oh, sure..." ("base", xpos="far_left", ypos="head")
        cho "But I'm surprised she even took up the task..." ("annoyed", "base", "base", "R")
        gen "Right away. No questions asked." ("grin", xpos="far_left", ypos="head")
        cho "And little miss Granger wasn't even the slightest bit intimidated by her new obligation?" ("open", "base", "raised", "mid")
        gen "Not at all. She seemed rather joyous about her situation." ("grin", xpos="far_left", ypos="head")
        cho "Oh..." ("annoyed", "base", "worried", "down") # Bit sad.
        cho "Well, she just doesn't know what's coming towards her yet!" ("annoyed", "narrow", "angry", "mid")
        cho "{size=-4}I hope she gets hit by a bludger as well! I might even tell the boys to aim at her once or twice!{/size}" ("angry", "narrow", "angry", "R") # Small text.
        gen "Make sure you tell everyone how your great and very proactive headmaster sorted everything out..." ("grin", xpos="far_left", ypos="head")
        cho "Oh, I will. Thank you very much!" ("soft", "base", "base", "mid")

        $ states.cho.ev.quidditch.lock_training = True # Removes training menu.
        $ states.cho.ev.quidditch.hufflepuff_stage = "ready" # Able to start main match.

        hide cho_main
        show screen blkfade
        with d3

        $ cho.equip(cho_outfit_last)

        call cho_chibi("stand", "mid", "base")
        call gen_chibi("sit_behind_desk")

        call reset_menu_position

        hide screen blkfade
        cho "" ("base", "base", "base", "mid", xpos="base", ypos="base", trans=fade)

        jump cho_requests
    elif not states.cho.ev.talk_to_me.t1_e3_complete: # Has NOT completed "Talk to me" favour yet.
        gen "Have any ideas on how to beat those {i}huffers{/i}?" ("base", xpos="far_left", ypos="head")
        cho "Isn't that your job?" ("soft", "base", "raised", "mid")
        gen "Oh, yeah..." ("base", xpos="far_left", ypos="head")
        gen "(How does she expect me to help her without knowing anything about the opponents?)" ("base", xpos="far_left", ypos="head")
        gen "(Maybe I could get her to talk to me and gain more information through favours...)" ("base", xpos="far_left", ypos="head")
    elif not states.cho.ev.quidditch.hufflepuff_prepared:
        gen "Are you ready for the big win?" ("base", xpos="far_left", ypos="head")
        cho "Have you actually found out a tactic we could use?" ("open", "base", "raised", "mid")
        gen "(Oh right... I didn't discuss our new tactic with her yet.)" ("base", xpos="far_left", ypos="head")
    elif states.cho.level < 3: # Has Cho enough confidence?
        gen "So, how about those tactics?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I don't know if I can do...{w=0.4} That..." ("disgust", "narrow", "base", "mid")
        gen "What do you mean you can't? It's the perfect strategy!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "But..." ("soft", "base", "base", "down")
        gen "Where's your confidence, your spirit?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I'm sorry, [name_genie_cho], forget I said anything..." ("open", "happyCl", "base", "mid")
        gen "(*Hmm*... She doesn't look very confident to me...)" ("base", xpos="far_left", ypos="head")
        gen "(Perhaps I should train her more in private.)" ("base", xpos="far_left", ypos="head")
    else:
        cho "I'm confident that we can win this, [name_genie_cho]." ("smile", "base", "base", "mid")

    cho "" (xpos="base", ypos="base", trans=fade)

    jump cho_training.choices
