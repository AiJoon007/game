
# Ravenclaw vs Gryffindor

label start_gryffindor_match:
    # Chat with Cho the day before the match

    gen "It's time..." ("base", xpos="far_left", ypos="head")
    cho "Time, [name_genie_cho]?" ("soft", "narrow", "raised", "mid")
    gen "It's Game Time! Get your Hanes on, lace up your Nike's, grab your Wheaties and your Gatorade, and we'll pick up a Big Mac on the way to the ballpark." ("base", xpos="far_left", ypos="head")
    cho "What are you on about?" ("disgust", "narrow", "base", "mid")
    gen "The big game, of course!" ("grin", xpos="far_left", ypos="head")
    cho "The--{w=0.4} Are you talking about the Quidditch Finals?" ("soft", "base", "raised", "mid")
    gen "You got it." ("grin", xpos="far_left", ypos="head")
    gen "Time to put your game face on, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    gen "I hope you've had some practice on that broom." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I... Yes, you could say that." ("open", "narrow", "base", "downR")
    gen "Great." ("base", xpos="far_left", ypos="head")
    gen "And what of our tactics?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "*Huh*?" ("soft", "base", "base", "mid")
    gen "Did riding that thing make you forget about them?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Of course not!" ("clench", "narrow", "base", "R")
    cho @ cheeks blush "\"Get close to the enemy team, and annoy Hermione as much as possible\"." ("open", "closed", "angry", "mid")
    gen "Precisely!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("soft", "narrow", "base", "mid")
    gen "If you do well enough, I'm confident we'll be victorious before the game even starts!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "If we're lucky..." ("soft", "narrow", "base", "downR")
    gen "Luckily for us -- Luck has got nothing to do with it this time." ("base", xpos="far_left", ypos="head")
    cho "{size=-4}Let's hope you're right...{/size}" ("annoyed", "narrow", "base", "downR")
    gen "Besides, we both know she can't take her eyes off of you, even if she wanted to." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "What's that supposed to mean?" ("angry", "wide", "base", "mid")

    menu:

        "-Tell Cho that she's obviously looking out for foul play-":
            $ states.cho.ev.quidditch.hermione_affection = "neither"

            gen "Err... To keep an eye out for any foul activity. Obviously." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Foul play? What do you mean?" ("clench", "narrow", "base", "R")
            gen "Like someone smacking some Gryffinwhore's ass!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "Oh... As if I would ever pull a stunt like that..." ("base", "narrow", "base", "R")
            gen "Isn't that the plan?" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "Oh, right..." ("soft", "base", "base", "mid")
            gen "You seem oddly distracted today [name_cho_genie]." ("base", xpos="far_left", ypos="head")

        "-Tell Cho that Hermione obviously Likes her-": #(Happens on cc_pf_strip_T2_intro_E3 which is mandatory)
            $ states.cho.ev.quidditch.hermione_affection = "hermione"

            gen "Isn't it obvious?" ("base", xpos="far_left", ypos="head")
            gen "The girl has been checking you out ever since she caught you in my office." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "W-what? That's nonsense!" ("disgust", "narrow", "base", "R")
            gen "Is it? Could've fooled me with how she reacted when you displayed that firm body of yours." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "But--" ("disgust", "base", "base", "mid")
            gen "Especially once she saw those firm buns you grip that broom with." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "She- She looked at my--" ("mad", "narrow", "base", "mid")
            gen "Of course! Who wouldn't if a toned and hot young gal such as yourself stood in front of them." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "I... I have never thought that she--" ("disgust", "narrow", "base", "down")
            gen "Now, now, there's no need to be overthinking it. Let's focus on responsibilities first, pleasantries second." ("base", xpos="far_left", ypos="head")

        "-Tell Cho that she obviously likes Hermione-": #(Cho sees Hermione's Naked body when Tonks transforms)
            $ states.cho.ev.quidditch.hermione_affection = "cho"

            gen "Is it really important to know why?" ("base", xpos="far_left", ypos="head")
            gen "We both know you enjoyed seeing her naked body as much as I did." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "N-No I did not!" ("angry", "happyCl", "angry", "mid")
            gen "It's obvious... You should've seen your flustered face." ("base", xpos="far_left", ypos="head")
            gen "You could tell from a mile off with how much those cheeks lit up." ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "B-but she's..." ("clench", "narrow", "base", "mid")
            gen "Such prejudice is unacceptable in my school, Miss Cho!" ("base", xpos="far_left", ypos="head")
            cho @ cheeks blush "(That's not what I meant...)" ("disgust", "narrow", "base", "R")
            gen "We'll get back to it later, for now though, let's focus on what's important." ("base", xpos="far_left", ypos="head")

    gen "Tomorrow's the day, the highlight of your career!" ("base", xpos="far_left", ypos="head")
    gen "Make sure to enjoy it, it's all downhill from there." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Huh?" ("angry", "base", "raised", "mid")
    gen "Sports are all about money after all. Not everyone is prepared to get tossed around and transferred between different teams like property." ("base", xpos="far_left", ypos="head")
    cho "Tossed around, [name_genie_cho]? I'm sorry, I'm a little confused..." ("disgust", "narrow", "base", "mid")
    gen "I know the feeling... Enough about that, you've got a game to win!" ("base", xpos="far_left", ypos="head")
    gen "Go-go Ravenclaw!" ("base", xpos="far_left", ypos="head")
    cho "Right..." ("disgust", "base", "base", "mid")

    if game.weather in {"rain", "storm"}:
        cho "Let's just hope it stops raining before then." ("soft", "base", "base", "R")
    elif game.weather in {"snow", "blizzard"}:
        cho "Let's just hope it stops snowing before then." ("soft", "base", "base", "R")
    elif game.weather == "overcast":
        cho "Let's just hope the weather doesn't get worse." ("soft", "base", "base", "R")
    else:
        cho "Let's hope the weather stays like it is." ("soft", "base", "base", "R")

    gen "Get yourself ready, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    gen "And remember, keep your eyes on the prize!" ("base", xpos="far_left", ypos="head")
    cho "The cup..." ("smile", "narrow", "base", "R") #stare, smile

    hide cho_main
    with d3

    #Cho turns around (CG maybe?)
    call cho_chibi(flip=True)
    with d3

    gen "(That ass...)" ("grin", xpos="far_left", ypos="head")

    call cho_walk(action="leave")

    $ states.cho.busy = True
    $ cc_event_pause  += 1 # Event starts on the next day
    $ cc_summon_pause += 1 # Can't be summoned until next event

    $ states.cho.ev.quidditch.lock_training = True
    $ states.cho.ev.quidditch.lock_practice = True

    $ states.cho.ev.quidditch.gryffindor_stage = "start"

    jump end_cho_event

