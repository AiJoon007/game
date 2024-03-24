

### Snape Hangout Event ###

label snape_hangout:

    call setup_fireplace_hangout(char="snape")

    $ states.gen.stats.hangouts_with_snape += 1

    $ sna_eventqueue_hangouts_drinking.start()

    label snape_hangout_continue:
        hide screen bld1
        hide snape_main
        show screen with_snape(ani=False)
        with fade
        call bld

    ### Intro Events ###
    # Events are located in the character's intro file.

    # Hermione
    if states.her.ev.intro.e1_complete and not states.sna.ev.hangouts.hermione_e1:
        jump ss_he_hermione_E1 # Fist discussion about Hermione with Snape.
    if states.her.ev.intro.e2_complete and not states.sna.ev.hangouts.hermione_e2:
        jump ss_he_hermione_E2 # Second discussion about Hermione with Snape.

    # Tonks
    if states.ton.ev.intro.e1_complete and not states.sna.ev.hangouts.tonks_e1:
        jump ss_he_tonks_E1
    if states.ton.ev.intro.e3_complete and not states.sna.ev.hangouts.tonks_e2:
        jump ss_he_tonks_E2
    if states.sna.ev.hangouts.tonks_e2 and not states.sna.ev.hangouts.tonks_e3:
        if states.her.tier < 2: # Event won't happen at this point in the game anymore.
            $ states.sna.ev.hangouts.tonks_e3 = True
        else:
            jump ss_he_tonks_E3

    # Cho
    if states.cho.ev.intro.e2_complete and not states.sna.ev.hangouts.cho_e1:
        jump ss_he_cho_E1
    if states.cho.ev.quiz.lost and not quidditchguide_ITEM.unlocked and not states.cho.ev.quiz.complete and not states.sna.ev.hangouts.cho_e2:
        # After failing the Quiz.
        jump ss_he_cho_E2


    ### General Events ###
    # Events are located here.

    # Hermione
    if states.her.status.stripping and not states.sna.ev.hangouts.hermione_strip_invite: #After second dance where Snape entered room.
        jump ss_he_hermione_strip # Get to invite Snape to watch.

    # (Quidditch) Ask Snape for help with Slytherins.
    if states.cho.ev.quidditch.e6_complete and not states.cho.ev.quidditch.e8_complete and not states.cho.ev.quidditch.e9_complete:
        jump cho_quid_E9

    ### Snape Stories ###
    # Events are located here.

    $ sna_eventqueue_hangouts_stories.start()

    label end_snape_hangout:
        show screen with_snape(ani=True)
        call bld
        call notes
        nar "You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."

    label end_snape_hangout_points:

    if states.sna.level < 100:
        if game.weather in {"rain", "storm"}:
            # Rain puts him in a good mood.
            $ states.sna.level += 1

        if game.difficulty == 1:
            $ states.sna.level += 5
        elif game.difficulty == 2:
            $ states.sna.level += 4
        else:
            $ states.sna.level += 3

    if states.sna.level > 100:
        $ states.sna.level = 100

    $ slytherin += renpy.random.randint(5, 15)

    label end_snape_hangout_no_points:

    $ chair_OBJ.hidden = False
    $ fireplace_OBJ.foreground = None

    hide screen with_snape

    if game.daytime:
        jump night_start
    else:
        jump day_start

label ss_he_wine_intro:
    call bld
    gen "Look what I've got!" ("base", xpos="far_left", ypos="head")
    sna "*Hmm*...?" ("snape_05", ypos="head")
    sna "Let me see..."
    pause.1

    # Show wine
    call give_gift("You hand over the bottle you found in the cupboard to professor Snape...", wine_ITEM)

    sna "This one has got to be from Albus' personal stash!" ("snape_24")
    sna "Some pricey and incredibly rare stuff." ("snape_06")
    gen "Shall we then?" ("base", xpos="far_left", ypos="head")
    sna "We most certainly shall!" ("snape_02")

    jump snape_hangout_continue


