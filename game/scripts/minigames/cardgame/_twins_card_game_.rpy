label twins_first_duel:
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.ogg" fadein 1 if_changed

    $ renpy.call_in_new_context("start_duel", twins_first_deck)

    if duel_response == "Close":
        jump twins_duel_cancel
    elif not duel_response == "win":
        jump twins_duel_lost

    hide screen blkfade
    stop music fadeout 1

    if states.twi.ev.cardgame.stage < 1:
        twi "No way!"
        ger "You must've been cheating."
        gen "It's all in the cards, boys." ("base", xpos="far_left", ypos="head")
        ger "I can certainly see that..."
        ger "Are you thinking what I'm thinking Fred?"
        fre "I believe I am, George!"
        fre "If the cards you have play such a big role..."
        ger "You'd need to buy more and more just to stay competitive."
        fre "And we..."
        twi "We'll be rich!"
        gen "So you'll stock some then?" ("base", xpos="far_left", ypos="head")
        ger "Absolutely!"
        ger "We'll send you an owl when we've set things up."
        fre "So you better get ready for a rematch!"
        twi "Because we'll win next time!"
        gen "We'll see about that... I can't have students going around showing up to their headmaster, can I?" ("base", xpos="far_left", ypos="head")
        
        $ states.twi.ev.cardgame.stage = 1
        $ letter_cards_store.send()
        pass
    else:
        twi "Not again..."
        gen "Tough luck boys." ("base", xpos="far_left", ypos="head")
        pass

    "You return to your office."

    $ tokens += 1

    jump main_room

label twins_second_duel:
    if states.twi.ev.cardgame.stocked == False:
        gen "(I need to wait for an owl from them before we can duel again)" ("base", xpos="far_left", ypos="head")
        jump twins_duel_menu

    fre "Good luck."
    ger "You'll need it."

    play music "music/vs_twins.ogg" fadein 1.0 if_changed
    play sound "sounds/Genie_VS_Twins_Teleport.ogg"
    show screen genie_vs_twins
    show screen move_genie
    pause 1
    show screen move_twins
    pause 3.5
    hide screen move_twins
    hide screen move_genie
    show screen genie_vs_twins_smile
    with flash
    pause
    hide screen genie_vs_twins_smile
    hide screen genie_vs_twins

    $ renpy.call_in_new_context("start_duel", twins_second_deck, twins_after)

    if duel_response == "Close":
        jump twins_duel_cancel

    elif  not duel_response == "win":
        jump twins_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if states.twi.ev.cardgame.stage < 2:
        fre "I feel like we should have foreseen this."
        ger "I blame Trelawney on this, she said that luck would be on our side today..."
        fre "Well... A promise is a promise."
        fre "Here's your reward."
        ger "And we also heard about your wins against Snape, so here are some extra tokens."
        fre "Make sure to come back and spend those tokens in our token shop."
        $ card_rand_twins = renpy.random.choice([[card_fred, "fred"], [card_george, "george"]])
        $ unlocked_cards += [card_rand_twins[0]]
        call give_reward("You have received a special card!", "images/cardgame/t1/special/%s_v1.webp" % str(card_rand_twins[1]))
        $ states.twi.ev.cardgame.stage = 2
        $ tokens += 3
    else:
        twi "Not again..."
        gen "Tough luck boys." ("base", xpos="far_left", ypos="head")
        $ tokens += 1

    "You return to your office."
    jump main_room