#Next day
#Cho flies up in the window and reminds genie about the game
label gryffindor_match:

    label .introspection1: # not required, but added for clarity

    if _in_replay:

        show screen blkfade
        with d5

        $ game.gold = 1984
        $ game.day = 665
        $ game.daytime = True
        $ game.weather = "clear"
        call room("main_room")

        hide screen blkfade
        with d5

    # Quidditch match: Ravenclaw vs. Gryffindor

    $ lun_outfit_last.save()
    $ her_outfit_last.save()
    $ ton_outfit_last.save()
    $ cho_outfit_last.save()

    # $ luna.equip(lun_outfit_lion)
    $ hermione.equip(her_outfit_default)
    $ tonks.equip(ton_outfit_default)
    $ luna.equip(lun_outfit_lion_event)

    $ cho.equip(cho_outfit_quidditch)
    $ cho.set_pose("broom")
    $ cho.animation = sprite_fly_idle

    $ snape_chibi.zorder = 4
    $ tonks_chibi.zorder = 3
    $ hermione_chibi.zorder = 6
    $ genie_chibi.zorder = 5

    play music "music/Brittle Rille.ogg" fadein 1 if_changed

    gen "*Yawn*" ("base", xpos="far_left", ypos="head")

    if _in_replay:
        nar "Cho hovers on her broom outside the window, just below Genie's line of sight."
        cho "(Oh coach...)"
        cho "(I should have pushed harder on the broom being an issue earlier...)"

        play music "music/marty-gots-a-plan-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

        cho "(How do I tell him that his plan isn't going to work?)"
        cho "(But... What if he's got a backup plan?)"
        cho "(I'll have to ask him!)"

        cho "[name_genie_cho]!"

        cho "(Wait, he's expecting me to drink the potion as a backup!)"
        cho "(I'll just tell him I came to fetch--)"

        gen "I'm such an idiot!" ("angry", xpos="far_left", ypos="head")

        cho "(Is he talking to himself?)"
        cho "(I should say something, so he won't think I've been eavesdropping.)"

    else:
        gen "(Alright then, time to get up and moving.)" ("base", xpos="far_left", ypos="head")
        gen "(Today is going to be a good day, I can feel it in those old bones!)" ("grin", xpos="far_left", ypos="head")
        gen "(Seeing Cho on that broom again, and wiping the smirk off Snape's smug face when she stomps those--)" ("grin", xpos="far_left", ypos="head")

        stop music fadeout 1

        gen "(Hold on...)" ("base", xpos="far_left", ypos="head")

        play music "music/marty-gots-a-plan-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed

        gen "(The final match...)" ("base", xpos="far_left", ypos="head")
        gen "{size=-4}*Murmur*...{w=0.4} I feel like I've forgotten something...{/size}" ("base", xpos="far_left", ypos="head")
        gen "(Hold your carpets!)" ("angry", xpos="far_left", ypos="head")
        gen "(Since it's the finals... That means no more matches!)" ("angry", xpos="far_left", ypos="head")
        gen "(Cho won't have any more reason to let me coach her!)" ("angry", xpos="far_left", ypos="head")
        gen "(I've been so focused on Snape and our stupid bet that I didn't even begin to see the bigger picture!)" ("base", xpos="far_left", ypos="head")
        gen "(What good for is money when there's not a single brothel you can spend it at.)" ("base", xpos="far_left", ypos="head")
        gen "(There's only so many sweets and clothes one can buy...)" ("base", xpos="far_left", ypos="head")
        gen "(*Hmm*...)" ("base", xpos="far_left", ypos="head")
        gen "(Perhaps I could pay her to--)" ("base", xpos="far_left", ypos="head")

        # Note: I've tried using chibis, but it's too difficult/buggy.

        #Cho appears in the window on her broom/knocks on door
        #show image "ch_cho fly_window_masked" onlayer screens zorder 5
        #call cho_chibi("fly_window", "mid", "base")

        cho "[name_genie_cho]!"

        if states.cho.ev.suck_it.variant == "points":
            gen "(No, she got pissed when I offered points before.)" ("base", xpos="far_left", ypos="head")
            gen "(Even now I can hear her calling me out, and who knows what she would do if I offered her real money...)" ("base", xpos="far_left", ypos="head")
        else:
            gen "(Nah, I can hear her screaming at me in my head.)" ("base", xpos="far_left", ypos="head")
            gen "(All she cares about is that broomstick sport of hers.)" ("base", xpos="far_left", ypos="head")

        gen "I'm such an idiot!" ("angry", xpos="far_left", ypos="head") # Says out loud
    cho "Hey, [name_genie_cho]!"
    cho "The game is about to start... You're going to be late!"
    gen "W-What..." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand", 225, "base")
    with d3
    # Genie jumps to his feet

    gen "Who said that?!" ("angry", xpos="far_left", ypos="head")

    call gen_chibi("stand_alt")
    with d3

    gen "[name_cho_genie]?" ("base", xpos="far_left", ypos="head")
    gen "What are you doing in here?" ("base", xpos="far_left", ypos="head")
    gen "Or rather, what are you doing {i}out there{/i}, outside my window?" ("base", xpos="far_left", ypos="head")

    if _in_replay:
        cho "(I screwed up the whole plan, I poured out the potion you left for me, the broom isn't working, and my world is crumbling to pieces!)"
        cho "(...)"

    cho "I flew up here to remind you about the finals, [name_genie_cho]."

    gen "Ah yes, I suppose I better get going..." ("base", xpos="far_left", ypos="head")
    call gen_chibi("stand") # Genie slowly walks away.
    with d3
    call gen_walk(path=[(210, 470), (390, 470), (410, 420)], speed=0.5)
    cho "Aren't you going to wish me luck?"
    call chibi_emote("thought", "genie")
    pause 1.5
    call chibi_emote("hide", "genie")
    gen "Yeah, good luck..." ("base", xpos="far_left", ypos="head")
    call gen_walk(xpos="mid", ypos="base", speed=0.75)
    cho "Are you alright, [name_genie_cho]?"
    gen "It's nothing, don't worry about it..." ("base", xpos="far_left", ypos="head")
    gen "Meet you at the pitch." ("base", xpos="far_left", ypos="head")
    cho "Alright... See you at the pitch then."

    call gen_walk(action="leave")

    cho "(That's weird. He didn't make even a single dirty joke.)"
    cho "(Is it because--)"
    cho "(No, that's impossible... is it?)"

    #Cho flies off

    #Blackfade
    show screen blkfade
    with d5

    stop music fadeout 1

    # Used in Quidditch Outro
    if _in_replay:
        return

    play sound "sounds/steps_grass.ogg"
    nar "You begin making your way down to the pitch."
    nar "After struggling to navigate the Great staircase and the indistinguishable corridors, you finally find the way to the entrance of the pitch."
    nar "Reaching the entrance, you hear the murmurs of the crowd die down, signalling that the match is about to begin."
    nar "You quickly climb the steep staircase up the commentator's tower."

    #Pitch Background sun high variant, Snape is at the podium with Hermione to the side of him. Tonks is at the back
    #Genie appears at the back

    call room("quidditch_stands",)
    call quidditch_stands(weather="sun_high", crowd=crowd_full)
    call ton_chibi("stand", 212, 318, flip=True)
    call sna_chibi("stand", 280, 400, flip=True)
    call her_chibi("stand", 260, 440, flip=True)
    play background "sounds/crowd_very_low.ogg" fadein 10
    with d5

    pause 0.5
    call gen_chibi("stand", 148, 346, flip=True)
    with d3
    pause 0.5

    ton "{size=-4}Thank Merlin, you're here...{/size}" ("normal", "base", "shocked", "R", ypos="head", flip=True) #whisper
    #genie walks next to Tonks # <- Not possible to do.
    ton "{size=-4}Where have you been?{/size}" ("open", "base", "base", "mid") #whisper
    gen "{size=-4}You'd think that in a place of magic, there'd be some better means of transport than simply walking...{/size}" ("base", xpos="far_left", ypos="head") #whisper
    gen "{size=-4}What's Snape doing?{/size}" ("base", xpos="far_left", ypos="head") #whisper
    #Snape middle of the screen standing
    sna "And seeing that our dear headmaster couldn't make it today, it's fallen upon me--" ("snape_24", flip=True, xpos=340, ypos="base", trans=d5)
    ton "{size=-4}The headmaster is supposed to kick off the final game, you better get up there.{/size}" ("soft", "base", "base", "R")
    gen "{size=-4}I feel like I should be getting briefed on these things...{/size}" ("base", xpos="far_left", ypos="head")
    sna "So...{w=0.4} Everyone do your best...{w=0.4} And stuff like that..." ("snape_25", flip=True, xpos=340, ypos="base", trans=d5)

    call gen_chibi("stand", 180, 435, flip=True)
    call her_chibi("stand", 260, 440, flip=True)
    with d3

    #Genie walks down to the podium next to Hermione
    nar "You walk up to Hermione and notice that she is looking tentatively at whatever Snape is trying to achieve."

    menu:
        "-Slap her ass-":
            call slap_her

        "-Give her a headpat-":
            pass

    play sound "sounds/gasp3.ogg"
    pause 0.5

    call gen_chibi("stand", 170, 435, flip=True)
    call her_chibi("stand", 270, 440, flip=False)
    with d3

    her "Professor!" # She turns around and sees Genie, but Snape thinks she's calling for him.
    sna "What is it now Miss--" ("snape_07", flip=True, xpos=340, ypos="base", trans=d5)

    #Snape turns to Hermione and sees genie
    call sna_chibi("stand", 280, 400, flip=False)
    call gen_chibi("stand", 170, 435, flip=True)
    call her_chibi("stand", 270, 440, flip=False)
    hide snape_main
    with d3

    sna "Oh..."
    gen "I'll take it from here if you don't mind..." ("base", xpos="far_left", ypos="head")
    sna "As you wish..."

    #Snape walks back to the seats
    call gen_chibi("stand", 280, 400, flip=True)
    call sna_chibi("stand", 148, 340, flip=True)
    call her_chibi("stand", 260, 440, flip=True)
    with d3

    #Team introductions
    #microphone feedback
    play sound "sounds/microphone_feedback.ogg"
    gen "Ladies and gentlemen!" ("base", xpos="far_left", ypos="head")
    gen "*Ahem*...{w=0.4} One moment, please." ("base", xpos="far_left", ypos="head")

    #Genie turns back to Tonks
    call gen_chibi("stand", 280, 400, flip=False)
    call her_chibi("stand", 260, 440, flip=True)
    with d3

    gen "What was I supposed to do again?"
    ton "Introduce the teams and kick off the finals!" ("scream", "base", "base", "L")
    gen "Oh right..."
    #turns to audience
    call gen_chibi("stand", 280, 400, flip=True)
    call her_chibi("stand", 260, 440, flip=True)
    with d3

    hide screen genie_main
    with d3
    pause .8
    play sound "sounds/killswitch_on.ogg"
    stop background fadeout 3.0
    hide screen blktone
    call quidditch_stands(spotlight=True)
    pause 1.5

    sna "Dear lord... Always with the dramatics..." ("snape_06", xpos="base", ypos="head", flip=False)

    gen "" ("base", xpos=0, ypos="base")
    show genie zorder states.gen.image.zorder
    with d3

    gen "*Ahem*...{w=0.4}{nw}" ("grin")

    play sound "sounds/microphone_feedback2.ogg"

    gen "*Ahem*...{fast} Testing, testing, is this thing still on?" ("grin")
    sna "..." ("snape_11", xpos="base", ypos="head", flip=False)

    gen "Perfect!" ("grin")

    play background "music/fanfare.ogg" fadeout 3 fadein 1.0

    gen "Now, this is it ladies and gentlemen!" ("grin")
    gen "The most important game of these incredible athletes' careers!" ("open")
    sna "What's he on about now?" ("snape_06")
    gen "I wish for everyone to put in their best efforts today, and make today's match, {b}the{/b} match that you'll talk about with your children and grandchildren!" ("base")
    gen "Remember this moment!" ("open")
    gen "Cherish it!" ("open")
    gen "It's all you'll have once you're fifty, and stuck in your boring nine-to-five desk job!" ("angry")

    #murmurs
    call quidditch_stands(crowd_react=["emoq", "qu", None])
    play sound "sounds/murmur.ogg"
    gen "Now, let's welcome and give it up for our first team!" ("open")
    call quidditch_stands(crowd_react=[None, None, None])
    gen "Team Gryffindor!" ("open")

    #cheers
    call quidditch_stands(crowd_react=["emo8", "th", "emo8"])
    play sound "sounds/crowd_cheer.ogg"
    pause 2.0
    call quidditch_stands(crowd_react=[None, None, None])

    gen "We've got some incredible athletes coming up today!" ("base")
    gen "Give a round of applause to the team captain and chaser...{w=0.4} Angelina Johnson!" ("open")

    #cheers
    call quidditch_stands(crowd_react=["emo8", "sal", "emo8"])
    play sound "sounds/crowd_cheer.ogg"
    pause 2.0
    call quidditch_stands(crowd_react=[None, None, None])

    gen "And now...{w=0.4} The two other chasers of Team Gryffindor, Alicia Spinnet and Katie Bell!" ("open")

    #cheers
    call quidditch_stands(crowd_react=["emo8", "sal", "emo8"])
    play sound "sounds/crowd_cheer.ogg"
    pause 2.0
    call quidditch_stands(crowd_react=[None, None, None])

    gen "And lest we forget the twins, now walking onto the pitch--" ("open")

    gen "{size=-4}Psst... [name_hermione_genie], what were their names again?{/size}" ("base")
    her "The Beaters? Fred and--" ("open", "happy", "base", "mid", xpos="base", ypos="head", flip=False)

    play sound "sounds/microphone_feedback.ogg"

    #cheers
    call quidditch_stands(crowd_react=["emo8", "emo7", "qu"])
    play sound "sounds/crowd_cheer.ogg"

    gen "{size=+2}{i}The beater{/i} brothers!{/size}" ("open")

    her "Sir..." ("disgust", "base", "base", "mid")
    call quidditch_stands(crowd_react=[None, None, None])

    gen "{size=-4}What position were they again?{/size}" ("base")
    her "That's what I--" ("angry", "narrow", "base", "mid")

    play sound "sounds/microphone_feedback.ogg"
    gen "{size=+2}Hold on, the next guy is coming up...{/size}" ("base")

    #gasp
    $ renpy.music.set_volume(0.0, delay=2.0, channel="background")
    pause 1.0

    gen "It's...{w=0.4} *Err*...{w=0.4} You know who!{w=0.3}{nw}" ("open")

    $ renpy.music.set_pause(True, channel="background")
    play sound "sounds/crowd_gasp.ogg"
    call quidditch_stands(crowd_react=["excl", "emo8", "excl"])

    gen "It's... *Err*... You know who!{fast}" ("base")
    gen "You know who it is, it's another one of those red haired guys!" ("base")
    sna "..." ("snape_11", xpos="base", ypos="head", flip=False)
    gen "What?{w} Not a fan?" ("base")

    call quidditch_stands(crowd_react=[None, None, None])
    $ renpy.music.set_pause(False, channel="background")
    $ renpy.music.set_volume(1.0, delay=1.0, channel="background")

    gen "Don't listen to them, boy. Just get out there and show who's boss, boss man!" ("base")
    her "..." ("disgust", "happy", "worried", "mid")
    gen "And now... Last but not least, who else but the Potter boy!" ("base")

    call quidditch_stands(crowd_react=["emo8", "th", "emo8"])
    play sound "sounds/crowd_cheer.ogg"
    gen "Yeah! We all know that guy!" ("grin")

    call quidditch_stands(crowd_react=[None, "excl", None])
    "This one guy" "Booooo! You suck!"
    call quidditch_stands(crowd_react=[None, None, None])
    gen "Wait, who said that?" ("open")
    sna "..." ("snape_47") # smirks

    gen "I bet it was one of you Slut-herians." ("angry")
    gen "Wait. I meant Sly-therians." ("angry")
    gen "Slipperins?" ("base")
    gen "I give up... Anyway." ("base")
    gen "Snape never stops talking about this Potter guy! So he must be good!" ("grin")
    sna "What is he--" ("snape_25")
    gen "That Potter gang this and that..." ("grin")
    sna "I'm going to jinx him into oblivion--" ("snape_32")
    ton "You will do no such thing. Let me take care of it." ("mad", "narrow", "base", "L", ypos="head", flip=False)

    #Tonks walks down
    call sna_chibi("stand", 168, 326, flip=True)
    call ton_chibi("stand", 250, 380, flip=True)
    call gen_chibi("stand", 280, 400, flip=True)
    call her_chibi("stand", 260, 440, flip=True)
    with d3

    gen "*Hah-Hah*... That guy sure is a prevalent character!" ("grin")
    ton "I think it might be best if Miss Granger took over the introductions..." ("open", "base", "raised", "R")

    call ton_chibi("stand", 250, 380, flip=True)
    call gen_chibi("stand", 280, 400, flip=False)
    call her_chibi("stand", 260, 440, flip=True)
    play sound "sounds/killswitch_off.ogg"
    call quidditch_stands(spotlight=False)
    hide genie
    with d3

    pause 0.5

    gen "But I haven't gotten to the good part yet!" ("angry", xpos="far_left", ypos="head")
    ton @ hair upset "*piercing gaze*" ("normal", "narrow", "annoyed", "mid") #The look
    gen "Fine..." ("base")

    call ton_chibi("stand", 250, 380, flip=True)
    call gen_chibi("stand", 280, 400, flip=True)
    call her_chibi("stand", 260, 440, flip=True)
    play sound "sounds/killswitch_on.ogg"
    call quidditch_stands(spotlight=True)
    with d3

    gen "" (xpos=0, ypos="base")
    show genie zorder states.gen.image.zorder
    with d3
    gen "Go team, go Tune Squad!" ("grin")
    hide genie
    with d3
    gen "" (xpos="far_left", ypos="head")

    play background "sounds/crowd_low.ogg" fadein 5 fadeout 5
    play sound "sounds/crowd_cheer.ogg"

    play sound "sounds/killswitch_off.ogg"
    call quidditch_stands(spotlight=False)
    pause 1

    $ snape_chibi.zorder = 3
    $ tonks_chibi.zorder = 4

    call sna_chibi("stand", 150, 290, flip=True)
    call ton_chibi("stand", 130, 310, flip=True)
    call gen_chibi("stand", 168, 326, flip=True)
    call her_chibi("stand", 300, 400, flip=True)
    hide genie
    with d3

    #Genie and Tonks head back to the seats
    #Hermione goes up to the podium
    her "*Ahem*..." ("soft", "happy", "base", "R", xpos=290, ypos="base", flip=True, trans=d5)
    her "Moving on..." ("open", "happy", "base", "L")
    her "What could only be described as a debut at the Quidditch Finals..." ("grin", "closed", "base", "L")
    her "A surprise to everyone, I'm sure..." ("grin", "base", "base", "L")
    her "A surprise to everyone, I'm sure...{fast} Team Ravenclaw!" ("scream", "base", "base", "L")

    hide hermione_main
    with d3

    play sound "sounds/crowd_cheer2.ogg"
    call quidditch_stands(crowd_react=["emo8", "th", "emo8"])
    nar "Cheering from the Ravenclaw students erupts, but is soon drowned out by excessive booing and jeering from the Slytherin crowd."
    call quidditch_stands(crowd_react=[None, None, None])

    gen "{size=-4}Why'd you cut me off like that?{/size}" ("base", xpos="far_left", ypos="head") #Whisper
    sna "{size=+12}*Breathing heavily*{/size}" ("snape_43")
    gen "{size=-4}What's up with him?{/size}" ("base", xpos="far_left", ypos="head")
    ton "{size=-4}Trust me...{w=0.4} It was for your own good.{/size}" ("soft", "narrow", "base", "R")
    sna "{size=-4}\"He never stops talking about him\" he says...\n{/size}{w=0.4}How {w=0.2}{size=+4}{b}dare{/b}{/size} {w=0.2}you--" ("snape_12")
    ton "{size=-2}Let's just focus on the game, shall we?{/size}" ("open", "base", "raised", "R")
    sna "Fine...{w=0.4} Count yourself lucky our bet is still up." ("snape_01")
    gen "I don't doubt you've got some filthy tricks up your sleeves again." ("base", xpos="far_left", ypos="head")
    sna "Says you." ("snape_39")
    sna "And I don't know what you're talking about...{w=0.4} I'm just here to watch the game." ("snape_37") # Recovers himself
    gen "{size=+4}Don't play dumb with me. Tell me what you're planning!{/size}" ("angry", xpos="far_left", ypos="head")
    sna "As I said--" ("snape_01")
    ton "*Sigh*...{w=0.4} You boys and your silly bets." ("open", "narrow", "shocked", "downR")

    label .introspection2:

    if _in_replay:

        $ cho.equip(cho_outfit_quidditch_gryffindor)
        $ game.gold = 1984
        $ game.day = 667
        $ game.daytime = True
        $ game.weather = "clear"
        $ snape_chibi.zorder = 3
        $ tonks_chibi.zorder = 4
        call room("quidditch_stands",)
        call quidditch_stands(weather="sun_high", crowd=crowd_full)
        call sna_chibi("stand", 150, 290, flip=True)
        call ton_chibi("stand", 130, 310, flip=True)
        call gen_chibi("stand", 168, 326, flip=True)
        call her_chibi("stand", 300, 400, flip=True)

        play background "sounds/crowd_low.ogg" fadein 1 fadeout 5

        hide screen blkfade
        with d5

    her "--And finally, making their way onto the pitch..." ("angry", "happy", "base", "L", xpos=290, ypos="base", flip=True, trans=d5)
    her "The Ravenclaw seeker...{w=0.6}{nw}" ("open", "base", "base", "L")

    play sound "sounds/crowd_cheer.ogg"
    call quidditch_stands(crowd_react=["emo8", "emo7", "emo8"])

    her "The Ravenclaw seeker...{fast} Cho Chang!" ("scream", "base", "base", "L")

    her "Hold on...{w=0.4} Why is she already on her broom?" ("disgust", "happy", "base", "L")
    nar "You look down the pitch, and watch Cho as she slowly hovers up to her team, smiling awkwardly towards Madam Hooch."

    play sound "sounds/crowd_cheer2.ogg"
    "The Crowd" "Cho! Cho! Cho!"

    # Used in Quidditch Outro
    if _in_replay:
        return

    her @ cheeks blush "*Hmph*...{w=0.4} It appears some of us aren't here just for sports." ("open", "squint", "annoyed", "L")
    call quidditch_stands(crowd_react=[None, None, None])
    sna "She sure has become quite popular amongst the students hasn't she." ("snape_37")
    ton @ hair horny "*Mhmm* And not just amongst students..." ("horny", "narrow", "base", "stare")

    #Whistling (catcalling)
    play sound "sounds/wolf_whistle.ogg"
    call quidditch_stands(crowd_react=[None, "emo7", None])

    mal "Show us your tits!"
    her @ cheeks blush "Settle down, please." ("open", "squint", "annoyed", "L")

    play sound "sounds/wolf_whistle2.ogg"
    call quidditch_stands(crowd_react=["emo8", None, None])

    fem "Shake that booty, sister!"
    stop background fadeout 3.0
    play sound "sounds/kick.ogg"
    with hpunch
    play background "sounds/wind_long_loop.ogg" fadein 3 fadeout 2
    call quidditch_stands(crowd_react=[None, None, None])
    her @ cheeks blush "{size=+10}Quiet!{/size}" ("scream", "closed", "angry", "L") #big text

    #crowd dies down
    her @ cheeks blush "" ("normal", "narrow", "angry", "L") #big text
    play sound "sounds/cough_male.ogg"
    mal "..."


    her @ cheeks blush "Good." ("grin", "base", "base", "L")
    her @ cheeks blush "Then perhaps we could get to watching some actual Quidditch today." ("grin", "base", "base", "L")
    her "Madam Hooch, when you're ready." ("open", "squint", "base", "L")

    pause 1
    #Whistle sound
    play sound "sounds/referee.ogg"
    play background "sounds/crowd_very_low.ogg" fadein 5 fadeout 5
    play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
    pause .4

    hide hermione_main
    with d3

    nar "As the balls are released, Cho shoots straight up into the air to get an overview of the game."
    sna "Already up to her usual schemes I see..." ("snape_03")
    gen "You bet." ("grin", xpos="far_left", ypos="head")
    gen "(Let's hope she's had enough practice, bonding with that broom...)" ("base", xpos="far_left", ypos="head")
    play sound "sounds/ball_hit.ogg"
    her "Katie Bell, of course, has already gotten a hold of the quaffle, and is speeding up towards Ravenclaw's side of the pitch!" ("grin", "squint", "base", "L", xpos=290, ypos="base", flip=True, trans=d5)
    her "Davies is moving up to intercept--{w=0.2}" ("angry", "squint", "base", "L")
    #her "Watch out Katie!!" ("base", "base", "base", "mid") # Confusing.

    #Hit sound
    #crowd groan
    play sound ["sounds/card_punch4.ogg", "sounds/crowd_ouch.ogg"]
    with hpunch
    pause 1.0

    her "*Hah*! Fred Weasley hit him right on his side with a bludger!" ("smile", "squint", "base", "L")
    hide hermione_main
    with d3

    ton "{size=-4}She's sure improved a lot on her commentating since the first game.{/size}" ("base", "narrow", "base", "R", xpos="far_right", ypos="head", flip=False) #whisper
    sna "{size=-4}She's clearly got a bias towards her own house...{/size}" ("snape_01")
    ton "{size=-4}Don't you start--{/size}" ("soft", "narrow", "annoyed", "R")
    nar "Ignoring the two, you look up towards Cho who is fidgeting around a bit on her new broom."
    ton "{size=-4}Didn't you give some Slytherin girl fifty points the other night--{/size}" ("soft", "narrow", "annoyed", "R")
    sna "{size=-4}*Ahem*...{w=0.4} Voice down, please {b}Nymphadora{/b}.{/size}" ("snape_14")

    $ tonks.set_body_hue(280)
    play sound "sounds/kettle.ogg"
    ton "What did I tell you about calling me--" ("mad", "wide", "annoyed", "mid", animation=shake) with d9 #fuming
    gen "I'm trying to watch the game here..." ("base", xpos="far_left", ypos="head")
    $ tonks.set_body_hue(0)
    ton "He started it..." ("mad", "narrow", "annoyed", "mid", animation=None)
    sna "No, you did!" ("snape_17")
    gen "*Sigh* Like children." ("base", xpos="far_left", ypos="head")

    show screen blkfade
    hide tonks_main
    with d5

    #Fade black
    #Set background to sun low
    call quidditch_stands(weather="sun_low")

    nar "Some time passes and you watch Gryffindor score even more goals as Cho fruitlessly tries to get comfortable on her broom."

    hide screen blkfade
    with d5

    #Fade back to pitch

    sna "What's she up to anyway? She looks like a niffler who's got caught stealing their grandmother's brooch." ("snape_01")

    label .introspection3:

    if _in_replay:

        #Shifts to new view of Cho Doll flying in the air (her perspective when genie starts gesticulating wildly to have her spank the enemy on their ass)
        # TODO: No idea what view is supposed to be.

        show screen blkfade
        with d5

        $ cho.equip(cho_outfit_quidditch_gryffindor)
        $ game.gold = 1984
        $ game.day = 667
        $ game.daytime = True
        $ game.weather = "clear"
        $ snape_chibi.zorder = 3
        $ tonks_chibi.zorder = 4
        call room("quidditch_stands",)
        call quidditch_stands(weather="sun_high", crowd=crowd_full)
        call sna_chibi("stand", 150, 290, flip=True)
        call ton_chibi("stand", 130, 310, flip=True)
        call gen_chibi("stand", 168, 326, flip=True)
        call her_chibi("stand", 300, 400, flip=True)

        play music "music/machinations-by-kevin-macleod.ogg" fadein 1 fadeout 1 if_changed
        play background "sounds/crowd_low.ogg" fadein 1 fadeout 5

        hide screen blkfade
        with d5

        cho "(Come on... This stupid broom!)"
        cho "(Get it going already!)"
        cho "(Why...{w=0.4} Can't...{w=0.4} I...{w=0.6} Get Horny!!)"

        nar "Cho, frustrated in a multitude of ways, looks down towards the commentator's tower in desperation."
        nar "She notices her coach making funny faces and gesticulating wildly."

        cho "(What is he doing...)"
        cho "(Oh! The other part of our plan! Get close to the enemy team!)"

        show screen blkfade
        with d5

        stop background fadeout 1

        nar "Cho gets close to one of the enemy chasers, Katie Bell."

        cho "Hey Katie!"
        "Katie" "Not now Cho, I'm a little busy if you haven't noticed!"
        cho "Cannot say that I have. All I see is you staring at Alicia's butt."
        "Katie" "Are you trying to piss me off, little raven?"
        cho "So what if I am?"
        "Katie" "Nice try, but I won't lose my temper, unlike you, I am trying to win this game--"

        #Spank sound
        play sound "sounds/slap_02.ogg"
        "*Smack*!!" with hpunch

        nar "Cho smacks Katie on her shapely bum."
        "Katie" "*Owww*!!"
        play sound "sounds/giggle2_loud.ogg"
        cho "*Imitates Katie's voice* \"Ohh yes Alicia, please spank me harder\"!"
        "Katie" "H-How--"
        nar "Cho grins at her briefly, then swiftly flies away."
        "Katie" "Why you little--"

        play sound "sounds/giggle2.ogg"

        nar "Katie dashes after Cho."
        "Katie" "Come back here, I'm not done with you!"

        play background "sounds/crowd_low.ogg" fadein 1 fadeout 5
        hide screen blkfade
        with d3

        #Hermione turns around
        call her_chibi("stand", 300, 400, flip=False)
        with d3

        "Hermione" "Sir!"
        cho "(Finally! That's done it!)"
        "Hermione" "*inaudible*"
        cho "(Look at her going, she's bound to distract her team for me!)"
        gen "*Shrugs*"
        "Hermione" "*inaudible shouting*"

        call her_chibi("stand", 300, 400, flip=True)
        with d3

        nar "Hermione gritting her teeth holds back her anger, and eventually resumes commentating the game."

        #Shifts to screen of Cho Doll flying in the air

        show screen blkfade
        with d5

        nar "Cho is being chased by Katie, but not for long, as Angelina's attention turns to them."
        "Angelina" "What the hell are you doing, Katie?!"
        "Katie" "N-Nothing, I'm just--"
        "Angelina" "I don't wanna hear it, just get back to the game!"
        "Katie" "... Yes ma'am."
        nar "Katie gives up the chase, glaring daggers at Cho."

        cho "(What the--)"
        cho "(It didn't work!?!)"
        cho "(Our Plan! What am I supposed to do now?!)"

        hide screen blkfade
        with d5

        call chibi_emote("thought", "genie")
        call chibi_emote("thought", "snape")

        nar "Cho looks down towards her Coach, who appears to be in some sort of argument with Professor Snape."

        call chibi_emote("hide", "genie")
        call chibi_emote("hide", "snape")

        "Hermione" "Another goal for Team Gryffindor!"

        cho "(Another goal!)" #Worried
        "Hermione" "And with such a steady lead, soon it won't even matter if Ravenclaw catches the snitch or not!"
        nar "Moving her gaze away from her coach, Cho briefly locks eyes with Hermione."
        cho "(Stupid bitch!)"
        cho "(Stupid broom!)"
        cho "(Now where's that--{w=0.4} Stupid--{w=0.4} snitch!?)"

        show screen blkfade
        with d5

        nar "Cho begins to feverishly look around for the snitch, her eyes darting around the pitch."
        nar "Unable to locate it, she looks back towards the commentator's tower for assistance."

        call gen_chibi("hide")

        hide screen blkfade
        with d5

        cho "(Where did he vanish?!)"

        "Hermione" "A fantastic--{w=0.4} Hold on...{w=0.4} What's that on the pitch? Is that--"

        nar "Cho watches her coach dash through the pitch with inhuman speed."

        cho "(What the--{w=0.4} Where's he going?)"

        pause 0.3

        call room("quidditch_stands2")
        call quidditch_stands2(weather="sun_low", crowd=crowd_full)
        call lun_chibi(xpos=620, ypos=400)
        play background "sounds/crowd_low.ogg" fadein 1 fadeout 5
        show image Transform("images/misc/redhead.webp", zoom=0.26, pos=(805, 240), xzoom=-1) as redhead zorder 2
        show screen blkfade
        with ComposeTransition(pushleft, before=faderight)
        hide screen blkfade
        with ComposeTransition(pushleft, after=faderight)

        #Camera transitions and Genie appears in Luna's tower on the opposite side of the pitch

        play sound "sounds/run_02.ogg"
        pause 1.5

        call gen_chibi("stand", 780, 480, flip=False)
        with d3
        call gen_walk(xpos=740, ypos=470)

        pause 0.5

        call gen_chibi(flip=True)
        with d3

        cho "(Is he talking to Gi--)"
        cho "(Hold on... What's that thing near the balustrade... Is that... Luna?!)"

        lun "*Waves at Cho*" ("grin", "happyCl", "base", "mid", xpos="right", ypos="base", trans=d3)

        $ luna.hide()
        with d3

        cho "(What is she wearing?!)"

        #Genie walks down to Luna.
        call gen_walk(xpos=650, ypos=430)

        #Hit sound
        play sound "sounds/ball_hit.ogg"

        "Hermione" "Ouch... What a blunder! Surely he should've seen that coming!" #big text
        gen "*Inaudible*"
        "Hermione" "Katie Bell passing to Alicia Spinnet..." #text larger
        cho "(Oh right, I did ask him to get someone to cheer for me...)"
        "Hermione" "Expertly dodging a bludger..." #text larger
        cho "(...)"
        "Hermione" "Coming up towards the goal..." #text larger
        cho "(To think he'd go so far as asking Loony Luna...)"
        "Hermione" "Gryffindor!" #text larger
        cho "(He still believes I can do it without the potion...)"

        nar "Staring into the distance, Cho begins shuffling on her broom, thinking hard on what to do..."

        cho "(If I can't get this stupid broom going... Then what else could I do...)"

        #Cut to cho Doll flying

        nar "Glancing towards the commentator booth, Cho's eyes are once again drawn towards Hermione, who is grinning from ear to ear, and jumping on the spot excitedly."
        nar "Cho moves her gaze away from Hermione angrily, promptly staring into space, trying to figure out what to do next."

        cho "(Think, Cho... Think...)"
        cho "(What would coach tell me to do...)" #closes eyes to think

        # Note: We need to make a call because we already are in Replay scope
        call cc_pf_strip_T2_intro_E1.introspection

        $ cho.equip(cho_outfit_quidditch_gryffindor)
        $ cho.set_pose("broom")
        $ cho.animation = sprite_fly_idle
        $ game.gold = 1984
        $ game.day = 667
        call room("quidditch_stands2")
        call quidditch_stands2(weather="sun_low", crowd=crowd_full)
        call lun_chibi(xpos=620, ypos=400)
        show image Transform("images/misc/redhead.webp", zoom=0.26, pos=(805, 240), xzoom=-1) as redhead zorder 2
        call gen_chibi("stand", 650, 430, flip=False)
        play background "sounds/crowd_low.ogg" fadein 1 fadeout 5

        hide screen blkfade
        with d5

        cho "(That's not it...)" #blush, open eyes
        "Hermione" "{{Gryffindor scores another goal!}"

        play sound "sounds/crowd_cheer.ogg"

        cho "..." #angry #eyes closed

        call cc_pf_blowjob_T3_intro_E1.introspection

        $ cho.equip(cho_outfit_quidditch_gryffindor)
        $ cho.set_pose("broom")
        $ cho.animation = sprite_fly_idle
        $ game.gold = 1984
        $ game.day = 667
        call room("quidditch_stands2")
        call quidditch_stands2(weather="sun_low", crowd=crowd_full)
        call lun_chibi(xpos=620, ypos=400)
        show image Transform("images/misc/redhead.webp", zoom=0.26, pos=(805, 240), xzoom=-1) as redhead zorder 2
        call gen_chibi("stand", 650, 430, flip=False)

        hide screen blkfade
        with d5

        cho "(Yes coach... But what am I supposed to do?)"
        gen "Go on, girl. Start with the top..." ("grin", xpos="far_left", ypos="head", animation=Transform(alpha=0.5))
        cho "(Coach... Please, this isn't the time--)"
        cho "(Hold on...)"
        cho "(That's it!!)" #open eyes wide
        cho "(Granger...)" #mischievous
        cho "(She'll be furious...)" #horny
        cho "(But... Doing it in front of the entire school...)"

        nar "Cho shifts around slightly on her new broom and suddenly finds herself able to slide up and down the dildo effortlessly."
        cho "(...{w} Well then...)"

        stop background fadeout 0.5

        #Cho flies off the screen

        return

    else:
        gen "(Come on, girl...{w=0.4} Focus.)" ("base", xpos="far_left", ypos="head")
        gen "(Get that broom going...)" ("base", xpos="far_left", ypos="head")

        nar "Cho, frustrated in a multitude of ways, looks down towards you in desperation."

        menu:
            "-Give her a sign-":
                nar "You begin moving one of your hands in a spanking motion."
                nar "Her expression changes as she stares at you in confusion."
                nar "You put your other hand out over what could only be described as an imaginary ass and begin spanking the air violently."
                ton "Professor?" ("soft", "base", "raised", "mid") #Confused

            "-Point towards the Gryffindor players-":
                nar "You point towards the Gryffindor side of the pitch."
                nar "Cho looks at you confused, and then points towards that side as well."
                nar "Shaking your head, you point towards one of the female players."

            "-Give her a seductive look-":
                nar "You begin fluttering your eyelashes up towards Cho."
                nar "She looks down at you in confusion."
                nar "You lick your lips and give her a wink."
                nar "Looking at you in horror for a brief moment, she then finally understands what you were trying to say."

        nar "Cho gives you a quick nod and then flies up towards one of the Gryffindor chasers who have positioned themselves near the Ravenclaw goalposts."

        her "Johnson passing to Spinnet--" ("grin", "base", "base", "L", xpos=290, ypos="base", flip=True, trans=d5)

        #Spank sound
        play sound "sounds/slap_02.ogg"
        "*Smack*!!"
        her @ cheeks blush "What the--" ("soft", "wide", "base", "up")
        her @ cheeks blush "What is Cho doing?" ("disgust", "wide", "base", "up")

        hide hermione_main
        with d3

        #Hermione turns around
        call her_chibi("stand", 300, 400, flip=False)
        with d3

        her @ cheeks blush "Sir!" ("disgust", "narrow", "annoyed", "mid", xpos=290, ypos="base", flip=False, trans=d5)
        her @ cheeks blush "She--{w=0.2} She smacked one of the chasers on the bum..." ("angry", "happy", "annoyed", "mid")
        her @ cheeks blush "Sir, you can't let her get away with this!" ("clench", "happy", "annoyed", "mid")
        gen "I'm not hearing any objections from the referee...{w=0.5} Or the player, matter-of-factly..." ("base", xpos="far_left", ypos="head")
        gen "Unless she used her elbows, that's not against the rules." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "But...{w=0.4} Sir!" ("disgust", "base", "annoyed", "mid")
        gen "I didn't write the rules, Miss Granger..." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "*Tsk*..." ("soft", "happy", "angry", "R")

        hide hermione_main
        with d3

        call her_chibi("stand", 300, 400, flip=True)
        with d3

        nar "Hermione gritting her teeth holds back her anger, and eventually resumes commentating the game."
        nar "Looking up at Cho, you see a mix of frustration and worry across her face as she flies off again."

        gen "{size=-4}Damn it...{/size}" ("base", xpos="far_left", ypos="head") #whisper
        sna "{size=-4}Miss Chang isn't doing so well this time, is she?{/size}" ("snape_05") #whisper
        sna "{size=-4}It appears your feeble attempts at riling up Miss Granger were in vain.{/size}" ("snape_37") #whisper
        gen "{size=-4}How did you--{/size}" ("angry", xpos="far_left", ypos="head") #whisper
        sna "{size=-4}Why, you were the one who told me about their contempt for each other when we made our little bet.{/size}" ("snape_02") #whisper
        gen "..." ("base", xpos="far_left", ypos="head")
        ton "*Hmm*?" ("soft", "base", "base", "R")
        sna "{size=-4}That little witch has successfully been making my life a misery since the moment she got here.{/size}" ("snape_01")
        sna "{size=-4}To think that Miss Chang would be able to rile her up...{/size}" ("snape_37")
        her "Another goal for Team Gryffindor!" ("crooked_smile", "happy", "base", "L", xpos=290, ypos="base", flip=True, trans=d5)

        #crowd cheer
        play sound "sounds/crowd_cheer.ogg"
        call quidditch_stands(crowd_react=["th", None, "emo8"])

        sna "Go-Go Gryffindor..." ("snape_37") #Smugface, out loud
        call quidditch_stands(crowd_react=[None, None, None])
        her "And with such a steady lead, soon it won't even matter if Ravenclaw catches the snitch or not!" ("smile", "base", "base", "L")

        hide hermione_main
        with d3

        gen "Hold the fuck up." ("angry", xpos="far_left", ypos="head")
        gen "No one has told me that's a thing! I thought the rules were set up in favour of the protagonist!" ("angry", xpos="far_left", ypos="head")

        if quidditchguide_ITEM.used:
            sna "I see someone hasn't been paying attention to the \"Basics of Quidditch\"." ("snape_41")
            gen "Of course I did, I just... forgot." ("base", xpos="far_left", ypos="head")
            sna "Oh well, perhaps next time... Oh wait, there's no next time..." ("snape_46")
        else:
            sna "Of course, you can win the game even without your team being the ones to catch the snitch, albeit it is very uncommon..." ("snape_41")
            sna "Perhaps if you'd learnt the actual game, you wouldn't need to rely on silly rules like excessive elbow usage..." ("snape_46") # smug

        gen "{size=-4}Smug bastard...{/size}" ("base", xpos="far_left", ypos="head")
        sna "I'll take that as a compliment." ("snape_37")

        nar "As you turn your gaze back to Cho, you see her eyes darting around, seemingly searching for the snitch."
        gen "(Damn it... She's lost all confidence in our plan!)" ("base", xpos="far_left", ypos="head")
        gen "(Hold on...{w=0.4} Yes! That's it, confidence!)" ("base", xpos="far_left", ypos="head")
        gen "Tonks, Where's Lovegood?" ("base", xpos="far_left", ypos="head")
        ton "Lovegood, sir?" ("soft", "base", "base", "mid")
        gen "Yes, what tower is she in?" ("base", xpos="far_left", ypos="head")
        ton "Oh, Miss Lovegood... She should be in that one across the pitch--" ("open", "base", "raised", "mid")

        #Genie chibi disappears
        play sound "sounds/run_02.ogg"
        call gen_chibi("hide")

        ton "Where are you going?!" ("clench", "wide", "base", "mid")

        with hpunch
        play sound "sounds/falling_stairs.ogg"

        #Falls down stairs
        pause 2.0
        sna "*Tsk*, *Tsk*...{w=0.4} The sense of imminent loss must've been too much for him." ("snape_37")

        her "A fantastic--{w=0.4}{nw}" ("grin", "base", "base", "L", xpos=290, ypos="base", flip=True, trans=d5)
        her "A fantastic--{fast} Hold on...{w=0.4} What's that on the pitch?{nw}" ("soft", "narrow", "base", "L")
        her "A fantastic-- Hold on... What's that on the pitch?{fast} Is that--" ("clench", "wide", "base", "L")
        play sound "sounds/murmur.ogg"
        sna "What the--" ("snape_25")
        sna "He's going to blow our cover, running like that!" ("snape_32")
        ton "Focus on the game, Miss Granger!" ("scream", "wide", "base", "mid")
        her "R-Right!" ("mad", "happy", "base", "L")
        her "Fred--{w=0.2} I mean, George Weasley intercepting a bludger--" ("scream", "squint", "base", "L")
        hide screen bld1
        hide hermione_main
        with d3

    pause 0.3

    call room("quidditch_stands2")
    call quidditch_stands2(weather="sun_low", crowd=crowd_full)
    call lun_chibi(xpos=620, ypos=400)
    show image Transform("images/misc/redhead.webp", zoom=0.26, pos=(805, 240), xzoom=-1) as redhead zorder 2
    show screen blkfade
    with ComposeTransition(pushleft, before=faderight)
    hide screen blkfade
    with ComposeTransition(pushleft, after=faderight)

    #Camera transitions and Genie appears in Luna's tower on the opposite side of the pitch

    play sound "sounds/run_02.ogg"
    pause 1.5

    call gen_chibi("stand", 780, 480, flip=False)
    with d3
    call gen_walk(xpos=740, ypos=470)

    gen "*Ah*...{w=0.4} *Ah*...{w=0.4}  Stairs...{w=0.4}  Why did it have to be--" ("base", xpos="far_left", ypos="head")
    "Cute Redhead" "Professor Dumbledore?"

    call gen_chibi(flip=True)
    with d3

    gen "I don't have the time for this, girl... Where's Lovegood?" ("base", xpos="far_left", ypos="head")
    "Cute Redhead" "Luna Lovegood? She's up there by the front."

    #Genie walks down to Luna.
    call gen_walk(xpos=650, ypos=430)

    gen "Lovegood! Where's your cheerleading squad?!" ("base", xpos="far_left", ypos="head")
    gen "What the hell are you wearing?" ("base", xpos="far_left", ypos="head")

    #Luna doll shows with her wearing the lion outfit
    lun "Oh, hello sir! Come to cheer with me?" ("smile", "base", "base", "R", xpos="right", ypos="base", trans=d3)
    gen "What in the great desert sands is this..." ("base", xpos="far_left", ypos="head")
    lun "Great isn't it! Would you like to try on my lion head?" ("grin", "base", "base", "R")
    gen "Lion head--" ("base", xpos="far_left", ypos="head")
    gen "...{w=1.0} Miss Lovegood." ("base", xpos="far_left", ypos="head")
    lun "Yes?" ("grin", "base", "raised", "R")
    gen "When I told you to cheer..." ("base", xpos="far_left", ypos="head")
    gen "Did you not think I meant for your own house?!" ("angry", xpos="far_left", ypos="head")
    lun "My own...{w=0.4}{nw}" ("open", "base", "raised", "R")
    lun "My own...{fast} Oooooh!" ("soft", "base", "base", "stare")

    #Hit sound
    play sound "sounds/ball_hit.ogg"

    "Hermione" "{{Ouch... What a blunder! Surely he should've seen that coming!}" #big text
    gen "You absolute--" ("base", xpos="far_left", ypos="head")
    "Hermione" "{{Katie Bell passing to Alicia Spinnet...}" #text larger
    gen "Do you even use your--" ("base", xpos="far_left", ypos="head")
    "Hermione" "{{Expertly dodging a bludger...}" #text larger
    gen "I thought I told you to bring your friends--" ("base", xpos="far_left", ypos="head")
    "Hermione" "{{Coming up towards the goal...}" #text larger
    lun "I can't hear you, sir!" ("mad", "base", "base", "R")
    gen "Why would I ask you to cheer for--" ("base", xpos="far_left", ypos="head")
    "Hermione" "{{Gryffindor!}" #text larger

    #Crowd cheer
    play sound "sounds/crowd_cheer.ogg"
    lun "Yaaaay!" ("grin", "base", "base", "stare")
    gen "..........." ("base", xpos="far_left", ypos="head") # At a loss for words; Requires more dots. :P
    lun "Sorry, what did you say, sir?" ("grin", "base", "base", "R")
    play sound "sounds/crowd_stomping.ogg"
    gen "Take that stupid-- off!" ("base", xpos="far_left", ypos="head")
    lun "Take off what--" ("angry", "base", "base", "R")
    gen "Now!" ("base", xpos="far_left", ypos="head")
    lun "Okay!" ("angry", "happyCl", "base", "mid")

    #Luna takes off trousers
    play sound "sounds/cloth_sound3.ogg"
    $ luna.strip("bottom")
    with d3

    pause 1.0

    gen "What are you doing?!" ("angry", xpos="far_left", ypos="head")
    "Cute Redhead" "Oh my..."

    lun "I'm doing what you asked, sir." ("clench", "base", "base", "mid")

    gen "I told you to take off that stupid head of yours--" ("base", xpos="far_left", ypos="head")
    gen "No. Wait. You're confusing me again..." ("angry", xpos="far_left", ypos="head")
    gen "What I meant to say is, could you kindly take off that lion costume of yours... please..." ("base", xpos="far_left", ypos="head")

    lun "Oh, right, no problem! You could've just said so from the start, professor!" ("grin", "base", "base", "mid")

    gen "*sigh*..." ("base", xpos="far_left", ypos="head")

    #Luna puts trousers back on
    $ luna.wear("bottom")
    with d3

    pause 0.5

    $ luna.strip("accessory")
    with d3

    pause 0.5

    nar "Glancing up at Cho, you see her looking towards the commentator booth."
    gen "I hope she didn't see you..." ("base", xpos="far_left", ypos="head")
    lun "Who?" ("soft", "base", "base", "up")
    gen "It doesn't matter, I'll be heading back now." ("base", xpos="far_left", ypos="head")
    lun "Oh, okay!" ("base", "base", "base", "mid")
    gen "(I hope Cho doesn't think that I left the pitch...)" ("base", xpos="far_left", ypos="head")

    #Genie chibi goes to the back of the seats
    lun "Bye then, Professor!" ("smile", "base", "base", "mid")

    hide luna_main
    hide screen bld1
    with d3

    play sound "sounds/run_02.ogg"
    call gen_chibi("hide")
    with d3
    pause 1.0

    lun "*Hmm*... He never said I cannot put it back on..." ("open", "base", "base", "down", trans=d8)

    play sound "sounds/cloth_sound3.ogg"
    $ luna.wear("all")
    with d3

    pause 1.0

    #Genie chibi disappears
    "Hermione" "{{Gryffindor scores another goal!}" #text larger


    #Crowd cheer
    play sound "sounds/crowd_cheer.ogg"
    lun "Yaaaay!" ("smile", "base", "base", "stare") # Happy, eyes closed
    hide luna_main
    hide screen bld1
    with d3

    call room("quidditch_stands")
    call quidditch_stands(weather="sun_low", crowd=crowd_full)
    call sna_chibi("stand", 150, 290, flip=True)
    call ton_chibi("stand", 130, 310, flip=True)
    call her_chibi("stand", 300, 400, flip=True)
    hide image redhead
    show screen blkfade
    with ComposeTransition(pushright, before=fadeleft)
    hide screen blkfade
    with ComposeTransition(pushright, after=fadeleft)

    # Camera transitions back to commentator booth

    #Tonks and Snape are talking before genie arrives
    sna "--And that's how I invented a potion for treating genital warts." ("snape_37", trans=d3)
    ton "Fascinating... Truly..." ("open", "narrow", "base", "R", trans=d3)

    play sound "sounds/run_02.ogg"
    pause 1.5

    call gen_chibi("stand", 168, 326, flip=True)
    with d3

    gen "*Heavy panting*" ("base", xpos="far_left", ypos="head")
    ton "Thank Merlin..." ("disgust", "base", "base", "mid")
    gen "I'll never look at staircases the same way..." ("base", xpos="far_left", ypos="head")
    sna "There he is." ("snape_02")
    ton "What was that all about?" ("soft", "base", "raised", "mid")
    gen "*Err*...{w=0.4} Don't worry about it..." ("base", xpos="far_left", ypos="head")
    gen "How's the game going?" ("base", xpos="far_left", ypos="head")
    ton "Gryffindor scored another goal." ("open", "base", "base", "mid")
    nar "You look up at Cho who is staring blankly into the distance."
    gen "What's she doing?" ("base", xpos="far_left", ypos="head")
    sna "Finally..." ("snape_47")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    nar "Cho's expression changes abruptly into one of determination as she starts attempting to catch the attention of the boys on the Gryffindor team."

    #At this point, Cho has taken the luck potion and its effect is starting to kick off. Snape's "finally" comment confirms that something happened. His smugness goes up from this point as in his mind it doesn't matter who wins if Cho is caught cheating since the victory would go to Gryffindor.

    her "Davies taking a nasty bludger--{w=0.2}{nw}" ("open", "base", "base", "up", trans=d3)
    her "Davies taking a nasty bludger--{fast} Hold on... what is--" ("clench", "base", "base", "up")
    # Cuts to Cho who has taken off Gloves, goggles and leggings. Still wearing top, skirt, bra
    # Cho takes her top off

     # Transition to Cho on her broom
    $ cho.equip(cho_outfit_quidditch_gryffindor)
    $ cho.set_pose("broom")
    $ cho.animation = sprite_fly_idle

    call cho_chibi("fly", 1100, 140)
    call cho_walk(530, 360, speed=2)
    pause 1

    call cho_chibi("fly", flip=True)

    play background "sounds/crowd_very_low.ogg" fadein 10
    cho "That's right boys, look this way!" ("smile", "narrow", "base", "L", xpos=580, ypos=-200, flip=True, trans=d3)

    $ cho.strip("top")
    with d3

    pause .8

    her "Chang, what are you doing!?" ("disgust", "wide", "angry", "L", trans=d3)
    cho "What does it look like I'm doing?" ("grin", "narrow", "base", "R")

    $ cho.strip("accessory")
    with d3

    pause .8

    her @ cheeks blush "You're--" ("mad", "wide", "angry", "L")

    if states.cho.ev.quidditch.hermione_affection == "hermione": # If Genie told Cho that Hermione likes her.
        cho @ cheeks blush "Do you like the view?" ("smile", "narrow", "base", "R")
        her @ cheeks blush "What are you--" ("angry", "happy", "angry", "L")
        cho @ cheeks blush "Shush. You don't have to answer that, I already know the truth." ("base", "narrow", "base", "R")

    elif states.cho.ev.quidditch.hermione_affection == "cho": # If Genie told Cho that she likes Hermione.
        her @ cheeks blush "Why are you taking your clothes off?!" ("angry", "wide", "angry", "L")
        cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "L")
        cho @ cheeks heavy_blush "Do you... like the view?" ("soft", "narrow", "base", "R")
        her @ cheeks blush "Do {i}I{/i} What?!" ("angry", "happy", "base", "L")
        cho @ cheeks heavy_blush "Don't be shy now, you can look as much as you want." ("base", "narrow", "base", "R")

    else: # If genie was clueless (generic response)
        # Note: We're using 'else' check here in case player uses cheats. It is equivalent of `states.cho.ev.quidditch.hermione_affection == "neither"`.
        cho "I'm taking my clothes off!" ("grin", "narrow", "base", "R")

    her @ cheeks blush "Why are you doing this?" ("mad", "happy", "angry", "L")
    cho @ cheeks blush "Why?" ("smile", "narrow", "raised", "R")
    cho @ cheeks blush "Well, I thought I'd give your friends a bit of a show." ("grin", "narrow", "base", "R")
    cho @ cheeks blush "Don't you think they deserve to look at something nice for once?" ("base", "narrow", "raised", "R")
    her @ cheeks blush "What?!" ("upset", "wide", "base", "L")

    gen "Oh no she didn't..." ("grin", xpos="far_left", ypos="head")

    "Harry" "*drools audibly*" # el yu el
    "Ron" "Hubba hubba!" # el yu el bis

    cho @ cheeks blush "It appears looks beats brains yet again." ("base", "narrow", "base", "L")
    her @ cheeks blush "I--{w=0.4} I--" ("angry", "narrow", "worried", "L")

    play sound "sounds/crowd_cheer.ogg"
    nar "Hermione's gaze moves to her friends as a cheer from the Ravenclaw stands erupts as they score a goal."

    her @ cheeks blush "Guys! Ignore that floozy and focus on the game!" ("scream", "happyCl", "angry", "mid", trans=d3)
    cho @ cheeks blush "" ("smile", "narrow", "base", "L")
    nar "Cho smirks as even the Gryffindor girls stop to ogle at her."

    her @ cheeks blush "S--{w=0.2} Stop that! Stop staring at her." ("mad", "squint", "worried", "L")

    hide hermione_main
    with d3

    gen "She's got their team under a spell." ("base", xpos="far_left", ypos="head")


    ton @ hair horny "*Mmm*... Me too..." ("horny", "narrow", "base", "mid")

    sna "Now this is a plan I can get behind." ("snape_02")
    gen "Hah! Yeah, this was my plan alright..." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "But perhaps we should call for a--" ("soft", "base", "base", "R")
    her "{size=+7}Boys!{/size}" with hpunch
    nar "The boys quickly snap out of it and move their gaze towards the commentator booth."

    $ hermione.strip("top")

    #Gasp from crowd
    play sound "sounds/crowd_gasp.ogg"
    her @ cheeks blush "" ("base", "closed", "angry", "mid", trans=d3)
    cho @ cheeks heavy_blush "" ("clench", "wide", "base", "R")
    call ctc

    her @ cheeks blush "I believe I told you to stop looking at her!" ("grin", "narrow", "base", "L")
    gen "Miss Granger!" ("base", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush hair horny "Oh dear..." ("soft", "base", "base", "mid")
    her @ cheeks blush "You boys are despicable!" ("open", "closed", "angry", "mid")
    her @ cheeks blush "Why would you pay any attention to that walking stick when the girls of your own house are a hundred times more appealing!" ("disgust", "squint", "angry", "L")
    cho @ cheeks heavy_blush "*inaudible noise*" ("disgust", "narrow", "angry", "R")
    her @ cheeks blush "What was that?" ("grin", "squint", "base", "L")
    her @ cheeks blush "Sorry I can't hear you over the wind... You'll have to speak up." ("grin", "narrow", "base", "L")

    $ cho.strip("bra")
    with d3

    #Gasp from crowd
    play sound "sounds/crowd_gasp.ogg"
    cho @ cheeks heavy_blush "" ("smile", "narrow", "angry", "R")
    her @ cheeks blush "" ("clench", "wide", "base", "L")
    nar "Staring daggers at Hermione, Cho takes off her bra and drops it to the ground."

    gen "Now that's my attention-seeker!" ("grin", xpos="far_left", ypos="head")
    #Crowd stomping
    play sound "sounds/crowd_stomping.ogg"
    qcr "Cho! Cho! Cho!"

    ton @ cheeks blush hair horny "*Hmm*... We should probably put a stop to this..." ("disgust", "base", "base", "mid")
    her @ cheeks blush "*Grr*!!!" ("clench", "wide", "angry", "stare_soft")
    ton @ hair upset "*Ehm*...{w=0.4} Why don't you do it, Severus?" ("mad", "narrow", "shocked", "R")

    #Hermione takes off bra
    $ hermione.strip("bra")
    with d3
    her @ cheeks blush "" ("crooked_smile", "squint", "base", "stare")
    cho @ cheeks heavy_blush "" ("soft", "narrow", "angry", "R")

    pause .8
    play sound "sounds/crowd_cheer.ogg"

    qcr "Hermione!{w=0.4} Hermione!{w=0.4} Hermione!"
    her @ cheeks blush "That's right! She doesn't have anything that I don't!" ("grin", "closed", "angry", "mid")
    #whistle (catcalling)
    play sound "sounds/wolf_whistle2.ogg"
    femv "Show us your panties!"
    cho @ cheeks heavy_blush "" ("horny", "narrow", "angry", "R")
    qcr "Panties!{w=0.4} Panties!{w=0.4} Panties!"
    cho @ cheeks heavy_blush "" ("annoyed", "base", "angry", "L")
    nar "The focus on the game, now completely lost, has everyone's eyes moving back and forth between Hermione and Cho, waiting with bated breath to see who will push things further."
    cho @ cheeks heavy_blush "" ("smile", "base", "base", "L")

    if states.her.public_level < 3:
        her @ cheeks blush "P--{w=0.2} Panties?" ("angry", "squint", "worried", "stare") #happycl
        qcr "Panties!{w=0.4} Panties!{w=0.4} Panties!"

        hide cho_main
        with d3
        call cho_walk(1100, 140, speed=2)

        her @ cheeks blush "I--{w=0.2} I..." ("disgust", "happyCl", "base", "mid", trans=d3) #happycl
        qcr "Take it off!{w=0.4} Take it off!"
        her @ cheeks blush "I can't!" ("disgust", "squint", "base", "stare") #Open eyes #stare
        qcr "Boo!"
        her @ cheeks blush "That's right, Gryffindors will never go as low as--" ("angry", "narrow", "angry", "L")
    else:
        her @ cheeks blush "Can't get enough of me can you?" ("grin", "closed", "base", "mid")

        hide cho_main
        with d3
        call cho_walk(1100, 140, speed=2)

        her @ cheeks blush "Of course, now when you've seen the real deal, why would you ever look at someone like--" ("crooked_smile", "narrow", "base", "L", trans=d3)

    stop background fadeout 3.0

    her @ cheeks blush "--Cho?!" ("clench", "wide", "base", "L")
    her "Harry, she's going for the snitch!" ("scream", "base", "base", "L")
    "Harry" "*keeps drooling*"
    her @ cheeks blush "Heaven's sake!" ("disgust", "happy", "annoyed", "L")

    #Hermione puts clothes back on
    $ hermione.wear("all")
    with d3

    her "Go after her!" ("scream", "base", "angry", "L")
    nar "Snapping out of it, Harry speeds off after Cho who is now darting between the towers chasing the snitch."

    show CG quidditch cho_sitting entry as cg zorder 16
    hide snape_main
    hide hermione_main
    hide tonks_main
    $ cho.strip("panties", "bottom")
    with fade

    nar "All of a sudden she shoots up after it into the sky, with Harry's head at her heels."
    her "Faster, Harry!"

    call ctc

    show cho_quidditch2 slide cho_siting entry zorder 17 as cg2
    with dissolve

    nar "Cho speeds up even more, her skirt clinging on for dear life."
    nar "Harry still on her tail, is struggling, hard and is barely keeping up with her.{#LINT_IGNORE}"

    call ctc

    hide image cg2
    with dissolve

    her "What are you doing?! Don't you have a firebolt?"
    sna "Yes, how is she--"
    gen "The broom, she's become one with the broom!"
    sna "She's what?"

    show cho_quidditch2 slide cho_siting zorder 17 as cg2
    with dissolve

    pause 0.5

    # Wet sound?

    show CG quidditch cho_standing as cg zorder 16
    show cho_quidditch2 slide cho_standing zorder 17 as cg2 with dissolve

    call ctc

    her "Is that a dildo?!!"
    ton "Oh my!"
    sna "..."

    nar "Cho's secret now revealed--"
    sna "*Cough*... {i}Deletrius{/i}... *Cough*..."
    play sound "sounds/magic4.ogg"

    show cho_quidditch2 slide cho_standing_panties zorder 17 as cg2 with flashbulb

    call ctc

    show CG quidditch cho_standing_panties as cg zorder 16 with d3

    ton "Severus!"
    sna "What? I just coughed!"

    hide cg2
    with dissolve

    nar "Cho, whose panties are now revealed to the crowd, speeds up even further, edging ever so closer towards the snitch."
    qcr "Panties! Panties! Panties!"
    ton "*Cough*... {i}Ventus{/i}... *Cough*..."
    play sound "sounds/magic4.ogg"
    show CG quidditch cho_standing_panties_down as cg zorder 16 with flashbulb
    nar "Suddenly, a strong gust of wind grabs hold of her panties, and they slide down to her knees."

    call ctc

    show cho_quidditch2 slide cho_standing_panties_down zorder 17 as cg2
    with dissolve

    call ctc

    sna "Tonks!"
    ton "Won't you look at that? I think I got your same cough!"

    call ctc

    show CG quidditch cho_standing_smile as cg zorder 16
    hide cg2
    with dissolve

    nar "The focus now shifted from the snitch to Cho's wet snatch leaves no doubts just how much she's enjoying this."
    her "She's getting off doing this!?"
    qcr "Slut! Slut! Slut!"
    gen "Go on, girl... Don't lose focus now..."
    nar "Cho, basking in the attention, loses a bit of speed and Harry begins catching up to her."
    her "You silly slut, you're nothing compared to a real seeker like Harry!"
    her "The only thing you're good for is showing off your body!"

    nar "All of a sudden, Cho convulses and some translucent fluid escapes her nether."

    #Cho cums from Hermione insulting her and it flies off the screen into Harry's face

    play sound "sounds/slick_01.ogg"

    show CG quidditch cho_standing_ahegao as cg zorder 16 with kissiris

    pause .6

    show CG quidditch cho_standing_smile as cg zorder 16 with kissiris

    her "Harry!"

    play sound "sounds/crash.ogg"
    nar "As if hit by some unknown force,{w=1.0} Harry suddenly spins off,{nw}{w=0.5}"
    nar "As if hit by some unknown force, Harry suddenly spins off,{fast} and crashes into one of the confectionery carts." with vpunch

    play sound "sounds/crowd_ouch.ogg"
    qcr "Ouch!"
    nar "Cho's mind, now clearer than ever, gets a sudden burst of speed and stretches out her fingers towards the snitch."
    gen "That's right, fuck you Snape!!"
    #Cho catches the snitch

    show CG quidditch cho_standing_snitch as cg zorder 16 with d3

    #Crowd cheers
    play sound "sounds/crowd_cheer.ogg"

    pause 5.0

    # She mad bro
    play sound "sounds/microphone_feedback.ogg"
    her "{size=+15}No!!!{/size}"
    gen "Hell yes!"

    #Cho sits back down on the dildo, snitch in hand
    show CG quidditch cho_sitting_snitch as cg zorder 16 with d3

    pause 1.0

    show cho_quidditch2 slide cho_sitting_snitch zorder 17 as cg2
    with dissolve

    call ctc

    her "How?!?"
    #CG end here

    hide cg
    hide cg2
    with fade

    $ cho.equip(choq_panties_in_hand)

    stop music fadeout 1
    play background "sounds/crowd_low.ogg" fadein 5

    sna "Well, I'll be damned..." ("snape_01", trans=d3) #doesn't look too bothered
    her @ cheeks blush "She...{w=0.4} She cheated!" ("clench", "wide", "base", "stare", trans=d3)
    #TODO Cho flies up, panties in her hand

    call cho_chibi("fly", 1100, 140)
    call cho_walk(530, 360, speed=2)
    pause 1.5

    cho @ cheeks blush "You mad, Granger?" ("grin", "narrow", "base", "L", flip=False, trans=d3)
    her @ cheeks blush "You did something to Harry!" ("mad", "squint", "angry", "L", trans=d3)
    cho @ cheeks blush "I did? You sure he wasn't just blinded by my charm?" ("soft", "narrow", "raised", "L")
    her "A charm! You must've cast some spell on him!" ("angry", "wide", "base", "stare")
    cho @ cheeks blush "With what wand exactly?" ("smile", "narrow", "base", "L")
    cho @ cheeks heavy_blush "The only stiff object here is placed between my legs, and that's not a {i}magic wand{/i}." ("grin", "narrow", "base", "L")
    cho @ cheeks heavy_blush "Although I don't expect you to know the difference between a dildo and--" ("crooked_smile", "narrow", "base", "R")
    her @ cheeks blush "You...{w=0.4} You..." ("mad", "wide", "angry", "L")
    gen "Now-now, don't be a sore loser, Miss Granger... There's no way she'd be able to keep a wand on her." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "She...{w=0.4} She..." ("angry", "wide", "angry", "stare")
    gen "So unless you want us to do a cavity search..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Sure, I don't mind." ("base", "narrow", "base", "mid")
    her @ cheeks blush "You... {w=0.4}You slut!" ("scream", "wide", "angry", "L") # angry tears
    cho @ cheeks heavy_blush "Sorry, what was that?" ("soft", "narrow", "base", "L")
    cho @ cheeks heavy_blush "I got a bit distracted seeing your friend get carried on a stretcher to the hospital wing..." ("smile", "narrow", "base", "L")
    her @ cheeks blush "*Grr*..." ("angry", "squint", "angry", "R")
    cho @ cheeks blush "Here you go Granger, something for you to remember your loss..." ("smile", "narrow", "base", "L")


    # Cho panties appear on Hermione's head as Cho throws them at her
    play sound "sounds/woosh.ogg"
    $ cho.unequip(choq_panties_in_hand) # Panties
    pause .8
    play sound "sounds/squelch.ogg"
    $ hermione.equip(herq_panties_on_head)
    with d3

    her @ cheeks blush "Cho!" ("angry", "wide", "annoyed", "up")
    cho @ cheeks blush "Later, Granger!" ("smile", "wink", "base", "mid")

    hide cho_main
    with d5

    play sound "sounds/crowd_cheer.ogg"
    call cho_walk(1100, 140, speed=2)

    ton "*Giggles*" ("crooked_smile", "narrow", "raised", "L", trans=d3)

    call her_chibi(flip=False)
    with d3

    her @ cheeks blush "Professor!" ("clench", "base", "angry", "L", flip=False, trans=d3)
    ton "Sorry..." ("soft", "base", "base", "down")
    qcr "Cho! Cho! Cho!"
    her @ cheeks blush "*Grr*!" ("angry", "base", "angry", "R")

    call her_walk(213, 414)

    sna "I must say that I am truly sorry Gryffindor has lost." ("snape_04", trans=d3)
    sna "Truly..." ("snape_06", trans=d3)
    her @ cheeks blush "*Hmph*!" ("upset", "closed", "angry", "mid", trans=d3)

    # Hermione chibi walks up stairs next to Tonks
    # Hermione removes panties off head.
    $ hermione.unequip("headgear")

    show image "panties_on_the_ground" as panties zorder 2:
        pos (268, 380)

    with d3

    hide hermione_main
    call her_chibi("hide")
    with d3

    pause 1.0

    sna "What's her problem?" ("snape_05", trans=d3)
    gen "I think your sincerity got lost somewhere in translation." ("base", xpos="far_left", ypos="head")
    gen "Speaking of losses..." ("base", xpos="far_left", ypos="head")
    gen "Ravenclaw won the game, where's my money?" ("base", xpos="far_left", ypos="head")
    sna "Can't even wait one minute before gloating I see..." ("snape_03")
    gen "Show me the money!" ("grin", xpos="far_left", ypos="head")
    sna "Very well...{w=1.0} I shall fetch your winnings and deliver it to your office shortly." ("snape_01")
    gen "Hell yes!" ("grin", xpos="far_left", ypos="head")
    sna "..." ("snape_37") # Smug

    hide snape_main
    call sna_chibi("hide")
    with d3

    gen "I better head back as well then." ("base", xpos="far_left", ypos="head")

    call gen_walk(path=[(135, 360), (213, 414)])
    call gen_chibi(flip=False)
    with d3
    call gen_chibi("stand_alt", flip=False)
    with d3


    gen "Drinks on me?" ("base", xpos="far_left", ypos="head")
    ton "*Hmm*... Why not... I could do with something to take the edge off things." ("base", "narrow", "raised", "R")

    call gen_chibi("hide")
    hide screen bld1
    with d3

    pause 0.5

    call ton_walk(path=[(100, 334), (194, 400)])

    ton @ hair horny "Nice, free panties." ("horny", "base", "base", "down", trans=d3)

    play sound "sounds/cloth_sound2.ogg"
    hide image panties
    with d3

    pause 0.8

    ton @ hair horny "*Hmm*...{w=0.1} Someone should probably pick up the rest of her clothes..." ("soft", "base", "base", "R", trans=d3)
    ton @ hair horny "{w=0.8}{nw}" ("annoyed", "base", "base", "L")
    ton @ hair horny "{w=0.8}{nw}" ("annoyed", "base", "base", "R")
    ton @ hair horny "Nobody?{w=0.8}{nw}" ("annoyed", "base", "base", "R")
    ton @ hair horny "Nobody?{fast} Oh fine, I suppose I'll do it then..." ("base", "base", "base", "R")
    ton @ hair horny "(Before Madam Hooch gets there first.)" ("soft", "base", "base", "R")

    hide tonks_main
    call ton_chibi("hide")
    with d3

    pause 1.0

    call cho_chibi("fly", 1100, 140)
    call cho_walk(530, 360, speed=2)
    pause 1.5

    cho @ cheeks blush "Hey Professor--" ("grin", "closed", "base", "mid", flip=False, trans=d3)
    cho @ cheeks blush ".......?" ("soft", "base", "base", "L")
    cho @ cheeks blush "(*Hmm*... Did he already go back to his office?)" ("soft", "narrow", "base", "L")
    cho "(I better catch up with him...)" ("soft", "base", "base", "L")
    cho @ cheeks blush "(Although...)" ("base", "narrow", "base", "R")
    cho @ cheeks blush "(A few victory laps around the pitch wouldn't hurt.)" ("smile", "narrow", "base", "R") # horny

    play sound "sounds/crowd_cheer.ogg"
    stop background fadeout 2.0
    call cho_walk(1100, 140, speed=2)

    #Reset z.order
    $ snape_chibi.zorder = 3
    $ tonks_chibi.zorder = 3
    $ hermione_chibi.zorder = 3
    $ genie_chibi.zorder = 3



    jump gryffindor_match_return

#Event after game where Cho, Tonks, Snape and Hooch arrive and Cho is accused of cheating. Cho is hidden under the desk as she had arrived first and Tonks tells her to hide. During the event once the cheating is brought up, Cho starts sucking genie off, genie assuming she's doing it so that he'd save her. Genie saves her ass which leads to a sex event after where genie is confused as she doesn't have a reason to do it. The potion is meant to give her the best day ever after all, and that's what she truly wants.

label gryffindor_match_return:

    #Setup
    $ tonks.zorder = 18
    $ hooch.zorder = 17
    $ states.sna.image.zorder = 16
    $ cho.zorder = 16 #Shows/Hides Cho doll on CG

    $ snape_chibi.zorder = 4

    show screen blkfade
    with d5

    pause 1

    $ cho.set_pose(None)
    $ cho.animation = None
    $ cho.strip("clothes")

    stop music fadeout 1

    call room("main_room")
    call gen_chibi("hide")

    hide screen blkfade
    with d5

    play sound "sounds/door.ogg"
    call gen_chibi("stand", "door", "base", flip=False)
    with d3
    pause 0.8

    #Genie walks into the office
    gen "*Hmm*... Sure feels weird now that it's over..." ("base", xpos="far_left", ypos="head")
    gen "I suppose that's the life of a coach once they're done coaching..." ("base", xpos="far_left", ypos="head")
    gen "Back in the chair we go." ("base", xpos="far_left", ypos="head")

    #Walks and sits down at his desk.
    call gen_walk("desk")
    call gen_chibi("sit_behind_desk")
    with d3

    pause 0.5

    gen "I wonder what chairs think about all day...{w=0.8}\n\"Oh, here comes another asshole\"." ("base", xpos="far_left", ypos="head")

    pause 0.3

    #Cho chibi appears naked next to the window turned to right

    "Voice outside the window" "Stay... [states.cho.ev.quidditch.broom_name]."
    #Cho walks to the front of the desk

    gen "[states.cho.ev.quidditch.broom_name]? Isn't that--" ("base", xpos="far_left", ypos="head")

    call cho_chibi("stand", xpos=441, ypos=400, flip=False)
    call cho_walk("desk", "base")

    with d3

    pause 0.5
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho "Sorry for the wait, I just had to take a few victory laps." ("smile", "narrow", "base", "mid", xpos="mid", ypos="base", trans=d3)

    gen "!!!" ("angry", xpos="far_left", ypos="head")

    cho @ cheeks blush "Who would've thought flying would{nw}" ("smile", "wink", "base", "mid")
    cho @ cheeks blush "Who would've thought flying would{fast} be so freeing without the restrictions of clothes." ("base", "base", "base", "mid")

    gen "(Damn! What a view!)" ("grin", xpos="far_left", ypos="head")
    gen "I'm glad everything turned out the way you imagined it." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "" ("base", "narrow", "base", "downR")
    call ctc
    cho @ cheeks heavy_blush "" ("soft", "narrow", "base", "R") #blush
    call ctc

    # Cho Chibi rushes up to genie's side
    call cho_walk(path=[(390, 470), (240, 460)], speed=1.5)
    call cho_chibi(flip=True)
    with d3

    #Kisses sound, pink visual effect
    play sound "sounds/kiss.ogg"
    with kissiris

    gen "What was that for?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "For all the--" ("smile", "narrow", "base", "L", xpos="left", ypos="base", flip=True, trans=d3)

    #Tonks enters
    stop music fadeout 1
    play sound "sounds/door_down.ogg"
    call ton_chibi("stand","door","base")
    with hpunch

    cho @ cheeks heavy_blush "" ("clench", "wide", "base", "mid") #wide eyed

    play music "music/Under-the-Radar by PhobyAk.ogg" if_changed


    ton @ hair upset "We've got a situation--{w=0.2}" ("mad", "base", "base", "R", xpos="base", ypos="base")
    ton @ cheeks blush hair horny "Cho?!" ("clench", "wide", "shocked", "L")
    cho @ cheeks heavy_blush "Professor?!" ("angry", "wide", "base", "L")
    gen "(For fuck's sake... {i}Always something{/i}...)" ("angry", xpos="far_left", ypos="head")
    ton "Shit... You have to hide, now!" ("mad", "base", "base", "R")
    cho @ cheeks heavy_blush "But why--" ("angry", "narrow", "base", "L")
    ton "Just do it, quick!" ("scream", "base", "shocked", "L")

    show screen blkfade
    with d5

    call cho_chibi("hide")
    call ton_chibi(xpos="mid", ypos="420")
    #Tonks walks to desk (closest to window)

    nar "In an act of desperation, Cho decides to hide under your desk."

    hide cho_main
    hide tonks_main
    hide screen blkfade
    with d5

    gen "Tonks, explain yourself!" ("angry", xpos="far_left", ypos="head")

    call sna_walk(action="enter", xpos="400", ypos="460")

    #Snape enters office and walks to desk (left)
    sna "Headmaster..." ("snape_01", trans=d3, xpos=200, ypos="base")
    gen "Severus! I should've known!" ("grin", xpos="far_left", ypos="head")
    gen "Come to deliver my winnings, I presume?" ("grin", xpos="far_left", ypos="head")
    sna "Not exactly..." ("snape_37") #Smugface

    hide snape_main
    hide screen bld1
    with d3

    play sound "sounds/door.ogg"
    chibi hooch move (path=[(790, 450), (610, 445)])
    pause 1.0

    #Hooch enters and walks up behind Snape and Tonks
    hoo "You can't just walk in like that without knocking Severus, show the headmaster some respect." ("angry", "shocked", "base", "mid", xpos=700, ypos="base", flip=False, trans=d3)
    sna "..." ("snape_35", trans=d3)
    hoo "Sorry for arriving unannounced like this, Headmaster." ("normal", "base", "base", "mid")
    gen "No worries at all, Miss Hooch... Seeing your face always puts a smile on my face." ("base", xpos="far_left", ypos="head")
    hoo "Why thank you Professor, how nice." ("base", "shocked", "shocked", "mid")
    sna "Yes, always such a {i}nice guy{/i}..." ("snape_31")
    ton "*Ahem*...{w=0.4}{nw}" ("soft", "base", "base", "R", xpos=460, ypos="base", trans=d3)
    ton "*Ahem*...{fast}{w=0.4}{nw}" ("soft", "base", "base", "L")
    ton "*Ahem*...{fast}" ("soft", "base", "base", "R")
    sna "" ("snape_39")
    gen "So, what can I do you for? It's not often that three teachers enter my office at the same time." ("base", xpos="far_left", ypos="head")
    hoo "Yes, unfortunately it can't be helped, a very serious matter regarding the finals has come up." ("normal", "base", "shocked", "mid")
    gen "Oh?" ("base", xpos="far_left", ypos="head")
    ton "" ("normal", "base", "base", "mid", xpos=460, ypos="base")
    gen "That Potter boy didn't die, did he?" ("base", xpos="far_left", ypos="head")
    hoo "Who?" ("open", "base", "raised", "mid")
    ton "The Gryffindor seeker who crashed into one of the confectionery carts." ("open", "base", "base", "R")
    hoo @ cheeks blush "He did? I must have missed that." ("open", "shocked", "worried", "R")
    ton "" ("base", "base", "base", "R")
    gen "Figures..." ("base", xpos="far_left", ypos="head")
    sna "The boy will live...{nw}" ("snape_01")
    ton "" ("normal", "base", "base", "L")
    hoo "" ("normal", "shocked", "base", "L")
    sna "The boy will live...{fast} Albeit some permanent scarring across his forehead." ("snape_37")
    gen "The boy who lived..." ("base", xpos="far_left", ypos="head")
    gen "So what's this all about then?" ("base", xpos="far_left", ypos="head")
    hoo "It's--" ("open", "shocked", "shocked", "mid")
    sna "The matter at hand{nw}" ("snape_01")
    hoo "" ("normal", "base", "angry", "L")
    ton "" ("normal", "narrow", "base", "mid")
    sna "The matter at hand{fast} is in regard to the Ravenclaw girl...{w=0.4} Miss Chang." ("snape_01")
    gen "Oh? There's not a rule against cumming--" ("base", xpos="far_left", ypos="head")

    #Thud sound
    play sound "sounds/kick.ogg"
    gen "*Hngh*!" ("angry", xpos="far_left", ypos="head")
    gen "I mean...{w=0.4} Coming first?" ("base", xpos="far_left", ypos="head")

    sna "" ("snape_39")
    hoo "Sorry?" ("open", "shocked", "raised", "mid")
    gen "Nevermind...{w=0.4} So what about Miss Chang?" ("base", xpos="far_left", ypos="head")
    hoo "Well... Some evidence has come forward, which suggests that Miss Chang was under the influence of a luck potion." ("open", "shocked", "base", "mid")
    gen "Under the--" ("base", xpos="far_left", ypos="head")

    #Thud sound (Cho hits her head on the desk)
    play sound "sounds/kick.ogg"
    pause .6

    gen "Desk!" ("angry", xpos="far_left", ypos="head")
    gen "I mean... Ouch! I hit my knee on the desk!" ("angry", xpos="far_left", ypos="head")
    gen "Hold on, did you say luck potion?" ("base", xpos="far_left", ypos="head")
    sna "" ("snape_37")
    ton "" ("normal", "base", "base", "R")
    hoo "Yes, I came across an empty vial near some of the clothing she had discarded during the game." ("open", "shocked", "raised", "mid")
    hoo "Professor Snape here insists that it's \"felix felicis\"." ("normal", "shocked", "base", "L")
    ton "" ("normal", "base", "base", "L")
    gen "{size=-4}So this was your plan...{/size}" ("base", xpos="far_left", ypos="head") #small text
    sna "" ("snape_13")
    gen "Performance enhancing drugs... Now that is some serious business." ("base", xpos="far_left", ypos="head")
    sna "" ("snape_40")
    ton "" ("normal", "narrow", "base", "mid")
    hoo "Yes indeed..." ("base", "base", "base", "mid")
    hoo "I'm sure you've heard the rumours about the Slytherin players using it during their match against Ravenclaw." ("open", "base", "base", "mid")
    sna "Lies and slander is what it was." ("snape_09")
    hoo "*Hmph*...{w=0.4} In any case--" ("normal", "shocked", "base", "R")
    hoo "The usage of such things is considered cheating and is prohibited during organized sports and academic examinations." ("open", "narrow", "angry", "mid")
    ton "" ("annoyed", "base", "base", "mid")
    gen "So if this bottle is a luck potion, she'd get disqualified?" ("base", xpos="far_left", ypos="head")
    sna "*Snort*" ("snape_22") #smirk
    hoo "Yes, although disqualification would be the least of her worries." ("open", "shocked", "angry", "mid")
    gen "You're not saying..." ("base", xpos="far_left", ypos="head")
    sna "" ("snape_37") #smirk
    hoo "Indeed..." ("normal", "shocked", "worried", "down")
    gen "Prison?" ("base", xpos="far_left", ypos="head")

    #Zipper sound/cloth sound
    play sound "sounds/zipper.ogg"
    gen "...{w=0.8}{nw}" ("base", xpos="far_left", ypos="head")
    gen "...{w=0.8}{nw}" ("angry", xpos="far_left", ypos="head")

    hoo "Prison? No, not that, thank heavens." ("open", "shocked", "shocked", "mid")
    hoo "But she could kiss getting into any sort of professional league goodbye." ("open", "shocked", "base", "down")
    gen "Kiss--" ("base", xpos="far_left", ypos="head")

    #kiss sound, pink visual effect as Cho kisses genie's dick
    play sound "sounds/kiss.ogg"
    hide snape_main
    hide tonks_main
    hide hooch_main
    with kissiris


    gen "*Hngh*--" ("angry", xpos="far_left", ypos="head")

    #Cut to CG
    show image "cho_under_desk_idle_snape_no_spit" as cg_doll zorder 16
    with fade
    call ctc

    ton "Professor?" ("soft", "narrow", "raised", "mid", xpos="far_right", ypos="head")

    play sound "sounds/spit.ogg"
    show image "cho_under_desk_idle_snape" as cg_doll

    gen "..." ("angry", xpos="far_left", ypos="head")
    ton "Are you alright?" ("soft", "base", "raised", "mid")

    #Cho's head starts moving
    play background "sounds/slickloop.ogg" fadein 2
    show image "cho_under_desk_blowjob" as cg_doll
    with d3

    cho @ cheeks heavy_blush "*Slurp*...{w=0.4} *Gobble*...{w=0.4} *Slurp*" ("open_wide_tongue", "narrow", "base", "up", xpos="far_right", ypos="head", flip=False, trans=d3)
    gen "Oh, yes!{w=0.4} *Ahem*--{w=0.4} Sorry, I was just thinking how terrible that would be." ("grin", xpos="far_left", ypos="head")
    gen "(What the hell does she think she's doing!?)" ("angry", xpos="far_left", ypos="head")
    gen "Don't--{w=0.2} *Hngh*...{w=0.4} Don't worry about me, I'll be fine. Just taken by surprise by this whole ordeal, that's...{w=0.4} That's it." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "*Gobble*...{w=0.4} *Gobble*...{w=0.4} *Slurp*" ("open_wide_tongue", "closed", "base", "up")
    hoo "Are you sure? Your face does look a bit white, sir." ("open", "shocked", "worried", "L", ypos="head")
    gen "(With all my blood flow being redirected, that's not surprising.)" ("base", xpos="far_left", ypos="head")
    gen "I'll...{w=0.4} *Ah*...{w=0.4} I'll be fine." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "*Slurp*... {w=0.4}*Slurp*...{w=0.4} *Slurp*" ("open_wide_tongue", "closed", "base", "up")
    gen "So... Regarding this--{w=0.2} *Ah*...{w=0.4}{nw}" ("base", xpos="far_left", ypos="head")
    gen "So... Regarding this-- *Ah*...{fast} Fuck..." ("grin", xpos="far_left", ypos="head")
    gen "Luck!{w} Regarding this Luck potion!" ("angry", xpos="far_left", ypos="head")
    gen "I find it seriously hard...{w=0.4} *Ngh*...{w=0.4} To believe she'd ever gobble, *Err*...{w=0.4} Drink something like that with such a high risk of...{w=0.4} *Hngh*...{w=0.4} Getting caught." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "*Gobble*...{w=0.4} *Slurp*...{w=0.4} *Slurp*" ("open_wide_tongue", "closed", "base", "up")
    gen "You're certain it's a luck potion and not...{w=0.4} *Ah*...{w=0.4} {i}Gatorade{/i}, or something?" ("base", xpos="far_left", ypos="head")
    hoo "Gator aid?" ("open", "base", "raised", "mid")
    hoo "That's not some performance enhancing drug is it?" ("open", "narrow", "worried", "mid")
    gen "Nah, it's just a sports--" ("base", xpos="far_left", ypos="head")

    play background "sounds/slickloopfast.ogg"
    show image "cho_under_desk_blowjob_fast" as cg_doll

    cho @ cheeks heavy_blush "*Gobble*...{w=0.2} *Slurp*...{w=0.2} *Gobble*" ("open_wide_tongue", "happyCl", "base", "mid")
    gen "*Ngh*...{w=0.4} sports drink." ("angry", xpos="far_left", ypos="head")
    hoo "I see." ("open", "base", "base", "mid")
    gen "Electrobytes or whatchamacallit." ("base", xpos="far_left", ypos="head")
    hoo "Well I suppose it could be, I can't say I've seen what a Gator Aid container looks like." ("normal", "narrow", "base", "downL")
    sna "Now hold on just one second!" ("snape_10", xpos="far_right", ypos="head")
    sna "Did you not see how fast she was going on that broom?" ("snape_32")
    sna "It has to have been a luck potion!" ("snape_32")
    sna "Such precise movements should be impossible on anything but a firebolt!" ("snape_17")
    hoo "I thought you tested the remaining drops in the vial, Severus." ("open", "shocked", "shocked", "mid")
    sna "*Err*... Not yet, but--" ("snape_14")
    hoo "Are these accusations all just assumptions based on her athletic abilities?" ("angry", "narrow", "angry", "mid")
    sna "No, of course not!" ("snape_18")
    sna "Hand me the vial, and I'll inspect it right now!" ("snape_17")
    gen "..." ("angry", xpos="far_left", ypos="head")
    ton "*Ahem*!" ("open", "narrow", "annoyed", "mid") #Tonks to the rescue
    ton "I may be wrong here, but don't you happen to have a stake in this game, Severus?" ("open", "closed", "annoyed", "mid")
    sna "W--{w=0.2} What?" ("snape_36")
    gen "Oh yes, the bet!" ("grin", xpos="far_left", ypos="head")
    hoo "Bet?" ("open", "narrow", "base", "mid")

    #Cho stops moving
    stop background fadeout 2
    play sound "sounds/slick_pop.ogg"
    show image "cho_under_desk_idle_snape" as cg_doll

    cho @ cheeks heavy_blush "*Pwah*." ("open_tongue", "narrow", "base", "up")

    show image "cho_under_desk_handjob" as cg_doll
    with d3

    ton "The boys have a bet on which team would end up winning the Quidditch cup." ("open", "base", "base", "R")
    hoo "I see... Well, that changes things..." ("normal", "base", "base", "L")
    sna "You think I'd put some bet above my reputation as a potions master!?" ("snape_18") #Fake offended
    gen "...{w} Probably." ("base", xpos="far_left", ypos="head")
    hoo "Highly likely." ("open", "narrow", "base", "mid")
    ton "Most definitely." ("soft", "narrow", "shocked", "mid")
    sna "*Hmph*... In that case, I'll just bring the vial to professor Slughorn and have him test it!" ("snape_16")

    #Snape's legs vanish from CG as he goes to grab the bottle.
    show image "cho_under_desk_idle" as cg_doll
    with d3

    play sound "sounds/cloth_sound3.ogg"
    ton "Get off me, I'll bring it to him myself! We just said we can't trust--" ("disgust", "base", "annoyed", "mid")
    sna "Give it here! I'm not going to--" ("snape_32")

    #Smashing bottle sound.
    play sound "sounds/glass_break.ogg"
    pause 0.75

    ton "Whoopsie." ("soft", "wide", "base", "up")
    hoo "Oh dear..." ("open", "shocked", "shocked", "down")
    sna "..." ("snape_11") #wide eyed
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Show me the money!" ("grin", xpos="far_left", ypos="head")
    play sound "sounds/kettle.ogg"
    sna "..." ("snape_08") #Raging
    hoo "Oh, look at the time. I think I better get going--" ("open", "shocked", "shocked", "R")

    #hooch sprints out the office sound
    $ hooch_chibi.hide()
    play sound "sounds/run_03.ogg"
    pause 1.0
    play sound "sounds/door.ogg"

    sna "{size=+10}{cps=10}Fuuuuuuuuuck{/cps}!!!!{/size}"
    cho "*Giggles*"

    #fade to black
    #fade back to office
    hide cg_doll
    hoo "" (xpos="base", ypos="base") # This will ensure her character has correct positioning in the future events.
    hide hooch
    hide hooch_main
    hide tonks_main
    hide snape_main
    with fade

    ton "Calm down Severus... Accidents happen." ("soft", "narrow", "shocked", "mid", xpos=460, ypos="base", trans=d3)
    sna "No, you did that on purpose!" ("snape_17", xpos=200, ypos="base", trans=d3)
    ton "Don't be silly, I have no reason to get involved with your silly little bets." ("base", "narrow", "base", "R")
    sna "*Grr*... I'll be in my office." ("snape_16")

    #Snape turns right
    call sna_walk(xpos="mid", speed=0.6)

    play sound "sounds/MaleClearThroat.ogg"
    gen "Forgetting something?" ("base", xpos="far_left", ypos="head")
    sna "*Breathing heavily*" ("snape_43", xpos=460, ypos="base", trans=d3, flip=True)
    gen "Show me the--" ("grin", xpos="far_left", ypos="head")

    #Snape walks to desk
    call sna_walk(xpos="desk", speed=1.5)

    play sound "sounds/money_thud.ogg"
    $ game.gold += 2000

    sna "Here, now shut...{w=0.2} Up!" ("snape_17", xpos=200, ypos="base", trans=d3, flip=False)
    call sna_walk(action="leave", speed=1.5)
    play sound "sounds/kick.ogg"
    with hpunch
    #Snape leaves
    #Slams door

    gen "Pleasure doing business with you!" ("grin", xpos="far_left", ypos="head")

    stop music fadeout 1

    play sound "sounds/giggle2.ogg"
    ton "*Giggles*..." ("grin", "narrow", "base", "R", trans=d3) #smirks

    label .introspection:

    if _in_replay:
        show screen blkfade
        with d5

        pause 1

        $ cho.set_pose(None)
        $ cho.animation = None
        $ cho.strip("clothes")

        call room("main_room")
        call gen_chibi("sit_behind_desk")
        call ton_chibi(xpos="mid", ypos="420")

        ton "" ("base", "narrow", "base", "L", xpos="base", ypos="base")

        hide screen blkfade
        with d5

    ton "You can come out now, Miss Chang... The scary pale man is gone." ("base", "narrow", "base", "L")
    gen "Just give her one more minute--" ("base", xpos="far_left", ypos="head")
    ton "Go on Miss Chang, no need to worry." ("soft", "base", "base", "L")

    call cho_chibi(xpos=240, ypos=460, flip=True)
    with d3

    #Cho chibi appears next to the desk.

    gen "(Damn...)" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "There you are..." ("horny", "base", "base", "L")
    ton @ hair horny "I apologise for making you hide under the headmaster's desk like that, Miss Chang." ("soft", "narrow", "base", "L")
    cho @ cheeks heavy_blush "Thank you professor." ("open", "narrow", "base", "down", xpos="left", ypos="base", flip=True, trans=d3)
    cho @ cheeks heavy_blush "" ("soft", "narrow", "base", "R", xpos="left", ypos="base")
    ton @ hair horny "*Hmm*?" ("soft", "narrow", "raised", "L")
    ton @ hair horny "Oh yes, the potion thing... I'm sorry Miss Chang, but you're quite distracting." ("base", "base", "base", "L")
    ton @ hair horny "*Mmm*...{w=0.4} Although I'm not complaining." ("horny", "narrow", "base", "L")
    ton "You should probably put something on before entering the hallways though." ("base", "narrow", "base", "R")
    ton "I took the liberty of fetching your clothes for you, put them on once you two are finished in here, will you?" ("grin", "wink", "base", "mid")
    cho @ cheeks heavy_blush "Yes, professor." ("soft", "narrow", "base", "L")

    #Ravenclaw clothpile
    play sound "sounds/cloth_sound4.ogg"
    show screen cho_cloth_pile
    with d3

    ton "Good girl." ("grin", "base", "base", "L")
    ton @ hair horny "Make sure you use that potion to its full extent now, Miss Chang." ("horny", "base", "shocked", "L")
    ton @ hair horny "Have fun!" ("grin", "wink", "base", "mid")

    #Tonks leaves
    call ton_walk(action="leave")

    cho @ cheeks blush "*Hmm*..." ("soft", "narrow", "base", "down", trans=d3)

    cho @ cheeks heavy_blush "Have f--{w=0.2} Oh, I see..." ("soft", "narrow", "base", "down")

    if _in_replay:
        cho "(She thinks I drank the potion... But how does she know I want to--)"
        cho "(Is it that obvious...)"
        cho "(But how could I ask him... I didn't drink it...)"
        cho "(Unless I told him--)"

    cho @ cheeks heavy_blush "{size=-4}The potion would let me know if this wasn't what he wanted...{/size}" ("soft", "narrow", "base", "downR")
    gen "*Huh*?" ("base", xpos="far_left", ypos="head")
    gen "What are you mumbling--" ("base", xpos="far_left", ypos="head")
    play music "music/marty-gots-a-plan-by-kevin-macleod.ogg" fadeout 3 fadein 1.0 if_changed
    cho @ cheeks blush "[name_genie_cho], Why don't you take your clothes off and get on that desk for me?" ("soft", "narrow", "base", "mid") #smirk

    if _in_replay:
        return

    gen "W--{w=0.2} What?!" ("base", xpos="far_left", ypos="head")
    play sound "sounds/giggle.ogg"
    cho @ cheeks heavy_blush "*Giggles*" ("smile", "narrow", "base", "R")
    cho @ cheeks heavy_blush "You've heard me..." ("base", "narrow", "base", "mid")
    gen "But I thought..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Isn't this what you wanted?" ("soft", "narrow", "raised", "mid")
    gen "Well, yes but--" ("base", xpos="far_left", ypos="head")
    # reference from police academy
    cho @ cheeks heavy_blush "On your feet, soldier!" ("scream", "closed", "angry", "mid")
    gen "Yes ma'am!" ("grin", xpos="far_left", ypos="head")
    #

    #Cho and Genie has sex
    #Black fade
    #Chair sound or similar
    stop music fadeout 1.0
    show screen blkfade
    with d5

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    play sound "sounds/giggle.ogg"
    cho "*Giggles*" ("base", "base", "base", "mid")
    cho "So, all it took was a bit of coaching?" ("base", "base", "base", "mid")
    gen "*Err*..."

    cho "Alright...{w=0.4} I suppose I could coach you a bit this time..." ("base", "base", "base", "mid")
    gen "..."
    cho "Go on then...{w=0.4} Take those clothes off already." ("base", "base", "base", "mid")
    cho "No, hold on... Let me do it!" ("base", "base", "base", "mid")

    play sound "sounds/cloth_sound3.ogg"
    pause .8

    cho "What the--{w=0.2} Your figure feels a lot more muscular than I imagined." ("base", "base", "base", "mid")
    gen "[name_cho_genie]?"
    cho "No matter..." ("base", "base", "base", "mid")
    cho "Now, lay down on the desk for me." ("base", "base", "base", "mid")

    #desk creak sound
    play sound "sounds/08_hop_on_desk.ogg"
    pause 3

    show image "cho_sex idle" as cg_doll zorder 16
    show image "dustfloating" as cg_doll_effects zorder 17
    hide screen blkfade
    hide cho_main
    with d9


    cho @ cheeks heavy_blush "*Mmm*...{w=0.4} You're lucky I've been training for this, [name_genie_cho]..." ("smile", "narrow", "base", "down", xpos="base", ypos="head", flip=False, trans=d3)
    cho @ cheeks heavy_blush "Of course... I figured it'd come to this eventually..." ("open", "closed", "base", "mid")
    cho @ cheeks heavy_blush "Ever since I saw this thing for the first time..." ("base", "narrow", "base", "down")
    gen "(Why's she doing this? She already won the cup, didn't she?)"
    cho @ cheeks heavy_blush "*Sigh*..." ("base", "closed", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "To think that I would actually agree to all of this just so that I could win that cup..." ("base", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "I would've never imagined that I'd go so far as to take my clothes off in front of the entire school..." ("base", "closed", "worried", "mid")
    gen "Well, I don't think I asked you--"
    cho @ cheeks heavy_blush "Sure, I enjoyed showing off my athletic body before." ("soft", "closed", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "But even then..." ("base", "closed", "base", "stare")
    cho @ cheeks heavy_blush "If you had told me that the thrills leading up to every game would've gradually changed from winning the cup to looking forward to doing all those despicable things..." ("base", "closed", "base", "mid")
    cho @ cheeks heavy_blush "Well, I'm not sure I would've believed it..." ("base", "narrow", "base", "stare")
    gen "*Ahem*... I'm sure your fans would say the same!"
    cho @ cheeks heavy_blush "I'm not just talking about the things I did on the pitch..." ("base", "narrow", "base", "R", trans=d3)
    gen "..."
    cho @ cheeks heavy_blush "You know... I was getting increasingly worried once the finals loomed closer." ("open", "narrow", "base", "down", trans=d3)
    cho @ cheeks heavy_blush "After all... Once I had won the game, there wouldn't be any more need for our... extracurricular activities, would there?" ("soft", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "You'd have no more leverage over me...{w=0.4} Right?" ("smile", "narrow", "raised", "mid")
    gen "..."
    cho @ cheeks heavy_blush "No more reason for me to sell you any favours..." ("open", "closed", "base", "mid", trans=d3)
    gen "Miss--"
    cho @ cheeks heavy_blush "You thought you were the only one having those thoughts?" ("soft", "narrow", "base", "mid", trans=d3)
    gen "*Err*..."
    cho @ cheeks heavy_blush "After I sucked your dick I couldn't help but worry--" ("open", "narrow", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "That I'd end up winning the cup before ever knowing what my coach's thick beater's bat would feel like inside my tight little... Snitch." ("horny", "narrow", "base", "down")

    #Cho up position dick in front of body
    show image "cho_sex up" as cg_doll
    with d3

    gen "Miss Chang!"
    cho @ cheeks heavy_blush "I was hoping it wouldn't come to this..." ("open", "closed", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "That we could've reached this stage within our agreement..." ("soft", "narrow", "base", "down")
    cho @ cheeks heavy_blush "Although it's quite fitting to have this be part of my reward, don't you think?" ("smile", "narrow", "base", "down")

    #Cho positioning dick against pussy pose
    show image "cho_sex insert" as cg_doll
    with d3

    $ states.cho.status.sex = True

    cho @ cheeks heavy_blush "As much as it is a reward for you..." ("base", "narrow", "base", "down")
    gen "Are you... Are you sure about this?"
    cho @ cheeks heavy_blush "Sure? I've never been so sure about anything in my life!" ("smile", "base", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "This potion is incredible!" ("crooked_smile", "base", "base", "stare")
    gen "The...{w=0.4} So it's just the potion talking?"
    cho @ cheeks heavy_blush "*Tsk*... Of course not... Luck potion doesn't work that way, we both know that." ("smile", "narrow", "base", "R", trans=d3)
    cho @ cheeks heavy_blush "And let me tell you, what they say about it is true... This is the best day I've had in my life!" ("crooked_smile", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "And it's about to get even better..." ("crooked_smile", "narrow", "base", "down")

    #Cho sits down on genie's dick and gets fully penetrated
    show image "cho_sex up inside" as cg_doll
    with d3
    pause 0.25
    cho @ cheeks heavy_blush "*Nnngh--{w=0.40}{nw}" ("angry", "closed", "angry", "mid")
    show image "cho_sex middle" as cg_doll
    with d3
    pause 0.25
    play sound "sounds/slick_02.ogg"
    show image "cho_sex down" as cg_doll
    with d3
    pause 0.25

    with hpunch
    cho @ cheeks heavy_blush "*Ah*..." ("open_wide_tongue", "narrow", "base", "up")
    gen "*Ngh*!"
    gen "By the great--{w=0.2} You've already almost made me bust from that blowjob, girl!"
    cho @ cheeks heavy_blush "Then let's finish the job this time, shall we?" ("grin", "narrow", "base", "mid", trans=d3)

    #Cho starts moving
    play background "sounds/slickloop.ogg"
    show image "cho_sex loop slow" as cg_doll
    with d3

    gen "*Hngh*!"
    gen "So... *Ngh*-- You didn't blow me just to get out of trouble?"
    cho @ cheeks heavy_blush "*Ah*...{w=0.4} No...{w=0.4} Although normally, I probably would've considered...{w=0.4} *Ah*...{w=0.4} Justifying it that way." ("soft", "closed", "base", "stare", trans=d3)
    cho @ cheeks heavy_blush "But...{w=0.2} *Ah*...{w=0.4} The potion ...{w=0.2} *Ah*..." ("smile", "closed", "base", "mid")
    cho @ cheeks heavy_blush "Well, for some reason I don't feel the need to..." ("soft", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "And that...{w=0.2} *Ah*...{w=0.4} I shouldn't hide..." ("smile", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "The things I truly--{w=0.2}*Ah*...{w=0.4} Want from my coach." ("horny", "narrow", "base", "stare")
    gen "Clever little potion, that."
    gen "In that case, why don't you tell me..."
    cho @ cheeks heavy_blush "*Hmm*?" ("soft", "narrow", "base", "stare", trans=d3)
    gen "I knew you enjoyed showing off your body--"
    gen "But when did you start getting so naughty?"
    cho @ cheeks heavy_blush "That's the first thing you ask?" ("smile", "narrow", "raised", "stare", trans=d3)
    gen "Of course!"
    cho @ cheeks heavy_blush "*Giggles*..." ("grin", "closed", "base", "downR", trans=d3) #sound
    cho @ cheeks heavy_blush "Well--{w=0.2} *Ah*...{w=0.4} Let me think..." ("base", "closed", "base", "mid")
    cho @ cheeks heavy_blush "It--{w=0.2} *Ah*... It was probably when I first saw Hermione's naked--{w=0.2}*Ah*... Naked body in your office..." ("open", "narrow", "base", "stare")
    gen "*Heh-he*... I knew--"
    cho @ cheeks heavy_blush "It made me extremely--{w=0.2} *Ah*...{w=0.4} Angry...{w=0.4} And confused..." ("angry", "narrow", "base", "stare")
    gen "Oh?"
    cho @ cheeks heavy_blush "Yes! I had just won the game against Slytherin, and as I came--{w=0.2} *Ah*...{w=0.4} came in here to celebrate with my coach..." ("angry", "closed", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "Who do I see but Hermione Granger, smiling, and stark naked!" ("soft", "closed", "angry", "down")
    gen "Well... It wasn't--"
    cho @ cheeks heavy_blush "That's when I--{w=0.2} *Ah*...{w=0.4} When I realised that maybe I wanted more than just winning the cup." ("soft", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "I mean, I didn't even think to go celebrate with my team. I instinctively went straight to your office." ("annoyed", "base", "base", "stare")
    cho @ cheeks heavy_blush "And if there was any{w=0.2} *Ngh*...{w=0.4}  Any doubt after that..." ("open", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "Getting--{w=0.2} *Mmm*...{w=0.4} Getting that broom from Madam Hooch just proved it to me even more..." ("smile", "narrow", "base", "up")
    cho @ cheeks heavy_blush "Since I really had to try and figure out what makes me tick if I wanted to win the cup." ("smile", "narrow", "base", "up")
    cho @ cheeks heavy_blush "I couldn't help--{w=0.2}{nw}" ("soft", "narrow", "base", "up")
    cho @ cheeks heavy_blush "I couldn't help--{fast} *Ah*..." ("smile", "narrow", "base", "stare")
    cho @ cheeks heavy_blush "The only thing I could think about was what it would be like to have you bend me over and--{w=0.2}*Ah*...{w=0.4} fuck me on the commentator's podium with everyone watching me..." ("smile", "narrow", "base", "stare") #Big moan text
    gen "You little exhibitionist slut!"
    gen "If only they could see you now."
    cho @ cheeks heavy_blush "Yes! Let's call Hermione up here!" ("grin", "narrow", "base", "stare", trans=d3)
    gen "What?!"
    cho @ cheeks heavy_blush "*Giggles*" ("smile", "closed", "base", "mid", trans=d3)
    cho @ cheeks heavy_blush "Maybe some other time... She's probably still mad over their loss." ("smile", "narrow", "base", "stare")
    gen "And the fact that you came on that boy's face."
    cho @ cheeks heavy_blush "That's why he crashed?" ("soft", "base", "base", "stare", trans=d3)
    gen "..."
    cho @ cheeks heavy_blush "*Pfff-- Ha-ha-hah*!" ("grin", "happyCl", "base", "mid", trans=d3)
    gen "*Heh-heh*"
    gen "She looked so jealous too!"
    cho @ cheeks heavy_blush "..." ("soft", "base", "base", "stare", trans=d3)
    cho @ cheeks heavy_blush "She did?!" ("angry", "base", "base", "mid")
    gen "..."
    cho @ cheeks heavy_blush "Oh, you're just teasing me..." ("annoyed", "narrow", "base", "stare", trans=d3)
    cho @ cheeks heavy_blush "Well, two can play that game..." ("base", "narrow", "angry", "mid")

    hide cho_main

    #sexloop fast. #speedlines
    play background "sounds/sexloopfast.ogg"
    show image "cho_sex loop fast" as cg_doll
    with d1

    gen "*Argh*...{w=0.4} You little--"
    cho @ cheeks heavy_blush "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..." ("open_tongue", "narrow", "base", "up", trans=d3)
    gen "Someone's--{w=0.2} *Ngh*...{w=0.4} Suddenly eager for their reward--"
    cho @ cheeks heavy_blush "*Ah*...{w=0.2} *Ah*...{w=0.2} *Ah*..." ("open_tongue", "narrow", "base", "up", trans=d3)
    cho @ cheeks heavy_blush "Coach--" ("smile", "narrow", "base", "up")
    cho @ cheeks heavy_blush "I'm...{w=0.2} I'm close to--" ("smile", "narrow", "base", "up")
    gen "Me too!"

    with kissiris
    play sound "sounds/slick_01.ogg"
    cho @ cheeks heavy_blush "Coach!" ("scream", "narrow", "base", "up", trans=d3)
    with kissiris
    play sound "sounds/slick_01.ogg"
    cho @ cheeks heavy_blush "{heart}Aaaah!!!{w=0.4} Yes!!!{heart}" ("open_wide_tongue", "narrow", "base", "up", trans=d3)

    menu:
        "Take my champagne shower!!!":

            #Cho standing, dick inside
            cho @ cheeks heavy_blush "*Nnnngh*--{w=0.2} Wait!!" ("angry", "narrow", "base", "up")
            #Cho holding dick pose
            cho @ cheeks heavy_blush "I'm still...{w=0.4} I'm still--" ("clench", "narrow", "base", "up")
            gen "Too late!!!"
            #Pull out sound
            #Cho standing pose, genie body 3 (cho normal up, jacking it)
            stop background fadeout 2
            play sound "sounds/slick_02.ogg"
            show image "cho_sex up jerking" as cg_doll
            with d3

            pause .5
            gen "*Aaargh*!!"
            #Genie cums
            play sound "sounds/slick_01.ogg"
            show image "cho_sex up cum outside stage0" as cg_doll
            with d3
            pause 0.66
            show image "cho_sex up cum outside stage1" as cg_doll
            with d3

            pause 0.66
            play sound "sounds/slick_01.ogg"
            show image "cho_sex up cum outside stage2" as cg_doll
            with d3
            pause 0.66

            show image "cho_sex up cum outside stage3" as cg_doll
            with d3

            gen "*Ah*..."

            pause 1.0

            #Adds cum on Cho doll breasts and body
            $ cho.set_cum(breasts="light", body="light")

            gen "That's...{w=0.4} That's some mad timing on that pullout game..."
            cho @ cheeks heavy_blush "*Ah*...{w=0.4} *Ah*...{w=0.4} Gotta wait for just the--{w=0.2} *Ah*..." ("smile", "narrow", "base", "stare")
            cho @ cheeks heavy_blush "Right moment..." ("base", "narrow", "base", "up")
            #Cho standing tasting cum pose, dick outside (cum on dick)

            #TODO change for variant with cum on her chest included
            show image "cho_sex up taste outside" as cg_doll
            with d2

            cho @ cheeks heavy_blush "*Mmm*..." ("base", "closed", "base", "stare")
            cho @ cheeks heavy_blush "My reward..." ("smile", "closed", "base", "stare")
            cho @ cheeks heavy_blush "*Giggles*." ("smile", "closed", "base", "stare")

            $ states.cho.status.cumshot = True

        "Take my seed in your golden cup!":

            cho @ cheeks heavy_blush "My--" ("smile", "narrow", "base", "up")
            gen "*Aaaargh*!!!"

            show image "cho_sex middle" as cg_doll
            pause 0.25
            show image "cho_sex down" as cg_doll
            play sound "sounds/slick_01.ogg"
            with kissiris
            stop background fadeout 1


            cho @ cheeks heavy_blush "*Ah*!!! {w=0.5} {nw}" ("open_wide_tongue", "base", "base", "ahegao")

            with flashbulb
            play sound "sounds/slick_02.ogg"
            show image "cho_sex idle creampie" as cg_doll
            with d3
            gen "*Ah*...."
            cho @ cheeks heavy_blush "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*..." ("grin", "narrow", "base", "up", trans=d3)

            #Cho moves to stand pose (cycle images?)
            show image "cho_sex middle cum inside" as cg_doll
            with d2
            pause 0.25
            show image "cho_sex up cum inside" as cg_doll
            with d2
            pause 0.25
            play sound "sounds/slick_02.ogg"
            show image "cho_sex up cum outside" as cg_doll
            with d2

            cho @ cheeks heavy_blush "I think--{w=0.4} *Ah*...{w=0.4} I think I've finally found a fun activity to put into my workout routine..." ("smile", "narrow", "base", "stare")

            show image "cho_sex insert cum inside" as cg_doll
            with d2
            pause 0.25
            show image "cho_sex up taste" as cg_doll
            with d2

            #Cum sound
            #Cho standing tasting cum pose, dick outside (cum on dick)

            cho @ cheeks heavy_blush "*Mmm*..." ("smile", "closed", "base", "stare")
            gen "You naughty girl..."
            cho @ cheeks heavy_blush "*Giggles*..." ("smile", "narrow", "base", "mid", trans=d3)

            #Adds cum on Cho doll pussy
            $ cho.set_cum(pussy="heavy")

            $ states.cho.status.creampie = True

    #Office screen
    #Cho is naked in front of the desk

    stop music fadeout 1.0

    hide image cg_doll
    hide image cg_doll_effects
    call cho_chibi(xpos="desk", ypos="base", flip=False)
    with fade

    gen "That... was amazing!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "...{w=0.5}{nw}" ("soft", "narrow", "base", "stare", xpos="base", ypos="base", trans=d3)
    cho @ cheeks heavy_blush "...{fast}" ("soft", "wide", "base", "stare")
    gen "[name_cho_genie]?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Oh my god...{w=0.4} The potion!" ("disgust", "wide", "base", "stare")
    gen "What are you--" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "I can't believe it made me do that!" ("disgust", "narrow", "angry", "down")
    gen "Uh-Oh..." ("angry", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "...{w=0.8}{nw}" ("annoyed", "narrow", "angry", "mid")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    cho @ cheeks heavy_blush "...{fast}" ("grin", "narrow", "base", "mid") #smirks
    gen "*Heh-Heh*..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "*Giggles*" ("smile", "narrow", "base", "mid") #sound
    cho @ cheeks heavy_blush "Well then, I think I've almost run out of energy for today... I better spend the rest celebrating with everyone." ("smile", "narrow", "base", "mid")
    gen "Sure thing." ("base", xpos="far_left", ypos="head")
    gen "Although..." ("base", xpos="far_left", ypos="head")
    gen "Maybe take a shower first?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "*Hmm*... We'll see..." ("base", "narrow", "base", "R")
    #Cho walks to window
    call cho_walk(xpos=439, ypos=400)
    gen "*Ahem*..." ("base", xpos="far_left", ypos="head")
    #Cho turns
    cho @ cheeks heavy_blush "Yes?" ("soft", "base", "base", "mid")
    gen "You should probably put some clothes on..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Oh...{w=0.4} Well if I have to..." ("annoyed", "narrow", "base", "down")

    #cho walks to clothes pile and rummages through it
    call cho_walk(xpos=438, ypos=435)
    play sound "sounds/cloth_sound3.ogg"
    pause .8

    cho @ cheeks heavy_blush "*Huh*..." ("soft", "base", "base", "down", trans=d3)
    cho @ cheeks heavy_blush "My panties are missing." ("soft", "narrow", "base", "down")
    gen "Oh... *Err*..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Do you think Hermione took them?" ("soft", "narrow", "base", "mid")
    gen "...{w=0.4} Sure...{w=0.4} Why not." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Figured..." ("base", "narrow", "base", "downR")
    gen "I could probably get you another pair." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Nah." ("base", "narrow", "base", "R")
    cho @ cheeks heavy_blush "It'll be easier to ride the broom without them anyway." ("base", "narrow", "base", "down")

    #Cho gets dressed
    play sound "sounds/cloth_sound.ogg"
    hide cho_main
    $ cho.wear("all")
    $ cho.strip("panties")
    $ cho.set_cum(None)
    $ choq_accessory_protectors.zorder = 3

    hide screen cho_cloth_pile
    with d3
    pause 0.5

    call cho_walk(xpos=437, ypos=400)

    cho @ cheeks heavy_blush "Bye then!" ("smile", "base", "base", "mid", trans=d3)
    hide cho_main
    with d3
    pause .5

    play sound "sounds/boing05.ogg"
    call cho_chibi("hide")

    pause 1
    play sound "sounds/slick_02.ogg"
    with kissiris
    cho "{heart}{size=+4}*Ah*{/size}{heart}"
    gen "...{w} That girl sure is something else." ("base", xpos="far_left", ypos="head")

    if states.cho.level < 24:
        $ states.cho.level = 24
        call end_of_content

    $ states.ton.busy = True
    $ states.sna.busy = True
    $ states.her.busy = True
    $ states.lun.busy = True
    $ states.cho.busy = True

    #Reset zorder
    $ tonks.zorder = 15
    $ hooch.zorder = 15
    $ states.sna.image.zorder = 15
    $ cho.zorder = 15

    $ snape_chibi.zorder = 3

    #Reset Match specific clothing to player choice
    $ hermione.equip(her_outfit_last)
    $ tonks.equip(ton_outfit_last)
    $ luna.equip(lun_outfit_last)
    $ cho.equip(cho_outfit_last)

    $ choq_accessory_protectors.zorder = 27

    $ states.cho.tier = 4
    $ states.cho.favors_unlocked = False

    $ states.cho.ev.quidditch.lock_training = False
    $ states.cho.ev.quidditch.lock_practice = True
    $ states.cho.ev.quidditch.lock_tactic   = False
    $ states.cho.ev.quidditch.lock_training = True
    $ states.cho.ev.quidditch.gryffindor_stage = "completed"

    jump end_cho_event
