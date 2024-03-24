

### Grope me ###

# (Tonks lets her students play with her tits, ass...)

#TODO Add Tonks chibi to all her public request nightly reports

label nt_pr_grope_start:
    ton "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    if states.ton.tier == 2:

        if not _events_completed_any:
            gen "Ready for the next step?" ("base", xpos="far_left", ypos="head")
            ton "*Mmmm*... You make it sound so ominous." ("soft", "narrow", "base", "mid")
            ton "What shall I do next with my students..." ("soft", "narrow", "shocked", "R")

            if not states.ton.ev.oral_practice.completed_once:
                ton "Want me to make out with them?" ("horny", "narrow", "base", "mid")
                gen "Maybe, but not right now..." ("base", xpos="far_left", ypos="head")
            else:
                ton "Want me to make out with them again?" ("horny", "base", "angry", "mid")

            gen "I was thinking you could take a few of these boys to second base." ("base", xpos="far_left", ypos="head")
            ton "Second base?! Already?" ("open", "shocked", "shocked", "up")
            gen "We're trying to earn you a reputation as a favour trader." ("base", xpos="far_left", ypos="head")
            gen "Making your students write lines in their underwear isn't going to cut it..." ("base", xpos="far_left", ypos="head")
            ton "I suppose you might be right..." ("base", "base", "base", "up")
            ton "I'm not sure if the students will be ready for it though..." ("mad", "base", "shocked", "R")
            gen "Please, you sound like you're talking about a pop-quiz." ("base", xpos="far_left", ypos="head")
            gen "All you have to do is get them to grope your chest a little..." ("base", xpos="far_left", ypos="head")
            ton "My breasts?" ("horny", "happyCl", "shocked", "up")
            gen "I can't imagine any of them saying no to that..." ("grin", xpos="far_left", ypos="head")
            ton "*Mmm*... Well if you say so...{w} You are the expert." ("base", "narrow", "base", "down")
            gen "That I am." ("base", xpos="far_left", ypos="head")
            gen "Now get out there and buy some favours!" ("base", xpos="far_left", ypos="head")
            ton "Yes, sir!" ("grin", "closed", "base", "mid")
            ton @ cheeks blush "(This is way better than being an auror!)" ("horny", "base", "base", "stare")

        else:
            gen "Think you're up for messing around with your students again?" ("base", xpos="far_left", ypos="head")
            gen "Let them cop a feel?" ("base", xpos="far_left", ypos="head")
            ton "Consider it done, [name_genie_tonks]." ("horny", "narrow", "base", "R")
            gen "I'll see you after class..." ("base", xpos="far_left", ypos="head")

    elif states.ton.tier >= 3:

        if not _events_completed_any: # Tell her to be even lewder for the next level of favors.
            gen "I'd like you to go out and have some handsy fun with your students." ("base", xpos="far_left", ypos="head")
            ton "Just like that? " ("open", "base", "raised", "mid")
            gen "Just like that, but I want you to be more handsy this time." ("grin", xpos="far_left", ypos="head")
            ton "I can certainly do that..." ("horny", "base", "base", "mid")
            ton "See you after class...{heart}" ("base", "happyCl", "base", "mid")
            gen "See ya!" ("grin", xpos="far_left", ypos="head")

        else: # Repeat
            gen "Would you like to mess around with your students again?" ("base", xpos="far_left", ypos="head")
            ton "And let them grope their teacher?" ("base", "base", "base", "mid")
            gen "Any way they like!" ("grin", xpos="far_left", ypos="head")
            ton "That sounds perfect!" ("base", "base", "base", "mid")
            gen "I'll see you after class..." ("base", xpos="far_left", ypos="head")
            ton "Yes, [name_genie_tonks]...{heart}" ("base", "base", "base", "mid")

    $ states.ton.ev.hands_on_lessons.completed_once = True

    # Tonks leaves
    call ton_walk(action="leave")
    jump end_tonks_event

### Tier 1 ###

