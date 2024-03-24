

### Tonks Teaching ###

# Detention with Tonks
# (Tonks gives students detention or lets them stay after class)
# (Gets to see the boy's dicks, the girl's panties, punishs them...)
# (Gives hours points to each of the students)

#TODO Add Tonks chibi to all her public request nightly reports

label nt_pr_teach_start:
    ton "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    if states.ton.tier == 1:

        if not _events_completed_any:
            ton "So, what's the plan?" ("open", "base", "base", "mid")
            gen "The plan?" ("base", xpos="far_left", ypos="head")
            ton "You know, how does this go down?" ("soft", "base", "base", "mid")
            ton "I'm hardly a regular when it comes to this stuff." ("open", "base", "base", "R")
            gen "It would be best if we start small, don't you think?" ("base", xpos="far_left", ypos="head")
            gen "You should build up a bit of a reputation for yourself, before we start trying anything crazy." ("base", xpos="far_left", ypos="head")
            ton "A reputation?" ("normal", "base", "raised", "mid")
            ton "Think I'll get a nickname?{w} Maybe they'll call me touchy tonks?" ("soft", "narrow", "shocked", "mid")
            gen "Maybe..." ("base", xpos="far_left", ypos="head")
            ton "What did you do with Hermione on her first favour?" ("open", "narrow", "shocked", "down")
            gen "*Ugh*... I think I got her to make \"a silly face\", or something..." ("base", xpos="far_left", ypos="head")
            ton "You paid her for that? I expected something a little more...{w=0.4} Perverse." ("crooked_smile", "base", "base", "R")
            if states.her.status.show_panties:
                gen "In that case, the first \"real\" favour I bought was getting her to lift her skirt for me." ("base", xpos="far_left", ypos="head")
                ton "That's more like it!" ("horny", "base", "base", "mid")
                ton "But, even though we're in Scotland, none of the boys are wearing skirts..." ("open", "base", "base", "L")
            elif states.her.status.show_tits:
                gen "In that case, the first \"real\" favour I bought was getting her to show me her bra." ("base", xpos="far_left", ypos="head")
                ton "That's more like it!" ("horny", "base", "base", "mid")
                ton "Although it's not a big deal for boys to show you their chests..." ("open", "base", "base", "L")
            else:
                gen "Yes, Granger is greedy when it comes to points..." ("base", xpos="far_left", ypos="head")
                ton "I'm not interested in just chatting with my Students! I get to do that all day..." ("annoyed", "base", "raised", "downR")
            gen "Just get them to show you their dicks then." ("base", xpos="far_left", ypos="head")
            ton "Oh, wow! Are you serious?" ("crooked_smile", "wide", "shocked", "stare")
            gen "I don't see why not." ("base", xpos="far_left", ypos="head")
            gen "It isn't such a big deal for a boy to show a girl his wiener..." ("base", xpos="far_left", ypos="head")
            ton @ cheeks blush "Seeing their dicks... That does sound good..." ("soft", "happyCl", "base", "mid")
            ton "Can I touch them?" ("horny", "narrow", "raised", "mid")
            gen "Let's stick with looking for now..." ("base", xpos="far_left", ypos="head")
            ton "Fine... So how many am I allowed to look at?" ("annoyed", "base", "base", "down")
            gen "As many as you like..." ("base", xpos="far_left", ypos="head")
            ton "And how many points am I allowed to give out?" ("soft", "base", "base", "L")
            gen "Look, I'm not really convinced these points are real..." ("base", xpos="far_left", ypos="head")
            gen "I just say \"Ten points to Gryffindor!\" And these girls do whatever I want for some reason..." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 10
            gen "So as far as I'm concerned, hand out as many as you want." ("base", xpos="far_left", ypos="head")
            ton "All right... Well, I better get to class." ("base", "base", "base", "R")
            ton @ hair neutral "I've got some boys to \"teach\"..." ("horny", "narrow", "raised", "mid")
            gen "Don't forget to come back here after classes to fill me in." ("base", xpos="far_left", ypos="head")
            ton "Will do..." ("base", "happyCl", "base", "mid")

        else: # Repeat
            gen "Ready to help the boys earn some points?" ("base", xpos="far_left", ypos="head")
            ton "And reward them for showing me their dicks?" ("horny", "base", "base", "mid")
            gen "Yes. Return to me after class..." ("base", xpos="far_left", ypos="head")
            ton "*Mhmm*... Don't worry if I'm a little late though..." ("horny", "narrow", "base", "R")

    elif states.ton.tier >= 2:

        if not _events_completed_any: # Tell her to be even lewder for the next level of favors.
            gen "Would you like to give some boys detention again?" ("base", xpos="far_left", ypos="head")
            ton "And what would you suggest I do with them?" ("horny", "narrow", "base", "mid")
            ton "Make them show me their dicks?" ("horny", "narrow", "base", "R")
            ton "Or can we move on to something a little more... progressive?" ("base", "narrow", "base", "mid")
            gen "If that's what you want..." ("base", xpos="far_left", ypos="head")
            ton "*Hmm*...{w=0.4} Yes...{w=0.3} I wouldn't mind seeing the {b}hard cocks{/b} of some of my favourites." ("horny", "narrow", "base", "R")
            ton "Might even have them jerk off for me... I would love to see that!" ("horny", "base", "base", "ahegao")
            gen "And make sure they remember it." ("base", xpos="far_left", ypos="head")
            ton "Yes, [name_genie_tonks]. Don't wait for me..." ("base", "base", "base", "mid")

        else: # Repeat
            gen "Ready to give some boys detention again?" ("base", xpos="far_left", ypos="head")
            ton "Yes. I'm very much in the mood for some {b}hard cocks{/b}!" ("horny", "narrow", "base", "mid")
            gen "Go on then... Teach them a lesson..." ("grin", xpos="far_left", ypos="head")
            ton "I shall see you later, [name_genie_tonks]..." ("base", "base", "base", "mid")

    # Tonks leaves

    call ton_walk(action="leave")
    jump end_tonks_event

