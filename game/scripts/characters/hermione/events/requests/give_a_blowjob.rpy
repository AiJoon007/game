
### Give Classmate A Blowjob ###

label start_hg_pr_blowjob:

    # Setup
    $ current_payout = 65

    if not _events_completed_any:
        gen "{size=-4}(Tell her to go give a blowjob to one of her classmates?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    return

label hg_pr_blowjob:

    call start_hg_pr_blowjob

    her "" (xpos="mid", ypos="base", trans=fade)

    #Intro.
    if not _events_completed_any:
        gen "[name_hermione_genie], I will be buying another favour from you today." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]... I really appreciate it." ("open", "closed", "base", "mid")
        gen "Happy to help, as always." ("base", xpos="far_left", ypos="head")
        her "So, what can I do for you today?" ("open", "base", "base", "mid")
        gen "I need you to go give a blowjob to one of your classmates." ("base", xpos="far_left", ypos="head")

        stop music fadeout 1.0
        her "!!!" ("shock", "wide", "base", "stare")
        her "... With my mouth?"

        if not states.her.status.blowjob: # She will refuse unless she gave you a blowjob (event canceled)
            her "But we--.. I.." ("shock", "wide", "base", "stare")
            her "I've never done it before!" ("angry", "wide", "base", "mid")
            gen "Then I guess it's time you learnt what {i}using your head{/i} truly means." ("base", xpos="far_left", ypos="head")
            her "But..." ("annoyed", "narrow", "worried", "R")
            her "No, I'm sorry [name_genie_hermione]... I can't do this!" ("annoyed", "narrow", "worried", "R")

            call her_walk(action="leave")

            $ states.her.mood += 9

            gen "(*Hmm*...)" ("base", xpos="far_left", ypos="head")
            gen "(Perhaps I should show her the ropes first before sending her off to blow her classmates.)" ("base", xpos="far_left", ypos="head")

            $ _event.cancel()
            jump end_hermione_event

        if states.her.public_level < 15:
            $ _event.cancel()
            jump too_much_public

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
        gen "Yes, that's how it's usually done..." ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione], I..." ("upset", "closed", "base", "mid")
        her @ cheeks blush "I refuse to sell you a depraved favour like that, [name_genie_hermione]." ("open", "narrow", "annoyed", "mid")
        her "Can't I just kiss a girl or something, instead?" ("open", "happyCl", "worried", "mid")
        her "I do not mind that..." ("open", "narrow", "annoyed", "mid")
        gen "[name_hermione_genie], please stop wasting my time..." ("base", xpos="far_left", ypos="head")
        gen "If you are not in the mood to sell favours today..." ("base", xpos="far_left", ypos="head")
        gen "Then there is the door." ("base", xpos="far_left", ypos="head")
        her "But I need the points, [name_genie_hermione]... You know that." ("upset", "closed", "base", "mid")
        gen "It's as the saying goes, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        gen "\"If you won't suck a dick for it - You don't need it\"." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Tch*..." ("angry", "base", "angry", "mid")
        her "............................"
        gen ".........................................." ("base", xpos="far_left", ypos="head")
        her "... Alright." ("annoyed", "narrow", "angry", "R")
        her "I'll do it..." ("annoyed", "narrow", "angry", "R")
        gen "Go do it, then!" ("base", xpos="far_left", ypos="head")
        gen "Report back to me after your classes." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("angry", "base", "angry", "mid")
        her "....." ("angry", "base", "angry", "mid")
        her "......." ("angry", "base", "angry", "mid")
        gen "You may leave, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "..." ("angry", "base", "angry", "mid")
    else:
        if states.her.tier >= 6:
            play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
            gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
            gen "Do you believe in horoscopes?" ("base", xpos="far_left", ypos="head")
            her "Not even a little bit, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
            gen "Well, maybe you should..." ("base", xpos="far_left", ypos="head")
            her "...?" ("open", "base", "base", "mid")
            gen "Because I got yours right here and it says..." ("base", xpos="far_left", ypos="head")
            gen "\"Dedicate today to something you do well\"..." ("base", xpos="far_left", ypos="head")
            her "Something I do well...?" ("soft", "base", "base", "R")
            gen "Go suck on some cocks, [name_hermione_genie]." ("grin", xpos="far_left", ypos="head")
            her "....................." ("annoyed", "narrow", "annoyed", "mid") # :(
            gen "Report back to me after your classes as usual..." ("base", xpos="far_left", ypos="head")
            her "Of course..." ("annoyed", "narrow", "angry", "R")
        else:
            gen "Go give some lucky boy another blowjob, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "...... Again?" ("disgust", "narrow", "base", "mid_soft")
            gen "Yes, again." ("base", xpos="far_left", ypos="head")
            her ".........." ("annoyed", "narrow", "annoyed", "mid")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_blowjob_fail:
    call start_hg_pr_blowjob

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "Yes?" ("open", "squint", "base", "mid")
    gen "Don't you think it's about time you put that mouth to good use, by sucking off one of your classmates?" ("base", xpos="far_left", ypos="head")

    jump too_much_public

