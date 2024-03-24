### Yule Ball Ending ###

default her_ev_yule_ball_ending_e1 = Event(id="her_ev_yule_ball_ending_e1", wait=2, label="ball_ending_E1", priority=0, req="game.daytime", repeat=False)

label ball_ending_start:
    gen "[name_hermione_genie], that ball you've mentioned..." ("base", xpos="far_left", ypos="head")
    gen "When did you say it would start again?" ("base", xpos="far_left", ypos="head")
    her "The autumn ball?!" ("grin", "base", "base", "mid")
    her "I'm so excited!!! I can't wait for it!" ("grin", "happyCl", "base", "mid")
    her "Just two more days, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
    gen "That soon, *huh*?" ("base", xpos="far_left", ypos="head")
    her "Yep! I still have a tonne of preparation to do, though." ("soft", "base", "base", "R")
    gen "Well then I better not keep you occupied any longer..." ("base", xpos="far_left", ypos="head")
    gen "Unless..." ("base", xpos="far_left", ypos="head")
    gen "Maybe we could..." ("grin", xpos="far_left", ypos="head")
    her "Have some fun?" ("soft", "narrow", "base", "mid_soft")
    gen "You read my mind, girl." ("grin", xpos="far_left", ypos="head")

    $ states.her.ev.yule_ball.started = True
    $ ss_event_pause += 2
    $ her_ev_yule_ball_ending_e1.enqueue()

    jump hermione_favor_menu

screen genie_snape_shake_hands(shake=False):
    if shake:
        add "characters/snape/chibis/handshake/hand_01.webp" pos (220, 205) zoom 0.5
    else:
        add "characters/snape/chibis/handshake/hand_00.webp" pos (220, 205) zoom 0.5

label ball_ending_E1:
    stop music fadeout 1.0

    call sna_walk(action="enter", xpos="desk", ypos="base")
    pause.8

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    sna "Genie..." ("snape_01", xpos="base", ypos="base")
    gen "Severus?" ("base", xpos="far_left", ypos="head")
    sna "I think I may have figured out why your magic does not work the way it should..." ("snape_05")
    gen "Seriously?!" ("angry", xpos="far_left", ypos="head")
    sna "Yes..." ("snape_23")
    sna "It's quite obvious actually... I'm surprised that it didn't cross my mind before."
    sna "You see, the thing is that every building in Hogwarts is enchanted with all kinds of protection spells..." ("snape_24")
    gen "Protection spells, *huh*?" ("base", xpos="far_left", ypos="head")
    sna "Yes..." ("snape_23")
    sna "Very powerful, old, and nasty magic..."
    sna "Even the land itself is heavily enchanted for miles in every direction..." ("snape_24")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    sna "Basically, any number of spells could be interfering with your powers around here..." ("snape_25")
    gen "Wait, then how come you have no problems casting {i}your{/i} spells?" ("base", xpos="far_left", ypos="head")
    sna "Well, you see, my magic is \"Hogwarts magic\"..." ("snape_05")
    sna "But I suspect your powers are alien enough to be perceived as a threat."
    gen "Interesting..." ("base", xpos="far_left", ypos="head")
    sna "I think if you manage to get away far enough from the school grounds--" ("snape_24")
    gen "I will be able to go home!{w=0.5} finally..." ("base", xpos="far_left", ypos="head")
    sna "Yes, and the best time to do that would be tonight." ("snape_02")
    sna "While everyone is preoccupied with that bloody Autumn ball, you could sneak out unnoticed..." ("snape_23")

    ### SHAKE HANDS WITH SNAPE ###
    hide snape_main
    call blkfade

    hide screen bld1
    call gen_chibi("hide")
    call sna_chibi("hide")
    show screen genie_snape_shake_hands(False)

    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    pause 1
    call hide_blkfade

    gen "Right, today is the night of the Autumn ball..." ("base", xpos="far_left", ypos="head")
    gen "So it ends tonight then..." ("base", xpos="far_left", ypos="head")
    sna "Seems like it..." ("snape_09")
    call hide_blkfade
    pause.5

    sna "So... Just in case I will never see you again..." ("snape_05")
    gen "Right..." ("base", xpos="far_left", ypos="head")

    show screen genie_snape_shake_hands(True)
    with d3
    pause 2

    sna "The past several months were the best months of my life, Genie..." ("snape_26")
    sna "Thank you for that...{w=0.3} you incredible traveller from another world..."
    sna "Thank you, my friend..."
    gen "I don't know what to say, Severus..." ("base", xpos="far_left", ypos="head")
    sna "Then don't say anything..." ("snape_06")
    sna "Just move on to your next adventure..."
    sna "Our world has stalled you long enough..."
    gen "Thank you for keeping me company and being my only friend here, Severus." ("base", xpos="far_left", ypos="head")
    sna "Thank you for being mine..." ("snape_27")
    sna "I'd better go now..." ("snape_06")

    # Goes to the door, stops and turns around.
    call blkfade

    hide snape_main
    hide screen genie_snape_shake_hands
    call gen_chibi("sit_behind_desk")
    call sna_chibi("stand","desk","base")
    hide screen bld1
    call hide_blkfade
    pause.5

    call sna_walk("door", "base")
    pause.5

    call sna_chibi("stand","door","base", flip=False)
    pause.5

    sna "One more thing though..." ("snape_01", ypos="head")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    sna "If it all goes well..." ("snape_24")
    sna "Will I find the real Albus Dumbledore in that chair tomorrow?"
    gen "I believe so..." ("base", xpos="far_left", ypos="head")
    sna "*Hmm*..." ("snape_04")
    sna "Albus can't know that I was aware of his absence..." ("snape_03")
    sna "Is there a way to tell you guys apart?" ("snape_01")
    gen ".............." ("base", xpos="far_left", ypos="head")
    gen "How about a secret password?" ("base", xpos="far_left", ypos="head")
    sna "A password?" ("snape_05")
    gen "Yes... just ask me tomorrow: \"Who rules\"?" ("base", xpos="far_left", ypos="head")
    sna "\"Who rules\"?" ("snape_01")
    gen "\"Robin Williams\"!" ("grin", xpos="far_left", ypos="head")
    sna "Robin Wil--... *Err*...{w=0.3} I'm sorry, who?" ("snape_05")
    gen "You didn't see the \"Flubber\"? Great movie. Just came out." ("base", xpos="far_left", ypos="head")
    sna "Can't say that I have..." ("snape_02")
    sna "Alright then..." ("snape_06")
    sna "Have a safe trip home..."
    gen "Thank you. Have fun hosting the ball..." ("base", xpos="far_left", ypos="head")
    sna "*Sigh*" ("snape_06")

    call hide_characters

    pause.3

    stop music fadeout 1.0

    call sna_chibi("stand","door","base", flip=True)
    with d3
    pause.3

    call sna_chibi("leave")
    with d3
    pause.8

    gen "............................" ("base", xpos="far_left", ypos="head")
    gen "So this is it then..." ("base", xpos="far_left", ypos="head")

    play music "music/Despair_by_erenik.ogg" fadein 1 if_changed
    gen "Seems like my time in this world has come to an end..." ("base", xpos="far_left", ypos="head")
    gen "......................." ("base", xpos="far_left", ypos="head")

    if not "public" in states.her.ev.yule_ball.variant:
        # Personal whore ending
        # Writing a letter
        gen "That Means I'll probably never see the girl again..." ("base", xpos="far_left", ypos="head")
        gen "..........." ("base", xpos="far_left", ypos="head")
        gen "When I first met her she was so annoying..." ("base", xpos="far_left", ypos="head")
        gen "to be honest, all the training I put her through changed very little in that regard..." ("base", xpos="far_left", ypos="head")
        gen "But we did have a few special moments together..." ("base", xpos="far_left", ypos="head")
        gen ".............." ("base", xpos="far_left", ypos="head")
        gen "......................" ("base", xpos="far_left", ypos="head")
        gen "It doesn't feel right to leave her without saying goodbye properly..." ("base", xpos="far_left", ypos="head")
        gen "And yet I don't want to miss my chance to sneak out unnoticed..." ("base", xpos="far_left", ypos="head")
        gen "I don't like long goodbyes..." ("base", xpos="far_left", ypos="head")
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        gen "I suppose I could leave her a note or something..." ("base", xpos="far_left", ypos="head")

        gen "Let's see..." ("base", xpos="far_left", ypos="head")

        call gen_chibi("paperwork")
        with d3
        gen "\"Dear\"..." ("base", xpos="far_left", ypos="head")
        call gen_chibi("paperwork_idle")
        with d3
        gen "*Hmm*... How should I address her?" ("base", xpos="far_left", ypos="head")

        menu:
            gen "Dear..." ("base", xpos="far_left", ypos="head")
            "\"Miss Granger\"":
                $ word_01 = "Hermione Granger"
            "\"Nasty whore\"":
                $ word_01 = "Nasty whore"
            "\"Slut\"":
                $ word_01 = "Slut"
            "\"Cumbucket\"":
                $ word_01 = "Cumbucket"
            "\"Human female\"":
                $ word_01 = "Human female"
            "\"friend\"":
                $ word_01 = "Friend"

        call gen_chibi("paperwork")
        with d3
        gen "Yes, \"Dear [word_01]\" fits perfectly..." ("base", xpos="far_left", ypos="head")
        "*Scribble-scribble-scribble*"
        "*Scribble-scribble-scribble*"
        gen "...{w=0.4} \"It is time for me to go back\"..." ("base", xpos="far_left", ypos="head")
        call gen_chibi("paperwork_idle")
        with d3
        gen "What should I write now?" ("base", xpos="far_left", ypos="head")

        menu:
            gen "... time to go back..." ("base", xpos="far_left", ypos="head")
            "\"home\"":
                $ word_02 = "home"
            "\"to the mother-ship\"":
                $ word_02 = "to the mother-ship"
            "\"to Dimension \"X\"":
                $ word_02 = "to Dimension \"X\""
            "\"to my world\"":
                $ word_02 = "to my world"
            "\"To my Home Planet - Krypton\"":
                $ word_02 = "to my Home Planet - Krypton"

        call gen_chibi("paperwork")
        with d3
        gen "Yes, \"Time to go back [word_02]\" that will do..." ("base", xpos="far_left", ypos="head")
        "*Scribble-scribble-scribble*"
        "*Scribble-scribble-scribble*"
        gen "...{w=0.4} \"farewell my little\"..." ("base", xpos="far_left", ypos="head")
        call gen_chibi("paperwork_idle")
        with d3
        gen "What should I write now?" ("base", xpos="far_left", ypos="head")

        menu:
            gen "... farewell my little..." ("base", xpos="far_left", ypos="head")
            "\"cock-hungry slut\"":
                $ word_03 = "cock-hungry slut"
            "\"cum receptacle\"":
                $ word_03 = "cum receptacle"
            "\"Girl\"":
                $ word_03 = "girl"
            "\"Witch\"":
                $ word_03 = "witch"

        call gen_chibi("paperwork")
        with d3
        gen "Yes, \"farewell my little [word_03]\" sounds about right..." ("base", xpos="far_left", ypos="head")
        "*Scribble-scribble-scribble*"
        "*Scribble-scribble-scribble*"
        call gen_chibi("paperwork_idle")
        with d3
        gen "And now to sign it as..." ("base", xpos="far_left", ypos="head")

        label stupid_kent:
            pass

        menu:
            gen "..." ("base", xpos="far_left", ypos="head")

            "\"Genie\"":
                $ word_04 = "Genie"

            "\"Clark Kent\"":
                $ word_04 = "Clark Kent"
                call gen_chibi("paperwork")
                with d3
                gen "Yes, \"sincerely yours, [word_04]\"..." ("base", xpos="far_left", ypos="head")
                call gen_chibi("paperwork_idle")
                with d3
                gen "..........." ("base", xpos="far_left", ypos="head")
                gen "No, that doesn't make any sense..." ("base", xpos="far_left", ypos="head")
                jump stupid_kent

            "\"Lord Voldemort\"":
                $ word_04 = "Lord Voldemort"

            "\"Traveller\"":
                $ word_04 = "Traveller"

            "\"[name_genie_hermione]\"":
                $ word_04 = name_genie_hermione

        call gen_chibi("paperwork")
        with d3
        gen "Yes, \"[word_04]\"..." ("base", xpos="far_left", ypos="head")
        call gen_chibi("sit_behind_desk")
        with d3
        gen "........................" ("base", xpos="far_left", ypos="head")
        gen "Yes, this should do..." ("base", xpos="far_left", ypos="head")

    gen "Well, off I go then..." ("base", xpos="far_left", ypos="head")

    call blkfade

    call gen_chibi("stand","desk","base")
    hide screen bld1
    call hide_blkfade

    call gen_walk("door", "base")
    pause.5

    gen "...................." ("base", xpos="far_left", ypos="head")
    gen "Agrabah... here I come..." ("base", xpos="far_left", ypos="head")
    pause .5

    call gen_chibi("leave")
    pause 1
    call blkfade

    stop music fadeout 1.0
    stop background
    stop weather

    # Outskirts of Hogwarts
    centered "{size=+7}{color=#cbcbcb}Outskirts of Hogwarts{/color}{/size}"

    play background "sounds/night.ogg" fadein 1

    show her_ball outskirts as cg zorder 15

    pause.3
    call hide_blkfade
    call ctc

    pause.5
    play sound "sounds/steps_grass.ogg"

    show her_ball outskirts g1 as cg

    gen "Severus was right..." ("base", xpos="far_left", ypos="head")
    gen "The farther away I get from the school grounds..." ("base", xpos="far_left", ypos="head")
    gen "The more powerful I'm starting to feel..." ("base", xpos="far_left", ypos="head")

    show her_ball outskirts g1 m1 as cg
    pause.5

    gen "I think  this is far enough..." ("base", xpos="far_left", ypos="head")
    gen "Time to undo the spell and go back home..." ("base", xpos="far_left", ypos="head")
    gen ".........." ("base", xpos="far_left", ypos="head")
    gen "...................." ("base", xpos="far_left", ypos="head")
    gen "Agrabah, here I come..." ("base", xpos="far_left", ypos="head")

    if not persistent.game_complete:
        # First play-through
        # Fake early ending
        call ctc

        show screen blkfade
        with d9
        pause .5

        play music "music/Plaint.ogg" fadein 1 fadeout 1 #SAD CREDITS MUSIC. if_changed

        centered """{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}This is ending \"00\" out of \"02\".{/color}{/size}{#LINT_IGNORE}"""

        centered "{size=+7}{color=#cbcbcb}Thank you for playing!{/color}{/size}\n\n{#LINT_IGNORE}"

        play sound "sounds/scratch.ogg"
        stop music
        with hpunch
        gen "Wait, I'm still here!" ("angry", xpos="far_left", ypos="head")

        centered "{size=+7}{color=#cbcbcb}WHAT?!{/color}{/size}"

        gen "I said I am still here, dammit!" ("angry", xpos="far_left", ypos="head")

        centered "{size=+7}{color=#cbcbcb}Oh... :({/color}{/size}{#LINT_IGNORE}"

        show her_ball outskirts -m1 as cg
        hide screen blkfade
        with d9

    gen "....................." ("base", xpos="far_left", ypos="head")

    gen "No, I can't just leave like this!" ("base", xpos="far_left", ypos="head")
    gen "I must see the girl one last time..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/steps_grass.ogg"
    call ctc

    hide cg
    call blkfade
    stop background fadeout 1.0

    if not persistent.game_complete:
        # First play-through
        centered "{size=+7}{color=#cbcbcb}Fine whatever...{/color}{/size}"

    jump ball_ending_E2

