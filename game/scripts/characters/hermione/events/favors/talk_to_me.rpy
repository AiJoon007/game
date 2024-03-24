
### Hermione 'Talk to me' ###

label start_hg_pf_talk:
    if not _events_completed_any:
        gen "{size=-4}(All I'll do is have an innocent conversation with her...){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    $ current_payout = 5
    return

label end_hg_pf_talk:

    # Setup
    stop music fadeout 2.0
    call hide_characters
    show screen blkfade
    with d3

    call her_chibi("stand", flip=False)
    call gen_chibi("sit_behind_desk")
    her "" (xpos="mid", ypos="base")

    hide screen blkfade
    with d3

    # Points
    if states.her.tier <= 3:
        $ gryffindor += current_payout
        gen "{number=current_payout} points to Gryffindor, [name_hermione_genie]. Well done." ("base", xpos="far_left", ypos="head")
    elif states.her.tier == 4 and not _events_filtered_completed_any:
        gen "{number=current_payout} points to Gryff--" ("base", xpos="far_left", ypos="head")
        her "Oh, don't worry about the points, [name_genie_hermione]. We were just having a nice talk."
        gen "Really? What about Gryffindor winning the cup?" ("base", xpos="far_left", ypos="head")
        her "It's only {number=current_payout} points..." ("soft", "base", "base", "R")
        gen "If you say so." ("base", xpos="far_left", ypos="head")

    if states.her.mood != 0:
        her "Will this be all then?" ("annoyed", "base", "angry", "mid")
    else:
        her "Will this be all then?" ("soft", "base", "base", "mid")
    gen "Yes, you can go now." ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    # Hermione leaves
    call her_walk("door", "base")

    if states.her.tier == 1 and not _events_completed_any:
        her "Another {number=current_payout} points... The Guys will be so happy!" ("base", "happyCl", "base", "mid")

    call her_chibi("leave")

    # Increase level
    if states.her.tier == 1:
        if states.her.level < 3: # Points til 3
            $ states.her.level += 1

    if states.her.tier == 2:
        if states.her.level < 9: # Points til 9
            $ states.her.level += 1

    jump end_hermione_event

### Tier 1 ###

