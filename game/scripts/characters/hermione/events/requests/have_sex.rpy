
### Have Sex With A Classmate ###

label start_hg_pr_sex:

    # Setup
    $ current_payout = 75

    if not _events_completed_any:
        gen "{size=-4}(Tell her to fuck one of her classmates?){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    return

label hg_pr_sex:

    call start_hg_pr_sex

    her "" (xpos="mid", ypos="base", trans=fade)

    #Intro.
    if not _events_completed_any:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "Today I need you to have sex with a classmate of your choice." ("base", xpos="far_left", ypos="head")

        if not states.her.status.sex: # She will refuse unless she slept with you
            her "But we--{w=0.2} I..." ("shock", "wide", "base", "stare")
            her "I've never done it before!" ("angry", "wide", "base", "mid")
            gen "So?" ("base", xpos="far_left", ypos="head")
            her "{size=+5}\"So\"?!{/size}" ("annoyed", "narrow", "angry", "R")
            her "I'm leaving this instant." ("scream", "closed", "angry", "mid")

            call her_walk(action="leave")

            $ states.her.mood += 16

            gen "(*Hmm*...)" ("base", xpos="far_left", ypos="head")
            gen "(Maybe she'll be up for it if I pop her cherry first...)" ("base", xpos="far_left", ypos="head")

            $ _event.cancel()
            jump end_hermione_event

        if states.her.public_level < 18:
            $ _event.cancel()
            jump too_much_public

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
        her ".............." ("angry", "base", "angry", "mid")
        her "I had the feeling that we would get to this sooner or later..." ("disgust", "narrow", "base", "mid_soft")
        her "But..." ("annoyed", "narrow", "angry", "R")
        her "..................."
        gen "If you do this, Gryffindor will be getting {number=current_payout} points tonight." ("base", xpos="far_left", ypos="head")
        her "Very well...{w=0.4} I will do it, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
        gen "Great... See you after your classes then." ("base", xpos="far_left", ypos="head")
        her "............." ("upset", "closed", "base", "mid")
    else:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "I need you to go have sex with another classmate of yours." ("base", xpos="far_left", ypos="head")
        her "Again, [name_genie_hermione]?" ("angry", "base", "base", "mid")
        gen "Yes. And you will get {number=current_payout} points again as well." ("base", xpos="far_left", ypos="head")
        her "Well, alright..." ("annoyed", "narrow", "base", "R")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_sex_fail:
    call start_hg_pr_sex

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "squint", "base", "mid")
    gen "You seem a bit uptight... Why don't you take the day off, to have sex with one of your classmates." ("base", xpos="far_left", ypos="head")

    jump too_much_public

label end_hg_pr_sex:
    $ gryffindor += current_payout
    gen "Gryffindor gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if _events_completed_all:

        her "(I did it... I finally did it.)" ("grin", "narrow", "base", "dead", xpos="base", ypos="base", flip=True, trans=d3)

    call her_chibi("leave")

    label .quick_end:

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    $ states.her.status.public_sex = True
    jump end_hermione_event