label ss_he_wine_intro_E2:
    call bld
    gen "Care for another bottle?" ("base", xpos="far_left", ypos="head")
    pause.1

    call give_gift("You hand over the bottle you found in the cupboard to professor Snape...", wine_ITEM)

    sna "Another bottle of Dumbledore's wine?" ("snape_05", ypos="head")
    sna "Did you find Albus' secret stash or was it his personal wine cellar?" ("snape_05")
    gen "It's more of a \"wine cabinet\", I'd say." ("base", xpos="far_left", ypos="head")
    gen "And I believe there is more where this came from..." ("base", xpos="far_left", ypos="head")
    sna "Seriously, how big is that stash?" ("snape_05")
    gen "Why don't we find out?" ("grin", xpos="far_left", ypos="head")
    sna "It's sure good to be us! let's uncork that bastard!" ("snape_02")

    jump snape_hangout_continue


label ss_he_wine_repeat:
    call bld
    gen "Look what I've got!" ("base", xpos="far_left", ypos="head")
    pause.1

    call give_gift("You hand over the bottle you found in the cupboard to professor Snape...", wine_ITEM)

    sna "Another one?" ("snape_05", ypos="head")

    random:
        sna "Splendid!" ("snape_02")
        sna "Well done, my friend!" ("snape_02")
        sna "Lately I am having a hard time drinking anything but this!" ("snape_02")
        sna "Great! I feel less stressed out already!" ("snape_02")
        sna "This just keeps getting better and better!" ("snape_02")
        sna "Let's uncork that bastard!" ("snape_02")

    jump snape_hangout_continue



### Events ###

label ss_he_hermione_strip:
    # TAKES PLACE AFTER Hermione has danced for you and Snape.
    sna "So..." ("snape_31", ypos="head")
    sna "You got the girl to strip for you..." ("snape_35")
    sna "And you didn't even invite me?!" ("snape_08")
    gen "Well..." ("base", xpos="far_left", ypos="head")
    gen "I don't think the girl would be willing to--" ("base", xpos="far_left", ypos="head")
    sna "Those naked, perfectly shaped breasts..." ("snape_40")
    sna "Those magnificent long legs..." ("snape_41")
    sna "Her ample and tender behind..." ("snape_40")
    sna "I've seen everything..." ("snape_41")
    sna "I've seen it all!" ("snape_46")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    sna "As much of a nuisance I think the girl is..." ("snape_43")
    sna "{size=+7}I could stare at those tits all day!!!{/size}" ("snape_33")
    gen "..." ("base", xpos="far_left", ypos="head")
    sna "You've got to invite me next time, my friend!" ("snape_35")
    sna "My life depends on it!" ("snape_36")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Sure, why the hell not.\"":
            pass
        "\"*Uhh*\"":
            pass

    sna "Splendid!" ("snape_45")
    sna "I can hardly wait, I tell you!" ("snape_37")
    sna "Do you think she will let me touch them...?" ("snape_47")

    hide snape_main

    nar "You spend the rest of the evening in Snape's company talking about Hermione's naked breasts."

    $ states.sna.ev.hangouts.hermione_strip_invite = True

    jump end_snape_hangout_points



### Snape Narrative ###