label twins_random_duel:
    if states.twi.ev.cardgame.first_random:
        $ states.twi.ev.cardgame.first_random = False
        gen "How about another game?" ("base", xpos="far_left", ypos="head")
        twi "Sure, why not?"
        fre "But let's make it a bit interesting."
        gen "I was going to suggest something similar but go on..." ("base", xpos="far_left", ypos="head")
        ger "Let's make a wager."
        gen "Interesting... So, what kind of wager are you boys suggesting?" ("base", xpos="far_left", ypos="head")
        ger "How about a monetary one?"
        gen "Of course, what else is there in this world other than monetary rewards?" ("base", xpos="far_left", ypos="head")
        twi "Exactly!"
        ger "Okay, how about..."
        ger "If you win then we'll give you a cut from our weekly profits."
        gen "That confident, are we?" ("base", xpos="far_left", ypos="head")
        twi "Always!"
        gen "Well, if it's a monetary reward you're looking for..." ("base", xpos="far_left", ypos="head")
        gen "Then how about if I lose, I'll give you ten gold?" ("base", xpos="far_left", ypos="head")
        ger "Let me just do some maths real quick."
        ger "..."
        ger "... Carry the one..."
        gen "Finished?" ("base", xpos="far_left", ypos="head")
        ger "Just a second..."
        ger "Done!"
        if game.gold < 10:
            ger "Unfortunately we will have to refuse."
            gen "Why?" ("angry", xpos="far_left", ypos="head")
            fre "{size=-2}The further extension to fractional values of your current income in the first instance on the establishment of a method of algebraical evolution which bears the same relation to arithmetical evolution that algebraical division bears to arithmetical division gives unsatisfactory results.{/size}"
            gen "........... what?" ("base", xpos="far_left", ypos="head")
            ger "It means you're broke, sir."
            fre "Come back with your offer when you have more gold, professor."
            gen "Fine..." ("base", xpos="far_left", ypos="head")
            "You return to your office."
            jump main_room
        ger "Yes, that is quite satisfactory..."
        fre "This deal is only until we leave Hogwarts by the way..."
        gen "Obviously..." ("base", xpos="far_left", ypos="head")
        fre "Just making sure that we have all grounds covered."
        gen "Let's begin then..." ("base", xpos="far_left", ypos="head")
    elif states.twi.ev.cardgame.profit == 0.2:
        gen "Ready for another wager?" ("base", xpos="far_left", ypos="head")
        ger "No, I think we've had quite enough of a dent in our profit margin..."
        fre "We're almost halfway to where we were before we introduced the card game."
        gen "Only half?" ("angry", xpos="far_left", ypos="head")
        ger "Yes, we still need to think about growth."
        gen "(I should've asked for a cut to begin with.)" ("base", xpos="far_left", ypos="head")
        gen "(Well, hopefully if I can get Miss Granger to help them promote their shop I'll see some more profit that week...)" ("base", xpos="far_left", ypos="head")
        jump twins_menu
    else:
        gen "Ready for another wager?" ("base", xpos="far_left", ypos="head")
        twi "Always!"
        ger "Remember, after your first win we'll give you another 1%% from our weekly profits on your every subsequent victory."
        gen "Is there a limit?" ("base", xpos="far_left", ypos="head")
        fre "There is... But no offence, sir... I doubt you're going to reach it."
        gen "(We'll see about that...)" ("base", xpos="far_left", ypos="head")
        gen "Okay then... If you two win, then I'll give you ten gold." ("base", xpos="far_left", ypos="head")
        ger "One second, professor."
        nar "George takes out a calculator and starts calculating something."
        if game.gold < 10:
            ger "We have to refuse."
            gen "Why?" ("base", xpos="far_left", ypos="head")
            fre "Long explanation or short?"
            menu:
                "-Long-":
                    fre "{size=-2}The further extension to fractional values of your current income in the first instance on the establishment of a method of algebraical evolution which bears the same relation to arithmetical evolution that algebraical division bears to arithmetical division gives unsatisfactory results.{/size}"
                "-Short-":
                    ger "You are broke, sir."
            fre "Come back with your offer when you have more gold, professor."
            gen "Fine..." ("base", xpos="far_left", ypos="head")
            nar "You return to your office."
            jump main_room
        ger "Acceptable..."
        twi "Let's play."

    play music "music/Juhani_Junkala.ogg" fadein 1 if_changed

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ renpy.call_in_new_context("start_duel", random_enemy_deck, twins_after, [0, True, True, False], random_player_deck)

    if duel_response == "Close":
        jump twins_duel_cancel

    elif  not duel_response == "win":
        jump twins_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if states.twi.ev.cardgame.stage < 3:
        twi "Impossible!"
        ger "How did you even do that? We weighed these packs for a reason..."
        gen "You did what, sorry?" ("base", xpos="far_left", ypos="head")
        fre "Don't mind him, he doesn't know what he's saying when he's angry."
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "So... We had a deal." ("base", xpos="far_left", ypos="head")
        fre "Yes, about that..."
        gen "You're not backing out, are you?" ("base", xpos="far_left", ypos="head")
        fre "Of course not, I just wanted to make sure we're on the same page about this."
        fre "You can come pick up your cut once a week."
        ger "The amount may vary, obviously."
        fre "It all depends on how many sales we get that week."
        fre "We're always looking to have someone help with promoting the shop and card game."
        gen "(Sounds like something Hermione might be able to do.)" ("base", xpos="far_left", ypos="head")
        gen "(After some convincing...)" ("base", xpos="far_left", ypos="head")
        ger "I guess you're a part owner now, congratulations!"
        gen "I suppose I am." ("base", xpos="far_left", ypos="head")
        fre "Anything else?"
        gen "No." ("base", xpos="far_left", ypos="head")
        gen "Unless..." ("base", xpos="far_left", ypos="head")
        twi "Unless?"
        gen "Unless you're willing to do another wager?" ("base", xpos="far_left", ypos="head")
        fre "We're not giving you another cut that big again..."
        gen "Well, how about a lower percentage? I'll adjust my wager as well." ("base", xpos="far_left", ypos="head")
        ger "We'll think about it..."

        call give_reward("You have received 5%% of the twins' profits!", "interface/icons/cards.webp")
        $ states.twi.ev.cardgame.profit += 0.05
        $ states.twi.ev.cardgame.stage = 3
        $ tokens += 3
    elif states.twi.ev.cardgame.profit >= 1.2:
        fre "Nice job but you've reached the cap I'm afraid."
        ger "Yeah, we don't want to go into the minus, do we?"
        $ tokens += 1
    else:
        twi "Not again..."
        gen "Time to pay up, boys." ("base", xpos="far_left", ypos="head")
        ger "Fine... We'll up your weekly cut by 1%%..."
        $ tokens += 1
        $ states.twi.ev.cardgame.profit += 0.01

    "You return to your office."
    jump main_room