### Tier 1 ###

label nt_pr_teach_T1_E1: #Tier 1 - Event 1 - Slytherin boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hello, [name_genie_tonks]." ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    ton "I'm back with my report..." ("horny", "narrow", "base", "mid")

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass

            "\"Make it quick!\"":
                ton "I had some fun with that Slytherin boy again..." ("horny", "base", "angry", "mid")
                ton "Gave him a couple of points for his house." ("open", "base", "base", "R")
                gen "Well done, [name_tonks_genie]... We'll talk next time." ("base", xpos="far_left", ypos="head")
                ton "Yes, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")
                $ slytherin += 20

                if states.ton.public_level < 4: # Points til 4.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")

                jump end_tonks_event

    gen "How were your... \"extra curricular activities\" today?" ("base", xpos="far_left", ypos="head")
    ton "It's such a rush!" ("grin", "happyCl", "base", "mid")
    ton "I can't believe how naughty I feel!" ("soft", "base", "base", "ahegao")
    gen "So I take it you managed to sneak a peek?" ("base", xpos="far_left", ypos="head")
    ton "Sort of... I didn't really see it." ("mad", "base", "base", "R")
    ton "But it was still incredible..." ("base", "happyCl", "base", "mid")
    ton "*Ugh*... that look on his face..." ("mad", "base", "base", "ahegao")
    gen "What did you see then?" ("base", xpos="far_left", ypos="head")
    ton "Well, this sweet little Slytherin student had been staring at my breasts all lesson..." ("base", "base", "base", "down")
    ton "So, naturally, I get him to stay behind after class." ("open", "closed", "base", "mid")
    ton "I couldn't tell if he was angry about it, or just scared..." ("soft", "base", "base", "R")
    ton "But, as his teacher, I insisted that he should write out some lines to correct his behaviour..." ("open", "closed", "base", "mid")
    gen "Do I need to ask what he had to write?" ("base", xpos="far_left", ypos="head")
    ton "\"I shall not stare at my teacher's big, beautiful breasts\"..." ("soft", "base", "base", "ahegao")
    gen "Was the \"big\" and \"beautiful\" part really necessary?" ("base", xpos="far_left", ypos="head")
    ton "Oh, that's not the best bit..." ("horny", "wide", "base", "mid")
    ton "I went on to lecture him just how \"naughty\" and \"wrong\" it is for a student to peek at his teacher's tits......" ("soft", "wink", "annoyed", "mid")
    ton "Oh, and I made him pull down his trousers while he wrote his lines!" ("silly", "narrow", "base", "mid")
    gen "So you did see it!" ("base", xpos="far_left", ypos="head")
    ton "He still had his underwear on..." ("open", "base", "base", "R")
    ton "If I had pushed him any further... he probably would've snapped!" ("soft", "base", "base", "downR")
    ton "Besides, I could still see how {b}hard{/b} he was..." ("base", "closed", "annoyed", "mid")
    ton "It was crazy..." ("silly", "base", "base", "stare")
    ton "I started to really tease him at the end... while he wrote out the last of his lines..." ("grin", "narrow", "shocked", "mid")
    gen "That poor boy..." ("base", xpos="far_left", ypos="head")
    ton "Don't worry, I just whispered in his ear a little..." ("horny", "narrow", "base", "R")
    ton "Told him what a naughty boy he'd been..." ("horny", "base", "shocked", "mid")
    ton "While my boobs dug into him... and my nipples poked into his back..." ("soft", "narrow", "base", "stare")
    ton "His underwear was practically {b}soaked{/b} in pre-cum." ("horny", "narrow", "shocked", "stare")
    gen "And do you think he'll spread the word about you?" ("base", xpos="far_left", ypos="head")
    ton "I sure hope so..." ("base", "base", "base", "down")
    ton "He earned twenty whole points from me today!" ("base", "happyCl", "base", "down")
    ton "Certainly he won't be able to keep his eyes off me anymore..." ("soft", "narrow", "shocked", "mid")
    gen "Very good." ("base", xpos="far_left", ypos="head")
    gen "And try to reward those \"evil Slytherins\" with at least double the amount of points." ("base", xpos="far_left", ypos="head")
    ton "If you say so, [name_genie_tonks]..." ("soft", "narrow", "base", "R")
    ton "It's so... iniquitous... what we are doing.{w} I fucking love it!" ("base", "base", "shocked", "stare")
    gen "That'll be all now..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, [name_genie_tonks]." ("horny", "wink", "base", "mid")
    ton "Sweet dreams." ("grin", "narrow", "base", "mid")

    # Tonks leaves

    $ slytherin += 20

    if states.ton.public_level < 4: # Points til 4.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event

