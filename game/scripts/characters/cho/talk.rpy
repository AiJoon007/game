# Cho Talk
label cho_talk:
    menu:
        #"-Working-":

        "-Discuss Quidditch Training-" (icon="interface/icons/small/quidditch.webp") if not states.cho.ev.quidditch.lock_training:
            if states.cho.tier == 1:
                jump cc_ht_talk
            elif states.cho.tier == 2:
                jump cc_st_talk
            elif states.cho.tier == 3:
                jump cc_gt_talk

            jump cho_talk

        # Naming
        "\"-Address me only as-\"" if states.cho.ev.quidditch.e1_complete:
            menu:
                "\"-Sir-\"":
                    $ name_genie_cho = "Sir"
                "\"-Dumbledore-\"":
                    $ name_genie_cho = "Dumbledore"
                "\"-Professor-\"":
                    $ name_genie_cho = "Professor"
                "\"-Coach-\"":
                    $ name_genie_cho = "Coach"
                "\"-Sergeant-\"":
                    $ name_genie_cho = "Sergeant"
                "\"-Captain-\"":
                    $ name_genie_cho = "Captain"
                "\"-Old Man-\"":
                    $ name_genie_cho = "Old Man"
                "\"-Daddy-\"" if states.cho.tier >= 4:
                    $ name_genie_cho = "Daddy"
                "-Custom Input-":
                    $ name_genie_cho = renpy.input("(Please enter the name.)", name_genie_cho, ALLOWED_CHARACTERS, length=14).strip() or "Professor"
                "\"-Never mind-\"":
                    jump cho_talk

            jump genie_cho_change

        "\"-From now on, I will refer to you as-\"" if states.cho.ev.quidditch.e1_complete:
            menu:
                "\"-Miss Chang-\"":
                    $ name_cho_genie = "Miss Chang"
                "\"-Cho-\"":
                    $ name_cho_genie = "Cho"
                "\"-Cadet-\"":
                    $ name_cho_genie = "Cadet"
                "\"-Pilot-\"":
                    $ name_cho_genie = "Pilot"
                "\"-Maggot-\"":
                    $ name_cho_genie = "Maggot"
                "\"-Tomboy-\"":
                    $ name_cho_genie = "Tomboy"
                "\"-Boy-\"":
                    $ name_cho_genie = "Boy"
                "\"-Champ-\"" if states.cho.tier >= 4:
                    $ name_cho_genie = "Champ"
                "\"-Slut-\"" if states.cho.tier >= 4:
                    $ name_cho_genie = "Slut"
                "-Custom Input-":
                    $ name_cho_genie = renpy.input("(Please enter the name.)", name_cho_genie, ALLOWED_CHARACTERS, length=14).strip() or "Miss Chang"
                "\"-Never mind-\"":
                    jump cho_talk

            jump name_cho_genie

        "\"-Never mind-\"":
            jump cho_requests

label genie_cho_change:
    if name_genie_cho == "Sir":
        cho "Certainly, sir." ("base", "base", "base", "mid")
    elif name_genie_cho == "Dumbledore":
        cho "Of course Dumbledore..." ("open", "base", "base", "mid")
    elif name_genie_cho == "Professor":
        cho "Yes Professor..." ("open", "base", "base", "mid")
    elif name_genie_cho == "Coach":
        cho "Yes Coach!" ("smile", "base", "base", "mid")
    elif name_genie_cho == "Sergeant":
        gen "Is that clear?" ("base", xpos="far_left", ypos="head")
        cho "Yes Sergeant!" ("smile", "base", "base", "mid")
    elif name_genie_cho == "Captain":
        cho "Yes Captain!" ("smile", "base", "base", "mid")
    elif name_genie_cho == "Old Man":
        cho "You want me to call you an old man?" ("soft", "base", "base", "mid")
        gen "Just \"Old man\" is good for now." ("base", xpos="far_left", ypos="head")
        cho "Okay then..." ("open", "base", "base", "R")
    elif name_genie_cho == "Daddy":
        cho @ cheeks blush "You want me to--" ("soft", "narrow", "base", "mid")
        gen "Call me daddy..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("base", "narrow", "base", "downR")
        cho @ cheeks heavy_blush "Yes daddy..." ("base", "narrow", "base", "down")
    else: #custom/fallback
        cho "Very well..." ("open", "narrow", "base", "mid")
    jump cho_talk

