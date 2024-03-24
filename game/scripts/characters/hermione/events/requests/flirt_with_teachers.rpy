

### Flirt With Teacher ###

label hg_pr_flirt_teacher:

    # Setup
    $ current_payout = 15

    if not _events_completed_any:
        gen "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    her "" (xpos="right", ypos="base", trans=fade)
    gen "[name_hermione_genie], I want you to be especially flirtatious with your teachers today." ("base", xpos="far_left", ypos="head")

    #Intro
    if not _events_completed_any:
        if states.her.ev.flirt_with_students.done_before:
            her "I will do my best, [name_genie_hermione]!" ("base", "base", "base", "mid")
            her "Now I understand why you asked me to flirt with these pesky Slytherin boys." ("open", "closed", "angry", "mid")
            her "I am glad you finally decided to act, [name_genie_hermione]!" ("open", "base", "base", "mid")
        else:
            her "*Huh*?!" ("open", "base", "angry", "mid")
            her "Why would I want to flirt with the teach--" ("angry", "base", "angry", "mid")
            her "O-oh... I see..." ("grin", "base", "base", "R")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        her "You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?" ("normal", "squint", "angry", "mid")
        her "I am honoured to pose as bait in this noble endeavour." ("open", "closed", "base", "mid")
        gen "*Ehm*... Yeah, that's exactly what I'm doing." ("base", xpos="far_left", ypos="head")
        her "Splendid! You can count on me, [name_genie_hermione]!" ("smile", "squint", "angry", "mid")
    else:
        if states.her.tier >= 3:
            her "As you wish, [name_genie_hermione]." ("base", "squint", "base", "mid")
        elif states.her.tier >= 2:
            her "I'll make sure to note every single detail, [name_genie_hermione]." ("base", "squint", "angry", "mid")
            gen "Looking forward to it..." ("base", xpos="far_left", ypos="head")
        else:
            her "I shall provide you with a detailed report later tonight, [name_genie_hermione]." ("normal", "squint", "angry", "mid")
            gen "I will be waiting..." ("base", xpos="far_left", ypos="head")

    her "Well, I'd better go now. Classes are about to start..."

    call her_walk(action="leave")

    jump end_hermione_event


# End Event
label end_hg_pr_flirt_teacher:
    $ gryffindor += current_payout
    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk(action="leave")

    # Unequip lockhart tattoo after the event
    if hermione.is_equipped_item(her_tattoo_lockhart):
        $ hermione.unequip(her_tattoo_lockhart)

    label .quick_end:

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    jump end_hermione_event

label hg_pr_flirt_teacher_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")

    her "Good evening, [name_genie_hermione]." ("open", "closed", "base", "mid", xpos="mid", ypos="base", trans=fade)
    her "" ("normal", "base", "base", "mid")
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you complete your task?" ("base", xpos="far_left", ypos="head")
    her "I did as you asked, [name_genie_hermione]..."

    if _events_completed_all: # If you have seen all events in this tier once, you get the choice to skip it.
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_flirt_teacher

            "\"Give me the details.\"":
                pass

    gen "Tell me, [name_hermione_genie], which teachers did you flirt with?" ("base", xpos="far_left", ypos="head")

    if not _events_completed_any:
        her "*Ehm*... Okay..." ("soft", "base", "base", "R")

    return

### Tier 1 ###

transform hg_pr_flirt_teacher_flitwick_panning:
    ypan 0
    ease_quart 6.0 ypan 180