label hg_pr_sex_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("open", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you do it?" ("base", xpos="far_left", ypos="head")

    if _events_filtered_completed_all:
        her "Of course, [name_genie_hermione]."
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_sex

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("base", "narrow", "base", "mid")

    gen "Have you been enjoying yourself today?" ("base", xpos="far_left", ypos="head")

    return

### Tier 6 ###

label hg_pr_sex_T6_intro_E1:

    gen "....." ("base", xpos="far_left", ypos="head")
    gen ".........." ("base", xpos="far_left", ypos="head")
    gen "Hermione was supposed to be here, by now..." ("base", xpos="far_left", ypos="head")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

    $ states.her.busy = True
    
    jump main_room_menu

label hg_pr_sex_T6_intro_E2:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    gen "[name_hermione_genie], you missed your debriefing yesterday." ("base", xpos="far_left", ypos="head")
    gen "Explain yourself." ("base", xpos="far_left", ypos="head")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "Yes, [name_genie_hermione], I apologise... *Yawn*..." ("open", "closed", "base", "mid", xpos="mid", ypos="base", trans=d3)
    gen "Care to explain yourself?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course, [name_genie_hermione]." ("open", "happy", "base", "mid")
    her @ cheeks blush "It is sort of embarrassing, though..." ("base", "base", "base", "R")
    her @ cheeks blush "I didn't spend the night alone..." ("open", "happy", "base", "mid")
    gen "A slumber party with some girlfriends, *huh*?" ("base", xpos="far_left", ypos="head")
    her "Girlfriends?" ("angry", "wink", "base", "mid")
    her @ cheeks blush "No, [name_genie_hermione]... What I'm saying is..." ("open", "base", "base", "R")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I spent the night with a boy... Actually, a couple of boys to be precise..." ("base", "base", "base", "R")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    gen "A couple of them? And here I thought you had skipped out on your assignment." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, that's what I did initially... But then late last night..." ("angry", "narrow", "base", "R")
    her @ cheeks blush "Well, something came over me and I allowed these boys to make me their little plaything..." ("angry", "closed", "base", "mid_soft")
    gen "*Hmm*... You did, did you?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, I was a bit nervous at first, but after a while I did not mind it one bit..." ("soft", "closed", "base", "dead")
    her @ cheeks blush "They did everything they wanted to do to me..." ("base", "closed", "base", "dead")
    her @ cheeks blush "And everything I wanted to be done to me has been done..." ("grin", "closed", "base", "dead")
    her @ cheeks blush "................." ("soft", "narrow", "worried", "up")
    her "Will I get paid for this, [name_genie_hermione]?" ("angry", "wink", "base", "mid")

    jump end_hg_pr_sex

label hg_pr_sex_T6_E3:

    call hg_pr_sex_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I did it, [name_genie_hermione]." ("upset", "closed", "base", "mid")
    her @ cheeks blush "And in the school library of all places..." ("open", "narrow", "annoyed", "mid")
    her @ cheeks blush "At first I was kind of worried that we would make too much noise..." ("open", "narrow", "worried", "R")
    her "But the boy literally lasted only one minute, [name_genie_hermione]." ("soft", "closed", "annoyed", "R")
    gen "Don't hold it against him, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "You are quite attractive... So, he probably got too excited..." ("base", xpos="far_left", ypos="head")
    her "Merely a dozen of rather mediocre thrusts, and he is finished?" ("upset", "closed", "base", "mid")
    her "As a girl, I cannot help but feel disappointed..." ("annoyed", "narrow", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "What did you do afterwards?" ("base", xpos="far_left", ypos="head")
    gen "Pulled up your panties and went about your business as if nothing happened?" ("base", xpos="far_left", ypos="head")
    her "My panties?" ("open", "narrow", "worried", "down")
    her "I wasn't wearing any panties, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    her "In fact, I didn't wear them the entire day..." ("annoyed", "narrow", "angry", "R")
    gen "Oh really?" ("base", xpos="far_left", ypos="head")
    her "Yes... It felt quite empowering, actually..." ("open", "closed", "annoyed", "mid")
    gen "Good for you, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    if hermione.is_worn("panties"):
        her "It's not really a problem for me if you want me to avoid wearing them in here as well..." ("annoyed", "narrow", "base", "R")
        gen "I'll consider it..." ("base", xpos="far_left", ypos="head")
    else:
        gen "So, are you feeling empowered right now, as well?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*... Yes, perhaps a little bit..." ("base", "narrow", "base", "R")

    gen "Very well, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_sex

label hg_pr_sex_T6_E4:

    call hg_pr_sex_intro

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "I did it, [name_genie_hermione]." ("upset", "closed", "base", "mid")
    her "I took one of the Ravenclaw boys to the girl's restroom..." ("base", "narrow", "worried", "down")
    her "... and let him have his way with me in one of the stalls."
    gen "Well done, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "....................." ("annoyed", "narrow", "angry", "R")
    gen "I said you did great... What's with the face?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Well..." ("open", "closed", "base", "R")
    her "I am getting paid well for performing these tasks..." ("soft", "closed", "base", "R")
    her "So I shouldn't really have any right to complain, but..." ("angry", "narrow", "base", "R")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "My reputation is starting to suffer, and it troubles me, [name_genie_hermione]..." ("open", "base", "base", "mid")
    gen "Your reputation?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, yes... *Ehm*..." ("open", "base", "base", "R")
    gen ".............." ("base", xpos="far_left", ypos="head")
    her "No, sorry, please disregard what I just said, [name_genie_hermione]." ("upset", "closed", "base", "mid")
    gen "(At this point I'm not so sure she has any reputation left.)" ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_sex