label ball_ending_E2:
    # Main part of the ball event
    # Event replay starts here

    call blkfade
    play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    centered "{size=+7}{color=#cbcbcb}The Annual Hogwarts Autumn Ball{/color}{/size}"

    # Scene Setup
    $ game.daytime = True

    hide screen bld1
    hide screen blktone
    call her_chibi("hide")

    show her_ball entrance wall as cg zorder 15

    #Setting up Hermione's outfit.
    $ hermione.equip(her_outfit_ball)

    hide hermione_main
    hide screen room # MAIN BG (DAY).

    hide screen notes
    with fade
    pause.1

    hide screen bld1
    hide screen blktone
    call hide_blkfade
    call ctc


    gen "I better make sure to avoid being noticed..." ("base", xpos="far_left", ypos="head")
    gen "......................" ("base", xpos="far_left", ypos="head")
    gen "That's a whole lot of people out there..." ("base", xpos="far_left", ypos="head")
    gen "How big is this school?!" ("base", xpos="far_left", ypos="head")
    gen ".................." ("base", xpos="far_left", ypos="head")
    gen ".................................." ("base", xpos="far_left", ypos="head")
    gen "I don't see the girl anywhere..." ("base", xpos="far_left", ypos="head")
    gen ".............." ("base", xpos="far_left", ypos="head")
    gen "......................" ("base", xpos="far_left", ypos="head")
    gen "She has got to be here somewhere..." ("base", xpos="far_left", ypos="head")
    gen "................" ("base", xpos="far_left", ypos="head")
    gen "................................." ("base", xpos="far_left", ypos="head")

    call blktone_top

    if "public" in states.her.ev.yule_ball.variant:
        # Public whore ending
        # Students talking
        mal "Have you heard that rumour about Hermione Granger?"
        mal2 "That she is a major slut?"
        mal "*huh*? No, that's not a rumour, that's a fact."
        mal "The rumour was that she is being paid in house points to whore herself out."
        mal2 "*Hmm*... I don't believe that. I think she is just a slut."
        fem "Who's a slut?"
        mal "Oh, hey you..."
        fem "So, who's a slut?"
        mal2 "Hermione Granger..."
        fem "*Tsk*! You, guys are talking about that whore again?"
        fem "That girl jerks off a couple of dicks, gives a few blowjobs and suddenly she is the school's new sensation."
        fem "Pathetic little muggle-born..."
        mal "You should not be jealous of--"
        fem "Jealous? Of her? Puh-lease!"
        fem "I have no use for popularity that comes from putting cocks in my mouth!"
        mal "Well, if you ever change your mind..."
        fem "*Huh*?"
        mal "Feel free to use me as a stepping stone on your road to fame!"
        fem "You wish!"
        mal2 "Hey, guys, I think that's Hermione over there!"
        mal "You're right!"
        mal2 "Do you think if I ask her to the dance, I might get lucky later?"
        mal "Not if I ask her first!"
        play sound "sounds/run_04.ogg"
        pause 2
        mal2 "Hey, wait up! That was my idea!"
        play sound "sounds/run_03.ogg"
        pause 2
        fem "Guys...?"
        fem "........................."
        fem "*Tsk*... Men......"

    else:
        # Personal whore ending
        # Students talking
        mal "{size=-4}Have you heard the rumours?{/size}"
        mal2 "{size=-4}Yeah, they say Hermione took one for the team.{/size}"
        fem "{size=-4}Whoring herself out for house points!{/size}"
        fem "{size=-4}How disgraceful!{/size}"
        mal "{size=-4}Those are just rumours!{/size}"
        fem "{size=-4}I think it's more than just that...{/size}"
        mal "{size=-4}Oh, shut up! You are just jealous.{/size}"
        mal2 "{size=-4}Yeah, you wish you had Hermione's courage!{/size}"
        mal "{size=-4}Exactly! No one is more loyal to Gryffindor than she is!{/size}"
        mal "{size=-4}Even if the rumours are true, what does it matter?{/size}"
        mal "{size=-4}Thanks to her sacrifice, our house will be getting the cup this year!{/size}"
        mal2 "{size=-4}Yeah, and what did you ever do for our house?{/size}"
        fem "{size=-4}I..... But....{/size}"
        mal "{size=-4}Exactly! So don't you bad-mouth Hermione!{/size}"
        mal2 "{size=-4}You said it, man.{/size}"
        fem "{size=-4}*Pouting*{/size}"

    hide screen bld1
    call hide_blktone_top
    call ctc

    show her_ball entrance hall crowd as cg zorder 15
    pause 1.0
    gen "(*Hmm*... I don't see her...)" ("base", xpos="far_left", ypos="head")
    pause 1.0
    show her_ball entrance h1 as cg
    pause 0.5
    gen "(There she is!)" ("grin", xpos="far_left", ypos="head")

    mal "Hermione, hey..."
    her "Oh, hello." ("base", "base", "base", "mid", ypos="head", flip=False)
    mal "You look... so beautiful tonight, Hermione."
    her "Thank you, you are too sweet." ("base", "closed", "base", "mid")
    mal2 "Can I have the next dance?"
    mal "What? Back off, buddy! I was here first!"
    mal2 "Like hell you were!"
    mal "Alright, pal! That does it!"
    mal2 "I'm not your \"pal\", buddy!"
    her ".............." ("open", "wide", "worried", "stare")

    call blktone_top
    stop music fadeout 3.0
    gen "(Here is my chance!)" ("base", xpos="far_left", ypos="head")
    gen "Psst! Girl!" ("base", xpos="far_left", ypos="head")
    her "???" ("upset", "base", "base", "mid")
    gen "Girl, it's me! Over here!" ("base", xpos="far_left", ypos="head")
    her "[name_genie_hermione]?" ("open", "base", "base", "mid")
    gen "Shush! Keep your voice down and follow me." ("base", xpos="far_left", ypos="head")
    her "Oh?" ("open", "base", "base", "mid")

    show her_ball wall -h1 as cg
    call hide_blktone_top
    call ctc

    her "Sir, what is going on? Why are you... lurking in the shadows?" ("upset", "base", "base", "mid")
    gen "Just be quiet and listen for a second! Can you do that for me?" ("base", xpos="far_left", ypos="head")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.
    her "Yes, sir..." ("upset", "base", "base", "mid")
    gen "Well, here is the thing..." ("base", xpos="far_left", ypos="head")
    gen "There is something you need to kn--" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Of course sir!" ("grin", "happy", "base", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Let's just make this quick, alright?" ("soft", "narrow", "base", "R_soft")
    gen "Let's make what quick?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "You want me to thank you for the dress, don't you, sir?" ("base", "narrow", "base", "mid_soft")
    gen "The dress? No, no... That's not why I am here." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "It is fine, sir. I do not mind." ("soft", "narrow", "base", "R_soft")
    gen "Listen to me, girl! I am not who you think--" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Please, sir, let me suck on your cock a little." ("open_tongue", "narrow", "worried", "mid_soft")
    gen "*Gh*--!!!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "Just a little will do. Please? I'm begging you..." ("open_tongue", "narrow", "worried", "mid_soft")
    gen "Damn you, you damn witch!" ("angry", xpos="far_left", ypos="head")
    gen "Stop this! I really need to talk to you!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "Well of course, sir." ("base", "narrow", "base", "mid_soft")
    her @ cheeks blush "Put your dick in my mouth and talk to me." ("open_tongue", "narrow", "worried", "mid_soft")
    her "Talk dirty to me..."
    gen "*Growl*!" ("angry", xpos="far_left", ypos="head")
    gen "*Sigh*...." ("base", xpos="far_left", ypos="head")
    gen "Fine, have it your way..." ("base", xpos="far_left", ypos="head")
    gen "But you are abusing your power, girl!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "*Giggle*!" ("crooked_smile", "happyCl", "worried", "mid")
    gen "And after we're done, we'll have that talk!" ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d7

    her "*Slurp*! *Slurp*! *Slurp*!"
    gen "................." ("base", xpos="far_left", ypos="head")

    hide screen bld1
    hide screen blkfade
    show her_ball blowjob h1 mouth_none blush_none eyes_none sweat_s1 as cg
    call ctc

    her "*Slurp*! *Gulp*! *Slurp*!"
    her "*Slurp*--"
    show her_ball blowjob h2 mouth_none blush_none eyes_none sweat_s2 as cg
    her "*huh*.........."
    her "...................."
    show her_ball blowjob h1 mouth_none blush_none eyes_none sweat_s1 as cg
    her "*Slurp*! *Gulp*! *Slurp*!"
    gen "Yes... Like that.... oh... yes..." ("base", xpos="far_left", ypos="head")
    her "*Gulp*! *Slurp*! *Slurp*!"
    her "*Gulp*--"
    show her_ball blowjob h2 mouth_none blush_none eyes_none sweat_s2 as cg
    her "...................." #LOOKING BACK
    gen "Just keep going, girl." ("base", xpos="far_left", ypos="head")
    gen "I will let you know if I see someone coming..." ("base", xpos="far_left", ypos="head")
    show her_ball blowjob h2 mouth_open2 blush_none eyes_up2 sweat_s2 as cg
    her "Oh... I'm not worried about that, sir..."
    gen "*Hmm*?" ("base", xpos="far_left", ypos="head")
    her "They are supposed to make the announcement soon..."
    show her_ball blowjob h1 sweat_s1 mouth_none eyes_none as cg
    her "*Slurp*! *Gulp*! *Slurp*!"
    gen "The announcement?" ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Slurp*! *Slurp*!"
    her "*Slurp*--"
    show her_ball blowjob h2 sweat_s2 mouth_open2 eyes_up2 as cg
    her "Yes. About the coronation..."
    show her_ball blowjob h1 sweat_s1 mouth_none eyes_none as cg
    her "*Gulp*! *Slurp*! *Gulp*!"
    gen "What...?" ("base", xpos="far_left", ypos="head")
    her "*Slurp*--"
    show her_ball blowjob h2 sweat_s2 mouth_open2 eyes_closed2 as cg
    her "The Hogwarts autumn ball queen coronation, sir."
    gen "Oh... Is that a thing?" ("base", xpos="far_left", ypos="head")
    gen "Any chance you might be chosen?" ("base", xpos="far_left", ypos="head")
    her "A chance?"
    her "It's already been decided, sir."
    gen "What?" ("base", xpos="far_left", ypos="head")
    her "Oh, I mean... I hope I will win..."
    her "But since I am the one who organised the whole thing, it is only fair..."
    her "Wouldn't you agree, sir?"
    gen "Well... Sounds like cheat--" ("base", xpos="far_left", ypos="head")
    show her_ball blowjob h1 sweat_s1 mouth_none eyes_up1 as cg
    her "*Slurp*! *Slurp*! *Slurp*!"
    show her_ball blowjob h2 sweat_s2 mouth_smile2 eyes_up2 as cg
    her "Wouldn't you agree, sir?"
    gen "*Err*..." ("base", xpos="far_left", ypos="head")
    her "Wouldn't you?"
    with hpunch
    show her_ball blowjob h3 sweat_none eyes_none mouth_none blush_b3 as cg
    her "{size=+7}*gobble*!{/size}" #DEEPTHROATING
    gen "{size=+7}Oh, yes!!!{/size}" ("angry", xpos="far_left", ypos="head")
    her "*Gobble-gobble-gobble*!"
    her "*Gobble*"
    show her_ball blowjob h2 sweat_s2 eyes_up2 mouth_smile2 blush_none as cg
    her "Good. I knew you would approve."
    show her_ball blowjob h1 sweat_s1 eyes_up1 mouth_none as cg
    show her_ball blowjob h1 mouth_none blush_none eyes_up1 sweat_s1 as cg
    her "*Slurp*! *Slurp*! *Gulp*!"
    gen "Oh... This is amazing..." ("base", xpos="far_left", ypos="head")
    her "*Slurp*! *Slurp*! *Gulp*!"

    sna "*Ahem*!"
    sna "Attention, maggots!"
    gen "(Snape?)" ("base", xpos="far_left", ypos="head")
    sna "Quiet down, everyone!"
    sna "It is time to announce who will be this year's queen of the annual Hogwarts autumn ball."

    her "*Slurp*--"
    show her_ball blowjob h2 mouth_none blush_none eyes_none sweat_s2 as cg
    her "Oh no! I think they are about to start..."
    show her_ball blowjob h2 mouth_open2 blush_none eyes_up2 sweat_s2 as cg
    her "But I can't just leave you in this...{w=0.5} condition, sir."

    show her_ball blowjob h2 mouth_none blush_none eyes_down2 sweat_s2 as cg
    her "What should I do?"
    gen "Just go, girl. We can finish this up later." ("base", xpos="far_left", ypos="head")
    show her_ball blowjob h2 mouth_open2 blush_none eyes_up2 sweat_s2 as cg
    her "But... But you got me this dress, sir, and..."
    her ".........."
    show her_ball blowjob h2 mouth_open2 blush_none eyes_closed2 sweat_s2 as cg
    her "No, I can't just leave you like this, sir."
    show her_ball blowjob h2 mouth_smile2 blush_none eyes_closed2 sweat_s2 as cg
    gen "Fine! Finish the job then." ("base", xpos="far_left", ypos="head")
    gen "If you put some effort into this we'll be done in no time." ("base", xpos="far_left", ypos="head")
    gen "I believe in you, girl." ("base", xpos="far_left", ypos="head")
    show her_ball blowjob h2 mouth_none blush_none eyes_closed2 sweat_s2 as cg
    her "*Hmm*..."
    show her_ball blowjob h2 mouth_open2 blush_none eyes_up2 sweat_s2 as cg
    her "Then you must promise me something, sir."
    gen "Yes, what is it?" ("base", xpos="far_left", ypos="head")
    show her_ball blowjob h2 mouth_happy2 blush_none eyes_up2 sweat_s2 as cg
    her "Please, do not restrain yourself."
    gen "*Heh*... I rarely do, girl." ("grin", xpos="far_left", ypos="head")

    show her_ball blowjob h2 mouth_none blush_none eyes_none sweat_s2 as cg
    sna "This year's Hogwarts Autumn Ball queen is..."
    sna "Let's see... Can't open the damn envelope..."
    show her_ball blowjob h2 mouth_none blush_none eyes_closed2 sweat_s2 as cg
    her "Alright, sounds like we have no time to lose."

    if "public" in states.her.ev.yule_ball.variant:
        # Public whore ending
        show her_ball blowjob h1 mouth_none blush_none eyes_none sweat_s1 as cg
        her "*Slurp*! *Gulp*! *Slurp*!"
        gen "Yes! That's the spirit!" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sweat_s1 sperm_s1 lashes_l1 as cg
        her "*Gulp*! *Slurp*! *Gulp*!"
        her "*Slurp*--"
        show her_ball blowjob h2 sweat_s2 sperm_none lashes_none mouth_open2 eyes_up2 blush_b2 as cg
        her "Sir, is this really the proper way to treat one of your students?"
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sweat_s1 sperm_s1 lashes_l1 mouth_none eyes_none blush_none as cg
        her "*Slurp*! *Gulp*! *Gulp*!"
        her "*Slurp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_none eyes_closed2 blush_b2 sweat_s2 as cg
        her "I am like a fragile and impressionable little dove..."
        her "Entrusted to your care by my parents..."
        show her_ball blowjob h2 sperm_none lashes_none mouth_grimmace2 eyes_up2 brows_b2 blush_b2 sweat_s2 as cg
        her "You were supposed to treat me {i}right{/i}, sir..."
        her "And what did you do instead?"
        gen "*Ahem*! Let me repeat my previous statement..." ("base", xpos="far_left", ypos="head")
        gen "{size=+7}\"*Huh*?\"{/size}" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h2 sperm_none lashes_none mouth_happy2 eyes_down2 brows_b2 blush_b2 sweat_s2 as cg
        her "You put your penis in my innocent mouth, sir!"
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_closed1 brows_none blush_b1 sweat_s1 as cg
        her "*Slurp*! *Slurp*! *Slurp*!"
        gen "Oh, I see! Yes, I like this innocent girl act!" ("grin", xpos="far_left", ypos="head")
        her "*Slurp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_open2 eyes_up2 brows_none blush_b2 sweat_s2 as cg
        her "You pretended to be kind to me..."
        her "You bought me this dress..."
        show her_ball blowjob h2 sperm_none lashes_none mouth_none eyes_closed2 brows_none blush_b2 sweat_s2 as cg
        her "And then........."
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_up1 brows_none blush_none sweat_s1 as cg
        her "*Slurp*! *Gulp*! *Gulp*!"
        her "*Slurp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_none eyes_closed2 brows_none blush_b2 sweat_s2 as cg
        her "You took advantage of me, sir!"
        her "Tricked me into sucking your big cock!"
        gen "Oh... Yes! You're good!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h2 sperm_none lashes_l2 mouth_grimmace2 eyes_none brows_none blush_b2 sweat_none as cg
        her "I'm supposed to be enjoying the ball with my classmates right now..."
        show her_ball blowjob h2 sperm_none lashes_none mouth_grimmace2 eyes_none brows_b2 blush_b2 sweat_none as cg
        her "But what am I doing instead?"
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_up1 brows_none blush_none sweat_none as cg
        her "*Slurp*! *Slurp*! *Slurp*!"
        gen "Oh..." ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_closed1 brows_b1 blush_b1 sweat_none as cg
        her "*Slurp*! *Gulp*! *Slurp*! *Slurp*! *Slurp*!"
        her "*Slurp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_open2 eyes_closed2 brows_b2 blush_b2 sweat_none as cg
        her "I'm on my knees, sucking off my headmaster!"
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_closed1 brows_b1 blush_b1 sweat_none as cg
        her "*Slurp*! *Slurp*! *Gulp*!"
        gen "Oh, yes you are, you little slut!" ("base", xpos="far_left", ypos="head")
        her "*Slurp*! *Slurp*! *Slurp*!"
        her "*Slurp*! *Slurp*! *Gulp*!"
        gen "You are really good at this dirty talk stuff..." ("angry", xpos="far_left", ypos="head")
        gen "You should try writing a fairy tale, or something..." ("grin", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_up1 brows_none blush_b1 sweat_none as cg
        her "*Slurp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_open2 eyes_up2 brows_none blush_b2 sweat_none as cg
        her "Oh, but I wouldn't know how, sir..."
        show her_ball blowjob h2 sperm_none lashes_none mouth_none eyes_closed2 brows_none blush_b2 sweat_none as cg
        gen "You nasty little thing!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_closed1 brows_b1 blush_b1 sweat_none as cg
        her "*Slurp*! *Slurp*! *Gulp*! *Slurp*! *Slurp*!"

        sna "Miss Granger?"
        sna "{size=-4}(Where is that girl?){/size}"
        nar "A murmur starts running through the crowd of students."

        her "*Slurp*! *Slurp*! *Gulp*!"
        her "*Gulp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_open2 eyes_up2 brows_none blush_b2 sweat_none as cg
        her "Sir, am I being an obedient little slut?"
        gen "Yes you are, girl!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h2 sperm_none lashes_none mouth_grimmace2 eyes_none brows_b2 blush_b2 sweat_none as cg
        her "Would you say that I am a good student?"
        gen "I would say that you are an excellent student, girl!" ("grin", xpos="far_left", ypos="head")
        show her_ball blowjob h2 sperm_none lashes_none mouth_none eyes_closed2 brows_none blush_b2 sweat_none as cg
        her "Good..."
        show her_ball blowjob h2 sperm_none lashes_none mouth_smile2 eyes_down2 brows_b2 blush_b2 sweat_none as cg
        her "I'm making my mum and dad proud!"
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_closed1 brows_none blush_b1 sweat_none as cg
        her "*Slurp*! *Slurp*! *Gulp*!"
        gen "Oh, girl, you are killing me!" ("angry", xpos="far_left", ypos="head")
        her "*Slurp-slurp-slurp-slurp*!!!"
        gen "Oh, yes! Like that!" ("angry", xpos="far_left", ypos="head")
        her "*Slurp*--"
        show her_ball blowjob h2 sperm_none lashes_none mouth_grimmace2 eyes_none brows_b2 blush_b2 sweat_none as cg
        her "Do I deserve a reward, sir?"
        show her_ball blowjob h2 sperm_none lashes_none mouth_happy2 eyes_up2 brows_none blush_b2 sweat_none as cg
        her "I would like you to reward me with your cum, please."
        gen "*Grh*!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_closed1 brows_b1 blush_b1 sweat_none as cg
        her "*Slurp*! *Slurp*! *Slurp*!"
        gen "*Geh*! Almost...!" ("angry", xpos="far_left", ypos="head")
        her "{size=+5}*Slurp-gulp-slurp-slurp*!!!{/size}"
        gen "{size=+5}Here it com--{/size}" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h1 sperm_none lashes_none mouth_none eyes_down1 brows_b1 blush_b1 sweat_none as cg
        her "*Slurp*.........................."
        her "!!!"
        call ctc

        call blkfade
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_none eyes_none brows_b4 blush_b4 sweat_none as cg
        gen "{size=+5}What the...!? Why did you stop?!{/size}" ("angry", xpos="far_left", ypos="head")
        gen "{size=+5}What the hell are you doing--{/size}" ("angry", xpos="far_left", ypos="head")
        call hide_blkfade
        call ctc

        her "{size=+5}Cum for me, sir! Cum for me!{/size}"
        with hpunch
        gen "{size=+5}What the hell is this?!{/size}" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_smile4 eyes_up4 brows_b4 blush_b4 sweat_none as cg
        her "{size=+5}Cum for me, sir! I want your hot cum on me!{/size}"
        gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_none eyes_up4 brows_b4 blush_b4 sweat_none as cg
        her "{size=+5}Yes I am!{/size}"
        her "{size=+5}Nothing but a cum hungry whore, sir!{/size}"
        with hpunch
        gen "{size=+7}*Argh*!!!{/size}" ("angry", xpos="far_left", ypos="head")
        gen "{size=+7}Take this, then!!!{/size}" ("angry", xpos="far_left", ypos="head")

        show screen white
        pause .1
        hide screen white
        with hpunch

        gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_none eyes_up4 brows_none blush_b4 sweat_none as cg
        her "{size=+5}*Ah*! Yes, sir! Yes! cum for me!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch

        gen "{size=+7}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
        gen "{size=+7}*Argh*!!! YES!!!{/size}" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_none eyes_none brows_none blush_b4 sweat_none as cg
        her "*Ah*... yes... *Ah*..."
        gen "Oh... *ght*... *panting*" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_none eyes_up4 brows_none blush_b4 sweat_none as cg
        her "Thank you sir..."
        show her_ball blowjob h4 sperm_none lashes_l4 mouth_smile4 eyes_none brows_none blush_b4 sweat_none as cg
        her "..........................................."
        call ctc

        call blkfade
        pause.5

        gen "What on earth just happened, girl?!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "What do you mean, sir?" ("soft", "narrow", "base", "R_soft", ypos="head", flip=False)
        hide cg
        call hide_blkfade

        gen "Do I really need to point this out to you?" ("base", xpos="far_left", ypos="head")
        gen "{size=+5}Do I really?{/size}" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "Oh... You mean the hair thing...?" ("soft", "narrow", "base", "R_soft")
        gen "Yes... \"the hair thing\"..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well, what did you expect me to do, sir?" ("crooked_smile", "happyCl", "worried", "mid")
        gen "Literally anything..." ("base", xpos="far_left", ypos="head")
        gen "... but {size=+7}THAT!{/size}" ("angry", xpos="far_left", ypos="head")
        her "But... I need to look my best for the coronation..." ("open", "base", "base", "mid")
        gen "And a hairdo full of cum is supposed to ensure that?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Well... yes..." ("soft", "narrow", "base", "R_soft")
        her "You see, cum is a great hair fixative and--" ("open", "base", "base", "mid")

        stop music fadeout 1.0
        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"
        sna "{size=-4}Not that I care...{/size}"

        her "The coronation! I must go now!" ("open", "wide", "worried", "stare")
        play sound "sounds/run_03.ogg"
        pause 3

        gen ".............................." ("base", xpos="far_left", ypos="head")
        gen "................" ("base", xpos="far_left", ypos="head")
        gen "..." ("base", xpos="far_left", ypos="head")
        with hpunch
        gen "{size=+9}WHAT THE HELL...?!!{/size}" ("angry", xpos="far_left", ypos="head")
        call ctc

        call blkfade

    else:
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_none brows_none blush_b3 sweat_none as cg
        with hpunch
        her "{size=+5}*GOBBLE*!{/size}"
        gen "{size=+5}Yeeeeeeeeeees!{/size}" ("angry", xpos="far_left", ypos="head")

        sna "There! *Hmm*...?"
        sna "(Well of course... Why am I not surprised?)"
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_none blush_b3 sweat_none as cg
        sna "Miss Hermione Granger of the Gryffindor house..."
        nar "Loud applause and cheering erupts from the crowd."
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_none brows_none blush_b3 sweat_none as cg
        sna "Miss Granger, if you would be so kind to grace us with your presence..."

        her "*Gobble-gobble-gobble*!"
        gen "Yes! That's a good slut!" ("base", xpos="far_left", ypos="head")
        her "{size=+5}*gobble-gobble-gobble*!!!{/size}"
        gen "Yes. Now, move your tongue..." ("base", xpos="far_left", ypos="head")
        gen "Lick my balls, girl. Come on!" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_closed3 brows_none blush_b3 sweat_none as cg
        her "*Gobble*! *Lick*! *Lick*! *Gobble*!"
        gen "Yes... Like that." ("base", xpos="far_left", ypos="head")
        gen "What a good whore you are..." ("base", xpos="far_left", ypos="head")
        her "*Lick*! *Lick*! *Gobble*! *Lick*!"
        gen "Now look up at me, whore." ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_up3 brows_none blush_b3 sweat_none as cg
        her "???................"

        play sound "sounds/spit.ogg"
        show screen white
        pause.3
        hide screen white
        with vpunch
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_none blush_b3 sweat_none spit_base3 as cg
        call ctc

        her "*Gobble*??!"
        gen "No, don't you stop now!" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_angry3 blush_b3 sweat_none spit_base3 as cg
        her "*Gobble-gobble-gobble*!"
        gen "Yes, whore! Yes!" ("base", xpos="far_left", ypos="head")

        sna "Miss Granger?"
        sna "If you would, please..."
        sna "Miss Granger?"

        play sound "sounds/spit.ogg"
        show screen white
        pause.3
        hide screen white
        with vpunch
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_none blush_b3 sweat_none spit_forehead3 spit_base3 as cg
        call ctc

        her "!!!!!!!!!!!"
        her "......................................?"
        gen "What's the matter, my little spit bucket?" ("base", xpos="far_left", ypos="head")
        gen "Keep sucking my cock!" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_angry3 blush_b3 sweat_none spit_base3 spit_forehead3 tears_base3 as cg
        her "*Gobble-gobble-gobble*!"
        gen "Yes. Good whore." ("base", xpos="far_left", ypos="head")
        her "*Gobble-gobble-gobble*!"
        gen "Keep deep throating me like that, yes!" ("base", xpos="far_left", ypos="head")
        her "*Gobble*! *Gobble*! *Gobble*!"
        gen "The balls, girl! Don't forget to work your tongue!" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_none brows_none blush_b3 sweat_none spit_base3 spit_forehead3 tears_base3 as cg
        her "*Gobble*! *Lick*! *Lick*!"
        gen "Yes! Keep at it, and we will be done here in no time!" ("base", xpos="far_left", ypos="head")
        gen "Oh, I almost forgot..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/spit.ogg"
        pause.3
        with vpunch
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_angry3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        call ctc

        her "..........................."
        her ".................."
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_happycl3 brows_angry3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "*Gobble*! *Gobble*! *Lick*... *Gobble*!"
        gen "you just look so pretty with your face all covered in my spit!" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_none brows_angry3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "*Gobble*! *Gobble*! *Lick*... *Gobble*!"
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        her "*Gobble*! *Gobble*! *Lick*... *Gobble*!"
        gen "Maybe we should show your pretty face to everyone?" ("base", xpos="far_left", ypos="head")
        gen "Should I call some of your classmates over?" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_stare3 brows_angry3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "!!!!!!!!!!!!!!!"
        gen "Relax..." ("base", xpos="far_left", ypos="head")
        gen "I want to get caught as much as you do." ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_none brows_angry3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg

        sna "Miss Granger?"
        sna "{size=-4}Where is that girl?{/size}"
        nar "A murmur starts running through the crowd of students."

        gen "Alright, listen up, whore." ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3 sperm_none lashes_none mouth_none eyes_squintup3 brows_none blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "*Gobble*?"
        gen "I need you to stay still now." ("base", xpos="far_left", ypos="head")
        her "???"
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_up3 brows_none blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        gen "Yes, just like that." ("base", xpos="far_left", ypos="head")
        her "................"

        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_dead3 brows_none blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "....................................."
        gen "I plan to choke you a little bit with my cock..." ("base", xpos="far_left", ypos="head")
        gen "It'll be fun... just relax..." ("base", xpos="far_left", ypos="head")
        her "......................................"
        gen "Your throat is the best, girl." ("base", xpos="far_left", ypos="head")
        her "..........."
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_squintdead3 brows_none blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        gen "So warm and tight..." ("base", xpos="far_left", ypos="head")
        her "............................................."
        her "...................."
        her "......."
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_up3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        with hpunch
        her "!!!"
        gen "I know, I know, you can't really breathe..." ("base", xpos="far_left", ypos="head")
        gen "But that's what makes this so much fun!" ("grin", xpos="far_left", ypos="head")

        with hpunch
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        gen "Stop struggling, slut. You are not going anywhere!" ("base", xpos="far_left", ypos="head")
        with hpunch
        her "{size=+9}!!!!!!!!!!!!!!!!{/size}"

        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"

        gen "*Heh*..." ("grin", xpos="far_left", ypos="head")
        gen "Your queen is right here..." ("grin", xpos="far_left", ypos="head")
        gen "Choking on my engorged cock!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_happycl3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        gen "Oh. You are turning blue, love." ("base", xpos="far_left", ypos="head")
        gen "Will you be alright?" ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_none brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "{size=+9}!!!!!!!!!!!!!!!!........................{/size}"
        gen "Look up whore!" ("base", xpos="far_left", ypos="head")
        her "{size=+3}........................{/size}"
        gen "I said, look at me!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_up3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 tears_base3 as cg
        her "{size=+9}??!.....................{/size}"

        play sound "sounds/spit.ogg"
        pause.5

        with vpunch
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_up3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_on_eye3 tears_base3 as cg
        her "{size=+9}!!!!!!!!!!!!!!!!!!{/size}"

        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_closed3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 -spit_on_eye3 tears_base3 as cg
        her "...................................................................................."
        gen "There you go! You wear it well!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_closed3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 tears_crying3 as cg
        her "...........................................................*SOB!*"
        with hpunch
        gen "*Gght*!" ("angry", xpos="far_left", ypos="head")
        gen "Here it comes!" ("angry", xpos="far_left", ypos="head")
        gen "I know you are fighting for air down there..." ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_dead3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 tears_crying3 as cg
        gen "But all you will get from me is a load of hot cum!" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_stare3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 tears_crying3 as cg
        with hpunch
        her "{size=+9}*GHT*!!!!!!!!!!!!!!!!{/size}"
        with hpunch
        gen "{size=+9}*ARGH*!{/size}" ("angry", xpos="far_left", ypos="head")
        with hpunch
        show her_ball blowjob h3_alt sperm_s3 lashes_none mouth_none eyes_dead3 brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 tears_crying3 as cg
        her "{size=+9}*GULP-GULP-GULP-GULP-GULP*!!!{/size}"
        gen "{size=+5}Yes, whore! Drink my cum!{/size}" ("angry", xpos="far_left", ypos="head")
        her "*GULP-GULP-GULP-GULP*......"
        with hpunch
        gen "Not done yet!{w=0.3} Not... done... *Argh!*" ("angry", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_s3 lashes_none mouth_none eyes_none brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 tears_crying3 as cg
        her "{size=-4}*Gulp*! *Gulp*! *Gulp...*{/size}"
        gen "Oh, yes..." ("base", xpos="far_left", ypos="head")
        show her_ball blowjob h3_alt sperm_none lashes_none mouth_none eyes_none brows_b3 blush_b3 sweat_none spit_base3 spit_forehead3 spit_nose3 spit_eye3 tears_crying3 mascara_m3 as cg
        her "...................................................."
        gen "Well, I think that was the last of it--" ("base", xpos="far_left", ypos="head")
        with hpunch
        gen "{size=+5}*Huh*?!{/size}" ("angry", xpos="far_left", ypos="head")
        call blkfade

        stop music fadeout 1.0
        gen "Hey, what are you--" ("angry", xpos="far_left", ypos="head")
        nar "Hermione gets up abruptly and runs off without saying a word..."
        play sound "sounds/run_03.ogg"
        pause 3
        gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
        gen "Oh, that's right... The coronation thing..." ("base", xpos="far_left", ypos="head")
        gen "............." ("base", xpos="far_left", ypos="head")

    pause 1.5

    if "public" in states.her.ev.yule_ball.variant:

        # Public whore ending
        sna "Miss Granger...?" ("snape_03", ypos="head")
        sna "So you decided to show up after all." ("snape_04")
        sna "What an unpleasant surprise..." ("snape_03")

        her "Professor..." ("upset", "base", "base", "mid", ypos="head", flip=False)
        sna "Well, go ahead then..." ("snape_10")
        sna "Here is the tiara..."

        her "Professor..." ("upset", "base", "base", "mid")

        sna "And the stage is yours..."
        her "Thank you, professor." ("base", "closed", "base", "mid")
        pause.7

        hide screen blkfade
        show her_ball speech h1 as cg

        play sound "sounds/applause01.ogg"
        call ctc

        her "..............."
        her ".................................."
        show her_ball speech h1 mouth_open eyes_closed as cg

        play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
        her "Hello, everyone!"
        her "Thank you for making me your ball queen for two years in a row!"

        show screen blktone
        gen "!!!" ("base", xpos="far_left", ypos="head")
        gen "Her hairdo looks perfect!" ("base", xpos="far_left", ypos="head")
        gen "I suppose I was wrong and--" ("base", xpos="far_left", ypos="head")
        show her_ball speech h1 mouth_open eyes_closed sperm_cum0 as cg
        gen "Nope, there it is!" ("angry", xpos="far_left", ypos="head")
        gen "Dripping down behind her ear!" ("angry", xpos="far_left", ypos="head")
        hide screen blktone

        her "I would like to dedicate my speech to every girl in this room..."

        show screen blktone
        gen "What was she thinking pulling a stunt like that?" ("angry", xpos="far_left", ypos="head")
        hide screen blktone

        show her_ball speech h1 mouth_open eyes_squint sperm_cum1 as cg
        her "I shall not go as far as to say that I do not deserve this honour..."
        her "Because I think I do..."
        show her_ball speech h1 mouth_open eyes_none sperm_cum2 as cg
        her "But I am still very grateful to stand here before all of you tonight..."

        show screen blktone
        mal "{size=-4}*Huh*?{/size}"
        mal "{size=-4}What's that stuff on her forehead, you wager?{/size}"
        mal2 "{size=-4}Sweat...?{/size}"
        mal "{size=-4}*Hmm*... Probably...{/size}"
        hide screen blktone

        show her_ball speech h1 mouth_open eyes_squint sperm_cum3 as cg
        her "I would especially like to thank our esteemed teachers for their hard work."

        show screen blktone
        gen "Doesn't she feel it by now?!" ("angry", xpos="far_left", ypos="head")
        gen "She'd better cut her speech short!" ("angry", xpos="far_left", ypos="head")
        hide screen blktone

        her "Hogwarts truly did become a second home for all of us..."
        show her_ball speech h1 mouth_open eyes_squint sperm_cum4 as cg
        her "I know that I speak for every student in this building when I say this."
        show screen blktone

        mal "{size=-4}That doesn't look like sweat, though...{/size}"
        mal2 "{size=-4}Yeah...{/size}"
        mal2 "{size=-4}Some weird goo seeping out of her hair...{/size}"
        fem "{size=-4}Are you guys really {i}that{/i} dim?{/size}"
        mal "{size=-4}What?{/size}"
        fem "{size=-4}That's cum... obviously.{/size}"
        mal2 "{size=-4}What? Bullshit, girl!{/size}"
        fem "{size=-4}I think I know cum when I see it.{/size}"
        mal "{size=-4}I bet you do. *Chuckle*{/size}"
        fem "{size=-4}Whatever. Just take a better look...{/size}"
        fem "{size=-4}She must've let some guy bury his cock in her hair and pump it full of semen.{/size}"
        mal "{size=-4}*Hmm*... Hair fucking then? Is that a thing now?{/size}"
        mal2 "{size=-4}You girls do the craziest things.{/size}"
        fem "{size=-4}*Humph*! Not all of us are sluts, you know.{/size}"
        mal "{size=-4}Unfortunately not...{/size}"
        fem "{size=-4}\"Unfortunately\"?!{/size}"
        fem "{size=-4}*Tsk*! You men are so clueless about everything!{/size}"
        fem "{size=-4}You could never build a meaningful relationship with a slut!{/size}"
        mal "{size=-4}What's a \"meaningful relationship\"?{/size}"
        fem "{size=-4}It's when your girl is also your best friend.{/size}"
        mal "{size=-4}Oh, I don't need {i}that{/i}!{/size}"
        mal "{size=-4}I already have a best friend, this ugly bugger right here.{/size}"
        mal2 "{size=-4}Right back at you, mate!{/size}"
        mal "{size=-4}But I sure could use a slut in my life!{/size}"
        mal2 "{size=-4}What he said!{/size}"
        fem "{size=-4}you guys are...{/size}"
        fem "Such idiots!!!"
        hide screen blktone

        show her_ball speech h1 mouth_open eyes_closed sperm_cum4 as cg
        her "I remember when I was just a little girl..."

        show screen blktone
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        hide screen blktone

        her "Frightened of my power... confused..."

        show screen blktone
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        gen "There... She did it again..." ("base", xpos="far_left", ypos="head")
        hide screen blktone

        her "Who knows what would have become of me if not for Hogwarts!"

        show screen blktone
        gen "And again..." ("base", xpos="far_left", ypos="head")
        gen "Why does she keep on jerking her shoulder in that awkward manner...?" ("base", xpos="far_left", ypos="head")
        hide screen blktone

        her "I am so lucky to be a student here..."
        call ctc

        # Reveal titty
        stop music
        show her_ball speech h2 mouth_open eyes_closed sperm_cum4 as cg
        play sound "sounds/boing02.ogg"
        call ctc

        show screen blktone
        with hpunch
        gen "!!!" ("angry", xpos="far_left", ypos="head")
        sna "!!!" ("snape_11")
        hide screen blktone

        play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
        her "Thank you, everyone..."
        her "Let me say this again..."
        her "Thank you for making me your ball queen this year..."
        show her_ball speech h2 mouth_open eyes_closed sperm_cum5 as cg
        call ctc

        call blktone_top
        mal "{size=-4}Am I hallucinating?{/size}"
        mal2 "{size=-4}No, it's really happening... I see it too...{/size}"
        mal "{size=-4}Hermione... Granger's... tit...{/size}"
        mal "{size=-4}Major wardrobe malfunction, mate!{/size}"
        fem "{size=-4}Oh no! Poor thing! We must let her know!{/size}"
        mal "{size=-4}Don't you dare to take this away from us, girl!{/size}"
        fem "{size=-4}But...!!{/size}"
        call hide_blktone_top
        call ctc

        her "And most of all, I am thankful to my parents..."
        her "The people who raised me..."
        her "Mum... Dad..."
        show her_ball speech h2 mouth_open eyes_squint sperm_cum6 brows_down as cg
        her "I wish you could see how much Hogwarts changed me..."
        her "I wish you could see what has happened to that little girl you raised..."
        her "{size=-5}*Ah*...{/size}{heart}"
        call ctc

        call blktone_top
        gen "The whore is blushing! She is well aware of what's going on!" ("angry", xpos="far_left", ypos="head")
        gen "Nasty slut!" ("angry", xpos="far_left", ypos="head")
        gen "(She planned the whole thing??!)" ("angry", xpos="far_left", ypos="head")
        gen "(By the great desert sands... What have I unleashed!?)" ("base", xpos="far_left", ypos="head")
        call hide_blktone_top

        show her_ball speech h2 mouth_open eyes_squint sperm_cum6 brows_down as cg
        her "..............................."
        her ".................."
        call ctc

        call blktone_top
        mal "{size=-4}Now she just sort of stands there...{/size}"
        mal2 "{size=-4}Giving us a better look...?{/size}"
        mal "{size=-4}Do You think she is aware of her tit being visible at all?{/size}"
        fem "{size=-4}What a shameless display...{/size}"
        fem "{size=-4}And to think that I almost felt sorry for that slut...{/size}"
        fem "........................"
        with hpunch
        fem "{size=+5}Cover up, you shameless slut!!!{/size}"
        mal "{size=-4}!!!{/size}"
        mal2 "{size=-4}Have you lost your mind, yelling like that?!{/size}"
        with hpunch
        fem "{size=+5}Gryffindor whore!!!{/size}"
        call hide_blktone_top

        show her_ball speech h2 mouth_open eyes_closed sperm_cum6 brows_down as cg
        her "{size=-3}*Ah*...{/size}{heart}"
        her "...............................*A-ha*...{heart}{heart}{heart}"
        call ctc

        "Somebody from the crowd" "Show us both of them, Hermione!"
        "Another voice from the crowd" "Look! Her face is all covered in cum!"
        "Somebody from the crowd" "Have you no shame anymore, Hermione?!"
        "Another voice from the crowd" "Cover up, you slut!"

        show her_ball speech h2 mouth_open eyes_none sperm_cum6 brows_none as cg
        her "Oh... That's right..."
        her "I almost forgot..."
        show her_ball speech h2 mouth_open eyes_closed sperm_cum6 brows_none as cg
        her "{size=+5}Go Gryffindor!{/size}"
        play sound "sounds/applause01.ogg"
        nar "The crowd starts whistling and cheering wildly."
        show her_ball speech h2 mouth_open eyes_squint sperm_cum6 brows_down as cg
        her "......................................"
        her ".........................................................."
        call ctc

        sna "Quiet down, everyone!" ("snape_12", ypos="head")
        sna "As for you, Miss Granger..." ("snape_12")
        sna "I think that's enough." ("snape_12")
        sna "Cover up and get off the stage... Go..." ("snape_12")
        pause.1

        show her_ball speech h2 mouth_open eyes_none sperm_cum6 brows_none as cg
        her "\"Cover up\", sir?"
        show her_ball speech h2 mouth_open eyes_squint sperm_cum6 brows_down as cg
        her "Oh? What is this? One of my breasts is completely exposed..."
        show her_ball speech h2 mouth_none eyes_squint sperm_cum6 brows_down as cg
        her "How embarrassing..."
        show her_ball speech h2 mouth_open eyes_closed sperm_cum6 brows_down as cg
        her "*Ah*...{heart}{heart}{heart}"
        call ctc

        "Somebody from the crowd" "Whore!"
        "Another voice from the crowd" "Gryffindor slut!"
        "Somebody from the crowd" "I love you, Hermione!"
        "Another voice from the crowd" "Gryffindor rules!!!"

        sna "Miss Granger, I said that's enough!" ("snape_18", ypos="head")
        pause.1

        her "As you say, professor..."
        sna "And wipe your face, girl. You look repulsive." ("snape_12", ypos="head")
        pause.1

        show her_ball speech h2 mouth_open eyes_none sperm_cum6 brows_none as cg
        her "Oh, this? This is just my--"
        sna "Don't care! Get off the stage already!" ("snape_18", ypos="head")
        sna "Now!" ("snape_18")
        pause.1

        show her_ball speech h2 mouth_none eyes_squint sperm_cum6 brows_down as cg
        call ctc

        call blkfade
        play sound "sounds/applause01.ogg"
        nar "Wild whistling and cheering continues as Hermione descends from the stage."
        pause 1
        stop music fadeout 3.0

        # Back in the alcove
        hide cg
        call hide_blkfade
        call ctc

        her @ cheeks blush "[name_genie_hermione]..." ("soft", "narrow", "base", "R_soft", ypos="head", flip=False)
        her "There was something you wanted to discuss with me?"
        gen "Not right now, whore!" ("angry", xpos="far_left", ypos="head")
        call blkfade

        her @ cheeks blush "Sir?!" ("base", "narrow", "base", "mid_soft")
        gen "I want to fuck you so badly! Come over here!" ("angry", xpos="far_left", ypos="head")
        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed
        her @ cheeks blush "Of course, sir..." ("silly", "squint", "worried", "up")

        # Insertion
        play sound "sounds/gltch.ogg"
        with hpunch
        with kissiris
        pause.5
        gen "{size=+7}OH YEEEES!{/size}" ("angry", xpos="far_left", ypos="head")

        show her_ball sex h1 mouth_open1 eyes_none blush_b1 as cg
        show screen bld1
        call hide_blkfade
        call ctc

        her "*Aaah*!!!"
        gen "Your acceptance speech was a disgrace, girl!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_closed brows_b1 blush_b1 as cg
        her "I thought it went rather well..."
        gen "Showing off your tits like that?!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_closed brows_none blush_b1 as cg
        her "Only one... *Ah*..."
        gen "What?" ("angry", xpos="far_left", ypos="head")
        her "Only one tit, sir..."
        gen "Whatever happened to that idealistic and self-righteous girl you once were?!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_none brows_none blush_b1 lashes_l1 as cg
        her "You fucked her out of me, [name_genie_hermione]!"
        gen "You're damn right I did!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_up brows_b1 blush_b1 lashes_l1 as cg
        her "You fucked her out of me with your enormous cock, [name_genie_hermione]!"
        gen "*Argh*! You whore!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.1
        hide screen white
        with hpunch

        show her_ball sex h1 mouth_none eyes_wide brows_none blush_b1 lashes_none as cg
        her "Ah!!!"
        gen "Quiet, whore! Someone will hear you!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.1
        hide screen white
        with hpunch

        her "Ah! [name_genie_hermione]!"
        gen "I said be quiet!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.1
        hide screen white
        with hpunch

        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none as cg
        her "Ah! [name_genie_hermione]!"
        show her_ball sex h1 mouth_none eyes_up brows_b1 blush_b1 lashes_none as cg
        her "Yes! Fuck me harder!"
        gen "Are you raising your voice on purpose, whore?" ("base", xpos="far_left", ypos="head")
        gen "Do you want to get caught like this?" ("angry", xpos="far_left", ypos="head")
        gen "On your professor's cock?" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open_tongue1 eyes_r brows_none blush_b1 lashes_none as cg
        her "Ah! Maybe..."
        show her_ball sex h1 mouth_none eyes_up brows_b1 blush_b1 lashes_none as cg

        her "Call me a mudblood, sir!"
        gen "What?" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none as cg
        her "Call me a mudblood, please!"
        gen "A \"mudblood\"?" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_wide brows_none blush_b1 lashes_none as cg
        her "Ah! Yes! Yes! I am a mudblood whore!"
        gen "Whatever!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.5
        hide screen white
        with hpunch

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.4
        hide screen white
        with hpunch

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch

        show her_ball sex h1 mouth_none eyes_stare brows_none blush_b1 lashes_none tears_t1 spank_s1 as cg

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.2
        hide screen white
        with hpunch

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.1
        hide screen white
        with hpunch

        show her_ball sex h1 mouth_none eyes_stare brows_none blush_b1 lashes_none tears_t2 spank_none as cg
        her "*AAAAAAAhH*!"
        her "Yes!!! Yeeees! Ah!"
        show her_ball sex h1 mouth_open_tongue1 eyes_stare brows_b1 blush_b1 lashes_none tears_t2 spank_none as cg
        her "Fuck me [name_genie_hermione]! Fuck me harder!!!"
        gen "*Grh*! Harder than this, whore?!" ("angry", xpos="far_left", ypos="head")
        gen "!!!" ("angry", xpos="far_left", ypos="head")
        gen "Crap!  Someone's coming!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_stare brows_none blush_b1 lashes_none tears_t2 spank_none as cg
        her "No, sir, not yet. But if you keep spanking me--"
        gen "No, whore! A bunch of students are coming this way!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_up brows_none blush_b1 lashes_none tears_t2 spank_none as cg
        her "What?!"

        # Students join
        show her_ball sex h1 mouth_open1 eyes_stare brows_none blush_b1 lashes_none tears_t1 spank_none guy2_pose1 as cg
        sly1 "Well, well, well... What do we have here?"
        her "!!!"
        sly1 "I thought it could be you, Gryffindor filth..."
        sly1 "Moaning like a whore..."
        sly1 "Getting fucked by... Oh..."
        with hpunch
        sly1 "Professor Dumbledore!?"
        gen "Hello, boys..." ("base", xpos="far_left", ypos="head")
        her ".........................."
        sly1 "Oh... *Ehm*... We didn't know..."
        sly1 "We'll be leaving now..."
        gen "What? Don't be silly, boys." ("base", xpos="far_left", ypos="head")
        gen "You are more than welcome to stay." ("base", xpos="far_left", ypos="head")
        sly1 "We are?"
        show her_ball sex h1 mouth_open1 eyes_wide brows_none blush_b1 lashes_none tears_none spank_none guy2_pose1 as cg
        her "What?!"
        gen "Of course." ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none tears_none spank_none guy2_pose1 as cg

        her "Professor!!!?"
        gen "The girl's front side is completely at your disposal." ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose1 as cg
        her "Professor! No!"
        gen "What's wrong, [name_hermione_genie]?" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none tears_none spank_none guy2_pose1 as cg
        her "Sir, don't call me that in front of them, please..."
        gen "What's the matter? Why are you acting shy all of a sudden?" ("base", xpos="far_left", ypos="head")
        her "Can't you see that they are from Slytherin?!"
        gen "So what?" ("base", xpos="far_left", ypos="head")
        her "Our two houses... we have a history."
        gen "Oh..." ("base", xpos="far_left", ypos="head")
        gen "Well, then you shall become the bridge between Slytherin and Gryffindor." ("base", xpos="far_left", ypos="head")
        gen "Hermione Granger, the ambassador of peace!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_happycl brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose1 as cg
        her "No, sir! I refuse!"
        her "And stop moving your hips while we're talking, sir!"
        gen "Boys, what is taking you so long?" ("base", xpos="far_left", ypos="head")
        gen "I said, the whore is yours!" ("base", xpos="far_left", ypos="head")
        her "Professor Dumbled--"
        sly1 "Shut up, filth!"

        # Spit on face
        play sound "sounds/spit.ogg"
        show her_ball sex h1 mouth_open1 eyes_dead brows_none blush_b1 lashes_none tears_none spank_none guy2_pose1 spit_guy_face as cg
        pause.2
        with hpunch

        show her_ball sex h1 mouth_open1 eyes_dead brows_none blush_b1 lashes_none tears_none spank_none guy2_pose1 spit_on_face -spit_guy_face as cg
        her "!!!"
        gen "There you go!" ("base", xpos="far_left", ypos="head")
        sly2 "*Ha-ha-ha*! Nice one! Look at her stupid face!"
        show her_ball sex h1 mouth_open1 eyes_stare brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose1 spit_on_face as cg
        her "You... You...!"
        sly1 "We really enjoyed your speech, Gryffindor slut."
        sly2 "Yeah... Sure did..."
        her "That wasn't meant for you, you Slytherin scum!"
        sly1 "Wasn't meant for us? What are you, stupid?"
        sly1 "You bared your filthy, muggle-born flesh on stage! In front of the entire school!"
        sly1 "{size=+7}Of course it was for everyone, you dumb cunt!{/size}"
        show her_ball sex h1 mouth_open1 eyes_down brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose1 spit_on_face as cg
        her "Sir! Stop fucking me!"
        gen "*Huh*? You mean, like this?" ("base", xpos="far_left", ypos="head")
        with hpunch
        pause.3

        her "*Ah-aha*! No, professor, stop it!"
        gen "Stop? I think I will fuck you harder instead!" ("base", xpos="far_left", ypos="head")
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3

        show her_ball sex h1 mouth_open1 eyes_dead brows_none blush_b1 lashes_none tears_none spank_none guy2_pose1 spit_on_face as cg
        her "*Ah-ah*!!!"
        sly1 "Yes... You are ours now, slut!"
        call ctc

        # Dicks out
        show her_ball sex h1 mouth_open1 eyes_none brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face as cg
        her "What?! What are you doing?!"
        her "Put your filthy dicks away immediately!"
        with hpunch
        pause.3
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face as cg
        her "*Ah*... *Ah-a*..."
        sly1 "Yes... I wanted to do this for quite some time now..."
        her "Professor!"
        gen "*Huh*? Oh, don't you mind me, girl." ("base", xpos="far_left", ypos="head")
        gen "Imagine that I'm not even here..." ("base", xpos="far_left", ypos="head")

        play sound "sounds/spit.ogg"
        show her_ball sex h1 mouth_open1 eyes_dead brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face spit_guy_face as cg
        pause.2
        with hpunch

        show her_ball sex h1 mouth_open1 eyes_happycl brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face -spit_guy_face as cg
        pause.2
        her "Stop it! Stop spitting in my face, you bastards!"
        sly1 "Make us, whore!"
        her "I am warning--"

        play sound "sounds/spit.ogg"
        show her_ball sex h1 mouth_open_tongue1 eyes_dead brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face spit_guy_mouth as cg
        pause.2
        with hpunch

        show her_ball sex h1 mouth_smile1 eyes_dead brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face -spit_guy_mouth as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*Gulp*!{/size}"
        sly2 "*Ha-ha-ha*! Right in the mouth! Good shot, mate!"
        sly1 "And she swallowed it too!"
        show her_ball sex h1 mouth_open1 eyes_happycl brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face as cg
        her "That was an accident!"
        sly1 "Was it? Let's see."
        her "*Huh*?"

        play sound "sounds/spit.ogg"
        show her_ball sex h1 mouth_open_tongue1 eyes_dead brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face spit_guy_mouth as cg
        pause.2
        with hpunch

        show her_ball sex h1 mouth_smile1 eyes_dead brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face -spit_guy_mouth as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*Gulp*!{/size}"

        sly2 "She did it again!"
        show her_ball sex h1 mouth_open1 eyes_happycl brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face as cg
        her "That's because I didn't expect it... It's just a reflex!"
        sly1 "That's one hot reflex!"
        gen "Oh... yes..." ("angry", xpos="far_left", ypos="head")
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Ah*... *Ah-aha*..."
        her "You will pay for this, you spineless slytheri--"
        sly1 "Shut it, mudblood!"
        with vpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        call ctc

        # Dick in mouth
        her "!!!........................................................."
        sly2 "Cool! I'm next!"
        her "*Gulp*!"
        sly1 "Suck my cock, bitch! Suck it!"
        gen "Do what the boy tells you, girl." ("base", xpos="far_left", ypos="head")
        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch

        gen "Come on!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_happycl brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        her "*Slurp*..."
        sly1 "She's doing it! Hermione Granger sucking me off, lads!"
        sly2 "Awesome! Can't wait to give it a go myself!"
        sly1 "Oh... wow... she's good..."
        her "*Slurp*! *Slurp*! *Gulp*!"
        sly1 "Oh yes... Yes..."
        sly1 "Oh... You are so good at this, whore!"
        sly1 "It's... I..."

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        show her_ball sex h1 mouth_full1 eyes_dead brows_none blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        her "{size=+7}*Gobble*?!?{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"

        # Swallowing cum
        show her_ball sex h1 mouth_none eyes_happycl brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*Gulp-gulp-gulp-gulp*!{/size}"
        play sound "sounds/gulp.ogg"
        her "*{size=+3}Gulp-gulp-gulp*...{/size}"
        play sound "sounds/gulp.ogg"
        her "*Gulp-gulp-gulp*..."
        play sound "sounds/gulp.ogg"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        show her_ball sex h1 mouth_none eyes_happycl brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        her "*Gu-aha*..."
        her "Is this all you got? Pathetic!"
        sly2 "Oh... Shut up whore... You sucked me dry..."
        show her_ball sex h1 mouth_none eyes_none brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face -guy1_bj1 as cg
        her "Come on! Who's next?!"
        sly2 "Me! I'm next!"
        with hpunch
        show her_ball sex h1 mouth_none eyes_none brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        call ctc

        show her_ball sex h1 mouth_none eyes_closed brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        her "*Slurp*! *Slurp*! *Slurp*!"
        gen "Oh... Yes... Yes!" ("angry", xpos="far_left", ypos="head")
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Slurp*! *Slurp*! *Slurp*!"
        sly2 "Oh! Her mouth is so slippery and warm!"
        her "*Slurp*! *Slurp*! *Slurp*!"
        gen "Yes! Suck that cock, you whore!" ("angry", xpos="far_left", ypos="head")
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Gulp*! Gulp!* *Slurp*!"
        sly2 "I don't know... *Ghh*... How much longer..."
        sly2 "... I could keep up like that."
        her "*Slurp-Slurp-Slurp-slurp*!"
        her "*Slurp-Gulp-Slurp-Slurp-gulp*!!!"
        sly2 "Oh, man... Oh, man..."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp*!!"
        sly2 "I... I..."
        sly2 "..................."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp*!!"
        with hpunch
        sly2 "{size=+7}I'm cummiiiiiiiiing!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        show her_ball sex h1 mouth_none eyes_dead brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        her "{size=+7}*gobble*?!?{/size}"
        show her_ball sex h1 mouth_none eyes_closed brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_face guy1_bj1 as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*Gulp-gulp-gulp-gulp*!{/size}"
        play sound "sounds/gulp.ogg"
        her "{size=+3}*Gulp-gulp*...{/size}"
        play sound "sounds/gulp.ogg"
        her "*Gulp..."
        sly2 "*Argh*... My cock..."
        show her_ball sex h1 mouth_none eyes_happycl brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_body spit_on_face -guy1_bj1 as cg
        her "*Gu-aha*..."
        show her_ball sex h1 mouth_none eyes_none brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_body spit_on_face as cg
        her "Next! Come on! Is this all you got?"
        sly1 "I'm next, mudblood!"
        show her_ball sex h1 mouth_open1 eyes_none brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_body spit_on_face as cg
        her "{size=-5}*Ah*... Don't call me that, you bastard...{/size}{heart}"
        sly1 "Gonna fuck your face real good, whore!"
        sly1 "And after I fill your mouth with my cum, you're gonna thank me!"
        sly1 "Aren't you, mudblood whore?"
        show her_ball sex h1 mouth_open1 eyes_up brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_body spit_on_face as cg
        her "Fuck you!"

        play sound "sounds/spit.ogg"
        show her_ball sex h1 mouth_none eyes_none brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_body spit_on_face spit_guy_mouth as cg
        pause.2
        with hpunch

        show her_ball sex h1 mouth_smile1 eyes_dead brows_b1 blush_b1 lashes_none tears_none spank_none guy2_pose2 spit_on_body spit_on_face -spit_guy_mouth as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*Gulp*!{/size}"

        sly1 "That's what I thought!"
        show her_ball sex h1 mouth_open1 eyes_none brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 spit_on_body spit_on_face as cg
        her "You worthless... slythe--"
        show her_ball sex h1 mouth_none eyes_down brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 -spit_on_body spit_on_face guy1_bj3 as cg
        her "!!?"
        show her_ball sex h1 mouth_none eyes_closed brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 spit_on_face guy1_bj3 as cg
        her "*Slurp*! *Slurp*! *Slurp*!"
        sly1 "Yes! Yes, you mudblood filth! Suck my cock! Suck it!"
        gen "This is quite extraordinary..." ("base", xpos="far_left", ypos="head")
        sly1 "Sir?"
        gen "It's just..." ("base", xpos="far_left", ypos="head")
        gen "Her pussy..." ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_down brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 spit_on_face guy1_bj3 as cg
        her "*Slurp*?"
        gen "It tightens every time you call the girl a \"mudblood\"..." ("base", xpos="far_left", ypos="head")
        gen "Try calling her that again, boy." ("base", xpos="far_left", ypos="head")
        sly1 "Gladly, sir."
        show her_ball sex h1 mouth_none eyes_closed brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 spit_on_face guy1_bj3 as cg
        her "*Slurp*! *Slurp*! *Slurp*!"
        sly1 "Yes, whore! I love fucking your {i}mudblood{/i} face!"
        sly1 "And you're loving every moment of this, aren't you?"
        sly1 "Aren't you, {i}mudblood{/i}?"
        her "*Slurp*! *Slurp*! *Gulp*!"
        gen "Yup... Every time you say that..." ("base", xpos="far_left", ypos="head")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        gen "What is this? Her legs are shaking!" ("base", xpos="far_left", ypos="head")
        gen "Are you cumming, girl?" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_none brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 spit_on_face guy1_bj3 as cg
        her "..............................................."
        gen "I think you are!" ("base", xpos="far_left", ypos="head")
        gen "Come on, boy, let's speed this thing up a little!" ("base", xpos="far_left", ypos="head")
        gen "Let's fuck her from both ends while she is cumming like a dirty slut!" ("base", xpos="far_left", ypos="head")
        sly1 "Of course, sir."

        sly1 "Take this, you mudblood whore!"
        with vpunch
        pause.3
        with vpunch
        pause.3
        with vpunch
        pause.3

        gen "And this!!!" ("angry", xpos="far_left", ypos="head")
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3

        her "{size=+7}!!!!!!!!{/size}"
        gen "Yes! Her pussy is flooded with juice!" ("angry", xpos="far_left", ypos="head")
        sly1 "*Agh*! Her mouth as well, sir."
        sly1 "I don't know how much longer I... oh..."
        sly1 "*Argh*!"
        sly1 "{size=+3}Take this, whore!{/size}"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause.1
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_b1 blush_b1 lashes_l1 tears_none spank_none guy2_pose2 spit_on_face guy1_bj3 sperm_cum_nose as cg
        her "{size=+7}*gobble*?!?{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"

        # Swallowing cum
        show her_ball sex h1 mouth_none eyes_dead brows_b1 blush_b1 lashes_l1 tears_t1 spank_none guy2_pose2 spit_on_face guy1_bj3 -sperm_cum_nose as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        play sound "sounds/gulp.ogg"
        her "*{size=+3}Gulp-gulp-gulp...*{/size}"
        play sound "sounds/gulp.ogg"
        her "*Gulp-gulp-gulp*..."
        play sound "sounds/gulp.ogg"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        her "....................."
        show her_ball sex h1 mouth_open1 eyes_none brows_b1 blush_b1 lashes_l1 tears_t1 spank_none guy2_pose2 spit_on_body spit_on_face -guy1_bj3 as cg
        her "*Gu-aha*..."
        sly2 "You drained my balls, bitch..."
        gen "Alright, boys! Let's bring this little party to a worthy conclusion." ("base", xpos="far_left", ypos="head")
        her "{size=+7}I'm cumming!{/size}"
        gen "Yeah, whatever, whore." ("base", xpos="far_left", ypos="head")
        gen "So, rest of you boys, you can just jerk off on her face now, alright?" ("base", xpos="far_left", ypos="head")
        sly1 "Of course, sir."
        sly2 "Yes, sir!"
        gen "Yes, just plaster her face with cum. She loves that shit!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_dead brows_b1 blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face as cg
        her "{size=+3}No! I am already cumming... Stop!{/size}"
        sly1 "*Heh*... Hermione Granger... What a whore!"
        sly2 "Yeah! Nothing but a mudblood cunt!"
        her "{size=+9}AAAAAH!!!!!{/size}"
        her "{size=+3}Yes! I'm a whore! I'm a whore!{/size}"
        sly1 "She even admits it!"
        sly2 "I don't think I can last much longer!"
        sly1 "Me neither!"
        sly2 "*ARGH*!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_b1 blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_dudes_cum as cg
        call ctc

        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        her "{size=+3}My face!!{/size}"
        sly1 "Take this, whore!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face -sperm_dudes_cum sperm_dudes_cum2 as cg
        call ctc

        her "{size=+5}*AAAAAAAAAAAAH*!{/size}"
        sly2 "*Argh*! Here! Me too!"

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face -sperm_dudes_cum2 sperm_dudes_cum3 as cg
        call ctc

        show her_ball sex h1 mouth_none eyes_closed brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_dudes_cum3 sperm_bukkake as cg
        call ctc

        her "{size=+4}I'm cumming!{/size}"
        gen "Well, don't mind if I do!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_happycl brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_dudes_cum3 sperm_bukkake as cg
        her "{size=+3}No professor, I............!{/size}"
        gen "*Argh*!" ("angry", xpos="far_left", ypos="head")

        show screen white
        pause.1
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_happycl brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_dudes_cum3 sperm_bukkake sperm_cum_anal sperm_cum_pussy as cg
        call ctc

        her "{size=+8}*AAAAAAAAAAAAH*!{/size}"
        show her_ball sex h1 mouth_none eyes_happycl brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_cum_after -sperm_dudes_cum3 sperm_bukkake sperm_cum_anal sperm_cum_pussy as cg
        her "{size=+5}No! My face! My pussy! Ah! I can't stop cumming!!!{/size}"
        sly1 "What a slut!"
        sly2 "Whore!"
        sly1 "Mudblood!"
        her "{size=+8}*AAAAAAAAAAAAH*!{/size}"

        play sound "sounds/spit.ogg"
        pause.3
        with vpunch
        show her_ball sex h1 mouth_none eyes_happycl brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_cum_after -sperm_dudes_cum3 sperm_bukkake sperm_cum_anal sperm_cum_pussy spit_guy_mouth as cg
        call ctc

        show her_ball sex h1 mouth_smile1 eyes_happycl brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_cum_after -sperm_dudes_cum3 sperm_bukkake sperm_cum_anal sperm_cum_pussy -spit_guy_mouth as cg
        play sound "sounds/gulp.ogg"
        her "{size=+8}*Gulp*!{/size}"

        show her_ball sex h1 mouth_none eyes_happycl brows_none blush_b1 lashes_l1 tears_t2 spank_none guy2_pose2 spit_on_body spit_on_face sperm_cum_after -sperm_dudes_cum3 sperm_bukkake sperm_cum_anal sperm_cum_pussy spit_guy_mouth as cg
        her "{size=+8}I'll go insane!{/size}"
        call ctc

        show screen white
        with d9
        pause 1
        hide screen white
        show screen blkfade
        with d9

        call ctc

        gen "Well, thank you for your cooperation, boys." ("base", xpos="far_left", ypos="head")
        sly1 "Of course, professor Dumbledore."
        sly2 "Glad to be of help, sir."
        sly1 "Thank you, professor."
        sly2 "Alright, let's go back to the ball."
        sly1 "Yeah, let's go!"
        sly2 "Bye, mudblood whore!"
        sly1 "Yeah, thank you for being such a slut!"
        her @ cheeks blush tears mascara_soft ".........................." ("soft", "narrow", "annoyed", "up", ypos="head", flip=False)

        play sound "sounds/footsteps.ogg"
        hide cg
        pause 2

        hide screen blkfade
        with d9

        sly1 "{size=-4}Man, professor Dumbledore sure is one cool dude.{/size}"
        sly2 "{size=-4}Yeah... Who would have thought...{/size}"
        sly1 "{size=-4}True. I can't help but respect the man...{/size}"
        gen "(*Aww*... Such nice lads...)" ("base", xpos="far_left", ypos="head")
        sly2 "{size=-4}Yeah... I hope I will be as agile as he is when I am that ancient.{/size}"
        gen "(I'm not ancient, you punks!)" ("angry", xpos="far_left", ypos="head")
        gen "(Although I suppose in some way I am...)" ("base", xpos="far_left", ypos="head")

        #TODO Cum layer on Hermione doll (and ball ending CG?)

        her @ cheeks blush tears mascara_soft ".........................." ("soft", "narrow", "annoyed", "up")
        gen "Whore! Why are you so quiet?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "I..." ("silly", "narrow", "annoyed", "up")
        her @ cheeks blush tears mascara_soft "I am... not sure..."
        her @ cheeks blush tears mascara_soft "What...? What is..." ("soft", "narrow", "annoyed", "up")
        gen "Come on, girl. Pull yourself together!" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "I... I... What?" ("open", "narrow", "worried", "mid_soft")
        her @ cheeks blush tears mascara_soft "I don't understand... I..."
        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        gen "I will be leaving now." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "Leaving...?" ("soft", "narrow", "annoyed", "up")
        gen "Yes. Maybe you should too..." ("base", xpos="far_left", ypos="head")
        gen "Go clean yourself up and rest or something." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "But I can't leave... No... I must..." ("open", "narrow", "worried", "mid_soft")
        her @ cheeks blush tears mascara_soft "The formal dance... I must..."
        gen "A dance? You can't dance in this condition." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "No! I am the ball queen! I must..." ("soft", "narrow", "annoyed", "up")
        gen "Well, suit yourself." ("base", xpos="far_left", ypos="head")
        gen "I'm leaving..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "Goodbye... sir..." ("soft", "narrow", "annoyed", "up")
        gen "............." ("base", xpos="far_left", ypos="head")
        gen "Farewell, girl." ("base", xpos="far_left", ypos="head")
        call ctc

        call blkfade
        show her_ball entrance hall crowd h2 as cg
        pause.5
        call hide_blkfade

        play music "music/Brandenburg No4-1 BWV1049 Kevin-McKleod.ogg" fadein 1 fadeout 1 if_changed
        call ctc

        gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
        gen "Maybe I should stay and watch Hermione's post-multiple-orgasm dancing?" ("base", xpos="far_left", ypos="head")
        gen "No... This ball is almost over. This is my only chance to sneak out unnoticed." ("base", xpos="far_left", ypos="head")
        call ctc

        call blkfade
        pause.5

    else:

        # Personal whore ending
        sna "Miss Granger...?" ("snape_03", ypos="head")
        sna "You decided to show up after all? What an unpleasant surprise..." ("snape_04")
        her @ cheeks blush tears mascara "..............................." ("full", "narrow", "annoyed", "up", ypos="head", flip=False)
        sna "What happened to your face, girl?" ("snape_13")
        her @ cheeks blush tears mascara "......................................." ("full", "narrow", "worried", "down")
        sna "*Hmm*... Well, go ahead then..." ("snape_13")
        sna "Here is the tiara..." ("snape_13")
        her @ cheeks blush tears mascara "......................................." ("full", "narrow", "worried", "down")

        sna "And the stage is yours..." ("snape_13")
        pause.7

        show her_ball speech h1 mouth_full eyes_none sperm_cum_nose brows_none blush_heavy mascara_drip sweat_light as cg
        hide screen bld1
        call hide_blkfade

        play sound "sounds/applause01.ogg"
        call ctc

        her "..............."
        her ".................................."
        her ".........................................................................."

        play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
        show her_ball speech h1 mouth_open eyes_squint sperm_cum_mouth brows_down blush_heavy mascara_drip sweat_light as cg
        her "*Ah-a*........."

        gen "Is that...?" ("base", xpos="far_left", ypos="head")
        gen "Are there leftovers of my cum still in her mouth?" ("base", xpos="far_left", ypos="head")
        gen "What the hell is she doing?" ("angry", xpos="far_left", ypos="head")

        show her_ball speech h1 mouth_open eyes_closed sperm_cum_mouth brows_down blush_heavy mascara_drip sweat_light as cg
        her "...................................."
        her "*{i}Ello ev'ryone{/i}*..." #Misspelled on purpose.

        show her_ball speech h1 mouth_open eyes_closed sperm_cum_mouth brows_down blush_heavy mascara_drip sweat_light as cg
        her "{i}t'hank 'ou for comin' 'ere taday{/i}..." #Misspelled on purpose.
        gen "I can barely understand a word she is saying..." ("base", xpos="far_left", ypos="head")
        her "{i}Firs' of all, I woul' like t' t'hank fess'r umbled're...{/i}" #Misspelled on purpose.
        gen "Me?" ("base", xpos="far_left", ypos="head")
        her "................"

        show her_ball speech h1 mouth_full eyes_none sperm_cum_nose brows_down blush_heavy mascara_drip sweat_light as cg
        stop music fadeout 1.0
        her ".................................................."
        call ctc

        show her_ball speech h1 mouth_none eyes_none sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        play sound "sounds/gulp.ogg"
        her "{size=+5}*GULP*!!!{/size}"
        show her_ball speech h1 mouth_open eyes_squint sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        her "*Gua-ha*..."
        her "Thank you, professor."
        with hpunch
        gen "YOU WHORE!!!" ("angry", xpos="far_left", ypos="head")
        gen "When did you get this nasty!?" ("angry", xpos="far_left", ypos="head")

        play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
        show her_ball speech h1 mouth_open eyes_none sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        her "I would also like to thank my parents..."
        her "And I would like to thank my fellow students!"

        play sound "sounds/applause01.ogg"
        nar "Loud cheering and whistling erupts from the crowd."

        her "As well as the teachers, of course..."
        show her_ball speech h1 mouth_none eyes_none sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        nar "A few people can be heard clapping their hands."
        call ctc

        call blktone_top
        mal "{size=-4}So it's Hermione Granger again this year...{/size}"
        fem "{size=-4}*Tsk*... Why am I not surprised?{/size}"
        mal2 "{size=-4}Maybe because she deserves it?{/size}"
        mal "{size=-4}Yeah! Stop hating on Hermione!{/size}"
        fem "{size=-4}*Tch*... Whatever.{/size}"
        mal "{size=-4}By the way, when Hermione went on stage-{/size}"
        mal2 "{size=-4}Yeah, there was something in her mouth. I noticed it too.{/size}"
        fem "{size=-4}I bet it was someone's cum!{/size}"
        mal "{size=-4}WHAT?!!{/size}"
        mal2 "{size=-4}Get your head out of the gutter, girl!{/size}"
        fem "{size=-4}Why not?{/size}"
        fem "{size=-4}Everyone knows she is sleeping with Professor Dumbledore!{/size}"
        mal "{size=-4}No, not your gossips again.{/size}"
        mal2 "{size=-4}Wait, I want to hear this one. Tell us more.{/size}"
        fem "{size=-4}What is there to tell?{/size}"
        fem "{size=-4}Hermione Granger is a whore. She enjoys sucking cocks....{/size}"
        fem "{size=-4}Yes, she loves to suck cocks but she loves sperm even more!{/size}"
        mal "{size=-4}....{/size}"
        fem "{size=-4}She is a sperm addict! She must swallow half a cup of sperm every day...{/size}"
        fem "{size=-4}Because if she doesn't she goes into a sex-craze...{/size}"
        mal2 "{size=-4}.....{/size}"
        fem "{size=-4}And when that happens she cannot control herself and will gladly sleep with the first man she sees.{/size}"
        mal "{size=-4}.............{/size}"
        mal2 "{size=-4}.....................{/size}"
        fem "{size=-4}*Hmm*? Why are you staring at me like that?{/size}"
        mal "{size=-4}What? We're not staring.{/size}"
        mal2 "{size=-4}Yes, keep talking. You are good at this!{/size}"
        fem "{size=-4}Good at what?!{/size}"
        fem "{size=-4}Wait a second, are you guys getting off on this?{/size}"
        mal "{size=-4}*Heh*... Look at the crow calling the raven black!{/size}"
        fem "{size=-4}What do you mean?{/size}"
        mal2 "{size=-4}You are blushing like crazy, girl! And your eyes are all misty!{/size}"
        mal "{size=-4}Yeah! You enjoy this as much as we do!{/size}"
        fem "{size=-4}!!!?{/size}"
        fem "{size=-4}You guys are idiots!{/size}"

        play sound "sounds/run_03.ogg"
        pause 3
        mal "{size=-4}What? What did I say?{/size}"
        mal2 "{size=-4}Who knows, bro? Witches be crazy...{/size}"
        mal "{size=-4}They do be crazy...{/size}"
        call hide_blktone_top

        show her_ball speech h1 mouth_open eyes_none sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        her "Thank you, everyone, for being such a big help in organising tonight's event."
        her "And thank you for choosing me as your queen again this year..."
        show her_ball speech h1 mouth_open eyes_closed sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        her "What a pleasant and completely unexpected surprise...!"
        her "And one more thing..."
        show her_ball speech h1 mouth_open eyes_none sperm_cum_nose2 brows_down blush_heavy mascara_drip sweat_light as cg
        her "{size=+5}Go Gryffindor!{/size}"

        play sound "sounds/applause01.ogg"
        nar "The crowd explodes with loud cheers and whistles, interspersed by occasional booing..."

        call ctc

        call blkfade
        pause.7

        stop music fadeout 1.0
        gen "Great speech..." ("base", xpos="far_left", ypos="head")
        gen "Very arousing... *Ehm*... I mean inspiring." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Thank you, sir." ("soft", "narrow", "base", "R_soft", ypos="head", flip=False)
        gen "Swallowing my load in front of the entire school?" ("base", xpos="far_left", ypos="head")
        gen "A very nice touch." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "........................................................" ("crooked_smile", "happyCl", "worried", "mid")

        play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

        hide cg
        show screen bld1
        call hide_blkfade

        gen "Alright, girl. Let's have that talk now..." ("base", xpos="far_left", ypos="head")
        her "...................." ("upset", "base", "base", "mid")
        gen "There is something I need to tell you..." ("base", xpos="far_left", ypos="head")
        gen "Not sure where to start though..." ("base", xpos="far_left", ypos="head")
        gen "........................................" ("base", xpos="far_left", ypos="head")
        gen "Well, first of all I am--" ("base", xpos="far_left", ypos="head")
        her "Sir, I think I know exactly what you are about to say." ("open", "base", "base", "mid")
        gen "You do?" ("base", xpos="far_left", ypos="head")
        her "Of course." ("open", "base", "base", "mid")
        her @ cheeks blush "One hasty blowjob is not nearly enough to repay my debt to you, am I right?" ("base", "narrow", "base", "mid_soft")
        gen "What? No, that's not what I--" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "It's fine, sir. Really." ("base", "narrow", "base", "mid_soft")
        her @ cheeks blush "Let me just pull my panties down a little..." ("soft", "narrow", "base", "R_soft")
        gen "Damn you girl! Will you let me finish!?" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush "Of course sir..." ("base", "narrow", "base", "mid_soft")
        gen "*Huh*?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Just make sure you don't hit my dress, alright?" ("open_tongue", "narrow", "worried", "mid_soft")
        gen "*Growl*!" ("angry", xpos="far_left", ypos="head")
        gen "Come here, whore!" ("angry", xpos="far_left", ypos="head")
        gen "Suppose I might as well fuck you one last time!" ("angry", xpos="far_left", ypos="head")
        her "(One last time?)" ("upset", "base", "base", "mid")
        call ctc

        call blkfade
        play sound "sounds/gltch.ogg"
        with hpunch
        with kissiris

        her @ cheeks blush tears soft "{size=+5}Ahh!!!{/size}" ("open", "wide", "worried", "stare")
        gen "Oh, yes!" ("angry", xpos="far_left", ypos="head")

        show her_ball sex h1 mouth_none eyes_none brows_none blush_b1 lashes_none as cg
        hide screen bld1
        call hide_blkfade
        call ctc

        her "*Ah-ah*..."
        gen "*Hmm*? Your pussy..." ("base", xpos="far_left", ypos="head")
        gen "It's dripping wet, girl." ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_down brows_none blush_b1 lashes_none as cg
        her "*Ah*...{heart} It is, sir?"
        her "That's probably from before..."
        gen "From before?" ("base", xpos="far_left", ypos="head")
        gen "You mean when you were choking on my cock?" ("base", xpos="far_left", ypos="head")
        her "*Ah*...{heart} Yes, sir..."
        gen "Did it make you cum?" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_closed brows_none blush_b1 lashes_none as cg
        her "A little..."
        gen "Well, you're just precious then, aren't you?" ("base", xpos="far_left", ypos="head")
        her "*Ah*......"
        gen "Aren't you, whore?!" ("base", xpos="far_left", ypos="head")
        her "*Ah*... Whatever you say, sir."
        gen "Yes, you are precious, you slut!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_closed brows_none blush_b1 lashes_none as cg
        her "............."
        gen "Squeezing my cock with your little pussy!" ("base", xpos="far_left", ypos="head")
        her "......................"
        gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
        gen "Why are you being so quiet?" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none as cg
        her "Oh... I'm just afraid that someone would--"
        gen "I think that's because you want to get spanked!" ("base", xpos="far_left", ypos="head")
        her "What!?"

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.1
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_open1 eyes_stare brows_b1 blush_b1 lashes_none tears_t1 as cg

        her "*EEeeeeeeeegh*!"
        gen "Quiet, whore! Someone could hear you!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_b1 blush_b1 lashes_none tears_t1 as cg
        her "Sir, I--"

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_smile1 eyes_stare brows_b1 blush_b1 lashes_none tears_t1 as cg

        her "{size=+7}*EEghh*!!!{/size}"
        gen "Be quiet, I said!" ("base", xpos="far_left", ypos="head")
        gen "Or do you want to get caught like this, on your headmaster's cock?" ("base", xpos="far_left", ypos="head")
        gen "Do you, Miss queen of the autumn ball?" ("base", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_b1 blush_b1 lashes_none tears_t1 as cg

        her "*Ah*..."
        gen "Yes, you're liking this, aren't you?!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_smile1 eyes_happycl brows_b1 blush_b1 lashes_none tears_none as cg
        her ".............."
        gen "Answer me, slut!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_t1 as cg

        her "Yes, sir! I love it!!!"
        show her_ball sex h1 mouth_open1 eyes_up brows_b1 blush_b1 lashes_none tears_t1 as cg
        her "Spank me harder, sir! I deserve it!"
        gen "That's the spirit!" ("base", xpos="far_left", ypos="head")
        call ctc

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_t1 as cg
        call ctc

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_t1 as cg
        call ctc

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_t1 spank_s1 as cg
        call ctc

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_t1 spank_s1 as cg
        call ctc

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_open_tongue2 eyes_dead brows_none blush_b1 lashes_l1 tears_t1 spank_s1 as cg
        call ctc

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_open_tongue2 eyes_dead brows_none blush_b1 lashes_l1 tears_t1 spank_s1 as cg
        call ctc

        her "{size=+7}*Aaaaaah*............................{/size}"

        call blktone_top
        sna "Attention, maggots!"
        sna "The formal dance of the Hogwarts Autumn Ball is about to begin..."
        call hide_blktone_top

        show her_ball sex h1 mouth_open1 eyes_wide brows_none blush_b1 lashes_none tears_t1 spank_s1 as cg
        her "!!!"
        her "The dance! I completely forgot!!!"
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none tears_t1 spank_s1 as cg
        her "Sir, excuse me, but you have to let me go..."
        gen "*Ah*... Your pussy is something else!" ("angry", xpos="far_left", ypos="head")
        her "Sir-- *Ah*...{w=0.3} I am serious."
        her "As the queen, I am expected to lead the dance."
        gen "Yes... Like that, just like that... Oh, yes..." ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_b1 blush_b1 lashes_none tears_t1 spank_s1 as cg
        her "Sir, are you even listening?"
        gen "Oh, I hear you alright... But let me make you a counteroffer." ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_none tears_t1 spank_s1 as cg
        her "Sir?"
        gen "Instead of letting you go..." ("base", xpos="far_left", ypos="head")
        gen "I will stick my cock up your ass." ("base", xpos="far_left", ypos="head")
        gen "How about that?" ("base", xpos="far_left", ypos="head")
        her "What? B-but..."
        gen "I think that is a great plan!" ("base", xpos="far_left", ypos="head")
        her "Sir, no! I--"
        gen "One sec, one sec..." ("base", xpos="far_left", ypos="head")
        call blkfade

        gen "Let me take my dick out of your pussy first..." ("base", xpos="far_left", ypos="head")

        play sound "sounds/plop.ogg"
        with hpunch
        pause.3

        # Insertion
        her @ cheeks blush tears soft "*Ah*..." ("open", "wide", "worried", "stare", ypos="head", flip=False)
        her @ cheeks blush "Sir, no. You must listen to me--" ("open_tongue", "narrow", "worried", "mid_soft")
        play sound "sounds/gltch.ogg"
        with hpunch
        with kissiris

        her @ cheeks blush tears soft "{size=+7}!!!!!!!!!!!!!!!!!{/size}" ("scream", "wide", "worried", "stare")
        her "My...{w} My...{w} My..."
        gen "Shut it, girl! You are being loud." ("base", xpos="far_left", ypos="head")
        with hpunch
        her @ cheeks blush tears soft "{size=+7}My anus!!!!!!!!!!!!!{/size}" ("scream", "wide", "worried", "stare")
        gen "Dammit, girl. I said be quiet." ("angry", xpos="far_left", ypos="head")

        show her_ball sex h1 mouth_open_tongue1 eyes_stare brows_b1 blush_b1 lashes_none tears_t2 spank_none as cg
        call hide_blkfade

        her "{size=+7}I can't! I don't care! It hurts!!!{/size}"
        gen "Maybe you don't care, but I do, you whore!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_stare brows_b1 blush_b1 lashes_none tears_t2 as cg
        her "{size=+5}Your cock is so huge!{/size}"
        gen "We'll get caught because of you, you stupid slut!" ("angry", xpos="far_left", ypos="head")
        gen "Maybe this will help you shut up..." ("base", xpos="far_left", ypos="head")

        # Fishhooking
        show her_ball sex h2 mouth_none eyes_none brows_none blush_b2 lashes_none tears_none as cg
        her "!!!............"
        gen "That's right, you slut. Keep quiet!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h2 mouth_open_tongue2 eyes_none brows_none blush_b2 lashes_none tears_none as cg
        her "*Ah*... *Blah*..."
        gen "Your butthole... It's so damn tight..." ("angry", xpos="far_left", ypos="head")
        show her_ball sex h2 mouth_open_tongue2 eyes_none brows_none blush_b2 lashes_none tears_none spit_on_body as cg
        her "*Ah*... *Blah*... *Ah*..."
        gen "You are drooling all over my hand, you nasty slut!" ("angry", xpos="far_left", ypos="head")
        her "*Ah*... *Blah-blhah*... *Ah*... *Bla-ah*..."

        call blktone_top
        stop music fadeout 1.0
        sna "Well, we are about to start..."
        sna "Get into pairs now..."
        sna "No! Male-female pairs, you dull creatures. What do you think this is? A laboratory assignment?"

        call hide_blktone_top
        show her_ball sex wall2 h1 mouth_open_tongue2 eyes_r brows_none blush_b1 lashes_l1 tears_none spit_on_body as cg

        play music "music/Brandenburg No4-1 BWV1049 Kevin-McKleod.ogg" fadein 1 fadeout 1 if_changed
        gen "Don't you worry about missing out on your dance, whore." ("base", xpos="far_left", ypos="head")
        gen "We will do a little bit of dancing of our own..." ("base", xpos="far_left", ypos="head")
        her "*Ah*..."
        gen "Yes, this year's ball queen is performing a complicated pirouette with a dick buried deep in her tiny asshole!" ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open_tongue2 eyes_stare brows_none blush_b1 lashes_l1 tears_none spit_on_body as cg
        her "*Ah*... I am--{w=0.2} *Ahh*..."
        gen "Did you say something, your majesty?" ("base", xpos="far_left", ypos="head")
        her "*Ah*... I am the autumn ball queen... *ah*..."
        gen "Well of course you are!" ("base", xpos="far_left", ypos="head")
        gen "But you're also a whore!" ("base", xpos="far_left", ypos="head")
        her "I'm a whore..."
        show her_ball sex h1 mouth_open_tongue2 eyes_stare brows_b1 blush_b1 lashes_l1 tears_none spit_on_body as cg
        her "{size=+7}I'm a whore!!!{/size}"
        show her_ball sex h1 mouth_open_tongue2 eyes_stare brows_none blush_b1 lashes_none tears_none spit_on_body as cg
        her "{size=+10}I'm a whoooooooore!!!{/size}"
        gen "Yes you are!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_open_tongue2 eyes_wide brows_b1 blush_b1 lashes_none tears_none spit_on_body as cg

        her "{size=+5}I'm a whore!!!{/size}"
        gen "Yes you are!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        her "{size=+5}I'm a whore!!!{/size}"
        gen "Yes you are!" ("angry", xpos="far_left", ypos="head")

        play sound "sounds/slap_02.ogg"
        show screen white
        pause.3
        hide screen white
        with hpunch
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_none spit_on_body as cg
        her "{size=+5} I'm cumming!!!{/size}"

        with hpunch
        gen "*Argh*! My cock!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_dead brows_b1 blush_b1 lashes_none tears_none spit_on_body as cg
        her "{size=+10}I'M CUMMING! I'm a whore!{/size}"
        gen "I can't fucking move it anymore!" ("angry", xpos="far_left", ypos="head")
        her "{size=+10}I'm CUMMING!{/size}"

        gen "My cock is stuck in your asshole, slut!" ("angry", xpos="far_left", ypos="head")
        her "{size=+10}I'm a whooore!!!{/size}"
        gen "Relax your muscles a little, dammit!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_none spit_on_body as cg
        her "{size=+7}I can't! I'm cumming!!!{/size}"
        gen "Fine! Have it your way. I am switching back to your pussy..." ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_up brows_none blush_b1 lashes_none tears_none spit_on_body as cg
        her "*Huh*?"
        call blkfade

        gen "Can't pull out!" ("angry", xpos="far_left", ypos="head")
        gen "Relax your damn anus, girl! ..." ("angry", xpos="far_left", ypos="head")

        play sound "sounds/plop.ogg"
        with hpunch
        pause.3

        her @ cheeks blush tears messy "..........." ("angry", "narrow", "annoyed", "up", ypos="head", flip=False)
        gen "There..." ("base", xpos="far_left", ypos="head")


        ### INSERTING ###

        play sound "sounds/gltch.ogg"
        with hpunch
        with kissiris
        pause.5

        hide screen bld1
        hide screen blkfade
        show her_ball sex h1 mouth_none eyes_dead brows_none blush_b1 lashes_none tears_none spit_on_body mascara_m1 as cg
        her "{size=+10}*AAAAAAAAAAAH*!!{/size}"
        her "It's in my pussy again..."
        gen "Yes it is, slut!" ("angry", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_open1 eyes_up brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 as cg
        her "But I'm still cumming!"
        her "What is happening to me, sir!?"
        gen "Relax girl, I know what I'm doing!" ("base", xpos="far_left", ypos="head")
        gen "This is normal for a slut." ("base", xpos="far_left", ypos="head")
        show her_ball sex h1 mouth_none eyes_up brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 as cg
        her "{size=+5}No! I will go insane!!!{/size}"
        gen "You will not. Just ride the wave." ("angry", xpos="far_left", ypos="head")
        gen "Enjoy the sensation while I keep on pounding your pussy!" ("angry", xpos="far_left", ypos="head")
        her "{size=+5}*Ah*!!!{/size}"

        show her_ball sex h1 mouth_open1 eyes_down brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 as cg
        her "{size=+5}*Ah*!!!{/size}"
        her "{size=+5}I'm a whore!!!{/size}"
        gen "Yes you are!" ("angry", xpos="far_left", ypos="head")
        her "{size=+5}I'm a slut!!!{/size}"
        gen "Yes you are!" ("angry", xpos="far_left", ypos="head")
        gen "*Ah*... I think I am getting close myself..." ("angry", xpos="far_left", ypos="head")
        gen "*Argh*!" ("angry", xpos="far_left", ypos="head")

        menu:
            "-Cum inside Hermione's pussy-":
                $ states.her.status.creampie = True
                $ d_flag_01 = True # Came into pussy

                gen "You think your pussy is ready for this, whore?" ("angry", xpos="far_left", ypos="head")
                her "Sir?!"
                gen "Then take this!" ("angry", xpos="far_left", ypos="head")

                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch
                show her_ball sex h1 mouth_none eyes_wide brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_pussy as cg

                her "{size=+5}*Ah*! *AAaaah*!!{/size}"
                gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}" ("angry", xpos="far_left", ypos="head")

                her "{size=+5}*Ah*! I can feel it! It's so hot!{/size}"
                gen "*Argh*! Yes!" ("angry", xpos="far_left", ypos="head")
                show her_ball sex h1 mouth_none eyes_up brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_pussy sperm_cum_extra as cg

                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                gen "Yes! You whore! I'll pump your witch cunt full of my cum!" ("angry", xpos="far_left", ypos="head")

                show her_ball sex h1 mouth_open_tongue2 eyes_wide brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_pussy sperm_cum_extra as cg
                her "[name_genie_hermione]! My dress!"
                gen "What?" ("angry", xpos="far_left", ypos="head")
                her "Make sure you don't get any on my dress!"
                gen "Shut up about your dress, whore! You are ruining the moment!" ("angry", xpos="far_left", ypos="head")
                show her_ball sex h1 mouth_none eyes_up brows_none blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_pussy sperm_cum_extra as cg
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                gen "Yes! Much better!" ("angry", xpos="far_left", ypos="head")
                gen "*Ah*......." ("angry", xpos="far_left", ypos="head")

            "-Cum inside Hermione's butt-":
                $ states.her.status.anal_creampie = True
                $ d_flag_01 = False # Came into asshole

                gen "Your butthole better be ready for this, whore!" ("angry", xpos="far_left", ypos="head")
                her "What?!"

                play sound "sounds/gltch.ogg"
                pause.5
                her "*Ah*..."

                play sound "sounds/plop.ogg"
                with hpunch
                with kissiris
                show her_ball sex h1 mouth_open1 eyes_stare brows_b1 blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 as cg
                her "{size=+10}*AAaaaahhhhh*!!!{/size}"
                her "{size=+5}It's in my butthole again!{/size}"
                show her_ball sex h1 mouth_open1 eyes_up brows_b1 blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 as cg
                her "{size=+5}No, sir, please! Don't cum in my butt!{/size}"
                her "{size=+5}No, I will die!!!{/size}"
                gen "You will not die, you silly girl." ("angry", xpos="far_left", ypos="head")
                gen "You will orgasm like crazy, maybe even pass out for a while, but that's all..." ("angry", xpos="far_left", ypos="head")
                her "No, sir, please... I'm scared..."
                gen "Take this, whore!" ("angry", xpos="far_left", ypos="head")
                show screen white
                pause.1
                hide screen white
                pause.2
                show screen white
                pause .1
                hide screen white
                with hpunch

                gen "{size=+15}*ARGH*!!!!!!!!!!!!!!!!{/size}" ("angry", xpos="far_left", ypos="head")
                show her_ball sex h1 mouth_open1 eyes_stare brows_b1 blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 as cg
                her "{size=+5}*Ah*! I can feel it!!!{/size}"
                gen "*Argh*! Yes!" ("angry", xpos="far_left", ypos="head")
                show her_ball sex h1 mouth_none eyes_stare brows_b1 blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_anal as cg
                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                gen "Yes! You whore! I'll pump you full of my cum!" ("angry", xpos="far_left", ypos="head")
                show her_ball sex h1 mouth_none eyes_down brows_b1 blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_anal as cg
                her "[name_genie_hermione]! My dress!"
                gen "What?" ("angry", xpos="far_left", ypos="head")
                her "Make sure you don't get any on my dress!"
                gen "Shut up about your dress, whore! You are ruining the moment!" ("angry", xpos="far_left", ypos="head")
                show her_ball sex h1 mouth_none eyes_up brows_b1 blush_b1 lashes_l1 tears_none spit_on_body mascara_m1 sperm_cum_anal as cg
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                gen "Yes! Much better!" ("angry", xpos="far_left", ypos="head")

        call ctc

        show screen blkfade
        with d9

        stop music fadeout 1.0
        her @ cheeks blush tears mascara_soft "*Ah*..." ("silly", "narrow", "annoyed", "up", ypos="head", flip=False)
        her "I can... barely... stand..."
        gen "I know what you mean, girl." ("angry", xpos="far_left", ypos="head")
        gen "This was our most intense fucking session yet!" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "Yes... I never knew I could..." ("silly", "narrow", "annoyed", "up")
        her "orgasm so hard..."
        her @ cheeks blush tears mascara_soft "Sir... That thing you wanted to discuss with me..." ("soft", "narrow", "annoyed", "up")
        gen "Yeah... You know what? I actually wrote you a little letter on the matter..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "A letter?" ("open", "narrow", "worried", "mid_soft")
        gen "Yeah... It should explain a couple of things..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara_soft "Oh... Alright..." ("silly", "narrow", "annoyed", "up")
        gen "Just come and pick it up from my office tomorrow morning..." ("base", xpos="far_left", ypos="head")
        gen "Or whenever..." ("base", xpos="far_left", ypos="head")
        gen "Or don't pick it up, I don't care..." ("base", xpos="far_left", ypos="head")
        gen "............." ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara "Sir...?" ("base", "base", "worried", "mid")
        gen "Stop it with the eyes! You're making me feel uncomfortable..." ("base", xpos="far_left", ypos="head")
        gen "I wrote you a letter, so what?" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara "I think it's sweet........." ("base", "base", "worried", "mid")
        gen "I said, stop gawking at me, girl. I thought you were late for your dance or something!" ("angry", xpos="far_left", ypos="head")
        her @ cheeks blush tears mascara "{size=+5}THE DANCE!{/size}" ("open", "wide", "base", "stare")
        her "I'm sorry, I have to go!"
        her "I will see you later, sir!"

        play sound "sounds/run_03.ogg"
        pause 3
        gen "......................" ("base", xpos="far_left", ypos="head")
        gen "No you won't..." ("base", xpos="far_left", ypos="head")
        gen "Farewell...{w=0.3} Hermione..." ("base", xpos="far_left", ypos="head")

        pause 2

        play music "music/court-of-the-queen-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

        show her_ball entrance hall crowd h2 as cg

        nar "You linger in the alcove for a short while longer..."
        nar "And watch Hermione participate in the formal dance."
        hide screen bld1
        call hide_blkfade
        call ctc

        nar "There is no doubt that she is tired and exhausted, but she hides it well..."

        gen "(*Hmm*... The girl really is strong...)" ("base", xpos="far_left", ypos="head")
        gen "(In all sorts of ways...)" ("base", xpos="far_left", ypos="head")


        if d_flag_01: # Came into pussy
            nar "You see a tiny stream of glistening liquid dripping down her inner thighs, going unnoticed by the crowd."
        else: # Came into asshole
            nar "You notice that she sort of clenches her buttocks together every now and then..."
            nar "Probably doing her best to keep in the enormous load you deposited up her butthole just a moment ago..."


        gen "................................................." ("base", xpos="far_left", ypos="head")
        gen "..............." ("base", xpos="far_left", ypos="head")
        gen "(I'd better go now...)" ("base", xpos="far_left", ypos="head")

        call ctc

    $ renpy.end_replay()

    label test_final_scene:

    # Genie is leaving
    call blkfade
    pause 1
    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of Hogwarts{/color}{/size}"

    $ game.daytime = False

    hide cg
    pause.3
    show her_ball outskirts as cg
    call hide_blkfade

    play background "sounds/night.ogg" fadein 1
    call ctc

    play sound "sounds/steps_grass.ogg"
    pause 2

    show her_ball outskirts g1 as cg
    pause 1
    gen "Well, now it is really time for me to go..." ("base", xpos="far_left", ypos="head")

    show her_ball outskirts g1 m1 as cg
    pause.5

    gen "Goodbye, world of bizarre magic..." ("base", xpos="far_left", ypos="head")
    gen "Goodbye, my whores..." ("base", xpos="far_left", ypos="head")
    gen "Goodbye, smart cumslut Hermione..." ("base", xpos="far_left", ypos="head")
    if states.cho.unlocked:
        gen "And my token Asian Cho..." ("base", xpos="far_left", ypos="head")
    if states.ast.unlocked:
        gen "And my sassy blonde Astoria..." ("base", xpos="far_left", ypos="head")
    if states.lun.unlocked:
        gen "And my {i}wackspit-sucking{/i} queen Luna..." ("base", xpos="far_left", ypos="head")
    if states.sus.unlocked:
        gen "And my big-titted redhead Susan..." ("base", xpos="far_left", ypos="head")
    gen "and of course, goodbye to my favourite nympho, Tonks..." ("base", xpos="far_left", ypos="head")
    gen "....................." ("base", xpos="far_left", ypos="head")
    gen "..........." ("base", xpos="far_left", ypos="head")
    "......"

    play sound "sounds/magic4.ogg"
    with hpunch

    show her_ball outskirts -g1 m2 as cg
    pause.2

    show her_ball outskirts m1 as cg
    pause.2

    show her_ball outskirts -m1 as cg
    call ctc

    show screen blktone
    with d7

    $ achievements.unlock("ending")
    stop background fadeout 1.0

    if "public" in states.her.ev.yule_ball.variant:
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n{color=#cbcbcb}This is one of two possible endings (public whore){/color}"
    else:
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n{color=#cbcbcb}This is one of two possible endings (personal whore){/color}"

    show screen blkfade
    with d7

    if not persistent.game_complete:
        call original_credits

    pause.5

    # Dumbledore is back at Hogwarts
    centered "{size=+7}{color=#cbcbcb}The next morning...{/color}{/size}"

    $ game.daytime = True

    $ hermione.equip(her_outfit_default)

    hide cg
    hide screen blktone
    stop weather
    hide screen notes
    hide screen bld1

    $ game.weather = "random"
    call weather_sound

    show screen main_room
    $ chair_OBJ.hidden = False

    call gen_chibi("hide")
    $ owl_OBJ.hidden = True
    hide screen with_snape

    $ chair_OBJ.hidden = False
    $ desk_OBJ.idle = "desk_dumbledore"

    hide screen blkfade
    with d9

    if "public" in states.her.ev.yule_ball.variant:
        play sound "sounds/door.ogg"
        call sna_chibi("stand","door","base", flip=False)
        with d3
        pause.8
        call sna_walk("mid", "base")
        pause.8

        play music "music/Dark Fog.ogg" fadein 1 if_changed
        dum1 "Good morning, Severus."
        sna "......................................." ("snape_09", xpos="base", ypos="base")
        dum1 "I have the most extraordinary tale to share with you, old friend."
        sna "......................................"
        dum1 "But before I do..."
        sna "........................................"
        dum2 "*Ehm*... Severus?"
        sna "........................................."
        sna "Who rules?" ("snape_06")
        dum2 "I beg your pardon?"
        sna "Who rules?" ("snape_26")
        dum2 "... who rules what?"
        sna "R...?"
        dum2 "R?"
        sna "Robin....?" ("snape_27")
        dum2 "You don't make any sense, Severus."
        sna "Ah, bloody hell........." ("snape_29")
        pause.5
        call ctc

        stop music fadeout 1.0

        hide snape_main
        hide screen bld1
        show screen blkfade
        with d7
        pause.1

    else:
        # Personal whore ending
        play sound "sounds/door.ogg"
        call her_chibi("stand","door","base", flip=False)
        pause.8

        call her_walk("mid", "base")
        pause.8

        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
        her "Sir, if this is about yesterday..." ("upset", "closed", "base", "mid", xpos="right", ypos="base")
        dum1 "Good morning, Miss Granger."
        her "It's not like I actually enjoyed it or anything, you know..." ("annoyed", "narrow", "annoyed", "mid")
        dum1 "Miss Granger, I found this letter on my desk..."
        dum1 "It's addressed to you..."
        her "A letter, sir?" ("soft", "base", "base", "mid")
        her "Oh, of course! The one you wrote for me, sir." ("grin", "happyCl", "worried", "mid",emote="sweat")
        dum1 "This letter is not from me, miss Granger."
        her "It is not?" ("annoyed", "squint", "base", "mid")
        her "Oh, I see..." ("grin", "happyCl", "worried", "mid",emote="sweat")
        her "There is no need to be so shy about this, sir. It's alright."
        dum1 "*Ahem*... Here it is."
        her "Thank you, sir." ("base", "base", "base", "mid")
        her "Let's see..." ("annoyed", "narrow", "worried", "down")
        hide hermione_main
        with d3
        stop music fadeout 7.0
        pause.1

        # Read letter from Genie
        $ letter = Letter(text="""{size=-5}To: Hermione Granger{/size}

{size=-4}Dear [word_01],

I am not who you think I am... I'm not even human, so to speak. For months I have been posing as a person known to you as Professor Dumbledore. But now it is time for me to go back [word_02], where I belong.
By the time you will read this letter I shall be long gone. We shall never cross paths again, but I promise you that I will cherish the memories of my brief time in your strange world.

Farewell, my little [word_03].{/size}

{size=-5}-Yours truly,\n[word_04]-{/size}"""
        )

        $ letter.open()

        her @ cheeks blush "..........................................................................................................." ("disgust","wide","worried","shocked")
        dum1 "I assume you were expecting to meet with that \"[word_04]\" fellow?"
        dum1 "The one who has been impersonating me for the past several months?"
        her @ cheeks blush "..........................................................................................................." ("disgust","wide","worried","shocked")
        dum1 "Well, now that I am back..."
        dum1 "I will be putting an end to all that \"favour selling business\", of course."
        her "" ("scream", "base", "angry", "mid",emote="angry")
        pause.1
        with hpunch
        play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
        her "{size=+7}What?!!{/size}"
        her "How am I supposed to win any points then?" ("disgust", "narrow", "base", "mid_soft")
        dum1 "The same way you always did, miss Granger."
        her @ cheeks blush "Huh...?" ("open", "narrow", "annoyed", "mid")
        dum1 "With hard work."
        her @ cheeks blush "That's just stupid!" ("angry", "base", "angry", "mid")
        dum2 "Miss Granger, would you mind guarding your tongue when--"

        ### TITS ###
        $ hermione.strip("robe", "accessory")
        $ hermione.strip("top", "bra")
        her "" ("annoyed", "narrow", "annoyed", "mid")
        stop music
        call ctc

        dum3 "{size=+4}!!!{/size}"
        her "Or would you rather see my pussy, sir?" ("scream", "base", "angry", "mid",emote="angry")
        her "" ("annoyed", "base", "angry", "mid")

        $ hermione.strip("bottom", "panties")
        call ctc

        with hpunch
        dum5 "{size=+7}*GHT*!!!{/size}"
        her "I am willing to do anything to get those points, sir!"

        her "And I mean {size=+9}ANYTHING!!!{/size}" ("scream", "base", "angry", "mid",emote="angry", trans=hpunch)
        call her_walk("desk", "base", reduce=0.8)
        call blkfade

        play sound "sounds/08_hop_on_desk.ogg"
        pause.7

        dum4 "Oh, dear... {heart}"
        pause 1


    play sound "sounds/win2.ogg"

    centered "{color=#cbcbcb}This concludes the original Witch Trainer ending{fast}\n\n{size=+7}-\{Thank you for playing!\}-{/size}{/color}"

    pause 2

    $ states.her.ev.yule_ball.complete = True
    $ persistent.game_complete = True
    $ persistent.gold = game.gold

    if "public" in states.her.ev.yule_ball.variant:
        $ persistent.ending_02 = True
    else:
        $ persistent.ending_01 = True

    # But wait, there's even more
    jump ending_after

label original_credits:
    play music "music/Only 115 (Electro Loop)_125 BPM.ogg" fadein 1 fadeout 1 if_changed

    centered """{cps=20}{size=+5}{color=#ea91b0}-Witch Trainer-{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}The following credits are the creators of the original game, Witch Trainer,\nand did not take part in creating, or are affiliated in any way with the Silver mod.{/color}{/size}\n\n
    {color=#e5e297}-\{Written and directed by\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Head programmer\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Artwork by\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Additional Artwork\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n
    {color=#e5e297}-\{Texts proofread and edited by\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n
    {color=#e5e297}-\{Technical advisor\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n
    {color=#e5e297}-\{Game testers\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}{#LINT_IGNORE}"""

    centered """{cps=40}
    {size=+2}{color=#e5e297}-\{CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK\}-{/color}{/size}\n\n
    {size=+5}{color=#cbcbcb}Dahr{/color}{/size}\n
    {color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}\n\n
    {size=+5}{color=#cbcbcb}Xaljio{/color}{/size}\n
    {color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n\n{/color}
    {size=+5}{color=#cbcbcb}Lyk.D9 (a.k.a. Silentchill){/color}{/size}\n
    {color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar.{/color}\n\n
    {size=+5}{color=#cbcbcb}Bookfisher{/color}{/size}\n
    {color=#e5e297}For everything.\n\n{/color}
    {size=+5}{color=#cbcbcb}The fate (universe or higher power){/color}{/size}\n
    {color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.{/color}\n\n\n
    {size=-1}{color=#cbcbcb}A whole bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n
    {color=#cbcbcb}And of course to everyone else who supports\nme and my work.{/color}{/size}{/cps}{#LINT_IGNORE}"""

    centered """{cps=70}
    {color=#cbcbcb}This is not a commercial video game. The entire project was independently founded solely through\nhttp://www.patreon.com/ and\nby \"Hentai United\" subscribers.{/color}\n\n\n
    {color=#e5e297}{size=-1}-People who supported development of this game with extraordinary amount of money-{/size}{/color}\n
    {color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}\n\n
    {size=-1}{color=#e5e297}-\"INVESTOR\" pledges-{/color}{/size}\n
    {color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}\n\n
    {size=-1}{color=#e5e297}-\"AGENT\" pledges-{/color}{/size}\n
    {color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/cps}{#LINT_IGNORE}"""

    centered """{cps=70}{size=-1}{color=#e5e297}-\"REBEL\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}\n\n{/cps}{#LINT_IGNORE}"""

    centered """{cps=70}
    {size=-1}{color=#e5e297}-\"ACTIVIST\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}\n\n
    {size=-1}{color=#e5e297}-\"SUPPORTER\" pledges-{/color}{/size}\n
    {size=-4}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MehMonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}\n\n
    {color=#e5e297}{size=-4}-\{Thank you, Joseph Antoni, for organizing all these 750+ names for me.\}-{/size}{/color}{/cps}{#LINT_IGNORE}"""

    pause 1
    call ctc
    stop music fadeout 3.0
    return
