label her_promoter_job:

    if states.her.ev.promote_cardgame.first_time:
        gen "Alright then, I think it's time you go help the twins with their shop." ("base", xpos="far_left", ypos="head")
        her "Sir... Why do you want me to help them, exactly?" ("annoyed", "closed", "base", "mid")
        gen "That is my business." ("grin", xpos="far_left", ypos="head")
        her "What do you want me to tell them then?" ("open", "narrow", "worried", "mid_soft")
        gen "Just ask them if they have a need for any help promoting their card game." ("base", xpos="far_left", ypos="head")
        gen "If they're as business minded as I think, then there's no way they'd say no." ("grin", xpos="far_left", ypos="head")
        gen "And make sure you ask them for payment." ("grin", xpos="far_left", ypos="head")
        her "Fine..." ("base", "closed", "base", "mid")
        her "I'll see you tonight." ("open", "base", "base", "mid")
        gen "Forgetting something?" ("base", xpos="far_left", ypos="head")
        her "*Hmm*?" ("annoyed", "base", "worried", "mid")
        gen "Your uniform!" ("base", xpos="far_left", ypos="head")
        gen "Here you are..." ("base", xpos="far_left", ypos="head")
        play sound "sounds/cloth_sound3.ogg"
        pause 1

        if states.her.level < 19:
            # Failstate
            her "I know I said I'd help them, but you want me to wear... this?" ("open", "base", "angry", "mid")
            gen "Of course, is that going to be a problem?" ("base", xpos="far_left", ypos="head")
            her "Yes!" ("angry", "base", "angry", "mid")
            her "I can't believe you've done this."
            her "Did you have this commissioned?" ("open", "squint", "angry", "mid")
            gen "The twins sold it to me..." ("base", xpos="far_left", ypos="head")
            her "Of course they did..."
            gen "So it's a--" ("base", xpos="far_left", ypos="head")
            her "Of course it's a no!" ("shock", "base", "angry", "mid")
            her "" ("angry", "base", "angry", "mid")

            $ states.her.mood += 5

            $ _event.cancel()
            jump hermione_favor_menu.odd_jobs

        random:
            block:
                her "Why are the cards placed like that?" ("mad", "narrow", "worried", "down")
                her @ cheeks blush "..." ("normal", "happyCl", "worried", "mid")
                her @ cheeks blush "Fine..." ("open", "narrow", "base", "down")
            block:
                her @ cheeks blush "..." ("normal", "base", "worried", "mid")
                her @ cheeks blush "Well, if it stops you from deducting those points." ("open", "happyCl", "worried", "mid")
                her "I'll do it." ("base", "wink", "base", "mid")
            block:
                her @ cheeks blush "It's a bit revealing... but I'll do it." ("smile","happy")
                her @ cheeks blush "For Gryffindor house obviously!" ("open", "happyCl", "base", "mid")
            block:
                her "That doesn't leave a lot to the imagination..." ("smile", "happy", "base", "mid")
                her "At least the straps should cover my nipples..." ("open", "wink", "base", "mid")
                her @ cheeks blush "I'll do it..." ("normal", "happy", "base", "mid")
    else:
        gen "I think it's time you go help the twins with their shop again." ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d5
    play sound "sounds/cloth_sound.ogg"
    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_poker)
    hide screen blkfade
    with d5

    gen "Looking great!" ("grin", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you..." ("open","happy")
    gen "Off you go then..." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")
    $ states.her.busy = True
    $ current_job = "promoter"

    call music_block
    jump main_room_menu

label her_promoter_job_return:
    $ current_job = None
    $ hermione.equip(her_outfit_poker)

    call her_walk(action="enter", xpos="mid", ypos="base")

    if states.her.ev.promote_cardgame.first_time:
        $ states.her.ev.promote_cardgame.first_time = False
        gen "Hello, [name_hermione_genie], how was your day?" ("base", xpos="far_left", ypos="head")
        her "Good..." ("normal", "happy", "base", "mid")
        her "I'm still not that comfortable wearing the outfit you provided though, so I just stood behind the shop counter today." ("open", "closed", "base", "mid")
        her @ cheeks blush "Apparently we sold a lot more items than usual though." ("base","happy", "base", "mid")
        gen "Great news, I bet the twins are ecstatic." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "Indeed, It was nice seeing them in such high spirits." ("open", "happyCl", "base", "mid")
        her "Whilst I might not agree with all their business methods, I think they might become great salesmen some day." ("base", "happy", "base", "mid")
        gen "Seems to me like they are already..." ("grin", xpos="far_left", ypos="head")
        gen "So, how come you had such a surge in new customers?" ("base", xpos="far_left", ypos="head")
        her "No idea, maybe the card game got more people interested in browsing the rest of their stock." ("annoyed", "happy", "base", "R")
        her "They actually had some problems with people stealing things before I started working there though." ("open", "closed", "base", "mid")
        gen "And this stopped after you started working there?" ("base", xpos="far_left", ypos="head")
        her "Well, probably not because of it. They put in some anti-thieving measures." ("base", "base", "base", "mid")
        gen "Patent pending?" ("base", xpos="far_left", ypos="head")
        her "It's pretty clever actually, they put up a mirror behind the counter so that when I have to turn around and grab something I'll be able to see if anyone takes anything." ("smile", "wink", "base", "mid")
        gen "\"Yeah, I'm sure that's why they put the mirror there\"..." ("grin", xpos="far_left", ypos="head")
        gen "Sounds like you're doing a great job." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "Thanks!" ("open","happy")
        her "Here's your payment." ("open", "base", "base", "mid")

        call give_reward("You have received twenty gold", "interface/icons/gold.webp")
        $ game.gold += 20
        gen "Well done [name_hermione_genie], fifteen points to Gryffindor." ("base", xpos="far_left", ypos="head")
        $ gryffindor += 15

    random:
        block:
            her ""
            gen "Hello, [name_hermione_genie], how was your day?" ("base", xpos="far_left", ypos="head")
            her "It was fine, the outfit is a bit chilly though." ("normal", "happy", "base", "mid_soft")
            gen "So, no other complications?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well..." ("soft", "narrow", "worried", "down")
            her @ cheeks blush "The twins asked me to give out some free promotional starter packs." ("open", "happy", "base", "mid")
            gen "Yes?" ("base", xpos="far_left", ypos="head")
            gen "Sounds like a great way to get people into playing..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Well, I didn't have anywhere to store the packs as you could imagine." ("base", "narrow", "worried", "down")
            her @ cheeks blush "So I had to resort to putting them behind my suspenders and the top of my stockings..." ("open", "closed", "base", "mid")
            her @ cheeks blush "And one customer got a bit..." ("normal", "closed", "base", "mid")
            her @ cheeks blush "Touchy." ("base", "narrow", "annoyed", "up")
            gen "I see..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "I did get a bit agitated at one point actually..." ("open", "closed", "base", "mid")
            gen "They didn't fire you, did they?" ("angry", xpos="far_left", ypos="head")
            her "No!" ("mad", "wide", "base", "mid")
            her "The customer was quite apologetic actually and bought a bunch of things." ("smile", "closed", "angry", "mid")
            her "The twins obviously took the credit for getting such a big sale and seemed rather pleased with themselves." ("crooked_smile", "narrow", "annoyed", "mid")
            her "I'm fine with them believing they had anything to do with it, though." ("smile", "closed", "base", "mid")
            gen "How noble of you..." ("base", xpos="far_left", ypos="head")
            her "Here's your payment." ("open", "base", "base", "mid")

            call give_reward("You have received twenty gold", "interface/icons/gold.webp")
            $ game.gold += 20
            gen "Well done [name_hermione_genie], twenty points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 20

        block:
            her ""
            gen "Hello, [name_hermione_genie], how was your day?" ("base", xpos="far_left", ypos="head")
            her "Awful..." ("normal", "narrow", "worried", "down")
            gen "Really, why is that?" ("base", xpos="far_left", ypos="head")
            her "Well, I'm not actually angry..." ("open", "base", "base", "mid")
            her "Just a bit annoyed, that's all." ("annoyed", "closed", "base", "mid")
            gen "With?" ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Myself..." ("open", "base", "worried", "R")
            her "We've set up a practice day where you get to borrow a deck of cards to get more people into the game." ("normal", "happy", "base", "mid")
            gen "Sounds like a good idea, get people invested." ("grin", xpos="far_left", ypos="head")
            her "Well, that was fine and all until the amount of new people interested started to slow down." ("open", "narrow", "worried", "down")
            gen "I see, so I expect the responsibility fell on you as you're the one meant to promote the game?" ("base", xpos="far_left", ypos="head")
            her "Yes... I thought it was a great idea, so if it ended up not working out, then it would look very bad on my part." ("normal", "closed", "base", "mid")
            gen "So, you had to stop the practice sessions?" ("base", xpos="far_left", ypos="head")
            her "No, that's not why I'm annoyed..." ("annoyed", "happy", "base", "R")
            her @ cheeks blush "In my haste to find a solution I thought it would be a great idea to play a few rounds of strip cards to get more people interested." ("open", "narrow", "base", "down")
            her @ cheeks blush "..." ("angry", "closed", "angry", "mid")
            her @ cheeks blush "I've played enough not to be beaten by a new player ,I thought." ("mad", "narrow", "angry", "R")
            gen "Of course, you've played against me after all..." ("grin", xpos="far_left", ypos="head")
            her "..." ("base", "base", "angry", "mid")
            gen "Sorry, go on." ("base", xpos="far_left", ypos="head")
            her "Well, I managed to get a bunch of people into the card game, so practice day is still on the schedule." ("annoyed", "closed", "angry", "mid")
            gen "That's good!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Though I might reconsider the whole strip card idea..." ("angry", "narrow", "worried", "down")
            her @ cheeks blush "I lost pretty quickly..." ("normal", "closed", "base", "mid")
            her @ cheeks blush "It turned out they had been cheating the whole time..." ("normal", "base", "base", "mid")
            gen "Well, cheaters never prosper..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "That's not true in this case... they prospered alright." ("open", "happy", "base", "R")
            her "In any case, they seemed... happy, they bought a bunch of things so that makes me..." ("normal", "base", "base", "mid")
            her @ cheeks blush "Happy as well..." ("angry", "closed", "base", "mid")
            gen "A job well done then, I bet the twins are very grateful for your contribution." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Thank you." ("annoyed", "happyCl", "base", "mid")
            her "Anyway..." ("base", "base", "base", "mid")
            her "Here's your payment." ("open", "base", "base", "mid")

            call give_reward("You have received twenty gold", "interface/icons/gold.webp")
            $ game.gold += 20
            gen "Well done [name_hermione_genie], twenty points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 20

        block:
            her ""
            gen "Hello, [name_hermione_genie], how was your day?" ("base", xpos="far_left", ypos="head")
            her "Great, they held a card game tournament today." ("base", "base", "base", "mid")
            gen "Wait, a tournament? How come I wasn't invited?" ("angry", xpos="far_left", ypos="head")
            her "It was students only, obviously..." ("open", "happy", "base", "R")
            gen "Oh... of course." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "There were way more participants than I expected seeing that there was an entry fee." ("base", "closed", "base", "mid")
            gen "Must've been a great prize pool then..." ("base", xpos="far_left", ypos="head")
            her "That's the weird thing. The prize pool only amounted to about half of the total entry fee amount." ("open", "base", "base", "mid")
            her "Apparently... Someone had gone around spreading the rumour that the winner would..." ("normal", "narrow", "worried", "down")
            her @ cheeks blush "Get a go with me if they won the tournament..." ("annoyed", "narrow", "base", "down")
            gen "And did they?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Of course that was never on the table..." ("base", "base", "angry", "mid")
            gen "On a desk then?" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "Well..." ("annoyed", "base", "base", "mid")
            her @ cheeks blush "The winner did end up standing there with such an expectant look on his face after everyone had left..." ("open", "narrow", "worried", "down")
            gen "..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "So I told him that whatever he was expecting it wasn't happening." ("angry", "narrow", "angry", "R")
            her "He seemed so disheartened, I felt a bit bad about the whole thing..." ("open", "closed", "angry", "mid")
            her @ cheeks blush "So, since I didn't want to bring his feeling of victory down, I figured since some students had spread the rumour, they'd assume the worst anyway..." ("open", "base", "angry", "mid")
            her @ cheeks blush "So I put my hand down his pants and fiddled around a bit whilst letting the guy get a peek behind my suspenders." ("grin", "base", "angry", "mid")
            gen "Good on you!" ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "You don't think that was a bit much?" ("annoyed", "base", "base", "mid")
            gen "No! That was the right thing to do in that situation." ("grin", xpos="far_left", ypos="head")
            gen "There wasn't a lot you could do about the rumours... Even if nothing had happened, he'd probably lie about it anyway." ("base", xpos="far_left", ypos="head")
            gen "You most likely ended up making that guy's night." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "More like month... seeing how much he..." ("open", "narrow", "worried", "down")
            her "Anyway..." ("normal", "base", "base", "mid")
            her "glad you agree." ("base", "happy", "base", "mid_soft")
            her "Here's your payment." ("open", "base", "base", "mid")

            call give_reward("You have received twenty gold", "interface/icons/gold.webp")
            $ game.gold += 20
            gen "Well done [name_hermione_genie], twenty points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 20

        block:
            $ hermione.set_cum(hair="light")
            her "" ("cum", "narrow", "base", "dead")
            gen "What happened to you?" ("base", xpos="far_left", ypos="head")
            her "What do you mean..." ("open", "narrow", "worried", "mid_soft")
            her @ cheeks blush "Oh, that..." ("base", "narrow", "worried", "down")
            gen "Yes, that..." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "There's a good explanation for this." ("normal", "narrow", "base", "down")
            gen "..." ("base", xpos="far_left", ypos="head")
            gen "Go on." ("base", xpos="far_left", ypos="head")
            her @ cheeks blush "Oh, sorry... Well, I was trying out a new sales tactic..." ("open", "happy", "base", "R")
            gen "Something the twins came up with I assume?" ("base", xpos="far_left", ypos="head")
            her "No, I read about it in one of their books, actually." ("grin", "happy", "base", "mid_soft")
            her "Much like how you should always put the most lucrative cheap items at the counter to make the customer..." ("open", "base", "base", "mid")
            gen "Get on with it." ("angry", xpos="far_left", ypos="head")
            her @ cheeks blush "Fine..." ("annoyed", "narrow", "base", "R_soft")
            her @ cheeks blush "I read that by putting the customer in a state of peace and happiness it would make them more susceptible to making hasty decisions." ("smile", "happyCl", "base", "mid")
            gen "Didn't think you'd be interested in such... unorthodox sales tactics..." ("grin", xpos="far_left", ypos="head")
            her @ cheeks blush "I was curious to see if it would work more than anything else." ("base", "closed", "base", "mid")
            her "I tried it out to test the legitimacy of the claims in that book of theirs..." ("open", "base", "base", "mid")
            gen "of course..." ("base", xpos="far_left", ypos="head")
            gen "And how many times did you test this... theory of yours." ("base", xpos="far_left", ypos="head")
            her "There's no conclusion to be made by just testing a theory once [name_genie_hermione]." ("normal", "closed", "angry", "mid")
            her "Anyway..." ("open", "base", "base", "mid")
            her "Here's your payment." ("open", "base", "base", "mid")

            call give_reward("You have received twenty gold", "interface/icons/gold.webp")
            $ game.gold += 20
            gen "Well done [name_hermione_genie], twenty-five points to Gryffindor." ("base", xpos="far_left", ypos="head")
            $ gryffindor += 25

    her "Good night, [name_genie_hermione]."
    call her_walk(action="leave")

    $ hermione.equip(her_outfit_last)
    $ hermione.set_cum(None)
    $ states.her.ev.promote_cardgame.helped = True

    call music_block
    jump main_room_menu
