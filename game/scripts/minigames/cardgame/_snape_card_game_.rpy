

# Snape Duel Menu

label snape_duel_menu:
    if geniecard_level == 1:
        if not states.sna.ev.cardgame.known:
            gen "Ever heard of Wizard Cards?" ("base", xpos="far_left", ypos="head")
            sna "What about them?" ("snape_05")
            gen "Do you have any?" ("grin", xpos="far_left", ypos="head")
            sna "I do, I collected some when I was younger... Never played though." ("snape_09")
            gen "Why not?" ("base", xpos="far_left", ypos="head")
            sna "Didn't really have anyone to play with, so I stopped buying them." ("snape_06")
            gen "Up for a game or two?" ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_03")
            sna "Why not?" ("snape_02")
            gen "What do I get if I win?" ("base", xpos="far_left", ypos="head")
            sna "What do you mean? There never used to be prizes in Wizard Cards..." ("snape_01")
            gen "What..." ("angry", xpos="far_left", ypos="head")
            gen "No wonder this game never took off..." ("base", xpos="far_left", ypos="head")
            gen "Let's just play a few practice rounds for now then." ("base", xpos="far_left", ypos="head")
            sna "And then?" ("snape_05")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "And then we'll think about prizes." ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_01")
            sna "Fine, I'm confident enough to beat a beginner." ("snape_06")
            sna "But first a bit of practice..." ("snape_02")
            gen "Let's play." ("grin", xpos="far_left", ypos="head")
            $ states.sna.ev.cardgame.known = True

        menu:
            "-First Duel-":
                jump snape_first_duel
            "-Second Duel-" if states.sna.ev.cardgame.stage >= 1:
                jump snape_second_duel
            "-You need to beat the first duel-" (style="disabled") if states.sna.ev.cardgame.stage < 1:
                jump snape_duel_menu
            "-Challenge-" if states.sna.ev.cardgame.stage >= 2:
                jump snape_third_duel
            "-You need to beat the second duel-" (style="disabled") if states.sna.ev.cardgame.stage < 2:
                jump snape_duel_menu
            "-Never mind-":
                jump snape_ready

    else:
        gen "Up for another game?" ("base", xpos="far_left", ypos="head")
        if not states.sna.ev.cardgame.wagers:
            sna "With you?"
            sna "..."

            if states.sna.level < 30:
                sna "no..." ("snape_03")
                gen "Why not?" ("angry", xpos="far_left", ypos="head")
                gen "What if we did a game as a part of a wager?" ("base", xpos="far_left", ypos="head")
                sna "A wager..." ("snape_09")
                sna "No, I have better things to do right now..." ("snape_06")
                gen "(He doesn't seem that keen, maybe I should ask again when we know each other a bit better.)" ("base", xpos="far_left", ypos="head")
                nar "Improve your relationship with Snape before trying again."
                jump snape_ready

            sna "Do you know how hard it is to progress with this game with no one to play against?" ("snape_03")
            sna "I even traded some of my potion ingredients to some weird guy in Knockturn alley for one of the old booster packs..." ("snape_01")
            sna "Turns out... That card I gave you, whilst not very powerful, it was quite rare." ("snape_08")
            gen "Sounds like a you problem." ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_29")
            gen "How about we do a wager?" ("base", xpos="far_left", ypos="head")
            sna "A wager?" ("snape_05")
            gen "Yes, how about just one token and a wager on top of that to make it interesting." ("grin", xpos="far_left", ypos="head")
            sna "..." ("snape_04")
            sna "Fine, but only if it's on equal terms..." ("snape_10")
            gen "What does that mean?" ("angry", xpos="far_left", ypos="head")
            sna "It means, you set your prize, and I'll set mine accordingly." ("snape_03")
            gen "Okay, so..." ("base", xpos="far_left", ypos="head")
            gen "If you win I'll give you some wine." ("base", xpos="far_left", ypos="head")
            sna "Don't you provide me with plenty of wine anyway?" ("snape_05")
            gen "I mean, I could stop doing it... The office has my name on it after all, and last I checked, that means whatever is in it belongs to me as well." ("base", xpos="far_left", ypos="head")
            sna "..."
            gen "In a figurative way, obviously... It doesn't actually have my name on the door." ("grin", xpos="far_left", ypos="head")
            sna "Obviously..." ("snape_03")
            gen "It's not like this office came with any of those Slytherin sluts you have yet to share with me..." ("base", xpos="far_left", ypos="head")
            sna "Fine, if that's your only proposal. If you win, then I'll give you something from my personal collection." ("snape_03")
            gen "Like what?" ("angry", xpos="far_left", ypos="head")
            sna "You'll see..." ("snape_02")
            gen "(Must be something good if he's not going to tell me...)" ("base", xpos="far_left", ypos="head")
            gen "I'm in." ("grin", xpos="far_left", ypos="head")

            $ states.sna.ev.cardgame.wagers = True
            if wine_ITEM.owned < 1:
                sna "Show me the bottle."
                gen "What?" ("base", xpos="far_left", ypos="head")
                sna "I want to see the wine first."
                gen "I don't have one, right now..." ("base", xpos="far_left", ypos="head")
                sna "That's a shame, the wager will have to wait then."
                gen "Damn..." ("base", xpos="far_left", ypos="head")
                gen "(I should see if I could find some more wine in that cupboard, or perhaps check the local store...)" ("base", xpos="far_left", ypos="head")
                jump snape_ready

        else:
            if wine_ITEM.owned < 1:
                sna "Do you have it?"
                gen "What?" ("base", xpos="far_left", ypos="head")
                sna "The wine, of course!"
                gen "I don't..." ("base", xpos="far_left", ypos="head")
                sna "That's a shame... Our wager will have to wait then."
                gen "Can't we just duel anyway? I'm not intending to lose..." ("base", xpos="far_left", ypos="head")
                sna "Neither am I."
                sna "No wine, no duel."
                gen "Damn!" ("base", xpos="far_left", ypos="head")
                gen "(I should see if I could find some more wine in that cupboard, or perhaps check the local store...)" ("base", xpos="far_left", ypos="head")
                jump snape_ready

            random:
                sna "Sure, let's do it!" ("snape_02")
                sna "You don't have to ask me twice." ("snape_02")
                block:
                    sna "Is there another bottle in it for me?" ("snape_05")
                    gen "If you win..." ("grin", xpos="far_left", ypos="head")
                    sna "Good." ("snape_02")
                    sna "Then let's begin..." ("snape_02")
                block:
                    sna "Same wager?" ("snape_05")
                    gen "Sure." ("base", xpos="far_left", ypos="head")
                    sna "Okay then..." ("snape_01")
                    sna "Let's do it." ("snape_02")
                block:
                    sna "Always!" ("snape_02")
                    sna "I'll make sure you lose this time, Genie..." ("snape_01")
                block:
                    sna "My stock is filled so why not?" ("snape_03")
                    gen "Great." ("grin", xpos="far_left", ypos="head")
                    sna "Good luck... You'll need it." ("snape_02")

                block:
                    sna "Prepare to lose!" ("snape_10")
                    gen "..." ("base", xpos="far_left", ypos="head")
                    gen "Let's just play..." ("base", xpos="far_left", ypos="head")
                block:
                    sna "I've been practising... there's no way I'll lose!" ("snape_10")
                    gen "Are you sure about that?" ("base", xpos="far_left", ypos="head")
                    sna "Yes, I came here to win..." ("snape_08")
                block:
                    sna "You're going to lose this time..." ("snape_04")
                    gen "In your dreams..." ("grin", xpos="far_left", ypos="head")
                block:
                    sna "Of course!" ("snape_02")
                    sna "But I think we should up our wager a bit..." ("snape_02")
                    gen "In what way?" ("base", xpos="far_left", ypos="head")
                    sna "I was thinking maybe you could send the Granger girl to my room tonight if I win." ("snape_20")
                    if states.her.status.public_sex or states.her.public_level >= 21:
                        gen "We'll see about that." ("base", xpos="far_left", ypos="head")
                    else:
                        gen "I doubt she would agree to that." ("base", xpos="far_left", ypos="head")
                    gen "Let's just stick to the original bet for now..." ("base", xpos="far_left", ypos="head")
                    sna "Fine..." ("snape_06")

        jump snape_random_duel

