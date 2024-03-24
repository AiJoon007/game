

label hg_tutor_start:

    # Tier 1
    if states.her.ev.tutoring.stage == 1:
        jump hg_tutor_E1
    elif states.her.ev.tutoring.stage == 2:
        jump hg_tutor_E2
    elif states.her.ev.tutoring.stage == 3:
        jump hg_tutor_E3

    # Tier 2
    elif states.her.ev.tutoring.stage == 4 and states.her.tier >= 2:
        jump hg_tutor_E4
    elif states.her.ev.tutoring.stage == 5 and states.her.tier >= 2:
        jump hg_tutor_E5

    # Tier 3
    elif states.her.ev.tutoring.stage == 6 and states.her.tier >= 3:
        jump hg_tutor_E6
    elif states.her.ev.tutoring.stage == 7 and states.her.tier >= 3:
        jump hg_tutor_E7

    # Tier 4
    elif states.her.ev.tutoring.stage == 8 and states.her.tier >= 4:
        if adult_mag_ITEM.owned >= 1: # Adult magazines
            jump hg_tutor_E8
        else:
            gen "I need to buy adult magazines for this lesson." ("base", xpos="far_left", ypos="head")
    elif states.her.ev.tutoring.stage == 9 and states.her.tier >= 4:
        if porn_mag_ITEM.owned >= 1: # Porn magazines
            jump hg_tutor_E9
        else:
            gen "I need to buy porn magazines for this lesson." ("base", xpos="far_left", ypos="head")

    # Tier 5
    elif states.her.ev.tutoring.stage == 10 and states.her.tier >= 5:
        if vibrator_ITEM.owned >= 1: # Vibrator
            jump hg_tutor_E10
        else:
            gen "I need to buy a vibrator for this lesson." ("base", xpos="far_left", ypos="head")
    elif states.her.ev.tutoring.stage == 11 and states.her.tier >= 5:
        if anal_plugs_ITEM.owned >= 1: # Anal plugs
            jump hg_tutor_E11
        else:
            gen "I need to buy anal plugs for this lesson." ("base", xpos="far_left", ypos="head")

    # Tier 6
    elif states.her.ev.tutoring.stage == 12 and states.her.tier >= 6:
        jump hg_tutor_E12
    elif states.her.ev.tutoring.stage == 13 and states.her.tier >= 6:
        jump hg_tutor_E13
    elif states.her.ev.tutoring.stage == 14 and states.her.tier >= 6 and states.her.status.sex and states.her.status.anal:
        jump hg_tutor_E14
    elif states.her.ev.tutoring.stage == 15:
        gen "(I have taught her everything there was to teach.)" ("base", xpos="far_left", ypos="head")
    else:
        gen "(She's not ready for her next lesson yet.)" ("base", xpos="far_left", ypos="head")
        gen "(I should ask her for some favours first.)" ("base", xpos="far_left", ypos="head")

    jump hermione_requests

