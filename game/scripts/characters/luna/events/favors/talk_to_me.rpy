

### Luna Talks ###

label ll_pf_talk:

    if not _events_completed_any:
        gen "{size=-4}(All I'll do is have a little chat with her...){/size}" ("base", xpos="far_left", ypos="head")
        
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump luna_favor_menu
    return

label ll_pf_talk_end:

    # Setup
    stop music fadeout 2.0
    call hide_characters

    call gen_chibi("sit_behind_desk")

    # Increase level
    if states.lun.tier == 1:
        if states.lun.level < 3:
            $ states.lun.level += 1

    elif states.lun.tier == 2:
        if states.lun.level < 6:
            $ states.lun.level += 1

    elif states.lun.tier == 3:
        if states.lun.level < 9:
            $ states.lun.level += 1

    jump end_luna_event

### Tier 1 ###

label ll_pf_talk_T1_E1_intro:

    call ll_pf_talk

    $ states.gen.masturbating = False

    gen "So... About the infestation..." ("base", xpos="far_left", ypos="head")
    lun "*Sniff* *Sniff*" ("soft", "narrow", "base", "L")
    gen "[name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "*Sniff* *Sniff*" ("soft", "base", "raised", "down")
    gen "Are you alright?" ("base", xpos="far_left", ypos="head")
    lun "This is such a peculiar smell..." ("open", "base", "base", "mid")
    gen "(What's she talking about? What smell?)" ("base", xpos="far_left", ypos="head")

    menu:
        "\"The spratters?\"":
            lun "Wrackspurts, [name_genie_luna]." ("base", "base", "base", "mid")
            lun "I've never smelled them this strongly." ("base", "base", "base", "mid")
            lun "Can you not smell them, [name_genie_luna]?" ("base", "base", "base", "mid")
            gen "I guess I just got used to the smell..." ("base", xpos="far_left", ypos="head")
            lun "*Hmm*..." ("base", "base", "base", "mid")

        "-Sniff your armpits-":
            play sound "sounds/sniff.ogg"
            pause .4
            gen "(Good grief, when was the last time I took a shower...)" ("angry", xpos="far_left", ypos="head")
            gen "(It's high time I search for a bath in this place...{w} Although...)" ("base", xpos="far_left", ypos="head")
            gen "(I did have countless women of Agrabah confess to me that they liked my manly odour.)" ("grin", xpos="far_left", ypos="head")
            gen "Do you like this smell, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
            lun "Oh, I find the smell quite interesting, [name_genie_luna]." ("base", "base", "base", "mid")
            gen "(That's good enough for me...)" ("base", xpos="far_left", ypos="head")

    gen "So, is there anything more you can tell me about these spurts?" ("base", xpos="far_left", ypos="head")
    gen "I'll need some more information before we get started." ("base", xpos="far_left", ypos="head")
    lun "Of course, [name_genie_luna]... What would you like to know?" ("grin", "base", "raised", "mid")
    gen "Tell me...{w=0.4} Who else knows about it?" ("base", xpos="far_left", ypos="head")
    lun "*Hmm*...{w=0.4} Well, there's you and me..." ("soft", "base", "base", "downL")
    gen "Apart from us..." ("base", xpos="far_left", ypos="head")
    lun "Oh...{w=0.4} Well I did try warning some Slytherin boys about them..." ("open", "narrow", "base", "stare")
    lun "But they just laughed and told me that they'll make sure to stay away from any mistletoe..." ("upset", "closed", "base", "mid")
    gen "Mistletoe?" ("base", xpos="far_left", ypos="head")
    lun "Yes! Can you believe it?" ("open", "narrow", "annoyed", "mid")
    lun "Wrackspurts don't care about mistletoe...{w=0.4} Nargles on the other hand!" ("open", "closed", "annoyed", "mid")
    gen "What's a--" ("base", xpos="far_left", ypos="head")
    gen "Actually... One problem at a time..." ("base", xpos="far_left", ypos="head")
    gen "Did you tell anybody else? Seen any further signs of the infestation spreading?" ("base", xpos="far_left", ypos="head")
    lun "Oh!" ("soft", "wide", "base", "mid")
    lun "There was this one girl who was clearly getting bothered by them!" ("angry", "base", "base", "stare")
    lun "I was in the bathroom when I heard her!" ("soft", "base", "base", "mid")
    gen "(In the bathroom, *huh*.)" ("grin", xpos="far_left", ypos="head")
    lun "There were some weird noises coming from one of the stalls, so I called out to her, asking if she was okay." ("angry", "base", "base", "mid")
    gen "Weird noises you say?" ("grin", xpos="far_left", ypos="head")

    menu:
        "-Whip it out-":
            $ states.gen.masturbating = True
            $ states.gen.stats.masturbated_to_luna += 1

            hide luna_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8
        "-Pay attention-":
            pass

    lun "Indeed." ("angry", "base", "base", "mid")
    lun "So of course I had to do my best to reassure her that what she was experiencing was nothing to be afraid of..." ("grin", "closed", "base", "mid")
    lun "I told her about my own experiences...." ("open", "base", "base", "down")
    lun "But they must've really gotten to her, [name_genie_luna]...{w=0.4} She barely paid me any attention..." ("angry", "closed", "base", "mid")

    if states.gen.masturbating:
        gen "You have my full attention, girl...{w=0.4} Tell me more!" ("angry", xpos="far_left", ypos="head")
    else:
        gen "(Sounds like the opposite to me...)" ("base", xpos="far_left", ypos="head")

    lun "I fear the whole school might get overrun, [name_genie_luna]..." ("angry", "narrow", "base", "mid")
    lun @ cheeks blush "The way people are acting..." ("open", "base", "base", "downL")
    gen "You're seeing similar symptoms as your own?" ("base", xpos="far_left", ypos="head")
    lun "Not just that!" ("angry", "base", "base", "mid")
    lun "It's Their auras, [name_genie_luna]!" ("clench", "base", "base", "stare")

    if states.gen.masturbating:
        gen "*Ugh*... What? Auras?" ("angry", xpos="far_left", ypos="head")
        gen "(Please don't make this weird, girl...)" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Auras?" ("base", xpos="far_left", ypos="head")

    lun "They're far too red!" ("angry", "wide", "base", "mid")
    lun "According to my father's bestiaries, they should only ever produce a grey tinge to an aura..." ("mad", "base", "raised", "mid")

    if states.gen.masturbating:
        gen "Yes, yes... But what about the girl that made those weird noises? Tell me about her!" ("angry", xpos="far_left", ypos="head")
        lun "Well, I never saw her, [name_genie_luna]." ("angry", "closed", "base", "mid")
        lun "I just observed her aura. It was so fascinating!" ("soft", "closed", "base", "mid")
        lun "But... Whatever they're doing to be making auras red..." ("normal", "narrow", "base", "downL")
        gen "(Come on, say something naughty already!)" ("angry", xpos="far_left", ypos="head")
    else:
        gen "(*Tsk*... Auras...)" ("base", xpos="far_left", ypos="head")

    lun "[name_genie_luna], we need to warn people... Before it's too late!" ("angry", "base", "base", "mid")

    if states.gen.masturbating:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        lun "[name_genie_luna]?" ("upset", "base", "raised", "mid")
        gen "(This isn't working...)" ("base", xpos="far_left", ypos="head")

        pause .8
        call gen_chibi("sit_behind_desk")

    gen "Why don't we focus on a cure rather than try to convince people of the existence of something they can't even see." ("base", xpos="far_left", ypos="head")
    lun "But [name_genie_luna]..." ("angry", "narrow", "base", "mid")
    gen "Once we have a way to properly deal with them then I'm sure we could administer the cure without causing a fuss." ("base", xpos="far_left", ypos="head")
    lun "You believe there's a cure for something like this, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "I have a theory... And if it works, then it should let us expel those spurty buggers." ("base", xpos="far_left", ypos="head")
    lun "You've found a way to expel them on command?" ("clench", "base", "base", "mid")
    gen "Well, I wouldn't say on command... Now that is beyond even my own capabilities..." ("base", xpos="far_left", ypos="head")
    gen "I need to conduct some more tests, and once that's done, I'll put it into practice." ("base", xpos="far_left", ypos="head")
    lun "Oh! I can't wait!" ("crooked_smile", "happyCl", "base", "mid")

    if game.daytime:
        gen "So for now, you better head back to class." ("base", xpos="far_left", ypos="head")
        lun "Of course... Good luck [name_genie_luna]." ("grin", "base", "base", "mid")
    else:
        gen "So for now it'd be best for you to head off to bed." ("base", xpos="far_left", ypos="head")
        lun "Of course... Goodnight [name_genie_luna]." ("grin", "base", "base", "mid")

    pause .8
    call lun_walk(action="leave")

    gen "Sure is a loony one..." ("base", xpos="far_left", ypos="head")
    gen "Good thing she's hot." ("base", xpos="far_left", ypos="head")

    jump ll_pf_talk_end

