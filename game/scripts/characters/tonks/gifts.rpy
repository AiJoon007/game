### Give Tonks Gift ###

label give_ton_gift(gift_item):
    hide tonks_main
    with d5
    ton "" (xpos="mid", ypos="base", trans=d5)

    $ states.ton.gifted = True

    if gift_item == lollipop_ITEM:
        ton "A lollipop?" ("open", "narrow", "base", "down")
        call give_gift("You give the lollipop to Tonks...", gift_item)
        ton "I know the perfect student to give this to." ("base", "narrow", "base", "R")
        call ton_friendship(1)

    elif gift_item == chocolate_ITEM:
        ton "*Mhmm*, Chocolate!" ("horny", "narrow", "base", "down")
        call give_gift("You give the chocolate to Tonks...", gift_item)
        ton "It's known that chocolate is a very effective mood enhancer after a Dementor attack." ("open", "closed", "base", "mid")
        ton "Although it's less known that it's because chocolate is considered to be a great aphrodisiac..." ("base", "narrow", "base", "mid")
        ton "I'll keep this for one of my private lessons." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == plush_owl_ITEM:
        ton "An Owl?" ("open", "narrow", "base", "down")
        ton "Oh, it's a toy... Haven't seen one of these in a while." ("soft", "narrow", "base", "mid")
        call give_gift("You give the stuffed owl to Tonks...",gift_item)
        ton "Okay, for nostalgia's sake then..." ("open", "closed", "base", "mid")
        call ton_friendship(0)

    elif gift_item == butterbeer_ITEM:
        ton "Butterbeer?" ("open", "narrow", "base", "down")
        ton "Don't you have anything stronger?" ("upset", "narrow", "base", "mid")
        call give_gift("You give the bottle to Tonks...", gift_item)
        ton "Just joking, I'll save it for when I've got company." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == science_mag_ITEM:
        ton "Jinxes and sphinxes? These could help with some of my lessons." ("open", "narrow", "base", "down")
        call give_gift("You give an assortment of educational magazines to Tonks...", gift_item)
        ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == girls_mag_ITEM:
        ton "Some girl magazines? I could definitely put these in my classroom." ("open", "narrow", "base", "down")
        call give_gift("You give an assortment of rather girly magazines to Tonks...", gift_item)
        ton "The girls do love staying after hours to socialise." ("base", "wink", "base", "mid")
        ton "" ("base", "base", "base", "mid")
        call ton_friendship(0)

    elif gift_item == adult_mag_ITEM:
        ton "Adult magazines?" ("open", "narrow", "base", "down")
        ton "Won't be the first time I've slipped one of these inside the stack of magazines in my classroom." ("base", "wink", "base", "mid")
        call give_gift("You give an assortment of adult magazines to Tonks...", gift_item)
        ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == porn_mag_ITEM:
        ton "Porn magazines?" ("open", "narrow", "base", "down")
        ton "I already know most positions in this book already of course..." ("base", "base", "base", "mid")
        call give_gift("You give an assortment of pornographic magazines to Tonks...", gift_item)
        ton "Although..." ("horny", "narrow", "base", "down")
        ton "I'll gladly accept them anyway... Thank you, [name_genie_tonks]." ("base", "wink", "base", "mid")
        ton "" ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == krum_poster_ITEM:
        ton "That's that Krum boy, isn't it?" ("open", "narrow", "base", "down")
        call give_gift("You give the poster to Tonks...", gift_item)
        ton "Nice figure... Yes, this would certainly set a good mood in my classroom... Or my office." ("base", "narrow", "base", "down")
        ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == sexy_lingerie_ITEM:
        ton "I see you're a man with a sense of style." ("open", "narrow", "base", "down")
        call give_gift("You give the sexy lingerie to Tonks...", gift_item)
        ton "If it were up to me, then a pair of these would be an obligatory part of the female school uniform..." ("horny", "wink", "base", "mid")
        ton "" ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == sexy_stockings_ITEM :
        ton "Nice... I have a pair just like these." ("open", "narrow", "base", "down")
        ton "Although another pair without holes in them won't hurt..." ("horny", "wink", "base", "mid")
        call give_gift("You give the sexy stockings to Tonks...", gift_item)
        ton "" ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == pink_condoms_ITEM:
        ton "Some condoms?" ("open", "narrow", "base", "down")
        call give_gift("You give some condoms to Tonks...", gift_item)
        ton "Safe sex is important..." ("horny", "wink", "base", "mid")
        ton "*Hmm*... Now that I think about it, I don't remember taking sex ed when I was in school..." ("annoyed", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == vibrator_ITEM:
        ton "A vibra--ting back massager?" ("open", "narrow", "base", "down")
        ton "*Mmm*... Mine seemingly went missing from my desk..." ("annoyed", "narrow", "base", "mid")
        ton "It's a bit small, but this should do until it turns up again." ("horny", "wink", "base", "mid")
        call give_gift("You give the vibrator to Tonks...", gift_item)
        ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == anal_lube_ITEM:
        ton "Now that's a big jar of Anal lube you have there." ("open", "narrow", "base", "down")
        call give_gift("You give the jar of lube to Tonks...", gift_item)
        ton "Looks like this might be enough to cover the entire body..." ("soft", "narrow", "base", "mid")
        ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == ballgag_and_cuffs_ITEM:
        ton "Ball gag and cuffs?" ("open", "narrow", "base", "down")
        call give_gift("You give the ball gag and cuffs to Tonks...", gift_item)
        ton "These are pretty cute. Should come in handy during my.... private lessons." ("horny", "wink", "base", "mid")
        ton "Thank you, [name_genie_tonks]." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == anal_plugs_ITEM:
        ton "Some anal plugs?" ("open", "narrow", "base", "down")
        ton "Wow... This is what they use these days?" ("soft", "narrow", "base", "down")
        ton "Very colourful..." ("base", "narrow", "base", "down")
        call give_gift("You give the assortment of anal plugs to Tonks...", gift_item)
        ton "Thank you, [name_genie_tonks]." ("horny", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == testral_strapon_ITEM:
        ton "Is that a strap-on?" ("open", "narrow", "base", "down")
        call give_gift("You give the thestral strap-on to Tonks...", gift_item)
        ton "This will be a perfect addition to my collection..." ("horny", "base", "angry", "mid")
        ton "Thank you, [name_genie_tonks]." ("base", "happyCl", "base", "mid")
        ton "" ("base", "base", "base", "mid")
        call ton_friendship(2)

    elif gift_item == broom_2000_ITEM:
        ton "I don't remember the brooms looking like this when I took flying lessons..." ("open", "narrow", "base", "down")
        call give_gift("You give the broom to Tonks...", gift_item)
        ton "Seems like a good way to stay put on the broom though... Unless you lose focus." ("horny", "base", "base", "mid")
        ton "Thank you, [name_genie_tonks]." ("base", "narrow", "base", "mid")
        ton "" ("base", "base", "base", "mid")
        call ton_friendship(3)

    elif gift_item == sexdoll_ITEM:
        ton "A sex doll?" ("open", "narrow", "base", "down")
        ton "Not too useful for me, but I might put it in one of our secret gift exchanges." ("horny", "narrow", "base", "R")
        call give_gift("You give the sex doll to Tonks...", gift_item)
        ton "They'll gossip for weeks, wondering who it's from." ("grin", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == anal_beads_ITEM:
        ton "Anal beads?" ("open", "narrow", "base", "down")
        ton "It's a bit short, but I'll take it..." ("horny", "narrow", "base", "down")
        call give_gift("You give the anal beads to Tonks...", gift_item)
        ton "Thank you, [name_genie_tonks]..." ("base", "base", "base", "mid")
        call ton_friendship(1)

    elif gift_item == wine_ITEM:
        ton "A bottle of wine?" ("open", "narrow", "base", "down")
        if not firewhisky_ITEM.unlocked:
            ton "I was hoping for something with a bit more \'punch\'." ("annoyed", "narrow", "base", "mid")
            call ton_friendship(0)
        else:
            ton "I've told you before... Wine doesn't particularly agree with me." ("annoyed", "narrow", "base", "mid")
            call ton_friendship(0)

    elif gift_item == firewhisky_ITEM:
        ton "Firewhisky?" ("open", "narrow", "base", "down")
        ton "*Mmm*... My favourite..." ("horny", "narrow", "base", "down")
        ton "But let's save it for later, shall we?" ("base", "narrow", "base", "mid")
        call ton_friendship(0)

    ton "" (xpos="base",ypos="base")
    hide tonks_main
    with d5

    return

label ton_friendship(value=0):

    if value > 0:
        if value == 1:
            "Tonks likes you a bit more now."
        else:
            "Tonks likes you more now."
    elif value < 0:
        if value == -1:
            "Tonks didn't seem to like that."
        else:
            "Tonks likes you a bit less now."
    else:
        "Tonks' friendship towards you hasn't changed much."

    $ states.ton.level = max(min(states.ton.level+value, 100), 0)
    return
