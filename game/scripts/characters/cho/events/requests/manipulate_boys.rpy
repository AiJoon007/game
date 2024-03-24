

### Manipulate the enemy male Quidditch players ###

### Start ###
label cc_pr_manipulate_boys_start:

    cho "" (xpos="right", ypos="base", trans=fade)

    ### Tier 1 (pre Hufflepuff) ###
    if states.cho.tier == 1:

        # Intro
        if not _events_filtered_completed_any:
            gen "So what do we know about our opponents?" ("base", xpos="far_left", ypos="head")
            cho "Hufflepuff? Well, their team isn't the best, but they have a really strong seeker." ("soft", "base", "base", "mid")
            gen "Right...{w=0.3} who was that again?" ("base", xpos="far_left", ypos="head")
            cho "Cedric Diggory. How often do I have to repeat that to you, [name_genie_cho]?" ("annoyed", "narrow", "base", "mid")
            gen "You will understand once you get to be my age..." ("base", xpos="far_left", ypos="head")
            cho "Oh, I'm sorry, Sir." ("soft", "narrow", "worried", "mid")
            cho "I should be more respectful of your age." ("soft", "narrow", "base", "downR")
            gen "(Because at my age you stop giving a damn...)" ("base", xpos="far_left", ypos="head")
            cho "Cedric is a bit of a blockhead, but he's quite a competent seeker." ("open", "base", "raised", "R")
            cho "And very popular with the girls..." ("soft", "base", "raised", "mid")
            gen "Do I sense a little bit of something in your voice?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Of course not! We stopped dating ages ago!" ("soft", "base", "base", "downR")
            cho "I didn't want to be seen with an idiot like him anymore..." ("open", "closed", "angry", "mid")
            cho "Not if I'm supposed to be a proper Ravenclaw..." ("annoyed", "narrow", "angry", "mid")
            cho @ cheeks blush "{size=-4}Even if he's cute...{/size}" ("normal", "base", "worried", "downR") # Small text.
            gen "That's good. We can use this to our advantage." ("base", xpos="far_left", ypos="head")
            cho "We can? How?" ("soft", "wide", "base", "mid")
            gen "You two, having history! Which means he'll be much easier to distract during the game." ("base", xpos="far_left", ypos="head")
            gen "All you have to do is make him believe something might actually happen." ("base", xpos="far_left", ypos="head")
            cho "What?{w=0.3} I don't want to go out with Cedric again!" ("angry", "wide", "base", "mid")
            gen "I know, I know, you just have to make him believe that you will." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Oh..." ("soft", "base", "base", "downR")
            cho "Well... how do I do that?" ("annoyed", "base", "base", "mid")
            gen "It's a little something called {b}seduction{/b}..." ("base", xpos="far_left", ypos="head")
            gen "It should be your gender's bread and butter." ("base", xpos="far_left", ypos="head")
            cho "Isn't that a little mean?" ("soft", "closed", "base", "mid")
            gen "Mean? You're not doing anything wrong, are you?" ("base", xpos="far_left", ypos="head")
            gen "You're just talking to him..." ("base", xpos="far_left", ypos="head")
            cho "So I'm just supposed to lead him down the garden path?" ("soft", "base", "raised", "mid")
            gen "Only if you want Ravenclaw to have a chance at winning." ("base", xpos="far_left", ypos="head")
            cho "*Hmm*..." ("annoyed", "narrow", "base", "R")
            gen "And don't worry about him.{w} He's hardly going to complain about having a pretty little thing like you to talk to..." ("base", xpos="far_left", ypos="head")
            gen "Not to mention look at..." ("grin", xpos="far_left", ypos="head")
            cho "Hey!" ("soft", "base", "base", "mid")
            gen "I'm just saying, he hasn't got anything to whine about." ("base", xpos="far_left", ypos="head")
            gen "And if you are worried about his feelings..." ("base", xpos="far_left", ypos="head")
            gen "Maybe you can fool around a little... I'm sure that would make him forget all about the garden path..." ("base", xpos="far_left", ypos="head")
            cho "Sir!" ("mad", "narrow", "base", "mid")
            gen "I'm just telling you to use what the gods gave you -- to try and win a game." ("base", xpos="far_left", ypos="head")
            cho "Can't I use what they gave me to catch the snitch?" ("annoyed", "narrow", "angry", "mid")
            gen "And how's that plan been working out so far?" ("base", xpos="far_left", ypos="head")
            cho "*Ugh!* Fine...{w} Point taken..." ("annoyed", "narrow", "angry", "R")
            cho "So I just have to make him think there's something between us again?" ("soft", "base", "base", "mid")
            cho "I think I can do that..." ("annoyed", "narrow", "base", "down")
            gen "Good, let me know how it goes..." ("base", xpos="far_left", ypos="head")
            cho "Yes, [name_genie_cho]!" ("base", "base", "base", "mid")

        # Repeated
        else:
            gen "Ready to mess with Hufflepuff again?" ("base", xpos="far_left", ypos="head")
            cho "I guess so..." ("soft", "base", "base", "mid")
            gen "Great! I'll see you later today for your report, [name_cho_genie]!" ("grin", xpos="far_left", ypos="head")
            cho "Yes, [name_genie_cho]!" ("base", "base", "base", "mid")

    ### Tier 2 (pre Slytherin) ###
    elif states.cho.tier == 2:

        # Intro
        if not _events_filtered_completed_any:
            gen "[name_cho_genie], how well -- in your opinion -- did you do in your last match?" ("base", xpos="far_left", ypos="head")
            cho "Well, I pretty much secured the win for my team, distracting those Hufflepuffs--" ("base", "closed", "base", "mid")
            gen "Only one Hufflepuff!{w=0.6} We were lucky you could secure that win with such low effort..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "(...)" ("annoyed", "closed", "base", "mid")
            gen "We have to up our game to win against the next house, don't you think?" ("base", xpos="far_left", ypos="head")
            gen "Manipulating just one player won't be enough this time! We have to put our focus on their entire team!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Hmm*... As much as I don't like it, you might be right about that, [name_genie_cho]." ("open", "narrow", "worried", "downR")
            cho "Slytherin's team is quite good overall, and they have some of the best players at this school." ("open", "narrow", "base", "mid")
            cho "What do you suggest I should do?" ("annoyed", "narrow", "worried", "mid")
            gen "Same as with that Diggory boy!" ("base", xpos="far_left", ypos="head")

            menu:
                "\"Be affectionate and flirty!\"":
                    gen "Just go and talk to them, and flirt with them for a bit..." ("angry", xpos="far_left", ypos="head")
                    cho "I suppose I can do that." ("annoyed", "base", "base", "downR")
                    cho "But, Sir... What if someone were to see me with them?" ("soft", "narrow", "angry", "mid")

                "\"Make out with them...\"":
                    cho @ cheeks heavy_blush "Make out with?{w=0.6} Those Slytherins--" ("soft", "wide", "worried", "mid")
                    cho @ cheeks blush "*guargh*" ("open_tongue", "happyCl", "angry", "mid", trans=hpunch)
                    cho @ cheeks blush "*cough*{w=0.6}-*guargh*!{w=0.8}-*cough*" ("open_wide_tongue", "happyCl", "worried", "mid", trans=hpunch)
                    nar "You hear Cho make some inadvertent gag noises..."
                    gen "Is everything okay, girl?" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "No!{w=0.3} It's not okay!" ("angry", "wide", "worried", "mid")
                    cho @ cheeks blush "Why would you think I want to snog those repulsive, yuck-ugly Slytherin degenerates?!" ("open", "wide", "worried", "mid")
                    cho @ cheeks blush "The thought alone utterly disgusts me, [name_genie_cho]!" ("open_tongue", "happyCl", "worried", "mid")
                    cho "I'll do anything but that!" ("mad", "narrow", "worried", "mid")
                    gen "So no kissing?" ("base", xpos="far_left", ypos="head")
                    cho @ cheeks blush "Absolutely not!{w=0.8} Not even with Malfoy..." ("angry", "closed", "angry", "mid")
                    gen "Very well.{w=0.3} Just flirt with them in that case..." ("base", xpos="far_left", ypos="head")
                    cho "And what if someone were to see me with them?" ("soft", "narrow", "angry", "mid")

            gen "Would that be an issue?" ("base", xpos="far_left", ypos="head")
            cho "Since they are on the enemy team, yes!" ("annoyed", "narrow", "angry", "mid")
            cho "What if my team were to find out I hang around Slytherins?" ("angry", "base", "base", "mid")
            cho "{b}Slytherins!!{/b}" ("clench", "wide", "base", "mid")
            gen "So? Just do it in secret then." ("base", xpos="far_left", ypos="head")
            cho "That...{w=0.3} might work." ("annoyed", "base", "base", "R")
            gen "Don't you have any classes with them?" ("base", xpos="far_left", ypos="head")
            cho "I do on some days." ("annoyed", "closed", "base", "mid")
            gen "Then give them a note to meet you alone once the class is finished.{w=0.6} Easy..." ("base", xpos="far_left", ypos="head")
            cho "I guess I could do that." ("open", "narrow", "base", "down")
            gen "They can read, right?" ("base", xpos="far_left", ypos="head")
            cho "Yes, I do believe they can read.{w=0.8} But don't take my word for it..." ("soft", "narrow", "base", "mid")
            gen "You need to find a way to convince them to throw the game. It's our only chance..." ("base", xpos="far_left", ypos="head")
            #gen "Do you have any ideas how you could accomplish that?" ("base", xpos="far_left", ypos="head")
            #cho "I-- *Ehm*..." ("annoyed", "base", "base", "R")
            #cho "I could still try to flirt with them a bit, I guess." ("soft", "base", "worried", "mid")
            #gen "I doubt that that will be enough..." ("base", xpos="far_left", ypos="head")
            #cho "" ("annoyed", "base", "worried", "mid")
            cho "I'll try my best, [name_genie_cho]." ("smile", "narrow", "base", "mid")
            gen "Let's just see how it goes." ("base", xpos="far_left", ypos="head")
            gen "If anything goes wrong...{w=0.8} just improvise..." ("base", xpos="far_left", ypos="head")
            cho "Very well, Sir." ("base", "base", "base", "mid")
            gen "Report back to me later today with your results." ("base", xpos="far_left", ypos="head")
            cho "Yes, Sir!" ("smile", "base", "base", "mid")

        # Repeated
        else:
            gen "Time to brighten up some Slytherin's day again..." ("base", xpos="far_left", ypos="head")
            gen "Go and get their players on {i}your{/i} side!" ("grin", xpos="far_left", ypos="head")
            cho "I will try my best, [name_genie_cho]!" ("smile", "narrow", "base", "mid")
            gen "Report to me later as usual, [name_cho_genie]!" ("grin", xpos="far_left", ypos="head")
            cho "Yes, Sir!" ("base", "base", "base", "mid")

    ### Tier 2 (pre Gryffindor) ###
    elif states.cho.tier == 3:
        if not states.cho.ev.manipulate_boys.t3_e1_complete: # Completed The Twins?

            if not states.cho.ev.spy_on_boys.t3_e1_complete:
                # Return if player has not spied on the Twins just yet.

                gen "Let's try and manipulate the boys on the enemy team!" ("base", xpos="far_left", ypos="head")
                cho "You're expecting me to just jump in blind?" ("angry", "base", "base", "mid")
                cho "I don't know any of these boys, how do you expect me to manipulate them in any way without knowing what I'm dealing with?" ("annoyed", "wide", "base", "mid")
                gen "Good point, perhaps we should consider spying on them a bit beforehand." ("base", xpos="far_left", ypos="head")

                cho "" (xpos="base", ypos="base", trans=fade)

                $ _event.cancel()
                jump cho_favor_menu

            gen "Time to manipulate the enemy a bit." ("base", xpos="far_left", ypos="head")

            gen "Today I'd like you to target the boys." ("base", xpos="far_left", ypos="head")
            cho "Okay..." ("open", "base", "base", "R")
            gen "Let's start off with the twins." ("base", xpos="far_left", ypos="head")
            gen "Remind me what we know about them." ("base", xpos="far_left", ypos="head")
            cho "They mostly focus on trickery and pranks, doing anything for a laugh..." ("soft", "narrow", "base", "mid")
            gen "Perhaps stooping to the Twins' level could help you learn more about them." ("base", xpos="far_left", ypos="head")
            cho "What do you mean by that?" ("annoyed", "base", "raised", "mid")
            gen "Since they're tricksters and love disrupting things..." ("base", xpos="far_left", ypos="head")
            gen "I suggest trying to find a way to make them use one of their tricks during the game. Surely they wouldn't be able to help themselves if presented an opportunity." ("base", xpos="far_left", ypos="head")
            cho "Okay then." ("soft", "base", "base", "mid")
            cho "Wish me luck!" ("open", "narrow", "base", "mid")
            gen "Good luck." ("base", xpos="far_left", ypos="head")

        elif not states.cho.ev.manipulate_boys.t3_e2_complete: # Completed Ron Weasley?

            if not states.cho.ev.spy_on_boys.t3_e2_complete:
                # Return if player has not spied on Ron Weasley just yet.

                gen "Let's try and manipulate--" ("base", xpos="far_left", ypos="head")
                cho "I'm going to stop you there..." ("angry", "base", "raised", "mid")
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                cho "There's no way I'll try this again before I know more about the boys." ("annoyed", "base", "angry", "mid")
                gen "Fine..." ("base", xpos="far_left", ypos="head")

                cho "" (xpos="base", ypos="base", trans=fade)

                $ _event.cancel()
                jump cho_favor_menu

            gen "Let's target the other Weasley boy this time." ("base", xpos="far_left", ypos="head")
            cho "You actually want me to target that pervert?" ("disgust", "narrow", "base", "mid")
            gen "Sort of... He won't be the main goal of this operation." ("base", xpos="far_left", ypos="head")
            cho "Then, what is?" ("annoyed", "base", "base", "mid")
            gen "Miss Granger is quite protective of her friends, isn't she?" ("base", xpos="far_left", ypos="head")
            cho "I guess... The few times I've seen them without her, she's usually just around the corner talking to some teacher or another." ("open", "narrow", "base", "downR")
            gen "Then use those moments to your advantage... And remember, Miss Granger is also part of the game." ("base", xpos="far_left", ypos="head")
            gen "If you can somehow spark that jealousy or protectiveness of her friends..." ("base", xpos="far_left", ypos="head")
            gen "Angering her enough could transfer to the game... And since she'll be stuck in the commentator booth the whole time, she won't be able to pull them away from you." ("base", xpos="far_left", ypos="head")
            cho "..." ("mad", "wide", "raised", "mid")
            cho "That might actually work..." ("crooked_smile", "base", "base", "R")
            cho "If anything, it gives me an excuse to piss her off..." ("crooked_smile", "closed", "base", "mid")
            cho "Not that I've needed one previously." ("smile", "closed", "base", "mid") #smirk
            gen "Then it's settled, report to me in the evening as usual." ("base", xpos="far_left", ypos="head")
            cho "Will do!" ("smile", "base", "base", "mid")

        elif not states.cho.ev.manipulate_boys.t3_e3_complete: # Completed Harry Potter?

            if not states.cho.ev.spy_on_boys.t3_e3_complete:
                # Return if player has not spied on Harry Potter just yet.
                gen "Let's try and manipulate--" ("base", xpos="far_left", ypos="head")
                cho "I'm going to stop you there..." ("angry", "base", "raised", "mid")
                gen "Yes?" ("base", xpos="far_left", ypos="head")
                cho "There's no way I'll try this again before I know more about the boys." ("annoyed", "base", "angry", "mid")
                gen "Fine..." ("base", xpos="far_left", ypos="head")

                cho "" (xpos="base", ypos="base", trans=fade)

                $ _event.cancel()
                jump cho_favor_menu

            gen "How about we annoy Miss Granger some more?" ("base", xpos="far_left", ypos="head")
            cho "Of course!" ("crooked_smile", "base", "base", "mid")
            gen "Let's target her other friend today." ("base", xpos="far_left", ypos="head")
            cho "Harry P--" ("smile", "base", "raised", "mid")
            gen "The Potter boy!" ("angry", xpos="far_left", ypos="head")
            cho "..." ("mad", "base", "base", "mid") #annoyed
            gen "*Ahem*... Yes..." ("base", xpos="far_left", ypos="head")
            gen "Try and really get under her skin this time!" ("base", xpos="far_left", ypos="head")
            cho "That shouldn't be very hard, seeing how she reacted last time..." ("smile", "base", "raised", "R")
            cho "Wish me luck!" ("smile", "base", "base", "mid")
            gen "Good luck." ("base", xpos="far_left", ypos="head")

        else:
            # Repeated

            gen "Let's manipulate those boys some more!" ("base", xpos="far_left", ypos="head")
            cho "I thought we were done?" ("angry", "base", "base", "mid")
            cho "Although..." ("soft", "base", "base", "R")
            cho "I could annoy Hermione some more!" ("crooked_smile", "wide", "base", "mid")
            gen "Don't forget the tw--" ("base", xpos="far_left", ypos="head")
            cho "This will be so much fun!" ("crooked_smile", "happyCl", "base", "mid")

            # Cho leaves early!
            call cho_walk(action="leave")

            gen "Twins..." ("base", xpos="far_left", ypos="head")
            gen "Well, can't say she lacks motivation anymore..." ("base", xpos="far_left", ypos="head")

            jump end_cho_event


    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event

