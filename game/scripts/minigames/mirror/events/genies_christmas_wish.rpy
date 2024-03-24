label genies_christmas_wish_rewards:

    if not her_outfit_reindeer.unlocked:
        call unlock_clothing(text="New clothing items for Hermione have been unlocked!", item=her_outfit_reindeer)
        call unlock_clothing(text="New clothing items for Cho have been unlocked!", item=cho_outfit_reindeer)
        call unlock_clothing(text="New clothing items for Luna have been unlocked!", item=lun_outfit_reindeer)
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_santa)

        python:
            naughty_list_ITEM.owned = 1
            xmas_garland_ITEM.owned = 1
            xmas_window_santa_ITEM.owned = 1

        call give_reward(text=">You have received a bunch of new room decorations!", gift="interface/icons/santas_naughty_list.webp")

    return

label genies_christmas_wish:

    # Setup

    #TODO Add decorations

    $ fireplace_OBJ.foreground = "fireplace_fire"
    $ window_OBJ.decoration = xmas_window_santa_ITEM
    $ chandelier_OBJ.decoration = xmas_garland_ITEM
    $ poster_OBJ.decoration = naughty_list_ITEM
    $ hermione.equip(her_outfit_reindeer)
    $ cho.equip(cho_outfit_reindeer)
    $ luna.equip(lun_outfit_reindeer)
    $ tonks.equip(ton_outfit_santa)

    stop weather
    $ game.daytime = False
    $ game.weather = "snow"
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Genie's Christmas Wish{/color}{/size}"

    hide screen blkfade
    with d5

    play weather "sounds/wind_long_loop.ogg" fadein 2 fadeout 2
    play music "music/Anguish.ogg" fadein 1 if_changed

    nar "It was the season of giving, in the world of sluts and magic."
    nar "But the genie was alone."
    nar "It sure was sad and tragic."

    nar "Everyone was gone, as they had left for the holidays."
    nar "No one left to see him wank, and to receive his cum on their face."

    nar "No one left to drink with, not a single hole to fuck."
    nar "Not even a sex doll, no hoovers to provide some suck."

    nar "No teachers, no students, not even an elf."
    gen "I wish I had that talent... Where you can suck off oneself." ("base", xpos="far_left", ypos="head")

    nar "Sure, why not! A voice said."
    nar "That's easy enough to do! It's Christmas after all, I'll make your wish come true."

    gen "What?! My wish?!" ("angry", xpos="far_left", ypos="head")
    gen "No, that's not what I want!" ("angry", xpos="far_left", ypos="head")
    nar "Yelled the genie, and the wish spell came to a sudden halt."

    nar "So the voice then asked him if they had understood him wrong."
    nar "Is this not what you wished for... To suck your own mighty schlong?"

    gen "Of course not, don't be stupid." ("base", xpos="far_left", ypos="head")
    gen "I was merely following the rhyme." ("base", xpos="far_left", ypos="head")
    gen "If what I truly wanted came true, this world would be cut in twine." ("base", xpos="far_left", ypos="head")

    gen "Such as all men being gone! And for the women to be by my side!" ("base", xpos="far_left", ypos="head")
    nar "Is this what you want?"
    gen "No, just let me think..." ("base", xpos="far_left", ypos="head")
    nar "I guess I'll wait until you decide..."

    gen "Make all women into sluts!" ("grin", xpos="far_left", ypos="head")
    nar "Your wish will now be real!"
    gen "No, wait!" ("angry", xpos="far_left", ypos="head")
    nar "Not again..."
    gen "I didn't consider, how that would make me feel..." ("base", xpos="far_left", ypos="head")

    gen "If they were already slutty... Then what left is there for me to do?" ("base", xpos="far_left", ypos="head")
    gen "The journey is just as important, as the act of woo-hoo!" ("base", xpos="far_left", ypos="head")

    nar "Are all genies this indecisive?"
    gen "Just give me a moment to think..." ("base", xpos="far_left", ypos="head")
    nar "I've got places to be, you know."
    gen "Quit stirring up a stink." ("base", xpos="far_left", ypos="head")

    gen "You know what... I yield." ("base", xpos="far_left", ypos="head")
    nar "What?"
    gen "You heard what I said." ("base", xpos="far_left", ypos="head")
    nar "You don't want a wish?"
    gen "Knowing me, it would surely end up with me dead." ("base", xpos="far_left", ypos="head")

    nar "But I have to grant you something. Or I have to stay here forever."
    gen "Someone immortal to keep me company!" ("base", xpos="far_left", ypos="head")
    nar "Now aren't you clever..."

    nar "Is there nothing else that you want?"
    gen "I wish for you to pick." ("base", xpos="far_left", ypos="head")
    nar "Yeah, yeah, very funny... Don't be such a dick."

    gen "Did I stutter, go on then. Pick the wish for me." ("base", xpos="far_left", ypos="head")
    nar "Wait, you're serious?"
    gen "As serious as I'll ever be." ("base", xpos="far_left", ypos="head")

    nar "Alright then, let me think..."
    gen "Not so easy now, is it?" ("base", xpos="far_left", ypos="head")
    gen "Just pick whatever, I don't care. At least I had someone visit." ("base", xpos="far_left", ypos="head")

    nar "I know what you need!"
    nar "Just close your eyes for a bit."
    gen "I ain't falling for that." ("base", xpos="far_left", ypos="head")
    nar "Close your eyes, you little shit."

    gen "You're not my dad." ("base", xpos="far_left", ypos="head")
    nar "Genie said, but he still followed the command."
    gen "No I'm not!" ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d3
    play sound "sounds/woosh.ogg"

    nar "His eyes now shut, as they had been sprayed by magic sand."

    gen "My eyes!" ("open", xpos="far_left", ypos="head")
    nar "He yelled loudly... His vision now impaired."
    gen "This better not be permanent!" ("angry", xpos="far_left", ypos="head")
    nar "He said, his tone sounding a bit scared."


    $ luna_chibi.zorder = 1
    $ hermione_chibi.zorder = 2
    $ cho_chibi.zorder = 3
    call lun_chibi("stand", 490, 420)
    call her_chibi("stand", 510, 440)
    call cho_chibi("stand", 530, 460)

    hide screen blkfade
    with d3

    nar "But his vision then returned, and he was greeted by some new outlines."
    nar "Three women in his office, and they were looking mighty fine."

    cho "How did I get here?" ("angry", "wide", "base", "stare", xpos="mid", ypos="base", trans=d5)
    nar "Said one."
    cho "" ("annoyed", "base", "base", "R")
    her "I was just with my mum and dad." ("mad", "base", "base", "stare", xpos=500, ypos="base", trans=d5)
    nar "Said the second, sounding confused, and a bit sad."

    her "" ("annoyed", "base", "base", "R")
    lun "Now what is this outfit?" ("soft", "base", "base", "down", xpos="base", ypos="base", trans=d5)
    nar "Said the third... While checking out the fit."
    her "" ("angry", "base", "base", "down")
    cho "" ("clench", "base", "base", "down")
    lun "" ("soft", "base", "base", "mid")
    nar "Then she looked up at genie, who was finding it hard... to admit."

    nar "Should he lie, or be truthful?"
    nar "What on earth should he say?"
    nar "When the truth sounds so unlike him."
    nar "That he felt alone this Christmas day."

    her "" ("annoyed", "base", "base", "mid")
    cho "" ("normal", "base", "base", "mid")
    gen "I can explain!" ("open", xpos="far_left", ypos="head")
    nar "Said the genie, in a stuttering voice."
    gen "There was this magic thing... Like a ghost!" ("angry", xpos="far_left", ypos="head")

    gen "I swear I didn't have a choice!" ("angry", xpos="far_left", ypos="head")

    her "" ("disgust", "narrow", "base", "mid")
    lun "" ("annoyed", "base", "base", "mid")
    cho "" ("angry", "narrow", "angry", "mid")
    nar "The expressions on the women changed to angry and displeased."
    nar "As they were in the middle of celebrations, the middle of their Christmas feast!"

    her "" ("open", "narrow", "angry", "mid")
    lun "" ("open", "base", "worried", "mid")
    cho "" ("open", "narrow", "angry", "mid")
    nar "They then opened their mouths to give him a piece of their mind."
    nar "But then the voice showed their presence, and answered their concerns in kind."

    her "" ("angry", "base", "base", "R")
    lun "" ("soft", "base", "base", "L")
    cho "" ("clench", "narrow", "base", "L")
    nar "You see your headmaster was lonely... it is Christmas after all."
    nar "And I felt his heart aching, so I answered his call."

    her "" ("soft", "base", "base", "mid")
    lun "" ("soft", "base", "base", "mid")
    cho "" ("open", "narrow", "base", "mid")
    nar "A wish I then bestowed, so he would not have to feel so grim."
    nar "But he could not clear his mind, and had me choose for him."

    nar "As it's the season to celebrate, with the ones you love the most--"
    gen "Love is a strong word." ("base", xpos="far_left", ypos="head")
    cho "Don't mind him... Now, tell us the wish, ghost." ("smile", "base", "base", "mid")

    nar "I brought you three to him, well, a copy of you all at least."
    nar "The other one is still at home, enjoying a Christmas feast."

    nar "The gift I give to you, is not having to choose."
    her "" ("open", "base", "base", "stare")
    lun "" ("grin", "base", "base", "mid")
    nar "Once Christmas is finally over, no memories you will lose."

    nar "The ones you make at home, the ones you make at school."
    nar "Both will be intact..."
    nar "Now, isn't that cool?"

    cho "A copy of us at home, while we can have sex over here?" ("grin", "narrow", "base", "mid")
    her "For how long will it last?" ("grin", "narrow", "base", "mid")
    nar "Let's make it the end of the year."

    lun "Are you crying, sir?" ("open", "base", "worried", "mid")
    nar "One of them asked, as a tear escaped genie's eye."
    gen "A Christmas filled with sex... Now that is enough, to make a grown man cry." ("base", xpos="far_left", ypos="head")

    gen santa "The End!" ("grin", xpos="far_left", ypos="head")

    show screen blkfade
    with d4

    pause .8
    call hide_characters

    hide screen blkfade

    play sound "sounds/door_down.ogg"
    with hpunch

    stop music fadeout 1

    call ton_chibi("stand", 810, 440)

    ton "I've detected some foreign magic--" ("clench", "wide", "base", "mid", xpos="base", ypos="base", trans=d5)
    ton @ hair horny "Oh, hello girls! Back already?" ("grin", "wide", "base", "L")

    gen "Wait, you were here the whole time?!" ("angry", xpos="far_left", ypos="head")

    show screen blkfade
    with d4

    nar "The end."

    cho "Why was I even in this story? We don't even celebrate Christmas at my home." ("open", "base", "base", "mid")
    gen "*Err*..." ("open", xpos="far_left", ypos="head")

    gen "Happy Holidays!" ("smile", xpos="far_left", ypos="head")

    $ renpy.end_replay()