label ll_pf_talk_T1_E2_intro:

    call ll_pf_talk

    gen "Let's continue with your training." ("base", xpos="far_left", ypos="head")
    lun "My training, [name_genie_luna]?" ("soft", "base", "raised", "mid")
    gen "*Err*... To become the best and first ever spurt hunter!" ("angry", xpos="far_left", ypos="head")
    lun "Oh!" ("grin", "base", "base", "mid")
    lun "Okay!" ("grin", "happyCl", "base", "mid")
    gen "Today we're going to put that theory of mine into practice." ("base", xpos="far_left", ypos="head")
    lun "Finally!" ("smile", "base", "base", "mid")
    gen "Now, I need to warn you... This could be quite dangerous." ("base", xpos="far_left", ypos="head")
    lun "Dangerous, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "Yes..." ("base", xpos="far_left", ypos="head")
    gen "Very dangerous!" ("base", xpos="far_left", ypos="head")

    lun "" ("soft", "wide", "base", "mid") #Wide eyed
    pause .8

    gen "If you don't do it correctly, you could end up with some severe burns..." ("base", xpos="far_left", ypos="head")
    gen "(Or mild chafing at the very least.)" ("base", xpos="far_left", ypos="head")
    gen "Which is why we're going to start by conducting some of the initial testing on myself." ("base", xpos="far_left", ypos="head")
    lun "But [name_genie_luna]!" ("angry", "wide", "base", "mid")
    lun "You didn't tell me this was going to be dangerous... If I knew you could potentially hurt yourself, then I would've never asked you to--" ("angry", "base", "worried", "mid")
    gen "Don't worry... I'm sure It'll be worth it for the cause..." ("base", xpos="far_left", ypos="head")
    lun "But [name_genie_luna], why not let me do it--" ("angry", "narrow", "base", "mid")
    gen "Nonsense!" ("base", xpos="far_left", ypos="head")
    gen "I've lived a very long life, you've got it all ahead of you..." ("base", xpos="far_left", ypos="head")
    lun "[name_genie_luna]... Surely--" ("mad", "closed", "base", "mid")
    gen "Don't you worry, I've been practising these movements for a very long time. I'm certain I'll be able to pull one off no problem..." ("base", xpos="far_left", ypos="head")
    lun "Okay..." ("upset", "narrow", "base", "mid")
    lun "I assume you won't be needing any of my help..." ("open", "narrow", "base", "down") #Looking down
    gen "On the contrary...{w=0.4} Your aid is integral for this to work, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "" ("soft", "base", "base", "mid") #Looks up again, surprised that he wants her help
    gen "Now... You just stand there for a bit." ("base", xpos="far_left", ypos="head")
    lun "Oh... Of course [name_genie_luna]!" ("soft", "narrow", "base", "stare")

    $ states.gen.masturbating = True
    $ states.gen.stats.masturbated_to_luna += 1
    hide luna_main

    nar "You pull out your cock and start stroking it."
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause .8

    gen "There we go..." ("base", xpos="far_left", ypos="head")
    lun "" ("grin", "base", "base", "mid") #Excited look
    call ctc
    lun "" ("base", "base", "raised", "mid") #quizzical look
    call ctc
    lun "Is it working?" ("open", "base", "raised", "mid")
    gen "Give me a moment..." ("base", xpos="far_left", ypos="head")

    nar "You move your gaze to the girl's chest, while rubbing your hardening cock with increased pace."

    lun "What is it that you're doing?" ("soft", "base", "raised", "mid")

    nar "A quizzical expression spreads across Luna's face as she, unbeknownst to her, watch her headmaster masturbate in front of her."

    lun "Are you casting a spell? I can see your arms moving." ("open", "base", "base", "mid")
    gen "*Ah*...{w=0.3} Yes...{w=0.3} I'm waving my wand all right..." ("base", xpos="far_left", ypos="head")
    lun "I knew it!" ("grin", "closed", "base", "mid")

    nar "As you continue stroking your cock, you watch as Luna's moment of excitement turns into confusion once more."

    lun "Is it supposed to take this long?" ("soft", "narrow", "base", "mid")
    gen "*Ah*...{w=0.3} Yes...{w=0.3} Sometimes..." ("base", xpos="far_left", ypos="head")
    lun "Sometimes?" ("soft", "base", "raised", "mid")
    lun "Isn't this the first time you're trying this?" ("angry", "narrow", "base", "mid")
    gen "Well...{w=0.3} *Ah*...{w=0.3} I just need to focus..." ("base", xpos="far_left", ypos="head")
    lun "Oooh... So, it's like the Patronus Charm?" ("soft", "wide", "base", "mid")
    gen "*Ah*...{w=0.4} The what?" ("base", xpos="far_left", ypos="head")
    lun "The Patronus... You focus on a Happy memory and if you succeed, a corporeal shape of your spirit animal bursts out from your wand!" ("grin", "base", "base", "mid")
    gen "*Ah*...{w=0.3} Yes, that's it...{w=0.3} Ten points to Ravenclaw!" ("base", xpos="far_left", ypos="head")
    $ ravenclaw += 10
    lun "Thank you, [name_genie_luna]!" ("base", "happyCl", "base", "mid")
    gen "Now, be quiet and stand there for a bit, will you?" ("base", xpos="far_left", ypos="head")
    lun "Yes [name_genie_luna]." ("base", "base", "base", "mid")

    nar "With great difficulty, you work your now softened shaft, staring at the girl's heaving chest."

    lun "" ("base", "base", "base", "downR") #looking away
    call ctc
    lun "" ("base", "base", "base", "mid") #Looks back
    call ctc
    lun "[name_genie_luna]?" ("open", "base", "raised", "mid")

    nar "You stop rubbing your cock and look up at Luna's face."

    call gen_chibi("sit_behind_desk")

    lun "What's your patronus?" ("open", "base", "base", "mid")
    gen "W--{w=0.2} What?" ("angry", xpos="far_left", ypos="head")
    lun "What's your spirit animal, [name_genie_luna]?" ("soft", "base", "base", "mid")
    lun "Surely you must've cast a patronus spell before..." ("grin", "base", "base", "mid")
    gen "*Err*..." ("base", xpos="far_left", ypos="head")

    menu:
        "\"A Rhinoceros...\"":
            lun "Really? Why a Rhino of all things?" ("soft", "base", "raised", "mid")
            gen "They're kinda Horny aren't they?" ("base", xpos="far_left", ypos="head")
            gen "Get it?" ("grin", xpos="far_left", ypos="head")
            lun "*Huh*?" ("upset", "base", "base", "mid")

        "\"A Sperm Whale...\"":
            lun "Wow, so it must be huge!" ("open", "wide", "base", "mid")
            gen "You bet!" ("grin", xpos="far_left", ypos="head")
            lun "That makes so much sense from a wizard of your calibre." ("grin", "base", "base", "mid")

        "\"A Sea Cucumber...\"":
            lun "A what?" ("soft", "base", "raised", "mid")
            gen "A Sea cucumber!" ("base", xpos="far_left", ypos="head")
            lun "I heard you... But why a Sea Cucumber?" ("open", "base", "raised", "mid")
            gen "Something about the shape I reckon." ("base", xpos="far_left", ypos="head")

        "\"A Blob-fish...\"":
            lun "A what?" ("soft", "base", "raised", "mid")
            gen "A Blob-fish!" ("base", xpos="far_left", ypos="head")
            lun "Why a Blob-fish?" ("mad", "base", "base", "mid")
            gen "They look pretty funny don't they?" ("base", xpos="far_left", ypos="head")
            lun "How is their appearance enough to manifest as your patronus?" ("open", "narrow", "base", "mid")

    # Patronuses seems to be the correct plural form of Patronus, not Patroni.
    lun "Patronuses are supposed to represent a hidden inner self that gets awakened in the time of need... Only a wizard who is obsessed about a particular animal would have it as their Patronus..." ("open", "closed", "base", "mid")
    gen "(What on earth is all this drivel?)" ("base", xpos="far_left", ypos="head")
    lun "Or are you pulling my leg, [name_genie_luna]?" ("clench", "narrow", "base", "mid")
    gen "Pulling--{w=0.2} Hey... You distracted me again!" ("base", xpos="far_left", ypos="head")
    lun "Oh... Sorry [name_genie_luna]!" ("soft", "wide", "base", "mid")
    lun "The other teachers do keep reminding me not to let my mind wander so much..." ("annoyed", "narrow", "base", "downR")
    gen "*Sigh*..." ("base", xpos="far_left", ypos="head")
    gen "It's not your fault..." ("base", xpos="far_left", ypos="head")
    lun "It's not?" ("mad", "narrow", "base", "mid")
    gen "No... We'll just have to try something different next time to keep you engaged..." ("base", xpos="far_left", ypos="head")
    lun "Oh... Okay!" ("angry", "base", "base", "mid") #Happy
    lun "..." ("base", "base", "base", "down") #Pondering
    gen "What's with that face?" ("base", xpos="far_left", ypos="head")
    lun "Oh... It's nothing... I was just thinking..." ("base", "happyCl", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Very well [name_luna_genie]... All things considered, I think we've at least done some progress today." ("base", xpos="far_left", ypos="head")
    gen "Well done." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "We have?" ("soft", "base", "base", "mid")
    lun @ cheeks blush "I mean...{w=0.3} Thank you [name_genie_luna]...{w=0.3} I didn't really do much..." ("open", "base", "base", "R") #blush #Looks away
    gen "(Is she blushing?)" ("base", xpos="far_left", ypos="head")
    gen "*Ahem*..." ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "" ("normal", "narrow", "base", "mid") #Looks back
    pause .8

    gen "I'm sure with your help, we'll find a way to get those spurts." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Okay, thank you [name_genie_luna]..." ("open", "base", "base", "down")

    if game.daytime:
        lun @ cheeks blush "I'll head back to class then, [name_genie_luna]." ("open", "base", "base", "R")
    else:
        lun @ cheeks blush "I'll head back to my dorm then, [name_genie_luna]." ("open", "base", "base", "R")

    gen "Yes, I'll let you know when I require further...{w=0.3} Assistance." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Okay!" ("base", "base", "base", "mid")
    lun @ cheeks blush "*Ehm*... Bye then..." ("soft", "base", "base", "mid")
    gen "Bye [name_luna_genie]..." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    jump ll_pf_talk_end

label ll_pf_talk_T1_E3_intro:

    $ states.lun.ev.talk_to_me.t1_e3_complete = True

    call ll_pf_talk

    gen "Right then... Let's have another crack at this shall we." ("base", xpos="far_left", ypos="head")
    lun "We're going to try and expel the wrackspurts again, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "That's right, [name_luna_genie]." ("base", xpos="far_left", ypos="head")
    lun "Can I see how you do it this time?" ("grin", "base", "raised", "mid")
    gen "*Err*... I'm not sure that's such a good idea..." ("base", xpos="far_left", ypos="head")
    lun "*Aww*... Why not?" ("annoyed", "base", "annoyed", "mid")
    gen "Well... Let's find out if it works first..." ("base", xpos="far_left", ypos="head")
    lun "Okay!" ("base", "base", "base", "mid")
    gen "I need to focus, so just follow my instructions..." ("base", xpos="far_left", ypos="head")
    lun "Of course, [name_genie_luna]!" ("grin", "base", "base", "mid")
    gen "Excellent... Just need to take out my wand and then we can begin..." ("base", xpos="far_left", ypos="head")
    gen "(Let's see if we can produce some real magic this time...)" ("base", xpos="far_left", ypos="head")

    $ states.gen.masturbating = True
    $ states.gen.stats.masturbated_to_luna += 1
    hide luna_main
    nar "You take your cock out and begin stroking it..."
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause .8

    gen "Now... Tell me a bit more about your experiences with the spratters..." ("base", xpos="far_left", ypos="head")
    lun "How's that supposed to--" ("soft", "base", "base", "mid")
    gen "Are you questioning my methods, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "Oh! Of course not!" ("mad", "narrow", "base", "mid")
    gen "Then answer my question..." ("base", xpos="far_left", ypos="head")
    lun "Right...{w=0.4} *Ehm*...{w=0.4} As I said before, they bother me at the most inopportune moments..." ("open", "narrow", "base", "R")

    nar "As the girl starts talking, you continue stroking your now hardening cock, taking in every word of her sexual experiences."

    lun "And there was that time down at the lake... Now I'd never think they'd be down there, I thought they hated water..." ("soft", "wide", "base", "mid")

    nar "As she goes on, talking about wrackspurts and how they make her feel, you notice that Luna has started grinding her legs together again."

    lun @ cheeks blush "*Ah*...{w=0.4} And the worst times are when I'm about to go to sleep...{w=0.4} It must be something with my pyjamas..." ("soft", "narrow", "base", "down")
    lun "[name_genie_luna]...{w=0.4} They're...{w=0.4} They're bothering me again..." ("base", "base", "base", "mid")
    gen "Just keep talking [name_luna_genie], they're sensing the magic..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh... So, it's working, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "Yes, just keep talking..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "But [name_genie_luna]..." ("open", "narrow", "base", "mid")

    nar "You keep stroking your cock as Luna stares at you, shifting her legs uncomfortably..."

    lun @ cheeks blush "[name_genie_luna], it feels weird... Please..." ("angry", "narrow", "base", "mid")
    gen "How weird does it feel, [name_luna_genie]? Describe it to me..." ("base", xpos="far_left", ypos="head")

    nar "Luna grinds her legs together even more as she tries to maintain eye contact with you, she then stutters for a moment as a wave of lust washes over her."

    lun @ cheeks blush "I--{w=0.2} I don't know how to describe it..." ("normal", "narrow", "base", "down")

    show screen blkfade
    with d5
    nar "You close your eyes, listening to the girl..."

    lun "It's--{w=0.2} *Ah*...{w=0.4} It's like a tingly sensation spreading from between my legs... Almost as If I'm about to wet myself..." ("base", "base", "base", "mid")
    lun "But it's--{w=0.2} It's different...{w=0.4} It feels really good." ("base", "base", "base", "mid")

    nar "An image of the girl's wet panties runs across your mind, and you feel your cock twitch slightly in your hand."

    lun "[name_genie_luna]... I don't know how long I can endure this... Please tell me it's working..." ("base", "base", "base", "mid")

    nar "You rub your cock even faster, and the sound of Luna's voice starts fading out of your mind..."

    lun "{size=-4}I can't bear it, [name_genie_luna]!{/size}" ("base", "base", "base", "mid")
    lun "{size=-4}I need--{/size}" ("mad", "wide", "base", "L", xpos="mid", ypos="base", flip=True, trans=dissolve)

    call gen_chibi("cum_behind_desk_done")
    call lun_chibi("stand", 230, 455, flip=True)
    play sound "sounds/gasp.ogg"


    nar "Your cock pulsates in your hand, and with a groan and a sudden rush of relief, you unload a torrent of cum all over your desk..."
    nar "As waves of pleasure spread across your body, you slowly begin to feel your other senses return to you..."

    hide screen blkfade
    with d9

    lun "[name_genie_luna]!" ("mad", "wide", "base", "L")
    gen "{size=-4}Oh shit!{/size}" ("angry", xpos="far_left", ypos="head") #small text
    lun "[name_genie_luna], you--" ("disgust", "wide", "base", "L")
    gen "I can explain!" ("base", xpos="far_left", ypos="head")
    lun "You've done it!" ("smile", "narrow", "base", "mid")
    gen "I was just scratching--" ("angry", xpos="far_left", ypos="head")
    gen "Sorry, what did you say?" ("angry", xpos="far_left", ypos="head")
    lun "You expelled the Wrackspurts!" ("grin", "happyCl", "base", "mid")
    gen "I did?" ("base", xpos="far_left", ypos="head")
    lun "And through your penis no less!" ("grin", "base", "base", "downL")
    lun "You're a genius!" ("grin", "base", "base", "mid")
    gen "Well...{w=0.2} *Err*...{w=0.2} I suppose--" ("base", xpos="far_left", ypos="head")
    lun "You've got to teach me how you did it!" ("angry", "wide", "base", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    gen "I mean...{w=0.4} I'd love to!" ("grin", xpos="far_left", ypos="head")
    lun "Yay!" ("base", "happyCl", "base", "mid")
    lun "So, how did you do it? I thought you were wielding your wand..." ("grin", "narrow", "base", "mid")
    lun "Or is that what you call a penis, do you call that a wand too?!" ("open", "wide", "base", "mid")
    lun "Did you cast a spell through it?--" ("soft", "wide", "base", "mid")
    gen "Slow down, [name_luna_genie]..." ("base", xpos="far_left", ypos="head")
    lun "Sorry [name_genie_luna]..." ("mad", "base", "base", "mid")
    gen "Well, you could say it's similar to a spell... I stroke my penis along the shaft and then--" ("base", xpos="far_left", ypos="head")
    lun "Can I do it now?" ("grin", "base", "base", "mid")
    gen "What? Right now?!" ("angry", xpos="far_left", ypos="head")
    lun "Yes!" ("smile", "wide", "base", "mid")
    gen "Sure!" ("grin", xpos="far_left", ypos="head")

    #Luna takes off her bottoms
    $ states.lun.status.show_panties = True
    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bottom")


    lun "Finally... A way to get rid of--" ("grin", "narrow", "base", "down")
    lun "Hold on a minute..." ("normal", "wide", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    lun "[name_genie_luna], I don't think this is going to work out..." ("angry", "base", "base", "mid")
    gen "What?! No! Keep going!" ("angry", xpos="far_left", ypos="head")
    lun "Well...{w=0.4} I just realised..." ("disgust", "narrow", "base", "down")
    lun "I don't have a penis, [name_genie_luna]..." ("angry", "narrow", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "You just realised?" ("base", xpos="far_left", ypos="head")
    lun "Yes..." ("annoyed", "base", "base", "R")
    lun "I don't have a shaft to stroke...{w=0.2} So how am I supposed to force them out?" ("angry", "narrow", "base", "downL")

    menu:
        "\"Are you serious...\"":
            pass
        "\".... What?\"":
            pass
        "\"..............\"":
            pass

    lun "" ("upset", "base", "base", "mid") #sad
    pause 1

    gen "..." ("base", xpos="far_left", ypos="head")
    lun "I'm sorry [name_genie_luna], I got a bit ahead of myself there..." ("angry", "narrow", "base", "mid")

    #Luna puts on her bottoms
    play sound "sounds/cloth_sound3.ogg"
    $ luna.wear("all")

    gen "No,{w=0.2} wait!" ("base", xpos="far_left", ypos="head")
    lun "[name_genie_luna]?" ("soft", "base", "raised", "mid")
    gen "*Err*... I'm sure we can think of something..." ("base", xpos="far_left", ypos="head")

    lun "" ("upset", "base", "base", "mid")
    pause .8

    gen "I know!" ("base", xpos="far_left", ypos="head")

    lun "" ("base", "base", "raised", "mid") #expectant
    pause .5

    gen "I'll give your body an inspection!" ("base", xpos="far_left", ypos="head")
    lun "An inspection?" ("soft", "base", "raised", "downL")
    lun "Is that what you did to figure out how to expel them from yourself?" ("open", "base", "raised", "mid")
    gen "Smart girl... That's exactly it!" ("base", xpos="far_left", ypos="head")
    gen "I'm sure with a thorough inspection, we'll figure out a way for you to expel them as well..." ("base", xpos="far_left", ypos="head")
    lun "You truly believe so?" ("grin", "base", "base", "mid")
    gen "Of course!" ("grin", xpos="far_left", ypos="head")
    gen "We'll have you spurting all over the place in no time, don't you worry!" ("base", xpos="far_left", ypos="head")
    lun "Yay!" ("base", "happyCl", "base", "mid")
    lun "Thank you [name_genie_luna]!" ("grin", "narrow", "base", "mid")
    lun "..." ("base", "base", "base", "R") #glances off

    if game.daytime:
        lun "Oh, shoot... I need to go... My lunch break is almost over." ("mad", "base", "base", "stare")
        gen "Of course... Off you go!" ("base", xpos="far_left", ypos="head")
    else:
        gen "But you better get some rest before that..." ("base", xpos="far_left", ypos="head")
        gen "(At least I do...)" ("base", xpos="far_left", ypos="head")
        lun "Oh... Of course, [name_genie_luna]!" ("mad", "base", "base", "stare")

    lun "Just let me know when you're ready to do the inspection." ("crooked_smile", "base", "base", "mid")
    gen "Certainly..." ("base", xpos="far_left", ypos="head")

    call lun_walk(path=[(240, 470),(440, 470),("mid", "base"),("door","base")])
    call lun_walk(action="leave")

    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(And now I wake up...)" ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(Okay, I guess all that did just happen...)" ("base", xpos="far_left", ypos="head")

    jump ll_pf_talk_end

label ll_pf_talk_T1_E4_repeat:

    call ll_pf_talk

    gen "How are you feeling, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "I...{w=0.4} I'm okay..." ("open", "narrow", "base", "down")
    lun "But I'm still worried about this burning sensation between my legs, [name_genie_luna]." ("upset", "narrow", "base", "mid")

    gen "I'm sure we'll find a way for you to deal with them once I've had a thorough inspection of your body...." ("base", xpos="far_left", ypos="head")
    lun "I do hope we'll find a solution soon... I've been spotting more and more of them through my spectrespecs by the day." ("upset", "narrow", "base", "R")
    gen "(With Tonks and Snape around, that's not surprising...)" ("base", xpos="far_left", ypos="head")
    gen "Well I better prepare for that inspection then..." ("base", xpos="far_left", ypos="head")
    lun "Yes...{w=0.4} Thank you, [name_genie_luna]." ("open", "base", "base", "mid")
    gen "Hold on...{w} Actually we may have a little problem..." ("base", xpos="far_left", ypos="head")
    lun "A little problem, [name_genie_luna]?" ("soft", "base", "base", "mid")
    gen "No, wait! It's a massive problem! A massive problem has arisen!" ("angry", xpos="far_left", ypos="head")
    lun "There's a massive problem?! [name_genie_luna], why didn't you tell me at the start!" ("clench", "base", "base", "mid")
    gen "It just started happening! Come here quick!" ("angry", xpos="far_left", ypos="head")
    lun "On it!" ("mad", "base", "base", "mid")

    $ states.gen.masturbating = True
    $ states.gen.stats.masturbated_to_luna += 1
    hide luna_main

    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause .8

    #Luna walks up to beside genie and turns
    call lun_walk(path=[(440, 470),(230, 470),(230, 455)])
    call lun_chibi("stand", 230, 455, flip=True)

    nar "As Luna rushes up to your desk, you pull out your cock and start stroking it."

    lun "[name_genie_luna]!" ("mad", "base", "base", "downL", xpos="mid", ypos="base", flip=True, trans=dissolve)
    lun "Your penis is getting all hard again!" ("angry", "narrow", "base", "downL")
    lun "How on earth did this happen so quickly?!" ("clench", "base", "base", "downL")

    gen "That's what I thought!" ("angry", xpos="far_left", ypos="head")
    lun "Does it hurt, [name_genie_luna]? Your penis looks as if it's about to burst!" ("angry", "base", "base", "downL")
    gen "*Ah*...{w=0.4} It...{w=0.4} It's fine, but you better keep a close eye on it as I deal with this." ("angry", xpos="far_left", ypos="head")
    lun "Yes, [name_genie_luna]!" ("mad", "base", "base", "mid")

    lun "" ("soft", "narrow", "base", "downL")
    nar "Luna fixes her gaze, and stares intently at your cock as you continue stroking it."
    nar "Even in her worried state, there's still quite a bit of excitement in her eyes."

    gen "Oh. I can't even look at it, tell me it still looks okay!" ("angry", xpos="far_left", ypos="head")
    lun "It's still intact, [name_genie_luna]!" ("angry", "narrow", "base", "downL")
    lun @ cheeks blush "Oh my...{w=0.4} It's twitching!" ("angry", "narrow", "base", "downL")
    gen "I can feel it coming, keep looking at it, [name_luna_genie]!" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "Yes, [name_genie_luna]!" ("clench", "base", "base", "downL")

    nar "You keep stroking your shaft as Luna watches your every move."
    nar "Stroking it faster and faster, you feel yourself getting closer and closer to the edge by the second."

    lun @ cheeks blush "It's pulsating! How many Wrackspurts do you have in there?" ("disgust", "base", "base", "downL")
    gen "It's...{w=0.4} Filled to the brim!" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "Do you need me to get Madam Pomfrey?" ("mad", "base", "base", "mid")
    gen "*Ah*...{w=0.4} Who?" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh my, they're making you go delirious!" ("angry", "happyCl", "base", "downL")
    lun @ cheeks blush "The Matron [name_genie_luna], should I fetch her?" ("angry", "narrow", "base", "mid")
    gen "Absolutely!" ("grin", xpos="far_left", ypos="head")
    nar "As the thought of Luna bringing a hot nurse crosses your mind, you feel yourself reaching climax."
    lun @ cheeks blush "I'll be back in just a moment!" ("angry", "happyCl", "base", "mid")

    #Luna walks to mid position
    call lun_walk(path=[(230, 455),(230, 470),(440, 470),("mid", "base")])
    call lun_chibi("stand", "mid", "base", flip=True)

    gen "*Argh*!!" ("angry", xpos="far_left", ypos="head")

    call lun_chibi("stand", "mid", "base", flip=False)
    lun "[name_genie_luna]?" ("mad", "base", "base", "mid", flip=False, trans=dissolve)

    call gen_chibi("cum_behind_desk")
    call cum_block
    call gen_chibi("jerk_off_behind_desk")
    lun "What is--" ("clench", "base", "base", "mid")
    call gen_chibi("cum_behind_desk")
    call cum_block
    gen "*Argh*..." ("angry", xpos="far_left", ypos="head")
    call gen_chibi("jerk_off_behind_desk")
    lun "[name_genie_luna], are you okay?!" ("angry", "base", "base", "mid")
    lun "Are you in pain?" ("angry", "narrow", "base", "mid")
    gen "Yes, it pains me that you didn't--" ("angry", xpos="far_left", ypos="head")
    call gen_chibi("cum_behind_desk")
    call cum_block
    gen "*Argh*-- *heavy panting*" ("angry", xpos="far_left", ypos="head")
    gen "Fetch the nurse in time..." ("angry", xpos="far_left", ypos="head")
    call gen_chibi("cum_behind_desk_done")
    with d3

    lun "[name_genie_luna]?" ("mad", "base", "base", "mid")
    gen "*Ah*... That was--" ("base", xpos="far_left", ypos="head")
    lun "Are you okay?" ("mad", "narrow", "base", "mid")
    gen "So good..." ("base", xpos="far_left", ypos="head")
    lun "Do I still need to fetch the matron?" ("angry", "narrow", "base", "mid")
    gen "The--{w=0.3} *Err*..." ("base", xpos="far_left", ypos="head")
    nar "You look around at your cum soiled desk."
    gen "(She might get a heart attack from seeing this battlefield...)" ("base", xpos="far_left", ypos="head")
    gen "It's...{w=0.3} I'm fine!" ("base", xpos="far_left", ypos="head")
    lun "Are you sure, [name_genie_luna]?" ("upset", "base", "base", "mid")
    gen "Yes...{w=0.3} *Ahem*...{w=0.3} Nothing a good nap won't sort out." ("base", xpos="far_left", ypos="head")
    lun "*Hmm*...{w=0.3} Okay then..." ("soft", "narrow", "base", "mid")
    lun "[name_genie_luna]..." ("mad", "narrow", "base", "mid")
    gen "Yes, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun "We'll have that inspection done soon, right?" ("angry", "narrow", "base", "mid")
    lun "I'm worried what might happen if they attacked me like this." ("disgust", "narrow", "base", "down")

    gen "Of course...{w=0.3} I'll check you out-- *Err*...{w=0.3} I mean, I'll have you checked as soon as possible!" ("base", xpos="far_left", ypos="head")
    lun "Thank Merlin..." ("open", "closed", "low", "mid")
    lun "Then let me know as soon as you're ready, [name_genie_luna]." ("angry", "base", "base", "mid")
    gen "Certainly..." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    jump ll_pf_talk_end

label ll_pf_talk_T2_E1_repeat:

    call ll_pf_talk

    gen "Tell me some more about these spurts..." ("base", xpos="far_left", ypos="head")
    lun "Again, [name_genie_luna]?" ("open", "base", "raised", "mid")
    gen "Yes... I still don't think I'm quite done with my personal research..." ("base", xpos="far_left", ypos="head")
    lun "Oh... Okay then..." ("soft", "base", "base", "mid")
    gen "One moment please." ("base", xpos="far_left", ypos="head")

    $ states.gen.masturbating = True
    $ states.gen.stats.masturbated_to_luna += 1
    hide luna_main

    nar "You pull out your cock and start stroking it."
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause .8

    gen "There we go..." ("base", xpos="far_left", ypos="head")
    gen "You may begin." ("base", xpos="far_left", ypos="head")

    lun "*Ehm*...{w=0.4} What would you like to know?" ("grin", "narrow", "base", "down")
    gen "Tell me more about how they make you feel." ("base", xpos="far_left", ypos="head")
    lun "Okay..." ("open", "base", "base", "mid")

    nar "You continue stroking your hardening cock in anticipation as Luna looks at you nervously."
    lun "..." ("normal", "narrow", "base", "downL")
    lun "*Ehm*... [name_genie_luna]..." ("open", "narrow", "base", "downL")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    lun "Could I...{w} Could I watch you do it?" ("open", "narrow", "base", "mid")
    gen "You want to...{w=0.4} Watch me?" ("base", xpos="far_left", ypos="head")
    lun "Yes, If I'm supposed to learn about these things, then wouldn't it be best if I watched you do it?" ("soft", "narrow", "base", "mid")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    lun "Please, [name_genie_luna]! Even if I'm not ready yet myself, I really want to be able to help you properly once I am!" ("mad", "base", "base", "mid")
    gen "Well...{w=0.4} *Ah*...{w=0.4} When you put it that way..." ("base", xpos="far_left", ypos="head")
    lun "Oh... Thank you [name_genie_luna], I'm so glad you trust me..." ("grin", "base", "base", "mid")

    #Luna walks up to beside genie and turns
    call lun_walk(path=[(440, 470),(230, 470),(230, 455)])
    call lun_chibi("stand", 230, 455, flip=True)
    call ctc

    lun "Wow...{w=0.4} It's quite big isn't it?" ("soft", "base", "base", "downL", xpos="mid", ypos="base", flip=True, trans=dissolve)
    gen "It gets bigger as I stroke it..." ("base", xpos="far_left", ypos="head")
    lun "Really?" ("mad", "base", "base", "mid")
    lun @ cheeks blush "How big is it going to get?" ("open", "base", "base", "downL")
    gen "Quite...{w=0.4} Quite a fair bit bigger..." ("base", xpos="far_left", ypos="head")

    nar "You look up at the girl, who's now watching your every stroke with excitement."

    lun @ cheeks blush "Wow, it's so much bigger now! It's like a unicorn horn!" ("open", "narrow", "base", "downL")

    nar "With Luna so close to you, you can't help but notice her reddening cheeks and quickening breath."

    lun @ cheeks blush "Wait, surely it can't be as hard as a unicorn horn..." ("soft", "base", "raised", "downL")
    gen "(*Ngh*...{w=0.4} You'd be surprised...)" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "It's more like...{w=0.4} like..." ("upset", "base", "base", "downL")
    gen "*Ah*...{w=0.4} Yes...{w=0.4} Tell me more about how big it is..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Like a python!" ("angry", "base", "base", "mid")
    gen "That's...{w=0.4} It...{w=0.4} Watch this python spit!" ("angry", xpos="far_left", ypos="head")

    call gen_chibi("cum_behind_desk")
    call lun_chibi("stand", 230, 455, flip=True)
    call cum_block
    lun "Whoa!" ("open", "wide", "base", "downL")
    call cum_block
    gen "*Argh*..." ("angry", xpos="far_left", ypos="head")
    lun "There's so much of it!" ("grin", "wide", "base", "stare")
    gen "(Yes, watch me spurt, you airheaded--)" ("angry", xpos="far_left", ypos="head")
    call cum_block
    gen "*Argh*-- *heavy panting*" ("angry", xpos="far_left", ypos="head")
    call gen_chibi("cum_behind_desk_done")
    call lun_chibi("stand", 230, 455, flip=True)
    with d3

    gen "*Ah*...{w=0.3} *Ah*...{w=0.4} *Ah*..." ("base", xpos="far_left", ypos="head")
    lun "Oh! It's shrinking again, that must mean it worked, right?" ("grin", "base", "base", "downL")
    gen "Don't look at that!" ("angry", xpos="far_left", ypos="head")
    lun "Oh! Sorry [name_genie_luna]!" ("mad", "base", "base", "mid")
    lun "I'll just go over there then!" ("soft", "base", "base", "mid")

    #Luna walks to mid position
    call lun_walk(path=[(230, 455),(230, 470),(440, 470),("mid", "base")])
    call lun_chibi("stand", "mid", "base", flip=False)

    lun "...{w} Do you feel better now, [name_genie_luna]?" ("soft", "base", "base", "mid", flip=False, trans=dissolve)
    gen "Much better..." ("base", xpos="far_left", ypos="head")
    lun "I'm so glad..." ("grin", "closed", "base", "mid")

    if game.daytime:
        lun "Well, I better head back to class." ("base", "base", "base", "mid")
        gen "Of course... Off you go!" ("base", xpos="far_left", ypos="head")
    else:
        gen "I'm spent..." ("base", xpos="far_left", ypos="head")
        lun "Oh...{w=0.4} Okay!" ("open", "base", "base", "mid")
        lun "I'll head off to my dorms then." ("base", "base", "base", "mid")
        gen "That'd probably be for the best." ("base", xpos="far_left", ypos="head")
        lun "Good night then, [name_genie_luna]." ("grin", "base", "base", "mid")
        gen "Good night [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    jump ll_pf_talk_end

label ll_pf_talk_T3_E1_repeat:

    call ll_pf_talk

    gen "Able to help me deal with those spurts again?" ("base", xpos="far_left", ypos="head")
    lun "Of course, what would you need me to do?" ("grin", "base", "raised", "mid")
    gen "Just stand there for a bit." ("base", xpos="far_left", ypos="head")
    lun "Oh... Okay, [name_genie_luna]." ("base", "happyCl", "base", "mid")

    $ states.gen.masturbating = True
    $ states.gen.stats.masturbated_to_luna += 1
    hide luna_main

    nar "You pull out your cock and start stroking it."
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause .8

    gen "So...{w=0.4} Any news on those spurts?" ("base", xpos="far_left", ypos="head")
    lun "*Ehm*..." ("soft", "base", "base", "mid")
    lun "Well, to be honest [name_genie_luna] they've not really left me alone at all." ("angry", "narrow", "base", "mid")
    gen "Really? I thought we had been taking good care of them." ("base", xpos="far_left", ypos="head")
    lun "Oh, don't get me wrong [name_genie_luna]. All our tests have helped me immensely." ("grin", "narrow", "base", "mid")
    lun @ cheeks blush "If it wasn't for you, I think I would've gone completely crazy by now..." ("open", "narrow", "base", "down")
    gen "(As if you're not already, you nympho!)" ("base", xpos="far_left", ypos="head")
    call ctc

    lun @ cheeks blush "*Ehm*, [name_genie_luna]..." ("soft", "narrow", "base", "mid")
    gen "*Ah*...{w=0.3} Yes, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I can't really see what you're doing from here..." ("open", "narrow", "base", "downL")
    lun @ cheeks blush "Wouldn't it be better if I came up and watched you?" ("base", "base", "raised", "mid")
    gen "I suppose..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Great!" ("crooked_smile", "base", "base", "mid")

    #Luna walks up to beside genie and turns
    call lun_walk(path=[(440, 470),(230, 470),(230, 455)])
    call lun_chibi("stand", 230, 455, flip=True)
    call ctc

    gen "..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "..." ("grin", "base", "base", "downL", xpos="mid", ypos="base", flip=True, trans=dissolve)
    gen "You suddenly went quiet..." ("base", xpos="far_left", ypos="head")
    gen "I don't think this will work if you just stand there..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh, sorry [name_genie_luna]..." ("mad", "base", "base", "mid")
    lun @ cheeks blush "Your penis is quite distracting." ("soft", "narrow", "base", "mid")
    gen "That's certainly one way to describe it..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Are they...{w} Would you say your penis is big, [name_genie_luna]?" ("open", "narrow", "raised", "downL")
    gen "Well..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Be modest-":
            gen "I'd say it's quite average..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Really? So, they can get bigger than this?" ("clench", "wide", "base", "mid")
            gen "If you compare it to an elephant trunk that is... Actually, when it comes to penis size, mine is absolutely massive!" ("base", xpos="far_left", ypos="head")
            gen "That's why I'm such a powerful wizard." ("base", xpos="far_left", ypos="head")
            gen "The two are directly related." ("base", xpos="far_left", ypos="head")
        "-Over-exaggerate-":
            gen "It's absolutely massive..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "I knew it!" ("grin", "base", "base", "downL")
            gen "Actually, I have to use magic to make it smaller than its true size." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Really?" ("angry", "narrow", "base", "mid")
            gen "Oh yes..." ("base", xpos="far_left", ypos="head")
            gen "Who do you think designed these robes?" ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "*Ehm*..." ("soft", "base", "base", "mid")
            gen "Me, of course!" ("base", xpos="far_left", ypos="head")
            gen "Ever since I normalised wearing loose-fitting robes, nobody has ever questioned me about it." ("base", xpos="far_left", ypos="head")
            gen "It is truly a curse... Sporting such a massive phallus..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "I--{w=0.2} I'm sorry [name_genie_luna]... I had no idea..." ("angry", "narrow", "base", "mid")
            gen "That's the downside of being such a powerful wizard..." ("base", xpos="far_left", ypos="head")
            gen "The more powerful you become, the larger the member... Yep... All that power goes straight to the head." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Oh, I think my dad told me something like that about the employees at the ministry." ("grin", "base", "base", "mid")
            gen "That would be the head above your shoulders, I'm still talking about the one between my legs." ("base", xpos="far_left", ypos="head")
        "-Play it down-":
            gen "Nah, it's tiny..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Really?" ("clench", "base", "base", "mid")
            gen "Yep..." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "How do other people even hide theirs then?" ("disgust", "base", "base", "downL")
            gen "Oh, you meant compared to other people?" ("base", xpos="far_left", ypos="head")
            gen "You should've specified... Size is quite relative, you know..." ("base", xpos="far_left", ypos="head")
            gen "This planet is tiny compared to the sun, which is tiny compared to the universe." ("base", xpos="far_left", ypos="head")
            lun @ cheeks blush "Then... How big is it compared to the average person?" ("open", "base", "base", "mid")
            gen "Absolutely massive!" ("grin", xpos="far_left", ypos="head")
            lun @ cheeks blush "I knew it..." ("grin", "base", "base", "downL")
            gen "I mean, that's to be expected from such a powerful wizard as myself." ("base", xpos="far_left", ypos="head")
            gen "Here's some advice for you... If you ever want to find out if a wizard is powerful, just check out his penis." ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "Truly?" ("soft", "base", "raised", "mid")
    gen "Of course!" ("grin", xpos="far_left", ypos="head")
    gen "The bigger the wand, the more powerful the wizard." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Wow... I can't believe I didn't know that..." ("angry", "base", "base", "downL")
    gen "Merlin, Saruman, Gandalf...{w=0.3} Jafar...{w=0.3} What do we all have in common?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I don't--" ("soft", "narrow", "base", "mid")
    gen "We all wear robes! To hide our true power, you see..." ("base", xpos="far_left", ypos="head")
    gen "(Although that last one had a power enlargement...)" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I see..." ("grin", "base", "base", "mid")
    gen "Now if you excuse me, I need to concentrate on this..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Of course [name_genie_luna]..." ("crooked_smile", "narrow", "base", "mid")
    gen "Feel free to tell me more about how big it is, by the way... It might help." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh... *Ehm*..." ("mad", "narrow", "base", "mid")
    nar "You continue stroking your cock in anticipation as Luna looks at you, pondering what to say."
    lun @ cheeks blush "Your penis is so big, [name_genie_luna]..." ("soft", "narrow", "base", "downL")
    gen "Yes, that's it... Keep going, tell me how great I am." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "And you're so powerful..." ("grin", "narrow", "base", "downL")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "That's it...{w=0.3} *Ah*...{w=0.3} How powerful am I?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "More powerful than Merlin!" ("smile", "base", "base", "mid")
    gen "*Ngh*...{w=0.3} Yeah...{w=0.3} That guy, he's so overrated!" ("base", xpos="far_left", ypos="head")
    nar "You feel yourself getting closer to the edge as Luna strokes your ego."
    gen "I'm... I'm close girl, keep going..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh... *Ehm*... I'm not sure what to--" ("angry", "narrow", "base", "downL")
    gen "Tell me I'm better than Jafar!" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "*Ehm*... I don't know who--" ("soft", "base", "base", "mid")
    gen "{size=+4}Tell me!{/size}" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "You're better than Jafar!" ("clench", "wide", "base", "mid")
    gen "That's it girl, feel my power!" ("base", xpos="far_left", ypos="head")

    call gen_chibi("cum_behind_desk")
    call lun_chibi("stand", 230, 455, flip=True)
    call cum_block
    lun @ cheeks blush "Whoa!" ("open", "wide", "base", "downL")
    call cum_block
    gen "*Argh*..." ("angry", xpos="far_left", ypos="head")
    lun "[name_genie_luna]!" ("soft", "wide", "base", "downL")
    lun "You truly are power--!" ("grin", "wide", "base", "stare")
    gen "I'm not done yet!" ("angry", xpos="far_left", ypos="head")
    call cum_block
    gen "*Argh*-- *heavy panting*" ("angry", xpos="far_left", ypos="head")
    call gen_chibi("cum_behind_desk_done")
    call lun_chibi("stand", 230, 455, flip=True)
    with d3

    lun "Wow... They went so far!" ("smile", "wide", "base", "L")
    lun "Is that related to your wizarding powers too?" ("angry", "base", "base", "mid")
    gen "*Ah*...{w=0.3} *Ah*...{w=0.3} That's just sheer willpower... And a couple of Kegel exercises every now and then." ("base", xpos="far_left", ypos="head")
    lun "Astonishing..." ("soft", "narrow", "base", "downL")
    gen "You can stop staring at it now..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh... Of course, [name_genie_luna]." ("angry", "narrow", "base", "mid")

    #Luna walks to mid position
    call lun_walk(path=[(230, 455),(230, 470),(440, 470),("mid", "base")])
    call lun_chibi("stand", "mid", "base", flip=False)

    lun "...{w} [name_genie_luna]?" ("open", "base", "base", "mid", flip=False, trans=dissolve)
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    lun "Do you mind answering a question?" ("base", "base", "base", "mid")
    gen "Shoot." ("base", xpos="far_left", ypos="head")
    lun "If a wizard's power is related to the size of his penis..." ("open", "base", "base", "mid")
    lun "Does that make you more powerful than normal when you stroke it?" ("soft", "base", "base", "mid")
    gen "I suppose..." ("base", xpos="far_left", ypos="head")
    gen "I sure feel more powerful when I do it." ("base", xpos="far_left", ypos="head")
    lun "Interesting... Thank you for answering." ("grin", "base", "base", "mid")

    if game.daytime:
        lun "Well, I better head back to class." ("base", "base", "base", "mid")
        gen "Of course... Off you go!" ("base", xpos="far_left", ypos="head")
    else:
        lun "Well... If that was everything..." ("base", "base", "base", "mid")
        gen "Yes, that shall do for tonight [name_luna_genie]." ("base", xpos="far_left", ypos="head")
        lun "Good night then, [name_genie_luna]." ("grin", "base", "base", "mid")
        gen "Good night [name_luna_genie]." ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    jump ll_pf_talk_end