### Tier 1 (pre Hufflepuff) ###

label cc_pr_manipulate_boys_T1_intro_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "How did it go?" ("base", xpos="far_left", ypos="head")
    cho "It went...{w=0.3} well?" ("soft", "base", "raised", "R")
    cho "Maybe a little too well... He tried to kiss me!" ("annoyed", "base", "raised", "mid")
    gen "Really? Nice work!{w=0.6} Did you slip him a little tongue?" ("grin", xpos="far_left", ypos="head")
    cho "[name_genie_cho]!{w=0.3} No, of course not!" ("soft", "wide", "base", "mid")
    gen "Why not?" ("base", xpos="far_left", ypos="head")
    cho "Because I'm not some slut who gives it away for free!" ("annoyed", "narrow", "angry", "mid")
    gen "It was only a kiss..." ("base", xpos="far_left", ypos="head")
    gen "(Now I'm falling asleep {unicode}♫{/unicode})" ("base", xpos="far_left", ypos="head")
    cho "A kiss is very personal!" ("soft", "closed", "base", "mid")
    cho "Besides, he didn't even try to make it special!" ("annoyed", "narrow", "angry", "R")
    cho "He just leaned in while I was in the middle of a conversation..." ("annoyed", "narrow", "angry", "mid")
    gen "Sounds special enough to me." ("base", xpos="far_left", ypos="head")
    cho "Well it wasn't! I want a bit of romance..." ("soft", "closed", "base", "mid")
    gen "At least it sounds like you're doing a good job distracting him." ("base", xpos="far_left", ypos="head")
    cho "If you say so..." ("annoyed", "base", "base", "down")
    gen "Just keep in mind why we're doing this." ("base", xpos="far_left", ypos="head")
    gen "You can't chicken out of something as small as a kiss -- if you want Ravenclaw to have a chance!" ("angry", xpos="far_left", ypos="head")
    cho "Right, [name_genie_cho]!" ("soft", "narrow", "worried", "mid")
    gen "That'll be all for now, you can go." ("base", xpos="far_left", ypos="head")
    cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 3: # Points til 3.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T1_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "What's my favourite Quidditch player been up to today?" ("base", xpos="far_left", ypos="head")
    cho "I think you'll be happy, [name_genie_cho]!" ("base", "narrow", "base", "mid")
    gen "I like the sound of that! Tell me what happened." ("grin", xpos="far_left", ypos="head")
    cho "Well, I thought about the best way to get to Cedric -- and I remembered how much he loved my bum!" ("soft", "base", "base", "R")
    gen "*Mhmm*... I can't say I blame him..." ("base", xpos="far_left", ypos="head")
    gen "Let me guess, you tried the old \"drop your pencil trick\" on him?" ("base", xpos="far_left", ypos="head")
    cho "\"Pencil trick\"?" ("mad", "base", "raised", "mid")
    gen "Yes. You \"accidentally\" drop your pencil, and then when you have the boy's attention, you bend down and--" ("base", xpos="far_left", ypos="head")
    cho "Sir, we're only allowed to use \"quills\" here." ("soft", "closed", "base", "mid")
    gen "So just use \"quills\" instead?" ("base", xpos="far_left", ypos="head")
    cho "That would just make a mess and get ink everywhere..." ("annoyed", "narrow", "angry", "mid")
    cho "But I {b}did{/b} try something close to what you described..." ("soft", "base", "base", "mid")
    gen "You did?" ("grin", xpos="far_left", ypos="head")
    cho "Yes, Sir.{w=0.3} I pretended to drop my books, and when I bent down to pick them up, I gave Cedric a good view of my bum." ("base", "narrow", "angry", "mid")
    gen "So...{w=0.3} you did the \"pencil trick\"...{w=0.8} Just with books." ("base", xpos="far_left", ypos="head")
    cho "I've put my own spin on it. It's different enough..." ("soft", "closed", "base", "mid")
    gen "No it isn't." ("base", xpos="far_left", ypos="head")
    cho "In any case, I think it worked." ("open", "narrow", "raised", "R")
    cho "He couldn't keep his eyes off my bum for the rest of classes!" ("base", "narrow", "angry", "mid")
    gen "Well done, [name_cho_genie]! You may leave now." ("grin", xpos="far_left", ypos="head")
    cho "Thank you, Sir." ("smile", "happyCl", "base", "mid")

    if states.cho.public_level < 3: # Points til 3.
        $ states.cho.public_level += 1

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_event


