label clothing_store:
    call room("clothing_store")
    play music "music/clothing_store.ogg" fadein 1 if_changed

    if mailbox.type_in_parcels("outfit"):
        maf "I'm sorry luv, but I'm still quite busy working on your previous order."
        maf "Come back once you received my package."
        jump return_office

    if not clothing_store_intro_done:
        $ clothing_store_intro_done = True

        nar "You enter to see an old woman sewing together two pieces of long dark fabric."
        nar "The woman is dressed almost entirely in pink and has a warm, approachable air to her."
        gen "Hello." ("base", xpos="far_left", ypos="head")
        maf "Hello, Professor Dumbledore."
        maf "What can I do for you? Would you like a new cloak, or do you require some alterations to an existing item?"
        gen "Neither thank you, I'm just here to make a few inquiries." ("base", xpos="far_left", ypos="head")
        maf "Of course sir, what could I help you with?"
        gen "Firstly, what type of items do you sell?" ("base", xpos="far_left", ypos="head")
        maf "Well, I'm a tailor. I make uniforms for the staff and students."
        maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
        gen "I see. Do you ever make custom orders?" ("base", xpos="far_left", ypos="head")
        maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
        gen "So you're interested in making unique outfits?" ("base", xpos="far_left", ypos="head")
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colours at the moment."
        maf "What did you have in mind?"
        gen "A few things. I haven't decided on anything specific yet." ("base", xpos="far_left", ypos="head")
        maf "Well, while you're making up your mind, feel free to browse the store."
    else:
        maf "What can I get you today?"

    call shop_dress

    gen "Thank you very much." ("base", xpos="far_left", ypos="head")
    maf "You're welcome, sir. Come back any time."

    jump return_office

screen clothing_store():
    tag room_screen
    zorder 0

    if game.daytime:
        add "images/rooms/_bg_/corridor.webp" #Need day image.
    else:
        add "images/rooms/_bg_/corridor.webp"