label snape_first_duel:
    sna "A bit dusty, but this should do!" ("snape_03")
    gen "You, or the deck?" ("base", xpos="far_left", ypos="head")
    sna "I...{w=0.3} The deck, obviously." ("snape_14")
    sna "Let's do this." ("snape_17")

    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed

    $ renpy.call_in_new_context("start_duel", snape_first_deck)

    if duel_response == "Close":
        jump snape_duel_cancel

    elif not duel_response == "win":
        jump snape_duel_lost

    stop music fadeout 1
    hide screen blkfade
    sna "Maybe I should've gone over the rules a bit more before trying this game again..." ("snape_05")
    sna "Well played though." ("snape_04")

    play sound "sounds/door.ogg"
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ states.sna.busy = True

    $ achievements.unlock("Cardwin")

    if states.sna.ev.cardgame.stage < 1:
        $ states.sna.ev.cardgame.stage = 1
    $ tokens += 1

    jump main_room_menu



label snape_second_duel:
    sna "That first one was just a warm-up, there's no way you'll beat me this time!" ("snape_16")
    gen "Time to get our decks out." ("grin", xpos="far_left", ypos="head")
    sna "...." ("snape_25")
    sna "Let's just play." ("snape_04")

    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed

    $ renpy.call_in_new_context("start_duel", snape_second_deck)

    if duel_response == "Close":
        jump snape_duel_cancel

    elif not duel_response == "win":
        jump snape_duel_lost

    stop music fadeout 1
    hide screen blkfade
    sna "Not again... I swear these cards used to be good when I bought them." ("snape_07")
    sna "They must've made them obsolete to get you to buy more." ("snape_04")
    sna "So deliciously mischievous." ("snape_02")

    play sound "sounds/door.ogg"
    call hide_characters
    call sna_chibi("hide")
    with d3

    if not states.her.ev.cardgame.known:
        call bld
        gen "This is awesome, I wonder if Miss Granger would want to play against me..." ("grin", xpos="far_left", ypos="head")

    $ states.sna.busy = True

    if states.sna.ev.cardgame.stage < 2:
        $ states.sna.ev.cardgame.stage = 2
    $ tokens += 1

    jump main_room_menu

