

### Spectrespecs Quest ###

### Event 1 ###

label spectrespecs_E1:

    $ states.lun.ev.spectrespecs.e1_complete = True
    $ ll_event_pause = 1

    gen "*Hmm* let's see...{w=0.3} Witch weekly...{w=0.3} The Daily Prophet...{w=0.3} Now where is The Quibbler?" ("base", xpos="far_left", ypos="head")
    fre "Did you just say..."
    twi "{size=+4}The Quibbler?!{/size}"
    gen "Yes? Do you not carry it?" ("base", xpos="far_left", ypos="head")
    ger "Why on earth would we carry the quibbler?"
    gen "I don't know... You tell me." ("base", xpos="far_left", ypos="head")
    fre "Sir, that pile of rubbish is full of nothing but conspiracy theories and old wives tales."
    ger "No offence, but nobody in their right mind reads the quibbler..."
    gen "Well, as it happens I do intend to read the thing." ("base", xpos="far_left", ypos="head")
    ger "{size=-4}We're all doomed...{/size}"
    fre "Please don't tell me you take that thing seriously, sir..."
    gen "*Err*...{w=0.3} Of course not...{w=0.3} It's work related." ("base", xpos="far_left", ypos="head")
    fre "*Oh*... Thank Merlin."
    fre "Wait...{w=0.3} Work related?"
    fre "What on earth would someone in your position need a copy of the quibbler for?"
    gen "..." ("base", xpos="far_left", ypos="head")
    ger "Fred...{w=0.4} Don't ask our valued customer such questions."
    fre "...{w} It's got something to do with Luna Lovegood right?"
    ger "Obviously, Fred... But you don't need to--"
    gen "If you have to know... I intend on using it to get a better understanding of what that girl's thought process is like..." ("base", xpos="far_left", ypos="head")
    ger "...{w} Well, Good luck with that."
    ger "Our sister finds her personality endearing, but personally, I don't really see any good reason to try and humour her."
    gen "(I can think of at least two good reasons...)" ("grin", xpos="far_left", ypos="head")
    gen "(Two humongous--{w=0.5} Plump,{w=0.2} squishy...{w=0.3} and...{w=0.8} *Err*...)" ("grin", xpos="far_left", ypos="head")
    gen "*Oh*... bouncy--" ("grin", xpos="far_left", ypos="head")
    fre "Bouncy, sir?"
    gen "What?" ("base", xpos="far_left", ypos="head")
    fre "You said--"
    gen "Can you get a copy for me or not?" ("base", xpos="far_left", ypos="head")
    fre "I...{w=0.4} Yes, I suppose we could..."
    fre "Although it'd be simpler if you just had it delivered by owl, we could help you set it up--"
    gen "I don't want a subscription to the bloody thing... A copy of the latest issue is enough." ("base", xpos="far_left", ypos="head")
    fre "Right..."
    ger "*Sigh*... Well, as much as it pains me to make a special order for something like this..."
    ger "We'll order a copy and have it ready for you to pick up by tomorrow."
    gen "Excellent." ("base", xpos="far_left", ypos="head")
    ger "Will that be all, sir?"
    gen "Yes, that shall do for today..." ("base", xpos="far_left", ypos="head")
    twi "Pleasure doing business with you."

    return

label spectrespecs_E2_reminder:
    $ states.lun.ev.quibbler.stocked = True
    call music_block
    gen "(The Twins promised to get me a copy of that {i}Quiver{/i} tabloid, I should probably talk to them.)" ("base", xpos="far_left", ypos="head")

    jump main_room_menu

label spectrespecs_E2:

    $ states.lun.ev.spectrespecs.e2_complete = True

    gen "Boys..." ("base", xpos="far_left", ypos="head")
    twi "Professor Dumbledore, sir!"
    ger "Your order has been processed and is ready for purchase."
    fre "Please don't make us order something like this again, sir..."
    fre "Our provider almost fell into the fireplace laughing when we said we wanted a copy of the Quibbler..."
    gen "No promises..." ("base", xpos="far_left", ypos="head")
    twi "*Sigh*..."

    $ thequibbler_ITEM.unlocked = True

    return