label end_hg_pr_blowjob:
    $ gryffindor += current_payout

    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if not _events_completed_any:
        $ states.her.status.public_blowjob = True

        her "(I did it...)" ("base", "narrow", "base", "dead", xpos="base", ypos="base", flip=True, trans=d3)
        her "(I sucked off one of my classmates...)" ("angry", "narrow", "base", "dead")

    call her_chibi("leave")

    label .quick_end:

    $ hermione.set_cum(None)

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    jump end_hermione_event

label hg_pr_blowjob_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("soft", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you complete your assignment?" ("base", xpos="far_left", ypos="head")

    if _events_filtered_completed_all:
        her "Yes, [name_genie_hermione]."

        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_blowjob

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("annoyed", "narrow", "angry", "R")
        gen ".............." ("base", xpos="far_left", ypos="head")

    gen "[name_hermione_genie], how did it go?" ("base", xpos="far_left", ypos="head")

    return

### Tier 5 ###

label hg_pr_blowjob_T5_E1:

    call hg_pr_blowjob_intro

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    gen "You know the drill, [name_hermione_genie]. Start talking." ("base", xpos="far_left", ypos="head")
    her "I gave a blowjob, [name_genie_hermione]..." ("disgust", "narrow", "base", "mid_soft")
    gen "Good... Tell me more." ("base", xpos="far_left", ypos="head")
    her "What is there to tell, [name_genie_hermione]?" ("annoyed", "narrow", "angry", "R")
    her "I sucked off one of my classmates today..." ("annoyed", "narrow", "angry", "R")
    her "And that's it..." ("annoyed", "narrow", "angry", "R")
    gen "*Hmm*... I see..." ("base", xpos="far_left", ypos="head")
    gen "..............." ("base", xpos="far_left", ypos="head")
    her "...................................." ("angry", "narrow", "base", "down")
    gen "Did you swallow?" ("base", xpos="far_left", ypos="head")
    her "..........................." ("annoyed", "narrow", "annoyed", "mid")
    gen "[name_hermione_genie], did you swallow the load properly?" ("base", xpos="far_left", ypos="head")
    her "I... I didn't... [name_genie_hermione]." ("angry", "base", "angry", "mid")
    gen "Well, I suppose that will do for now..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_blowjob

label hg_pr_blowjob_T5_E2:

    call hg_pr_blowjob_intro

    her "[name_genie_hermione], I..." ("angry", "narrow", "base", "down")
    her "I tried, but..." ("angry", "narrow", "base", "down")
    play music "music/Despair_by_erenik.ogg" fadein 1 if_changed # Music
    her @ tears soft "The boy turned me down, [name_genie_hermione]..." ("mad", "base", "worried", "mid")
    her @ tears soft "I cannot believe that actually happened..." ("angry", "base", "base", "mid")
    her "I am one of the top students in this school!" ("angry", "base", "base", "mid")
    her "One of the most popular ones too..." ("angry", "base", "base", "mid")
    her @ tears soft "And he turns me down?" ("angry", "base", "angry", "mid")
    her "Why would he insult me like that?!" ("angry", "base", "angry", "mid")
    gen "So you're insulted because that boy refused to put his cock in your mouth?" ("base", xpos="far_left", ypos="head")
    her @ tears crying "Wouldn't you be, [name_genie_hermione]?" ("angry", "base", "angry", "mid")
    gen "I... I never considered that option myself, but I think I would get over it rather quickly..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "He rejected me, [name_genie_hermione]..." ("angry", "base", "angry", "mid")
    her "Who does he think he is?!" ("angry", "base", "angry", "mid")
    her @ cheeks blush "With all due respect, [name_genie_hermione], you wouldn't understand..." ("open", "narrow", "annoyed", "mid")
    gen "Well, in any case. I can't pay you for this." ("base", xpos="far_left", ypos="head")
    her @ tears soft "Of course... I would not expect you to, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
    her @ tears soft "I failed to complete my task and deserve no praise of any kind..." ("annoyed", "narrow", "annoyed", "mid")
    her @ tears soft "And should you pay me out of pity..." ("annoyed", "narrow", "annoyed", "mid")
    her "Then that would only worsen the insult..." ("annoyed", "narrow", "angry", "R")
    gen "*Hmm*... In that case, maybe I should pay you anyway..." ("base", xpos="far_left", ypos="head")
    her "No, [name_genie_hermione]... I would not accept it..." ("annoyed", "narrow", "annoyed", "mid")
    gen "*Hmm*... Well, this will be all then." ("base", xpos="far_left", ypos="head")
    her "Have a good night, [name_genie_hermione]." ("open", "closed", "base", "mid")

    jump end_hg_pr_blowjob.no_points


label hg_pr_blowjob_T5_E3:

    call hg_pr_blowjob_intro

    her "I still find the idea of performing a favour like this unappealing, [name_genie_hermione]." ("annoyed", "narrow", "angry", "R")
    her "But it went surprisingly well..." ("annoyed", "narrow", "annoyed", "mid")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed

    her "I gave a proper blowjob to this handsome boy from Ravenclaw..." ("annoyed", "narrow", "annoyed", "mid")
    her "And he was such a gentleman about it..." ("open", "narrow", "worried", "down")
    her "He even warned me when he was about to finish." ("angry", "narrow", "base", "down")
    gen "A sign of a true gentleman indeed." ("base", xpos="far_left", ypos="head")
    gen "Did you swallow?" ("base", xpos="far_left", ypos="head")
    if states.her.status.gokkun:
        her "Of course I did, [name_genie_hermione]." ("upset", "closed", "base", "mid")
        her "I told you -- I gave the boy a {b}proper{/b} blowjob." ("upset", "closed", "base", "mid")
        her "It's the least I could do for someone who treated me with respect for a change..." ("angry", "narrow", "base", "down")
        gen "Well, in that case." ("base", xpos="far_left", ypos="head")

        $ states.her.status.public_gokkun = True
    else:
        her "Oh... *Ehm*..." ("angry", "base", "base", "R")
        gen "Did you not say that you gave him a {b}proper{/b} blowjob?" ("base", xpos="far_left", ypos="head")
        her "I did say that, I just didn't--" ("annoyed", "base", "base", "mid")
        her "I panicked, okay?" ("angry", "base", "base", "mid")
        her "I had never done that before, so when the moment came..." ("angry", "base", "base", "R")
        gen "You mean when the boy came..." ("base", xpos="far_left", ypos="head")
        her "..." ("disgust", "base", "base", "mid")
        gen "Oh, well... I suppose not everyone can be perfect... At least you did the actual sucking." ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "narrow", "base", "down")

    jump end_hg_pr_blowjob