label hg_tutor_E1:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    her "[name_genie_hermione], I'm very thankful that you're doing this for me." ("open", "base", "base", "mid")
    gen "Doing what?" ("base", xpos="far_left", ypos="head")
    her "My tutoring lessons..." ("soft", "squint", "base", "mid")
    her "I hope you're still planning to lecture me, [name_genie_hermione]?" ("annoyed", "base", "base", "mid")
    gen "Oh, I'll give you a lecture for sure." ("grin", xpos="far_left", ypos="head")
    her "Shall I go and fetch my books, then?" ("open", "squint", "base", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    her "My Books, [name_genie_hermione]. I need to study them more for my tests." ("soft", "base", "base", "R")
    her "All the knowledge I need is in those books!" ("annoyed", "narrow", "angry", "R")
    gen "Books can't teach you everything, girl... Some knowledge only comes with practice and experience!" ("base", xpos="far_left", ypos="head")
    gen "(I'm really just going to make this shit up as I go, ain't I?)" ("base", xpos="far_left", ypos="head")

    her "Maybe... I mean, as the head of Hogwarts you probably know best." ("annoyed", "squint", "base", "mid")
    gen "Sometimes you seem to forget that, Miss Granger." ("base", xpos="far_left", ypos="head")
    her "That sounded like something professor Snape would say..." ("open", "squint", "base", "mid")
    her "........." ("annoyed", "squint", "base", "mid")
    her "Sorry about that, he thinks he's always right and it annoys me." ("smile", "happyCl", "base", "mid")
    gen "..........." ("base", xpos="far_left", ypos="head")
    her "Sir?" ("soft", "base", "base", "R")
    gen "We're going to have to do it my way." ("base", xpos="far_left", ypos="head")

    $ d_flag_01 = False
    $ d_flag_02 = False

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "-No books-":
            $ d_flag_01 = True

            gen "Rule number one, no books allowed past this door." ("base", xpos="far_left", ypos="head")
            her "Too bad, I love books." ("annoyed", "narrow", "worried", "down")
            gen "{size=-4}And soon you'll love cock!{/size}" ("grin", xpos="far_left", ypos="head")
            her "Yes?" ("soft", "base", "base", "mid", trans=d5)
            gen "I didn't say anything..." ("base", xpos="far_left", ypos="head")
            her "If you say so, [name_genie_hermione]." ("open", "base", "base", "R")
        "-No back talk-":
            $ d_flag_02 = True

            gen "First rule, no back talk." ("base", xpos="far_left", ypos="head")
            her "Of course, sir!" ("base", "squint", "base", "mid")
            gen "Good." ("base", xpos="far_left", ypos="head")

    gen "Now it's time we talk about your future, child." ("base", xpos="far_left", ypos="head")
    her "I'm not a child anymore, professor!" ("normal", "squint", "angry", "mid")

    if d_flag_01:
        gen "You know what, let's add a second rule--" ("base", xpos="far_left", ypos="head")
        gen "No back talk!" ("angry", xpos="far_left", ypos="head")
        her "B-but...--" ("open", "happy", "worried", "mid")

    gen "What did I just say?" ("base", xpos="far_left", ypos="head")
    her "S-sorry..." ("annoyed", "squint", "worried", "R")

    if d_flag_02:
        gen "Let's add a second rule on top of the first one--" ("base", xpos="far_left", ypos="head")
        gen "No{w=0.3} more{w=0.3} books!" ("angry", xpos="far_left", ypos="head")
        gen "They're an obsolete and inferior medium anyway, you don't need them." ("base", xpos="far_left", ypos="head")
        her "(Too bad, I love books...)" ("annoyed", "narrow", "worried", "down")

    gen "Continuing--" ("base", xpos="far_left", ypos="head")
    gen "I can tutor you, but you need to understand certain things about magic." ("base", xpos="far_left", ypos="head")
    gen "With proper training, you can learn to increase your magic ability." ("base", xpos="far_left", ypos="head")
    her "Yes?" ("soft", "base", "base", "mid")
    gen "Certain emotions like love, and hate, pleasure, and pain..." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(If she falls for that, I'm a true genius!){/size}" ("grin", xpos="far_left", ypos="head")
    her "I've been studying magic for years and I've never heard of such a thing." ("normal", "base", "base", "mid")
    gen "{size=-2}(Shit.){/size}" ("angry", xpos="far_left", ypos="head")
    gen "And that's exactly why you're just an amateur. You still have much to learn about magic." ("base", xpos="far_left", ypos="head")
    her "Please stop that, professor. I'm not an amateur!" ("open", "squint", "worried", "mid")
    gen "Yes, maybe not empirically but..." ("base", xpos="far_left", ypos="head")
    her "Empirically?!" ("annoyed", "base", "base", "mid")
    gen "Enough of this. You came to me asking for my help, and if it starts like this--" ("angry", xpos="far_left", ypos="head")
    her "Yes, I suppose you are right..." ("angry", "base", "worried", "mid")
    her "Alright, I'm ready to study hard with you!" ("base", "base", "base", "mid")
    gen "{size=-2}Yes, we will study hard-on going forward!{/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Huh?" ("open", "narrow", "annoyed", "mid")
    her @ cheeks blush "" ("normal", "narrow", "annoyed", "mid")
    gen "What did I say about back talk?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "..........." ("annoyed", "narrow", "annoyed", "R")
    gen "You learn quick, that's good." ("base", xpos="far_left", ypos="head")
    gen "Alright, I want you to take some time and think about what we've discussed. I'll let you know when we can start with the first lesson." ("base", xpos="far_left", ypos="head")
    her "Can't we start now?" ("open", "base", "base", "mid")
    gen "Miss Granger, you're not the only student I must take care of." ("base", xpos="far_left", ypos="head")
    her "You're tutoring someone else?" ("open", "wide", "base", "mid")
    gen "{size=-2}(If only...){/size}" ("base", xpos="far_left", ypos="head")
    gen "I must take care of all the students of this school." ("base", xpos="far_left", ypos="head")
    gen "But yes, there is another girl who needs..." ("base", xpos="far_left", ypos="head")
    her "A Slytherin girl?!" ("shock", "wide", "base", "mid_soft")
    gen "That is none of your business, miss Granger." ("grin", xpos="far_left", ypos="head")
    her "Yes, professor. I'm sorry, but with all the recent events I'm a little on edge, and I would feel better if--" ("angry", "base", "angry", "mid")
    gen "Apology accepted, and now goodnight!" ("base", xpos="far_left", ypos="head")
    her "but--..." ("annoyed", "base", "angry", "L")
    gen "That's enough. Other students tutoring sessions are confidential." ("base", xpos="far_left", ypos="head")
    her "Well, when you put it that way..." ("soft", "base", "angry", "R")
    her "Anyway." ("normal", "closed", "base", "mid")
    her "Good night, professor, and thanks again for taking some of your precious time to help me." ("base", "base", "base", "mid")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(I'm glad the professor agreed to tutor me!){/size}" ("base", "happyCl", "worried", "mid", xpos="base", ypos="head", flip=False, trans=d3)
    her "{size=-4}(But pleasure and pain? I don't understand where this is going...){/size}" ("annoyed", "base", "base", "R")
    her "{size=-4}(And what other students is he tutoring?){/size}" ("annoyed", "base", "worried", "L")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 2
    jump end_hermione_event

label hg_tutor_E2:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Miss Granger, time for your first lesson." ("base", xpos="far_left", ypos="head")
    her "Yes, professor." ("soft", "base", "base", "R")
    gen "Have you thought about what we discussed?" ("base", xpos="far_left", ypos="head")
    her "Not really, I'm not sure what you meant by increasing magic ability through \"emotions\"." ("normal", "base", "base", "mid")
    gen "{size=-2}(You'll learn soon enough, girl.){/size}" ("grin", xpos="far_left", ypos="head")
    gen "For example, what was your state of mind when you heard those rumours about the Slytherin girls?" ("base", xpos="far_left", ypos="head")
    her "Please don't bring that up, sir! it really makes me mad!" ("clench", "base", "worried", "stare")
    gen "And what is this feeling?" ("base", xpos="far_left", ypos="head")
    her "...{w=0.5}an emotion, I suppose..." ("normal", "base", "base", "mid")
    gen "Yes, and don't you have emotions you prefer over others?" ("base", xpos="far_left", ypos="head")
    her "When I have the best score on a test." ("smile", "happyCl", "base", "mid")
    gen "{size=-2}(This girl is a monomaniac...){/size}" ("base", xpos="far_left", ypos="head")
    gen "Don't you have other passions, things you like to do?" ("base", xpos="far_left", ypos="head")
    her "Yes! Studying and reading books." ("smile", "happyCl", "base", "mid")
    gen "{size=-2}(By all the ancient gods...){/size}" ("angry", xpos="far_left", ypos="head")
    gen "Things are not going in the right direction..." ("base", xpos="far_left", ypos="head")
    her "And what direction is that, sir?" ("normal", "base", "base", "mid")
    gen "{size=-2}(You impaled on my cock!){/size}" ("grin", xpos="far_left", ypos="head")
    gen "Knowledge, Miss Granger, knowledge..." ("base", xpos="far_left", ypos="head")
    her "I am by far the most knowledgeable of my peers, professor. What more can you ask?" ("open", "closed", "base", "mid")
    gen "......{w=0.5}Miss Granger, did we not discuss this already? You need to accept you still have much to learn." ("base", xpos="far_left", ypos="head")
    gen "I'm tired of repeating myself, let's finish it for tonight." ("base", xpos="far_left", ypos="head")
    her "What? So soon?" ("open", "narrow", "annoyed", "mid")
    gen "There are other students requiring my attention, you're not the only one." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Don't tell me you're planning on tutoring one of those harlots from Slytherin, professor?" ("normal", "narrow", "annoyed", "mid")
    gen "Maybe, maybe not, that's none of your concern." ("base", xpos="far_left", ypos="head")
    her "But...{w=0.5} that's so wrong..." ("open", "base", "base", "mid")
    gen "One must make sacrifices to achieve greatness..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But--" ("open", "base", "worried", "mid")
    gen "If you want to progress and to restore the Gryffindor pride, you must!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I guess you're right. I'll do my best, professor." ("base", "base", "worried", "mid")
    gen "{size=-2}(She is so naive, it's adorable.){/size}" ("grin", xpos="far_left", ypos="head")
    gen "Good, now time to go to bed, my apprentice." ("base", xpos="far_left", ypos="head")
    her "{size=-2}(*Tsh*... Like I'm going to bed at this time, I need to study more.){/size}" ("normal", "squint", "angry", "mid")
    her "Of course! Goodnight, [name_genie_hermione]." ("base", "happyCl", "base", "mid")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(Filthy whores...){/size}" ("angry", "closed", "angry", "mid", xpos="far_right", ypos="head", flip=True, trans=d3)
    her @ cheeks blush "{size=-4}(Oh, I should not talk like that...{w=0.5} but it feels good to let my emotions out!){/size}" ("base", "happyCl", "worried", "mid")
    her @ cheeks blush "{size=-4}(Maybe professor is onto something, after all...){/size}" ("soft", "base", "base", "R")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 3
    jump end_hermione_event

label hg_tutor_E3:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So, have you thought about emotions and their usefulness in the practice of magic?" ("base", xpos="far_left", ypos="head")
    her "Yes, first I tried to cast a spell while thinking of the behaviour of those Slytherin girls." ("open", "closed", "base", "mid")
    her "It made me so angry and confused that I lost my focus and failed miserably." ("annoyed", "base", "base", "mid")
    her "I don't think it helps at all." ("annoyed", "squint", "base", "mid")
    gen "That's your problem Miss Granger, you think you already know the answer and don't follow my instructions." ("base", xpos="far_left", ypos="head")
    gen "I don't care about the behaviour of those girls." ("base", xpos="far_left", ypos="head")
    her "........." ("annoyed", "narrow", "annoyed", "up")
    her "Sorry about that, {w=0.5}again." ("open", "squint", "base", "mid")
    gen "I need you to focus on what those girls do with professors, not their behaviour in general." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But..." ("open", "base", "base", "mid")
    gen "Last time you were talking about your sacred duty and at the first hurdle you hesitate." ("base", xpos="far_left", ypos="head")
    her "{size=-2}(\"Sacred\"? Don't exaggerate, old man){/size}" ("annoyed", "narrow", "worried", "down")
    her @ cheeks blush "{size=-2}(Or not! Maybe I'll be remembered later for being the saviour of the Gryffindor house!){/size}" ("open", "happyCl", "worried", "mid")
    her "Yes, you're right! It {b}is{/b} my sacred duty!" ("smile", "base", "base", "R")
    gen "{size=-2}(It works every time, it's too easy... She looks so proud of herself.){/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "I'll do my best, professor!" ("open", "base", "base", "mid")
    gen "I'm excited too... uh, I'm sure you will." ("grin", xpos="far_left", ypos="head")
    her "I'm glad you have such high confidence in me." ("grin", "happyCl", "worried", "mid")
    gen "And I'm glad you're starting to believe in this. I think you have the potential to master this branch of magic." ("base", xpos="far_left", ypos="head")
    her "You seem tired, professor." ("open", "squint", "base", "mid")
    gen "{size=-2}(Tired of waiting to annihilate your ass.){/size}" ("angry", xpos="far_left", ypos="head")
    her "Yes, professor?" ("annoyed", "base", "base", "mid")
    gen "Yes we can!" ("grin", xpos="far_left", ypos="head")
    gen "Uh, I mean, I'm sure I'll tire you out soon enough, Miss Granger. How about you get some sleep?" ("base", xpos="far_left", ypos="head")
    her "Sleep? I must study first." ("open", "closed", "base", "mid")
    gen "I wasn't thinking about that, but you're right, time to go to bed!" ("base", xpos="far_left", ypos="head")
    gen "Just make sure to think about what you learned today." ("base", xpos="far_left", ypos="head")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(*Hmm*... I wonder what he {b}was{/b} thinking about.){/size}" ("base", "narrow", "base", "down", xpos="far_right", ypos="head", flip=True, trans=d3)
    her @ cheeks blush "{size=-4}(Probably all the problems caused by those harlots.){/size}" ("base", "narrow", "base", "mid_soft")
    her @ cheeks blush "{size=-4}(Well, I will never be like them, so no need to worry.){/size}" ("silly", "narrow", "base", "mid_soft")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 4
    jump end_hermione_event

label hg_tutor_E4:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    her "Sir, I want to apologise for doubting you." ("open", "base", "base", "mid")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    her "Your \"atypical\" method works!" ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "{size=-2}(Impossible!){/size}" ("base", xpos="far_left", ypos="head")
    gen "It works? I mean, yes, naturally it works!" ("base", xpos="far_left", ypos="head")
    gen "I'm glad you've succeeded. Now tell me more." ("base", xpos="far_left", ypos="head")
    her "I managed to levitate a heavy rock while thinking about the behaviour of two girls I saw earlier in the library." ("open", "closed", "base", "mid")
    her @ cheeks blush "Usually I only manage to move small rocks. I don't know, I felt kind of warm inside thinking about that." ("mad", "base", "angry", "mid")
    her "It felt weird but... {w=0.5}good at the same time."
    gen "{size=-2}(She is so ignorant of life! Unbelievable.){/size}" ("base", xpos="far_left", ypos="head")
    gen "You've never felt such a sensation before?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Generally I get angry and rush to stop such behaviour." ("clench", "base", "worried", "mid")
    her @ cheeks blush "But yesterday, I don't know, I just watched without interrupting them." ("open", "happyCl", "worried", "mid")
    her @ cheeks blush "And when I pictured it, as you told me to, it worked." ("open", "base", "base", "mid")
    her @ cheeks blush "I feel at the same level as those harlots, I'm so ashamed." ("angry", "base", "angry", "mid")
    gen "But you succeeded." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(To my surprise...){/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes! With this method I'll have better grades in my tests and win the House Cup for Gryffindor!" ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "{size=-2}(In your dreams.){/size}" ("grin", xpos="far_left", ypos="head")
    gen "Good, good. Now I want to know more about those two girls." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It's not very relevant, professor. And I'm not sure this is appropriate." ("annoyed", "narrow", "angry", "R")
    gen "How will you improve yourself if I can't guide you?" ("base", xpos="far_left", ypos="head")
    gen "And for that, I must know more." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Alright, but it's embarrassing." ("annoyed", "narrow", "angry", "R")
    gen "{size=-2}(Ooh, I hope they were naked!){/size}" ("grin", xpos="far_left", ypos="head")
    her "I went to the library to study interactions between plants..." ("open", "closed", "base", "mid")
    gen "{size=-2}(Yeah, yeah, come on...){/size}" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "... and I heard muffled sounds." ("base", "base", "base", "R")
    her @ cheeks blush "I was hoping to catch a teacher doing bad things with one of those Slytherin whores." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "I slowly headed towards the sounds and I discovered two girls in an alcove." ("open", "base", "base", "mid")
    her @ cheeks blush "I remained hidden to observe them." ("grin", "wink", "base", "mid")
    gen "{size=-2}(Come on!){/size}" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, professor?" ("base", "narrow", "base", "up")
    gen "Yes, no, please continue." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "They were kissing passionately." ("open", "happyCl", "worried", "mid")
    gen "And? And?" ("grin", xpos="far_left", ypos="head")
    her "And a moment later they began to..." ("open", "closed", "base", "mid")
    her @ cheeks blush "They began to..." ("open", "happyCl", "worried", "mid")
    her @ cheeks blush "They began to touch their breasts!" ("scream", "wide", "base", "stare")
    gen "They were naked, I hope?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What?" ("open", "happy", "base", "mid")
    her "No, fortunately they were dressed."
    her @ cheeks blush "How can such a thing happen in our beloved school!" ("angry", "base", "angry", "mid")
    gen "But you kept watching, didn't you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Only for educational purposes." ("annoyed", "narrow", "angry", "R")
    gen "{size=-2}(\"Educational purposes\"... ha-ha, I've never heard a worse excuse!){/size}" ("grin", xpos="far_left", ypos="head")
    gen "And during all this time you didn't feel a certain need?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "To my shame, yes. Like I said before, I felt kind of warm inside." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "Like when I have to pee but... different. Better." ("disgust", "narrow", "base", "down")
    gen "This good sensation... next time you experience it, let it come." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But..." ("open", "base", "base", "mid")
    gen "It's the only way to get better, Miss Granger." ("base", xpos="far_left", ypos="head")
    gen "If you suppress it, it won't work." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Ok...{w=0.3} I'll try my best." ("annoyed", "narrow", "angry", "R")
    her "But to be honest, sir, I thought you were going to punish those two sluts."
    gen "Can you provide proof of their crime? No?" ("base", xpos="far_left", ypos="head")
    gen "Even I can't punish students without proof of any wrongdoing." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(With the possible exception of you!){/size}" ("angry", xpos="far_left", ypos="head")
    gen "Anyway, you've done well. I think it will be enough for this lesson." ("base", xpos="far_left", ypos="head")
    gen "Remember what I've told you, and good night!" ("base", xpos="far_left", ypos="head")
    her "Good night, professor." ("base", "base", "base", "mid")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(Well, I'll try to investigate those two girls again.){/size}" ("disgust", "narrow", "base", "down", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(Like a real anthropologist!){/size}" ("base", "narrow", "base", "mid_soft")
    her @ cheeks blush "{size=-4}(Yes, that's right. Hermione the anthropologist!){/size}" ("base", "happyCl", "worried", "mid")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 5

    if states.her.level < 9:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E5:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So, any luck with your \"studies\"?" ("base", xpos="far_left", ypos="head")
    her "Yes! When you hear the results of my hunt, you'll be proud of me!" ("base", "happyCl", "base", "mid")
    gen "{size=-2}(\"Hunt?\"){/size}" ("base", xpos="far_left", ypos="head")
    gen "Your \"hunt,\" Miss Granger?" ("base", xpos="far_left", ypos="head")
    her "Yes, professor!" ("smile", "happyCl", "base", "mid")
    her @ cheeks blush "Like an explorer in the wild jungle, I tracked those two filthy animals." ("base", "narrow", "worried", "mid_soft")
    her @ cheeks blush "With success, sir!" ("smile", "happyCl", "base", "mid", emote="happy")
    her "Hogwarts has so many dark and discreet corners..." ("annoyed", "base", "base", "mid")
    her "Believe me, it wasn't easy, professor." ("base", "narrow", "worried", "mid_soft")
    gen "I'm sure you gave it your best." ("base", xpos="far_left", ypos="head")
    gen "But right now I await your report." ("base", xpos="far_left", ypos="head")
    her "Yes, but before that I want to clarify that my report is purely for scientific purposes." ("soft", "base", "base", "R")
    gen "{size=-2}(Sure...){/size}" ("base", xpos="far_left", ypos="head")
    her "So I tracked down those two harlots to an area in the attic." ("open", "closed", "base", "mid")
    her "Which, by the way, seems to be the meeting place for girls of this... sort." ("annoyed", "squint", "base", "mid")
    gen "And what is your opinion on them?" ("base", xpos="far_left", ypos="head")
    her "At least they don't sleep with professors in exchange for house points." ("open", "squint", "base", "mid")
    her "" ("annoyed", "squint", "base", "mid")
    gen "And that's it?" ("base", xpos="far_left", ypos="head")
    gen "No \"this behaviour must be severely punished\"?" ("base", xpos="far_left", ypos="head")
    gen "Are you attracted to girls of this sort, Miss Granger?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What? I'm not a-- I mean no, Sir." ("open", "base", "worried", "mid")
    gen "Alright, alright, back to your report, if you please." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-2}(I'm not a lesbian...{w=0.3} I think...){/size}" ("disgust", "narrow", "base", "down")
    her @ cheeks blush "{size=-2}(Hermione, pull yourself together! You're not a harlot!){/size}" ("mad", "happyCl", "worried", "mid")
    her @ cheeks blush "No, I'm not!" ("annoyed", "narrow", "worried", "down")
    gen "Excuse me?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Uh... Yes, my report. My {b}scientific{/b} report." ("open", "base", "base", "mid")
    gen "{size=-2}(Yeah, we get it...){/size}" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "So, like before, they started by kissing passionately." ("open", "happyCl", "worried", "mid")
    her @ cheeks blush "With the tongue and everything!" ("open", "base", "base", "R")

    menu:
        "-Start jerking off-":
            $ states.gen.masturbating = True
            hide hermione_main
            hide screen blktone
            nar "You reach under the desk and grab your cock..."
            call gen_chibi("jerk_off_behind_desk")
            with d3
            call ctc

        "-Just listen-":
            $ states.gen.masturbating = False
            pass

    her @ cheeks blush "" ("open", "base", "base", "mid")
    gen "And? And?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "They pulled up their shirts and caressed each other's breasts." ("open", "happyCl", "worried", "mid")
    her @ cheeks blush "{size=-2}(Their beautiful and tempting breasts...){/size}" ("open", "narrow", "base", "up")
    her @ cheeks blush "Later those nasty girls raised their skirts and started to touch each other \"there\" while kissing." ("silly", "narrow", "base", "up")
    her @ cheeks blush tears sweat "{size=-2}(I can't believe I said that!){/size}" ("base", "narrow", "base", "up")
    her @ cheeks blush "They were very excited, and I could see their panties become wet." ("open", "narrow", "base", "up")
    her @ cheeks blush "Disgusting." ("annoyed", "narrow", "base", "up")
    if states.gen.masturbating:
        gen "{size=-2}(Yes... yes...){/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "One of the girls went crazy and inserted her fingers into the other's \"thing,\" and worked them furiously." ("silly", "base", "worried", "mid")
    her @ cheeks blush "Soon imitated by her girlfriend." ("base", "narrow", "angry", "mid")
    her @ cheeks blush "Those whores came so hard I'm sure they heard the screams on the other side of the grounds!" ("soft", "narrow", "base", "mid")

    if states.gen.masturbating:
        her @ cheeks blush "{size=-2}(And I had to bite my lip, or else they would've heard me too...){/size}" ("clench", "narrow", "base", "down")
        hide hermione_main
        with d3

        call cum_block

        gen "Yes! That's the stuff!" ("angry", xpos="far_left", ypos="head")
        hide screen bld1
        with d1
        call gen_chibi("cum_behind_desk")
        call cum_block
        call ctc

        call gen_chibi("cum_behind_desk_done")
        with d3

        if states.her.status.voyer:
            her @ cheeks blush "Professor!" ("angry", "base", "angry", "mid")
            gen "You enjoyed it too, so don't act all innocent." ("base", xpos="far_left", ypos="head")
            gen "Anyway, I hope it was revealing." ("base", xpos="far_left", ypos="head")

            $ states.her.mood += 7
        else:
            her @ cheeks blush "Professor?" ("annoyed", "base", "base", "mid")
            gen "Ah, Yes... I hope it was revealing." ("base", xpos="far_left", ypos="head")

    else:
        gen "You enjoyed it too." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Maybe..." ("annoyed", "narrow", "angry", "R")
        gen "Anyway, I hope it was revealing." ("base", xpos="far_left", ypos="head")

    her "\"Revealing?\" I'm not sure what you mean by that." ("open", "squint", "base", "mid")
    her "You're the headmaster, act as such!" ("open", "base", "base", "mid")
    her "Do all you can to stop those acts of debauchery!"
    her "" ("annoyed", "narrow", "angry", "R")
    gen "Yes, of course." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(Hypocrite...){/size}" ("base", xpos="far_left", ypos="head")
    gen "You said that those girls became wet." ("base", xpos="far_left", ypos="head")
    gen "Weren't you a little too?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "When I went to bed I noticed it, yes." ("disgust", "narrow", "base", "down")
    her @ cheeks blush "Apparently bad fluids are released from your body when you have faced such acts." ("mad", "wide", "base", "stare")
    gen "No, they aren't bad. It happens when you're excited." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft_blink "No way! I can control myself!" ("scream", "happyCl", "worried", "mid")
    her @ cheeks blush "" ("angry", "base", "angry", "mid")
    gen "No one can control their base desires." ("base", xpos="far_left", ypos="head")
    gen "Consider this well, and enjoy your night, Miss Granger." ("base", xpos="far_left", ypos="head")
    her "Good night, professor." ("annoyed", "base", "worried", "R")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(I enjoyed it too much. Maybe I'm becoming a pervert as well){/size}" ("base", "narrow", "base", "up", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(I lost control, it won't happen again!){/size}" ("shock", "narrow", "base", "down")
    her @ cheeks blush "{size=-4}(Good thing I'm not a degenerate like those filthy girls!){/size}" ("base", "narrow", "base", "mid_soft")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 6

    if states.her.level < 9:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E6:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Bravo, last time you experienced your first \"emotion\"." ("base", xpos="far_left", ypos="head")
    her "Yes, I remember. But I still don't see the link with magic." ("open", "squint", "base", "mid")
    gen "{size=-2}(Me neither...){/size}" ("base", xpos="far_left", ypos="head")
    gen "If you want to progress, you have to go a little further than a simple observation." ("base", xpos="far_left", ypos="head")
    gen "You'll need to participate." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What! No way I'll participate in such debauchery!" ("scream", "closed", "base", "mid")
    her "How can you even suggest such a thing!" ("angry", "base", "angry", "mid")
    gen "Oh you don't have to go that far in one go." ("base", xpos="far_left", ypos="head")
    her "I'm not sure I want to go there at all." ("open", "closed", "base", "mid")
    gen "How many times do I have to remind you why you're doing this?" ("base", xpos="far_left", ypos="head")
    her "Yes but..." ("open", "base", "base", "mid")
    gen "But what?" ("base", xpos="far_left", ypos="head")
    her "A girl like me shouldn't stoop to such practices." ("annoyed", "squint", "base", "mid")
    gen "A girl like you should use all means at their disposal in order to excel." ("base", xpos="far_left", ypos="head")
    her "..........."
    her @ cheeks blush "Alright, but this must remain between us." ("annoyed", "narrow", "angry", "R")
    her "You cannot disclose this to other professors, especially professor Snape!" ("annoyed", "narrow", "worried", "down")
    gen "Oh, I have no intention of sharing alright." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(You're mine.){/size}" ("grin", xpos="far_left", ypos="head")
    gen "Speaking of you with professor Snape." ("base", xpos="far_left", ypos="head")
    her "Well, what must I do now?" ("open", "closed", "base", "mid")
    gen "Come here." ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_front")
    call hide_blkfade
    call ctc

    call bld
    gen "Have you ever touched yourself?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Professor!" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base")
    call her_chibi_scene("grope_ass_front")
    with d7

    nar "You touch her leg with your hands."
    gen "Please answer the question, Miss Granger. Have you ever touched yourself?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "No, it's... it's wrong!" ("annoyed", "narrow", "angry", "R")
    gen "But when you looked at these girls, you felt certain emotions." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes... and?" ("annoyed", "base", "base", "mid")
    gen "You didn't feel the need to touch yourself?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes... but I resisted." ("soft", "narrow", "base", "up")
    nar "You start to caress her thigh."
    her @ cheeks blush "Professor..." ("open", "happyCl", "worried", "mid")
    gen "And you felt those emotions without even touching yourself." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes..." ("open", "base", "base", "mid")
    gen "{size=-2}(What a slut!){/size}" ("grin", xpos="far_left", ypos="head")
    if hermione.is_worn("panties"):
        nar "You move forward to her panties."
    else:
        nar "You move forward to her pussy."
    her @ cheeks blush "" ("open", "happyCl", "worried", "mid")
    gen "Good." ("base", xpos="far_left", ypos="head")

    call her_chibi_scene("behind_desk_front")
    with d3

    nar "You stop caressing her."
    her @ cheeks blush "Why... why did you stop?" ("mad", "wide", "base", "stare")
    gen "Oh, because I need you to think about all this before we meet again." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But..." ("mad", "wide", "base", "stare")
    gen "Good night, my dear." ("base", xpos="far_left", ypos="head")
    her "Good night, professor." ("annoyed", "base", "worried", "R")

    hide hermione_main
    call blkfade

    "You dismiss Hermione."

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    hide screen bld1
    call hide_blkfade

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(This is wrong...){/size}" ("disgust", "narrow", "base", "down", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(I shouldn't listen to him.){/size}" ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "{size=-4}(And yet...){/size}" ("base", "narrow", "base", "down")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 7

    if states.her.level < 12:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E7:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So, have you started practising my teachings?" ("base", xpos="far_left", ypos="head")
    her "I don't even know where to start." ("open", "squint", "base", "mid")
    gen "You see, the secret is to stimulate appropriate areas." ("base", xpos="far_left", ypos="head")
    gen "Areas which are more sensitive than others." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You mean my intimate areas, sir?!" ("annoyed", "narrow", "angry", "R")
    gen "Well, they're called intimate for a reason." ("base", xpos="far_left", ypos="head")
    gen "You said you've never touched yourself because it was wrong." ("base", xpos="far_left", ypos="head")
    gen "But it's never wrong to exercise ones body in order to reach a new level of consciousness." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(The things I have to make up...){/size}" ("angry", xpos="far_left", ypos="head")
    gen "You can begin with your breasts, for example." ("base", xpos="far_left", ypos="head")
    gen "But you shouldn't only caress your nipples but also grab your tits and squeeze them." ("base", xpos="far_left", ypos="head")
    gen "And in the meanwhile, you can think of those two girls." ("base", xpos="far_left", ypos="head")
    gen "Or what you want to do with those girls." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "What makes you think... No, I don't want..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    her @ cheeks blush "I definitely don't want to have {b}anything{/b} to do with those harlots!" ("scream", "happyCl", "worried", "mid")
    gen "Don't lie to yourself. It's obvious that you feel a form of attraction to those two girls." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I...{w=0.3} I honestly don't know what to think anymore." ("mad", "base", "angry", "mid")
    her "At the moment my feelings are so confusing..."
    gen "{size=-2}(Exactly what I was hoping!){/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "I'm happy to earn points for my house and at the same time I feel so ashamed." ("angry", "squint", "base", "mid")
    her "And the same goes for your lessons."
    gen "Yet you can't deny your progress in the practice of magic." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Yes...{w=0.2} perhaps you're right." ("base", "narrow", "worried", "mid_soft")
    gen "You have to let it go, Miss Granger, follow your instincts!" ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(Grab my cock and wank it savagely!){/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "I'm not sure if..." ("open", "narrow", "worried", "mid_soft")
    gen "Enough procrastination, time for practice!" ("base", xpos="far_left", ypos="head")
    gen "Come here." ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    nar "Hermione walks towards your desk."
    nar "You grab her tits and massage them softly."
    pause .5

    call her_chibi_scene("grope_tits")
    with d1
    hide screen blkfade
    her @ cheeks blush "" ("open", "happyCl", "worried", "mid", xpos="mid", ypos="base")
    call ctc

    call bld
    gen "Like I said, it's important you learn how to properly stimulate your \"emotional\" body areas." ("base", xpos="far_left", ypos="head")
    gen "It's not enough if I do it myself, you need to practise when you're alone." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "" ("upset", "happyCl", "worried", "mid")
    gen "Like in your bed or in the shower, for example." ("base", xpos="far_left", ypos="head")
    nar "You keep massaging her tits..."
    her @ cheeks blush "" ("open", "happyCl", "worried", "mid")
    nar "You feel her nipples becoming hard."
    her @ cheeks blush "Yes but...{w=0.3} Professor, it's inappropriate for a girl of good education!" ("open", "base", "base", "mid")
    gen "Don't let old prejudices weigh you down. You're a girl with great potential." ("base", xpos="far_left", ypos="head")
    nar "You gently squeeze her nipples through the fabric."
    her @ cheeks blush "*Ah*... thank you Professor." ("open", "narrow", "base", "up")
    gen "A girl with a brilliant mind." ("base", xpos="far_left", ypos="head")
    nar "You increase your grip on her nipples."
    gen "A girl who will become a woman of exception." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Ahh* yes... I'm already a woman of exception!" ("grin", "base", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    nar "You firmly pinch her nipples."
    her @ cheeks blush tears soft "*Ahhh* {heart} not so hard..." ("silly", "happyCl", "worried", "mid")

    hide hermione_main
    call blkfade
    nar "You abruptly stop."
    pause .5
    her @ cheeks blush "*Hmph*...{w=0.3} Why did you stop, [name_genie_hermione]?" ("clench", "base", "worried", "mid", emote="angry", ypos="head", flip=False, trans=d3)
    gen "Lesson is over. Time to practise by yourself." ("base", xpos="far_left", ypos="head")

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    hide screen blkfade

    her @ cheeks blush "..........." ("annoyed", "narrow", "worried", "R", xpos="mid", ypos="base", trans=fade)
    gen "Good night, my little witch." ("base", xpos="far_left", ypos="head")
    her "Good night, professor, and thank you for this lesson." ("base", "happyCl", "base", "mid")
    her @ cheeks blush "{size=-2}(I just wish it had lasted longer...){/size}" ("annoyed", "squint", "base", "mid")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(\"My little witch?\"){/size}" ("annoyed", "narrow", "angry", "R", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(Why not, after all...){/size}" ("base", "narrow", "base", "up")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 8

    if states.her.level < 12:
        $ states.her.level += 1

    jump end_hermione_event


label hg_tutor_E8:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So, Miss Granger, have you practised my teachings?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes...{w=0.2} a little." ("annoyed", "narrow", "angry", "R")
    gen "And?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It feels even better when I'm naked." ("smile", "happyCl", "base", "mid", emote="happy")
    her @ cheeks blush "{size=-2}(Oh no, I shouldn't have said that...){/size}" ("mad", "wide", "base", "stare")
    gen "Well come here and undress, we'll practise." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Completely?!" ("annoyed", "base", "worried", "mid")
    gen "No, only the top will suffice." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(For the moment...){/size}" ("grin", xpos="far_left", ypos="head")
    her "I'll be showing you my breasts without even earning any points?" ("open", "squint", "base", "mid")
    gen "You can't have both points and lessons." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Okay..." ("angry", "happyCl", "worried", "mid", emote="sweat")

    $ hermione.strip("robe", "accessory")
    call her_chibi("lift_top")

    call set_her_action("lift_top")

    $ hermione.strip("top")
    pause .5

    her @ cheeks blush "Like that?" ("annoyed", "narrow", "angry", "R")

    if hermione.is_worn("bra"):
        gen "Without your bra Miss Granger..." ("base", xpos="far_left", ypos="head")
        pause .5
        $ hermione.strip("bra")
        pause .5

    gen "Yes, and now come here." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "........" ("annoyed", "closed", "base", "mid")
    her "" ("base", "closed", "base", "mid")
    gen "Now." ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    nar "Hermione slowly walks towards your desk."
    nar "She tries not to bounce her tits without much success..."
    call her_chibi_scene("behind_desk_show_tits")
    with d1

    hide screen blkfade
    her "" ("base", "closed", "base", "mid", xpos="mid", ypos="base")
    call ctc

    call bld
    gen "Now let's get serious if you want to." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(Well, even if you don't...){/size}" ("grin", xpos="far_left", ypos="head")

    hide hermione_main
    call blkfade

    nar "You grab her tits and squeeze them gently."

    call her_chibi_scene("grope_tits")
    call hide_blkfade
    call ctc

    her @ cheeks blush "Professor, what are you doing?" ("disgust", "narrow", "base", "down")
    gen "Teaching you, dear, teaching you." ("grin", xpos="far_left", ypos="head")
    gen "Doesn't it feel good?" ("base", xpos="far_left", ypos="head")
    her "A little..." ("base", "closed", "base", "mid")
    gen "Your hard nipples say the contrary." ("base", xpos="far_left", ypos="head")
    gen "I can stop if you want." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yeah sure!" ("grin", "base", "angry", "mid")
    her @ cheeks blush "Suck them professor." ("silly", "narrow", "base", "up")
    gen "As you wish, princess." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "" ("silly", "narrow", "base", "up")
    nar "You suck her nipples with devotion."
    her @ cheeks blush tears sweat "Yes {heart} like that." ("silly", "narrow", "base", "up")
    nar "You start to chew on her nipples."
    her @ cheeks blush "*Ahh*, no... Don't." ("open_tongue", "narrow", "base", "up")
    nar "You chew on them even harder."
    her @ cheeks blush "Not that hard, I will..." ("open_wide_tongue", "narrow", "base", "up")
    gen "{size=-2}(Time for the grand finale!){/size}" ("grin", xpos="far_left", ypos="head")

    if hermione.is_worn("panties"):
        nar "You quickly slip your hand into her panties and rub her pussy furiously."
    else:
        nar "You quickly move your hand toward her pussy and rub it furiously."

    her @ cheeks blush tears crying "Yes! {heart}" ("angry", "narrow", "base", "dead")
    her "I... I..."
    gen "Came, my dear." ("grin", xpos="far_left", ypos="head")

    hide hermione_main
    call blkfade
    call ctc

    call set_her_action("none","update")

    call her_chibi_scene("behind_desk_front")
    call hide_blkfade

    her @ cheeks blush tears mascara "Is the lesson over professor?" ("grin", "narrow", "base", "mid_soft")
    gen "Not if you don't want it to be." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "Maybe it's enough for tonight." ("open", "narrow", "base", "mid_soft")
    her @ cheeks blush tears mascara "After all, you have a lot of work to do." ("soft", "narrow", "worried", "mid_soft")
    gen "Sure." ("base", xpos="far_left", ypos="head")
    gen "But before that I have a little present for you." ("base", xpos="far_left", ypos="head")

    call give_gift("You give an assortment of adult magazines to Hermione.",adult_mag_ITEM)

    gen "I hope this will help you in your studies." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "Yes, certainly." ("base", "closed", "base", "mid")
    her @ cheeks blush tears mascara "Thank you and good night professor." ("base", "narrow", "base", "mid")

    hide hermione_main
    call blkfade

    "You dismiss Hermione."
    $ hermione.wear("all")

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(I'm such a slut...){/size}" ("base", "narrow", "base", "up", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(Cumming in front of my professor...){/size}" ("base", "narrow", "base", "down")
    her @ cheeks blush "{size=-4}(I definitely need to do that again!){/size}" ("base", "narrow", "base", "mid_soft")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 9

    if states.her.level < 18:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E9:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So tell me, were your readings enlightening?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I'm not sure if \"readings\" is the right term but yes. Very \"stimulating\" too." ("angry", "happyCl", "worried", "mid")
    gen "Maybe it's time to discover new areas to stimulate." ("base", xpos="far_left", ypos="head")
    her "You mean my pussy, right?" ("open", "squint", "base", "mid")
    her "I'm not an idiot, professor." ("annoyed", "narrow", "angry", "R")
    gen "If it doesn't suit you, we can stop here." ("base", xpos="far_left", ypos="head")
    her "And if I said stop?" ("annoyed", "squint", "base", "mid")
    gen ".........." ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "*Ha-ha*, you should have seen your face!" ("smile", "base", "angry", "mid")
    her "With all your recent lessons you can imagine that this area isn't a \"no man's land\" anymore." ("smile", "base", "base", "R")
    gen "Have you slept..." ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "No I haven't! I'm not a harlot who offers her pussy to every boy around." ("scream", "closed", "base", "mid")
    gen "{size=-2}(Good, your pussy is mine alone!){/size}" ("base", xpos="far_left", ypos="head")
    her "" ("annoyed", "narrow", "annoyed", "up")
    gen "{size=-2}(Although I may agree to share it with other girls...){/size}" ("grin", xpos="far_left", ypos="head")
    gen "I'm happy you're behaving honourably, Miss Granger." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Ha, who'd have guessed!" ("annoyed", "narrow", "angry", "R")
    gen "Yes, I'm glad that my favourite student is not wasting her precious time with boys." ("base", xpos="far_left", ypos="head")
    her "Sure...{w=0.3} {size=-4}old hypocrite{/size}."
    gen "Enough of this! Now take off your shirt and come here." ("base", xpos="far_left", ypos="head")
    her "Here we go for another \"lesson\"." ("open", "squint", "base", "mid")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")

    if hermione.is_worn("bra"):
        her "..." (ypos="head", flip=False, trans=d3)
        gen "And your bra..." ("base", xpos="far_left", ypos="head")

        $ hermione.strip("bra")

    her @ cheeks blush "........" ("annoyed", "closed", "base", "mid", ypos="head", flip=False, trans=d3)

    call her_chibi_scene("behind_desk_front")
    call hide_blkfade
    call ctc

    her @ cheeks blush "And free tits again, enjoy!" ("grin", "base", "angry", "mid", xpos="mid", ypos="base")
    gen "I definitely intend to." ("base", xpos="far_left", ypos="head")
    gen "Now take off your skirt." ("grin", xpos="far_left", ypos="head")
    pause .8

    call set_her_action("lift_skirt")
    pause .5

    $ hermione.strip("bottom")
    call set_her_action("None")
    pause .5

    her @ cheeks blush "" ("base", "base", "base", "R")
    call ctc

    if hermione.is_worn("panties"):
        her @ cheeks blush "You love my pussy don't you?" ("base", "narrow", "base", "up")
        gen "Oh yes, I love your smell, especially when you're wet." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Professor..." ("angry", "happyCl", "worried", "mid", emote="sweat")
        call her_chibi_scene("grope_ass_front")
        with d3
        nar "You caress her clit."
        her @ cheeks blush "Professor!" ("mad", "wide", "base", "stare")
    else:
        her @ cheeks blush "You love my panties don't you?" ("base", "narrow", "base", "up")
        gen "Oh yes, I love their smell, especially when you're wet." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Professor..." ("angry", "happyCl", "worried", "mid", emote="sweat")
        call her_chibi_scene("grope_ass_front")
        with d3
        nar "You caress her clit through the fabric."
        her @ cheeks blush "Professor!" ("mad", "wide", "base", "stare")
        gen "Now take them off." ("base", xpos="far_left", ypos="head")

        $ hermione.strip("panties")
        call set_her_action("pinch")

        nar "She slowly lowers her panties."

        call set_her_action("None")

        call her_chibi_scene("behind_desk_front")
        her "" ("base", "closed", "base", "mid")
        call ctc

    gen "What's great, you see, is that I have two hands." ("base", xpos="far_left", ypos="head")
    gen "One can caress your clit while the other can play with your pussy." ("base", xpos="far_left", ypos="head")
    nar "You move from words to deeds and penetrate her already wet pussy with ease."

    call her_chibi_scene("grope_ass_front")
    with d3

    her @ cheeks blush "Yes, you're probably right." ("grin", "base", "angry", "mid")
    gen "Probably?!" ("base", xpos="far_left", ypos="head")
    nar "While you're moving your finger in her pussy, you take over her clit with your thumb."
    her @ cheeks blush "*Haa* {heart} I'm only your humble student, I wouldn't know such naughty things." ("silly", "narrow", "base", "up")
    gen "One finger is rarely enough even with a tight pussy like yours." ("base", xpos="far_left", ypos="head")
    nar "You insert a second finger in her tight and warm pussy..."
    her @ cheeks blush "Yesss {heart} I'll try to remember your teachings." ("silly", "narrow", "base", "up")
    nar "You increase the pace and feel her pussy tighten on your fingers."
    gen "Maybe a third finger?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Don't be so bold." ("grin", "base", "angry", "mid")
    nar "Her whole body starts shaking as you increase your ramming."

    call her_chibi_scene("grope_ass_front_fast")
    with d3

    her @ cheeks blush "Noo {heart}{w=0.2} not so fast I will..." ("open_tongue", "narrow", "base", "up")
    nar "You increase your pace even more."
    her @ cheeks blush "I will I will..." ("open_wide_tongue", "narrow", "base", "up")
    gen "Time to get serious." ("grin", xpos="far_left", ypos="head")
    nar "You force your soaked thumb into her butthole."
    her @ cheeks blush "*Haaaaa* {heart} yesss! {heart}" ("open_wide_tongue", "narrow", "base", "up")
    gen "Lucky girl." ("grin", xpos="far_left", ypos="head")

    call blkfade

    hide hermione_main
    call her_chibi_scene("behind_desk_front")
    call hide_blkfade

    her @ cheeks blush tears mascara "I'm sure this lesson will be of great help tonight." ("grin", "narrow", "base", "mid_soft")
    her @ cheeks blush tears soft "And the other nights. {heart}" ("silly", "base", "worried", "mid")
    gen "Always glad to help my little witch in her studies." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "\"Studies,\" yes, that's right." ("grin", "narrow", "base", "mid_soft")
    gen "And to aid your studies I have even more scientific materials." ("base", xpos="far_left", ypos="head")

    call give_gift("You give an assortment of porn magazines to Hermione.",porn_mag_ITEM)

    her @ cheeks blush tears mascara "I promise to study them every night until I commit their lessons to memory!" ("grin", "closed", "base", "mid")
    her @ cheeks blush tears mascara "Thank you and good night, professor." ("grin", "narrow", "base", "mid_soft")
    gen "Good night, my favourite little witch." ("base", xpos="far_left", ypos="head")

    hide hermione_main
    call blkfade

    "You dismiss Hermione."
    $ hermione.wear("all")

    call her_chibi("stand","desk","base")
    call gen_chibi("sit_behind_desk")
    call hide_blkfade

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(Favourite...){/size}" ("base", "narrow", "base", "up", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(*Hmm*... Could there be another one?){/size}" ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "{size=-4}(I better do my best to remain his favourite!){/size}" ("base", "happyCl", "worried", "mid")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 10

    if states.her.level < 18:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E10:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Miss Granger, have you had an enjoyable night?" ("base", xpos="far_left", ypos="head")
    her "You shouldn't ask such things, Professor." ("open", "closed", "base", "mid")
    gen "I have to make sure my students have a pleasant nights rest." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "With your teachings and your \"scientific\" literature, indeed." ("base", "narrow", "worried", "mid_soft")
    her @ cheeks blush "I'll become proficient in human anatomy with all this documentation." ("angry", "happyCl", "worried", "mid")
    gen "Do you need some scientific instruments for your research?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "They could come in handy." ("grin", "wink", "base", "mid")
    her @ cheeks blush "As long as it's not your dick." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "{size=-2}(Not that I don't appreciate it but no points no cock!){/size}" ("smile", "base", "angry", "mid")
    gen "Miss Granger! This is a serious matter!" ("base", xpos="far_left", ypos="head")
    her "Sure..." ("annoyed", "squint", "base", "mid")
    gen ".........." ("base", xpos="far_left", ypos="head")
    her "So what's my gift this time?" ("open", "squint", "base", "mid")

    call give_gift("You give the vibrator to Hermione",vibrator_ITEM)

    her "And I suppose you want me to test this in front of you?" ("open", "closed", "base", "mid")
    gen "Of course." ("grin", xpos="far_left", ypos="head")
    her "Where is the educational purpose in all of this?" ("annoyed", "squint", "base", "mid")
    gen "Good question. Improving your skills?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "At what? Magic?" ("mad", "base", "angry", "mid")
    gen "Certainly." ("base", xpos="far_left", ypos="head")
    her "........."
    her @ cheeks blush "I have one request though." ("open", "base", "base", "R")
    her @ cheeks blush "If I'm going to masturbate I don't want to be the only one. So enjoy the free show." ("open", "happyCl", "worried", "mid")
    gen "With pleasure!" ("grin", xpos="far_left", ypos="head")
    nar "You reach under the desk and grab your cock."

    hide hermione_main
    call blkfade

    call gen_chibi("jerk_off_behind_desk")
    with d3

    call hide_blkfade

    her "{size=-2}(Thinking of the headmaster masturbating makes me wet already {heart}){/size}" (xpos="mid", ypos="base")
    her @ cheeks blush "{size=-2}(I've become such a whore. Not that I don't enjoy it...){/size}" ("smile", "base", "angry", "mid")
    her @ cheeks blush "So... where do we start?" ("open", "happy", "base", "mid")

    if hermione.is_worn("bra"):
        gen "Take off your shirt and bra, I want to see your tits." ("base", xpos="far_left", ypos="head")
        pause .5

        call set_her_action("lift_top")
        pause .5

        $ hermione.strip("robe", "accessory")
        $ hermione.strip("top")
        $ hermione.strip("bra")
        call set_her_action("None")
        pause .5

    else:
        gen "Take off your shirt, I want to see your tits." ("base", xpos="far_left", ypos="head")
        pause .5

        call set_her_action("lift_top")
        pause .5

        $ hermione.strip("robe", "accessory")
        $ hermione.strip("top")
        call set_her_action("None")
        pause .5

    her "You love them don't you?"
    gen "Oh yes..." ("grin", xpos="far_left", ypos="head")
    her "Having watched the other girls I now know why."
    her "Those breasts are so tempting."
    her @ cheeks blush "Big or small, I want to hold them in my hands and suck the nipples." ("open_tongue", "narrow", "base", "up")
    gen "Me too, me too!" ("grin", xpos="far_left", ypos="head")
    gen "Now remove your skirt!" ("base", xpos="far_left", ypos="head")
    pause .5

    call set_her_action("lift_skirt")
    pause .5

    $ hermione.strip("bottom")
    call set_her_action("None")
    pause .5

    call ctc

    her "Good idea."
    her @ cheeks blush "Sometimes I wish I could do this with others girls." ("open", "happy", "base", "mid")
    her @ cheeks blush "Masturbate naked in front of each other." ("open", "narrow", "base", "up")
    if hermione.is_worn("panties"):
        gen "Yes go on, take off your panties!" ("grin", xpos="far_left", ypos="head")
        her "Your wish is my command."
        pause .5

        call set_her_action("pinch")
        pause .5

        $ hermione.strip("panties")
        call set_her_action("None")
        pause .5

        $ u_tears_pic = "characters/hermione/face/e_her_tears_02b.webp"
        call ctc

        her @ cheeks blush "And mine is to touch another girl's pussy." ("silly", "narrow", "base", "up")
    else:
        her @ cheeks blush "Touch her pussy like I'm touching mine now." ("silly", "narrow", "base", "up")

    if hermione.is_any_worn("clothes"):
        gen "Get rid off the rest of your silly attire." ("base", xpos="far_left", ypos="head")
        $ hermione.strip("clothes")

    ### Milestone ###
    $ states.her.status.masturbating = True

    $ hermione.set_pose("hand_on_pussy")
    pause .5

    her @ cheeks blush "Caress it." ("open_tongue", "narrow", "base", "up")

    call set_her_action("fingering")
    pause .2

    her @ cheeks blush "Insert my fingers into her wet pussy." ("open_tongue", "narrow", "base", "up")
    gen "Yes, yes! Now the vibrator!" ("angry", xpos="far_left", ypos="head")


    ## TODO: show vibrator pose
    $ hermione.set_pose("hand_on_pussy_and_breast")

    hide screen blkfade
    call ctc

    her @ cheeks blush "Oh I had forgotten about it already." ("open_tongue", "narrow", "base", "up")
    her @ cheeks blush "I want to hear her moan as I work my fingers." ("open_wide_tongue", "narrow", "base", "up")
    her "Hear her cum!"
    her @ cheeks blush "Like me! *Aaah* yesssss! {heart} {heart}" ("open_wide_tongue", "narrow", "base", "up")
    call ctc

    gen "*Ahh*! You little whore!!!" ("angry", xpos="far_left", ypos="head")
    call gen_chibi("cum_behind_desk")
    her "The vibrator... *Aaah* I'm still cumming!!"
    gen "Take this!" ("angry", xpos="far_left", ypos="head")

    hide hermione_main
    call blkfade

    nar "Hermione catches her breath and puts her clothes back on."

    # Reset pose
    $ hermione.set_pose(None)
    $ hermione.wear("all")

    call her_chibi("stand","desk","base")
    call gen_chibi("cum_behind_desk_done")
    hide screen blkfade

    her @ cheeks blush tears mascara "I hope you enjoyed it as much I did." ("open", "narrow", "worried", "mid_soft", xpos="mid", ypos="base", trans=fade)
    gen "Oh fuck yes, you're doing great, my little witch!" ("base", xpos="far_left", ypos="head")
    gen "Very good!" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "Thank you, professor." ("grin", "narrow", "worried", "mid_soft")
    gen "After all this, you need to rest." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "Oh yes. Good night professor." ("grin", "closed", "base", "mid")
    gen "Good night, my dirty little slut." ("base", xpos="far_left", ypos="head")

    call her_walk("door", "base")

    her @ cheeks blush tears mascara "{size=-4}(Rest...){/size}" ("base", "narrow", "base", "down", ypos="head", flip=False, trans=d3)
    her @ cheeks blush tears mascara "{size=-4}(Not before I've played with this marvellous toy again){/size}" ("base", "narrow", "base", "mid_soft")
    her @ cheeks blush tears mascara "{size=-4}(And again){/size}" ("silly", "narrow", "base", "mid_soft")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 11

    if states.her.level < 21:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E11:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "So... I hope my lessons are paying off." ("base", xpos="far_left", ypos="head")
    her "You mean, by making me more \"open\" to the wonders of adulthood?" ("open", "squint", "base", "mid")
    gen "Among other things..." ("base", xpos="far_left", ypos="head")
    her "That's what I thought." ("annoyed", "squint", "base", "mid")
    her "But to be honest, I was looking forward to this lesson." ("open", "closed", "base", "mid")
    her "{size=-2}(Maybe, I shouldn't have said that){/size}" ("angry", "wide", "base", "stare")
    her @ cheeks blush "{size=-2}(He's gonna ravage me on his desk, isn't he?){/size}" ("angry", "happyCl", "worried", "stare")
    #her @ cheeks blush "{size=-2}(Not that I would mind...){/size}" ("angry", "happyCl", "worried", "mid")
    #her "{size=-2}(And I could ask him for points afterwards...){/size}" ("smile", "base", "base", "R")
    gen "Miss Granger? Are you alright?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes professor! Sorry, I was thinking of my next exam." ("grin", "wink", "base", "mid")
    gen "Oh, I'm sure it's an important one. Maybe next lesson I can help you revise." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I would love that!" ("open", "happyCl", "worried", "mid")
    gen "So, anal stimulation..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Ah! I knew you would say that." ("smile", "base", "angry", "mid")
    her "{size=-2}(Once again, not that I mind...){/size}"
    her @ cheeks blush "{size=-2}(I'm such a whore, even the Slytherin girls can't compete...){/size}" ("base", "narrow", "base", "up")
    gen "Come again, Miss Granger?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "In this school nobody can compete with me, right professor?" ("smile", "happyCl", "base", "mid", emote="happy")
    her @ cheeks blush "In any field!" ("smile", "base", "angry", "mid")
    gen "In any field? I'm not sure." ("base", xpos="far_left", ypos="head")
    gen "You still have things to learn..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What?! What are we waiting for then?" ("scream", "closed", "base", "mid")
    her @ cheeks blush "" ("normal", "narrow", "angry", "mid")

    call set_her_action("lift_top")
    pause .2

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")
    pause .5
    $ hermione.strip("bra")
    call ctc
    call set_her_action("None")

    nar "She rips off her shirt and rushes to your desk."

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("grope_ass_back")
    call hide_blkfade
    call ctc

    call bld
    gen "We haven't even started yet and you're already wet, my adorable slut." ("base", xpos="far_left", ypos="head")

    show screen blktone
    her @ cheeks blush "It's you and your dirty talk!" ("annoyed", "narrow", "angry", "R", xpos="mid", ypos="base")
    her "Talking about anal insertions, asshole licking and... and..."
    her @ cheeks blush "Fisting!" ("open", "narrow", "base", "up")
    gen "I never mentioned any of that." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh. You didn't?" ("annoyed", "narrow", "base", "up")
    her @ cheeks blush "Well maybe you didn't but you {b}were{/b} thinking about it!" ("base", "narrow", "base", "up")
    gen "Maybe." ("grin", xpos="far_left", ypos="head")
    gen "Your ass is so luscious I could eat it." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "My point exactly!" ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush tears soft "Enough talking, old man. Get to work!" ("base", "narrow", "worried", "mid_soft")
    gen "I haven't even given you your gift yet!" ("base", xpos="far_left", ypos="head")
    gen "I'll just put it where you'll be sure to find it." ("base", xpos="far_left", ypos="head")
    gen "So, can we start the lesson?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes for Merlin's sake!" ("open", "base", "base", "mid")
    gen "But before that..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "If you say another word I swear I will go back to my dorm right now!" ("scream", "base", "angry", "mid", emote="angry")
    nar "You suddenly insert the anal plug."
    her @ cheeks blush "Yesss {heart} like that!" ("silly", "narrow", "base", "up")
    nar "You remove it just as quickly while giving her butt a loud slap."

    play sound "sounds/plop.ogg"
    with flashbulb
    play sound "sounds/slap.ogg"
    with hpunch

    her @ cheeks blush "Yessss more! {heart}" ("open_tongue", "narrow", "base", "up")
    gen "As you wish, princess." ("grin", xpos="far_left", ypos="head")
    nar "You promptly insert and remove it."

    play sound "sounds/plop.ogg"
    pause .1
    play sound "sounds/slap.ogg"
    with hpunch

    her @ cheeks blush "More!!" ("open_tongue", "narrow", "base", "up")

    play sound "sounds/plop.ogg"
    pause .1
    play sound "sounds/slap.ogg"
    with hpunch

    $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.webp"
    her @ cheeks blush "*Aaaah* {heart}" ("open_wide_tongue", "narrow", "base", "up")

    play sound "sounds/plop.ogg"
    pause .1
    play sound "sounds/slap.ogg"
    with hpunch

    gen "You can touch yourself too, you know." ("base", xpos="far_left", ypos="head")
    $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.webp"
    her @ cheeks blush "I can't." ("open_wide_tongue", "narrow", "base", "up")
    her "{size=-2}(If I do, I will lose what little dignity I have left){/size}"
    her @ cheeks blush "{size=-2}(But tonight...){/size}" ("open_wide_tongue", "narrow", "base", "up")
    gen "I'll handle it then." ("base", xpos="far_left", ypos="head")
    nar "You finger both her butthole and her pussy."
    her @ cheeks blush "Nooo it's too much! {heart}" ("open_wide_tongue", "narrow", "base", "up")
    gen "Faster? No problem!" ("grin", xpos="far_left", ypos="head")
    call her_chibi_scene("grope_ass_back_fast")
    her @ cheeks blush tears crying "*Aaah* You're killing me! {heart}" ("angry", "narrow", "base", "dead")
    her @ cheeks blush tears soft "{size=-2}(And I love it){/size}" ("silly", "base", "worried", "mid")
    gen "More fingers?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "No more pleassse." ("open", "narrow", "worried", "mid_soft")
    gen "Actually, it wasn't a question." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears crying "If you keep this pace I will..." ("angry", "narrow", "base", "dead")
    nar "You feel her muscles tighten on your fingers."
    her @ cheeks blush "Come!!" ("open_wide_tongue", "narrow", "base", "up")
    gen "Good girl." ("grin", xpos="far_left", ypos="head")
    her "Keep it up, I..."
    her @ cheeks blush "Yessss... {heart}" ("open_wide_tongue", "narrow", "base", "up")
    gen "I can keep this up as long as you please." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Nooooo {heart} I will die!" ("open_wide_tongue", "narrow", "base", "up")
    gen "In ecstasy." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "*Aahh* not again {heart}" ("open_wide_tongue", "narrow", "base", "up")
    hide hermione_main
    hide screen bld1
    hide screen blktone
    with d3

    call her_chibi_scene("behind_desk_back")
    with d3
    pause .5

    call bld
    gen "I think you've had enough for one night." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes I... I better go." ("open_tongue", "narrow", "base", "up")
    gen "You forgot your gift." ("base", xpos="far_left", ypos="head")
    nar "You promptly insert the butt plug."
    with hpunch
    her @ cheeks blush "*Aaaaaaah*" ("open_wide_tongue", "narrow", "base", "up")

    hide hermione_main
    with d3
    call her_chibi_scene("lie_on_desk", trans=d5)
    pause .5

    show screen bld1
    nar "She collapses panting on the desk."
    gen "Best view in the world." ("grin", xpos="far_left", ypos="head")
    pause .8

    call blkfade
    nar "After a while, she puts her shirt back on."

    $ hermione.wear("all")

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    hide screen blkfade

    her @ tears mascara "Thank you for everything, professor." ("soft", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    her @ cheeks blush tears mascara "It was very...{w=0.5} enlightening." ("grin", "narrow", "worried", "mid_soft")
    her @ cheeks blush tears mascara "But please, try to go easy on me next time." ("grin", "closed", "base", "mid")
    gen "I have absolutely no idea what you mean by that." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "Good night professor." ("grin", "narrow", "base", "mid_soft")
    gen "Good night, my dear anal whore." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears mascara "Professor..." ("open", "narrow", "worried", "mid_soft")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(Finally tonight I'll just go to bed.){/size}" ("base", "happyCl", "worried", "mid", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(That was a little too intense...){/size}" ("angry", "happyCl", "worried", "mid")
    her @ cheeks blush "{size=-4}(Not that I'm complaining...){/size}" ("silly", "narrow", "base", "mid_soft")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 12

    if states.her.level < 21:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E12:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], I have something for you." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Another gift for me?" ("base", "narrow", "base", "up")
    her @ cheeks blush "Please, please." ("open", "happyCl", "worried", "mid")
    gen "You weren't this excited last time when I gave you a present..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh don't worry, it was just a moment of weakness." ("smile", "base", "angry", "mid")
    her "I'm ready now!"
    her "{size=-2}(My body perhaps not...){/size}" ("annoyed", "narrow", "worried", "down")
    gen "Did you have fun with your anal plug?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Y-yes... I wear it sometimes..." ("base", "narrow", "base", "up")
    her @ cheeks blush "But I cut the tail!" ("annoyed", "narrow", "angry", "R")
    her "{size=-2}(No way I could walk around like that...){/size}"
    gen "And you like it?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "It's very...{w=0.5} stimulating. It helps me whenever I cast a spell." ("base", "narrow", "worried", "mid_soft")
    gen "Tell me the truth Miss Granger, you wear it all the time, don't you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Nooo..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "Maybe..." ("open_tongue", "narrow", "base", "up")
    her "........"
    gen "Don't be ashamed, it's alright my little whore." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I wear it all the time and...{w=0.3} I love it!" ("smile", "happyCl", "base", "mid", emote="happy")
    gen "{size=-2}(Marvellous){/size}" ("grin", xpos="far_left", ypos="head")
    gen "I've taught you good." ("base", xpos="far_left", ypos="head")
    her "To be a slut? Yes you have..." ("open", "closed", "base", "mid")
    her "And now I want more, so where is my gift?!" ("annoyed", "squint", "base", "mid")
    gen "There, there." ("base", xpos="far_left", ypos="head")

    call give_gift("You give the anal beads to Hermione",anal_beads_ITEM)

    her @ cheeks blush "Oh! That's even better than a butt plug." ("shock", "wide", "base", "stare")
    gen "And they can be useful for your pussy too." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "So many possibilities..." ("smile", "base", "angry", "mid")
    her "... so little time."
    her "I suppose you want me to try them out?" ("smile", "happyCl", "base", "mid")
    her "Or would you rather try them out on me yourself?"
    gen "Oh yes." ("grin", xpos="far_left", ypos="head")
    her "I don't even know why I'm asking..." ("annoyed", "narrow", "annoyed", "up")
    her @ cheeks blush "{size=-2}(Old pervert...){/size}" ("open", "happyCl", "worried", "mid")

    call set_her_action("lift_top")
    pause .5

    $ hermione.strip("robe", "accessory")
    $ hermione.strip("top")
    with d3
    pause .5
    $ hermione.strip("bra")
    with d3
    pause .5

    her @ cheeks blush "My tits are the best in all of Hogwarts!" ("silly", "narrow", "base", "up")
    gen "Have you been with many girls to say that?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I wish..." ("grin", "narrow", "base", "up")
    gen "I can tutor you on that too." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Maybe we should finish this lesson first." ("base", "narrow", "base", "up")
    gen "Oh, we have time." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Speaking of that..." ("base", "narrow", "worried", "mid_soft")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    call her_chibi_scene("behind_desk_back")
    with d1
    call hide_blkfade
    call ctc

    call bld
    gen "As always, it's a delightful view." ("grin", xpos="far_left", ypos="head")
    call blktone
    her @ cheeks blush "I'm glad you love it." ("angry", "happyCl", "worried", "mid", xpos="mid", ypos="base")

    call set_her_action("lift_skirt")
    pause .5

    $ hermione.strip("bottom")
    $ hermione.strip("panties")
    call set_her_action("None")
    pause .5

    her @ cheeks blush "Can we start now?" ("grin", "base", "angry", "mid")
    gen "I suppose you want them in your ass?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Naturally." ("base", "narrow", "base", "up")
    her "{size=-2}(I'll try them in my pussy later tonight){/size}" ("base", "closed", "base", "mid")
    call her_chibi_scene("grope_ass_back")
    nar "You push the first bead in with ease."
    her "*Mmm*... {heart}"
    gen "How many do you think you can take, my dear?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "How many have you got?" ("base", "narrow", "base", "up")
    gen "That's the spirit!" ("grin", xpos="far_left", ypos="head")
    nar "You push another one inside with little resistance."
    her @ cheeks blush "Yess {heart} one more please." ("open", "narrow", "base", "up")
    nar "You feel the beads sink deeper when you push the third one inside."
    her @ cheeks blush "*Ohhh*, they're... they're moving {heart}." ("grin", "narrow", "base", "up")
    nar "The fourth takes some work before it pops in."
    her @ cheeks blush "*Ah*... {heart}*Ah*{heart}" ("silly", "narrow", "base", "up")
    nar "You push the last one forcefully inside."
    her @ cheeks blush "*Ahhhhh* {heart} delightful." ("open_tongue", "narrow", "base", "up")
    her "They're so deep in my ass... almost like your cock."
    gen "I can..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "No you can't! My butthole is too tight for both." ("annoyed", "closed", "base", "mid")
    her @ cheeks blush "{size=-2}(But it's such a good idea){/size}" ("grin", "narrow", "base", "up")
    gen "I'm sure there's still room for at least one finger." ("base", xpos="far_left", ypos="head")
    nar "You finger her butthole gently."
    her @ cheeks blush "*Ah*... {heart}{w=0.5} *Ah*... {heart}" ("silly", "narrow", "base", "up")
    her @ cheeks blush "W-What did I say..." ("grin", "narrow", "base", "up")
    nar "You wiggle the finger inside."
    her @ cheeks blush "You never listen, [name_genie_hermione]!" ("grin", "narrow", "base", "up")
    gen "What can I say, I just know what's best for you, my little witch." ("base", xpos="far_left", ypos="head")
    nar "You pick up the pace."
    her @ cheeks blush "Yesss! {heart}" ("grin", "narrow", "base", "up")
    gen "I thought you didn't want the finger?" ("base", xpos="far_left", ypos="head")
    gen "In that case, one more finger." ("grin", xpos="far_left", ypos="head")
    nar "She shivers when you insert a second finger."
    her @ cheeks blush "*Ahh*... No-- No more please." ("open_wide_tongue", "narrow", "worried", "up")
    her @ cheeks blush "My butthole is stretched so wide!" ("open", "narrow", "base", "up")
    gen "Your butthole is doing great." ("grin", xpos="far_left", ypos="head")
    nar "You finger her butthole fiercely."
    call her_chibi_scene("grope_ass_back_fast")
    her @ cheeks blush "Nooo... *Aahh* {heart}" ("clench", "narrow", "worried", "mid_soft")
    gen "Your pussy is getting neglected. We need to fix that!" ("base", xpos="far_left", ypos="head")
    nar "You start fingering her pussy with your other hand. She is panting heavily."
    her @ cheeks blush "*Ah*...{w=0.3} *Ah*... Just like that {heart}" ("open_wide_tongue", "narrow", "base", "up")
    nar "You suddenly pull out all the beads."
    her @ cheeks blush tears messy "*Ahhhhhh*!!" ("grin", "narrow", "base", "dead")
    nar "And insert four fingers in her ass."
    her @ cheeks blush "I'm cumming, [name_genie_hermione]... I cumming!" ("silly", "narrow", "base", "up")
    gen "If you must..." ("base", xpos="far_left", ypos="head")
    nar "You continue to work her ass while you finger her pussy."
    her "No don't I..."
    her @ cheeks blush tears soft "Cumm-- {heart} {heart}" ("silly", "base", "worried", "mid")
    her @ cheeks blush "Agaaain-- *Aaah* {heart}" ("open_wide_tongue", "narrow", "base", "up")
    gen "Sorry my little anal whore but I'm starting to get tired." ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "Don't you dare stop now!" ("scream", "base", "angry", "mid", trans=hpunch)
    her @ cheeks blush tears messy "Just a little more pleassse {heart}" ("grin", "narrow", "base", "dead")
    her @ cheeks blush tears messy "Because I will..." ("grin", "narrow", "base", "dead")
    her @ cheeks blush "Come again!!" ("open_wide_tongue", "narrow", "base", "up")
    hide hermione_main
    call blkfade

    nar "There's a small puddle on your desk from her juices. You slowly remove your fingers."

    call her_chibi_scene("lie_on_desk")
    call hide_blkfade
    pause .5

    her @ cheeks blush tears mascara "*Pant* *pant*" ("open", "narrow", "worried", "mid_soft")
    her @ cheeks blush tears mascara "I feel completely ravaged but happy." ("grin", "narrow", "base", "mid_soft")
    her @ cheeks blush tears mascara "Thank you professor, for letting me discover such great sensations." ("grin", "narrow", "base", "mid_soft")
    her @ cheeks blush tears mascara "But I'm exhausted so good night." ("grin", "closed", "base", "mid")
    hide hermione_main
    call blkfade

    nar "She puts her shirt back on and rushes to the door."

    $ hermione.wear("all")

    call her_chibi("stand","door","base",flip=True)
    call gen_chibi("sit_behind_desk")
    call hide_blkfade
    pause .5

    call bld
    gen "Come back here, girl." ("base", xpos="far_left", ypos="head")
    gen "I need your mouth, I can't hold it anymore." ("angry", xpos="far_left", ypos="head")
    pause .5

    call her_chibi("stand","door","base")
    pause .5

    her @ cheeks blush "Professor!" ("open", "happy", "base", "mid")
    her @ cheeks blush "........." ("base", "narrow", "base", "up")
    her @ cheeks blush "Can I have points for this?" ("mad", "wide", "base", "stare")
    gen "Now!" ("angry", xpos="far_left", ypos="head")
    hide hermione_main
    call blkfade

    nar "She comes back and does not seem particularly upset."

    call her_chibi_scene("bj")
    call hide_blkfade
    call ctc

    call bld
    her "*Slurp*! *Slurp*! *Gulp*!"
    gen "Yes, like that..." ("grin", xpos="far_left", ypos="head")
    nar "Hermione eagerly sucks your dick."
    gen "You seem to be in a hurry. Is it because you're not getting points for this?" ("base", xpos="far_left", ypos="head")
    gen "Consider it a payment for your private lessons." ("base", xpos="far_left", ypos="head")
    her "*Mmmh*..."
    gen "Next time, come with your robe and your robe only." ("base", xpos="far_left", ypos="head")
    nar "She briefly nods."
    her "*Slurp*! *Gulp*! *Slurp*!"
    gen "You're doing great my little whore, I will..." ("grin", xpos="far_left", ypos="head")
    gen "Yes!" ("angry", xpos="far_left", ypos="head")

    call cum_block
    call her_chibi_scene("bj_cum_in")
    hide screen bld1
    with d3

    her "*Gobble*! *Gobble*! *Gobble*!"
    call ctc

    gen "Good girl, you swallowed it all!" ("grin", xpos="far_left", ypos="head")
    call blkfade

    nar "She wipes her mouth."
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade
    call ctc

    her @ cheeks blush "Sir, I still think I deserve some..." ("annoyed", "narrow", "angry", "R")
    gen "Good night, my dear child." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "........." ("annoyed", "narrow", "base", "up")
    her @ cheeks blush "Good night, professor." ("annoyed", "closed", "base", "mid")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(Sucking his cock without getting any points!){/size}" ("annoyed", "narrow", "angry", "R", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(If he hadn't made me come so hard...){/size}" ("base", "narrow", "base", "up")
    her @ cheeks blush "{size=-4}(*sigh* Although I guess it's not that high a price...){/size}" ("base", "narrow", "base", "down")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 13

    if states.her.level < 24:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E13:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    ####################
    ### Robe Section ###
    ####################

    #her @ cheeks blush "Oh! I can't believe I forgot! Stay where you are, I'll be right back!" ("mad", "wide", "base", "stare")
    #hide hermione_main
    #play sound "sounds/door.ogg"
    #call blkfade

    #play sound "sounds/door.ogg"
    #pause .3

    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_2_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_2_s.webp"
    #call set_her_action("naked") #Removes all clothes.
    #$ hermione_wear_robe = True

    #call her_chibi("stand","door","base")
    #call hide_blkfade

    #call her_walk("mid", "base")

    #her @ cheeks blush "{size=-4}*panting*{/size} Oh good, you're still here." ("open", "base", "base", "mid", xpos="right", ypos="base")
    #gen "Is it safe to assume you have honoured my request this time?" ("base", xpos="far_left", ypos="head")
    #her @ cheeks blush "I thought it was obvious." ("open", "happy", "base", "mid")
    #her @ cheeks blush "I even had to hide in an alcove to avoid getting noticed on my way here!" ("open", "base", "base", "mid")
    #her @ cheeks blush "It was so embarrassing!" ("open", "happyCl", "worried", "mid")
    #her @ cheeks blush "{size=-2}(And exciting!){/size}" ("open", "happyCl", "worried", "mid")
    #gen "Are you sure you're not wearing anything underneath?" ("base", xpos="far_left", ypos="head")
    #nar "Hermione opens up her cloak a little."
    #pause .2

    #hide hermione_main
    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_s.webp"
    #her @ cheeks blush "" ("open", "happy", "base", "mid")
    #call ctc

    #her @ cheeks blush "Does this answer your question?" ("open", "happy", "base", "mid")
    #gen "Not really. It's hard to tell from this distance. I mean, it's so dark..." ("base", xpos="far_left", ypos="head")
    #her "..." ("annoyed", "narrow", "base", "up")
    #pause .2

    #hide hermione_main
    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_open_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_open_s.webp"
    #her @ cheeks blush "" ("base", "closed", "base", "mid", trans=d5)
    #call ctc

    #her @ cheeks blush "Is that better?" ("base", "narrow", "base", "mid_soft")
    #gen "Oh yes, definitely. Well done, my girl." ("grin", xpos="far_left", ypos="head")

    #hide hermione_main
    #if h_robe in gryffindor_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_g.webp"
    #elif h_robe in slytherin_robe_list:
    #    $ hermione_robe = "characters/hermione/clothes/robe/robe_3_s.webp"


    her @ cheeks blush "Alright then, can we start the lesson now?" ("smile", "base", "angry", "mid")
    gen "Maybe, I don't know... do you like butterbeer?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You know I do. What's that got to do with..." ("soft", "base", "base", "R")
    gen "......." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Do you mean...{w=0.3} no, no way professor!" ("scream", "wide", "base", "stare")
    gen "Oh, rest assured, we won't start with the bottom end." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Still, professor, this is so dirty..." ("silly", "narrow", "base", "up")
    her @ cheeks blush "{size=-2}(And exciting!){/size}" ("silly", "narrow", "base", "up")
    her @ cheeks blush "Moreover, my butthole isn't stretched enough." ("annoyed", "closed", "base", "mid")
    gen "Are you kidding me, with all your training!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "And what a training!" ("annoyed", "narrow", "base", "up")
    her @ cheeks blush "{size=-2}(Good thing I practised by myself, otherwise...){/size}" ("angry", "happyCl", "worried", "mid")
    gen "Now stop making up excuses!" ("angry", xpos="far_left", ypos="head")
    gen "I can see you rubbing your thighs from excitement!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I thought it was so dark in here..." ("open", "happy", "base", "mid")
    her "*Humm*...{w=0.3} Okay, but you better start out easy on me." ("annoyed", "squint", "base", "mid")
    gen "I'm always gentle with you, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")
    her "Yeah, obviously..." ("annoyed", "narrow", "annoyed", "up")
    gen "{size=-2}(It's not as if you don't like it rough){/size}" ("base", xpos="far_left", ypos="head")
    gen "Alright, my desk.{w=0.3} You{w=0.5}, naked{w=0.6}, now!" ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    play sound "sounds/08_hop_on_desk.ogg" #Sound of the desk squeaking.
    pause .5

    nar "Hermione slowly slides down her robe and climbs up your desk."

    $ hermione.strip("robe")

    call her_chibi("dance","on_desk","on_desk")
    # her "" (animation=bob)

    call hide_blkfade
    pause 1

    call blktone
    her "You're crazy for my body, aren't you?" (xpos="mid", ypos="base")
    gen "Why do you ask..." ("base", xpos="far_left", ypos="head")
    her "Because a girl likes to be complimented, professor!" ("annoyed", "squint", "base", "mid")
    her "Especially when she's about to do these kinds of things!" ("annoyed", "narrow", "annoyed", "up")
    gen "I meant, of course you have an amazing body! That's not up to question." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Best in the school?" ("base", "narrow", "base", "up")
    gen "......{w=0.3} Yeah, yeah, best in the school." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I can tell you're lying!" ("mad", "base", "angry", "mid")
    gen "Miss Granger, I've lived for a very long time and believe me, I have seen few women with a body like yours." ("base", xpos="far_left", ypos="head")
    gen "And definitely none in this school." ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(Severus still hasn't sent those Slytherin whores up){/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=-2}(I wonder if I can fire him for that...){/size}" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you, professor." ("open", "happyCl", "worried", "mid")
    her @ cheeks blush "Feel free to use my body as you please." ("angry", "happyCl", "worried", "mid")
    gen "{size=-2}(*sigh* women...){/size}" ("base", xpos="far_left", ypos="head")
    gen "Bend over the desk my dear little witch." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=-2}(It starts with my dear little witch and ends up with my dear anal whore...){/size}" ("annoyed", "narrow", "base", "up")
    her @ cheeks blush "{size=-2}(*sigh* men...){/size}" ("annoyed", "narrow", "base", "up")
    her @ cheeks blush "As you wish my dear {b}old{/b} headmaster." ("open", "happy", "base", "mid")
    gen "{size=-2}(If you knew how old I actually am...){/size}" ("base", xpos="far_left", ypos="head")
    her "" (animation=None)
    hide hermione_main
    call blkfade

    nar "Hermione languorously climbs down your desk and bends over it."

    call her_chibi_scene("lie_on_desk", trans=d5)

    her "I'm ready, [name_genie_hermione]." (ypos="head", flip=False, trans=d3)

    call give_gift("You take an empty butterbeer bottle, spit on the neck, and push it inside her butthole.",butterbeer_ITEM)

    call her_chibi_scene("lie_on_desk_fingering_slow")
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    call ctc

    her @ cheeks blush "*Mmm*... Yes... like that." ("base", "narrow", "base", "up", xpos="mid", ypos="base", flip=True)
    her @ cheeks blush "My pussy feels lonely without your care." ("grin", "wink", "base", "mid")
    nar "You start to finger her pussy too."
    gen "Poor little thing." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What's better in life than this professor?" ("open", "narrow", "base", "up")
    gen "Oh, I don't know." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you for letting me discover such pleasures." ("open", "happyCl", "worried", "mid")
    gen "{b}My{/b} pleasure." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "It's even better when it's mutual, isn't it?" ("open", "happy", "base", "mid")
    gen "*Hmm*... Yes you're right... I'm glad you feel that way." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Now a little deeper please." ("soft", "base", "base", "R")
    nar "You push the whole bottle neck up inside her asshole."
    her @ cheeks blush "*Ohhh* yesss! {heart}" ("open", "narrow", "base", "up")
    her @ cheeks blush "More, faster!" ("open", "narrow", "base", "up")
    call her_chibi_scene("lie_on_desk_fingering")
    nar "You rotate the bottle while going back and forth deeper and deeper."
    her @ cheeks blush "Yessss, don't forget my pussy. {heart}" ("grin", "narrow", "base", "up")
    gen "Oh, your pussy better be ready for what's coming!" ("grin", xpos="far_left", ypos="head")
    nar "You insert all four fingers in her sopping wet pussy."
    her @ cheeks blush tears mascara "Sweet Circe-- *Aah*... *Ah*, that's too much! {heart}" ("open", "narrow", "worried", "mid_soft")
    gen "Nothing is too much for my little whore." ("base", xpos="far_left", ypos="head")
    nar "You increase the pace of both hands."
    her @ cheeks blush tears messy "No, no, yes, yessss! {heart}" ("grin", "narrow", "base", "dead")
    nar "Most of the bottle is inside her now, leaving just enough to get a good grip."
    gen "Push the bottle, push it!" ("base", xpos="far_left", ypos="head")
    nar "Whenever she pushes it back you do the same in the other direction."
    her @ cheeks blush "This is, this is, *aaaah*!!! {heart}{heart}" ("open_wide_tongue", "narrow", "base", "up")
    nar "Her whole body convulses as she comes hard."
    hide hermione_main
    call blkfade

    call her_chibi_scene("lie_on_desk_fingering_pause")
    pause .3
    call hide_blkfade
    call ctc

    her @ cheeks blush tears messy "*Panting* *panting*" ("grin", "narrow", "base", "dead", ypos="head", flip=False, trans=d3)
    her @ cheeks blush tears soft "P-professor...{w=0.3} I'm so happy right now." ("base", "narrow", "worried", "mid_soft")
    gen "Glad to hear it." ("grin", xpos="far_left", ypos="head")
    hide hermione_main
    call blkfade

    nar "After a while, she makes herself somewhat presentable."

    #$ hermione_wear_robe = True

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade

    call bld
    gen "Sweet dreams my little princess." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You too, professor." ("open", "base", "base", "mid", xpos="mid", ypos="base", flip=False)
    gen "They are always sweet with you around." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you." ("base", "narrow", "base", "up")
    gen "And next time bring your books, I'll help you with your revisions." ("base", xpos="far_left", ypos="head")

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(Yes, sweet dreams...){/size}" ("base", "happyCl", "worried", "mid", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(Sweet and wet!){/size}" ("silly", "narrow", "base", "mid_soft")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 14

    if states.her.level < 24:
        $ states.her.level += 1

    jump end_hermione_event

label hg_tutor_E14:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    #her "I'll go get my books right away, sir!" ("soft", "base", "base", "R")
    #hide hermione_main
    #play sound "sounds/door.ogg"
    #call blkfade
    #pause 1

    #call set_her_action("hold_book")

    #play sound "sounds/door.ogg"
    #pause .3

    #call hide_blkfade
    #call ctc

    #her "Revisions are a serious matter, [name_genie_hermione]!" ("open", "base", "worried", "mid")
    #gen "{size=-2}(My cock in your ass is a serious matter...){/size}" ("base", xpos="far_left", ypos="head")
    #gen "In this regard, I kinda lied, it's more of a mock exam than revisions." ("base", xpos="far_left", ypos="head")
    #her @ cheeks blush "What a surprise!" ("annoyed", "narrow", "base", "up")

    gen "[name_hermione_genie], today I'd like to examine if you've been keeping up with your tutoring lessons..." ("base", xpos="far_left", ypos="head")
    gen "And make sure you've been working out your butthole." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "........" ("annoyed", "narrow", "base", "up")
    gen "With my cock." ("grin", xpos="far_left", ypos="head")
    her "I see..." ("annoyed", "base", "base", "R")
    her @ cheeks blush "I'm not against that but I bet I'll gain no points for this?" ("annoyed", "narrow", "angry", "R")
    gen "I'm helping you with your revisions, why should you be getting points for that?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "And what revisions..." ("annoyed", "closed", "base", "mid")
    her @ cheeks blush "Alright, since you have helped me a lot, I'm in." ("base", "base", "base", "R")
    her @ cheeks blush tears soft "{size=-2}(I give myself away for free now, what a bad whore I make){/size}" ("base", "narrow", "worried", "mid_soft")
    gen "Come here and strip." ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base", reduce=0.8)
    call blkfade

    hide hermione_main
    with d3

    #call set_her_action("naked")
    #call set_her_action("hold_book")
    $ hermione.strip("clothes")

    call her_chibi_scene("lie_on_desk")
    hide screen bld1
    call hide_blkfade
    call ctc

    show screen blktone
    her "" (xpos="mid", ypos="base")
    gen "You can open a book if you want." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "I should read about this spell called \"the Clap\"!" ("annoyed", "closed", "base", "mid")

    hide hermione_main
    nar "You take advantage of her moment of distraction to force your cock into her butthole."

    call her_chibi_scene("sex_naked_slow")
    hide screen bld1
    with d1
    with hpunch
    pause .8

    her @ cheeks blush "Ah, you brute {heart}" ("grin", "narrow", "base", "up")
    gen "Your butthole is the perfect fit, not too tight and not too stretched!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You've trained me well..." ("silly", "narrow", "base", "up")
    nar "You caress her clit while fucking her."
    her @ cheeks blush "*Mmmh*, yes {heart}" ("open", "narrow", "base", "up")
    gen "You love it don't you?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Your cock in my ass, oh yes." ("base", "narrow", "base", "up")
    gen "Even without points?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Don't make me regret agreeing to this." ("upset", "happyCl", "worried", "mid")
    gen "Say you love it even without points." ("base", xpos="far_left", ypos="head")
    call her_chibi_scene("sex_naked")
    nar "You increase the pace."
    her @ cheeks blush "*Ahh* yesss {heart}" ("open_tongue", "narrow", "base", "up")
    her @ cheeks blush "I'm such a whore, I love sex even for free." ("mad", "wide", "base", "stare")
    gen "You know it!" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Don't make it a habit." ("open", "happy", "base", "mid")
    gen "......" ("base", xpos="far_left", ypos="head")
    nar "You pull out your cock and roughly shove it back inside."
    with hpunch
    her @ cheeks blush "*Aaaaah* {heart}" ("open", "narrow", "annoyed", "up")
    her @ cheeks blush "I love being sodomised savagely by my headmaster." ("silly", "narrow", "base", "up")
    nar "And again."
    with hpunch
    her "Yessss {heart}"
    her @ cheeks blush tears soft "I love his big cock in my ass." ("silly", "base", "worried", "mid")
    nar "You slap her butt-cheek."
    play sound "sounds/slap.ogg"
    with hpunch
    her @ cheeks blush tears mascara "And being punished for my sluttiness." ("open", "narrow", "worried", "mid_soft")
    play sound "sounds/slap.ogg"
    with hpunch
    her @ cheeks blush tears soft "*Aah*, like this, punish me more master {heart}" ("silly", "base", "worried", "mid")
    play sound "sounds/slap.ogg"
    with hpunch
    her @ cheeks blush "Yess!" ("open_wide_tongue", "narrow", "base", "up")
    play sound "sounds/slap.ogg"
    with hpunch
    her @ cheeks blush "More!" ("open_wide_tongue", "narrow", "base", "up")
    play sound "sounds/slap.ogg"
    with hpunch
    her @ cheeks blush tears crying "I'm about to..." ("angry", "narrow", "base", "dead")
    play sound "sounds/slap.ogg"
    with hpunch
    pause .1
    play sound "sounds/slap.ogg"
    with hpunch
    pause .1
    her @ cheeks blush "Cuuuum {heart} {heart}" ("open_wide_tongue", "narrow", "base", "up")
    call her_chibi_scene("sex_naked_fast")
    nar "You fuck her butthole fiercely."
    her @ cheeks blush "Yes, yes, again, *aaaah* {heart}" ("open_wide_tongue", "narrow", "base", "up")
    gen "Yes, my little whore, yes!" ("angry", xpos="far_left", ypos="head")
    call her_chibi_scene("sex_naked_cum_out")
    her @ cheeks blush tears mascara "*Panting* *panting*" ("open", "narrow", "worried", "mid_soft")
    call her_chibi_scene("sex_naked_cum_out_done")
    gen "*Panting* *panting*" ("angry", xpos="far_left", ypos="head")

    hide hermione_main
    call blkfade

    hide hermione_main
    call her_chibi_scene("lie_on_desk")
    pause 1
    hide screen bld1
    hide screen blktone
    call hide_blkfade
    pause .8

    call bld
    gen "*sigh* that was, that was..." ("base", xpos="far_left", ypos="head")
    her "Marvellous {heart}" ("smile", "base", "base", "R")
    her @ cheeks blush "I'm so glad you agreed to tutor me, professor..." ("silly", "narrow", "base", "up")
    her @ cheeks blush "Your lessons have changed my life so much!" ("smile", "base", "angry", "mid")
    gen "{size=-2}(Victory!){/size}" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "But if you think you can fuck me all the time without giving me points..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "You're dreaming!" ("annoyed", "narrow", "base", "up")
    gen "{size=-2}(*Ohhh*...){/size}" ("base", xpos="far_left", ypos="head")
    gen "Even occasionally?" ("base", xpos="far_left", ypos="head")
    her "......."
    her @ cheeks blush "Only if you are well-behaved..." ("soft", "base", "base", "R")
    gen "I'm the most well-behaved professor in the whole school!" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Sure." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "{size=-2}(At least, you're not the worst...){/size}" ("annoyed", "narrow", "base", "up")
    gen "Good night, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Good night, [name_genie_hermione]." ("base", "base", "base", "R")

    hide hermione_main
    call blkfade

    nar "You dismiss Hermione."
    nar "She puts her clothes back on without haste."

    play sound "sounds/cloth_sound.ogg"
    $ hermione.wear("all")
    pause 1

    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","desk","base")
    call hide_blkfade
    pause 1

    call her_walk("door", "base")

    her @ cheeks blush "{size=-4}(He's hardly Prince Charming but...){/size}" ("base", "narrow", "base", "mid_soft", ypos="head", flip=False, trans=d3)
    her @ cheeks blush "{size=-4}(I doubt Prince Charming could fuck me half as well as he can!){/size}" ("grin", "narrow", "base", "up")

    call her_chibi("leave")

    $ states.her.ev.tutoring.stage = 15

    if states.her.level < 24:
        $ states.her.level += 1

    jump end_hermione_event
