

# Hermione Duel Menu

label hermione_cardgame_menu:
    if states.her.ev.cardgame.known == False:
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "Yes, [name_genie_hermione]?" ("base","base")
        gen "Are you familiar with Wizard Cards?" ("base", xpos="far_left", ypos="head")
        her "I've heard of it... it used to be a popular card game a decade or so ago." ("annoyed","squint")
        gen "So, would you like to play it?" ("grin", xpos="far_left", ypos="head")
        her "Do they even make the cards still? I don't think there's anyone in Hogsmeade stocking them." ("normal", "squint", "base", "mid")
        her "So I wouldn't be able to play against you..." ("base","base")
        her "Unless Fred and Geo..." ("clench","wide")
        gen "Unless... Who?" ("base", xpos="far_left", ypos="head")
        her "(Hermione... learn to keep your mouth shut.)" ("mad", "wide", "base", "R")
        gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="head")
        her "I'm sorry sir, I should have told you..." ("open", "base", "worried", "mid")
        her "Fred and George have a secret shop set up in the school." ("normal", "base", "worried", "R")
        gen "I see..." ("base", xpos="far_left", ypos="head")
        if item_store_intro_done:
            gen "(Probably shouldn't tell her that I already knew that...)" ("base", xpos="far_left", ypos="head")
        her "Please don't tell them I told you." ("open","happyCl")
        gen "So you say they might have some cards?" ("base", xpos="far_left", ypos="head")
        her "Wha... Yes, maybe." ("mad", "narrow", "base", "mid")
        her "You're not going to shut them down, are you?" ("angry", "squint", "base", "mid")
        gen "Why should I? It's a free market, is it not?" ("base", xpos="far_left", ypos="head")
        gen "A little bit of competition with Hoemead is good for consumers." ("grin", xpos="far_left", ypos="head")
        her "But...{w=0.3} I mean... Yes, of course." ("annoyed", "base", "worried", "mid")
        gen "So you'll play if they stock some cards?" ("base", xpos="far_left", ypos="head")
        her "I mean..." ("soft", "narrow", "base", "down")
        gen "If they don't get shut down I mean." ("base", xpos="far_left", ypos="head")
        her "Oh! Yes, of course I'll play!" ("shock","wide")
        her "..." ("soft", "wide", "worried", "stare")
        her "Anything else you needed or am I free to go?" ("base", "base", "worried", "mid")
        $ states.her.ev.cardgame.known = True
        jump hermione_requests

    elif states.her.ev.cardgame.known and states.twi.ev.cardgame.known == False:
        gen "(I should talk to Fred and George about wizard cards first.)" ("base", xpos="far_left", ypos="head")
        jump hermione_requests

    elif states.her.ev.cardgame.known and states.twi.ev.cardgame.known and not states.twi.ev.cardgame.stocked:
        gen "(I have to convince Fred and George to start stocking up cards in their shop first.)" ("base", xpos="far_left", ypos="head")
        jump hermione_requests

    elif states.twi.ev.cardgame.stock_talk and not states.her.ev.cardgame.has_cards:
        gen "Hello again [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
        her "Hello [name_genie_hermione]." ("base","base")
        gen "I wanted to thank you for mentioning the Weasley shop." ("base", xpos="far_left", ypos="head")
        her "You're not shutting them down, are you?" ("soft", "narrow", "worried", "down")
        gen "Of course not, where else am I supposed to get my supplies from?" ("base", xpos="far_left", ypos="head")
        her "Oh, yes... where." ("normal", "narrow", "base", "down")
        gen "I hope you've picked up some cards because we're playing today!" ("grin", xpos="far_left", ypos="head")
        her "Yes, I did pick up some earlier..." ("normal", "base", "base", "mid_soft")
        her "I had to go make sure that you hadn't shut them down and somehow ended up with a deck of cards." ("mad", "closed", "angry", "mid")
        gen "(Sounds like even I could learn some bartering tricks from those two.)" ("grin", xpos="far_left", ypos="head")
        gen "So, how about some practice rounds then?" ("base", xpos="far_left", ypos="head")
        her "*Ehm*... I've only recently started playing, so I'm not that good yet." ("base", "narrow", "base", "mid_soft")
        gen "Don't worry, after a few practice rounds you'll get up to speed, when you're ready, we'll play the real challenge..." ("base", xpos="far_left", ypos="head")
        $ states.her.ev.cardgame.has_cards = True
        jump hermione_duel_menu

    else:
        if geniecard_level < 2:
            label hermione_duel_menu:
            menu:
                "-First Duel-":
                    jump hermione_first_duel
                "-Second Duel-" if states.her.ev.cardgame.stage >= 1:
                    jump hermione_second_duel
                "-You need to beat the first duel-" (style="disabled") if states.her.ev.cardgame.stage < 1:
                    jump hermione_duel_menu
                "-Challenge-" if states.her.ev.cardgame.stage >= 2:
                    jump hermione_third_duel
                "-You need to beat the second duel-" (style="disabled") if states.her.ev.cardgame.stage < 2:
                    jump hermione_duel_menu
                "-Never mind-":
                    jump hermione_requests
        else:
            jump hermione_random_duel

