### Give Cho Gift ###

label give_cho_gift(gift_item):
    hide cho_main
    with d5
    cho "" (xpos="mid", ypos="base", trans=d5)

    $ states.cho.gifted = True

    if gift_item == lollipop_ITEM:
        if states.cho.tier <= 1:
            cho "Sweets?" ("soft", "base", "base", "mid")
            cho "My team captain hasn't let me buy any to keep my blood sugar balanced... Whatever that means." ("open", "narrow", "base", "R")
            call give_gift("You give the sweets to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-2)
        elif states.cho.tier == 2:
            cho "Sweets?" ("soft", "base", "base", "mid")
            call give_gift("You give the sweets to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]... Yes, I do think I deserve one, since we won our first match." ("smile", "narrow", "base", "mid")
            call cho_mood(-2)
        elif states.cho.tier == 3:
            cho "Sweets?" ("soft", "base", "base", "mid")
            cho "But we're up against Gryffindor soon, I don't want to get addicted to sugar..." ("soft", "base", "base", "R")
            call give_gift("You give the sweets to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("open", "base", "base", "mid")
            call cho_mood(-1)
        else:
            cho "Sweets?" ("soft", "base", "base", "mid")
            call give_gift("You give the sweets to Cho...",gift_item)
            cho "I'll keep it for later... I like licking it in front of my teammates to tease them a bit." ("smile", "narrow", "base", "R")
            cho @ cheeks blush "But in the future... I'm more of a savoury kind of girl..." ("base", "narrow", "base", "R")
            cho @ cheeks blush "If you follow my trail..." ("smile", "wink", "base", "mid")
            call cho_mood(-1)

    elif gift_item == chocolate_ITEM:
        if states.cho.tier <= 1:
            cho "Chocolate?" ("soft", "base", "base", "mid")
            cho "I probably shouldn't... Although." ("upset", "narrow", "base", "down")
            call give_gift("You give the chocolate to Cho...",gift_item)
            cho "I'll take it, [name_genie_cho]!" ("smile", "base", "base", "mid")
            call cho_mood(-2)
        elif states.cho.tier == 2:
            cho "Chocolate... Now that would be a treat..." ("open", "base", "base", "down")
            call give_gift("You give the chocolate to Cho...",gift_item)
            cho "What the heck, I deserve it." ("base", "narrow", "base", "mid")
            cho "Thank you, [name_genie_cho]." ("smile", "base", "base", "mid")
            call cho_mood(-2)
        elif states.cho.tier == 3:
            cho "Chocolate?" ("soft", "base", "base", "down")
            cho "But we're up against Gryffindor soon, I don't want to get addicted to sugar..." ("upset", "base", "base", "mid")
            call give_gift("You give the chocolate to Cho...",gift_item)
            cho "Thanks." ("open", "base", "base", "mid")
            call cho_mood(-1)
        else:
            cho "Chocolate?" ("soft", "base", "base", "down")
            call give_gift("You give the chocolate to Cho...",gift_item)
            cho "Yes!" ("grin", "happyCl", "base", "down")
            cho "I've been trying to stay away from it, but since the season is over, I can have as much as I'd like..." ("grin", "narrow", "base", "mid")
            cho "Within reason... of course." ("smile", "narrow", "base", "downR")
            call cho_mood(-2)

    elif gift_item == plush_owl_ITEM:
        if states.cho.tier <= 1:
            cho "A toy?" ("annoyed", "base", "base", "mid")
            call give_gift("You give the stuffed owl to Cho...",gift_item)
            cho "My team would probably laugh if they saw me with this..." ("disgust", "narrow", "base", "mid")
            cho "I'm sorry, but I can't accept this..." ("soft", "narrow", "base", "mid")
            call cho_mood(0)
        elif states.cho.tier == 2:
            cho "A toy?" ("soft", "base", "base", "down")
            call give_gift("You give the stuffed owl to Cho...",gift_item)
            cho "That's very nice of you [name_genie_cho], but I'd probably be made fun of for owning this..." ("annoyed", "base", "base", "mid")
            cho "I guess I could give it to someone." ("open", "base", "base", "R")
            call cho_mood(0)
        elif states.cho.tier == 3:
            cho "A toy?" ("soft", "narrow", "base", "down")
            call give_gift("You give the stuffed owl to Cho...",gift_item)
            cho "I'm not a child, [name_genie_cho]..." ("annoyed", "base", "base", "mid")
            cho "Thank you I guess..." ("open", "narrow", "base", "R")
            call cho_mood(0)
        else:
            cho "A toy?" ("soft", "narrow", "base", "down")
            call give_gift("You give the stuffed owl to Cho...",gift_item)
            cho "Not the kind of Toy I'd like..." ("horny", "narrow", "raised", "mid")
            cho "Thank you I suppose." ("open", "narrow", "base", "mid")
            call cho_mood(0)

    elif gift_item == butterbeer_ITEM:
        if states.cho.tier <= 1:
            cho "Butterbeer?" ("angry", "base", "base", "mid")
            cho "Isn't this supposed to be alcoholic? I'm not supposed to drink during the season..." ("upset", "base", "base", "mid")
            call cho_mood(1)
        elif states.cho.tier == 2:
            cho "Butterbeer?" ("open", "base", "base", "down")
            cho "Yes, I'll take it... Turns out my teammates had been lying about the alcohol content to mess with me." ("base", "narrow", "base", "mid")
            cho "I can't believe they made me miss out on this, for such a long time." ("open", "narrow", "base", "R")
            call give_gift("You give the Butterbeer to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-2)
        elif states.cho.tier == 3:
            cho "Butterbeer?" ("open", "base", "base", "down")
            cho "It's a bit tame, isn't it? I chugged a lot of it after our last win and can't say I felt a buzz even." ("soft", "narrow", "raised", "mid")
            call give_gift("You give the Butterbeer to Cho...",gift_item)
            cho "Thank you, I suppose, [name_genie_cho]." ("soft", "base", "base", "R")
            call cho_mood(0)
        else:
            cho "Butterbeer?" ("soft", "narrow", "raised", "down")
            cho "Don't you have any firewhisky?" ("annoyed", "base", "base", "mid")
            call give_gift("You give the Butterbeer to Cho...",gift_item)
            cho "Thanks, I suppose..." ("open", "narrow", "base", "down")
            call cho_mood(0)

    elif gift_item == science_mag_ITEM:
        if states.cho.tier <= 1:
            cho "Oh, I heard that they put out a new formula for broom polish in this issue." ("smile", "base", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)
        elif states.cho.tier == 2:
            cho "*Hmm*... Broom aerodynamics and how to utilise your opponent's slipstream..." ("open", "narrow", "raised", "down")
            cho "Interesting..." ("smile", "base", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)
        elif states.cho.tier == 3:
            cho "Five steps to modify your brooms legally..." ("soft", "base", "base", "down")
            cho "Sounds useful." ("smile", "base", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)
        else:
            cho "An expert's guide, on how to maintain and store your Quidditch gear." ("base", "narrow", "base", "down")
            cho "Isn't that what a broom closet is for?" ("soft", "wink", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Cho...",gift_item)
            cho "I suppose you learn something new every day... Thank you [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)

    elif gift_item == girls_mag_ITEM:
        if states.cho.tier <= 1:
            cho "Girls magazines, what do you think I am... A gi--" ("angry", "base", "base", "mid")
            cho "I'm good, thank you..." ("soft", "narrow", "base", "R")
            call cho_mood(0)
        elif states.cho.tier == 2:
            cho "Girls magazines?" ("soft", "narrow", "base", "down")
            call give_gift("You give an assortment of rather girly magazines to Cho...",gift_item)
            cho "I don't usually read these types of magazines, the boys used to make fun of me for it." ("annoyed", "narrow", "base", "R")
            cho "But they can't get into the girls' dorm." ("base", "narrow", "base", "R")
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)
        elif states.cho.tier == 3:
            cho "Girls magazines?" ("soft", "base", "base", "down")
            call give_gift("You give an assortment of rather girly magazines to Cho...",gift_item)
            cho "They do have some interesting stuff on skincare I suppose..." ("annoyed", "narrow", "base", "R")
            cho "Thank you, [name_genie_cho]." ("open", "base", "base", "R")
            call cho_mood(-1)
        else:
            cho "Girls magazines?" ("soft", "narrow", "base", "down")
            cho "I suppose I found the article in last month's issue about cultural appropriation interesting..." ("open", "narrow", "base", "downR")
            call give_gift("You give an assortment of rather girly magazines to Cho...",gift_item)
            cho "Don't tell the boys I said that." ("soft", "closed", "base", "mid")
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)

    elif gift_item == adult_mag_ITEM:
        if states.cho.tier <= 1:
            cho "Adult magazines?" ("angry", "wide", "raised", "mid")
            cho "This is highly inappropriate, [name_genie_cho]!" ("angry", "narrow", "raised", "mid")
            cho "Is this the kind of thing you usually give to people?" ("angry", "base", "base", "L")
            call cho_mood(1)
        elif states.cho.tier == 2:
            cho "Adult magazines?" ("soft", "narrow", "base", "down")
            call give_gift("You give an assortment of adult magazines to Cho...",gift_item)
            cho @ cheeks blush "These people do have nice posture..." ("open", "narrow", "base", "down")
            cho @ cheeks blush "I... I guess they could be useful." ("open", "base", "base", "R")
            cho @ cheeks blush "Thank you, [name_genie_cho]." ("open", "closed", "base", "mid")
            call cho_mood(-1)
        elif states.cho.tier == 3:
            cho "Adult magazines?" ("soft", "narrow", "base", "down")
            call give_gift("You give an assortment of adult magazines to Cho...",gift_item)
            cho "They're all so fit in these magazines... Totally my type." ("smile", "narrow", "base", "down")
            cho "Does this one model in the nude?" ("horny", "base", "base", "down")
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)
        else:
            cho @ cheeks blush "Adult magazines?" ("soft", "narrow", "base", "down")
            call give_gift("You give an assortment of adult magazines to Cho...",gift_item)
            cho @ cheeks blush "Wow, look at that guy's abs..." ("horny", "base", "base", "down")
            cho @ cheeks blush "And that girl's... What do you call it?" ("soft", "base", "raised", "down")
            cho @ cheeks blush "Cum-gutters?" ("horny", "narrow", "raised", "down")
            cho @ cheeks blush "Thank you, [name_genie_cho]." ("horny", "narrow", "base", "mid")
            call cho_mood(-2)

    elif gift_item == porn_mag_ITEM:
        if states.cho.tier <= 1:
            cho "What is this!?!" ("angry", "wide", "raised", "mid")
            cho "Porn magazines?" ("open", "wide", "angry", "mid")
            cho "Sir, why would you even think of giving me something like this?" ("scream", "narrow", "angry", "L")
            call cho_mood(3)
        elif states.cho.tier == 2:
            cho @ cheeks blush "What is this?" ("angry", "wide", "base", "down")
            cho @ cheeks blush "Porn magazines? Sir, that's too much..." ("angry", "narrow", "base", "down")
            cho @ cheeks heavy_blush "Is that a snitch in her sna--" ("open", "wide", "raised", "down")
            call cho_mood(2)
        elif states.cho.tier == 3:
            cho @ cheeks blush "What's this?" ("soft", "narrow", "base", "down")
            call give_gift("You give an assortment of porn magazines to Cho...",gift_item)
            cho @ cheeks blush "What's with these positions? Is that a broom handle up her--" ("angry", "base", "base", "down")
            cho @ cheeks blush "Oh my..." ("angry", "base", "base", "down")
            call cho_mood(0)
        else:
            cho @ cheeks blush "Porn magazines?" ("soft", "narrow", "base", "down")
            cho @ cheeks blush "Ooh, are those two doing it on a broom? That's impressive..." ("open", "base", "raised", "down")
            cho @ cheeks blush "[name_genie_cho], this is naughty... Even for you." ("smile", "narrow", "base", "downR")
            cho @ cheeks blush "I've got my eyes on you." ("base", "narrow", "raised", "mid")
            call give_gift("You give an assortment of porn magazines to Cho...",gift_item)
            cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "mid")
            call cho_mood(-3)

    elif gift_item == krum_poster_ITEM:
        if states.cho.tier <= 1:
            cho "A Viktor Krum poster?" ("angry", "base", "base", "mid")
            cho "Professor, he doesn't have his shirt on!" ("angry", "wink", "base", "mid")
            cho @ cheeks blush "That's...{w=0.3} highly inappropriate..." ("angry", "closed", "base", "downR")
            cho "I can't...{w=0.3} I can't accept this." ("upset", "closed", "base", "mid")
            call cho_mood(0)
        elif states.cho.tier == 2:
            cho @ cheeks blush "A Viktor Krum poster?" ("soft", "narrow", "base", "down")
            cho @ cheeks blush "He really is quite muscular isn't he..." ("disgust", "narrow", "base", "down")
            cho @ cheeks blush "I'll use it..." ("smile", "narrow", "base", "down")
            call give_gift("You give the poster to Cho...",gift_item)
            cho @ cheeks blush "As a motivational poster that is!" ("angry", "narrow", "raised", "downR")
            cho @ cheeks blush "Thank you [name_genie_cho]." ("open", "narrow", "base", "R")
            call cho_mood(-2)
        elif states.cho.tier == 3:
            cho "A Viktor Krum poster?" ("soft", "base", "base", "down")
            cho "Wasn't his nudes leaked in Wizard Hunks weekly?" ("open", "base", "raised", "down")
            cho "..." ("angry", "wide", "raised", "mid")
            cho "Not that I'd read such a thing." ("angry", "wide", "base", "downR")
            call give_gift("You give the poster to Cho...",gift_item)
            cho "Thank you [name_genie_cho]." ("angry", "base", "base", "downR")
            call cho_mood(-3)
        else:
            cho @ cheeks blush "A Viktor Krum poster?" ("soft", "narrow", "raised", "down")
            cho @ cheeks blush "But, isn't this almost the same as if he were to be watching me for real?" ("horny", "narrow", "base", "down")
            call give_gift("You give the poster to Cho...",gift_item)
            cho @ cheeks blush "..." ("horny", "narrow", "base", "down")
            cho @ cheeks blush "I love it, [name_genie_cho]." ("smile", "narrow", "base", "mid")
            call cho_mood(-5)

    elif gift_item == sexy_lingerie_ITEM:
        if states.cho.tier <= 1:
            cho "Lingerie?" ("open", "narrow", "raised", "down")
            cho "Sir, are you expecting me to wear this?" ("open", "wide", "raised", "mid")
            cho "Are you insane?!" ("disgust", "narrow", "angry", "mid")
            cho "No, thank you..." ("open", "base", "angry", "down")
            call cho_mood(2)
        elif states.cho.tier == 2:
            cho "Lingerie?" ("annoyed", "narrow", "base", "down")
            cho "Why would I want this? I have plenty of clothes I like already..." ("soft", "narrow", "raised", "mid")
            cho "I'll pass on that one, thanks." ("open", "base", "base", "R")
            call cho_mood(0)
        elif states.cho.tier == 3:
            cho "Lingerie?" ("soft", "narrow", "base", "down")
            cho "Seems pretty flexible. I might be able to use these when stretching." ("base", "narrow", "base", "down")
            call give_gift("You give the lingerie to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-2)
        else:
            cho @ cheeks blush "Lingerie?" ("soft", "narrow", "raised", "down")
            cho @ cheeks blush "very sexy... Did you pick them out yourself?" ("base", "wink", "base", "mid")
            cho @ cheeks blush "You've got good taste... I tore mine during the ball last year..." ("smile", "narrow", "base", "R")
            cho @ cheeks blush "That's what I get for thinking they'd fit, even after doing so many squats, I suppose..." ("smile", "narrow", "base", "mid")
            call give_gift("You give the lingerie to Cho...",gift_item)
            cho @ cheeks blush "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-3)

    elif gift_item == sexy_stockings_ITEM :
        if states.cho.tier <= 1:
            cho "Stockings?" ("soft", "narrow", "raised", "down")
            cho "Surely that must be against some kind of dress code..." ("open", "wide", "raised", "mid")
            cho "I'll pass..." ("open", "base", "angry", "down")
            cho "" ("annoyed", "base", "base", "mid")
            call cho_mood(1)
        elif states.cho.tier == 2:
            cho "Stockings?" ("annoyed", "narrow", "base", "down")
            cho "I guess I won't get sunburnt on my legs wearing these..." ("open", "narrow", "base", "mid")
            call give_gift("You give the lingerie to Cho...",gift_item)
            cho "Thank you [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)
        elif states.cho.tier == 3:
            cho @ cheeks blush "Stockings?" ("soft", "narrow", "base", "down")
            cho @ cheeks blush "I can almost see right through these..." ("soft", "narrow", "base", "down")
            call give_gift("You give the lingerie to Cho...",gift_item)
            cho @ cheeks blush "Thank you, [name_genie_cho]." ("open", "narrow", "base", "downR")
            call cho_mood(-2)
        else:
            cho "Stockings?" ("soft", "narrow", "base", "down")
            cho "But my legs get too itchy in these, I'd rather go without any leggings..." ("disgust", "narrow", "base", "mid")
            call cho_mood(0)

    elif gift_item == pink_condoms_ITEM:
        if states.cho.tier <= 1:
            cho "Condoms?" ("angry", "narrow", "base", "down")
            cho "Yes, why don't I use these and have sex with the teachers... That's what you want, right?" ("disgust", "narrow", "raised", "R")
            cho "I think you're confusing me with those Slytherin skanks who impale themselves on the daily." ("angry", "narrow", "base", "mid")
            cho "So, you can have these back and give it to them..." ("soft", "narrow", "angry", "mid")
            call cho_mood(2)
        elif states.cho.tier == 2:
            cho "Condoms?" ("angry", "base", "base", "down")
            cho "I'm not the kind of girl to walk around and bang anyone who cross my path..." ("open", "closed", "angry", "mid")
            cho "Thanks but no, thanks..." ("disgust", "narrow", "base", "R")
            call cho_mood(1)
        elif states.cho.tier == 3:
            cho @ cheeks blush "Condoms?" ("soft", "narrow", "base", "down")
            cho @ cheeks blush "Are you expecting that I'll need these?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "*Ehm*..." ("upset", "closed", "base", "down")
            call cho_mood(0)
        else:
            cho "Condoms?" ("soft", "narrow", "base", "down")
            call give_gift("You give a pack of condoms to Cho...", gift_item)
            cho @ cheeks blush "I thought you said we didn't need these?" ("soft", "narrow", "raised", "mid")
            cho @ cheeks blush "Although, perhaps we could find some use for them..." ("smile", "narrow", "base", "downR")
            call cho_mood(-2)

    elif gift_item == vibrator_ITEM:
        if states.cho.tier <= 1:
            cho "A vibrator?" ("mad", "base", "base", "down")
            cho "Sir, are you out of your mind?" ("disgust", "wide", "raised", "mid")
            cho "I'm your student for crying out loud... Giving gifts in general is a bit weird, but sex toys..." ("angry", "wide", "base", "mid")
            cho @ cheeks blush "Seriously?!" ("mad", "narrow", "base", "mid")
            call cho_mood(3)
        elif states.cho.tier == 2:
            cho @ cheeks blush "A vibrator?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "Why would you give me this?" ("disgust", "narrow", "base", "mid")
            cho @ cheeks blush "Give it to Granger... I'm sure she'd love to accept a sex toy from her headmaster." ("disgust", "narrow", "angry", "mid")
            call cho_mood(2)
        elif states.cho.tier == 3:
            cho @ cheeks blush "A vibrator?" ("soft", "narrow", "base", "down")
            cho @ cheeks blush "Sir, I don't think this would be appropriate to bring to my dorm..." ("upset", "narrow", "base", "mid")
            cho @ cheeks blush "The girls... They'd hear it... Not that I want it or anything!" ("horny", "narrow", "base", "R")
            call cho_mood(0)
        else:
            cho @ cheeks heavy_blush "A Vibrator?" ("open", "narrow", "base", "down")
            call give_gift("You give the vibrator to Cho...", gift_item)
            cho @ cheeks heavy_blush "*Hmm*... It does promote a healthy lifestyle..." ("base", "narrow", "base", "down")
            cho @ cheeks heavy_blush "Thank you, [name_genie_cho]." ("smile", "base", "base", "mid")
            call cho_mood(-3)

    elif gift_item == anal_lube_ITEM:
        if states.cho.tier <= 1:
            cho "Lubricant?" ("mad", "base", "base", "down")
            cho "What the hell, why do you think this is an appropriate gift? What's wrong with you..." ("angry", "wide", "raised", "mid")
            call cho_mood(4)
        elif states.cho.tier == 2:
            cho @ cheeks blush "Lubricant?" ("angry", "base", "base", "down")
            cho "*Eww*... Why are you giving me this? When would I ever have the need for lube?" ("angry", "narrow", "base", "down")
            cho "Give it to one of those Slytherin skanks, they probably go through a gallon every week." ("disgust", "closed", "angry", "mid")
            call cho_mood(3)
        elif states.cho.tier == 3:
            cho @ cheeks blush "Lubricant?" ("angry", "narrow", "base", "down")
            if states.cho.ev.quidditch.e12_complete:
                cho @ cheeks blush "Yes, I suppose this could be useful..." ("soft", "narrow", "raised", "mid")
                call cho_mood(-3)
            else:
                cho @ cheeks blush "Why would I need something like this?" ("soft", "narrow", "raised", "mid")
                call cho_mood(0)
        else:
            cho @ cheeks heavy_blush "Anal Lubricant?" ("soft", "base", "base", "down")
            call give_gift("You give the jar of anal lube to Cho...", gift_item)
            cho @ cheeks heavy_blush "You should've given me this yesterday, [name_genie_cho]." ("smile", "wink", "base", "mid")
            cho @ cheeks heavy_blush "I haven't been able to sit on a broom properly, not since my last flying session..." ("horny", "closed", "base", "mid")
            call cho_mood(-5)

    elif gift_item == ballgag_and_cuffs_ITEM:
        if states.cho.tier <= 1:
            cho "A ball gag... and cuffs?" ("soft", "narrow", "raised", "down")
            cho "Wait, is this a sex thing?" ("soft", "wide", "raised", "mid")
            cho "Professor, that's disgusting... Why would you give me this?" ("angry", "wide", "angry", "mid")
            call cho_mood(4)
        elif states.cho.tier == 2:
            cho @ cheeks blush "A ball gag and cuffs?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "Sir, this is a highly inappropriate gift to give to a student!" ("mad", "narrow", "base", "mid")
            cho @ cheeks blush "Why would you give me these? Are they supposed to help me with Quidditch?" ("disgust", "narrow", "base", "mid")
            call cho_mood(3)
        elif states.cho.tier == 3:
            cho @ cheeks blush "A ball gag and cuffs?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "I prefer not to lock myself up... I'm a free spirit." ("annoyed", "narrow", "base", "R")
            cho @ cheeks blush "Thanks... But no, thanks." ("soft", "base", "base", "R")
            call cho_mood(0)
        else:
            cho @ cheeks heavy_blush "A ball gag and cuffs?" ("soft", "narrow", "base", "down")
            call give_gift("You give the ball gag and cuffs to Cho...", gift_item)
            cho @ cheeks heavy_blush "How progressive... Do they require a safe-word to open?" ("horny", "narrow", "base", "down")
            cho @ cheeks heavy_blush "Wait, how would a safe-word work when you have a ball in your mouth..." ("disgust", "narrow", "base", "down")
            call cho_mood(-3)

    elif gift_item == anal_plugs_ITEM:
        if states.cho.tier <= 1:
            cho "Anal plugs?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "That's disgusting... Why would you think it'd be a good idea to give these to me?" ("disgust", "base", "angry", "down")
            cho @ cheeks heavy_blush "That one even has a tail on it..." ("disgust", "narrow", "raised", "down")
            call cho_mood(4)
        elif states.cho.tier == 2:
            cho @ cheeks blush "Anal plugs?" ("disgust", "narrow", "base", "down")
            cho "Why do you have these? They're not used, are they?" ("angry", "narrow", "raised", "mid")
            cho @ cheeks blush "*Eww*... Just, no." ("disgust", "closed", "angry", "mid")
            cho "" ("annoyed", "base", "base", "mid")
            call cho_mood(3)
        elif states.cho.tier == 3:
            cho @ cheeks blush "Anal plugs?" ("angry", "base", "base", "down")
            cho "Sir, are you expecting me to wear this?" ("angry", "base", "base", "mid")
            cho "During Quidditch?" ("angry", "wide", "raised", "mid")
            cho "No, no, no, noooo." ("open", "happyCl", "raised", "mid")
            cho "NO!" ("angry", "closed", "angry", "mid")
            call cho_mood(2)
        else:
            cho @ cheeks heavy_blush "Anal plugs?" ("soft", "narrow", "base", "down")
            call give_gift("You give a set of anal plugs to Cho...", gift_item)
            cho @ cheeks heavy_blush "I suppose I could use one and plug both holes when I'm riding [states.cho.ev.quidditch.broom_name]..." ("base", "narrow", "base", "down")
            cho @ cheeks heavy_blush "Then all that is left is a ball gag..." ("smile", "base", "base", "mid")
            cho @ cheeks heavy_blush "I'm joking, of course..." ("smile", "narrow", "base", "R")
            call cho_mood(-2)

    elif gift_item == testral_strapon_ITEM:
        if states.cho.tier <= 1:
            cho "Is that a strap-on?" ("angry", "wide", "base", "down")
            cho "It's huge!" ("mad", "narrow", "raised", "down")
            cho @ cheeks blush "I mean, why are you showing me this?" ("angry", "narrow", "raised", "R")
            cho @ cheeks blush "Get it away from me." ("angry", "narrow", "base", "mid")
            call cho_mood(3)
        elif states.cho.tier == 2:
            cho "A strap-on?" ("open", "wide", "worried", "down")
            cho "Why are you giving me this?" ("angry", "wide", "base", "mid")
            cho "That's disgusting..." ("disgust", "narrow", "base", "mid")
            call cho_mood(2)
        elif states.cho.tier == 3:
            cho @ cheeks blush "A strap-on?" ("open", "wide", "base", "down")
            cho @ cheeks blush "But it's so big..." ("horny", "wide", "raised", "mid")
            cho @ cheeks heavy_blush "I... I don't want it..." ("open", "closed", "base", "down")
            call cho_mood(0)
        else:
            cho @ cheeks heavy_blush "A strap-on?" ("open", "narrow", "base", "down")
            call give_gift("You give the thestral strap-on to Cho...", gift_item)
            cho @ cheeks heavy_blush "I've always-- *Ahem*..." ("soft", "narrow", "base", "down")
            cho @ cheeks heavy_blush "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)

    elif gift_item == broom_2000_ITEM:
        $ states.cho.ev.quidditch.given_thestral = True

        if states.cho.tier <= 1:
            cho "A broom! Finally, something better than my old--" ("smile", "base", "base", "down")
            cho "Hold on, is that a double ended dildo sticking out of it?!?" ("angry", "wide", "base", "down")
            cho "What's wrong with you?" ("scream", "happyCl", "base", "mid")
            cho "Get that away from my--{w=0.4} From me!" ("angry", "narrow", "base", "mid")
            call cho_mood(4)
        elif states.cho.tier == 2:
            cho "Is that a broom with dildos stuck to it?" ("disgust", "wide", "base", "down")
            cho "Professor, seriously... Why... Just why." ("angry", "narrow", "base", "mid")
            call cho_mood(2)
        elif states.cho.tier == 3:
            cho "A broom?" ("smile", "base", "base", "down")
            cho @ cheeks blush "A sex broom! Where did you even get this..." ("open", "wide", "base", "down")
            cho @ cheeks blush "No...{w=0.3} I don't--{w=0.3} I don't want that." ("horny", "narrow", "base", "mid")
            call cho_mood(0)
        else:
            cho @ cheeks heavy_blush "Is that a Lady Speed Stick-2000, with a built-in vibrator and pulse function?" ("angry", "wide", "base", "down")
            call give_gift("You give the broom to Cho...", gift_item)
            cho @ cheeks heavy_blush "I mean..." ("angry", "wide", "base", "mid")
            cho @ cheeks heavy_blush "Thank you, [name_genie_cho]..." ("angry", "base", "base", "stare")
            cho @ cheeks heavy_blush "I can't wait to learn more about it..." ("angry", "closed", "base", "mid")
            call cho_mood(-6)

    elif gift_item == sexdoll_ITEM:
        if states.cho.tier <= 1:
            cho @ cheeks blush "A sex doll? What the heck... Why do you have this?" ("angry", "base", "base", "down")
            cho @ cheeks blush "And more importantly..." ("angry", "closed", "base", "mid")
            cho @ cheeks blush "{size=+4}Why are you giving it to me?{/size}" ("disgust", "wide", "angry", "mid")
            cho @ cheeks blush "You disgust me..." ("upset", "closed", "angry", "mid")
            call cho_mood(4)
        elif states.cho.tier == 2:
            cho @ cheeks blush "A sex doll?" ("disgust", "narrow", "base", "down")
            cho @ cheeks blush "Why would you give this to me? Wait, did you use this?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "Get it away from me..." ("upset", "happyCl", "angry", "L")
            call cho_mood(3)
        elif states.cho.tier == 3:
            cho @ cheeks blush "A sex doll?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "Why would I need this... It's a girl doll." ("disgust", "narrow", "base", "mid")
            cho @ cheeks blush "I mean, why would I need a sex doll in general... I'm not into this sort of thing!" ("angry", "closed", "base", "mid")
            call cho_mood(1)
        else:
            cho @ cheeks heavy_blush "A sex doll?" ("soft", "narrow", "raised", "down")
            call give_gift("You give the sex doll to Cho...", gift_item)
            cho @ cheeks heavy_blush "It says Joanne on it..." ("base", "narrow", "base", "down")
            cho @ cheeks heavy_blush "I'll leave it in the boys' changing room... Should make a good reward after practice." ("base", "wink", "base", "mid")
            call cho_mood(-7)

    elif gift_item == anal_beads_ITEM:
        if states.cho.tier <= 1:
            cho "Anal beads?" ("angry", "wide", "base", "down")
            cho @ cheeks blush "Yeah, that's not going anywhere near their intended target..." ("disgust", "base", "angry", "downR")
            call cho_mood(4)
        elif states.cho.tier == 2:
            cho @ cheeks blush "Anal beads?" ("soft", "narrow", "worried", "down")
            cho @ cheeks blush "How... Where did you..." ("angry", "narrow", "raised", "down")
            cho @ cheeks blush "Gross!" ("open", "happyCl", "angry", "mid")
            cho "" ("annoyed", "base", "base", "mid")
            call cho_mood(3)
        elif states.cho.tier == 3:
            cho @ cheeks blush "Anal beads?" ("angry", "narrow", "base", "down")
            cho @ cheeks blush "Sir, how would ever be able to sit on a broom after using these?" ("disgust", "narrow", "angry", "mid")
            cho @ cheeks blush "Not that I would ever use them!" ("angry", "narrow", "raised", "R")
            cho @ cheeks blush "*Ahem*..." ("open", "narrow", "raised", "downR")
            call cho_mood(2)
        else:
            cho @ cheeks heavy_blush "Anal beads?" ("soft", "narrow", "base", "down")
            call give_gift("You give the anal beads to Cho...", gift_item)
            cho @ cheeks heavy_blush "Surely my butt would hurt after using these..." ("upset", "base", "base", "down")
            cho @ cheeks heavy_blush "Although I do have a cushioning charm on my broom for a reason..." ("horny", "narrow", "base", "down")
            cho @ cheeks heavy_blush "Thank you, [name_genie_cho]." ("smile", "narrow", "base", "mid")
            call cho_mood(-2)

    elif gift_item == wine_ITEM:
        if states.cho.tier <= 2:
            cho "A bottle of wine?" ("soft", "narrow", "raised", "down")
            cho "[name_genie_cho], I cannot drink alcohol, it would ruin my career..." ("angry", "narrow", "base", "mid")
            call cho_mood(4)
        elif states.cho.tier <= 3:
            cho "A bottle of wine?" ("soft", "narrow", "raised", "down")
            cho "Thank you, [name_genie_cho] but I can't take it." ("open", "closed", "base", "mid")
            cho "{size=-4}Although I probably would, if I were to win the Quidditch Cup...{/size}" ("base", "narrow", "base", "R")
            call cho_mood(0)
        else:
            cho "A bottle of wine?" ("soft", "narrow", "raised", "down")
            cho "Well, I suppose I've deserved to let loose a bit." ("smile", "base", "base", "mid")
            call give_gift("You give the sweets to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)

    elif gift_item == firewhisky_ITEM:
        if states.cho.tier <= 2:
            cho "Firewhisky?" ("soft", "narrow", "raised", "down")
            cho "Why would you give me that?" ("angry", "narrow", "base", "mid")
            call cho_mood(4)
        elif states.cho.tier <= 3:
            cho "Firewhisky?" ("soft", "narrow", "base", "down")
            cho "Thank you, [name_genie_cho] but I can't take it." ("open", "closed", "base", "mid")
            cho "{size=-4}Although I probably would, if I were to win the Quidditch Cup...{/size}" ("base", "base", "base", "mid")
            call cho_mood(0)
        else:
            cho "Firewhisky?" ("soft", "narrow", "raised", "down")
            cho "Well, I suppose I've deserved to let loose a bit." ("smile", "base", "base", "mid")
            call give_gift("You give the sweets to Cho...",gift_item)
            cho "Thank you, [name_genie_cho]." ("base", "base", "base", "mid")
            call cho_mood(-1)

    cho "" (xpos="base", ypos="base")
    hide cho_main
    with d5

    return

label cho_mood(value=0):

    if value > 0:
        if value == 1:
            "Cho's mood worsened slightly."
        else:
            "Cho's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Cho's mood has improved slightly."
        else:
            "Cho's mood has improved significantly."
    else:
        "Cho's mood hasn't changed."

    $ was_negative = states.cho.mood > 0
    $ states.cho.mood = max(min(states.cho.mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, states.cho.mood, value)

    return
