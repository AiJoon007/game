
### Flash A Classmate ###

label start_hg_pr_flash:

    # Setup
    $ current_payout = 25

    if not _events_completed_any:
        gen "{size=-4}(Tell her to flash her tits to one of her classmates?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu
    return

label hg_pr_flash:

    call start_hg_pr_flash

    her "" (xpos="mid", ypos="base", trans=fade)

    #Intro.
    if not _events_completed_any:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "I would like to award Gryffindor with twenty-five house points today." ("base", xpos="far_left", ypos="head")
        her "Really?" ("grin", "base", "base", "mid")
        her "Thank you, [name_genie_hermione]!"
        gen "Yes, but first I will require your help with something..." ("base", xpos="far_left", ypos="head")
        her "Of course, [name_genie_hermione]! Anything!"
        gen "I need you to go out there and show off your tits to people..." ("base", xpos="far_left", ypos="head")

        stop music fadeout 1.0

        her "...?" ("open", "base", "base", "mid")
        gen "You know, flash your breasts to some boys..." ("base", xpos="far_left", ypos="head")
        her "?!!" ("shock", "wide", "base", "stare")

        if states.her.public_level < 6:
            $ _event.cancel()
            jump too_much_public

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

        her "[name_genie_hermione]!"
        her "This is an entirely different level of inappropriateness, even for you, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
        her "How can you ask one of your pupils to perform such a task?"
        gen "So that's how you feel then? I see..." ("base", xpos="far_left", ypos="head")
        gen "I suppose I will be awarding those points to some other house instead..." ("base", xpos="far_left", ypos="head")
        gen "Slytherin perhaps?" ("base", xpos="far_left", ypos="head")
        her "................" ("disgust", "narrow", "base", "mid_soft")
        gen "But, you know, no pressure..." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
        her "The fate of my house is very important to me, but..."
        gen "Is it really?" ("base", xpos="far_left", ypos="head")
        gen "Why don't you show it to me then?" ("base", xpos="far_left", ypos="head")
        gen "Yes. Show me how important it is to you exactly, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "But this is inappropriate..." ("angry", "base", "angry", "mid")
        gen "Are you really in any position to discuss what is and isn't appropriate at this point?" ("base", xpos="far_left", ypos="head")
        her ".................." ("annoyed", "narrow", "angry", "R")
        gen "I would say that ship has sailed a long time ago..." ("base", xpos="far_left", ypos="head")
        her ".............." ("disgust", "narrow", "base", "mid_soft")
        gen "All I ask of you, is to give some lucky boy a quick peek... Nothing more." ("base", xpos="far_left", ypos="head")
        her "But why? Why must I do things like this, [name_genie_hermione]?" ("annoyed", "narrow", "angry", "R")
        gen "A minute of your time for twenty-five house points..." ("base", xpos="far_left", ypos="head")
        gen "A pretty nifty deal, wouldn't you agree?" ("base", xpos="far_left", ypos="head")
        her "I suppose..."
        her "Well alright, I'll see what I can do..."
    else:
        if states.her.tier >= 5:
            gen "[name_hermione_genie]... I need you to go out there and flash your tits to one of your classmates." ("base", xpos="far_left", ypos="head")
            her "I will do my best [name_genie_hermione]..." ("open", "closed", "base", "mid")
            gen "Really? Just like that? No complaints or anything?" ("base", xpos="far_left", ypos="head")
            her "I am getting paid for this, am I not?" ("base", "narrow", "base", "mid_soft")
            gen "Of course... {number=current_payout} points..." ("base", xpos="far_left", ypos="head")
            her "Why would I complain about a simple task like this then?" ("open", "closed", "base", "mid")
            her "{number=current_payout} house points is a fair price for a few seconds of excitement... *Err*..." ("open", "closed", "base", "mid")
            her "... I mean, embarrassment." ("base", "happyCl", "base", "mid")
            gen "{size=-3}(She's changed this much already?){/size}" ("base", xpos="far_left", ypos="head")
            her "Classes are about to start... I'd better leave now." ("base", "base", "base", "mid")
            her "I will see you later tonight, [name_genie_hermione]." ("open", "closed", "base", "mid")
        elif states.her.tier >= 4:
            gen "I need you to show off your tits, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Right now, [name_genie_hermione]?" ("upset", "wink", "base", "mid")
            gen "Sure! Although I was thinking for one of your classmates..." ("base", xpos="far_left", ypos="head")
            her "I see..." ("angry", "base", "base", "mid")
            gen "Now, give them something to look at, then come back and report to me..." ("base", xpos="far_left", ypos="head")
            her "You'll pay me as usual, right?" ("open", "base", "base", "R")
            gen "Most certainly, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            gen "{number=current_payout} house points. The usual rate..." ("base", xpos="far_left", ypos="head")
            her "................." ("annoyed", "narrow", "base", "R")
            her "Well alright... I will see what I can do, [name_genie_hermione]..." ("disgust", "narrow", "base", "mid_soft")
        else:
            gen "I think you need to show off your tits some more, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Right now, [name_genie_hermione]?" ("upset", "wink", "base", "mid")
            gen "Not to me, I need you to go out and show them to your classmates..." ("base", xpos="far_left", ypos="head")
            her "Oh..." ("angry", "base", "base", "mid")
            gen "Yes, go do that and then report back to me..." ("base", xpos="far_left", ypos="head")
            her "Will I get paid for this?" ("annoyed", "narrow", "angry", "R")
            gen "Of course you will get paid for this, [name_hermione_genie]. Don't be silly." ("base", xpos="far_left", ypos="head")
            gen "{number=current_payout} house points. The usual rate..." ("base", xpos="far_left", ypos="head")
            her "................." ("annoyed", "narrow", "angry", "R")
            her "Well alright... I will see what I can do, [name_genie_hermione]..." ("disgust", "narrow", "base", "mid_soft")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_flash_fail:
    call start_hg_pr_flash

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Today, I'd like you to go out and flash your tits to people." ("base", xpos="far_left", ypos="head")

    jump too_much_public