label hg_pr_flirt_teacher_T1_E1: # Flitwick

    call hg_pr_flirt_teacher_intro

    #if  states.her.level >= 3 and states.her.level < 6:

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "Well, I was going to flirt with Professor Flitwick..." ("open", "base", "worried", "R")
    her "But I didn't really get that far..." ("open", "squint", "worried", "R")
    her "Professor Flitwick asked me to show the class how to cast {i}wingardium leviosa{/i}, you see." ("open", "squint", "worried", "mid")
    her "And of course, seeing that I'm an expert in the subject, I obliged." ("open", "closed", "base", "mid")
    gen "Taking any and every opportunity to show off, I see." ("base", xpos="far_left", ypos="head")

    show her_flirt_public_flitwick zorder 15 as cg with fade

    her "So, I made my way to the front of the class, next to Professor Flitwick, and began casting the spell, making a feather float in the air."
    her "But, as I was explaining the proper swishing and flicking motions, it is when I realized--"
    gen "You weren't getting praised enough?" ("base", xpos="far_left", ypos="head")
    her "I had already shown the class how to cast that particular spell ages ago."
    her "It made me think, there must've been some ulterior motive as to why Professor Flitwick would have me do it again."
    gen "Maybe he's just forgetful? I forget to take my medication all the time." ("base", xpos="far_left", ypos="head") #unspecified medication makes it funnier
    her "I am sure he did it to take advantage of me, but unfortunately for him, \"forgetting\" that we've already learned that spell made it very clear to me!"
    gen "So, what you're saying is he never actually learnt how to cast the spell, and is making his students do it for him?" ("base", xpos="far_left", ypos="head")

    show her_flirt_public_flitwick eyes_down as cg with d5

    her "No, that isn't what I meant. He was having me cast that spell to distract me, so he could slide under my skirt!"

    show her_flirt_public_flitwick mouth_open as cg at hg_pr_flirt_teacher_flitwick_panning

    call ctc

    gen "He--{w=0.2} Hold on...{w=0.4} Even if your focus was on casting the spell, it took you that long to notice a grown-ass man disappearing beneath you?" ("base", xpos="far_left", ypos="head")
    her "He's a half-goblin! Of course I wouldn't notice right away!"
    gen "(Women and their obsession with height...)"
    gen "Just because the man isn't six feet tall doesn't mean--..." ("base", xpos="far_left", ypos="head")
    her "*Huh*?"
    gen "I never thought you'd be so judgmental, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "You shouldn't measure people by their height,{w=0.5} but by the size of their--" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]-- That's not what I meant! Could you listen to me first, please?"
    gen "Heart..." ("base", xpos="far_left", ypos="head")
    her "........"
    gen "Perhaps if you weren't so short-tempered, you'd let me finish talking for once." ("base", xpos="far_left", ypos="head")
    her "...{w=0.4} As I was saying--"

    hide cg with fade

    her "Even before I could react and stop him, Professor Flitwick was already standing right beside me... Almost as if he had apparated." ("angry", "base", "base", "mid")
    gen "How exciting." ("base", xpos="far_left", ypos="head")
    gen "Is this all you have for me today, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Y-yes..." ("open", "base", "worried", "mid")
    her "But [name_genie_hermione], I now know for a fact that professor Flitwick is \"dirty\"!" ("angry", "base", "worried", "mid")
    her "He looked at my panties, [name_genie_hermione]!" ("annoyed", "base", "worried", "R")

    if states.her.status.show_panties:
        gen "Didn't you show them off before?" ("base", xpos="far_left", ypos="head")
        her "What?" ("open", "base", "base", "mid")
        her @ cheeks blush "That was... different..." ("annoyed", "base", "angry", "R")
        gen "If you say so..." ("base", xpos="far_left", ypos="head")
        gen "So, do you believe that professor flit-stick is showing this kind of behaviour frequently?" ("base", xpos="far_left", ypos="head")
    else:
        gen "Lucky man." ("base", xpos="far_left", ypos="head")
        her "What?" ("open", "base", "base", "mid")
        gen "Yucky... Man..." ("base", xpos="far_left", ypos="head")
        gen "So, does this flick-shit fella do this to other students as well, you think?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... It's \"Professor Flitwick\", [name_genie_hermione]." ("normal", "squint", "angry", "mid")
    her "And yes, I don't doubt that this isn't the first time he's done this." ("normal", "squint", "angry", "mid")
    gen "Right. Putting him on my \"Naughty list\" as we speak." ("base", xpos="far_left", ypos="head")
    her "......................" ("annoyed", "squint", "base", "mid")
    gen "Even then, you failed the task I set for you today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "What, but I--" ("annoyed", "narrow", "angry", "R")

    menu:
        "\"Here are your points though.\"":
            gen "Know that I am a merciful master-- I mean a headmaster." ("base", xpos="far_left", ypos="head")
            her "Really?" ("angry", "base", "worried", "mid")
            her "Thank you so much, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid")

        "\"No points for you!\"":

            her "But [name_genie_hermione], I did my best!" ("angry", "base", "worried", "mid")
            her @ tears soft "You are going back on your promise [name_genie_hermione]!" ("mad", "base", "worried", "mid")
            gen "......................." ("base", xpos="far_left", ypos="head")
            stop music fadeout 1.0
            her "How unbecoming of a school headmaster!" ("scream", "happyCl", "worried", "mid")
            gen "You are dismissed, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "*Tsk*!" ("angry", "base", "angry", "mid", emote="angry")

            $ states.her.mood += 18
            jump end_hg_pr_flirt_teacher.no_points

    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T1_E2: # Snape

    call hg_pr_flirt_teacher_intro

    her ".................." ("soft", "base", "base", "R")
    her "............................"
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]... I'm sorry... I just..." ("open", "base", "worried", "mid")
    her "............" ("soft", "base", "base", "R")
    gen "Did you do what I asked you to do?" ("base", xpos="far_left", ypos="head")
    her "I tried, [name_genie_hermione]. I really did..." ("open", "base", "base", "mid")
    gen "Who did you try to flirt with?" ("base", xpos="far_left", ypos="head")
    her "........." ("soft", "base", "base", "R")
    her "Professor Snape, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    gen "Severus? Interesting..." ("base", xpos="far_left", ypos="head")
    gen "How did it go?" ("base", xpos="far_left", ypos="head")
    her "It was awful [name_genie_hermione]..." ("normal", "squint", "angry", "mid")
    her "I am sorry, but I really hate professor Snape, [name_genie_hermione]!"
    gen "(I'm pretty sure the feeling is mutual...)" ("base", xpos="far_left", ypos="head")
    gen "Tell me what happened." ("base", xpos="far_left", ypos="head")
    her "Nothing happened, [name_genie_hermione]. He just laughed at me..." ("annoyed", "squint", "angry", "mid")
    her "I may not have much feminine charm, but I tried to be nice..." ("annoyed", "base", "worried", "R")
    her "And he just started laughing in my face!" ("scream", "closed", "angry", "mid")
    her "... It is really scary to see professor Snape laugh..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    her "........"
    her "I am awful at flirting, I am sorry [name_genie_hermione]..."
    her "But I know that professor Snape is \"dirty\"!" ("angry", "base", "angry", "mid")
    her "If you were to send someone else, the outcome would be different, I just know it!"
    gen "Someone else?" ("base", xpos="far_left", ypos="head")
    her "Yes! Someone with more experience in this..." ("upset", "wink", "base", "mid")
    her "Someone..."
    her "Someone... *Ehm*..."
    gen "Sluttier?" ("base", xpos="far_left", ypos="head")
    her "Yes, I suppose..." ("disgust", "narrow", "base", "mid_soft")
    gen "Don't you give up, [name_hermione_genie]. We will make a slut *err*--" ("base", xpos="far_left", ypos="head")
    gen "I mean a woman out of you yet!" ("base", xpos="far_left", ypos="head")
    her "..................." ("annoyed", "narrow", "annoyed", "mid")

    menu:
        "\"Here are your points, [name_hermione_genie].\"":
            her "" ("base", "base", "worried", "mid")

        "\"... I'm afraid you get no points this time.\"":
            her "But I did my best..." ("annoyed", "narrow", "angry", "R")
            her "And I feel so humiliated now..." ("angry", "happyCl", "worried", "mid", emote="sweat")
            her "But I understand and won't argue with your decision..." ("normal", "happyCl", "worried", "mid")

            $ states.her.mood += 3
            jump end_hg_pr_flirt_teacher.no_points

    jump end_hg_pr_flirt_teacher

