
# Hermione Gift Responses

label give_her_gift(gift_item):
    hide hermione_main
    with d5
    her "" (xpos="mid",ypos="base",trans=d5)

    $ states.her.gifted = True

    if gift_item == lollipop_ITEM:
        if states.her.level < 6:
            her "A lollipop?" ("base", "base", "base", "mid")
            call give_gift("You give the lollipop to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-5)
        elif states.her.level < 12:
            her "A lollipop?" ("normal", "base", "base", "mid")
            her "Sweets are for kids, [name_genie_hermione]." ("open", "base", "base", "mid")
            call give_gift("You give the lollipop to Hermione...",gift_item)
            her "Thank you..." ("annoyed", "base", "worried", "R")
            call her_mood(-5)
        elif states.her.level < 18:
            her "A lollipop?" ("normal", "base", "base", "mid")
            call give_gift("You give the lollipop to Hermione...",gift_item)
            her "*Ehm*... Sure, thanks..." ("open", "squint", "base", "mid")
            call her_mood(-5)
        else:
            her "A lollipop?" ("base", "base", "base", "mid")
            her "Clever girls use sweets like these as a \"weapon\"." ("smile", "base", "base", "R")
            call give_gift("You give the lollipop to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "happyCl", "base", "mid")
            call her_mood(-5)

    elif gift_item == chocolate_ITEM:
        if states.her.level < 6:
            her "A chocolate bar?" ("base", "base", "base", "mid")
            call give_gift("You give the chocolate to Hermione...", gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-10)
        elif states.her.level < 12:
            her "A chocolate bar?" ("normal", "base", "base", "mid")
            her "*Hmm*..." ("annoyed", "squint", "angry", "mid")
            her "That thing about fairies..." ("annoyed", "squint", "angry", "mid")
            her "That is a joke of some sort, right?" ("open", "base", "worried", "mid")
            call give_gift("You give the chocolate to Hermione...", gift_item)
            her "Thank you..." ("soft", "base", "base", "mid")
            call her_mood(-10)
        elif states.her.level < 18:
            her "A chocolate bar?" ("normal", "base", "base", "mid")
            her "I just like the way it crunches, [name_genie_hermione]! N-not the taste..." ("grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give the chocolate to Hermione...", gift_item)
            her "*Ehm*... Sure, thanks..." ("base", "base", "base", "mid")
            call her_mood(-10)
        else: # Lv 7+
            her "A chocolate bar?" ("base", "base", "base", "mid")
            her "You spoil me, [name_genie_hermione]." ("smile", "base", "angry", "mid")
            call give_gift("You give the chocolate to Hermione...", gift_item)
            her "Thank you." ("base", "squint", "base", "mid")
            call her_mood(-10)

    elif gift_item == plush_owl_ITEM:
        if states.her.level < 6:
            her "A stuffed owl?" ("base", "base", "base", "mid")
            her "It's cute..." ("base", "base", "base", "mid")
            call give_gift("You give the owl to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-7)
        elif states.her.level < 12:
            her "A plush toy?" ("open", "base", "worried", "mid")
            her "I like it!" ("base", "base", "base", "mid")
            call give_gift("You give the owl to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-10)
        elif states.her.level < 18:
            her "A toy?" ("base", "base", "base", "mid")
            her "Toys are for kids, [name_genie_hermione]." ("open", "base", "base", "mid")
            her "But I'll take it..." ("annoyed", "base", "worried", "R")
            call give_gift("You give the owl to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-15)
        else:
            her "This is one of those adult toys, isn't it?" ("disgust", "narrow", "base", "mid_soft")
            her "There's got to be a switch or a button somewhere..." ("open", "narrow", "worried", "down")
            her "So... Does it vibrate or something?" ("base", "narrow", "worried", "down")
            her @ cheeks blush "Oh...?" ("open", "happy", "base", "mid")
            her "So it is really just a plush toy then?" ("open", "happy", "base", "mid")
            her "Shame..." ("angry", "narrow", "base", "down")
            her "I mean, thank you, [name_genie_hermione]." ("angry", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give the owl to Hermione...",gift_item)
            call her_mood(-4)

    elif gift_item == butterbeer_ITEM:
        if states.her.level < 6:
            her "Butterbeer?" ("base", "base", "base", "mid")
            her "Are you sure about that, [name_genie_hermione]?" ("open", "squint", "base", "mid")
            her "It does contain alcohol, you know..." ("base", "base", "base", "mid")
            call give_gift("You give the bottle to Hermione...",gift_item)
            her "Thank you." ("base", "base", "base", "mid")
            call her_mood(-3)
        elif states.her.level < 12:
            her "Butterbeer, [name_genie_hermione]?" ("open", "base", "worried", "mid")
            her "To let you in on a little secret, [name_genie_hermione]..." ("open", "base", "base", "mid")
            her "I'm a big fan of this completely harmless beverage." ("base", "base", "base", "mid")
            call give_gift("You give the bottle to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-10)
        elif states.her.level < 18:
            her "Butterbeer?" ("base", "base", "base", "mid")
            her "Thank you, [name_genie_hermione]." ("grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give the bottle to Hermione...",gift_item)
            her "I shall drink this with the girls later." ("base", "base", "base", "mid")
            call her_mood(-15)
        else:
            her "Butterbeer...?" ("base", "base", "base", "mid")
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call give_gift("You give the bottle to Hermione...",gift_item)
            her "I shall drink this later with the boys." ("base", "base", "base", "mid")
            her @ cheeks blush "*Err*... I meant to say with the girls, of course." ("open", "base", "base", "R")
            call her_mood(-20)

    elif gift_item == science_mag_ITEM:
        if states.her.level < 6:
            her "\"Popular magic\" magazines?" ("base", "base", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]!" ("base", "base", "base", "mid")
            her "I will use them for my research!"
            call her_mood(-15)
        elif states.her.level < 12:
            her "Sometimes I find information in magazines that I could never find in a book..." ("base", "base", "base", "mid")
            call give_gift("You give an assortment of educational magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]!" ("base", "base", "base", "mid")
            her "I will use them for my research!"
            call her_mood(-10)
        elif states.her.level < 18:
            her "Oh..." ("open", "base", "base", "mid")
            her "Yes, I used to read magazines like that a lot..." ("base", "base", "base", "mid")
            her "Lately not so much though..." ("open", "base", "worried", "R")
            call give_gift("You give an assortment of educational magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]!" ("base", "base", "base", "mid")
            call her_mood(-3)
        else:
            her "*Ehm*..." ("open", "base", "worried", "R")
            her "To be honest, magazines like that lost their appeal to me completely lately..." ("open", "squint", "base", "mid")
            her "But I don't mind taking them off your hands anyway, [name_genie_hermione]." ("open", "base", "worried", "mid")
            call give_gift("You give an assortment of educational magazines to Hermione...",gift_item)
            her "Thank you." ("soft", "base", "base", "R")
            call her_mood(0)

    elif gift_item == girls_mag_ITEM:
        if states.her.level < 6:
            her "*Hmm*?" ("soft", "base", "base", "mid")
            her "This is the sort of press some Slytherin bimbo would appreciate." ("annoyed", "squint", "base", "mid")
            her "I am way above silly magazines like that, [name_genie_hermione]." ("open", "closed", "base", "mid")
            call her_mood(0)
        elif states.her.level < 12:
            her "I don't read magazines of that nature, [name_genie_hermione]..." ("open", "closed", "angry", "mid")
            her "................" ("soft", "base", "base", "R")
            her "But I could give it a try just to humour you I suppose..." ("open", "closed", "angry", "mid")
            call give_gift("You give an assortment of rather girly magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]!" ("open", "squint", "base", "mid")
            call her_mood(-5)
        elif states.her.level < 18:
            her "I'm ashamed to admit this, but..." ("open", "base", "worried", "R")
            her "I really enjoy reading magazines like that lately..." ("grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give an assortment of rather girly magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("open", "squint", "base", "mid")
            call her_mood(-15)
        else:
            her "The Latest edition of \"Girlz\"?!" ("angry", "wide", "base", "stare")
            her "I can't have enough of that brilliant magazine!" ("grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give an assortment of rather girly magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("open", "squint", "base", "mid")
            call her_mood(-15)

    elif gift_item == adult_mag_ITEM:
        if states.her.level < 6:
            her "Are that...?" ("open", "base", "base", "mid")
            her "Adult magazines, [name_genie_hermione]?" ("open", "base", "base", "mid")
            her "Given to me by An esteemed wizard of your status?" ("annoyed", "narrow", "angry", "R")
            her "[name_genie_hermione], surely you could find a more productive way to spend your spare time." ("disgust", "narrow", "base", "mid_soft")
            her "And I most definitely would not have use for those..." ("angry", "base", "angry", "mid")
            call her_mood(7)
        elif states.her.level < 12:
            her "Adult magazines?" ("angry", "base", "angry", "mid")
            her "[name_genie_hermione], I have no interest in things like that." ("annoyed", "narrow", "angry", "R")
            her "And how is this an appropriate present for one of your students, [name_genie_hermione]?" ("angry", "base", "angry", "mid")
            call her_mood(3)
        elif states.her.level < 18:
            her "Adult magazines?" ("open", "base", "base", "mid")
            her "[name_genie_hermione], this is such an inappropriate present for a girl like me..." ("angry", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give an assortment of adult magazines to Hermione...",gift_item)
            her "I shall throw these away myself..." ("annoyed", "narrow", "annoyed", "mid")
            call her_mood(-8)
        else:
            her "The New edition of \"L.o.v.e.\"!!!" ("smile", "happyCl", "base", "mid")
            her "*Err*... I mean, adult magazines?" ("angry", "wink", "base", "mid")
            her "This is a little inappropriate..."
            her "But I will take them..." ("base", "happyCl", "base", "mid")
            call give_gift("You give an assortment of adult magazines to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "happyCl", "base", "mid")
            call her_mood(-15)

    elif gift_item == porn_mag_ITEM:
        if states.her.level < 6:
            her "*Hmm*... What is this?" ("base", "base", "base", "mid")
            her "[name_genie_hermione], those are porn magazines!" ("scream", "wide", "base", "stare")
            her @ cheeks blush "Shame on you, [name_genie_hermione]!" ("angry", "base", "angry", "mid")
            call her_mood(15)
        elif states.her.level < 12:
            her "Porn magazines?" ("shock", "wide", "base", "stare")
            her "[name_genie_hermione], what do you expect me to do with those?" ("open", "narrow", "worried", "down")
            her "Research them?" ("annoyed", "narrow", "annoyed", "mid")
            her "Despicable!" ("scream", "base", "angry", "mid",emote="angry")
            call her_mood(8)
        elif states.her.level < 18:
            her "That's hardcore porn, [name_genie_hermione]." ("open", "base", "base", "mid")
            her "Which is a completely inappropriate gift for a girl like me!" ("angry", "happyCl", "worried", "mid",emote="sweat")
            her ".............." ("angry", "narrow", "base", "down")
            her "But I will take them..." ("angry", "base", "base", "mid")
            call give_gift("You give an assortment of porn magazines to Hermione...",gift_item)
            her "And I shall throw them in the rubbish, where they, and girls who like these things belong..." ("annoyed", "narrow", "annoyed", "mid")
            call her_mood(0)
        else:
            her "Pornography?" ("shock", "wide", "base", "stare")
            her "................" ("angry", "narrow", "base", "down")
            her "How can women even agree to do things like that, [name_genie_hermione]?" ("angry", "base", "base", "mid")
            her "................." ("angry", "narrow", "base", "down")
            her "Alright, I shall accept them..." ("upset", "closed", "base", "mid")
            her @ cheeks blush "Solely for research purposes of course..." ("open", "base", "base", "R")
            call give_gift("You give an assortment of porn magazines to Hermione...",gift_item)
            call her_mood(-15)

    elif gift_item == krum_poster_ITEM:
        if states.her.level < 6:
            her "A Quidditch poster?" ("annoyed", "narrow", "worried", "down")
            her "What am I supposed to do with it, [name_genie_hermione]?" ("annoyed", "narrow", "annoyed", "mid")
            her "No, thank you." ("annoyed", "closed", "base", "mid")
            call her_mood(0)
        elif states.her.level < 12:
            her "A Quidditch poster?" ("annoyed", "narrow", "worried", "down")
            her "*Hmm*..." ("annoyed", "narrow", "annoyed", "mid")
            her "I think I saw this player once or twice..." ("annoyed", "narrow", "worried", "down")
            her "He is that Durmstrang student, right?" ("base", "base", "base", "mid")
            call give_gift("You give the poster to Hermione...",gift_item)
            call her_mood(-5)
        elif states.her.level < 18:
            her "A Viktor Krum poster, [name_genie_hermione]?" ("annoyed", "narrow", "worried", "down")
            her "Can't say that I care much for Quidditch, but..." ("open", "squint", "base", "mid")
            her "I can see why the girls find the brutish physique of some players appealing..." ("open", "narrow", "worried", "down")
            call give_gift("You give the poster to Hermione...",gift_item)
            call her_mood(-15)
        else:
            her "A Viktor Krum poster?!" ("scream", "wide", "base", "mid")
            her "Thank you, [name_genie_hermione]!" ("grin", "happyCl", "worried", "mid",emote="sweat")
            call give_gift("You give the poster to Hermione...",gift_item)
            her "Can't wait to hang it over my bed!" ("smile", "base", "base", "R")
            her "The girls will go green with envy..." ("smile", "narrow", "base", "mid_soft")
            call her_mood(-25)

    elif gift_item == sexy_lingerie_ITEM:
        if states.her.level < 6:
            her "Lingerie?" ("angry", "narrow", "base", "down")
            her "[name_genie_hermione], I cannot accept a gift like this from you..." ("upset", "closed", "base", "mid")
            call her_mood(10)
        elif states.her.level < 12:
            her "Sexy lingerie?" ("angry", "narrow", "base", "down")
            her "You know I cannot possibly accept a gift like this from you, [name_genie_hermione]." ("angry", "base", "base", "mid")
            her "(It's pretty though)........." ("angry", "narrow", "base", "down")
            call her_mood(0)
        elif states.her.level < 18:
            her "Sexy lingerie?" ("base", "narrow", "worried", "down")
            her "[name_genie_hermione] that is so inappropriate..." ("angry", "wink", "base", "mid")
            call give_gift("You give the lingerie to Hermione...",gift_item)
            her @ cheeks blush "Thank you, [name_genie_hermione]." ("base", "base", "base", "R")
            call her_mood(-7)
        else:
            her "Sexy lingerie?" ("base", "narrow", "worried", "down")
            her "Do you think wearing these will make me look like one of the witches in those adult magazines, [name_genie_hermione]?" ("grin", "narrow", "base", "dead")
            her "Oh... I mean, thank you, [name_genie_hermione]." ("angry", "wink", "base", "mid")
            call give_gift("You give the lingerie to Hermione...",gift_item)
            call her_mood(-15)

    elif gift_item == sexy_stockings_ITEM :
        if states.her.level < 6:
            her "Stockings?" ("base", "narrow", "worried", "down")
            her "[name_genie_hermione], are you insinuating that I wear these?" ("angry", "closed", "base", "mid")
            call her_mood(8)
        elif states.her.level < 12:
            her "Sexy stockings?" ("angry", "narrow", "base", "down")
            her "Isn't this a bit inappropriate, [name_genie_hermione]?" ("annoyed", "base", "base", "mid")
            call her_mood(0)
        elif states.her.level < 18:
            her "Sexy stockings?" ("base", "narrow", "worried", "down")
            her @ cheeks blush "Thank you I guess..." ("base", "wink", "base", "mid")
            call give_gift("You give the stockings to Hermione...",gift_item)
            her @ cheeks blush "Thank you, [name_genie_hermione]." ("base", "base", "base", "R")
            call her_mood(-8)
        else:
            her "Sexy stockings?" ("base", "narrow", "worried", "down")
            her "These are almost completely transparent, [name_genie_hermione]!" ("grin", "wide", "base", "mid")
            call give_gift("You give the stockings to Hermione...",gift_item)
            call her_mood(-10)

    elif gift_item == pink_condoms_ITEM:
        if states.her.level < 6:
            her "Condoms?!" ("angry", "wide", "base", "stare")
            her "[name_genie_hermione], I wouldn't even know what to do with them..." ("scream", "closed", "angry", "mid")
            call her_mood(6)
        elif states.her.level < 12:
            her "... Condoms?" ("normal", "squint", "angry", "mid")
            her "*Ehm*... Is this a part of some new Hogwarts sex ed program or something?" ("open", "closed", "angry", "mid")
            her @ cheeks blush "No, [name_genie_hermione]... It feels wrong to accept something like this from you..." ("open", "base", "base", "R")
            call her_mood(0)
        elif states.her.level < 18:
            her "A pack of condoms?" ("normal", "base", "base", "mid")
            her "[name_genie_hermione], what possible use could I have for those?" ("normal", "base", "base", "mid")
            her "Well, I shall accept them simply because it is rude to refuse a gift..." ("open", "closed", "angry", "mid")
            call give_gift("You give a pack of condoms to Hermione...", gift_item)
            call her_mood(-3)
        else:
            her "A pack of condoms?" ("open", "squint", "base", "mid")
            her "I appreciate your concern, [name_genie_hermione]. Thank you." ("base", "narrow", "base", "mid_soft")
            call give_gift("You give a pack of condoms to Hermione...", gift_item)
            call her_mood(-4)

    elif gift_item == vibrator_ITEM:
        if states.her.level < 6:
            her "A magic wand?" ("base", "base", "base", "mid")
            her "No, it doesn't look like--" ("soft", "base", "base", "mid")
            her ".........?" ("soft", "base", "base", "mid")
            her "!!!" ("angry", "wide", "base", "stare")
            her @ cheeks blush "[name_genie_hermione]!" ("angry", "base", "angry", "mid")
            her "This is just beyond inappropriate!" ("scream", "closed", "angry", "mid")
            call her_mood(10)
        elif states.her.level < 12:
            her "Is this what I think it is?" ("angry", "narrow", "base", "down")
            her @ cheeks blush "[name_genie_hermione], let me remind you that I belong to the noble house of Gryffindor." ("open", "narrow", "annoyed", "mid")
            her "A present like that would be appropriate for a girl from Slytherin, [name_genie_hermione]." ("upset", "closed", "base", "mid")
            call her_mood(10)
        elif states.her.level < 18:
            her "Is that a... vibrator?" ("angry", "narrow", "base", "down")
            her "The design..." ("angry", "narrow", "base", "down")
            her "It reminds me of my wand..." ("angry", "narrow", "base", "down")
            her "Did you have this custom-made for me [name_genie_hermione]?" ("angry", "narrow", "base", "down")
            her "This is inappropriate..." ("scream", "closed", "angry", "mid")
            her "But I shall take it nonetheless..." ("annoyed", "base", "worried", "R")
            call give_gift("You give the vibrator to Hermione...",gift_item)
            call her_mood(0)
        else:
            her "This vibrator..." ("open", "base", "worried", "mid")
            her "It's... calling out for me..." ("open", "base", "worried", "R")
            her "But not in a dirty way, [name_genie_hermione]." ("disgust", "narrow", "base", "mid_soft")
            call give_gift("You give the vibrator to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "narrow", "worried", "down")
            call her_mood(-10)

    elif gift_item == anal_lube_ITEM:
        if states.her.level < 6:
            her "I don't know what this is..." ("open", "base", "base", "mid")
            her "But I have the feeling that the jar is full of something vile and inappropriate..." ("angry", "base", "angry", "mid")
            her "No, thank you, [name_genie_hermione]." ("angry", "base", "angry", "mid")
            call her_mood(6)
        elif states.her.level < 12:
            her "*Hmm*..." ("annoyed", "narrow", "worried", "down")
            her "I think I know what this is..." ("disgust", "narrow", "base", "mid_soft")
            her "But why would you give something like this to one of your pupils, [name_genie_hermione]?"
            her "No, thank you." ("annoyed", "narrow", "angry", "R")
            call her_mood(2)
        elif states.her.level < 18:
            her "Anal lubricant?" ("angry", "narrow", "base", "down")
            her @ cheeks blush "*Ehm*... Well... I know this girl..." ("open", "base", "base", "R")
            her "I mean, I don't know her, she is a friend of a friend..." ("open", "base", "base", "R")
            her "Yes, I will take this for her..." ("open", "base", "base", "R")
            call give_gift("You give the jar to Hermione...",gift_item)
            her @ cheeks blush "Still, I think you should not give presents like this to one of your pupils, [name_genie_hermione]." ("open", "narrow", "annoyed", "mid")
            call her_mood(0)
        else:
            her "Anal lubricant, [name_genie_hermione]?" ("base", "narrow", "worried", "down")
            her @ cheeks blush "I know a couple of girls who would do anything for a commodity like that." ("open", "narrow", "annoyed", "mid")
            her "Thank for looking out for us, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
            call give_gift("You give the jar to Hermione...",gift_item)
            call her_mood(-5)

    elif gift_item == ballgag_and_cuffs_ITEM:
        if states.her.level < 6:
            her "What is this?" ("angry", "narrow", "base", "down")
            her @ cheeks blush "Is this like one of those adult toys?" ("angry", "squint", "base", "mid")
            her "What woman in her right mind would subject herself to a humiliation like that?" ("scream", "closed", "angry", "mid")
            her @ cheeks blush "And what possible use could I have for such objects?" ("open", "narrow", "annoyed", "mid")
            her @ cheeks blush "This is just insulting, [name_genie_hermione]..." ("angry", "base", "angry", "mid")
            call her_mood(10)
        elif states.her.level < 12:
            her @ cheeks blush "[name_genie_hermione], do you not realise how inappropriate it would be for me to accept a present like that?" ("open", "narrow", "annoyed", "mid")
            her @ cheeks blush "And I would not even know what to do with them anyway..." ("open", "base", "base", "R")
            her "I mean these fluffy things are obviously handcuffs..." ("angry", "narrow", "base", "down")
            her "But this ball... *Ehm*..." ("angry", "narrow", "base", "down")
            her "[name_genie_hermione], please..." ("upset", "closed", "base", "mid")
            her "Just put them away." ("upset", "closed", "base", "mid")
            call her_mood(5)
        elif states.her.level < 18:
            her "A month ago I would've felt insulted to receive a gift like this..." ("upset", "closed", "base", "mid")
            her "But by now I know that some girls really do find pleasure in toys like..." ("angry", "narrow", "base", "down")
            her "But I assure you that I am not one of them, [name_genie_hermione]." ("upset", "closed", "base", "mid")
            her @ cheeks blush "But I know a girl who knows a girl who is into things like..." ("open", "base", "base", "R")
            her @ cheeks blush "Yes, I shall take these to her..." ("base", "base", "base", "R")
            call give_gift("You give the ball gag and cuffs to Hermione...",gift_item)
            call her_mood(-9)
        else:
            her @ cheeks blush "A ball gag and handcuffs?" ("open", "happy", "base", "mid")
            her "This is completely inappropriate, [name_genie_hermione]." ("angry", "wink", "base", "mid")
            her "But a gift is a gift, right?" ("base", "squint", "base", "mid")
            call give_gift("You give the ball gag and cuffs to Hermione...",gift_item)
            call her_mood(-15)

    elif gift_item == anal_plugs_ITEM:
        if states.her.level < 6:
            her "*Hmm*...?" ("base", "base", "base", "mid")
            her "Is this some kind of keychain toy?" ("soft", "base", "base", "mid")
            call give_gift("You give the anal plugs to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("annoyed", "narrow", "annoyed", "mid")
            call her_mood(-8)
        elif states.her.level < 12:
            her @ cheeks blush "[name_genie_hermione], are those adult toys of some sort?" ("open", "narrow", "annoyed", "mid")
            her @ cheeks blush "Those are some of those anal things, aren't they?" ("angry", "base", "angry", "mid")
            her "[name_genie_hermione] this is nothing but a weapon meant to oppress women!" ("angry", "base", "angry", "mid")
            her "Despicable!" ("upset", "closed", "base", "mid")
            call her_mood(15)
        elif states.her.level < 18:
            her "Yes, I know that some girls have, *uhm*..." ("upset", "closed", "base", "mid")
            her @ cheeks blush "A use for things such as these..." ("open", "narrow", "annoyed", "mid")
            her "But not me, [name_genie_hermione]." ("open", "narrow", "annoyed", "mid")
            her "No, thank you." ("upset", "closed", "base", "mid")
            call her_mood(0)
        else:
            her "Anal plugs?" ("angry", "narrow", "base", "down")
            her "I have no use for things like that, [name_genie_hermione]..." ("angry", "base", "base", "mid")
            her "They are so pretty though..." ("angry", "wink", "base", "mid")
            her "....................." ("angry", "narrow", "base", "down")
            her "Well, alright. I shall take them off your hands if I must, [name_genie_hermione]." ("soft", "narrow", "annoyed", "up")
            call give_gift("You give the anal plugs to Hermione...",gift_item)
            her "But I shall never use them of course..." ("open", "closed", "base", "mid")
            her "................" ("base", "narrow", "worried", "down")
            call her_mood(-10)

    elif gift_item == testral_strapon_ITEM:
        if states.her.level < 6:
            her "What is that?" ("angry", "wide", "base", "stare")
            her "An artefact of some sort or a trophy?" ("open", "base", "base", "mid")
            her "So well-crafted..." ("base", "base", "base", "mid")
            her "Are you sure that it's alright for me to have it, [name_genie_hermione]?" ("base", "base", "base", "mid")
            call give_gift("You give the strap-on to Hermione...",gift_item)
            her "Thank you very much, [name_genie_hermione]. I promise to take good care of it." ("open", "closed", "base", "mid")
            call her_mood(-20)
        elif states.her.level < 12:
            her "!!!" ("angry", "wide", "base", "stare")
            her "That is..." ("angry", "narrow", "base", "down")
            her "But it doesn't even look... human..." ("angry", "narrow", "base", "down")
            her "I mean..." ("annoyed", "narrow", "angry", "R")
            her "[name_genie_hermione], do you have no shame?!" ("scream", "base", "angry", "mid",emote="angry")
            her "Presenting a thing like that to a pupil?!" ("scream", "base", "angry", "mid",emote="angry")
            her ".................." ("open", "narrow", "worried", "down")
            her "Please put it away, [name_genie_hermione]." ("angry", "base", "angry", "mid")
            call her_mood(15)
        elif states.her.level < 18:
            her "That thing..." ("angry", "narrow", "base", "down")
            her "Is that the actual size of the... of the real \"thing\"?" ("angry", "base", "base", "mid")
            her @ cheeks blush "I mean..." ("open", "base", "base", "R")
            her "......................." ("angry", "narrow", "base", "down")
            her "Is this like a party prank prop?" ("angry", "base", "base", "mid")
            her "It's so well-crafted though..." ("angry", "narrow", "base", "down")
            her "I will take it..." ("normal", "happyCl", "worried", "mid")
            call give_gift("You give the strap-on to Hermione...",gift_item)
            call her_mood(-10)
        else:
            her "It's... It's magnificent, [name_genie_hermione]..." ("shock", "wide", "base", "stare")
            her @ cheeks blush "Is it really modelled after a thestral?" ("open", "base", "base", "R")
            her @ cheeks blush "But the creatures are invisible..." ("open", "happy", "base", "mid")
            her ".................." ("angry", "narrow", "base", "down")
            her "Breathtaking..." ("grin", "narrow", "base", "dead")
            her "Not in the way you think, [name_genie_hermione]..." ("upset", "closed", "base", "mid")
            her "I am merely admiring the craftsmanship..." ("open", "closed", "base", "mid")
            call give_gift("You give the strap-on to Hermione...",gift_item)
            her "Thank you for the gift, [name_genie_hermione]." ("base", "squint", "base", "mid")
            call her_mood(-30)

    elif gift_item == broom_2000_ITEM:
        if states.her.level < 6:
            her "A broom...?" ("base", "base", "base", "mid")
            her "*Hmm*..." ("normal", "base", "base", "mid")
            her "What is that silly-looking thing attached to it?" ("normal", "squint", "angry", "mid")
            her "Is it some kind of saddle...?" ("open", "squint", "base", "mid")
            call give_gift("You give the broom to Hermione...",gift_item)
            her "Thank you for the gift, [name_genie_hermione]." ("open", "base", "worried", "mid")
            call her_mood(-20)
        elif states.her.level < 12:
            her "A broom...?" ("base", "base", "base", "mid")
            her "*Hmm*..." ("normal", "squint", "angry", "mid")
            her "It's a sex-toy of some sort, isn't it?" ("angry", "base", "angry", "mid")
            her "But it is so well crafted..." ("open", "narrow", "worried", "down")
            call give_gift("You give the broom to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("upset", "closed", "base", "mid")
            call her_mood(-20)
        elif states.her.level < 18:
            her "A broom...?" ("angry", "narrow", "base", "down")
            her "*Hmm*..." ("angry", "narrow", "base", "down")
            her "What kind of saddle is that...?" ("disgust", "narrow", "base", "mid_soft")
            her "Well, doesn't matter." ("open", "closed", "base", "mid")
            her "Refusing an expensive gift like that would be rude..." ("open", "closed", "base", "mid")
            call give_gift("You give the broom to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("upset", "closed", "base", "mid")
            call her_mood(-30)
        else:
            her "A broom..." ("base", "narrow", "worried", "down")
            her "*Hmm*..." ("base", "narrow", "worried", "down")
            her @ cheeks blush "That saddle, [name_genie_hermione]..." ("open", "base", "base", "R")
            her @ cheeks blush "It was designed specifically for witches, wasn't it?" ("open", "happy", "base", "mid")
            her "I am not sure whether this is inappropriate or clever..." ("annoyed", "narrow", "annoyed", "mid")
            her "But this is a brilliant piece of engineering either way..." ("base", "squint", "base", "mid")
            call give_gift("You give the broom to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")
            call her_mood(-30)

    elif gift_item == sexdoll_ITEM:
        if states.her.level < 6:
            her "Is this..." ("shock", "wide", "base", "stare")
            her "A sex doll?!" ("angry", "happyCl", "worried", "mid",emote="sweat")
            her "[name_genie_hermione]!!!" ("scream", "happyCl", "worried", "mid")
            call her_mood(20)
        elif states.her.level < 12:
            her "A sex doll?" ("shock", "wide", "base", "stare")
            her "This is just so unbecoming for an esteemed wizard such as yourself, [name_genie_hermione]..." ("upset", "closed", "base", "mid")
            call her_mood(20)
        elif states.her.level < 18:
            her "A sex doll..." ("angry", "narrow", "base", "down")
            her "This is a little inappropriate..." ("upset", "closed", "base", "mid")
            her "But maybe we could use it for a prank or something..." ("base", "narrow", "worried", "down")
            call give_gift("You give the blow-up doll to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "narrow", "worried", "down")
            call her_mood(-10)
        else:
            her "The Joanne sex doll?" ("annoyed", "narrow", "worried", "down")
            her @ cheeks blush "I Can't say that I approve of this..." ("open", "base", "base", "R")
            her "But I know Harry would love to have a go at it..." ("base", "narrow", "worried", "down")
            call give_gift("You give the blow-up doll to Hermione...",gift_item)
            her @ cheeks blush "Thank you, [name_genie_hermione]." ("base", "base", "base", "R")
            call her_mood(-30)

    elif gift_item == anal_beads_ITEM:
        if states.her.level < 6:
            her "*Hmm*...?" ("base", "base", "base", "mid")
            her "Is this a necklace?" ("soft", "base", "base", "mid")
            call give_gift("You give the anal beads to Hermione...",gift_item)
            her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")
            call her_mood(-8)
        elif states.her.level < 12:
            her @ cheeks blush "[name_genie_hermione], are those adult toys of some sort?" ("open", "narrow", "annoyed", "mid")
            her @ cheeks blush "This is one of those butt... bead things, aren't they?" ("angry", "base", "angry", "mid")
            her "[name_genie_hermione] get them away from me!" ("angry", "base", "angry", "mid")
            her "Gross!" ("upset", "closed", "base", "mid")
            call her_mood(15)
        elif states.her.level < 17:
            her "That's not a necklace..." ("upset", "closed", "base", "mid")
            her @ cheeks blush "I wouldn't have any use for this..." ("open", "narrow", "annoyed", "mid")
            her "Thanks but no, thanks [name_genie_hermione]." ("upset", "closed", "base", "mid")
            call her_mood(0)
        else:
            her "Anal beads?" ("angry", "narrow", "base", "down")
            her "Obviously I don't need this sort of thing, [name_genie_hermione]..." ("angry", "base", "base", "mid")
            her "Although it's got a nice colour..." ("angry", "wink", "base", "mid")
            her "....................." ("angry", "narrow", "base", "down")
            her "Fine, I'll use them as an armband, [name_genie_hermione]." ("soft", "narrow", "annoyed", "up")
            call give_gift("You give the anal beads to Hermione...",gift_item)
            her "But I won't use them for their intended purpose..." ("open", "closed", "base", "mid")
            her "................" ("base", "narrow", "worried", "down")
            call her_mood(-10)

    elif gift_item == wine_ITEM or gift_item == firewhisky_ITEM:
        if states.her.level < 7:
            call give_gift("You give the "+str(gift_item.name)+" bottle to Hermione...", gift_item)
            her @ cheeks blush "Thank you, [name_genie_hermione], I'll ask Ginny to drink some with me later." ("soft", "base", "base", "mid")
            call her_mood(-20)
        elif states.her.level < 12:
            her "[name_genie_hermione]?! Drinking alcohol on school grounds is forbidden..." ("open", "base", "angry", "mid")
            her "And you as a headmaster should know it!" ("upset", "base", "angry", "mid")
            call her_mood(10)
        elif states.her.level < 18:
            her "But, [name_genie_hermione]... I can't drink alcohol." ("base", "narrow", "worried", "down")
            her "I guess I could use it for some potion mixing though..." ("open", "base", "base", "R")
            call give_gift("You give the "+str(gift_item.name)+" bottle to Hermione...", gift_item)
            her "" ("base", "base", "base", "R")
            call her_mood(-5)
        else:
            her @ cheeks blush "But, [name_genie_hermione]... You know I can't drink..." ("soft","base", "base", "mid")
            her @ cheeks blush "I usually get drunk way too fast, and I'd rather not do something I'll regret later." ("open", "base", "base", "R")
            her @ cheeks blush "" ("base", "base", "base", "R")
            call her_mood(0)

    her "" (xpos="base",ypos="base")
    hide hermione_main
    with d5

    return

label her_mood(value=0):

    if value > 0:
        if value == 1:
            "Hermione's mood worsened slightly."
        else:
            "Hermione's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Hermione's mood has improved slightly."
        else:
            "Hermione's mood has improved significantly."
    else:
        "Hermione's mood hasn't changed."

    $ was_negative = states.her.mood > 0
    $ states.her.mood = max(min(states.her.mood+value, 100), 0)

    call describe_mood_after_gift(was_negative, states.her.mood, value)

    return
