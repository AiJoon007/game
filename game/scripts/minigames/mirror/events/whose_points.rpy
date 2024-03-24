
# Mirror story: Whose points is it anyway?
label whose_points:

    # Setup
    $ hermione.equip(her_outfit_default)
    $ astoria.equip(ast_outfit_default)
    $ luna.equip(lun_outfit_default)
    $ game.daytime = True
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    call ast_chibi("stand", 380, 420)
    call her_chibi("stand", 450, 426)
    call lun_chibi("stand", 530, 430)

    $ luna.zorder = 16
    $ astoria.zorder = 14

    centered "{size=+7}{color=#cbcbcb}Whose points is it anyway?{/color}{/size}"

    show screen whose_points_screen
    hide screen blkfade
    with d5

    stop music
    play sound "sounds/epic_intro.ogg"
    call bld

    gen "Hello and welcome to \"whose points is it anyway\"!" ("grin", xpos="far_left", ypos="head")
    gen "The show where everything is made up and the points don't matter." ("grin", xpos="far_left", ypos="head")
    gen "Just like at Hogwarts." ("grin", xpos="far_left", ypos="head")
    play sound "sounds/applause01.ogg"
    her "(I hope I win! I need those house points.)" ("base", "happy", "base", "R", xpos="base", ypos="head", flip=False)

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 fadeout 1 if_changed

    gen "First, let me introduce today's contestants." ("base", xpos="far_left", ypos="head")
    gen "The curly haired harlot we all know and love. Give it up for Hermione!" ("base", xpos="far_left", ypos="head")
    play sound "sounds/applause01.ogg"
    her @ cheeks blush "..." ("grin", "base", "worried", "mid", xpos=500, ypos="base")
    play sound "sounds/wolf_whistle.ogg"
    her @ cheeks blush "..." ("base", "base", "worried", "mid")

    gen "The ravishing Ravenclaw who will rock your socks off... Luna!" ("base", xpos="far_left", ypos="head")
    play sound "sounds/applause01.ogg"
    lun "..." ("base", "wink", "base", "mid", xpos=650, ypos="base")
    play sound "sounds/giggle2_loud.ogg"
    lun "*heh*... hello." ("grin", "narrow", "base", "mid")

    gen "And the small girl with a big personality. Astoria!" ("base", xpos="far_left", ypos="head")
    play sound "sounds/applause01.ogg"
    gen "..." ("grin", xpos="far_left", ypos="head")
    play sound "sounds/gasp3.ogg"
    ast "Hey!" ("scream", "base", "angry", "mid", xpos=380, ypos="base")

    pause.5
    hide hermione_main
    hide luna_main
    hide astoria_main
    with d5
    pause.5

    gen "Today we're playing scenes from a hat." ("base", xpos="far_left", ypos="head")

    with hpunch
    play sound "sounds/MaleGasp.ogg"
    hat "What!? Stay the fuck away from me!"

    gen "But the notes are already inside you...{w=0.5} I put them in there last night." ("angry", xpos="far_left", ypos="head")

    hat "You put notes inside me without my consent?"
    play sound "sounds/burp.ogg"
    hat "*Burp*"
    hat "Pardon me."

    gen "Looks like we have our first prompt." ("base", xpos="far_left", ypos="head")
    gen "\"Things you might say in potions class, but also in your bedroom\"." ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "This cauldron hasn't been used for years. It's all mouldy and full of muck!" ("grin", "base", "worried", "mid", xpos="right", ypos="base")

    play sound "sounds/applause01.ogg"
    hat "Boo! There are no cauldrons in the bedroom!"

    gen "Quiet now, it was a good euphemism. Ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
    hide hermione_main
    with d3

    ast "Snape! Get your gross hands off my shoulders, you creep!" ("clench", "narrow", "angry", "mid", xpos="right", ypos="base")

    play sound "sounds/cough_male.ogg"
    mal "..."
    gen "I'm not sure you got the idea of the game there..." ("base", xpos="far_left", ypos="head")
    hide astoria_main
    with d3

    lun "Oops... I was supposed to squeeze the mucus out with my hands and not crush it." ("mad", "base", "raised", "L", xpos="right", ypos="base")

    play sound "sounds/applause01.ogg"
    gen "Sounds painful... Fifteen points to Ravenclaw." ("base", xpos="far_left", ypos="head")
    hide luna_main
    with d3

    her "(How's that worth more than mine?)" ("annoyed", "base", "worried", "mid")
    hide hermione_main
    with d3

    gen "Any more?{w=0.5} On to the next prompt then... Hat?" ("base", xpos="far_left", ypos="head")
    hat "Sorry, what did you *cough* call me? That's {i}Sorting Hat{/i} to you..."
    play sound "sounds/burp.ogg"
    hat "*Burp*"
    hat "That one was spicy..."
    gen "Ah, this one..." ("base", xpos="far_left", ypos="head")
    gen "\"Things you might do in Quidditch, but also with your lover\"..." ("grin", xpos="far_left", ypos="head")

    ast "I'm going first this time! I have a good one!" ("smile", "base", "base", "mid")
    gen "Go on..." ("base", xpos="far_left", ypos="head")
    ast "Madam Hooch! Get your gross hands off my quidditch robes, you creep!" ("clench", "narrow", "angry", "mid")
    gen "Again, I don't think you understand the game..." ("base", xpos="far_left", ypos="head")
    ast "Give me the points!" ("scream", "narrow", "angry", "mid", trans=hpunch)
    gen "Disqualified!" ("base", xpos="far_left", ypos="head")
    ast "Wait, you can't do that!" ("clench", "base", "base", "mid")
    gen "It's my game, I make the rules." ("grin", xpos="far_left", ypos="head")
    ast "(We'll see about that...)" ("annoyed", "narrow", "angry", "R")
    hide astoria_main
    with d3

    her "My turn."
    her @ cheeks blush "I love the feeling of a hard wooden object between my legs.{w=0.5} I tend to tense up during the climax." ("grin")

    play sound "sounds/applause01.ogg"
    gen "A bit direct, but I like it.{w=0.5} Fifteen points to Gryffindor." ("base", xpos="far_left", ypos="head")
    hide hermione_main
    with d3

    lun "It's quite exciting but also a bit hard. You need to make sure not to end up with one of the balls in your throat." ("angry", "closed", "low", "mid")

    gen "(I don't mind having you end up with one of mine in your throat one day, if you know what I mean...)" ("grin", xpos="far_left", ypos="head")

    play sound "sounds/applause01.ogg"
    gen "Twenty points to Ravenclaw." ("base", xpos="far_left", ypos="head")
    hide luna_main
    with d3

    her "(Seems like pleasing the judge is the way to go. Only one round left...)" ("annoyed", "base", "worried", "mid")
    hide hermione_main
    with d3

    gen "Last round ladies. You better make it a good one. It's still all to play for." ("base", xpos="far_left", ypos="head")
    gen "The last note, if you please!" ("base", xpos="far_left", ypos="head")

    hat "..."
    gen "If you please..." ("base", xpos="far_left", ypos="head")
    hat "I'm all out, looks like you only wrote two after all."

    gen "That can't be right..." ("angry", xpos="far_left", ypos="head")

    ast "Let me check professor!" ("smile", "base", "base", "mid")
    play sound "sounds/cloth_sound.ogg"
    ast "*Hmm*...{w} It has to be here somewhere..." ("annoyed", "base", "base", "down")
    ast "There it is! It was stuck under one of the folds!" ("smile", "base", "base", "mid")
    hide astoria_main
    with d3

    play sound "sounds/MaleGasp.ogg"
    hat "Are you calling me fat, young lady?!"

    ast "I'll read it for you, shall I?" ("smile", "closed", "base", "mid")

    gen "Go ahead..." ("base", xpos="far_left", ypos="head")

    ast "\"Things that you would not share with your classmates, but would share with... \"what do you call him again? Ah yes, \"[name_genie_luna]\"." ("open", "base", "base", "down")
    hide astoria_main
    with d3

    gen "(I don't remember writing that one...)" ("base", xpos="far_left", ypos="head")

    lun "I see invisible creatures... but people don't believe--" ("upset", "closed", "worried", "downR")
    hide luna_main
    hide screen bld1
    with d3
    pause.1

    stop music
    call her_chibi("lift_top", 450, 426)
    with d5
    pause.8

    $ hermione.strip("bra", "top")

    play sound "sounds/crowd_gasp.ogg"
    her @ cheeks blush "..." ("grin", "squint", "worried", "mid")

    gen "Five hundred points to Gryffindor!" ("grin", xpos="far_left", ypos="head")
    hide hermione_main
    with d3

    lun "That's cheating, I didn't even get to finish!" ("disgust", "wide", "annoyed", "mid")
    hide luna_main

    gen "Well, that's all for this episode of \"whose points is it anyway\"?" ("base", xpos="far_left", ypos="head")

    her "I win, all the points for me!" ("crooked_smile", "closed", "base", "mid")
    hide hermione_main
    with d3

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 fadeout 1 if_changed
    lun "Don't end now! This game is rigged!" ("scream", "narrow", "annoyed", "L")
    hide luna_main
    with d3

    gen "And remember, the points don't matter!" ("base", xpos="far_left", ypos="head")

    her "Wait, they don't?! I thought they were house points!" ("annoyed", "base", "worried", "mid")
    hide hermione_main
    with d3

    ast "Harlot! Harlot! Harlot!" ("grin", "closed", "base", "mid", xpos=400, ypos="base")

    lun "How do those points taste now?" ("silly", "narrow", "annoyed", "L", xpos=600, ypos="base")
    lun "The whole wizarding world is going to see your tits!" ("smile", "happyCl", "base", "mid")
    hide luna_main
    hide astoria_main
    with d3

    her @ tears crying "Oh no, I forgot about that!" ("shock", "base", "worried", "mid")

    play sound "sounds/epic_intro.ogg"
    play sound2 "sounds/applause01.ogg"
    gen "Good night!" ("grin", xpos="far_left", ypos="head")

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}To be continued?{/color}{/size}"

    $ renpy.end_replay()

screen whose_points_screen():
    add "images/rooms/room_of_requirement/whose_points.webp"