label cc_pr_manipulate_boys_T1_E2:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_cho_genie]! Do you have some good news for me?" ("angry", xpos="far_left", ypos="head")
    cho "I'm afraid not this time, Sir." ("soft", "narrow", "worried", "mid")
    gen "Why not? Tell me what happened..." ("base", xpos="far_left", ypos="head")
    cho "Well, today I saw Cedric again down in the dungeons." ("open", "narrow", "worried", "R")
    gen "{size=-2}(The dungeons? I like where this is going already!){/size}" ("grin", xpos="far_left", ypos="head")
    cho "Before I approached him, I removed my Ravenclaw tie, and unbuttoned the top of my blouse." ("open", "closed", "base", "mid")
    gen "A very well-thought-out strategy, girl!" ("base", xpos="far_left", ypos="head")
    cho "I thought it would be enough to get his attention." ("soft", "narrow", "raised", "mid")
    gen "Which I assume you got straight away?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No, Sir. But somebody else's..." ("disgust", "narrow", "worried", "down")
    gen "Intriguing!{w=0.3} Who else did you manage to snag?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Professor Slughorn, Sir." ("mad", "base", "worried", "mid")
    gen "Who?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "{size=+4}Professor Slughorn!{/size}" ("scream", "closed", "angry", "mid", trans=hpunch)
    cho "He -- once again -- had to stand in for professor Snape, who couldn't make it in time for his lecture." ("open", "narrow", "angry", "R")
    gen "Snape is missing his classes? For how long has this been happening?" ("base", xpos="far_left", ypos="head")
    cho "Probably every other week or so." ("annoyed", "narrow", "raised", "R")
    gen "{size=-2}(Slacker...){/size}" ("base", xpos="far_left", ypos="head")
    cho "Anyway...{w=0.3} Slughorn sort of crossed paths with me when I was about to confront Cedric..." ("open", "narrow", "worried", "mid")
    cho "He came out of nowhere!" ("soft", "wide", "base", "mid")
    cho @ cheeks blush "And he stood so close, he could see right down my cleavage!" ("disgust", "narrow", "worried", "down")
    gen "{size=-2}(What a lucky git!){/size}" ("angry", xpos="far_left", ypos="head")
    cho "I couldn't move a single muscle! It was like I was frozen in place!" ("soft", "narrow", "worried", "R")
    cho "What if something like that happened during the game?!" ("soft", "narrow", "worried", "mid")
    gen "You're right. That could be an issue..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "And the worst thing is, he just kept staring!" ("clench", "happyCl", "worried", "mid")
    gen "And then? What happened?" ("base", xpos="far_left", ypos="head")
    cho "He commended me about how well I did in my last potion lesson with him, then awarded Ravenclaw five house points for my efforts." ("soft", "narrow", "angry", "mid")
    gen "Sounds like a nice guy..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "But Sir, I ruined my potion during the last lesson I had with him!" ("quiver", "narrow", "worried", "mid")
    cho @ cheeks blush "The only reason he gave me those points, is because I let him stare down my shirt!" ("disgust", "narrow", "worried", "down")
    cho @ cheeks blush "I feel so dirty because of it..." ("disgust", "happyCl", "worried", "down")
    gen "You shouldn't feel dirty...{w=0.6} Maybe only \"a little\" dirty, if anything..." ("base", xpos="far_left", ypos="head")
    cho "I'm sorry, Sir.{w=0.3} May I have permission to leave?" ("soft", "narrow", "worried", "mid")
    gen "Permission granted...{w=0.3} But try to be more effective next time." ("base", xpos="far_left", ypos="head")
    cho "I will, Sir." ("open", "narrow", "worried", "down")
    cho "Have a nice day." ("soft", "narrow", "worried", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 3: # Points til 3.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T1_E3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So? How did it go?" ("base", xpos="far_left", ypos="head")
    cho "Very well, Sir!" ("smile", "base", "base", "mid")
    gen "Yeah? Tell me about it!" ("grin", xpos="far_left", ypos="head")
    cho "I ran into Cedric on my way to the library...{w} Literally!" ("soft", "wide", "base", "mid")
    cho "I bumped into him and hit my head pretty hard..." ("soft", "narrow", "worried", "mid")
    gen "You poor thing..." ("base", xpos="far_left", ypos="head")
    cho "It's nothing, Sir. I'm more than capable of enduring pain!" ("soft", "narrow", "angry", "R")
    gen "A useful skill to have, I can imagine..." ("base", xpos="far_left", ypos="head")
    cho "I've grown to be quite tough -- and resistant to all sorts of pain -- after years of playing Quidditch..." ("mad", "narrow", "angry", "mid")
    play sound "sounds/gulp.ogg"
    gen "*gulp!*" ("angry", xpos="far_left", ypos="head")
    cho "Anyway... Cedric helped me back up on my feet." ("soft", "narrow", "base", "R")
    cho @ cheeks blush "But before he could even apologise, I kissed him." ("base", "narrow", "base", "mid")
    cho @ cheeks blush "It just... happened..." ("clench", "narrow", "worried", "downR")
    gen "Well done, girl!" ("base", xpos="far_left", ypos="head")
    cho "It was really nice, though." ("soft", "narrow", "base", "mid")
    cho "He still is a really good kisser!" ("horny", "narrow", "base", "R")
    cho "Compared to most of the others I had..." ("base", "narrow", "base", "mid")
    gen "!!!" ("angry", xpos="far_left", ypos="head")
    cho "Anyhow, I should get going." ("open", "base", "base", "R")
    cho "It's getting late..." ("soft", "base", "worried", "mid")
    gen "Of course. You are dismissed." ("base", xpos="far_left", ypos="head")
    cho "Good night, [name_genie_cho]." ("smile", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 3: # Points til 3.
        $ states.cho.public_level += 1

    jump end_cho_event



### Tier 2 (pre Slytherin) ###

label cc_pr_manipulate_boys_T2_intro_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "worried", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Good evening [name_cho_genie]... How did today's task go?" ("base", xpos="far_left", ypos="head")
    cho "I can't believe you convinced me to do this!" ("disgust", "narrow", "worried", "mid")
    gen "So...{w=0.3} badly I take it?" ("base", xpos="far_left", ypos="head")
    cho "No, it went perfectly..." ("annoyed", "narrow", "angry", "mid")
    gen "So why the face?" ("base", xpos="far_left", ypos="head")
    cho "Well, I did as you suggested.{w=0.6} I left a note for them to meet me alone after class." ("annoyed", "base", "worried", "downR")
    gen "Great, so did they show?" ("base", xpos="far_left", ypos="head")
    cho "Yes... Apparently they could read after all... And they met up with me after the lesson." ("soft", "narrow", "worried", "R")
    cho @ cheeks blush "Once everyone had left, and we were alone in the corridor... Well, I didn't really know how to go about it." ("quiver", "narrow", "worried", "mid")
    cho @ cheeks blush "They must have felt how awkward I was as I approached them...{w=0.8} Or they had literally never had any woman approach them before." ("quiver", "base", "worried", "mid")
    gen "So they didn't get that you were coming onto them?{w=0.6} Surely they can't be that thick..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "No, sir. They got it alright...{w=0.6} perhaps a little too well." ("annoyed", "base", "worried", "down")
    cho "Or they're just used to treating those Slytherin skanks as their personal squeeze toys..." ("annoyed", "narrow", "angry", "R")
    gen "So, what happened?" ("base", xpos="far_left", ypos="head")
    cho "I came onto them a little bit...{w=0.6} Told them how impressed I was when watching their practice match against Gryffindor." ("open", "closed", "base", "mid")
    gen "Boosting their ego... Good idea." ("base", xpos="far_left", ypos="head")
    cho "Thanks." ("soft", "narrow", "base", "downR")
    cho @ cheeks blush "I couldn't stand the idea of complimenting them on their looks, so instead I told them how impressed I was with their pure strength...{w=0.8} which technically isn't a lie." ("horny", "narrow", "worried", "down")
    gen "Understandable... but what about making them go a bit easier on you during the game itself?" ("base", xpos="far_left", ypos="head")
    cho "I'm getting to it..." ("open", "happyCl", "worried", "mid")
    cho "So, I tried my best to put on a charming voice, and asked if there was anything I could do to persuade them to go easy on me..." ("soft", "narrow", "base", "R")
    cho "And of course they had no clue what I was getting at...{w=0.4} Those knuckleheads just do whatever Draco tells them to do." ("soft", "narrow", "base", "mid")
    gen "Sounds like trying to make a cat understand how to bark." ("base", xpos="far_left", ypos="head")
    cho "Exactly..." ("annoyed", "narrow", "worried", "R")
    cho "I was a bit frustrated at that point, and running out of options on how I could even make my intentions clear to them..." ("soft", "narrow", "worried", "mid")
    cho @ cheeks heavy_blush "So I lifted my skirt a bit to show them my panties." ("soft", "happyCl", "worried", "mid")
    gen "You go, girl!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well, that's where I messed up...{w=0.6} They took it as an invitation and squeezed my butt cheeks quite hard and painfully." ("quiver", "narrow", "worried", "mid")
    gen "Ouch, then what happened?" ("base", xpos="far_left", ypos="head")
    cho "I pushed them away, of course! I won't just let them grope me as they please!" ("open", "wide", "base", "mid")
    cho @ cheeks blush "But...{w=0.3} I did tell them right after -- if they're kind to me during the game -- that I'll reward them handsomely for it..." ("horny", "narrow", "base", "downR")
    cho @ cheeks blush "Not that I have any intentions to do so..." ("annoyed", "narrow", "angry", "R")
    gen "Of course not..." ("base", xpos="far_left", ypos="head")
    gen "And what about the butt squeeze?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "What about it, sir?" ("soft", "wide", "base", "mid")
    gen "Did you like it?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Sir! They're Slytherins!" ("angry", "wide", "base", "mid")
    gen "That's not what I asked." ("base", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "narrow", "angry", "mid")
    cho "Can I please go now, Sir?{w} I've done what you asked of me." ("soft", "narrow", "angry", "R")
    gen "Yes, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    gen "You've done a great job today, you're definitely getting closer to beating those pesky Slytherins." ("base", xpos="far_left", ypos="head")
    cho "Thank you, Sir." ("base", "narrow", "base", "mid")
    gen "If you remind them of your meeting during the match, then I'm certain their desire to win... will wash away." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Hmph*..." ("horny", "narrow", "base", "downR")
    cho "I'll do my best." ("soft", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 9: # Points til 9.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_E1:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    cho "Sir, I managed to corner their seeker when he came out of the boys' bathroom." ("soft", "narrow", "base", "mid")
    cho "It's one of the few times those thugs weren't hanging around with him, you see." ("soft", "narrow", "base", "down")
    gen "Him?" ("base", xpos="far_left", ypos="head")
    cho "Malfoy..." ("soft", "narrow", "worried", "mid")
    cho "I cornered him and pushed him back into the bathroom." ("annoyed", "narrow", "base", "R")
    gen "That's against the school rules, Miss Chang..." ("base", xpos="far_left", ypos="head")
    cho "But I thought--" ("soft", "base", "worried", "mid")
    gen "Forget I just said that..." ("base", xpos="far_left", ypos="head")
    gen "Please continue." ("grin", xpos="far_left", ypos="head")
    cho "Oh, well... I asked him if he had ever touched a Quidditch player's ass before." ("soft", "base", "base", "R")
    cho "And before he could answer -- I pushed him up onto the wall, and put his hand around my waist -- right on my butt cheeks!" ("base", "narrow", "angry", "mid")
    gen "Impressive!" ("grin", xpos="far_left", ypos="head")
    gen "And what was his reaction?" ("base", xpos="far_left", ypos="head")
    cho "At first he was mostly surprised by the circumstance..." ("soft", "base", "base", "R")
    cho "But then I clenched my cheeks, so he could get a good feel of what a real athlete feels like." ("smile", "narrow", "angry", "mid")
    cho "When that happened he went from surprised to shocked." ("base", "narrow", "angry", "mid")
    cho "You should have seen it.{w=0.6} I was actually not as repulsed as I thought I might be." ("horny", "narrow", "base", "mid")
    cho "It was quite thrilling, actually." ("base", "narrow", "angry", "mid")
    gen "Why wouldn't you be, you've worked hard on your body." ("base", xpos="far_left", ypos="head")
    gen "Now you're starting to see some of the benefits." ("base", xpos="far_left", ypos="head")
    cho "Yeah... yeah! You're right!" ("soft", "wide", "base", "mid")
    gen "And he's not going to forget it.{w=0.6} I'm sure the snitch will be the last thing on his mind during the upcoming game!" ("base", xpos="far_left", ypos="head")
    cho "You know..." ("soft", "base", "base", "R")
    cho "You're smarter than I gave you credit for... you've not been wrong so far..." ("annoyed", "base", "base", "R")
    gen "That's why I'm the headmaster." ("grin", xpos="far_left", ypos="head")
    cho "Will that be all?" ("soft", "base", "base", "mid")
    gen "Yes [name_cho_genie], good work today!" ("base", xpos="far_left", ypos="head")
    cho "Thanks!" ("base", "base", "base", "mid")
    gen "Have a good night..." ("base", xpos="far_left", ypos="head")
    cho "Good night, [name_genie_cho]." ("smile", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 9: # Points til 9.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_intro_E2:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    gen "Back already? How did it go?" ("base", xpos="far_left", ypos="head")
    cho "Not too great this time, [name_genie_cho]." ("soft", "narrow", "worried", "R")
    gen "No? What happened?" ("base", xpos="far_left", ypos="head")
    cho "Nothing, actually. I didn't see any of their team members all day. Not even at the Quidditch pitch..." ("annoyed", "narrow", "worried", "mid")
    gen "Odd... Were they hiding from you?" ("base", xpos="far_left", ypos="head")
    cho "I believe they were, Sir..." ("soft", "closed", "base", "mid")
    gen "So, are they afraid of confronting you face to face? Why are they avoiding you?" ("grin", xpos="far_left", ypos="head")
    cho "I have reason to believe that they were observing me all day." ("soft", "narrow", "angry", "mid")
    gen "They were stalking you?" ("base", xpos="far_left", ypos="head")
    cho "You could say that." ("annoyed", "base", "base", "R")
    cho "I swear I could see Malfoy's blonde head around a corner at one point..." ("soft", "narrow", "angry", "downR")
    cho "But when I was about to confront them, I heard them running off..." ("soft", "narrow", "angry", "mid")
    cho "Cowards..." ("angry", "narrow", "angry", "mid")
    gen "I think this is a good thing, [name_cho_genie]!" ("base", xpos="far_left", ypos="head")
    cho "You do?" ("soft", "wide", "base", "mid")
    gen "The fact that they're following you..." ("base", xpos="far_left", ypos="head")
    gen "It proves that they are weak!{w} They are obsessed with you!" ("angry", xpos="far_left", ypos="head")
    cho "You think so?" ("annoyed", "base", "raised", "mid")
    gen "Yes! As long as you keep teasing them." ("base", xpos="far_left", ypos="head")
    gen "They won't be able to keep focus on anything else..." ("base", xpos="far_left", ypos="head")
    gen "Except your perfect bod!" ("grin", xpos="far_left", ypos="head")
    cho "I'll do my best, Sir." ("base", "base", "base", "mid")
    gen "You may go now, [name_cho_genie]. Nice work!" ("base", xpos="far_left", ypos="head")
    cho "Thank you, [name_genie_cho]!" ("smile", "base", "base", "R")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 9: # Points til 9.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T2_intro_E3:

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    gen "[name_cho_genie], how was your day?" ("base", xpos="far_left", ypos="head")
    gen "Were you successful this time?" ("base", xpos="far_left", ypos="head")
    cho "Sir, I believe they are onto me!" ("angry", "narrow", "worried", "mid")
    gen "Who are... they?" ("base", xpos="far_left", ypos="head")
    cho "Malfoy and his gang, Sir." ("soft", "base", "base", "R")
    cho @ cheeks blush "They confronted me, outside the girl's bathroom." ("angry", "narrow", "worried", "down")
    gen "How very rude of them." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "I'm just glad they didn't follow me inside, actually..." ("soft", "base", "worried", "mid")
    gen "But they're boys! They aren't allowed in there!" ("base", xpos="far_left", ypos="head")
    cho "Don't underestimate them, [name_genie_cho]." ("soft", "closed", "base", "mid")
    cho "I doubt that anything would stop them from breaking into a girl's most private place..." ("soft", "narrow", "angry", "mid")
    gen "They are ruthless!" ("angry", xpos="far_left", ypos="head")
    gen "What exactly did they want from you?" ("base", xpos="far_left", ypos="head")
    cho "They questioned me..." ("annoyed", "base", "worried", "R")
    cho @ cheeks blush "About what I'm up to... What my plan is, and why I'm acting...{w=0.8} strangely." ("soft", "narrow", "worried", "downR")
    gen "Strangely? In what way?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Typically, girls from other houses don't talk to boys from Slytherin..." ("soft", "happyCl", "worried", "mid")
    cho @ cheeks heavy_blush "Not to mention flirt with them!" ("mad", "narrow", "worried", "down")
    gen "So? What did you do?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "I panicked, [name_genie_cho]!" ("clench", "happyCl", "worried", "mid")
    cho @ cheeks blush "I tried to get out of the situation, although in my haste the only solution I could think of was to..." ("soft", "narrow", "base", "downR")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Flash them, Sir. I flashed them my breasts!" ("soft", "narrow", "worried", "mid")
    gen "Nice!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "I'm sorry, Sir.{w=0.6} I shouldn't have done it!" ("disgust", "narrow", "worried", "down")
    gen "And what was their reaction?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "I don't know... They were surprised?" ("angry", "wink", "raised", "mid")
    cho @ cheeks blush "I closed my eyes through most of it, and then I ran off..." ("soft", "base", "worried", "down")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Did I go too far, [name_genie_cho]?" ("soft", "narrow", "worried", "mid")
    gen "No girl, you did great!" ("grin", xpos="far_left", ypos="head")
    gen "You successfully got yourself out of an intricate situation." ("base", xpos="far_left", ypos="head")
    gen "You improvised, just as I taught you." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Thank you, Sir." ("base", "narrow", "worried", "mid")
    cho "But what would you suggest I do next time something like this happens?" ("soft", "narrow", "worried", "mid")
    gen "Trust your instincts, it worked once didn't it?" ("base", xpos="far_left", ypos="head")
    gen "Try it again. Show them your breasts, and see what effects it has on them..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Show them my breasts?! But I can't possibly do that!" ("clench", "wide", "base", "mid")
    gen "Why not? Didn't you just do that?" ("base", xpos="far_left", ypos="head")
    gen "They {b}have{/b} seen your tits, haven't they?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "My tits?!" ("soft", "wide", "base", "mid")
    cho @ cheeks blush "*Ehm*... I mean-- I guess they have seen them now but..." ("soft", "base", "worried", "downR")
    gen "Remember why we are doing this, girl! You need to get into their minds!" ("angry", xpos="far_left", ypos="head")
    gen "If they want to see your breasts again, or any other part of your body, you show it to them!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "But, Sir!" ("mad", "closed", "worried", "mid") # Embarrassed
    gen "Do as I say, [name_cho_genie]!" ("base", xpos="far_left", ypos="head")
    gen "Your mission, should you choose to accept it, is to please them!{w} No matter the cost!" ("angry", xpos="far_left", ypos="head")
    cho "What?!" ("soft", "wide", "base", "mid")
    gen "For now, you are dismissed." ("base", xpos="far_left", ypos="head")
    cho "Sir!" ("angry", "base", "angry", "mid")
    gen "Dismissed!{w} Now go to your dorm..." ("angry", xpos="far_left", ypos="head")
    cho "Fine..." ("annoyed", "narrow", "angry", "mid") # Annoyed
    cho "Good night, [name_genie_cho]." ("soft", "narrow", "angry", "mid") # Angry

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 9: # Points til 9.
        $ states.cho.public_level += 1

    jump end_cho_event

label cc_pr_manipulate_boys_T2_E3:

    $ states.cho.ev.manipulate_boys.t2_e4_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("annoyed", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5
    gen "[name_cho_genie]! You're back." ("grin", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "down") # Annoyed
    gen "How was your day? Anything exciting to tell me?" ("grin", xpos="far_left", ypos="head")
    cho "I-- *Ehm*..." ("soft", "narrow", "base", "down")
    cho "I did what you asked me to..." ("soft", "narrow", "worried", "mid")
    gen "Yes?" ("grin", xpos="far_left", ypos="head")
    cho "I... flashed them..." ("mad", "closed", "worried", "mid")
    gen "You showed them your tits again?!" ("angry", xpos="far_left", ypos="head")
    cho "What? No!" ("soft", "wide", "base", "mid")
    gen "But you just said--" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "They... didn't want to see them..." ("annoyed", "narrow", "angry", "downR")
    gen "Oh..." ("base", xpos="far_left", ypos="head")
    gen "(Could it be that they aren't into girls?)" ("base", xpos="far_left", ypos="head")
    cho "I was on my way to the Quidditch pitch, somewhere close to the library when they ambushed me..." ("soft", "narrow", "base", "R")
    gen "An ambush?!" ("angry", xpos="far_left", ypos="head")
    cho "I tried to be nice to them, even flirt a bit, but I just couldn't!" ("soft", "narrow", "worried", "mid")
    cho "It's hard enough to deal with one of those brutes, but three at the same time?!" ("angry", "wide", "base", "mid")
    gen "There are girls that could handle that with ease..." ("base", xpos="far_left", ypos="head")
    cho "Sir?" ("soft", "base", "raised", "mid")
    gen "Nothing... go on..." ("base", xpos="far_left", ypos="head")
    cho "They started mocking me... About what I did last time. Called me a slut, among other things..." ("soft", "narrow", "angry", "R")
    cho "Even threatened to report it as indecent behaviour..." ("angry", "narrow", "angry", "downR")
    cho "I was about to lash back as they were really starting to annoy me..." ("angry", "narrow", "worried", "mid")
    cho "But then I remembered what you told me." ("annoyed", "narrow", "base", "mid")
    cho "That I should do my best to be nice to them... and... try and please them..." ("annoyed", "base", "worried", "down")
    gen "So? What did you do?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I asked if they liked it..." ("mad", "happyCl", "worried", "mid")
    gen "Liked what?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Seeing my breasts, Sir." ("soft", "narrow", "worried", "mid")
    cho @ cheeks blush "Instead of insulting them, I begged them not to report me to a teacher -- and in return -- I'd let them see them again!" ("soft", "narrow", "worried", "R")
    gen "And then?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "They laughed at me!" ("annoyed", "narrow", "angry", "R")
    cho @ cheeks blush "Started mocking my breasts even... Calling them small..." ("annoyed", "narrow", "angry", "downR")
    gen "How foolish of those boys..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Well, I had to show them something else instead..." ("soft", "narrow", "worried", "mid")
    cho @ cheeks blush "After all, they asked for it." ("annoyed", "narrow", "worried", "down")
    gen "Intriguing..." ("angry", xpos="far_left", ypos="head")
    cho "They asked to see my bum, Sir!" ("soft", "narrow", "angry", "mid")
    gen "I see, they are men of culture..." ("grin", xpos="far_left", ypos="head")
    cho "I turned around and lowered my skirt for them..." ("annoyed", "base", "base", "down")
    gen "Sweet!" ("grin", xpos="far_left", ypos="head")
    gen "And how did they react to it?" ("base", xpos="far_left", ypos="head")
    cho "It seemed like they enjoyed it, Sir." ("soft", "closed", "base", "mid")
    cho "I mean, who wouldn't... I have a great butt." ("soft", "narrow", "angry", "R")
    gen "Yes indeed!" ("base", xpos="far_left", ypos="head")
    cho "They did ask why I keep wearing a skirt to school, though." ("annoyed", "base", "raised", "mid")
    cho "Said that it would look a lot better in trousers...{w=0.6} or some tight leggings..." ("annoyed", "base", "base", "downR")
    gen "They're not wrong... you would look great in some leggings!" ("base", xpos="far_left", ypos="head")
    cho "Anyway, I left before they had a chance to touch it..." ("annoyed", "narrow", "base", "mid")
    cho "The last thing I want is their grimy hands on it." ("annoyed", "narrow", "angry", "R")
    gen "Well, I believe you made the best out of the situation!" ("base", xpos="far_left", ypos="head")
    cho "I think so too, [name_genie_cho]!" ("base", "base", "base", "mid")
    gen "You may leave now. Exceptionally good work, [name_cho_genie]!" ("angry", xpos="far_left", ypos="head")
    cho "Thank you." ("smile", "base", "base", "R")
    gen "Dismissed." ("base", xpos="far_left", ypos="head")
    cho "Good night, Sir." ("base", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 9: # Points til 9.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_T3_twins:

    $ states.cho.ev.manipulate_boys.t3_e1_complete = True

    # Setup
    $ cho_outfit_last.save() # Save player outfit
    $ cho.strip("clothes")
    $ cho.set_body_hue(200)

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    stop music fadeout 1.0
    gen "Back so soon--" ("base", xpos="far_left", ypos="head")

    cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=fade)

    menu:
        "\"*Ha-ha-ha-ha*\"":
            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

            gen "{i}I'm blue, daba dee bada die, {size=-2}daba dee daba die,{/size} {size=-4}daba dee bada die,{/size} {size=-6}daba dee daba die........{/size}{/i}" ("grin", xpos="far_left", ypos="head")
            cho "*Grr*." ("clench", "wide", "angry", "mid")
            gen "*Ahem*...{w=0.4} I mean... Oh, no... What happened?" ("base", xpos="far_left", ypos="head")

        "\"Feeling blue today?\"":
            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

            cho "Oh? What gave it away?" ("soft", "base", "angry", "mid")
            cho "My face?" ("clench", "base", "angry", "mid")
            gen "Something like that." ("grin", xpos="far_left", ypos="head")
            gen "So, what happened?" ("base", xpos="far_left", ypos="head")

        "\"What the hell happened?\"":
            play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

            gen "Didn't expect to see a talking blueberry today!" ("grin", xpos="far_left", ypos="head")
            gen "Or are you a bilberry?" ("base", xpos="far_left", ypos="head")
            gen "Or a gummiberry?" ("grin", xpos="far_left", ypos="head")
            gen "Or maybe even a--" ("grin", xpos="far_left", ypos="head")
            cho "Could you start acting serious for just one moment?!" ("clench", "wide", "angry", "mid")
            gen "I'm berry serious." ("grin", xpos="far_left", ypos="head")
            cho "*Urghhhh*! I can't believe you!" ("disgust", "base", "angry", "mid") # Angry noises
            gen "Alright, alright. Tell me what happened." ("base", xpos="far_left", ypos="head")

    cho "What does it look like what happened?" ("upset", "base", "angry", "down")
    gen "Well, to me, it looks like you caught a case of the smurfs." ("grin", xpos="far_left", ypos="head")
    cho "Those bloody twins!" ("angry", "base", "angry", "downR")
    cho "They tricked me into eating one of their darn sweets!" ("open", "base", "angry", "mid")
    cho "You should lock those two up..." ("mad", "base", "angry", "mid")
    gen "I wish I could've been there..." ("grin", xpos="far_left", ypos="head")
    cho "{size=+4}WHAT!?{/size}" ("clench", "wide", "angry", "mid")
    gen "To stop them I mean!" ("angry", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "base", "angry", "mid")
    gen "So, why did you come straight to me and not go to your dorm?" ("base", xpos="far_left", ypos="head")
    cho "And pass through my common room?" ("soft", "base", "angry", "mid")
    cho "No, thank you... Your office was the closest thing to their stupid shop." ("clench", "base", "angry", "R")

    if not item_store_intro_done:
        gen "Shop? What shop?" ("base", xpos="far_left", ypos="head")
        cho "Are you kidding me? Surely, you must know about them and their shady businesses." ("soft", "base", "angry", "mid")
        gen "I have no clue what you're talking about." ("base", xpos="far_left", ypos="head")

    cho "..." ("disgust", "base", "base", "down")
    cho "Don't you have any spare robes or anything?" ("open", "base", "worried", "mid")
    gen "I suppose I--" ("base", xpos="far_left", ypos="head")

    menu:
        gen "(Actually, I might not get another opportunity like this...)" ("base", xpos="far_left", ypos="head")
        "-Let her deal with it-":
            gen "You'll figure something out." ("base", xpos="far_left", ypos="head")
            cho "What!?" ("open", "wide", "base", "mid")
            cho "You want me to just go out there without any clothes on?" ("clench", "wide", "angry", "mid")
            gen "Of course... Seems like a great exercise." ("base", xpos="far_left", ypos="head")
            cho "Exercise? How is this an exercise to you?" ("angry", "base", "angry", "down")
            gen "An exercise in confidence, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
            cho "You have got to be joking..." ("disgust", "wide", "base", "mid")
            cho "So, you're not going to help me?" ("disgust", "base", "angry", "mid")
            gen "This one's on you [name_cho_genie]." ("base", xpos="far_left", ypos="head")
            cho "*Grrrr*, whatever..." ("angry", "base", "angry", "mid")

            # Cho leaves.
            call cho_walk(action="leave")

            $ states.cho.mood += 20

            gen "She sure is a feisty one..." ("base", xpos="far_left", ypos="head")

        "-Offer to fetch her something-":
            call cc_pr_manipulate_boys_twins_branch

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    $ cho.wear("all")
    $ cho.set_body_hue(0)

    jump end_cho_event

label cc_pr_manipulate_boys_T3_ron:

    $ states.cho.ev.manipulate_boys.t3_e2_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Mission success?" ("base", xpos="far_left", ypos="head")
    gen "Did you manage to sneak up on Rob?" ("base", xpos="far_left", ypos="head")
    cho "Yes! It could not have gone better!" ("crooked_smile", "base", "base", "mid")
    gen "Great, let's hear it." ("base", xpos="far_left", ypos="head")
    cho "I found the perfect opportunity to approach him after practice as Hermione was arguing with Madam Hooch about some rule or another." ("smile", "base", "base", "R")
    cho "So as she was busy, I went up and praised him on his excellent goal keeping." ("smile", "base", "raised", "mid")
    cho "He was quite taken aback by this at first, and I doubt he's ever recie--" ("smile", "narrow", "raised", "R")
    gen "Surely you didn't just compliment him... That won't be enough to annoy Miss Granger!" ("base", xpos="far_left", ypos="head")
    cho "Of course not!" ("clench", "base", "raised", "mid")
    cho "The goal was for him to check me out... Which I soon caught him doing." ("smile", "narrow", "base", "R")
    gen "That boy could do with some lecturing!" ("base", xpos="far_left", ypos="head")
    cho "I know!" ("soft", "base", "angry", "mid")
    gen "Getting caught checking someone out that quickly..." ("base", xpos="far_left", ypos="head")
    cho "Right..." ("open", "narrow", "base", "R")
    cho "Anyhow, it was as if he was trying to stare through my clothing... He was barely paying any attention." ("open", "narrow", "base", "down")
    gen "Been there, done that..." ("base", xpos="far_left", ypos="head")
    cho "Yeah, no wonder Hermione is so annoyed at him all the time..." ("annoyed", "narrow", "base", "L")
    cho "It was at that point Madam Hooch turned and walked away from Hermione." ("open", "base", "base", "R")
    cho "So without any warning, I grabbed and planted Ron's hands on my breasts." ("crooked_smile", "narrow", "base", "mid")
    gen "Nice..." ("base", xpos="far_left", ypos="head")
    cho "He was so taken aback by this, he just froze." ("crooked_smile", "closed", "base", "mid")
    cho "You should've seen Hermione's expression as she turned and noticed us! It was if someone had flipped a switch in her brain." ("smile", "wide", "base", "mid")
    gen "Jealousy no doubt..." ("base", xpos="far_left", ypos="head")
    cho "Yeah right, as I said there's no way anything is going on between those two." ("smile", "narrow", "base", "R")
    gen "I wasn't talking about...{w=0.4} Never mind..." ("base", xpos="far_left", ypos="head")
    gen "Please, continue..." ("base", xpos="far_left", ypos="head")
    cho "Before I could even blink, she had rushed up next to us..." ("crooked_smile", "narrow", "base", "mid")
    cho "And then she smacked Ron right across the face!" ("smile", "wide", "angry", "mid")
    gen "*Hah*!" ("grin", xpos="far_left", ypos="head")
    gen "I mean... How could she hit another student like that?!" ("angry", xpos="far_left", ypos="head")
    cho "You don't have to pretend that you care..." ("angry", "narrow", "raised", "mid")
    gen "I don't." ("base", xpos="far_left", ypos="head")
    gen "What happened next?" ("base", xpos="far_left", ypos="head")
    cho "She dragged him away, yelling her head off the whole time." ("smile", "narrow", "base", "R")
    cho "I wouldn't be surprised if she's still going." ("grin", "narrow", "base", "mid") #smirk
    gen "Excellent work!" ("base", xpos="far_left", ypos="head")
    cho "Thank you." ("smile", "base", "base", "mid") #blushes
    gen "Hopefully we can remind her about this during the game, spark that jealousy once more." ("base", xpos="far_left", ypos="head")
    cho "If it annoys Hermione, then I'm all for it..." ("crooked_smile", "base", "base", "R")
    gen "Anything else to report?" ("base", xpos="far_left", ypos="head")
    cho "No, that's about it." ("soft", "base", "base", "downR")
    gen "Great, then that will be all for today." ("base", xpos="far_left", ypos="head")
    cho "Good night then..." ("base", "base", "base", "mid")
    gen "Good night, Miss Chang." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event

label cc_pr_manipulate_boys_T3_harry:

    $ states.cho.ev.manipulate_boys.t3_e3_complete = True

    # Cho enters.
    call cho_walk(action="enter", xpos="desk", ypos="base")

    cho "" ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Welcome back...{w=0.3} Mission success?" ("base", xpos="far_left", ypos="head")
    cho "Yes!" ("crooked_smile", "base", "base", "mid")
    cho "I've been stalk--{w=0.4} *Ehh*...{w=0.2} Following them... And sure enough, I managed to find the perfect opportunity!" ("soft", "base", "base", "R")
    cho "I was flying by the divination tower and noticed that Hermione and her friends were standing by one of the windows." ("open", "base", "base", "mid")
    cho "Luckily ,Ron and Hermione's backs were turned towards me, so it was easy to grab Harry's attention without them noticing me." ("base", "narrow", "base", "R")
    gen "Nice, gave him a bit of a show then, I presume?" ("base", xpos="far_left", ypos="head")
    cho "Of course..." ("crooked_smile", "closed", "base", "R") #smirk
    cho "And I found something out." ("crooked_smile", "base", "raised", "mid")
    cho "That boy has a broom fetish!" ("smile", "wide", "base", "mid")
    gen "A what?" ("base", xpos="far_left", ypos="head")
    cho "A broom fetish!{w} It's when you enjoy watching a girl play with herself using a broom." ("smile", "narrow", "raised", "mid")
    gen "Oh...{w=0.4} Yeah, that makes more sense." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "So, I stuck my tongue out at him and then began grinding my hips against the wood." ("crooked_smile", "narrow", "base", "mid")
    gen "You stuck your tongue out?" ("base", xpos="far_left", ypos="head")
    gen "I thought it was Hermione that you were trying to antagonize?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Not like that!" ("open", "happyCl", "angry", "mid")
    cho @ cheeks blush "I mean in a seductive way!" ("smile", "narrow", "base", "mid")
    gen "Like how?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Like this!" ("open", "wink", "base", "mid")
    cho "...{w=1.0}{nw}" ("open_tongue", "base", "base", "mid")
    cho @ cheeks blush "..." ("open_wide_tongue", "narrow", "raised", "mid") #Cho sticks her tongue out and eyes look seductive."
    gen "Whoa!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*U ikhe*?" ("open_wide_tongue", "wink", "raised", "mid") #Tongue still out
    gen "Very much...{w=0.4} But what about Potter?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Naturally, he completely lost focus on their conversation, so Hermione followed his gaze and finally spotted me through the window." ("crooked_smile", "closed", "base", "R")
    cho "And after staring daggers at me, she yanked the boys away by their robes, almost making them tumble down the stairs." ("crooked_smile", "narrow", "base", "mid")
    gen "Looks like you have her well jealous at this point!" ("base", xpos="far_left", ypos="head") #This is a bit of a British slang
    gen "Hopefully this should be enough to affect her during the finals." ("base", xpos="far_left", ypos="head")
    cho "Let's hope so..." ("smile", "base", "angry", "R")
    cho "If that's all, I'll head off for today." ("base", "base", "raised", "mid")
    gen "Yes, that will be all." ("base", xpos="far_left", ypos="head")
    cho "Good night then." ("smile", "base", "base", "mid")
    gen "Good night, Miss Chang." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    if states.cho.public_level < 12: # Points til 12.
        $ states.cho.public_level += 1

    jump end_cho_event


label cc_pr_manipulate_boys_twins_branch:
    # Genie visits Mafkin store to fetch some outfit for Cho

    if clothing_store_intro_done:
        gen "Madam Mafkin should be able to sort you out." ("base", xpos="far_left", ypos="head")
        cho "Mafkin? Don't you mean Malkin?" ("open", "base", "base", "mid")
        gen "Pretty sure it's Mafkin." ("base", xpos="far_left", ypos="head")
        gen "I'll go and check with her and see if there's anything she can spare for the moment..." ("base", xpos="far_left", ypos="head")
    else:
        gen "Surely this place has some sort of seamstress." ("base", xpos="far_left", ypos="head")
        cho "I guess there's Malkin... or Mafkin, whatever her name is..." ("soft", "base", "base", "downR")
        gen "Don't look at me, I don't remember all the names of every employee here." ("base", xpos="far_left", ypos="head")
        cho "Of course you don't..." ("normal", "base", "base", "R")
        gen "I'll go and check with her, see if there's anything she can spare for the moment..." ("base", xpos="far_left", ypos="head")

    cho @ cheeks blush "Please..." ("normal", "base", "base", "down")
    cho "I just hope this colour will fade before you get back..." ("disgust", "base", "angry", "downR")
    gen "I'll be back before you can say blueberry." ("base", xpos="far_left", ypos="head")
    #TODO Genie walks past Cho to the door and turns to her, she turns as he stops
    gen "But personally, I don't really see why it's such an issue." ("base", xpos="far_left", ypos="head")
    gen "I've been known to turn blue and swell up as well, and you don't see me complaining." ("base", xpos="far_left", ypos="head")

    cho "..." ("disgust", "base", "angry", "mid")

    gen "Give me some time, be right back." ("base", xpos="far_left", ypos="head")

    call blkfade
    stop music fadeout 1
    centered "{size=+7}{color=#cbcbcb}{cps=7}...{/cps}{/color}{/size}{w=1.0}{nw}"
    call room("clothing_store")
    play music "music/clothing_store.ogg" fadein 1 if_changed
    call hide_blkfade

    if not clothing_store_intro_done:
        $ clothing_store_intro_done = True
        nar "You enter to see an old woman sewing together two pieces of long dark fabric."
        nar "The woman is dressed almost entirely in pink and has a warm, approachable air to her."
        gen "Hello." ("base", xpos="far_left", ypos="head")
        maf "Hello, Professor Dumbledore."
        maf "What can I do for you? Would you like a new cloak, or do you require some alterations to an existing item?"
        gen "Neither, thank you, I'm just here to make a few inquiries." ("base", xpos="far_left", ypos="head")
        maf "Of course sir, what can I help you with?"
        gen "Firstly, what types of items do you sell?" ("base", xpos="far_left", ypos="head")
        maf "Well, I'm a tailor. I make uniforms for the staff and students."
        maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
        gen "I see. Do you ever make custom orders?" ("base", xpos="far_left", ypos="head")
        maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
        gen "So you're interested in making unique outfits?" ("base", xpos="far_left", ypos="head")
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colours at the moment."
        maf "What did you have in mind?"
    else:
        gen "Miss Mafkin... or was it Malkin?" ("base", xpos="far_left", ypos="head")
        maf "It's Mafkin, Dumbledore... we have been over this before."
        gen "(I knew she was wrong!)" ("grin", xpos="far_left", ypos="head")
        maf "Anything I can assist you with?"
        maf "I just got this new plaid fabric in, I was thinking of turning it into a kilt."
        maf "It's the perfect garment for letting the old family jewels get some fresh air."
        gen "I'm good, thank you." ("base", xpos="far_left", ypos="head")
        maf "Then what can I do you for?"

    gen "Well... As it happens..." ("base", xpos="far_left", ypos="head")
    gen "I'm in quite a pickle... A student was tricked into eating one of the weasel twins' sweets." ("base", xpos="far_left", ypos="head")
    maf "A sweet?"
    gen "Yes, or a candy... whatever you'd call it." ("base", xpos="far_left", ypos="head")
    gen "The sweet in question made her skin turn blue and swell up like a balloon, ruining her clothes in the process." ("base", xpos="far_left", ypos="head")
    maf "I see... that's an unfortunate situation indeed."
    gen "So I require a Female Ravenclaw school uniform." ("base", xpos="far_left", ypos="head")
    maf "Let's see...{w=0.5} Female Ravenclaw uniform...{w=0.4} Looks like I'm running a bit low on those at the moment, what size is she?"
    gen "She's a C...{w=0.4} or maybe a B actually..." ("base", xpos="far_left", ypos="head")
    maf "She's a... B, sir?"
    gen "No-no, she's a Human. That's her size." ("base", xpos="far_left", ypos="head")
    maf "I require her clothing measurements..."
    gen "Oh, I see..." ("base", xpos="far_left", ypos="head")
    maf "Or the name of this student, If I've had her fitted before, then I should have her measurements stored in my records."
    gen "Cho Chang." ("base", xpos="far_left", ypos="head")
    play sound "sounds/pageflip.ogg"
    maf "Cho Chang..."
    play sound "sounds/pageflip.ogg"
    maf "*Hmm*..."
    maf "Ah yes, here she is..."
    maf "Well, that's unfortunate..."
    gen "You don't have any clothing her size?" ("base", xpos="far_left", ypos="head")
    maf "I do, but none in Ravenclaw colours."
    maf "She might have to go with one of the other house colours for now until I can get these ones fitted for her."
    gen "That sure is unfortunate." ("base", xpos="far_left", ypos="head")

    # Setup
    $ d_flag_01 = False
    $ d_flag_02 = None

    label .choices:

    menu:
        gen "In that case I'll have the..." ("base", xpos="far_left", ypos="head")

        "-Slytherin uniform-":
            $ d_flag_02 = 1

            maf "Are you sure?"
            gen "Absolutely, she'll look great in green!" ("base", xpos="far_left", ypos="head")
            gen "But just so I know... how long will it take to get the Ravenclaw uniform ready?" ("base", xpos="far_left", ypos="head")

        "-Gryffindor uniform-":
            $ d_flag_02 = 2

            maf "Are you sure?"
            gen "Of course!" ("base", xpos="far_left", ypos="head")
            gen "She's best friends with Miss Granger, so I'm sure she wouldn't mind." ("base", xpos="far_left", ypos="head")
            gen "But just so I know... how long will it take to get the Ravenclaw uniform ready?" ("base", xpos="far_left", ypos="head")

        "-Hufflepuff uniform-":
            $ d_flag_02 = 3

            maf "Are you sure?"
            gen "Seems like the safest option, all things considered." ("base", xpos="far_left", ypos="head")
            gen "How long will it take to get the Ravenclaw uniform ready?" ("base", xpos="far_left", ypos="head")

        "-\"perfect\" Outfit-" if d_flag_01:
            $ d_flag_02 = 4

            maf "Are you sure?"
            gen "Of course!" ("base", xpos="far_left", ypos="head")
            gen "It looks as if it was made just for her." ("grin", xpos="far_left", ypos="head")
            maf "Well, you're the judge here."
            gen "One more thing, how long will it take to get the Ravenclaw uniform ready?" ("base", xpos="far_left", ypos="head")

        "-Ask for another option-" if not d_flag_01:
            # Genie finds a smurfette costume
            $ d_flag_01 = True

            gen "I don't think she'd be so keen on wearing another house's colours." ("base", xpos="far_left", ypos="head")
            maf "Well, I don't recommend it, but if that's the case, you can have a look through the pile over there."
            maf "I have a few miscellaneous pieces lying around that she could borrow for the time being."
            maf "There's not a lot to pick from, but you can take anything you need from it."
            gen "Great." ("base", xpos="far_left", ypos="head")
            #TODO have his chibi turn and walk so you just see his back inside the screen and then display the next line - No can do, not implemented
            # Rummage sound.
            gen "*Hmm*... Doesn't seem to be a lot to pick from." ("base", xpos="far_left", ypos="head")
            # Rummage sound.
            gen "Now what could I get that would suit her?" ("base", xpos="far_left", ypos="head")
            # Rummage sound.
            gen "Hold on a second." ("base", xpos="far_left", ypos="head")
            # Rummage sound.
            gen "(Oh, this is just perfect... Although perhaps it's a bit mean...)" ("base", xpos="far_left", ypos="head")
            gen "(Maybe I should just ask for one of the other house's clothing pieces instead...)" ("base", xpos="far_left", ypos="head")
            #TODO genie chibi turns and walks back to normal position - No can do, not implemented

            jump .choices

    maf "I'll have it done and delivered by tomorrow morning."
    gen "Great, that will be all then." ("base", xpos="far_left", ypos="head")
    maf "Until next time..."

    call blkfade

    # Add smurfette outfit to the shop if was not picked during the event
    if not d_flag_01:
        $ cho_outfit_smurfette.price = 100

    call room("main_room")
    stop music fadeout 1
    call gen_chibi("hide")
    call cho_chibi(xpos="desk", ypos="base", flip=True)
    call hide_blkfade
    pause 1.0

    play sound "sounds/door.ogg"
    call gen_chibi("stand", "door", "base", flip=False)
    with d3
    pause 0.3

    gen "I'm back!" ("base", xpos="far_left", ypos="head")
    call gen_walk("mid", "base")
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "Finally..." ("annoyed", "base", "angry", "mid", trans=d3)

    if not states.fireplace_started:
        cho "I've been freezing my butt off, and I couldn't figure out how to light the fire." ("open", "base", "angry", "mid")
        gen "Can't you use some spell for that?" ("base", xpos="far_left", ypos="head")
        cho "Where do you think I keep my wand?" ("annoyed", "base", "angry", "mid")
        gen "Well, most people hide it in their night stand or a drawer or something." ("base", xpos="far_left", ypos="head")
    else:
        cho "If it weren't for the fire in the fireplace, I'd freeze my butt off!" ("open", "base", "angry", "mid")
        gen "Then what are you complaining about?" ("base", xpos="far_left", ypos="head")
        cho "I don't like standing around stark naked..." ("soft", "base", "angry", "mid")
        gen "{size=-2}Sure could've fooled me...{/size}" ("base", xpos="far_left", ypos="head")

    cho "Where's that outfit you were fetching for me?" ("upset", "base", "base", "mid")

    if d_flag_02 == 1:
        # Slytherin

        gen "Got it right here, brings out the colour of your eyes for sure!" ("base", xpos="far_left", ypos="head")

        play sound "sounds/cloth_sound.ogg"
        nar "You hand the Slytherin uniform to Cho."

        cho "Such a charmer..." ("base", "base", "base", "R")
        cho "I was worried that you'd pick out something--" ("open", "base", "base", "down")
        cho "{size=+5}These are Slytherin colours!{/size}" ("open", "wide", "angry", "mid")
        gen "They are?" ("base", xpos="far_left", ypos="head")
        gen "That's unfortunate!" ("base", xpos="far_left", ypos="head")
        cho "Why did you assume it would be a good idea..." ("clench", "base", "angry", "down")
        cho "{size=+5}To get Slytherin colours!{/size}" ("angry", "base", "angry", "mid") #big text yelling
        gen "She didn't have any spare Ravenclaw outfits." ("base", xpos="far_left", ypos="head")
        cho "But why Slytherin..." ("disgust", "base", "angry", "downR")

        menu:
            "{size=-3}\"If you don't like it, you can go without any!\"{/size}":
                cho "What!?" ("open", "wide", "angry", "mid")
                gen "You heard me..." ("base", xpos="far_left", ypos="head")
                gen "I went out of my way to fetch those clothes for you..." ("base", xpos="far_left", ypos="head")
                gen "So you can take your Smurf looking ass and get out of my office." ("base", xpos="far_left", ypos="head")
                cho "Fine!" ("clench", "base", "angry", "mid")
                call cho_walk(action="leave", speed=2.0)
                play sound "sounds/door_down.ogg"
                with hpunch
                gen "..." ("base", xpos="far_left", ypos="head")
                $ states.cho.mood += 10

            "{size=-3}\"It's not my fault, Some idiot picked that option!\"{/size}":
                cho "What?" ("annoyed", "wide", "angry", "mid")
                gen "It was decided by some unknown external force." ("base", xpos="far_left", ypos="head")
                cho "That doesn't make any sense!" ("open", "base", "angry", "mid")
                gen "I know!" ("base", xpos="far_left", ypos="head")
                cho "..." ("upset", "base", "angry", "mid")

                $ cho.set_body_hue(0)

                cho "I thought you would know better than to pick a Slytherin uniform for me..." ("annoyed", "base", "angry", "downR", trans=d9)
                gen "As I said, not my fault." ("base", xpos="far_left", ypos="head")
                gen "Although, speaking of colour..." ("grin", xpos="far_left", ypos="head")
                gen "You're not blue anymore." ("base", xpos="far_left", ypos="head")
                cho "Thank Merlin for that..." ("clench", "base", "worried", "down")
                cho "Just hand me those clothes..." ("annoyed", "base", "angry", "mid")

                show screen blkfade
                with fade
                $ cho.equip(cho_outfit_slyt)
                play sound "sounds/cloth_sound3.ogg"
                cho "" ("upset", "base", "angry", "down")
                pause .8
                hide screen blkfade
                with fade

                cho @ cheeks blush "..." ("disgust", "base", "base", "down")
                cho @ cheeks blush "This feels wrong..." ("clench", "base", "worried", "downR")
                gen "I knew it!" ("grin", xpos="far_left", ypos="head")
                gen "You look great in green!" ("grin", xpos="far_left", ypos="head")
                cho "*Grrr*... I can't believe you!" ("clench", "base", "angry", "mid")
                call cho_walk(action="leave", speed=2.0)
                play sound "sounds/door_down.ogg"
                with hpunch
                $ states.cho.mood += 5

            "\"Sorry...\"":
                cho "..." ("normal", "wide", "base", "mid")
                cho "(Well, that's a first...)" ("soft", "base", "base", "R") #taken aback
                gen "Sorry for going out of my way to help you!" ("base", xpos="far_left", ypos="head")
                cho "*Sigh*" ("disgust", "base", "base", "down")
                cho "Why did you think it would be a good idea to pick Slytherin colours..." ("annoyed", "base", "angry", "downR") #pout
                gen "As I said, I thought they'd compliment your eyes..." ("base", xpos="far_left", ypos="head")
                cho @ cheeks blush "..." ("annoyed", "base", "angry", "down")
                cho @ cheeks blush "Fine, since you almost apologized..." ("disgust", "base", "angry", "downR")
                cho @ cheeks blush "Hand me those clothes." ("annoyed", "base", "angry", "mid")

                show screen blkfade
                with fade
                $ cho.equip(cho_outfit_slyt)
                play sound "sounds/cloth_sound3.ogg"
                cho "" ("upset", "base", "angry", "down")
                pause .8
                hide screen blkfade
                with fade

                gen "See, they don't look that bad!" ("base", xpos="far_left", ypos="head")
                cho @ cheeks blush "This feels wrong..." ("angry", "base", "worried", "downR")
                gen "You look great in any colour!" ("base", xpos="far_left", ypos="head")
                cho @ cheeks blush "That's not why..." ("normal", "base", "angry", "mid")

                $ cho.set_body_hue(0)

                cho "Thanks, I guess." ("disgust", "base", "base", "down", trans=d9)
                gen "Speaking of colour..." ("base", xpos="far_left", ypos="head")
                gen "You're not blue anymore." ("base", xpos="far_left", ypos="head")
                cho "Finally..." ("mad", "base", "base", "mid")
                cho "Hopefully everyone's gone to bed by now, and I can sneak my way past without anyone noticing." ("upset", "base", "base", "R")
                cho "So, what do I do about my normal uniform?" ("open", "base", "base", "down")
                gen "I've sorted it... Mafkin will have a new set delivered to your room in the morning." ("base", xpos="far_left", ypos="head")
                cho @ cheeks blush "Oh..." ("open", "base", "base", "downR")
                cho "Thanks..." ("upset", "base", "base", "downR")
                cho "Good night then." ("normal", "base", "base", "mid")
                call cho_walk(action="leave", speed=1.5)
                $ states.cho.mood += 2

    elif d_flag_02 == 2:
        # Gryffindor

        gen "Got it right here!" ("base", xpos="far_left", ypos="head")
        gen "She didn't have any Ravenclaw uniforms in your size, so I chose the next best thing." ("base", xpos="far_left", ypos="head")

        play sound "sounds/cloth_sound.ogg"
        nar "You hand the Gryffindor uniform to Cho."

        cho "Next best--" ("annoyed", "base", "base", "mid")
        cho "Is that a Gryffindor uniform?" ("open", "wide", "base", "mid") #shocked
        gen "Yes, I knew you'd like it!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "I...{w=0.5} I don't like Gryffindor!" ("annoyed", "base", "angry", "downR")
        gen "What... but I thought Hermione was like your bestie." ("angry", xpos="far_left", ypos="head")
        cho "Bestie?" ("upset", "wide", "base", "mid")
        cho @ cheeks blush "She...{w=0.4} Is...{w=0.4} Not!" ("clench", "wide", "angry", "mid")
        gen "Oh..." ("base", xpos="far_left", ypos="head")

        menu:
            "\"I could go back and fetch the Slytherin one instead...\"":
                cho @ cheeks blush "No!" ("angry", "wide", "base", "mid")
                cho "I mean... It's fine... You've already gone out of your way." ("angry", "wide", "base", "downR")
                gen "You sure? It's not that far--" ("base", xpos="far_left", ypos="head")
                cho "Yes... Just hand me the clothes." ("disgust", "base", "angry", "mid")

                show screen blkfade
                with fade
                $ cho.equip(cho_outfit_gryf)
                play sound "sounds/cloth_sound3.ogg"
                pause .8
                hide screen blkfade
                with fade

                cho "..." ("normal", "base", "base", "downR")
                cho @ cheeks blush "I guess it's not that bad..." ("normal", "base", "base", "down")
                cho @ cheeks blush "What do you think, do I pull off the red as well as...{w=0.6} Do I pull off the red?" ("open", "base", "base", "downR")
                gen "Looks great!" ("base", xpos="far_left", ypos="head")
                gen "They look a bit tight around the chest area, did I end up with a size too small?" ("base", xpos="far_left", ypos="head")
                cho @ cheeks blush "Oh... No, it's fine... I'm just a bit cold still." ("horny", "base", "base", "down") #Embarrassed
                gen "You do look a bit blue..." ("base", xpos="far_left", ypos="head")
                cho "Wait, I'm still..." ("upset", "wide", "angry", "down")

                $ cho.set_body_hue(0)

                cho "...{w=0.5} Thank Merlin..." ("soft", "base", "base", "down", trans=d9)
                cho @ cheeks blush "I'll be on my way then..." ("open", "base", "base", "R")
                call cho_walk(xpos="door", speed=1.5)
                cho @ cheeks blush "..." ("base", "base", "base", "down", flip=True, xpos="far_right", trans=d3)
                cho @ cheeks blush "Good night..." ("open", "base", "base", "mid")
                call cho_walk(action="leave")

            "\"I'm sure none of the Gryffindors will spot you...\"":
                cho "If that's the case, then why wear any clothes at all?" ("angry", "base", "angry", "mid")
                gen "That is an option..." ("base", xpos="far_left", ypos="head")
                cho @ cheeks blush "No!" ("clench", "wide", "base", "mid")
                cho "Give me those..." ("mad", "base", "base", "mid")

                show screen blkfade
                with fade
                $ cho.equip(cho_outfit_gryf)
                play sound "sounds/cloth_sound3.ogg"
                pause .8
                hide screen blkfade
                with fade

                gen "Actually, can I change my mi--" ("base", xpos="far_left", ypos="head")
                cho "No-no, we're good!" ("mad", "base", "base", "R")
                gen "But could you at least--" ("base", xpos="far_left", ypos="head")
                cho "Nope, these will have to do..." ("angry", "base", "base", "L")
                cho "Have a good night!" ("clench", "base", "base", "L")
                call cho_walk(action="leave", speed=1.5)

                call gen_chibi(flip=True)
                gen "Come ba--" ("base", xpos="far_left", ypos="head")
                gen "Damn...{w=0.4} Well at least she isn't angry." ("base", xpos="far_left", ypos="head")

    elif d_flag_02 == 3:
        # Hufflepuff

        gen "Got it right here!" ("base", xpos="far_left", ypos="head")
        gen "She didn't have any Ravenclaw uniforms in your size, so I went with something mellow." ("base", xpos="far_left", ypos="head")

        play sound "sounds/cloth_sound.ogg"
        nar "You hand the Hufflepuff uniform to Cho."

        cho "Mellow?" ("annoyed", "base", "base", "mid")
        cho "Wait, you don't mean..." ("disgust", "base", "base", "down") #Worried
        cho "A Hufflepuff uniform!" ("clench", "wide", "base", "mid") #Shocked
        gen "Sure is, I remembered how you can't get enough of those badgers!" ("base", xpos="far_left", ypos="head")
        cho "I only dated one of them when the Tri-wizard tournament was happening..." ("annoyed", "base", "angry", "mid")
        cho "And as you remembered, I used it to our advantage to win the match against them." ("clench", "base", "base", "mid")
        gen "Sure did!" ("base", xpos="far_left", ypos="head")
        cho "So, don't you think the Hufflepuffs would assume Cedric threw the match on purpose if they suddenly saw me wearing this?" ("angry", "base", "base", "downR")

        menu:
            "\"So what?\"":
                cho "So what?!?" ("open", "wide", "angry", "mid")
                gen "You didn't have any problems using his weaknesses during the game, so why do you care if he gets in trouble with his house?" ("base", xpos="far_left", ypos="head")
                cho "That's different..." ("angry", "base", "angry", "mid")
                gen "How is it different?" ("base", xpos="far_left", ypos="head")
                gen "I'm sure his teammates weren't happy with him losing focus like that... Fraternizing with the enemy..." ("base", xpos="far_left", ypos="head")
                cho "..." ("disgust", "base", "angry", "down")
                gen "They might already think he threw it on purpose." ("base", xpos="far_left", ypos="head")
                cho "Whatever, just give me the clothes." ("open", "base", "angry", "mid")

                show screen blkfade
                with fade
                $ cho.equip(cho_outfit_huff)
                play sound "sounds/cloth_sound3.ogg"
                pause .8
                hide screen blkfade
                with fade

                cho "I can't believe you turned this around on me like that... You're the one that made me do those things to begin with..." ("soft", "base", "angry", "downR")
                gen "Don't hate the player, hate the game." ("base", xpos="far_left", ypos="head")
                cho "..." ("upset", "base", "angry", "R")
                cho "I'm leaving." ("upset", "base", "angry", "mid")
                call cho_walk(action="leave", speed=1.5)
                $ states.cho.mood+= 2

            "\"That's true, maybe you should just head back naked...\"":
                cho "What!?" ("disgust", "wide", "base", "mid")
                gen "You heard me, make like a bee and buzz off!" ("base", xpos="far_left", ypos="head")
                gen "And you better hurry up before those sweets wear off, or you'll find it even harder to explain your current state." ("grin", xpos="far_left", ypos="head")
                cho @ cheeks blush "But... Surely, you can't be serious!" ("open", "wide", "base", "mid")
                gen "I am neither Shirley nor Sirius..." ("base", xpos="far_left", ypos="head")
                cho "*Grrr*... I can't believe you!" ("clench", "base", "angry", "mid")

                call cho_walk(xpos="door", speed=1.5)
                call cho_chibi(flip=True)
                call gen_chibi(flip=True)

                cho "..." ("upset", "base", "angry", "down", flip=True, xpos="far_right", trans=d3)
                gen "Tick-tock..." ("base", xpos="far_left", ypos="head")
                cho "Fine!" ("clench", "base", "angry", "R")

                call cho_walk(action="leave")
                play sound "sounds/door_down.ogg"
                with hpunch

                $ states.cho.mood += 10
                gen "So ungrateful..." ("base", xpos="far_left", ypos="head")

            "\"I'm sure none of the Hufflepuffs will spot you...\"":
                cho "How can you be so sure about--" ("soft", "base", "angry", "downR")
                cho "Actually, you're right...{w=0.3} You're a genius!" ("mad", "wide", "base", "mid")
                gen "I am?" ("angry", xpos="far_left", ypos="head")
                cho "Of course!" ("crooked_smile", "base", "base", "mid")
                cho "You know this castle inside out, it's very unlikely any Hufflepuff student would be anywhere near the route to the Ravenclaw dorm." ("smile", "base", "base", "R")
                gen "Oh yes... That's it!" ("grin", xpos="far_left", ypos="head")
                gen "You know me, always got an ace up my sleeve!" ("base", xpos="far_left", ypos="head")

                $ cho.set_body_hue(0)

                cho "Thank you [name_genie_cho]..." ("base", "base", "base", "mid", trans=d9)
                gen "Anything not to have my students \"feel blue\"." ("grin", xpos="far_left", ypos="head")
                gen "Speaking of... Your skin is back to normal." ("grin", xpos="far_left", ypos="head")
                cho @ cheeks blush "Very funny..." ("base", "base", "base", "down") #smile
                cho @ cheeks blush "Let's try this on then..." ("open", "base", "base", "mid")

                show screen blkfade
                with fade
                $ cho.equip(cho_outfit_huff)
                play sound "sounds/cloth_sound3.ogg"
                pause .8
                hide screen blkfade
                with fade

                cho "So, how do I look?" ("soft", "base", "base", "down")
                gen "Looking good!" ("base", xpos="far_left", ypos="head")
                cho "I better be off then..." ("smile", "base", "base", "mid")
                cho "Good night." ("base", "base", "base", "mid")
                gen "Good night, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
                call cho_walk(action="leave", speed=1.5)

    elif d_flag_02 == 4:
        # Smurfette

        gen "Got it right here." ("base", xpos="far_left", ypos="head")

        play sound "sounds/cloth_sound.ogg"
        nar "You hand the clothes to Cho."

        cho "Thank you, I knew I could count on--" ("base", "base", "base", "mid")
        cho "What is this?" ("open", "wide", "base", "down")
        gen "I know right!" ("grin", xpos="far_left", ypos="head")
        gen "I couldn't believe it when I found it. It's the perfect outfit for you!" ("grin", xpos="far_left", ypos="head")
        cho "You... are you serious? You actually expect me to wear this?" ("disgust", "wide", "base", "mid")
        gen "Wait, don't tell me you don't like it?" ("base", xpos="far_left", ypos="head")
        cho "..." ("disgust", "base", "angry", "down")
        cho "Why couldn't you pick up a normal school uniform like I asked you to?" ("clench", "base", "worried", "down")
        gen "Just put it on already." ("base", xpos="far_left", ypos="head")
        cho "..." ("annoyed", "base", "angry", "down")
        gen "Or you could just head back naked!" ("base", xpos="far_left", ypos="head")
        cho "Fine!" ("clench", "base", "angry", "mid")

        show screen blkfade
        with fade
        $ cho.equip(cho_outfit_smurfette)
        $ cho.equip(cho_hair_base) # Override hair
        play sound "sounds/cloth_sound3.ogg"
        cho @ cheeks blush "" ("upset", "base", "angry", "down")
        pause .8
        hide screen blkfade
        with fade

        gen "Smurfabunga!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("upset", "base", "angry", "mid") #Looking livid #red cheeks
        gen "I think some colour has started to return to your cheeks!" ("base", xpos="far_left", ypos="head")
        gen "I also got you this wig." ("base", xpos="far_left", ypos="head")
        cho "I am not wearing the wig!" ("clench", "wide", "angry", "mid")
        cho "I can't believe you!" ("angry", "base", "angry", "down")

        call cho_walk(action="leave", speed=1.5)
        play sound "sounds/door_down.ogg"
        with hpunch

        gen "I'll just keep the wig for later then..." ("base", xpos="far_left", ypos="head")
        $ states.cho.mood += 10
        call unlock_clothing("Congratulations! You have unlocked a new outfit!", cho_outfit_smurfette)

    $ cho.equip(cho_outfit_last)
    $ cho.set_body_hue(0)

    call gen_chibi("sit_behind_desk")
    with fade

    return
