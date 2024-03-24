
label susan_chitchat:

    if states.sus.chatted:
        return

    $ states.sus.chatted = True

    # Note: Susan does not have Tiers yet.

    # if states.ast.tier == 1:
    #     # $ random_number = renpy.random.randint(MIN, MAX)

    #     pass
    # elif states.ast.tier == 2:
    #     # $ random_number = renpy.random.randint(MIN, MAX)

    #     pass
    # elif states.ast.tier == 3:
    #     # $ random_number = renpy.random.randint(MIN, MAX)

    #     pass
    # elif states.ast.tier == 4:
    #     $ random_number = renpy.random.randint(1, 11)

    random:
        block:
            sus "My favourite subject is Herbology..." ("open", "closed", "base", "mid")
            sus "But when we're working in groups, the other students usually talk over me..." ("soft", "narrow", "base", "down")
            sus "" ("annoyed", "happy", "base", "mid")

        block:
            sus "The Hufflepuff house entrance is hidden in the kitchen corridor." ("open", "closed", "base", "mid")
            sus "Even though we're so close, I've only seen a house elf once." ("soft", "base", "raised", "mid")

        block:
            sus "Care for magical creatures is a bit scary sometimes..." ("soft", "happy", "base", "downR")
            sus "When we were taught how to properly approach Hippogriffs, I was shaking the entire time." ("open", "happy", "sad", "downR")
            sus "After bowing and letting it approach me, I only pet it a couple of times... I wouldn't dare to ride the thing." ("normal", "happy", "sad", "mid")

        block:
            sus "Sir, could you... Could you please tell professor Snape not to..." ("soft", "happy", "sad", "down")
            sus "Never mind..." ("soft", "closed", "sad", "mid")

        block:
            sus "Does flying have to be mandatory?" ("open", "closed", "sad", "mid")
            sus "Surely only a piece of wood between you, and falling from the sky can't be safe..." ("soft", "narrow", "worried", "mid")

        block:
            sus "Madam Hooch was keeping a close eye on me during the last flying lesson." ("open", "base", "base", "right")
            sus "I hope I'm not disappointing her too much..." ("open", "base", "sad", "downR")

        block:
            sus "Madam Pomfrey once prescribed me a \"Draught of peace\" to drink the night before exams, so I could get some sleep." ("open", "base", "base", "right")
            sus "But even with her prescription, Snape wouldn't give one to me." ("open", "base", "sad", "downR")

        block:
            sus "Why does everyone assume I'm a Weasley, just because I've got red hair?" ("open", "base", "sad", "right")
            sus "The Slytherin boys keep mocking me... Even though I'm clearly wearing Hufflepuff robes." ("annoyed", "happy", "worried", "downR")

        block:
            sus "I used to be scared of ghosts before I got to Hogwarts, but the \"Fat Friar\" is so nice it's hard to stay scared of them." ("base", "base", "base", "mid")
            sus "Poltergeists on the other hand..." ("angry", "happy", "sad", "mid")

        block:
            sus "The \"Defence against the dark arts\" lesson when we had to confront a Boggart was one of my worst days here..." ("soft", "happy", "worried", "down")
            sus "Professor Tonks had me stay behind after class to make sure I was okay." ("soft", "happy", "sad", "down")
            sus "Once I got back to my dorm, some of the other students were whistling at me for some reason..." ("soft", "happy", "sad", "mid")

        block:
            sus "Whilst most students go home during winter break, I usually stay at Hogwarts." ("base", "base", "base", "mid")
            sus "The castle is a lot quieter than usual, but I don't really mind." ("base", "base", "shocked", "right")

        block:
            sus "How come Professor Snape is allowed to ask us to gather ingredients in the forbidden forest?" ("soft", "happy", "sad", "mid")
            sus "The students who didn't go received a bad grade, and the ones who did got detention..." ("angry", "closed", "sad", "mid")
            sus "How is that fair?" ("soft", "happy", "sad", "mid")

        block:
            sus "I think my school robes must've shrunk in the wash." ("open", "happy", "sad", "down")
            sus "They're a lot tighter than when I bought them..." ("soft", "base", "sad", "mid")

        block:
            sus "Just because the Hufflepuff house is next to the kitchen, doesn't mean we can get food whenever we like." ("annoyed", "base", "base", "mid")
            sus "So why do the Slytherin students keep asking me to show where I hide my melons?" ("annoyed", "happy", "sad", "down")

        block:
            sus "Why do people seem to find my surname so funny?" ("soft", "happy", "sad", "down")
            sus "I mean, I suppose it's a bit unusual..." ("annoyed", "happy", "sad", "right")

    return
