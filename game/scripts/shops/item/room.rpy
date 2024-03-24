screen weasley_store_room():
    tag room_screen

    if game.daytime:
        add "images/rooms/weasley_store/store_day.webp"
    else:
        add "images/rooms/weasley_store/store_night.webp"

    use ui_top_bar

    zorder 0

label item_store:
    show screen blkfade
    with d3

    call room("weasley_store")
    call gen_chibi("stand", 0, "base")
    call gen_walk(xpos="left", ypos="base")
    play music "music/weasley_store.ogg" fadein 1 if_changed

    hide screen blkfade
    with d3

    if not item_store_intro_done:
        $ item_store_intro_done = True

        fre "Professor Dumbledore? What are you doing here? I thought you didn't leave your office anymore."
        ger "You're not here to shut us down are you?"
        gen "Shut you down? What for?" ("base", xpos="far_left", ypos="head")
        fre "NOTHING!"
        ger "We certainly aren't selling potion ingredients that we stole from Snape."
        fre "No prohibited goods being sold here."
        ger "None at all!"
        fre "But if we did sell them--"
        ger "--Which we don't--"
        fre "They would be sold at the best prices in the school."
        ger "Unbeatable."
        gen "I see..." ("base", xpos="far_left", ypos="head")
        gen "What sort of items are you \"not selling\"?" ("base", xpos="far_left", ypos="head")
        ger "We have books, treats, and knick-knacks for sale."
        fre "Take a look."
    elif states.twi.ev.cardgame.interest:
        $ states.twi.ev.cardgame.interest = False

        twi "Greetings Dumbledore, sir!"
        gen "Hello boys." ("base", xpos="far_left", ypos="head")
        gen "I'm here to pick up my weekly cut of profits." ("base", xpos="far_left", ypos="head")
        twi "Of course!"

        $ her_help = 0
        if states.her.ev.promote_cardgame.helped:
            ger "Miss Granger has helped us with promotions this week so that means more profits."
            $ her_help = 200
            $ states.her.ev.promote_cardgame.helped = False

        $ shop_profit = renpy.random.randint(50+her_help, 300)
        ger "Here, your weekly cut."
        call give_reward("You've received "+str(int(shop_profit*states.twi.ev.cardgame.profit))+" gold.", "interface/icons/gold.webp")

        $ game.gold += int(shop_profit*states.twi.ev.cardgame.profit)
        ger "..."
        twi "Did you need anything else?"
    else:
        twi "Hello Professor! Came here to buy?"

        ##Any quest that could play directly after intro can't have introductory dialogue##
    if states.sna.ev.hangouts.cho_e1 and not quidditchguide_ITEM.unlocked and not states.cho.ev.quiz.complete:
        $ quidditchguide_ITEM.unlocked = True
        # After talking to Snape about Cho.
        # If you haven't yet beaten the Quiz.
        gen "Let's see..." ("base", xpos="far_left", ypos="head")
        twi "How can we help you?"
        gen "Just having a look around at your fine merchandise..." ("base", xpos="far_left", ypos="head")
        fre "No need to be concerned, sir!"
        fre "Everything is completely above board and procured from totally legitimate sources!"
        ger "No stolen goods here!"
        gen "I wasn't looking out for stolen goods in particular...{w=0.4} should I be?" ("base", xpos="far_left", ypos="head")
        ger "Oh, well..."
        fre "Of course you weren't!"
        gen "Seems like I can't find what I'm looking for anyway..." ("base", xpos="far_left", ypos="head")
        fre "Well, if you're looking for something in particular then we could always look into procuring said item."
        ger "What type of object are you looking for?"
        gen "Well... As you boys may know, the Quidditch season is starting soon." ("base", xpos="far_left", ypos="head")
        fre "Yes?"
        gen "Well, I realised that I haven't actually gone in depth with the sport yet." ("base", xpos="far_left", ypos="head")
        ger "Really? You're telling me that {b}the{/b} Dumbledore doesn't know anything about--{nw}"
        play sound "sounds/kick.ogg"
        ger "Really? You're telling me that {b}the{/b} Dumbledore doesn't know anything about--{fast} {size=+4}*Hngh*!!{/size}"
        fre "{size=-4}Quiet, George!{/size}"
        fre "What he meant to say was, If you're looking to acquire something to touch up on your Quidditch knowledge then you've come to the right place!"
        ger "{size=-4}I suppose it explains why he's always staring out in the distance, clapping politely during the--{/size}"
        fre "{size=-4}George!{/size}"
        gen "Yes, a guidebook should be enough for me to be able to touch up the players--{w=0.2} I mean refresh my memory on the rules." ("base", xpos="far_left", ypos="head")
        ger "Touch up the--"
        gen "It's like Basketball right?" ("base", xpos="far_left", ypos="head")
        fre "Basket ball? Well, I wouldn't know anything about that, I always tune out whenever dad drones on about muggle sports."
        ger "Did he say touch up--"
        gen "So, do you have such a book in stock?" ("base", xpos="far_left", ypos="head")
        fre "Of course!"
        ger "We do?"
        fre "Yes George... We've got our own guidebook, since we're on the Gryffindor team."
        ger "Oh yeah!"
        gen "You are?" ("base", xpos="far_left", ypos="head")
        fre "Yep!"
        ger "Don't they note the Quidditch players names down in their records Fred?"
        fre "..."
        ger "Not that we'd know anything about those of course..."
        gen "Now, I wouldn't want you to part with your personal belongings if it's for school." ("base", xpos="far_left", ypos="head")
        ger "No worries, sir! We already know all the rules so you can have it for fr--"
        play sound "sounds/kick.ogg"
        fre "Blimey!"
        ger "What Fred wanted to say is--"
        ger "You can have it, for a hundred gold coins."
        gen "......" ("base", xpos="far_left", ypos="head")
        gen "Great, thanks again boys..." ("base", xpos="far_left", ypos="head")
        ger "Don't mention it..."
        fre "...Make sure to take notes!"
        gen "Are you assuming your headmaster doesn't know how studying works?" ("base", xpos="far_left", ypos="head")

        play sound "sounds/kick.ogg"
        with hpunch

        fre "*Cries out like a hurt puppy*"
        ger "Of course not, professor, Fred was just joking, right Fred?"
        fre "... Yes sir, just kidding."
        gen "Right..." ("base", xpos="far_left", ypos="head")
        ger "We've put the book in \"Quest Items\" section, can't miss it."

    elif states.cardgame.unlocked and states.her.ev.cardgame.known and not states.twi.ev.cardgame.known:
        gen "Let's see..." ("base", xpos="far_left", ypos="head")
        twi "Looking for something in particular, sir?"
        gen "I'm looking to acquire some Wizard cards." ("base", xpos="far_left", ypos="head")
        play sound "sounds/spit.ogg"
        fre "Wizard cards....*spit*"
        ger "Why would you want any of those?"
        gen "What does one do with playing cards... Play the game of course." ("base", xpos="far_left", ypos="head")
        fre "Well, we got some of our own to see if it was worth stocking them, but none for sale."
        ger "The profit margin was way to low... Something about import tax."
        ger "We would have to sell a lot of them to make good profit."
        gen "I see... So there's no way you'd stock them?" ("base", xpos="far_left", ypos="head")
        fre "Wizard cards haven't been popular in ages..."
        ger "It does have potential though, not everyone at Hogwarts is going to be into duelling... Or chess."
        fre "How about this... We did acquire a set of cards to try the game out."
        gen "So..." ("base", xpos="far_left", ypos="head")
        ger "If you beat us we'll do a trial run and stock some cards for the students."
        twi "(There's no way this\nold man would ever beat us.)"
        $ states.twi.ev.cardgame.known = True
        jump twins_duel_menu

    elif states.twi.ev.cardgame.stocked and states.twi.ev.cardgame.stage < 2 and not states.twi.ev.cardgame.stock_talk:
        gen "Well, well... Looking good as always boys!" ("base", xpos="far_left", ypos="head")
        twi "..."
        gen "In a professional sense that is... Don't you worry." ("base", xpos="far_left", ypos="head")
        gen "So, How are things going?" ("base", xpos="far_left", ypos="head")
        ger "You were right sir! We've seemed to have struck gold with Wizard Cards."
        gen "Glad to hear it." ("grin", xpos="far_left", ypos="head")
        fre "We've gone ahead and put up an official unofficial tier system ladder."
        gen "Unofficial... Official, you say?" ("base", xpos="far_left", ypos="head")
        ger "Yes, as we mentioned... There isn't really any official tournament rules."
        fre "We've sort of kept it that way in that we'll let the people playing set their own wagers and challenges to climb the ladder."
        fre "Any normal game will make you one token richer and once the agreed upon winning conditions for a challenge is achieved then you'll get three tokens!"
        fre "Three challenges won will let you climb to the next tier."
        ger "Which lets you challenge even higher skilled players."

        nar "Only first tier with Snape, Hermione and Twins is available for now."

        gen "And by skilled you mean players with better cards?" ("base", xpos="far_left", ypos="head")
        fre "Something like that."
        gen "I see..." ("base", xpos="far_left", ypos="head")
        # gen "How do I know which players are currently in my tier?" ("base", xpos="far_left", ypos="head")
        # fre "Ah yes, there's a notice board behind us. You should see some people that you know on it."
        ger "I must say, the game has really taken off... Even Snape came to pick up some tokens earlier."
        gen "Really? I'd think he would disapprove of your business." ("base", xpos="far_left", ypos="head")
        fre "He was using a Polyjuice potion to disguise himself as a student."
        ger "But that weird walk of his where he sort of slides across the floor gives him away a mile off."
        fre "Tell you what, let's set a wager right now."
        fre "We'd usually make it a bit more difficult but since you gave us the idea for this."
        ger "Beat us again and we'll give you three tokens and a card."
        gen "That's it? Sounds a bit out of character for you guys to make it this easy." ("base", xpos="far_left", ypos="head")
        fre "Let's call it an insurance so that we can continue our business."
        ger "There's no way you'll beat us again anyway."
        $ states.twi.ev.cardgame.stock_talk = True
        jump twins_duel_menu

    elif states.lun.unlocked and not states.lun.ev.spectrespecs.e1_complete:
        call spectrespecs_E1

        call gen_walk(xpos=0, ypos="base", speed=1.5)

        jump main_room
    elif states.lun.ev.quibbler.stocked and not states.lun.ev.spectrespecs.e2_complete:
        call spectrespecs_E2
    elif states.twi.ev.cardgame.known:
        twi "Perhaps a game of cards?"
        label twins_menu:
        menu:
            "-Buy something-":
                pass
            "-Let's duel- {image=interface/icons/small/cards.webp}":
                label twins_duel_menu:
                if geniecard_level < 2:
                    menu:
                        "-First Duel-":
                            jump twins_first_duel
                        "-Challenge-" if states.twi.ev.cardgame.stock_talk:
                            jump twins_second_duel
                        "-You need to beat the first duel-" (style="disabled") if not states.twi.ev.cardgame.stock_talk:
                            if states.twi.ev.cardgame.stage < 1:
                                gen "(I should beat them at their own game at least once before I try this again...)"
                            elif not states.twi.ev.cardgame.stock_talk:
                                gen "(I need to wait for a letter from them before we can continue...)"
                            jump twins_duel_menu
                        "-Never mind-":
                            twi "Your loss professor."
                            pass
                else:
                    jump twins_random_duel

    call shop_item

    twi "Come again!"

    call gen_walk(xpos=0, ypos="base", speed=1.5)

    jump main_room