label end_hg_pr_flash:
    $ gryffindor += current_payout

    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if states.her.tier <= 3 and not _events_completed_any:

        her "(Stupid Slytherins...)" ("angry", "narrow", "angry", "mid", xpos="far_right", flip=True, trans=d3)
        her "(I {b}HATE{/b} them!)" ("angry", "closed", "worried", "mid")

    if states.her.ev.admire_breasts.monologue:
        $ states.her.ev.admire_breasts.monologue = False

        her "(I can't believe I did that today...)" ("upset", "closed", "base", "mid", xpos="far_right", flip=True, trans=d3)
        her "(What if Harry or Ron saw me like that?)" ("angry", "wide", "base", "stare")
        her "(Standing there...)" ("angry", "wide", "base", "stare")
        her "(Pressing my breasts against that window...)" ("angry", "wide", "base", "stare")
        her "(I would probably just die of embarrassment right there on the spot...)" ("angry", "narrow", "base", "down")
        her "(No. Protecting the honour of the Gryffindor house is my number one priority.)" ("upset", "closed", "base", "mid")
        her "(We must get the cup this year, no matter the cost...)" ("upset", "closed", "base", "mid")
        her "(........)" ("angry", "narrow", "base", "down")

    call her_chibi("leave")

    label .quick_end:

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    $ states.her.status.public_stripping = True
    jump end_hermione_event

