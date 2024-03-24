

### Snape Intro ###

# First time genie meets snape

label snape_intro_E1:
    $ game.weather = "clear"
    call weather_sound

    pause 1

    gen "*Yawn*......." ("base", xpos="far_left", ypos="head")
    gen "These old bones seem to be getting tired." ("base", xpos="far_left", ypos="head")
    gen "Perhaps I should rest my eyes a bit." ("base", xpos="far_left", ypos="head")

    with fade

    pause 1
    play sound "sounds/snore2.ogg"
    gen "......{w=0.5}*Snore*{w=1.0}{nw}"

    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"

    anon "Albus? Are you in there?"

    play sound "sounds/snore1.ogg"
    gen "*Snore*{w=2.0}{nw}"
    anon "Don't ignore me, I know you're in there."

    "............."
    anon "I'm coming in either way!"

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    play sound "sounds/door.ogg"

    call sna_chibi("stand","door","base", flip=False)
    with d3
    pause.3

    call chibi_emote("thought", "snape")
    pause 1
    call chibi_emote("hide", "snape")

    call sna_walk("mid", "base")
    pause.2

    sna "" ("snape_01", xpos="base", ypos="base", trans=d3)
    call ctc

    sna "" ("snape_31")
    play sound "sounds/MaleClearThroat.ogg"
    anon "Albus... Do you have a moment?"

    sna "" ("snape_01")
    play sound "sounds/MaleGasp.ogg"
    gen "!!!" ("angry", xpos="far_left", ypos="head")
    gen "{size=-3}(An Indigenous life form!?){/size}" ("angry", xpos="far_left", ypos="head")
    gen "{size=-3}(looks human enough...){/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=-3}(Maybe if I just act cool he'll leave...?){/size}" ("base", xpos="far_left", ypos="head")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Actually, I'm a bit busy.\"":
            sna "" ("snape_04", trans=d3)
            anon "Well, aren't you always, Albus?"
        "\"Of course. What is it?\"":
            sna "" ("snape_06", trans=d3)
        "\"And Albus to you too.\"":
            sna "" ("snape_05", trans=d3)
            anon "What?"
            sna "" ("snape_04")
            anon "Albus, I'm not in the mood for your... shenanigans."
        "\"Take me to your leader.\"":
            sna "" ("snape_01", trans=d3)
            anon "What?"
            anon "*Hmm*...?"
            anon "You mean the Minister of Magic?"
            sna "" ("snape_03")
            anon "I would rather avoid having to deal with that bureaucrat..."
            gen "Fine, never mind... How can I be of help?" ("base", xpos="far_left", ypos="head")

    sna "" ("snape_06")
    anon "I have something important I need to discuss with you..."
    anon "I think we need to revise our admittance policy."
    gen "................?" ("base", xpos="far_left", ypos="head")
    sna "" ("snape_03")
    anon "Half of my... so-called \"pupils\" are nothing but annoying maggots that make my life miserable on a daily basis."
    gen "................" ("base", xpos="far_left", ypos="head")
    sna "" ("snape_06")
    anon "Most of them belong to your precious Gryffindor house, of course..."
    gen "......?" ("base", xpos="far_left", ypos="head")
    sna "" ("snape_03")
    anon "The wretched Weasley family, that noisy Granger girl and of course the hero of all the juvenile delinquents around the globe..."
    sna "" ("snape_08")
    anon "{size=+3}The Potter boy!{/size}"
    sna "" ("snape_01")
    anon "Mark my words, Albus. The Gryffindor house will become this school's undoing!"
    gen "...................." ("base", xpos="far_left", ypos="head")
    sna "" ("snape_01")
    anon "Nothing but annoying maggots, the lot of them!"
    sna "" ("snape_06")
    anon "And if that wasn't enough, now they spread all sorts of nasty rumours about the teachers!"
    anon "Particularly about yours truly..."
    gen "......................" ("base", xpos="far_left", ypos="head")
    sna "" ("snape_05")
    anon "You don't believe those rumours, do you Albus?"

    menu:
        gen ".............." ("base", xpos="far_left", ypos="head")
        "\"Well, of course not!\"":
            sna "" ("snape_09")
            anon "Good..."
            anon "You know me better than that. I wouldn't care for such things..."
        "\"Where there's smoke, there's fire.\"":
            sna "" ("snape_10")
            anon "Albus?! You can't be serious!"
            anon "Those are nothing but filthy lies, I'm telling you!"
        "\"I don't listen to rumours.\"":
            sna "" ("snape_03")
            anon "Don't play dumb with me Albus."
            sna "" ("snape_04")
            anon "I know exactly what those \"little birds\" of yours have been doing."

    gen "........................." ("base", xpos="far_left", ypos="head")
    sna "" ("snape_06")
    anon "Well, those wretched brats left me completely exhausted. I think I will retire for today."
    sna "" ("snape_09")

    menu:
        "\"Is that all?\"":
            sna "" ("snape_04")
            anon "It is."
        "-Stay silent-":
            sna "" ("snape_05")
            anon "................"
    anon "I'll leave you to it then."

    stop music fadeout 5.0
    call sna_walk("door", "base")

    sna "" ("snape_03", flip=True, trans=d3)
    anon "Please reconsider what we discussed earlier."

    call sna_walk(action="leave")

    call bld
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "So that tall, broody dude mistook me for someone else...?" ("base", xpos="far_left", ypos="head")
    gen "Which means I must be shrouded in a concealment spell..." ("base", xpos="far_left", ypos="head")
    gen "........." ("base", xpos="far_left", ypos="head")
    gen "So basically, I'm a genie disguised as a human, who is in turn disguised as another human..." ("base", xpos="far_left", ypos="head")
    gen "No, that's not stupid at all..." ("base", xpos="far_left", ypos="head")
    call bld("hide")

    $ states.sna.ev.intro.e1_complete = True
    $ ss_event_pause += 1

    jump day_start