label ss_he_story_E1:
    call bld
    gen "Alright. Teach me your wand-based magic now." ("base", xpos="far_left", ypos="head")
    sna "Sure, I could do that..." ("snape_23", ypos="head")
    sna "Or I could tell you some more about those ripe Slytherin sluts..." ("snape_02")
    gen "The latter, please." ("grin", xpos="far_left", ypos="head")
    sna "Great... Get a load of this, then..." ("snape_13")

    hide snape_main

    nar "You spend the evening by discussing all sorts of inappropriate things with Professor Snape."
    nar "You feel a faint bond forming between you two..."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E2:
    call bld
    gen "For our little enterprise to succeed..." ("base", xpos="far_left", ypos="head")
    gen "You need to be more generous with these house point things..." ("base", xpos="far_left", ypos="head")
    sna "Right, of course..." ("snape_09", ypos="head")
    sna "Miss Granger will require a strong incentive..." ("snape_09")
    sna "So putting my house in the lead is essential..." ("snape_09")
    sna "Could take time though..." ("snape_06")
    gen "Take time?" ("base", xpos="far_left", ypos="head")
    gen "Why not just award a couple of hundred points to Slytherin and be done with it?" ("base", xpos="far_left", ypos="head")
    sna "No, we need to be discreet with this..." ("snape_24")
    sna "Awarding a whole bunch of points to my house without any reason could draw unwanted attention..." ("snape_05")
    gen "*Hmm*... I see your point..." ("base", xpos="far_left", ypos="head")

    hide snape_main

    nar "You spend the evening by conspiring against Hermione with professor Snape..."
    nar "The faint bond of friendship between you two strengthens."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E3:
    sna "Have you heard of that \"men's rights movement\" nonsense?" ("snape_01", ypos="head")
    sna "She is smart, popular, and has a will made from iron..." ("snape_01")
    sna "Lately I am starting to feel very doubtful about our whole plan..." ("snape_06")
    gen "You shouldn't though..." ("base", xpos="far_left", ypos="head")
    sna "Is that so..." ("snape_26")
    gen "It may take some time, but I {size=+5}will{/size} break her." ("base", xpos="far_left", ypos="head")
    gen "Just trust me." ("base", xpos="far_left", ypos="head")
    sna "Alright..." ("snape_26")
    sna "What choice do I have but to hope for the best...?" ("snape_06")

    hide snape_main

    nar "You spend the evening by dreading the uncertain future with professor Snape."
    nar "A faint bond of trust is forming between you two."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E4:
    sna "Tell me something, Genie..." ("snape_24", ypos="head")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    sna "Do you believe in the theory of parallel worlds?" ("snape_25")
    gen "Well, it's hard not to. All things considered." ("base", xpos="far_left", ypos="head")
    sna "True..." ("snape_23")
    sna "So, you think somewhere out there is another version of me?" ("snape_05")
    gen "Probably..." ("base", xpos="far_left", ypos="head")
    sna "*Hmm*..." ("snape_23")
    sna "Severus Snape - the ever cheerful white mage..." ("snape_23")
    gen "Sure, why not?" ("base", xpos="far_left", ypos="head")
    sna "What unsettling imagery you put into my mind..." ("snape_03")
    gen "How about another version of that Granger girl?" ("base", xpos="far_left", ypos="head")
    sna "Yes! Hermione Granger - the repulsive slut without any dignity! Yes, I like it!" ("snape_02")
    gen "And what if in that other world the cheerful Severus teams up with some bizarre version of me?" ("base", xpos="far_left", ypos="head")
    gen "And maybe together we train the slut Hermione to be a proper girl and a good student?" ("base", xpos="far_left", ypos="head")
    sna "*Ha-ha-ha*! That's hilarious!" ("snape_28")

    hide snape_main

    nar "You spend the evening discussing science, metaphysics, philosophy, and sluts."
    nar "the bond of friendship between you and Professor Snape strengthens."

    call sly_plus

    jump end_snape_hangout_points