label twins_duel_lost:
    stop music fadeout 1
    if geniecard_level == 2:
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "It would appear that I may have lost this one..." ("base", xpos="far_left", ypos="head")
        twi "It appears so."
        gen "Well then, here's your reward..." ("base", xpos="far_left", ypos="head")
        $ game.gold -= 10

    menu:
        "-Rematch-":
            jump twins_duel_menu
        "-Be a loser-":
            pass

    ger "Cards not in your favour, Professor? Maybe next time..."
    "You return to your office."

    jump main_room

label twins_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    ger "Cards not in your favour, Professor? Maybe next time..."
    "You return to your office."

    jump main_room

screen genie_vs_twins():
    zorder 15
    add "images/cardgame/VS/background_twins.webp" xalign 0.5 yalign 0.5
screen move_twins():
    zorder 16
    add "images/cardgame/VS/twins_01.webp" at move_in(300, 1)

screen genie_vs_twins_smile():
    zorder 16
    add "images/cardgame/VS/genie_04.webp"
    add "images/cardgame/VS/twins_02.webp"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def twins_after():
        renpy.music.set_volume(0.5)
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play( "sounds/card_punch%s.ogg" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        rnd_text = twins_speech_card[renpy.random.randint(0,len(twins_speech_card)-1)]
        #$ rnd_twin = renpy.random.choice = [fre, goe]

        if renpy.random.randint(0, 1) == 0:
            renpy.say(fre, rnd_text)
        else:
            renpy.say(ger, rnd_text)
        renpy.music.set_volume(1.0)
        return