label snape_third_duel:
    if not states.her.ev.cardgame.known:
        gen "(I should probably see if Hermione is interested and practise some more before challenging Snape.)" ("base", xpos="far_left", ypos="head")
        jump snape_duel_menu

    if not states.twi.ev.cardgame.stock_talk:
        gen "(I should wait for an owl from Fred and George and train with Hermione first.)" ("base", xpos="far_left", ypos="head")
        jump snape_duel_menu

    gen "So, how about that prize?" ("base", xpos="far_left", ypos="head")
    sna "Again with the prize..." ("snape_01")
    gen "I'm bored okay... and I like prizes..." ("base", xpos="far_left", ypos="head")
    sna "Fine, I challenge you!!" ("snape_10")
    gen "..." ("base", xpos="far_left", ypos="head")
    sna "You don't say it like that anymore?" ("snape_05")
    gen "No, that's lame." ("base", xpos="far_left", ypos="head")
    sna "You're not going to beat me again genie, I've practised with the greatest Wizard cards player there is!" ("snape_02")
    gen "Me?" ("base", xpos="far_left", ypos="head")
    sna "I... no, of course not." ("snape_14")
    sna "Let's do this." ("snape_17")
    sna "Show me what you got Genie... Beat me, and I'll give you a card from my collection and 3 tokens." ("snape_18")
    gen "Bring it." ("base", xpos="far_left", ypos="head")

    play music "music/Juhani_Junkala.ogg" fadein 1 if_changed
    play sound "sounds/Genie_VS_Snape.ogg"
    show screen genie_vs_snape
    show screen move_genie
    pause 1
    show screen versus
    pause 1
    show screen move_snape
    pause 2.5
    hide screen move_genie
    hide screen move_snape
    show screen genie_vs_snape_smile
    pause
    hide screen versus
    hide screen genie_vs_snape
    hide screen genie_vs_snape_smile

    $ renpy.call_in_new_context("start_duel", snape_third_deck, snape_after)

    if duel_response == "Close":
        jump snape_duel_cancel

    elif not duel_response == "win":
        jump snape_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if states.sna.ev.cardgame.stage < 3:
        sna "Impossible... There must be something wrong with my cards!" ("snape_05")
        gen "They're old, that's what." ("base", xpos="far_left", ypos="head")
        gen "Now to the prize..." ("base", xpos="far_left", ypos="head")
        sna "Fine... Here's your tokens and one of my precious cards." ("snape_05")
        sna "(You were a good card, my boy... But it's time to grow up.)" ("snape_05")
        $ states.sna.ev.cardgame.stage = 3
        $ unlocked_cards += [card_snape]
        call give_reward("You have received a special card!", "images/cardgame/t1/special/snape_v1.webp")
        $ tokens += 3
    else:
        $ tokens += 1

    play sound "sounds/door.ogg"
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ states.sna.busy = True

    jump main_room_menu

