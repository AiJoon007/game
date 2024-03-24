label a_christmas_tale_rewards:
    if not card_exist(unlocked_cards, card_santa):
        call give_reward("You have received a special card as a gift!", "images/cardgame/t1/special/santa_v1.webp")
        $ unlocked_cards += [card_santa]

    if not xmas_phoenix_ITEM.owned:
        $ xmas_phoenix_ITEM.owned = 1
        $ xmas_owl_ITEM.owned = 1
        $ xmas_fireplace_ITEM.owned = 1
        $ xmas_lights_ITEM.owned = 1
        $ xmas_wreaths_ITEM.owned = 1
        $ xmas_giftchair_ITEM.owned = 1

        call give_reward("Christmas decorations have been unlocked!", gift="interface/icons/xmas_wreaths.webp")

    return

label a_christmas_tale:

    # Setup
    $ fireplace_OBJ.foreground = "fireplace_fire"
    $ phoenix_OBJ.decoration = xmas_phoenix_ITEM
    $ owl_OBJ.decoration = xmas_owl_ITEM
    $ fireplace_OBJ.decoration = xmas_fireplace_ITEM
    stop weather
    $ game.daytime = False
    $ game.weather = "snow"
    call room("main_room")
    stop music fadeout 1
    call gen_chibi("hide")
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}A Christmas tale{/color}{/size}"

    hide screen blkfade
    with d5

    play music "music/Anguish.ogg" fadein 1 if_changed
    show screen bld1
    with d3
    nar "It was the night before Christmas, with excitement at the school."
    nar "But the headmaster's room empty, now where is that fool?"
    nar "The stockings were hung by the chimney with care."
    nar "But no genie to be found. As if he'd never been there."
    hide screen bld1
    with d3
    pause.8

    play sound "sounds/door.ogg"
    call sna_chibi("stand","door","base")
    with d5
    pause.8

    show screen bld1
    with d3
    nar "Severus then entered, all flustered and spent."

    call sna_walk("mid", "base")
    pause.2

    sna "Genie? Where are you... I came here, to vent..." (face="snape_03", ypos="head")
    nar "He wondered if the genie had found a way home..."
    sna "Seems like a normal Christmas, spent all alone..." (face="snape_06")

    nar "But then a crash and a bang from the chimney was heard."
    play sound "sounds/kick.ogg"

    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.2

    sna "What the fuck was that, some kind of bird?" (face="snape_14")
    nar "With a snap and a crackle, and a strong blinding light."

    play sound "sounds/kick.ogg"
    $ fireplace_OBJ.foreground = None
    # Teleport Santa Genie into the fireplace
    show screen genie_santa_chibi(620, 150)
    call teleport((620+75, 420))
    pause.8

    nar "A figure appeared, in the most silent of nights."
    pause.2

    # Turn around
    show screen genie_santa_chibi(620, 150, True)
    with d3
    pause.2

    show screen bld1
    with d3
    gen santa "Oh hello there my friend." ("base", xpos="far_left", ypos="head")
    nar "Said the figure at last."
    gen "I thought you might be here, but where's that genie?" ("base", xpos="far_left", ypos="head")
    sna "..." (face="snape_25")
    gen "Blast..." ("base", xpos="far_left", ypos="head")

    sna "Genie..." (face="snape_24")
    nar "Said the teacher."
    sna "You're not fooling me." (face="snape_24")
    sna "Have you been drinking again?" (face="snape_25")
    sna "And I don't mean drinking tea." (face="snape_29")

    gen "I don't know what you mean." ("base", xpos="far_left", ypos="head")
    nar "Said the large bearded man..."
    gen "I'm Santa, of course." ("grin", xpos="far_left", ypos="head")
    gen "I bring presents..." ("grin", xpos="far_left", ypos="head")
    gen "That's the plan!" ("grin", xpos="far_left", ypos="head")
    pause.8

    nar "After silence and confusion, then Severus said..."
    sna "Well, just get it over with, so I can go back to bed." (face="snape_09")
    gen "Now boy where's your spirit, it's Christmas is it not?" ("base", xpos="far_left", ypos="head")
    sna "Now genie, look here..." (face="snape_24")
    nar "But then he froze on the spot."

    hide screen bld1
    # Teleport away
    call gen_chibi("hide")
    call teleport((620+75, 420))
    with d3
    pause.5

    show screen bld1
    with d3
    nar "The man had then vanished, without even a trace..."
    hide screen bld1
    with d3

    pause.2
    call sna_chibi("stand","mid","base",flip=False)
    with d3
    pause.5
    call sna_chibi("stand","mid","base",flip=True)
    with d3
    pause.8

    sna "I thought he couldn't use magic..." (face="snape_05")
    nar "You should've seen the look on Snape's face."
    hide screen bld1
    with d3

    call sna_chibi("hide")
    with d3
    call sna_chibi("stand",570,190+250,flip=True)
    with d3
    pause.5

    show screen bld1
    with d3
    nar "With only a gift left where he had stood, should he open or should he wait?"
    sna "My first present since childhood..." (face="snape_04")
    nar "As he peeled back the wrapping, he just stood there in shock."
    sna "Where on earth did he get this?" (face="snape_03")
    nar "Then suddenly..."
    play sound "sounds/knocking.ogg"
    nar "A knock."

    "Snape, are you in there, I think I lost my keys."
    sna "The door is open, you fool." (face="snape_08", xpos="base", ypos="base")
    nar "His voice... now just a wheeze."

    play sound "sounds/knocking.ogg"
    nar "The genie knocked again. The mutter, he hadn't heard."
    sna "" (face="snape_06")
    nar "Now Snape saying nothing, not even a word."
    show screen snape_picture_frame
    with d5
    nar "A picture we then see as it's our time to depart."
    sna "" (face="snape_23")
    nar "As sadness turned to joy in the cold teacher's heart."
    call ctc

    hide screen snape_picture_frame
    hide snape_main
    with d5
    pause.8

    gen "Happy Holidays." ("grin", xpos="far_left", ypos="head")

    show screen blkfade
    with d9
    pause 2

    $ renpy.end_replay()

# Screen with Genie dressed as Santa (only used in Christmas tale)
screen genie_santa_chibi(x, y, flip=False):
    tag genie_chibi
    zorder 2
    add "characters/misc/santa/santa_chibi.webp" pos (x,y) zoom 0.5 xzoom (-1 if flip else 1)

screen snape_picture_frame():
    add "characters/snape/main/picture_frame.webp" xpos states.sna.image.xpos ypos states.sna.image.ypos xzoom states.sna.image.xzoom zoom 0.5 xoffset -50
    zorder states.sna.image.zorder+1
