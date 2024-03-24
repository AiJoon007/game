# cc_st_intro  automatically plays when starting slytherin tier

# cc_st_start unlocks once you've convinced Cho to use tactics against slytherin (Will need some work as I don't know the code)
# cc_st_return_E1 Is the return event as Slytherin wont practice, practice locks after this event as Slytherins doesn't show up
#To play practice again you need to talk to Tonks to convince them to play again cc_st_tonks_E1 (cc_st_snape_E1 is optional until you talk to tonks)
# Hermione shows up next day after this event saying that she wont play cc_st_hermione_E1 once she leaves it unlocks the ability to blackmail her cc_st_hermione_blackmail

# cc_st_return_E2 Is the return event when Cho has practiced against Slytherins. Once this event finished one of two requirements to start the main match is completed (other being blackmail Hermione)
#cc_st_hermione_blackmail is one of two requirements to play the main match (other being cc_st_return_E2)


### Cho Slytherin Training ###
label cc_st_start:

    cho "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    # Intro 1
    if not states.cho.ev.quidditch.slytherin_prepared:
        gen "Alright, we need to try out those new tactics!" ("base", xpos="far_left", ypos="head")
        gen "There is a lot at stake here! We can't afford to lose even a single game!" ("angry", xpos="far_left", ypos="head")
        gen "We can't show any weakness to those Slytherins!" ("angry", xpos="far_left", ypos="head")
        cho @ cheeks blush "I'm glad my success is that important to you, Sir." ("smile", "happyCl", "base", "mid")

        show screen blktone
        with d3
        gen "(I can't lose this much gold to Snape. I'll show that bastard!)" ("base", xpos="far_left", ypos="head")
        hide screen blktone
        with d3

        gen "Return to my office after the game." ("grin", xpos="far_left", ypos="head")
        cho "Yes, Sir." ("base", "narrow", "base", "mid")

    # Intro 2 (For successful match against Slytherins) (playing is one of two needed requirements for match to unlock alongside with Blackmailing Hermione)
    else:
        gen "Let's try this again, shall we?" ("base", xpos="far_left", ypos="head")
        gen "I spoke with your teacher, she'll get those nitwits to play again..." ("base", xpos="far_left", ypos="head")
        cho "Professor Tonks, was it?" ("smile", "base", "base", "mid")
        gen "Yep." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I'm really glad we have her as a teacher." ("base", "happyCl", "base", "mid")
        gen "Make sure to thank her for it... some day." ("base", xpos="far_left", ypos="head")
        cho "I will, [name_genie_cho]." ("smile", "base", "base", "mid")
        cho "Off I go then..." ("base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    $ states.her.busy = True

    $ states.cho.ev.quidditch.in_progress = True

    call gen_chibi("sit_behind_desk")
    with fade

    jump end_cho_event


label cc_st_return:
    if not states.cho.ev.quidditch.slytherin_prepared:
        # Cho goes unprepared and fails.

        stop music fadeout 5.0

        play sound "sounds/snore1.ogg"
        gen "...*snore*{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
        pause .8
        play sound "sounds/snore3.ogg"
        gen "...{cps=10}*snooore*{/cps}{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
        pause 1.2
        play sound "sounds/snore1.ogg"
        gen "...*sno*-{w=0.5}{nw}" ("base", xpos="far_left", ypos="head") # Interrupts

        play sound "sounds/knocking.ogg"
        "*Knock-knock-knock*!"
        pause .2

        gen "Wha--?" ("base", xpos="far_left", ypos="head")

        $ cho.equip(cho_outfit_quidditch)

        call cho_walk(action="enter", xpos="desk", ypos="base")

        # Cho is furious.
        cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid",ypos="base", trans=d3)
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "What are you doing in here? You're not supposed to be back yet..." ("angry", xpos="far_left", ypos="head")
        cho "I'm surprised you could tell..." ("soft", "wide", "base", "mid")
        gen "You just woke me up in the middle of my nap!" ("angry", xpos="far_left", ypos="head")
        cho "Oh no, Sir. I'm terribly sorry!" ("soft", "base", "raised", "R")

        menu:
            gen "..." ("base", xpos="far_left", ypos="head")
            "\"Are you mocking me for taking a nap?\"":
                play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

                cho "No, sir." ("soft", "base", "base", "mid")
                gen "..." ("base", xpos="far_left", ypos="head")
                gen "(Damn it... That naivety of hers is turning me on!)" ("angry", xpos="far_left", ypos="head")

            "\"Brats like you need to be punished!\"":
                $ states.cho.mood += 2
                play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

                cho "Punished? For what?" ("soft", "narrow", "angry", "mid") # angry
                gen "For being a pain in my ass!" ("angry", xpos="far_left", ypos="head")
                cho "" ("annoyed", "narrow", "base", "mid")
                gen "And for waking me up in the middle of my nap!" ("angry", xpos="far_left", ypos="head")

        gen "Why aren't you on that Quidditch ditch right now?" ("base", xpos="far_left", ypos="head")
        cho "It's a pitch, Sir." ("soft", "narrow", "raised", "mid")
        gen "I thought we were going to prepare for the next match, or are we already finished with that?" ("base", xpos="far_left", ypos="head")
        gen "(Please say yes! I want to do the naughty stuff already!)" ("angry", xpos="far_left", ypos="head")
        cho "Yes, we are..." ("open", "closed", "base", "mid")
        gen "(Yes!)" ("grin", xpos="far_left", ypos="head")
        cho "For today, that is..." ("annoyed", "narrow", "base", "R")
        gen "(Balls...)" ("base", xpos="far_left", ypos="head")
        cho "We couldn't play today because the entire Slytherin team didn't even bother to show up!" ("annoyed", "narrow", "base", "mid")
        cho "Spineless cowards..." ("annoyed", "narrow", "angry", "downR")
        cho "They have no interest in training against us!" ("open", "narrow", "angry", "mid")
        cho "Because why should they... They'll win anyway!" ("open", "narrow", "angry", "R")
        cho "They assured me that they would be there today..." ("annoyed", "narrow", "angry", "downR")
        cho "Such a pathetic bunch of apes!" ("annoyed", "narrow", "angry", "R")
        gen "A troop." ("base", xpos="far_left", ypos="head")
        cho "What?" ("soft", "narrow", "raised", "mid")
        gen "It's called a troop of apes." ("base", xpos="far_left", ypos="head")
        cho "Whatever..." ("annoyed", "narrow", "angry", "R")
        cho "If I see their captain tomorrow, I'm gonna knee him in the groin!" ("soft", "narrow", "angry", "mid")
        gen "Yikes!" ("angry", xpos="far_left", ypos="head")
        gen "I'm afraid I can't have you do that..." ("base", xpos="far_left", ypos="head")
        cho "Why not? They deserve it!" ("annoyed", "base", "angry", "mid")
        gen "No guy deserves that..." ("base", xpos="far_left", ypos="head")
        gen "I'd rather deal with it myself, if you don't mind." ("base", xpos="far_left", ypos="head")
        cho "Fine..." ("annoyed", "narrow", "angry", "downR")
        cho "But you better do something, quickly! Get those idiots to play!" ("soft", "narrow", "angry", "mid")
        cho "We can't possibly win if we don't know their tactics." ("soft", "base", "base", "R")
        cho "Or know if our tactics work against them, for that matter..." ("annoyed", "narrow", "base", "mid")
        gen "I'm on it..." ("base", xpos="far_left", ypos="head")
        cho "And that's not all... I heard some people saying that Hermione won't commentate anymore!" ("angry", "narrow", "angry", "mid", emote="angry")
        gen "What?" ("angry", xpos="far_left", ypos="head")
        cho "I know, you better do something about it!" ("open", "narrow", "angry", "mid")
        gen "*Ugh*... Do I have to?" ("angry", xpos="far_left", ypos="head")
        cho "Yes!" ("angry", "base", "angry", "mid")
        cho "Get that spineless mop's ass back behind that podium!" ("soft", "narrow", "base", "mid")
        gen "{size=-6}At least let me finish the first quest -- before taking on another one...{/size}" ("base", xpos="far_left", ypos="head")
        cho "She agreed to do this! We need an announcer!" ("annoyed", "narrow", "base", "R")
        gen "I'll talk to her..." ("base", xpos="far_left", ypos="head")
        cho "Then make it quick!" ("annoyed", "narrow", "base", "mid")
        cho "Good night, Sir." ("soft", "narrow", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        gen "That girl sure is a piece of work..." ("base", xpos="far_left", ypos="head")

        $ cho.equip(cho_outfit_last) # Equip last worn clothes

        $ states.her.busy = True
        $ states.sna.busy = True #Set to busy since their hangouts are triggered after Hermione event next morning.
        $ states.ton.busy = True #Set to busy since their hangouts are triggered after Hermione event next morning.
        $ states.cho.mood += 6
        $ states.cho.ev.quidditch.lock_practice = True
        $ states.cho.ev.quidditch.slytherin_failed = True

        jump end_cho_event
    else:
        # Cho has been prepared and trained.

        call cho_walk(action="enter", xpos="desk", ypos="base")

        # Cho is furious.
        cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid",ypos="base", trans=d3)

        gen "Welcome back..." ("base", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "base", "angry", "R") #Annoyed
        gen "Don't tell me they didn't show up again... Tonks assured me she'd get them to--" ("base", xpos="far_left", ypos="head")
        cho "No, they did show up alright." ("open", "narrow", "angry", "mid")
        gen "Excellent!" ("grin", xpos="far_left", ypos="head")
        gen "Then what about our strategy, do you think it will work during the game?" ("base", xpos="far_left", ypos="head")
        cho "I can't believe I flaunted my ass at them... but yes, I believe it will work." ("soft", "closed", "raised", "mid")
        cho "Crabbe and Goyle especially should be a great help, turning the game to my favour." ("smile", "narrow", "raised", "R")
        cho "So long as they don't give my ass too much of a {i}bludgering{/i}..." ("clench", "base", "raised", "mid")
        gen "Just make sure to pick the right moment to distract them, and you'll be fine." ("base", xpos="far_left", ypos="head")
        gen "Very well then, I guess we're ready to take those snakes on for the main match!" ("base", xpos="far_left", ypos="head")
        if not states.cho.ev.quidditch.e7_complete:
            cho "What about Granger?" ("annoyed", "base", "raised", "mid")
            gen "What about her?" ("base", xpos="far_left", ypos="head")
            cho "Is she commentating or what? We can't play without a commentator." ("open", "base", "base", "mid")
            gen "Oh, that's true... I'll talk to her..." ("base", xpos="far_left", ypos="head")
            cho "Good." ("base", "base", "base", "mid")
        else:
            cho "I suppose..." ("annoyed", "base", "base", "R")
        gen "The match looms ever closer... I hope you're ready." ("base", xpos="far_left", ypos="head")
        cho "You bet your ass I am!" ("smile", "base", "angry", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        cho "Don't even say it..." ("upset", "base", "angry", "mid")
        gen "I... wasn't--" ("base", xpos="far_left", ypos="head")
        cho "Sure you weren't..." ("soft", "closed", "angry", "mid")
        cho "I'll head off to bed then." ("open", "base", "base", "R")
        gen "{size=+6}*MHHMMMM*{/size}" ("angry", xpos="far_left", ypos="head")

        call cho_walk(action="leave")

        gen "*NNNNGH!!!*" ("angry", xpos="far_left", ypos="head")
        gen "{b}You'll{/b} be betting your ass on it!" ("grin", xpos="far_left", ypos="head")
        cho "{size=-4}I heard that!{/size}" # Cho outside the door
        gen "Dammit..." ("base", xpos="far_left", ypos="head")

        $ cho.equip(cho_outfit_last) # Equip last worn clothes

        $ states.cho.ev.quidditch.slytherin_stage = "ready"
        $ states.cho.ev.quidditch.slytherin_training = True
        $ states.cho.ev.quidditch.lock_practice = True
        if states.cho.ev.quidditch.e7_complete:
            $ states.cho.ev.quidditch.lock_training = True

        jump end_cho_event

### Stage 3 ###

label cc_st_talk:

    cho "" (xpos="right", ypos="base", trans=fade)

    if states.cho.ev.quidditch.e6_complete and (not states.cho.ev.quidditch.e8_complete or not states.cho.ev.quidditch.e7_complete):
        if not states.cho.ev.quidditch.e8_complete and not states.cho.ev.quidditch.e7_complete:
            # Haven't done either
            cho "Wow, that was quick! I didn't think you'd get it done already!" ("open", "base", "base", "mid")
            gen "*Err*... Get what done?" ("base", xpos="far_left", ypos="head")
            cho "Get Hermione to commentate and get those pigs flying again!" ("annoyed", "narrow", "base", "mid")
            gen "Flying pigs?!" ("base", xpos="far_left", ypos="head")
            cho "The Slytherins!" ("angry", "narrow", "base", "mid")
            gen "Oh... Right... I forgot about that..." ("base", xpos="far_left", ypos="head")
            gen "And how am I supposed to do that?" ("base", xpos="far_left", ypos="head")
            cho "How would I know, I'm not a teacher, am I?...{w} Ask one of them." ("annoyed", "base", "base", "mid")
            if states.cho.ev.quidditch.e9_complete:
                gen "Well, I asked Snape..." ("base", xpos="far_left", ypos="head")
                cho "And how did that work out for you?" ("open", "narrow", "raised", "mid")
                gen "It didn't." ("base", xpos="far_left", ypos="head")
                cho "Ask another teacher then..." ("annoyed", "narrow", "base", "mid")
                gen "(*Hmm*... Maybe I could ask Tonks for help during one of our hangouts?)" ("base", xpos="far_left", ypos="head")
            else:
                gen "(I wonder if Snape would help me with this...)" ("base", xpos="far_left", ypos="head")
        elif not states.cho.ev.quidditch.e8_complete:
            # Haven't done Tonks event
            cho "Have you gotten those Slytherin pigs to play yet?" ("open", "narrow", "base", "mid")
            gen "Not yet, but I'm on it." ("base", xpos="far_left", ypos="head")
            cho "Please just hurry up, Sir." ("annoyed", "narrow", "base", "mid")
            cho "We need to try out those tactics..." ("annoyed", "narrow", "worried", "R")
            gen "Any ideas on how to get them to practice against you?" ("base", xpos="far_left", ypos="head")
            cho "How would I know, I'm not a teacher, am I?...{w} Ask one of them." ("open", "narrow", "base", "mid")
            if states.cho.ev.quidditch.e9_complete:
                gen "Well, I asked Snape..." ("base", xpos="far_left", ypos="head")
                cho "And how did that work out for you?" ("open", "narrow", "raised", "mid")
                gen "It didn't." ("base", xpos="far_left", ypos="head")
                cho "Ask another teacher then..." ("annoyed", "narrow", "base", "mid")
                gen "(*Hmm*... Maybe I could ask Tonks for help during one of our hangouts?)" ("base", xpos="far_left", ypos="head")
            else:
                gen "(I wonder if Snape would help me with this...)" ("base", xpos="far_left", ypos="head")
        elif not states.cho.ev.quidditch.e7_complete:
            # Haven't done Hermione event
            cho "Will Hermione commentate the match or not?" ("open", "base", "base", "mid")
            gen "Probably..." ("base", xpos="far_left", ypos="head")
            cho "What do you mean probably?" ("clench", "base", "raised", "mid")
            gen "I haven't confronted her about it yet." ("base", xpos="far_left", ypos="head")
            cho "Then do it!" ("open", "base", "angry", "mid")
    elif states.cho.ev.quidditch.e5_complete and not states.cho.ev.quidditch.e6_complete:
        cho "I'm still a bit worried about those brutes..." ("annoyed", "base", "raised", "down")
        cho "You better find a foolproof way of dealing with them." ("soft", "base", "angry", "mid")
        gen "(Perhaps I should {b}talk to her{/b} more, the problem might solve itself.)" ("base", xpos="far_left", ypos="head")
    elif states.cho.ev.talk_to_me.t2_e3_complete and not states.cho.ev.quidditch.lock_tactic:
        cho @ cheeks blush "You really believe that showing off my ass is the best tactic against Slytherin?" ("soft", "base", "base", "R")
        gen "I'm certain of it..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("annoyed", "base", "worried", "R") #Worried
        gen "(Perhaps doing some more favours will improve her confidence.)" ("base", xpos="far_left", ypos="head")
    else:
        cho "I'm confident that we can win this, [name_genie_cho]." ("smile", "base", "base", "mid")
        cho "Slytherin has no blasted chance against us!" ("base", "narrow", "base", "mid")

    cho "" (xpos="base", ypos="base", trans=fade)

    jump cho_training.choices