label nt_pr_teach_T1_E2: # Tier 1 - Event 2 - Racenclaw boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                ton "I was fooling around with my favourite Ravenclaw boy again..." ("horny", "base", "angry", "mid")
                ton "And he earned a bunch of points from me." ("base", "happyCl", "base", "mid")
                gen "Well done, [name_tonks_genie]... We'll talk next time." ("base", xpos="far_left", ypos="head")
                ton "Yes, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")

                $ ravenclaw += 10 

                if states.ton.public_level < 4: # Points til 4.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How were your classes today?" ("base", xpos="far_left", ypos="head")
    ton "*Mmmm*... Long and hard..." ("soft", "base", "base", "stare")
    ton "Just how I like them..." ("grin", "base", "shocked", "mid")
    gen "I take it you were able to steal a few glances?" ("base", xpos="far_left", ypos="head")
    ton "It was even better than I thought it'd be!" ("grin", "closed", "base", "mid")
    ton "Who knew they'd be so nervous!" ("base", "wide", "base", "mid")
    gen "What happened?" ("base", xpos="far_left", ypos="head")
    ton "Well, I figured I'd have to be alone with a student, to convince them to whip it out for me..." ("base", "base", "base", "R")
    ton "So I gave the cutest little thing I could find detention..." ("grin", "base", "shocked", "mid")
    ton "Poor boy... I'm not sure he'd ever even been in trouble before." ("grin", "base", "raised", "R")
    ton "So, when the bell rang, he immediately began babbling about how sorry he was for speaking in class, and that he'd never do it again..." ("base", "closed", "shocked", "mid")
    ton "*Ugh*... I had to hold myself back from jumping on him right then and there..." ("horny", "closed", "angry", "stare")
    ton "Anyway, I eventually managed to calm him down and tell him it'll be okay." ("soft", "base", "base", "stare")
    ton "I even let him know that, if he was a good boy, he could earn some points for his house." ("base", "narrow", "base", "mid")
    gen "Did he like the sound of that?" ("base", xpos="far_left", ypos="head")
    ton "You should have seen his eyes light up! Like a kid on Christmas!" ("grin", "base", "base", "R")
    gen "You fooled around with a kid?" ("base", xpos="far_left", ypos="head")
    ton "What? No of course not.{w} Every student is of age here..." ("open", "shocked", "angry", "mid")
    ton "And he didn't look like a kid at all down there..." ("grin", "base", "base", "stare")
    ton "(He was so fucking hung!)" ("horny", "base", "shocked", "ahegao")
    ton "It was child's play... Getting what I wanted from him." ("soft", "base", "angry", "R")
    gen "..................." ("base", xpos="far_left", ypos="head")
    ton "*Mmmm*, I even had him play with himself for a little bit..." ("horny", "base", "base", "stare")
    ton "Fuck, he looked tasty..." ("open_wide_tongue", "narrow", "base", "ahegao")
    gen "*Ahem*... So did you award him his points or just tease him?" ("base", xpos="far_left", ypos="head")
    ton "Don't worry, I made sure Ravenclaw was paid handsomely." ("base", "happyCl", "base", "mid")
    gen "And did he look like the kind to talk?" ("base", xpos="far_left", ypos="head")
    ton "Probably not..." ("upset", "base", "base", "R")
    gen "Well, try and get a talker next time..." ("base", xpos="far_left", ypos="head")
    gen "We're trying to build your reputation, remember?" ("base", xpos="far_left", ypos="head")
    ton "I'll try..." ("annoyed", "happyCl", "base", "mid")
    ton "(Although, I'll have to play with this one a few more times...)" ("horny", "narrow", "base", "stare")
    gen "That will be all for now, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
    ton "Thanks, [name_genie_tonks]." ("base", "base", "base", "mid")

    # Tonks leaves

    $ ravenclaw += 10

    if states.ton.public_level < 4: # Points til 4.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event

label nt_pr_teach_T1_E3: # Tier 1 - Event 3 - Two Gryffindor boys. Guess who...
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                ton "I had some fun with those two Gryffindor boys again..." ("horny", "base", "base", "R")
                ton "Of course I didn't give them any points..." ("open", "closed", "base", "mid")
                ton "I wouldn't want Gryffindor to have an unfair advantage." ("horny", "base", "angry", "mid")
                ton "They practically begged me if they could do it for free anyway..." ("open", "base", "base", "R")
                gen "Well done, [name_tonks_genie]... Until next time." ("base", xpos="far_left", ypos="head")
                ton "Have a good night, [name_genie_tonks]." ("base", "happyCl", "base", "mid")

                if states.ton.public_level < 4: # Points til 4.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How'd it go?" ("base", xpos="far_left", ypos="head")
    ton "Great! I even managed to convince two boys to show me their dicks..." ("grin", "base", "base", "mid")
    ton "At the same time!" ("horny", "wink", "base", "mid")
    gen "Two at once? Congratulations!" ("grin", xpos="far_left", ypos="head")
    ton "Yep... To be honest, they probably would have done it for free." ("crooked_smile", "happyCl", "base", "mid")
    ton "Not that they turned down the offer of points, though..." ("base", "base", "base", "mid")
    gen "Care to elaborate?" ("base", xpos="far_left", ypos="head")
    ton "Alright then... you old perv..." ("base", "base", "shocked", "R")
    ton "Normally I'd just have the cutest thing that takes my eye stay behind after class..." ("open", "base", "base", "R")
    ton "For a little one-on-one time..." ("horny", "base", "base", "stare")
    ton "But I actually had to punish these two idiots for real." ("upset", "closed", "annoyed", "mid")
    gen "What did they do?" ("base", xpos="far_left", ypos="head")
    ton "*Ugh*... They just wouldn't shut up during the whole lesson!" ("upset", "base", "base", "mid")
    ton "And then they tried to lift a girl's skirt with \"wingardium leviosa\"..." ("mad", "base", "base", "R")
    gen "A classic." ("grin", xpos="far_left", ypos="head")
    ton "They reminded me of my younger self..." ("horny", "narrow", "base", "R")
    ton "Which probably meant that they were going too far..." ("upset", "base", "base", "mid")
    ton "So... I kept them after class... Gave them the whole lecture about \"responsibility\" and \"respect\"..." ("open", "closed", "base", "mid")
    gen "................" ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "Then I told them that I'd pay them both ten points, to show me their cocks... {heart}" ("grin", "closed", "base", "mid")
    gen "Just like that?" ("base", xpos="far_left", ypos="head")
    ton "Well, there's a lot more subtlety to it in practice..." ("soft", "base", "base", "stare")
    ton "Not that I think I needed subtlety, given how horny they were..." ("crooked_smile", "base", "shocked", "mid")
    ton "I think those poor buggers actually thought I was going to jerk them both off..." ("horny", "narrow", "base", "stare")
    ton "Still, I think they had a fun time." ("soft", "wink", "base", "mid")
    gen "Any chance they'll tell their friends about it?" ("base", xpos="far_left", ypos="head")
    ton "Oh yes! The Gryffindor common room is probably a buzz already!" ("grin", "closed", "shocked", "mid")
    ton "It wouldn't surprise me if I start getting asked to give more boys detention..." ("horny", "base", "shocked", "mid")
    gen "Fooling around with Gryffindors and rewarding them isn't too helpful for our situation..." ("base", xpos="far_left", ypos="head")
    gen "But great work nonetheless..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, [name_genie_tonks]. That means a lot coming from you." ("base", "happyCl", "base", "mid")
    gen "Even if it is encouragement for seducing your students?" ("base", xpos="far_left", ypos="head")
    ton "Even then." ("base", "narrow", "base", "mid")
    ton "Well, I better get back to work, these halls aren't safe unless there's a teacher on patrol." ("horny", "base", "base", "R")
    gen "(I'm not sure they're safe with her on patrol...)" ("base", xpos="far_left", ypos="head")

    # Tonks leaves

    $ gryffindor += 20

    if states.ton.public_level < 4: # Points til 4.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event

