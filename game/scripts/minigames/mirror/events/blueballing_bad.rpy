
# Mirror story: Blueballing Bad
label blueballing_bad:

    # Setup
    $ hermione.equip(her_outfit_default)
    $ tonks.equip(ton_outfit_default)
    $ game.daytime = True
    $ game.weather = "clear"
    stop weather
    stop music fadeout 1
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Blueballing Bad{/color}{/size}"

    nar "In an alternate universe, Genie, wanting to go back to Agrabah, never took any risks to keep his cover as the Headmaster of Hogwarts..."
    nar "And stopped being a pervert."
    call room("main_room")
    call gen_chibi("paperwork")
    with fade

    call music_block

    nar "Sitting at his desk, doing some paperwork peacefully, Genie suddenly heard some voices, talking loudly while getting closer and closer to the office door..."
    her "{size=-6}What now?{/size}"
    ton "{size=-6}Miss Granger... Enough is enough.{/size}"
    ton "{size=-6}Even if he was a bit perverted, surely that wouldn't--{/size}{w=1.0}{nw}"
    her "{size=-4}A little bit perverted?!{/size}"
    gen "(What's this fuss about?)" ("open", xpos="far_left", ypos="head")
    ton "{size=-4}Miss Granger, wait!{/size}{w=0.75}{nw}"
    play sound "sounds/door_down.ogg"
    with hpunch
    call her_chibi("stand", "door", "base")
    call gen_chibi("sit_behind_desk")
    call her_walk("mid", "base", speed=2.0)
    
    with d3
    $ hermione.strip("bottom", "panties")

    stop music fadeout 0.5

    her "{b}I AM NOT CRAZY!{/b}" ("scream", "closed", "angry", "mid", xpos="far_right", ypos="head")
    play sound "sounds/MaleGasp.ogg"
    gen "What the--" ("open", xpos="far_left", ypos="head")

    play music "music/Under-the-Radar by PhobyAk.ogg" if_changed

    call ton_chibi("stand", "door", "base")
    with d3

    her "I'm not crazy..." ("mad", "base", "annoyed", "mid")
    ton @ hair neutral "Miss Granger, you--" ("open", "wide", "shocked", "L", xpos="far_right", ypos="head")
    her "I {b}know{/b} what I saw. He has to be the one who stole my panties!" ("angry", "base", "annoyed", "mid")
    her "I knew that house elf was his!" ("mad", "base", "annoyed", "R")
    gen "The what?{w=0.5}{nw}" ("open", xpos="far_left", ypos="head")
    her "Who else would have the authority and be perverted enough to--" ("mad", "closed", "annoyed", "mid")
    gen "I'm right here you know. Also, you--" ("open", xpos="far_left", ypos="head")
    her "You commanded that thing to steal panties, {b}MY{/b} panties." ("angry", "base", "annoyed", "L")
    her "As if I would ever make up such a lie!" ("angry", "base", "annoyed", "L")
    her "Never." ("clench", "base", "angry", "mid")
    her "{b}NEVER!{/b}" ("scream", "base", "angry", "mid")
    her "I just--{w=0.25} I just need to find them to prove it!" ("mad", "base", "annoyed", "mid")

    call her_walk(xpos="480", ypos="400", speed=1.5)
    gen "You lost your--" ("base", xpos="far_left", ypos="head")
    call her_walk(xpos="418", ypos="430", speed=1.5)
    her "He--{w=0.2} He's covered his tracks... Or he made that {size=-3}idiot{/size} teacher Snape take them!" ("angry", "base", "annoyed", "R_soft")
    call her_walk(xpos="600", ypos="410", speed=1.5)
    ton @ hair upset "Miss Granger, please, you have to--{w=0.5}{nw}" ("open", "base", "annoyed", "stare")
    her "You think this is something-{w=0.25} You think this is bad?{w=0.25} This, this chicanery?!" ("angry", "wide", "angry", "L_soft", flip=True)
    call her_walk(xpos="599", ypos="410", speed=1.5)

    her "He's done worse!" ("shock", "base", "angry", "mid", flip=False)
    her "He asked me about my day!" ("mad", "base", "angry", "L")
    ton @ hair neutral "Wha--" ("normal", "shocked", "raised", "L")
    her "Are you telling me that you just happened to \"scratch your leg\" every time I spoke about those perverted Slytherin sluts?" ("disgust", "squint", "angry", "mid")
    gen "I really was--" ("open", xpos="far_left", ypos="head")
    her "NO!{w=0.25} {b}YOU{/b} were {b}MASTURBATING{/b}! {b}YOU{/b}, THE {b}HEADMASTER!{/b}" ("scream", "base", "angry", "L")
    gen "Miss Granger, please listen to us... You--" ("base", xpos="far_left", ypos="head")
    her "{b}YOU {size=+3}MADE ME{/size}{w=0.25} DO {size=+5}SILLY FACES!{/size}{/b}" ("scream", "closed", "angry", "mid")
    her "And I trusted you!" ("mad", "base", "annoyed", "up")
    her "I shouldn't have been blinded by the house points...{w=0.5} What was I thinking?! Giving him a chance to satisfy his male desires..." ("mad", "squint", "worried", "R_soft")
    her "He's a pervert." ("angry", "base", "worried", "L_soft")
    her "He's a pervert!{w=0.25} Ever since I talked to him about my grades, he just couldn't keep his hands out of his robe!" ("clench", "base", "annoyed", "mid")
    gen "I swear I wasn't--" ("base", xpos="far_left", ypos="head")
    her "Everyone kept telling me I was making stuff up..." ("clench", "base", "annoyed", "mid")
    her "\"Not the Headmaster!\"{w=0.25}, \"Our Headmaster is not like that!\"..." ("clench", "base", "angry", "up")
    her "{b}WHAT A {size=+2}SICK{/size} JOKE!{/b}" ("scream", "wide", "angry", "stare")
    her "I should have stopped him when I had the chance..." ("clench", "base", "annoyed", "R_soft")
    her "{size=-3}You--{/size}{w=1.0} You have to stop him Professor Tonks!{w=0.25} You--" ("mad", "wide", "worried", "R_soft")
    with hpunch
    stop music fadeout 0.5
    ton @ hair angry "{b}{size=+3}MISS GRANGER, YOU LOST YOUR SKIRT ON YOUR WAY IN!{/size}{/b}" ("scream", "closed", "angry", "mid")
    her "" ("open", "wide", "base", "down", xpos="mid", ypos="base")
    pause
    her "..." ("open", "wide", "base", "shocked")
    ton @ hair upset "..." ("annoyed", "base", "annoyed", "stare")
    gen "..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{w=0.5}{size=+5}-!{/size}" ("disgust", "wide", "worried", "R")

    call her_walk(action="run", xpos="door", ypos="base", speed=2.0)
    call her_chibi("leave")

    call music_block

    ton @ hair upset "..." ("annoyed", "base", "annoyed", "stare")
    ton @ hair neutral "I guess this proves that the greatest prudes are the ones with the biggest stick up their asses." ("soft", "base", "base", "L")
    gen "Tonks, what the fuck are you talking about?" ("open", xpos="far_left", ypos="head")
    ton @ hair neutral "I'm saying this girl should really learn how to loosen up." ("annoyed", "base", "annoyed", "L")
    gen "Why?" ("open", xpos="far_left", ypos="head")
    ton @ hair neutral "I mean, so what if you stole her panties?" ("annoyed", "base", "annoyed", "L")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton @ hair neutral "Wait, you didn't steal her panties?" ("annoyed", "base", "raised", "L")
    gen "No?! Why would I do that?" ("base", xpos="far_left", ypos="head")
    ton @ hair neutral "Really? You didn't do anything perverted for a whole month?" ("open", "shocked", "shocked", "mid")
    gen "No! I've just been reading, and sometimes summoning her to my office to talk and tutor her in exchange for house points!" ("open", xpos="far_left", ypos="head")
    ton @ hair neutral "What about the silly faces?" ("annoyed", "base", "raised", "L")
    gen "I panicked! She was begging for house points and I didn't want to blow my cover!" ("open", xpos="far_left", ypos="head")
    ton @ hair neutral "My god, you really are an innocent idiot." ("open", "wide", "shocked", "stare")
    gen "Hey!" ("open", xpos="far_left", ypos="head")
    ton @ hair neutral "You know I could erase people's memories if you get caught? Right?" ("open", "base", "base", "mid")
    gen "...Wait,{w=0.5} you can do that?" ("base", xpos="far_left", ypos="head")
    ton @ hair neutral "Well, not too often, or it might affect their brain, but--" ("open", "base", "raised", "mid")
    with hpunch
    play sound "sounds/card_punch1.ogg"
    gen "{b}{size=+6}I'VE BEEN BLUEBALLING MYSELF THIS WHOLE TIME, FOR NOTHING?!{/size}{/b}" ("open", xpos="far_left", ypos="head")
    ton @ hair neutral "Well..." ("soft", "base", "base", "R")
    with hpunch
    play sound "sounds/card_punch2.ogg"
    call gen_chibi("stand")
    call gen_walk("door", "base", speed=2.0)
    gen "{b}{size=+4}MISS GRANGER, COME BACK. I'LL PAY YOU ONE THOUSAND POINTS IF YOU LET ME MASTURBATE IN FRONT OF YOU!{/size}{/b}" ("open", xpos="far_left", ypos="head")
    call gen_chibi("leave")
    ton @ hair neutral "{b}WAIT NO! What are you doing?!{/b}" ("open", "shocked", "shocked", "R")
    call ton_chibi("leave")
    "Genie""{size=-3}{b}Hermione?! {w=0.5}Hermioooooooooooone!!!{/b}{/size}"


    $ renpy.end_replay()

label blueballing_bad_rewards:

    if not her_outfit_bb.unlocked:
        call unlock_clothing(text="New clothing items for Hermione have been unlocked!", item=her_outfit_bb)

    return
