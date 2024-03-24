

### Kissing ###

# ([name_tonks_genie] makes out with her students...)

#TODO Add Tonks chibi to all her public request nightly reports

label nt_pr_kiss_start:
    ton "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=fade)

    if states.ton.tier == 2:

        if not _events_completed_any:
            gen "Ready to try something a little different?" ("base", xpos="far_left", ypos="head")
            ton "*Mmmm*... Absolutely! This is the most fun I've had in years!" ("horny", "base", "base", "mid")
            ton "What did you have in mind?" ("base", "base", "shocked", "mid")
            gen "What do you think?" ("base", xpos="far_left", ypos="head")

            if not states.ton.ev.hands_on_lessons.completed_once:
                ton "I think making out with them would be really fucking hot..." ("horny", "base", "base", "R")
                gen "Just kissing?" ("base", xpos="far_left", ypos="head")
                ton "You don't understand...{w} The way I make out..." ("soft", "base", "base", "mid")
                ton "It's way more intense than anything these students would have ever experienced..." ("base", "base", "annoyed", "stare")
            else:
                ton "I know you shot it down earlier... but I think a little making out would be really fucking hot..." ("horny", "base", "angry", "mid")
                gen "*Pfft*... you're such a bad girl..." ("base", xpos="far_left", ypos="head")
                gen "You've already gotten to second base! Let's not jump back to first!" ("base", xpos="far_left", ypos="head")
                ton "You don't get it...{w} The way I make out..." ("horny", "base", "base", "R")
                ton "It's way more intense than anything these students would have ever experienced..." ("base", "base", "angry", "mid")
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            gen "So you're not just going to give them a peck on the cheek, are you?" ("grin", xpos="far_left", ypos="head")
            ton "Oh no..." ("crooked_smile", "narrow", "base", "mid")
            ton "They'll be lucky if they can talk straight after I'm done with them..." ("crooked_smile", "closed", "base", "mid")
            gen "You've set my expectations in you quite high, you know that right?" ("base", xpos="far_left", ypos="head")
            ton "I'll make sure you get your money's worth, don't worry..." ("soft", "wink", "base", "mid")
            gen "Just see me after class." ("base", xpos="far_left", ypos="head")
            ton "Yes, sir!" ("grin", "base", "base", "R")

        else:

            gen "Fancy another student-snog-session?" ("base", xpos="far_left", ypos="head")
            ton @ hair horny "*Mmmm*... You bet... Teaching is my job..." ("horny", "base", "base", "R")
            ton "Even if that lesson is \"French Kissing\"..." ("soft", "wink", "shocked", "mid")
            gen "Well, don't let me stop you." ("base", xpos="far_left", ypos="head")
            ton "Thank you, sir..." ("grin", "base", "base", "mid")

    elif states.ton.tier >= 3: # Not in 1.37

        if not _events_completed_any: # Tell her to be even lewder for the next level of favors.

            gen "Would you like to help your students with their oral skills again?" ("base", xpos="far_left", ypos="head")
            ton "*Mmmm*, yes... Some of them are in dire need of some practice..." ("horny", "base", "raised", "mid")
            gen "Then go give them some practice!" ("grin", xpos="far_left", ypos="head")
            ton "I will, [name_genie_tonks]..." ("base", "base", "base", "mid")

        else: # Repeat

            gen "How would you feel about French kissing your students again?" ("base", xpos="far_left", ypos="head")
            ton @ hair horny "*Mmmm*... Pretty good if the last few times are anything to go by..." ("horny", "base", "base", "R")
            ton "I'll see you after class..." ("base", "base", "angry", "mid")

    # Tonks leaves

    $ states.ton.ev.oral_practice.completed_once = True

    call ton_walk(action="leave")
    jump end_tonks_event



### Tier 1 ###