# Event 2

# Snape talks to Genie about Hermione, Snape becomes suspicious

label snape_intro_E2:
    play music "music/Music for Manatees.ogg" fadein 1 if_changed

    play sound "sounds/knocking.ogg"
    "*knock-knock-knock*"
    anon "It's me."
    gen "{size=-3}(That broody guy again...){/size}" ("base", xpos="far_left", ypos="head")
    gen "(Maybe if I stay silent he'll go away...)" ("base", xpos="far_left", ypos="head")

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    call sna_walk(action="enter", xpos="mid", ypos="base")

    call bld

    sna "" ("snape_01",xpos="base",ypos="base")
    anon "Albus!"
    gen "Hey..........{w=0.3} you..." ("base", xpos="far_left", ypos="head")
    anon "You need to do something about that Granger girl..."
    sna "" ("snape_06")
    anon "Honestly... I'm running out of ways to punish that... that..."
    sna "" ("snape_04")
    anon "That little witch!"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Granger? Hermione Granger, right?\"":
            anon "Yes, her..."
            anon "She also happens to be a part of the \"Potter gang\"."
        "\"I got your back, Jack, witches be crazy!\"":
            anon "What...? Albus, you're behaving oddly lately."
            anon "Is everything alright?"
            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"Yes, I'm fine. Go on.\"":
                    anon "If you say so..."
                "\"You know me. I love my shenanigans.\"":
                    anon "*Hmm*....."

        "\".....................................................\"":
            pass

    anon "Remember how back in the days they used to publicly flog the students?"
    anon "I swear if we could bring that back all of our problems would be solved..."
    anon "Yes... I would gladly tie that girl to a flogging pole in front of the entire school..."
    sna "" ("snape_20")
    anon "Then lift her skirt up, and..."
    sna "" ("snape_12")
    anon "*Ahem*! Sadly, nowadays, us teachers are severely limited in the disciplinary measures we have at our disposal..."
    anon "I know you are just as powerless as I am in this matter, but I'm telling you, that girl had better stop testing my patience."

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"I'll take care of that brat!\"":
            sna "" ("snape_05")
            anon "...?!"
            anon "Albus..."
            anon "What are--"
        "\"Nobody ever said this job would be easy.\"":
            sna "" ("snape_06")
            anon "Sometimes I feel like I would rather deal with a classroom full of Dementors..."
        "\"You will feel better tomorrow.\"":
            sna "" ("snape_06")
            anon "You are probably right..."

    anon "*Hmm*..."
    sna "" ("snape_06")
    anon "Perhaps I'd better go get some sleep."
    anon "I need to be in my top shape every morning..."
    anon "You can't show weakness to those brats, or they will swallow you whole..."
    sna "" ("snape_24")
    anon "Good night, Albus."

    call sna_walk("door", "base")
    pause.2

    anon "................."

    call sna_chibi("stand","door","base",flip=False)
    with d3
    pause.2

    anon "One more thing..."
    show screen bld1
    sna "" ("snape_24", trans=d3)
    anon "You should ignore any lies you hear about me and those slytherin girls..."
    hide snape_main
    with d3
    gen "Got it." ("base", xpos="far_left", ypos="head")

    hide screen bld1
    call sna_chibi("stand","door","base",flip=True)
    with d3
    pause.2

    call sna_chibi("leave")

    $ states.sna.ev.intro.e2_complete = True
    $ ss_event_pause += 1

    jump day_start