label name_cho_genie:
    if name_cho_genie == "Miss Chang":
        cho "Of course [name_genie_cho]." ("base", "base", "base", "mid")
    elif name_cho_genie == "Cho":
        cho "Of course [name_genie_cho]." ("base", "base", "base", "mid")
    elif name_cho_genie == "Cadet":
        cho "Yes [name_genie_cho]!" ("smile", "base", "base", "mid")
    elif name_cho_genie == "Pilot":
        cho "Yes [name_genie_cho]!" ("base", "base", "base", "mid")
    elif name_cho_genie == "Maggot":
        cho "I--" ("angry", "narrow", "base", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        cho "Yes [name_genie_cho]!" ("angry", "happyCl", "base", "mid")
    elif name_cho_genie == "Tomboy":
        if states.cho.tier <= 3:
            cho "Tomboy?" ("soft", "base", "base", "mid")
            gen "Is that not accurate?" ("base", xpos="far_left", ypos="head")
            cho "I--{w=0.4} I suppose..." ("angry", "narrow", "base", "down")
            gen "Great! Tomboy it is!" ("base", xpos="far_left", ypos="head")
        else:
            cho @ cheeks blush "Am I not feminine enough for you?" ("annoyed", "narrow", "base", "mid")
            gen "Nonsense! You are feminine in all the right places." ("grin", xpos="far_left", ypos="head")
            gen "Except your personality..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "*Hmph*..." ("annoyed", "narrow", "base", "R")
            cho @ cheeks blush "Fine... I guess that's fair..." ("open", "narrow", "base", "R")
    elif name_cho_genie == "Boy":
        if states.cho.tier <= 3:
            cho "You want to call me what?!" ("angry", "base", "base", "mid")
            gen "Boy!" ("base", xpos="far_left", ypos="head")
            cho "But [name_genie_cho]!" ("disgust", "narrow", "base", "mid")
            cho "I'm not a boy!" ("clench", "narrow", "base", "mid")
            gen "I know that..." ("base", xpos="far_left", ypos="head")
            cho "Then why--" ("angry", "base", "base", "mid")
            gen "Don't you wanna be one of the boys?" ("base", xpos="far_left", ypos="head")
            cho "...{w=0.4} What's that's supposed to mean?" ("disgust", "narrow", "base", "mid")
            gen "Well, I suppose maybe you're not fit to be one of the boys..." ("base", xpos="far_left", ypos="head")
            cho "No! I am! I can be one of the boys!" ("clench", "base", "base", "mid")
            gen "Great, then boy it is!" ("base", xpos="far_left", ypos="head")
            cho "..." ("smile", "base", "base", "mid") #smiles
            cho "..." ("disgust", "base", "base", "stare") #Hold on a minute...
        else:
            cho @ cheeks blush "Boy?" ("soft", "narrow", "base", "mid")
            cho @ cheeks blush "But [name_genie_cho]... Won't that be weird?" ("soft", "base", "base", "mid")
            gen "..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Alright then... If that's what you're into..." ("base", "base", "base", "R")
    elif name_cho_genie == "Champ":
        cho "Champ?" ("open", "base", "raised", "mid")
        gen "Yep... Gotta give some credit where it's due." ("base", xpos="far_left", ypos="head")
        cho "Oh... Thank you [name_genie_cho]..." ("smile", "base", "base", "mid")
    elif name_cho_genie == "Slut":
        cho @ cheeks heavy_blush "You want to call me..." ("soft", "narrow", "base", "down")
        gen "A slut!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "stare") #horny
        cho @ cheeks heavy_blush "*Ah*...{w=0.4} Yes, I suppose that's fine..." ("soft", "narrow", "base", "mid")
    elif name_cho_genie == "Princess": #Custom choice
        if states.cho.tier <= 3:
            cho "Princess?!" ("angry", "base", "base", "mid")
            gen "Yes, is that a problem?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "It's... It's a bit girly, don't you think?" ("clench", "narrow", "base", "mid")
            gen "You're a girl, I see nothing wrong with it." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("disgust", "narrow", "base", "mid")
            cho @ cheeks blush "Yes, I suppose I am." ("disgust", "narrow", "base", "mid")
            cho @ cheeks blush "Fine..." ("annoyed", "base", "base", "mid")
        else:
            cho @ cheeks blush "You want to call me..." ("angry", "narrow", "base", "mid")
            gen "Princess." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "..." ("angry", "narrow", "base", "downR")
            cho @ cheeks blush "Okay... I suppose you could call me that..." ("angry", "narrow", "base", "down")
    else: #custom/fallback
        cho "Very well..." ("open", "narrow", "base", "mid")

    jump cho_talk
