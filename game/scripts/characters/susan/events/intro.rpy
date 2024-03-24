
### Susan Intro ###

label nt_he_susan_E1:
    ton "................." ("annoyed", "base", "shocked", "down", ypos="head", flip=False)
    gen "Something on your mind?" ("base", xpos="far_left", ypos="head")
    ton "Yes, there's this student in my class. She seems to be having a bad time." ("open", "narrow", "worried", "mid")
    gen "Education isn't meant to be enjoyable." ("base", xpos="far_left", ypos="head")
    ton "It's not that, she's being bullied by the other students apparently..." ("normal", "base", "worried", "R")
    gen "Why is she being singled out?" ("base", xpos="far_left", ypos="head")
    ton "For being shy... insecure..." ("upset", "closed", "base", "mid")
    gen "About what?" ("base", xpos="far_left", ypos="head")
    ton "About her massive tits!" ("open", "wide", "base", "mid")
    gen "!!!" ("angry", xpos="far_left", ypos="head")
    gen "Why would she be insecure about that?" ("base", xpos="far_left", ypos="head")
    gen "Surely that's something most girls would kill for!" ("grin", xpos="far_left", ypos="head")
    ton "That's what I said..." ("open", "closed", "shocked", "mid")
    ton "She didn't seem to think I was being genuine." ("soft", "base", "worried", "down")
    gen "They're probably just jealous of her." ("base", xpos="far_left", ypos="head")
    ton "Naturally... Even I'm jealous of those {b}milk-bags{/b} of hers!" ("open", "shocked", "shocked", "mid")
    gen "I definitely need to see them!" ("grin", xpos="far_left", ypos="head")
    ton "That being said, I'm quite worried about her..." ("open", "closed", "worried", "mid")
    ton "Lately she's been too shy to even answer the simplest of questions during my class." ("annoyed", "base", "worried", "R")
    ton "She's lost quite a few points for her house that way." ("upset", "base", "worried", "mid")
    ton "Not in my lessons, of course. I'd never take points from Hufflepuff!" ("soft", "base", "worried", "R")
    gen "Just send her my way, and I'll drown her in house points!" ("grin", xpos="far_left", ypos="head")
    gen "And show her that her bod--" ("base", xpos="far_left", ypos="head")
    gen "*Ahem!* Show her that she's appreciated..." ("angry", xpos="far_left", ypos="head")
    ton "That's what I was thinking..." ("open", "closed", "base", "mid")
    gen "Wait, you were?" ("angry", xpos="far_left", ypos="head")
    ton "Of course, why else would I be telling you about her?" ("open", "wide", "annoyed", "mid")
    gen "I don't know... banter?" ("base", xpos="far_left", ypos="head")
    gen "Snape sure as hell hasn't sent me any girls..." ("base", xpos="far_left", ypos="head")
    ton "I can teach him a thing or two about sharing - if you'd like..." ("soft", "base", "annoyed", "mid")
    ton "The more, the merrier in my opinion..." ("base", "happyCl", "base", "mid")
    gen "You don't mean Snape and I..." ("base", xpos="far_left", ypos="head")
    ton "Of course not, don't be silly!" ("base", "narrow", "base", "mid")
    ton "Maybe he's afraid you'd steal them from him if you got the chance..." ("horny", "base", "angry", "mid")
    gen "I have my doubts those girls he's talking about even exist..." ("base", xpos="far_left", ypos="head")
    gen "But don't tell him I said that." ("base", xpos="far_left", ypos="head")
    ton "I shall talk to Miss Bones." ("open", "closed", "base", "mid")

    if letter_favors.read:
        gen "Bones... I think I've heard that name before..." ("base", xpos="far_left", ypos="head")
        ton "Her Aunt works at the ministry." ("open", "base", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
    else:
        gen "*He-He*... Bones." ("grin", xpos="far_left", ypos="head")

    ton "I'm sure you'll find her less than bony..." ("base", "base", "angry", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton "But, you have to promise me that you won't go overboard with her!" ("mad", "base", "base", "mid")
    ton "I'd rather not risk having her contact that aunt of hers..." ("open", "base", "base", "R")
    gen "I can be slick and subtle when I want to..." ("base", xpos="far_left", ypos="head")
    ton "..." ("upset", "base", "worried", "R")
    ton "You're making me regret this decision already..." ("open", "closed", "worried", "mid")

    nar "As the hours pass, you convince Tonks to describe Susan's {b}massive tits{/b} to you..."
    nar "It didn't take much convincing..."

    $ states.ton.ev.hangouts.susan_e1 = True
    $ sb_event_pause += 1 # New event the next day.

    jump end_tonks_hangout_points


label susan_intro_E1:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"
    femv "*Uhm*... Professor Dumbledore, Sir?"
    femv "May I come in?"
    gen "Another girl?" ("base", xpos="far_left", ypos="head")

    $ d_flag_01 = False
    $ d_flag_02 = False

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Come on in.\"":
            femv "Thank you, Sir."

        "\"Who's there?\"":
            $ d_flag_01 = True # Knows name.
            sus "Sus--{w=0.3} Susan Bones, sir."
            gen "Susan Bones who?" ("grin", xpos="far_left", ypos="head")
            sus "... I'm sorry?"
            gen "*Ha-ha-ha-ha!*" ("grin", xpos="far_left", ypos="head")
            gen "(I'm a terrible person...)" ("base", xpos="far_left", ypos="head")
            sus "Professor?"
            gen "Yes, please come on in..." ("base", xpos="far_left", ypos="head")
            sus "Thank you, sir."

        "\"Not now.\"":
            $ d_flag_02 = True # Susan walks in anyway.
            femv "Okay, Sir."

    call sus_walk(action="enter", xpos="desk", ypos="base")

    if d_flag_02:
        gen "Didn't I say not now--" ("angry", xpos="far_left", ypos="head")
    else:
        gen "How can I help you--" ("base", xpos="far_left", ypos="head")

    play music "music/teddy-bear-waltz-by-kevin-macleod.ogg" fadein 1 if_changed
    pause.8

    $ susan.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
    show CG susan as cg zorder 17:
        pos (-1045, -390)
    with fade

    play sound "sounds/boing03.ogg" #Big boobas
    with hpunch
    gen "(Damn! Look at them titties...)"

    menu:
        "\"Hello, Gorgeous!\"":
            show CG susan as cg zorder 17:
                pos (-1045, -390)
                ease_quad 3.0 pos (-1045, -150)

            sus @ cheeks blush "*Ehm*..." ("soft", "happy", "base", "downR") # Embarrassed.
            sus @ cheeks blush "H-Hello..." ("open", "happy", "base", "downL")

        "\"Susan! How great to see you!\"" if d_flag_01:
            show CG susan as cg zorder 17:
                pos (-1045, -390)
                ease_quad 3.0 pos (-1045, -150)

            gen "Where have you been all my life?"
            sus @ cheeks blush "I--{w=0.4} I've been here at school for a couple of years now, Sir." ("open", "happy", "base", "mid")
            gen "You don't say..."

        "\"My day just got a whole lot brighter!\"":
            show CG susan as cg zorder 17:
                pos (-1045, -390)
                ease_quad 3.0 pos (-1045, -150)

            sus @ cheeks blush "Sir?" ("open", "happy", "base", "downL")
            gen "(Or should say darker?)"
            gen "(Those tits must cast a huge-ass shadow...)"

    show CG susan as cg zorder 17:
        zoom 1.0
        pos (-1045, -150)
        ease_quad 3.0 zoom 0.5 pos (0, 0)

    sus @ cheeks blush "Professor Tonks said you wanted to see me?" ("soft", "happy", "base", "downL")
    gen "Did she now?"
    gen "(I have to get that woman a drink for introducing me to this magnificently voluptuous creature...)"
    gen "Well, how nice of her."
    sus "Is there anything I can help you with, Professor?" ("angry", "happy", "base", "mid")
    gen "..."
    sus "S-Sir?" ("soft", "happy", "shocked", "mid")
    gen "(This must be that girl she wanted me to help with body confidence...)"
    gen "Did professor Tonks tell you why I wanted to see you?"
    sus "N-no...{w} I'm not in trouble, am I?" ("open", "happy", "base", "stare")
    gen "Don't worry, I just needed to confirm something - You're free to go..."
    sus "C-confirm something?" ("angry", "happy", "base", "mid")
    sus "So I'm not in trouble then?" ("open", "happy", "sad", "mid")
    gen "(This girl's got some confidence issues for sure...)"
    gen "No miss Bones... You're not in any trouble."
    sus "Very well..." ("soft", "closed", "low", "mid")

    if game.daytime:
        sus "I shall return to class then." ("open", "happy", "base", "right")
        sus "Good--{w=0.4} Good day, sir." ("open", "happyCl", "base", "mid")
    else:
        sus "I shall return to my dormitory then." ("open", "happy", "base", "right")
        sus "Good--{w=0.4} Good night, sir." ("open", "happyCl", "base", "mid")

    $ susan.hide()
    hide cg
    with fade

    call sus_walk(action="leave")

    call bld
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Massive tits...{w=0.4} confirmed." ("base", xpos="far_left", ypos="head")

    $ states.sus.busy = True

    $ states.sus.unlocked = True
    $ achievements.unlock("unlocksus", True)
    call popup("{size=-4}You can now summon Susan into your office.{/size}", "Character unlocked!", "interface/icons/head/susan.webp")

    $ states.sus.ev.intro.e1_complete = True
    $ ag_event_pause += 2 # Astoria intro starts in 2 days.

    call music_block
    jump main_room_menu