label nt_pr_teach_T1_E4: # Tier 1 - Event 4 - Slytherin girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                ton "I confronted that little Slytherin girl again..." ("horny", "base", "base", "mid")
                ton "Although, I kept myself in check with her... didn't want to scare her away again..." ("open", "base", "base", "R")
                ton "But she was very happy about the points." ("base", "base", "angry", "mid")
                gen "Well done, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "Yes, [name_genie_tonks]. Good night." ("silly", "happyCl", "base", "mid")
                
                $ slytherin += 20

                if states.ton.public_level < 4: # Points til 4.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "Did you manage to sneak a peek today?" ("base", xpos="far_left", ypos="head")
    ton "*Umm*... I'm afraid not..." ("open", "narrow", "base", "R")
    gen "Oh..." ("base", xpos="far_left", ypos="head")
    ton "But I do have a story for you!" ("base", "happyCl", "base", "mid")
    gen "Why didn't you just start with that? You had me worried for a moment!" ("base", xpos="far_left", ypos="head")
    ton "Are you that desperate to hear about me \"fooling around\" with my students?" ("horny", "narrow", "annoyed", "mid")
    gen "I'm desperate to hear {b}anything{/b}..." ("base", xpos="far_left", ypos="head")
    gen "This office isn't exactly riveting to listen to..." ("base", xpos="far_left", ypos="head")
    ton "In that case, I'll try and add some flair to it." ("base", "closed", "base", "mid")
    ton "Once upon a time--" ("open", "wide", "base", "R")
    gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
    ton "Too much?" ("crooked_smile", "happyCl", "base", "mid")
    gen "Just a tad." ("base", xpos="far_left", ypos="head")
    ton "So, I know my job is to try and balance out the favour trading a little..." ("soft", "narrow", "base", "R")
    ton "But I just couldn't help myself today..." ("normal", "base", "worried", "R")
    gen "Help yourself? You mean..." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "*Ugh*... I don't normally mess around with girls..." ("open", "base", "base", "down")
    ton "(Not since I left here anyway...)" ("mad", "base", "raised", "R")
    ton "But today there was {b}the tastiest morsel{/b} I have ever seen in my class!" ("horny", "wide", "base", "stare")
    gen "...................." ("base", xpos="far_left", ypos="head")
    ton "Now, I know when I'm being checked out, I can feel anyone's eyes on me..." ("open", "closed", "shocked", "mid")
    gen "...................." ("base", xpos="far_left", ypos="head")
    nar "You nod, unconsciously... Gazing directly at her tits..."
    ton "And most of the time I don't mind... I might even encourage it from time to time..." ("base", "narrow", "shocked", "mid")
    with hpunch
    pause.8
    nar "Tonks gives her boobs a subtle little shake."
    gen ".................." ("grin", xpos="far_left", ypos="head")
    ton "So, when I felt a pair of cute little eyes struggling their hardest not to stare at me..." ("horny", "base", "annoyed", "down")
    ton "I just {b}had{/b} to play with her!" ("horny", "base", "base", "ahegao")
    gen "*Mmmm*... what happened?" ("base", xpos="far_left", ypos="head")
    ton "Nothing much... I'm pretty sure she would have freaked if I tried anything..." ("soft", "base", "base", "stare")
    ton "So I just asked her to stay after class for a little... \"chat\"." ("base", "base", "shocked", "mid")
    gen "What did that chat involve?" ("base", xpos="far_left", ypos="head")
    ton "Well, what do you think?" ("horny", "base", "shocked", "mid")
    ton "I just sat directly in front of her desk..." ("open", "base", "base", "mid")
    ton "Asked her if she was doing well in class..." ("normal", "base", "base", "R")
    ton "If anything was making her feel... distracted..." ("base", "closed", "annoyed", "mid")
    ton "All the while I was playing with the buttons on my shirt..." ("soft", "base", "shocked", "down")
    ton "*Ugh*... I've never seen someone so flustered..." ("horny", "base", "base", "stare")
    ton "Eventually, it got too much for her, so she just yelled that I was wasting her time and ran off in typical Slytherin fashion." ("open", "closed", "base", "mid")
    gen "Do you really think she was looking at you?" ("base", xpos="far_left", ypos="head")
    ton "After that? There's no doubt... She's hooked." ("base", "narrow", "annoyed", "mid")
    ton "Now I've just got to reel her in." ("grin", "base", "base", "R")
    ton "If that's all right with you, sir!" ("soft", "base", "base", "mid")
    gen "You're asking for my permission?" ("base", xpos="far_left", ypos="head")
    ton "Well, I was only supposed to buy favours from the boys..." ("open", "closed", "base", "mid")
    gen "Eat your heart out!" ("grin", xpos="far_left", ypos="head")
    gen "Just make sure you keep me in the loop..." ("base", xpos="far_left", ypos="head")
    ton "Thanks, [name_genie_tonks]." ("base", "base", "base", "mid")
    gen "Did she receive any points for it?" ("base", xpos="far_left", ypos="head")
    ton "Well, not this time..." ("open", "base", "shocked", "R")
    gen "I think you should give her some anyway." ("base", xpos="far_left", ypos="head")
    gen "For being a tease!" ("grin", xpos="far_left", ypos="head")
    ton "Very well..." ("grin", "base", "base", "mid")
    ton "Twenty points for Slytherin!" ("open", "closed", "base", "mid")
    ton "Now, if you don't mind... It's getting a bit late..." ("open", "base", "base", "R")
    gen "Yes. You may leave..." ("base", xpos="far_left", ypos="head")
    ton "Good night, [name_genie_tonks]." ("base", "happyCl", "base", "mid")
    gen "Good night, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")

    # Tonks leaves

    $ slytherin += 20

    if states.ton.public_level < 4: # Points til 4.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event