label snape_random_duel:
    play music "music/Juhani_Junkala.ogg" fadein 1 if_changed

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck, snape_after, [renpy.random.randint(0,3), False, True, False], random_player_deck)

    if duel_response == "Close":
        $ wine_ITEM.owned -= 1
        jump snape_duel_cancel
    elif duel_response == "draw":
        jump snape_duel_draw
    elif not duel_response == "win":
        $ wine_ITEM.owned -= 1
        jump snape_duel_lost

    stop music fadeout 1
    hide screen blkfade

    python:
        ingredients = [x for x in inventory.get_instances_of_type("ingredient") if x.price > 0]
        item = renpy.random.choice(ingredients)

    if states.sna.ev.cardgame.stage < 4:
        $ states.sna.ev.cardgame.stage = 4

        gen "Yes!" ("base", xpos="far_left", ypos="head")
        gen "No wine for you..." ("grin", xpos="far_left", ypos="head")
        sna "..." ("snape_04")
        gen "Now, how about that prize we discussed." ("grin", xpos="far_left", ypos="head")
        sna "Ah, yes... something from my collection." ("snape_05")

        $ item.owned += 1
        call give_reward("You've received [item.name] from Snape!", item)

        gen "What the fuck is this?" ("angry", xpos="far_left", ypos="head")
        sna "As I said..." ("snape_01")
        sna "Something from my collection..." ("snape_02")
        gen "..." ("base", xpos="far_left", ypos="head")
        sna "I'm the potions master, what did you think it was going to be?" ("snape_03")
        gen "I don't know... Like a whip or something?" ("base", xpos="far_left", ypos="head")
        sna "Hey, just because I reside in the dungeon it doesn't mean I--" ("snape_07")
        gen "I bet you do have a whip..." ("grin", xpos="far_left", ypos="head")
        sna "Well..." ("snape_12")
        gen "Whatever, I'll take it." ("base", xpos="far_left", ypos="head")

        if not states.map.snape_office.intro_e3:
            gen "Maybe I can find some use for it later..." ("base", xpos="far_left", ypos="head")

        sna "What, the whip--" ("snape_18")
        sna "*Ohh*, the potion ingredient..." ("snape_14")
        sna "There's plenty more where that came from if you want another game..." ("snape_24")
        gen "I'll think about it." ("base", xpos="far_left", ypos="head")

    else:
        random:
            block:
                gen "Another victory in the bag." ("grin", xpos="far_left", ypos="head")
                sna "I don't get it..." ("snape_03")
                sna "You must've been cheating." ("snape_04")
                gen "Skill...{w=0.3} It's called skill." ("base", xpos="far_left", ypos="head")
            block:
                sna "Not again... Did you look at my cards before the game?" ("snape_10")
                gen "How would I have done that?" ("base", xpos="far_left", ypos="head")
                sna "I don't know..." ("snape_08")
                sna "Some kind of Genie hocus-pocus?" ("snape_07")
                gen "..." ("base", xpos="far_left", ypos="head")
                sna "*Hmm*... Perhaps that comment might've been a bit..." ("snape_25")
                gen "Yeah, a just a little..." ("base", xpos="far_left", ypos="head")
                sna "I'm just going to leave this here." ("snape_14")
            block:
                gen "Sweet, another win for me!" ("grin", xpos="far_left", ypos="head")
                sna "I let you win that one..." ("snape_03")
                gen "Sure you did." ("base", xpos="far_left", ypos="head")
            block:
                sna "Damn it!" ("snape_17")
                gen "Hey, chill out... It's just a game." ("angry", xpos="far_left", ypos="head")
                sna "Just a game?!" ("snape_18")
                sna "Do you know what students from House Slytherin are known for, Genie?" ("snape_07")
                gen "Well, from what you've told me... Being massive sluts?" ("grin", xpos="far_left", ypos="head")
                sna "{size=+4}YES!{/size}" ("snape_08")
                sna "Wait... No!" ("snape_16")
                sna "We're known for being cunning..." ("snape_17")
                gen "..." ("base", xpos="far_left", ypos="head")
                sna "Cunning...{w=0.3} Genie." ("snape_18")
                gen "Yeah, I got you." ("base", xpos="far_left", ypos="head")
                gen "Hey, I could just give you another bottle..." ("base", xpos="far_left", ypos="head")
                sna "..." ("snape_12")
                sna "No... I'll beat you next time." ("snape_16")
                gen "That's the spirit." ("grin", xpos="far_left", ypos="head")
            block:
                sna "Maybe I should've gone over the rules a bit more before trying this game again..." ("snape_05")
                sna "Well played though." ("snape_04")

        $ item.owned += 1
        call give_reward("You've received [item.name] from Snape!", item)

        if not states.map.snape_office.intro_e3:
            gen "(I still don't have any use for it, but I won't turn down free shit.)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/door.ogg"
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ states.sna.busy = True
    $ tokens += 1

    jump main_room_menu



