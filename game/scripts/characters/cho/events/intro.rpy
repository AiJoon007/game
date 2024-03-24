

### Cho Intro ###

### Event 1 ###
# Fist visit of Cho, complains about Hermione.
# Hermione enters, and they have a fight.

label cho_intro_E1:

    # Force default outfit for first event.
    $ cho.equip(cho_outfit_default)

    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"
    gen "(...)" ("base", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    gen "(Who's that?)" ("base", xpos="far_left", ypos="head")
    gen "(Can't be Hermione, she never knocks anymore.)" ("base", xpos="far_left", ypos="head")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "I bet it's another girl!" ("grin", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    gen "Please, give me a moment..." ("base", xpos="far_left", ypos="head")
    gen "I just need to--{w=1.0} *Urgh*!" ("angry", xpos="far_left", ypos="head")
    play sound "sounds/cloth_sound.ogg"
    gen "Adjust my pants...{w=1.0} There we go." ("base", xpos="far_left", ypos="head")

    $ d_flag_01 = False

    menu:
        "\"Who is it?\"":
            $ d_flag_01 = True

            call bld
            cho "Cho Chang, Sir."
            gen "(Such a cute name... Please be hot, please be hot...!)" ("angry", xpos="far_left", ypos="head")
            cho "May I come in?"
            gen "Please have nice tits!" ("grin", xpos="far_left", ypos="head")
            cho "Sir?"
            gen "Oh, right... Come in." ("base", xpos="far_left", ypos="head")

        "\"Come in!\"":
            pass


    # Cho enters your office for the first time.
    call cho_walk("desk", "base", action="enter")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    $ cho.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")

    show CG cho as cg zorder 17:
        zoom 0.5
    with fade

    cho "Good morning, Sir." ("base", "base", "base", "mid", xpos="mid", ypos="base")

    menu:
        "\"Hello, Miss Chang.\"" if d_flag_01 == True:
            cho "Hello to you too, Professor." ("smile", "base", "base", "mid")

        "\"Hello, Princess.\"":
            cho "*Uhm*..." ("annoyed", "wide", "base", "mid")
            cho "Sir, I'd much prefer not to be called nicknames." ("open", "closed", "base", "mid")
            cho "Mutual respect is very important for a student-teacher relationship to work." ("open", "base", "base", "down")
            gen "(She must be fun at parties...)"
            cho "I'd much prefer if you called me Cho, or Miss Chang..." ("open", "base", "raised", "mid")
            gen "And how is that any different..."
            cho "It's my name, Sir!" ("annoyed", "narrow", "base", "mid")
            gen "I see..."
            gen "Very well... Miss Chang it is..."
            cho "Thank you." ("smile", "base", "base", "mid")
            cho "Anyway..." ("silly", "happyCl", "base", "mid")

        "\"Hey there, Chap.\"":
            cho "Sir?" ("clench", "wide", "base", "mid")
            gen "What?"
            cho "I'm a girl!" ("angry", "narrow", "angry", "mid")
            gen "Oh, of course you are... You just seemed a bit..."
            cho "A bit what?" ("annoyed", "narrow", "angry", "mid")
            gen "(Don't say tomboy-ish, don't say tomboy-ish...)"

            menu: # doesn't matter what you pick
                "\"Tomboyish\"":
                    pass
                "\"Flat\"":
                    pass
                "\"Short\"":
                    pass

            cho "What? Professor how dare you suggest I--" ("clench", "wide", "base", "mid")
            gen "Hold on!"
            gen "Silly me, I forgot where I put my glasses."
            cho "" ("annoyed", "narrow", "angry", "mid")
            gen "You have to excuse my poor eye-sight."
            gen "I'm very,{w} very,{w} very,{w} very old."
            gen "You're clearly \"not\" a boy..."
            gen "(Smooth...)"
            cho "Right... Well, since you seem unable to see very well..." ("open", "narrow", "base", "downR")
            gen "..."
            cho "It's Cho Chang." ("base", "narrow", "base", "mid")
            gen "Ah, Miss Chang..."
            gen "(Should I know who she is?)"
            cho "Yes, anyway..." ("open", "closed", "base", "mid")

        "\"Xiao Hua...\"":
           cho "*Uhm*... thanks..." ("normal", "narrow", "raised", "mid")
           cho "But I don't speak that much Mandarin, Sir." ("open", "closed", "base", "mid")
           cho "I was actually born here..." ("base", "narrow", "base", "mid")
           gen "Where?"
           cho "In Scotland, Sir." ("angry", "wink", "base", "mid")
           cho "People always act surprised when they find that out." ("open", "base", "base", "R")
           cho "It doesn't help that my name sounds so Asian...{w} Cho Chang..." ("annoyed", "narrow", "angry", "up")
           gen "..."
           cho "Anyway..." ("open", "closed", "base", "mid")

    hide cg
    with fade

    cho "I'm terribly sorry for bothering you, Sir.{w=0.8} I hope I'm not interrupting anything important." ("open", "base", "worried", "mid")
    gen "No worries, I can always spare some of my...{w=0.6} valuable time...{w=1.0} *Ahem*{w=0.6} for my dear students..." ("base", xpos="far_left", ypos="head")
    gen "What's on your mind?" ("grin", xpos="far_left", ypos="head")

    # Talk about her issue with Hermione
    cho "It's-- It's Hermione Granger, Sir." ("annoyed", "narrow", "worried", "R")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "-The Granger girl?-":
            gen "What did she do this time?" ("base", xpos="far_left", ypos="head")
            pass
        "-That troublemaker...-":
            gen "I promise you, I'll give her a good {i}ole fashioned spanking{/i} next time I see her." ("grin", xpos="far_left", ypos="head")
            cho "A Spanking?" ("angry", "wide", "base", "mid")
            cho "And why would you do that, Professor?" ("open", "narrow", "raised", "mid")
            cho "(He really must be old...{w} They probably did stuff like that all the time back in the day...)" ("angry", "narrow", "worried", "downR")
            pass

    cho "Well Sir, it's about that new movement of hers..." ("open", "closed", "base", "mid")
    gen "The \"Men's rights movement?\" I'm familiar." ("base", xpos="far_left", ypos="head")
    cho "Not that one, Sir...{w=0.8} The other one..." ("open", "narrow", "worried", "downR")
    gen "Oh good...{w=0.5} another one..." ("angry", xpos="far_left", ypos="head")
    cho "Yes... And you need to stop it, Professor!" ("angry", "base", "base", "mid")
    cho "Her{w=0.5} \"Quidditch equality movement\"." ("soft", "narrow", "angry", "mid")
    gen "Her what now?" ("base", xpos="far_left", ypos="head")
    cho "I know! It's absolutely ridiculous...{w=0.5} It's going to ruin the sport for all of us!" ("clench", "base", "worried", "mid")

    gen "Sport? Which sport?" ("base", xpos="far_left", ypos="head")
    cho "Quidditch!" ("scream", "narrow", "angry", "mid")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "(Quidditch? What a stupid name for a sport.)" ("base", xpos="far_left", ypos="head")
    cho "The movements' goal is to grant a larger portion of our female students the ability to play." ("open", "narrow", "base", "down")
    gen "And...{w} that's a bad thing?" ("base", xpos="far_left", ypos="head")
    cho "What she is doing to try and achieve it is..." ("annoyed", "narrow", "angry", "R")
    cho "Granger is trying to separate us into male and female teams." ("annoyed", "narrow", "worried", "mid")
    cho "She believes it would put girls on an equal playing field against other girl teams." ("open", "closed", "worried", "mid")
    cho "But what she's forgetting is that all the female players who made it into a team are already considered a valuable asset -- or they wouldn't be there!" ("open", "narrow", "angry", "R")
    cho "I worked hard to be at the same level as my fellow teammates..." ("annoyed", "narrow", "worried", "downR")
    cho "Splitting us up into a male and female league would just bring on girls that are just there to flaunt their bodies, instead of taking the sport seriously..." ("open", "narrow", "angry", "downR")
    gen "Doesn't sound like the worst idea, honestly..." ("base", xpos="far_left", ypos="head")
    cho "Sir... I've trained all my life to be where I'm at." ("clench", "narrow", "angry", "mid")
    cho "Just as hard as all the other great female Quidditch players of history!" ("scream", "closed", "angry", "mid")
    cho "They played side by side with men... Earning their place amongst the best!" ("open", "narrow", "angry", "down")
    cho "It never mattered what gender they were." ("angry", "narrow", "angry", "mid")
    cho "To be shoved aside and forced to play alongside a collection of mediocre amateurs..." ("clench", "closed", "angry", "down")
    cho "If this goes through it'd mean that I would never get a proper chance at winning the Quidditch cup!" ("clench", "closed", "angry", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    cho "Sir... This would destroy the foundations of the entire sport, traditions going back centuries..." ("open", "narrow", "angry", "down")
    gen "Now, I think you're being a bit overdramatic Miss--" ("base", xpos="far_left", ypos="head")
    cho "I'd get even less attention as one of the few girls in the league!" ("open", "narrow", "angry", "mid")
    gen "Ah... So, that's where the problem lies." ("base", xpos="far_left", ypos="head")

    cho "Sir, could you please talk to her? I'd be very grateful if you did." ("upset", "base", "worried", "mid")
    cho "I would be forever in your debt." ("soft", "narrow", "base", "mid")
    gen "Forever in my debt you say?" ("base", xpos="far_left", ypos="head")
    cho "Yes, Professor. I'd do anything if you make this right." ("smile", "base", "angry", "mid")
    cho "Anything!" ("clench", "narrow", "angry", "mid")
    gen "It's your lucky day, Miss Chang!" ("grin", xpos="far_left", ypos="head")
    gen "I will gladly talk to Miss Granger, but in return..." ("base", xpos="far_left", ypos="head")
    gen "How about you come over here and suck on my--" ("grin", xpos="far_left", ypos="head")

    # Hermione walks in
    stop music fadeout 1.0
    call hide_characters

    play sound "sounds/door.ogg"
    call her_chibi("stand", "door", "base")
    with d3

    her "Professor, I'm sorry to bother you, but I wanted to..." ("open", "closed", "base", "mid", xpos="base", ypos="base", flip=False)
    her "!!!" ("normal", "wide", "base", "stare", trans=hpunch)

    call her_walk(570, "base")
    call her_chibi("stand",570,"base")
    pause .5

    play music "music/deadly-roulette-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    cho "" ("annoyed", "narrow", "angry", "downR", xpos="mid", ypos="base")
    her "Cho...{w=0.5} How nice to see you here..." ("open", "closed", "base", "mid")
    her "And why are you here exactly?" ("annoyed", "narrow", "annoyed", "L")

    cho "Oh, you know...{w=0.5} Just having a discussion with our dear headmaster..." ("soft", "base", "base", "R")

    play sound "sounds/slap_03.ogg"
    her "{size=-5}Bitch...{/size}" ("angry", "closed", "angry", "mid", trans=hpunch)

    play sound "sounds/slap_02.ogg"
    cho "{size=-5}Whore...{/size}" ("clench", "closed", "angry", "mid", trans=hpunch)
    her @ cheeks blush "..." ("normal", "squint", "angry", "L")
    cho "..." ("upset", "narrow", "base", "L")
    her @ cheeks blush "So... What have you been discussing?{w=0.4} Anything I should know?" ("open", "squint", "base", "mid")
    cho "Oh, it's nothing that you need to worry your pretty little head about..." ("smile", "closed", "angry", "mid")
    gen "(This could take a while...)" ("base", xpos="far_left", ypos="head")


    # Choice to start jerking off
    menu:
        "\"(I will jerk off a little while they talk.)\"":
            call hide_characters
            with d3
            pause .2

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .5

            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.stats.masturbated_to_hermione += 1
            $ states.cho.ev.intro.masturbated = True # Optional dialogue with Snape.

            $ states.gen.masturbating = True

        "\"(I should probably listen to them.)\"":
            $ states.gen.masturbating = False

    # Masturbating
    if states.gen.masturbating:
        nar "You pull your cock out and begin masturbating... focusing on the now heated argument between the two girls in front of you."

        cho "" (trans=d3)
        her "Oh yeah, well... I bet it can't be anything good, seeing how you usually act around men..." ("mad", "narrow", "angry", "L")
        cho "What's that supposed to mean?!?" ("clench", "base", "angry", "R")
        her "You know exactly what I mean..." ("crooked_smile", "narrow", "base", "R_soft")
        her "I heard about how you were flaunting those... \"things\" of yours at Seamus Finnigan." ("crooked_smile", "narrow", "base", "R_soft")
        with hpunch
        cho "\"Things\"?" ("angry", "narrow", "angry", "R")
        cho "Oh, miss perfect Hermione Granger.{w=0.8} Too afraid to even use the word \"tits\"..." ("open", "narrow", "angry", "R")
        her @ cheeks blush "Well yours hardly qualify as such..." ("annoyed", "narrow", "angry", "L")
        cho "How dare you!" ("clench", "closed", "angry", "mid")
        cho "And so what? What's wrong with being confident about your body..." ("open", "narrow", "angry", "down")
        cho "You should try it sometime... You might even get a boyfriend one day..." ("soft", "narrow", "angry", "R")
        cho "Though what do I know..." ("open", "closed", "base", "mid")
        cho "I didn't need to get my teeth shortened, just so I wouldn't be confused for a rabbit!" ("grin", "closed", "angry", "mid")
        her @ cheeks blush "..." ("normal", "narrow", "angry", "down")
        cho "Not that anyone would even see them through that horribly bushy hair of yours..." ("smile", "narrow", "angry", "R")
        her @ cheeks blush "Well, I heard that you were caught snogging someone in one of the carriages after the triwizard tournament." ("soft", "closed", "base", "mid")
        her @ cheeks blush "I'm sure that will go down in the Hogwarts book of history..." ("grin", "narrow", "base", "mid")
        gen "(How naughty, didn't expect such indecent behaviour from a girl with such a cute face...)" ("grin", xpos="far_left", ypos="head")
        cho "Yeah? You ever even kissed a boy before, Granger?" ("soft", "narrow", "raised", "R")
        her @ cheeks blush "" ("normal", "base", "worried", "R")
        cho "And I'm talking about a real kiss, and not your daddy kissing you good night..." ("soft", "narrow", "raised", "R")
        her @ cheeks blush "Oh...{w=0.5} Of course I have!" ("angry", "base", "worried", "R")
        her @ cheeks blush "Just because I don't jump on every opportunity to glimpse random boys' wands..." ("soft", "closed", "base", "mid")
        her @ cheeks blush "Unlike some other girls at this school..." ("normal", "narrow", "angry", "L")
        her @ cheeks blush "That doesn't mean I've never kissed anyone..." ("soft", "base", "worried", "mid")
        gen "..." ("grin", xpos="far_left", ypos="head")
        her @ cheeks blush "And I didn't need to have my breasts enlarged so that I wouldn't be confused for a boy!" ("annoyed", "narrow", "annoyed", "L")
        cho "Oh yeah... Like you haven't been flaunting yours around either..." ("open", "narrow", "angry", "R")
        cho "Don't you try and act all innocent!" ("upset", "narrow", "angry", "R")
        her @ cheeks blush "As If..." ("normal", "narrow", "annoyed", "mid")
        cho "I wouldn't doubt that's why you're here in the first place!" ("open", "closed", "base", "mid")
        cho "To push your stupid agendas, whilst you push your breasts together at the same time." ("clench", "narrow", "angry", "L")
        gen "{size=-4}You fucking sluts!{/size}" ("angry", xpos="far_left", ypos="head")

        # Genie cums
        call hide_characters
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        gen "*heavy breathing* {size=-4}Fuck yes...{/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block

        gen "*Argh!* {size=-4}You whores!{/size}" ("angry", xpos="far_left", ypos="head")

        stop music fadeout 2.0
        cho "Sir?" ("soft", "narrow", "base", "mid")

        gen "(Shit...)" ("base", xpos="far_left", ypos="head")

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        cho "Sir, I'm sorry about all this... it's not what I came here for..." ("open", "closed", "worried", "mid")
        gen "Oh, of course not!" ("base", xpos="far_left", ypos="head")
        cho "Please consider what we've talked about..." ("open", "closed", "base", "mid")
        gen "Certainly..." ("base", xpos="far_left", ypos="head")

        # Cho walks to the door and stops.
        call cho_walk("door", "base")
        pause .8
        call cho_chibi("stand", "door", "base")
        with d3
        pause .8

        cho "{size=-4}You have fun now... getting at that wand of his...{/size}" ("soft", "narrow", "angry", "L", xpos="base", ypos="base", trans=dissolve)
        her "*Tzzzh!*..." ("clench", "closed", "angry", "mid", xpos="mid", ypos="base", trans=d3)


    # Not masturbating
    else:
        gen "Ladies, no arguing now..." ("base", xpos="far_left", ypos="head")
        gen "You're in the headmaster's office, surely there's a time and place." ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "narrow", "base", "R_soft")
        cho "*Hmph*... There's no argument here..." ("open", "narrow", "angry", "L")
        cho "I'm sure that Hermione's reasons for interrupting are totally valid..." ("upset", "narrow", "angry", "R")
        her "And I'm sure Cho wasn't just coming here to flaunt her body..." ("soft", "narrow", "base", "L")
        cho "What's that supposed to mean?!?" ("clench", "narrow", "angry", "R", trans=vpunch)
        gen "(I guess I'll just have to wait this one out...)" ("base", xpos="far_left", ypos="head")

        # Black screen
        call hide_characters
        call blkfade
        pause 2

        centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

        pause 1
        call hide_blkfade

        play sound "sounds/snore1.ogg"
        gen "*Snore*{w=2.0}{nw}"
        her "" ("annoyed", "narrow", "annoyed", "R")
        cho "As if I'm going to believe that nonsense, Granger!" ("angry", "narrow", "angry", "R", trans=vpunch)
        play sound "sounds/snore2.ogg"
        gen "......{w=0.5}*Snore*{w=1.0}{nw}"
        her "I had completely legitimate reasons for coming here..." ("soft", "closed", "base", "mid")
        her "You tell her Professor!" ("open", "base", "annoyed", "mid")
        play sound "sounds/snore3.ogg"
        gen "*Sn{cps=8}oooooooreeee*{/cps}{w=2.0}{nw}"
        her "Professor!" ("scream", "base", "angry", "mid", trans=hpunch)
        gen "*Grunt* {size=-4}Huh, what?{/size}" ("angry", xpos="far_left", ypos="head")
        her "I always have a valid reason for coming here, don't I?" ("base", "base", "base", "mid")
        gen "Of course you--" ("base", xpos="far_left", ypos="head")
        cho "Always? So, you \"do\" come here often!" ("smile", "narrow", "base", "R")
        her "So what..." ("angry", "closed", "angry", "mid")
        gen "Ladies, I think it's time to--" ("base", xpos="far_left", ypos="head")
        cho "Don't worry about it Sir, I was just about to leave anyway..." ("soft", "narrow", "angry", "mid")
        her "..." ("annoyed", "narrow", "angry", "R")

        # Cho walks to the door and stops.
        call cho_walk("door", "base")
        pause .8
        call cho_chibi("stand", "door", "base")
        with d3
        pause .8

        cho "Professor, please do consider what we discussed earlier..." ("soft", "closed", "base", "mid", xpos="base", ypos="base", trans=dissolve)
        gen "Of course." ("base", xpos="far_left", ypos="head")
        her "*Hmm*?" ("normal", "squint", "base", "R", xpos="mid", ypos="base", trans=dissolve)

        stop music fadeout 2.0

    hide cho_main
    hide hermione_main
    with d3

    # Cho leaves
    pause .2
    call cho_chibi("stand", "door", "base",flip=True)
    with d3
    pause .5

    call cho_chibi("leave")

    her "..." ("annoyed", "base", "angry", "mid", trans=d3)
    gen "..." ("base", xpos="far_left", ypos="head")
    her "You're buying favours from her aren't you?" ("soft", "narrow", "base", "mid_soft")
    gen "I'm--" ("base", xpos="far_left", ypos="head")
    her "I knew it!" ("angry", "base", "angry", "mid")
    gen "Now, if you could just listen for a second!" ("angry", xpos="far_left", ypos="head")
    her "I don't want to hear it!" ("open", "closed", "base", "mid")
    her "I'm leaving." ("normal", "squint", "angry", "mid")

    # Hermione leaves
    call her_walk(action="leave")

    # Hermione Mood down
    $ states.her.mood += 6
    $ states.her.busy = True

    $ states.cho.ev.intro.e1_complete = True

    gen ".......{w=0.5} Women..." ("base", xpos="far_left", ypos="head")

    call gen_chibi("sit_behind_desk")
    call music_block
    jump main_room_menu


### Event 2 ###
# Cho complains about Hermione again.
# You need to talk to Hermione and have her drop her Quidditch movement.
# You need to tell Snape about Cho. (Hangout)

label cho_intro_E2:
    stop music fadeout 1.0
    play sound "sounds/door.ogg"
    call cho_chibi("stand", "door", "base")
    with d3
    pause .5
    call cho_chibi("stand", "door", "base",flip=True)
    with d1
    play sound "sounds/kick.ogg"
    pause .8
    call cho_chibi("stand", "door", "base",flip=False)
    with d1
    pause .3
    call cho_walk("desk", "base")
    pause .2

    cho "I hate her!" ("scream", "closed", "angry", "mid", xpos="mid", ypos="base", trans=hpunch)
    cho "" ("clench", "narrow", "angry", "mid")

    gen "Miss Chang! My favourite student!" ("grin", xpos="far_left", ypos="head")
    gen "I'm so glad to see you. Is there something I can--" ("grin", xpos="far_left", ypos="head")

    play music "music/hitman.ogg" fadein 1 if_changed
    cho "Cut the crap, Professor!{w=0.6} I know you've told her!" ("soft", "narrow", "angry", "mid")
    gen "{size=-4}Please don't hurt me.{/size}" ("angry", xpos="far_left", ypos="head")
    cho "How could you have done this?{w=0.6} Sending this dim-witted Gryffindor tramp after me?" ("open", "narrow", "angry", "mid")
    gen "W-who?" ("angry", xpos="far_left", ypos="head")
    cho "Granger!" ("scream", "closed", "angry", "mid", trans=hpunch)
    gen "Aaa-h!" ("angry", xpos="far_left", ypos="head") # Girly scream
    cho "Gryffindor's role model student..." ("angry", "narrow", "angry", "mid")
    cho "She's out there spreading mean rumours about me!" ("open", "narrow", "angry", "R")
    gen "How mean are we talking?" ("base", xpos="far_left", ypos="head")
    cho "The worst kind! That I'm cheating at Quidditch!" ("angry", "narrow", "angry", "down")
    cho "How am I cheating, Professor? Ravenclaw is always in last place?!" ("soft", "narrow", "worried", "downR")
    cho "Not to mention that she's told everyone that I'm whoring myself out to my other classmates, and even my teachers!" ("open", "narrow", "angry", "L")
    cho "I did none of that, Professor! None!" ("scream", "closed", "angry", "mid", trans=hpunch)
    cho "And she still won't lay off her stupid equality movement thing!" ("annoyed", "narrow", "angry", "mid")
    gen "You need to calm down, girl." ("base", xpos="far_left", ypos="head")
    cho "{size=-4}When I'm out of here I'm going to rip that bitch's head off...{/size}" ("clench", "narrow", "angry", "downR")
    gen "(Yikes!)" ("angry", xpos="far_left", ypos="head")
    gen "I could hear that." ("base", xpos="far_left", ypos="head")
    cho "Good. Then you already know what I'm willing to do if this continues..." ("open", "closed", "angry", "mid")
    cho "If you can't stop her, Professor, Then I will!" ("open", "base", "angry", "mid")
    cho "And rest assured that I will end her!" ("soft", "narrow", "angry", "mid")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Sure, go for it!\"":
            cho "What?" ("annoyed", "narrow", "angry", "mid")
            cho "Sir, I'm not joking around. This is serious!" ("open", "base", "angry", "mid")
            cho "Tell Granger to keep her bushy head out of it!" ("clench", "narrow", "angry", "mid")
            gen "Fine, whatever... This isn't worth the drama..." ("base", xpos="far_left", ypos="head")
            gen "(I can just bribe Granger with some house points anyway.)" ("base", xpos="far_left", ypos="head")
            gen "I shall talk to her." ("base", xpos="far_left", ypos="head")

        "\"I'd prefer you didn't...\"":
            cho "Then do something about it!" ("clench", "closed", "angry", "mid")
            cho "And don't even think about calling me to your office again..." ("open", "narrow", "angry", "mid")
            cho "Not until you've dealt with that skank!" ("clench", "narrow", "angry", "mid")
            cho "Do I make myself clear, Sir?" ("scream", "closed", "angry", "mid", trans=hpunch)
            cho "" ("angry", "narrow", "angry", "mid")
            gen "I suppose..." ("base", xpos="far_left", ypos="head")

    # Back to cheerful.
    play music "music/Music for Manatees.ogg" fadein 1 if_changed
    cho "Good." ("base", "base", "base", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    cho "Have a nice evening, Professor." ("smile", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    gen "I better talk to Hermione about this..." ("base", xpos="far_left", ypos="head")
    gen "Or Snape first. Maybe he can help me more." ("base", xpos="far_left", ypos="head")
    gen "With his unfailing wisdom." ("angry", xpos="far_left", ypos="head")
    gen "Who am I even kidding..." ("base", xpos="far_left", ypos="head")

    $ states.her.busy = True
    $ states.sna.busy = False

    $ states.cho.ev.intro.e2_complete = True

    $ states.cho.unlocked = True
    $ achievements.unlock("unlockcho", True)
    call popup("{size=-4}You can now summon Cho into your office.{/size}", "Character unlocked!", "interface/icons/head/cho.webp")
    $ states.cho.busy = True

    jump main_room_menu


### Snape Hangout Event 1 ###
# You tell Snape about Cho's visit.

label ss_he_cho_E1:
    call bld
    gen "I had another girl visiting me the other day." ("base", xpos="far_left", ypos="head")
    sna "I told you not to get involved with the outside world." ("snape_09", ypos="head")
    sna "I hope you were smart enough to not let her into your office." ("snape_05")
    gen "How couldn't I let her in? She sounded cute." ("grin", xpos="far_left", ypos="head")
    sna "Why doesn't that surprise me..." ("snape_06")
    sna "And who was this girl?" ("snape_03")

    menu:
        "\"Her name was Cho Chan.\"":
            sna "Cho Chang?" ("snape_01")
            gen "No, I'm sure it was \"Chan\"." ("base", xpos="far_left", ypos="head")
            sna "I know my students' names, Genie." ("snape_04")

        "\"I can't remember. I got too distracted by her legs...\"":
            sna "Can you describe her?" ("snape_05")
            sna "Hair colour, height, her uniform colour? Anything?" ("snape_02")
            gen "I believe she was Asian." ("base", xpos="far_left", ypos="head")
            sna "Cho Chang?" ("snape_10")
            gen "Bless you." ("base", xpos="far_left", ypos="head")
            sna "No. That's her name." ("snape_08")
            sna "We only have one Asian girl at our school." ("snape_24")
            sna "You'd think as the only wizarding school in all of Britain, it would be more diverse..." ("snape_09")

    sna "And what did she want from you exactly?" ("snape_05")
    gen "She asked me a couple of things about Quidditch." ("base", xpos="far_left", ypos="head")
    sna "Of course." ("snape_09")
    sna "Her entire world revolves around that stupid broomstick rally." ("snape_08")
    gen "I take it that you aren't a fan?" ("base", xpos="far_left", ypos="head")

    gen "She could be a great candidate for our little training scheme." ("base", xpos="far_left", ypos="head")
    sna "What? Do you want to turn her into a slut too?" ("snape_01")
    gen "Not only that. I believe she could be of help to deal with the Granger girl as well." ("base", xpos="far_left", ypos="head")
    sna "Interesting. It seems like you have already made plans for her." ("snape_02")
    gen "I thought of a couple of things." ("base", xpos="far_left", ypos="head")
    sna "You have my attention!" ("snape_13")

    $ d_flag_01 = False
    $ d_flag_02 = False

    label discuss_cho_plan:
        if d_flag_01 and d_flag_02:
            jump discussed_cho_plan

    menu:
        "\"Help her win the Quidditch cup.\"" if not d_flag_01:
            $ d_flag_01 = True

            sna "And help her win against Slytherin?" ("snape_16")
            sna "I can't agree to that, Genie. As much as I'd like to see the Potter boy demoralised by losing to a girl..." ("snape_10")
            sna "Or Malfoy for that matter... He's been way too cocky lately." ("snape_08")
            gen "Who?" ("base", xpos="far_left", ypos="head")
            sna "A student of mine... Rich parents, bought his way into our Quidditch team... Spoiled beyond belief." ("snape_29")
            gen "Didn't you say you don't care much about Quidditch?" ("base", xpos="far_left", ypos="head")
            sna "Of course I don't... But a win is a win." ("snape_09")
            sna "Besides, Ravenclaw doesn't have a chance against Slytherin." ("snape_03")
            sna "They are notoriously bad at Quidditch. And they have been for years." ("snape_02")
            gen "You sound very confident." ("base", xpos="far_left", ypos="head")
            gen "Want to bet on it?" ("grin", xpos="far_left", ypos="head")
            sna "A bet? How very enticing!" ("snape_20")
            sna "How much are you willing to bet?" ("snape_18")
            gen "Twenty bucks?" ("base", xpos="far_left", ypos="head")
            sna "Don't you mean gold?" ("snape_05")
            gen "Twenty... gold then..." ("base", xpos="far_left", ypos="head")
            sna "That's barely worth it." ("snape_04")
            sna "How about two thousand gold?" ("snape_13")

            if game.gold < 2000:
                gen "I don't have that much gold." ("base", xpos="far_left", ypos="head")
                sna "Well, you have plenty of time to gather that amount." ("snape_22")
            else:
                gen "Are you feeling \"that\" confident?" ("base", xpos="far_left", ypos="head")
                sna "About Slytherin winning the cup?" ("snape_20")
                sna "Absolutely!" ("snape_22")

            sna "So, what do you say? Want to take the bet?" ("snape_13")
            gen "Under one condition." ("base", xpos="far_left", ypos="head")
            gen "You won't cheat, and you won't give Slytherin any unfair advantages." ("base", xpos="far_left", ypos="head")
            sna "I'd never think of it." ("snape_09")
            gen "So, you want to take on the bet?" ("base", xpos="far_left", ypos="head")
            sna "Of course, I have no doubt Slytherin will win the cup." ("snape_02")
            sna "At least Quidditch will be worth watching now. I can't say no to some good old gambling." ("snape_20")
            sna "But how will you help Miss Chang in Quidditch? You know nothing about it!" ("snape_05")

            menu:
                "\"I'll just read a book about it.\"":
                    sna "You are really planning to take this bet seriously, aren't you?" ("snape_04")
                    gen "You have no idea! I'll do anything to get into that girl's panties." ("base", xpos="far_left", ypos="head")
                    sna "Blinded by the sweet love for a girl..." ("snape_13")
                    sna "You have already lost, my friend!" ("snape_21")
                    gen "We'll see about that." ("base", xpos="far_left", ypos="head")
                    gen "(Now, where could I get a book about Quidditch from...)" ("base", xpos="far_left", ypos="head")

                "\"I trust my instincts!\"":
                    sna "Your instincts?" ("snape_14")
                    gen "Never underestimate the capabilities of a Genie..." ("base", xpos="far_left", ypos="head")
                    sna "(...)" ("snape_12")

            if not d_flag_02:
                sna "So, that's it then? You're staking both your money and the chance at getting inside this girl's panties on Ravenclaw winning the cup?" ("snape_01")
                gen "You bet I--{w=0.2} No wait! Of course, that's not all of it!" ("angry", xpos="far_left", ypos="head")
                gen "*Err*..." ("base", xpos="far_left", ypos="head")
                gen "Oh! I'm also planning to..." ("base", xpos="far_left", ypos="head")

            jump discuss_cho_plan

        "\"Have her and Hermione go at each other.\"" if not d_flag_02:
            $ d_flag_02 = True

            sna "Granger? Why her?" ("snape_05")
            gen "They absolutely despise each other." ("base", xpos="far_left", ypos="head")
            sna "They do?" ("snape_20")
            gen "Yes. They had a little confrontation here in my room..." ("base", xpos="far_left", ypos="head")
            sna "A confrontation? So so..." ("snape_13")
            sna "What was it about?" ("snape_20")

            if states.her.ev.intro.masturbated and states.cho.ev.intro.masturbated:
                gen "I have no idea. I jerked off during their whole exchange." ("base", xpos="far_left", ypos="head")
                sna "You did that again? And neither of them realised?" ("snape_22")
                gen "Didn't seem like it. They were too occupied with insulting each other..." ("base", xpos="far_left", ypos="head")

            elif states.cho.ev.intro.masturbated:
                gen "I have no idea. I jerked off during their whole exchange." ("base", xpos="far_left", ypos="head")
                sna "You did what?" ("snape_15")
                gen "I jerked off.{w} Beat my meat.{w} Wrestled the snake.{w} Whatever you want to call it." ("base", xpos="far_left", ypos="head")
                gen "Don't tell me you never do it..." ("base", xpos="far_left", ypos="head")
                sna "Not in front of my students!" ("snape_07")
                sna "How did neither of them realise what you were doing?" ("snape_10")
                gen "They were too occupied with insulting each other..." ("base", xpos="far_left", ypos="head")
                sna "I can imagine that..." ("snape_20")

            else:
                gen "Some nonsense about wasting my time." ("base", xpos="far_left", ypos="head")
                sna "Which they probably did?" ("snape_05")
                gen "Yeah. But I slept through most of it..." ("base", xpos="far_left", ypos="head")
                sna "I wish I could do the same." ("snape_09")
                sna "Zone out and dream of stuffing that witch's relentless mouth!" ("snape_06")
                gen "I feel you..." ("base", xpos="far_left", ypos="head")

            sna "*Hmm*... That reminds me of something I witnessed at the end of last year..." ("snape_23")
            sna "Granger was scolding the poor girl for kissing a boy in the hallways." ("snape_20")
            gen "Hot...{w} What happened then?" ("base", xpos="far_left", ypos="head")
            sna "They were screaming and grabbing at each other's hair before I had the chance to interfere." ("snape_18")
            sna "I ended up taking fifty points from Gryffindor. I should have taken at least one hundred now that I think about it..." ("snape_22")
            gen "Does she often do things like that?" ("base", xpos="far_left", ypos="head")
            sna "Are you kidding? All the bloody time!" ("snape_17")
            sna "Granger is a nuisance to everyone. Didn't I already tell you that?" ("snape_16")
            gen "No. I meant the Cho girl..." ("base", xpos="far_left", ypos="head")
            gen "Does she make out with boys often?" ("grin", xpos="far_left", ypos="head")
            sna "How should I know. I'm not her stalker." ("snape_12")
            gen "Well, if what you've said is true... Training her should be a piece of cake." ("base", xpos="far_left", ypos="head")
            gen "And what a delicious piece of cake it will be!" ("grin", xpos="far_left", ypos="head")

            if not d_flag_01:
                sna "So, how are you planning on achieving all this exactly?" ("snape_01")
                sna "Surely you can't rely on Miss perfect to get anywhere with this girl..." ("snape_04")
                gen "No, but I'm sure she'll play her part in the next step of my plan with Miss Chang..." ("base", xpos="far_left", ypos="head")
                sna "Which is?" ("snape_05")

            jump discuss_cho_plan


    # Ending #TODO might need some reminder for the player to talk to Hermione here. How would I add that?
    label discussed_cho_plan:

    show screen with_snape(ani=True)
    call notes
    nar "You spend the rest of the evening in Snape's company, talking about Cho's impressive thighs."


    $ states.sna.ev.hangouts.cho_e1 = True

    jump end_snape_hangout_points


### Hermione Talk 1 ###
# You talk to Hermione to drop her Quidditch movement. You then summon Cho.
# Cho is now unlocked and you can summon her.

label cho_intro_E3:

    her "" (xpos="mid", ypos="base", trans=fade)

    #So Hermione doesn't walk over her during exit
    $ cho_chibi.zorder = 4

    # Intro
    if not states.cho.ev.intro.e3_complete:
        $ states.cho.ev.intro.e3_complete = True

        gen "I got some word about you that needs to be addressed..." ("base", xpos="far_left", ypos="head")
        her "About what? I'm not in any trouble or anything, am I?" ("soft", "wide", "base", "mid")
        gen "Miss Chang..." ("base", xpos="far_left", ypos="head")
        her "Oh..." ("annoyed", "narrow", "base", "up")
        her "What about her?" ("annoyed", "base", "angry", "mid")
        gen "Well, it has come to my attention that you've been spreading false rumours about her." ("base", xpos="far_left", ypos="head")
        her "And? It's well deserved in my opinion..." ("soft", "narrow", "annoyed", "mid")
        gen "Don't you feel like it's unbefitting of you to publicly talk badly about another student?" ("base", xpos="far_left", ypos="head")
        her "..." ("annoyed", "narrow", "base", "down")
        gen "Surely that isn't something to expect from Gryffindor's finest..." ("grin", xpos="far_left", ypos="head")
        her "Did Cho put you up to this?" ("normal", "squint", "base", "mid")
        gen "..." ("angry", xpos="far_left", ypos="head")
        gen "(She's onto me!)" ("base", xpos="far_left", ypos="head")
        gen "Of course not... it was another teacher, actually." ("base", xpos="far_left", ypos="head")
        her "Who was it?" ("open", "base", "angry", "mid")
        gen "Not important..." ("base", xpos="far_left", ypos="head")
        her "It was Snape wasn't it?" ("annoyed", "narrow", "base", "mid_soft")
        gen "(She's good!)" ("angry", xpos="far_left", ypos="head")
        gen "Well, I'd like you to stop and that's all that matters..." ("base", xpos="far_left", ypos="head")
        gen "And that includes the..." ("base", xpos="far_left", ypos="head")
        gen "Quidditch...{w} whatever it was...{w} movement." ("base", xpos="far_left", ypos="head")

    # Repeat (This won't happen anymore)
    else:
        gen "[name_hermione_genie], there is something we need to talk about." ("base", xpos="far_left", ypos="head")
        her "Is it about Cho again?" ("annoyed", "squint", "base", "mid")
        gen "Yes indeed." ("base", xpos="far_left", ypos="head")
        gen "I'd like you to stop your..." ("base", xpos="far_left", ypos="head")
        gen "Quidditch...{w} something, something...{w} movement." ("base", xpos="far_left", ypos="head")

    if states.her.level < 10: # T3
        her "My \"Quidditch equality movement\"?" ("soft", "base", "base", "mid")
        her "But Sir, I'm on the verge of a breakthrough with it!" ("soft", "closed", "base", "mid")
        her "I worked very hard on gathering all records of past Quidditch matches, throughout the complete history of Quidditch!" ("open", "wink", "base", "mid")
        her "You'd be surprised just how few female--" ("soft", "closed", "base", "mid")
        gen "I'll give you ten house points." ("base", xpos="far_left", ypos="head")
        her "Ten points?" ("soft", "wide", "base", "stare", trans=hpunch)
        her "Sir, do you even realise how much time it took me to do all that research?" ("angry", "squint", "angry", "mid")
        gen "Twenty?" ("base", xpos="far_left", ypos="head")
        her "One hundred!" ("angry", "closed", "angry", "mid")
        gen "One hundred? Are you nuts?" ("angry", xpos="far_left", ypos="head")
        her "And just points isn't going to cut it..." ("open", "closed", "base", "mid")
        gen "Then what else?" ("base", xpos="far_left", ypos="head")
        her "*Uhm*..." ("annoyed", "base", "base", "R")
        gen "You're testing my patience, Miss Granger..." ("base", xpos="far_left", ypos="head")
        her "Oh, I know!{w=0.5} I want a seat in the teacher stands during the Quidditch matches!" ("smile", "happyCl", "base", "mid")
        her "Cho would be so jealous if she saw me sitting near the commentator and teachers..." ("grin", "narrow", "base", "mid_soft")
        gen "So, you want both one hundred points and a seat in the teacher stands..." ("base", xpos="far_left", ypos="head")
        her "Yes..." ("base", "happy", "base", "mid_soft")

        menu:
            gen "(...)" ("base", xpos="far_left", ypos="head")
            "\"Very well...\"":
                gen "Anything else?" ("base", xpos="far_left", ypos="head")
                her "Well..." ("soft", "happy", "base", "R")
                gen "Don't push your luck..." ("base", xpos="far_left", ypos="head")
                her "No, I think that should do..." ("smile", "happyCl", "base", "mid")
                if states.sna.level <= 30:
                    gen "(I'm going to need to get real friendly with Snape to get those Slytherins in a steady lead...)" ("base", xpos="far_left", ypos="head")
                gen "One hundred points to Gryffindor...{w=0.6} Happy?" ("base", xpos="far_left", ypos="head")
                $ gryffindor += 100

                her "If I'm truly honest with you Sir,{w=0.6} My plans weren't that popular with the Quidditch teams in any case." ("soft", "narrow", "base", "mid_soft")
                gen "I can't imagine why..." ("base", xpos="far_left", ypos="head")
                pass

            "\"Fifty points!\"":
                her "What?... Only Fifty?!" ("shock", "wide", "base", "stare", trans=hpunch)
                gen "Yes, only fifty! Because you are being unreasonable." ("base", xpos="far_left", ypos="head")
                her "But you made it sound like it was something important to you!" ("disgust", "narrow", "worried", "mid_soft")
                gen "And you believe that I'd just throw a hundred points at you because of that?" ("base", xpos="far_left", ypos="head")
                her "{size=-4}It was worth a try...{/size}" ("annoyed", "narrow", "worried", "down")
                gen "Try to remember this, Miss Granger. You can't rip me off that easily." ("base", xpos="far_left", ypos="head")
                her "*Tzzzz*- Fine.. Fifty points then, but I'm not happy about it..." ("angry", "base", "angry", "mid")
                gen "Fine by me..." ("base", xpos="far_left", ypos="head")
                gen "Fifty points to Gryffindor." ("base", xpos="far_left", ypos="head")
                $ gryffindor += 50
                $ states.her.mood += 6
                her "Thanks I guess..." ("open", "closed", "angry", "mid")
                gen "You may leave now..." ("base", xpos="far_left", ypos="head")
                her "*Hmph*... I don't think so, sir..." ("annoyed", "closed", "angry", "mid")
                gen "What now? You've received your points already." ("base", xpos="far_left", ypos="head")
                her "Well, It's just..." ("open", "narrow", "base", "R")


    elif states.her.level < 21:
        her "Oh... My \"Quidditch equality movement\"?" ("soft", "base", "base", "mid")
        gen "That's the one." ("base", xpos="far_left", ypos="head")
        her "It never really got off the ground..." ("open", "base", "base", "R")
        her "No pun intended..." ("base", "closed", "base", "mid")
        gen "(...)" ("base", xpos="far_left", ypos="head")
        her "To be honest, I don't have that much time apart from my visits here and studying..." ("open", "narrow", "worried", "down")
        her "I might consider dropping it." ("base", "base", "base", "R")
        her "Even though it would take away the immense pleasure of seeing Cho getting all worked up about it..." ("grin", "base", "base", "mid")
        gen "(...)" ("base", xpos="far_left", ypos="head")
        her "There is something I'd like from you in return, [name_genie_hermione].{w=0.8} Or else I'll just continue with it!" ("base", "narrow", "base", "mid_soft")
        gen "Go on girl." ("base", xpos="far_left", ypos="head")
        gen "Tell me what you want." ("base", xpos="far_left", ypos="head")
        gen "What you really{w}, really want..." ("base", xpos="far_left", ypos="head")
        her "Very well, [name_genie_hermione]." ("soft", "base", "base", "R")
        her "I'll tell you what I want!" ("open", "closed", "base", "mid")
        her "What I really, really want!" ("grin", "narrow", "base", "mid_soft")
        gen "{size=-4}Nice!{/size}" ("grin", xpos="far_left", ypos="head")
        her "I'd like a seat in the teacher stands, during the Quidditch matches..." ("open", "closed", "base", "mid")
        gen "Is that all?" ("base", xpos="far_left", ypos="head")
        her "Oh, and a hundred points for Gryffindor..." ("grin", "base", "base", "R")
        gen "(...)" ("base", xpos="far_left", ypos="head")
        gen "I'd say fifty would be more appropriate in this instance..." ("base", xpos="far_left", ypos="head")
        her "Sir, it took a lot of effort to gather all those records of past Quidditch matches, throughout the whole history of Quidditch." ("open", "closed", "base", "mid")
        gen "Fifty points..." ("base", xpos="far_left", ypos="head")
        her "(...)" ("annoyed", "narrow", "angry", "R")
        her "Very well then." ("soft", "closed", "base", "mid")
        gen "Fifty points, to the Gryffindor house..." ("base", xpos="far_left", ypos="head")
        $ gryffindor += 50
        her "Thank you, [name_genie_hermione]." ("base", "base", "base", "mid")

    else:
        her "My what?" ("open", "narrow", "base", "mid_soft")
        gen "Your Quidditch movement." ("base", xpos="far_left", ypos="head")
        gen "Regarding the male and female roles in Quidditch..." ("base", xpos="far_left", ypos="head")
        her "Oh. I barely even remember doing that." ("annoyed", "narrow", "base", "R_soft")
        gen "So it wouldn't be an issue for you to drop it?" ("base", xpos="far_left", ypos="head")
        her "I guess so..." ("soft", "narrow", "worried", "down")
        her "Although, if I were to drop it..." ("open", "narrow", "base", "down")
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her "I want a seat in the teacher stands during the Quidditch matches!" ("grin", "narrow", "base", "mid_soft")
        gen "I'm sure that could be arranged..." ("base", xpos="far_left", ypos="head")
        her "Thank you, [name_genie_hermione]." ("base", "narrow", "base", "mid_soft")

    her "[name_genie_hermione], may I ask...{w=0.6} What exactly were you and Cho talking about when I entered your office?" ("open", "base", "base", "R")
    gen "Oh. She just wanted my help with Quidditch." ("base", xpos="far_left", ypos="head")
    her "*Pffff*-{w=0.4} Why doesn't it surprise me that she'd need your help with it." ("grin", "narrow", "base", "R_soft")
    her "How else could she possibly win that stupid Quidditch cup..." ("soft", "closed", "angry", "mid")
    gen "I thought that cup was important to you?" ("base", xpos="far_left", ypos="head")
    her "I couldn't care less about it, [name_genie_hermione]." ("open", "closed", "base", "mid")
    her "The only cup that is worth winning is the {i}house cup{/i}." ("open", "narrow", "base", "R_soft")
    her "They're completely different..." ("annoyed", "base", "angry", "mid")
    gen "Totally different..." ("base", xpos="far_left", ypos="head")

    if states.her.level < 18:
        her "It's the most prestigious award one could earn for your house!{w=0.6} The Quidditch cup is nothing in comparison..." ("open", "closed", "base", "mid")
        her "Surely there are better ways to spend your time than participating in this silly sports game." ("annoyed", "narrow", "annoyed", "mid")
        gen "(My irony senses are tingling...)" ("base", xpos="far_left", ypos="head")

    if states.her.level < 8:
        her "They're given the privilege of attending one of the most prestigious wizarding schools in the world..." ("open", "narrow", "angry", "R")
        her "And what do they do? They spend their time playing some silly sports game that will get them nowhere." ("open", "base", "angry", "mid")
        gen "Yes. Because why enjoy yourself when you could study instead..." ("base", xpos="far_left", ypos="head")
        her "Exactly!" ("normal", "closed", "base", "mid")
        gen "(She's so predictable.)" ("base", xpos="far_left", ypos="head")

    gen "Well... The Quidditch teams are none of your concern anymore..." ("base", xpos="far_left", ypos="head")
    gen "You'll tell Cho that you are sorry about your previous interferences." ("base", xpos="far_left", ypos="head")
    her "(...)" ("annoyed", "base", "angry", "mid")
    gen "And that the \"Quidditch equality movement\" will be...{w} \n\"no more\"." ("base", xpos="far_left", ypos="head")

    if states.her.level < 18:
        her "Do I really have to do all that?" ("upset", "base", "base", "R")
        gen "If you want to keep on buying favours from me." ("base", xpos="far_left", ypos="head")
        her "*Ugh*...{w=0.4} Very well, I guess..." ("soft", "narrow", "worried", "down")
    else:
        her "Sure, whatever..." ("open", "narrow", "base", "R_soft")


    # Summon Cho
    gen "Great!" ("grin", xpos="far_left", ypos="head")
    gen "Let's call her up here then..." ("grin", xpos="far_left", ypos="head")
    her "What? Now?" ("clench", "wide", "base", "stare")

    # Hermione quickly gets dressed.
    if not hermione.is_worn("top") or not hermione.is_worn("bottom"):
        her "Wait, she can't see me like this!" ("disgust", "narrow", "worried", "down")

        hide hermione_main
        with d3
        pause .8

        gen "(...)" ("base", xpos="far_left", ypos="head")

        $ hermione.wear("all")
        pause .5

    else:
        hide hermione_main
        hide screen bld1
        with d3
        pause .5

    stop music fadeout 1.0
    # Cho enters the office.
    call cho_walk(580, 450, action="enter")

    pause 1
    play music "music/deadly-roulette-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    cho "Hello, Sir.{w=0.6} You've called for me?" ("soft", "narrow", "raised", "L", xpos="base", ypos="base")
    her "" ("normal", "closed", "base", "mid", xpos=450, ypos="base")
    cho "Granger..." ("soft", "narrow", "angry", "L")
    her "Chang..." ("annoyed", "narrow", "angry", "R")
    gen "Go on, girl. Tell her." ("base", xpos="far_left", ypos="head")
    cho "Tell me what?" ("normal", "narrow", "angry", "L")
    her "..." ("annoyed", "narrow", "base", "up")
    her "About my \"Quidditch equality movement\"..." ("normal", "closed", "base", "mid")
    cho "Did our Professor finally convince you what a terrible idea it would be?" ("soft", "narrow", "angry", "mid")
    gen "Actually, I still think granting more people the ability to--" ("base", xpos="far_left", ypos="head")
    cho "*Shhsh!* Professor!{w=0.6} I'd like to hear it from her." ("annoyed", "narrow", "angry", "mid")
    cho "I'm going to enjoy this!" ("horny", "narrow", "base", "L")
    her "..." ("annoyed", "base", "angry", "mid")
    her "*Sigh*...{w=0.6} I will end my movement, and I won't interfere with Quidditch again..." ("open", "closed", "base", "mid") #[Looking bored]
    cho "This is amazing! I feel as if it's my birthday!" ("smile", "base", "base", "mid")
    her "After all, Quidditch is a huge waste of everyone's time.{w=0.6} Including mine..." ("soft", "narrow", "base", "R_soft") #[Still looking bored]
    cho "You're just jealous that I'm better than you at something." ("smile", "narrow", "angry", "L")
    her "I am not jealous!" ("angry", "closed", "angry", "mid")
    gen "You may go now, Miss Granger." ("base", xpos="far_left", ypos="head")
    her "(...)" ("annoyed", "base", "angry", "mid")
    her "Until next time, Sir." ("normal", "closed", "base", "mid")
    her "..." ("annoyed", "narrow", "base", "R_soft")

    # Hermione leaves after glaring one last time at Cho.
    call her_walk("door", "base")
    pause .2
    call her_chibi("stand", "door", "base",flip=False)
    with d3
    pause .2

    her "*glare*" ("normal", "base", "angry", "mid", ypos="head", flip=False)
    # Add Cho glaring back with her 'head' image.

    call her_chibi("stand", "door", "base",flip=True)
    with d3
    pause .8

    call her_chibi("leave")
    with d3
    pause .5

    stop music fadeout 1.0

    cho "Thank you for getting her off my back, Professor." ("soft", "narrow", "base", "mid")
    gen "No problem." ("base", xpos="far_left", ypos="head")
    cho "Hopefully this means we'll have a chance at winning the cup this time around..." ("base", "base", "base", "R")
    cho "However small that chance may be." ("normal", "narrow", "base", "downR")
    gen "(Time to get in there, Genie...)" ("base", xpos="far_left", ypos="head")
    gen "Sounds to me like you could use a coach." ("base", xpos="far_left", ypos="head")
    cho "Tell me about it...{w=0.4} Our current captain is hopeless..." ("disgust", "narrow", "base", "down")
    cho "During our last meeting he brought up wanting to add stripes to our Quidditch Robes." ("soft", "narrow", "base", "mid")
    cho "Believing that doing so would somehow make us go faster..." ("disgust", "narrow", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "Sorry, sir... I've already taken up enough of your time... Surely, you've got more important things--" ("open", "narrow", "base", "R")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

    gen "Why don't I coach you?" ("base", xpos="far_left", ypos="head")
    cho "Sorry?" ("clench", "narrow", "base", "mid")
    gen "I could coach you." ("base", xpos="far_left", ypos="head")
    cho "You want to coach me, sir?" ("open", "wide", "base", "mid")
    cho "I'm sorry, but I'm a bit confused... Why would the Headmaster want to coach a Quidditch team?" ("clench", "narrow", "raised", "mid")
    gen "Why there's a simple answer to that Miss Chang..." ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "Yes?" ("disgust", "narrow", "raised", "mid")
    gen "Isn't the point of a Headmaster to make sure that their students' talents aren't wasted?" ("base", xpos="far_left", ypos="head")
    cho "I suppose so, but--" ("open", "base", "base", "downR")
    gen "Well, as soon as you first stepped through that door I could tell that this girl has got what it takes to make it big." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "...{w} You could tell that just by looking at me?" ("angry", "narrow", "base", "mid")
    gen "Indeed... No doubts about it!" ("base", xpos="far_left", ypos="head")
    gen "Or are you telling me that I'm wrong?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course not, but--" ("soft", "base", "base", "R")
    gen "Great!" ("grin", xpos="far_left", ypos="head")
    gen "Then I shall summon you shortly, so we can further discuss this arrangement." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "(Arrangement?)" ("soft", "narrow", "base", "down")
    gen "That will be all for now Miss Chang, you may leave." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "...{w} Alright then, sir." ("normal", "base", "base", "mid")
    cho @ cheeks blush "(He could tell just by looking at me?)" ("normal", "narrow", "base", "down")
    cho @ cheeks blush "(...)" ("soft", "narrow", "base", "R")

    # Cho leaves.
    call cho_walk(action="leave")

    # You can now summon Cho Chang to your office.
    stop music fadeout 1.0

    # End of Intro.
    $ states.her.busy = True
    $ states.cho.busy = True

    #Reset z-order
    $ cho_chibi.zorder = 3

    $ states.cho.ev.intro.e4_complete = True

    call music_block
    jump main_room_menu