label nt_pr_kiss_T2_intro_E1: # Tier 1 - Event 1 - Slytherin boy
    #Gentle kissing
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass
            "\"Make it quick!\"":
                ton "I made out with my favourite Slytherin boy again..." ("open", "base", "base", "R")
                ton "He's getting quite good at it..." ("horny", "base", "base", "up")
                gen "Well done, [name_tonks_genie]... We'll talk next time." ("base", xpos="far_left", ypos="head")
                ton "Have a good night, [name_genie_tonks]." ("base", "happyCl", "base", "mid")
                
                $ slytherin += 40

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "Fun day?" ("base", xpos="far_left", ypos="head")
    ton "It was!" ("crooked_smile", "happyCl", "base", "mid")
    ton "I got to show some students a Boggart for the first time...{w} That was pretty entertaining!" ("silly", "base", "base", "mid")
    gen ".................." ("base", xpos="far_left", ypos="head")
    ton "Not to mention that I got to take a boy's first kiss..." ("soft", "narrow", "annoyed", "mid")
    gen "A first for everybody!" ("grin", xpos="far_left", ypos="head")
    ton "*Mmmm*... I know which one I preferred..." ("crooked_smile", "base", "base", "up")
    gen "Care to fill me in?" ("base", xpos="far_left", ypos="head")
    ton "I'd love to!" ("base", "base", "shocked", "stare")
    ton "So, today I had class with my favourite little \"Slytherin boy\"..." ("open", "closed", "base", "mid")
    ton "I didn't really have much to do after classes, so I figured I may as well hold him back..." ("grin", "base", "base", "R")
    ton "He was expecting me to buy a favour straight away..." ("soft", "closed", "base", "mid")
    ton "However, I was in the mood for a little conversation today..." ("base", "narrow", "base", "mid")
    ton "Some rather unimportant banter... Such as his performance in class..." ("open", "base", "base", "down")
    ton "Then I asked if he had a girlfriend, to maybe help with him at school..." ("base", "happyCl", "base", "mid")
    ton "He answered {b}no{/b}, of course... so I showed him some sympathy..." ("soft", "narrow", "base", "R")
    ton "Saying how {b}hard{/b} it must be - trying your best to concentrate on school with so many pretty girls running around..." ("soft", "narrow", "shocked", "mid")
    gen "(I should go for a walk as well some day...)" ("base", xpos="far_left", ypos="head")
    ton "Then I asked if he'd ever made out with any of the girls..." ("base", "base", "raised", "mid")
    ton "And of course he hadn't..." ("soft", "base", "shocked", "up")
    ton "So, obviously, I just had to buy this little favour from him..." ("open", "closed", "shocked", "mid")
    ton "It's my duty as a teacher of this school - to see to my students education!" ("soft", "wink", "shocked", "mid")
    gen "How noble..." ("base", xpos="far_left", ypos="head")
    ton "He was so excited by the whole thing." ("crooked_smile", "base", "base", "down")
    ton "You should have seen his face... It was precious." ("base", "happyCl", "base", "mid")
    gen "Was it as intense as you promised?" ("base", xpos="far_left", ypos="head")
    ton "Not that intense, per se... I wanted to take it slow for his first time..." ("soft", "narrow", "base", "downR")
    ton "I just sat next to him, and slowly peppered a few kisses on his lips..." ("soft", "narrow", "base", "mid")
    ton "After the initial excitement died down, we eventually got into a nice rhythm of kissing... and some light tongue-play..." ("horny", "base", "base", "stare")
    ton "He was very inexperienced, but definitely eager to learn." ("horny", "wink", "annoyed", "mid")
    ton "Then, after five minutes or so, I awarded him some house points... and sent him on his way..." ("base", "narrow", "base", "R")
    gen "And that was all?" ("base", xpos="far_left", ypos="head")
    ton "I don't think it's the last I'll see of him... Besides, I don't want to push him too far." ("soft", "closed", "base", "mid")
    ton "This favour trading might actually be a good way to address student behaviour!" ("crooked_smile", "base", "raised", "mid")
    gen "Oh... How so?" ("base", xpos="far_left", ypos="head")
    ton "His behaviour has really started to improve after I began buying favours from him!" ("base", "narrow", "base", "mid")
    gen "Maybe you should consider dealing with all your troublemakers this way?" ("base", xpos="far_left", ypos="head")
    ton "*Hmm*... Don't tempt me..." ("horny", "base", "base", "R")
    gen "That'll be all then." ("base", xpos="far_left", ypos="head")
    ton "Right, see you, [name_genie_tonks]." ("base", "base", "base", "mid")

    # Tonks leaves.

    $ slytherin += 40

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_kiss_T2_E2: # Tier 1 - Event 2 - Ravenclaw boy
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass

            "\"Make it quick!\"":
                ton "Sorry I'm a bit late today..." ("open", "base", "base", "R")
                ton "I was \"occupied\" kissing that little Ravenclaw boy again..." ("horny", "base", "angry", "mid")
                gen "Very good, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
                ton "Thank you, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")
                
                $ ravenclaw += 20

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "You're a bit late..." ("base", xpos="far_left", ypos="head")
    gen "Got caught up having too much fun with your students?" ("grin", xpos="far_left", ypos="head")
    ton "*Mmmm*... and then some..." ("horny", "base", "base", "R")
    gen "I like the sound of that!" ("grin", xpos="far_left", ypos="head")
    gen "Now, care to elaborate?" ("base", xpos="far_left", ypos="head")
    ton "Alright then, you old perv..." ("soft", "wink", "annoyed", "mid")
    ton "Today's event was with my favourite little Ravenclaw boy..." ("open", "closed", "base", "down")
    gen "That shy one?" ("base", xpos="far_left", ypos="head")
    ton "Yes, the cute one!{w} He made a classic mistake today..." ("crooked_smile", "wide", "base", "mid")
    gen "Which is?" ("base", xpos="far_left", ypos="head")
    ton "Calling your teacher \"Mommy\"." ("open", "base", "shocked", "down")
    gen "*ha-ha-ha*!... Really?" ("grin", xpos="far_left", ypos="head")
    gen "I bet the students had a field day with that one!" ("base", xpos="far_left", ypos="head")
    ton "Surprisingly not... Everyone just sort of went quiet." ("annoyed", "narrow", "base", "R")
    gen "I know that {b}I{/b} would have given him hell for that..." ("base", xpos="far_left", ypos="head")
    ton "I might have blushed as much as him - after he said it..." ("upset", "base", "base", "down")
    ton "Anyhow... I decided that it was reason enough to hold him back..." ("open", "closed", "base", "mid")
    ton "Not that I needed to... He seemed almost paralysed for the rest of the lesson..." ("crooked_smile", "base", "raised", "R")
    ton "He just sat there with his head down... waiting for everyone to leave the classroom..." ("soft", "closed", "base", "mid")
    ton "So, I figured I'd indulge him..." ("soft", "narrow", "base", "mid")
    ton "I walked over - and plonked myself onto his lap, facing him..." ("grin", "base", "base", "mid")
    gen "Bet that woke him up!" ("grin", xpos="far_left", ypos="head")
    ton "Yes... However I wouldn't say it bothered him too much..." ("open", "base", "base", "R")
    ton "He just looked up at me with those big puppy eyes..." ("soft", "base", "base", "mid")
    ton "And then I broke our gaze and kissed him..." ("horny", "wink", "base", "mid")
    gen "How did he take it?" ("base", xpos="far_left", ypos="head")
    ton "Great! That kiss must have awoken something in him..." ("crooked_smile", "base", "shocked", "mid")
    ton "He really got into it after a while..." ("base", "happyCl", "base", "mid")
    ton "*Ugh*!... I've never had someone attack me with their tongue like that..." ("horny", "base", "base", "up")
    ton @ hair horny "It was intense! And neither of us wanted it to end..." ("soft", "base", "shocked", "ahegao")
    gen "Is that why you were late today?" ("grin", xpos="far_left", ypos="head")
    ton "*Hmm*... Can you blame me?" ("crooked_smile", "base", "base", "up")
    gen "So you spent all afternoon French kissing one of your students?" ("grin", xpos="far_left", ypos="head")
    ton "Yes, [name_genie_tonks]..." ("soft", "closed", "base", "mid")
    ton @ hair neutral "I guess I fucking did!" ("crooked_smile", "base", "shocked", "mid")
    gen "I'm very proud!" ("grin", xpos="far_left", ypos="head")
    gen "Great work, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "..." ("crooked_smile", "base", "base", "up")
    ton "Thank you, [name_genie_tonks]. Have a good night." ("base", "wink", "base", "mid")

    # Tonks leaves.

    $ ravenclaw += 20

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_kiss_T2_E3: # Tier 1 - Event 3 - Slytherin girls
    #Tonks pays two best friends to make out
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass

            "\"Make it quick!\"":
                ton "I gave those two Slytherin sluts detention again..." ("open", "base", "base", "R")
                ton "Fuck, I came so hard watching them kiss!" ("base", "base", "base", "mid")
                gen "You wouldn't believe how jealous I am!" ("base", xpos="far_left", ypos="head")
                ton "You have no idea, [name_genie_tonks]!" ("base", "base", "angry", "mid")
                ton "I better get going. Until next time!" ("base", "happyCl", "base", "mid")
                
                $ slytherin += 40

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    gen "How was your day?" ("base", xpos="far_left", ypos="head")
    ton "Better than most... You'll love this one!" ("base", "wink", "base", "mid")
    gen "Don't let me stop you then..." ("grin", xpos="far_left", ypos="head")
    ton "As always, there were a few Slytherins messing around in class..." ("base", "base", "base", "mid")
    ton "With an especially annoying pair of girls that wouldn't shut up!" ("open", "closed", "raised", "mid")
    ton "So... I gave them detention... which thankfully got them to quiet down a little." ("soft", "base", "base", "L")
    gen "So far so good..." ("base", xpos="far_left", ypos="head")
    ton "Normally, I only try and buy favours from one person at a time..." ("normal", "closed", "base", "mid")
    ton "But then I figured, why not give both those Slytherin sluts a shot." ("crooked_smile", "base", "base", "mid")
    gen "So you took turns kissing the girls?" ("grin", xpos="far_left", ypos="head")
    ton "No, but I could have..." ("soft", "base", "base", "R")
    ton "I gave them the option of staying behind - for a full hour of detention..." ("open", "closed", "base", "mid")
    ton "Or... have them do their teacher a little favour..." ("base", "base", "base", "mid")
    gen "Which was?" ("grin", xpos="far_left", ypos="head")
    ton "*Mmmm*... They had to make out with each other!" ("horny", "base", "shocked", "down")
    ton "And they had to do it properly. For at least ten minutes." ("soft", "closed", "base", "mid")
    ton "*Ugh*... It was the hottest thing to witness, I tell you..." ("horny", "base", "base", "stare")
    gen "Don't spare any details!" ("grin", xpos="far_left", ypos="head")
    ton "Well, they were a bit hesitant at first... which I can't even blame them for..." ("soft", "base", "base", "mid")
    ton "It doesn't happen often that you have a teacher watch you make out... and savouring every second of it!" ("horny", "narrow", "base", "mid")
    ton "But, I have a feeling that wasn't their first time kissing another girl..." ("crooked_smile", "closed", "base", "mid")
    ton "Maybe not even each other..." ("base", "narrow", "annoyed", "mid")
    gen "Ought to be young again..." ("base", xpos="far_left", ypos="head")
    ton "I couldn't help myself, [name_genie_tonks]!" ("crooked_smile", "base", "base", "stare")
    ton @ hair horny "I simply {b}had{/b} to play around while they did it..." ("horny", "happyCl", "shocked", "mid")
    gen "Did they care?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "Not one bit!" ("horny", "base", "base", "down")
    ton "They'd just take it in waves..." ("soft", "base", "base", "L")
    ton @ cheeks blush "Making out... Calling me a pervert..." ("horny", "base", "base", "up")
    ton @ cheeks blush "Locking their mouths together, only to break apart again to tease me  more..." ("base", "base", "base", "ahegao")
    ton @ cheeks blush "*Ugh*... It was so {b}bloody hot!{/b}..." ("open_wide_tongue", "base", "base", "ahegao")
    gen "I take your word for it..." ("base", xpos="far_left", ypos="head")
    ton "This really is the best job ever!" ("grin", "wide", "shocked", "mid")
    gen "Very good! That shall be all for now, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
    ton "Have a good night, [name_genie_tonks]." ("base", "happyCl", "base", "mid")

    # Tonks leaves.

    $ slytherin += 40

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event