label hermione_first_duel:
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed

    $ renpy.call_in_new_context("start_duel", her_first_deck)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    hide screen blkfade
    stop music fadeout 1

    if states.her.ev.cardgame.stage < 1:
        $ states.her.ev.cardgame.stage = 1

        her "Well, that's interesting. I was sure that my deck would've been balanced enough..." ("angry", "closed", "angry", "mid")
        gen "It's just a practice round, I'm sure you'll do better next time." ("grin", xpos="far_left", ypos="head")
        her "Your smile says otherwise." ("mad", "narrow", "angry", "R")
        gen "..." ("base", xpos="far_left", ypos="head")

    else:
        her "This game is stupid, I'm leaving!" ("angry", "closed", "angry", "mid")

    $ tokens += 1

    call her_walk(action="leave")
    jump end_hermione_event

label hermione_second_duel:
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed

    $ renpy.call_in_new_context("start_duel", her_second_deck)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    hide screen blkfade
    stop music fadeout 1

    if states.her.ev.cardgame.stage < 2:
        $ states.her.ev.cardgame.stage = 2

        her "I got 5 boosters, how isn't that enough to build a better deck than yours?" ("mad", "narrow", "annoyed", "mid")
        gen "It's more important where you place those cards..." ("base", xpos="far_left", ypos="head")
        her "I know what I'm doing..." ("open", "closed", "angry", "mid")
        gen "So, do you want to take a break?" ("grin", xpos="far_left", ypos="head")
        her "No, I'm ready..." ("soft", "narrow", "worried", "mid_soft")
        gen "You sure?" ("base", xpos="far_left", ypos="head")
        her "I said I'm ready." ("clench", "base", "angry", "mid")

        jump hermione_duel_menu
    else:
        her "This game is stupid, I'm leaving!" ("angry", "closed", "angry", "mid")

    $ tokens += 1

    call her_walk(action="leave")
    jump end_hermione_event