### Tier 6 ###

label hg_pr_blowjob_T6_intro_E1:

    call hg_pr_blowjob_intro

    her "Splendid, [name_genie_hermione]...{w=0.4} Simply splendid." ("base", "happyCl", "base", "mid")
    gen "Really? Do tell." ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Today I did something I have wanted to do for a long time..." ("base", "narrow", "base", "up")
    her "Something I've never been able to muster up enough courage for..." ("base", "narrow", "base", "up")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    her "Today I sucked off two of my classmates at the same time!" ("soft", "narrow", "annoyed", "up")
    her "And it was every bit as exciting as I thought it would be." ("base", "narrow", "worried", "down")
    gen "At the same time, you say?" ("base", xpos="far_left", ypos="head")
    her "Well, I was periodically moving between them... But I'm sure you know what I meant..." ("base", "narrow", "worried", "down")
    gen "Impressive... I presume you had to do this for quite a while, before they finished?" ("base", xpos="far_left", ypos="head")
    her "*Mmm*... Yes, it did take quite a while..." ("base", "narrow", "worried", "dead")
    her "By the end, their cocks were all sloppy with saliva..." ("grin", "narrow", "base", "dead")
    her "And their balls as well..." ("grin", "narrow", "base", "dead")
    gen "By the end, you say? So, you made sure to swallow?" ("base", xpos="far_left", ypos="head")
    her "Of course, [name_genie_hermione]! Since there were two of them... Who knows how much of a mess they would've made otherwise." ("grin", "closed", "base", "dead")
    gen "So, you only did it to avoid a mess?" ("base", xpos="far_left", ypos="head")
    her "Well, there was that... I was also wanted to see the surprised look on their faces when I swallowed..." ("angry", "narrow", "base", "R")
    her "When I did it, they looked at if they couldn't believe it was actually happening..."
    her "To be honest, neither could I..." ("base", "closed", "base", "dead")
    her "Me... Hermione Granger... The girl they've spent years alongside..."
    her "Sucking their cocks..." ("open_wide_tongue", "narrow", "annoyed", "up")
    her @ cheeks blush "Like some nasty slut..." ("angry", "narrow", "base", "up")
    her "Of course, I made them promise not to tell anyone..." ("open", "closed", "annoyed", "mid")
    gen "Are you in love with those boys, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "I don't know about that, [name_genie_hermione]... But I surely enjoyed the experience..." ("base", "wink", "base", "mid")
    her "Could I get paid now, please?"
    gen "Sure..." ("base", xpos="far_left", ypos="head")

    $ states.her.status.public_gokkun = True

    jump end_hg_pr_blowjob

