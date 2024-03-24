label purchase_item(item):

    if item.currency == "tokens":
        if tokens < item.price:
            gen "(I don't have enough tokens.)" ("base", xpos="far_left", ypos="head")
            return
    else:
        if game.gold < item.price:
            gen "(I don't have enough gold.)" ("base", xpos="far_left", ypos="head")
            return

    if item == sealed_scroll_ITEM:
        show screen blktone
        with d3
        if not states.her.status.sex:
            gen "What's in this scroll?" ("base", xpos="far_left", ypos="head")
            ger "Don't worry about it."
            gen "Why?" ("base", xpos="far_left", ypos="head")
            fre "You're not ready for what's in this scroll."
            gen "Well, that just makes me want it more." ("base", xpos="far_left", ypos="head")
            ger "Too bad, professor."
            gen "(Perhaps I should check it out later...)" ("base", xpos="far_left", ypos="head")
            hide screen blktone
            with d3
            return

        gen "I'd like to buy this scroll." ("base", xpos="far_left", ypos="head")
        ger "Five hundred gold coins."
        gen "Five hundred!? Why on earth is it so expensive?" ("angry", xpos="far_left", ypos="head")
        fre "Forbidden magic is quite a risky and expensive endeavour Professor, We'll sell it for no less than five hundred."
        gen "What's it for anyway?" ("base", xpos="far_left", ypos="head")
        fre "It is one of the components needed for a forbidden spell."
        ger "Acquired completely legitimately, I might add!"
        gen "What does it do?" ("base", xpos="far_left", ypos="head")
        fre "It transforms you into... something."
        gen "Like what?" ("base", xpos="far_left", ypos="head")
        fre "We don't know, it could be anything."
        ger "A powerful phoenix, a terrifying gorgon, a deadly basilisk or an awe-inspiring dragon."
        gen "Not sure I'd really want to transform into any of those..." ("base", xpos="far_left", ypos="head")
        ger "Well... those are just theories, we've not been able to use the scroll to find the second component ourselves."
        gen "Really? Now that is surprising." ("base", xpos="far_left", ypos="head")
        fre "Yes, although it's blank for some reason... not really anything new to us as we used to have a ma--"
        ger "massive amounts of scrolls just like this one!"
        ger "Yep... lots of them, shame they all burnt."
        fre "What are you-- *HHNG*"
        fre "Oh! I see... Yes, very unfortunate..."
        gen "That is unfortunate... Well, I'm sure I'll manage." ("base", xpos="far_left", ypos="head")
        hide screen blktone
        with d3

    if item == collar_ITEM and not states.her.ev.magic_collar.worn and item.owned == 0:
        show screen blktone
        with d3
        gen "A Magic collar..." ("base", xpos="far_left", ypos="head")
        fre "Oh yes... That thing."
        ger "I'd be careful with that one if I were you."
        gen "How come?" ("base", xpos="far_left", ypos="head")
        fre "Well... It might reveal some secrets that most people would want to keep to themselves."
        gen "Such as?" ("base", xpos="far_left", ypos="head")
        twi "Their true self!"
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Colour me intrigued..." ("base", xpos="far_left", ypos="head")
        gen "And it works?" ("base", xpos="far_left", ypos="head")
        fre "Of course it does, we tested it on ourselves!"
        ger "Just know that the collar loses its magic once it is put on one's neck."
        ger "So you'll have to buy another collar if you want to test if anything's changed..."
        # ger "So you'll have to buy multiple collars if you want to test it on multiple subjects..."
        # fre "Or multiple times on one subject to see if anything's changed..."
        gen "I see." ("base", xpos="far_left", ypos="head")
        gen "So, what did the collar say when you guys put it on?" ("base", xpos="far_left", ypos="head")
        fre "Voyeu--"
        ger "Thrifty!"
        ger "Wait, what did you just say, Fred?"
        fre "..."
        gen "Alright then, I'll take it..." ("base", xpos="far_left", ypos="head")
        fre "*Ahem*... It's a pleasure doing business with you, sir!"
        hide screen blktone
        with d3

    elif item == poker_outfit_ITEM:
        $ item.used = True

        call unlock_clothing("Congratulations! You have unlocked a new outfit!", her_outfit_poker)

    play sound "sounds/money.ogg"

    if item.currency == "tokens":
        $ tokens -= item.price
    else:
        $ game.gold -= item.price
    $ item.owned += 1

    $ item_store_achievements()
        
    return

init python:
    def item_store_achievements():
        # We require a function because lambdas aren't pickleable
        if isinstance(item, Decoration):
            _posters = filter(lambda x: (x.type == "decoration" and x.placement == poster_OBJ), inventory.items)
            _hats = filter(lambda x: (x.type == "decoration" and "hat" in x.name.lower()), inventory.items)

            if all(i.owned > 0 for i in _posters):
                achievements.unlock("postman")

            if all(i.owned > 0 for i in _hats):
                achievements.unlock("hats")