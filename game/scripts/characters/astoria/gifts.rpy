# Astoria Gift Responses

label give_ast_gift(gift_item):
    $ states.ast.gifted = True
    hide astoria_main
    with d5
    ast "" (xpos="mid", ypos="base", trans=d5)

    if gift_item == lollipop_ITEM:

        if states.ast.level < 6:
            ast "A lollipop?" ("horny", "narrow", "base", "mid")
            ast "Why are you giving me sweets, I'm not a kid!" ("upset", "base", "angry", "mid")
            call ast_mood(1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "A lollipop?" ("open", "narrow", "base", "mid")
            call give_gift("You give the lollipop to Astoria...", gift_item)
            ast "why are you being so nice to me..." ("upset", "base", "angry", "mid")
            ast "Although... the other students haven't had any left since the last Hogsmeade trip." ("open", "narrow", "base", "mid")
            ast "They'll be so jealous!" ("grin", "narrow", "base", "mid")
            call ast_mood(-1)
        else:
            ast "A lollipop?" ("open", "narrow", "base", "mid")
            call give_gift("You give the lollipop to Astoria...", gift_item)
            ast "That's going to take all day to suck on..."
            ast "I guess my mouth will be too busy to do anything else for the entire day!"
            call ast_mood(-2)

    elif gift_item == chocolate_ITEM:

        if states.ast.level < 6:
            ast "Some chocolate?" ("open", "narrow", "base", "mid")
            ast "Don't you have any dung-bombs?"
            ast "They're way more fun!"
            call ast_mood(0)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Some chocolate?" ("open", "narrow", "base", "mid")
            call give_gift("You give the chocolate to Astoria...", gift_item)
            ast "Thank you, [name_genie_astoria]." ("open", "narrow", "base", "mid")
            ast "I don't know what I did to deserve it." ("annoyed", "narrow", "base", "R")
            ast "But I'm not going to say no..." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)
        else:
            ast "Some chocolate?" ("open", "narrow", "base", "mid")
            call give_gift("You give the chocolate to Astoria...", gift_item)
            ast "Did you hear chocolate is supposed to be an aphrodisiac?"
            ast "Although it was a muggle that came up with that one, so I doubt there's any truth to it."
            ast "Oh well, that sucks doesn't it?"
            call ast_mood(-2)

    elif gift_item == plush_owl_ITEM:

        if states.ast.level < 6:
            ast "An owl plushie?" ("open", "narrow", "base", "mid")
            ast "Why are you giving me this?"
            ast "Toys are for children..."
            call ast_mood(1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "An owl plushie?" ("open", "narrow", "base", "mid")
            call give_gift("You give the stuffed toy to Astoria...", gift_item)
            ast "I don't use stuffed toys..." ("open", "narrow", "base", "mid")
            ast "I know someone that hates owls though... I'll put this in front of her face when she's waking up..." ("annoyed", "narrow", "base", "R")
            call ast_mood(-1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "An owl plushie?" ("open", "narrow", "base", "mid")
            call give_gift("You give the stuffed toy to Astoria...", gift_item)
            ast "Do I look like a girl that plays with toys?"
            ast "Actually, don't answer that..."
            ast "Guess it'd be rude not to take it..."
            call ast_mood(-1)
        else:
            ast "An owl plushie?" ("open", "narrow", "base", "mid")
            call give_gift("You give the stuffed toy to Astoria...", gift_item)
            ast "If you want to give me toys, you better be prepared for me to call you daddy..."
            ast "So, thank you..."
            ast "Daddy..."
            call ast_mood(-3)

    elif gift_item == butterbeer_ITEM:

        if states.ast.level < 6:
            ast "Butterbeer?" ("smile", "narrow", "base", "mid")
            call give_gift("You give the bottle to Astoria...", gift_item)
            ast "Time to get smashed!" ("smile", "narrow", "base", "mid")
            ast "The other students will be so jealous I got beer into the school..." ("annoyed", "base", "angry", "mid")
            call ast_mood(-2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Butterbeer?" ("smile", "narrow", "base", "mid")
            call give_gift("You give the bottle to Astoria...", gift_item)
            ast "Don't you have something stronger?" ("annoyed", "narrow", "base", "mid")
            ast "Like something you can't get in the school usually?" ("annoyed", "narrow", "base", "R")
            ast "Fine, I'll take it!" ("smile", "narrow", "base", "mid")
            call ast_mood(-1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Butterbeer?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give the bottle to Astoria...", gift_item)
            ast "This watered down piss-water can barely get a house elf tipsy."
            ast "Actually, that gives me an idea..."
            call ast_mood(-1)
        else:
            ast "Butterbeer?" ("open", "narrow", "base", "mid")
            call give_gift("You give the bottle to Astoria...", gift_item)
            ast "It's more of a cider really, isn't it?" ("base", "base", "base", "mid")
            ast "Thanks!" ("smile", "narrow", "base", "mid")
            call ast_mood(-2)

    elif gift_item == science_mag_ITEM:
        if states.ast.level < 6:
            ast "(...)" ("annoyed", "narrow", "base", "down")
            ast "Creating your own itch powder using household ingredients?" ("open", "narrow", "base", "down")
            ast "Is the kitchen even open to students?" ("annoyed", "narrow", "base", "down")
            ast "What am I supposed to do with this, [name_genie_astoria]?" ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Magazines?" ("open", "narrow", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Astoria...", gift_item)
            ast "Making your own stink bombs..." ("annoyed", "narrow", "base", "mid")
            ast "Looks like I might be able to make these in potions class..."
            ast "If Snape doesn't catch me doing it." ("clench", "narrow", "base", "mid")
            call ast_mood(-1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Magazines?" ("upset", "base", "angry", "mid")
            ast "You want me to do more school work?" ("annoyed", "base", "angry", "mid")
            call ast_mood(1)
        else:
            ast "magazines?" ("open", "narrow", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Astoria...", gift_item)
            ast "I was hoping for something a bit more risqué..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)

    elif gift_item == girls_mag_ITEM:
        if states.ast.level < 6:
            ast "Girl magazines?" ("open", "narrow", "base", "mid")
            ast "This is that trash my sister reads." ("clench", "narrow", "base", "down")
            ast "Such a massive waste of time..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Girl magazines?" ("base", "narrow", "angry", "mid")
            call give_gift("You give an assortment of rather girly magazines to Astoria...", gift_item)
            ast "I'll take it for the free mascara sample. I once drew a unibrow on someone with it." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Girl magazines?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give an assortment of rather girly magazines to Astoria...", gift_item)
            ast "Well, I am a girl, so of course I'd want it!" ("annoyed", "narrow", "base", "mid")
            call ast_mood(-1)
        else:
            ast "Girl magazines?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give an assortment of rather girly magazines to Astoria...", gift_item)
            ast "Don't I look hot enough for you [name_genie_astoria]?" ("open", "closed", "base", "mid")
            ast "I'm just teasing you, I'll have it." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)

    elif gift_item == adult_mag_ITEM:
        if states.ast.level < 6:
            ast "Adult magazines?" ("clench", "narrow", "angry", "mid")
            ast "I'm good, thanks." ("base", "narrow", "angry", "mid")
            call ast_mood(0)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Adult magazines?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give an assortment of adult magazines to Astoria...", gift_item)
            ast "Of course I read them. I'm an adult, after all... It's in the name." ("upset", "base", "angry", "mid")
            call ast_mood(-1)
        else:
            ast "Adult magazines?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give an assortment of adult magazines to Astoria...", gift_item)
            ast "This is that magazine Tonks was reading during our writing test..." ("annoyed", "narrow", "base", "down")
            ast "Perhaps I'll wave it at her, so she thinks I stole it..." ("smile", "base", "angry", "mid")
            call ast_mood(-1)

    elif gift_item == porn_mag_ITEM:
        if states.ast.level < 6:
            ast "Porn magazines?" ("base", "narrow", "angry", "mid")
            call give_gift("You give an assortment of pornographic magazines to Astoria...", gift_item)
            ast "I'll take it!" ("grin", "narrow", "base", "mid")
            ast "I'll put one in Susan's bag when she's not looking. Can't wait to see that cows face when her friends notice." ("open", "base", "angry", "mid")
            ast "Thank you, [name_genie_astoria]." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Porn magazines?" ("annoyed", "narrow", "base", "mid")
            ast "Why do you have these?" ("annoyed", "narrow", "base", "mid")
            ast "Give them to Susan..." ("annoyed", "narrow", "base", "R")
            call ast_mood(0)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Porn magazines?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give an assortment of pornographic magazines to Astoria...", gift_item)
            ast "That's some extreme stuff you got there..." ("base", "narrow", "angry", "mid")
            ast "BDSM, what does that stand for..." ("clench", "base", "angry", "mid")
            ast "She looks like she's enjoying it. That's not fun..."
            ast "Although..."
            call ast_mood(-1)
        else:
            ast "Porn magazines?" ("smile", "narrow", "base", "mid")
            call give_gift("You give an assortment of pornographic magazines to Astoria...", gift_item)
            ast "Is this where you get your ideas from?" ("upset", "base", "angry", "mid")
            ast "A swing? Why would you have that in a porn ma... oh there's the next page." ("clench", "base", "angry", "mid")
            ast "Yeah fuck it, give it here..." ("grin", "base", "angry", "mid")
            call ast_mood(-2)

    elif gift_item == krum_poster_ITEM:
        if states.ast.level < 6:
            ast "Viktor Krum?" ("annoyed", "narrow", "base", "mid")
            ast "Is that the Quidditch player everyone seems to fancy?" ("open", "base", "base", "mid")
            call give_gift("You give the poster to Astoria...", gift_item)
            ast "*Hmph*, I guess I'll take it if he's that popular..." ("annoyed", "narrow", "base", "R")
            call ast_mood(0)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Viktor Krum?" ("annoyed", "narrow", "base", "mid")
            ast "Bet he could crush m... someone with his bare hands." ("base", "narrow", "angry", "mid")
            ast "Give it here..." ("smile", "narrow", "base", "mid")
            call give_gift("You give the poster to Astoria...", gift_item)
            call ast_mood(-1)
        else:
            ast "Viktor Krum?" ("smile", "narrow", "base", "mid")
            ast "His trousers aren't even off. What's the point..." ("upset", "base", "angry", "mid")
            call ast_mood(1)

    elif gift_item == sexy_lingerie_ITEM:
        if states.ast.level < 6:
            ast "Lingerie?" ("base", "narrow", "angry", "mid")
            ast "Sexy Lingerie?!?"
            ast "Why do you care so much about what I wear? Isn't this shitty school uniform enough for you?" ("upset", "base", "angry", "mid")
            call ast_mood(2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Lingerie?" ("open", "narrow", "base", "mid")
            ast "I... No, I'd just end up looking like a tramp!" ("upset", "base", "angry", "mid")
            call ast_mood(0)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Lingerie?" ("annoyed", "narrow", "base", "mid")
            ast "Sexy..." ("annoyed", "narrow", "base", "down")
            ast "Why not, I don't know if you could tell, but I'm a bit of a rebel. Might even wear these in class." ("grin", "base", "angry", "mid")
            call give_gift("You give the sexy lingerie to Astoria...", gift_item)
            call ast_mood(-1)
        else:
            ast "Lingerie?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give the sexy lingerie to Astoria...", gift_item)
            ast "Is this is the kind of clothing you want your students to dress up in from now on?" ("annoyed", "narrow", "base", "mid")
            ast "*Heh*- I don't blame you, the school uniform is the most basic piece of trash ever without some spice..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(-1)

    elif gift_item == sexy_stockings_ITEM :
        if states.ast.level < 6:
            ast "Stockings?" ("base", "narrow", "angry", "mid")
            ast "What happened to the dress code at this place?"
            ast "What next, shorter skirts?" ("upset", "base", "angry", "mid")
            call ast_mood(1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Stockings?" ("open", "narrow", "base", "mid")
            call give_gift("You give the stockings to Astoria...", gift_item)
            ast "Seems pretty elastic... I could totally lob some stink bombs with these." ("grin", "base", "angry", "mid")
            call ast_mood(-1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Stockings?" ("annoyed", "narrow", "base", "mid")
            ast "Hah, you fool! With these, you won't be able to stare at my legs any more!" ("grin", "base", "angry", "mid")
            call give_gift("You give the stockings to Astoria...", gift_item)
            call ast_mood(-2)
        else:
            ast "Stockings?" ("annoyed", "narrow", "base", "mid")
            ast "These are almost as see-through as your wicked intentions..." ("grin", "base", "angry", "mid")
            call give_gift("You give the stockings to Astoria...", gift_item)
            ast "Disgusting..." ("upset", "base", "angry", "mid")
            call ast_mood(-1)

    elif gift_item == pink_condoms_ITEM:
        if states.ast.level < 6:
            ast "Condoms?" ("base", "narrow", "angry", "mid")
            ast "Yeah, no... I'll take them, but there's not going to be any dick going near these bad boys..." ("annoyed", "narrow", "base", "mid")
            ast "These will be the perfect thing to fill with water and drop down the staircase..." ("smile", "base", "angry", "mid")
            call give_gift("You give the pack of Condoms to Astoria...", gift_item)
            ast "Cheers for the ammo, [name_genie_astoria]." ("smile", "narrow", "base", "mid")
            call ast_mood(-2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Condoms?" ("base", "base", "base", "mid")
            ast "Oh, thank you so much! I'll prick some holes in these and hand them out at once!" ("grin", "base", "angry", "mid")
            ast "What?" ("annoyed", "narrow", "base", "mid")
            ast "I see your concern... They probably would be able to trace it back to me." ("annoyed", "narrow", "base", "mid")
            ast "Oh well, a gift is a gift." ("base", "base", "base", "mid")
            call give_gift("You give the pack of Condoms to Astoria...", gift_item)
            call ast_mood(0)
        else:
            ast "Condoms?" ("annoyed", "narrow", "base", "mid")
            ast "Why would I need condoms when I could just go in raw?" ("grin", "base", "angry", "mid")
            ast "*Ha-Ha-Hah* The look on your face, now that's something money can't buy." ("smile", "narrow", "base", "mid")
            call give_gift("You sheepishly give the pack of Condoms to Astoria...", gift_item)
            ast "*Hmm*.... Yeah, why not." ("base", "base", "base", "mid")
            call ast_mood(-1)

    elif gift_item == vibrator_ITEM:
        if states.ast.level < 6:
            ast "A vibrator?" ("base", "narrow", "angry", "mid")
            ast "Gross, where did you even get that from?" ("upset", "base", "angry", "mid")
            call ast_mood(2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "A vibrator?" ("base", "narrow", "angry", "mid")
            ast "Get the fuck out..." ("upset", "base", "angry", "mid")
            ast "Oh right, I'm in your office... Yeah, that's going to be a solid no on that one." ("annoyed", "narrow", "base", "mid")
            call ast_mood(1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "A vibrator?" ("base", "narrow", "angry", "mid")
            ast "Hold on a second, that's the noise I've been hearing in the girls chambers!" ("smile", "narrow", "base", "mid")
            ast "Do they work?" ("smile", "narrow", "base", "mid")
            ast "I mean, I'll take it, I guess." ("base", "base", "base", "mid")
            call give_gift("You give the vibrator to Astoria...",gift_item)
            call ast_mood(-1)
        else:
            ast "A vibrator?" ("base", "base", "base", "mid")
            call give_gift("You give the vibrator to Astoria...",gift_item)
            ast "That's disgusting! What a disgusting old man you are. Well, aren't you being disgusting..." ("upset", "base", "angry", "mid")
            ast "Disgusting..." ("upset", "base", "angry", "mid")
            ast "Give it here." ("smile", "narrow", "base", "mid")
            call ast_mood(-2)

    elif gift_item == anal_lube_ITEM:
        if states.ast.level < 6:
            ast "Lube?" ("open", "narrow", "base", "mid")
            ast "I know the perfect staircase for this!" ("smile", "narrow", "base", "mid")
            call give_gift("You give the jar of lube to Astoria...", gift_item)
            ast "Thank you, [name_genie_astoria]." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Anal Lube?" ("smile", "narrow", "base", "mid")
            ast "Swiggity swooty I'm coming for that booty!" ("smile", "base", "angry", "mid")
            ast "Come on now, what's with that dry humour. Maybe you could use some of that lube?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You cautiously give the jar of lube to Astoria...", gift_item)
            ast "Boo!" ("annoyed", "narrow", "base", "mid")
            ast "*ha-ha-ha*!" ("smile", "narrow", "base", "mid")
            call ast_mood(-2)
        else:
            ast "Anal Lube?" ("smile", "narrow", "base", "mid")
            call give_gift("You give the jar of lube to Astoria...", gift_item)
            ast "Why would I need this, surely the initial pain is the best part..." ("upset", "base", "angry", "mid")
            ast "Oh, for me? Duh!" ("annoyed", "narrow", "base", "mid")
            ast "Yeah, actually I'll take it..." ("smile", "narrow", "base", "mid")
            call ast_mood(-2)

    elif gift_item == ballgag_and_cuffs_ITEM:
        if states.ast.level < 6:
            ast "Handcuffs? And what.... a ball gag?" ("base", "narrow", "angry", "mid")
            ast "I don't know what you're trying to insinuate." ("upset", "base", "angry", "mid")
            ast "The cuffs could be useful but why the ball gag?" ("base", "narrow", "angry", "mid")
            ast "I'd rather not." ("annoyed", "narrow", "base", "mid")
            call ast_mood(1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Handcuffs? And a Ball gag?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give the handcuffs to Astoria...", gift_item)
            ast "I can break these cuffs!" ("upset", "base", "angry", "mid")
            ast "*HNNNNNGH!" ("upset", "base", "angry", "mid")
            ast "I can't break those cuffs..." ("annoyed", "narrow", "base", "mid")
            ast "Do you have a key?" ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "Handcuffs? And a Ball gag?" ("smile", "narrow", "base", "mid")
            call give_gift("You give the handcuffs to Astoria...", gift_item)
            ast "So I guess these are one of those BDSM items?" ("base", "base", "base", "mid")
            ast "Colour me intrigued..." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)

    elif gift_item == anal_plugs_ITEM:
        if states.ast.level < 6:
            ast "anal plugs?" ("base", "narrow", "angry", "mid")
            ast "Yuck, what the hell is wrong with you... do you know where these go?" ("upset", "base", "angry", "mid")
            ast "Of course you do... you detestable dingbat." ("upset", "base", "angry", "mid")
            call ast_mood(2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "anal plugs?" ("base", "narrow", "angry", "mid")
            ast "Why don't you try and sit on one yourself..." ("upset", "base", "angry", "mid")
            call ast_mood(1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "anal plugs?" ("base", "narrow", "angry", "mid")
            call give_gift("You give the anal plugs to Astoria...", gift_item)
            ast "Why are you giving me this?" ("annoyed", "narrow", "base", "mid")
            ast "I'll take it I guess..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "anal plugs?" ("base", "base", "base", "mid")
            call give_gift("You give the anal plugs to Astoria...", gift_item)
            ast "You do know these hurts a bit if you're not used to them?" ("annoyed", "narrow", "base", "mid")
            nar "Astoria absent-mindedly pockets the anal plug."
            ast "Don't see why you'd give these out as if they were sweets..." ("annoyed", "base", "base", "mid")
            call ast_mood(-1)


    elif gift_item == testral_strapon_ITEM:
        if states.ast.level < 6:
            ast "A strap-on?" ("base", "narrow", "angry", "mid")
            ast "Why would you give me this... it's so ribbed..." ("upset", "base", "angry", "mid")
            ast "As if anyone would want something like that!" ("upset", "base", "angry", "mid")
            call ast_mood(1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "A strap-on?" ("base", "narrow", "angry", "mid")
            ast "What do you want me to do with this?" ("annoyed", "narrow", "base", "mid")
            ast "Well, I know what you want me to do with it." ("annoyed", "narrow", "base", "mid")
            ast "It's not happening..." ("upset", "base", "angry", "mid")
            call ast_mood(0)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "A strap-on?" ("upset", "base", "angry", "mid")
            call give_gift("You give the strap-on to Astoria...", gift_item)
            ast "I'll strap it on your forehead and make you into a sex unicorn!" ("grin", "base", "angry", "mid")
            ast "I read about people having sex on top of a unicorn..." ("base", "narrow", "angry", "mid")
            ast "Bit of an odd segment that one was..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(-1)
        else:
            ast "A strap-on?" ("annoyed", "narrow", "base", "mid")
            call give_gift("You give the strap-on to Astoria...", gift_item)
            ast "It says Thestral on the side..." ("annoyed", "narrow", "base", "mid")
            ast "Isn't' that the creature where only people that have witnessed someone die can see?" ("annoyed", "narrow", "base", "mid")
            ast "That makes the person who made he mould kinda fucked up if you think about it..." ("base", "narrow", "angry", "mid")
            ast "I like it..." ("smile", "narrow", "base", "mid")
            call ast_mood(-2)

    elif gift_item == broom_2000_ITEM:
        if states.ast.level < 6:
            ast "A broom?" ("base", "base", "base", "mid")
            ast "What's that sticking out on the top? That's not going to help me fly!" ("annoyed", "narrow", "base", "mid")
            call ast_mood(1)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "A broom?" ("base", "base", "base", "mid")
            call give_gift("You give the broom to Astoria...", gift_item)
            ast "Now if anything would motivate you enough to fly, that would..." ("grin", "base", "angry", "mid")
            ast "Bit awkward during broom care though..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "A broom?" ("smile", "narrow", "base", "mid")
            call give_gift("You give the broom to Astoria...", gift_item)
            ast "Now that will keep you sturdy." ("grin", "base", "angry", "mid")
            ast "What a depraved little invention..." ("smile", "base", "angry", "mid")
            ast "Totally something I'd come up with!"
            ast "You look sceptical..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(-1)

    elif gift_item == sexdoll_ITEM:
        if states.ast.level < 6:
            ast "A sex doll?" ("base", "narrow", "angry", "mid")
            ast "That's gross [name_genie_astoria]!" ("upset", "base", "angry", "mid")
            ast "Yuck, it smells gross too!" ("upset", "base", "angry", "mid")
            call ast_mood(2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "A sex doll?" ("base", "narrow", "angry", "mid")
            ast "This is literally worthless to me, why would you even consider this a good gift?" ("upset", "base", "angry", "mid")
            call ast_mood(1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "A sex doll?" ("upset", "base", "angry", "mid")
            call give_gift("You give the doll to Astoria...", gift_item)
            ast "I hope you got this for cheap. It looks awful..." ("annoyed", "narrow", "base", "mid")
            ast "I mean... why thank you, I shall cherish this forever!" ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "A sex doll?" ("base", "narrow", "angry", "mid")
            call give_gift("You give the doll to Astoria...", gift_item)
            ast "But I'm a girl..." ("annoyed", "narrow", "base", "mid")
            ast "I'll leave it in the Slytherin common room to see if anyone has balls, big enough to take it..." ("grin", "base", "angry", "mid")
            call ast_mood(-1)

    elif gift_item == anal_beads_ITEM:
        if states.ast.level < 6:
            ast "Anal beads?" ("base", "narrow", "angry", "mid")
            ast "Like, ones that you putt in your ass?" ("upset", "base", "angry", "mid")
            ast "What... the hell!" ("upset", "base", "angry", "mid")
            call ast_mood(2)
        elif states.ast.level > 5 and states.ast.level < 12:
            ast "Anal beads?" ("base", "narrow", "angry", "mid")
            ast "Put it up your own ass, and I'll let er rip!" ("upset", "base", "angry", "mid")
            call ast_mood(1)
        elif states.ast.level > 11 and states.ast.level < 18:
            ast "Anal beads?" ("base", "narrow", "angry", "mid")
            ast "Why would I need these?" ("annoyed", "narrow", "base", "mid")
            ast "I'll pass..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "Anal beads?" ("base", "base", "base", "mid")
            ast "Looks painful." ("annoyed", "narrow", "base", "mid")
            call give_gift("You give the anal beads to Astoria...", gift_item)
            ast "And they're green... Did you get these made just for me?" ("annoyed", "base", "base", "mid")
            call ast_mood(-1)

    elif gift_item == wine_ITEM:
        if states.ast.level < 6:
            ast "Wine?" ("base", "narrow", "angry", "mid")
            call give_gift("You give the wine to Astoria...", gift_item)
            ast "You're joking, right?" ("annoyed", "narrow", "base", "mid")
            ast "Professor Snape would murder me if he saw me bringing alcohol into the common room." ("upset", "base", "angry", "mid")
            ast "I can't make you shut up after hours even without alcohol in your system..." ("annoyed", "narrow", "base", "mid")
            ast "Such a slimy slithering killjoy..." ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "Wine?" ("smile", "narrow", "base", "mid")
            ast "Well aren't we fancy?" ("base", "base", "base", "mid")
            call give_gift("You give the wine to Astoria...", gift_item)
            ast "This is the real shit. Look at the date on that." ("base", "base", "base", "mid")
            ast "You really are ancient if you bought it new..." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)

    elif gift_item == firewhisky_ITEM:
        if states.ast.level < 6:
            ast "Firewhisky?" ("base", "base", "base", "mid")
            ast "That's the stuff Tonks always reeks off." ("base", "narrow", "angry", "mid")
            ast "I'm not gonna drink whatever she does." ("annoyed", "narrow", "base", "mid")
            ast "It'd be like wearing old people's perfume!" ("annoyed", "narrow", "base", "mid")
            call ast_mood(0)
        else:
            ast "Firewhisky?" ("smile", "narrow", "base", "mid")
            ast "Fine, I'll give in. If Tonks likes it so much, it can't be that bad..." ("smile", "narrow", "base", "mid")
            call give_gift("You give the firewhisky to Astoria...", gift_item)
            ast "*Hmm*... not made using real fire... Well, that's bloody obvious..." ("base", "base", "base", "mid")
            ast "Might experience a slight pain and burning sensation when consuming..." ("base", "narrow", "angry", "mid")
            ast "Why didn't you say so before!" ("upset", "base", "angry", "mid")
            ast "I might even take a sip or two myself..." ("smile", "narrow", "base", "mid")
            call ast_mood(-1)

    ast "" (xpos="base",ypos="base")
    hide astoria_main
    with d5

    return


label ast_mood(value=0):

    if value > 0:
        if value == 1:
            "Astoria's mood worsened slightly."
        else:
            "Astoria's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Astoria's mood has improved slightly."
        else:
            "Astoria's mood has improved significantly."
    else:
        "Astoria's mood hasn't changed."

    $ was_negative = states.ast.mood > 0
    $ states.ast.mood = max(min(states.ast.mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, states.ast.mood, value)

    return