# Event 3

# Snape comes in, has a talk with Genie, then the duel starts.

label snape_intro_E3:
    play music "music/Dark Fog.ogg" fadein 1 if_changed

    call sna_walk(action="enter", xpos="mid", ypos="base")

    sna "" ("snape_01",xpos="base",ypos="base")
    call ctc

    anon "Good evening, Albus."
    anon "I want to talk to you about those damn brats again..."
    anon "But first I want to ask you something..."
    sna "" ("snape_05")
    anon "Have you noticed anything strange going on around here lately?"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-2}\"Like you being especially whiny?\"{/size}":
            anon "What? B-but..."
            sna "" ("snape_06")
            anon "Well, perhaps you are right..."
        "{size=-2}\"An owl is fetching my mail, man!\"{/size}":
            anon "What about it?"
            gen "What do you mean, what about it?" ("base", xpos="far_left", ypos="head")
            gen "An owl...{w=0.4} Is fetching...{w=0.4} My mail..." ("base", xpos="far_left", ypos="head")
            sna "" ("snape_03")
            anon "......"
            sna "" ("snape_04")
            anon "Never mind the owl..."
        "{size=-2}\"No, not really. It's just business as usual.\"{/size}":
            anon "*Hmm*... Maybe I'm just being paranoid..."

    sna "" ("snape_24")
    anon "The reason why I'm here today is the \"Potter Gang\"."
    sna "" ("snape_01")
    anon "There are only so many points I can subtract from the Gryffindor house, you know..."
    anon "And the Granger girl became the worst of them lately..."
    sna "" ("snape_06")
    anon "She practically leads the onslaught."
    sna "" ("snape_05")
    anon "Speaking of which, has she been sending you any letters lately?"

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Hermione Granger? No, Nothing from her.\"":
            anon "I see... So, she's been bluffing then."
            sna "" ("snape_16")
            anon "What an annoying witch."
        "\"Yes...\"":
            anon "Really now?"
            anon "Did she lie about me in particular in that letter?"
            anon "I hope you know better than to listen to the likes of her..."

    sna "" ("snape_03")
    anon "She would never admit it, but I know she's been spreading those nasty rumours about me around the school..."
    sna "" ("snape_29")
    anon "*Tsk*... Noisy little...... witch."
    sna "" ("snape_09")
    anon "I would never stoop so low as to trade house points in exchange for sexual favours..."
    anon "I mean, sure, we use house points to motivate students, but that's completely different..."
    anon "I can't speak for the rest of the staff though..."
    sna "" ("snape_13")
    anon "The stories I hear about Minerva McGonagall and those poor Gryffindor freshmen may be true..."
    sna "" ("snape_01")
    anon "Well, I just wanted to make sure that you take those rumours about me for what they are..."
    anon "Nasty lies made up by a bunch of spoiled--"

    anon "Oh.... Before I go..."
    anon "There is one thing I meant to ask you for a while now..."
    sna "" ("snape_09")
    anon "........................."
    sna "" ("snape_05")
    anon "What is my name?"

    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"What? What kind of question is that?\"":
            sna "" ("snape_06")
            anon "You are right..."
            anon "Forgive me... I'm just being paranoid, I suppose..."
            sna "" ("snape_05")
            anon "But you can never be too cautious with rumours about  \"you know who\" still being alive and all..."
        "\"Tall broody guy?\"":
            sna "" ("snape_06")
            anon "Albus, lately you adopted a peculiar sense of humour, that I do not care for in the slightest..."
            anon "Maybe you should spend a little less time in the company of that big oaf Hagrid."
        "-Use magic to get the right answer-":
            $ d_flag_01 = True
            hide snape_main
            with d3
            nar "You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
            sna "" ("snape_03")
            anon "...!"
            gen "What kind of question is this...{w=0.1} Severus?" ("base", xpos="far_left", ypos="head")
            anon "Forgive me... I'm just being paranoid, I suppose..."

    sna "" ("snape_06")
    anon "Well, good night, Albus."

    call sna_walk("door", "base")
    pause.2

    stop music fadeout 1.0
    call bld
    anon "........................"

    # Hide Snape chibi and fade to black
    hide screen snape_chibi
    show screen blkfade
    with d3

    play sound "sounds/07_run.ogg"
    pause 2
    gen "?!" ("angry", xpos="far_left", ypos="head")

    show screen snape_defends
    hide screen bld1
    call hide_blkfade

    play music "music/hitman.ogg" fadein 1 #TENSE THEME if_changed
    call ctc

    call bld
    if d_flag_01:
        sna "Who are you, scum!" ("snape_34", ypos="head", wand=True)
        gen "What? It's me... *Ehm*... {i}Abius{/i}! I mean, Albus!" ("angry", xpos="far_left", ypos="head")
        sna "You cannot fool me." ("snape_32", wand=True)
        sna "Just now, you used some sort of alien magic!" ("snape_32", wand=True)
        sna "Reveal your true self to me now, fiend! Who are you?!" ("snape_34", wand=True)
    else:
        sna "My name is Severus Snape!" (ypos="head", wand=True)
        sna "Now, who might you be...?" ("snape_01", wand=True)

    gen "!!!" ("angry", xpos="far_left", ypos="head")
    sna "Easy now... Just answer my question." ("snape_01", wand=True)
    gen "Alright, alright. Just calm down, would you?" ("base", xpos="far_left", ypos="head")
    gen "You might poke someone's eye with that stick if you're not careful." ("base", xpos="far_left", ypos="head")
    sna "........" ("snape_01", wand=True)

    label no_wait:
    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"I am not your enemy.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna "That's the first thing an enemy would say." ("snape_01", wand=True)
        "\"I'm just a tourist. I'll be leaving now.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna "You are not going anywhere." ("snape_01", wand=True)
        "\"I work for {i}Alvin Dombledork{/i}!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna "It's Albus Dumbledore, you moron!" ("snape_01", wand=True)

    if d_points == 2:
        pass
    else:
        jump no_wait

    sna "Who sent you here? What did you do with the real \nAlbus?" ("snape_01", wand=True)
    sna "Shed your disguise and reveal your true self at once, \nthis is your last warning!" ("snape_01", wand=True)

    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label no_wait_2:
    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"I can't. It's hard to explain...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            sna "I have no interest in your explanations. I wouldn't \nbelieve a single word you'd say anyway!" ("snape_01", wand=True)
        "\"Stop threatening me, human!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            sna "\"Human\"?" ("snape_01", wand=True)
            sna "Are you implying that you are {size=+5}not{/size} one?" ("snape_01", wand=True)
            sna "What are you then?! Dispel your cloaking charm immediately or else!" ("snape_01", wand=True)
        "\"I mean you no harm, I swear!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            sna "Is that so?" ("snape_01", wand=True)
            sna "Prove it then. Dispel your cloaking charm now!" ("snape_01", wand=True)

    if d_points == 2:
        pass
    else:
        jump no_wait_2

    sna "I've heard enough!" ("snape_01", wand=True)
    gen "By the great desert sands! Would you let me explain, human?!" ("angry", xpos="far_left", ypos="head")
    sna "There is nothing left to explain!" ("snape_01", wand=True)
    sna "Since you refuse to co-operate, I'll be taking you \ninto custody by force!" ("snape_01", wand=True)
    gen "What?! Wait!" ("angry", xpos="far_left", ypos="head")
    hide snape_main
    with d3

    $ renpy.choice_for_skipping()

    $ states.sna.ev.intro.e3_complete = True
    if skip_duel == True:
        $ states.sna.ev.intro.duel_complete = True
        jump snape_lost

    stop music
    play music "music/boss_battle_#2_metal_loop.ogg" fadein 1 fadeout 1 if_changed
    play sound "sounds/glass_break.ogg"

    pause.1

    hide screen bld1
    show screen snape_glass
    $ renpy.pause(2.3, hard=True)

    jump duel