label hg_pf_talk_T1_intro_E1:

    call start_hg_pf_talk

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    gen "Alright then..." ("base", xpos="far_left", ypos="head")
    gen "Just tell me some news about yourself." ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Alright..." ("open", "squint", "base", "mid")
    her "I just stand here and talk then...? Like this?" ("base", "squint", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause.8

    gen "Well?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... very well..." ("open", "base", "worried", "mid")
    nar "Hermione is feeling confused..."
    her "..................." ("annoyed", "narrow", "angry", "R")

    call hg_pf_talk_T1

    jump end_hg_pf_talk


label hg_pf_talk_T1_E1:

    call start_hg_pf_talk

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    gen "Alright then..." ("base", xpos="far_left", ypos="head")
    gen "Just tell me some more news about yourself." ("base", xpos="far_left", ypos="head")
    her "Here in the middle, right? I remember..." ("open", "squint", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause.8

    gen "Yes?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... very well..." ("open", "base", "worried", "mid")

    call hg_pf_talk_T1

    jump end_hg_pf_talk


label hg_pf_talk_T1: # Call label
    her "My life has been quite uneventful lately, to be honest..." ("annoyed", "narrow", "angry", "R")
    her "Apart from the day when I failed that test..." ("open", "closed", "base", "mid")
    her "I still can't believe it happened..." ("annoyed", "narrow", "angry", "R")

    menu:
        "-Jerk off while she is talking-":
            $ states.gen.stats.masturbated_to_hermione += 1
            $ states.gen.masturbating = True

            hide hermione_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8

            her "[name_genie_hermione], what are you doing?" ("open", "base", "base", "mid", xpos="mid", trans=d3)
            gen "What? Oh, it's nothing. Just scratching my leg." ("base", xpos="far_left", ypos="head")
            gen "You were saying?" ("base", xpos="far_left", ypos="head")
            her "Yes... Well, that test I failed..." ("open", "base", "base", "mid")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False #NOT JERKING OFF.
            gen "Yes, what a tragedy that was..." ("base", xpos="far_left", ypos="head")
            her "Exactly! I'm glad you understand, [name_genie_hermione]." ("open", "base", "angry", "mid")

    her "Come to think of it, I don't feel like talking about it anymore..." ("annoyed", "narrow", "worried", "down")
    gen "Alright, what else has happened lately?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Well, I'm doing pretty well at Herbology..." ("annoyed", "base", "base", "R")
    her "I mean, I always score the top marks, but I have been studying really hard anyway..." ("open", "closed", "base", "mid")
    her "And now I sort of feel like sometimes I know more than professor Sprout herself..." ("base", "base", "base", "mid")

    if states.gen.masturbating:
        gen "{size=-4}(Yes... *Ah*...){/size}" ("base", xpos="far_left", ypos="head")
    else:
        gen "(Professor Sprout... *He-he*, what a ridiculous name...)" ("grin", xpos="far_left", ypos="head")

    her "Did you say something, [name_genie_hermione]?" ("normal", "squint", "angry", "mid")
    gen "It's nothing, keep going..." ("base", xpos="far_left", ypos="head")
    her "Well, some students are making fun of professor Quirrell behind his back..." ("open", "base", "base", "mid")

    her "I disapprove of such behaviour, of course." ("base", "closed", "base", "mid")
    if states.gen.masturbating:
        gen "{size=-4}(Come on! Say something naughty!){/size}" ("base", xpos="far_left", ypos="head")
    else:
        gen ".................." ("base", xpos="far_left", ypos="head")

    her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..." ("open", "base", "base", "mid")
    her "I'm very happy about that..." ("smile", "base", "base", "R")
    her "I think, given time, we will be able to make a real difference..." ("open", "closed", "base", "mid")
    her "It is so invigorating to know that you are doing the right thing!" ("base", "base", "base", "mid")
    her "Wouldn't you agree, professor?" ("base", "base", "base", "mid")

    if states.gen.masturbating:
        $ states.gen.masturbating = False
        gen "{size=-4}(Dammit. Now she's killed the mood completely...){/size}" ("base", xpos="far_left", ypos="head")
        call gen_chibi("sit_behind_desk")
        with d3
        pause.8
    else:
        gen "*Snore*........" ("base", xpos="far_left", ypos="head")

    her "[name_genie_hermione]?" ("angry", "base", "angry", "mid")
    gen "Yes, yes, I'm totally listening..." ("base", xpos="far_left", ypos="head")
    gen "This is all very self-righteous, er..." ("base", xpos="far_left", ypos="head")
    gen "I mean, very invigorating and stuff..." ("base", xpos="far_left", ypos="head")
    her ".........................." ("normal", "squint", "angry", "mid")

    return



### Tier 2 ###

# Hermione realises you've been jerking off this whole time!
# 'states.her.status.voyer' is required to advance into the next tier.
# Event 1 (i) - Hermione can spot you jerking off.
# Event 2 (r) - Slight dialogue variation if you've been busted jerking off before.

label hg_pf_talk_T2_intro_E1:

    call start_hg_pf_talk

    her "Very well, Sir." ("base", "base", "base", "mid")

    call hg_pf_talk_T2

    jump end_hg_pf_talk


label hg_pf_talk_T2_E1:

    call start_hg_pf_talk

    her "Another talk, [name_genie_hermione]?" ("soft", "base", "base", "mid")
    her "(I hope he doesn't do \"that\" again...)" ("disgust", "narrow", "base", "down")

    call hg_pf_talk_T2_repeat

    jump end_hg_pf_talk


label hg_pf_talk_T2:
    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    her "My life has been quite uneventful lately, to be honest..." ("annoyed", "narrow", "angry", "R")
    her "*Hmm*..." ("annoyed", "base", "base", "R")
    her "Except there's a fierce competition going on between the Slytherin and the Gryffindor house." ("open", "closed", "base", "mid")
    her "To be honest, [name_genie_hermione], there should be none..." ("open", "narrow", "angry", "R")
    her "Gryffindor would have been in the lead if not for those Slytherin harlots..." ("annoyed", "base", "angry", "mid")
    her "The things I hear those girls do - simply to get a few extra points..." ("angry", "narrow", "angry", "R")
    her "How despicable!" ("open", "closed", "angry", "mid")
    gen "What does this make you then, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "Exactly!" ("normal", "base", "base", "mid")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    her "I have to work even harder to compensate for the damage those nasty girls are doing..." ("open", "closed", "angry", "mid")
    her "Thank you for helping me out, [name_genie_hermione]." ("normal", "base", "base", "mid")

    menu:
        "-Start jerking off-":
            $ states.gen.stats.masturbated_to_hermione += 1
            $ states.gen.masturbating = True

            hide hermione_main
            nar "You reach under the desk and grab your cock..."
            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8

            her "[name_genie_hermione], what are you doing?" ("open", "base", "base", "mid")
            her "You are not.....?" ("open", "base", "worried", "mid")
            her "Are you...?" ("annoyed", "base", "worried", "R")
            gen "What? Oh, I'm just scratching my leg...{w=0.4} Keep going." ("base", xpos="far_left", ypos="head")
            her "*Hmm*..." ("normal", "squint", "angry", "mid")
            gen "{size=-4}(Is she onto me? Nah...){/size}" ("base", xpos="far_left", ypos="head")
            her "Well, like I was saying..." ("open", "closed", "base", "mid")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False
            gen "Don't mention it." ("base", xpos="far_left", ypos="head")

    her "I'm not sure if you're aware of this [name_genie_hermione]..."
    her "But there are rumours that this one girl sold some naughty pictures of herself for ten house points." ("open", "narrow", "angry", "R")

    if states.gen.masturbating:
        gen "{size=-4}(What a slut... *Ah*... Yes...){/size}" ("base", xpos="far_left", ypos="head")
        her "And these two other girls..." ("annoyed", "base", "worried", "R")
    else:
        gen "Ten points, *huh*?" ("base", xpos="far_left", ypos="head")
        her "Yes... Can you believe it?" ("open", "closed", "base", "mid")
        gen "Well, surely they can't be that bad if it's only--" ("base", xpos="far_left", ypos="head")
        her "Not that bad?!" ("angry", "base", "base", "mid")
        her "Of course they're bad! This is a Slytherin we're talking about!" ("angry", "base", "angry", "mid")
        gen "(There she goes again...)" ("base", xpos="far_left", ypos="head")
        her "We should have her camera confiscated immediately, and--" ("open", "closed", "angry", "mid")
        gen "(Screw this...)" ("base", xpos="far_left", ypos="head")

        $ states.gen.stats.masturbated_to_hermione += 1
        $ states.gen.masturbating = True

        hide hermione_main
        nar "You reach under the desk and grab your cock..."
        call gen_chibi("jerk_off_behind_desk")
        with d3
        pause.8

        her "She should be expelled!" ("angry", "closed", "angry", "mid")
        gen "*Mmm*... Yes..." ("base", xpos="far_left", ypos="head")
        her "We need to put an end to this behaviour, [name_genie_hermione]!" ("open", "closed", "base", "mid")
        gen "Yeah, sure..." ("base", xpos="far_left", ypos="head")
        her "So you agree with me then?" ("base", "narrow", "base", "mid_soft")
        her "I think we need to implement a new penalty system to punish girls who step over the line..." ("open", "base", "base", "R")
        gen "(All I heard was \"punish girls\"...)" ("base", xpos="far_left", ypos="head")
        her "This will also help the boys in our school to feel less discriminated against!" ("open", "closed", "base", "mid")
        gen "The boys?" ("base", xpos="far_left", ypos="head")
        gen "Oh, right... Poor bastards." ("base", xpos="far_left", ypos="head")
        her "I'm so glad that you understand my concerns, [name_genie_hermione]." ("base", "base", "base", "mid")
        gen "Yes, yes, sure..." ("base", xpos="far_left", ypos="head")
        her "Now, onto my next--" ("base", "base", "base", "mid")
        her "[name_genie_hermione]... What are you doing?" ("open", "base", "base", "mid")
        her "You are not.....?" ("open", "base", "worried", "mid")
        her "Are you...?" ("annoyed", "base", "worried", "R")
        gen "What? Oh, I'm just scratching my leg...{w=0.4} Keep going." ("base", xpos="far_left", ypos="head")
        her "*Hmm*..." ("normal", "squint", "angry", "mid")
        gen "{size=-4}(Is she onto me? Nah...){/size}" ("base", xpos="far_left", ypos="head")
        her "As I was saying..." ("annoyed", "base", "worried", "R")
        her "We have to do something about these Slytherin harlots..." ("open", "closed", "worried", "mid")

    her "There is a rumour that they are actually sleeping with professor Snape..." ("annoyed", "base", "worried", "mid")
    gen "{size=-4}(Yes... Those nasty Slytherin sluts!){/size}" ("base", xpos="far_left", ypos="head")
    her "Also, there was this one girl who gave a teacher a handjob, right during class..." ("base", "base", "base", "mid")
    gen "{size=-4}(Yes... This is good stuff, go on!){/size}" ("base", xpos="far_left", ypos="head")
    her "And this other girl, she sucked off a teacher!" ("annoyed", "base", "worried", "R")
    gen "{size=-4}(Yes! Yes!){/size}" ("base", xpos="far_left", ypos="head")
    her "And another girl let a teacher cum in her mouth..." ("smile", "base", "base", "R")
    her "And she swallowed it all and loved it!" ("soft", "base", "base", "R")
    gen "{size=-4}(Wait... Is she making this up?){/size}" ("base", xpos="far_left", ypos="head")
    her "I'm a nasty girl too, you know..." ("smile", "narrow", "base", "mid_soft")
    gen "What?!" ("angry", xpos="far_left", ypos="head")
    her "I just want to suck a cock..." ("soft", "narrow", "base", "mid_soft")
    her "I want men to cum on my face like in those magazines I saw!" ("open_tongue", "narrow", "base", "mid_soft")
    gen "{size=-4}(You little slut! That did it!) *Argh!*{/size}" ("angry", xpos="far_left", ypos="head")

    call cum_block
    call gen_chibi("cum_behind_desk")
    with d3
    pause.8

    call cum_block
    gen "*Argh*! YES!" ("angry", xpos="far_left", ypos="head")
    her "You were touching yourself, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
    gen "What? No, I was just... Ah, shit, this feels good..." ("angry", xpos="far_left", ypos="head")

    call hide_characters
    call gen_chibi("cum_behind_desk_done")
    with d3
    pause.8

    her "This is disgusting! How could you!?" ("scream", "happyCl", "worried", "mid")
    her "[name_genie_hermione], you are the headmaster! You are supposed to set a good example!" ("scream", "base", "angry", "mid")
    gen "Hey, little Missy, are you going to judge me or do you want your points?" ("base", xpos="far_left", ypos="head")
    her "My points please, I believe I earned those." ("angry", "happyCl", "worried", "mid",emote="sweat")
    gen "Yes, you did." ("base", xpos="far_left", ypos="head")
    her "*Eww*... I feel so dirty now..." ("angry", "base", "angry", "mid")

    $ states.her.mood = +7
    $ states.her.status.voyer = True

    if not states.her.ev.talk_to_me.caught_masturbating:
        $ states.her.ev.talk_to_me.caught_masturbating = True

        $ achievements.unlock("busted")

    return

label hg_pf_talk_T2_repeat:
    her "" ("normal", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    her "*Ahem*... Things have been pretty normal..." ("open", "closed", "base", "mid")
    her "I caught one of the Slytherin girls flickering her eyelashes towards Professor Snape the other day." ("open", "base", "base", "R")
    her "I assume she was trying to look seductive, but to me, it appeared more like she had some sort of tick." ("soft", "narrow", "base", "R")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "This is a regular occurrence, I assume?" ("base", xpos="far_left", ypos="head")
    her "It's a daily occurrence! Just the other day--" ("angry", "narrow", "base", "mid")
    her "*Ehm*... I mean..." ("angry", "base", "base", "R")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... I'm not sure if I should tell you..." ("disgust", "narrow", "base", "down")
    gen "Why not?" ("base", xpos="far_left", ypos="head")
    her "I just figured you'd just end up... *Ahem*..." ("angry", "narrow", "base", "down")
    gen "Go on..." ("base", xpos="far_left", ypos="head")
    her "Alright, fine... I'll tell you about it..." ("open", "squint", "base", "R")
    her "It's that Slytherin girl I mentioned before... I actually caught her taking pictures in public this time." ("angry", "base", "base", "mid")

    menu:
        "-Start jerking off-":
            $ states.gen.stats.masturbated_to_hermione += 1
            $ states.gen.masturbating = True

            hide hermione_main
            nar "You reach under the desk and grab your cock..."
            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8

            her "[name_genie_hermione], this is precisely why I didn't want to tell you!" ("angry", "narrow", "worried", "mid")
            gen "What do you mean?" ("base", xpos="far_left", ypos="head")
            her "You're touching yourself again!" ("angry", "narrow", "annoyed", "R")
            gen "I'm just a bit itchy. You know how it is..." ("base", xpos="far_left", ypos="head")
            her "..." ("normal", "narrow", "angry", "mid")
            gen "Don't mind me... Feel free to resume your story..." ("base", xpos="far_left", ypos="head")
            her "Fine..." ("open", "closed", "annoyed", "mid")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False
            gen "In public?" ("base", xpos="far_left", ypos="head")
            her "I know! I couldn't believe it!" ("angry", "narrow", "base", "mid")

    her "As I waited outside the potion classroom for our scheduled lesson to commence, I observed that the door was ajar." ("open", "closed", "base", "mid")
    her "Since Professor Snape always makes sure to keep the doors locked, I figured something must be going on..." ("open", "base", "base", "R")
    her "So, I opened the door a bit more to get a peek inside..." ("open", "closed", "base", "mid")
    her "And there she was!" ("scream", "base", "base", "mid")
    her "[name_genie_hermione]! I actually caught her this time! Now you have to do something about it!" ("angry", "squint", "base", "mid")
    if states.gen.masturbating:
        gen "*Ah*... Caught her... Doing what?" ("base", xpos="far_left", ypos="head")
        her "Taking pictures, while she was touching herself!" ("scream", "base", "annoyed", "mid")
        gen "*Ah*... Really?" ("base", xpos="far_left", ypos="head")
        her "Yes!" ("angry", "narrow", "annoyed", "mid")
        her "And it can't have been the first time, seeing how she was effortlessly focusing her magic while also keeping the camera steady..." ("open", "narrow", "annoyed", "R")
        gen "*Ngh*--{w=0.2} Jealous, are you?" ("base", xpos="far_left", ypos="head")
        her "Jealous? Of a Slytherin? Surely, you must be joking..." ("angry", "squint", "base", "mid")
        gen "She sure--{w=0.2} *Ngh*... She's found a pretty easy way to earn points, don't you think?" ("base", xpos="far_left", ypos="head")
        her "*Hmph*...{w=0.4} As if she even cares about the points...." ("annoyed", "narrow", "annoyed", "R")
        gen "She doesn't?" ("base", xpos="far_left", ypos="head")
        her "Of course she doesn't! None of them do! They're all just doing it to fullfil their own twisted desires!" ("angry", "happy", "annoyed", "mid")
        gen "(As if you're not--)" ("base", xpos="far_left", ypos="head")
        her "You should've seen how wet she was!" ("open", "base", "annoyed", "R")
        her @ cheeks blush "I mean--" ("angry", "base", "worried", "mid") #blushing
        gen "{size=-4}(*Ngh*--{w=0.2} That did it!) *Argh!*{/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause.8

        call cum_block

        gen "*Argh*! YES!" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "I can't believe it, [name_genie_hermione]!" ("angry", "base", "worried", "stare")
        her "You were touching yourself!{w} Again!" ("angry", "base", "angry", "mid")

        gen "What? No, I was just... *Ngh*..." ("angry", xpos="far_left", ypos="head")

        call hide_characters
        call gen_chibi("cum_behind_desk_done")
        with d3
        pause.8

        her "You disgust me!" ("scream", "happyCl", "worried", "mid")
        gen "Yeah, yeah... Do you still want the points, or not?" ("base", xpos="far_left", ypos="head")
        her "..." ("disgust", "narrow", "annoyed", "down")
        her "I do..." ("open", "narrow", "annoyed", "down")
        gen "I figured you would..." ("base", xpos="far_left", ypos="head")

        $ states.her.mood = +7

    else:
        gen "Did you bring me some proof?" ("base", xpos="far_left", ypos="head")
        her "Did I--" ("angry", "squint", "base", "stare")
        gen "After seeing what you saw, surely, you must have confronted her and confiscated her camera." ("base", xpos="far_left", ypos="head")
        her "Of course I didn't confront her! How do you think that would have looked?" ("angry", "squint", "worried", "mid")
        her "Even if I had, I wouldn't have dared to touch her camera after what I--" ("angry", "squint", "worried", "R")
        her @ cheeks blush "*Ehm*..." ("angry", "narrow", "worried", "down")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Hmph*...{w=0.4} Nevermind." ("annoyed", "narrow", "annoyed", "R")
        her "May I have my points now?" ("open", "closed", "angry", "mid")
        gen "Very well..." ("base", xpos="far_left", ypos="head")

    return
### Tier 3 ###

# Hermione knows by now that you like to jerk off while she talks.
# She tells you true stories that happened at Hogwarts.
# Favours can revolve around Cho, Luna, Tonks

label hg_pf_talk_T3_intro_E1:
    
    call start_hg_pf_talk

    gen "Let's have another chat, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Okay..." ("annoyed", "base", "worried", "mid")
    gen "I'd like you to tell me a bit about your day." ("base", xpos="far_left", ypos="head")
    her "Are you going to...{w=0.8} touch yourself again, sir?" ("open", "squint", "base", "mid")
    gen "I can't guarantee I won't..." ("base", xpos="far_left", ypos="head")
    gen "You will be awarded with house points - as usual." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("mad", "narrow", "worried", "down") #mad Blush
    gen "You've not walked out the door, so please, tell me about your day." ("base", xpos="far_left", ypos="head")

    call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_intro_E2:

    call start_hg_pf_talk

    gen "{size=-4}(Perhaps I could spice things up a bit...){/size}" ("base", xpos="far_left", ypos="head")
    menu:
        #"-Suggest inviting Snape-":
        #    pass
        #    #To be added
        "-Suggest inviting Tonks-":
            # Start event chronologically
            $ her_eventqueue_talk_to_me_tonks.start()
        "-Decide against it-":
            gen "Let's have another chat, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Okay..." ("base", "base", "base", "mid")

            call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3_repeat:

    call start_hg_pf_talk

    menu:
        #"-Suggest inviting Snape-":
        #    pass
        #    #To be added
        "-Suggest inviting Tonks-":
            # Start event chronologically
            $ her_eventqueue_talk_to_me_tonks.start()
        "-Decide against it-":
            gen "Tell me about your day, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "Okay..." ("base", "base", "base", "mid")
            call hg_pf_talk_T3

    jump end_hg_pf_talk


label hg_pf_talk_T3:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause.5

    menu:
        "-Start jerking off-":
            $ states.gen.stats.masturbated_to_hermione += 1
            $ states.gen.masturbating = True

            hide hermione_main
            nar "You reach under the desk and grab your cock..."
            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.8
            her "[name_genie_hermione]... I hoped we wouldn't do this again." ("open", "squint", "base", "mid")
            her "Are you actually... Masturbating?" ("disgust", "squint", "base", "mid")
            gen "Me? I'd never do such a thing..." ("base", xpos="far_left", ypos="head")
            gen "Anyhow... Don't forget why you're here, [name_hermione_genie]. To earn some points..." ("base", xpos="far_left", ypos="head")
            gen "Now, tell me about your day." ("base", xpos="far_left", ypos="head")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False
            gen "And put some effort into it, if you want to earn those points." ("base", xpos="far_left", ypos="head")

    her "Right..." ("open", "closed", "base", "mid")
    her "So, our first lesson of today was muggle studies." ("open", "base", "base", "R")
    her "Professor Burbage babbled on about things she doesn't understand, as usual." ("open", "base", "base", "mid")
    her "As a muggle-born, I can't help but notice how inaccurate most of her teachings are, so I briefly considered dropping the subject." ("open", "base", "base", "mid")
    her "But ever since I failed that test, I feel like I should take all the extra credit that I can get..." ("open", "narrow", "worried", "down")
    her "It's not too bad though... Her views on muggle and wizarding relations are quite refreshing." ("base", "happy", "base", "mid_soft")
    if states.gen.masturbating:
        gen "*Hmm*... Yes, very refreshing..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Ugh*... Do you have to touch yourself, [name_genie_hermione]?" ("disgust", "narrow", "worried", "down")
        gen "Just keep talking, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Fine..." ("annoyed", "narrow", "angry", "R")
        her "So, I probably would've found her lessons quite enjoyable if it wasn't for the Slytherins always trying to disrupt it..." ("annoyed", "narrow", "base", "mid")
        gen "*Ah*...{w=0.4} Yes...{w=0.4} Those naughty Slytherins...{w=0.4} What were they up to this time?" ("base", xpos="far_left", ypos="head")
    else:
        gen "So, what you're saying is that even though you're not learning anything, you're still enjoying it?" ("base", xpos="far_left", ypos="head")
        her "Well, I would, if the Slytherins weren't making it their mission to disrupt every single lesson..." ("annoyed", "narrow", "base", "mid")
        gen "Right..." ("base", xpos="far_left", ypos="head")
        her "Yes... And I'm certain that the only reason why they're even taking the subject, is so that they get to make fun of her, and anything muggle related..." ("annoyed", "narrow", "base", "mid")
        gen "So, what were those naughty Slytherins doing exactly?" ("base", xpos="far_left", ypos="head")

    her "Well... Since they had a room filled with a bunch of muggle toys, instruments, and trinkets at their disposal..." ("open", "base", "base", "mid")
    her "They thought it would be funny to play around with them, and to try and make it look like they were handling various sexual devices." ("open", "base", "base", "R")
    her @ cheeks blush "Since most Slytherins are pure-blooded, they had no idea that they were just making fun of miscellaneous house-hold items..." ("open", "base", "base", "mid")

    if states.gen.masturbating:
        gen "(If only you knew about the time I had with Henry the hoover.)" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Well, if you're brave enough..." ("base", xpos="far_left", ypos="head")

    her "Each time Professor Burbage brought out another object, they would start spouting various suggestive remarks, and ask her where she'd insert it and so on..." ("angry", "narrow", "angry", "R")
    her @ cheeks blush "Which, of course, triggered this incessant giggling from the Slytherin girls..." ("disgust", "narrow", "angry", "down")
    her @ cheeks blush "Of course, not a single muggle-born found it funny... Until Professor Burbage brought out what she actually believed to be a back massager..." ("angry", "narrow", "base", "R")
    gen "Isn't that what it says on the box?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes, but--" ("annoyed", "narrow", "worried", "mid")
    gen "Wait, so you're saying that you're aware of what people actually use them for?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("disgust", "wide", "worried", "shocked")
    gen "Well?" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "I..." ("annoyed", "happyCl", "worried", "mid")
    her @ cheeks blush "Well, it's obvious to anyone with common sense, isn't it!" ("open", "narrow", "angry", "R")
    her @ cheeks blush "Even those Slytherin girls quickly realised what people actually use it for... And they're thicker than polyjuice potion!" ("mad", "closed", "angry", "mid")
    if states.gen.masturbating:
        gen "(I bet you've got a whole drawer full of them...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "Why don't {size=+4}you{/size} inform me, since you seem so knowledgeable about the subject..." ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Sorry?" ("mad", "base", "worried", "mid")
    gen "What {size=+4}do{/size}{w=0.6} most people use those massagers for?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well, you know..." ("open", "narrow", "worried", "down")
    gen "Pretend that I don't." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "..." ("normal", "narrow", "base", "down")

    if states.gen.masturbating:
        her "People use it, to do what you're doing..." ("open", "happyCl", "worried", "mid")
        gen "Which is..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well, you put it against--{w=0.2}*Ahem*...{w=0.4} And then you turn it on to..." ("normal", "narrow", "worried", "down")
        gen "To what?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "To pleasure yourself..." ("open", "narrow", "angry", "down")
        gen "Fascinating... Perhaps you should bring yours next time, so you can show them how it's meant to be used." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Bring--{w=0.2} Why do you think I have--{w=0.2} Muggle electronics doesn't even work at Hogwarts!" ("base", "happyCl", "base", "mid")
        gen "Truly?" ("grin", xpos="far_left", ypos="head")
        gen "Then how come you're so knowledgeable about the--" ("grin", xpos="far_left", ypos="head")
        gen "Don't tell me you've got one at home!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "I..." ("normal", "narrow", "worried", "down")
        gen "(I knew it, you dirty slut!)" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "I don't have to talk about my personal health to you!" ("open", "narrow", "angry", "R")
        gen "I bet you use it as soon as your parents get out of the house!" ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "I do not!" ("angry", "base", "angry", "mid")
        gen "{size=-4}So you use it even when they're at home?{/size}" ("grin", xpos="far_left", ypos="head")
        gen "{size=-4}You dirty--{w=0.2}*Hngh*...{w=0.5} *Argh*!{/size}" ("angry", xpos="far_left", ypos="head")

        stop music fadeout 1
        call hide_characters
        with d3
        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause.8

        call cum_block
        call bld
        gen "*Argh*! YES!" ("angry", xpos="far_left", ypos="head")

        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
        if states.her.tier <= 4:
            $ states.her.mood = +7
            her "[name_genie_hermione]...{w} Did you just...?" ("disgust", "narrow", "base", "down")
        else:
            her "[name_genie_hermione]...{w} Did you just...?" ("soft", "narrow", "worried", "down")

        call hide_characters
        hide screen bld1
        with d3
        pause.1
        call gen_chibi("cum_behind_desk_done")
        with d3
        pause.5

        if states.her.tier <= 4:
            her "*Yuck*!..." ("annoyed", "narrow", "base", "mid_soft")
        gen "That...{w=0.4} Felt...{w=0.4} Amazing!" ("base", xpos="far_left", ypos="head")
        her "..." ("base", "narrow", "base", "mid_soft", xpos="mid", ypos="base")
        gen "Don't be so uptight, [name_hermione_genie]... Try to relax a bit for once." ("grin", xpos="far_left", ypos="head")
        her "(.........)" ("annoyed", "narrow", "angry", "R")
        gen "How about I fetch that massager, that way--" ("base", xpos="far_left", ypos="head")
        her "No!" ("angry", "narrow", "angry", "mid")
        gen "Oh right... I forgot it wouldn't function..." ("base", xpos="far_left", ypos="head")
        gen "Well... Surely, there are other magical alternatives available for you to--" ("base", xpos="far_left", ypos="head")
        her "Please, I don't want to think about that right now..." ("annoyed", "happyCl", "worried", "mid")
        gen "I'll figure something out, don't you worry... I'll make it a priority to loosen you up one way or another..." ("base", xpos="far_left", ypos="head")
        her "{size=-4}What's that supposed to--{/size}" ("annoyed", "happyCl", "worried", "mid")
        her "(...................)" ("disgust", "base", "worried", "mid")
        gen "You've done well today, [name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "You've soiled your entire desk!" ("mad", "wide", "base", "stare")
        gen "That's odd... Well, I'm sure it will get cleaned at one point or another." ("base", xpos="far_left", ypos="head")
        if states.her.tier <= 4:
            her @ cheeks blush "Gross..." ("normal", "happyCl", "worried", "mid")
        else:
            her @ cheeks blush "(Such a waste...)" ("soft", "narrow", "worried", "down")
        her @ cheeks blush "May I have my points now?" ("open", "narrow", "worried", "down")
        gen "Certainly..." ("base", xpos="far_left", ypos="head")

    else:
        gen "Go on..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "They're...{w=0.5} They're back massagers... As it says on the box... Didn't you say so yourself?" ("open", "base", "worried", "R")
        gen "In that case, you'd have no problem watching those Slytherin girls having a go, using one?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Of course I wouldn't!" ("angry", "happyCl", "worried", "mid")
        gen "Bet..." ("base", xpos="far_left", ypos="head")
        gen "Although... What if they end up doing it wrong? Surely, being the only one in your class familiar with such a device..." ("base", xpos="far_left", ypos="head")
        her "What do you--" ("open", "happy", "base", "mid_soft")
        gen "Surely, during your next lesson, you should volunteer to properly demonstrate how to use it." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "What? Why on earth do you think I would do that?" ("shock", "wide", "base", "stare")
        her @ cheeks blush "Do you take me for some sort of exhibitionist?" ("mad", "wide", "base", "stare")
        gen "Sorry?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Don't you \"sorry\" me!{w=0.5} You expect me to get my fanny out, and just casually display how to use a vibrator for the entire class?" ("angry", "base", "angry", "mid")
        with hpunch
        her @ cheeks blush "How{w=0.8} {size=+6}dare{/size} you suggest--" ("open", "base", "angry", "mid")
        gen "What are you talking about? Weren't we talking about back massagers?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "-Yes, why don't I just tear my clothes off in the middle of class while I'm at it, and--" ("open", "closed", "angry", "mid")
        play sound "sounds/glass_shatter.ogg"
        her @ cheeks blush "..." ("mad", "wide", "base", "stare")
        her "I...{w} I'm sorry [name_genie_hermione]!"
        gen "I didn't take you for such a naughty girl, [name_hermione_genie]!" ("grin", xpos="far_left", ypos="head")
        gen "I thought we were having an innocent conversation about back massagers, then you spring all this on me." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "[name_genie_hermione]... I didn't mean to--" ("soft", "happyCl", "worried", "mid")
        gen "I don't want to hear it, [name_hermione_genie]..." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "But please, I assure you--" ("open", "base", "worried", "mid")
        gen "That will be all for today [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "You've surely opened my eyes..." ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "base", "base", "mid")
    return



label hg_pf_talk_tonks_T3_intro_E1:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie], for today's favour, I'd like to bring in a guest to join us." ("base", xpos="far_left", ypos="head")
    her "A guest? But I thought we decided that this was only going to be between you and me." ("open", "squint", "worried", "mid")
    gen "Why only the two of us when there was an option to bring another person in?" ("base", xpos="far_left", ypos="head")
    her "An option to--{w=0.4} What?" ("normal", "squint", "angry", "mid")
    her "Sorry, I'm not following..." ("normal", "squint", "base", "mid")
    gen "Tell me [name_hermione_genie]... What's your opinion of Miss Tonks?" ("base", xpos="far_left", ypos="head")
    her "Well, she's a very talented witch... You'd have to be, to become an auror." ("open", "closed", "base", "mid")
    gen "Very talented indeed...{w=0.4} Anything else you know about her?" ("base", xpos="far_left", ypos="head")
    her "*Hmm*... Nothing that any other student wouldn't know, I don't think." ("open", "base", "base", "mid")
    gen "Truly? From what I've heard, you two had a bit of a private talk at one point." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "You know about that? Who told--" ("angry", "base", "worried", "mid")
    gen "I'm the headmaster, [name_hermione_genie]...{w} It's my job to know what goes on within the castle." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Right..." ("open", "base", "worried", "mid")
    gen "So, during that talk, Miss Tonks suggested you try selling me some favours, didn't she?" ("base", xpos="far_left", ypos="head")
    her "She did, but--" ("open", "narrow", "base", "down")
    her "Hold on... What are you suggesting, exactly?" ("disgust", "narrow", "base", "mid")
    gen "I just thought that we could have a conversation with her." ("base", xpos="far_left", ypos="head")
    her "Oh, I see..." ("angry", "base", "base", "mid")
    gen "I'll award points to your house for your efforts, of course." ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "base", "base", "R")
    her "And Professor Tonks?" ("open", "base", "base", "mid")
    gen "Sorry?" ("base", xpos="far_left", ypos="head")
    her "Would she pay me as well?" ("open", "base", "base", "mid")
    gen "Well, that would be up to her, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Alright then, I accept... Just let me get more presentable." ("base", "base", "base", "mid")
    gen "Great, I'll call for her then..." ("base", xpos="far_left", ypos="head")

    call hg_pf_talk_tonks

    jump end_hg_pf_talk


label hg_pf_talk_tonks_T3_E1:
    her "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    gen "Let's call Miss Tonks up for this one, shall we." ("base", xpos="far_left", ypos="head")
    her "For what?" ("open", "happy", "base", "mid")
    gen "For today's favour of course!" ("base", xpos="far_left", ypos="head")
    her "..." ("annoyed", "narrow", "base", "mid_soft")
    her "Will I get any extra points for this?" ("open", "base", "base", "mid")
    gen "Well, that will be up to Miss Tonks, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Alright... Just let me get more presentable." ("base", "base", "worried", "R")

    call hg_pf_talk_tonks

    jump end_hg_pf_talk


label hg_pf_talk_tonks:
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    pause 1

    # Setup
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_default)

    $ ton_outfit_last.save()
    $ tonks.equip(ton_outfit_default)

    #call ton_chibi("stand",500,"base")
    call her_chibi("stand","desk","base")
    hide screen blkfade
    with d5
    pause.8

    play sound "sounds/door.ogg"
    call ton_walk(500,"base")

    ton @ hair basic "" ("base", "base", "base", "mid", xpos=600, ypos="base", trans=d3)
    her "" ("base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    if game.daytime:
        gen "Good day, Miss Tonks." ("base", xpos="far_left", ypos="head")
        ton "Good day, Professor." ("base", "happyCl", "base", "mid")
    else:
        gen "Good evening, Miss Tonks." ("base", xpos="far_left", ypos="head")
        ton "Good evening, Professor." ("base", "happyCl", "base", "mid")
    ton @ hair horny "Miss Granger..." ("horny", "base", "base", "L")
    ton @ hair basic "Is there some sort of special circumstance as to why the two of you summoned me here?" ("base", "base", "raised", "mid")
    gen "More or less." ("base", xpos="far_left", ypos="head")
    gen "I think the three of us should have a bit of a chat..." ("base", xpos="far_left", ypos="head")
    ton "Miss Granger, you didn't cause any trouble, I hope?" ("open", "base", "base", "L")
    her "Me? Of course not!" ("open", "closed", "base", "mid")
    ton @ hair horny "Having some \"DADA\" issues? I could tutor you, if you'd like..." ("horny", "base", "base", "L")
    her "That's not--" ("angry", "base", "base", "mid")
    gen "I figured it was about time we had a chat, regarding these favour trading allegations..." ("base", xpos="far_left", ypos="head")
    gen "Mainly the concerns that Miss Granger so kindly brought forward." ("base", xpos="far_left", ypos="head")
    her "Oh, those..." ("open", "narrow", "worried", "down")
    gen "Unless you've suddenly changed your mind on that sort of thing?" ("base", xpos="far_left", ypos="head")
    her "..." ("normal", "base", "base", "R")
    her @ cheeks blush "No, I'll talk about it - if you like..." ("open", "narrow", "base", "down")
    her @ cheeks blush "" ("normal", "base", "base", "mid")
    ton @ hair horny "..." ("horny", "base", "base", "mid")
    gen "Why don't we start with..." ("base", xpos="far_left", ypos="head")
    $ _yourself = False

    menu:
        "\"Those pesky Slytherin Sluts!\"":
            $ _yourself = False
            ton "Yes, I've heard those Slytherin girls are up to no good..." ("horny", "base", "angry", "mid")
            her @ cheeks blush "They are! Where do I begin?" ("open", "closed", "angry", "mid")

            menu:
                "-Start jerking off-":
                    $ states.gen.stats.masturbated_to_hermione += 1
                    $ states.gen.masturbating = True
                    call hide_characters
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("jerk_off_behind_desk")
                    with d3
                    pause.8

                    nar "You reach under the desk and grab your cock..."

                "-Participate in the conversation-":
                    $ states.gen.masturbating = False

            ton "" ("horny", "base", "base", "down")
            her @ cheeks blush "There's the time Tracey Davis gave Slughorn a lap dance, in the middle of class!" ("annoyed", "narrow", "angry", "R")
            ton "In the middle of class?" ("mad", "wide", "shocked", "stare")
            her @ cheeks blush "Yes..." ("disgust", "narrow", "worried", "down")
            ton @ hair horny "Oh my..." ("base", "narrow", "raised", "mid")
            her @ cheeks blush "She was just sitting on his lap, while he taught from his desk..." ("open", "base", "base", "R")
            her @ cheeks blush "But we could all see her moving her hips!" ("annoyed", "base", "base", "R")
            ton "Interesting..." ("grin", "narrow", "shocked", "down")
            ton @ cheeks blush "Any other incidents, Miss Granger?" ("upset", "wide", "shocked", "L")
            her "More than I could count!" ("open", "closed", "angry", "mid")
            ton "" ("mad", "base", "base", "mid")
            her "I'm almost certain one of the girls wasn't wearing any underwear in class - which is completely unhygienic." ("angry", "narrow", "worried", "mid_soft")
            her @ cheeks blush "It was as if a snail had dragged themselves across one of the seats." ("annoyed", "base", "base", "R")
            her @ cheeks blush "I had to insist on staying after class - and I spent a good ten minutes scourgifying everything." ("disgust", "narrow", "worried", "down")
            if states.gen.masturbating:
                gen "(I bet you lapped it all up, slut!)" ("grin", xpos="far_left", ypos="head")
            ton "Why bother, the elves would've done it anyway." ("mad", "narrow", "raised", "R")
            her "About that--" ("open", "squint", "angry", "mid")
            ton "Actually, let's save that topic for another time..." ("normal", "narrow", "base", "L")
            if states.gen.masturbating:
                gen "(You wanted it all for yourself, that's why!)" ("angry", xpos="far_left", ypos="head")
            ton @ hair horny "Is there anything else you could tell us about these... Naughty Slytherin girls?" ("horny", "base", "angry", "mid")
            her "Of course!" ("open", "closed", "angry", "mid")
            her "I could go on for hours about the vile things they've been up to..." ("annoyed", "narrow", "annoyed", "mid")
            ton @ cheeks blush "I'm not in a rush." ("base", "narrow", "base", "down")
            ton @ cheeks blush "But even if I was, it can wait until later." ("horny", "base", "raised", "L")
            her "Well, there's another Slytherin girl...{w=0.3} Pansy Parkinson..." ("open", "closed", "angry", "mid")
            her "She just lets Snape grab her ass whenever he wants... and gives her five points each time..." ("annoyed", "base", "angry", "mid")
            ton "Only five measly points?" ("open", "shocked", "worried", "R")
            ton "(She'd get double from me... easily...)" ("upset", "base", "base", "R")
            gen "..." ("base", xpos="far_left", ypos="head")
            ton "Now, we can't have that, can we..." ("open", "base", "annoyed", "L")
            her "I know... It angers me to the core..." ("annoyed", "base", "worried", "mid")
            ton @ hair basic "" ("upset", "base", "worried", "L")
            her @ cheeks blush "Everyone has been working so hard towards winning the cup... I have been working so hard..." ("open", "base", "worried", "mid")
            if states.gen.masturbating:
                gen "(You have no idea what your hard work does to me...)" ("base", xpos="far_left", ypos="head")
            her "The way it is right now doesn't promote fairness at all." ("annoyed", "narrow", "worried", "down")
            ton "I can see how that could be a problem..." ("open", "closed", "base", "mid")
            her "It's a huge problem!" ("angry", "base", "angry", "mid")
            ton "" ("base", "base", "worried", "L")

        "\"Yourself, Miss Granger!\"":
            $ _yourself = True
            her "What?!" ("soft", "base", "worried", "mid")
            ton @ hair horny "Yes, I would love to hear a bit more about what's going on with you, Miss Granger..." ("horny", "base", "base", "L")
            ton "When I took the teaching position, you and I had a bit of a discussion, didn't we?" ("base", "base", "raised", "L")
            ton "From what I've been hearing on the Portrait vine, you have been selling a few favours yourself to professor Dumbledore here..." ("base", "narrow", "shocked", "down")
            her @ cheeks blush "I have not!" ("shock", "squint", "angry", "mid")

            menu:
                "-Start jerking off-":
                    $ states.gen.stats.masturbated_to_hermione += 1
                    $ states.gen.masturbating = True
                    call hide_characters
                    hide screen bld1
                    with d3
                    pause.2
                    call gen_chibi("jerk_off_behind_desk")
                    with d3
                    pause.8

                    nar "You reach under the desk and grab your cock..."

                "-Participate in the conversation-":
                    $ states.gen.masturbating = False

            ton "" ("horny", "base", "base", "down")
            her @ cheeks blush "" ("annoyed", "squint", "angry", "mid")

            if states.gen.masturbating:
                gen "(Oh yes you have, you naughty slut...)" ("grin", xpos="far_left", ypos="head")
            else:
                # TODO: Might need changes, depending on how we'll deal with statistics.
                # $ tmp_val = states.gen.stats.masturbated_to_hermione+hg_pf_admire_panties.counter+hg_pf_admire_breasts.counter+hg_pf_grope.counter+hg_pf_strip.counter+hg_pf_handjob.counter+hg_pf_blowjob.counter+hg_pf_titjob.counter+hg_pf_sex.counter
                # $ tmp_word = num_to_word(tmp_val) # Sum up all favour counters and turn them into a word.

                # gen "{size=-4}... [tmp_word]...{/size}" ("base", xpos="far_left", ypos="head")
                # her @ cheeks blush "*huh*?" ("open", "squint", "angry", "mid")
                # gen "You've sold me exactly [tmp_word] favours." ("base", xpos="far_left", ypos="head")
                # her @ cheeks blush "B-but that's--" ("angry","happy", "angry", "mid")
                # if tmp_val < 10:
                #     ton @ hair basic "Disappointing, but it's a start." ("open", "closed", "base", "mid")
                #     her @ cheeks blush "..." ("annoyed", "narrow", "base", "R_soft")
                # elif tmp_val >= 10 and tmp_val < 20:
                #     ton @ hair basic "Not bad, but I expected better from one of our top students." ("open", "base", "base", "L")
                # elif tmp_val >= 20 and tmp_val < 30:
                #     her @ cheeks blush "" ("angry", "narrow", "base", "R_soft")
                #     ton @ hair basic "You go, girl! I expected as much from one of my students." ("open", "base", "angry", "L")
                #     gen "..." ("base", xpos="far_left", ypos="head")
                #     ton @ hair basic "I meant to say, one of {i}our{/i} students, of course." ("upset", "base", "worried", "mid")
                # elif tmp_val >= 30 and tmp_val < 40:
                #     ton @ hair horny "Aren't you a sneaky one, *huh*? Almost tricked me that you were an innocent girl with those doe-like eyes of yours." ("horny", "base", "angry", "L")
                #     ton @ hair basic "But, as it turns out, you're actually quite high on the list." ("open", "base", "raised", "L")
                #     her @ cheeks blush "(... There's a list...?)" ("open", "happyCl", "worried", "mid")
                #     ton "At the very top, in fact!" ("silly", "happyCl", "base", "mid")
                #     her @ cheeks blush "..." ("angry", "narrow", "base", "down")
                # else:

                ton "Wow! Who would have thought you're the girl at the top of the list." ("silly", "happyCl", "base", "mid")
                ton @ hair horny "Colour me surprised... Looks like they were telling the truth after all." ("horny", "base", "angry", "L")
                her @ cheeks blush "(... A list... What list...?)" ("angry", "wide", "worried", "stare")
                ton "Congratulations on being a \"top\" student." ("horny", "base", "raised", "L")
                her @ cheeks blush "..." ("disgust", "narrow", "base", "R_soft")

            ton @ hair basic "Don't be so shy, girl. I'm happy that you took my advice to heart..." ("open", "base", "base", "L")
            ton "Consider for a minute where your house would be if you hadn't." ("base", "base", "base", "L")
            her @ cheeks blush "I guess..." ("disgust", "narrow", "base", "down")
            her @ cheeks blush "I assure you that I wasn't considering selling favours myself, when I sent that letter..." ("annoyed", "narrow", "worried", "down")
            her @ cheeks blush "But then we had that talk..." ("soft", "base", "base", "R")
            her @ cheeks blush "And I finally decided, that if I wanted to help my house catch up in points... To help Gryffindor..." ("soft", "narrow", "worried", "down")
            if states.gen.masturbating:
                gen "(And because you love it.)" ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "Well, if you can't beat them..." ("horny", "base", "base", "R")
            ton @ hair basic "So, how has it been working out for you so far, Miss Granger?" ("open", "base", "base", "L")
            ton "How's the morale amongst the Gryffindor students, now?" ("base", "base", "raised", "L")
            her @ cheeks blush "It's great! Although... I still believe that it isn't fair..." ("soft", "base", "base", "mid")
            her "That is why I created the \"M.R.M\"!" ("open", "happy", "base", "mid_soft")
            ton "Yes. The \"Men's Reign Movement\"..." ("open", "closed", "base", "mid")
            ton "" ("base", "base", "base", "mid")
            her "But...{w=0.5} that's not what \"M.R.M\" stands for!" ("angry", "base", "worried", "mid")
            her "It's the \"Men's Rights Movement\"!" ("open", "closed", "base", "mid")
            her "I've told you both about it... In detail!" ("annoyed", "base", "angry", "mid")
            ton "I see... I probably wrote it down and put it somewhere in my...{w=0.8} Extensive notes folder..." ("soft", "base", "raised", "R")
            gen "{size=-5}(*Heh*! It's like looking at myself in a mirror...){/size}" ("base", xpos="far_left", ypos="head") # Small text
            her "(...)" ("annoyed", "narrow", "worried", "down")
            her "The \"M.R.M\" is there to provide male students with the same fairness, righteousness, and just benefits that girls are receiving at this school." ("open", "closed", "base", "mid")
            her "I felt its creation was necessary..." ("annoyed", "base", "base", "mid")

    her "All this favour trading has been completely unfair to the boys!" ("open", "narrow", "annoyed", "mid")
    ton "Ah, yes... Yes." ("open", "closed", "worried", "mid")
    ton "... Wait, what?" ("mad", "shocked", "raised", "L")
    gen "..." ("grin", xpos="far_left", ypos="head")
    her "*Ugh*... I assumed you had read through my initial letter more thoroughly..." ("open", "narrow", "worried", "mid_soft")
    if states.gen.masturbating:
        gen "(Too busy packing her bags, I bet...)" ("base", xpos="far_left", ypos="head")
    else:
        gen "Now-now, Miss Granger... Miss Tonks was very quick to get here when she heard about your accusations." ("base", xpos="far_left", ypos="head")
        her "I suppose..." ("annoyed", "narrow", "base", "R_soft")
    ton "So your problem was never that the girls are engaging in illicit, sexual favours with their teachers..." ("normal", "wide", "raised", "L")
    ton "But that the boys haven't had the same opportunities?" ("upset", "base", "raised", "L")
    her "Exactly!" ("open", "closed", "angry", "mid")
    ton "Why didn't you say so during our talk, Miss Granger?" ("grin", "narrow", "raised", "L")
    ton @ hair horny "I can easily sort out that problem!" ("horny", "base", "base", "L")
    her "I {i}did{/i} mention it!" ("angry", "happyCl", "worried", "mid")
    ton @ hair basic "Oh..." ("annoyed", "base", "raised", "downR")
    if not states.gen.masturbating:
        gen "..." ("base", xpos="far_left", ypos="head")
    if not _yourself:
        ton "Hold on..." ("open", "closed", "base", "mid")
        ton "That doesn't explain as to why {i}you{/i} decided to contribute to this problem, and sell favours as well." ("open", "base", "raised", "L")
        her "..." ("disgust", "base", "base", "R")
        ton "There is no need for you to keep up an act, Miss Granger..." ("soft", "base", "base", "down")
        ton @ cheeks blush hair horny "You can tell us if you've changed your stance. I most certainly won't judge you..." ("horny", "base", "base", "L")
        her "I just...{w=0.6} Sometimes Gryffindor gets behind in points..." ("soft", "narrow", "base", "down")
        ton @ hair basic "Oh, I see..." ("base", "base", "base", "L")
        her @ cheeks blush "So when you suggested that I should try asking Professor Dumbledore for a favour..." ("soft", "base", "base", "mid")
        her @ cheeks blush "Well, I figured if an auror thought it wasn't such a bad thing... Then perhaps I could try and see for myself..." ("open", "narrow", "base", "down")

        if not states.gen.masturbating:
            gen "And boy has she tried it out a bunch..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "angry", "R")

        ton @ hair horny "I'm glad you took my advice to heart, Miss Granger." ("horny", "base", "raised", "L")
        ton @ hair horny "Gryffindor's got a much better chance at winning the house cup now, thanks to your efforts, I presume?" ("horny", "base", "raised", "L")
        her "I... Yes, I believe so... And the morale amongst my friends has risen substantially." ("base", "narrow", "base", "down")
        ton @ hair horny "Excellent." ("grin", "base", "raised", "L")
    else:
        ton @ hair basic "Well, I'm sure your male friends appreciate the fact that you've been making up for their shortcomings..." ("base", "base", "base", "L")
        her "It's not their fault that the teachers aren't as interested in buying favours from them." ("open", "closed", "angry", "mid")
        ton @ hair basic "Yes... The women earning more than the men is a complex dilemma, that's for sure..." ("open", "base", "base", "L")
        ton @ hair basic "Well, at least they can sleep easy, knowing that they've got you out there doing what is necessary for the sake of your house, right?" ("open", "base", "base", "L")
        her "I suppose... {size=-4}Although they don't really know about it...{/size}" ("annoyed", "base", "base", "mid")
        her "I'm just worried it won't be enough..." ("annoyed", "closed", "base", "mid")
    ton @ hair horny "In that case... Would you be against the idea of selling favours to another teacher?" ("horny", "base", "raised", "L")
    her @ cheeks blush "I..." ("angry", "narrow", "worried", "down")
    her @ cheeks blush "*Uhm*..." ("soft", "base", "base", "R")
    her @ cheeks blush "I haven't actively considered it..." ("soft", "narrow", "base", "mid_soft")
    if states.gen.masturbating:
        gen "(Yes! You want to make out with your slutty teacher, don't you!)" ("angry", xpos="far_left", ypos="head")
    ton @ hair basic "Then perhaps you should consider it, Miss Granger." ("base", "base", "base", "L")
    ton "I'm sure your house would be even more ecstatic about a sudden spike in house points." ("soft", "wide", "raised", "L")
    if states.gen.masturbating:
        gen "(And they're not the only ones who'd be ecstatic!)" ("angry", xpos="far_left", ypos="head")
        nar "*fap-fap-fap*"
        gen "(I'm getting close. Maybe I should ask her about something else...)" ("base", xpos="far_left", ypos="head")
        $ tmp_name = name_hermione_genie[:3]
        gen "[tmp_name]-...{w=0.3} *Ugh*... Miss Granger..." ("angry", xpos="far_left", ypos="head")
        gen "Why don't you tell us more about..." ("angry", xpos="far_left", ypos="head")
    else:
        gen "I think we've been trailing a bit off-topic here..." ("base", xpos="far_left", ypos="head")
        ton @ hair basic "Oh yes, perhaps..." ("base", "base", "base", "L")
        gen "Miss Granger, why don't you tell us more about..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"Those pesky Slytherin Sluts!\"":
            her "What else would you like to know?" ("open", "base", "base", "mid")
            if states.gen.masturbating:
                gen "What other--{w=0.2} *Ugh*...{w=0.4} Activities do you have here?" ("base", xpos="far_left", ypos="head")
            else:
                gen "What other activities do you have here?" ("base", xpos="far_left", ypos="head")
            her "I'm not sure what you mean, Professor..." ("annoyed", "base", "base", "R")
            ton "I think what your headmaster is getting at..." ("open", "closed", "base", "mid")
            if not _yourself:
                ton @ hair horny "Is there any other... uncouth behaviour going on, regarding your fellow students or teachers?" ("grin", "base", "raised", "L")
            else:
                ton @ hair horny "Is there any other... uncouth behaviour going on, outside the dungeons?" ("grin", "base", "raised", "L")
                ton "You've only mentioned potions and alchemy class thus far." ("base", "base", "base", "L")
            if states.gen.masturbating:
                gen "(Where did those bad teachers touch you?)" ("grin", xpos="far_left", ypos="head")
            else:
                gen "Yes, that!" ("base", xpos="far_left", ypos="head")
            her "Well, of course there is..." ("annoyed", "base", "angry", "mid_soft")
            her "There are plenty of filthy tactics being used - all over the school." ("open", "base", "angry", "mid")
            if states.gen.masturbating:
                gen "(Filthy, *huh*?)" ("angry", xpos="far_left", ypos="head")
                nar "*fap-fap-fap*"
            else:
                gen "Such-{w=0.5}{nw}" ("base", xpos="far_left", ypos="head")
            ton "Such as?" ("horny", "base", "raised", "L")

            random:
                block if states.cho.tier >= 2: # After winning against Hufflepuff.
                    her "It's not even just the Slytherins doing it!" ("open", "closed", "angry", "mid")
                    ton "Oh really?" ("base", "base", "raised", "L")
                    her "Yes, that girl from Ravenclaw...{w=0.6} Cho Chang..." ("open", "base", "angry", "mid")
                    if states.cho.tier >= 4: # After winning the cup.
                        her "She used some pretty dirty tactics, just so that Ravenclaw could win the Quidditch cup this season!" ("angry", "base", "angry", "mid")
                    else:
                        her "She's been using some pretty dirty tactics during Quidditch this season!" ("angry", "base", "angry", "mid")
                    gen "(Yes, very dirty indeed...)" ("grin", xpos="far_left", ypos="head")
                    her "You could clearly see her panties during the match between Ravenclaw and Hufflepuff..." ("soft", "base", "angry", "mid")
                    if states.cho.tier >= 3: # After winning against Slytherin
                        her "And there it no doubt in my mind that she was wearing those trousers during her match against Slytherin so that she could egg on their beaters." ("soft", "base", "angry", "mid")
                    her "Why is she even playing the game if the only thing she's good at is distracting the enemy team..." ("annoyed", "narrow", "angry", "R")
                    if states.gen.masturbating:
                        gen "(I'm sure it distracted the commentator as well...)" ("base", xpos="far_left", ypos="head")
                    else:
                        gen "Just the enemy team, Miss Granger?" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("annoyed", "narrow", "base", "R_soft")
                    if states.cho.tier >= 4:
                        ton "*Hmm*... Yes, she certainly did use some quite interesting tactics..." ("horny", "base", "raised", "mid")
                    else:
                        ton "*Hmm*... Yes, she certainly has been using some quite interesting tactics thus far..." ("horny", "base", "raised", "mid")
                    her @ cheeks blush "I wouldn't use the word \"interesting\" to describe it..." ("annoyed", "base", "worried", "mid")
                    ton "I'll make sure to show up to the next match, to see what's going on for myself." ("base", "base", "base", "mid")
                    her "Thank you professor..." ("open", "closed", "base", "mid")
                    her "Even then, that doesn't even compare to what the Slytherins are doing..." ("open", "closed", "base", "mid")

                block if states.cho.status.stripping: # After Cho stripped for you.
                    her "You're well aware that it's not just the Slytherins that have been doing stuff like this..." ("open", "closed", "angry", "mid")
                    ton "If you'd like to give an example..." ("base", "base", "base", "L")
                    her "I'm talking about Cho Chang!" ("open", "base", "angry", "mid")
                    ton "Ah yes, the Ravenclaw seeker..." ("base", "base", "raised", "mid")
                    ton "She's a feisty one, isn't she!" ("horny", "base", "angry", "mid")
                    her "..." ("annoyed", "base", "angry", "mid")
                    ton "Would you like to tell me what she did?" ("horny", "base", "base", "L")
                    if states.gen.masturbating:
                        gen "(Stripped right in front us is what she did!)" ("angry", xpos="far_left", ypos="head")
                        "*fap-fap-fap*"
                    else:
                        gen "I can tell you all about Miss Chang's little--" ("grin", xpos="far_left", ypos="head")
                    her "She was dancing! Right here!" ("open", "closed", "base", "mid")
                    ton "Oh, did she really?" ("base", "base", "raised", "L")
                    ton "With or without clothes?" ("horny", "base", "angry", "mid")
                    if states.gen.masturbating:
                        her "Without..." ("soft", "narrow", "base", "R_soft")
                    else:
                        gen "The latter!" ("grin", xpos="far_left", ypos="head")
                    ton "Oh my... What kind of girl would do such a shameful thing..." ("open", "base", "worried", "mid")
                    if states.her.status.stripping:
                        her @ cheeks blush "..." ("disgust", "narrow", "worried", "down")
                        ton "Are you blushing, Miss Granger?" ("base", "base", "angry", "L")
                        her @ cheeks blush "..." ("disgust", "narrow", "base", "down")
                        her "N-no...? Anyway..."
                    else:
                        her "I know!" ("disgust", "narrow", "base", "down")
                    her "Even then, that doesn't compare to the things those Slytherins have been doing." ("angry", "narrow", "angry", "down")

                block weight 0.9 if states.ast.unlocked: # After Astoria got caught.
                    her "That Astoria girl, casting imperio on a student, and making her lift her top..." ("soft", "narrow", "angry", "R")
                    ton @ hair basic "Ah, yes... That was unfortunate." ("normal", "base", "worried", "R")
                    if states.gen.masturbating:
                        gen "(And hot...)" ("angry", xpos="far_left", ypos="head")
                    her "I take it that has been dealt with?" ("normal", "base", "base", "R")
                    ton @ hair basic "Yes, there's no need for you to worry about her, Miss Granger..." ("base", "happyCl", "raised", "mid")
                    ton @ hair horny "She has been properly reprimanded - and both professor Dumbledore and I have taken it upon ourselves to work on her behaviour." ("horny", "base", "base", "mid")
                    if states.gen.masturbating:
                        gen "(If only there was a reason to punish your naughty behaviour...)" ("grin", xpos="far_left", ypos="head")
                        nar "*fap-fap-fap*"
                    her "I see..." ("normal", "narrow", "worried", "down")
                    her "Well, that's good to hear..." ("open", "closed", "base", "mid")
                    her "I would have just handed her over to the authorities, if it was up to me..." ("open", "base", "angry", "mid")
                    her "Anyway..." ("open", "closed", "base", "mid")
                    her "She's not even the worst person amongst the Slytherins." ("angry", "narrow", "angry", "down")

                block if not any(((states.cho.tier >= 2), (states.cho.status.stripping), states.ast.unlocked)):
                    her @ cheeks blush "..." ("annoyed", "narrow", "worried", "down")
                    ton "Miss Granger?" ("normal", "base", "raised", "L")
                    her @ cheeks blush "*Ehm*..." ("annoyed", "base", "base", "R")
                    her "Well, I could pick any of the girls in Slytherin, really..." ("soft", "narrow", "angry", "R")

            her "It is quite astonishing to what level those Slytherins go to get the teachers going..." ("annoyed", "base", "angry", "mid")
            her "Such as that one time during our care of magical creatures class..." ("open", "closed", "angry", "mid")
            ton "Oh? You weren't studying centaurs, were you?" ("horny", "base", "raised", "mid")
            her "No? Why would you assume that?" ("normal", "wink", "base", "mid")
            ton @ cheeks blush hair horny "No reason...{w=0.4} Please continue." ("open", "base", "raised", "R")
            ton @ hair basic "" ("base", "base", "raised", "mid")
            her "One of the Slytherin students was being quite rough with a {i}Blast-ended Skrewt{/i}... Making it go off on purpose..." ("annoyed", "narrow", "worried", "down")

            if states.gen.masturbating:
                her "She was shaking it up and down... Which was only agitating it a bit initially." ("annoyed", "base", "base", "mid")
                gen "(Yes, I bet you'd love to do that with my cock.)" ("grin", xpos="far_left", ypos="head")
                her "But then she really got going, and it got to the point where it could blast off at a moment's notice..." ("open", "base", "base", "mid")
                gen "(Yes, any minute now...)" ("angry", xpos="far_left", ypos="head")
                her "I was just about to call her out on her disgraceful behaviour, when suddenly the Skrewt started shaking violently." ("open", "base", "base", "R")
                gen "(Yes, any second now...)" ("angry", xpos="far_left", ypos="head")
                ton @ cheeks blush "Then what happened?" ("open", "base", "raised", "L")
                her @ cheeks blush "There was a moment of shock spread across her face, just as the {i}Skrewt{/i} exploded right into it..." ("open", "narrow", "worried", "down")
                ton @ cheeks blush hair horny "" ("horny", "base", "angry", "mid")
                gen "(Yes, take it right on your face, you slut!)" ("angry", xpos="far_left", ypos="head")

                call hide_characters
                hide screen bld1
                with d3
                call cum_block
                call gen_chibi("cum_behind_desk")
                with d3
                pause.8

                call cum_block
                call bld
                gen "{size=-5}*Argh*! YES!{/size}" ("angry", xpos="far_left", ypos="head")

                her @ cheeks blush "" ("annoyed", "base", "base", "mid")
                ton @ cheeks blush "Are you okay, professor? You're awfully quiet..." ("base", "base", "raised", "mid")
                her "(.............)" ("soft", "base", "base", "mid")
                call gen_chibi("cum_behind_desk_done")
                with d3
                pause.2
                call bld
                gen "Oh... yes, I was just so engaged in the conversation." ("base", xpos="far_left", ypos="head")
                ton "Oh really?" ("horny", "narrow", "raised", "mid")
                ton "What were we talking about then?" ("base", "base", "angry", "mid")
                gen "Fast...{w=0.4} Blended...{w=0.6} Fruits?" ("base", xpos="far_left", ypos="head")
                ton @ hair basic "Right..." ("open", "closed", "raised", "mid")
                ton "Well, then... I think we're done here..." ("base", "narrow", "raised", "R")
                her @ cheeks blush "..." ("normal", "base", "base", "R")
                if game.daytime:
                    ton "I'll leave you two to it, have a lovely day, Miss Granger." ("base", "base", "base", "L")
                    her "Good day, professor." ("soft", "base", "base", "R")
                else:
                    ton "I'll leave you two to it, have a good night, Miss Granger." ("base", "base", "base", "L")
                    her "Good night, professor." ("soft", "base", "base", "R")
                ton "Headmaster..." ("horny", "base", "raised", "mid")
                gen "Miss Tonks..." ("base", xpos="far_left", ypos="head")

                call ton_walk(action="leave")

            else:
                ton @ hair basic "Oh no, those poor things!" ("upset", "base", "worried", "mid")
                her "..." ("annoyed", "base", "base", "R")
                ton "That's not how you're supposed to care for a Blast-ended skrewt..." ("open", "closed", "angry", "mid")
                ton "Wait, what is a {i}Blast-ended Skrewt{/i} actually?" ("upset", "base", "worried", "L")
                her "It's some cross-breed that Hagrid came up with... I don't even know how he managed it..." ("annoyed", "narrow", "worried", "down")
                ton "Sounds to me like this Hagrid fellow has been up to some illegal breeding..." ("upset", "base", "raised", "mid")
                gen "(*He-he-he*)" ("grin", xpos="far_left", ypos="head")
                gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
                ton "Although, all things considered!" ("open", "closed", "base", "mid")
                ton "It's probably nothing too bad." ("silly", "happyCl", "base", "mid")

                ton "Well then, I think we're done here." ("open", "base", "worried", "mid")
                ton "I'll leave you two to it..." ("base", "base", "base", "mid")
                if game.daytime:
                    ton "Have a good day, Miss Granger." ("base", "base", "base", "L")
                    her "Good day, professor." ("open", "base", "base", "R")
                else:
                    ton "Have a good night, Miss Granger." ("base", "base", "base", "L")
                    her "Good night, professor." ("open", "base", "base", "R")
                ton "Headmaster..." ("horny", "base", "raised", "mid")
                gen "Miss Tonks..." ("base", xpos="far_left", ypos="head")

                call ton_walk(action="leave")

        "\"Yourself.\"":
            her "Well..." ("angry", "narrow", "worried", "down")
            ton @ hair horny "Tell me, Miss Granger... What does our Headmaster ask of you to earn those house points?" ("horny", "base", "angry", "mid")
            gen "..." ("angry", xpos="far_left", ypos="head")
            if states.gen.masturbating:
                gen "(Let's take a short break, my hands are getting tired.)" ("base", xpos="far_left", ypos="head")
                call gen_chibi("sit_behind_desk")
            her "I..." ("angry", "happyCl", "worried", "mid")
            ton "Go on, I'm sure the Headmaster doesn't mind." ("grin", "narrow", "raised", "L")
            ton "My lips are sealed. {heart}" ("horny", "base", "base", "mid")
            her "Professor..." ("disgust", "narrow", "base", "down")
            gen "Miss Granger, your professor asked you a question..." ("base", xpos="far_left", ypos="head")
            her "But, I thought it was supposed to stay between just you and me..." ("disgust", "narrow", "base", "mid_soft")

            menu:
                "\"That's true\"":
                    gen "Then let's end it here for today..." ("base", xpos="far_left", ypos="head")
                    ton @ hair sad "But sir..." ("open", "base", "worried", "mid")
                    gen "Tonks..." ("base", xpos="far_left", ypos="head")
                    ton @ hair basic "Fine..." ("upset", "base", "worried", "down")
                    ton "I've thoroughly enjoyed our little chat, either way." ("base", "base", "base", "L")
                    gen "Good to hear." ("grin", xpos="far_left", ypos="head")
                    ton "I'll leave you two to it..." ("base", "base", "base", "mid")
                    if game.daytime:
                        ton "Have a good day, Miss Granger." ("base", "base", "base", "L")
                        her "Good day, Professor Tonks." ("open", "base", "base", "R")
                    else:
                        ton "Have a good night, Miss Granger." ("base", "base", "base", "L")
                        her "Good night, Professor Tonks." ("open", "base", "base", "R")

                    call ton_walk(action="leave")

                    gen "(She ignored me...?)" ("base", xpos="far_left", ypos="head")
                    if states.gen.masturbating:
                        gen "(And I just got blue-balled, bollocks...)" ("base", xpos="far_left", ypos="head")
                    $ states.gen.masturbating = False

                "\"Tonks isn't some kind of snitch\"":
                    gen "Or are you telling me that her word isn't good enough?" ("base", xpos="far_left", ypos="head")
                    her "No, of course not, but--" ("disgust", "narrow", "worried", "mid_soft")
                    gen "I'm sure Miss Tonks would be happy to provide you with additional points, as you'd basically be providing a favour for us both." ("base", xpos="far_left", ypos="head")
                    ton @ hair horny "*Hmm*? Oh yes, I'd love to be of help for the Gryffindor house." ("horny", "base", "base", "mid")
                    her "Well... In that case, I want another five points." ("annoyed", "base", "base", "mid")
                    gen "That can be arrange--" ("base", xpos="far_left", ypos="head")
                    ton "Done!" ("base", "base", "angry", "mid")
                    $ current_payout = 10
                    if states.gen.masturbating:
                        call gen_chibi("jerk_off_behind_desk")
                        gen "(This should be good...)" ("base", xpos="far_left", ypos="head")
                    her @ cheeks blush "W-{w=0.3}What would you like to know about, professor?" ("open", "base", "base", "R")
                    ton "I'd be happy with anything you'd like to tell me sweetie..." ("base", "base", "base", "L")
                    her @ cheeks blush "It's... It's quite embarrassing." ("disgust", "narrow", "worried", "down")
                    ton "Yes?" ("soft", "base", "raised", "L")
                    if states.her.status.stripping: # (Tonks asks if she stripped, later.)
                        her @ cheeks blush "Well, he asked me to dance for him..." ("open", "narrow", "base", "R_soft")
                        ton "Dance for him, you say..." ("open", "base", "raised", "R")
                        if states.gen.masturbating:
                            gen "(And you loved every second of it, judged by how much that butt was bouncing...)" ("angry", xpos="far_left", ypos="head")
                    elif states.her.status.show_pussy:
                        her @ cheeks blush "Well, he made me show him my privates..." ("open", "narrow", "base", "R_soft")
                        ton @ cheeks blush "You don't say..." ("base", "base", "raised", "L")
                        if states.gen.masturbating:
                            gen "(And you loved every second of it... I bet you were trying your hardest not to get wet!)" ("angry", xpos="far_left", ypos="head")
                    elif states.her.status.show_tits:
                        her @ cheeks blush "Well, he made me show him my breasts..." ("open", "narrow", "base", "R_soft")
                        ton @ cheeks blush "You don't say..." ("base", "base", "raised", "L")
                        if states.gen.masturbating:
                            gen "(And you loved every second of it... Those nipples could've cut glass!)" ("angry", xpos="far_left", ypos="head")
                    elif states.her.status.show_panties:
                        her @ cheeks blush "Well, he made me show him my panties..." ("open", "narrow", "base", "R_soft")
                        ton @ cheeks blush "Your panties, you say..." ("base", "base", "raised", "L")
                        if states.gen.masturbating:
                            gen "(And you loved every second of it... I bet you were totally wet under those panties!)" ("angry", xpos="far_left", ypos="head")
                    elif states.her.status.show_bra:
                        her @ cheeks blush "Well, he made take my top off..." ("open", "narrow", "base", "R_soft")
                        ton @ cheeks blush "Your top, you say..." ("base", "base", "raised", "L")
                        if states.gen.masturbating:
                            gen "(And you loved every second of it... I bet your nipples were completely stiff, against your bra!)" ("angry", xpos="far_left", ypos="head")
                    else: # Mentions Genie masturbating when she was talking to him, which is required to reach T3
                        her @ cheeks blush "Well, he made me stand here and talk to him about my day, while he touched himself..." ("open", "narrow", "base", "R_soft")
                        gen "We both know there's no proof of that happening, I was merely scratching my leg." ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
                    ton @ cheeks blush "And how did that make you feel?" ("soft", "base", "raised", "L")
                    her @ cheeks blush "Humiliated!" ("annoyed", "narrow", "base", "R_soft")
                    ton "And your headmaster, did he enjoy it?" ("base", "narrow", "raised", "mid")

                    if states.gen.masturbating:
                        if states.her.status.stripping:
                            her @ cheeks blush "He did seem to enjoy it." ("open", "closed", "base", "mid")
                            gen "(Yes! I thoroughly enjoyed that little show of yours, you slut!)" ("angry", xpos="far_left", ypos="head")
                            ton "I'm sure it was quite the sight...{w=0.4} Did you take your clothes off?" ("base", "narrow", "base", "L")
                            her "Professor!" ("disgust", "narrow", "base", "R")
                            her "I--" ("clench", "narrow", "base", "down")
                            ton "There's nothing to be ashamed of, if you're only doing it for the honour of your house..." ("soft", "base", "base", "L")
                            her "You believe so, Professor?" ("open", "base", "worried", "R")
                            ton "Of course! Otherwise, I wouldn't have suggested you sell favours to your headmaster in the first place." ("grin", "base", "base", "L")
                            ton "So, just continue doing what your headmaster asks of you, and make your house proud." ("base", "base", "base", "L")
                            gen "(Yes, anything I ask, you little--)" ("angry", xpos="far_left", ypos="head")
                        else:
                            her @ cheeks blush "He did seem to enjoy... it." ("soft", "narrow", "base", "down")
                            gen "(Damn right!)" ("angry", xpos="far_left", ypos="head")

                        call hide_characters
                        hide screen bld1
                        with d3
                        pause.2
                        call cum_block
                        call gen_chibi("cum_behind_desk")
                        with d3
                        pause.8

                        call cum_block
                        call bld
                        gen "{size=-5}*Argh*! YES!{/size}" ("angry", xpos="far_left", ypos="head")

                        her "" ("annoyed", "base", "base", "R")
                        ton @ hair horny "Seems like the headmaster enjoyed our little discussion..." ("horny", "base", "angry", "mid")
                        her "(.............)" ("soft", "base", "base", "mid")

                        call gen_chibi("cum_behind_desk_done")
                        with d3
                        pause.2

                        gen "*Ah-Ah*..." ("angry", xpos="far_left", ypos="head")
                        ton @ hair horny "What have you been doing back there?" ("soft", "narrow", "raised", "mid")
                        gen "I--" ("base", xpos="far_left", ypos="head")
                        her @ cheeks blush "Just \"scratching his leg\"... As always." ("open", "base", "worried", "mid")
                        ton "Right..." ("normal", "base", "shocked", "R")
                        ton @ hair basic "Well then, since my work here is done... I think I better get back to my regular duties." ("open", "closed", "base", "mid")

                    else:
                        gen "I sure--" ("grin", xpos="far_left", ypos="head")
                        ton "I'm asking Miss Granger." ("upset", "base", "base", "mid")
                        gen "Oh, of course!" ("base", xpos="far_left", ypos="head")

                        her @ cheeks blush "He did have the appearance of someone who was enjoying... \"it\"." ("open", "closed", "base", "mid")
                        her @ cheeks blush "Someone who was enjoying it a bit too much, even..." ("angry", "narrow", "base", "R_soft")
                        ton "That just means you did a great job, Miss Granger." ("base", "base", "base", "L")
                        ton "I'm sure your house benefited greatly from his enjoyment." ("horny", "base", "raised", "L")
                        her @ cheeks blush "I suppose..." ("soft", "base", "base", "R")
                        ton @ hair basic "Well, I do believe we're done here..." ("open", "closed", "base", "mid")
                        ton "Thank you for sharing these things with me, Miss Granger... I can see that you've put significant effort into helping your house." ("open", "base", "base", "L")
                        ton "They should be proud to have you." ("base", "base", "base", "mid")
                        her @ cheeks blush "Thank you, Professor..." ("base", "base", "base", "R")

                    ton @ hair basic "I'll leave you two to it..." ("base", "base", "base", "mid")
                    if game.daytime:
                        ton "Have a good day, Miss Granger." ("base", "base", "base", "L")
                        her "Good day, professor." ("open", "base", "base", "R")
                    else:
                        ton "Have a good night, Miss Granger." ("base", "base", "base", "L")
                        her "Good night, professor." ("open", "base", "base", "R")
                    ton "Professor..." ("horny", "base", "raised", "mid")
                    gen "Miss Tonks..." ("base", xpos="far_left", ypos="head")

                    call ton_walk(action="leave")


    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)
    $ states.ton.busy = True

    return