label ss_he_story_intro_E5:
    sna "So... How is our little plan coming along?" ("snape_05", ypos="head")
    sna "Is that wretched girl giving you trouble?" ("snape_05")

    menu:
        "\"Yeah. She's stubborn.\"":
            sna "No surprise there..." ("snape_06")
        "\"No, not really...\"":
            sna "Seriously?" ("snape_05")
            sna "Interesting..." ("snape_05")

    sna "But you are positive you will be able to break her?" ("snape_01")
    gen "Oh, absolutely." ("base", xpos="far_left", ypos="head")
    gen "It may take some time though..." ("base", xpos="far_left", ypos="head")
    sna "Well, we do have time..." ("snape_06")
    sna "You are still pretty much powerless, right?" ("snape_05")
    gen "Yeah, pretty much..." ("base", xpos="far_left", ypos="head")
    sna "Splendid!" ("snape_02")
    gen "......................." ("base", xpos="far_left", ypos="head")
    sna "I mean, it is bad for {size=+5}you{/size}, but good for {size=+5}us{/size}, right?" ("snape_29")
    gen "Right..." ("base", xpos="far_left", ypos="head")

    hide snape_main

    nar "Professor Snape seems to feel awkward about benefiting from your misery..."
    nar "The bond of friendship between you two strengthens slightly..."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_E6:
    call bld
    gen "So, tell me about those Slytherin sluts some more!" ("base", xpos="far_left", ypos="head")
    sna "What can I say? Life's been good to me lately, my friend." ("snape_23", ypos="head")
    sna "These days I have a whole harem of skimpy students to choose from." ("snape_22")
    gen "Nice!" ("grin", xpos="far_left", ypos="head")
    sna "Yes. Thanks to you, I can do whatever the bloody hell I want!" ("snape_02")
    sna "And more importantly..." ("snape_02")
    sna "Whoever the hell I want!" ("snape_13")
    gen "Seriously?" ("base", xpos="far_left", ypos="head")
    sna "Well, sort of..." ("snape_09")
    sna "Obviously I don't actually walk around and \"do whoever I want\"..." ("snape_09")
    sna "But you wouldn't believe what some of those girls are willing to do in exchange for house points!" ("snape_13")
    sna "Or even for the mere promise of good grades..." ("snape_22")

    hide snape_main

    nar "Professor Snape's usual cold exterior disintegrates before your eyes..."
    nar "The bond of your friendship strengthens yet again..."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E7:
    sna "So, back in your world you are some kind of all-powerful being?" ("snape_05", ypos="head")
    gen "Yeah, sort of..." ("base", xpos="far_left", ypos="head")
    sna "Then how come you do the bidding of that Jasmine woman?" ("snape_05")
    gen "Oh... Well..." ("base", xpos="far_left", ypos="head")
    gen "... she is a princess." ("base", xpos="far_left", ypos="head")
    sna "So?" ("snape_05")
    sna "Is she your princess? You are not even human." ("snape_05")
    sna "Did you swear your loyalty to her?" ("snape_05")
    gen "Not really..." ("base", xpos="far_left", ypos="head")
    sna "Why do you even bother then?" ("snape_06")
    sna "The way I see it, you are an all-powerful being, and she is just some muggle..." ("snape_09")
    gen "She's a what?" ("base", xpos="far_left", ypos="head")
    sna "A human... She's just a human..." ("snape_25")
    sna "So why bother trying to please her?" ("snape_05")
    gen "Well, it's complicated..." ("base", xpos="far_left", ypos="head")
    sna ".............." ("snape_05")
    gen ".................." ("base", xpos="far_left", ypos="head")
    sna "She's hot, isn't she?" ("snape_02")
    gen "Smoking..." ("base", xpos="far_left", ypos="head")
    sna "Gotcha." ("snape_23")

    hide snape_main

    nar "You and professor Snape share a bittersweet moment of complete male solidarity."
    nar "The bond of your friendship strengthens."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E8:
    call bld
    sna "Do you think if we wanted to..." ("snape_05", ypos="head")
    sna "We could bring the public flogging back?" ("snape_05")
    gen "What do you mean?" ("base", xpos="far_left", ypos="head")
    sna "Well, years ago flogging was a completely acceptable measure of punishment for the students." ("snape_06")
    sna "*Sigh* Simpler times..." ("snape_06")
    sna "These days students just completely lack discipline..." ("snape_16")
    sna "I would like nothing more than to publicly flog every single one of them..." ("snape_16")
    sna "Especially the girls..." ("snape_22")
    gen "*Hmm*... Fine by me..." ("base", xpos="far_left", ypos="head")
    gen "But won't a reform like that attract unnecessary attention towards us?" ("base", xpos="far_left", ypos="head")
    sna "Yes. You are right, of course." ("snape_29")
    sna "I am getting greedy..." ("snape_29")
    sna "I'm getting drunk with power, my friend!" ("snape_28")
    sna "And this exquisite wine does not improve my judgment in the slightest either!" ("snape_28")

    hide snape_main

    nar "Professor Snape seems to be completely at ease around you now."
    nar "The bond of male friendship between you two strengthens even more.\n>Slytherin house point payouts have increased formidably..."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E9: # Replace this event.
    sna "... so, after that, I return back to Russia, right?" ("snape_24", ypos="head")
    gen "Back to Russia?" ("angry", xpos="far_left", ypos="head")
    sna "But wait, it gets worse." ("snape_01")
    sna "Apparently I am fluent in Russian now." ("snape_05")
    gen "Wait, what?" ("angry", xpos="far_left", ypos="head")
    sna "And I am this miserable muggle guy who lives in this shithole of a town full of run-down buildings." ("snape_06")
    sna "I try to make a living by drawing comics and creating games with \"Ren'Py\"..." ("snape_06")
    sna "And that is so bizarre because I don't even know what a \"Ren'Py\" is!" ("snape_24")
    gen "*Hmm*... Then what happened?" ("base", xpos="far_left", ypos="head")
    sna "Not much... Mostly worked my ass off for months..." ("snape_05")
    sna "Then managed to create a relatively successful game somehow..." ("snape_05")
    sna "Eventually began to make decent money with my craft..." ("snape_24")
    sna "And then, just when I was about to allow myself to feel hopeful about the future..." ("snape_06")
    sna "I woke up..." ("snape_04")
    sna "...................." ("snape_09")
    gen "......................" ("base", xpos="far_left", ypos="head")
    sna "What do you think all of that means?" ("snape_05")
    gen "Some form of self insert, probably." ("base", xpos="far_left", ypos="head")
    sna "What?" ("snape_05")
    gen "Just ignore the whole thing." ("base", xpos="far_left", ypos="head")
    gen "A silly dream, nothing more." ("base", xpos="far_left", ypos="head")
    sna "Felt more like a nightmare..." ("snape_29")

    hide snape_main

    nar "Professor Snape trusts you more than he used to..."
    nar "To the point where he doesn't think twice about sharing his weird-ass dreams with you."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E10:
    sna "What is the meaning of life, Genie?" ("snape_29", ypos="head")
    gen "What?" ("angry", xpos="far_left", ypos="head")
    sna "Since you are an all-powerful being, you've got to know things like that, right?" ("snape_05")
    gen "Maybe..." ("base", xpos="far_left", ypos="head")
    sna "Great. Tell me then." ("snape_06")
    gen "*Hmm*... You sure you're ready for this?" ("base", xpos="far_left", ypos="head")
    sna "Yes. Lay it on me, friend." ("snape_05")
    gen "Alright then..." ("base", xpos="far_left", ypos="head")
    sna "................!" ("snape_01")
    gen "It's plastic..." ("base", xpos="far_left", ypos="head")
    sna "I beg your pardon?" ("snape_05")
    gen "It's plastic..." ("base", xpos="far_left", ypos="head")
    sna "I don't get it..." ("snape_25")
    gen "This planet plans to evolve into something else in a million years or so..." ("base", xpos="far_left", ypos="head")
    gen "In order to do that it needs a special kind of material that it can't produce on its own." ("base", xpos="far_left", ypos="head")
    gen "So it spawns a new form of life - humans." ("base", xpos="far_left", ypos="head")
    sna ".............." ("snape_11")
    gen "You wanted to know the purpose of your existence?" ("base", xpos="far_left", ypos="head")
    gen "It's to produce plastic. Simple as that." ("base", xpos="far_left", ypos="head")
    sna "Are you fucking kidding me?!" ("snape_30")
    sna "No, no... That can't be it..." ("snape_26")
    gen "*He-heh*..." ("grin", xpos="far_left", ypos="head")
    sna "Are you pulling my leg?" ("snape_25")
    gen "You should've seen your face." ("grin", xpos="far_left", ypos="head")
    sna "You really had me worried there, you bloody non-human bastard!" ("snape_15")
    gen "I know! It was hard to resist..." ("grin", xpos="far_left", ypos="head")

    hide snape_main

    nar "You spend the evening by skilfully avoiding a whole variety of similar questions."
    nar "Despite your refusal to co-operate, the bond of friendship between you two strengthens yet again."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E11:
    sna "So... Back in your world, do you people have a country named England?" ("snape_05", ypos="head")
    gen "We used to..." ("base", xpos="far_left", ypos="head")
    sna "What happened?" ("snape_26")
    gen "\"The great catastrophe\"..." ("base", xpos="far_left", ypos="head")
    gen "It incinerated most of the world's population in a matter of hours..." ("base", xpos="far_left", ypos="head")
    sna "................" ("snape_26")
    gen "Turning about eighty percent of the planet's surface into a scorching desert..." ("base", xpos="far_left", ypos="head")
    gen "And the remaining twenty percent into an icy wasteland..." ("base", xpos="far_left", ypos="head")
    gen "............." ("base", xpos="far_left", ypos="head")
    sna "That is..." ("snape_26")
    sna "Horrible..." ("snape_06")
    sna "Are you sure that you want to return to that place?" ("snape_25")
    gen "Of course." ("base", xpos="far_left", ypos="head")
    gen "It may be a bit barbaric, but hey... it's home." ("base", xpos="far_left", ypos="head")

    hide snape_main

    nar "Professor Snape finds a new level of respect for you..."
    nar "The bond of friendship between you two solidifies."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E12:
    sna "I've been thinking about what you've said the other day..." ("snape_09", ypos="head")
    sna "About your home world being nothing but a scorched desert and all..." ("snape_09")
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    sna "Do you think Albus will be alright there?" ("snape_06")
    gen "Oh, absolutely!" ("base", xpos="far_left", ypos="head")
    gen "Since I quite literally replaced him in his chair..." ("base", xpos="far_left", ypos="head")
    gen "He probably replaced me in exactly the same place back in Agrabah." ("base", xpos="far_left", ypos="head")
    sna "Agrabah?" ("snape_05")
    gen "Yes... A very big city." ("base", xpos="far_left", ypos="head")
    gen "One of the few that rose after the great catastrophe." ("base", xpos="far_left", ypos="head")
    gen "Probably the biggest of them all as well..." ("base", xpos="far_left", ypos="head")
    gen "The heart of the human civilization if you will." ("base", xpos="far_left", ypos="head")
    sna "I am relieved to hear that..." ("snape_23")
    gen "Sure..." ("base", xpos="far_left", ypos="head")
    gen "Although if your Albus friend really materialised in exactly the same spot I occupied before I cast the spell..." ("base", xpos="far_left", ypos="head")
    gen "I suppose the princess could have him beheaded..." ("base", xpos="far_left", ypos="head")
    sna "WHAT?!" ("snape_01")
    gen "But the probability of that happening is very slim..." ("base", xpos="far_left", ypos="head")
    gen "About five percent... Maybe ten... Twenty percent tops." ("base", xpos="far_left", ypos="head")
    sna "......................................................." ("snape_03")

    hide snape_main

    nar "Professor Snape seems grateful to you for {i}sort of{/i} putting his concerns about Albus Dumbledore's well-being to rest..."
    nar "The bond of your friendship strengthens yet again..."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E13:
    sna "You know what?" ("snape_01", ypos="head")
    gen "What?" ("base", xpos="far_left", ypos="head")
    sna "For the first time in a very long time..." ("snape_01")
    sna "I think..." ("snape_03")
    sna "I am actually content with the way my life is going." ("snape_25") # 0_0
    sna "What an unsettling feeling..." ("snape_26")
    gen "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?" ("base", xpos="far_left", ypos="head")
    sna "Could be." ("snape_22")
    sna "Nonetheless, training that girl had such a great impact on my life..." ("snape_24")
    sna "And even the school itself..." ("snape_24")
    gen "In other words, you are getting less broody, and you blame me." ("base", xpos="far_left", ypos="head")
    sna "Something like that..." ("snape_23")
    sna "I'm losing my dark presence, man." ("snape_28") # :)

    hide snape_main

    nar "Professor Snape really did become a little more cheerful lately..."
    nar "He even looks younger now than back when you first met him..."
    nar "Professor Snape's feeling of gratitude fortifies the bond of your friendship."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_E14:
    sna "... So, she says, \"Sir, could you choke me a little, please\"!" ("snape_02", ypos="head")
    sna "And I am happy to oblige of course!" ("snape_13")
    sna "So, I choke that little bitch while I'm fucking her, right?" ("snape_19")
    sna "And she rolls her eyes up to the point where I can't even see her pupils anymore!" ("snape_19")
    sna "Her face turns to a cute tint of purple, and she's barely breathing." ("snape_19")
    sna "So I think that maybe I should loosen up my grip a little..." ("snape_14")
    sna "And that's when the bitch starts to cum!" ("snape_21")
    gen "Sweet! And then you woke up?" ("base", xpos="far_left", ypos="head")
    sna "What? No, it actually happened." ("snape_05")
    sna "I finally nailed that blond witch from Slytherin." ("snape_13")
    gen "Nice!" ("grin", xpos="far_left", ypos="head")
    sna "I know." ("snape_13")
    sna "She is pretty twisted though..." ("snape_25")
    sna "And I mean really fucking messed up." ("snape_26")
    gen "Our type of girl!" ("grin", xpos="far_left", ypos="head")
    sna "Exactly!" ("snape_22")

    hide snape_main

    nar "You and professor Snape bond over the similarities of your taste in women."
    nar "The bond of your friendship has never been stronger."

    call sly_plus

    jump end_snape_hangout_points


