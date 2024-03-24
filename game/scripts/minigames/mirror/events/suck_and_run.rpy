label suck_and_run_rewards:
    # Unlock outfit message. Should only appear once.
    if not ton_outfit_succubus.unlocked:
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_succubus)
    return

# Mirror story: Suck and Run
label suck_and_run:

    with d5
    centered "{size=+7}{color=#cbcbcb}Suck & Run{/color}{/size}"

    label .choices:

    # Setup
    $ tonks.equip(ton_outfit_default)
    $ game.daytime = False
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    menu:
        "For the best experience it is recommended to play the story in chronological order."
        "-Part one-":
            $ pathvalue = 0
        "-Part two-":
            $ pathvalue = 1
        "-Part three-":
            $ pathvalue = 2
        "-Return-":
            $ renpy.end_replay()

    stop music fadeout 1.0
    pause 1.0

    if pathvalue == 0:
        call music_block

        call setup_fireplace_hangout(char="snape")

        sna "*Ah*... I've been looking forward to this..." ("snape_23", ypos="head")
        gen "Rough day, I take it?" ("base", xpos="far_left", ypos="head")
        sna "Bloody slackers, all of them!" ("snape_17")
        gen "..." ("angry", xpos="far_left", ypos="head")
        sna "What's the point of me teaching them anything if they can't even bother staying awake?" ("snape_32")
        gen "Are we talking about your Slytherin sluts again?" ("base", xpos="far_left", ypos="head")
        gen "Surely that's on you if anything." ("base", xpos="far_left", ypos="head")
        gen "Maybe you need to spice things up a bit." ("base", xpos="far_left", ypos="head")
        sna "What? No! I'm perfectly capable in that capacity!" ("snape_04")
        sna "... Unless you've heard something?" ("snape_03")
        sna "No, these students in particular are some Hufflepuff boys." ("snape_16")
        sna "Now they're lazy at the best of times, but catching someone sleeping in my class... That's a first." ("snape_07")
        sna "I wish I could hang them up by their ankles, like in the old days! That would show them!" ("snape_08")
        gen "Come on, man... It's Halloween!" ("base", xpos="far_left", ypos="head")
        gen "Cheer up a little, will you?" ("base", xpos="far_left", ypos="head")
        sna "*Mmm*... The time of year when girls will put on any type of outfit with the word \"slutty\" written in front of it." ("snape_23")
        gen "Exactly!" ("grin", xpos="far_left", ypos="head")
        sna "Wait a minute..." ("snape_01")
        sna "Do genies even celebrate Holidays?" ("snape_04")
        sna "I'd think the novelty of it would wear off rather quickly." ("snape_01")
        gen "You kidding me?" ("base", xpos="far_left", ypos="head")
        gen "The time these Holiday celebrations have been around has been but a blip of my entire existence." ("base", xpos="far_left", ypos="head")
        gen "I was around when they burnt your kind at the stake... And that wasn't even that long ago to me." ("base", xpos="far_left", ypos="head")
        sna "Right..." ("snape_31")
        gen "Besides... Nightmare before Christmas is like my favourite Halloween movie..." ("base", xpos="far_left", ypos="head")
        sna "*Uhm*... What?" ("snape_05") # Snape doesn't know what a movie is
        gen "Christmas movie... Whatever." ("base", xpos="far_left", ypos="head")
        sna "You're such a mystery to me sometimes, Genie..." ("snape_06")
        gen "Come on, you must have seen it! At least heard of it." ("angry", xpos="far_left", ypos="head")
        sna "I'm afraid I have not seen this Nightmare {i}moo-wee{/i} thing." ("snape_09")
        gen "Okay, so there's this guy... Jack Skellington, and he's the \"Pumpkin King\" of Halloween Town." ("base", xpos="far_left", ypos="head")
        gen "Which kind of makes him the boss of the place. Only there's a mayor. Look, I don't know enough about the politics." ("base", xpos="far_left", ypos="head")
        gen "Anyway... He decides he wants to be Santa Claus, so he kidnaps him in order to take over his position." ("base", xpos="far_left", ypos="head")
        gen "Only then the Americans shoot him down and Jack has to release Santa in order to save Christmas." ("base", xpos="far_left", ypos="head")
        sna "..." ("snape_03")
        gen "Actually, maybe it is a Christmas movie after all..." ("base", xpos="far_left", ypos="head")
        sna "..." ("snape_04")
        gen "Yeah, you're right... In that case, Die Hard would easily take the top spot." ("base", xpos="far_left", ypos="head")
        gen "Now that I think of it, the villain kind of looks like--" ("base", xpos="far_left", ypos="head")
        sna "Die... Hard?" ("snape_05")
        gen "Don't you dare tell me it's not A Christmas movie!" ("base", xpos="far_left", ypos="head")
        sna "Whatever it is you're on about sounds dreadfully boring." ("snape_03")

        nar "You and Snape continue drinking long into the night. You exchange tales of the skimpiest outfits you've seen girls wearing, and the issues with sticking your dick in crazy."

        show screen blkfade with d3
        stop music fadeout 1.0
        hide screen with_snape

        centered "{size=+7}{color=#cbcbcb}End of part one{/color}{/size}"

        jump suck_and_run.choices

    elif pathvalue == 1:
        play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed

        call setup_fireplace_hangout(char="tonks")

        call bld
        gen "Getting into the Halloween spirit?" ("base", xpos="far_left", ypos="head")
        ton "Of course!" ("grin", "wide", "base", "mid", xpos="base", ypos="head", flip=False)
        ton "I've been looking forward to the Halloween feast ever since I got here." ("crooked_smile", "closed", "base", "mid")
        ton "Brings back memories." ("base", "base", "base", "downR")
        gen "*Ha-hah*, yeah... That food thing that I do all the time. Love it!" ("base", xpos="far_left", ypos="head")
        ton "It also gives me a great excuse to dress down!" ("base", "happyCl", "base", "mid")
        gen "Don't you mean dress up?" ("base", xpos="far_left", ypos="head")
        ton "Same thing..." ("horny", "narrow", "base", "mid")
        gen "So, what will it be this year then?" ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Why don't you have a guess..." ("crooked_smile", "base", "base", "mid")

        menu:
            "\"A Slutty Nurse?\"":
                ton "Ohhh... that'd be fun. Do you have a fever?" ("horny", "wink", "base", "mid")
                ton "I could take your temperature." ("grin", "narrow", "raised", "mid")
                ton "Orally, of course." ("soft", "narrow", "shocked", "mid")
                gen "You naughty--" ("grin", xpos="far_left", ypos="head")
                gen "Wait, what do you mean about that exactly?" ("angry", xpos="far_left", ypos="head")
                ton "Wouldn't you like to know..." ("soft", "base", "raised", "downR")
                ton "But no, that's not it..." ("base", "narrow", "base", "mid")
            "\"A Slutty School girl?\"":
                ton "Someone's getting greedy." ("base", "narrow", "base", "mid")
                ton "Don't you have enough of those already?" ("horny", "base", "raised", "mid")
                gen "Never." ("base", xpos="far_left", ypos="head")
            "\"A Slutty Witch?\"":
                ton "Isn't that just my normal clothing?" ("soft", "base", "base", "down")
                gen "That's true..." ("base", xpos="far_left", ypos="head")

        gen "So... What is it, then?" ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Not sure I should ruin the surprise." ("horny", "wink", "base", "mid")
        ton @ hair horny "I'm sure you'll find out soon enough..." ("base", "narrow", "base", "R") #Glance #hornyhair
        gen "Looking forward to it." ("grin", xpos="far_left", ypos="head")
        ton "Anyway..." ("open", "base", "shocked", "mid")
        ton "Anything else going on that I should know of?" ("soft", "base", "base", "mid")
        gen "*Err*... I had a little chat with Severus the other night." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*... Not really the kind of thing I was talking about..." ("annoyed", "base", "base", "mid")
        ton "Although I'm always up for gossip." ("crooked_smile", "narrow", "shocked", "mid")
        ton "I assume you weren't talking about Halloween... Since I doubt Snape would care about it in the slightest." ("open", "narrow", "base", "mid")
        gen "Oh no, he absolutely loves it." ("base", xpos="far_left", ypos="head")
        ton "Really?" ("disgust", "wide", "shocked", "mid")
        ton "Well... Colour me surprised..." ("open", "closed", "base", "mid")
        gen "Yes... He seemed quite eager to find out what the girls will be wearing this year in fact." ("base", xpos="far_left", ypos="head")
        ton "Oh, so it's like that, is it?" ("base", "narrow", "raised", "mid")
        gen "He also mentioned that some Hufflepuff boys have been falling asleep during his lessons... What do you think--" ("base", xpos="far_left", ypos="head")
        ton @ cheeks heavy_blush hair horny "What?! Why do you think I'd know anything about Hufflepuff boys falling asleep in class!?" ("silly", "happyCl", "worried", "mid")
        ton @ cheeks blush hair horny "Are you implying that I'm sneaking into their room to fuck them? That I'm draining their cocks dry every night!?" ("scream", "base", "angry", "mid")
        gen "What? I was just going to ask if you thought they'd been staying up late partying or something." ("base", xpos="far_left", ypos="head")
        ton @ cheeks blush hair horny "Oh... No, I don't think they're doing anything like that." ("soft", "base", "base", "R")
        gen "What was that about sucking them dry at night?" ("base", xpos="far_left", ypos="head")
        ton @ cheeks blush hair horny "Did I say that? Are you sure you didn't just hear what you wanted to hear, Genie?" ("disgust", "narrow", "base", "mid")
        gen "I'm pretty sure I heard you ask if I thought you were fucking your students at night." ("base", xpos="far_left", ypos="head")
        ton @ hair horny "Then you must've misheard me..." ("normal", "closed", "base", "mid")
        gen "... Are you drooling?" ("base", xpos="far_left", ypos="head")
        ton "*Mhmm*?" ("normal", "wide", "base", "down")
        ton "Oh, this?" ("mad", "base", "raised", "mid")
        ton "I was just thinking about what I'll be having for dinner tonight..." ("soft", "closed", "base", "R")
        ton @ cheeks blush hair horny "Creamy mushroom soup... Delicious!" ("horny", "narrow", "shocked", "up")
        gen "I see...{w=0.3} Very well." ("base", xpos="far_left", ypos="head")
        gen "Please keep an eye on those Hufflepuff boys, alright?" ("base", xpos="far_left", ypos="head")
        ton "Of course.... I'll make sure to inspect their dorms thoroughly." ("open", "closed", "base", "mid")
        ton "I'll even give them a little pat down. Make sure they're not smuggling alcohol up there." ("grin", "narrow", "base", "mid")
        ton "Maybe a strip search or two." ("soft", "narrow", "base", "mid") #drooling ahegao face
        gen "I don't think that will be necessary." ("base", xpos="far_left", ypos="head")
        gen "Just make sure they're not staying up all night, alright?" ("base", xpos="far_left", ypos="head")
        ton "*Aww*, You're no fun at all." ("annoyed", "narrow", "base", "mid") #pout
        gen "*glares*" ("base", xpos="far_left", ypos="head")
        ton "*Sigh* Fiiiiiine... Goodnight [name_genie_tonks]." ("annoyed", "base", "base", "mid")
        gen "Goodnight [name_tonks_genie]." ("base", xpos="far_left", ypos="head")

        show screen blkfade with d3
        stop music fadeout 1.0
        hide screen with_tonks_animated

        centered "{size=+7}{color=#cbcbcb}End of part two{/color}{/size}"

        jump suck_and_run.choices

    elif pathvalue == 2:
        hide screen bld1

        call gen_chibi("sit_behind_desk")
        play music "sounds/night.ogg" fadein 1 if_changed # Intentional, because background channel is already preoccupied

        hide screen blkfade
        with d5

        play sound "sounds/snore1.ogg"
        gen "*Snore*...{w=0.4}" ("base", xpos="far_left", ypos="head")

        call ton_walk(action="enter")
        call chibi_emote("exclaim", "tonks")
        pause 1.0
        call ton_walk("desk", "base")
        call chibi_emote("hearts", "tonks")
        pause 0.5

        #Black screen
        show screen blkfade
        with d3

        pause 1.5
        play sound "sounds/zipper.ogg"
        pause 0.5
        play sound "sounds/giggle2_loud.ogg"
        pause 1.0

        call ton_chibi_scene("bj_desk")
        hide screen blkfade
        with d9

        pause 1.0
        play background "sounds/slickloop.ogg" fadein 2
        "*Slurp* *Slurp* *Slurp*"
        gen "*Mmm*...{w=0.3} Yes...{w=0.3} That's it, princess...{w=0.4} *Snore*..." ("base", xpos="far_left", ypos="head")
        "*Slurp* *Slurp* *Gulp*"
        gen "*Nghh*...{w=0.3} I'm almost...{w=0.3} There...{w=0.4} Princess." ("base", xpos="far_left", ypos="head")
        "*Slurp* *Slurp* *Gulp*"
        gen "*Snore*... *Sn--*" ("base", xpos="far_left", ypos="head")
        gen "Princess--" ("base", xpos="far_left", ypos="head")
        call ton_chibi_scene("bj_desk_shocked")
        gen "Tonks?!" ("open", xpos="far_left", ypos="head")

        play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
        ton "*Slurp* *Slurp* *Gulp*!" ("open_wide_tongue", "narrow", "shocked", "stare", xpos="far_right", ypos=200, trans=d3) # Explicit positions to avoid hiding the doll

        call ton_chibi_scene("bj_desk")
        gen "am I still dreaming?" ("angry", xpos="far_left", ypos="head")
        ton "*Slurp* *Slurp* *slurp*!" ("open_wide_tongue", "narrow", "shocked", "stare")
        gen "*Ngh*... But it feels so real!" ("angry", xpos="far_left", ypos="head")
        stop background
        ton @ hair angry "..." ("base", "closed", "annoyed", "up") #Hair turns red
        call ton_chibi_scene("bj_desk_shocked")
        gen "*Ah*... T-Tonks?!" ("base", xpos="far_left", ypos="head")

        stop music fadeout 0.5
        ton "" ("base", "narrow", "base", "mid", xpos="mid", ypos="base")
        with fade
        pause .5

        play sound "sounds/magic3.ogg"
        $ tonks.equip(ton_outfit_succubus)
        ton "" ("horny", "narrow", "base", "mid", trans=flash)

        pause 0.8
        play sound "sounds/giggle2_loud.ogg"
        ton "*Giggles*"

        play music "music/determined_pursuit_loop.ogg" if_changed
        hide tonks_main
        with d3
        pause .5

        gen "*ARGH*!" ("angry", xpos="far_left", ypos="head")
        play sound "sounds/punch01.ogg"
        with vpunch
        gen "Unhand me, foul demon!" ("angry", xpos="far_left", ypos="head")
        ton @ hair angry "Of course, Sir..." ("grin", "base", "base", "L", ypos="head", flip=False)
        play sound "sounds/giggle2_loud.ogg"
        pause .8
        ton @ hair angry "Right away, Sir..." ("crooked_smile", "base", "angry", "mid")
        ton @ hair angry "Once I've gotten what I want..." ("soft", "narrow", "shocked", "up")

        gen "You may not have my life essence, you foul--" ("angry", xpos="far_left", ypos="head")


        stop music fadeout 1.0
        ton @ hair angry "" ("horny", "base", "angry", "mid")
        play sound "sounds/spit.ogg"
        pause 1
        gen "Temptress?" ("angry", xpos="far_left", ypos="head")
        play sound "sounds/giggle2_loud.ogg"
        ton @ hair angry "*Giggles*" ("grin", "base", "angry", "up")
        ton @ hair angry "Just close your eyes and relax..." ("normal", "narrow", "angry", "stare")
        call ton_chibi_scene("bj_desk")
        gen "*Ehm*..." ("base", xpos="far_left", ypos="head")
        gen "So you don't want my soul?" ("base", xpos="far_left", ypos="head")
        ton @ cheeks blush hair angry "Me? Want a soul as tainted and corrupt as yours?" ("silly", "happyCl", "shocked", "stare")
        ton @ hair angry "Don't make me laugh..." ("normal", "base", "angry", "mid")
        gen "Then what do you--" ("base", xpos="far_left", ypos="head")
        ton @ hair angry "{heart}" ("soft", "narrow", "base", "up")
        gen "I see..." ("base", xpos="far_left", ypos="head")
        ton @ hair angry "Now just relax and enjoy it...{heart}" ("horny", "narrow", "base", "mid")
        gen "Well I guess that could be arranged..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/giggle2_loud.ogg"
        pause 1
        gen "Excellent..." ("base", xpos="far_left", ypos="head")
        play background "sounds/slickloopfast.ogg" fadein 2
        ton @ hair angry "*Slurp* *Slurp* *slurp*!" ("open_wide_tongue", "narrow", "base", "up")
        gen "*Argh*!" ("angry", xpos="far_left", ypos="head")
        gen "So...{w=0.4} *Ah*... What is it, then?" ("angry", xpos="far_left", ypos="head")
        ton @ hair angry "*Slurp*?" ("open_wide_tongue", "base", "base", "mid")
        gen "What kind of foul creature am I dealing with?" ("base", xpos="far_left", ypos="head")
        ton @ hair angry "*Slurp*?" ("open_wide_tongue", "base", "raised", "mid")
        gen "Oh! Let me guess!" ("base", xpos="far_left", ypos="head")
        gen "Are you a--" ("base", xpos="far_left", ypos="head")

        play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed

        stop background
        ton @ hair angry "A succubus?" ("crooked_smile", "base", "angry", "mid")
        gen "*Argh*... You're no fun, I was just about to--" ("base", xpos="far_left", ypos="head")
        play background "sounds/slickloopveryfast.ogg" fadein 2
        ton @ cheeks blush hair horny "*Slurp* *Slurp* *Slurp*" ("open_wide_tongue2", "narrow", "base", "up")
        gen "*Nghh*...{w=0.4} To..." ("base", xpos="far_left", ypos="head")
        ton @ cheeks blush "*Slurp*! *Slurp*! *Slurp*!" ("open_wide_tongue2", "closed", "base", "up")
        gen "Cum down your throat!" ("base", xpos="far_left", ypos="head")
        ton @ cheeks blush "*Slurp* *Slurp* *Slurp*" ("open_wide_tongue", "happyCl", "shocked", "mid")
        gen "You asked for it!" ("angry", xpos="far_left", ypos="head")
        gen "Take this, foul demon!" ("angry", xpos="far_left", ypos="head") #large text?
        stop background
        play sound "sounds/slick_02.ogg"
        ton @ cheeks blush "*mmhf*!" ("open_wide_tongue", "wide", "shocked", "mid")

        with hpunch

        gen "May the seed of an immortal--" ("angry", xpos="far_left", ypos="head") #large text?
        play sound "sounds/slick_02.ogg"
        ton "*Mmm*! *Gulp* *Gulp*" ("open_wide_tongue", "shocked", "shocked", "stare")

        with hpunch

        gen "Quench your lust filled desires!" ("base", xpos="far_left", ypos="head")
        play sound "sounds/slick_02.ogg"
        ton @ cheeks blush "*Gulp*...{w=0.4} *Gulp*...{w=0.6} *Gulp*" ("open_wide_tongue", "happyCl", "shocked", "mid")
        ton @ cheeks blush "*Ah*..." ("open_wide_tongue_cum", "base", "base", "down")
        play sound "sounds/gulp.ogg"
        ton @ cheeks blush "*Gulp*..." ("normal", "closed", "base", "mid")
        ton @ cheeks blush "Now that hit the--" ("grin", "base", "base", "mid")

        play sound "sounds/magic3.ogg"
        $ tonks.equip(ton_outfit_default)
        with flash

        ton "Spot..." ("open", "closed", "base", "mid")
        gen "..." ("grin", xpos="far_left", ypos="head")
        ton "Hey!" ("clench", "wide", "base", "down")
        ton "How did you do that?" ("clench", "wide", "base", "mid")
        gen "Do what?" ("base", xpos="far_left", ypos="head")
        ton "My form changed..." ("disgust", "narrow", "base", "down")
        gen "Nice, It worked!" ("grin", xpos="far_left", ypos="head")
        gen "My seed actually did quench your--" ("grin", xpos="far_left", ypos="head")
        ton "You idiot!" ("open", "wide", "angry", "mid")
        gen "What?!" ("angry", xpos="far_left", ypos="head")
        ton "Halloween is the only time I can get away with this..." ("clench", "base", "annoyed", "down")
        ton @ hair sad "And now you've ruined it!" ("annoyed", "closed", "worried", "mid")
        gen "Surely it is not my fault that my semen contains such immeasurable--" ("base", xpos="far_left", ypos="head")
        ton @ hair sad "..." ("annoyed", "narrow", "base", "down") #sad
        gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
        gen "So... A Succubus... *eh*?" ("base", xpos="far_left", ypos="head")
        ton @ hair sad "Obviously..." ("open", "narrow", "shocked", "downR")
        gen "A sexual deviant that can't hold in their own desires..." ("base", xpos="far_left", ypos="head")
        gen "Not sure why I didn't figure it out sooner..." ("grin", xpos="far_left", ypos="head")
        ton "Don't you dare tell anybody..." ("annoyed", "base", "annoyed", "mid")
        gen "Tell anybody that there's a lust filled creature hiding in plain sight?" ("base", xpos="far_left", ypos="head")
        gen "Who are we talking about again?" ("grin", xpos="far_left", ypos="head")
        play sound "sounds/giggle2_loud.ogg"
        ton "*Giggles*" ("base", "happyCl", "base", "mid")

        show screen blkfade with d3
        stop music fadeout 1.0

        centered "{size=+7}{color=#cbcbcb}End of part three{/color}{/size}"

        jump suck_and_run.choices
