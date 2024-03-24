label a_christmas_tale2_rewards:
    # Unlock outfit message. Should only appear once.

    if not her_outfit_ribbon.unlocked:
        call unlock_clothing(text="New clothing items for Hermione have been unlocked!", item=her_outfit_ribbon)
        call unlock_clothing(text="Several new clothing items for Hermione have been unlocked!", item=her_outfit_xmas)
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_ribbon)
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_elf)
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_xmas)

        call give_reward("Some lesser clothing items have been unlocked as well. *Ho-ho-ho!*")

    if not xmas_phoenix_ITEM.owned:
        $ xmas_phoenix_ITEM.owned = 1
        $ xmas_owl_ITEM.owned = 1
        $ xmas_fireplace_ITEM.owned = 1
        $ xmas_lights_ITEM.owned = 1
        $ xmas_wreaths_ITEM.owned = 1
        $ xmas_giftchair_ITEM.owned = 1

        call give_reward("Christmas decorations have been unlocked!", gift="interface/icons/xmas_wreaths.webp")

    return

label a_christmas_tale2():

    # Setup
    $ fireplace_OBJ.foreground = "fireplace_fire"
    $ phoenix_OBJ.decoration = xmas_phoenix_ITEM
    $ owl_OBJ.decoration = xmas_owl_ITEM
    $ fireplace_OBJ.decoration = xmas_fireplace_ITEM
    $ tonks.equip(ton_outfit_elf)
    $ hermione.equip(her_outfit_ribbon)
    $ hermione_chibi.zorder = 4
    stop weather
    $ game.daytime = False
    $ game.weather = "snow"
    call room("main_room")
    stop music fadeout 1
    call gen_chibi("hide")
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Santa's Little Helper{/color}{/size}"

    hide screen blkfade
    with d5

    play weather "sounds/wind_long_loop.ogg" fadein 2 fadeout 2
    play music "music/Anguish.ogg" fadein 1 if_changed

    show screen bld1
    with d3

    nar "T'was the night before Christmas on a cold winter night."
    nar "We see the headmaster's room, but there's no one in sight."
    nar "No sound but the wind as the storm outside roars."
    nar "But then a man enters, as he never knocks on any doors."

    call sna_walk(action="enter")
    pause 0.5
    sna "Genie I wanted--" ("snape_06", trans=d3)
    hide snape_main
    with d3
    nar "Said the man as he entered."
    call sna_walk("desk", "base")
    sna "Never here when you need him..." ("snape_01", trans=d3)
    sna "Are genies always this self-centred?" ("snape_29")
    sna "Another walk to the pub if I want to get pissed..." ("snape_06")
    sna "Another--" ("snape_04")

    hide snape_main
    hide screen bld1
    with d3

    nar "Interrupted dialogue as the room filled with mist."
    nar "With three booming ho's, Santa Claus appeared."

    play sound "sounds/fire_woosh.ogg"
    $ fireplace_OBJ.foreground = None
    stop background
    show screen genie_santa_chibi(620, 170, flip=True)
    call teleport((620+75, 440))
    call sna_chibi(flip=True)
    with d3
    sna "Genie of course... You think I'd fall for that fake beard?" ("snape_05", trans=d3)

    gen santa "I think you must be mistaken." ("base", xpos="far_left", ypos="head")
    hide snape_main
    hide screen bld1
    with d3
    nar "Said Santa to the man."
    show screen bld1
    with d3
    gen "I'm not Genie, I'm Santa!" ("base", xpos="far_left", ypos="head")
    gen "I deliver presents!" ("base", xpos="far_left", ypos="head")
    gen "That's the plan!" ("grin", xpos="far_left", ypos="head")

    gen "I bring cheers and presents, to all across the land." ("base", xpos="far_left", ypos="head")
    sna "Are you sure about that? I don't see a sack in your hand..." ("snape_01", trans=d3)
    hide snape_main
    with d3
    gen "Be patient, dear boy... Don't you give me that face." ("base", xpos="far_left", ypos="head")
    gen "Your gift will get here soon through this office fireplace." ("base", xpos="far_left", ypos="head")
    hide screen bld1
    with d3

    nar "With a big puff of smoke and a whiz and a whirl, an elf stood before them."

    show ch_ton elf zorder tonks_chibi.zorder at Transform(pos=(750, 430))
    show screen xmas_bag((750, 290))
    call teleport((680+75, 460))

    show screen bld1
    with d3
    gen "Now check out this girl!" ("grin", xpos="far_left", ypos="head")

    ton @ hair happy "" ("horny", "narrow", "base", "mid", xpos="mid", ypos="base", trans=d3)
    call ctc
    hide tonks_main
    sna "Now that is a present!" ("snape_13", trans=d3)
    sna "You've outdone yourself." ("snape_20")
    hide snape_main
    gen "That's not your present, that's my sexy helper elf..." ("base", xpos="far_left", ypos="head")

    ton @ hair happy "Eye's up here boy..." ("base", "base", "base", "mid", trans=dissolve)
    ton @ hair happy "Your present is in this sack..." ("soft", "narrow", "base", "down")
    ton @ hair horny "These milkers belong to Santa!" ("horny", "narrow", "base", "L")
    gen "They're my after-work Christmas snack!" ("grin", xpos="far_left", ypos="head")

    hide tonks_main
    hide screen bld1

    show ch_ton elf zorder tonks_chibi.zorder at Transform(pos=(750, 430), xzoom=-1)
    with d3

    nar "And with a swish of her wand his present was revealed."

    hide screen xmas_bag
    show screen xmas_bagfloor((750, 290))
    show ch_hem ribbon zorder hermione_chibi.zorder at Transform(pos=(785, 450), xzoom=1)
    #call her_chibi(xpos=750, ypos=460)
    play sound "sounds/magic4.ogg"
    with flash

    show ch_ton elf zorder tonks_chibi.zorder at Transform(pos=(750, 430), xzoom=1)
    with d3

    her @ cheeks blush "" ("soft", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    nar "In front of him a girl, no longer concealed."
    nar "With a bow around her pussy and ribbons around her tits."

    hide hermione_main
    with d3

    sna "Now that's a proper present!" ("snape_13", trans=d3)
    hide snape_main
    with d3
    gen "Now unwrap those naughty bits!" ("grin", xpos="far_left", ypos="head")

    ton @ hair happy "Wait, I just remembered, don't unwrap the present yet!" ("mad", "shocked", "base", "L", trans=dissolve)
    ton @ hair happy "If he's not been good this year, then a gift he cannot get." ("open", "closed", "shocked", "mid")
    hide tonks_main
    with d3

    gen "I'm certain he's been good... Now unwrap her, I insist!" ("grin", xpos="far_left", ypos="head")

    ton @ hair happy "I'm not so sure myself... His offences fill this list." ("upset", "narrow", "base", "down", trans=dissolve)
    hide tonks_main
    with d3

    gen "Then read it for me, elf... I'm sure it will be quick..." ("base", xpos="far_left", ypos="head")
    hide screen bld1
    with d3
    nar "The elf then unrolled it... A scroll six inches thick."

    ton @ hair happy "Inflating the points gained to put the Slytherins in the lead..." ("open", "base", "raised", "down", trans=dissolve)
    hide tonks_main
    with d3

    her "What?" ("clench", "happy", "angry", "mid", trans=dissolve)
    hide hermione_main
    with d3

    gen "That can't be true!" ("base", xpos="far_left", ypos="head")
    sna "Mere fabrications that, indeed..." ("snape_35", trans=d3)
    hide snape_main
    with d3

    ton @ hair happy "Teaching plenty of classes despite that he's blind drunk." ("upset", "base", "shocked", "down", trans=dissolve)
    sna "I can't believe they bought that it was {i}\"Essence du Skunk\"{/i}..." ("snape_45", trans=d3)
    hide snape_main
    with d3

    ton @ hair happy "Punishing students for talking in class..." ("open", "closed", "base", "mid")
    sna "They were breaking the rules!" ("snape_07", trans=d3)
    hide snape_main
    with d3

    ton @ hair happy "So is slapping their ass..." ("disgust", "narrow", "base", "mid")
    gen "Well, I'm sure they're all right... It was only a slap..." ("base", xpos="far_left", ypos="head")
    ton @ hair happy "I'm not done yet santa, there's more..." ("annoyed", "narrow", "base", "L")
    gen "What the crap..." ("base", xpos="far_left", ypos="head")

    ton @ hair happy "Stealing mounds of sweets and sniffing girls hair..." ("normal", "base", "raised", "down")
    sna "Now let's be reasonable for a minute, this list isn't fair!" ("snape_18", trans=d3)
    hide snape_main
    with d3

    gen "I think he's got a point, at least he didn't curse..." ("base", xpos="far_left", ypos="head")
    ton @ hair happy "You say that but now, is when the list is getting worse..." ("disgust", "base", "base", "mid")

    ton @ hair happy "He's bought blowjobs with house points... Now, that doesn't sound great..." ("open", "narrow", "base", "down")
    gen "A misprint I'm sure!" ("grin", xpos="far_left", ypos="head")
    ton @ hair happy "The list says thirty-eight..." ("mad", "wide", "base", "down")

    ton @ hair upset "Wrapped around his finger... This is making me sick..." ("upset", "base", "base", "down")
    ton @ hair angry "This list is massive!" ("clench", "wide", "annoyed", "down")
    gen "Then just skim it real quick..." ("base", xpos="far_left", ypos="head")

    ton @ hair happy "Taking girls books and replacing it with smut..." ("disgust", "narrow", "base", "down")
    ton @ hair happy "Then punishing them for it by spanking their butt..." ("annoyed", "narrow", "annoyed", "mid")

    sna "She had it coming I tell you... That girl was a whore..." ("snape_12", trans=d3)
    hide snape_main
    with d3

    ton @ hair disgusted "See what I mean Santa?" ("disgust", "base", "base", "L")
    ton @ hair happy "And this list has even more..." ("upset", "base", "base", "down")

    ton @ hair happy "Confiscating panties... Cumming on floors..." ("soft", "base", "annoyed", "down")
    ton @ hair disgusted "Spying in the toilets..." ("disgust", "narrow", "base", "down")
    ton @ hair happy "Never knocks on any doors..." ("open", "closed", "base", "mid")

    gen "Never knocks on any doors?!" ("base", xpos="far_left", ypos="head")
    nar "Said Santa at last."
    gen "Now that's a big offence!" ("base", xpos="far_left", ypos="head")
    ton @ hair happy "You really think so Santa?" ("annoyed", "wide", "raised", "mid")
    sna "Blast..." ("snape_11", trans=d3)
    hide snape_main
    with d3

    gen "Sexual acts is one thing... But not knocking on doors!" ("base", xpos="far_left", ypos="head")
    gen "A man without manners is what Santa Claus abhors." ("base", xpos="far_left", ypos="head")
    gen "I can't give you a gift, but I offer this advice." ("base", xpos="far_left", ypos="head")
    gen "Most things I will ignore, but good manners deem you nice." ("base", xpos="far_left", ypos="head")

    gen "Now ladies it's time to leave, it is a busy time of year..." ("base", xpos="far_left", ypos="head")
    gen "Let us empty this sack and spread my Christmas cheer." ("base", xpos="far_left", ypos="head")
    ton @ hair happy "This meeting took way too long so we better spread it quick..." ("mad", "base", "base", "L")
    ton @ hair happy "I hope I get overtime for this..." ("annoyed", "base", "base", "R")
    hide tonks_main
    with d3
    gen "I'll let you ride my magic di--" ("grin", xpos="far_left", ypos="head")

    call gen_chibi("hide")
    #call ton_chibi("hide")
    #call her_chibi("hide")
    hide ch_hem ribbon
    hide ch_ton elf
    play sound "sounds/magic4.ogg"
    show screen xmas_smoke
    with flash

    #Effect and then they're gone

    nar "Smoke then filled the room and then slowly dispersed, his present now gone..."
    sna "Santa, You're the worst..." ("snape_03", trans=d3)
    nar "With the man's final words left echoing across the halls."
    nar "He had to spend another Christmas with the bluest of blue balls..."

    call hide_characters
    with d5

    $ renpy.end_replay()

screen xmas_bag(pos):
    zorder 5
    add "images/misc/bag.webp" zoom 0.5 pos pos

screen xmas_bagfloor(pos):
    zorder 2
    add "images/misc/bag_floor.webp" zoom 0.5 pos pos

screen xmas_smoke():
    zorder 10
    add "xmas_smoke"

image xmas_smoke:
    "images/misc/smoke.webp"
    align (0.5, 0.5)
    zoom 0.55
    subpixel True

    parallel:
        linear 2.5 yoffset -10
        linear 2.5 yoffset 10
        repeat

    parallel:
        linear 5.0 xoffset 20
        linear 5.0 xoffset -20
        repeat