label hg_pr_flirt_teacher_T1_E3: # Filch

    call hg_pr_flirt_teacher_intro

    stop music fadeout 1.0
    her "I tried to flirt with mister Filch, [name_genie_hermione]..." ("open", "base", "worried", "R")
    gen "I see. {size=-5}(No idea who that is.){/size}" ("base", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "Yes, I know that technically mister Filch is not a teacher..." ("open", "base", "worried", "mid")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    her "But he is part of the school's staff..." ("base", "base", "base", "mid")
    her "And we did hit it off quite well too!"
    her "He was surprisingly sweet."
    her "But I don't think he is \"dirty\", [name_genie_hermione]."
    gen "Gotcha... Mister Filth is off the list then." ("base", xpos="far_left", ypos="head")
    her "It's \"mister Filch\", [name_genie_hermione]..." ("normal", "squint", "angry", "mid")
    gen "What did I say?" ("base", xpos="far_left", ypos="head")
    her "......." ("normal", "squint", "angry", "R")
    her "Can I get my points now?" ("open", "base", "worried", "mid")

    jump end_hg_pr_flirt_teacher

### Tier 2 ###

label hg_pr_flirt_teacher_T2_E1: # Slughorn

    call hg_pr_flirt_teacher_intro

    #elif states.her.level >= 6 and states.her.level < 9:

    stop music fadeout 1.0
    her "Well, professor Slughorn invited me over to one of his..." ("open", "base", "worried", "R")
    her "Rather disturbing tea parties..."
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "There were plenty of girls..." ("open", "closed", "base", "mid")
    her "But none of them were in my year..."
    her "Almost every guest was a freshman..." ("annoyed", "squint", "base", "mid")
    her "We had tea and some cake..." ("open", "closed", "base", "mid")
    her "Everything was pretty harmless..."
    gen "Did you flirt with the man or not?" ("base", xpos="far_left", ypos="head")
    her "I did..."
    her "Or at least I tried to..." ("annoyed", "squint", "base", "mid")
    her "Professor Slughorn seemed to be more interested in the other girls..."
    gen "You almost sound jealous, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "What?!" ("angry", "wide", "base", "stare")
    her "That is preposterous!" ("annoyed", "narrow", "angry", "R")
    gen "Here are your points..." ("base", xpos="far_left", ypos="head")
    her "...................."

    jump end_hg_pr_flirt_teacher

label hg_pr_flirt_teacher_T2_E2:

    $ hermione.equip(her_tattoo_lockhart) # Tattoo

    call hg_pr_flirt_teacher_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME

    if hermione.is_worn("robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ hermione.strip("robe")
        pause .8
        her "Ah..." ("smile", "happyCl", "base", "mid")

    if not hermione.is_worn("bottom"):
        her "I had an amazing day, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid", emote="happy")
        gen "Glad to--" ("base", xpos="far_left", ypos="head")
        gen "[name_hermione_genie]... What have you done to your leg?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "What do you...{w=0.4} Oh, that..." ("mad", "base", "base", "down")
        gen "Yes that..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "It's... It's nothing." ("open", "base", "base", "mid")

        if not hermione.is_worn("stockings"):
            gen "The hell it is...{w=0.4} Is that writing on your leg?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I... Yes..." ("normal", "happyCl", "worried", "mid")
            gen "Gil... Gilde--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Sigh*... Gilderoy Lockhart... [name_genie_hermione]." ("open", "narrow", "base", "down")
            gen "Now that's dirty!" ("base", xpos="far_left", ypos="head")
            her "What!?" ("clench", "base", "worried", "mid")
            gen "Tagging the students... Why didn't I think of that!" ("base", xpos="far_left", ypos="head")
            her "Sir, what are you on about?" ("annoyed", "squint", "base", "mid")
            gen "Why else would he put his name there?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Sir, he's a famous author!" ("normal", "squint", "angry", "mid")
            gen "Doesn't give him the right to--" ("base", xpos="far_left", ypos="head")
            gen "Oh... It's an autograph!" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I... What else would it be?" ("clench", "squint", "worried", "mid")
            gen "Nothing..." ("base", xpos="far_left", ypos="head")
            gen "Here are your points..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you, [name_genie_hermione]." ("annoyed", "base", "worried", "down")
        else:
            gen "I can clearly see something..." ("base", xpos="far_left", ypos="head")
            gen "Take that off and let me have a proper look." ("base", xpos="far_left", ypos="head")
            her "I..."
            her "Well, alright, but don't get any ideas..." ("angry", "base", "angry", "mid")
            pause.5
            her @ cheeks blush "Here..." ("disgust", "narrow", "base", "down")

            play sound "sounds/cloth_sound3.ogg"
            $ hermione.strip("bottom", "stockings")
            with d3
            pause .5

            gen "Gil... Gilde--" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Sigh*... Gilderoy Lockhart... [name_genie_hermione]." ("open", "narrow", "base", "down")
            her @ cheeks blush "He very kindly gave me his autograph after today's lesson..." ("base", "narrow", "base", "down")
            gen "And why would you want such a thing?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "He's a very popular and esteemed author, surely you know this..." ("annoyed", "base", "base", "mid")
            gen "Of course!" ("grin", xpos="far_left", ypos="head")
            gen "Who would say no to having their leg signed by \"The\" {i}Spocktart{/i}?" ("grin", xpos="far_left", ypos="head")
            gen "Not me, that's for sure!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I didn't ask him to sign my leg specifically..." ("angry", "base", "worried", "mid")
            gen "I see...{w=0.4} Well, can't say I'm surprised..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Sir?" ("annoyed", "base", "worried", "mid")
            gen "An esteemed author making dirty requests from a fan is more common than you thi--" ("base", xpos="far_left", ypos="head")

            jump hg_pr_flirt_teacher_T2_E2.angry
    else:
        her "I had an amazing day, [name_genie_hermione]!" ("smile", "happyCl", "base", "mid", emote="happy")
        gen "Do tell, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "I had a class with professor Lockhart today..." ("grin", "base", "base", "R")
        her "[name_genie_hermione], he is so charming and smart and--" ("base", "base", "base", "mid")
        her "And perfect..." ("base", "narrow", "base", "up")
        gen "Please spare me your schoolgirl crush, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "He was even kind enough to give me his autograph..." ("smile", "happyCl", "base", "mid", emote="happy")
        gen "How kind of him indeed..." ("base", xpos="far_left", ypos="head")
        her "Yes, I can't wait to show it to the girls!" ("grin", "base", "base", "R")
        her "It was a bit weird that he wouldn't sign my notebook though..." ("annoyed", "base", "base", "mid")
        gen "He wouldn't--" ("base", xpos="far_left", ypos="head")
        her "It's just going to fade away in the shower now..." ("upset", "base", "worried", "mid")
        gen "It's going to--" ("base", xpos="far_left", ypos="head")
        gen "Show me!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]?" ("open", "base", "worried", "mid")
        her @ cheeks blush "I... It's just an autograph..." ("base", "squint", "worried", "R")
        gen "Just an autograph? It's {i}Lockfart{/i} we're talking about here, I have to see it!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "I..." ("disgust", "base", "worried", "down")

        menu:
            "\"Show me or I won't pay you!\"":
                $ states.her.mood += 9

                her "What?!" ("scream", "base", "base", "mid")
                her "..............." ("annoyed", "narrow", "worried", "down")
                her ".................." ("annoyed", "base", "worried", "R")

                her "Well, alright, but don't get any ideas..." ("angry", "base", "angry", "mid")
                pause.5
                her @ cheeks blush "Here..." ("disgust", "narrow", "base", "down")

                play sound "sounds/cloth_sound3.ogg"
                $ hermione.strip("bottom", "stockings")
                with d3
                pause .5

                gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "" ("angry", "narrow", "annoyed", "mid", emote="angry")
                call ctc

                gen "Well then, this {i}Goldenheart{/i} is most certainly \"dirty\"!" ("base", xpos="far_left", ypos="head")

                label .angry:

                her @ cheeks blush "What do you mean?!" ("clench", "happy", "base", "mid")
                gen "Surely a piece of paper would've been--" ("base", xpos="far_left", ypos="head")

                her "Professor Lockhart is nothing but an embodiment of everything pure and courageous!" ("annoyed", "narrow", "annoyed", "mid")
                her "You should not worry about professor Lockhart, [name_genie_hermione]." ("base", "base", "worried", "R")
                her "He is not \"dirty\"." ("annoyed", "base", "worried", "L")
                gen "Whatever you say [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
                her "............?" ("annoyed", "narrow", "annoyed", "mid", emote="angry")
                gen "Anyhow..." ("base", xpos="far_left", ypos="head")
                call ctc

            "\"Fine... Here are your points.\"":
                her "Thank you for understanding, [name_genie_hermione]." ("base", "happyCl", "base", "mid")

    $ hermione.wear("all")
    call unlock_clothing(text="A new tattoo for Hermione has been unlocked!", item=her_tattoo_lockhart)
    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T2_E3: # Filch

    call hg_pr_flirt_teacher_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "Well, I spent a fair bit of my time, flirting with mister Filch today." ("soft", "base", "base", "mid")
    her "What a well-read and exceptionally well-mannered gentleman mister Filch is." ("open", "closed", "base", "mid")
    gen "........" ("base", xpos="far_left", ypos="head")
    her "But I don't think anyone knows him like that..." ("soft", "base", "base", "R")
    her "I don't think anyone knows mister Filch like I do."
    her "I feel like he really opened up to me, [name_genie_hermione]." ("base", "base", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "This, mister Fli{size=+7}nt{/size}--" ("base", xpos="far_left", ypos="head")
    her "It's mister Filch, [name_genie_hermione]." ("open", "closed", "angry", "mid")
    gen "Yeah, whatever... Is he a teacher here then?" ("base", xpos="far_left", ypos="head")
    her "Mister Filch? A teacher? No, [name_genie_hermione]..."
    her "He is the caretaker... Shouldn't you know your school personnel, [name_genie_hermione]?" ("base", "base", "base", "mid")
    gen "A caretaker...?" ("base", xpos="far_left", ypos="head")
    gen "You mean he is a janitor?" ("base", xpos="far_left", ypos="head")
    her "Well..." ("open", "base", "worried", "R")
    gen "[name_hermione_genie], I did not send you out there to charm school janitors!" ("base", xpos="far_left", ypos="head")
    her "But mister Filch is part of the school staff, [name_genie_hermione]!" ("open", "base", "base", "mid")

    menu:
        "\"Just take your points and go!\"":
            her "........................." ("normal", "base", "base", "mid")

            jump end_hg_pr_flirt_teacher

        "\"Favour failed! No points for you!\"":
            her "But [name_genie_hermione]?" ("normal", "squint", "angry", "mid")
            gen "You are dismissed, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "........................................." ("angry", "base", "angry", "mid")

            $ states.her.mood +=15
            jump end_hg_pr_flirt_teacher.no_points

### Tier 3 ###

label hg_pr_flirt_teacher_T3_E1: # Filch

    call hg_pr_flirt_teacher_intro

    stop music fadeout 1.0
    her "............................." ("normal", "happyCl", "worried", "mid")
    her "....................................."
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], I..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "What is it? What happened?" ("base", xpos="far_left", ypos="head")
    her "Well..." ("annoyed", "base", "worried", "R")
    her "It's mister Filch, [name_genie_hermione]..."
    gen "The janitor?" ("base", xpos="far_left", ypos="head")
    her "I flirted with him a little..." ("open", "base", "base", "mid")
    her "And it went great at first..."
    her "......................." ("annoyed", "base", "worried", "R")
    gen "................?" ("base", xpos="far_left", ypos="head")
    her "And then..." ("open", "base", "base", "mid")
    her "Well, perhaps I shouldn't..." ("annoyed", "base", "worried", "R")
    gen "[name_hermione_genie], if you are not going to speak up, you may as well leave." ("base", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "He showed me his \"thing\", [name_genie_hermione]!" ("scream", "happyCl", "worried", "mid")
    gen "His what?" ("base", xpos="far_left", ypos="head")
    her "His... manhood, [name_genie_hermione]." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "Way to go, Janitor-guy!" ("grin", xpos="far_left", ypos="head")
    her "What?!" ("scream", "wide", "base", "mid")
    gen "*Ahem*... I mean, this is unspeakable!" ("base", xpos="far_left", ypos="head")
    her @ tears soft "Yes... It was a vile, crooked thing, all covered in veins..." ("angry", "base", "base", "mid")
    gen "Spare me the grisly details, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her @ tears soft_blink "Why would he do such a thing?" ("mad", "happyCl", "worried", "mid")
    her "One second we were just talking and then..."
    gen "Well, your noble  sacrifice shall not go unnoticed, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    gen "{number=current_payout} points to Gryf--" ("base", xpos="far_left", ypos="head")
    her @ tears soft "Professor, please wait." ("soft", "base", "base", "mid")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    her "Well, aren't you going to do something about this?" ("open", "base", "base", "mid")
    gen "Err..." ("base", xpos="far_left", ypos="head")
    her "What if I am not the first victim...?" ("angry", "base", "angry", "mid")
    her "Some unfortunate freshman could be traumatised for life!"
    gen "Who wouldn't be, really?" ("base", xpos="far_left", ypos="head")
    her "Does this mean you will take action, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "*Ehm*... Yeah, sure..." ("base", xpos="far_left", ypos="head")
    gen "There! Putting it on my {i}to-do-list{/i}..." ("base", xpos="far_left", ypos="head")
    play sound "sounds/scribble.ogg"
    gen "\"Take care of the creepy janitor-guy and his crooked cock.\"..." ("base", xpos="far_left", ypos="head")
    gen "Yes, first thing tomorrow." ("base", xpos="far_left", ypos="head")
    her "Thank you [name_genie_hermione]." ("open", "closed", "base", "mid")
    her "Can I have my points now?" ("smile", "happyCl", "base", "mid")

    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T3_E2: # Snape

    call hg_pr_flirt_teacher_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "Professor Snape!" ("angry", "base", "angry", "mid", emote="angry")
    gen "*Ehm*... Yeah, I'm pretty sure it's Dumbledore or something..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], please, you need to listen to me!" ("open", "base", "base", "mid")
    gen "Yes, yes, [name_hermione_genie], I'm listening." ("base", xpos="far_left", ypos="head")
    her "I just confirmed that professor Snape is corrupted and {i}dirty{/i}, [name_genie_hermione]!" ("open", "closed", "angry", "mid")
    gen "Tell me what happened." ("base", xpos="far_left", ypos="head")
    her "Well, during classes today..." ("open", "base", "base", "mid")
    her "I have been doing my best to attract professor Snape's attention..." ("open", "base", "base", "R")
    her "I have been giving him \"dreamy looks\"..." ("open", "narrow", "worried", "down")
    her "And I've been eyeing his crotch..." ("soft", "base", "base", "R")
    gen "You..." ("base", xpos="far_left", ypos="head")
    gen "Eyed his crotch?" ("base", xpos="far_left", ypos="head")
    her "Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly..." ("open", "closed", "angry", "mid")
    gen "Where do you get this stuff?" ("base", xpos="far_left", ypos="head")
    her "Women's magazines..." ("open", "base", "worried", "R")
    her "Well, anyway, it worked, [name_genie_hermione]." ("normal", "squint", "angry", "mid")
    her "As soon as the class was over, professor Snape grabbed my buttocks, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
    gen "The fiend!" ("grin", xpos="far_left", ypos="head")
    gen "Did you enjoy it, though?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], I am only doing this--" ("scream", "closed", "angry", "mid")
    gen "Go Gryffindor! Honour and all that... Yes, I remember." ("base", xpos="far_left", ypos="head")
    her "" ("normal", "closed", "angry", "R", xpos="mid", ypos="base")

    jump end_hg_pr_flirt_teacher


label hg_pr_flirt_teacher_T3_E3: # Lockhart

    call hg_pr_flirt_teacher_intro

    stop music fadeout 1.0
    her "Professor Lockhart!" ("annoyed", "squint", "angry", "mid")
    gen "Got it! Adding him to the \"Naughty list\"!" ("base", xpos="far_left", ypos="head")
    her "No, [name_genie_hermione], it's not that..." ("open", "base", "worried", "mid")
    her "Or..." ("annoyed", "narrow", "angry", "R")
    her "I'm not sure..."
    her "I used to adore him..." ("open", "base", "worried", "mid")
    her "But he..." ("soft", "base", "base", "R")
    her "He just..."
    her @ tears soft_blink "How is this possible?" ("mad", "happyCl", "worried", "mid")
    her "I can't believe this..."
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    gen "{size=-4}(*Argh*! The suspense is killing me!){/size}" ("base", xpos="far_left", ypos="head")
    gen "What was it, [name_hermione_genie]? Speak up!" ("angry", xpos="far_left", ypos="head")
    her "*Huh*?" ("open", "base", "base", "mid")
    gen "What did Professor Lockhart do to you?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Nothing, [name_genie_hermione]..." ("soft", "base", "base", "R")
    gen "Nothing?!" ("base", xpos="far_left", ypos="head")
    her "Yes, I sort of cornered mister Lockhart today..." ("open", "base", "worried", "mid")
    her "And I also may have sort of made a pass at him..." ("open", "base", "base", "mid")
    gen "Seriously?" ("base", xpos="far_left", ypos="head")
    her "Yes... I don't know what had gotten into me, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "Way to go, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
    her "Hear me out first [name_genie_hermione], please!" ("scream", "happyCl", "worried", "mid")
    gen "My apologies. Please continue." ("base", xpos="far_left", ypos="head")
    her "Well, I always knew that mister Lockhart was a true gentleman, and..." ("open", "base", "base", "mid")
    her "And... And I just wanted to clear his name from any suspicions once and for all..."
    her "..............." ("annoyed", "base", "worried", "R")
    her "Well, mister Lockhart did not reject me..."
    gen "You are killing me [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    gen "He didn't reject you, he didn't do anything to you..." ("base", xpos="far_left", ypos="head")
    gen "What the hell happened then?" ("base", xpos="far_left", ypos="head")
    her "............." ("normal", "happyCl", "worried", "mid")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # HERMIONE'S THEME.
    her "I made him cry, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "..............{w=0.5}wait what?" ("base", xpos="far_left", ypos="head")
    her "He gave me a bewildered look and then started to sob..." ("angry", "base", "worried", "mid")
    her "He looked like he was genuinely afraid of me, [name_genie_hermione]."
    her "I think..." ("annoyed", "base", "worried", "R")
    her "I think mister Lockhart might be afraid of women..."
    gen "Afraid of women?" ("base", xpos="far_left", ypos="head")
    gen "What is that supposed to mean?" ("base", xpos="far_left", ypos="head")
    her "That he is into boys, [name_genie_hermione]?" ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "Oh... To each their own I guess." ("base", xpos="far_left", ypos="head")
    her "............" ("upset", "wink", "base", "mid")
    gen "..........." ("base", xpos="far_left", ypos="head")
    gen "Well, I bet it was a traumatising experience for you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "It was, [name_genie_hermione]..." ("open", "base", "base", "mid")
    gen "Well, I hope these points will make you feel better." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_flirt_teacher