label nt_pr_kiss_T2_E4: #Level 1 Event 4
    #Tender make-out session with a Slytherin lesbian
    call ton_walk(action="enter", xpos="mid", ypos="base")
    ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"You are back!\"":
                pass

            "\"Make it quick!\"":
                ton "I kissed that cute little Slytherin girl..." ("open", "base", "base", "mid")
                ton "She getting there!" ("base", "happyCl", "base", "mid")
                gen "Very good, [name_tonks_genie]." ("base", xpos="far_left", ypos="head")
                ton "Thank you, [name_genie_tonks]. Have a good night." ("base", "base", "base", "mid")
                
                $ slytherin += 40

                if states.ton.public_level < 9: # Points til 9.
                    $ states.ton.public_level += 1

                call ton_walk(action="leave")
                jump end_tonks_event

    ton "I have a story for you!" ("grin", "base", "shocked", "mid")
    gen "Let's hear it!" ("grin", xpos="far_left", ypos="head")
    ton "This is so good, I feel I should write it down and turn it into a novel..." ("base", "happyCl", "base", "mid")
    gen "About a boy snogging his teacher?" ("grin", xpos="far_left", ypos="head")
    ton "No.{w} About a tender and confused girl..." ("crooked_smile", "closed", "base", "mid")
    ton "Who's coming to terms with her sexuality, thanks to her stunningly intelligent teacher." ("soft", "wink", "annoyed", "mid")

    ton "That little Slytherin girl is starting to come around to me more often - as of late..." ("crooked_smile", "narrow", "base", "mid")
    ton "So, I figured now might be a good time to take it to the next level..." ("base", "base", "base", "R")
    ton "Getting her to stay after class is easy enough now..." ("open", "closed", "base", "mid")
    ton "I just brush her hand as I walk past her... and throw her a subtle wink." ("horny", "narrow", "base", "mid")
    gen "You're getting brazen!" ("grin", xpos="far_left", ypos="head")
    ton "Wasn't that the plan?" ("upset", "base", "shocked", "R")
    gen "I never said it was a bad thing..." ("base", xpos="far_left", ypos="head")
    ton "Good!{w} Because I don't intend on slowing down..." ("crooked_smile", "closed", "annoyed", "mid")
    ton "Not after what happened today!" ("horny", "base", "angry", "mid")
    ton "She was so cute!..." ("open", "happyCl", "worried", "mid")
    ton "Still nervous, but not nearly as cocky..." ("soft", "base", "shocked", "R")
    ton "Today, she simply let her reddened cheeks do most of the talking... Until the end of my lessons..." ("grin", "narrow", "base", "mid")
    ton "And, once the classroom had emptied out, I offered to purchase another favour from her." ("base", "closed", "base", "mid")
    ton "It's not as if she'd say no at this stage." ("soft", "wink", "base", "mid")
    ton "I believe she wasn't expecting me to ask for a kiss though... It really threw her for a loop..." ("crooked_smile", "narrow", "base", "mid")
    gen "....................." ("base", xpos="far_left", ypos="head")
    ton "She couldn't quite work out whether it was too extreme of a favour... or too mild..." ("annoyed", "base", "shocked", "R")
    gen "Well, it all depends on how you kiss..." ("base", xpos="far_left", ypos="head")
    ton "*Hmm*... Yes!" ("horny", "base", "base", "ahegao")
    ton "For an emotionally charged schoolgirl, she really didn't let me down one bit..." ("horny", "base", "annoyed", "up")
    ton "Her lips kept quivering...{w} And I'm not sure if it was because of fear... or anticipation..." ("soft", "narrow", "base", "R")
    ton "And she gazed at me like a stunned deer... Waiting for me to make the first move..." ("soft", "narrow", "base", "mid")
    ton "*Mmmm*... Her lips were so soft!" ("soft", "base", "base", "up")
    gen "This is good!" ("grin", xpos="far_left", ypos="head")
    gen "Did you slip in some tongue?" ("grin", xpos="far_left", ypos="head")
    ton "*Mhmm*... More than some..." ("horny", "base", "base", "stare")
    ton "I was surprised just how easily she opened her mouth for me..." ("grin", "base", "shocked", "mid")
    ton "Once my tongue was in there - it was game-over for her!" ("soft", "closed", "base", "mid")
    ton "I just softly cradled her head - and spent the next five minutes teaching her how to \"french\"..." ("soft", "base", "shocked", "up")
    ton "They can't offer you an experience like that at the Ministry!" ("grin", "wink", "base", "mid")
    gen "Consider yourself lucky then." ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Oh, I do!{w} Believe me!" ("crooked_smile", "closed", "shocked", "mid")
    gen "That shall be all for now..." ("base", xpos="far_left", ypos="head")
    ton "Thank you, [name_genie_tonks]." ("soft", "narrow", "base", "mid")

    # Tonks leaves.

    $ slytherin += 40

    if states.ton.public_level < 9: # Points til 9.
        $ states.ton.public_level += 1

    call ton_walk(action="leave")
    jump end_tonks_event