label spectrespecs_E3:

    $ states.lun.ev.spectrespecs.e3_complete = True

    call book_start

    gen "The Rotfang conspiracy... A group of individuals set on taking down the ministry of magic using gum disease..." ("base", xpos="far_left", ypos="head")
    with fade
    gen "Grooming your beard the proper way...{w=0.4} To properly take care of your beard you first need the right tools, the saliva of the spitting..." ("base", xpos="far_left", ypos="head")
    with fade
    gen "Crumple-Horned Snorkack Sighting spotted in a small Swedish town..." ("base", xpos="far_left", ypos="head")
    with fade
    gen "Buy your shungite today at bob Barkins rock emporium..." ("base", xpos="far_left", ypos="head")
    with fade
    gen "Unfuzz the mystery...{w=0.4} Wrackspurts are invisible creatures that go into your ear, by thinking positive thoughts you can..." ("base", xpos="far_left", ypos="head")
    with fade
    nar "After wasting a massive amount of time, you finally close the magazine."

    call book_end

    gen "Now that was some great beard grooming advice..." ("base", xpos="far_left", ypos="head")
    gen "(Wait, why did I read the entire thing?!)" ("angry", xpos="far_left", ypos="head")
    gen "(Those twins were right... Who even buys this trash?)" ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(Well, I've read it now, so might as well check on Miss Lovegood about this supposed infestation...)" ("base", xpos="far_left", ypos="head")

    $ thequibbler_ITEM.owned = 0
    $ thequibbler_ITEM.used = True

    if game.daytime:
        jump night_start
    else:
        jump day_start

label spectrespecs_E4:

    $ states.lun.ev.spectrespecs.e4_complete = True

    gen "Alright, so I read that ridiculous magazine, but I still don't know what the hell those spratters are supposed to be..." ("base", xpos="far_left", ypos="head")
    lun "My daddy's magazine is not ridiculous, sir..." ("angry", "base", "annoyed", "mid")
    gen "I mean... If he's the one who wrote those articles..." ("base", xpos="far_left", ypos="head")
    lun "Our magazine is for the people, by the people!" ("smile", "closed", "base", "mid")
    lun "Anyone can submit an article to the quibbler." ("crooked_smile", "base", "base", "mid")
    gen "So... He just fact checks it?" ("base", xpos="far_left", ypos="head")
    lun "He prints it!" ("grin", "base", "base", "mid")
    gen "Well, even after reading it, I still haven't got the faintest clue what those creatures are supposed to be." ("base", xpos="far_left", ypos="head")
    gen "The only thing I learnt is that they go into your ear or something..." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "That's right...{w=0.5} At least that is what they're supposed to be doing." ("open", "narrow", "base", "down")

    lun @ cheeks blush "" ("angry", "narrow", "base", "mid")
    nar "Luna gives you another uncomfortable look, which she then quickly wipes off her face as she continues..."

    lun "Why don't you have a look for yourself sir, there should've been a pair of spectrespecs in the back of the magazine." ("soft", "base", "base", "mid")
    gen "(So the magazine comes with toys as well...{w=0.4} How is she actually taking this trash seriously?)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/paper_rustle.ogg"

    gen "*Ngh*!" ("base", xpos="far_left", ypos="head")
    gen "Why aren't they coming out!" ("base", xpos="far_left", ypos="head")
    gen "Hold on... These are cut-outs! What year is this?" ("base", xpos="far_left", ypos="head")
    lun "The severing charm should--" ("soft", "base", "raised", "mid")
    gen "Come here you stupid bird!" ("base", xpos="far_left", ypos="head")
    lun "Sir, what are you--" ("angry", "base", "raised", "L")
    gen "Lazy thing..." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", 225, "base")
    with fade

    pause .4
    call gen_walk(path=[(230, 470), (410, 470), (417, 426)])

    pause .4
    call gen_chibi("stand_alt")

    gen "Bird... Cut these out for me, will you?" ("base", xpos="far_left", ypos="head")
    lun "Sir, I doubt the--" ("mad", "narrow", "base", "L")
    faw "*Squawk*!"

    call gen_chibi("grab_high", phoenix_OBJ.xpos, phoenix_OBJ.ypos+365, flip=False)
    with d3

    play sound "sounds/scissors.ogg"

    pause .8

    lun "My word..." ("soft", "wide", "base", "mid")
    gen "Nice...{w=0.4} I knew there had to be a reason for your existence." ("base", xpos="far_left", ypos="head")

    pause .4
    call gen_chibi("stand", 417, 426, flip=False)
    pause .4

    call gen_walk(path=[(417, 426), (410, 470), (230, 470)])
    call gen_chibi("stand", 225, "base")
    call gen_chibi("sit_behind_desk")
    with fade


    gen "Right then... So, I just put these silly things on?" ("base", xpos="far_left", ypos="head")
    lun "Yes sir... Once you've put them on, you should be able to see--" ("grin", "base", "raised", "mid")

    $ wrackspurts_count = 0

    play sound "sounds/magic1.ogg"
    show layer screens at sepia(0.5, "#9402fc", desat=(0.25, 0.25, 0.5), brightness=0.25)
    show screen spectrevision
    if not renpy.mobile:
        show screen spectrevision_cursor
    with d9

    pause 0.5
    nar "The world around you starts shifting."

    gen "Gah!" ("angry", xpos="far_left", ypos="head")
    gen "(Who brought the UV light?)" ("angry", xpos="far_left", ypos="head")
    gen "(My desk looks like a Jackson Pollock painting!)" ("angry", xpos="far_left", ypos="head")
    lun "Do you see them?!" ("grin", "wide", "base", "mid")
    gen "*Err*... No, there's nothing in here... Everything just turned purple..." ("base", xpos="far_left", ypos="head")
    lun "But... I'm sure I saw some..." ("clench", "narrow", "base", "mid")
    gen "Nope... Absolutely no traces of spurts anywhere that I can see..." ("base", xpos="far_left", ypos="head")
    lun "Wrackspurts, sir..." ("mad", "narrow", "base", "mid")
    gen "(All I see is semen...)" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "And I fear in these quantities, they've proven themselves to be quite the pain, sir." ("normal", "narrow", "base", "down")
    gen "(I should probably clean this place one of these days...)" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Sir, I had been hoping that you'd find a solution by reading the magazine, because I wasn't sure how to tell you this..." ("open", "narrow", "base", "down")
    gen "(Although if I had somewhere else to release my seed, then this wouldn't be a--)" ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "..." ("upset", "closed", "base", "down")
    nar "Through the haze, you suddenly notice that Luna is rubbing her thighs together."
    gen "(What the--)" ("angry", xpos="far_left", ypos="head")

    gen "What are you doing, Miss Lovegood?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "It's the Wrackspurts, sir..." ("clench", "narrow", "base", "down")
    gen "What?" ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "They've been bothering me for months..." ("mad", "narrow", "base", "down")
    lun @ cheeks blush "And they're just like \"The Quibbler\" says, except..." ("clench", "closed", "base", "mid")
    nar "You can see Luna is rocking her pelvis as if grinding the air."
    lun @ cheeks blush "Except... It's not my brain they're making fuzzy." ("disgust", "base", "base", "mid")
    gen "So where exactly is this fuzzy feeling coming from, [name_luna_genie]?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I... I'm not sure I should say, sir." ("soft", "narrow", "base", "downR")
    gen "Then I don't see how I'm supposed to be able to--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Between my legs, sir..." ("disgust", "happyCl", "base", "mid")
    gen "!!!" ("angry", xpos="far_left", ypos="head")

    menu:
        "-Start Masturbating-":
            pass
        "-Don't-":
            gen "(As if I'd miss an opportunity like this...)" ("base", xpos="far_left", ypos="head")

    call gen_chibi("jerk_off_behind_desk")

    nar "You take your cock out and start stroking it..."

    gen "Nice...{w=0.4} I mean...{w=0.4} That's very unfortunate..." ("grin", xpos="far_left", ypos="head")
    gen "Tell me about these spurts... When do they usually bother you?" ("base", xpos="far_left", ypos="head")

    lun @ cheeks blush "At the most inopportune moments, sir!" ("clench", "narrow", "base", "mid")
    lun @ cheeks blush "" ("normal", "narrow", "base", "down")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "So what were you doing when it first happened?" ("base", xpos="far_left", ypos="head")
    gen "I need to know everything, with as much detail as possible." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "I believe it was when one of the Slytherin boys hit me with a tickling charm during potions..." ("disgust", "narrow", "base", "down")
    lun @ cheeks blush "A swarm of those pesky little wrackspurts flew right in beneath my skirt and started attacking me." ("angry", "base", "base", "down")
    lun @ cheeks blush "Buzzing around between my legs..." ("angry", "base", "base", "down")
    gen "(Sounds like a well aimed tickling charm to me...)" ("grin", xpos="far_left", ypos="head")

    lun @ cheeks blush "" ("upset", "narrow", "base", "mid")
    nar "Luna looks up at you again, shifting her legs around slightly."
    gen "(This girl's been missing out...)" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "But it doesn't make sense, sir..." ("clench", "closed", "base", "mid")
    lun @ cheeks blush "I've only heard of people's brain going fuzzy..." ("clench", "narrow", "base", "mid")
    lun @ cheeks blush "The way you're supposed to get rid of them is to think positive thoughts." ("disgust", "base", "base", "R")
    lun @ cheeks blush "But this is like an unbearable itch I can't scratch!" ("disgust", "narrow", "base", "mid")
    gen "(Oh, there's a way... You just don't know it yet...)" ("grin", xpos="far_left", ypos="head")
    gen "Does this happen often?" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Daily!" ("angry", "closed", "base", "mid")
    lun @ cheeks blush "They wouldn't leave me alone during today's flying lessons!" ("open", "narrow", "base", "mid")
    lun @ cheeks blush "I wasn't wearing my glasses, but I'm sure I must've flown through a whole swarm of them!" ("soft", "base", "annoyed", "mid")
    lun @ cheeks blush "My broom suddenly started shaking during a particularly tense training exercise..." ("mad", "base", "base", "mid")
    lun @ cheeks blush "And I could feel that fuzzy sensation build up between my legs again." ("angry", "narrow", "base", "down")
    gen "(Such a horny slut, just like the lot of them...)" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "This was the first time I had ever come across such a large amount in the open..." ("open", "base", "base", "mid")
    lun @ cheeks blush "And no matter how much I wriggled, they wouldn't leave me alone for the remainder of the lesson..." ("disgust", "narrow", "low", "down")
    nar "Luna awkwardly continues to grind her legs together in front of you."
    gen "(I bet you enjoyed every second of it...)" ("angry", xpos="far_left", ypos="head")
    lun @ cheeks blush "It was... intense... I could barely keep my broom steady..." ("soft", "closed", "low", "mid")
    lun @ cheeks blush "But I didn't want to alarm anyone, so I managed to pull through." ("soft", "narrow", "base", "down")
    lun @ cheeks blush "But..." ("angry", "base", "base", "down")
    lun @ cheeks blush "" ("angry", "base", "base", "mid")
    nar "Luna grinds her legs with even more vigour, as she looks into your eyes."
    lun @ cheeks blush "That feeling, sir..." ("mad", "narrow", "base", "mid")
    lun @ cheeks blush "It was as if something inside of me was building up... Desperate to come out!" ("open", "wide", "base", "mid")

    gen "(That's it slut, you asked for it!)" ("angry", xpos="far_left", ypos="head")
    gen "*ARGH*!" ("angry", xpos="far_left", ypos="head")

    call gen_chibi("cum_behind_desk")
    call cum_block

    $ wrackspurts_count = 15
    lun @ cheeks blush "Sir, there they are!" ("clench", "wide", "base", "mid")

    call cum_block
    $ wrackspurts_count = 25
    gen "Yes, take my spurt!" ("angry", xpos="far_left", ypos="head")

    call cum_block
    $ wrackspurts_count = 35

    pause 1.5
    call gen_chibi("cum_behind_desk_done")
    pause .8

    gen "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("base", xpos="far_left", ypos="head")
    lun "I saw them!" ("clench", "wide", "base", "mid")
    gen "That was awesome." ("base", xpos="far_left", ypos="head")
    lun "There are so many of them now!" ("open", "wide", "base", "mid")

    gen "I can see them!" ("grin", xpos="far_left", ypos="head")
    lun "I know! Fascinating creatures, aren't they?" ("grin", "base", "raised", "mid")
    gen "*Ha-ha*! Look at those buggers go!" ("grin", xpos="far_left", ypos="head")

    lun "And it's not just in here sir, they're everywhere!" ("open", "base", "annoyed", "mid")
    lun "The dungeons are full of them!" ("open", "base", "annoyed", "mid")

    play sound "sounds/magic1.ogg"
    show layer screens
    hide screen spectrevision
    hide screen spectrevision_cursor
    with d9

    nar "You quickly remove your glasses and Luna shifts into focus."

    gen "The dungeons you say?" ("base", xpos="far_left", ypos="head")
    lun "Yes, the potions classroom especially!" ("clench", "base", "base", "mid")
    gen "(How doesn't that surprise me...)" ("base", xpos="far_left", ypos="head")
    gen "What about Miss Tonks' classroom?" ("base", xpos="far_left", ypos="head")
    lun "It's even worse than the dungeons!" ("soft", "wide", "base", "mid")
    gen "Really?" ("angry", xpos="far_left", ypos="head")
    lun "Yes... They're everywhere..." ("clench", "base", "base", "mid")
    lun "On the desks... On the floor..." ("mad", "base", "base", "mid")

    lun "..." ("normal", "base", "base", "down")
    nar "Luna shifts her legs again, staring at her feet..."

    gen "Oh my..." ("grin", xpos="far_left", ypos="head")
    lun "On the railing going up to professor Tonks' office..." ("clench", "base", "base", "down")
    gen "On the railing too!?" ("grin", xpos="far_left", ypos="head")
    lun "Yes! I swear I even saw some on Tonks' face!" ("open", "wide", "base", "mid")
    gen "On her--" ("grin", xpos="far_left", ypos="head")
    lun "You have to help, sir!" ("mad", "happyCl", "base", "mid")
    lun "Please, if what I fear is true, then it's not just me being bothered by them..." ("angry", "narrow", "base", "mid")
    gen "Well...  Alright then..." ("base", xpos="far_left", ypos="head")

    lun "You'll do it?" ("clench", "base", "base", "mid")
    gen "I'll for sure do something..." ("base", xpos="far_left", ypos="head")
    lun "Oh, thank you, sir!" ("smile", "happyCl", "base", "mid")

    gen "But you're going to have to help me, Miss Lovegood." ("base", xpos="far_left", ypos="head")
    lun "Me? Why me?" ("soft", "base", "base", "mid")
    gen "I thought you wanted to help?" ("base", xpos="far_left", ypos="head")
    lun "Yes, but I thought...{w=0.4} *Ehm*...{w=0.4} Usually people don't really include me in these sorts of things." ("soft", "narrow", "base", "downR")

    nar "Luna glances away again, and you notice a glimpse of doubt in her eyes for a brief moment."

    gen "Most certainly, Miss Lovegood... You have the most experience with these things, after all..." ("base", xpos="far_left", ypos="head")
    gen "But if you don't want to be involved, then--" ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "No!" ("angry", "wide", "base", "mid")

    nar "Luna locks her eyes with you as she rubs her legs together once more."

    lun @ cheeks blush "I...{w=0.4} just didn't think--" ("angry", "base", "base", "down")
    lun @ cheeks blush "Of course, sir! I'll do anything that will help me deal with this..." ("open", "narrow", "base", "mid")
    gen "Excellent." ("base", xpos="far_left", ypos="head")
    gen "Then I shall let you know once I need your assistance." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Yes sir... Thank you, sir." ("base", "base", "base", "mid")
    gen "On your way now, Miss Lovegood." ("base", xpos="far_left", ypos="head")
    lun @ cheeks blush "Oh... Right..." ("grin", "base", "base", "R")

    call lun_walk("door", "base")
    pause .5
    lun "(I can't believe \"The\" Albus Dumbledore is asking for my assistance...)" ("base", "base", "base", "down", flip=True)
    lun "(I never would've thought.)" ("base", "base", "base", "downL")
    gen "(Damn... Her ass looks so good.)" ("base", xpos="far_left", ypos="head")

    call lun_walk(action="leave")

    gen "(Hopefully I haven't said yes to crazy...)" ("base", xpos="far_left", ypos="head")
    gen "(...{w=0.5} Although the blowjobs might be worth it...)" ("base", xpos="far_left", ypos="head")

    call popup("You have unlocked the ability to buy sexual favours from Luna.", "Congratulations!", "interface/icons/head/luna.webp")

    $ states.lun.wardrobe_unlocked = True
    $ states.lun.favors_unlocked = True

    call gen_chibi("sit_behind_desk")

    jump end_luna_event
