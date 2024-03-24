
### Hermione Intro ###

### Event 1 ###
# Fist visit of Hermione.

label hermione_intro_E1:
    stop music fadeout 1.0
    pause 1

    # Force default outfit for first event.
    $ hermione.equip(her_outfit_default)

    play sound "sounds/knocking.ogg"
    call bld
    "*Knock-knock-knock*"
    gen "*huh*?" ("base", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    pause.7

    gen "Somebody is knocking on the door..." ("base", xpos="far_left", ypos="head")
    gen "Crap... I'm supposed to avoid any human contact!" ("base", xpos="far_left", ypos="head")
    gen "*Hmm*... What are the chances that the thing knocking on my door is not human?" ("base", xpos="far_left", ypos="head")
    gen "Yeah, quite slim..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    gen "Persistent little bastard..." ("base", xpos="far_left", ypos="head")

    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"Who is it?\"":
            $ d_flag_01 = True
            call bld
            femv "It's me, professor..."
            femv "Hermione Granger. Can I come in?"
            gen "{size=-4}(It's that woman who's been harassing me with her letters lately...){/size}" ("base", xpos="far_left", ypos="head")

            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"Go away, please. I'm busy.\"":
                    call bld
                    her "But, professor, I really need to talk to you..."
                    gen "..........................................." ("base", xpos="far_left", ypos="head")
                    her "Professor? I'm coming in!"
                    gen "{size=-4}(Crap...){/size}" ("base", xpos="far_left", ypos="head")
                "\"Yes, yes, you can come in.\"":
                    pass

        "\"Come in!\"":
            pass
        "\"Go away!\"":
            call bld
            femv "But, professor, I really need to talk to you..."
            gen "..........................................." ("base", xpos="far_left", ypos="head")
            femv "Professor? I'm coming in!"
            gen "{size=-4}(Crap...){/size}" ("base", xpos="far_left", ypos="head")
        "\"................\"":
            call bld
            femv "Professor, are you there?"
            gen "{size=-4}(Go away...){/size}" ("base", xpos="far_left", ypos="head")
            femv "Professor, I really need to talk to you..."
            gen "..........................................." ("base", xpos="far_left", ypos="head")
            her "Professor? I'm coming in!"
            gen "{size=-4}(Crap...){/size}" ("base", xpos="far_left", ypos="head")

    call bld("hide")
    pause.2

    play sound "sounds/door.ogg"
    call her_chibi("stand","door","base")
    with d3
    pause.5

    call bld
    if d_flag_01:
        gen "{size=-3}(This is the Granger girl? Well, well, well.){/size}" ("grin", xpos="far_left", ypos="head")
    else:
        gen "A girl?!" ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base")
    pause.5

    $ hermione.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
    $ hermione.set_pose("hold_book")
    show CG her_intro hermione as cg zorder 17:
        align (0.5, 0.5)
        pos (-520, -300)
    with fade

    show CG her_intro hermione as cg zorder 17:
        align (0.5, 0.5)
        pos (-520, -300)
        easein 5.0 pos (-520, -70)
        pause 5.0

    her "Good morning, professor."
    gen "(Oh my...)"

    show CG her_intro hermione as cg zorder 17:
        zoom 1.0
        align (0.5, 0.5)
        pos (-520, -70)
        easein_quad 3.0 align (0.0, 0.0) pos (0, 0) zoom 0.5

    menu:
        "\"Good morning, Hermione.\"" if d_flag_01:
            her "{size=-4}(At least he remembers my name.){/size}" ("base", "base", "base", "mid")
        "\"Good morning... girl.\"" if not d_flag_01:
            her "{size=-4}(\"Girl\"?){/size}" ("normal", "squint", "worried", "mid")
        "\"Good morning, child.\"":
            her "{size=-4}(\"Child\"...?){/size}" ("upset", "narrow", "worried", "mid")
        "\"Greetings fellow human!\"":
            her "Are you alright, professor?" ("normal", "squint", "worried", "mid")
            gen "Why, of course, I'm a human after all!"
            her "..." ("normal", "base", "low", "mid")
            her "Are you sure, professor? I can call for madam Pomfrey to examine you..." ("open", "base", "worried", "mid")
            play sound "sounds/punch01.ogg"
            with hpunch
            gen "{size=+4}NO!{/size}"
            pause 1.0
            gen "*Err*...{w=0.5} I mean... No, thank you, dear child, it won't be necessary."
            her "If you say so, professor..." ("annoyed", "base", "worried", "L")
            her "*Clears throat*" ("normal", "closed", "base", "mid")
        "\"................................\"":
            her "..........." ("normal", "base", "base", "mid")
            gen "................................."
            her "..... *Ahem*......" ("open", "closed", "angry", "mid")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "I am very busy with my class schedule, but I kept my morning free today so that I could see you, professor." ("open", "base", "base", "mid")
    gen "Right..."
    her "One moment, professor..." ("open", "narrow", "base", "down")

    show CG her_intro hermione bendover as cg zorder 17
    with d5

    nar "Hermione turns around and puts her book down."
    gen "!!!"


    $ hermione.set_pose(None)
    show CG her_intro hermione as cg zorder 17
    with d5

    her "That's better... My arms were getting sore." ("open", "closed", "base", "mid")

    gen "{size=-4}(Damn, I haven't seen a woman in weeks.){/size}"

    menu:
        "\"(I will jerk off a little while she talks.)\"":
            call hide_characters
            hide screen bld1
            with d3
            pause.2

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause.5

            show screen bld1
            nar "You reach under the desk and grab your cock..."

            $ states.gen.stats.masturbated_to_hermione += 1
            $ states.her.ev.intro.masturbated = True #Affects next conversation with Snape.
            $ states.gen.masturbating = True

        "\"(No, that's stupid! I need to behave!)\"":
            $ states.gen.masturbating = False

    her "You probably know why I am here too."
    her "The issue I have been fruitlessly trying to bring to your attention lately." ("open", "closed", "angry", "mid")
    her "I cannot understand why you are not acting to stop that nonsense, professor!"
    her "This simply cannot continue!"
    her "The inequality is starting to affect all of the houses..." ("open", "base", "base", "mid")
    her "Simply because Gryffindor has more integrity than the rest..."
    her "Do you think it's fair that the people who deserve to be in the lead are being pushed back instead?"
    her "Do you think that's fair, professor? Do you?"
    her "" ("normal", "base", "base", "mid")
    gen "{size=-4}(Would you look at that pretty little thing?){/size}"
    gen "{size=-4}(Look at her going on and on about something... She's adorable.){/size}"
    gen "Yes, keep on going, dear."
    her "\"Yes\"?! So, you think it's fair?" ("angry", "base", "angry", "mid")
    gen "Oh, of course not, I meant \"no\". But keep on going anyway..."
    her "That's a relief. I'm glad that you agree with me, professor..." ("soft", "closed", "base", "mid")
    her "As I was saying, the whole issue is simply ridiculous, and I cannot believe that it is taking place in our day and age!" ("open", "closed", "angry", "mid")

    if states.gen.masturbating:
        nar "*Fap-fap-fap*"
        nar "You keep on stroking your cock..."
    else:
        gen "I see..."

    her "I mean, I would understand if something like this were to occur during the Middle Ages..."
    her "But we left the Middle Ages behind a long time ago, did we not?"

    if states.gen.masturbating:
        gen "{size=-4}(Would you look at those rosy cheeks? I want to poke 'em with my cock.){/size}"
        nar "You keep stroking your cock..."
    else:
        gen "*Ehm*... I suppose you did. I mean, we did."

    her "So it hurts the whole house point distribution system."
    her "But it doesn't even stop there!"
    her "It hurts our entire educational system as well..."
    her "And more importantly, the motivation among students is steadily decreasing due to it!"

    if states.gen.masturbating:
        gen "{size=-4}(Look at those huge knockers on you, girl!){/size}"
        gen "{size=-4}(Yes... I want to squeeze my dick between them...){/size}"

    her "As you can see, the situation is dire..."
    her "But we can still set everything right..." ("open", "base", "base", "mid")
    her "As the president of our school's Student Representative Body..."
    her "I have a few suggestions on how to do that more efficiently."

    if not states.gen.masturbating:
        gen ".............."

    her "First of all, the house point system needs to be maintained!"
    her "You need to control the point distribution better, sir." ("open", "base", "base", "mid")

    if states.gen.masturbating:
        gen "{size=-4}(Yes, you are a whore... A nasty little whore... I bet you love to suck cocks... Don't you? Yes, I bet you do...){/size}"
        nar "You stroke your rock-hard cock ferociously!"

    her "Of course you agree with me on this, professor, do you not?"

    if states.gen.masturbating:
        gen "{size=-4}*Panting heavily*{/size}"
        her "Professor...?" ("normal", "squint", "angry", "mid")
        gen "{size=-4}(Crap. What does she want now?){/size}"
        gen "Yes, it's all true. Please keep going..."
        her "*Ehm*... So, as I was saying..."
        gen "{size=-4}(Oh... That was a good jerk-off session, but I'm getting dangerously close to the \"grand finale\".){/size}"
        gen "{size=-4}(Maybe I should stop before I get myself into trouble.){/size}"

        menu:
            "\"(Yes, time to actually listen to her.)\"":
                $ states.gen.masturbating = False

                call hide_characters
                hide screen bld1
                with d3

                call gen_chibi("sit_behind_desk")
                with d3
                pause.5

            "\"(No! I want to keep on jerking off!)\"":
                gen "Yes, yes! *pants*"

    if not states.gen.masturbating:
        gen "{size=-4}(Do I? I honestly don't give a damn...){/size}"
        gen "*Err*... I suppose I do..."
        her "{size=-4}(\"Suppose\"?){/size}" ("annoyed", "base", "base", "mid")
        her "{size=-4}(When did Professor Dumbledore become so... apathetic?){/size}" ("annoyed", "base", "worried", "R")

    her "Another measure you could take into consideration is tightening your control over the staff..." ("open", "closed", "angry", "mid")
    her "Especially the teachers..."
    her "I hope I'm not stepping out of line here, sir, but some of the teachers really do require supervision..." ("normal", "base", "base", "mid")

    if states.gen.masturbating:
        gen "{size=-4}(Yes! You little whore! You little fucking whore!) *Panting*{/size}"
    else:
        gen "......................."

    her "I understand that you may not have time for this, professor. After all, you are the headmaster of our school, and a very busy man." ("open", "closed", "angry", "mid")
    her "Being a top student is hard on me as well, sometimes..."

    if states.gen.masturbating:
        gen "{size=-4}(She said \"hard-on\"!) *Panting*{/size}"

    her "But you could delegate that task to me--"

    show CG her_intro hermione bendover as cg zorder 17
    with d5
    nar "Hermione bends down again to pick up her book."

    her "--Just put your faith in me, professor."

    $ hermione.set_pose("hold_book")
    show CG her_intro hermione as cg zorder 17
    with d5

    if states.gen.masturbating:
        her "Yes, you can do it! Just put it in me, sir!" ("base", "closed", "base", "mid")
        stop music fadeout 1.0

        gen "{size=-4}(Oh crap, that did it!) *Argh*!{/size}"

        hide cg
        hide hermione_main
        hide screen bld1
        with fade
        pause.2

        call cum_block

        call gen_chibi("cum_behind_desk")
        with d3
        pause 3

        her "Professor?! What is going on...?" ("angry", "wide", "base", "mid", trans=d3, xpos="mid")

        gen "*Ah*... YESSSSS.....!" ("angry", xpos="far_left", ypos="head")
        call cum_block
        her "...???"
        gen "*breathing heavily* Yes! yes..." ("angry", xpos="far_left", ypos="head")

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause.5

        gen "Yes, girl. It's all exactly as you say and I will.... take care of it all." ("base", xpos="far_left", ypos="head")
    else:
        gen "Alright... I will think about your proposal, I promise."

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "Really?" ("normal", "squint", "angry", "mid")
    her "*Hmm*..........."

    her "That's a relief! Thank you, professor." ("open", "closed", "angry", "mid", xpos="mid")

    if not states.gen.masturbating:
        hide cg
        with fade

    if states.gen.masturbating:
        gen "No, no, thank you..." ("base", xpos="far_left", ypos="head")
        her "*Hmm*..." ("normal", "squint", "angry", "mid")

    her "My classes are about to start, so I'd better go now." ("open", "closed", "angry", "mid")
    her "Thank you for your time..." ("base", "base", "base", "mid")
    her "Have a good day, professor." ("base", "base", "base", "mid")

    call her_walk(action="leave")

    $ hermione.set_pose(None)

    if states.gen.masturbating:
        gen "{size=-4}(This was awesome...) *Panting*{/size}" ("base", xpos="far_left", ypos="head")
        gen "{size=-4}(My trousers are ruined though...){/size}" ("base", xpos="far_left", ypos="head")
    else:
        gen "................." ("base", xpos="far_left", ypos="head")
        gen "(She is cute, but quite a piece of work...)" ("base", xpos="far_left", ypos="head")

    call gen_chibi("sit_behind_desk")
    with d3

    $ states.sna.busy = True # No point in calling him during the day.
    $ states.her.ev.intro.e1_complete = True

    jump end_hermione_event


### Snape Hangout Event 1 ###
# Snape shares his opinion of Hermione with you.

label ss_he_hermione_E1:
    sna "..........................." ("snape_31", ypos="head")
    gen "...............................?" ("base", xpos="far_left", ypos="head")
    sna "I hate her so much..." ("snape_08")

    menu:
        "\"Yeah! That bitch!\"":
            sna "Good to know that we are on the same page..." ("snape_01")
            sna "That girl..." ("snape_31")
        "\"You hate who?\"":
            sna "Why would you ask that?" ("snape_01")
            sna "That Hermione girl of course!" ("snape_01")
        "\"Is she that bad?\"":
            sna "She is the worst!" ("snape_01")

    sna "A top student..." ("snape_31")
    sna "Leads all sorts of extracurricular activities and clubs..." ("snape_08")
    sna "the president of the school's Student Representative Body..." ("snape_08")
    sna "Likely to become the head girl soon..." ("snape_08")
    sna "................" ("snape_31")
    sna "............" ("snape_08")
    with hpunch
    sna "{size=+7}I hate that fucking witch!!!{/size}" ("snape_33")
    gen "{size=-4}(What the...?){/size}" ("angry", xpos="far_left", ypos="head")
    sna ".............." ("snape_31")
    sna "She used to be just an annoyance, but these days..." ("snape_31")
    sna "She's become a full-fledged menace..." ("snape_01")
    sna "That witch is officially my least favourite student in the entire school now..." ("snape_01")
    gen "What about that Potter boy?" ("base", xpos="far_left", ypos="head")
    sna "The Potter boy? Ha! Who's that!?" ("snape_34")
    sna "No, I'm serious..." ("snape_01")
    sna "I will go as far as to say that Potter and his wretched father combined..." ("snape_01")
    sna "Have never caused me as much grief as this little witch does lately..." ("snape_01")
    gen "Now, now. We both know that's not true..." ("base", xpos="far_left", ypos="head")
    sna "Yeah... You're probably right..." ("snape_31")
    sna "That bastard James Potter really did a number on me--" ("snape_35")
    sna "Wait, how do you know this?" ("snape_34")

    menu:
        "\"Well... I've read the books...\"":
            sna "What? What books?" ("snape_34")
            gen "Nah, never mind. I'm a genie, remember? I know things..." ("base", xpos="far_left", ypos="head")
            sna "*Hmm*... And yet, you need me to teach you stuff..." ("snape_37")
            gen "Well, I told you. My magic is acting up in your world..." ("base", xpos="far_left", ypos="head")
            sna "Sure, sure..." ("snape_37")
            gen "......" ("base", xpos="far_left", ypos="head")
        "\"You mentioned the potter boy earlier.\"":
            sna "I did? I don't remember." ("snape_05")
            sna "No matter." ("snape_09")

    gen "She came by the other day, by the way..." ("base", xpos="far_left", ypos="head")
    sna "Who did?" ("snape_38")
    gen "The Hermione girl..." ("base", xpos="far_left", ypos="head")
    sna "What?!" ("snape_01")
    sna "I thought we agreed on the \"no human contact\" rule." ("snape_31")
    sna "(Even though lately, I've been wondering whether or not she is human at all...)" ("snape_35")
    gen "I know... She kinda forced her way in..." ("base", xpos="far_left", ypos="head")
    sna "I imagine she did..." ("snape_01")
    sna "What did she want?" ("snape_01")

    if states.her.ev.intro.masturbated:
        gen "I'm not sure..." ("base", xpos="far_left", ypos="head")
        sna "...?" ("snape_39")
        gen "I was jerking off the entire time she was talking..." ("base", xpos="far_left", ypos="head")
        sna "You've been..." ("snape_31")
        sna "... doing what?" ("snape_14")
        gen "Hey, don't judge me!" ("base", xpos="far_left", ypos="head")
        gen "You don't know what it's like to be cooped up in this tower like a prisoner!" ("base", xpos="far_left", ypos="head")
        sna "You... y-you..." ("snape_12")
        sna "*Snickers*......" ("snape_13")
        sna "*Ha*... *ha-ha*... *HA-HA-HA*!!!" ("snape_28")
        gen "Wha--? What did I say?" ("base", xpos="far_left", ypos="head")
        sna "*Ha-ha-ha*! You are amazing!" ("snape_42")
        sna "Are all genies so... wonderfully nihilistic?" ("snape_42")
        gen "Yeah... We immortals tend to not give a fuck." ("base", xpos="far_left", ypos="head")
        sna "Understandable..." ("snape_37")
        sna "Unfortunately, us mere mortals cannot afford such a luxury..." ("snape_39")
    else:
        gen "Not sure... She was talking a lot..." ("base", xpos="far_left", ypos="head")
        gen "Something about some {i}grief-n-door{/i} points... and..." ("base", xpos="far_left", ypos="head")
        gen "*Err*... I wasn't paying attention, to be honest..." ("base", xpos="far_left", ypos="head")
        sna "Nah... Probably another load of self-righteous crap..." ("snape_01")
        sna "She is famous for that..." ("snape_35")

    sna "I have a class early tomorrow, so let us call it a night." ("snape_01")
    gen "What about you teaching me magic and stuff?" ("base", xpos="far_left", ypos="head")
    sna "Yeah, absolutely..." ("snape_38")
    sna "Next time..." ("snape_38")
    gen "Alright..." ("base", xpos="far_left", ypos="head")

    nar "Your meeting comes to an end, and you decide to go to sleep."

    $ states.sna.ev.hangouts.hermione_e1 = True

    jump end_snape_hangout_points

### Event 2 ###
# Second visit from Hermione. Says she sent a letter to the Minestry.
# Takes place after the first special event with Snape, where he just complains about Hermione.

label hermione_intro_E2:
    stop music fadeout 3.0
    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock!*"

    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger."
            gen "(It's that witch again...)" ("base", xpos="far_left", ypos="head")
            her "Can I come in, sir?"
            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow, then..."
                    $ achievements.unlock("knock")
                    $ hg_event_pause += 1

                    call music_block
                    jump main_room_menu

                "\"Of course. Come on in.\"":
                    pass

        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            $ achievements.unlock("knock")
            $ hg_event_pause += 1

            call music_block
            jump main_room_menu

        "\"Yes, come in.\"":
            pass

        "\"...................................\"":
            play sound "sounds/knocking.ogg"
            "*Knock-knock-knock*!"
            gen "............................." ("base", xpos="far_left", ypos="head")
            her "Professor, I'm coming in..."
            gen "{size=-4}(Crap!){/size}" ("base", xpos="far_left", ypos="head")

    # Let Hermione in.
    call her_walk(action="enter", xpos="mid", ypos="base")
    pause.5

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "" ("normal", "base", "base", "mid", xpos="base", ypos="base")
    call ctc

    her "Good morning, professor Dumbledore." ("open", "closed", "angry", "mid")

    menu:

        "\"Good morning, child.\"":
            her "{size=-4}(Again with the \"child\"...){/size}" ("annoyed", "squint", "angry", "mid")
            her "Sir, I would appreciate it if you would treat me as an equal..." ("open", "closed", "angry", "mid")
            gen "{size=-4}(I'm literally millions of years older than you, witch. We are anything but equal.){/size}" ("base", xpos="far_left", ypos="head")
            gen "...................." ("base", xpos="far_left", ypos="head")
            her "................" ("annoyed", "squint", "angry", "mid")
        "\"Good morning, miss Granger.\"":
            her "*Ehm*... So, about the reason for me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            her "................" ("annoyed", "squint", "angry", "mid")

    her "I see that no matter what I do I simply cannot get through to you, sir."
    her "So in light of your negligence, I decided to take the initiative myself!" ("open", "closed", "angry", "mid")
    gen "Did you now...?" ("base", xpos="far_left", ypos="head")
    her "Yes! We, the proud students of Hogwarts, detest sexism..."
    her "No individual shall be treated differently based on his or her gender."
    gen "But--" ("base", xpos="far_left", ypos="head")
    her "Please, let me finish, professor!" ("angry", "base", "angry", "mid")
    her "I'm organizing the \"Men's rights movement\" in our school!" ("open", "closed", "angry", "mid")
    gen "Oh boy, this is just so typical!" ("angry", xpos="far_left", ypos="head")
    gen "Blame everything on--" ("angry", xpos="far_left", ypos="head")
    stop music fadeout 1.0
    gen "Wait, did you say {size=+5}MEN'S{/size} rights movement?" ("base", xpos="far_left", ypos="head")
    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "You have no idea how hard it is to be a boy in our school these days..." ("open", "base", "worried", "mid")
    menu:
        "\"Didn't see this one coming...\"":
            her "No, you did not, because you refuse to listen to us, sir!" ("open", "closed", "angry", "mid")
            her "But we will make you hear us..."
        "{size=-3}\"That's literally the dumbest idea I've ever heard.\"{/size}":
            her "I knew you would say something like that..." ("normal", "squint", "angry", "mid")

    her "Did you know that some of the girls in this school are now selling favours for house points...?" ("annoyed", "squint", "angry", "mid")
    her "Sometimes even for good grades..."
    gen "Really?" ("base", xpos="far_left", ypos="head")
    her "Nobody from the Gryffindor house, of course..." ("open", "closed", "angry", "mid")
    her "And that's what puts us at a disadvantage -- our integrity!"
    her "As for the boys -- they have to work ten times harder than the girls simply to pass a test..."
    her "Or, if they are lucky enough, to get one meagre house point..."
    her "This is sexism in its purest form!" ("open", "base", "base", "mid")
    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "\"What do you want me to do?\"":
            her "Nothing!" ("normal", "base", "base", "mid")
            gen "Great. I'm good at that." ("base", xpos="far_left", ypos="head")
        "\"I'm not sure what to say...\"":
            her "You do not need to say anything anymore, professor." ("normal", "base", "base", "mid")
        "\"You are being ridiculous!\"":
            her "Am I? Well, we'll see..." ("normal", "squint", "angry", "mid")

    her "I have already sent a letter to the ministry of magic." ("open", "closed", "angry", "mid")

    $ renpy.music.set_volume(0.0, 1.0)
    pause 1.0
    $ renpy.music.set_pause(True, channel="music")
    with hpunch
    gen "{size=+7}You did what?!{/size}" ("angry", xpos="far_left", ypos="head")
    gen "{size=-4}(Wait, do I really give a damn about that?){/size}" ("base", xpos="far_left", ypos="head")
    $ renpy.music.set_pause(False, channel="music")
    $ renpy.music.set_volume(1.0, 1.0)
    her "I'm sorry, but you left me no choice, professor."

    her "Now, if you'll excuse me, I must get to my classes..."

    call her_walk(action="leave")

    call bld
    gen "...................." ("base", xpos="far_left", ypos="head")

    $ states.sna.busy = True # No point in calling him during the day.
    $ states.her.ev.intro.e2_complete = True

    jump end_hermione_event


### Snape Hangout Event 2 ###
# You scheme a plan to take down Hermione.

label ss_he_hermione_E2:
    call bld
    gen "......................." ("base", xpos="far_left", ypos="head")
    gen "Hermione Granger came by again..." ("base", xpos="far_left", ypos="head")
    sna "Don't mention the witch's name when I'm off-duty..." ("snape_01", ypos="head")
    sna "..............." ("snape_31")
    sna "Dammit! I am a grown man, Albus!" ("snape_08")
    gen "My name is not--" ("base", xpos="far_left", ypos="head")
    sna "An esteemed wizard..." ("snape_08")
    gen "Well, alright, let it out..." ("base", xpos="far_left", ypos="head")
    sna "How come one tiny... cunt, is able to cause me so much grief?!" ("snape_31")
    sna "I thought with you as my ally I will have a chance to--" ("snape_32")
    gen "To unclench?" ("base", xpos="far_left", ypos="head")
    sna "Yeah, that could be the word..." ("snape_31")
    sna "But all I did was give her more leverage to harass me with..." ("snape_43")
    sna "She's even turning the teachers against me now..." ("snape_43")
    sna "................." ("snape_08")
    sna "She must go..." ("snape_35")
    gen "What do you mean?" ("base", xpos="far_left", ypos="head")
    with hpunch
    sna "{size=+6}We have to get rid of her!{/size}" ("snape_33")
    gen "Like, literally?" ("angry", xpos="far_left", ypos="head")
    sna "Do I have any other choice?" ("snape_34")
    gen "You're joking, right?" ("base", xpos="far_left", ypos="head")
    sna "Do I look like I'm joking?" ("snape_34")
    sna "Can you do this for me?" ("snape_39")
    gen "*Ehm*..." ("base", xpos="far_left", ypos="head")
    gen "Even if I agreed to murdering someone..." ("base", xpos="far_left", ypos="head")
    gen "Genies can't kill..." ("base", xpos="far_left", ypos="head")
    sna "Rats!" ("snape_35")
    gen "And we frown upon murderers..." ("base", xpos="far_left", ypos="head")
    if states.her.ev.intro.masturbated:
        sna "Really? I thought you didn't give a fuck..." ("snape_44")
        gen "to a certain degree..." ("base", xpos="far_left", ypos="head")
        gen "I don't mind swinging my \"sword\" in front of the girl--" ("base", xpos="far_left", ypos="head")
        gen "--but stabbing her with one is another thing." ("base", xpos="far_left", ypos="head")
        sna "............." ("snape_35")
    sna "Well... don't mind me then..." ("snape_31")
    sna "I'm all talk..." ("snape_31")
    sna "I would never cause harm to one of my students..." ("snape_31")
    sna "(... permanently, that is.)" ("snape_08")
    gen "Listen, if she bugs you so much, why not just find a less radical way to deal with her?" ("base", xpos="far_left", ypos="head")
    sna "Nah... Flogging has been outlawed for years now..." ("snape_35")
    gen "That's not what I mean..." ("base", xpos="far_left", ypos="head")
    sna "*Huh*?" ("snape_01")
    gen "She is a top student, right?" ("base", xpos="far_left", ypos="head")
    sna "Yes, damn her. The girl is a hard worker, I will give her that." ("snape_31")
    gen "She also has a reputation for being self-righteous." ("base", xpos="far_left", ypos="head")
    sna "Oh, yes!" ("snape_34")
    gen "And she thinks that she is better than everyone else..." ("base", xpos="far_left", ypos="head")
    sna "Where are you going with this?" ("snape_44")
    gen "Well, it seems like all of her power comes from her reputation and good grades..." ("base", xpos="far_left", ypos="head")
    sna "......................?" ("snape_39")
    gen "What if we take that away from her?" ("base", xpos="far_left", ypos="head")
    sna "That would shut her up I suppose..." ("snape_38")
    sna "But how? She's practically a saint--" ("snape_31")
    sna "Even students who hate her secretly admire her." ("snape_35")
    sna "She hasn't failed a single test in her entire time here...--" ("snape_31")
    sna "She is always way ahead of schedule..." ("snape_31")
    sna "Damn, how I hate it when she corrects me during my classes..." ("snape_08")
    sna "And thanks to her the Gryffindor house is way ahead of everybody else now..." ("snape_34")
    sna "It's only a matter of time before they win the house cup..." ("snape_34")
    gen "(Students fighting for imaginary points... That sure seems like a normal school.)" ("base", xpos="far_left", ypos="head")
    sna "Even Slytherin is no match for them this year..." ("snape_35")
    sna "........................" ("snape_43")
    sna "Dammit... I need more wine..." ("snape_34")
    gen "The wine can wait. Hear me out!" ("base", xpos="far_left", ypos="head")
    sna "*Huh*...?" ("snape_01")
    gen "*Hmm*... Let us..." ("base", xpos="far_left", ypos="head")

    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False

    label .choices:

    menu:
        gen "..." ("base", xpos="far_left", ypos="head")
        "{size=-3}\"Make sure she is not a top student any longer!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            sna "What? You mean grade her unfairly?" ("snape_01")
            sna "Nah... Dumbledore would never allow--" ("snape_31")
            sna "Wait a second!" ("snape_37")
            gen "Exactly!" ("base", xpos="far_left", ypos="head")
            sna "You're right! I can grade her tests unfairly! I could even persuade other teachers to do the same!" ("snape_02")
            sna "I could say that the order comes from you..." ("snape_02")
            sna "And when the real Dumbledore shows up, I will pretend that I had no idea that he was away..." ("snape_45")
            gen "Works for me." ("base", xpos="far_left", ypos="head")
            sna "*Err*..." ("snape_38")
            sna "This is still you, genie, right?" ("snape_38")
            gen "Yeah, yeah, still here..." ("base", xpos="far_left", ypos="head")
            sna "OK, good." ("snape_02")

        "{size=-3}\"Make sure Gryffindor loses the cup this year!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            sna "You mean to just start subtracting points from them for no good reason?" ("snape_01")
            sna "Oh, I like that!" ("snape_02")
            sna "There are a couple of Slytherin girls who are long overdue for receiving some extra house points as well." ("snape_46")
            sna "Oh, this will work out magnificently!" ("snape_45")
            sna "You are a Genius!" ("snape_02")
            gen "Yes, I am a genius genie. What are the odds of that..." ("base", xpos="far_left", ypos="head")

        "{size=-3}\"Ruin her reputation!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            sna "Tarnish her reputation?" ("snape_01")
            sna "But the girl is incorruptible..." ("snape_01")
            gen "Nonsense!" ("base", xpos="far_left", ypos="head")
            gen "All we need to do is convince her that she needs to make some sacrifices \"for the greater good\"." ("base", xpos="far_left", ypos="head")
            sna "Oh, but of course..." ("snape_37")
            sna "She would gladly \"Get her hands dirty\" to save the honour of her precious Gryffindor house!" ("snape_47")
            sna "And when she does, we will have the leverage we need..." ("snape_37")

    if d_flag_01 and d_flag_02 and d_flag_03:
        pass
    else:
        gen "Nextly--" ("base", xpos="far_left", ypos="head")
        jump ss_he_hermione_E2.choices

    sna "This could actually work!" ("snape_37")
    gen "I think so too." ("base", xpos="far_left", ypos="head")
    sna "Oh, I feel so alive tonight!" ("snape_45")
    sna "Pour me another goblet!" ("snape_28")
    sna "Potions class will start late tomorrow!" ("snape_45")
    gen "Although....." ("base", xpos="far_left", ypos="head")
    gen "I do feel like the measures are a little severe." ("base", xpos="far_left", ypos="head")
    gen "I mean, she's just a girl..." ("base", xpos="far_left", ypos="head")
    sna "Just a girl?" ("snape_36")
    sna "Oh no, no, no..." ("snape_36")
    sna "She is the embodiment of pure evil!" ("snape_32")
    sna "If we don't do this now..." ("snape_31")
    sna "One of these days I may just snap and {i}Avada Kedavra{/i} her!" ("snape_08")
    gen "You'll do what?" ("base", xpos="far_left", ypos="head")
    sna "Murder her for real!" ("snape_32")
    gen "Alright, alright... got it." ("base", xpos="far_left", ypos="head")
    gen "Let's choose the lesser of two evils then." ("base", xpos="far_left", ypos="head")
    sna "Yes..." ("snape_35")
    sna "Now, pour me some more wine." ("snape_34")

    nar "You spend the rest of the evening in Snape's company drinking your worries away."

    $ states.sna.ev.hangouts.hermione_e2 = True
    $ ss_event_pause += 1
    $ chair_OBJ.hidden = False

    jump end_snape_hangout_points

### Event 3 ###
# Third visit, after second special date with Snape.
# Hermione complains that she almost failed a test. (EVENING EVENT!)

label hermione_intro_E3:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*!"

    her "Professor, I'm coming in!"
    gen "...." ("base", xpos="far_left", ypos="head")

    call her_walk(action="enter", xpos="mid", ypos="base")
    pause.5

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "" ("annoyed", "squint", "angry", "mid", xpos="base", ypos="base")
    call ctc

    her "Good evening, Professor." ("annoyed", "narrow", "angry", "R")

    menu:
        "-stare full of hatred-":
            her "You can stare at me all you want, sir." ("normal", "squint", "angry", "mid")
            her "It will not make the problems of this school go away."
        "-sigh of exasperation-":
            her "Is this a bad time?" ("normal", "base", "base", "mid")
            her "Well, since I'm already here..." ("open", "base", "base", "mid")
        "\"....................................\"":
            her "Professor?" ("open", "base", "base", "mid")
            gen "Yes, yes..." ("base", xpos="far_left", ypos="head")

    her "Something... bizarre has happened today..." ("open", "closed", "angry", "mid")
    her "I'm not sure how to describe this..." ("normal", "squint", "angry", "mid")
    her "................................" ("annoyed", "squint", "angry", "mid")
    her "I think I almost failed a test..." ("annoyed", "narrow", "angry", "R")

    menu:
        "\"That happens to students sometimes.\"":
            her "To other students, yes. But not to me, sir!" ("annoyed", "narrow", "angry", "R")
            her "Never to me..." ("soft", "base", "base", "R")
        "{size=-5}\"Way to go, Snape!\"{/size}":
            her "Excuse me?" ("normal", "base", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            gen "Oh, I said, that's too bad. How are you holding up?" ("base", xpos="far_left", ypos="head")
            her "................." ("normal", "squint", "angry", "mid")
        "\"So, why tell me?\"":
            her "Because... this is not an ordinary event!"

    her "I'm not sure what is going on here..."
    gen "An evil scheme against you, miss Granger?" ("base", xpos="far_left", ypos="head")
    her "This is not a laughing matter, Sir." ("normal", "base", "angry", "mid")
    her "You should consider me a \"measuring stick\" for our educational system." ("open", "closed", "angry", "mid")
    her "If I \"almost\" fail a test, the rest of the students will definitely fail it."
    gen "Is that so...?" ("base", xpos="far_left", ypos="head")
    her "Yes, professor. Something went terribly wrong today..." ("normal", "squint", "angry", "mid")
    her "................................." ("annoyed", "narrow", "angry", "R")
    her "But what if it didn't?" ("open", "base", "worried", "mid")
    her "What if all the tests will be this difficult from now on?"

    menu:
        "\"You should study more, girl!\"":
            her @ tears soft "But I studied all night for this test!" ("upset", "base", "base", "mid")
        "\"There, there... It'll be alright.\"":
            her @ tears soft_blink "No it won't! This is a catastrophe!" ("mad", "happyCl", "worried", "mid")

    her @ tears soft "And the worst part is that I think I might be the only one who failed... Well... {i}Almost failed{/i}." ("angry", "base", "base", "mid")
    her @ tears soft "How will this make me look?" ("angry", "base", "base", "mid")
    her @ tears soft "I will know for sure when we get the results though..." ("normal", "base", "base", "R")
    her "Yes, I'm sure everyone else failed as well..." ("soft", "base", "base", "R")
    her "I mean, they must have, right?" ("open", "base", "worried", "mid")
    her "....................." ("soft", "base", "base", "R")
    her ".... right?" ("open", "base", "worried", "mid")

    $ d_flag_01 = False

    label .choices:
    menu:
        "{size=-3}\"Of course. You are a top student, after all.\"{/size}":
            her "Exactly..." ("annoyed", "squint", "angry", "mid")
            her "Or at least I used to be until today..."
            her @ tears soft_blink "I cannot believe this is happening!" ("mad", "happyCl", "worried", "mid")
        "{size=-3}\"You could prepare better if I were to tutor you.\"{/size}":
            $ states.her.ev.tutoring.offered = True
            her "*Hmm*..." ("annoyed", "squint", "base", "mid")
            her "Yes, that could help I suppose..." ("soft", "base", "base", "R")
            her "I appreciate your offer, professor, but..." ("open", "base", "base", "mid")
            her "The best tutor is a book, and I have the entire Hogwarts library at my disposal." ("open", "closed", "base", "mid")
            her "I don't think it would be necessary, sir. But..." ("soft", "base", "base", "mid")
            her "May I think about it?"
            gen "Don't take too long..." ("base", xpos="far_left", ypos="head")
        "{size=-3}\"I suppose we'll know soon enough.\"{/size}":
            her "Yes, I suppose we will..." ("soft", "base", "base", "mid")
        "{size=-3}\"You need to put my cock in your mouth.\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            gen "You need to put my co--" ("base", xpos="far_left", ypos="head")
            her "*huh*?" ("soft", "base", "base", "mid")
            gen "{size=-4}(No, I can't actually say that...){/size}" ("base", xpos="far_left", ypos="head")
            her "......?" ("annoyed", "squint", "base", "mid")
            jump hermione_intro_E3.choices

    gen "............" ("base", xpos="far_left", ypos="head")
    her "I'm sorry, professor, I'm probably just overreacting anyway..." ("grin", "happyCl", "worried", "mid", emote="sweat")
    her "But you must understand that my reputation is at stake here!" ("open", "base", "base", "mid")
    her "There's gotta be something wrong with the test..." ("annoyed", "narrow", "angry", "R")
    her "And although the entire class might have failed, I probably still got the most points on the test..."
    her "As usual..."
    her "Well, I'd better go now. We have another \"MRM\" meeting today." ("open", "closed", "angry", "mid")
    her "I will let you know about the new ideas we come up with."
    gen "I can hardly wait..." ("base", xpos="far_left", ypos="head")
    her "Well, if there is nothing else, I have a studying schedule to keep." ("open", "closed", "base", "mid")
    gen "By all means..." ("base", xpos="far_left", ypos="head")

    call her_walk(action="leave")

    $ states.sna.busy = False
    $ hg_event_pause += 1
    $ states.her.ev.intro.e3_complete = True

    jump end_hermione_event

### Event 4 ###
# Hermione complains that she did fail the test. (EVENING EVENT!)

label hermione_intro_E4:
    stop music fadeout 1.0

    # Gryffindor gets shafted by Snape and has 50% of Slytherin's points.
    $ gryffindor = int(slytherin*0.5)
    call update_ui_points

    # Wear default outfit. She's in shock so she didn't change.
    $ hermione.equip(her_outfit_default)

    call her_walk(action="enter", xpos="mid", ypos="base")

    call bld
    her "....................."
    gen "???" ("base", xpos="far_left", ypos="head")

    call her_walk("desk", "base")

    call bld
    her "............"
    gen "Miss Granger?" ("base", xpos="far_left", ypos="head")
    her "..............................."
    gen "Miss Granger?!!" ("base", xpos="far_left", ypos="head")

    her @ tears mascara "" ("upset", "narrow", "base", "stare", xpos="right", ypos="base")
    call ctc

    her @ tears mascara "*Huh*?" ("upset", "narrow", "base", "mid")
    her @ tears mascara "Oh, I'm already here?" ("upset", "narrow", "base", "L")
    her @ tears mascara "I'm sorry, sir... I..." ("upset", "narrow", "base", "down")
    her @ tears mascara ".................." ("angry", "narrow", "base", "down")
    her @ tears mascara "It seems that I did..." ("angry", "happyCl", "base", "dead")
    her @ tears mascara "I did... *Ehm*..." ("normal", "happyCl", "base", "dead")
    her @ tears mascara "... I failed that test after all." ("open", "happyCl", "base", "dead")
    her @ tears mascara "On top of that I... caused my house to lose a lot of points..." ("disgust", "narrow", "base", "down")
    her @ tears mascara_soft_blink "I'm sorry, professor..." ("upset", "happyCl", "worried", "mid")
    her @ tears tears_mascara_crying_blink "I'm not sure why I'm here..." ("upset", "happyCl", "worried", "mid")
    her @ tears mascara_soft_blink "I think I'd better go..." ("angry", "happyCl", "worried", "mid")
    her @ tears tears_mascara_crying_blink "..................." ("angry", "happyCl", "worried", "mid")

    call her_walk(action="run", xpos="door", speed=2, reduce=True)
    call her_chibi("leave")

    call bld
    gen "............." ("base", xpos="far_left", ypos="head")
    gen "She will be alright..." ("base", xpos="far_left", ypos="head")
    gen "I think..." ("base", xpos="far_left", ypos="head")

    $ states.her.ev.intro.e4_complete = True

    jump end_hermione_event

### Event 5 ###
# Hermione comes after her breakdown (when she failed the test).
# She is asking for tutoring.
# Tutoring unlocked!

label hermione_intro_E5:
    stop music fadeout 1.0

    call her_walk(action="enter", xpos="desk", ypos="base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed
    her "Good morning, Professor." ("base", "base", "base", "mid", xpos="right", ypos="base", trans=d3)
    gen "(So She doesn't even bother to knock anymore?)" ("base", xpos="far_left", ypos="head")
    gen "How can I help you today, miss Granger?" ("base", xpos="far_left", ypos="head")
    her "Well, first of all, I am terribly sorry about yesterday's display, sir..." ("open", "closed", "angry", "mid")
    her "I've never failed a test in my life, so I wasn't sure how to react..." ("open", "squint", "base", "mid")
    her "But I'm all better now..." ("open", "closed", "angry", "mid")

    menu:
        "\"Glad to hear it.\"":
            pass
        "\".........\"":
            pass

    her "I will not take much of your time, I promise..."

    if states.her.ev.tutoring.offered:
        her "I am here to take you up on your offer."

        menu:
            "\"What offer?\"":
                her "A while back you offered to tutor me, sir..."
                menu:
                    "\"Oh... That offer has expired.\"":
                        her "It..." ("open", "base", "base", "mid")
                        her "Expired, sir?" ("angry", "base", "base", "mid")
                        her "B-but..." ("open", "base", "worried", "mid")
                        her "But I require tutoring, and you are the smartest wizard I know..." ("annoyed", "base", "worried", "mid")
                        her "Please, sir. I really need your help." ("angry", "base", "worried", "mid")
                        menu:
                            "\"Show me your tits, and it's a deal!\"":
                                her "M-my...?" ("shock", "wide", "base", "stare")
                                her "............" ("angry", "base", "angry", "mid")
                                her "....."
                                with hpunch
                                her "{size=+5}Professor Dumbledore!!!{/size}" ("scream", "closed", "angry", "mid")
                                gen "{size=-5}(Well, at least I tried...){/size}" ("base", xpos="far_left", ypos="head")
                                her "I am not some Slytherin floozy!"
                                gen "Of course not, miss Granger." ("base", xpos="far_left", ypos="head")
                                gen "It was a test...{w=0.5} You passed. Good job." ("base", xpos="far_left", ypos="head")
                                her "What...?" ("open", "base", "base", "mid")
                                her "Oh, of course. I'm so silly sometimes. Sorry about the yelling, sir." ("grin", "happyCl", "worried", "mid", emote="sweat")
                                gen "My offer is still valid. If you want me to, then I can tutor you." ("base", xpos="far_left", ypos="head")
                                her ".............." ("annoyed", "base", "worried", "R")
                            "\"Well, alright, alright...\"":
                                pass
                    "\"Oh, that's right. Great.\"":
                        pass

            "\"Splendid! Starting today?\"":
                pass
    else:
        her "I... *Ehm*..." ("normal", "squint", "angry", "mid")
        her "Sir, I hope this is not too much to ask..."
        gen "Yes?" ("base", xpos="far_left", ypos="head")
        her "*Ehm*... would it be alright if..."
        her "..............."
        her "do You think you could tutor me a little, sir?" ("annoyed", "squint", "angry", "mid")
        menu:
            "\"I suppose that is possible.\"":
                pass
            "\"*Hmm*... I'm quite busy, actually.\"":
                her "Sir, please, you are the smartest wizard I know!" ("open", "base", "worried", "mid")
                gen "{size=-4}(You have no idea, little witch.){/size}" ("base", xpos="far_left", ypos="head")
                gen "Well, it could be arranged, I suppose..." ("base", xpos="far_left", ypos="head")

    her "Thank you, sir. I am very grateful." ("base", "base", "base", "mid")
    her "Just let me know when, and I will bring my books!" ("open", "closed", "base", "mid")
    her "I must study even harder from now on..." ("annoyed", "squint", "angry", "mid")
    her "And I'll be taking private lessons from you, sir, as often as possible." ("base", "base", "base", "mid")
    her "But that's not all..." ("normal", "squint", "angry", "mid")
    her "The \"MRM\" shall investigate our education system much closer now..."
    her "I think some sort of foul play might be taking place..."
    gen "*Exaggerated gasp* No way!" ("base", xpos="far_left", ypos="head")
    her "I have a list of suspects already, but I will get back to you on this later..."
    gen "*Ehm*... Alright..." ("base", xpos="far_left", ypos="head")
    her "Oh, my classes are about to start. I'd better go..." ("open", "base", "worried", "R")
    her "Good day to you, sir." ("base", "happyCl", "base", "mid")

    call her_walk(action="leave")

    stop music fadeout 1.0

    $ states.her.unlocked = True
    $ achievements.unlock("unlockher", True)
    call popup("{size=-4}You can now summon Hermione into your office.{/size}", "Character unlocked!", "interface/icons/head/hermione.webp")

    $ states.her.ev.tutoring.unlocked = True

    $ states.her.ev.intro.e5_complete = True #Allows next event to start.
    $ hg_event_pause += 2

    jump end_hermione_event

### Tonks Hangout Event ###
# Tonks will help convince Hermione to buy favours.

label nt_he_hermione_E1:
    ton "So, what did Severus think about me joining you on your little scheme?" ("open", "base", "base", "mid", ypos="head", flip=False)

    if not states.sna.ev.hangouts.tonks_e2: # You haven't talked to Snape yet.
        gen "Oh, I haven't told him yet." ("base", xpos="far_left", ypos="head")
        ton "You haven't told him?" ("open", "narrow", "raised", "mid")
        gen "Not yet." ("base", xpos="far_left", ypos="head")
        ton "Why you better let him know then... I wouldn't want to step on any toes..." ("annoyed", "base", "raised", "down") # looks down
        nar "Tonks moves her gaze towards your feet."
        ton @ hair horny "Unless that's something you're into..." ("horny", "narrow", "base", "mid") # looks at Genie
        play sound "sounds/gulp.ogg"#Genie gulps
        gen "..." ("angry", xpos="far_left", ypos="head")
        if game.daytime:
            nar "You spend the afternoon talking about how big your feet are, and its implications..."
        else:
            nar "You spend the evening talking about how big your feet are, and its implications..."
        call notes
        nar "You feel a faint bond forming between you two..."

        #Event fails
        jump end_tonks_hangout_points

    gen "Oh, he couldn't believe it." ("base", xpos="far_left", ypos="head")
    ton "That thrilled, was he?" ("open", "base", "raised", "mid")
    ton "Now that's surprising." ("annoyed", "base", "base", "R")
    gen "No, he literally couldn't believe it... He thought I was lying at first." ("base", xpos="far_left", ypos="head")
    gen "Although after he stopped laughing like a maniac..." ("base", xpos="far_left", ypos="head")
    gen "He did figure out quite quickly that the ministry probably wouldn't have sent a full-fledged Auror for a minor case like this one." ("base", xpos="far_left", ypos="head")
    ton "Well, what can I say... I'm an open book." ("base", "happyCl", "base", "mid")
    ton "I'm sure you'll both find out the benefits of having me around soon enough..." ("horny", "narrow", "base", "R")
    gen "I'm sure..." ("base", xpos="far_left", ypos="head")
    ton "So, is that Granger girl causing you two trouble?" ("open", "base", "base", "mid")
    gen "Quite a bit. She's not too thrilled on the idea of favour trading." ("base", xpos="far_left", ypos="head")
    ton "Maybe I can be of help with her?" ("base", "base", "base", "mid")
    ton "I can be very convincing." ("horny", "narrow", "annoyed", "mid")
    gen "What are you suggesting?" ("base", xpos="far_left", ypos="head")
    ton "To persuade her into giving it a try before being judgemental, for a start..." ("open", "base", "base", "R")
    ton "Convince her that trading favours isn't all bad." ("base", "base", "base", "mid")
    gen "That would indeed be very helpful. She's stubborn in that regard." ("base", xpos="far_left", ypos="head")
    ton "You don't have to tell me. She's been lecturing me about those \"sexual favours\" since the very day I got here..." ("upset", "base", "base", "R")
    ton "But I shouldn't complain about that..." ("open", "closed", "base", "mid")
    ton @ hair horny "Hearing those naughty words spill out of her gorgeous little mouth really gets me going!" ("soft", "narrow", "base", "R")
    gen "I can imagine so." ("grin", xpos="far_left", ypos="head")
    ton "When she describes all the wrongdoings of those \"filthy Slytherin girls\"..." ("soft", "base", "shocked", "stare")
    ton "How could I possibly get tired of that!" ("crooked_smile", "narrow", "base", "stare")
    ton "I'm very glad I decided to join you two." ("open", "base", "base", "down")
    ton "As an Auror It's just constant busy work..." ("open", "base", "raised", "mid")
    ton "Not to mention the hours." ("mad", "base", "base", "down")
    ton "And the mortality rate..." ("upset", "base", "worried", "R")
    ton "If I had known the benefits of being a teacher at Hogwarts, I would have signed up straight away!" ("horny", "base", "base", "up")

    if game.daytime:
        nar "You spend the afternoon conspiring against Hermione with Tonks..."
    else:
        nar "You spend the evening conspiring against Hermione with Tonks..."
    call notes
    nar "You feel a faint bond forming between you two..."

    $ states.her.ev.intro.convinced = True
    $ states.ton.ev.hangouts.hermione_e1 = True

    jump end_tonks_hangout_points

### Event 6 ###
# Hermione comes and asks to buy a favour from her.

label hermione_intro_E6:
    stop music fadeout 1.0
    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock!*"

    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger."
            gen "(It's that witch again...)" ("base", xpos="far_left", ypos="head")
            her "Can I come in, sir?"
            menu:
                gen "..." ("base", xpos="far_left", ypos="head")
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    $ achievements.unlock("knock")
                    $ hg_event_pause += 1

                    call music_block
                    jump main_room_menu

                "\"Of course. Come on in.\"":
                    pass

        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well, alright..."
            $ achievements.unlock("knock")
            $ hg_event_pause += 1

            call music_block
            jump main_room_menu

        "\"Yes, come in.\"":
            pass

        "\"...................................\"":
            play sound "sounds/knocking.ogg"
            "*Knock-knock-knock!*"
            gen "............................." ("base", xpos="far_left", ypos="head")
            her "Professor, I'm coming in..."
            gen "{size=-4}(Crap!){/size}" ("base", xpos="far_left", ypos="head")

    call her_walk(action="enter", xpos="mid", ypos="base")

    play music "music/Chipper Doodle v2.ogg" fadein 1 if_changed

    her "Good day, professor..." ("soft", "base", "base", "R", xpos="base", ypos="base", trans=d3)
    her "........................"
    her "........................" ("annoyed", "base", "worried", "R")
    her "........................"
    her "*Ehm*......" ("open", "base", "base", "mid")
    her "................." ("annoyed", "base", "worried", "R")
    gen "What is it, miss Granger?" ("base", xpos="far_left", ypos="head")
    her "Well... *Ehm*." ("open", "base", "base", "mid")

    if not is_in_lead(gryffindor):
        her "You see... The Gryffindor house is not in the lead anymore..." ("open", "base", "worried", "R")
    else:
        her "You see... The Gryffindor house is struggling with points..." ("open", "base", "worried", "R")

    her "And... everyone is working so hard..." ("annoyed", "base", "worried", "R")
    her "And they look up to me for help, but I don't know what to do..." ("disgust", "base", "worried", "down")
    gen "............................" ("base", xpos="far_left", ypos="head")
    her "Professor Dumbledore..." ("open", "base", "worried", "mid")

    $ renpy.music.set_volume(0.0, 1.0)
    pause 1.0
    $ renpy.music.set_pause(True, channel="music")
    her "I want you to buy a favour from me!" ("open", "happyCl", "worried", "mid")
    her "" ("normal", "happyCl", "worried", "mid")
    gen "(What in the...?!)" ("angry", xpos="far_left", ypos="head")
    $ renpy.music.set_pause(False, channel="music")
    $ renpy.music.set_volume(1.0, 1.0)

    gen "(Way to go Tonks!)" ("grin", xpos="far_left", ypos="head")

    menu:
        "\"You mean like a sexual favour?\"":
            her "*Ehm*... I'm not sure..." ("angry", "wink", "worried", "mid", emote="sweat")
            her "The kind that would gain our house additional points..."
            her "I could write an essay for you or..." ("open", "base", "worried", "R")
            her "Or maybe clean your tower...?" ("angry", "wink", "worried", "mid", emote="sweat")
            gen "{size=-4}(Clean my tower? Heh... There's gotta be a dirty joke in there somewhere...){/size}" ("base", xpos="far_left", ypos="head")
            gen "Well, alright then, I think we can figure something out." ("base", xpos="far_left", ypos="head")
        "\"Well, if you insist...\"":
            pass
        "\"I don't think so, miss Granger.\"":
            her "B-but... We need the points..." ("open", "base", "worried", "mid")
            her "Professor, please, I am really desperate..." ("open", "squint", "low", "mid")
            gen "Desperate you say...?" ("base", xpos="far_left", ypos="head")
            gen "Well, alright..." ("base", xpos="far_left", ypos="head")

    her "Really?" ("silly", "base", "base", "mid")
    her "Thank you, professor..." ("base", "happyCl", "base", "mid")
    her "So... What will it be?" ("base", "base", "base", "mid")

    $ d_flag_01 = False

    label .choices:
    $ current_favor = ""

    menu:
        "\"Show me your tongue...\"":
            $ current_favor = "show_tongue"
        "\"Stand there. Let me look at you\"":
            $ current_favor = "stand_there"
        "\"Make a silly face...\"":
            $ current_favor = "silly_face"
        "\"Say 'I've been a bad girl'\"":
            $ current_favor = "bad_girl"
        "\"Blow me\"" if not d_flag_01:
            $ d_flag_01 = True
            gen "(*heh*, if only that worked...)" ("grin", xpos="far_left", ypos="head")
            gen "(I don't think she's ready for that just yet.)" ("base", xpos="far_left", ypos="head")
            gen "(Let's start with something simpler.)" ("base", xpos="far_left", ypos="head")
            jump hermione_intro_E6.choices

    her "*Ehm*..." ("angry", "base", "base", "mid")
    her "How many house points will I get for that...?" ("angry", "wink", "base", "mid")

    menu:
        "\"One point.\"":
            if not current_favor in ["show_tongue", "stand_there"]:
                her "I don't think it's worth it then..." ("annoyed", "base", "worried", "mid")
                jump hermione_intro_E6.choices
            $ current_payout = 1
        "\"Five points.\"":
            if not current_favor in ["show_tongue", "stand_there", "silly_face"]:
                her "I don't think it's worth it then..." ("annoyed", "base", "worried", "mid")
                jump hermione_intro_E6.choices
            $ current_payout = 5
        "\"Ten points.\"":
            her "(So little...?)" ("annoyed", "base", "worried", "down")
            $ current_payout = 10
        "\"Twenty points.\"":
            her "(Wow. That's quite a lot for such a simple request...)" ("base", "base", "base", "mid")
            $ current_payout = 20

    her "*Ehm*, alright..." (xpos="mid", ypos="base", trans=fade)

    if current_favor == "show_tongue":
        her "M-my... tongue, sir?" ("grin", "happyCl", "worried", "mid", emote="sweat")
        gen "Yes, girl. Open your mouth, and show me your tongue." ("base", xpos="far_left", ypos="head")
        her "{size=-4}(What an odd request...){/size}" ("annoyed", "narrow", "angry", "R")
        her "*Ehm*... well, alright then..." ("soft", "squint", "worried", "mid")
        her "Here..." ("open", "squint", "base", "mid")
        her "............." ("open_tongue", "narrow", "base", "mid_soft")
        her "............." ("open_tongue", "narrow", "base", "L")
        her "................." ("open_tongue", "narrow", "angry", "R")

        menu:
            "\"Very good. Here are your points.\"":
                pass
            "\"Not good enough. You can do better\"":
                her "..............." ("annoyed", "narrow", "angry", "R")
                her "Alright, I will try to do better, sir..." ("open", "closed", "angry", "R")
                her "How about this?" ("open", "base", "worried", "mid")
                her "*A-a-ah*........." ("scream", "base", "base", "R")
                her "............................" ("open_wide_tongue", "happy", "base", "R")
                her "......................................" ("open_wide_tongue", "narrow", "base", "down")
                her "...................................................................."
                her "......................................................................................................." ("open_wide_tongue", "closed", "angry", "mid")
                her "*khow* *ish* *thish*?" ("open_wide_tongue", "base", "annoyed", "mid")

                menu:
                    "\"Good enough. Here, your points.\"":
                        pass
                    "\"Keep that mouth open.\"":
                        her "......." ("open_wide_tongue", "happy", "worried", "mid")
                        her "{size=-4}(My mouth is starting to hurt...){/size}" ("open_wide_tongue", "happy", "worried", "mid")
                        call ctc
                        gen "Alright, that's enough." ("base", xpos="far_left", ypos="head")
                        her "{size=-4}(Finally...){/size}" ("annoyed", "narrow", "base", "R")
    elif current_favor == "stand_there":
        her "So, I just have to stand here then...?" ("soft", "base", "base", "mid")

        $ d_flag_01 = "mid"
        $ d_flag_02 = 0

        label .stand_there_choices:

        if d_flag_02 >= 3:
            her "Professor, could you make up your mind already?!" ("angry", "base", "annoyed", "R", trans=dissolve)
            gen "Alright, alright, there's no need to get worked up about it, sheesh." ("base", xpos="far_left", ypos="head")
        else:
            menu:
                "\"No, come closer\"" if d_flag_01 == "mid":
                    $ d_flag_01 = "desk"
                    $ d_flag_02 += 1
                    her "*Ehm*... alright..."
                    call her_walk("desk", "base")

                    jump hermione_intro_E6.stand_there_choices
                "{size=-4}\"On second thought, go back to the middle\"{/size}" if d_flag_01 == "desk":
                    $ d_flag_01 = "mid"
                    $ d_flag_02 += 1
                    her "*Ehm*... alright..."
                    call her_walk("mid", "base")
                    call her_chibi("stand", flip=False)
                    with d3

                    jump hermione_intro_E6.stand_there_choices
                "\"Yes, stand right where you are.\"":
                    pass

        her "................................." ("annoyed", "base", "annoyed", "R", trans=d3)

        menu:
            gen "*Hmm*..." ("base", xpos="far_left", ypos="head")
            "\"Your attire suits you, miss Granger...\"":
                her @ cheeks blush "............" ("soft", "base", "base", "R")
                her @ cheeks blush "Thank you, professor..." ("open", "base", "base", "R")
                her @ cheeks blush "" ("base", "base", "base", "R")
            "\"You have a nice body, miss Granger...\"":
                her "!!?" ("soft", "wide", "base", "stare")
                her @ cheeks blush ".............." ("annoyed", "narrow", "angry", "R")
                her @ cheeks blush "Thank you, professor..."
            "\"That's enough. Here are your points...\"":
                jump hermione_intro_E6.end
    elif current_favor == "silly_face":
        her "A silly face then..." ("grin", "happyCl", "worried", "mid", emote="sweat")
        her "Let's see..."
        label .silly_face_choices:

        her "How about this one?" ("silly", "base", "base", "squint")

        menu:
            "\"Good! Very stupid! I mean, silly.\"":
                jump hermione_intro_E6.end
            "\"Not stupid enough.\"":
                pass

        her "........." ("annoyed", "narrow", "angry", "R")
        her "What about this one then?" ("disgust", "slit", "low", "stare")

        menu:
            "\"*Ha-ha*! You look like an idiot!\"":
                jump hermione_intro_E6.end
            "\"No, not stupid enough.\"":
                pass

        her "........." ("annoyed", "narrow", "angry", "R")
        her "What if I do it like this?" ("full", "slit", "worried", "ahegao")

        menu:
            "\"Good! Very stupid.\"":
                jump hermione_intro_E6.end
            "\"Not stupid enough.\"":
                pass

        her "........." ("annoyed", "narrow", "angry", "R")
        her "I give up..." ("upset", "narrow", "worried", "down")

        menu:
            "\"*Ha-ha-ha*, perfect!\"":
                her "What?" ("open", "base", "angry", "mid")
                her "But that's my normal face!" ("angry", "base", "angry", "mid")
                gen "*he-he-he* Don't get mad, [name_hermione_genie], I'm just messing with you." ("grin", xpos="far_left", ypos="head")
                gen "Although you look cute when you're upset." ("base", xpos="far_left", ypos="head")
                her @ cheeks blush "......." ("annoyed", "base", "worried", "R")
                jump hermione_intro_E6.end
            "\"Not stupid enough.\"":
                jump hermione_intro_E6.silly_face_choices
    elif current_favor == "bad_girl":
        her "I..." ("normal", "squint", "angry", "mid")
        her "I have been a very bad girl..." ("open", "squint", "angry", "R")
        gen "Have you been a very, very, very bad girl?" ("grin", xpos="far_left", ypos="head")
        her "*Umm*... Maybe?" ("grin", "wink", "worried", "mid")

        $ d_flag_01 = False

        label .bad_girl_choices:
        menu:
            gen "..." ("grin", xpos="far_left", ypos="head")
            "\"Do you need to be punished?\"":
                her "Do I need to... be punished?" ("open", "base", "worried", "mid")
                her "*Ehm*..." ("upset", "base", "base", "down")
                her "....................."
                her "Well, I am not perfect, if that's what you mean, sir..." ("annoyed", "narrow", "angry", "R")
                her "But do I need to be punished?" ("annoyed", "base", "base", "R")
                her "Is this really for me to decide...? I mean..." ("normal", "squint", "angry", "mid")
                her "What does this have to do with anything?" ("open", "squint", "angry", "mid")
                her "" ("normal", "squint", "angry", "mid")
                gen "You are overanalysing this, girl." ("base", xpos="far_left", ypos="head")
                gen "Just say that you need to be punished!" ("base", xpos="far_left", ypos="head")
                her "Fine. I need to be punished!" ("angry", "base", "angry", "mid")
                her "{size=-5}(And I truly do think so sometimes...){/size}" ("normal", "narrow", "worried", "down")
                gen "That's a good girl." ("base", xpos="far_left", ypos="head")
                her "................??" ("annoyed", "base", "base", "R")
                gen "Now that wasn't hard at all, was it?" ("base", xpos="far_left", ypos="head")
                her "N-no , sir, I guess not..." ("angry", "happyCl", "worried", "R")
                her "" ("annoyed", "base", "worried", "R")
                gen "Alright then..." ("base", xpos="far_left", ypos="head")
            "\"Do you want to get spanked?\"":
                her "Do I want to..." ("open", "base", "worried", "mid")
                her "Get s-spanked??" ("angry", "wide", "base", "stare")
                her "*Tsk*!" ("angry", "base", "angry", "mid")
                her "Professor, I don't think I'm comfortable with--" ("open", "closed", "angry", "mid")
                gen "Apologies, let me rephrase the question..." ("base", xpos="far_left", ypos="head")
                gen "How badly do you need those points?" ("base", xpos="far_left", ypos="head")
                her ".................." ("annoyed", "squint", "angry", "mid")
                her "Yes, sir. I do need to get spanked." ("open", "closed", "angry", "mid")
                gen "Alright, that's good enough for now..." ("base", xpos="far_left", ypos="head")
                her "{size=-4}(For now?){/size}" ("normal", "squint", "angry", "mid")
            "\"Bend over!\"" if not d_flag_01:
                $ d_flag_01 = True
                gen "{size=-5}(Too early for this... I need to reel her in first.){/size}" ("base", xpos="far_left", ypos="head")
                jump hermione_intro_E6.bad_girl_choices

    label .end:
        if current_payout == 1:
            gen "{number=current_payout} point to the Gryffindor house." ("base", xpos="far_left", ypos="head")
        else:
            gen "{number=current_payout} points to the Gryffindor house." ("base", xpos="far_left", ypos="head")
        $ gryffindor += current_payout

    her "..... Yay!......." ("grin", "happyCl", "worried", "mid", emote="sweat")
    her "This was quite easy..."
    her "Do you think you could buy some more favours from me in the future, professor?" ("grin", "wink", "worried", "mid")

    menu:
        "\"I don't think that's a good idea.\"":
            her "Please, professor..." ("angry", "base", "worried", "mid")
            her "We really need those points..."
            gen "......." ("base", xpos="far_left", ypos="head")
            her "You are an esteemed wizard and to be honest..." ("annoyed", "base", "worried", "R")
            her "The only person in this school whom I don't mind asking for this..."
            gen "Well, when you put it that way..." ("base", xpos="far_left", ypos="head")
        "\"That's a possibility...\"":
            pass

    her "Thank you, professor. Thank you so much!" ("smile", "happyCl", "base", "mid")
    her "Well... I suppose I'd better go now..." ("base", "base", "base", "mid")
    gen "............" ("base", xpos="far_left", ypos="head")

    call her_walk("door", "base")
    pause.3

    if current_favor == "show_tongue":
        her "{size=-4}(*Hmm*...){/size}" ("annoyed", "narrow", "worried", "down", xpos="far_right", ypos="head", flip=True, trans=d3)
        her "{size=-4}(Students show teachers their tongues all the time...){/size}" ("soft", "base", "base", "R")
        her "{size=-4}(Although that's usually when the teacher is not looking...){/size}" ("base", "narrow", "base", "R_soft")
        her "{size=-4}(But there is nothing wrong with what I did today...){/size}" ("annoyed", "base", "base", "L")
        her "{size=-4}(I earned my house extra points...){/size}" ("smile", "happyCl", "base", "mid")
    elif current_favor == "stand_there":
        her "{size=-4}(I can just stand there and let the professor look at me...){/size}" ("annoyed", "base", "base", "R", xpos="far_right", ypos="head", flip=True, trans=d3)
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}" ("base", "closed", "base", "mid")
    elif current_favor == "silly_face":
        her "{size=-4}(Stupid face...){/size}" ("silly", "base", "base", "squint", xpos="far_right", ypos="head", flip=True, trans=d3)
        her "{size=-4}(Stupid face...){/size}" ("disgust", "happy", "base", "squint")
        her "{size=-4}(I need to practise this.){/size}" ("base", "happyCl", "base", "mid")
    elif current_favor == "bad_girl":
        her "{size=-4}(I'm a bad girl...){/size}" ("angry", "base", "angry", "stare", xpos="far_right", ypos="head", flip=True, trans=d3)
        her "{size=-4}(I am a very bad girl...){/size}" ("base", "base", "angry", "stare")
        her "{size=-4}(Yes, I can say things like that easily...){/size}" ("smile", "happyCl", "base", "mid")
        her "{size=-4}(I guess I'm a born actress...){/size}" ("base", "happyCl", "base", "mid")

    call her_chibi("leave")
    with d3

    stop music fadeout 1.0

    call popup("You have unlocked the ability to buy sexual favours from Hermione.", "Congratulations!", "interface/icons/head/hermione.webp")

    $ states.her.wardrobe_unlocked = True
    $ states.her.favors_unlocked = True

    $ states.her.ev.intro.e6_complete = True

    jump end_hermione_event