label hermione_third_duel:
    her "I'll make my house proud, you'll see." ("grin","happy")
    her "Wait, I should have asked for point for this." ("shock", "wide", "worried", "shocked")
    gen "Too late, here we go." ("grin", xpos="far_left", ypos="head")
    hide hermione_main
    play music "music/Juhani_Junkala.ogg" fadein 1 if_changed
    play sound "sounds/Genie_VS_Hermione4.ogg"
    show screen genie_vs_hermione
    show screen move_genie
    pause 1
    show screen versus
    pause 1
    show screen move_hermione
    pause 3
    hide screen move_genie
    hide screen move_hermione
    show screen genie_vs_hermione_smile
    with hpunch
    stop music fadeout 0
    pause
    hide screen versus
    hide screen genie_vs_hermione
    hide screen genie_vs_hermione_smile
    play music "music/vs_hermione.ogg" if_changed

    $ renpy.call_in_new_context("start_duel", her_third_deck, her_after)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if states.her.ev.cardgame.stage < 3:
        $ states.her.ev.cardgame.stage = 3

        her "Nooo, how's this even possible?" ("clench", "wide", "worried", "shocked")
        her "I'm supposed to be the smartest girl in my year..." ("mad", "wide", "worried", "stare")
        gen "Looks like Wisdom beats intelligence..." ("grin", xpos="far_left", ypos="head")
        her "You don't have to patronise me, I'll get you next time. You'll see." ("upset", "squint", "base", "mid")
        gen "You seem to have forgotten something..." ("grin", xpos="far_left", ypos="head")
        her "Fine..." ("angry", "narrow", "base", "mid_soft")
        her "Here..." ("mad", "narrow", "base", "mid_soft")

        $ unlocked_cards += [card_her_librarian]
        call give_reward("You have received a card!", "images/cardgame/t1/hermione/her_librarian_v1.webp")

        $ tokens += 3
    else:
        $ tokens += 1

    her "I'll be going now, goodbye."
    call her_walk(action="leave")
    jump end_hermione_event

label hermione_random_duel:
    gen "Ready for another game of cards?" ("base", xpos="far_left", ypos="head")

    if states.her.level < 8:
        her "You've already challenged me though..." ("open", "happy", "base", "R")
        her "and I lost." ("annoyed", "narrow", "worried", "down")
        gen "What if we made it a wager..." ("grin", xpos="far_left", ypos="head")
        her "Like gambling? No, thank you!" ("clench", "narrow", "annoyed", "mid")
        gen "It's not gambling, just a friendly house point wager..." ("base", xpos="far_left", ypos="head")
        her "Sounds like gambling to me..." ("normal", "squint", "base", "mid")
        gen "So, how about it?" ("base", xpos="far_left", ypos="head")
        her "I'll pass, [name_genie_hermione]..." ("open", "base", "worried", "R")

        gen "(Seems like she's a bit to pure minded to accept any kind of wager right now...)" ("base", xpos="far_left", ypos="head")
        jump hermione_requests
    else:
        her "You've already challenged me though..." ("open", "happy", "base", "R")
        her "and I lost." ("annoyed", "narrow", "worried", "down")
        gen "What if we made it a wager?" ("grin", xpos="far_left", ypos="head")
        her "Gambling you mean?" ("open", "base", "worried", "mid")
        gen "Not for money, obviously." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "What are you suggesting then?" ("base","happy")
        gen "Well, I was thinking house points." ("base", xpos="far_left", ypos="head")
        her "House points..." ("normal", "happy", "base", "R")
        her "How would this work then?" ("open", "happy", "base", "mid")
        gen "Well, if you win, I'll give you ten points to Gryffindor." ("base", xpos="far_left", ypos="head")
        her "Only ten?" ("annoyed", "narrow", "base", "mid_soft")
        gen "Twenty then..." ("base", xpos="far_left", ypos="head")
        her "And if I lose?" ("open", "happy", "base", "R")
        gen "I'll take the same amount away." ("base", xpos="far_left", ypos="head")
        gen "(As if she's going to let that happen...)" ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "..." ("normal","happyCl")
        her "Okay... In that case, to make it fair, let's add these extra rules..." ("open", "happy", "base", "mid_soft")

    label hermione_random_duel_rematch:

    play music "music/Juhani_Junkala.ogg" fadein 1 if_changed

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck, her_after, [5, False, False, True], random_player_deck)

    if duel_response == "Close":
        jump her_duel_cancel
    elif duel_response == "draw":
        jump her_duel_draw
    elif not duel_response == "win":
        jump her_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if states.her.ev.cardgame.stage < 4:
        $ states.her.ev.cardgame.stage = 4
        $ tokens += 3
    else:
        $ tokens += 1

    gen "Seems like I've won this one [name_hermione_genie]." ("base", xpos="far_left", ypos="head")
    her "I noticed..." ("normal", "base", "worried", "R")
    gen "You do know what this means, don't you?" ("base", xpos="far_left", ypos="head")
    her "..." ("normal", "base", "worried", "mid")
    gen "This means I'm going to have to deduct twenty points from the Gryffindor house." ("grin", xpos="far_left", ypos="head")
    her "Please, don't. I don't want the others to wake up tomorrow wondering why there are twenty house points missing..." ("open", "happyCl", "worried", "mid")
    gen "Well, in that case..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Send Hermione to work, promoting the card game-" if not states.her.ev.promote_cardgame.offered:
            $ states.her.ev.promote_cardgame.offered = True
            gen "In that case, I think I have a good idea for a job..." ("grin", xpos="far_left", ypos="head")
            her "A job?" ("open", "happy", "base", "mid")
            gen "Yes, I'd like you to start helping the twins promote the card game..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I can do that..." ("base", "base", "worried", "mid")
            her "But not today if that's okay with you." ("open", "narrow", "worried", "down")
            gen "That's fine, wouldn't want you to go there looking as defeated as you are at the moment." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "..." ("normal", "happy", "base", "R")
            her @ cheeks blush "Did you need anything else?" ("open", "base", "base", "mid_soft")
            call give_reward("Hermione can now work by helping the twins promote the card game.", "interface/icons/icon_gambler_hat.webp")
            jump hermione_requests
        "-Ask her for a blowjob instead-":
            jump hg_wager_bj
        "-Deduct the points-":
            pass

    gen "No, sorry miss Granger... Minus twenty points from Gryffindor..." ("base", xpos="far_left", ypos="head")
    her "..." ("disgust", "narrow", "worried", "down")
    her "Fine, that's fair..." ("open", "narrow", "base", "down")
    her @ cheeks blush "But I'm done playing for today..." ("normal", "happyCl", "worried", "mid")
    $ gryffindor -= 20

    call her_walk(action="leave")
    jump end_hermione_event