### Tier 2 ###

label nt_pr_teach_T2_E1: # Tier 2 - Event 1 - Hufflepuff girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Guess what happened, [name_genie_tonks]!" ("base", "happyCl", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"................\"":
                pass
            "\"You made that Hufflepuff girl squirt again?\"":
                ton "Yes! Right on point! I'm impressed..." ("open", "base", "raised", "mid")
                ton "I just got done cleaning my desk..." ("horny", "base", "base", "down")
                ton "And I didn't use my wand to clean it..." ("horny", "base", "angry", "mid")
                gen "Very good, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "Thank you, [name_genie_tonks]. Until next time..." ("base", "base", "base", "mid")
                
                $ hufflepuff += 40

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "*Umm*... You found the golden ticket?" ("base", xpos="far_left", ypos="head")
    ton "Better! I had a student come to me to sell a favour!" ("grin", "base", "base", "mid")
    gen "And you haven't bought a favour from them before?" ("base", xpos="far_left", ypos="head")
    ton "Not one! They're not even in any of my classes!" ("grin", "base", "base", "R")
    gen "Very good! Word must be getting around that you're... \"purchasing\"." ("base", xpos="far_left", ypos="head")
    gen "So what house is he in?" ("base", xpos="far_left", ypos="head")
    ton "Oh... *Umm*... it wasn't a he..." ("base", "base", "base", "down")
    ton "I hope that's fine... I know I'm supposed to be balancing out the favours for the boys..." ("mad", "base", "shocked", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "(I'd forgotten about Miss Granger's dumb \"M.R.M.\" thing...)" ("base", xpos="far_left", ypos="head")
    gen "(Does she even still run that?)" ("base", xpos="far_left", ypos="head")
    gen "I wouldn't worry about that too much... As long as you're also buying from the boys, I don't think it should matter." ("base", xpos="far_left", ypos="head")
    ton "Good... Because there was no way I could turn down this cute little Hufflepuff..." ("grin", "closed", "base", "mid")
    ton "Poor thing must have spent hours building up the courage..." ("base", "wink", "base", "mid")
    gen "So what did you buy from her?" ("base", xpos="far_left", ypos="head")
    ton "Well... I asked her what sort of favour she wanted to sell me..." ("soft", "narrow", "base", "R")
    ton "She was so flustered... And probably didn't plan this far ahead at all..." ("grin", "happyCl", "base", "mid")
    ton "She started babbling on and on, so I calmed her down by letting her know what favour I wanted..." ("soft", "narrow", "base", "L")
    gen "Was it something naughty?" ("grin", xpos="far_left", ypos="head")
    ton "Naturally..." ("horny", "closed", "base", "mid")
    ton "She just sort of stood there after I told her, stunned for a little bit..." ("soft", "closed", "base", "mid")
    ton "I rushed to the door and made sure it was locked." ("soft", "base", "base", "R")
    ton "After that, I sat down in the front row of the class, and told her to sit on my desk..." ("grin", "base", "shocked", "mid")
    gen "*Mmm*, now that's a front row seat to die for." ("base", xpos="far_left", ypos="head")
    ton "All that was missing was a bucket of popcorn..." ("horny", "wide", "annoyed", "mid")
    ton "Eventually, she was able to muster up enough courage to pull up her skirt..." ("base", "base", "angry", "mid")
    ton "Poor thing only thought to ask how many points she'd be paid after she lifted her skirt though." ("silly", "happyCl", "base", "mid")
    ton "I told her five for showing me her panties..." ("soft", "base", "base", "R")
    gen "Only five?" ("base", xpos="far_left", ypos="head")
    ton "She said the same. I explained that showing her plain white panties only gets five points." ("base", "closed", "annoyed", "mid")
    ton "If she were to take those panties off though... Then that might get Hufflepuff an extra twenty..." ("horny", "base", "angry", "mid")
    gen "Did she say yes?" ("base", xpos="far_left", ypos="head")
    ton "She didn't say anything... but she pulled them down all the same..." ("soft", "closed", "base", "mid")
    ton "" ("base", "base", "angry", "mid")
    gen "Nice! Getting a student to strip on the first favour is hard work!" ("grin", xpos="far_left", ypos="head")
    ton "Oh, we're not done yet..." ("open", "closed", "base", "mid")
    ton "After soaking in the view for a while, I started to notice she was soaking as well..." ("horny", "base", "angry", "mid")
    ton "So... I offered her forty points to play with herself... for me..." ("open", "closed", "base", "mid")
    gen "*Mmmm*... Go on..." ("base", xpos="far_left", ypos="head")
    ton "*Ugh*... It was amazing!{w} She was so nervous... the expression on her face looked incredible..." ("horny", "base", "base", "ahegao")
    ton "That, and the soft mewling while she did it..." ("horny", "base", "angry", "mid")
    ton "It was that perfect combination of \"slutty need\" and \"statuesque beauty\"..." ("base", "base", "base", "ahegao")
    ton "I wanted to taste her so badly..." ("open_wide_tongue", "wide", "base", "ahegao")
    gen "..................." ("grin", xpos="far_left", ypos="head")
    ton "It was a struggle to hold myself back... I don't think she would've been ready for that just yet..." ("open", "closed", "worried", "mid")
    gen "...................." ("base", xpos="far_left", ypos="head")
    ton "But she was more than ready to squirt all over my table..." ("silly", "happyCl", "base", "mid")
    gen "She did what?!" ("angry", xpos="far_left", ypos="head")
    ton "*Ugh*... I had to spend ten whole minutes scourgifying the desk afterwards..." ("mad", "base", "shocked", "down")
    gen "*Ah*... Very good..." ("base", xpos="far_left", ypos="head")
    ton "" ("base", "base", "base", "mid")
    gen "I think that should be all for now..." ("base", xpos="far_left", ypos="head")
    gen "Much more of this, and I'll need to \"scour-ify\" my own desk as well..." ("angry", xpos="far_left", ypos="head")
    ton "I can help you with that." ("horny", "base", "angry", "mid")
    gen "Maybe some other time..." ("base", xpos="far_left", ypos="head")
    ton "*Mmmm*... okay then, [name_genie_tonks]." ("base", "base", "annoyed", "mid")
    ton "I better be on my way as well now..." ("open", "base", "base", "R")
    ton "(Fuck knows, I could use a bit of \"alone time\" myself...)" ("base", "base", "base", "stare")

    # Tonks leaves

    $ hufflepuff += 40

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_teach_T2_E2: # Tier 2 - Event 2 - Ravenclaw boy
    #TODO Have a few drops of cum on her clothes when she comes in
    $ tonks.set_cum(hair="light")
    $ _cum_known=False

    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hello, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass
            "\"Make it quick!\"":
                ton "Remember that cute boy?" ("open", "base", "base", "mid")
                ton "Every time he shot out some cum for me I gave him five points..." ("horny", "base", "angry", "mid")
                gen "I bet he earned quite a lot today. Well done, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "That he did, [name_genie_tonks]... See you next time..." ("base", "base", "base", "mid")
                
                $ ravenclaw += 20

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How did your day go?" ("base", xpos="far_left", ypos="head")
    ton "The teaching was a little dull..." ("upset", "base", "base", "stare")
    ton "Simple wards, hex-detection, basic stuff..." ("soft", "base", "base", "stare")
    ton "Not that anyone else would think so, with how much they all struggled with it..." ("upset", "base", "annoyed", "R")
    gen "I was more interested in hearing about your... \"extracurricular\" activities..." ("base", xpos="far_left", ypos="head")
    ton "I know, I just wanted to get that off my chest." ("upset", "closed", "base", "mid")
    ton "I'd complain to someone else, but I'm not that fond of the other teachers..." ("annoyed", "base", "base", "down")
    gen "Like who?" ("base", xpos="far_left", ypos="head")
    ton "Well, McGonagall is as stuck-up as ever and Slughorn is a gross weirdo..." ("open", "closed", "shocked", "R")
    ton "Anyway, let's get on with the story, shall we?" ("grin", "wink", "base", "mid")

    menu:
        "-Let her know about the cum-":
            $ _cum_known=True

            gen "You do know that you've got some cum on you?" ("base", xpos="far_left", ypos="head")
            ton "*Hmm*?..." ("base", "base", "base", "down")
            ton "Oh..." ("mad", "base", "shocked", "down")
            ton "That cheeky bugger! I can't believe he actually shot it that far..." ("open", "base", "base", "down")
            gen ".................." ("base", xpos="far_left", ypos="head")
            ton "Best to start from the beginning..." ("soft", "closed", "base", "mid")

        "-Ignore it-":
            pass

    ton "So, I spent a little time with my favourite Ravenclaw student today..." ("soft", "narrow", "base", "down")
    gen "Another detention session after class?" ("base", xpos="far_left", ypos="head")
    ton "I don't need to resort to detention anymore... He's learned what a wink in class means." ("grin", "wink", "base", "mid")
    ton "Plus, I think a few of the other students have worked out what it means as well." ("base", "narrow", "base", "R")
    ton "There were a few whispers today... Hopefully that helps get the word out..." ("soft", "base", "base", "mid")
    gen "I bet." ("base", xpos="far_left", ypos="head")
    ton "So, after class, I locked the door like normal and went over to him..." ("open", "base", "base", "R")
    ton "Let him know that I wanted another favour..." ("open", "closed", "base", "mid")
    ton "He wanted to sell me a kiss today... I almost took him up on it..." ("horny", "base", "base", "stare")
    ton "I think he was a little disappointed when I told him I wanted another look..." ("grin", "base", "shocked", "R")
    ton "So I told him I didn't {b}just{/b} want to look at it..." ("soft", "narrow", "shocked", "mid")
    ton "But watch him play with it..." ("horny", "narrow", "annoyed", "mid")
    gen "Make him an offer he can't refuse..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "His eyes truly lit up after that..." ("base", "happyCl", "base", "mid")
    ton "He just kept on staring at me, while he started stroking it..." ("horny", "narrow", "base", "mid")
    ton "Getting it hard for his teacher..." ("horny", "base", "base", "ahegao")
    ton "*Mmmm*... The way he was staring at my tits... with such hunger..." ("soft", "closed", "shocked", "mid")
    ton "I just {b}had{/b} to get them out for him..." ("silly", "base", "shocked", "mid")
    gen "Nice!" ("grin", xpos="far_left", ypos="head")
    ton @ cheeks blush "They got him even more excited..." ("horny", "base", "base", "ahegao")
    ton @ cheeks blush "He even started to speak after that..." ("base", "closed", "base", "mid")
    gen "What did he say?" ("base", xpos="far_left", ypos="head")
    ton "The usual stuff..." ("soft", "base", "base", "R")
    ton "How pretty I was, how nice my tits looked..." ("crooked_smile", "base", "base", "down")
    ton "You know how guys are..." ("base", "base", "annoyed", "mid")
    ton "What was weird was... when he started to call me mommy again..." ("upset", "closed", "base", "mid")
    gen "What a wimp." ("base", xpos="far_left", ypos="head")
    ton "Don't be cruel, [name_genie_tonks]! It's just a little dirty talk..." ("soft", "base", "raised", "R")
    ton "And you have to admit, it's kinda hot... I even joined in on it." ("base", "narrow", "base", "mid")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    ton "What do you think made him fire his load across the room?" ("horny", "narrow", "base", "mid")
    ton "All it took was me saying \"cum for Mommy\"... and he had shot the biggest load towards me." ("horny", "closed", "base", "mid")
    ton "" ("base", "base", "angry", "mid")
    gen "Fuck... That {b}is{/b} pretty hot..." ("base", xpos="far_left", ypos="head")
    ton "I know..." ("crooked_smile", "narrow", "base", "mid")
    ton "*Ugh*... I definitely have to go rub one out after this..." ("mad", "base", "base", "ahegao")
    ton "See you, [name_genie_tonks]." ("base", "narrow", "base", "L")

    if _cum_known:
        gen "Are you going to do anything about the cum?" ("base", xpos="far_left", ypos="head")
        ton "*Hmm*?... The cum?" ("upset", "base", "worried", "down")
        ton "Oh... Why bother..." ("soft", "base", "base", "down")
        ton "It was already there on my way over here." ("soft", "closed", "shocked", "mid")
        ton "Besides, it'll be good for spreading the word, don't you think?" ("horny", "narrow", "base", "mid")
        gen "Whatever you say..." ("base", xpos="far_left", ypos="head")

    gen "Goodbye, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")

    # Tonks leaves

    $ ravenclaw += 20

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")

    $tonks.set_cum(None)

    jump end_tonks_event