label hg_pr_flash_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("open", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you complete your task?" ("base", xpos="far_left", ypos="head")
    her "I did as you asked, [name_genie_hermione]..." ("open", "base", "base", "R")

    if _events_filtered_completed_all:
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_flash

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("annoyed", "narrow", "angry", "R")
        her "Well... *Ehm*..." ("soft", "base", "base", "R")
        gen "Speak up, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    gen "Did you flash some lucky guy? How did it go?" ("base", xpos="far_left", ypos="head")

    return

### Tier 3 ###

label hg_pr_flash_T3_E1:

    call hg_pr_flash_intro

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "*Ehm*... Not too well, actually..." ("angry", "happyCl", "worried", "mid",emote="sweat")
    her "................................"
    gen "Just tell me what happened, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "That's the thing, [name_genie_hermione]..." ("open", "base", "base", "mid")
    her "Nothing happened..."
    her "The only chance I had, was with this one Slytherin... But I just couldn't bring myself to do it..." ("open", "narrow", "worried", "down")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "Well, I can't just give you the points for nothing, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]... I understand..." ("open", "closed", "base", "mid")
    her "I shall try harder next time... I promise..." ("annoyed", "base", "worried", "R")
    gen "Then I will just put these {number=current_payout} points aside for now..." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]..." ("annoyed", "base", "worried", "R")
    her "..."
    her "I'd better go now."

    jump end_hg_pr_flash.no_points

label hg_pr_flash_T3_E2:

    call hg_pr_flash_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "*Ehm*... Sort of..." ("annoyed", "base", "worried", "R")
    gen "Sort of?" ("base", xpos="far_left", ypos="head")
    her "Yes... *Ehm*..." ("open", "base", "base", "mid")
    her "Well, I've had my eyes on this Hufflepuff guy for a while, so I decided he could potentially be the \"someone\" that I try it on..."
    gen "You've \"had your eyes on him\" have you?" ("base", xpos="far_left", ypos="head")
    her "Yes, as he's always the person to arrive to his classes first, I made the assumption I might be able to catch him alone."
    gen "Right." ("base", xpos="far_left", ypos="head")

    show her_flash_public eyes_open_left mouth_frown zorder 15 as cg
    hide hermione_main
    with fade

    her "So, today I've been standing in one of the corridors near the entrance to the Hufflepuff Common Room, anticipating the moment he usually leaves for class..."
    her "As I waited, I started feeling increasingly worried that something might go wrong..."
    her "And, of course, as I would soon find out, everything that could - did..."
    her "I thought that I had everything planned perfectly, but when the moment of him walking down the corridor finally arrived..."
    her "Well... All my plans sort of fell apart."

    show her_flash_public mouth_soft eyes_open_forward npc_pose1 as cg
    with d5

    her "Once he got close enough, the only thing I managed to let out was a small stutter to try and get his attention."

    show her_flash_public as cg
    with d5

    her "Fortunately for me, it was enough, and he stopped to look at me questioningly."

    show her_flash_public npc_pose2 hermione_pose2 mouth_smile effects_question as cg
    with d5

    her "I wasn't really sure what to say, so I just put on a smile and went for it."
    her "Albeit in my nervousness, I only managed to pull up my vest..."

    show her_flash_public hermione_pose3 eyes_open_right effects_questions as cg
    with d5

    her "During this moment of confusion, I quickly took the opportunity to try and correct my mistake."

    show her_flash_public npc_pose3 hermione_pose4 eyes_clenched blush_heavy effects_exclamation as cg
    with d5

    her "But even then, I only managed to free one of my breasts..."
    her "And as I desperately tried to free the other one--"

    show her_flash_public npc_pose4 eyes_open_left mouth_soft as cg
    with d5

    her "We were suddenly interrupted by the sounds of the other Hufflepuff students footsteps around the corner."
    her "So, before even getting the chance to properly take in his reaction, I had to put my clothes back into place, and quickly."

    show her_flash_public npc_pose3 hermione_pose3 eyes_clenched mouth_soft as cg
    with d5

    pause 1

    # TODO: Man running sounds
    show her_flash_public -npc_pose3 -effects_exclamation eyes_clenched as cg
    with d5

    pause 1

    show her_flash_public hermione_pose1 as cg
    with d5

    pause 1

    show her_flash_public npc_pose5 effects_herquestion eyes_open_forward mouth_frown as cg
    with d5

    her "And neither did I get one afterwards... Once I finished, he was already gone."

    hide cg
    with fade

    her "" ("annoyed", "base", "worried", "R", xpos="mid", ypos="base")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "You've got one tit out at least. As a wise man once said--" ("base", xpos="far_left", ypos="head")
    gen "{i}A tit in the hand is worth two in the bush.{/i}" ("base", xpos="far_left", ypos="head")
    her "I suppose... although I don't know if he ever realised I was trying to do something for his benefit." ("open", "narrow", "worried", "down")
    her "......................" ("annoyed", "base", "worried", "R")
    her "I'm sorry, [name_genie_hermione]..." ("open", "base", "base", "mid")
    gen "That's alright..." ("base", xpos="far_left", ypos="head")

    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "I wouldn't expect you to perform perfectly this early in your training anyway..." ("base", xpos="far_left", ypos="head")
    her "(My training?)" ("angry", "base", "base", "mid")

    $ states.her.status.public_show_tits = True

    jump end_hg_pr_flash

