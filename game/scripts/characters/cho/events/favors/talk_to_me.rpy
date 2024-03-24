

### Cho Talks ###

label cc_pf_talk:

    if not _events_completed_any:
        gen "{size=-4}(All I'll do is have an innocent conversation with her...){/size}" ("base", xpos="far_left", ypos="head")

        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                $ _event.cancel()
                jump cho_favor_menu

    # Start Event
    return

    # End Event Jump
label end_cho_talk_event:

    if states.cho.tier == 1:
        if states.cho.level < 3: # Points til 3
            $ states.cho.level += 1

    elif states.cho.tier == 2:
        if states.cho.level < 9: # Points til 9
            $ states.cho.level += 1

    elif states.cho.tier == 2:
        if states.cho.level < 9: # Points til 9
            $ states.cho.level += 1

    elif states.cho.tier == 3: # Points til 15
        if states.cho.level < 15:
            $ states.cho.level += 1

    jump end_cho_event

### Tier 1 (pre Hufflepuff) ###

label cc_pf_talk_T1_intro_E1:

    call cc_pf_talk

    gen "Let's have a little chat shall we." ("base", xpos="far_left", ypos="head")
    cho "A chat, [name_genie_cho]?" ("open", "base", "raised", "mid")
    gen "Just to get to know each other a little bit better." ("grin", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]." ("smile", "base", "base", "mid")
    gen "First, I'd like you to come a bit closer." ("base", xpos="far_left", ypos="head")
    cho "Very well..." ("soft", "base", "base", "R")

    call cho_walk("desk", "base")
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=d3)
    call ctc

    cho "What would you like to talk about?" ("soft", "base", "base", "mid")
    gen "Do you have a boyfriend, Miss Chang?" ("base", xpos="far_left", ypos="head")
    cho "Excuse me?" ("open", "wide", "base", "mid", trans=hpunch) # Shocked
    gen "I asked if you have a boyfriend... Anybody you fool around with?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Me? sir? Ha--{w=0.4} hav--{w=0.4} a boyfriend?" ("open", "wide", "base", "R") # Reluctant, Embarassed
    gen "Or a girlfriend! That would be even better, now that I think about it!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Sir, that's--{w=0.3} that's not something a headmaster should be concerned about." ("soft", "happyCl", "worried", "L")
    cho @ cheeks blush "And I don't see how this information would be of importance for my training." ("open", "wide", "raised", "downR")
    cho @ cheeks blush "Why would it matter if--{w=0.5} Even if I did I'd--" ("soft", "wide", "base", "down")
    gen "So you don't have one?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "You're making me nervous, [name_genie_cho]. {heart}" ("horny", "narrow", "worried", "R")
    gen "(So cute.{w=0.5} Perhaps this is something I could push her further on...)" ("base", xpos="far_left", ypos="head")

    cho "Sir, I do not have a boyfriend at the moment." ("soft", "closed", "angry", "mid")
    cho "I hope that answers your question." ("annoyed", "narrow", "base", "mid")
    gen "So, a girlfriend then?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "!!!" ("angry", "wide", "raised", "mid")
    cho "No. Why would you even think that, [name_genie_cho]?!" ("open", "closed", "angry", "mid")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "(She doesn't seem that keen on the subject, perhaps I could tell her...)" ("base", xpos="far_left", ypos="head")

    label .choices:
    menu:
        "\"It's important to open up to your headmaster.\"":
            gen "Emphasis on \"opening up\"..." ("base", xpos="far_left", ypos="head")
            cho "I don't think that will be necessary, [name_genie_cho]." ("annoyed", "narrow", "angry", "mid")
            gen "There's a lot more to gather from discussing previous life choices than you might think." ("base", xpos="far_left", ypos="head")
            gen "You get to learn a lot about the way someone has matured by previous experiences..." ("base", xpos="far_left", ypos="head")
            gen "Like a first kiss, who it was with, and so on..." ("base", xpos="far_left", ypos="head")
            cho "You think I'm mature?" ("soft", "base", "base", "mid")
            gen "(That's what she's focusing on?)" ("angry", xpos="far_left", ypos="head")
            gen "*Ahem*, yes.{w=0.5} Of course you are, don't you think so?" ("base", xpos="far_left", ypos="head")
            cho "Well, my previous boyfriend didn't seem to think so..." ("open", "base", "raised", "R")
            gen "So you did have one?" ("base", xpos="far_left", ypos="head")
            cho "*Ugh*{w=0.8} Fine...{w=0.8} I'll tell you about him..." ("soft", "narrow", "base", "down")

            pass

        "\"It's okay if you like girls...\"":
            if states.cho.mood == 0:
                $ states.cho.mood += 1
            gen "Some people prefer to swing the other way..." ("base", xpos="far_left", ypos="head")
            cho "What?" ("angry", "wide", "base", "mid")
            gen "You know... When you prefer flicking the bean over rubbing a wand..." ("base", xpos="far_left", ypos="head")
            cho "*Uhm*, I never said I had a preference either way..." ("quiver", "narrow", "worried", "R")
            gen "So you have had a girlfriend?" ("base", xpos="far_left", ypos="head")
            cho "I'd rather not talk about it right now..." ("soft", "narrow", "worried", "mid")
            gen "(Damn, maybe that's not the way to go about this, maybe instead I could tell her...)" ("base", xpos="far_left", ypos="head")

            jump cc_pf_talk_T1_intro_E1.choices

        "\"In my previous relationships...\"":
            if states.cho.mood == 0:
                $ states.cho.mood += 1
            cho "Sir, I'd rather not hear a boring old tale about any of your old flames..." ("open", "narrow", "base", "R")
            gen "Oh they weren't boring at all!" ("grin", xpos="far_left", ypos="head")
            cho "*Hmm*?" ("annoyed", "narrow", "base", "mid")
            gen "They were very intimate..." ("grin", xpos="far_left", ypos="head")
            cho "???" ("annoyed", "base", "raised", "mid")
            gen "Very sexual!" ("angry", xpos="far_left", ypos="head")
            cho "!!!" ("annoyed", "wide", "base", "mid")
            gen "Lots of acrobatic stuff!" ("grin", xpos="far_left", ypos="head")
            cho "NO Sir, please!{w=0.5} I don't want to know any of that!" ("scream", "closed", "angry", "mid", trans=hpunch)
            cho "(Gross!{w=0.5} Keep it to yourself...)" ("angry", "narrow", "worried", "R")
            gen "I just wanted to expand my backstory a little bit...{w=0.5} What's so wrong with that..." ("base", xpos="far_left", ypos="head")

            jump cc_pf_talk_T1_intro_E1.choices

    # Cedric Diggory
    cho "Cedric Diggory was my boyfriend during the time Hogwarts was hosting the \"triwizards tournament\"." ("soft", "base", "base", "R")
    gen "(They host tournaments here? Interesting...)" ("base", xpos="far_left", ypos="head")
    cho "That year was the most fun I've ever had!" ("smile", "base", "base", "mid")
    gen "Was he that good?" ("base", xpos="far_left", ypos="head")
    cho "What?{w=0.5} No, Sir, not because of him!{w} The tourney, [name_genie_cho]!" ("soft", "narrow", "base", "mid")
    gen "Sure..." ("base", xpos="far_left", ypos="head")
    cho "We should have it every year if you were to ask me!" ("open", "closed", "base", "mid")
    gen "(A cosplay tournament is what this school needs...)" ("grin", xpos="far_left", ypos="head")
    cho "Sir, that would be great!" ("smile", "narrow", "base", "mid")
    gen "(Wait, wait!{w=0.8} A \"nude\" cosplay tournament!{w=0.6} Even better!)" ("angry", xpos="far_left", ypos="head")
    gen "(Is it even cosplay if they're naked?)" ("angry", xpos="far_left", ypos="head")
    cho "And with new contestants every month! You've got to do this, Sir!" ("smile", "base", "base", "mid")
    gen "I'll think about it..." ("base", xpos="far_left", ypos="head")

    gen "Now tell me, how come you two ended up together?" ("base", xpos="far_left", ypos="head")
    cho "Oh. Well..." ("soft", "base", "base", "down")
    cho "I have this thing for...{w=0.5} athletes." ("horny", "base", "base", "down")
    cho "Cedric was the representative champion of our school, so of course I had to date him." ("horny", "base", "worried", "down")
    gen "Of course..." ("base", xpos="far_left", ypos="head")
    gen "(She's into athletes, who could've guessed...)" ("base", xpos="far_left", ypos="head")
    gen "(You should see me, girl. I'm shredded!)" ("angry", xpos="far_left", ypos="head")
    gen "(Too bad you can only see the body of that wrinkly old geezer...)" ("base", xpos="far_left", ypos="head")
    gen "(Maybe there's like a steroid spell...)" ("base", xpos="far_left", ypos="head")
    gen "{size=-4}Plexus Maximus!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "Did you say something?" ("soft", "base", "raised", "mid")
    gen "Oh, it was nothing... go on." ("base", xpos="far_left", ypos="head")

    cho "Anyway, Cedric even put his life at risk during the whole thing." ("open", "base", "base", "R")
    gen "Oh you poor, poor thing..." ("base", xpos="far_left", ypos="head")
    gen "I can see why you didn't want to mention him before then..." ("base", xpos="far_left", ypos="head")
    cho "Why?" ("soft", "narrow", "raised", "mid")
    gen "He surely will be missed." ("base", xpos="far_left", ypos="head")
    cho "Sir?" ("angry", "narrow", "base", "mid")
    gen "Died just the way he lived...{w} as a plot device." ("base", xpos="far_left", ypos="head")
    cho "Sir, Cedric isn't dead." ("open", "narrow", "angry", "mid")
    gen "Oh...{w=0.3} he's not?" ("base", xpos="far_left", ypos="head")
    cho "No!" ("annoyed", "narrow", "angry", "mid")
    gen "I could've sworn I read that somewhere..." ("base", xpos="far_left", ypos="head")
    gen "Are you sure he's still around?{w=0.6} What if he {b}did{/b} die, but then he returned from the dead?" ("base", xpos="far_left", ypos="head")
    gen "For all you know, he could be a vampire!" ("angry", xpos="far_left", ypos="head")
    cho "Sir, you're talking nonsense..." ("annoyed", "narrow", "angry", "R")
    cho "Please don't joke about your student like that. It's so unlike you..." ("open", "closed", "base", "mid")
    cho "He's one of your bests! The best student Hufflepuff has ever seen!" ("open", "base", "base", "mid")
    gen "A Hufflepuff? Well, that explains everything..." ("base", xpos="far_left", ypos="head")
    gen "If he's such an exceptionally great student, then why aren't you two still together?" ("base", xpos="far_left", ypos="head")
    cho "Things didn't work out, naturally..." ("open", "base", "raised", "R")
    cho "The tourney ended, and he didn't win, so..." ("soft", "base", "raised", "down")
    gen "So you two broke up?... Because he didn't win?" ("base", xpos="far_left", ypos="head")
    cho "That was one of the reasons..." ("soft", "base", "base", "downR")
    cho "There is also the fact that he's on the Hufflepuff Quidditch team, as their Seeker." ("open", "base", "base", "mid")
    cho "It's our last shot at winning the Quidditch house cup, for the both of us." ("angry", "base", "base", "down")
    cho "We'd constantly be at each other's throats." ("soft", "narrow", "angry", "mid")
    gen "Intriguing!" ("angry", xpos="far_left", ypos="head")
    gen "You are missing out, girl..." ("base", xpos="far_left", ypos="head") # Small text
    gen "{size=-4}Hate-sex is the best!{/size}" ("grin", xpos="far_left", ypos="head") # Small text
    cho "I didn't quite hear that, Sir." ("base", "base", "base", "mid")
    gen "Who else did you do it with?" ("base", xpos="far_left", ypos="head")
    cho "Do it with?" ("soft", "narrow", "raised", "mid") # Shocked
    gen "Smooching, kissing, snogging...{w=0.8} whatever you call it nowadays..." ("base", xpos="far_left", ypos="head")
    cho "With all due respect sir, it's very odd that you'd ask me about these sorts of things..." ("open", "closed", "base", "mid")
    cho "But... you {b}are{/b} helping me.{w=0.8} So I guess I owe you that much..." ("annoyed", "base", "base", "R")
    gen "That's what I wanted to hear." ("grin", xpos="far_left", ypos="head")

    # Fleur
    cho "Well, Cedric wasn't the only one I was with during the year of the tourney..." ("open", "base", "raised", "down")
    gen "Is that so...{w} feel free to elaborate!" ("grin", xpos="far_left", ypos="head")
    cho "I was sort of dating somebody else..." ("soft", "base", "worried", "downR")
    cho "At the same time." ("horny", "base", "worried", "R") # Embarrassed
    gen "No{w} way!" ("base", xpos="far_left", ypos="head")
    gen "You were cheating on that {i}Hufflepuffer{/i}?" ("angry", xpos="far_left", ypos="head")
    cho "I wouldn't call it cheating, sir. It wasn't even that serious with Cedric to begin with." ("annoyed", "narrow", "base", "mid")
    cho "I had a unique opportunity, that's all..." ("soft", "base", "base", "R")
    cho "One of those \"no strings attached\" kind of things... Trying out new stuff..." ("smile", "base", "base", "downR")
    gen "Like what?" ("base", xpos="far_left", ypos="head")
    cho "Dating a girl, for example." ("base", "narrow", "base", "mid")
    gen "(Finally this is getting interesting!)" ("grin", xpos="far_left", ypos="head")
    cho "She was one of the students from Beauxbatons." ("soft", "base", "base", "downR")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    cho "A French girl." ("soft", "base", "base", "down")
    gen "I hope you {i}frenched{/i} that French girl!" ("grin", xpos="far_left", ypos="head")
    cho "*Ehm*..." ("angry", "closed", "worried", "mid") # Super embarrassed
    cho "(Why am I telling him this?)" ("horny", "narrow", "worried", "R")
    gen "Tell me more about this girl." ("base", xpos="far_left", ypos="head")
    gen "What's her name?" ("grin", xpos="far_left", ypos="head")
    cho "Fleur Delacour...{w} She was also a champion at the tourney." ("soft", "base", "worried", "mid")
    gen "I'm in shock!" ("angry", xpos="far_left", ypos="head")

    # Viktor
    cho "Then there also was Viktor Krum who--" ("open", "base", "base", "R")
    with hpunch
    gen "Slow down, girl! I'm still not over the fact that you made out with a girl!" ("angry", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "base", "mid")

    menu:
        "-Jerk off while she's talking-":
            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.masturbating = True

            hide cho_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

        "-Participate in the conversation-":
            $ states.gen.masturbating = False

    gen "I want to hear everything!" ("grin", xpos="far_left", ypos="head")

    cho "I'm sorry, Sir. It's just that..." ("open", "closed", "raised", "mid")

    if game.daytime:
        cho "I'm really late for classes. May we postpone this talk to some other time?" ("soft", "narrow", "worried", "R")
    else:
        cho "It's getting really late. May we postpone this talk to some other time?" ("soft", "narrow", "worried", "R")

    if states.gen.masturbating:
        gen "What? Please don't go now. I've only just started!" ("angry", xpos="far_left", ypos="head")
        cho "Started with what, [name_genie_cho]?" ("annoyed", "narrow", "angry", "mid")
        gen "I'll give you ten house points if you stay!{w=0.8} Just a tiny bit longer!" ("angry", xpos="far_left", ypos="head")
        cho "And what makes you believe that I'd agree to such a thing?{w=0.8} Getting rewarded with points for doing nothing?" ("open", "closed", "base", "mid")
        cho "Earning house points in such a way is despicable, and it would be unfair towards the other school houses, as well as my fellow students..." ("open", "narrow", "base", "mid")
        cho "" ("annoyed", "narrow", "angry", "mid")
        gen "Fifty points?" ("angry", xpos="far_left", ypos="head")
        cho "I have to go now, Sir." ("annoyed", "narrow", "angry", "R")
        gen "(Fuck me...)" ("base", xpos="far_left", ypos="head")

        call gen_chibi("sit_behind_desk")
        with d3
        pause .8

        cho "Until next time!" ("soft", "narrow", "base", "mid")

    else:
        gen "Okay, girl. You may leave..." ("base", xpos="far_left", ypos="head")
        cho "Thank you, Sir." ("base", "base", "base", "down")
        cho "See you next time." ("smile", "base", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    call bld
    gen "(...)" ("base", xpos="far_left", ypos="head")
    if states.gen.masturbating:
        gen "(Blue-balled...)" ("base", xpos="far_left", ypos="head")
        gen "(Oh well...{w=0.4} Maybe I deserved it.)" ("base", xpos="far_left", ypos="head")

    jump end_cho_talk_event

label cc_pf_talk_T1_intro_E2:

    call cc_pf_talk

    gen "Get closer, [name_cho_genie]..." ("grin", xpos="far_left", ypos="head")
    cho "..." ("annoyed", "base", "base", "down")

    call cho_walk("desk", "base")
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "" ("annoyed", "narrow", "angry", "mid", xpos="mid", ypos="base", trans=d3)
    pause .5

    cho "Another talk, sir?" ("soft", "narrow", "angry", "mid")
    cho "Are we going to discuss my previous relationships again?" ("open", "narrow", "base", "R")
    gen "I don't know.{w=1.0} Would you like to?" ("base", xpos="far_left", ypos="head")
    cho "I'd rather not." ("soft", "narrow", "angry", "mid")
    gen "Tell me about yourself then." ("base", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]." ("smile", "base", "base", "mid")
    cho "We had a training session yesterday." ("soft", "base", "base", "R")
    gen "Training session?" ("base", xpos="far_left", ypos="head")
    cho "Yes. We are preparing ourselves for the Quidditch match against Hufflepuff." ("open", "narrow", "base", "mid")
    cho "Our team really believes that we have a chance to win this time!" ("smile", "base", "base", "mid")
    cho "They got a huge boost of confidence after I told 'em that the {i}Great Albus Dumbledore{/i} would be training us himself!" ("base", "narrow", "base", "mid")
    gen "The... Great?" ("base", xpos="far_left", ypos="head")
    cho "That's right!" ("smile", "base", "base", "mid")
    menu:
        "-Play it down-":
            gen "Surely that can't be right..." ("base", xpos="far_left", ypos="head")
            cho "But you are, [name_genie_cho]!" ("smile", "narrow", "base", "mid")
            cho "Every witch and wizard has heard of the great Albus Dumbledore." ("smile", "closed", "base", "mid")
            gen "Are you sure they weren't referring to {i}My Albus{/i}?" ("base", xpos="far_left", ypos="head")
            cho "Your Albus, [name_genie_cho]?" ("soft", "base", "base", "mid")
            cho "I'm not sure I--" ("open", "base", "raised", "mid")
        "-Be modest-":
            gen "Well, I wouldn't say great..." ("base", xpos="far_left", ypos="head")
            cho "(He's so modest.)" ("base", "narrow", "base", "downR")
            gen "{i}Massive{/i} is a more accurate description." ("base", xpos="far_left", ypos="head")
            cho "Massive, [name_genie_cho]?" ("soft", "base", "base", "mid")
            cho "I'm not sure I understand..." ("soft", "narrow", "base", "mid")
            gen "I'm sure you'll find out in due time." ("base", xpos="far_left", ypos="head")
        "-Boast-":
            gen "Ah... Yes... Albin the great, that's me, alright!" ("base", xpos="far_left", ypos="head")
            gen "I hope you realise how lucky you are to get the opportunity to experience my greatness first hand." ("grin", xpos="far_left", ypos="head")
            cho "Oh, of course [name_genie_cho]! Thank you again, [name_genie_cho]!" ("angry", "base", "base", "mid")
            gen "And perhaps one day, you'll get the privilege to experience my greatness {i}first mouth{/i}." ("grin", xpos="far_left", ypos="head")
            cho "First... Mouth, [name_genie_cho]?" ("soft", "base", "raised", "mid")
            gen "That's right." ("base", xpos="far_left", ypos="head")
            cho "I don't--" ("annoyed", "base", "base", "mid")
    gen "Speaking of your team...{w=0.4} You're getting along with them well, I hope?" ("base", xpos="far_left", ypos="head")
    cho "I'd say so...{w=1.0} Although there was a time when--" ("soft", "base", "base", "mid")
    cho "Let's just say it was a bit difficult for me at first. After all, Quidditch is largely dominated by men..." ("open", "narrow", "worried", "down")
    cho "Getting accepted into our Quidditch team was a challenge. I really had to prove I was worth it." ("soft", "narrow", "worried", "mid")
    gen "And how exactly did you manage that? Mind spilling the beans?" ("grin", xpos="far_left", ypos="head")
    cho "Through diligence, expertise, and determination!" ("open", "closed", "base", "mid")
    cho "" ("normal", "base", "base", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "I was sort of expecting something else entirely but... you do you..." ("base", xpos="far_left", ypos="head")
    cho "And as you can see -- it did work out in my favour, Sir." ("smile", "base", "base", "mid")
    cho "Very few teams have allowed a female player into their ranks over the past years." ("open", "narrow", "angry", "R")
    cho "And I've been the only female seeker at this school in over half a century!" ("open", "wide", "base", "mid")
    cho "Can you even believe that, [name_genie_cho]?" ("soft", "base", "raised", "mid")
    gen "(Half a century? That's like a coffee break for me, girl...)" ("base", xpos="far_left", ypos="head")
    cho "I don't want to brag, [name_genie_cho], but the role of a seeker is {b}the{/b} most important position in a team by far!" ("smile", "narrow", "base", "mid")
    cho "If you don't have a good seeker, you have no chance of winning!" ("soft", "closed", "base", "mid")
    gen "No wonder you need my help so badly then..." ("base", xpos="far_left", ypos="head")
    cho "Our losses is neither my, nor my team's fault, [name_genie_cho]!" ("open", "base", "angry", "mid")
    gen "So whose is it then?" ("base", xpos="far_left", ypos="head")
    cho "The enemy team's, obviously!" ("soft", "narrow", "angry", "mid")
    cho "They are cheating! And they have done so for years!" ("mad", "narrow", "angry", "R")
    cho "This is my last chance! And I'm growing more and more desperate with my situation..." ("mad", "narrow", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")

    menu:
        "-Jerk off while she is talking-":
            hide cho_main
            hide screen bld1
            with d5
            pause .5

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.masturbating = True

        "-Participate in the conversation-":
            $ states.gen.masturbating = False

    cho "Ever since I was a little girl -- Quidditch has been my dream..." ("soft", "narrow", "worried", "down")
    cho "[name_genie_cho], can you imagine how {b}hard{/b} it was for me?" ("soft", "narrow", "worried", "mid")
    if states.gen.masturbating:
        gen "{size=-4}(Yes, yes... It's so hard for you, you little slut!!!){/size}" ("angry", xpos="far_left", ypos="head")
    cho "How difficult it was for me at first?" ("open", "narrow", "worried", "R")
    cho "Getting accepted?" ("soft", "closed", "worried", "mid")
    if states.gen.masturbating:
        gen "{size=-4}(I'd accept your ass on my cock if you're in such a need for acceptance, you whore!){/size}" ("angry", xpos="far_left", ypos="head")
    cho "I'm the only female in my team. Constantly surrounded by other men..." ("soft", "base", "worried", "down")
    if states.gen.masturbating:
        gen "{size=-4}(Yes! Yes! And they all would like to have their way with you!){/size}" ("angry", xpos="far_left", ypos="head")
    else:
        gen "(Quite a sausage-party this Quidditch, I have to admit.)" ("base", xpos="far_left", ypos="head")
        gen "(Maybe telling Hermione off was a bad idea after all...)" ("angry", xpos="far_left", ypos="head")
        gen "(An \"all female\" team would be more fun to watch...)" ("grin", xpos="far_left", ypos="head")
    cho "Always feeling their gaze behind my back..." ("disgust", "base", "worried", "down")
    cho "My own team, [name_genie_cho]!{w} They treat me like the plague!" ("upset", "base", "worried", "mid")
    cho "They ignore me during class..." ("soft", "closed", "base", "mid")
    cho "When I meet them in the common room they go out of their way not to cross paths with me..." ("annoyed", "narrow", "angry", "R")
    cho "And when we shower after practice they're scared to even look at me!" ("angry", "narrow", "angry", "mid")
    if states.gen.masturbating:
        gen "{size=-4}(Yes, yes!{w=0.5} Afraid to even look at you in the--){/size}" ("angry", xpos="far_left", ypos="head")
        with hpunch
        gen "Wait a bloody minute!{w} You shower {b}with{/b} your team?" ("angry", xpos="far_left", ypos="head")
    else:
        gen "The showers?{w} You shower {b}with{/b} your team?" ("angry", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]. It was after my request, after all." ("soft", "base", "raised", "mid")
    gen "No kidding?" ("angry", xpos="far_left", ypos="head")
    cho "They shouldn't exclude me from team activities just because I'm a girl." ("open", "narrow", "base", "R")
    cho "It makes absolutely no difference!" ("open", "closed", "angry", "mid")
    if states.gen.masturbating:
        gen "You are naked with them? In the showers?" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Just to be clear. You are naked with them, in the shower." ("base", xpos="far_left", ypos="head")
    cho "Of course we're all naked, [name_genie_cho]!" ("soft", "base", "angry", "mid")
    cho "Why would we shower with our clothes on?" ("soft", "closed", "base", "mid")

    # Genie cums.
    if states.gen.masturbating:
        gen "{size=-4}(You exhibitionist slut!){/size}" ("angry", xpos="far_left", ypos="head")
        gen "*Argh*! {size=-4}(Here it comes!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        call bld
        gen "*heavy breathing* {size=-4}(Take it!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        cho "" ("base", "narrow", "base", "mid")
        gen "*Argh*! {size=-4}(Shower in this, you slut!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        cho "[name_genie_cho], are you alright?" ("soft", "base", "base", "mid")
        cho "You're sweating and breathing quite heavily..." ("annoyed", "base", "worried", "mid")

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        cho "Shall I get Madam Pomfrey to check on you--" ("soft", "narrow", "base", "mid")
        gen "No, no! I'm..." ("angry", xpos="far_left", ypos="head")
        gen "I'm done.{w=0.3} Let's get back to the topic." ("base", xpos="far_left", ypos="head")
        cho "Which was?" ("open", "base", "raised", "mid")
        gen "You, taking showers with your \"teammates\"..." ("base", xpos="far_left", ypos="head")
        cho "(...)" ("annoyed", "narrow", "angry", "mid") # Annoyed

    gen "Don't you think, the fact that they've seen you naked hasn't affected any of their actions?" ("base", xpos="far_left", ypos="head")
    cho "Why would it, [name_genie_cho]? We're all adults here..." ("soft", "closed", "base", "mid")
    gen "Perhaps that's just your take on it, girl." ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "Maybe your \"teammates\" aren't as... \"mature\" as you." ("grin", xpos="far_left", ypos="head")
    cho "I've known my team for years.{w=0.6} We're all professionals!" ("soft", "narrow", "base", "mid")
    gen "Let me ask you a question..." ("base", xpos="far_left", ypos="head")
    gen "In the showers,{w=0.3} do they all have their backs turned towards you?" ("base", xpos="far_left", ypos="head")
    cho "I don't know. Maybe they--{w=0.2} *Uhm*..." ("open", "base", "base", "mid")
    cho "!!!" ("normal", "wide", "base", "mid") # Cho remembers something?!
    cho @ cheeks heavy_blush "" ("normal", "happyCl", "worried", "mid")
    pause .6
    gen "Yes?{w=0.3} What is it?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "May I... May I leave, [name_genie_cho]?" ("soft", "narrow", "worried", "mid")
    gen "Don't want to tell me?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "No." ("disgust", "happyCl", "worried", "mid")
    gen "Fine...{w=0.3} you may leave..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Thank you, [name_genie_cho]." ("open", "narrow", "worried", "mid")

    # Cho very slowly walks out of your office...
    call cho_walk(action="leave")

    call bld
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "(That just gave me an idea!)" ("grin", xpos="far_left", ypos="head")
    stop music fadeout 1.0

    call gen_chibi("sit_behind_desk")
    $ states.cho.requests_unlocked = True
    call popup("You can now buy \"Public Requests\" from Cho!", "Congratulations!", "interface/icons/head/cho.webp")

    jump end_cho_talk_event

label cc_pf_talk_T1_E3:

    $ states.cho.ev.talk_to_me.t1_e3_complete = True

    call cc_pf_talk

    gen "Care to tell me more about Quidditch?" ("base", xpos="far_left", ypos="head")
    cho "Of course, [name_genie_cho]." ("smile", "base", "base", "R")
    cho "I always love talking about Quidditch!" ("base", "base", "base", "mid")
    gen "Yeah, yeah... I know." ("base", xpos="far_left", ypos="head")
    gen "First, come closer. Let me have a good look at you!" ("base", xpos="far_left", ypos="head")
    cho "Yes, Sir." ("base", "base", "base", "mid")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    cho "Anything specific you'd like to know?" ("soft", "base", "base", "mid")
    gen "Yes. Let's talk some more about Duggery..." ("base", xpos="far_left", ypos="head")
    cho "*Huh*?" ("soft", "narrow", "base", "mid")
    gen "Your ex-boyfriend." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "{size=-4}I knew I shouldn't have told him...{/size}" ("disgust", "narrow", "base", "down")
    cho "Sir, do you have to bring him up?" ("soft", "narrow", "base", "mid")
    cho "What's past is in the past..." ("annoyed", "narrow", "angry", "R")
    gen "I believe otherwise..." ("base", xpos="far_left", ypos="head")
    gen "Have you already forgotten that he's our enemy?!" ("angry", xpos="far_left", ypos="head")
    gen "Your relationship with him is of the utmost importance right now!" ("base", xpos="far_left", ypos="head")
    gen "I need to know every tiny bit of detail about the two of you." ("base", xpos="far_left", ypos="head")
    gen "His sexual preferences. Secret fetishes he might have. That sort of stuff..." ("base", xpos="far_left", ypos="head")
    cho "Sir, that's a very personal thing to ask for!" ("open", "narrow", "base", "mid")
    cho "I will not tell you about any of that!" ("annoyed", "narrow", "angry", "mid")
    gen "[name_cho_genie], we need to find something we can use against him. To our advantage!" ("base", xpos="far_left", ypos="head")
    cho "But... {w=0.4} His sexual preferences? Are you sure knowing about that is important?" ("open", "narrow", "angry", "mid")
    gen "Very." ("base", xpos="far_left", ypos="head")
    cho "(...)" ("annoyed", "narrow", "angry", "R")
    cho "Very well, [name_genie_cho]..." ("open", "closed", "angry", "mid")
    cho "I'll tell you what I know about him." ("open", "narrow", "base", "mid")
    gen "Excellent." ("base", xpos="far_left", ypos="head")
    cho "Cedric was always a bit of a loner..." ("annoyed", "narrow", "base", "R")
    cho "He was cold, focused, and competitive. Never showed too much affection towards me...{w=0.4} Except for--" ("open", "base", "angry", "downR")
    cho "(...)" ("annoyed", "narrow", "base", "R")
    gen "Yes? Go on..." ("base", xpos="far_left", ypos="head")
    cho "I believe he had a bit of an obsession with my panties, Sir." ("soft", "narrow", "base", "mid")

    if not states.cho.ev.quidditch.hufflepuff_prepared:
        gen "A panties obsession? So so..." ("base", xpos="far_left", ypos="head")
    else:
        gen "*Ha!* Called it!" ("grin", xpos="far_left", ypos="head")

    cho "It was a little bit creepy how often he tried to look up my skirt..." ("angry", "wide", "base", "mid")
    cho "I mean, who would do such a thing?" ("soft", "base", "base", "mid")
    gen "Yes, yes... how terrible of him..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Jerk off while she's talking-":
            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.masturbating = True

            hide cho_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            call bld
            gen "Please tell me more about your panties!" ("grin", xpos="far_left", ypos="head")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False

            gen "(No, I need to focus!)" ("base", xpos="far_left", ypos="head")
            gen "(This might be useful information in our game against him...)" ("base", xpos="far_left", ypos="head")
            gen "Please, carry on..." ("base", xpos="far_left", ypos="head")
            cho "Of course, Sir." ("base", "base", "base", "mid")

    if states.gen.masturbating:
        cho "That's an oddly specific question, don't you think?" ("soft", "base", "raised", "mid", trans=d3)
        gen "Come on, girl! Which were the ones he liked the most?" ("angry", xpos="far_left", ypos="head")
        cho "*Uhm*..." ("annoyed", "base", "base", "R")
        cho "I never wore panties too often..." ("angry", "narrow", "base", "downR")
        cho "At least not those fancy ones the other girls are wearing." ("soft", "narrow", "base", "mid")
        gen "*Argh*! {size=-4}(I'd love to see those!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "If you can even call them that..." ("annoyed", "narrow", "base", "R")
        cho "Most of them look like shoelaces!" ("annoyed", "narrow", "angry", "R")
        gen "{size=-4}(What a bunch of sluts!){/size}" ("angry", xpos="far_left", ypos="head")
        nar "*Fap* *Fap* *Fap*..."
        cho "You should see them, [name_genie_cho]!" ("annoyed", "narrow", "angry", "mid")
        cho "They're all a bunch of sluts!!!" ("soft", "narrow", "angry", "mid")
        cho "They wear their skirts so low -- you just have to wonder how they haven't fallen off yet..." ("soft", "narrow", "base", "downR")
        gen "{size=-4}(Indeed, I'd love to see that!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "And pull their panty-string up and over their hip bones..." ("soft", "narrow", "base", "mid")
        gen "{size=-4}(Yes! So fucking slutty!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "They look like arrows pointing down at their \"Snitch\", if you get what I mean..." ("angry", "narrow", "angry", "mid")
        gen "*Argh!* {size=-4}(Those cheap whores!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "As if they give any boy an open invitation to lay with them..." ("soft", "narrow", "angry", "R")
        gen "*Fuck!* {size=-4}(That did it!!!){/size}" ("angry", xpos="far_left", ypos="head")

        # Genie cums.
        call hide_characters
        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        cho "As for me, panties have to be practical, first and foremost!" ("soft", "closed", "base", "mid")
        gen "*Ahg!* {size=-4}(So you can quickly get them off, you whore!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        cho "And there needs to be enough fabric to soak up all the sweat..." ("soft", "narrow", "base", "R")
        gen "{size=-4}(I bet you are so wet right now too!){/size}" ("angry", xpos="far_left", ypos="head")

        # Genie finished.
        call hide_characters
        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        cho "(...)" ("annoyed", "narrow", "base", "mid")
        cho "Sir, would it be alright if I head off now?" ("soft", "base", "base", "R")
        gen "Already? Do you have to be somewhere?" ("grin", xpos="far_left", ypos="head")
        gen "Did our little talk about panties maybe... excite you?" ("grin", xpos="far_left", ypos="head")
        cho "What? No, of course not!" ("angry", "wide", "base", "mid")

        if game.daytime:
            cho "I simply have to go to my next lesson..." ("soft", "closed", "base", "mid")
            cho "Or I will be late again." ("annoyed", "base", "base", "R")
        else:
            cho "But if you expect me to do well during our next Hufflepuff game, then I'll require some sleep..." ("soft", "base", "base", "R")

        gen "Of course. You may go..." ("base", xpos="far_left", ypos="head")
        cho "Thank you, Sir." ("base", "base", "base", "mid")
        cho "Until next time." ("smile", "narrow", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")
        call bld

        if not states.cho.ev.quidditch.hufflepuff_prepared:
            gen "(I bet she enjoyed every second of it, or she'd most definitely have called him out...)" ("base", xpos="far_left", ypos="head")
            gen "(...)" ("base", xpos="far_left", ypos="head")
            gen "(Wait a minute... That's it!)" ("base", xpos="far_left", ypos="head")
            gen "(Now we just need her to fly in the perfect position to show them off during the game...)" ("base", xpos="far_left", ypos="head")
            gen "(Well then, better get back to training and discuss my brilliant tactics with her...)" ("base", xpos="far_left", ypos="head")
            gen "(To think I'd have such a good excuse to have her show me her panties already.)" ("grin", xpos="far_left", ypos="head")
        else:
            gen "(Well, can't say that I blame him...)" ("base", xpos="far_left", ypos="head")
            gen "(I'd take any and every chance to see those panties as well...)" ("base", xpos="far_left", ypos="head")

        call gen_chibi("sit_behind_desk")
        jump end_cho_talk_event

    else:
        cho "He'd always walk behind me when we went up the stairs, to get a better view, I bet..." ("soft", "narrow", "angry", "R")
        gen "Did you ever show them to him on purpose?" ("base", xpos="far_left", ypos="head")
        cho "My panties?" ("soft", "base", "raised", "mid")
        gen "No, your good manners...{w} Yes, your panties!" ("base", xpos="far_left", ypos="head")
        cho "Why would I do that?" ("soft", "narrow", "raised", "mid")
        gen "What kind of girl doesn't show her panties to her beloved?" ("base", xpos="far_left", ypos="head")
        cho "I beg your pardon?!" ("angry", "wide", "raised", "mid")

        if not states.cho.ev.quidditch.hufflepuff_prepared:
            gen "But, that made me think..." ("base", xpos="far_left", ypos="head")
            gen "If he's as obsessed with panties as you say, why don't we use that information to our advantage?" ("base", xpos="far_left", ypos="head")
            cho "Like how?" ("soft", "narrow", "raised", "mid")
            gen "We use them as a distraction!" ("base", xpos="far_left", ypos="head")
            gen "Now we only have to find out how to show them off properly during the game." ("base", xpos="far_left", ypos="head")
            cho "I have to say I don't like this notion one bit." ("annoyed", "narrow", "base", "mid")
            cho "But it might be worth a try..." ("soft", "narrow", "base", "R")
        else:
            gen "Well, it worked." ("base", xpos="far_left", ypos="head")
            gen "This {i}Quayditch{/i} thing is easy!" ("base", xpos="far_left", ypos="head")
            cho "Quidditch, Sir..." ("soft", "closed", "base", "mid")
            gen "To think all we had to do was put some good-old panties in front of his face..." ("base", xpos="far_left", ypos="head")
            cho "" ("annoyed", "narrow", "base", "mid")
            gen "He must've looked like a wild goat, chasing after them." ("angry", xpos="far_left", ypos="head")
            cho "A goat?" ("soft", "narrow", "raised", "mid")
            gen "Yes. Don't you have those here?" ("base", xpos="far_left", ypos="head")
            cho "Goats don't chase after panties, Sir..." ("soft", "narrow", "base", "R")
            gen "They do where I'm from..." ("base", xpos="far_left", ypos="head")
            cho "(...)" ("annoyed", "narrow", "angry", "R")
            cho "But you were correct with your assumption, Sir." ("soft", "closed", "base", "mid")
            cho "I'm surprised how well it worked out in our favour." ("annoyed", "base", "raised", "down")
            cho "He really {b}does{/b} love panties..." ("soft", "narrow", "base", "mid")
            gen "I mean who doesn't..." ("base", xpos="far_left", ypos="head")

        cho "Sir, if you don't mind..." ("soft", "closed", "base", "mid")
        if game.daytime:
            cho "I'm already late for class." ("soft", "narrow", "base", "R")
            cho "I really should be going now..." ("angry", "narrow", "worried", "mid")
        else:
            cho "It's getting late." ("soft", "narrow", "base", "mid")
            cho "I really should head to bed now..." ("angry", "narrow", "worried", "mid")

        gen "Of course. You are dismissed." ("base", xpos="far_left", ypos="head")
        cho "Thank you, Sir." ("base", "base", "base", "mid")
        if game.daytime:
            cho "Until next time." ("smile", "narrow", "base", "mid")
        else:
            cho "Have a good night." ("smile", "narrow", "base", "mid")

        # Cho leaves.
        call cho_walk(action="leave")

        call bld
        gen "(I wonder what colours they are...)" ("base", xpos="far_left", ypos="head")
        gen "(If she's even wearing any...{w} You never know.)" ("base", xpos="far_left", ypos="head")

        jump end_cho_talk_event

### Tier 2 (pre Slytherin) ###

label cc_pf_talk_T2_intro_E1:

    call cc_pf_talk

    gen "Miss Chang, it's time we have another chat." ("base", xpos="far_left", ypos="head")
    gen "Please come a bit closer..." ("base", xpos="far_left", ypos="head")
    cho "Yes, Sir." ("base", "base", "base", "mid")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    gen "Tell me, how have you been?" ("base", xpos="far_left", ypos="head")
    gen "I bet a lot has changed for you after your big win!" ("grin", xpos="far_left", ypos="head")
    cho "More or less..." ("soft", "base", "raised", "mid")
    cho "School has been rather uneventful the past couple of days." ("soft", "base", "base", "R")
    cho "That is, if constantly getting bullied is the new norm at this school..." ("annoyed", "narrow", "angry", "mid")
    gen "Bullied by whom?" ("base", xpos="far_left", ypos="head")
    cho "The Slytherin Quidditch team!{w=0.6} They've been total dicks lately..." ("open", "narrow", "angry", "mid")
    gen "You don't say.{w=0.8} Why is that?" ("base", xpos="far_left", ypos="head")
    cho "Because they are scared of us, I wager..." ("soft", "narrow", "angry", "downR")

    cho "We'll be playing against them next." ("annoyed", "narrow", "base", "R")
    cho "And of course they have to behave like the absolute worst!" ("soft", "narrow", "angry", "mid")
    cho "They deserve to be publicly disgraced in front of the whole school!{w=0.8} The whole lot of them!" ("scream", "closed", "angry", "mid", trans=hpunch)
    cho "I'll make sure of it, [name_genie_cho]!{w=0.6} The Slytherin team will lose!" ("mad", "narrow", "angry", "mid")
    gen "(And I'll win my bet with Snape even sooner! Sweet!)" ("grin", xpos="far_left", ypos="head")
    gen "Anything you can tell me about them?{w=0.6} Are they better than Hufflepuff?" ("base", xpos="far_left", ypos="head")
    cho "They are, by quite a bit." ("annoyed", "base", "base", "mid")
    cho "However, Hufflepuff only had one really good player. Which was Cedric." ("soft", "base", "base", "R")
    cho "Slytherin on the other hand, they are almost unbeatable!" ("angry", "wide", "base", "mid")
    cho "They might even be better than Gryffindor..." ("annoyed", "base", "base", "up")
    gen "You don't say. So, why are they next and not Gryffindor?" ("base", xpos="far_left", ypos="head")
    cho "Because of their seeker, Sir." ("soft", "narrow", "base", "mid")
    cho @ cheeks blush "He's so...{w=0.6} so bad!" ("clench", "narrow", "base", "R")
    gen "Who is their seeker?" ("base", xpos="far_left", ypos="head")
    cho "Draco Malfoy, Sir." ("open", "closed", "base", "mid")
    gen "(The cocky fella! Snape mentioned him before...)" ("base", xpos="far_left", ypos="head")
    cho "They've been continuously harassing my team..." ("annoyed", "narrow", "angry", "R")
    cho "Well, mostly me, actually." ("angry", "narrow", "base", "downR") # Embarrassed

    menu:
        "-Jerk off while she's talking-":
            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.masturbating = True

            hide cho_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            gen "(Just to make this clear, I'm not getting off because I like the thought that she's getting bullied...)" ("base", xpos="far_left", ypos="head")
            nar "Right..."
            gen "I hope you fought back those bullies?" ("angry", xpos="far_left", ypos="head")
            cho "Of course, [name_genie_cho]!" ("base", "base", "base", "mid")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False
            gen "(No, I need to focus!)" ("base", xpos="far_left", ypos="head")
            gen "So... would you like to report them?" ("base", xpos="far_left", ypos="head")
            cho "No, Sir." ("soft", "closed", "base", "mid")
            gen "No?" ("base", xpos="far_left", ypos="head")

    cho "I do not endorse their behaviour, Sir.{w=0.6} And I hope no other student has to share the same harassment that I received." ("soft", "narrow", "angry", "mid")
    cho "{size=-4}Unless maybe Granger...{/size}" ("annoyed", "narrow", "angry", "R") # Small text.
    cho "But{w=0.3}, watching them succumb to me has been rather fun..." ("base", "narrow", "angry", "mid")
    gen "Succumb to you?" ("base", xpos="far_left", ypos="head")
    cho "Yes.{w=0.3} They're so desperately trying to embarrass me.{w=0.6} To make me doubt myself before the big game..." ("smile", "narrow", "angry", "mid")

    if states.gen.masturbating:
        gen "Those asshole bullies...{w=0.6} Show them who's boss!" ("angry", xpos="far_left", ypos="head")
    else:
        gen "And a strong, independent woman like yourself would never be intimidated by puny Slytherins!" ("grin", xpos="far_left", ypos="head")
        cho "Of course not, Sir." ("soft", "closed", "base", "mid")
        gen "I'm so proud!" ("angry", xpos="far_left", ypos="head")

    cho @ cheeks blush "After all, I'm only a small, helpless girl{w=0.6}, and they are a group of strong, ruthless alpha males!" ("soft", "base", "worried", "R")
    cho "Their attempts are pathetic!" ("angry", "narrow", "angry", "mid")
    cho "They are pathetic!!!" ("clench", "narrow", "angry", "mid", trans=hpunch)
    cho "Trying to lift my skirt with first-year spells..." ("soft", "narrow", "angry", "R")
    cho "Stealing my underwear while I'm taking a shower after practice..." ("angry", "narrow", "angry", "downR")
    if states.gen.masturbating:
        gen "*Argh!* {size=-4}(Dirty panty muggers!){/size}" ("angry", xpos="far_left", ypos="head")
    cho "They even had the audaciousness to write \"Cho, the Ravenclaw ho\" on the blackboard during divination class." ("open", "narrow", "angry", "mid")
    if states.gen.masturbating:
        gen "{size=-4}(They must have seen your future, you whore!){/size}" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "Half the class saw it before I could get there...{w=0.8} Not that I care much about it..." ("annoyed", "narrow", "base", "downR")
    cho "If I'm honest, I'm surprised they could even spell my name correctly..." ("soft", "narrow", "angry", "mid")
    if states.gen.masturbating:
        nar "*Fap* *Fap* *Fap*..."
    cho "They think they can intimidate me. But that's where they are mistaken!" ("angry", "narrow", "angry", "down")

    if states.gen.masturbating:
        cho "They should be scared of me, [name_genie_cho]!" ("soft", "narrow", "angry", "mid")
        gen "{size=-4}(Yes! Show them, you slut!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "Of what {b}I'm{/b} capable of!" ("clench", "base", "angry", "mid")
        gen "*Argh*! (I'm getting close!)" ("angry", xpos="far_left", ypos="head")
        cho "Scared of what's about to come!" ("soft", "narrow", "angry", "mid")

        # Genie cums.
        gen "{size=-4}(Yes! Yes!{w=0.6} It's coming!){/size}" ("angry", xpos="far_left", ypos="head")
        call hide_characters

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        gen "*Argh*! {size=-4}(Take it!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        gen "*Panting* {size=-4}(You fucking slut!){/size}" ("angry", xpos="far_left", ypos="head")

        call gen_chibi("cum_behind_desk_done")
        with d3
        pause .8

        cho "" ("annoyed", "narrow", "base", "mid")
        gen "(*Phewwww*...)" ("base", xpos="far_left", ypos="head")
        gen "(That was nice.)" ("base", xpos="far_left", ypos="head")
        cho "Are you feeling well, Sir?" ("open", "narrow", "raised", "mid")
        gen "Never felt better!" ("grin", xpos="far_left", ypos="head")
        cho "That's good to hear." ("smile", "base", "base", "mid")

    gen "I'm glad you aren't letting yourself get oppressed by those Slytherins." ("base", xpos="far_left", ypos="head")
    cho "Not in a million years!" ("base", "narrow", "base", "mid")
    gen "Admirable." ("base", xpos="far_left", ypos="head")

    gen "Anything else you could tell me about their team?{w=0.6} Anything that could help us?" ("base", xpos="far_left", ypos="head")
    gen "Did you maybe fool around with their seeker as well?" ("base", xpos="far_left", ypos="head")
    cho "Malfoy?" ("soft", "wide", "base", "mid") # Shocked
    cho "*Tzzzz*!{w=0.3} I'd never surround myself with that Slytherin scum!" ("angry", "closed", "angry", "mid")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "I guess you and Granger have at least some things in common..." ("base", xpos="far_left", ypos="head")
    cho "His {b}daddy{/b} bought their whole team new brooms, which is the only reason they've even let him in." ("soft", "narrow", "raised", "mid")
    gen "His \"daddy\"?" ("base", xpos="far_left", ypos="head")
    cho "His father, Sir." ("soft", "closed", "angry", "mid")
    gen "Oh. I thought you might be talking about a different kind of \"daddy\"." ("base", xpos="far_left", ypos="head")
    cho "Very funny, [name_genie_cho]..." ("annoyed", "narrow", "angry", "R")
    cho "Now, if that's everything..." ("soft", "closed", "base", "mid")

    if game.daytime:
        cho "Classes are about to start, and I'm already late for them..." ("open", "narrow", "base", "R")
        cho "I hope it would be okay if I leave?" ("soft", "narrow", "base", "mid")
    else:
        cho "It's getting late, and I have to go and get some sleep..." ("open", "narrow", "base", "R")
        cho "I hope you don't mind, Sir?" ("soft", "narrow", "base", "mid")

    gen "Not at all.{w=0.3} You may go." ("base", xpos="far_left", ypos="head")
    cho "Thank you, Sir." ("smile", "base", "base", "mid")
    cho "Until next time..." ("base", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_talk_event

label cc_pf_talk_T2_intro_E2:

    call cc_pf_talk

    gen "Would you mind if we had another chat?" ("base", xpos="far_left", ypos="head")
    cho "Of course not, [name_genie_cho]!" ("smile", "base", "base", "mid")
    gen "Come closer then..." ("base", xpos="far_left", ypos="head")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    gen "How's school? Have anything to tell me?" ("base", xpos="far_left", ypos="head")
    cho "Quite a bit, Sir!" ("smile", "happyCl", "base", "mid")
    cho "I feel like people have shown me more affection ever since our game against Hufflepuff." ("base", "base", "base", "mid")
    gen "You don't say..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Jerk off while she's talking-":
            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.masturbating = True

            hide cho_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            cho "" ("soft", "base", "base", "up")
            gen "*Agh*! Go on!" ("angry", xpos="far_left", ypos="head")
            cho "What?" ("soft", "narrow", "raised", "mid")
            cho "Oh, I'm sorry, Sir.{w=0.6} Of course!" ("soft", "wide", "base", "mid")
            cho "I had my head in the clouds there for a second." ("smile", "happyCl", "base", "mid")

        "-Participate in the conversation-":
            $ states.gen.masturbating = False
            gen "Do you have any idea why that might be?" ("base", xpos="far_left", ypos="head")
            cho "Because of our win, why else!" ("smile", "narrow", "base", "mid")
            gen "And it had nothing to do with the fact that half the school got to see your panties?" ("base", xpos="far_left", ypos="head")
            cho "No! Of course not!" ("soft", "narrow", "angry", "mid")
            cho "Please don't try to diminish my achievement, Sir!" ("annoyed", "narrow", "base", "R")

    cho "It's like I'm a celebrity now!{w=0.6} I'm getting so much attention!" ("soft", "base", "base", "R")
    cho "It never happened that Ravenclaw won a game.{w=0.6} And I made that possible!" ("smile", "base", "base", "mid")
    if states.gen.masturbating:
        gen "{size=-4}And soon you'll be on your knees thanking me for it!{/size}" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Hey! Don't you forget about me!" ("base", xpos="far_left", ypos="head")
        gen "Where would you be without the great {i}Dooblydore{/i}..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Of course, Sir!" ("clench", "happyCl", "worried", "mid")
        cho @ cheeks blush "Sorry, Sir!" ("soft", "narrow", "worried", "mid")

        menu:
            gen "(Maybe it wouldn't be such a bad idea to...)" ("base", xpos="far_left", ypos="head")
            "-Jerk off while she's talking-":
                $ states.gen.stats.masturbated_to_cho += 1
                $ states.gen.masturbating = True

                hide cho_main
                nar "You reach under the desk and grab your cock..."

                call gen_chibi("jerk_off_behind_desk")
                with d3
                pause .8

                call bld
                gen "Please, don't let me interrupt your thought..." ("base", xpos="far_left", ypos="head")
                gen "I'd like to hear more!" ("grin", xpos="far_left", ypos="head")

            "-Participate in the conversation-":
                $ states.gen.masturbating = False
                gen "(No, I need to focus!)" ("base", xpos="far_left", ypos="head")
                gen "Please, don't let me interrupt your thought..." ("base", xpos="far_left", ypos="head")
                gen "Continue..." ("base", xpos="far_left", ypos="head")

        cho "Of course, Sir." ("base", "base", "base", "mid")

    cho "It's fun receiving all of the boys attention!{w=0.8} And seeing how jealous it makes all of the girls!" ("soft", "base", "base", "mid")
    cho "Especially Granger!" ("smile", "narrow", "base", "mid")
    if states.gen.masturbating:
        gen "{size=-4}Yes, the Gryffindor whore!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "You should have seen her face, [name_genie_cho]!" ("soft", "narrow", "angry", "mid")
    cho "She's so angry at me! I love it!" ("smile", "happyCl", "base", "mid")
    cho "She can't even bear to look at me anymore." ("grin", "narrow", "angry", "mid")
    cho "You should know, for whatever reason, almost all of Hufflepuff blames her for helping Ravenclaw secure the win!" ("soft", "base", "base", "R")
    cho "She announced several times that Hufflepuff was leading in points, when they actually weren't!" ("smile", "narrow", "angry", "mid")
    cho "Which resulted in Hufflepuff playing far more defensively, when they should have been aggressive!" ("base", "narrow", "base", "mid")
    if states.gen.masturbating:
        gen "{size=-4}Oh, you are one of those girls! I like going aggressive!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "I caught the Snitch at just the right time!{w=0.6} If Hufflepuff had gone too far in the lead, we would have lost!" ("open", "narrow", "angry", "mid")
    cho "I really need to thank Granger the next time I see her.{w=0.6} I owe her a great deal..." ("soft", "narrow", "angry", "R")
    if states.gen.masturbating:
        gen "{size=-2}I'd love to watch you \"thank her!\"{/size}" ("angry", xpos="far_left", ypos="head")
        cho "Maybe I'll do something fun with her the next time I see her..." ("base", "narrow", "base", "R")
        cho "Something that would rile her up even more!" ("smile", "narrow", "angry", "downR")
    else:
        gen "Yes? And how exactly would you \"thank her\"?" ("grin", xpos="far_left", ypos="head")
        cho "I don't know. Maybe something that would rile her up even more..." ("annoyed", "base", "base", "downR")
    cho "Like a kiss on her cheek, or an uncomfortably long hug!" ("soft", "narrow", "base", "mid")
    cho "Or I'll do something more sinister! Something she'd never expect!" ("base", "base", "base", "R")
    if states.gen.masturbating:
        gen "*Ugh*! {size=-2}Like what?{/size}" ("angry", xpos="far_left", ypos="head")
    else:
        gen "More sinister? Like what?" ("base", xpos="far_left", ypos="head")
    cho "Give her a proper kiss on the lips, perhaps?" ("soft", "narrow", "angry", "mid")
    with hpunch
    gen "!!!" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes! I bet a prude like her would be {b}so{/b} shocked by that!{w=0.8} I might even be her first!" ("soft", "base", "angry", "downR")

    # Forced to jerk off.
    if states.gen.masturbating:
        gen "{size=-4}Yes! You fucking sluts!{/size}" ("angry", xpos="far_left", ypos="head")
    else:
        gen "(Fuck it, this is too much!)" ("angry", xpos="far_left", ypos="head")

        menu:
            "-Flog the dong-":
                pass
            "-Practice Onanism-":
                pass
            "-Diddle do-":
                pass

        $ states.gen.stats.masturbated_to_cho += 1
        $ states.gen.masturbating = True

        hide cho_main
        nar "You reach under the desk and grab your cock..."

        call gen_chibi("jerk_off_behind_desk")
        with d3
        pause .8

        call bld
        gen "Please, continue!" ("angry", xpos="far_left", ypos="head")

    cho @ cheeks blush "Just thinking about her puffy pink lips..." ("annoyed", "narrow", "angry", "down")
    gen "{size=-2}Yes! Yes!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "I should make her choke on my tongue, whether she likes it or not..." ("clench", "narrow", "angry", "downR")
    gen "{size=-2}Yes! That would be so fucking hot!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "Push her against a wall and force it into her bitch mouth!" ("angry", "narrow", "angry", "down")
    gen "*Argh!* {size=-2}You fucking sluts!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "And then I pull her vest over her stupidly large breasts..." ("smile", "narrow", "angry", "L")
    cho "And embarrass her in front of the whole class!" ("soft", "base", "base", "up")
    cho "Show everyone her ridiculous {b}cow tits!{/b}" ("soft", "narrow", "angry", "up")
    gen "{size=-2}Yes!!!{/size} {size=-4}(I'm almost there!){/size}" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "She deserves it..." ("angry", "closed", "angry", "R")
    cho @ cheeks blush "That know-it-all, pretentious little bitch!" ("soft", "narrow", "angry", "downR")

    # Genie cums.
    gen "{size=-2}Yes, yes! You nasty slut!{/size}" ("angry", xpos="far_left", ypos="head")
    call hide_characters
    hide screen bld1
    with d3

    call cum_block
    call gen_chibi("cum_behind_desk")
    with d3
    pause .8

    call bld
    gen "*Argh*! {size=-4}Take it!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "Oh, I'm so sorry, Sir." ("soft", "narrow", "base", "mid")
    cho "I forgot I was talking to you for a second!" ("angry", "closed", "worried", "mid")

    call cum_block
    gen "*Argh* {size=-4}You lesbian slut!{/size}" ("angry", xpos="far_left", ypos="head")
    cho "I hope you didn't hear any of it! I would never do--" ("soft", "narrow", "worried", "mid")

    call cum_block
    cho "Sir?!" ("annoyed", "narrow", "raised", "mid")
    call cum_block
    pause .8

    cho @ cheeks heavy_blush "[name_genie_cho]! What the bloody hell are you doing?!" ("angry", "wide", "base", "mid", trans=hpunch)
    gen "{size=-4}(Oh no!){/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=-4}(I'm busted!){/size}" ("angry", xpos="far_left", ypos="head")

    # Genie stops.
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call gen_chibi("cum_behind_desk_done")
    pause .8

    cho @ cheeks blush "" ("clench", "wide", "base", "mid")
    gen "Nothing, I was just--" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Don't tell me you were..." ("disgust", "happyCl", "worried", "mid")
    gen "I was merely scratching my leg!" ("angry", xpos="far_left", ypos="head")
    cho "Don't lie to me, [name_genie_cho]!{w=0.6} I know exactly what you were doing!" ("clench", "narrow", "angry", "mid")
    cho "{size=+4}You were touching yourself!{/size}" ("scream", "closed", "angry", "mid", trans=hpunch) # Scream
    cho "" ("angry", "narrow", "angry", "mid")
    gen "{size=-2}Not so loud! People might hear you!{/size}" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "Why would you think I care?!" ("open", "narrow", "angry", "L")
    cho @ cheeks blush "You were wanking off!" ("soft", "wide", "base", "mid")
    gen "No I wasn't..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "In front of your own student!" ("disgust", "happyCl", "worried", "down")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    gen "Stop making a big deal out of it, would you?" ("base", xpos="far_left", ypos="head")
    cho "So you're admitting that you did it!" ("angry", "narrow", "angry", "mid")
    gen "Fine... I don't care at this point..." ("base", xpos="far_left", ypos="head")
    cho "That's disgusting!" ("soft", "narrow", "base", "mid")
    gen "You're making an even bigger fuss about it than Hermione..." ("base", xpos="far_left", ypos="head")
    cho "Good for her!" ("angry", "closed", "angry", "mid")
    cho "Maybe you should call her up here to clean up your mess as well!" ("soft", "narrow", "base", "mid")
    cho "And lick it all up!{w} I bet she'd love that!!!" ("angry", "narrow", "angry", "mid")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I'm leaving." ("disgust", "happyCl", "worried", "mid")
    cho @ cheeks blush "Have a nice day, [name_genie_cho]!" ("soft", "narrow", "angry", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    gen "(I really did make a mess...)" ("base", xpos="far_left", ypos="head")
    gen "(Maybe I {b}should{/b} get Hermione to clean it up for me?)" ("base", xpos="far_left", ypos="head")
    gen "(With her mouth!)" ("grin", xpos="far_left", ypos="head")
    gen "(..........)" ("base", xpos="far_left", ypos="head")
    gen "(Aaaaaaand I'm hard again...{w} Maybe some other time...)" ("base", xpos="far_left", ypos="head")

    $ states.cho.mood += 9

    jump end_cho_talk_event


label cc_pf_talk_T2_E3:

    $ states.cho.ev.talk_to_me.t2_e3_complete = True

    call cc_pf_talk

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "" ("soft", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    gen "[name_cho_genie], how is school life?" ("grin", xpos="far_left", ypos="head")
    gen "I need to stay \"on top\" of all the latest \"hot goss\"..." ("base", xpos="far_left", ypos="head")
    cho "Sir, I don't tend to pay attention to that sort of stuff." ("soft", "closed", "base", "mid")
    gen "You must at least have heard something raunchy here at the school?" ("base", xpos="far_left", ypos="head")
    cho "*Uhm*...{w} well..." ("annoyed", "base", "base", "R")

    menu:
        "-Jerk off while she's talking-":
            $ states.gen.stats.masturbated_to_cho += 1
            $ states.gen.masturbating = True

            hide cho_main
            nar "You reach under the desk and grab your cock..."

            call gen_chibi("jerk_off_behind_desk")
            with d3
            pause .8

            cho "" ("base", "base", "base", "mid")
            gen "You don't mind if I..." ("base", xpos="far_left", ypos="head")
            cho "Mind what?!" ("soft", "base", "raised", "mid")
            cho @ cheeks blush "!!!" ("upset", "wide", "base", "mid") # Shocked
            gen "I have needs, girl." ("base", xpos="far_left", ypos="head")
            cho "Gross!!!" ("angry", "closed", "angry", "mid")
            cho "[name_genie_cho], might I suggest that you sort out those needs on your own then?" ("soft", "narrow", "angry", "R")
            cho "Without me..." ("soft", "narrow", "angry", "mid")
            gen "What a Bummer...{w=0.6} Last time you were such a great aid..." ("base", xpos="far_left", ypos="head")
            cho "What?! When did I ever help you with that?" ("soft", "wide", "base", "mid")
            gen "When you told me about that little fantasy you had with Granger!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "You shouldn't have paid attention to any of that!" ("mad", "happyCl", "worried", "mid")
            gen "But I did!" ("grin", xpos="far_left", ypos="head")
            gen "I could just tell Hermione that you're into her, you know..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I am so not into her!" ("clench", "narrow", "angry", "mid")
            cho @ cheeks heavy_blush "(...)" ("annoyed", "narrow", "angry", "R") # Embarrassed
            gen "Yes you are! Don't you dare lie to me...{w=0.6} Or yourself for that matter." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "(...)" ("annoyed", "narrow", "angry", "downR")
            gen "So...{w=0.3} Is this going to be a problem or what?" ("base", xpos="far_left", ypos="head")
            cho "Fine...{w=0.3} If you can't help yourself." ("soft", "narrow", "angry", "mid")
            gen "Great!{w=0.3} Pretend like I'm not even here!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "I more likely will be pretending that {b}I'm{/b} not here..." ("soft", "narrow", "angry", "downR") # Small text

        "-Participate in the conversation-":
            $ states.gen.masturbating = False
            gen "(Seems like I'm not feeling the need to jack off today...{w=0.4} Free will is an illusion.)" ("base", xpos="far_left", ypos="head")
            gen "(Oh well... Might as well pay attention for once.)" ("base", xpos="far_left", ypos="head")
            gen "Go on, [name_cho_genie]..." ("base", xpos="far_left", ypos="head")

    gen "Why don't you tell me some more about..." ("base", xpos="far_left", ypos="head")
    cho "The Slytherins? Gladly!" ("open", "narrow", "angry", "mid")
    gen "(I was going to say Hermione but sure...)" ("base", xpos="far_left", ypos="head")

    # Malfoy
    cho "It was only yesterday that I had that stinking Malfoy boy snickering behind my back as I walked past him." ("open", "narrow", "angry", "R")
    if states.gen.masturbating:
        cho "I can only imagine the things that were on his mind..." ("annoyed", "narrow", "angry", "downR")
    else:
        gen "Yeah? Like what?" ("base", xpos="far_left", ypos="head")
        cho "It's obvious if you ask me, Sir." ("open", "closed", "base", "mid")
        cho "After all, he's just like any boy at this school...{w=0.6} They are all pervs." ("annoyed", "narrow", "angry", "mid")
    cho "He even had the audaciousness to whistle at me, in front of everybody!" ("soft", "narrow", "base", "mid")
    cho "And shout about what a \"great arse\" I have, and that he couldn't wait to \"beat it\"!" ("soft", "narrow", "angry", "mid")
    if states.gen.masturbating:
        gen "Great minds...{w=0.2} *Argh*! think alike!" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Sounds to me like he was just enjoying the view!" ("grin", xpos="far_left", ypos="head")
    cho "Next time he does it I'll turn him into a filthy ferret, I swear!" ("clench", "narrow", "angry", "down")
    cho "" ("annoyed", "narrow", "angry", "mid")
    if states.gen.masturbating:
        gen "{size=-4}(You can do whatever you want with me too, if that's what turns you on baby!){/size}" ("angry", xpos="far_left", ypos="head")
        gen "{size=-4}(I'd love to be your little pet ferret!){/size}" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Your ass is a real head turner, isn't it?" ("base", xpos="far_left", ypos="head")
        cho "To be frank with you, Sir...{w=0.6} I would be disappointed if it wasn't." ("base", "narrow", "base", "mid")
        gen "Why don't you tease him a bit more then? Get him hooked on it..." ("base", xpos="far_left", ypos="head")
        gen "It would be to our benefit, don't you think?" ("base", xpos="far_left", ypos="head")
        cho "*Hmm*{w=0.3} Yes, I could give him a peak once or twice." ("annoyed", "base", "base", "R")
        cho "For as long as I don't have to let him touch it." ("soft", "narrow", "angry", "mid")
        gen "..." ("base", xpos="far_left", ypos="head")
        gen "Anything else you could tell me?" ("base", xpos="far_left", ypos="head")

    # Crabbe & Goyle
    if states.gen.masturbating:
        cho "Then there are the two Slytherin beaters, Crabbe and Goyle..." ("soft", "narrow", "base", "mid")
    else:
        cho "Well, there are also the Slytherin beaters, Crabbe and Goyle..." ("soft", "narrow", "base", "mid")
    cho "Malfoy's extraordinarily dense thugs..." ("angry", "closed", "angry", "mid")
    cho "They've been strutting around school with their two bats..." ("soft", "narrow", "angry", "mid")
    cho "Hitting any girl's bum that happens to be in their reach..." ("annoyed", "narrow", "angry", "R")

    if states.gen.masturbating:
        cho "It's like they use them as target practice." ("soft", "narrow", "angry", "mid")
        gen "*Argh*! {size=-4}(How nasty!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "I dare them to try it on me, those bastards!" ("clench", "narrow", "angry", "R")
        gen "*Yes*! {size=-4}(You deserve a good spanking!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "I saw them go after Katie Bell today." ("soft", "narrow", "base", "mid")
        cho "She was carrying a whole bunch of books...{w=0.8} so she couldn't simply run off or drop them." ("open", "narrow", "angry", "mid")
        cho "She would have probably beaten them up immediately if that wasn't the case. Those cowards..." ("angry", "narrow", "angry", "mid")
        gen "*Yes*! {size=-4}(I wouldn't mind borrowing one of those bats!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "They really did her dirty, Sir.{w} Even pulled down her skirt before they ran off!" ("annoyed", "narrow", "base", "mid")
        gen "What a bunch of daredevils!" ("angry", xpos="far_left", ypos="head")
        cho @ cheeks blush "Her bum was so red afterwards...{w=0.6} It was hard not to look at it..." ("soft", "narrow", "base", "down")
        gen "(Fuck yeah! You'd love to bury your face in some girl's ass, wouldn't you?!)" ("angry", xpos="far_left", ypos="head")
        cho @ cheeks heavy_blush "She really does have a cute bum..." ("horny", "narrow", "base", "downR")
        gen "But not as cute as Granger's, right?" ("angry", xpos="far_left", ypos="head")
    else:
        cho "They aren't even allowed to make use of any Quidditch equipment outside the Quidditch pitch area!" ("soft", "narrow", "angry", "R")
        gen "Aren't you a bit too harsh on them?" ("base", xpos="far_left", ypos="head")
        cho "Sir, since when is sexual harassment tolerated at this school?" ("angry", "closed", "angry", "mid")
        gen "I bet there are many girls who enjoy the occasional spanking..." ("base", xpos="far_left", ypos="head")
        cho "What?" ("soft", "wide", "base", "mid")
        gen "Next time you should ask one of those girls..." ("base", xpos="far_left", ypos="head")
        cho "Why would anyone enjoy that?{w=0.6} How ridiculous." ("soft", "narrow", "angry", "mid")
        gen "They might just be too embarrassed to admit it..." ("base", xpos="far_left", ypos="head")
        cho "" ("annoyed", "narrow", "base", "mid")
        gen "I'm sure miss Granger wouldn't be afraid to admit it, don't you think?" ("base", xpos="far_left", ypos="head")

    cho "Granger?" ("annoyed", "narrow", "angry", "R")
    cho "Don't even talk to me about her..." ("annoyed", "narrow", "angry", "mid")
    cho "She's a hypocrite and a slut..." ("soft", "closed", "base", "mid")
    cho "And I hate her..." ("soft", "narrow", "angry", "mid")
    cho "If you could make her die of embarrassment, I'd be more than thankful for it..." ("annoyed", "narrow", "angry", "mid")
    gen "Embarrass her?{w=0.3} How?" ("grin", xpos="far_left", ypos="head")
    gen "Share some of your ideas with me! I'd love to hear them!" ("grin", xpos="far_left", ypos="head")
    cho "Very well..." ("soft", "closed", "base", "mid")
    cho "(...)" ("annoyed", "base", "base", "R") # Thinks
    cho "(...................)" ("annoyed", "narrow", "angry", "R") # Thinks harder
    if states.gen.masturbating:
        gen "Please?!" ("angry", xpos="far_left", ypos="head")
    else:
        gen "Anything?" ("base", xpos="far_left", ypos="head")
    cho "Oh, I know!" ("smile", "wide", "base", "mid")
    cho "Strip her down, and put her in a pillory!{w=0.8} -- In the middle of the Quidditch pitch!" ("smile", "narrow", "angry", "mid")
    gen "Kinky! I like it!" ("grin", xpos="far_left", ypos="head")
    cho "And let the entire school watch her as she's getting pounded by a horde of centaurs!!!" ("mad", "narrow", "angry", "mid")

    if states.gen.masturbating:
        gen "*Argh*!{w=0.3} {size=-4}(What the hell?){/size}" ("angry", xpos="far_left", ypos="head")
        cho "While there are bludgers flying around -- hitting her disgusting udders..." ("soft", "narrow", "angry", "mid")
        gen "{size=-4}(That sounds really painful!){/size}" ("angry", xpos="far_left", ypos="head")
        nar "*Fap* *Fap* *Fap*!"
        cho "Maybe another centaur takes her from the front..." ("open", "narrow", "angry", "R")
        gen "*Agh*!{w=0.3} {size=-4}(I won't last long if she continues like this!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "And once those two are done breeding her, they trade places with another batch." ("clench", "narrow", "angry", "R")
        gen "*Ahh* {size=-4}(This is getting too crazy!){/size}" ("angry", xpos="far_left", ypos="head")
        cho "Or even better, let some trolls have their way with her!{w=0.8} Let them rip her apart!" ("clench", "base", "angry", "downR")
        gen "*Fuck!* {size=-4}(Come on! Unload! Before it's too late!!!){/size}" ("angry", xpos="far_left", ypos="head")

        # Genie cums.
        call hide_characters
        hide screen bld1
        with d3

        call cum_block
        call gen_chibi("cum_behind_desk")
        with d3
        pause .8

        call bld
        gen "{size=-4}(Yes! Here it comes!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        gen "*Agh*! {size=-4}(Here comes another!){/size}" ("angry", xpos="far_left", ypos="head")

        call cum_block
        gen "*Phew*... {size=-4}(That was close!){/size}" ("base", xpos="far_left", ypos="head")

        # Genie stops.
        hide screen bld1
        with d3
        pause .2

        call gen_chibi("cum_behind_desk_done")
        pause .8

        cho "And put a large bucket under her, so when they--" ("soft", "closed", "base", "mid")
        gen "Stop! No more!" ("angry", xpos="far_left", ypos="head")
        cho "" ("annoyed", "base", "base", "mid")
        gen "I've heard enough!" ("angry", xpos="far_left", ypos="head")
        cho "(...)" ("annoyed", "narrow", "angry", "mid")
        gen "That was...{w=0.3} Very good." ("angry", xpos="far_left", ypos="head")
        cho "Are we done here, Sir?" ("soft", "narrow", "angry", "mid")

    else:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        cho "While there are bludgers flying around, hitting her disgusting udders..." ("soft", "narrow", "angry", "downR")
        gen "*Uhm*..." ("base", xpos="far_left", ypos="head")
        cho "What?!" ("angry", "narrow", "angry", "mid", trans=hpunch) # Angry
        gen "Don't you think that's a bit extreme?" ("base", xpos="far_left", ypos="head")
        cho "Why? For putting Granger in her natural habitat?" ("annoyed", "narrow", "angry", "mid")
        cho "Enclosed on a vast grassy field..." ("soft", "closed", "base", "mid")
        cho "Getting bred by a horde of bulls!" ("soft", "narrow", "base", "mid")
        cho @ cheeks blush "A cow like her would love it..." ("annoyed", "narrow", "base", "downR")
        gen "You seem very interested in the thought of it." ("base", xpos="far_left", ypos="head")
        gen "From my perspective -- it appears that the worse you talk about her -- the more attracted to her you truly are!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "Rubbish..." ("soft", "narrow", "base", "mid")
        gen "Girl, you are in denial!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "I am not!" ("clench", "closed", "angry", "mid")
        cho "Sir, are we done here?" ("soft", "narrow", "angry", "mid")

    if game.daytime:
        cho "I'm late for class." ("soft", "narrow", "angry", "R")
    else:
        cho "I need to get some sleep." ("soft", "narrow", "angry", "R")

    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "*Uhm*... Sure..." ("base", xpos="far_left", ypos="head")
    gen "I suppose we can wrap things up here." ("base", xpos="far_left", ypos="head")
    gen "You are dismissed..." ("base", xpos="far_left", ypos="head")
    cho "Thank you, Sir." ("soft", "closed", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    gen "(Well, that was weird.)" ("base", xpos="far_left", ypos="head")
    gen "(That girl has a very wild imagination, I've got to say...)" ("base", xpos="far_left", ypos="head")
    gen "(Although I have to admit, I'm a bit of a fanboy now...)" ("base", xpos="far_left", ypos="head")
    gen "Go! Go! Ravenclaw!" ("grin", xpos="far_left", ypos="head")

    gen "(These boys do seem to have a particular fetish... Although having Cho confirm it herself should help...)" ("base", xpos="far_left", ypos="head")

    if not states.cho.requests_unlocked:
        call popup("You can yet again buy \"Public Requests\" from Cho!", "Congratulations!", "interface/icons/head/cho.webp")
        $ states.cho.requests_unlocked = True

    jump end_cho_talk_event

label cc_pf_talk_T3_intro_E1:

    call cc_pf_talk

    # Talk about Harry, Mentions Ron

    gen "[name_cho_genie].{w=1.0} Are you in the mood for a little chat?" ("base", xpos="far_left", ypos="head")
    cho "I suppose I am, [name_genie_cho]." ("open", "narrow", "base", "downR")

    # Cho moves to the middle

    cho "..." ("annoyed", "narrow", "base", "downR")
    gen "*Sigh*... What is it?" ("base", xpos="far_left", ypos="head")
    cho "It's Granger. She's been interfering with Quidditch again." ("open", "narrow", "base", "R")
    gen "Of course that's it... Because there's never anything else on your mind..." ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho], Quidditch is important to me!" ("disgust", "narrow", "angry", "mid")
    gen "(I cannot wait until this quid-pitch nonsense is over...)" ("angry", xpos="far_left", ypos="head")
    cho "I won't have her meddling with our training!" ("annoyed", "narrow", "angry", "R")
    cho "I just won't have it!" ("open", "narrow", "angry", "mid")
    cho "[name_genie_cho], please do something about it!" ("angry", "narrow", "base", "mid")
    gen "Alright... Why don't you tell me more, and I'll do my best to listen..." ("base", xpos="far_left", ypos="head")
    cho "Thank you, [name_genie_cho]." ("grin", "closed", "base", "mid")

    menu:
        gen "(Although perhaps I could multitask...)" ("base", xpos="far_left", ypos="head")

        "-Masturbate-":
            $ states.gen.masturbating = True
            call gen_chibi("jerk_off_behind_desk")
            with d5

            cho "[name_genie_cho]!" ("clench", "narrow", "base", "mid")
            gen "What?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Weren't you going to listen to what I had to say?" ("disgust", "narrow", "angry", "mid")
            gen "Yes." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Then why are you jacking off?!" ("upset", "narrow", "angry", "mid")
            "*fap-fap-fap-fap*"
            gen "Why not? I can do both things perfectly fine if I want to..." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Unbelievable..." ("disgust", "narrow", "base", "R")

        "-Pay attention-":
            $ states.gen.masturbating = False

    gen "So tell me, what's Granger up to this time?" ("base", xpos="far_left", ypos="head")
    cho "She won't let me talk to her friends!" ("annoyed", "closed", "angry", "down")
    gen "Her friends?" ("base", xpos="far_left", ypos="head")
    cho "Yeah... Surprising, isn't it?" ("annoyed", "narrow", "base", "mid")
    cho "But yes, Granger does indeed have friends, believe it or not!" ("soft", "narrow", "base", "mid")

    if states.gen.masturbating:
        gen "Are they hot?" ("grin", xpos="far_left", ypos="head")
        cho "..." ("normal", "narrow", "base", "mid")
        gen "Go on..." ("base", xpos="far_left", ypos="head")
        cho "Do I have to answer that?" ("open", "narrow", "base", "downR")
        gen "It would make things go so much quicker." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Alright then..." ("disgust", "closed", "base", "mid")
        "*fap* *fap* *fap*"
        cho @ cheeks blush "Well I suppose they're pretty good-looking." ("open", "narrow", "base", "downR")
        gen "Describe them to me." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "Hmm... Well one's a redhead, lots of freckles, the other is raven-haired, and quite skinny." ("soft", "narrow", "base", "down")
        gen "Nice! I fucking love redheads!" ("grin", xpos="far_left", ypos="head")
        "*Fap* *Fap* *Fap*..."
        gen "Does the carpet match the drapes?" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I don't know, I don't exactly ask random dudes to drop trou for me." ("angry", "narrow", "base", "mid")
        gen "Oh, well... That's understandable--" ("base", xpos="far_left", ypos="head")
        gen "Hold on, did you say dudes?" ("angry", xpos="far_left", ypos="head")
        cho "Yeah, they're both guys." ("disgust", "narrow", "base", "mid")
        gen "Why didn't you say so?!" ("angry", xpos="far_left", ypos="head")
        cho "You didn't ask." ("annoyed", "narrow", "base", "mid")
        gen "Does she not have any hot girlfriends you could tell me about instead?" ("base", xpos="far_left", ypos="head")
        cho "Girlfriends? Well, there's Ginny--" ("soft", "narrow", "base", "R")
        cho "Hey! Don't think I don't know what you're trying to achieve here!" ("angry", "narrow", "angry", "mid")
        cho "Would you please just focus for a minute? Without interrupting me?" ("annoyed", "narrow", "angry", "mid")
        "*Fap* *Fap* *Fap*..."
        cho "And, by Merlin's beard, could you please stop masturbating!" ("scream", "closed", "angry", "mid")
        cho "" ("annoyed", "base", "angry", "mid")
        gen "Fine... I didn't want to finish anyway..." ("base", xpos="far_left", ypos="head") #Genie stops masturbating

        call gen_chibi("sit_behind_desk")

        gen "Who are these boys then?" ("base", xpos="far_left", ypos="head")
    else:
        gen "Is that sarcasm I hear in your voice? Don't tell me you're jealous..." ("base", xpos="far_left", ypos="head")
        cho "Jealous of what? I have better friends than her!" ("soft", "base", "angry", "mid")
        gen "Of course you do." ("base", xpos="far_left", ypos="head")
        cho "What? Are you making fun of me?" ("open", "narrow", "angry", "mid")
        gen "I wouldn't dare, [name_cho_genie], just looking out for you." ("base", xpos="far_left", ypos="head")
        gen "You're a renowned, pretty, and talented little witch... The wrong people could be drawn to you." ("base", xpos="far_left", ypos="head")
        cho "Who cares? I like being popular... At least none of them are as dense as those two..." ("soft", "closed", "angry", "mid")
        gen "Who are you talking about exactly?" ("base", xpos="far_left", ypos="head")

    cho "Potter and Weasley!" ("open", "base", "angry", "mid")
    gen "Could it be... The \"Potter Gang\"?" ("angry", xpos="far_left", ypos="head")
    cho "The what, [name_genie_cho]?" ("angry", "base", "base", "mid")
    gen "That's what Snape called them..." ("base", xpos="far_left", ypos="head")
    cho "*Huh*... Does he now?" ("angry", "narrow", "base", "mid")
    cho "The \"Granger Gang\" would be a more suitable name, if you asked me." ("disgust", "narrow", "base", "R")
    cho "They just blindly follow her and do whatever she says..." ("open", "narrow", "angry", "R")
    cho "I bet they only like her because of her big tits! Those pervs!" ("annoyed", "narrow", "angry", "downR")
    gen "Why do you need to talk to these boys so badly, anyway?" ("base", xpos="far_left", ypos="head")
    cho "Well, for starters... Their seeker... The Potter boy isn't playing fair at all." ("soft", "closed", "angry", "mid")
    cho "Everyone knows Professor McGonagall keeps spoiling him..." ("annoyed", "closed", "angry", "mid")
    cho "She's servicing his equipment on the daily!" ("soft", "narrow", "angry", "mid")
    cho "Once he joined the Gryffindor team, he hasn't needed to polish his handle himself even once." ("open", "narrow", "angry", "downR")
    gen "Not once?" ("base", xpos="far_left", ypos="head")
    gen "Sounds like a real player..." ("base", xpos="far_left", ypos="head")
    cho "I'm certain If I caught him alone I'd be able to get something out of him..." ("normal", "narrow", "angry", "R")
    gen "And what would that be?" ("angry", xpos="far_left", ypos="head")
    cho "If I could just get close enough to get an insight of how he uses his tools..." ("soft", "narrow", "angry", "downR")
    gen "You want to see how he uses his tools?" ("angry", xpos="far_left", ypos="head")
    cho "See? Don't be silly!" ("disgust", "narrow", "angry", "mid")
    gen "Good, I was worried there for a--" ("base", xpos="far_left", ypos="head")
    cho "I want to touch it at the very least! I'd do anything to lay my hands on that magnificent piece of wood of his..." ("open", "narrow", "angry", "mid")
    gen "What!" ("angry", xpos="far_left", ypos="head")
    cho "I fondly remember the day I first laid my eyes on it..." ("base", "closed", "base", "mid")
    cho @ cheeks blush "How could a girl like me not fall in love with it?" ("smile", "closed", "base", "mid")
    gen "(Oh no!)" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "It was the most exquisite piece of wood I had ever seen..." ("grin", "closed", "base", "mid")
    gen "(!!!)" ("angry", xpos="far_left", ypos="head")
    cho "Truly a sight to behold..." ("grin", "base", "base", "mid")
    gen "Certainly it can't be {b}that{/b} impressive." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "There's nothing to even compare it to, [name_genie_cho]! It's magnificent!" ("smile", "base", "base", "mid")
    cho @ cheeks blush "And the way he uses it..." ("smile", "closed", "base", "mid")
    gen "(I can't lose to some meagre mortal!)" ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "I've been trying to ask him to let me ride on it for years but Granger always--" ("soft", "closed", "base", "mid")
    gen "Well luckily for you, [name_cho_genie], you have me!" ("grin", xpos="far_left", ypos="head")
    gen "Just let me take it out of my--" ("base", xpos="far_left", ypos="head")
    cho "You'll get me the firebolt?!" ("angry", "wide", "base", "mid")
    gen "Get you a what, sorry?" ("base", xpos="far_left", ypos="head")
    cho "The firebolt! Surely, you must have seen Potter's?" ("smile", "wide", "base", "mid")
    gen "I most certainly have not!" ("base", xpos="far_left", ypos="head")
    cho "I'm sure if you could get me a broom like that it would assure my--, I mean, our victory!" ("smile", "base", "base", "mid")
    gen "Wait... A broom? That's what all of this is about?" ("angry", xpos="far_left", ypos="head")
    cho "Yes? What else would it be?" ("soft", "narrow", "raised", "mid")
    gen "I'm going to need a moment..." ("base", xpos="far_left", ypos="head")
    cho "[name_genie_cho]?" ("open", "base", "raised", "mid")
    gen "That will be all for today..." ("base", xpos="far_left", ypos="head")
    cho "What about the broom?" ("angry", "base", "base", "mid")
    gen "Enough with the broom!" ("base", xpos="far_left", ypos="head")
    gen "You've got a perfectly good broom already. I don't see why you'd need another one." ("base", xpos="far_left", ypos="head")
    cho "Scrooge..." ("annoyed", "narrow", "base", "R") #sad
    gen "Don't give me that..." ("base", xpos="far_left", ypos="head")

    if broom_2000_ITEM.owned > 0:
        #flag true, if genie owns a dildo broom
        gen "Fine..." ("base", xpos="far_left", ypos="head")
        gen "If you want a new broom this badly then I got just the thing..." ("grin", xpos="far_left", ypos="head")
        cho "Really? Is it the Firebolt?" ("smile", "base", "base", "mid")
        gen "Even better!" ("grin", xpos="far_left", ypos="head")
        cho "A prototype?!" ("grin", "base", "base", "L") # excited
        cho "I heard rumours about a new nimbus--" ("smile", "base", "base", "L")
        gen "Why don't you have a look for yourself, here you go!" ("base", xpos="far_left", ypos="head")
        gen "You can thank me later." ("grin", xpos="far_left", ypos="head")
        nar "You hand the broom to Cho."
        #TODO have it show the broom
        cho "Thank--" ("smile", "narrow", "base", "mid")
        cho "Is that a dildo!?!" ("clench", "wide", "base", "down")
        gen "Yes! I'm sure this will be perfect for our plans!" ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "You can't be serious..." ("disgust", "wide", "base", "mid")
        gen "Why wouldn't I be serious... surely you can't deny this would grab some attention." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "But..." ("angry", "base", "base", "down")
        gen "Yes indeed, that's where one of them--" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "Let's just forget about the idea of a new broom for now..." ("angry", "narrow", "base", "mid")
        gen "But you were so insistent a minute ago..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "No, just forget about it.... Let's try something else..." ("angry", "narrow", "base", "downR")
        gen "Okay then..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I think--{w=0.3} I better--{w=0.3}" ("clench", "narrow", "base", "R")

        if game.daytime:
            cho @ cheeks blush "Head back to class." ("disgust", "narrow", "base", "R")
        else:
            cho @ cheeks blush "Go to bed." ("disgust", "narrow", "base", "R")
        gen "Alright." ("base", xpos="far_left", ypos="head")
    else:
        cho "Okay then..." ("annoyed", "narrow", "base", "R")
        gen "That will be all for today [name_cho_genie]." ("base", xpos="far_left", ypos="head")
        cho "But... I didn't even get to tell you about the other member of Weasley's family--" ("angry", "base", "base", "mid")
        gen "Enough boy talk for today..." ("base", xpos="far_left", ypos="head")
        cho "Sir, but--" ("soft", "base", "base", "mid")
        gen "I said that's enough." ("base", xpos="far_left", ypos="head")
        cho "Fine..." ("annoyed", "narrow", "base", "mid")

        if game.daytime:
            cho "I'll just head back to class then..." ("annoyed", "base", "base", "R")
        else:
            cho "I'll just head off to bed then..." ("annoyed", "base", "base", "R")
        gen "Until next time [name_cho_genie]." ("base", xpos="far_left", ypos="head")

    # Cho leaves.
    call cho_walk(action="leave")

    $ states.cho.mood += 3

    gen "(A Broom... Of course she was talking about a broom.)" ("base", xpos="far_left", ypos="head")

    jump end_cho_talk_event

label cc_pf_talk_T3_intro_E2:

    call cc_pf_talk

    #Mentions the twins and the girls
    gen "Let's have another chat, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho "About Quidditch?" ("smile", "base", "base", "mid")
    gen "About--" ("base", xpos="far_left", ypos="head")
    gen "Why is it always about Quidditch with you?" ("angry", xpos="far_left", ypos="head")
    gen "Don't you have anything else on your mind?" ("base", xpos="far_left", ypos="head")
    cho "Of course I do!" ("soft", "base", "base", "mid")
    cho "But I thought my Quidditch training was the reason you summoned me here, or am I wrong?" ("open", "base", "raised", "mid")
    gen "That was not the reason." ("base", xpos="far_left", ypos="head")
    gen "Now step closer would you?" ("base", xpos="far_left", ypos="head")
    cho "Alright?" ("open", "base", "raised", "mid")

    # Cho moves to desk
    call cho_walk(xpos="desk")

    cho "So, what would you like to talk about, [name_genie_cho]?" ("soft", "narrow", "base", "R")
    gen "I don't know..." ("base", xpos="far_left", ypos="head")
    gen "Cute boys... Or your very attractive male teachers..." ("base", xpos="far_left", ypos="head")
    gen "You know, silly girls stuff..." ("base", xpos="far_left", ypos="head")
    cho "Really?" ("disgust", "narrow", "base", "mid")
    gen "No." ("base", xpos="far_left", ypos="head")
    cho "You know, there are a whole bunch of girls who take Quidditch seriously, just like I do!" ("disgust", "narrow", "base", "mid")
    gen "And I've yet to meet a single one. Except for you, of course..." ("base", xpos="far_left", ypos="head")
    gen "Besides, didn't you and Granger make a huge deal out of it? The lack of acceptance for female players and all that jazz?" ("base", xpos="far_left", ypos="head")
    gen "You both made it seem as if it was a hopeless endeavour to be taken seriously as a female player..." ("base", xpos="far_left", ypos="head")
    cho "That doesn't mean there aren't exceptions." ("angry", "narrow", "base", "mid")
    gen "What do you mean?" ("base", xpos="far_left", ypos="head")
    cho "Gryffindor has plenty of girls on their team!" ("angry", "base", "base", "mid")
    gen "What?! Why didn't you say so sooner?" ("angry", xpos="far_left", ypos="head")
    cho "Besides Potter and the Weasleys, the rest of them are all girls." ("open", "base", "base", "mid")
    gen "Five girls?!?" ("base", xpos="far_left", ypos="head")
    cho "What... No... There's three of them." ("disgust", "base", "base", "mid")
    gen "But you just said--" ("base", xpos="far_left", ypos="head")
    cho "There's Harry Potter, Ron Weasley and his two older twin brothers, Fred and George." ("open", "base", "base", "mid")

    if item_store_intro_done:
        gen "Of course... The twins..." ("base", xpos="far_left", ypos="head")
        gen "As if one weasel wasn't enough." ("base", xpos="far_left", ypos="head")
    else:
        gen "That's a lot of Weasels." ("base", xpos="far_left", ypos="head")

    cho "That's just the ones on their Quidditch team." ("soft", "base", "base", "mid")
    gen "Their parents must've been some busy... Weasels." ("base", xpos="far_left", ypos="head")
    gen "Anyhow, enough about them." ("base", xpos="far_left", ypos="head")
    gen "Tell me everything you know about the girls!" ("grin", xpos="far_left", ypos="head")
    gen "What are their shoe sizes?{w=0.5} No, actually, cup sizes... What are their cup sizes?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "How do you expect me to know?!" ("angry", "base", "base", "mid")
    gen "You're right, I'm getting ahead of myself...{w=0.4} One thing at a time." ("base", xpos="far_left", ypos="head")
    gen "Let's start with their names. What are their names?" ("base", xpos="far_left", ypos="head")
    cho "Well... There's Angelina Johnson, she's their Captain." ("soft", "base", "base", "mid")
    gen "What? I thought the Potter boy was?" ("base", xpos="far_left", ypos="head")
    cho "*Pfff*... What? Don't make me laugh..." ("smile", "narrow", "base", "mid")
    cho "Angelina Johnson has been their captain ever since she took over after Oliver Wood." ("soft", "base", "base", "mid")
    gen "I see... So, the requirement is that your last name has to be an innuendo for male genitalia... Got it." ("base", xpos="far_left", ypos="head")
    gen "What about the other girls? What are their names?" ("base", xpos="far_left", ypos="head")
    cho "Katie Bell and Alicia Spinnet." ("open", "base", "base", "mid")
    gen "Anything important I should know about them?" ("base", xpos="far_left", ypos="head")
    cho "The three of them make up the chaser positions on their team." ("open", "base", "base", "mid")
    gen "A threesome of girls, very nice..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "A threesome?!" ("angry", "narrow", "base", "mid")
    gen "A trio!{w=1.0} A trio of girl chasers, is what I said." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks blush "That's not what I heard..." ("disgust", "narrow", "base", "mid") # suspicious
    gen "(I should distract her.)" ("base", xpos="far_left", ypos="head")
    gen "Girl power!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("disgust", "narrow", "angry", "mid")
    gen "(Task failed successfully!)" ("grin", xpos="far_left", ypos="head")
    gen "So what's their deal then?" ("base", xpos="far_left", ypos="head")
    gen "Anything you can tell me about their... team-play?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Their actual team play?" ("annoyed", "base", "angry", "mid")
    gen "Sure." ("base", xpos="far_left", ypos="head")

    cho "Well, I'd lie if I said that their team play isn't one of their strong suits." ("open", "closed", "angry", "mid")
    cho "When it comes to the girls at least." ("soft", "narrow", "base", "mid")
    cho "Angelina has put a lot more effort into training them than the boys." ("open", "closed", "base", "mid")
    cho "She works them long and hard, the girls always show up late for lessons, or dinner..." ("open", "base", "base", "mid")
    cho "Their training routine must be intense, they always look tired and dishevelled, but also happy, just like me after a hard training session!" ("smile", "base", "base", "mid")

    gen "Girl, you've got this completely wrong..." ("base", xpos="far_left", ypos="head")
    cho "What do you mean, [name_genie_cho]?" ("soft", "base", "base", "mid")
    gen "They're probably doing it." ("base", xpos="far_left", ypos="head")
    cho "Doing what?" ("open", "base", "base", "mid")
    gen "Doing \"it\"...{w} With each other!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yeah, right..." ("base", "narrow", "base", "R")
    cho @ cheeks blush "They do seem pretty close-knit as far as I can tell... But that doesn't mean they're... {i}Doing it{/i}..." ("smile", "narrow", "base", "R")
    gen "Trust me, they're doing it alright." ("base", xpos="far_left", ypos="head")
    gen "And that's great news for us!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Why on earth would that be--" ("disgust", "base", "base", "mid")
    gen "Why there are plenty of ways to take advantage of that." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "[name_genie_cho]?" ("disgust", "narrow", "base", "mid") #shocked
    gen "Just a thought..." ("base", xpos="far_left", ypos="head")
    gen "In any case, you'll have to tell me more about them later... I'm sure we've only scratched the surface regarding those three." ("base", xpos="far_left", ypos="head")
    cho "Alright..." ("annoyed", "base", "base", "mid")

    if game.daytime:
        cho "I'll head back to class in that case." ("open", "base", "base", "R")
        gen "Certainly..." ("base", xpos="far_left", ypos="head")
    else:
        cho "I'll head off to bed then..." ("open", "base", "base", "R")
        gen "Of course..." ("base", xpos="far_left", ypos="head")

    call cho_walk(xpos="door")

    gen "Three girls! Hot damn!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Sigh*..." ("base", "narrow", "base", "down", flip=True)

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_talk_event

label cc_pf_talk_T3_E3:

    $ states.cho.ev.talk_to_me.t3_e3_complete = True

    call cc_pf_talk

    # Talk more about each player. (Detailed descriptions.)

    gen "Let's discuss those girls again..." ("base", xpos="far_left", ypos="head")
    cho "What girls?" ("soft", "base", "base", "mid")
    gen "The ones on the Gryffindor team, of course!" ("base", xpos="far_left", ypos="head")
    cho "Oh, okay then!" ("base", "base", "base", "mid")

    $ _selected = [False, False, False]

    label .choices_female:

    if not all(x == True for x in _selected):

        menu:
            cho "Who would you like to know about?"

            #Lets you pick any order but you do all of them
            #Angelina Johnson
            "\"Tell me more about their Captain, Angelina.\"" if not _selected[0]:
                $ _selected[0] = True

                cho "I'm surprised you remembered her name." ("soft", "base", "base", "mid")
                gen "Of course, she's the one with the Johnson, wasn't she?" ("base", xpos="far_left", ypos="head")
                cho "Her name is Johnson." ("disgust", "narrow", "base", "mid")
                gen "That's the one." ("base", xpos="far_left", ypos="head")
                gen "So what more can you tell me about her--{w=0.2} I mean, Miss Johnson." ("base", xpos="far_left", ypos="head")
                cho "Well, as I said before, Angelina's main focus is on the girls of their team rather than the boys." ("open", "narrow", "base", "mid")
                cho "She's quite temperamental and has little patience with their antics... The twins especially." ("open", "base", "base", "R")
                gen "So she's putting more effort into training the ones that she's sexually involved with?" ("grin", xpos="far_left", ypos="head")
                cho "If that's actually what's happening..." ("open", "narrow", "raised", "mid")
                gen "Preferential treatment in exchange for sex... In my school..." ("base", xpos="far_left", ypos="head")
                cho "Yes, who could've imagined..." ("open", "narrow", "base", "R")
                gen "So there's no synergy between the boys and the girls of their team then?" ("base", xpos="far_left", ypos="head")
                cho "Not really." ("open", "base", "base", "mid")
                gen "Then how the hell did they make the finals?" ("base", xpos="far_left", ypos="head")
                cho "Well, As long as the chasers and beaters have good synergy between each other, then you'll probably be fine." ("soft", "narrow", "base", "mid")
                cho "The girls all play extremely well together and so do the twins." ("soft", "base", "base", "mid")
                cho "The Keeper and seeker sort of do their own thing." ("open", "base", "base", "mid")
                gen "Right... Miss Grangers friends..." ("base", xpos="far_left", ypos="head")
                cho "Yes... To be honest, I doubt Harry and Ron would still be on their team if it wasn't for Angelina's lack of interest in training them..." ("soft", "narrow", "base", "mid")
                gen "Really?" ("base", xpos="far_left", ypos="head")
                cho "Granger is quite protective of her friends but she still lets them play despite having a female captain." ("annoyed", "base", "base", "mid")
                cho "She bosses them around a lot, and would probably feel threatened if Angelina actually did her job properly." ("smile", "narrow", "base", "R")
                gen "*Hmm*... Interesting..." ("base", xpos="far_left", ypos="head")

                jump .choices_female

            #Katie Bell
            "\"Tell me about Katie Bell.\"" if not _selected[1]:
                $ _selected[1] = True

                cho "She's the bell end of the {i}triple threat{/i}." ("smile", "narrow", "base", "mid")
                gen "*Heh*! A bellend... Good one!" ("grin", xpos="far_left", ypos="head")
                gen "Did you come up with that yourself?" ("base", xpos="far_left", ypos="head")
                cho "I did! Surprised?" ("smile", "wink", "base", "mid")
                gen "A little, I didn't think you had it in you." ("base", xpos="far_left", ypos="head")
                cho "I'm full of surprises, [name_genie_cho]." ("smile", "narrow", "base", "mid") # wink
                cho "As for Katie, well... She's a bit weird to be honest..." ("base", "narrow", "base", "R")
                gen "What makes you say so?" ("base", xpos="far_left", ypos="head")
                cho "I don't know... She doesn't talk much, and always seems to have her head in the clouds during practice." ("open", "narrow", "base", "downR")
                gen "I didn't think you flew that high during practice!" ("base", xpos="far_left", ypos="head")
                cho "*Giggles*" ("smile", "narrow", "base", "downR")
                cho @ cheeks blush "..." ("base", "narrow", "base", "downR") #Blushes
                cho "Anyway... Not much else to say about her." ("open", "base", "base", "mid")
                gen "We'll figure something out." ("base", xpos="far_left", ypos="head")

                jump .choices_female

            #Alicia Spinnet
            "\"Tell me about Alicia Spinnet.\"" if not _selected[2]:
                $ _selected[2] = True

                cho "Well, honestly, I find it difficult to dislike her." ("soft", "base", "base", "mid")
                gen "Why is that, isn't she your enemy?" ("base", xpos="far_left", ypos="head")
                cho "*Hmm*... Then let's just say she has my respects." ("base", "base", "base", "downR")
                cho "Whilst Angelina is the captain, she doesn't pay enough attention to the boys--" ("base", "base", "base", "mid")
                cho "--but Alicia has no problem taking control of them." ("soft", "narrow", "base", "mid")
                gen "Taking control?" ("base", xpos="far_left", ypos="head")
                gen "She's a bit of a {i}domina{/i} then?" ("base", xpos="far_left", ypos="head")
                cho "A what?" ("soft", "base", "base", "mid")
                gen "Never mind, please continue..." ("base", xpos="far_left", ypos="head")
                cho "Alicia is very clever, she uses manipulation on people to get her way." ("soft", "narrow", "base", "R")
                gen "Manipulation? How cruel!" ("base", xpos="far_left", ypos="head")
                cho "I'm not exactly sure how she does it, but it works, the boys doesn't seem much wiser about it either." ("base", "narrow", "base", "R")
                gen "(Sounds less like manipulation and more like a female teacher I know...)" ("base", xpos="far_left", ypos="head")
                gen "Anything else you know about her?" ("base", xpos="far_left", ypos="head")
                cho "That about covers it." ("soft", "base", "base", "mid")

                jump .choices_female

    gen "Alright then... I suppose we should discuss those pesky boys as well..." ("base", xpos="far_left", ypos="head")

    $ _selected = [False, False, False]

    label .choices_male:

    if not all(x == True for x in _selected):

        menu:
            #Lets you pick any order but you do all of them
            #Harry Potter
            "\"Tell me about their seeker.\"" if not _selected[0]:
                $ _selected[0] = True

                cho "Harry Potter?" ("soft", "base", "base", "mid")
                gen "The Potter boy!" ("base", xpos="far_left", ypos="head")
                cho "Yes?" ("soft", "base", "raised", "mid")
                gen "I feel like that name should have more importance for some reason..." ("base", xpos="far_left", ypos="head")
                cho "I don't know about that, he seems pretty boring if you ask me." ("open", "narrow", "base", "R")
                gen "What do you know about him? And don't give me another spiel about his broomstick..." ("base", xpos="far_left", ypos="head")
                cho "*Hmm*..." ("soft", "narrow", "base", "downR")
                gen "Any weaknesses?" ("base", xpos="far_left", ypos="head")
                cho "I assume you're not talking about Quidditch." ("open", "narrow", "base", "mid")
                gen "Is he like a boob guy or an ass guy?" ("base", xpos="far_left", ypos="head")
                cho "He's the winning type of guy." ("soft", "closed", "base", "mid")
                gen "So you say you don't know?" ("base", xpos="far_left", ypos="head")
                cho "As I have mentioned before, I haven't been able to talk with him one on one because of Granger..." ("disgust", "narrow", "base", "R")
                cho "All I know is that he's really competitive, his father used to be a great chaser, so I suppose it runs in the family." ("open", "base", "base", "mid")
                gen "Fair enough." ("base", xpos="far_left", ypos="head")

                jump .choices_male

            #Weasley Twins
            "\"Tell me about their beaters.\"" if not _selected[1]:
                $ _selected[1] = True

                cho "That would be the Weasley twins." ("open", "base", "base", "mid")
                gen "Know anything about them?" ("base", xpos="far_left", ypos="head")
                cho "They're tricksters..." ("angry", "narrow", "base", "mid")
                cho "They love controversy and stirring things up for a laugh." ("angry", "base", "base", "mid")
                cho "The type of player that values messing around rather than focusing on winning the game." ("disgust", "narrow", "base", "mid")
                gen "So they're basically trolls?" ("base", xpos="far_left", ypos="head")
                cho "Trolls? *Giggles*" ("smile", "narrow", "base", "mid")
                cho "I know looks can be deceiving, but I don't think they're trolls, [name_genie_cho]." ("smile", "narrow", "base", "R")
                gen "*Hmm*... Maybe not." ("base", xpos="far_left", ypos="head")
                cho "All they care about is that joke shop of theirs..." ("base", "narrow", "base", "R")
                cho "It's everything they ever talk about during lunch." ("base", "base", "base", "mid")
                cho "I feel like if they could and had a good reason to, they'd just ditch school altogether." ("base", "narrow", "base", "downR")
                gen "So, what do you suggest we do against those two?" ("base", xpos="far_left", ypos="head")
                cho "I'm not sure, I think they might enjoy the idea of throwing the game for a laugh, but I doubt their younger brother would forgive them if they did..." ("smile", "base", "base", "mid")
                gen "I see..." ("base", xpos="far_left", ypos="head")

                jump .choices_male

            #Ron Weasley
            "\"Tell me about their keeper.\"" if not _selected[2]:
                $ _selected[2] = True

                cho "That's one of the Weasley brothers... Ron Weasley..." ("open", "base", "base", "mid")
                gen "Wrong Weasley you say..." ("base", xpos="far_left", ypos="head")
                cho "Ron, [name_genie_cho]..." ("soft", "narrow", "base", "mid")
                gen "Oh, sorry... What did you say his name was?" ("base", xpos="far_left", ypos="head")
                cho "...{w} His name is Ron." ("disgust", "base", "base", "mid")
                gen "Right...{w} So what do you know about him?" ("base", xpos="far_left", ypos="head")
                cho "Not much aside from the fact that he's one of Granger's friends..." ("annoyed", "narrow", "base", "mid")
                gen "I see." ("base", xpos="far_left", ypos="head")
                cho "He's a new addition to their team, so I haven't yet been able to see how good he is with a broom." ("open", "base", "base", "mid")
                cho "All I've heard is that he's gone from quite the nervous rookie to a great keeper..." ("soft", "base", "base", "mid")
                gen "Sounds suspicious..." ("base", xpos="far_left", ypos="head")
                cho "It's likely that Granger has been enticing him to do better." ("annoyed", "narrow", "base", "R")
                gen "They aren't dating, are they?" ("base", xpos="far_left", ypos="head")
                cho "No... All I'm saying is that it wouldn't surprise me if Granger had something to do with it." ("annoyed", "narrow", "angry", "downR")
                gen "I see..." ("base", xpos="far_left", ypos="head")
                cho "Granger dating a {i}weasel{/i}... Now that's funny." ("smile", "narrow", "base", "downR")

                jump .choices_male

    gen "Is that all of them?" ("base", xpos="far_left", ypos="head")
    cho "Yes, that's it." ("base", "base", "base", "mid")
    gen "I think I've got a rough idea how to approach this, but..." ("base", xpos="far_left", ypos="head")
    gen "It might be worth learning a bit more about their non-curriculum activities." ("base", xpos="far_left", ypos="head")
    cho "And how do you suggest I do that?" ("open", "base", "base", "mid")
    gen "Espionage!" ("base", xpos="far_left", ypos="head")
    cho "Espionage?" ("soft", "base", "raised", "mid")
    gen "It's worth considering at least, don't you think?" ("base", xpos="far_left", ypos="head")
    cho "*Hmm*... Maybe..." ("soft", "base", "base", "mid")
    gen "Anyway, I think that's enough for now. My attention span only lasts for so long." ("base", xpos="far_left", ypos="head")
    cho "Alright then..." ("open", "base", "base", "mid")
    cho "Until next time." ("base", "base", "base", "mid")

    #Cho leaves
    call cho_walk(action="leave")

    if not states.cho.requests_unlocked:
        call popup("You can yet again buy \"Public Requests\" from Cho!", "Congratulations!", "interface/icons/head/cho.webp")
        $ states.cho.requests_unlocked = True

    jump end_cho_talk_event
