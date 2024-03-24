
### Let Classmate Molest Her ###

label start_hg_pr_grope:

    # Setup
    $ current_payout = 25

    if not _events_completed_any:
        gen "{size=-4}(Tell her to go get groped by one of her classmates?){/size}" ("base", xpos="far_left", ypos="head")
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump hermione_favor_menu

    return

label hg_pr_grope:

    call start_hg_pr_grope

    her "" (xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("base", "base", "base", "mid")

    #Intro.
    if not _events_completed_any:
        gen "You do like boys your age, don't you?" ("base", xpos="far_left", ypos="head")
        her "...?" ("normal", "base", "base", "mid")
        gen "One of your classmates maybe?" ("base", xpos="far_left", ypos="head")
        her "Well..." ("open", "base", "worried", "R")
        her "Must I really discuss things like this with you, [name_genie_hermione]?"
        her "It's a bit embarrassing..." ("annoyed", "base", "worried", "R")
        gen "Sure, I understand. I don't need to know the details..." ("base", xpos="far_left", ypos="head")
        gen "But here is what I need you to do today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Go confront that boy...{w=0.5} Or a girl, you fancy. The one you think is \"just so dreamy\"..." ("base", xpos="far_left", ypos="head")
        her ".......?" ("open", "base", "base", "mid")
        gen "And let them touch you..." ("base", xpos="far_left", ypos="head")

        if states.her.public_level < 3:
            $ _event.cancel()
            jump too_much_public

        her "Let them... Touch me, [name_genie_hermione]?" ("open", "base", "base", "mid")
        gen "Yes, touch you. The way boys touch girls?" ("base", xpos="far_left", ypos="head")
        gen "How old are you, [name_hermione_genie]? You look mature enough..." ("base", xpos="far_left", ypos="head")
        gen "Haven't you had \"the talk\" with your parents already?" ("base", xpos="far_left", ypos="head")
        her "\"The talk\", [name_genie_hermione]?" ("angry", "happyCl", "worried", "mid", emote="sweat")
        gen "Yes, \"the talk\"! About how boys are different than the girls...?" ("base", xpos="far_left", ypos="head")
        gen "Boys have a \"pee-pee\" and girls like to put that \"pee-pee\" in their mouths?" ("base", xpos="far_left", ypos="head")
        her "[name_genie_hermione]!!!" ("normal", "base", "base", "mid")
        her "What kind of demented parent would have such a talk with their child?" ("angry", "base", "angry", "mid")
        gen "{size=-3}I wish mine did.{/size}" ("base", xpos="far_left", ypos="head")
        her "I beg your pardon, [name_genie_hermione]?" ("annoyed", "squint", "base", "mid")
        gen "*Ahem*! I said, a responsible and caring one!" ("base", xpos="far_left", ypos="head")
        gen "Well, in any case. That is your task for today, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        gen "Find a way to persuade one of your classmates to fondle you a little..." ("base", xpos="far_left", ypos="head")
        her ".........." ("annoyed", "narrow", "angry", "R")
        gen "You are a pretty girl, it shouldn't be too hard." ("base", xpos="far_left", ypos="head")
        her "....................."
        her "How many points would I receive after completing such a task, [name_genie_hermione]?" ("disgust", "narrow", "base", "mid_soft")
        gen "*Hmm*... {number=current_payout} should do..." ("base", xpos="far_left", ypos="head")
        her "{number=current_payout} house points..." ("annoyed", "narrow", "angry", "R")
        her "...."
        her "Well, so be it then..." ("disgust", "narrow", "base", "mid_soft")
        gen "Great..." ("base", xpos="far_left", ypos="head")
        her "I'd better go now. The classes are about to start..." ("angry", "base", "angry", "mid")
    else:
        if states.her.tier >= 4:
            gen "I need you to go out there..." ("base", xpos="far_left", ypos="head")
            gen "Find a handsome guy and force yourself on him!" ("base", xpos="far_left", ypos="head")
            her "You mean like..." ("angry", "base", "base", "mid")
            her "In a sexual way, [name_genie_hermione]?" ("angry", "wink", "base", "mid")
            gen "What? No, I mean just let him get under your uniform, that's all..." ("base", xpos="far_left", ypos="head")
            her "Oh, I see..." ("grin", "happyCl", "worried", "mid", emote="sweat")
            her "I wonder who I could approach this time..." ("soft", "base", "base", "R")
            gen "Who it is, doesn't matter... It could be a group of them for all I care." ("base", xpos="far_left", ypos="head")
            her "Alright then... I will see you after the classes, [name_genie_hermione]. As usual." ("angry", "wink", "base", "mid")
            gen "Yes. Good luck." ("base", xpos="far_left", ypos="head")
        elif states.her.tier >= 3:
            gen "I need you to go out there, and make one of your classmates molest you a little." ("base", xpos="far_left", ypos="head")
            her "I understand, [name_genie_hermione]..." ("open", "base", "base", "mid")
            gen "Off you go then." ("base", xpos="far_left", ypos="head")
            her "..........."
        else:
            gen "How about you go let one of your classmates molest you a little again?" ("base", xpos="far_left", ypos="head")
            her "........" ("upset", "closed", "base", "mid")
            gen "{number=current_payout} house points, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
            her "[name_genie_hermione], it's just..." ("annoyed", "narrow", "angry", "R")
            her "I do not understand why I must do things like that..." ("annoyed", "narrow", "annoyed", "mid")
            gen "To help out your house?" ("base", xpos="far_left", ypos="head")
            her "That's not what I meant..." ("disgust", "narrow", "base", "mid_soft")
            her "Oh, never mind..." ("annoyed", "narrow", "angry", "R")
            her "The classes are about to start, I'd better go..."
            gen "Will you do it?" ("base", xpos="far_left", ypos="head")
            her "I don't know... Maybe..." ("disgust", "narrow", "base", "mid_soft")

    call her_walk(action="leave")

    jump end_hermione_event

label hg_pr_grope_fail:
    call start_hg_pr_grope

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "What do you say about going out and letting some lucky guy cop a feel?" ("base", xpos="far_left", ypos="head")

    jump too_much_public

label end_hg_pr_grope:
    $ gryffindor += current_payout

    gen "The Gryffindor house gets {number=current_payout} points!" ("base", xpos="far_left", ypos="head")
    her "Thank you, [name_genie_hermione]."

    label .no_points:

    call her_walk("door", "base")
    pause.2

    # Inner monologue
    if states.her.tier <= 2 and not _events_completed_any:

        her "(Why did I agree to this...)" ("disgust", "base", "worried", "down", ypos="base", xpos="base", flip=True, trans=d3)

    call her_chibi("leave")

    label .quick_end:

    $ states.her.status.public_groping = True

    # Increase Points
    if not _events_filtered_completed_all:
        $ states.her.public_level += 1

    jump end_hermione_event

label hg_pr_grope_intro:
    call her_walk(action="enter", xpos="mid", ypos="base")
    her "Good evening, [name_genie_hermione]." ("open", "base", "base", "R", xpos="mid", ypos="base", trans=fade)
    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
    gen "Did you finish your task?" ("base", xpos="far_left", ypos="head")
    her "I did, just as you asked [name_genie_hermione]..." ("open", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    if _events_filtered_completed_all:
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_grope

            "\"Give me the details.\"":
                pass

    stop music fadeout 3.0

    if not _events_completed_any:
        her "......" ("annoyed", "narrow", "angry", "R")
        her "I... *Uhh*..." ("soft", "base", "base", "R")

    gen "Did you let some lucky guy feel you up, or what?" ("base", xpos="far_left", ypos="head")

    return

### Tier 2 ###

label hg_pr_grope_T2_E1:

    call hg_pr_grope_intro

    her "Well, there is not much to tell..."
    her "I told that one guy I know that he could touch me a little if he wanted..." ("open", "base", "base", "mid")
    her "He thought I was joking at first..." ("annoyed", "base", "worried", "R")
    her "It was so embarrassing..." ("normal", "happyCl", "worried", "mid")
    gen "So, did he cop a feel or not?" ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "He did..." ("normal", "happyCl", "worried", "mid")
    gen "Well, where did he touch you, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... My legs..." ("annoyed", "base", "worried", "R")
    her "And my breasts a little I suppose..."
    gen "That's all?" ("base", xpos="far_left", ypos="head")
    her "Yes, [name_genie_hermione]..." ("open", "base", "base", "mid")
    her "It's getting late... I think I'd better leave now..." ("normal", "happyCl", "worried", "mid")
    her "I'm sorry, [name_genie_hermione]..." ("angry", "happyCl", "worried", "mid", emote="sweat")
    gen "Nothing to be sorry about, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "You did good. This will do for now." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_grope

label hg_pr_grope_T2_E2:

    call hg_pr_grope_intro

    her "I did, but it was all very awkward and embarrassing..." ("annoyed", "narrow", "angry", "R")
    gen "That's the whole point of it, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    gen "Tell me where you were touched today..." ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "*Ehm*..."
    her "Well, he touched me under my skirt a little..." ("angry", "base", "base", "mid")
    her "Then I let him rub my..."
    her "... my c-crotch through my panties, [name_genie_hermione]." ("angry", "narrow", "base", "down")
    gen "Very good... And what happened next?" ("base", xpos="far_left", ypos="head")
    her "He just sort of started... Touching himself, [name_genie_hermione]." ("open", "happyCl", "worried", "mid")
    her "So, I decided to leave..."
    gen "I see..." ("base", xpos="far_left", ypos="head")
    her "............." ("normal", "happyCl", "worried", "mid")

    jump end_hg_pr_grope

label hg_pr_grope_T2_E3:

    call hg_pr_grope_intro

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "I led this one guy from Hufflepuff to an empty classroom and I told him that he can touch me if he wanted." ("open", "base", "base", "mid")
    her "That I don't mind..."
    her "..........." ("annoyed", "base", "worried", "R")
    gen "And?" ("base", xpos="far_left", ypos="head")
    her "Well, he did touch me a little at first..." ("open", "base", "base", "mid")
    her "......" ("normal", "happyCl", "worried", "mid")
    gen "Don't make me pull every word out of you, [name_hermione_genie]!" ("base", xpos="far_left", ypos="head")
    gen "What happened?" ("base", xpos="far_left", ypos="head")
    her "Well..." ("open", "narrow", "worried", "down")

    stop music fadeout 1.0

    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
    her "He asked me to call him a \"sissy boy\"..." ("upset", "wink", "base", "mid")
    play music "music/Despair_by_erenik.ogg" fadein 1 if_changed # Music
    her "And he kept on reassuring me that he has a very small penis..." ("open", "base", "worried", "down")
    her @ tears soft "He just kept repeating that *sob*!..." ("angry", "base", "base", "mid")
    her @ tears soft "Why would anyone be like this?" ("angry", "base", "base", "mid")
    her "*Sob*! I Could not stay in his company a moment longer, so I just ran."
    gen "I'm sorry to hear this..." ("base", xpos="far_left", ypos="head")
    her @ tears soft "It was truly awful, [name_genie_hermione]..." ("angry", "base", "base", "mid")
    gen "There, there..." ("base", xpos="far_left", ypos="head")
    her @ tears soft "*Sob*!" ("normal", "base", "base", "R")
    gen "Will ten extra points make you feel better?" ("base", xpos="far_left", ypos="head")
    her @ tears soft "*Huh*? That would be very sweet of you [name_genie_hermione]." ("soft", "base", "base", "mid")
    gen "Of course... Don't mention it." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears soft "Thank you [name_genie_hermione]..." ("base", "base", "worried", "mid")

    $ current_payout += 10

    jump end_hg_pr_grope

### Tier 3 ###

label hg_pr_grope_T3_E1:

    call hg_pr_grope_intro

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Well... There is not much to tell..." ("open", "closed", "base", "mid")
    her "I found this one boy from Ravenclaw..."
    her "And I led him to one of the empty classrooms in the eastern wing..."
    her "He thought I wanted to make out with him..."
    her "But I told him that I only wanted him to touch me..."
    her "... So he did." ("normal", "happyCl", "worried", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "Well done, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "Will I be getting my points now?" ("upset", "wink", "base", "mid")
    gen "In a minute, [name_hermione_genie]. I have a question I would like to ask you before that." ("base", xpos="far_left", ypos="head")
    her "Yes?" ("open", "base", "base", "mid")
    gen "Did you enjoy it?" ("base", xpos="far_left", ypos="head")
    gen "Did it feel good when that boy touched you?" ("base", xpos="far_left", ypos="head")
    her "Oh..." ("open", "closed", "base", "mid")
    her "Well, he was rather handsome I suppose..."
    her "I didn't hate it, if that's what you mean, [name_genie_hermione]..." ("upset", "closed", "base", "mid")
    gen "I see..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_grope

label hg_pr_grope_T3_E2:

    call hg_pr_grope_intro

    her "Well..." ("open", "closed", "base", "mid")
    her "I'm not sure whether or not this counts, but..."
    her "During Herbology class today..."
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "I let this one boy slide his hand under my skirt..." ("upset", "wink", "base", "mid")
    her "So while Professor Sprout explained the differences between {i}mandrake{/i} and {i}mandragore{/i}..."
    her "--Something I already knew of course--..." ("open", "squint", "base", "mid")
    her "I let my lab partner grab my buttocks once..." ("upset", "wink", "base", "mid")
    her "And that is all..."

    menu:
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")

        "\"Kudos to you for doing this during class.\"":
            her "Thank you, [name_genie_hermione]." ("base", "happyCl", "base", "mid")
            gen "I say you deserve to get paid." ("base", xpos="far_left", ypos="head")

        "\"You can do better than that, [name_hermione_genie].\"":
            gen "I'm afraid I cannot pay you." ("base", xpos="far_left", ypos="head")
            her "Yes, I know, [name_genie_hermione]. I am sorry." ("open", "base", "base", "mid")
            gen "Just make sure you try harder next time." ("base", xpos="far_left", ypos="head")
            her "I will, [name_genie_hermione]."

            jump end_hg_pr_grope.no_points

    jump end_hg_pr_grope

label hg_pr_grope_T3_E3:

    call hg_pr_grope_intro

    her "................." ("annoyed", "narrow", "angry", "R")
    gen "???" ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "I don't want to talk about it, [name_genie_hermione]..." ("annoyed", "narrow", "angry", "R")
    gen "Come off it, [name_hermione_genie]... Spit it out." ("base", xpos="far_left", ypos="head")
    her "................." ("annoyed", "narrow", "annoyed", "mid")
    her "But... It's so embarrassing..." ("open", "base", "worried", "mid")
    her "Do I really have to, [name_genie_hermione]?" ("normal", "happyCl", "worried", "mid")
    gen "Yes, I happen to love embarrassing things!" ("grin", xpos="far_left", ypos="head")
    her "................." ("annoyed", "narrow", "angry", "R")
    her "Well, alright..."
    her "I approached this one guy that I've always found attractive..."
    her "After talking for a bit, I finally managed to muster up enough courage to ask him to follow me..."
    her "Normally I wouldn't dare..." ("open", "base", "base", "mid")
    her "But the fact that I was doing this as a task entrusted to me by someone else..."
    her "It made it easier somehow..."
    gen "Happy to help, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "So... I led him towards a secluded spot behind one of the bookshelves in the library." ("open", "narrow", "worried", "down")
    her "And once we got there, I told him that he could touch me wherever he wanted..."
    her "And..."
    her ".........." ("clench", "narrow", "base", "down")
    gen "And, What?" ("base", xpos="far_left", ypos="head")
    her "....................." ("normal", "happyCl", "worried", "mid")
    play music "music/Despair_by_erenik.ogg" fadein 1 if_changed # Music
    her "He started to touch my--{w=0.4} feet, [name_genie_hermione]." ("scream", "happyCl", "worried", "mid")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    gen "Your \"Feet\"? You meant to say \"breasts\", right?" ("base", xpos="far_left", ypos="head")
    gen "Or is this some zoomer lingo that I'm too unhip to understand?" ("base", xpos="far_left", ypos="head")
    her "No, [name_genie_hermione]..." ("disgust", "narrow", "base", "mid_soft")
    her "He took off my shoes and socks..."
    her "Then he--"
    her @ tears soft "He started to smell my toes, [name_genie_hermione]!" ("angry", "base", "base", "mid")
    her @ tears soft "I felt so...{w=0.4} Violated!" ("angry", "base", "base", "mid")
    gen "Wait... Are you telling me he didn't even touch your tits, or your butt?" ("base", xpos="far_left", ypos="head")
    gen "Or even in-between your thighs?!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush tears crying "No, [name_genie_hermione]... *Sob*!" ("shock", "narrow", "base", "down")
    gen "Alright, then what happened?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears crying "Nothing! I couldn't bear the humiliation... I just ran..." ("angry", "narrow", "base", "mid")
    her "I even left my shoes behind... I had to come back later to pick them up."
    her @ cheeks blush tears messy "*Sob*!............" ("angry", "squint", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "I'd probably wash those shoes out if I were you." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "*Sob*! Why couldn't he just touch my breasts like any normal boy would, [name_genie_hermione]... *Sob!*" ("angry", "squint", "base", "mid")
    gen "There, there..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush tears messy "Will-- *Sob*... Will I still receive my points [name_genie_hermione]?" ("angry", "squint", "base", "mid")
    gen "*Hmm*... I suppose, you did get molested..." ("base", xpos="far_left", ypos="head")
    gen "Although in a rather unconventional manner..." ("base", xpos="far_left", ypos="head")
    gen "Yes, you've most definitely earned your points today..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_grope

### Tier 4 - ###

label hg_pr_grope_T4_E1:

    call hg_pr_grope_intro

    her "......" ("annoyed", "base", "worried", "R")
    her "Well..." ("disgust", "base", "base", "mid")
    her "During the potions class today..." ("soft", "base", "base", "mid")
    her "I wrote a note on a piece of paper..." ("open", "base", "base", "mid")
    her "I was about to slide it to my lab partner's coat, when..."
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed # Music
    her "Professor Snape snatched it right out of my hand..." ("annoyed", "narrow", "angry", "R")
    her @ cheeks blush "He then read it out aloud for the entire class..." ("annoyed", "narrow", "annoyed", "mid")
    her @ cheeks blush "I thought I was going to die from embarrassment..." ("disgust", "narrow", "annoyed", "down")
    gen "What did the note say?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Well..." ("open", "narrow", "worried", "down")
    her @ cheeks blush "It said... \"You can touch my butt if you want, I bet professor Snape would never notice\"." ("open", "narrow", "worried", "R")
    her @ cheeks blush "Of course, the entire class, including Snape, then burst into laughter..." ("angry", "narrow", "base", "down")
    her "It was so embarrassing..."
    her @ cheeks blush "Professor Snape really is the worst..." ("angry", "base", "angry", "mid")
    gen "Yes, I think we've established that." ("base", xpos="far_left", ypos="head")
    gen "What happened then?" ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "Class was over, and everyone started packing up their things..."
    her "As I was hurriedly trying to put away some vials, two nasty-looking boys from Slytherin cornered me..." ("open", "narrow", "worried", "mid")
    gen "Uh-oh." ("base", xpos="far_left", ypos="head")
    her "Don't worry [name_genie_hermione]... They weren't being mean to me or anything."
    her "In fact... They wanted to take me up on the offer."
    gen "Your offer?" ("base", xpos="far_left", ypos="head")
    gen "Oh, the note!" ("base", xpos="far_left", ypos="head")
    her "Yes..." ("soft", "base", "base", "R")
    her "I mean, it wasn't meant to be an open invitation or anything..." ("open", "base", "base", "R")
    her @ cheeks blush "But seeing that Snape and my lab partner had already left..." ("soft", "base", "base", "R")
    her "Well, I decided I might as well go through with it..."
    her "So, once everyone else had left the classroom..."
    her "I let them touch me..." ("angry", "base", "base", "mid")
    her "And not only did they touch my butt... They touched me everywhere, [name_genie_hermione]..."
    gen "\"Everywhere\", *huh*?" ("base", xpos="far_left", ypos="head")
    her "Yes...{w=0.4} Everywhere, [name_genie_hermione]..." ("angry", "narrow", "annoyed", "stare")
    her "Their grubby little hands went under my skirt, under my shirt..." ("open", "narrow", "base", "mid_soft")
    her "I must say, it was quite overwhelming... And I started breathing quite heavily..." ("open", "narrow", "base", "down")
    her @ cheeks blush "And noticing this, one of them put his hand over my mouth, while running the other over my chest..." ("soft", "narrow", "annoyed", "mid")
    her @ cheeks blush "..." ("base", "narrow", "base", "stare")
    gen "So...{w=0.4} What happened then?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh...{w=0.4} *Ehm*...{w=0.4} Well, the rest was a bit of a blur to be honest, as my head started spinning..." ("angry", "wink", "base", "mid")
    gen "I guess that's a plausible enough excuse..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Huh*?" ("angry", "base", "base", "mid")
    gen "Very good work today, [name_hermione_genie]. Very good indeed." ("base", xpos="far_left", ypos="head")

    gen "Sounds to me like you had a good time." ("base", xpos="far_left", ypos="head")
    her "I'm just doing what is necessary to help my house." ("open", "closed", "base", "mid_soft")

    jump end_hg_pr_grope

label hg_pr_grope_T4_E2:

    call hg_pr_grope_intro

    her "Actually something quite unexpected happened to me today, [name_genie_hermione]..." ("soft", "base", "base", "mid")
    her "Right after the D.A.D.A class..." ("open", "base", "base", "mid")
    gen "D.A.D.A?" ("base", xpos="far_left", ypos="head")
    her "Defence Against the Dark Arts, [name_genie_hermione]." ("open", "closed", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    her "Anyway..." ("open", "base", "base", "mid")
    her "This stocky Hufflepuff boy came up to me..." ("open", "base", "base", "R")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    her "He said that someone had told him that I allow boys to touch me..." ("angry", "wink", "base", "mid")
    gen "(\"Allow\"... More like encourage...)" ("base", xpos="far_left", ypos="head")
    her "Of course, normally I would deny everything..." ("soft", "narrow", "base", "R")
    her "But I decided not to waste the opportunity..." ("open", "closed", "base", "mid")
    her "So, I led the boy to a quiet spot, and let him touch me..." ("soft", "narrow", "base", "stare")
    her "I let him run his hands up and down my thighs..." ("base", "narrow", "base", "stare")
    her "I let him fondle my breasts..." ("base", "narrow", "base", "up")
    her "..." ("base", "closed", "base", "up")
    her "" ("clench", "base", "base", "stare")
    gen "[name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh, *Ehm*... Yes, I made sure to do all the usual things you expect from me, [name_genie_hermione]!" ("angry", "base", "base", "mid")
    gen "That's great, [name_hermione_genie]." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_grope

label hg_pr_grope_T4_E3:

    call hg_pr_grope_intro

    her "Well... I tried..." ("upset", "wink", "base", "mid")
    her "But it sort of--{w=0.2} *Ehm*..." ("upset", "wink", "base", "mid")
    her "Well, it sort of escalated into something else..." ("base", "narrow", "base", "stare")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # Music
    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*..." ("upset", "wink", "base", "mid")
    her "I sort of... Got caught while I was letting this one boy fondle my breasts..." ("upset", "wink", "base", "mid")
    gen "You got caught? By one of the teachers?" ("base", xpos="far_left", ypos="head")
    her "No, [name_genie_hermione]..." ("angry", "base", "base", "mid")
    her "By the boy's girlfriend..." ("soft", "base", "base", "R")
    gen "Uh-oh..." ("base", xpos="far_left", ypos="head")
    gen "I bet she was pissed..." ("base", xpos="far_left", ypos="head")
    her "Yes, she was furious with him...{w=0.4} At first." ("angry", "base", "base", "mid")
    her "But then--" ("angry", "wink", "base", "mid")
    her "*Ehm*...{w=0.4} Then she started to touch my breasts as well..." ("angry", "narrow", "worried", "down")
    gen "Whoa... Wait, hold on a second..." ("base", xpos="far_left", ypos="head")
    her "Yes, it took me by complete surprise as well... I didn't know what to say or do." ("angry", "narrow", "angry", "down")
    her @ cheeks blush "I kind of just stood there in shock, and just let it happen..." ("disgust", "closed", "worried", "down")
    gen "You just stood there while she touched you? Surely that's not all--" ("base", xpos="far_left", ypos="head")
    her "No [name_genie_hermione]... While she was touching me, the boy started profusely apologizing to her." ("angry", "base", "base", "mid")
    her "It was kind of surreal to be honest..." ("annoyed", "narrow", "base", "down")
    her "In the midst of his apology, she suddenly snapped and told him to be quiet, while she firmly grabbed a hold of my nipples at the same time..." ("angry", "closed", "base", "mid")
    her "Of course, I expected the worst... I mean, she had me pinned up against the wall, and with the grip that she had, I didn't dare to move a muscle..." ("angry", "happyCl", "base", "mid")
    her "But after a brief pause, she just said..." ("angry", "narrow", "base", "mid")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    her "\"I love you baby, and I want to share everything with you\"..." ("open", "narrow", "base", "mid")
    her @ cheeks blush "\"... And that includes your whores\"." ("disgust", "narrow", "base", "mid")
    gen "Whoa! Wait... Who is this girl exactly?" ("angry", xpos="far_left", ypos="head")
    her "Of course, I did not like being called a whore by some Slytherin Harlot..." ("annoyed", "narrow", "base", "R")
    gen "(Ignored again...)" ("base", xpos="far_left", ypos="head")
    gen "So, what you're saying is that this girl wanted to \"share\" you between herself and her boyfriend?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes... And the way she said it... Well, it made it sound like I was just some toy for them to use." ("angry", "narrow", "worried", "down")
    her "I suppose this is what they call a \"sweet and romantic gesture\" amongst the Slytherins..." ("disgust", "narrow", "worried", "R")
    gen "So true love {size=+5}does{/size} exist after all." ("base", xpos="far_left", ypos="head")
    gen "Then what happened?" ("base", xpos="far_left", ypos="head")
    her "*Ehm*... Well..." ("disgust", "narrow", "worried", "mid", emote="sweat")
    her "They both started touching me..." ("upset", "wink", "base", "mid")
    her "And then they started kissing in front of me..." ("annoyed", "base", "worried", "R")
    her "A moment later, their hands were all over each other."
    her "I felt like the third wheel in that situation, so I just slipped away quietly..."
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "So you didn't think that perhaps staying a little longer... Or taking some initiative..." ("base", xpos="far_left", ypos="head")
    her "What are you implying?" ("annoyed", "base", "worried", "mid")
    gen "No matter..." ("base", xpos="far_left", ypos="head")

    jump end_hg_pr_grope