label hg_pr_flash_T3_E3:

    call hg_pr_flash_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I think it went well, [name_genie_hermione]." ("annoyed", "base", "worried", "R")
    gen "Good. Tell me more." ("base", xpos="far_left", ypos="head")
    her "*Ehm*... There is not much to tell, really..." ("open", "base", "base", "mid")
    her "I spent the first half of the day studying in the library..."
    her "It is usually quite deserted during that time..."
    her "Apart from me there was only one other student..."
    her "Some boy from Ravenclaw..." ("upset", "closed", "base", "mid")
    her "So I waved at him, and when I finally had his attention..."
    her "I quickly pulled up my top..." ("angry", "base", "base", "mid")
    gen "Good job." ("base", xpos="far_left", ypos="head")
    gen "How did he react to the sight of your naked tits?" ("base", xpos="far_left", ypos="head")
    her "I'm not sure... I didn't look at him for too long." ("angry", "narrow", "base", "down")
    her "He looked rather shocked I suppose..." ("angry", "base", "base", "mid")
    her "After I showed him my breasts, I got too embarrassed and couldn't bear it any longer..." ("angry", "narrow", "base", "down")
    her "So I just gathered all my books and left..." ("angry", "base", "base", "mid")
    gen "Couldn't bare it any longer... I see..." ("base", xpos="far_left", ypos="head")
    gen "Very well, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_flash

### Tier 4 ###

label hg_pr_flash_T4_E1:

    call hg_pr_flash_intro

    her "..........." ("upset", "base", "worried", "R")
    gen "[name_hermione_genie], did you complete your task or not?" ("base", xpos="far_left", ypos="head")
    her "Yes I did, [name_genie_hermione]." ("upset", "wink", "base", "mid")
    her "............." ("angry", "narrow", "base", "down")
    gen "Well?" ("base", xpos="far_left", ypos="head")
    her "................" ("angry", "narrow", "base", "down")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Just for the record, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
    her "I think that forcing your pupils to do things like this..." ("scream", "closed", "angry", "mid")
    her "Is beneath an esteemed wizard such as yourself..." ("upset", "closed", "base", "mid")
    gen "\"Forcing\"? Nobody is forcing you to do anything, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "You came to me, remember?" ("base", xpos="far_left", ypos="head")
    her ".........." ("open", "base", "base", "mid")
    gen "You begged me to buy a sexual favour from you." ("base", xpos="far_left", ypos="head")
    her "... I--" ("annoyed", "base", "worried", "R")
    her "I never said \"sexual\"..." ("open", "base", "base", "mid")
    gen "Nevertheless, you can stop selling me these favours at any moment, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I suppose..." ("annoyed", "narrow", "angry", "R")
    gen "And yet, you keep on coming back..." ("base", xpos="far_left", ypos="head")
    her "............................" ("angry", "narrow", "base", "down")
    gen "I think you may actually be taking some twisted form of pleasure from this." ("base", xpos="far_left", ypos="head")
    her "What?" ("angry", "base", "angry", "mid")
    gen "Shame on you, [name_hermione_genie]. Shame on you." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione], I never...!" ("angry", "base", "angry", "mid")
    gen "Enough of this. Did you complete your task or not?" ("base", xpos="far_left", ypos="head")
    her "Yes I did..." ("upset", "closed", "base", "mid")
    gen "And?" ("base", xpos="far_left", ypos="head")
    her "And that is all I am going to say..." ("open", "narrow", "worried", "down")
    her "........" ("upset", "closed", "base", "mid")
    gen ".........." ("base", xpos="far_left", ypos="head")
    her "........"
    gen "Oh, whatever. Just take your points and go." ("base", xpos="far_left", ypos="head")
    her "" ("annoyed", "closed", "base", "mid")

    $ states.her.status.public_show_tits = True

    jump end_hg_pr_flash