label her_duel_draw:
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump hermione_duel_menu
            else:
                jump hermione_random_duel_rematch
        "-Stop playing-":
            pass

    her "Okay, another time then..."

    call her_walk(action="leave")
    jump end_hermione_event

label her_duel_lost:
    stop music fadeout 1

    if geniecard_level > 1:
        her "*Hah*! Told you I could do it!"
        her "I'll take those points now."
        gen "Fine, twenty to Gryffindor." ("base", xpos="far_left", ypos="head")
        $ gryffindor += 20

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump hermione_duel_menu
            else:
                jump hermione_random_duel
        "-Be a loser-":
            pass
    her "Cards not in your favour, [name_genie_hermione]? Maybe next time..."

    call her_walk(action="leave")
    jump end_hermione_event

label her_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    her "Cards not in your favour [name_genie_hermione]? Maybe next time..."

    call her_walk(action="leave")
    jump end_hermione_event

screen genie_vs_hermione():
    zorder 15
    add "images/cardgame/VS/background_twins.webp" xalign 0.5 yalign 0.5
screen move_hermione():
    zorder 16
    add "images/cardgame/VS/hermione_01.webp" at move_in(300, 0.5)

screen genie_vs_hermione_smile():
    zorder 16
    add "images/cardgame/VS/genie_03.webp"
    add "images/cardgame/VS/hermione_02.webp"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def her_after():
        renpy.music.set_volume(0.5)
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play("sounds/card_punch%s.ogg" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        her_speech = her_speech_card[renpy.random.randint(0,len(her_speech_card)-1)]
        renpy.say(her, her_speech)
        renpy.hide_screen("hermione_main")
        renpy.music.set_volume(1.0)
        return