label nt_pr_grope_T2_E1: # Tier 1 - Event 1 - Slytherin boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass

            "\"Make it quick!\"":
                ton "Remember that Slytherin boy?..." ("horny", "base", "angry", "mid")
                ton "I let him play with his favourite pair of tits again..." ("base", "base", "angry", "mid")
                gen "Well done, [name_tonks_genie]... We'll talk next time." ("base", xpos="far_left", ypos="head")
                ton "Yes, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")
                
                $ slytherin += 40

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How were classes today, [name_tonks_genie]?" ("base", xpos="far_left", ypos="head")
    gen "Taught your students some valuable lessons?" ("base", xpos="far_left", ypos="head")
    ton "I'm not sure about valuable..." ("base", "narrow", "base", "downR")
    ton "But I do know that he isn't going to forget it any time soon!" ("soft", "wink", "shocked", "mid")
    gen "That's what I like to hear!" ("base", xpos="far_left", ypos="head")
    ton "Remember that Slytherin cutie I held back to write lines?" ("base", "wide", "base", "R")
    gen "Vaguely." ("base", xpos="far_left", ypos="head")
    ton "Well, I decided to hold him back after class again." ("open", "closed", "base", "mid")
    ton "He tried to put on a proud Slytherin facade, claiming that I had no right to hold him back." ("base", "base", "annoyed", "downR")
    ton "Saying I was lucky he didn't \"report me\" for making him pull down his pants..." ("soft", "base", "annoyed", "mid")
    ton "It was all empty words, of course..." ("open", "closed", "base", "mid")
    ton "And I could tell by the {b}bulge{/b} in his pants that he {b}wanted{/b} to be there - more than anything." ("horny", "closed", "annoyed", "mid")
    ton "Still, I let him act tough... just so he wouldn't run away..." ("soft", "narrow", "base", "down")
    gen "So? How did you manage to get him to grab a handful?" ("base", xpos="far_left", ypos="head")
    ton "I let him know today wasn't a \"punishment\"." ("base", "narrow", "annoyed", "mid")
    ton "Asked what kept him distracted in class..." ("open", "base", "base", "R")
    ton "What he was constantly staring at..." ("soft", "narrow", "annoyed", "downR")
    ton "He didn't want to say it at first..." ("soft", "narrow", "base", "mid")
    ton "So I leaned in closer...{w} Let him feel my breath on his neck..." ("base", "closed", "annoyed", "mid")
    ton "And then I whispered the truth into his ear..." ("soft", "narrow", "annoyed", "stare")
    ton @ hair neutral "That he's a dirty little \"tit addict\"!" ("crooked_smile", "base", "angry", "up")
    gen "You naughty girl!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Ugh*... He went redder than a tomato when I said that." ("horny", "closed", "base", "mid")
    ton "And as both you and I know there's only one cure for that..." ("open", "closed", "base", "mid")
    ton "So I grabbed his wrist and forced it up to my chest!" ("open", "closed", "annoyed", "mid")
    gen "Just like that?" ("base", xpos="far_left", ypos="head")
    ton "He was hardly going to grab them himself!" ("crooked_smile", "narrow", "base", "downR")
    ton "Besides, grabbing them is the only way to get them off his mind..." ("soft", "narrow", "base", "R")
    ton "Or at least that's what I told him..." ("horny", "base", "base", "mid")
    gen "And he believed you?" ("base", xpos="far_left", ypos="head")
    ton "Maybe... Maybe not..." ("base", "base", "base", "R")
    ton "All I know is that he wasn't afraid to give it a go." ("grin", "happyCl", "base", "mid")
    gen "I gather that he enjoyed himself?" ("base", xpos="far_left", ypos="head")
    ton "He just sat there, silently groping my tits for several minutes..." ("soft", "narrow", "shocked", "down")
    ton @ hair horny "*Ugh*... It took everything I had not to hold him down and jump his bone..." ("horny", "base", "base", "up")
    gen "[name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
    ton "Right, well after letting him play with them for a little while, I sent him back to class." ("mad", "narrow", "base", "down")
    gen "Think you'll gain any reputation from this encounter?" ("base", xpos="far_left", ypos="head")
    ton "*Hmm*... I'm not sure if he'll talk..." ("annoyed", "narrow", "base", "R")
    ton "But the fact I ask students to stay behind after class should start spreading some rumours." ("base", "wink", "base", "mid")
    gen "Good to hear. That'll be all then, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
    ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")

    # Tonks leaves

    $ slytherin += 40

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_grope_T2_E2: # Tier 1 - Event 2 - Ravenclaw boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                ton "That shy Ravenclaw boy stayed behind in class again..." ("base", "base", "base", "mid")
                ton "He almost suffocated himself in between my cleavage..." ("silly", "happyCl", "base", "mid")
                gen "Well done, [name_tonks_genie]... We'll talk next time." ("base", xpos="far_left", ypos="head")
                ton "Yes, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")
                
                $ ravenclaw += 20

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "So, how are you finding the education industry?" ("base", xpos="far_left", ypos="head")
    ton "Fun!" ("grin", "happyCl", "base", "mid")
    ton "I never thought lesson planning and marking tests would actually be enjoyable, but there's something rather cathartic to it..." ("base", "base", "base", "mid")
    gen "And your... other tasks?" ("base", xpos="far_left", ypos="head")
    ton "Oh, of course messing around with our students is a nice bonus!" ("grin", "narrow", "base", "mid")
    gen "Speaking of..." ("base", xpos="far_left", ypos="head")
    ton "Don't worry, I've got a story for you, [name_genie_tonks]." ("base", "base", "annoyed", "mid")
    ton "Remember that shy Ravenclaw boy I had touch himself for me the other day?" ("base", "narrow", "base", "R")
    gen "Maybe, but go on..." ("base", xpos="far_left", ypos="head")
    ton "He stayed behind after class today..." ("open", "closed", "base", "mid")
    gen "He asked you to buy a favour from him?" ("base", xpos="far_left", ypos="head")
    ton "No... he's too shy. He wouldn't have the courage to do that..." ("soft", "base", "worried", "down")
    ton "He just - sort of - stayed in his seat after class... while looking down at his desk." ("soft", "narrow", "base", "down")
    ton "I waited until every other student had left, and then locked the door..." ("open", "closed", "base", "mid")
    gen "Who wouldn't want to be locked-up together with you!" ("grin", xpos="far_left", ypos="head")
    ton "It's more to keep the other students out..." ("soft", "base", "raised", "R")
    ton "But that doesn't mean he didn't gasp a little when I did it." ("horny", "wink", "annoyed", "mid")
    ton "So, after that, I went over and asked if there was anything wrong." ("base", "narrow", "base", "mid")
    ton "He just began mumbling about being sorry I had to give him detention..." ("soft", "base", "base", "downR")
    ton "And promised he'd never do anything bad in class again..." ("open", "base", "base", "R")
    ton "Those poor Ravenclaws sure do care about school!" ("silly", "happyCl", "base", "mid")
    ton "I made sure to let him know he was forgiven..." ("base", "wide", "base", "down")
    gen "How very wholesome of you..." ("base", xpos="far_left", ypos="head")
    ton "However... after this was done, he didn't give any inclination he wanted to get up from his seat..." ("soft", "closed", "base", "mid")
    ton "So, I figured he wanted to fool around again..." ("base", "narrow", "shocked", "down")
    ton "And boy was I right!" ("horny", "base", "base", "stare")
    ton "His face lit right up, when I asked if he wanted to buy another favour..." ("base", "base", "base", "mid")
    ton "Perhaps cupping a feel of his teacher's tits!" ("horny", "wide", "annoyed", "mid")
    gen "Naughty!" ("grin", xpos="far_left", ypos="head")
    ton "He had such an awe-struck look on his face... looking pretty nervous at first..." ("grin", "base", "base", "up")
    ton "It made it difficult for me to tell where his mind was going, that cheeky bugger!" ("mad", "closed", "shocked", "mid")
    gen "Which was?" ("base", xpos="far_left", ypos="head")
    ton "Straight in for the motorboat!" ("soft", "shocked", "annoyed", "mid")
    gen "Good on him..." ("base", xpos="far_left", ypos="head")
    gen "Did he do the noise as well?" ("grin", xpos="far_left", ypos="head")
    ton "No...{w} it was more like a hug if I'm being honest." ("annoyed", "base", "shocked", "up")
    ton "He just went in, face first into my cleavage, while locking his hands together behind my back." ("open", "closed", "shocked", "mid")
    ton "I thought he would've needed a lot more coaxing-into..." ("silly", "narrow", "base", "mid")
    gen "I suppose guys might be a bit different in that regard..." ("base", xpos="far_left", ypos="head")
    gen "So where did it go from there?" ("base", xpos="far_left", ypos="head")
    ton "Nowhere, really...{w} He just stared nuzzling his face into my tits..." ("annoyed", "narrow", "shocked", "R")
    ton "Grinding himself against my thigh, while giving me the tightest hug of his life..." ("base", "narrow", "base", "R")
    gen "Sounds like heaven..." ("base", xpos="far_left", ypos="head")
    ton "It was pretty cute if you ask me." ("grin", "happyCl", "base", "mid")
    gen "How long did this \"hug\" last exactly?" ("base", xpos="far_left", ypos="head")
    ton "*Pfff*... Five... maybe ten minutes..." ("annoyed", "base", "raised", "downR")
    ton "Eventually, it all got a bit too much... and he broke-off the hug..." ("annoyed", "closed", "base", "mid")
    ton "Stammered a thanks, and ran off." ("base", "base", "raised", "down")
    gen "Did you even get to reward any points?" ("base", xpos="far_left", ypos="head")
    ton "I did, even if he wasn't there to hear it..." ("silly", "closed", "base", "mid")
    gen "Very good. That'll be all then." ("base", xpos="far_left", ypos="head")
    ton "Have a good night, [name_genie_tonks]." ("base", "base", "shocked", "mid")

    # Tonks leaves

    $ ravenclaw += 20

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_grope_T2_E3: # Tier 1 - Event 3 - Two Gryffindor boys
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass

            "\"Make it quick!\"":
                ton "I let those two Gryffindors feel me up again..." ("open", "base", "base", "R")
                ton "Of course they didn't get any points for it..." ("base", "base", "angry", "mid")
                gen "Great job, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "Thank you, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "I didn't notice any extra points today..." ("base", xpos="far_left", ypos="head")
    gen "Does that mean what I think it does?" ("base", xpos="far_left", ypos="head")
    ton "Perhaps..." ("soft", "closed", "raised", "mid")
    gen "So... you went for one of the Gryffindor students?" ("base", xpos="far_left", ypos="head")
    ton "Kind of..." ("grin", "base", "base", "R")
    ton "It might have been \"two boys\" today..." ("open", "wide", "base", "R")
    gen "Nice, selling two favours in one day should get the word around..." ("base", xpos="far_left", ypos="head")
    ton "Well... it wasn't exactly two favours..." ("mad", "base", "base", "down")
    gen "Oh... Wait, Oh...{w} I see..." ("base", xpos="far_left", ypos="head")
    ton "They're such good friends! I don't think I could manage splitting them apart..." ("grin", "happyCl", "base", "mid")
    ton "Besides, I've already fooled around a little with them, so there was barely any convincing involved..." ("base", "base", "annoyed", "down")
    gen "I'm sure there wasn't... so how was it?" ("base", xpos="far_left", ypos="head")
    ton "Honestly? Pretty fucking hot..." ("horny", "base", "angry", "mid")
    ton "Having four hands grabbing at you at once is {b}intense{/b}..." ("horny", "base", "annoyed", "up")
    gen "I bet...{w=0.3} So did they just play with your tits?" ("base", xpos="far_left", ypos="head")
    ton "They did at first...{w} But then I quickly found one of their hands somewhere else..." ("base", "base", "shocked", "mid")
    ton "Pretty soon after that, they each moved the other onto my ass as well..." ("soft", "base", "base", "stare")
    ton "*Ugh*... I had to draw the line once they tried groping me under my shirt..." ("mad", "base", "base", "ahegao")
    gen "*Mmmm*... did you?" ("base", xpos="far_left", ypos="head")
    ton "I don't think I would have been able to stop them at all if I didn't..." ("open", "closed", "base", "mid")
    ton "Or myself, for that matter..." ("upset", "base", "base", "up")
    ton "Not that it would have been the worst thing in the world to let them touch my tits directly..." ("base", "base", "base", "R")
    ton "Anyhow, I offered them some house points for it... but to my surprise they both kindly refused..." ("open", "closed", "base", "mid")
    ton "Said they'd much rather have a \"go at it\" again..." ("base", "base", "angry", "mid")
    gen "Think they'll spread the word this time?" ("base", xpos="far_left", ypos="head")
    ton "They were both pitching a pretty big tent when they left class... that was noticeable to say the least..." ("silly", "happyCl", "base", "mid")
    gen "Very good, [name_tonks_genie], very good..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, sir." ("base", "happyCl", "base", "mid")
    ton "Now, if you don't mind... I think I better head to my room for some...{w} \"unwinding\"..." ("mad", "narrow", "base", "R")
    gen "Have a good night then..." ("base", xpos="far_left", ypos="head")
    ton "Night, [name_genie_tonks]!" ("silly", "happyCl", "base", "mid")

    # Tonks leaves

    # No points for Gryffindor.
    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_grope_T2_E4: # Tier 1 - Event 4 - Slytherin girl
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                ton "I tried my luck with that Slytherin girl again..." ("open", "base", "base", "mid")
                ton "She's the hardest nut to crack, I tell you..." ("open", "base", "worried", "R") # hardest instead of tough in the UK.
                gen "You will have better luck next time, [name_tonks_genie]..." ("base", xpos="far_left", ypos="head")
                ton "I hope so too, [name_genie_tonks]... Have a good night." ("base", "base", "worried", "mid")
                
                $ slytherin += 40

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How's my favourite teacher doing today?" ("base", xpos="far_left", ypos="head")
    ton "Never been better!" ("silly", "happyCl", "base", "mid")
    gen "I take it you were able to buy a favour then?" ("base", xpos="far_left", ypos="head")
    ton "You bet! Even if she might not have wanted to sell it at first..." ("base", "wink", "shocked", "mid")
    gen "A She?" ("grin", xpos="far_left", ypos="head")
    ton "Remember that naive Slytherin that couldn't keep her eyes off me?" ("grin", "base", "raised", "mid")
    gen "I think so..." ("base", xpos="far_left", ypos="head")
    ton "Well, I held her back after class again." ("base", "closed", "base", "mid")
    ton "Of course she made a fit about it... Not that she made any efforts to leave, though..." ("base", "narrow", "shocked", "R")
    ton "So, I sat her down, and had a little conversation with her." ("soft", "base", "base", "mid")
    gen "About what?" ("base", xpos="far_left", ypos="head")
    ton "You know... girl talk..." ("grin", "closed", "base", "mid")
    ton "How it's okay to be a little - \"sexually confused\" sometimes..." ("open", "closed", "base", "mid")
    ton "And that - maybe - she just needed to get it all out of her system..." ("base", "narrow", "base", "mid")
    gen "How did she take that?" ("base", xpos="far_left", ypos="head")
    ton "She kept insisting of not having the slightest idea of what I was talking about." ("soft", "narrow", "raised", "R")
    ton "Even though her eyes were glued to my chest as she spoke..." ("base", "base", "base", "down")
    gen "*Mhmm*................" ("base", xpos="far_left", ypos="head")
    ton "Eventually, I just grabbed her wrist and pulled it up to meet my chest..." ("open", "closed", "shocked", "mid")
    gen "Just like that?" ("base", xpos="far_left", ypos="head")
    ton "*Mhmm*... It was fantastic!" ("base", "base", "base", "stare")
    ton "You should have seen the war-of-emotions taking place behind her eyes!" ("horny", "base", "annoyed", "stare")
    ton "It was incredible! I love seeing Slytherins get all flustered like that." ("grin", "happyCl", "annoyed", "mid")
    gen "Sweet... What happened next?" ("base", xpos="far_left", ypos="head")
    ton "She calmed down a bit once I offered her points for this little favour..." ("base", "narrow", "base", "mid")
    gen "That calmed her down?" ("base", xpos="far_left", ypos="head")
    ton "Apparently. After all, this wasn't the first favour I bought off her..." ("base", "narrow", "raised", "R")
    gen "Did she start playing with you after that?" ("base", xpos="far_left", ypos="head")
    ton "Not exactly, she just sat there face bright-red, whilst she let me hold her hands against my breasts..." ("open", "base", "shocked", "downR")
    ton "And I let her go a couple of seconds after that..." ("normal", "base", "base", "down")
    gen "Do you think she'll spread the word that you're buying favours?" ("base", xpos="far_left", ypos="head")
    ton "I can't say... I think she's still pretty conflicted about the whole thing..." ("annoyed", "base", "raised", "down")
    gen "Do you really think she's a lesbian?" ("base", xpos="far_left", ypos="head")
    ton "Maybe... she does seem a little {b}curious{/b}..." ("open", "closed", "base", "mid")
    ton "Couple that with her being a stubborn Slytherin..." ("open", "base", "base", "R")
    ton "She's a whole mix of confused emotions... but she'll figure it out." ("base", "base", "base", "mid")
    gen "Let's hope this isn't a hopeless cause..." ("base", xpos="far_left", ypos="head")
    ton "Don't be silly... she's perfect!{w} Just the way I like them." ("horny", "wink", "raised", "mid")
    gen "........................" ("base", xpos="far_left", ypos="head")
    gen "Well, keep me informed... That should be all for now..." ("base", xpos="far_left", ypos="head")
    ton "Yes, [name_genie_tonks]!" ("base", "base", "base", "mid")

    # Tonks leaves

    $ slytherin += 40

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event

### Tier 3 ###

# label nt_pr_grope_T3_E1: # Tier 2 - Event 1
#     #Begrudgingly talks about how pretty tonks is


# label nt_pr_grope_T3_E2: # Tier 2 - Event 2 - Ravenclaw boy again
#     #breastfeeding and mommy play



# label nt_pr_grope_T3_E3: # Tier 2 - Event 3
#     #hufflepuff girl comes in asking for another favour
#     #ends up sucking tonks boobs



# label nt_pr_grope_T3_E4: # Tier 2 - Event 4 -
#     #Tonks has her a slyhterin girl sit there and do work while she has no top on