label ss_he_story_intro_E15:
    sna "It's been a while now..." ("snape_05", ypos="head")
    gen "What do you mean?" ("base", xpos="far_left", ypos="head")
    sna "The spell that brought you here..." ("snape_24")
    sna "You said it would wear off in time..." ("snape_24")
    sna "Do you feel any different?" ("snape_05")
    gen "No... Not really..." ("base", xpos="far_left", ypos="head")
    gen "Maybe it needs more time?" ("base", xpos="far_left", ypos="head")
    sna "Could be..." ("snape_01")
    sna "Or there could be something else..." ("snape_01")
    gen "Like what?" ("base", xpos="far_left", ypos="head")
    sna "No idea..." ("snape_09")
    sna "But I shall give this some more thought..." ("snape_09")
    sna "Oh, and one more thing..." ("snape_24")
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    sna "This time of the year is usually pretty busy..." ("snape_24")
    sna "Even more so now when I need to constantly cover up for Albus' absence." ("snape_24")
    gen "..................." ("base", xpos="far_left", ypos="head")
    sna "I'm not sure how often I will be able to spend my evenings with leisurely drinking wine anymore..." ("snape_06")
    gen "Really?" ("base", xpos="far_left", ypos="head")
    sna "Yes..." ("snape_06")
    sna "I'll still be around for a quick chat from time to time, but that's about it." ("snape_06")
    gen "I see..." ("base", xpos="far_left", ypos="head")
    gen "I will have to find another way of spending my evenings from now on then..." ("base", xpos="far_left", ypos="head")
    sna "I'm sure miss Granger will be happy to help." ("snape_02")
    gen "Yes, for as long as Slytherin is in the lead." ("base", xpos="far_left", ypos="head")
    sna "Seriously? She still cares about that?" ("snape_05")
    gen "Very much so." ("base", xpos="far_left", ypos="head")
    sna "Well, in that case, I shall personally ensure that the Slytherin house gets as many house points as possible." ("snape_23")

    hide snape_main

    nar "Your friendship level with professor Snape reached its maximum value."
    nar "Congratulations. If this were a \"Dating Sim\" you would be getting the ending with Severus Snape."
    nar "The Slytherin house point payout has increased greatly and reached its maximum level."
    nar "Any future hangouts will result in a small bump in house points for Slytherin."

    jump end_snape_hangout_points

label sly_plus:
    call notes
    nar "The Slytherin house point payout has increased..."
    return