# Event 4

# THE TALK AFTER THE DUEL ENDS.

label snape_intro_E4:
    $ states.healing_potions = 0 #Makes sure there are no potions left in the possessions.
    $ renpy.choice_for_skipping()

    stop music fadeout 2.0

    $ duel_OBJ.genie = "no_magic"
    call bld
    with d3

    gen "*Panting*" ("angry", xpos="far_left", ypos="head")
    gen "Ready to talk now?!" ("angry", xpos="far_left", ypos="head")
    sna "(... i-impossible...)" ("snape_36", ypos="head")

    play music "music/Dark Fog.ogg" fadein 1 if_changed
    hide screen duel
    hide snape_main
    call gen_chibi("stand","desk","base")
    call sna_chibi("stand", "door", "base")
    with fade

    gen "I told you that you're no match for me..." ("base", xpos="far_left", ypos="head")
    gen "You did give me a good run for my money though..." ("base", xpos="far_left", ypos="head")
    sna "The way you conjure the spells with your bare hands..." ("snape_01")
    sna "No human could do that... who--" ("snape_01")
    sna "{size=+5}What are you?{/size}" ("snape_32")
    sna "Some sort of shapeshifting demon summoned by \"you know who\"?" ("snape_01")
    gen "Summoned by whom?" ("base", xpos="far_left", ypos="head")
    sna "By \"you know who\"!" ("snape_31")
    gen "What?" ("base", xpos="far_left", ypos="head")
    sna "......................" ("snape_35")
    gen "............................" ("base", xpos="far_left", ypos="head")
    gen "Listen, I'm not a demon..." ("base", xpos="far_left", ypos="head")
    gen "And I sure as heck don't work for \"I don't know who\"!" ("base", xpos="far_left", ypos="head")
    sna "............................." ("snape_01")
    gen "I've been *Ehm*..." ("base", xpos="far_left", ypos="head")
    gen "... Conducting an experiment back in my world, during which something went wrong, and I ended up here." ("base", xpos="far_left", ypos="head")
    gen "That's all..." ("base", xpos="far_left", ypos="head")
    sna ".........................." ("snape_01")
    sna "What became of the real Albus Dumbledore then?" ("snape_01")
    gen "I'm sure he is fine." ("base", xpos="far_left", ypos="head")
    gen "He's Probably feeling just as surprised finding himself in my world as I am about finding myself here..." ("base", xpos="far_left", ypos="head")
    sna "...................................." ("snape_01")
    sna "When did this happen?" ("snape_01")
    gen "It happened a few days ago..." ("base", xpos="far_left", ypos="head")
    sna "Can you go back?" ("snape_01")
    gen "I think so..." ("base", xpos="far_left", ypos="head")
    sna "Why didn't you?" ("snape_31")
    gen "Not sure..." ("base", xpos="far_left", ypos="head")
    gen "The Magic of this world is so bizarre... I just got curious." ("base", xpos="far_left", ypos="head")
    sna "..................." ("snape_01")
    sna "You need to fix this..." ("snape_01")
    gen "Fix what?" ("base", xpos="far_left", ypos="head")
    sna "Everything. You need to bring back Albus and leave our world." ("snape_32")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Yes, yes, I know. Off I go then.\"":
            gen "Sorry for the ruckus." ("base", xpos="far_left", ypos="head")
            sna "No harm done..." ("snape_01")
        "\"But I like it here! Can't I stay?\"":
            sna "Absolutely not." ("snape_01")
            sna "Whoever you are, you are not from this plane of existence." ("snape_01")
            sna "Your very presence here upsets the natural order of things." ("snape_01")
            sna "And these days this school needs a proper headmaster more than ever." ("snape_01")
        "{size=-2}\"I didn't like it here anyway....\"{/size}":
            gen "This is the worst resort I have ever visited..." ("base", xpos="far_left", ypos="head")
            gen "No air-conditioning, no complimentary chocolate..." ("base", xpos="far_left", ypos="head")
            gen "I doubt there's even a pool." ("base", xpos="far_left", ypos="head")
            gen "And the attitude of the personnel..." ("base", xpos="far_left", ypos="head")
            sna "........" ("snape_05")

    sna "Have a safe trip home now." ("snape_01")
    gen "*Ehm*... Thank you, Mr Servus." ("base", xpos="far_left", ypos="head")
    sna "My name is {b}Severus{/b}, not Servus..." ("snape_43")
    gen "Right..." ("base", xpos="far_left", ypos="head")
    gen "Good luck with your students and the \"Potter Gang\"." ("base", xpos="far_left", ypos="head")
    sna "\"The potter gang\"?" ("snape_01")
    sna "Oh, right, those buggers..." ("snape_35")
    hide snape_main
    with d3

    menu:
        "-Undo the spell-":
            play sound "sounds/fire_woosh.ogg"
            show screen gfx_effect(510, 350, img="smoke", zoom=0.8)
    menu:
        "-Undo the spell-":
            play sound "sounds/fire_woosh.ogg"
            show screen gfx_effect(510, 350, img="smoke", zoom=0.8)
            gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    menu:
        "-Undo the spell-":
            play sound "sounds/fire_woosh.ogg"
            show screen gfx_effect(510, 350, img="smoke", zoom=0.8)

    gen "(Something's not right, I can't undo the spell...)" ("base", xpos="far_left", ypos="head")
    sna "Did it work? Albus, is that really you?" ("snape_01")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Yeah, that's me. So good to be back!\"":
            sna "Glad to have you back, old friend. Are you alright?" ("snape_01")
            gen "I'm fine, Severus, thank you." ("base", xpos="far_left", ypos="head")
            sna "How was it, in that other world?" ("snape_01")
            gen "A lot of sand and very hot, but other than that quite pleasant." ("base", xpos="far_left", ypos="head")
            sna "I see... Did you miss your brother?" ("snape_01")
            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"Yes, I missed you so much!\"":
                    sna "......................." ("snape_01")
                    sna "Yeah, right..." ("snape_01")
                "\"I don't have a brother, Severus.\"":
                     sna "........................" ("snape_01")
                     sna "You may not have one, but the real Albus Dumbledore does." ("snape_01")
                "-Use magic to get the right answer-":
                    nar "You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
                    gen "My little brother Aberforth? Why would I miss him?" ("base", xpos="far_left", ypos="head")
                    sna "I can feel it whenever you use your alien magic..." ("snape_01")

        "\"Nope. It's still me. The non-human guy.\"":
            pass

    sna "Why are you still here, creature?" ("snape_01")
    gen "There's no need to be rude." ("base", xpos="far_left", ypos="head")
    gen "And I'm not sure... I tried to undo the spell, but nothing happened..." ("base", xpos="far_left", ypos="head")
    sna "Marvellous..." ("snape_35")
    sna "What does this mean? You're staying here for good?" ("snape_01")
    gen "Of course not..." ("base", xpos="far_left", ypos="head")
    gen "Me being here at all is only possible because the spell is compensating for the imbalance caused by itself..." ("base", xpos="far_left", ypos="head")
    gen "said spell will wear off eventually, and I shall be pulled back into my world." ("base", xpos="far_left", ypos="head")
    gen "Likewise, your Dumb-le-dork friend shall be pulled back here." ("base", xpos="far_left", ypos="head")
    sna "I see..." ("snape_01")
    sna "How long until the spell wears off?" ("snape_01")

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"A couple of days.\"":
            sna "I see..." ("snape_01")
        "\"A week or so...\"":
            sna "*Hmm*.... A week, huh..." ("snape_01")
        "\"Could be months...\"":
             sna "That long?" ("snape_01")
             sna "Now isn't that just \"perfect\"?" ("snape_01")
        "\"I have no clue...\"":
            sna "....................." ("snape_01")
            sna "Splendid..." ("snape_31")

    gen "Alright, to be honest, I'm not sure where to go from here..." ("base", xpos="far_left", ypos="head")
    gen "All this time I thought I could undo the spell whenever I wanted to..." ("base", xpos="far_left", ypos="head")
    sna "..................................................." ("snape_01")
    sna ".................................." ("snape_01")
    sna "..................." ("snape_01")
    gen "Snape?" ("base", xpos="far_left", ypos="head")
    sna "..................................................." ("snape_01")
    gen "Severus?" ("base", xpos="far_left", ypos="head")
    sna "Yes, yes..." ("snape_34")
    sna "Listen, it's very late, and too much has happened already..." ("snape_01")
    sna "I need to process all of this." ("snape_35")
    sna "I will come to see you tomorrow, after my classes." ("snape_01")
    sna "Until then, keep your true identity and our conversation a secret, alright?" ("snape_34")
    gen "Not a problem." ("base", xpos="far_left", ypos="head")
    sna "Alright then..." ("snape_01")
    sna "But before I go, I have one more question..." ("snape_01")
    gen "I'm listening..." ("base", xpos="far_left", ypos="head")
    sna "........" ("snape_31")
    sna "If you are not a human, then..." ("snape_01")
    sna "What are you?" ("snape_35")
    gen "... I'm a genie." ("base", xpos="far_left", ypos="head")
    sna "A genie?" ("snape_01")
    gen "Yes, I possess phenomenal cosmic powers and all that..." ("base", xpos="far_left", ypos="head")
    sna "Seriously?" ("snape_01")
    gen "Oh, yes." ("base", xpos="far_left", ypos="head")
    sna "Unbelievable..." ("snape_01")
    sna "Well, I'll see you tomorrow.... Genie." ("snape_01")
    gen "I'll be here..." ("base", xpos="far_left", ypos="head")

    sna "(A genie? Now that's new...)" ("snape_35")

    hide screen duel
    call sna_chibi("hide")
    $ states.sna.ev.intro.e4_complete = True

    jump day_start