label nt_pr_teach_T2_E3: # Tier 2 - Event 3 - Slytherin boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "[name_genie_tonks]..." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass

            "\"Make it quick!\"":
                ton "This Slytherin dickhead was asking for trouble again!" ("mad", "base", "angry", "R")
                ton "I did my best to punish him... thoroughly..." ("horny", "base", "angry", "mid")
                gen "Very good, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "*Mhmm*... Until next time, [name_genie_tonks]..." ("base", "happyCl", "base", "mid")
                
                $ slytherin += 20

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How'd your favour go today?" ("base", xpos="far_left", ypos="head")
    ton "It was all right..." ("open", "base", "base", "R")
    ton "I was able to kill two birds with one stone, though." ("base", "closed", "annoyed", "mid")
    gen "I'm intrigued." ("base", xpos="far_left", ypos="head")
    ton "So, I had some cocky little brat from Slytherin cause all sorts of trouble in class." ("open", "narrow", "annoyed", "downR")
    ton "Talking... letting a chocolate frog loose... forgetting to lock his \"Monster Book of Monsters\"..." ("open", "closed", "base", "mid")
    gen "(His what?)" ("base", xpos="far_left", ypos="head")
    ton "Just being a general pain in the ass." ("open", "base", "angry", "R")
    gen "Sounds like a hassle." ("base", xpos="far_left", ypos="head")
    ton "Slytherins always are." ("upset", "base", "base", "stare")
    ton "Anyway, I let him know he'd earned himself detention after class." ("open", "closed", "base", "mid")
    ton "Little bastard cursed me out for that... Disrespected me in front of the entire class..." ("upset", "base", "angry", "mid")
    ton "Once the class had emptied out, I proceeded to lock the door... to scare him a little..." ("soft", "base", "annoyed", "R")
    ton "After that I let him know that his \"Punishment\" was going to be selling me a favour." ("soft", "closed", "base", "mid")

    ton "I made him pull down his pants and whip his cock out..." ("open", "base", "shocked", "mid")
    ton "At first the idiot thought I was going to jerk him off..." ("disgust", "base", "shocked", "R")
    ton "I might have, if he'd played his cards right..." ("open", "narrow", "base", "mid")
    ton "Instead, his favour wouldn't be nearly as fun." ("soft", "narrow", "shocked", "R")
    ton "I demanded of him to start jacking it..." ("soft", "base", "annoyed", "mid")
    ton "It was actually pretty cute at first..." ("open", "closed", "base", "mid")
    ton "Then just as he was about to blow his load..." ("soft", "closed", "base", "mid")
    ton "Boom! Petrficus Totalus!" ("scream", "shocked", "angry", "mid", trans=vpunch)
    gen "{i}Petrifi{/i}-{w} {i}Petrifico{/i}?-{w} {i}Petrificato{/i}--" ("base", xpos="far_left", ypos="head")
    ton "I petrified him!" ("open", "wide", "angry", "mid")
    gen "*Ahh*..." ("base", xpos="far_left", ypos="head")
    ton "*Ha-ha-ha*... You should have seen his look on his face!" ("silly", "happyCl", "base", "mid")
    ton "That's what he gets, the little shit!" ("mad", "base", "angry", "down")
    ton "Not only did I leave him blue balled... I also left him pants down in the class." ("base", "base", "angry", "mid")
    gen "Forever?" ("base", xpos="far_left", ypos="head")
    ton "No, just until the spell wears off..." ("open", "closed", "base", "mid")
    ton "In an hour or so..." ("upset", "base", "angry", "R")
    ton "That, or someone else finds him..." ("upset", "base", "base", "up")
    ton "Either way, he learned his lesson about not screwing around in my class." ("open", "closed", "base", "mid")
    gen "Very good..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, Sir..." ("base", "base", "base", "mid")
    ton "See you..." ("base", "happyCl", "base", "mid")

    # Tonks leaves

    call bld
    gen "(This bitch might be crazier than I thought...)" ("base", xpos="far_left", ypos="head")

    $ slytherin += 20

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event