label hg_pr_flash_T4_E2:

    call hg_pr_flash_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her ".........." ("normal", "happyCl", "worried", "mid")
    gen "................" ("base", xpos="far_left", ypos="head")
    her "..............."
    gen "Well?" ("base", xpos="far_left", ypos="head")
    her "Can I get paid first?" ("open", "base", "base", "mid")
    gen "Not before you tell me what you did today." ("base", xpos="far_left", ypos="head")
    her "...................." ("normal", "happyCl", "worried", "mid")
    her "Do I really have to, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "When you are being coy like this..." ("base", xpos="far_left", ypos="head")
    gen "It only makes me more curious. You know that, right?" ("base", xpos="far_left", ypos="head")
    her "Right..." ("angry", "base", "base", "mid")
    her "Well... *Ehm*..." ("angry", "narrow", "base", "down")
    her "Well, alright, here it goes..."
    her "{size=+4}I flashed my tits to that Slytherin boy!{/size}" ("scream", "happyCl", "worried", "mid")
    gen "..." ("angry", xpos="far_left", ypos="head")
    her "But I made a mistake... I was standing way too close to him..." ("angry", "narrow", "worried", "mid")
    her "So he... He--" ("angry", "closed", "worried", "mid")
    her "He grabbed one of my breasts, [name_genie_hermione]!" ("disgust", "base", "worried", "mid")
    her "And he squeezed it like his life depended on it, and wouldn't let go..." ("disgust", "happyCl", "worried", "mid")
    gen "Sounds like a clear-cut case of childhood trauma." ("base", xpos="far_left", ypos="head")
    her "He even tried to make me promise to meet him after my classes finished for the day..." ("angry", "base", "base", "mid")
    her "And let him..."
    her "\"Play with my tits\" some more..." ("open", "happyCl", "worried", "mid")
    her "You see, this is why I hate Slytherin boys, [name_genie_hermione]..." ("angry", "narrow", "base", "down")
    her "They don't have a shred of honour..."
    her "..."
    gen "So... Did you promise to meet him or not?" ("base", xpos="far_left", ypos="head")
    her "I didn't utter a word to him once he started treating my breast like some sort of squeeze toy..." ("annoyed", "narrow", "base", "R")
    her "That said, I am planning to turn up, and give him a piece of my mind after we are done here, [name_genie_hermione]." ("grin", "closed", "base", "mid")
    gen "A piece of your body, more like..." ("base", xpos="far_left", ypos="head")
    her "What, I'd never--" ("angry", "closed", "angry", "mid")
    gen "Well... Shouldn't keep him waiting." ("base", xpos="far_left", ypos="head")
    her "" ("annoyed", "base", "base", "mid")

    jump end_hg_pr_flash