label snape_special_duel:
    play music "music/Juhani_Junkala.ogg" fadein 1 if_changed

    $ random_enemy_deck = create_random_deck(get_deck_score(playerdeck)-2, get_deck_score(playerdeck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck)

    stop music fadeout 1
    hide screen blkfade

    if duel_response == "draw":
        gen "Not another fucking--" ("angry", xpos="far_left", ypos="head")
        her "*Gltch*, *Slurp*, *Gobble*"
        gen "Draaaaaaw!" ("angry", xpos="far_left", ypos="head")
        return "draw"

    elif not duel_response == "win" or duel_response == "Close":
        sna "Well, well... It appears I've--"
        gen "{size=+4}Fuuuuuuuuck!{/size}" ("base", xpos="far_left", ypos="head")
        return "loss"

    else:
        gen "Yeeeeees!" ("grin", xpos="far_left", ypos="head")
        gen "That's it you whore! Take it!" ("angry", xpos="far_left", ypos="head")
        return "win"


label snape_duel_draw:
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump snape_duel_menu
            else:
                jump snape_random_duel
        "-Stop playing-":
            pass

    sna "Alright, another time then..."

    jump main_room_menu


label snape_duel_lost:
    hide screen blkfade
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump snape_duel_menu
            else:
                gen "I demand a rematch!" ("base", xpos="far_left", ypos="head")
                if wine_ITEM.owned < 1:
                    sna "It appears you've lost all of your bottles, maybe next time."
                    gen "You evil creature..." ("angry", xpos="far_left", ypos="head")
                    pass
                else:
                    sna "Fine."
                    sna "More wine for me!"
                    jump snape_random_duel
        "-Be a loser-":
            pass

    if geniecard_level == 1:
        sna "Cards not in your favour today? Maybe next time..."
    else: # Rub it in
        random:
            block:
                sna "Thanks for the bottle... Genie."
                gen "...." ("angry", xpos="far_left", ypos="head")
            block:
                gen "..." ("base", xpos="far_left", ypos="head")
                gen "Good game..." ("base", xpos="far_left", ypos="head")
                sna "Forgetting something?"
                gen "Fine, here's your bottle..." ("base", xpos="far_left", ypos="head")
            block:
                sna "Another win for me..." ("snape_02")
                gen "And your last..." ("base", xpos="far_left", ypos="head")
                sna "Sorry, can't hear you over the sound of my victory." ("snape_01")
                gen "..." ("base", xpos="far_left", ypos="head")
            block:
                sna "Child's play..." ("snape_02")
                gen "I'm thousands of years old, you know..." ("base", xpos="far_left", ypos="head")
                sna "And I beat you..." ("snape_02")
                gen "That just shows how luck based the game is, honestly..." ("base", xpos="far_left", ypos="head")
            block:
                sna "..." ("snape_02")
                gen "Just take your prize and go." ("base", xpos="far_left", ypos="head")
            block:
                sna "Nice one..." ("snape_02")
                gen "Hey, don't be a bad winner." ("base", xpos="far_left", ypos="head")
                sna "Hey, I was just--" ("snape_03")
                sna "I see what you're doing..." ("snape_04")
                sna "I'll have that wine now..." ("snape_02")
            block:
                sna "Hah!"
                sna "I mean...{w=0.3} Good game."
                gen "You're allowed to show enthusiasm, you know..." ("base", xpos="far_left", ypos="head")
                sna "I know, but it's bad for my image..."
                gen "..." ("base", xpos="far_left", ypos="head")
                gen "Whatever you say, here's your bottle." ("base", xpos="far_left", ypos="head")

    play sound "sounds/door.ogg"
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ states.sna.busy = True

    jump main_room_menu


label snape_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    hide screen blkfade
    with dissolve

    if geniecard_level == 1:
        sna "Cards not in your favour today? Maybe next time..."
    else:
        sna "In that case, it's a forfeit."
        sna "I'll take that wine now."
        gen "Wait a minute..." ("base", xpos="far_left", ypos="head")
        sna "I don't make the rules, I just play by them."
        gen "Fine..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/door.ogg"
    call hide_characters
    call sna_chibi("hide")
    with d3

    $ states.sna.busy = True

    jump main_room_menu



screen genie_vs_snape():
    zorder 16
    add "images/cardgame/VS/background_snape.webp" xalign 0.5 yalign 0.5
screen move_genie():
    zorder 16
    add "images/cardgame/VS/genie_01.webp" at move_in(-300, 0.5)
screen versus():
    zorder 15
    add "images/cardgame/VS/vs.webp"
screen move_snape():
    zorder 16
    add "images/cardgame/VS/snape_01.webp" at move_in(300, 0.5)

screen genie_vs_snape_smile():
    zorder 16
    add "images/cardgame/VS/genie_02.webp"
    add "images/cardgame/VS/snape_02.webp"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def snape_after():
        renpy.music.set_volume(0.5)
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play("sounds/card_punch%s.ogg" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        renpy.say(sna,snape_speech_card[renpy.random.randint(0,len(snape_speech_card)-1)])
        renpy.music.set_volume(1.0)
        return

    # Unused?
    # def snape_after_special():
    #     renpy.call("sna_main", "It's my time to shine, I'm counting on an explosive victory.", face="snape_02")
    #     renpy.call("her_main", "*Slurp*, *Slurp*, *Gobble*")
    #     renpy.say(g4, "*Ngh*... Not on my watch... I'll do my best to prevent any unwarranted explosions during the current circumstance...")
    #     renpy.call("sna_main", "Now you're talking! Usually I'm the one doing all the trash talk...", face="snape_28")
    #     renpy.say(m, "I feel like today especially it's important to keep the conversation going...")
    #     renpy.call("her_main", "*Gltch*, *Slurp*, *Gobble*")
    #     renpy.say(g4, "...")
    #     renpy.call("sna_main", "Great, I can't wait to see your face as I destroy you...", face="snape_22")
    #     renpy.say(m, "Surely you'd know by now I'm not the kind of person to lose--")
    #     renpy.call("her_main", "*Slurp*, *Slurp*, *Gobble*")
    #     renpy.say(g4, "My composure that easily...")
    #     renpy.call("sna_main", "I'll make you bust this time for sure... I can already taste victory...", face="snape_21")
    #     renpy.say(m, "That's not the only thing that someone will be tasting in a second...")
    #     return