### Tier 3 ###

# label nt_pr_kiss_T3_E1: # Tier 2 Event 1 # Not in use.
#     call ton_walk(action="enter", xpos="mid", ypos="base")
#     ton "Hi, [name_genie_tonks]." ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)

#     gen "How did your extracurricular activities pan out today?" ("base", xpos="far_left", ypos="head")
#     ton "Honestly? I don't think I've ever been as turned on in my life..." ("base", "base", "base", "mid")
#     ton "Fuck... It was incredible... the power I felt over him... it was intoxicating..." ("base", "base", "base", "mid")
#     gen "Care to elaborate?" ("base", xpos="far_left", ypos="head")
#     ton "Well, you know that stuck up little Slytherin I've been fooling around with?" ("base", "base", "base", "mid")
#     gen "The guy or the girl?" ("base", xpos="far_left", ypos="head")
#     ton "The boy." ("base", "base", "base", "mid")
#     gen "Yep, I think I remember them..." ("base", xpos="far_left", ypos="head")
#     ton "I asked them to stay back after classes again... Even if it was by staring at them during class..." ("base", "base", "base", "mid")
#     ton "Either way... He knew he had to stay behind to play with \"auntie\" Tonks..." ("base", "base", "base", "mid")
#     gen "Kinky..." ("base", xpos="far_left", ypos="head")
#     ton "Mmmm, I walked over to him slowly... Making sure I savoured that frightened look on his face..." ("base", "base", "base", "mid")
#     ton "Then, I got to his desk... I was half expecting him to blabber on about not deserving to be there..." ("base", "base", "base", "mid")
#     ton "But today he just looked up at me with a delectable mix of fear and anticipation..." ("base", "base", "base", "mid")

