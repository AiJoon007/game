
# Mirror story: The not so great escape
#Office night

label not_so_great_escape_rewards:
    if not ton_outfit_police.unlocked:
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_police)
        call unlock_clothing(text="New clothing items for Cho have been unlocked!", item=cho_outfit_police)
        call unlock_clothing(text="New clothing items for Luna have been unlocked!", item=lun_outfit_police)

        $ halloween_rug_ITEM.owned = 1
        $ halloween_chandelier_ITEM.owned = 1
        $ halloween_fireplace2_ITEM.owned = 1
        $ halloween_window_monster.owned = 1
        $ halloween_cupboard_caskets.owned = 1
        $ halloween_chair_caskets.owned = 1
        $ halloween_bat_trophy_ITEM.owned = 1
        $ halloween_lampL_ITEM.owned = 1
        $ halloween_lampR_ITEM.owned = 1

        call give_reward(text=">You have received a bunch of new room decorations!", gift="interface/icons/halloween_chandelier.webp")
    return

label not_so_great_escape:

    # Setup
    $ tonks.equip(ton_outfit_police)
    $ cho.equip(cho_outfit_police)
    $ luna.equip(lun_outfit_police)
    $ game.daytime = False
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    $ halloween_rug_ITEM.owned = 1
    $ halloween_chandelier_ITEM.owned = 1
    $ halloween_fireplace2_ITEM.owned = 1
    $ halloween_window_monster.owned = 1
    $ halloween_cupboard_caskets.owned = 1
    $ halloween_chair_caskets.owned = 1
    $ halloween_bat_trophy_ITEM.owned = 1
    $ halloween_lampL_ITEM.owned = 1
    $ halloween_lampR_ITEM.owned = 1

    $ halloween_rug_ITEM.use()
    $ halloween_chandelier_ITEM.use()
    $ halloween_fireplace2_ITEM.use()
    $ halloween_window_monster.use()
    $ halloween_cupboard_caskets.use()
    $ halloween_chair_caskets.use()
    $ halloween_bat_trophy_ITEM.use()
    $ halloween_lampL_ITEM.use()
    $ halloween_lampR_ITEM.use()

    $ candleL_OBJ.get_action()()
    $ candleR_OBJ.get_action()()

    centered "{size=+7}{color=#cbcbcb}A not so great escape{/color}{/size}"

    hide screen blkfade
    with d5

    call music_block

    call bld
    play sound "sounds/snore1.ogg"
    gen "*Snore*{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    pause 1.0
    play sound "sounds/snore3.ogg"
    gen "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    pause 1.0
    play sound "sounds/snore2.ogg"
    gen "......{w=0.5}*Snore*{w=1.0}{nw}" ("base", xpos="far_left", ypos="head")
    stop music fadeout 6.0

    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"

    play sound "sounds/snore1.ogg"
    gen "*Snore*{w=2.0}{nw}" ("base", xpos="far_left", ypos="head")
    pause 1.0

    "Commanding Voice" "This is Ministry of Magic Enforcement Division, please open the door."

    play sound "sounds/knocking_loud.ogg"
    "*knock-knock-knock*"

    play sound "sounds/snore1.ogg"
    pause .4
    stop sound fadeout 6.0
    gen "Zzzz... W--{w=0.3} what?" ("base", xpos="far_left", ypos="head")

    "Commanding Voice" "{size=+4}Police! Open the door this instant!{/size}"

    play music "music/Hitman.ogg" fadein 1 fadeout 1 if_changed
    gen "(The fuzz!)" ("angry", xpos="far_left", ypos="head")
    gen "(What do I do?!)" ("angry", xpos="far_left", ypos="head")

    play sound "sounds/knocking_loud.ogg"
    "Commanding Voice" "{size=+4}Open the door or we'll have to bring it down!{/size}"

    call gen_chibi("stand", 210, "base")
    call gen_walk(230, 470, speed=2.0)
    gen "(Oh Fuck-fuck-fuck!)" ("angry", xpos="far_left", ypos="head")

    call gen_walk(380, 470, speed=2.0)

    gen "(Shit-shit-SHIT!)" ("angry", xpos="far_left", ypos="head")

    call gen_walk(420, "base", speed=2.0)
    pause 0.5
    call gen_chibi(flip=False)
    with d3

    gen "(Where do I--{w=0.3} The window!)" ("angry", xpos="far_left", ypos="head")
    gen "(Wait, I'd die if I jumped from up here.)" ("angry", xpos="far_left", ypos="head")

    "Commanding Voice" "{size=+4}Take the door down, girls!{/size}"

    play sound "sounds/door_down.ogg"
    with hpunch

    pause 0.3

    call gen_chibi(flip=True)
    with d3

    gen "(Crap, they're knocking the door down!)" ("angry", xpos="far_left", ypos="head")


    call chibi_emote("exclaim", "genie")
    pause 0.5
    call chibi_emote("hide", "genie")

    gen "(The fireplace! No... I'll ruin my robes.)" ("angry", xpos="far_left", ypos="head")

    play sound "sounds/door_down.ogg"
    with hpunch

    "Commanding Voice" "Come on girls, you can do better than this!"
    "Another Voice" "This door must have some sort of protective enchantment on it!"
    "Commanding Voice" "Don't be silly, let me show you how it's done!"
    play sound "sounds/gulp.ogg"

    gen "..." ("base", xpos="far_left", ypos="head")
    gen "(I suppose there isn't much choice...)" ("base", xpos="far_left", ypos="head")

    call gen_walk(565, "base")
    call gen_chibi("stand_alt")
    with d3

    pause 0.5

    call gen_chibi("hide")
    show screen blkfade
    with d3

    play sound "sounds/cloth_sound3.ogg"
    nar "You crawl up the chimney's shaft..."

    gen "(Shit, I can't see a thing...)" ("base", xpos="far_left", ypos="head")
    gen "(Hold on, I'm immortal... Why didn't I just jump out the--)" ("angry", xpos="far_left", ypos="head")

    "Commanding Voice" "One last push, we're almost in!"

    play sound "sounds/door_down.ogg"
    with hpunch

    stop music fadeout 1

    pause 2

    hide screen blkfade
    with d3

    #Tonks, Luna and Cho enters in police costumes. Tonks stands next to fireplace looking left. The other two next to her.

    $ luna_chibi.zorder = 1
    $ tonks_chibi.zorder = 2
    $ cho_chibi.zorder = 3
    call lun_chibi("stand", 790, 420)
    call ton_chibi("stand", 810, 440)
    call cho_chibi("stand", 830, 460)
    with d3

    play background "sounds/wind_long_loop.ogg" fadein 2 fadeout 2

    $ name_cho_genie = "Officer Cho?"
    $ name_tonks_genie = "Officer Tonks?"
    $ name_luna_genie = "Officer Luna?"

    call cho_walk("right", 460, speed=1.5)

    cho "Put your hands where I can--" ("scream", "base", "base", "mid", xpos="mid", ypos="base", trans=d5)

    call chibi_emote("thought", "cho")
    cho "...?" ("mad", "base", "base", "mid")
    call chibi_emote("hide", "cho")

    hide cho_main
    with d3

    call cho_chibi(flip=True)
    with d3

    cho @ cheeks blush "Miss! He's gone!" ("angry", "base", "base", "mid", flip=True, trans=d3)
    ton "Yes, I can see that rookie..." ("open", "narrow", "base", "L", xpos=500, ypos="base", trans=d5)

    call ton_walk("mid", "base")
    call cho_chibi(flip=False)
    with d3

    lun "Then where is he Miss? Is he invisible?" ("angry", "base", "raised", "mid", xpos="base", ypos="base", trans=d5)

    play sound "sounds/crunch.ogg"
    "*Rustle*" #Sound from fireplace
    gen "(Oh fuck, my foot almost slipped!)" ("angry", xpos="far_left", ypos="head")

    call chibi_emote("exclaim", "cho")
    pause 0.3
    call chibi_emote("hide", "cho")
    # Skyrim reference

    call cho_chibi(flip=True)
    with d3
    cho "What was that?" ("soft", "base", "base", "mid", xpos=500, ypos="base", trans=d5)
    lun "Huh?" ("mad", "narrow", "base", "L")
    cho "Never mind, must have been the wind..." ("annoyed", "base", "base", "mid")
    #

    call ton_chibi(flip=True)
    with d3
    ton "*Hmm*..." ("soft", "narrow", "raised", "L", xpos="mid", ypos="base", flip=True, trans=d5)

    call lun_walk(620, 420)
    call cho_chibi(flip=False)
    with d3
    call lun_walk("desk", 420)

    cho "What are you doing, waving your arms like that?" ("disgust", "base", "base", "mid", xpos="base", ypos="base", flip=False, trans=d5)

    call lun_chibi(flip=True)
    with d3

    lun "If I can't see him then I'll have to search for him some other way!" ("mad", "base", "base", "L", xpos="mid", ypos="base", flip=True, trans=d5)
    cho "*Sigh*..." ("disgust", "base", "base", "mid")
    ton "Well he's here somewhere, that's for sure." ("base", "narrow", "base", "L", xpos=500, ypos="base", trans=d5)
    cho "Really?" ("angry", "base", "base", "mid")
    gen "(How does she know?)" ("angry", xpos="far_left", ypos="head")
    cho "How do you know, miss?" ("angry", "base", "base", "mid")
    gen "(That's my line!)" ("angry", xpos="far_left", ypos="head")

    hide tonks_main
    with d3

    call ton_chibi(flip=False)
    with d3
    ton "Why don't you help your partner to search the place?" ("open", "base", "base", "R", xpos=450, ypos="base", flip=False, trans=d5)

    ton "I'm sure the chief would be really happy if we brought that scumbag in." ("soft", "base", "base", "R")
    gen "(Now that's just rude...)" ("base", xpos="far_left", ypos="head")
    cho "Oh! Of course, miss! We'll find him!" ("mad", "base", "base", "mid")

    call cho_walk("desk_close", 460)

    stop background
    show screen blkfade
    with d3

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    $ luna_chibi.zorder = 3
    $ cho_chibi.zorder = 1
    call lun_chibi("stand", 240, 460, flip=True)
    call cho_chibi("stand", 760, 420)

    hide screen blkfade
    with d3

    play background "sounds/wind_long_loop.ogg" fadein 2 fadeout 2

    cho "Where the hell is he?" ("angry", "base", "base", "mid", trans=d5)
    lun "Miss... We've been searching for hours... I'm starting to get tired." ("disgust", "narrow", "base", "L", trans=d5)
    gen "({b}You're{/b} starting to get tired? Huh?)" ("angry", xpos="far_left", ypos="head")
    cho "Are you sure he's still in here, miss?" ("upset", "base", "base", "mid")
    ton "Giving up already?" ("open", "narrow", "raised", "mid", trans=d5)
    lun @ cheeks blush "" ("upset", "base", "base", "down")
    cho @ cheeks blush "" ("annoyed", "base", "base", "mid")
    call ctc
    ton "Very well then..." ("upset", "closed", "base", "mid")
    gen "(Finally...)" ("base", xpos="far_left", ypos="head")
    ton "{w=0.6}{nw}" ("grin", "base", "base", "mid")

    play sound "sounds/punch01.ogg"
    pause .5

    play sound "sounds/door_down.ogg"
    with hpunch

    show screen blkfade
    with d3

    play sound "sounds/falling_stairs.ogg"

    call ton_chibi(flip=True)
    call hide_characters
    call lun_chibi("stand", 440, 460, flip=True)
    call cho_chibi("stand", 690, 420)
    call gen_chibi("stand", 585, "base", flip=False)
    pause 2

    hide screen blkfade
    with d3

    gen "Bloody hell!" ("angry", xpos="far_left", ypos="head")

    lun "Wow! Was he in there this entire time?" ("angry", "wide", "base", "mid", trans=d5)
    cho @ cheeks blush "How did you know, miss?" ("mad", "base", "base", "mid", trans=d5)
    ton "Years of experience, girls... You'll get there some day..." ("base", "wink", "base", "mid", xpos=500, ypos="base", flip=True, trans=d5)
    ton "Now... Time to put this filth where it belongs..." ("mad", "narrow", "annoyed", "mid")
    gen "No, wait!" ("angry", xpos="far_left", ypos="head")

    stop music fadeout 4
    stop background fadeout 3
    play sound "sounds/level_failed.ogg"
    show screen cartoon_zoom
    gen "...{w=6.0}{nw}" ("angry", xpos="far_left", ypos="head")
    show screen blkfade
    with d3
    call ton_chibi("hide")
    call cho_chibi("hide")
    call lun_chibi("hide")

    # pre-sets expressions for later #
    lun @ cheeks blush "" ("soft", "narrow", "base", "mid", xpos=400, ypos="base", flip=False)
    cho @ cheeks blush "" ("smile", "base", "base", "mid")
    ton "" ("grin", "base", "base", "mid", xpos=500, ypos="base", flip=False)

    # Hides decorations
    $ halloween_rug_ITEM.use()
    $ halloween_chandelier_ITEM.use()
    $ halloween_fireplace2_ITEM.use()
    $ halloween_window_monster.use()
    $ halloween_cupboard_caskets.use()
    $ halloween_chair_caskets.use()
    $ halloween_bat_trophy_ITEM.use()
    $ halloween_lampL_ITEM.use()
    $ halloween_lampR_ITEM.use()

    $ candleL_OBJ.get_action()()
    $ candleR_OBJ.get_action()()

    call hide_characters
    call gen_chibi("sit_behind_desk")
    call gameover(fake=True)

    stop music fadeout 1
    $ game.daytime = True

    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"

    play sound "sounds/snore1.ogg"
    gen "zzz... No... I swear, I had no sexual relations..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/snore2.ogg"
    gen "zzz... With that woman..." ("base", xpos="far_left", ypos="head")

    "Another Female Voice" "Maybe he isn't in..."
    "Commanding Voice" "Don't be silly, when does he ever leave the office?"
    "Another Female Voice" "That's true..."

    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"

    play sound "sounds/snore2.ogg"
    gen "zzz...." ("base", xpos="far_left", ypos="head")

    "Another Female Voice" "*Hmm*... Perhaps he's sleeping."
    "Yet Another Female Voice" "Aww... But I really wanted him to see our Halloween costumes..."
    "Commanding Voice" "Don't worry girls, I know how to deal with this..."

    play sound "sounds/knocking_loud.ogg"
    "*knock-knock-knock*"

    play sound "sounds/snore1.ogg"
    pause .4
    stop sound fadeout 6.0
    gen "zzz-- W-- What the..." ("base", xpos="far_left", ypos="head")

    femv "Hold on, the door's open."

    play music "music/Hitman.ogg" fadein 1 fadeout 1 if_changed
    gen "(No, this can't be happening AGAIN!)" ("angry", xpos="far_left", ypos="head")

    play sound "sounds/door.ogg"
    $ luna_chibi.zorder = 1
    $ tonks_chibi.zorder = 2
    $ cho_chibi.zorder = 3
    $ luna.zorder = 14
    $ cho.zorder = 15
    $ tonks.zorder = 16
    call lun_chibi("stand", 790, 420)
    call ton_chibi("stand", 810, 440)
    call cho_chibi("stand", 830, 460)
    with d3

    pause 0.3

    play sound "sounds/MaleGasp.ogg"
    call gen_chibi("stand", 210, "base")
    with d3

    gen "Oh shit!" ("angry", xpos="far_left", ypos="head")

    lun "" (trans=d3)
    cho "" (trans=d3)
    ton "" (trans=d3)
    with d5

    ton "Looks like someone's been a naughty boy!" ("grin", "base", "base", "mid")


    play sound "sounds/magic4.ogg"
    call gen_chibi("stand", 370, 295)
    call teleport(position="genie", effect=False)

    stop music fadeout 3
    gen "You'll never catch me alive!" ("angry", xpos="far_left", ypos="head")
    cho "" ("angry", "base", "base", "up")
    lun "" ("clench", "base", "base", "up")
    ton "What are you--" ("clench", "base", "base", "up")


    play sound "sounds/boing05.ogg"
    call gen_chibi("hide")
    with d3

    pause 1
    play sound "sounds/falling.ogg"

    pause 2.0

    play sound "sounds/gasp.ogg"
    lun "" ("disgust", "base", "base", "R")
    ton "" ("normal", "closed", "base", "R")
    cho "Did he just jump out the window?!" ("mad", "base", "base", "mid")
    ton "Appears so..." ("open", "closed", "base", "mid")
    cho @ cheeks blush "Is he okay?" ("angry", "base", "base", "mid")
    lun "Did he not like our Halloween costumes?" ("annoyed", "base", "worried", "down")
    cho "" ("disgust", "base", "base", "mid")
    ton "" ("disgust", "narrow", "base", "L")
    call ctc
    lun "" ("annoyed", "base", "worried", "R")
    call ctc
    lun "Oh... I mean, Is he okay?!" ("angry", "wide", "base", "R")

    call ton_walk(415, 400, speed=1.2)

    nar "Tonks leans over the window and sees Genie lying face down in a rose bush."

    gen "Bloody hell..." ("angry", xpos="far_left", ypos="head")
    ton "*Sigh*... He'll be fine..." ("soft", "closed", "base", "mid", xpos="mid", ypos="base", trans=d5)

    call blkfade
    centered "{size=+10}{color=#cbcbcb}Happy Halloween!{/color}{/size}"

    $ renpy.end_replay()