label hg_pr_flash_T4_E3:

    call hg_pr_flash_intro

    her "It went well." ("open", "base", "base", "mid")
    gen "I'm listening..." ("base", xpos="far_left", ypos="head")
    her "Well..." ("open", "base", "base", "mid")
    her "I had to spend a big portion of the day at the school library..." ("soft", "base", "base", "R")
    her "So I didn't really have the time to perform your task properly, [name_genie_hermione]..." ("angry", "base", "base", "R")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Instead, as I was outside in one of the courtyards..."
    her "... I just pulled my shirt up and pressed my bare chest against the window of a nearby classroom..." ("angry", "narrow", "base", "down")
    her "I stood there like that for several seconds..."
    her "To make sure that at least someone would see them from the outside..."
    her "I hope this still counts, [name_genie_hermione]..." ("angry", "base", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "How many students would you estimate, being behind that window?" ("base", xpos="far_left", ypos="head")
    her "I am not sure, [name_genie_hermione]... A couple maybe...?" ("angry", "narrow", "base", "down")
    gen "\"Maybe\"?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I don't know, [name_genie_hermione]..." ("open", "happyCl", "worried", "mid")
    her "To be honest, I kept my eyes closed..."
    gen "How do you know that anyone saw you at all then, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh! I heard someone shout, \"Look! Over there, behind that window!\"." ("angry", "squint", "base", "mid")
    her "That's when I covered up and sprinted out of there..."
    her "..." ("angry", "base", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Well, alright... In that case, I suppose it counts..." ("base", xpos="far_left", ypos="head")

    $ states.her.ev.admire_breasts.monologue = True

    jump end_hg_pr_flash

### Tier 5 ###

label hg_pr_flash_T5_E1:

    call hg_pr_flash_intro

    her "It went as usual, [name_genie_hermione]..." ("base", "base", "base", "mid")
    gen "I'm listening..." ("base", xpos="far_left", ypos="head")
    her "I had to spend a big portion of the day in the school library..." ("upset", "wink", "base", "mid")
    her "So I didn't really have the time to perform your task properly, [name_genie_hermione]..."
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    her "Instead, I just made sure there were no teachers around..." ("angry", "base", "base", "mid")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Pulled my shirt up..."
    her "And then I just sat there like that for a while..." ("open", "base", "base", "mid")
    her "trying to get some studying done..." ("open", "narrow", "worried", "down")
    her "I don't think there were many people around..."
    her "Or at least I hope so..." ("angry", "narrow", "base", "down")
    her "But they definitely saw my breasts, [name_genie_hermione]..." ("angry", "base", "base", "mid")
    her "Eventually, some first years seemed to notice..." ("angry", "narrow", "base", "down")
    her "Of course... As they noticed, I made it look like it was an accident, and then quickly ran out of there..." ("angry", "base", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "How many people would you say saw your tits today, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Hard to say, [name_genie_hermione]..." ("open", "base", "base", "mid")
    her "Two dozen boys or so, I suppose..." ("open", "base", "base", "mid")
    her "A couple of girls perhaps..." ("annoyed", "base", "worried", "R")
    her "I think the school librarian may have seen me too..."
    gen "*Hmm*... Well, I'd say that's a job well done." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_flash

label hg_pr_flash_T5_E2:

    call hg_pr_flash_intro

    her "It went alright, I suppose." ("open", "closed", "base", "mid")
    gen "Tell me all about it, then." ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Okay..." ("open", "base", "base", "mid")
    her "I flashed my breasts to this boy in the Gryffindor common room..." ("open", "base", "base", "mid")
    her "When a friend of mine... walked in on us..." ("soft", "narrow", "base", "down")
    gen "Another boy? I thought you said it went well?" ("base", xpos="far_left", ypos="head")
    her "A boy? No, this was one of my many female friends, [name_genie_hermione]." ("angry", "narrow", "base", "mid")
    gen "One of your many... Hold on... Why haven't I ever heard--" ("base", xpos="far_left", ypos="head")
    her "Anyway..." ("open", "closed", "angry", "mid")
    gen "Alright, fine, continue..." ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("soft", "base", "base", "R")
    her "......." ("annoyed", "base", "base", "R")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "*Giggle*" ("grin", "happyCl", "worried", "mid",emote="sweat")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    her "So, my friend came up to me and grabbed my breasts..." ("smile", "base", "base", "R")
    her "And then she started squeezing them..." ("smile", "base", "base", "R")
    her "She then started to kiss my breasts passionately..." ("smile", "closed", "base", "R")
    gen "............" ("base", xpos="far_left", ypos="head")
    her "She even started sucking on my nipples..." ("smile", "base", "angry", "mid")
    her "Of course, I couldn't help myself, and I started to moan..." ("base", "narrow", "base", "mid_soft")
    gen ".............." ("base", xpos="far_left", ypos="head")
    her "And then the boy took out his throbbing cock!" ("smile", "squint", "base", "mid")
    her "And sprayed his hot spunk all over us both!" ("smile", "closed", "base", "mid")
    her "And then we licked his hot sperm off each other's bodies..." ("smile", "closed", "angry", "mid")
    gen ".............." ("base", xpos="far_left", ypos="head")
    gen "Are you making this up, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "... Maybe." ("grin", "closed", "worried", "mid", emote="sweat")
    her "I just thought that you would like to hear something like that, [name_genie_hermione]..." ("base", "squint", "base", "mid_soft")
    gen "What I would like to hear, [name_hermione_genie], is the truth." ("base", xpos="far_left", ypos="head")
    her "Even if it's incredibly dull, [name_genie_hermione]?" ("angry", "squint", "base", "mid")
    gen "Dull or not..." ("base", xpos="far_left", ypos="head")
    gen "I only want to know what actually happened..." ("base", xpos="far_left", ypos="head")
    gen "Keep your fantasies to yourself, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "As you wish, [name_genie_hermione]." ("annoyed", "narrow", "worried", "R")
    her "My friend walked in on me while I was flashing my tits to that guy." ("open", "narrow", "worried", "mid")
    her "But since she came up behind me, I managed to put them away..." ("open", "base", "worried", "R")
    her "And that's all that happened, [name_genie_hermione]..." ("soft", "base", "base", "mid")
    gen "Exciting..." ("base", xpos="far_left", ypos="head")
    her "You think so, [name_genie_hermione]?" ("angry", "base", "base", "mid")
    gen "Of course, [name_hermione_genie]... Did you not find it exciting?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... I suppose..." ("soft", "narrow", "base", "down")

    jump end_hg_pr_flash

label hg_pr_flash_T5_E3:

    call hg_pr_flash_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her @ cheeks blush "*Hmm*..." ("base", "narrow", "base", "down")
    gen "How did it go, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh, *Ehm*... let's see..." ("soft", "narrow", "base", "down")
    her @ cheeks blush "First I flashed them to that one boy from Slytherin... You know, the one who grabbed my breasts." ("open", "base", "base", "mid")
    her @ cheeks blush "Then to that Hufflepuff guy who I previously flashed in the corridor outside the Hufflepuff common room..." ("open", "closed", "base", "mid")
    her @ cheeks blush "Then there was this boy from Ravenclaw that I previously flashed inside the library..." ("open", "base", "base", "R")
    gen "???" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "After that, I flashed them to that Gryffindor underclassman who I told you about the other day..." ("open", "base", "base", "mid", emote="sweat")
    her @ cheeks blush "No, wait... The boy from Gryffindor was after that other boy..." ("angry", "base", "worried", "R")
    gen "How many boys did you flash your tits to, [name_hermione_genie]?!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh... Well, that's about all of them..." ("angry", "base", "base", "mid")
    her @ cheeks blush "I had an opening in my schedule... And I figured I'd give them another look..." ("angry", "squint", "base", "mid")
    her @ cheeks blush "I mean, that's the least I could do... Seeing that I wasn't actually pursuing any of them." ("soft", "squint", "base", "R")
    gen "Yes... Doing it again certainly won't give them that idea..." ("base", xpos="far_left", ypos="head")
    her "Anyway... I figured that you may want to give me a good grade since I went well beyond what was required from my assignment, [name_genie_hermione]." ("open", "squint", "base", "mid")
    gen "This is not an assignment, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "There is no grading..." ("base", xpos="far_left", ypos="head")
    her "Oh..." ("open", "narrow", "base", "down")
    gen "You are doing this for points, [name_hermione_genie]... Not a grade..." ("base", xpos="far_left", ypos="head")
    her "Oh... Right..." ("annoyed", "base", "worried", "R")
    gen "But, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "If you were to receive a grade... It'd be a high one." ("grin", xpos="far_left", ypos="head")
    her "I see... Well, I guess that will have to do..." ("grin", "narrow", "base", "mid_soft")

    jump end_hg_pr_flash