#     # Genie starts jerking off

#     #">Unable to help yourself any longer, you start to inconspicuously stroke your cock under your desk."
#     #ton "*tsk* *tsk* *tsk*...{w} Couldn't help yourself, could you?"
#     #gen "Can you blame me?" ("base", xpos="far_left", ypos="head")
#     #ton "I suppose not..."
#     #ton "Anyway, back to that cute little thing..."

#     ton "Eventually I'd had enough of his eager expression..." ("base", "base", "base", "mid")
#     ton "I pounced upon him... Sitting down on his lap, pinning him to his chair and forcing my chest into his..." ("base", "base", "base", "mid")
#     ton "I could feel his heartbeat... It was so fast... Like a mouse..." ("base", "base", "base", "mid")
#     ton "Whispering in his ear I asked if he wanted a little kiss..." ("base", "base", "base", "mid")
#     ton "Making sure to let him know that I'd pay him plenty of points..." ("base", "base", "base", "mid")
#     ton "Just for a kiss..." ("base", "base", "base", "mid")
#     gen "*Mmmmm*..." ("base", xpos="far_left", ypos="head")
#     ton "Of course he said yes... Even if it was so faint I could barely hear it..." ("base", "base", "base", "mid")
#     ton "But once he said it... I was on him..." ("base", "base", "base", "mid")
#     ton "I pinned him down as I held his head in place..." ("base", "base", "base", "mid")
#     ton "Ugh... My tongue was going crazy..." ("base", "base", "base", "mid")
#     ton "I'm not sure if you remember this from school, sir, but I'm an Metamorphmagus..." ("base", "base", "base", "mid") # Note: I'd wait with adding Tonks' abilities and reserve them for the 2nd level of favors (longer tongue, bigger breasts...)
#     ton "Normally I just use that to blend in or for jokes..." ("base", "base", "base", "mid")
#     ton "But sometimes I use it to... Play around..." ("base", "base", "base", "mid")
#     ton "And all the excitement today may have caused me to lose control of my tongue..." ("base", "base", "base", "mid")
#     gen "Lose control of your tongue?" ("base", xpos="far_left", ypos="head")
#     ton "Ugh... it was so long..." ("base", "base", "base", "mid")
#     ton "It was like I was fucking that poor boys mouth with it..." ("base", "base", "base", "mid") # Note: This section is a bit too extreme for the first level.
#     ton "I wrapped his tongue in mine... stuck it down his throat..." ("base", "base", "base", "mid")
#     ton "Ugh... I even licked his face clean..." ("base", "base", "base", "mid")
#     ton "By the time I was done there wasn't a dry spot on his face..." ("base", "base", "base", "mid")
#     gen "*Argh*..." ("base", xpos="far_left", ypos="head")
#     ton "Poor thing... I think I broke him if I'm being honest..." ("base", "base", "base", "mid")
#     gen "That's it..." ("base", xpos="far_left", ypos="head")
#     ton "I thought he'd like it... but there were so many tears--" ("base", "base", "base", "mid")