# Event 5

# Snape visits you after the dual (next evening).

label snape_intro_E5:
    play music "music/Dark Fog.ogg" fadein 1 if_changed

    call sna_walk(action="enter", xpos="mid", ypos="base")

    sna "" ("snape_01",xpos="base",ypos="base")

    sna "..................."
    gen "Good evening..." ("base", xpos="far_left", ypos="head")
    sna "Is the spell still in effect?"
    gen "Yes. very much so." ("base", xpos="far_left", ypos="head")
    sna "I see..."
    sna "Last night I gave our little.... conundrum some thought."
    sna "And I think I came up with a solution..."
    gen "Really? Great! I'm listening." ("base", xpos="far_left", ypos="head")

    sna "Let's just roll with it..." ("snape_29")
    gen "Excuse me?" ("base", xpos="far_left", ypos="head")
    sna "Well, what else could we do?" ("snape_06")
    sna "Normally I would alert the ministry of magic and let them take care of this mess..."
    sna "But I'd rather avoid any dealings with those rotten bureaucrats this time..."
    sna "Also, losing a headmaster, even temporarily, could hurt the school's reputation..." ("snape_10")
    sna "And what if your spell wears off tomorrow, or even tonight?"
    sna "I see no reason to start a commotion..." ("snape_09")
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    sna "So we shall keep the charade going for now..." ("snape_03")

    gen "By doing what exactly?" ("base", xpos="far_left", ypos="head")
    sna "Just act like Albus always does; Never leave this tower and avoid any human contact..." ("snape_05")
    gen "That..." ("base", xpos="far_left", ypos="head")
    gen "Sounds..." ("base", xpos="far_left", ypos="head")
    gen "Incredibly boring!" ("angry", xpos="far_left", ypos="head")
    gen "What am I supposed to do here?" ("angry", xpos="far_left", ypos="head")
    sna "You are a Genie. Conjure up some sort of entertainment for yourself." ("snape_01")
    gen "My magic doesn't seem to be working properly here for some reason..." ("base", xpos="far_left", ypos="head")
    gen "And my lamp is literally worlds away..." ("base", xpos="far_left", ypos="head")
    sna "Well, what do you expect me to do about that?" ("snape_03")
    sna "Send you a couple of girls from Slytherin maybe?"
    gen "I have no idea what Slytherin is, but I think that would work..." ("grin", xpos="far_left", ypos="head")
    sna "That was a joke, obviously." ("snape_04")
    sna "Although..." ("snape_09")
    sna "*Hmm*..."
    sna "Well, in any case, I don't see how entertaining {size=+7}you{/size} is {size=+7}my{/size} problem." ("snape_01")
    gen "Oh, but it is!" ("base", xpos="far_left", ypos="head")
    gen "I'm immortal and all-powerful..." ("base", xpos="far_left", ypos="head")
    gen "Being bored is one of the worst things that could happen to me!" ("base", xpos="far_left", ypos="head")
    gen "And I have a thing against being cooped up in small spaces with nothing to do!" ("angry", xpos="far_left", ypos="head")
    gen "I may lose my mind..." ("angry", xpos="far_left", ypos="head")
    gen "Oh! Ah! I think it's happening already!" ("angry", xpos="far_left", ypos="head")
    sna "......." ("snape_03")
    gen "I'm losing my mind! It's getting hard to breathe!" ("angry", xpos="far_left", ypos="head")
    sna "...." ("snape_04")
    gen "It's so dark..." ("angry", xpos="far_left", ypos="head")
    gen "Are you still here?" ("angry", xpos="far_left", ypos="head")
    sna "...." ("snape_03")
    gen "........." ("base", xpos="far_left", ypos="head")
    sna "Are you done?" ("snape_10")
    gen "Yes..." ("base", xpos="far_left", ypos="head")
    gen "Seriously though, I don't see how this whole affair benefits me at all." ("base", xpos="far_left", ypos="head")
    sna "Do you have any choice?" ("snape_01")
    gen "I do..." ("base", xpos="far_left", ypos="head")
    gen "Instead of sitting here on my ass all day and being quiet, I could explore your world..." ("base", xpos="far_left", ypos="head")
    sna "*Hmm*..." ("snape_03")
    sna "Well, alright, what do you want?" ("snape_01")

    menu:
        "\"A chair.\"":
            sna "What's wrong with your current chair?" ("snape_05")
            gen "Nothing. But I want another one in case I wanted to sit by the fire." ("base", xpos="far_left", ypos="head")
            sna "I guess that can be arranged..." ("snape_01")
            sna "What else?"
            gen "I want to learn more about your magic..." ("base", xpos="far_left", ypos="head")
        "\"A maid!\"":
            gen "Send me the cutest one!" ("grin", xpos="far_left", ypos="head")
            sna "{size=-6}*Hmm*... I guess I could assign a house elf to clean this room.{/size}" ("snape_09")
            sna "Alright. Is that all?" ("snape_01")
            gen "I want you to teach me your magic..." ("base", xpos="far_left", ypos="head")
        "\"I want three wishes.\"":
            sna "Three wishes?" ("snape_44")
            sna "Who do you think I am? A genie?" ("snape_24")
            gen "Three wishes, or I'm walking through that door right now." ("base", xpos="far_left", ypos="head")
            sna "...Fine." ("snape_31")
            sna "What do you want?" ("snape_35")
            gen "First, I want a maid!" ("grin", xpos="far_left", ypos="head")
            sna "This isn't a motel--" ("snape_08")
            sna "{size=-6}*Hmm*... I guess I could assign a house elf to clean this room.{/size}" ("snape_09")
            gen "What was that?" ("base", xpos="far_left", ypos="head")
            sna "Nothing, go on." ("snape_01")
            gen "Second, a chair." ("base", xpos="far_left", ypos="head")
            sna "A chair? What do you need the chair for?" ("snape_05")
            sna "You're already sitting on one." ("snape_05")
            gen "I don't want my guests to just stand." ("base", xpos="far_left", ypos="head")
            sna "Guests? You're not supposed to have g--" ("snape_10")
            sna "*sigh* It's pointless reasoning with you, isn't it?" ("snape_06")
            gen "You're learning quick." ("base", xpos="far_left", ypos="head")
            sna "Alright, you'll have your chair." ("snape_03")
            gen "and lastly..." ("base", xpos="far_left", ypos="head")
            gen "Teach me your magic..." ("base", xpos="far_left", ypos="head")

    sna "My magic?" ("snape_05")
    gen "Yes... The way you conjure up your spells is..." ("base", xpos="far_left", ypos="head")

    hide snape_main
    call bld("hide")
    call sna_chibi(flip=True)
    with d3

    play sound "sounds/fire_woosh.ogg"
    show screen gfx_effect(780, 300, img="smoke", zoom=0.7)
    $ chair_OBJ.hidden = False

    "Snape takes out his magic wand and conjures a chair."

    gen "Intriguing..." ("base", xpos="far_left", ypos="head")
    call sna_chibi(flip=False)
    sna "*Hmm*... I suppose that could be arranged..." ("snape_05", trans=d3)
    gen "Oh, and I wouldn't mind if you sent me some of those Slytherin girls as well..." ("base", xpos="far_left", ypos="head")
    sna "..............." ("snape_05")
    sna "........................."
    sna "*Ha-ha-ha*!!!" ("snape_28")
    gen "What? What did I say?" ("base", xpos="far_left", ypos="head")
    sna "*A-ha-ha-ha-ha*..." ("snape_28")
    sna "No, no, my apologies..." ("snape_02")
    sna "It's just that to me, you still look and sound like Albus..."
    sna "To hear Professor Dumbledore say things like \"Send me some of those girls\"..."
    sna "It's hysterical..." ("snape_22")
    sna "But you wouldn't understand..." ("snape_09")
    gen "*Heh*..." ("base", xpos="far_left", ypos="head")
    gen "Send those whores up, Severus. I'm feeling lonely tonight." ("grin", xpos="far_left", ypos="head")
    sna "*Ha-ha-ha*! Stop it, you're killing me!" ("snape_28")
    sna "*A-Ha-ha-ha*!"
    gen "No, I'm serious... Is it possible?" ("base", xpos="far_left", ypos="head")
    sna "*Hmm*..." ("snape_02")
    sna "We'll see..."
    sna "You being our new headmaster presents me with interesting possibilities..."
    sna "I need some time to figure out how to use this situation to my advantage."
    gen "You mean {size=+7}our{/size} advantage, right?" ("base", xpos="far_left", ypos="head")
    sna "Oh, yes. Yes, of course..." ("snape_06")
    sna "Well, I think we are done for today..."
    sna "Good night... genie." ("snape_24")
    gen "Yes. Good night, Severus." ("base", xpos="far_left", ypos="head")

    call sna_walk("door", "base")
    pause.2

    sna "................." ("snape_06", ypos="head")
    sna "\"Send those whores up, Severus!\" *Ha-ha-ha*..." ("snape_28")

    call sna_chibi("leave")

    call bld
    gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
    gen "I Suppose I'll just curl up in a ball on top of this desk as usual..." ("base", xpos="far_left", ypos="head")
    pause.2

    $ states.sna.unlocked = True
    # Silently add an achievement, then display a popup message.
    $ achievements.unlock("unlocksna", True)
    call popup("{size=-4}You can now summon Snape into your office.{/size}", "Character unlocked!", "interface/icons/head/snape.webp")
    $ states.sna.ev.intro.e5_complete = True

    call tutorial("hangouts")

    jump day_start