label hg_pr_blowjob_T6_E2:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    $ hermione.set_cum(hair="heavy", face="heavy")

    her "" ("angry", "base", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    pause 1.0

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "You look like you've been through hell..." ("base", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her @ tears soft "[name_genie_hermione], I... Yes, thanks to that Slytherin boy..." ("angry", "narrow", "angry", "mid")
    gen "A Slytherin did this?{w=0.4} Seriously?!" ("angry", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
    her "A nasty boy from Slytherin seemed to take a fancy to my face..." ("annoyed", "narrow", "annoyed", "mid")
    her "Or...{w=0.5} My mouth rather I suppose..." ("disgust", "narrow", "annoyed", "down")
    her "And--" ("open", "narrow", "annoyed", "down")
    play sound "sounds/burp.ogg"
    her "*Burp*!..." ("full", "happyCl", "worried", "mid")
    her "{i}Excuse moi{/i}." ("angry", "narrow", "annoyed", "R")
    her "Anyway... He came so much I was barely able to swallow it all..." ("angry", "closed", "annoyed", "mid", emote="angry")
    her "Bloody bastard!" ("scream", "base", "angry", "mid", emote="angry")
    her @ cheeks blush "You think I could file a complaint, [name_genie_hermione]?" ("angry", "base", "angry", "mid")
    gen "*Hmm*... I suppose..." ("base", xpos="far_left", ypos="head")
    gen "But keep in mind that the moment we bring the ministry into this..." ("base", xpos="far_left", ypos="head")
    gen "All this \"favour selling business\" will have to stop immediately." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh... Right..." ("open", "base", "base", "R")
    her ".................." ("open", "base", "base", "R")
    her "Please, never mind what I just said then..." ("angry", "happyCl", "base", "mid")
    gen "Are you sure? You look pretty messed up." ("base", xpos="far_left", ypos="head")
    her "No, no. It's nothing really..." ("smile", "happyCl", "base", "mid")
    her "After all... I was the one who offered him a free blowjob..." ("smile", "happyCl", "base", "mid")
    her "He just got a bit rough with me towards the end, that's all..." ("smile", "squint", "worried", "mid")
    her "I think I am just overreacting..." ("smile", "narrow", "worried", "R")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    her "Can I just--" ("angry", "narrow", "base", "mid")

    play sound "sounds/burp.ogg"

    her "*Burp*!..." ("full", "wide", "base", "stare")
    her "Excuse me, [name_genie_hermione]." ("angry", "narrow", "base", "down")
    her "{size=-3}(He just kept on cumming... My stomach feels so full...){/size}" ("disgust", "happyCl", "worried", "mid", emote="sweat")
    her "Can I get my payment now, please?" ("angry", "base", "base", "mid")
    gen "Of course..." ("base", xpos="far_left", ypos="head")

    $ states.her.status.public_cumshot = True

    jump end_hg_pr_blowjob

label hg_pr_blowjob_T6_E3:

    # Special intro
    stop music fadeout 3.0
    call her_walk(action="enter", xpos="mid", ypos="base")

    $ hermione.set_cum("heavy")

    her "" ("base", "narrow", "base", "up", xpos="mid", ypos="base", trans=d3)
    pause 1.0

    her "Good evening, [name_genie_hermione]..." ("base", "narrow", "base", "up")
    gen "Hermione?!" ("angry", xpos="far_left", ypos="head")
    gen "What happened to you?" ("angry", xpos="far_left", ypos="head")
    gen "All I asked you to do was to give a blowjob to one of your classmates." ("angry", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "That...{w=0.4} That was exactly what I did, [name_genie_hermione]." ("grin", "narrow", "base", "up")
    gen "[name_hermione_genie], you are covered head to toe in cum..." ("base", xpos="far_left", ypos="head")
    her "I am?" ("angry", "narrow", "worried", "dead")
    her "Oh... Did I forget to clean myself up?" ("soft", "narrow", "worried", "down")
    her "How embarrassing..." ("base", "narrow", "base", "mid_soft")
    her "That thing inside the boy's restroom sort of escalated I suppose..." ("soft", "narrow", "base", "R")
    her "Before I knew what happened I was surrounded by hard, throbbing, cocks..." ("base", "narrow", "base", "up")
    her "Oh... Just talking about it makes me shiver with excitement... *Err*..." ("silly", "narrow", "base", "dead")
    her "I mean, with fear... No... Not fear..." ("grin", "narrow", "annoyed", "up")
    her @ cheeks blush "Embarrassment...? No, that's not it either... *Hmm*..." ("base", "narrow", "base", "up")
    gen "Are you asking me?" ("base", xpos="far_left", ypos="head")
    her "Oh, excuse me, [name_genie_hermione]... I feel a little lightheaded..." ("grin", "narrow", "base", "dead")
    her "I think I need to go lie down for a while..."
    gen "Don't miss the shower room this time." ("base", xpos="far_left", ypos="head")
    her "The shower room? Why?" ("soft", "narrow", "worried", "mid_soft")
    gen "Forget I said anything..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_blowjob