#     #gen "UGH... THERE IT IS!!!" ("grin", xpos="far_left", ypos="head")
#     # Genie cums
#     #">You begin firing a load of under your desk, making a dull thud with each blast hitting against the backboard..."

#     ton "*Mmmm*, looks like you enjoyed our little lesson as well..." ("base", "base", "base", "mid")
#     gen "Ugh... can you blame me? That was... Ugh..." ("base", xpos="far_left", ypos="head")
#     ton "I told you I knew how to kiss..." ("base", "base", "base", "mid")
#     gen "I believe you... that'll be all for now..." ("base", xpos="far_left", ypos="head")
#     gen "I need to clean up..." ("base", xpos="far_left", ypos="head")
#     ton "Very well... Thank you, sir." ("base", "base", "base", "mid")

#     call ton_walk(action="leave")
#     jump end_tonks_event

# label tonks_teacher_event_3_6: #Level 3 Event 2
#     #Spends afternoon making out with ravenclaw, topless

#     return

# label tonks_teacher_event_3_7: #Level 3 Event 3
#     #Tonks has two best friends make out while she plays with herself

#     return

# label tonks_teacher_event_3_8: #Level 3 Event 4
#     #Another make out sesh with slytherin involving tonks fingering the student

#     call ton_walk(action="leave")
#     jump end_tonks_event