label nt_pr_teach_T2_E4: # Tier 2 - Event 4 - Slytherin girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"How was your day?\"":
                pass

            "\"Make it quick!\"":
                ton "This cute Slytherin girl earned herself a couple of points from me today..." ("open", "base", "base", "R")
                ton "She's really starting to get into it!" ("base", "base", "angry", "mid")
                gen "Good work, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "Thank you... Have a good night, [name_genie_tonks]..." ("base", "base", "base", "mid")
                
                $ slytherin += 20

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "Anything interesting happen today, [name_tonks_genie]?" ("base", xpos="far_left", ypos="head")
    ton "Oh yes!... I broke new ground today..." ("silly", "base", "shocked", "mid")
    gen "That's very promising... So what happened?" ("base", xpos="far_left", ypos="head")
    ton "Remember that cute little Slytherin?" ("horny", "base", "base", "mid")
    ton "The one that's still coming to grips with her budding sexuality?" ("base", "base", "angry", "mid")
    gen "The girl that you're turning into a lesbian?" ("base", xpos="far_left", ypos="head")
    ton "Well, I had her stay back after class today..." ("horny", "closed", "base", "mid")
    ton "For someone who supposedly hates selling favours... she was surprisingly keen today..." ("base", "base", "shocked", "mid")
    gen "Maybe she's finally coming around..." ("base", xpos="far_left", ypos="head")
    ton "I got her to give me a little peek under her skirt, for twenty house points..." ("base", "narrow", "base", "down")
    ton "And, after she'd pulled up her skirt, I did the old... \"offer more points for something else\" trick..." ("grin", "base", "base", "mid")
    ton "Had her drop her panties as well." ("base", "narrow", "base", "down")
    ton "I was expecting her to at least argue at least a bit about the amount of points she would receive for it..." ("open", "base", "base", "R")
    ton "But she dropped them in an instant, without even hearing my offer." ("horny", "base", "annoyed", "mid")
    ton "Next, she just looked at me as if to ask, \"what next\"?" ("open", "base", "base", "mid")
    ton @ hair horny "*Ugh*... It was so fucking hot..." ("soft", "base", "base", "stare")
    gen "And?... What did happen \"next\"?" ("grin", xpos="far_left", ypos="head")
    ton "I had her play with herself..." ("grin", "closed", "shocked", "mid")
    ton @ cheeks blush "But... that cute face of hers... and all the teasing..." ("open", "closed", "shocked", "R")
    ton @ cheeks blush "I decided to take matters into my own hands..." ("grin", "base", "base", "stare")
    ton "Specifically her matter..." ("horny", "base", "base", "mid")
    gen "You couldn't help yourself, could you?" ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "Can you blame me for wanting to \"finger\" that cute little slut?" ("soft", "base", "annoyed", "mid")
    gen "You're a bad teacher, you know that?" ("grin", xpos="far_left", ypos="head")
    ton "Tell me about it..." ("horny", "narrow", "base", "up")
    gen "What did she have to say about the whole thing?" ("base", xpos="far_left", ypos="head")
    ton "Not much..." ("soft", "narrow", "base", "R")
    ton "She just looked up at me, with those puppy-dog eyes... whispering \"wow\" and \"don't stop\" to me..." ("base", "narrow", "shocked", "up")
    ton "To think only a couple of days ago she tried pretending not to be into me..." ("open", "closed", "base", "mid")
    gen "Think she'll start talking now?" ("base", xpos="far_left", ypos="head")
    ton "Not unless she's ready to out herself as bi..." ("annoyed", "base", "base", "R")
    ton "But there are already some whispers going around school..." ("base", "base", "annoyed", "down")
    ton "And I may or may not have contributed to that..." ("grin", "base", "base", "R")
    gen "Very good work." ("base", xpos="far_left", ypos="head")
    gen "That'll be all then..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, [name_genie_tonks]..." ("base", "happyCl", "base", "mid")
    ton "See you next time..." ("base", "base", "base", "mid")

    # Tonks leaves

    $ slytherin += 20

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event
