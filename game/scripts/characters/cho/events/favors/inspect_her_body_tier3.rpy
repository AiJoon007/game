
## Tier 3 - Event 1 ##

# Cho hops on your desk and she strips for you.
# You talk about the last match and Tonks' role in it.
# You tell Cho about Tonks' ability, and what she did to help winning the game.
# Notes: Cho could be naked at this point so some sounds/effects like cloth pile has been moved.

label cc_pf_strip_T3_intro_E1:

    call cc_pf_strip

    gen "Come closer, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]..." ("base", "narrow", "base", "mid")

    call cho_chibi("stand", "desk", "base")

    cho "" ("base", "base", "base", "mid", xpos="mid", ypos="base", trans=fade)

    gen "Would you like to hop on my desk and give me another show?" ("grin", xpos="far_left", ypos="head")
    cho "You want to look at my body again?" ("soft", "narrow", "raised", "mid")
    cho "Naturally you'd like to see if I've been keeping up with my workout? Staying in shape and all that..." ("soft", "narrow", "angry", "mid")

    menu:
        "\"Of course...\"":
            cho "[name_genie_cho], no need to continue the pretence..." ("open", "closed", "base", "mid")
            cho "We both know you don't really care about that stuff." ("open", "narrow", "base", "mid")
            cho "All you want to do is ogle at my naked body." ("soft", "narrow", "angry", "mid")
            cho "You're just like all the other teachers..." ("annoyed", "narrow", "base", "R")
            gen "You are one to say, you little slut!" ("base", xpos="far_left", ypos="head")
            gen "You went through quite the effort to show the whole school your ass on that broom..." ("base", xpos="far_left", ypos="head")
            cho "I only did that, so we'd win!" ("normal", "narrow", "angry", "mid")
            gen "Keep telling yourself that, you little show-off!" ("grin", xpos="far_left", ypos="head")
            gen "Come here and hop on my desk already!" ("grin", xpos="far_left", ypos="head")
            cho "..." ("annoyed", "narrow", "angry", "mid")

        "\"No, I just want to see your naked body up close.\"":
            gen "Let me see that ass of yours bounce, baby!" ("grin", xpos="far_left", ypos="head")
            cho "At least you are honest with me..." ("open", "closed", "base", "mid")
            cho "I can't really blame you, you're just a man, after all..." ("soft", "narrow", "base", "L")
            cho "And I'm simply irresistible." ("smile", "narrow", "angry", "mid")
            gen "That you are, you little slut!" ("grin", xpos="far_left", ypos="head")
            gen "Now hop onto my desk, so I can have a good look at you." ("grin", xpos="far_left", ypos="head")
            cho "Yes, [name_genie_cho]." ("base", "narrow", "angry", "mid")


    # Cho hops on your desk.
    call hide_characters
    show screen blkfade
    with d5
    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    call cho_chibi("stand", "on_desk", "on_desk", flip=False)
    hide screen bld1
    hide screen blkfade
    with d5
    call ctc

    cho "" ("base", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    call ctc

    gen "Yes! Show me what you got, you naughty girl!" ("grin", xpos="far_left", ypos="head")
    pause .2

    #Remove robes.
    if cho.is_worn("robe"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe")
        with d3
        pause .5

        cho "Let's just get rid of this thing to start with..." ("horny", "narrow", "base", "down")

    # Remove top.
    if cho.is_worn("top"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("top")
        with d3
        pause .5

        cho @ cheeks blush "" ("horny", "narrow", "angry", "mid")
        call ctc

        gen "Marvellous as always." ("grin", xpos="far_left", ypos="head")
        cho "I'm glad you're enjoying yourself, [name_genie_cho]..." ("base", "narrow", "angry", "down")
        gen "That I do!" ("grin", xpos="far_left", ypos="head")
        pause .2

    # Remove bottoms.
    if cho.is_worn("bottom"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bottom")
        with d3
        pause .5

        gen "Such a tease, just take it all off already!" ("base", xpos="far_left", ypos="head")
        cho "Patience, [name_genie_cho]..." ("base", "narrow", "base", "mid")

    # Remove bra.
    if cho.is_worn("bra"):
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bra")
        with d3
        pause .5

        gen "There they are... My favourite pair of Quaffles." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "..." ("base", "narrow", "base", "downR")

    # Remove panties + everything else.
    if cho.is_equipped("panties"):

        gen "And now your panties!" ("grin", xpos="far_left", ypos="head")
        cho "Of course, [name_genie_cho]..." ("smile", "narrow", "base", "mid")
        pause .2

        play sound "sounds/cloth_sound3.ogg"
        hide cho_main
        $ cho.strip("clothes")
        pause 1.2
        call cho_chibi("stand", "on_desk", "on_desk", flip=True)
        pause .4
        play sound "sounds/cloth_sound4.ogg"
        show screen cho_cloth_pile
        pause .6
        call cho_chibi("stand", "on_desk", "on_desk", flip=False)
        cho "" (trans=d3)
        pause .5

        cho @ cheeks blush "..." ("soft", "narrow", "base", "downR")
        cho @ cheeks blush "Here, [name_genie_cho]... You can have them." ("horny", "narrow", "angry", "mid")
        pause .5

        # Panties acquired message!
        call give_reward("You have acquired Cho's panties!", "interface/icons/panties.webp")
        $ states.cho.ev.panty_thief.acquired = True

    else:
        pause .8

        #Remove any remaining items (no sound since she might be naked)
        $ cho.strip("clothes")
        with d3
        pause .5

        cho @ cheeks blush "" ("horny", "narrow", "base", "mid")
        call ctc

    cho "Do you like watching me, [name_genie_cho]?" ("soft", "narrow", "base", "mid")
    cho "You should know, Sir, I'm {b}incredibly{/b} thankful for your help." ("open", "closed", "base", "mid")
    cho "Thanks to you, I get to do what I love..." ("smile", "narrow", "base", "mid")
    gen "Showing yourself off?" ("base", xpos="far_left", ypos="head")
    cho "No. Quidditch!" ("annoyed", "narrow", "angry", "mid")
    cho "Winning, to be precise..." ("soft", "narrow", "base", "mid")
    gen "Yes. I feel like a winner as well!" ("grin", xpos="far_left", ypos="head")
    cho "Although, to tell you a secret..." ("soft", "closed", "base", "mid")

    # mirror sprite
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=True)
    with d3
    pause .8

    cho "" ("smile", "narrow", "angry", "R", xpos=360, ypos="base", flip=True)
    pause .8

    cho @ cheeks blush "I am starting to love doing {b}this{/b} as well." ("soft", "narrow", "base", "R")
    gen "Yes, you little slut! Shake that ass for me!" ("grin", xpos="far_left", ypos="head")
    cho "I love the reaction I get from people..." ("base", "base", "base", "up")
    cho "From you... From Hermione..." ("soft", "narrow", "base", "downR")
    cho "Why don't we summon her? Maybe she'll join me this time..." ("base", "narrow", "base", "downR")
    cho "I think that could be fun." ("crooked_smile", "closed", "base", "mid")
    gen "Miss Granger, you say?" ("base", xpos="far_left", ypos="head")
    gen "How about we invite somebody else in her stead?" ("grin", xpos="far_left", ypos="head")
    pause .2

    # mirror sprite
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=False)
    with d3
    pause .5

    cho "Somebody else?" ("upset", "base", "raised", "mid", xpos="mid", ypos="base", flip=False)
    gen "Yes, to keep things interesting." ("grin", xpos="far_left", ypos="head")
    cho "*Hmm*..." ("annoyed", "base", "raised", "mid")
    cho "I suppose..." ("soft", "base", "base", "R")
    gen "Or are you only prepared to do it if you get to tease Miss Granger at the same time?" ("base", xpos="far_left", ypos="head")
    cho "*Hmm*...{w=0.3} Alright, what's one student over another." ("soft", "narrow", "base", "R")
    gen "It's not a student I'm thinking of." ("base", xpos="far_left", ypos="head")
    cho "What do you mean, Sir?" ("open", "base", "base", "mid")
    gen "I want you to strip for one of your teachers!" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "A teacher?" ("disgust", "wide", "base", "mid") # shocked
    cho @ cheeks blush "No way I could do that!" ("clench", "wide", "base", "mid")
    gen "Look at it as just another challenge." ("grin", xpos="far_left", ypos="head")
    cho "" ("annoyed", "base", "base", "mid")
    gen "The teachers already got a good look at your assets during the last couple of games." ("base", xpos="far_left", ypos="head")
    gen "And I know for a fact that a couple of them are quite interested in a closer look." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Oh, yeah?" ("soft", "base", "base", "down")
    cho @ cheeks blush "Then who is it that you have in mind?" ("open", "base", "base", "R")

    $ cc_strip_no_snape = False # throwaway var used only in the next event.

    label .choice:

    menu:
        "\"Tonks\"":
            pass

        "\"Snape\"" if cc_strip_no_snape == False:
            $ cc_strip_no_snape = True # throwaway var used only in the next event.
            cho @ cheeks blush "What?!" ("clench", "wide", "base", "mid")
            cho "You can't be serious!" ("angry", "base", "angry", "mid") # angry
            cho "[name_genie_cho], thanks to him, we almost lost the match!" ("open", "narrow", "angry", "mid")
            cho "He gave those idiots a luck potion, remember?" ("open", "closed", "angry", "mid")
            cho "You should have thrown him out for that!" ("clench", "narrow", "angry", "mid")
            gen "All I care about is that he and his band of greenhorns lost the match against us..." ("base", xpos="far_left", ypos="head")
            cho "..." ("annoyed", "narrow", "angry", "mid")
            cho "There is no way I'd ever strip for that greasy old bastard!" ("open", "narrow", "angry", "mid")
            cho "I'm not giving him the satisfaction." ("annoyed", "narrow", "angry", "R")
            gen "Very well, forget about Snape." ("base", xpos="far_left", ypos="head")
            gen "But what about..." ("base", xpos="far_left", ypos="head")
            jump .choice


    cho "Professor Tonks?" ("quiver", "base", "base", "mid")
    gen "You have yet to show her your gratitude for the help she provided..." ("base", xpos="far_left", ypos="head")
    gen "She was such an important player during that last match, and greatly helped us secure that win." ("base", xpos="far_left", ypos="head")
    cho "She did?" ("upset", "base", "raised", "mid")
    cho "I mean, she did get the Slytherins to join practice, but..." ("annoyed", "base", "raised", "R")
    cho "She wasn't even present for most of the actual game." ("soft", "base", "base", "R")
    gen "Are you sure about that?" ("grin", xpos="far_left", ypos="head")
    gen "Well, you would have hardly been able to recognize her..." ("base", xpos="far_left", ypos="head")
    cho "*Hmm*...?" ("annoyed", "base", "raised", "mid")
    gen "Curly long hair, and tits as big as honeydews." ("grin", xpos="far_left", ypos="head")

    gen "Did you not find Miss Granger's flirtatious behaviour with the Slytherin players a bit odd?" ("base", xpos="far_left", ypos="head")
    gen "You might even say... Familiar?" ("grin", xpos="far_left", ypos="head")
    cho "Are you suggesting that Professor Tonks..." ("mad", "base", "base", "mid")
    cho "But how?" ("clench", "base", "raised", "mid")
    gen "Magic...{w=0.8} Duh!" ("base", xpos="far_left", ypos="head")
    gen "How about we call her on your next visit, then you can ask her yourself..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "I suppose we could do that..." ("normal", "base", "base", "downR")
    gen "Splendid!" ("grin", xpos="far_left", ypos="head")
    gen "That should be all for today, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    gen "You're dismissed..." ("base", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]." ("base", "happyCl", "base", "mid")

    # Cho hops off your desk.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    play sound "sounds/08_hop_on_desk.ogg"
    call cho_chibi("stand", "desk", "base", flip=False)

    # Cho puts her clothes back on. (No sounds in case she never took any off)
    $ cho.wear("all")
    hide screen cho_cloth_pile
    with d3
    pause 1.5

    hide screen blkfade
    cho "" ("base", "narrow", "base", "mid", xpos="mid", ypos="base", trans=fade)
    pause .5

    if game.daytime:
        cho "I'll head back to classes, then." ("soft", "narrow", "base", "mid")
    else:
        cho "I'll head back to our dorms, then." ("soft", "narrow", "base", "mid")

    cho @ cheeks blush "Until next time, [name_genie_cho]." ("base", "narrow", "base", "mid")

    # Cho leaves.
    call cho_walk(action="leave")

    jump end_cho_strip_event


### Tier 3 - Event 2 ###

# Cho prompts genie to summon Tonks as she wants to know how she turned into Hermione
# Tonks enters and is immediately enticed by cho, she flirts with her a bit before cho starts asking questions.

label cc_pf_strip_T3_intro_E2:

    call cc_pf_strip

    gen "Alright, let's do this again." ("base", xpos="far_left", ypos="head")
    gen "We're gonna get your teacher up here -- and you'll strip for us, understood?" ("base", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]." ("smile", "base", "base", "mid")
    gen "You might want to change into your school clothing before she gets here..." ("base", xpos="far_left", ypos="head")
    cho "Of course." ("base", "happyCl", "base", "mid")

    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    # Equip Cho & Tonks default clothing.
    $ cho_outfit_last.save() # Store current outfit.
    $ ton_outfit_last.save() # Store current outfit.
    $ cho.equip(cho_outfit_default)
    $ tonks.equip(ton_outfit_default)

    call cho_chibi("stand", "desk", "base")

    hide screen blkfade
    cho "*Ehm*..." ("quiver", "narrow", "base", "downR", xpos="mid", ypos="base", trans=fade)
    cho "The teacher you're about to summon, [name_genie_cho]..." ("open", "narrow", "base", "mid")
    cho "You're talking about Professor Tonks, right?" ("soft", "narrow", "base", "mid") # suspicious
    gen "Oh... of course." ("base", xpos="far_left", ypos="head")
    cho "Well then, I'm ready." ("base", "base", "base", "mid")
    gen "Ready to strip for your teacher?" ("grin", xpos="far_left", ypos="head")
    cho "I'm well aware of what I'm about to do, [name_genie_cho], and I'm not going to falter." ("annoyed", "narrow", "angry", "mid")
    cho "Besides, it's not like I have any bits that she doesn't..." ("open", "closed", "base", "mid")
    gen "Not even trying to play coy anymore, are you?" ("base", xpos="far_left", ypos="head")
    cho "Why should I? It's good practice." ("open", "narrow", "raised", "down") # confident
    gen "Great positive thinking, [name_cho_genie].{w=0.8} You'll make it far with that mindset." ("grin", xpos="far_left", ypos="head")
    cho "It's no big deal for me, [name_genie_cho]." ("base", "narrow", "base", "mid")
    cho "I'm not as prude and buttoned up as Hermione, you know..." ("soft", "narrow", "base", "mid")
    cho "And I'll finally get to know how Professor Tonks helped us during the Slytherin match!" ("base", "happyCl", "base", "mid")
    gen "Oh boy, you're in for a treat!" ("grin", xpos="far_left", ypos="head")
    gen "Just wait here at my desk while I summon her..." ("base", xpos="far_left", ypos="head")
    cho "Yes, [name_genie_cho]." ("base", "narrow", "base", "mid")
    stop music fadeout 1

    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    call cho_chibi(flip=True)

    # end blkfade
    hide screen blkfade
    with d5
    pause .8

    # Tonks enters.
    play sound "sounds/door.ogg"
    call ton_chibi("stand", "door", "base")
    with d3
    pause .5

    # thought emote
    call chibi_emote("thought", "tonks")
    pause .8

    # Tonks walks next to Cho.
    call ton_walk(540, "base")

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    cho @ cheeks blush "" ("soft", "narrow", "worried", "L", xpos="left", ypos="base", flip=True)
    if game.daytime:
        ton "Hello, Professor." ("base", "base", "base", "mid", xpos="right", ypos="base")
    else:
        ton "Good evening, Professor." ("base", "base", "base", "mid", xpos="right", ypos="base")

    ton "Miss Chang. Didn't expect to see you here..." ("base", "narrow", "base", "L")
    ton "What a nice surprise." ("horny", "narrow", "base", "mid") # horny tongue
    cho @ cheeks blush "..." ("quiver", "narrow", "worried", "downR") # nervous
    cho @ cheeks blush "*Ehm*..." ("soft", "narrow", "worried", "down")
    gen "Go on, Cho. She's not going to bite you..." ("base", xpos="far_left", ypos="head")
    ton "*Hmm*?" ("base", "base", "raised", "mid")
    gen "Miss Chang was hoping she could repay you with a favour. For the help you provided against Slytherin." ("grin", xpos="far_left", ypos="head")
    ton "A favour, you say..." ("crooked_smile", "narrow", "base", "mid")
    cho @ cheeks blush "Y-yes, if that's okay with you, professor..." ("horny", "narrow", "worried", "L") # blushing, still nervous
    ton "Oh, anything for you, darling." ("base", "narrow", "base", "L")
    ton "So, what will it be then?" ("open", "base", "base", "mid")
    ton "I presume you didn't invite me for a cup of tea, did you?" ("base", "narrow", "base", "mid") # why remove?

    menu:
        "\"We need a second opinion on the girl's physique.\"":
            ton "*Mhmm*?" ("base", "base", "base", "mid")
            ton "So, naturally you thought of me to provide this... opinion?" ("open", "narrow", "raised", "mid")
            gen "You're quite the athletic witch yourself, are you not?" ("base", xpos="far_left", ypos="head")
            ton "" ("base", "narrow", "base", "mid")
            gen "I'm certain there's no one better suited to judge the girl's body than yourself." ("grin", xpos="far_left", ypos="head")
            ton "Very well, professor..." ("base", "base", "base", "mid")
            ton "I'm not the one to question the headmaster's judgement." ("base", "narrow", "base", "mid")
            gen "Great, then I'll look forward to hearing your assessment -- from head to toe please -- let us know if there's anything she could improve." ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "" ("normal", "happyCl", "worried", "mid")
            ton @ hair horny "Oh, I doubt I'll find anything to improve on this one..." ("horny", "narrow", "base", "L") # horny
            gen "Okay then..." ("base", xpos="far_left", ypos="head")
            gen "Girl, You may start with the show." ("base", xpos="far_left", ypos="head")
            ton "The show?!" ("soft", "base", "raised", "mid")
            gen "She'll have to take her clothes off, obviously!" ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "Oh my!" ("grin", "base", "shocked", "mid") # lip bite?
            gen "Let's get started then, shall we." ("base", xpos="far_left", ypos="head")
            ton @ hair horny "" ("base", "narrow", "base", "L")
            gen "Get on that desk, Miss Chang!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "Okay." ("soft", "narrow", "worried", "downR")

        "\"She's going to strip for us...\"":
            cho @ cheeks heavy_blush "" ("normal", "happyCl", "worried", "mid")
            ton @ hair horny "Really?" ("crooked_smile", "base", "shocked", "mid")
            cho @ cheeks blush "..." ("mad", "narrow", "worried", "downR") # embarrassed
            gen "It's all just part of the girl's training..." ("base", xpos="far_left", ypos="head")
            gen "To improve her confidence, and all that. And not shy away from a bit of nudity." ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "I see... so this is why you've been such a daredevil on the pitch lately..." ("horny", "narrow", "base", "L")
            cho @ cheeks blush "..." ("normal", "happyCl", "worried", "mid") #Blushes
            ton "Well, if you think I can be of assistance, then you have my full support." ("base", "base", "base", "L")
            cho @ cheeks blush "Thank you, Professor." ("soft", "narrow", "worried", "L")
            gen "Great! Then get on that desk, Cho!" ("grin", xpos="far_left", ypos="head")
            cho @ cheeks blush "Okay." ("soft", "narrow", "worried", "down")


    # Cho starts stripping.
    stop music fadeout 1
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    play sound "sounds/08_hop_on_desk.ogg"
    pause 1

    call cho_chibi("stand", 330, 360)
    call ton_chibi("stand", 410, "base")

    hide screen blkfade
    with d5
    pause .8

    call bld
    gen "Excellent..." ("base", xpos="far_left", ypos="head")
    gen "Now, what would you say are Miss Chang's best assets, Professor?" ("base", xpos="far_left", ypos="head")
    call bld("hide")
    pause .2

    # Cho turns around.
    call cho_chibi(flip=True)
    with d3
    pause .3

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    cho @ cheeks blush "" ("quiver", "narrow", "worried", "L", xpos=330, ypos="base", flip=True)
    ton "" ("base", "narrow", "base", "L", xpos=460, ypos="base")
    gen "Are you more into the girl's tits... or her ass?" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmm*--" ("base", "narrow", "annoyed", "L")
    cho @ cheeks heavy_blush "Sir!" ("soft", "happyCl", "worried", "mid")
    gen "It's a fair question..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("soft", "narrow", "worried", "L")
    ton "If you're not comfortable with this, Miss Chang, then I'm not going to--" ("open", "base", "base", "L")
    cho @ cheeks blush "No!" ("clench", "happyCl", "worried", "mid")
    ton "*Hmm*?" ("base", "narrow", "raised", "L")
    cho @ cheeks blush "I mean...{w=0.5} It's fine..." ("open", "narrow", "worried", "down")
    cho @ cheeks blush "Feel free to answer him, Professor..." ("soft", "narrow", "worried", "L")
    play sound "sounds/giggle2_loud.ogg"
    ton "*Giggles*" ("base", "happyCl", "base", "mid")
    ton "She's so cute when she's all flustered, isn't she?" ("crooked_smile", "base", "base", "mid")
    cho @ cheeks blush "..." ("quiver", "happyCl", "base", "mid") #Heavy blush
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "So, what's your opinion?" ("base", xpos="far_left", ypos="head")
    gen "I'm sure Miss Chang is dying to know..." ("grin", xpos="far_left", ypos="head")
    ton "I don't know how I could possibly answer such a difficult question, Professor." ("soft", "narrow", "base", "mid")
    gen "Then let me help you with your decision..." ("base", xpos="far_left", ypos="head")

    gen "Cho, do your thing." ("grin", xpos="far_left", ypos="head")
    ton "" ("base", "narrow", "base", "L")
    cho @ cheeks blush "Of course, Sir..." ("open", "narrow", "worried", "mid")
    cho @ cheeks blush "..." ("angry", "narrow", "base", "down")
    pause .2

    # Remove top.
    play sound "sounds/cloth_sound3.ogg"
    $ cho.strip("robe", "top")
    with d3
    pause .5

    cho @ cheeks blush "" ("horny", "happyCl", "worried", "mid")
    call ctc

    ton "*Hmm*... Very promising." ("base", "narrow", "base", "L")
    cho @ cheeks blush "..." ("horny", "narrow", "worried", "down")
    pause .2

    # Remove bra.
    play sound "sounds/cloth_sound3.ogg"
    $ cho.strip("bra")
    with d3
    pause .5

    ton @ hair horny "" ("base", "narrow", "raised", "L")
    cho @ cheeks heavy_blush "" ("quiver", "narrow", "base", "downR")
    call ctc

    ton @ hair horny "Merlin's burly bosom!" ("grin", "narrow", "annoyed", "L")
    cho @ cheeks heavy_blush "" ("upset", "happyCl", "worried", "mid")
    gen "How about now?" ("grin", xpos="far_left", ypos="head")
    gen "Ever seen such a perfectly shaped pair of quaffles before?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "Did you just call them quaffles?" ("soft", "narrow", "raised", "mid")
    cho @ cheeks blush "..." ("mad", "narrow", "worried", "downR")
    gen "So, what's your opinion?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "What would you like me to say, Professor?" ("base", "narrow", "base", "mid")
    ton @ hair horny "That I'd like to run my mouth all over those perky nipples of hers?" ("horny", "narrow", "angry", "L")
    cho @ cheeks heavy_blush "Professor!" ("open", "happyCl", "worried", "mid") # closed eyes, worried, embarrassed.
    ton @ hair horny "Sorry sweetie, but Professor Dumbledore wanted my honest opinion." ("open", "closed", "raised", "mid")
    ton @ hair horny "Your breasts are quite perfect, Miss Chang." ("base", "narrow", "base", "L")
    cho @ cheeks blush "..." ("normal", "narrow", "worried", "L")
    cho @ cheeks heavy_blush "I don't think they're big enough." ("open", "narrow", "worried", "downR") # sad
    cho @ cheeks heavy_blush "" ("normal", "narrow", "worried", "down")
    ton @ hair angry "Big enough for what? Impress some idiot?" ("open", "narrow", "annoyed", "L")
    ton "No offence, Professor." ("soft", "narrow", "base", "mid")
    gen "None taken..." ("base", xpos="far_left", ypos="head")
    ton "You don't need large breasts. Especially not if you want to have a career in Quidditch." ("open", "base", "base", "L")
    cho @ cheeks blush "" ("annoyed", "narrow", "base", "L")
    ton "Just have a look at mine... They're bothersome to fly with, even at my size..." ("soft", "base", "shocked", "down")
    stop music fadeout 1
    pause .2

    # Tonks starts stripping.

    # Remove robe.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("robe")
    with d3
    pause .5

    cho @ cheeks blush "" ("disgust", "base", "raised", "L")
    ton "" ("base", "happyCl", "base", "mid")
    call ctc

    cho @ cheeks blush "Professor, you don't have to--" ("mad", "base", "raised", "L") #blush
    pause .2

    # Remove top and bra.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("top", "bra")
    with d3
    pause .5

    ton @ hair horny "" ("horny", "narrow", "annoyed", "L")
    call ctc

    cho @ cheeks heavy_blush "P-{w=0.3}Professor!" ("silly", "happyCl", "worried", "mid") #lip bite "glances away from Tonks #Heavy blush
    gen "*He-he-he!*" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "No need to be shy, Miss Chang." ("base", "narrow", "base", "L")
    gen "Yes, it's not like she has any bits you haven't seen before... is that not what you said, Cho?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "R-Right." ("angry", "happyCl", "worried", "mid")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "L")
    gen "So... what would you like to see next, Miss Tonks?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "Her ass cheeks sure looked great on top of that broom..." ("soft", "narrow", "base", "mid")
    ton @ hair horny "I'd love to see them up close..." ("base", "narrow", "base", "L")
    gen "Couldn't agree more!" ("grin", xpos="far_left", ypos="head")
    gen "Cho, you heard your teacher's request." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("horny", "narrow", "worried", "mid")
    gen "Turn around, and take off your skirt." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, Sir." ("clench", "narrow", "worried", "mid")
    pause .2

    # Cho faces Genie.
    hide cho_main
    with d5
    call cho_chibi(flip=False)
    cho @ cheeks blush "" ("quiver", "narrow", "worried", "down", xpos=260, ypos="base", flip=False, trans=d5)
    pause .8
    ton @ hair horny "" ("base", "narrow", "base", "down")
    gen "Slowly..." ("base", xpos="far_left", ypos="head")
    pause .5

    # Remove bottom.
    play sound "sounds/cloth_sound3.ogg"
    $ cho.strip("bottom")
    with d5
    pause .5

    cho @ cheeks blush "" ("normal", "happyCl", "base", "mid")
    call ctc

    gen "And now the rest, Miss Chang." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "..." ("horny", "narrow", "base", "down") # horny
    pause .2

    # Remove all.
    play sound "sounds/cloth_sound3.ogg"
    hide cho_main
    $ cho.strip("clothes")
    pause 1.2
    play sound "sounds/cloth_sound4.ogg"
    show screen cho_cloth_pile
    pause .6

    cho @ cheeks heavy_blush "" ("horny", "narrow", "raised", "R")
    call ctc

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    gen "Quite firm, aren't they?" ("grin", xpos="far_left", ypos="head")
    play sound "sounds/giggle2_loud.ogg"
    ton @ hair horny "*Giggles*" ("base", "happyCl", "base", "mid")
    ton @ hair horny "Yes, Indeed..." ("grin", "narrow", "base", "mid")
    ton @ hair horny "No wonder she's so steady on that broomstick." ("horny", "narrow", "angry", "down")
    cho @ cheeks blush "..." ("horny", "narrow", "base", "mid") # blushing
    ton @ hair horny "Can't see anyone beating that, that's for sure." ("open", "narrow", "raised", "down")
    # ton "Although, maybe in a physical--"

    gen "So... what's your opinion, what do you prefer?" ("base", xpos="far_left", ypos="head")
    gen "Her tits, or her ass?" ("base", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmm*..." ("base", "narrow", "base", "down")
    ton @ hair horny "You're not holding out on me, are you, Miss Chang?" ("open", "narrow", "base", "L")
    cho @ cheeks blush "What do you--" ("angry", "narrow", "worried", "R")
    ton @ hair horny "There's something missing...{w=0.5} I haven't seen everything yet, have I?" ("crooked_smile", "narrow", "raised", "mid")
    gen "But of course!" ("grin", xpos="far_left", ypos="head")
    ton @ cheeks blush hair horny "If I were to do any sort of judgement, I'd first need to see that cute little Snitch of yours." ("soft", "narrow", "base", "down")
    cho @ cheeks heavy_blush "!!!" ("clench", "wide", "base", "mid") # shock
    gen "Miss Chang, why don't you turn around so Professor Tonks can give you a proper assessment." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "..." ("clench", "happyCl", "worried", "mid") # blush
    pause .2

    # Cho faces Tonks.
    hide cho_main
    with d5
    call cho_chibi(flip=True)
    cho @ cheeks heavy_blush "" ("normal", "happyCl", "worried", "mid", xpos=330, ypos="base", flip=True, trans=d5)
    pause .8

    ton @ hair horny "*Hmm*... Will you look at that..." ("base", "narrow", "base", "down")
    cho @ cheeks heavy_blush "..." ("horny", "narrow", "worried", "L")
    ton @ hair horny "Now, this is a level of confidence I haven't seen in a student before..." ("horny", "narrow", "base", "mid")
    gen "Yes, she's quite something, isn't she?" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "..." ("base", "closed", "base", "mid") # blushing but faking confidence
    ton @ hair horny "Although..." ("base", "narrow", "base", "L")
    ton @ hair horny "Does this snitch get frightened and dart away, once you try and get up close to it?" ("grin", "narrow", "raised", "mid")
    cho @ cheeks blush ".........." ("base", "closed", "base", "mid") #not paying much attention/didn't know she was being addressed
    ton @ hair horny "Miss Chang?" ("open", "narrow", "raised", "L")
    cho @ cheeks heavy_blush "Oh, sorry!" ("crooked_smile", "happyCl", "worried", "mid")
    cho @ cheeks blush "Of course not, Professor -- I don't dart away from anything!" ("soft", "narrow", "worried", "downR")

    ## Tonks wants to strip too. ##
    ton @ hair horny "Excellent, since that question has been answered..." ("base", "happyCl", "base", "mid")
    ton @ hair horny "I assume you don't mind if I joined you on that desk, do you?" ("horny", "narrow", "angry", "L")

    stop music fadeout 1
    cho @ cheeks blush "What?!" ("soft", "wide", "raised", "mid") # blushing
    gen "!!!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmm*... Or is that snitch of yours going to dart off after all?" ("soft", "narrow", "base", "down")
    cho @ cheeks blush "" ("angry", "happyCl", "worried", "mid")
    gen "(I sure hope the desk is sturdy enough...)" ("base", xpos="far_left", ypos="head")
    call hide_characters
    show screen blkfade
    with d5

    # Tonks chibi on desk next to Cho's. # Tonks is facing left

    call cho_chibi("stand", 314, 366, flip=True)
    call ton_chibi("stand", 370, 360, flip=False)

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    hide screen blkfade
    with d5
    pause .8

    $ cho.zorder = 16 # in front of Tonks. 15 is default.
    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton @ hair horny "" ("base", "narrow", "base", "L", xpos=345, ypos="base")
    cho @ cheeks heavy_blush "T-Tonks!" ("clench", "happyCl", "raised", "L", xpos=280, ypos="base", flip=True) #Closed eyes, embarrassed
    ton @ hair angry "That's {b}Professor Tonks{/b} to you, Miss Chang." ("open", "narrow", "angry", "L") # stern look
    cho @ cheeks heavy_blush "Sorry!" ("clench", "happyCl", "worried", "mid")
    play sound "sounds/giggle2_loud.ogg"
    ton @ hair horny "*Giggles*" ("base", "happyCl", "base", "mid")
    ton @ hair horny "I'm just kidding, you can call me whatever you like, sweetie..." ("soft", "narrow", "base", "L")
    ton @ hair horny "Catch that Snitch for me, will you..." ("horny", "narrow", "base", "L")
    cho @ cheeks blush "Snitch? What Snitch?" ("soft", "narrow", "base", "L")
    ton @ hair horny "Down here." ("grin", "narrow", "base", "down")
    cho @ cheeks blush "" ("annoyed", "narrow", "base", "down")
    pause .2

    # Remove bottom.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("bottom","panties")
    with d3
    pause .5

    ton @ hair horny "" ("horny", "narrow", "base", "down")
    pause .8

    cho @ cheeks blush "!!!" ("normal", "wide", "raised", "down")
    gen "Now that's what I'm talking about!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Professor!" ("clench", "wide", "raised", "down")
    ton @ hair horny "Believe me, I'm just getting started..." ("base", "narrow", "base", "mid")
    pause .5

    # Remove other clothes.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("clothes")
    with d3
    pause .5

    ton @ hair horny "" ("horny", "narrow", "base", "L")
    cho @ cheeks heavy_blush "" ("base", "narrow", "worried", "down")
    call ctc

    cho @ cheeks heavy_blush "..." ("angry", "narrow", "worried", "downR") # heavy blush
    gen "Don't be shy, Miss Chang." ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "*Hmm*... Yes, don't be shy." ("crooked_smile", "narrow", "base", "L")
    ton @ hair horny "I've yet to give you my verdict." ("soft", "narrow", "raised", "down")
    cho @ cheeks heavy_blush "..." ("normal", "happyCl", "worried", "mid")
    ton @ hair horny "Now, up this close, it's obvious what your best feature is, Miss Chang..." ("open", "narrow", "base", "down")
    ton @ hair horny "I must say I simply love your--" ("horny", "narrow", "base", "down")

    # Snape enters.
    stop music fadeout 1
    call hide_characters
    hide screen bld1
    with d3

    play sound "sounds/door.ogg"
    call sna_chibi("stand", "door", "base")
    with d3
    pause .1

    call bld
    gen "*Hmm*...?" ("base", xpos="far_left", ypos="head")
    with hpunch
    gen "{b}Balls!{/b}" ("angry", xpos="far_left", ypos="head")
    sna "..." ("snape_47", ypos="head") #smirk
    ton "What? No, I was talking about her--" ("soft", "narrow", "base", "mid", ypos="head", flip=False)
    with hpunch
    cho "Professor Snape?!" ("open", "wide", "raised", "L", ypos="head", flip=True) # shock
    sna "Oh-- now what do we have here?..." ("snape_13", ypos="head")
    call bld("hide")
    pause .2

    # Tonks turns around.
    call ton_chibi(xpos=360, ypos=360, flip=True)
    with d3

    # Snape walks closer to the middle.
    call sna_walk(xpos="mid", ypos="base")
    pause .8

    # Position Cho's sprite behind Tonks.
    $ cho.zorder = 15 # reset to default.
    $ tonks.zorder = 16 # in front of Cho. 15 is default.
    play music "music/Dark Fog.ogg" fadein 1 if_changed
    sna "" ("snape_40", xpos=560, ypos="base")
    cho "" ("normal", "wide", "base", "L", xpos=275, ypos="base", flip=True)
    ton "" ("annoyed", "narrow", "annoyed", "L", xpos=390, ypos="base", flip=True)

    ton "Severus?" ("mad", "base", "base", "L", trans=d5)
    ton "{size=-4}Get behind me, Cho...{/size}" ("open", "narrow", "base", "R") #small text

    $ cho_chibi.zorder = 2 # default is 3
    call cho_chibi("stand", 320, 366, flip=True)
    cho @ cheeks heavy_blush "{size=-4}Yes-- Thank you.{/size}" ("disgust", "happyCl", "worried", "mid", xpos=295, ypos=17, flip=True, trans=d3) # Sprite is slightly lowered.

    ton "What are you doing here?" ("annoyed", "base", "angry", "stare")
    ton @ hair horny "Have you been spying on us behind that door?" ("soft", "narrow", "base", "up")
    sna "Of course not..." ("snape_46")
    cho @ cheeks heavy_blush "P-{w=0.3}Professor..." ("open", "happyCl", "worried", "mid")
    ton @ hair horny "" ("base", "narrow", "base", "downR")

    sna "Ah, Miss Chang... Hiding behind Professor Tonks, are we?" ("snape_02")
    sna "I take it you're here to repay our headmaster for his help with your sudden Quidditch success?" ("snape_37")
    #sna "But how come Professor Tonks--" ("snape_01")
    ton @ hair horny "Well, what if she is,{w=0.5} Snivellus?" ("soft", "narrow", "annoyed", "R")
    sna "" ("snape_38")
    ton @ hair horny "She isn't doing anything wrong... at least not by your standards." ("grin", "closed", "shocked", "mid")
    sna "Did I accuse her of doing anything wrong?" ("snape_09")
    sna "On the contrary..." ("snape_02")
    ton "" ("annoyed", "narrow", "raised", "up")
    sna "As head of the slytherin house, I'd like to personally congratulate her on her fair play." ("snape_37")
    sna "Your performance was quite remarkable, Miss Chang." ("snape_13")
    sna "Putting your best {b}ass{/b}ets on display for everyone was quite the sight." ("snape_46")
    cho @ cheeks heavy_blush "..." ("angry", "narrow", "worried", "downR") # embarrassed
    sna "How very -- {b}ass{/b}piring of you..." ("snape_41")
    cho @ cheeks heavy_blush "{size=-4}Please do something, sir.{/size}" ("soft", "base", "angry", "mid") #small text
    gen "What?" ("base", xpos="far_left", ypos="head")
    gen "(Oh, right... I should probably do something about this...)" ("base", xpos="far_left", ypos="head")

    menu:
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\"Severus, I think you should leave.\"":
            cho @ cheeks blush "" ("normal", "base", "angry", "L")
            sna "Already? But I just got here..." ("snape_05")
            ton "I can't recall us inviting you, Severus." ("soft", "narrow", "shocked", "L")
            sna "Do I require some kind of appointment to see the headmaster?" ("snape_09")
            sna "If there's a schedule I could look at, then perhaps I could plan my visits for when Miss Chang is not busy working on her insecurities..." ("snape_03")
            #sna "If there's a schedule I could look at, then perhaps I could plan my visits for when you two aren't taking advantage of Miss Chang's insecurities..." ("snape_03") # Alternative line instead of the one above?
            cho @ cheeks blush "..." ("angry", "narrow", "angry", "L") #Blush #closed eyes #embarrassed
            #gen "How did you--" ("base", xpos="far_left", ypos="head")
            ton "What do you want, Snape?" ("upset", "narrow", "annoyed", "L")

        "\"Severus! Please, stay and watch.\"":
            if cc_strip_no_snape: # Cho clearly told you she won't strip for Snape.
                $ states.cho.mood += 30
                cho "Are you mad?!" ("clench", "base", "angry", "mid", trans=hpunch)
                cho "Sir, I clearly told you before, I won't do this in front of Professor Snape!" ("open", "base", "angry", "mid")
                sna "So you actually considered inviting me..." ("snape_20")
                cho @ cheeks blush "" ("normal", "base", "angry", "L")
                sna "That's surprising, considering our current bet..." ("snape_21")
                sna "I must admit, however, that I appreciate the gesture, Albus." ("snape_22")
                gen "Bros before--" ("grin", xpos="far_left", ypos="head")
                ton "Quiet! Both of you!" ("open", "closed", "base", "mid")
                sna "*Tssz*..." ("snape_46")
                sna "Well, I can read the room..." ("snape_09")
                ton "Clearly..." ("upset", "narrow", "raised", "L")
                sna "As it happens, I can't stay for too much longer anyway." ("snape_03")

            else:
                $ states.cho.mood += 12
                cho @ cheeks heavy_blush "Sir, you can't be serious!" ("angry", "wide", "raised", "mid")
                gen "Calm yourself, girl." ("base", xpos="far_left", ypos="head")
                gen "There's no touching allowed anyway... Those are the rules." ("base", xpos="far_left", ypos="head")
                ton @ hair horny "Really? You never told me--" ("annoyed", "narrow", "raised", "mid") #pout
                cho @ cheeks heavy_blush "Send him away!" ("clench", "base", "angry", "mid")
                gen "Whatever... no need to get all indignant about this." ("angry", xpos="far_left", ypos="head")
                sna "..." ("snape_09")
                gen "You more than happily strip for all your other teachers... so why not Snape?" ("base", xpos="far_left", ypos="head")
                cho "All my other teachers? It was only you and Tonks that I agreed to do this for!" ("clench", "wide", "raised", "mid")

    sna "As much as I'd like to watch you make a fool of yourself for us, Miss Chang, I have more important things to do." ("snape_13")
    gen "(More important than this?...)" ("base", xpos="far_left", ypos="head")
    sna "I merely came here to discuss a private matter with our headmaster." ("snape_24")
    sna "About this... misunderstanding that occurred during the last Quidditch game." ("snape_09")

    cho "There is nothing more to discuss." ("open", "closed", "angry", "R")
    cho "We won against you, fair and square, you cheat..." ("clench", "narrow", "angry", "L")
    sna "Hold your tongue, Miss Chang, or I'll have to dock some points from your house..." ("snape_03")
    sna "Or worse..." ("snape_20") #smirks
    cho "*Pfff*... only first years care about house points..." ("annoyed", "narrow", "base", "R") # small text
    gen "Not taking that loss easy, are you? Disappointed that we won -- against all odds?" ("grin", xpos="far_left", ypos="head")
    sna "*Tzzzs*... by sheer luck you did." ("snape_32")
    cho @ cheeks blush "Says the one who literally gave his team liquid luck!" ("disgust", "narrow", "angry", "L")
    sna "Ten points from Ravenclaw!" ("snape_31")
    $ ravenclaw -= 10
    cho @ cheeks blush "{size=-4}Like I care...{/size}" ("annoyed", "narrow", "angry", "down")
    ton "Let the girl speak her mind, Severus!" ("open", "closed", "shocked", "mid")
    ton "Or shall I remind you that you were the one who barged in here uninvited..." ("open", "narrow", "base", "L")
    sna "*Hmph*..." ("snape_35")
    sna "Can't let her spew such lies in the headmaster's presence, can I?" ("snape_03")
    gen "The hell is that supposed to mean?" ("base", xpos="far_left", ypos="head")
    sna "I merely gave those boys some encouragement." ("snape_04")
    sna "There was no need to involve something as valuable as a luck potion..." ("snape_09")
    cho @ cheeks blush "What?!" ("angry", "happyCl", "angry", "mid")

    # Cho stops hiding behind Tonks.
    stop music fadeout 1
    $ cho_chibi.zorder = 3 # Reset to default.
    call cho_chibi("stand", 314, 366, flip=True)
    ton "" ("annoyed", "narrow", "raised", "downR")
    cho "But the entire Slytherin team drank some! They were even bragging about it!" ("clench", "narrow", "angry", "L", xpos=275, ypos="base", flip=True, trans=hpunch)

    sna "I suppose if that's what they said, then who am I to refute it..." ("snape_37") #smirk
    sna "Now, if you'll excuse me..." ("snape_09")
    sna "I'll leave you three to indulge further in your...{w=0.8} debaucheries..." ("snape_47")
    cho "No! You stay where you are!" ("scream", "base", "angry", "L")
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    # Cho moves in front of Tonks.
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    $ cho_chibi.zorder = 2 # Behind Tonks, so her ponytail doesn't cover her head.
    call ton_chibi("stand", 322, 360, flip=True)
    call cho_chibi("stand", 360, 360, flip=True)
    with d3
    pause .5

    $ tonks.zorder = 15 # Reset to default.
    $ cho.zorder = 16 # In front of Tonks. Default is 15.
    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    sna "" ("snape_13")
    ton @ hair horny "" ("annoyed", "shocked", "raised", "stare", xpos=310, ypos="base", flip=True)
    cho "First you're going to explain yourself!" ("clench", "base", "angry", "L", xpos=415, ypos="base", flip=True, trans=hpunch)
    ton @ cheeks blush hair horny "" ("clench", "wide", "shocked", "L")
    cho "You somehow tricked them! They played far better than usual." ("mad", "base", "angry", "L")
    ton @ cheeks heavy_blush hair horny "" ("horny", "narrow", "worried", "down")
    sna "*Hmm*... Very well, Miss Chang." ("snape_20")

    # Space Jam
    sna "You truly believe I'd waste such a valuable potion on those blokes?" ("snape_18")
    cho "" ("annoyed", "base", "angry", "L")
    sna "It takes three months to brew and distil only a tiny vial of Felix Felicis... and it's quite the tedious endeavour to do so." ("snape_12")
    sna "That prize money would barely cover half of the materials..." ("snape_03")
    cho "Prize money? What prize money?!" ("open", "base", "angry", "mid")
    gen "Don't interrupt your teacher." ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush hair horny "" ("base", "narrow", "worried", "L")
    cho "" ("annoyed", "narrow", "angry", "L")
    sna "I merely provided them with a vial of pumpkin juice..." ("snape_41")
    sna "Then I told them I mixed in some liquid luck." ("snape_13")
    cho "What stupid kind of tactic is that?" ("soft", "narrow", "angry", "mid")
    sna "" ("snape_39")
    ton @ cheeks blush hair horny "" ("base", "narrow", "base", "mid")
    gen "Hold on a minute..." ("angry", xpos="far_left", ypos="head")
    gen "Are you seriously telling me you gave them pumpkin juice... and pretended it was \"{b}Michael's secret stuff{/b}\"?" ("base", xpos="far_left", ypos="head")
    sna "Michael's...{w=0.3} what?" ("snape_38")
    gen "You ripped off {b}Space Jam{/b}!" ("angry", xpos="far_left", ypos="head")
    sna "I'm sorry?" ("snape_25") # confused
    gen "You ripped off the plot of Space Jam!" ("angry", xpos="far_left", ypos="head")
    sna "I have no idea what you're talking about..." ("snape_44")
    ton @ hair horny "Neither do I." ("annoyed", "base", "raised", "mid")
    cho "Sir, is this about that basketball thing again?" ("disgust", "narrow", "angry", "mid")
    gen "Even Bugs Bunny couldn't help him win. Serves you right!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "Who's Bugs Bunny?" ("soft", "narrow", "raised", "mid")
    gen "Oh boy, let me tell you--" ("grin", xpos="far_left", ypos="head")
    sna "Anyway." ("snape_31")
    cho "" ("annoyed", "narrow", "angry", "L")
    sna "Miss Chang, I wish you the very best of luck on your next match." ("snape_45")
    ton @ hair horny "" ("normal", "narrow", "base", "L")
    sna "You lot look like you're going to need it..." ("snape_42")
    cho "*Hmph*..." ("annoyed", "base", "angry", "L")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    stop music fadeout 1
    call hide_characters
    hide screen bld1
    with d3
    pause .1

    # Snape walks to the door.
    call sna_walk("door", "base")
    pause .2

    call sna_chibi("stand", "door", "base", flip=False)
    with d3
    pause .5

    sna "Until then, Albus... Miss Chang..." ("snape_20", xpos="base", ypos="head")
    sna "{cps=7}Nymphadora...{/cps}" ("snape_41", xpos="base", ypos="head")
    ton @ hair angry "Stop calling me--" ("clench", "closed", "angry", "mid", ypos="head", flip=True)

    # Snape leaves.
    call sna_chibi("stand", "door", "base", flip=True)
    with d3
    call sna_chibi("leave")
    pause .5

    call bld
    gen "Fucking guy..." ("base", xpos="far_left", ypos="head")
    gen "Who does he think he is?" ("base", xpos="far_left", ypos="head")
    gen "Besmirching a classic such as Space Jam, like it was nothing..." ("base", xpos="far_left", ypos="head")

    # The girls face Genie.
    hide screen cho_chibi
    hide screen tonks_chibi
    $ cho_chibi.zorder = 2
    call cho_chibi("stand", 330, 364, flip=False)
    call ton_chibi("stand", 370, 360, flip=False)
    with d3

    cho "" ("annoyed", "narrow", "base", "mid", xpos=190, ypos="base", flip=False)
    ton "Well, that was a bit uncalled-for... even for him." ("open", "narrow", "annoyed", "R", xpos=350, ypos="base", flip=False, trans=d5)

    ton "When did I step on his toes?" ("upset", "base", "base", "mid")
    gen "Maybe when you called him Snivellus--" ("base", xpos="far_left", ypos="head")
    ton "I'm not even part of your silly bet..." ("upset", "base", "shocked", "downR")
    cho "Bet?" ("angry", "narrow", "raised", "mid")
    gen "Let's not concern ourselves with Snape. He's out of the picture anyway." ("base", xpos="far_left", ypos="head")
    cho "What bet?" ("open", "narrow", "angry", "mid")
    ton "So, shall we wrap things up, Professor?" ("base", "happyCl", "base", "mid")
    gen "Yes please." ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")

    if game.daytime:
        ton @ hair horny "Let me escort you back to class, Miss Chang." ("soft", "base", "base", "L")
    else:
        ton @ hair horny "Let me escort you back to your common room. It's getting late." ("soft", "base", "base", "L")

    # Fade to black.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    # The girls get dressed and wait at the door.
    $ cho.wear("all")
    $ tonks.wear("all")

    # Reset zorder.
    $ cho.zorder = 15 # reset to default.
    $ tonks.zorder = 15 # reset to default.
    $ cho_chibi.zorder = 3 # reset to default.
    $ tonks_chibi.zorder = 3 # reset to default.
    hide screen cho_cloth_pile

    call cho_chibi("stand", 690, "base", flip=False)
    call ton_chibi("stand", "door", "base", flip=False)

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    hide screen blkfade
    with d5
    pause .5

    ton "Thank you for your time, Professor." ("base", "base", "base", "mid", ypos="head", flip=False)
    if game.daytime:
        cho "Good day, Sir." ("base", "base", "base", "mid", ypos="head", flip=False)
    else:
        cho "Good night, Sir." ("base", "base", "base", "mid", ypos="head", flip=False)
    gen "Until next time." ("grin", xpos="far_left", ypos="head")
    call bld("hide")
    pause .1

    # They both leave.
    call cho_chibi(flip=True)
    pause .3
    call ton_chibi(flip=True)
    with d3
    pause .2

    play sound "sounds/door.ogg"
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    pause .5


    # Reset clothing.
    $ cho.equip(cho_outfit_last)
    $ tonks.equip(ton_outfit_last)

    $ states.ton.busy = True
    $ states.sna.busy = True

    # End event.
    jump end_cho_strip_event


### Tier 3 - Event 3 ###

# Cho and Tonks strip on your desk again.
# CG: Tonks spreading and spanking Cho's ass.
# Tonks gives Cho a demonstration of her Metamorphmagi ability.

label cc_pf_strip_T3_intro_E3:
    gen "[name_cho_genie], why don't we summon your teacher again?" ("base", xpos="far_left", ypos="head")
    cho "So we can give you another show, [name_genie_cho]?" ("soft", "narrow", "angry", "mid") # annoyed
    gen "Well, if you insist on it..." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "" ("annoyed", "narrow", "angry", "mid")
    gen "Surely you haven't forgotten the actual reason we summoned her..." ("base", xpos="far_left", ypos="head")
    cho "Of course not..." ("open", "closed", "base", "mid")
    cho "I wanted to ask her about what she did during the Slytherin match..." ("annoyed", "narrow", "base", "mid")
    cho @ cheeks blush "But then Professor Snape busted in before I got a chance to." ("angry", "narrow", "angry", "R")
    gen "Right... let's give it another go then, shall we?" ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "But no Snape this time!" ("soft", "narrow", "angry", "mid")
    cho @ cheeks blush "If you expect me to expose myself to Professor Snape again, then you're sadly mistaken!" ("clench", "base", "angry", "mid")
    gen "No more Snivellus... got it..." ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "angry", "mid")
    gen "Wait here at my desk while I summon your Teacher." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, [name_genie_cho]." ("soft", "narrow", "worried", "R")

    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5
    pause 1

    # (Cho's outfit doesn't change this time.)
    #$ cho_outfit_last.save() # Store current outfit.
    $ ton_outfit_last.save() # Store current outfit.
    $ her_outfit_last.save() # Store current outfit.
    #$ cho.equip(cho_outfit_default)
    $ tonks.equip(ton_outfit_default)   # Equip Tonks default clothing.
    $ hermione.equip(her_outfit_default)    #Equip Hermione default clothing.
    $ cho.strip("robe") # removes school robe.

    call cho_chibi("stand", "desk", "base", flip=True)

    stop music fadeout 1
    hide screen blkfade
    with d5
    pause .8

    nar "You attempt to summon Tonks to your office."
    pause .2

    call bld
    gen "..." ("base", xpos="far_left", ypos="head")
    cho "..." ("quiver", "narrow", "base", "L", ypos="base", flip=True)


    # Fireplace turns on.
    if not states.fireplace_started:
        pause .2
        $ states.fireplace_started = True
        $ fireplace_OBJ.foreground = "fireplace_fire"
        with d5
        pause .8

    gen "..................?" ("base", xpos="far_left", ypos="head")
    call bld("hide")
    pause .5

    # Fire flashes green. # Tonks appears in the fireplace.
    play sound "sounds/fire_woosh.ogg"
    $ states.fireplace_started = True
    show screen gfx_effect(690, 330, img="smoke", zoom=0.5)
    pause .1
    $ fireplace_OBJ.foreground = "fireplace_greenfire"
    call ton_chibi("stand", 642, 392, flip=False) # In fireplace
    with d5

    # Tonks walks next to Cho.
    call ton_walk(540, "base")
    pause .8

    # Fireplace turns off.
    stop background #Stops playing the fire SFX.
    $ states.fireplace_started = False
    $ fireplace_OBJ.foreground = None
    with d5
    pause .2

    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    cho @ cheeks blush "" ("base", "narrow", "worried", "L", xpos="left", ypos="base", flip=True)
    ton "You called?" ("base", "narrow", "base", "mid", xpos="right", ypos="base")

    cho @ cheeks blush "Hello, Professor." ("soft", "narrow", "worried", "L")
    gen "What{w=0.3} {b}the fuck{/b} just happened?" ("angry", xpos="far_left", ypos="head")
    ton "Oh, my apologies... I forgot we don't usually use the school's floo powder network." ("grin", "base", "base", "mid")
    gen "Network? Do I need to set a password on my fireplace now?" ("base", xpos="far_left", ypos="head")
    cho "" ("annoyed", "narrow", "base", "mid")
    gen "Could anyone just poof in here as they please?" ("base", xpos="far_left", ypos="head")
    ton "At the moment, yes." ("silly", "happyCl", "base", "mid")
    gen "(So much for privacy in this place...)" ("base", xpos="far_left", ypos="head")
    ton "You might want to renew the protective enchantments that were cast on it. It's quite the security flaw." ("upset", "base", "raised", "mid")
    gen "I'll have the {b}IT{/b} guy sort it out... A simple firewall should do it..." ("base", xpos="far_left", ypos="head")
    ton "Anyhow, I thought it'd be faster than walking those dreadful stairs." ("base", "base", "base", "mid")
    ton "Even if it's a bit of a waste of powder..." ("upset", "base", "shocked", "down")
    cho "They are by no means dreadful, Professor Tonks." ("open", "narrow", "base", "L")
    ton "" ("base", "base", "raised", "L")
    cho "Without a gym, there's only a limited number of ways to do any exercises here at school." ("open", "closed", "base", "mid")

    menu: # change
        gen "(...)" ("base", xpos="far_left", ypos="head")
        "\".............\"": # Genie lets them speak
            cho "I take divination lessons solely as an opportunity to climb the north tower once a week." ("base", "happyCl", "base", "mid")
            ton "Of course you do..." ("base", "base", "base", "L")
            ton @ hair horny "(Those thick legs have to come from somewhere.)" ("grin", "narrow", "base", "mid")
            ton @ hair horny "I had a hunch that something special was in store for me today." ("horny", "narrow", "raised", "mid")

        "\"You could exercise with me!\"":
            gen "I can give you a workout of the likes you've never seen!" ("grin", xpos="far_left", ypos="head")
            ton @ hair horny "" ("base", "narrow", "annoyed", "mid")
            cho "*Hmm*?" ("soft", "base", "raised", "mid")
            gen "I'll wear you out until your muscles are sorer than ever!" ("angry", xpos="far_left", ypos="head")
            cho "Really!?" ("crooked_smile", "base", "base", "mid") # happy
            ton @ hair horny "Now-now, Professor. Don't make promises you can't keep..." ("soft", "narrow", "base", "mid")
            cho "Why haven't you shown me any of these workouts, sir?" ("open", "base", "angry", "mid")
            gen "We'll get to it at some point, I'm sure." ("base", xpos="far_left", ypos="head")
            ton @ hair horny "I sure wouldn't mind seeing you try out his techniques as well." ("grin", "narrow", "base", "L")
            gen "No objections here!" ("grin", xpos="far_left", ypos="head")
            cho "Wicked!" ("grin", "happyCl", "base", "mid")

    ton @ hair horny "Come on, Miss Chang..." ("open", "narrow", "base", "L")
    cho "" ("annoyed", "base", "base", "L")
    ton @ hair horny "Let's give our headmaster a good show!" ("crooked_smile", "narrow", "base", "mid")
    cho "Alright." ("open", "happyCl", "base", "mid")
    ton @ hair horny "Now, after you..." ("horny", "narrow", "base", "L")

    # Cho and Tonks hop onto the desk.
    call hide_characters
    hide screen bld1
    with d3
    pause .2

    call cho_chibi(flip=False)
    with d3
    pause .1

    show screen blkfade
    with d5


    # Tonks chibi on desk next to Cho's. # Tonks is facing left

    call cho_chibi("stand", 314, 366, flip=True)
    call ton_chibi("stand", 370, 360, flip=False)

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    hide screen blkfade
    with d5
    pause .8

    $ cho.zorder = 16 # in front of Tonks. 15 is default.
    cho @ cheeks heavy_blush "" ("base", "narrow", "base", "L", xpos=280, ypos="base", flip=True)
    ton @ hair horny "..." ("base", "narrow", "raised", "L", xpos=345, ypos="base")
    ton @ hair horny "Are you watching closely, Professor?" ("open", "narrow", "base", "mid")
    gen "You bet!" ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "I wouldn't want you to miss what's about to happen..." ("base", "narrow", "base", "mid")

    # Cho and Tonks undress.
    $ temp_var = False
    if cho.is_any_worn("robe", "top", "bottom"):
        $ temp_var = True
        ton @ hair horny "Let me help you with that, Miss Chang." ("soft", "narrow", "base", "L")
        ton @ hair horny "" ("base", "narrow", "base", "L")

    # Remove Cho's robe. #TODO are they not already removed near the start of the event?
    if cho.is_worn("robe"):
        pause .2
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("robe")
        with d3
        pause .5
        cho @ cheeks blush "" ("base", "narrow", "base", "R")
        pause .8

    # Remove Cho's top.
    if cho.is_worn("top"):
        pause .2
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("top")
        with d3
        pause .5
        cho @ cheeks heavy_blush "" ("horny", "narrow", "raised", "R")
        pause .8

        nar "Tonks swiftly pulls the girl's top over her chiselled frame."

    # Remove Cho's bottom.
    if cho.is_worn("bottom"):
        cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "mid") # embarrassed
        pause .2
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bottom")
        show screen cho_cloth_pile
        with d3
        pause .5
        cho @ cheeks heavy_blush "" ("horny", "narrow", "raised", "R")
        pause .8

        nar "A quick tug by her teacher, and Cho's bottom clothing slips down her muscular things."

    if temp_var == True:
        cho @ cheeks heavy_blush "Please, Professor...{w=0.4} not so fast." ("clench", "happyCl", "base", "mid") # embarrassed?
        gen "..." ("grin", xpos="far_left", ypos="head")
        ton @ hair horny "*Hmm*... Okay then." ("base", "narrow", "raised", "mid")
        ton @ hair horny "I'll go next, shall I?" ("grin", "narrow", "base", "mid")
    else: # Cho was already in underwear or nude.
        ton @ hair horny "Couldn't you have waited for me, Miss Chang?" ("soft", "narrow", "base", "L")
        ton @ hair horny "I would have loved to help you undress..." ("base", "narrow", "base", "L")
        gen "No, that's just the girl's regular dress code around my office." ("base", xpos="far_left", ypos="head")
        cho @ cheeks heavy_blush "" ("clench", "narrow", "base", "downR")
        ton @ hair horny "Is that so..." ("soft", "narrow", "raised", "mid")
        ton @ hair horny "*Hmm*... I suppose I should follow suit, then?" ("base", "narrow", "base", "mid")
        cho @ cheeks blush "..." ("horny", "narrow", "base", "R") # embarrassed

    gen "Go right ahead!" ("grin", xpos="far_left", ypos="head")
    ton "I've been dying to get out of this stuffy coat." ("open", "base", "shocked", "down")
    play music "music/scheming-weasel-slower-version-by-kevin-macleod.ogg" fadein 1 if_changed
    ton "" ("base", "base", "base", "down")
    pause .2

    # Tonks removes her coat.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("robe")
    with d3
    pause .8

    ton "There... much better, don't you think?" ("base", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "..." ("base", "narrow", "worried", "downR") #embarrassed
    ton "Miss Chang, could you switch places with me, please?" ("open", "base", "shocked", "L")
    cho @ cheeks heavy_blush "*Ehm*... Y-Yes. Of course..." ("soft", "narrow", "worried", "L")

    # Tonks' sprite moves in front of Cho, both are facing Genie.
    call hide_characters
    hide screen bld1
    with d3
    pause .5

    $ tonks_chibi.zorder = 2 # default is 3
    call cho_chibi("stand", 370, 360, flip=False)
    call ton_chibi("stand", 320, 360, flip=False)
    with d3
    pause .5

    $ cho.zorder = 15 # reset to default.
    $ tonks.zorder = 16 # in front of Cho # Default is 15.
    cho @ cheeks heavy_blush "" ("horny", "narrow", "base", "mid", xpos=345, ypos="base", flip=False)
    ton @ hair horny "..." ("crooked_smile", "narrow", "base", "mid", xpos=215, ypos="base", flip=False)

    ton @ hair horny "Miss Chang, would you be so kind and assist me with my shirt?" ("soft", "base", "shocked", "down")
    cho @ cheeks heavy_blush "Yes, Professor..." ("smile", "narrow", "base", "down")
    pause .2
    cho @ cheeks heavy_blush "" ("base", "narrow", "raised", "down", xpos=315, ypos="base", flip=False, trans=d5) # moves closer to Tonks.
    pause .8
    cho @ cheeks heavy_blush "" ("horny", "narrow", "base", "down")
    pause .2

    # Remove Tonks top.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("top")
    with d3
    pause .5

    ton @ hair horny "" ("horny", "narrow", "base", "mid")
    pause .8

    nar "With some effort, Cho manages to remove her teacher's shirt."
    ton @ hair horny "Thank you, sweetie." ("soft", "narrow", "raised", "downR")
    cho @ cheeks heavy_blush "" ("base", "narrow", "base", "mid")
    ton @ hair horny "*Hmm*..." ("annoyed", "base", "raised", "down")
    ton @ hair horny "I guess my tight trousers are next..." ("base", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "down") # blush
    ton @ hair horny "I'll take it from here..." ("soft", "narrow", "shocked", "downR")
    pause .2

    # Tonks turns around facing Cho.
    call ton_chibi(flip=True)
    #$ tonks.zorder = 15 # Reset to default.
    #$ cho.zorder = 16 # in front of Tonks # Default is 15.
    #cho @ cheeks heavy_blush "" ("base", "narrow", "raised", "L", xpos=345, ypos="base", flip=False)
    ton @ hair horny "Let me show you how it's done. {heart}" ("crooked_smile", "narrow", "base", "down", xpos=280, ypos="base", flip=True, trans=d5)

    cho @ cheeks heavy_blush "..." ("horny", "narrow", "worried", "down") # lip bite
    ton @ cheeks heavy_blush hair horny "With trousers like these, you should start slowly... that's how the headmaster likes it. {heart}" ("horny", "narrow", "base", "mid")

    nar "Tonks carefully tugs at the thin fabric of her leggings, and slowly pulls them past her cheeks..."
    nar "As the fabric bundles up between her fingers, reaching lower and lower past her thighs, she pulls them off in one swift motion."

    # Remove Tonks bottom.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("bottom")
    with hpunch
    pause .5

    ton @ cheeks blush hair horny "" ("horny", "narrow", "raised", "mid")
    pause .8

    gen "Not wearing any underwear, I see..." ("base", xpos="far_left", ypos="head")
    ton @ hair horny "I avoid it when I can..." ("crooked_smile", "narrow", "base", "mid")
    ton @ hair horny "Even while I'm in uniform. {heart}" ("grin", "wink", "raised", "mid") #wink
    ton @ hair horny "" ("base", "narrow", "base", "mid")
    gen "Anything you'd like to say, Miss Chang?" ("base", xpos="far_left", ypos="head")
    gen "It's not every day you get to see such a gorgeous woman strip for you..." ("grin", xpos="far_left", ypos="head")
    gen "(...)" ("base", xpos="far_left", ypos="head")
    pause .5

    # Slap Tonks' ass!
    call slap_her
    cho @ cheeks heavy_blush "" ("open", "wide", "base", "mid")
    ton @ cheeks heavy_blush hair scared "!!!" ("clench", "shocked", "base", "stare") # shocked
    nar "You give Tonks a hard slap on her ass."
    cho @ cheeks heavy_blush "" ("horny", "base", "base", "down")
    ton @ cheeks heavy_blush hair horny "Ouch...{w=0.4} Professor!" ("crooked_smile", "narrow", "annoyed", "mid")
    gen "Right, should've warned you, shouldn't I..." ("base", xpos="far_left", ypos="head")

    menu:
        "-Slap it one more time!-":
            call slap_her
            ton @ cheeks blush hair horny "..." ("clench", "base", "shocked", "ahegao") #pout #blush
            gen "Want another?" ("grin", xpos="far_left", ypos="head")
            ton @ cheeks heavy_blush hair horny "Yes, please. {heart}" ("crooked_smile", "narrow", "base", "mid")

            menu:
                "-Slap it again!-":
                    call slap_her
                    ton @ cheeks heavy_blush hair horny "*Mmm*... Spank me, Sir!" ("horny", "narrow", "angry", "mid")

                    menu:
                        "-Again!-":
                            pass
                    call slap_her
                    ton @ cheeks heavy_blush hair angry "More...{w=0.3} Harder!" ("clench", "base", "angry", "mid")
                    cho @ cheeks heavy_blush "..." ("disgust", "happyCl", "worried", "mid") # blushing #lip bite #looking away

                    menu:
                        "-Slap it hard!-":
                            pass
                    call slap_her
                    ton @ cheeks heavy_blush hair scared "" ("clench", "base", "shocked", "ahegao")
                    pause .5
                    call slap_her
                    pause .3
                    call slap_her
                    pause .3
                    call slap_her
                    cho @ cheeks heavy_blush "" ("horny", "narrow", "worried", "mid")
                    ton @ cheeks heavy_blush hair horny "*Hngh*..." ("upset", "narrow", "base", "ahegao")
                    ton @ cheeks heavy_blush hair horny "Thank you, Professor. {heart}{heart}{heart}" ("crooked_smile", "narrow", "worried", "mid")
                    gen "You're welcome." ("grin", xpos="far_left", ypos="head")
                    cho @ cheeks heavy_blush "..." ("horny", "narrow", "base", "downR")

                "\"Cho, you do the honours!\"":
                    cho @ cheeks heavy_blush "What?! I can't--" ("open", "wide", "base", "mid")
                    pause .2

                    # Tonks turns around.
                    call ton_chibi(flip=False)
                    ton @ cheeks blush hair horny "" ("base", "base", "base", "mid", xpos=215, ypos="base", flip=False, trans=d5)
                    pause .5

                    ton @ cheeks blush hair horny "It's fine, Cho. Just give it a little slap." ("soft", "narrow", "base", "downR")
                    cho @ cheeks heavy_blush "..." ("angry", "base", "raised", "down")
                    call slap_her
                    ton @ cheeks blush hair horny "That's it! Try a little harder..." ("horny", "narrow", "base", "downR")
                    call slap_her
                    ton @ cheeks blush "One more time..." ("soft", "narrow", "shocked", "up")
                    call slap_her
                    ton @ cheeks heavy_blush hair horny "*Hngh*..." ("upset", "narrow", "shocked", "ahegao")
                    pause .2

                    # Tonks turns around.
                    call ton_chibi(flip=True)
                    ton "" ("base", "base", "base", "mid", xpos=280, ypos="base", flip=True, trans=d5)
                    pause .8

                    ton @ cheeks heavy_blush "Thank you, sweetie." ("crooked_smile", "narrow", "base", "L")
                    cho @ cheeks heavy_blush "..." ("quiver", "narrow", "worried", "down")

        "-Stop here...-":
            pass

    gen "Tell me, Cho...{w=0.3} do you like your teacher's body?" ("base", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush hair horny "" ("base", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "Of course I do." ("open", "narrow", "base", "down")
    ton @ cheeks blush hair horny "" ("base", "narrow", "base", "down")
    cho @ cheeks blush "She's very fit and athletic and pretty, just like me." ("crooked_smile", "happyCl", "base", "mid")
    gen "That's not what I meant..." ("base", xpos="far_left", ypos="head")
    gen "Does her body turn you on?" ("grin", xpos="far_left", ypos="head")
    ton @ cheeks blush hair horny "" ("base", "narrow", "annoyed", "mid") # eager look at Cho.
    cho @ cheeks heavy_blush "Sir!" ("clench", "wide", "base", "mid")
    gen "It's a simple question..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "Do I really need to answer?" ("clench", "happyCl", "worried", "mid")
    ton @ cheeks blush hair horny "Please, Miss Chang..." ("open", "narrow", "base", "L")
    ton @ cheeks blush hair horny "I'm quite curious about your thoughts as well. {heart}" ("base", "narrow", "base", "L")
    ton @ cheeks blush hair horny "We'll keep it our little secret, I promise..." ("crooked_smile", "narrow", "annoyed", "down")
    cho @ cheeks heavy_blush "*Hmm*..." ("mad", "narrow", "worried", "down")
    cho @ cheeks heavy_blush "Fine...{w=0.3} I do think you're quite attractive, Professor." ("soft", "narrow", "worried", "downR")
    #gen "Thanks." ("grin", xpos="far_left", ypos="head")
    #cho "" ("annoyed", "narrow", "base", "mid")
    #ton @ hair horny "Very funny, Professor Dumbledore... But I believe she was talking to me." ("open", "narrow", "raised", "mid")
    ton @ cheeks blush hair horny "..." ("base", "narrow", "annoyed", "mid") # sharp look at Genie
    cho @ cheeks heavy_blush "Especially for a teacher." ("clench", "narrow", "raised", "down")
    ton @ hair horny "For a teacher?" ("horny", "narrow", "base", "L")
    cho @ cheeks heavy_blush "I mean--" ("soft", "happyCl", "worried", "mid") #clench #worried
    ton @ hair horny "*Ha-ha*... I'll have to add that to my resume." ("grin", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "" ("base", "narrow", "worried", "down")

    ton @ cheeks blush hair horny "Although, teachers shouldn't be employed for their looks, but for their competence, isn't that right?" ("open", "narrow", "annoyed", "mid")
    gen "What?" ("base", xpos="far_left", ypos="head")
    gen "Oh-- I mean yes...{w=0.3} of course..." ("angry", xpos="far_left", ypos="head")
    play sound "sounds/giggle2_loud.ogg"
    ton @ cheeks blush hair horny "*Giggles*..." ("base", "happyCl", "base", "mid")
    ton @ cheeks blush hair horny "Enough with the small talk -- let's get these clothes off!" ("soft", "base", "annoyed", "mid")

    stop music fadeout 1
    ton @ hair horny "" ("horny", "narrow", "base", "mid")
    pause .1

    # Tonks removes the rest of her clothes.
    play sound "sounds/cloth_sound3.ogg"
    $ tonks.strip("clothes")
    with hpunch
    pause .2

    cho @ cheeks heavy_blush "" ("clench", "narrow", "worried", "mid")
    pause .5

    nar "Within a blink of an eye, Tonks has removed all of her remaining clothing."
    # nar "One minute her clothes were there, and then they were gone! It was like magic!"
    cho @ cheeks heavy_blush "..." ("clench", "narrow", "worried", "downR")
    ton @ hair horny "Get in front of me, Miss Chang." ("open", "narrow", "base", "L")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed
    if cho.is_worn("bra"):
        ton @ hair horny "It's time you show your headmaster your cute little breasts as well." ("soft", "narrow", "base", "mid")
    else:
        ton @ hair horny "Let's show your headmaster these cute little breasts of yours." ("soft", "narrow", "base", "mid")

    cho @ cheeks heavy_blush "They aren't that little..." ("annoyed", "narrow", "worried", "down") # annoyed
    ton @ hair horny "No, you're right, sweetie..." ("soft", "narrow", "base", "down")
    ton @ hair horny "They're just about perfect." ("horny", "narrow", "raised", "down")
    ton @ cheeks blush hair horny "Now stand here, so the headmaster can see your tits." ("crooked_smile", "narrow", "base", "mid")
    cho @ cheeks heavy_blush "..." ("annoyed", "happyCl", "base", "mid")
    pause .2

    # Cho moves in front.
    $ cho.zorder = 16 # in front of Tonks # Default is 15.
    $ tonks.zorder = 15 # reset to default.
    cho @ cheeks heavy_blush "" ("angry", "narrow", "base", "down", xpos=300, ypos="base", trans=d5)
    pause .8

    # Remove Cho's bra.
    if cho.is_worn("bra"):

        ton @ hair horny "Let me help you with that, Miss Chang." ("base", "narrow", "raised", "down")
        pause .2

        # Remove Cho top.
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("bra")
        with d3
        pause .5

        cho @ cheeks heavy_blush "" ("base", "happyCl", "worried", "mid")
        pause .8

        nar "The lust-filled teacher effortlessly removes the bra of her student."

    cho @ cheeks heavy_blush "..." ("crooked_smile", "narrow", "worried", "mid")
    ton @ hair horny "Fucking perfect {heart} aren't they, Professor?..." ("horny", "narrow", "base", "mid")
    ton @ hair horny "Move next to me, Cho. I need you to stand -- right here {heart}{heart}{heart}" ("open", "base", "base", "downR")
    cho @ cheeks heavy_blush "*Ehm*... yes, Professor." ("soft", "narrow", "worried", "L")
    call hide_characters
    hide screen bld1
    with d3
    pause .5

    # Cho turns around, facing Tonks.
    call cho_chibi("stand", 314, 366, flip=True)
    call ton_chibi("stand", 370, 360, flip=False)
    with d3
    pause .5

    cho @ cheeks heavy_blush "" ("base", "narrow", "base", "mid", xpos=280, ypos="base", flip=True)
    ton @ hair horny "..." ("grin", "narrow", "base", "L", xpos=345, ypos="base", flip=False, trans=d5)

    play sound "sounds/giggle2_loud.ogg"
    ton @ hair horny "*Giggles*..." ("grin", "narrow", "shocked", "mid")
    ton @ cheeks blush hair horny "This is so much fun!" ("base", "narrow", "base", "up")

    if cho.is_worn("panties"):
        cho @ cheeks heavy_blush "..." ("horny", "narrow", "worried", "L")
        ton @ hair horny "Let's unveil this magnificent thing, next!" ("crooked_smile", "narrow", "base", "down")

        nar "Tonks eyes up Cho's panties, and before you can blink, she undresses her completely."
        cho @ cheeks heavy_blush "Professor, not so fast--" ("horny", "narrow", "worried", "down")
        pause .2

        # Remove Cho Panties + Everything else.
        play sound "sounds/cloth_sound3.ogg"
        $ cho.strip("clothes")
        with vpunch
        pause .5

        cho @ cheeks heavy_blush "" ("horny", "narrow", "raised", "down")
        pause .8

        cho @ cheeks heavy_blush "Ah!" ("mad", "happyCl", "worried", "mid") # startled?

    else:
        cho @ cheeks heavy_blush "Glad you're enjoying it, Professor..." ("horny", "narrow", "worried", "L")

        #Remove any remaining items (no sound since she might be naked)
        $ cho.strip("clothes")
        with d3
        pause .5

        cho @ cheeks blush "" ("horny", "narrow", "base", "down")
        gen "She's not the only one!" ("grin", xpos="far_left", ypos="head")
        cho @ cheeks blush "" ("horny", "narrow", "base", "mid")
        call ctc


    ton @ cheeks blush hair horny "*Hmm*... I can't decide which teacher has the best view now..." ("horny", "narrow", "base", "down")
    gen "Looking pretty good from where I'm sitting..." ("grin", xpos="far_left", ypos="head")

    play sound "sounds/giggle2_loud.ogg"
    cho @ cheeks blush "" ("horny", "narrow", "base", "mid")
    ton @ cheeks blush hair horny "*Giggles*" ("grin", "base", "base", "mid")

    ton @ cheeks blush hair horny "Well, we still have the best saved for last." ("grin", "narrow", "base", "down")
    ton @ cheeks blush hair horny "Let's give Professor Dumbledore a proper view of what a real athlete can achieve..." ("grin", "base", "base", "L")
    cho @ cheeks blush "*Ehm*..." ("disgust", "narrow", "base", "L")
    ton @ cheeks blush hair horny "Your buns, hun." ("crooked_smile", "narrow", "base", "L")

    stop music fadeout 1.0

    cho @ cheeks blush "Oh... Alright..." ("angry", "narrow", "base", "downR")

    play music "music/(Orchestral) Playful Tension by Shadow16nh.ogg" fadein 1 if_changed # SEX THEME.

    #Cho and Tonks on Desk CG

    show dustfloating as cg_effects zorder 18

    if game.daytime:
        show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg zorder 17
    else:
        show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg zorder 17 at color_temperature(1.0)

    with fade

    ton "There you go, professor..."
    ton "The magnificent ass of a Quidditch player."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_open as cg
    with d3

    cho "Professor!"

    show cho_strip_personal_t3_e3_on_knees cho_mouth_annoyed cho_eyes_open_down as cg
    with d3

    gen "*Heh-Heh*..."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
    with d3

    ton "Someone had to say it."
    ton "I must say, gripping that broom has done wonders for your thighs and butt, Miss Chang."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_annoyed cho_eyes_open_look_at_tonks as cg
    with d3

    cho "...{w=0.4} Thank you, I suppose."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
    with d3

    ton "No, really Miss Chang...{w=0.4} Have a feel of mine, and I'm sure you'll notice the difference."


    show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tits cho_mouth_lip_bite as cg
    with d3

    cho "You--{w=0.2} You want me to..."
    ton "Don't be shy now."

    #Cho grabs Tonks ass
    show cho_strip_personal_t3_e3_on_knees cho_body_grab as cg
    with d3

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_base tonks_eyes_open_down as cg
    with d3

    cho "..."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
    with d3

    ton "So?"

    show cho_strip_personal_t3_e3_on_knees cho_mouth_smirk as cg
    with d3

    cho "It's...{w=0.4} Nice."

    play sound "sounds/giggle2_loud.ogg"
    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile tonks_eyes_open_look_at_cho as cg
    with d3
    ton "*Giggles*... I was asking if you could feel the difference, not for a review, Miss Chang."

    #Base Pose
    show cho_strip_personal_t3_e3_on_knees -cho_body_grab cho_mouth_open cho_eyes_wide_look_at_tonks cho_blush_heavy as cg
    with d3

    cho "Oh, I'm so sorry, Professor!"

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_tits cho_eyes_open_down tonks_mouth_base cho_mouth_base as cg
    with d3

    ton "Don't worry, Miss Chang... Your honesty is greatly appreciated."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
    with d3

    ton "So, what do you say? Quite a fair bit softer than your own, wouldn't you say?"

    show cho_strip_personal_t3_e3_on_knees cho_eyes_closed cho_mouth_open as cg
    with d3

    cho "I...{w=0.4} Suppose...{w=0.4} Maybe just a little bit."
    ton "No need to be modest, Miss Chang... Your grip on that broom is unmatched."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_smirk as cg
    with d3

    cho "..."
    gen "You know..."

    show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down tonks_eyes_open_down cho_mouth_smirk as cg
    with d3

    gen "There's a simple way if you'd like to measure the difference."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_tits as cg
    with d3

    ton "I was thinking the same thing."

    show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_look_at_tonks tonks_eyes_open_look_at_cho tonks_mouth_open as cg
    with d3

    ton "Miss Chang...{w=0.4} If I may?"

    show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks cho_mouth_lip_bite as cg
    with d3

    cho "*Ah*--{w=0.2} Alright..."

    #Tonks grabs Cho's cheeks, spreading them

    show cho_strip_personal_t3_e3_on_knees tonks_body_grab_spread tonks_eyes_open_look_at_tits cho_eyes_closed tonks_mouth_lip_bite cho_mouth_open as cg
    with d3

    cho "*Ah*..."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite as cg
    with d3

    cho "..."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_base as cg
    with d3

    ton "*Mmm*...{w=0.4} As suspected...{w=0.4} A lot firmer than mine."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_base as cg
    with d3

    cho "Oh..."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
    with d3

    ton "That's not a bad thing, Miss Chang... A tight butt has its advantages, not only for Quidditch..."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down as cg
    with d3

    ton "So, what do you think, professor?"

    show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down cho_mouth_smirk as cg
    with d3

    gen "I like both."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_base as cg
    with d3

    ton "I'm talking about her training."
    gen "Oh...{w=0.4} She's done very well."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_open tonks_eyes_open_look_at_tits as cg
    with d3

    ton "Very well indeed..."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down tonks_mouth_base cho_mouth_base cho_eyes_open_down as cg
    with d3

    gen "Is that jealousy I'm hearing in your voice?"

    show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_look_at_tonks cho_mouth_smile as cg
    with d3

    gen "If you're looking for a workout, I'm sure I could sort something out."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_lip_bite as cg
    with d3

    ton "*Mmm*..."
    ton "Perhaps it's time I bring out the old comet..."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_open cho_eyes_open_look_at_tonks as cg
    with d3

    cho "Professor?"

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho tonks_mouth_smile as cg
    with d3

    ton "Yes, sweetie?"

    show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite as cg
    with d3

    cho "You're squeezing my butt still."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_open tonks_eyes_open_look_at_tits as cg
    with d3

    ton "Oh... So I am..."

    #Base pose
    show cho_strip_personal_t3_e3_on_knees -tonks_body_grab_spread tonks_eyes_open_look_at_cho as cg
    with d3

    ton "Sorry, Miss Chang... I got lost appreciating your butt, I forgot what we were doing for a second."

    #Tonks looks at genie
    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down as cg
    with d3

    ton "*Hmm*... It appears I'm not the only one..."

    #Cho looks at genie who has a boner (off screen)

    show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down cho_mouth_annoyed as cg
    with d3

    pause .8

    show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_down cho_mouth_angry as cg
    with d3

    cho "Sir! Not when Tonks-- I mean--"

    show cho_strip_personal_t3_e3_on_knees cho_mouth_base tonks_mouth_smile as cg
    with d3

    ton "No, I think he's got the right idea."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_angry cho_eyes_wide_look_at_tonks as cg
    with d3

    cho "What?!"

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_base cho_eyes_wide_down as cg
    with d3

    ton "Go on, professor... Whip it out."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_open cho_eyes_wide_look_at_tonks as cg
    with d3

    cho "Professor Tonks!"

    show cho_strip_personal_t3_e3_on_knees cho_mouth_annoyed tonks_eyes_open_look_at_cho as cg
    with d3

    ton "Now-now, Miss Chang... This is a necessary part of your training."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_open cho_eyes_open_look_at_tonks as cg
    with d3

    cho "But, professor!"

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile cho_mouth_annoyed as cg
    with d3

    ton "It's inevitable with how your matches have been going recently, that at least a couple of boys would end up whipping it out during the finals."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_open as cg
    with d3

    ton "You wouldn't want to get distracted by such a sight during Quidditch now, would you?"

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_base cho_mouth_lip_bite cho_eyes_open_down as cg
    with d3

    if states.cho.status.dick_seen:
        cho "But I've already seen--{w=0.2} I mean..."
    else:
        cho "..."

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile tonks_eyes_open_down as cg
    with d3

    ton "I'm sure your professor... Or should I say coach... Would agree."
    gen "I'll agree to--{w=0.2} *Ngh*...{w=0.4} anything at this point."

    play sound "sounds/giggle2_loud.ogg"
    ton "*Giggles*"

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down cho_mouth_base as cg
    with d3

    ton "I'll remember that next time we discuss my salary."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho cho_eyes_open_look_at_tonks as cg
    with d3

    ton "So, what do you say Miss Chang?"

    show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite as cg
    with d3

    cho "{size=-4}Alright...{/size}"

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
    with d3

    ton "Marvellous."

    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down tonks_mouth_base cho_eyes_open_down as cg
    with d3

    ton "Please, help yourself professor."
    gen "(Finally!)"

    # TODO: cloth sounds

    #Cho wide eyed looking at dick
    show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile cho_eyes_wide_down cho_mouth_open as cg
    with d3
    pause .8
    #Cho clenched eyes
    show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite cho_eyes_closed_happy as cg
    with d3

    nar "*Fap* *Fap* *Fap*"

    show cho_strip_personal_t3_e3_on_knees tonks_mouth_open as cg
    with d3

    ton "Wow, look at him go!"

    #Tonks looking at Cho
    show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho tonks_mouth_base as cg
    with d3

    ton "...{w=0.4} Miss Chang, I urge you to take advantage of this opportunity."
    ton "Closing your eyes won't be an option during Quidditch."

    show cho_strip_personal_t3_e3_on_knees cho_mouth_annoyed as cg
    with d3

    cho "..." #Eyes still closed

    menu:
        "-Motion Tonks to spank Cho's ass-": #Tonks spanks Cho's ass, Tonks gets wet

            # tonks smile
            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open tonks_eyes_open_down as cg
            with d3

            ton "...?" # Doesn't get it at first
            pause 0.8

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
            with d3

            nar "Tonks nods, grinning mischievously, letting you know she's on-board with your plan."

            play sound "sounds/slap_02.ogg"
            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho cho_handprint cho_eyes_wide_down cho_mouth_open as cg
            with flash

            cho "{heart}*Ah*!{heart}"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_angry as cg
            with d3

            cho "..."
            ton "There you go...{w=0.4} That wasn't so hard was it?"

            #Tonks wet down legs
            show cho_strip_personal_t3_e3_on_knees tonks_wetness cho_eyes_open_look_at_tonks cho_mouth_lip_bite as cg
            with d3

            cho "..."
            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_closed tonks_mouth_base as cg
            with d3

            play sound "sounds/giggle2_loud.ogg"
            ton "*Giggles*"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down cho_eyes_open_down as cg
            with d3

            ton "Looks like that really got him going."
            gen "You're the one to talk."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open as cg
            with d3

            ton "Shush now..."

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho cho_eyes_open_look_at_tonks tonks_mouth_base cho_mouth_base as cg
            with d3

            cho "Professor, what is he talking--"

            call slap_her
            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_down cho_mouth_open as cg

            cho "{heart}*Ah*!{heart}"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed_happy cho_mouth_lip_bite tonks_mouth_smile tonks_eyes_open_look_at_tits as cg
            with d3

            ton "Oh yes, I'm sure a broomstick would slide quite nicely between these cheeks!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down cho_mouth_annoyed as cg
            with d3

            cho "...{w=0.4} Slide?"

            nar "*Fap* *Fap* *Fap*"

            gen "(*Ngh*... This isn't good, If they keep going like this, I'll paint their asses white!)"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down tonks_mouth_base as cg
            with d3

            ton "*Hmm*... Already?"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks cho_mouth_base as cg
            with d3

            cho "Professor?"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho tonks_mouth_smile as cg
            with d3

            ton "I believe coach is almost ready to show his appreciation for your hard work."

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_down cho_mouth_open as cg
            with d3

            cho "Wait, you don't mean--"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho tonks_mouth_open cho_mouth_lip_bite as cg
            with d3

            ton "Oh?{w=0.6} Is that not what we're doing?"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks as cg
            with d3

            ton "My apologies."

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_tits tonks_mouth_smile tonks_body_grab as cg
            with d3

            ton "I was under the impression that seduction was part of your winning strategy..."

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_look_at_tonks cho_mouth_open as cg
            with d3

            cho "How did you--"

            show cho_strip_personal_t3_e3_on_knees -tonks_body_grab tonks_mouth_base tonks_eyes_open_look_at_cho as cg
            with d3

            ton "Sweetie... You're speaking to an expert..."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_base as cg
            with d3

            cho "Professor?"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_closed as cg
            with d3

            play sound "sounds/giggle2_loud.ogg"
            ton "*Giggles*"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho tonks_mouth_smile as cg
            with d3

            ton "You thought that I got to where I am by working hard?"
            ton "Please... When you've got a body like mine, the only thing you need is the knowledge of how to use it..."
            ton "For example, if you're ever looking to get a raise, just show some skin and any man is sure to just nod and agree to anything you say."

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open tonks_eyes_open_down as cg
            with d3

            ton "Observe..."

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down tonks_mouth_smile as cg
            with d3

            ton "So, how about that raise, Professor?"

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open as cg
            with d3

            ton "Professor?"

            gen "Huh?"
            gen "Oh...{w=0.2} *Err*...{w=0.2} Sure!{w=0.4} Whatever you say."

            #Tonks looks at Cho

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base tonks_eyes_open_look_at_cho cho_eyes_open_look_at_tonks as cg
            with d3

            ton "See?"
            ton "Of course, even though I got what I wanted, you should finish what you started, or they'll know something's up..."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite as cg
            with d3

            cho "..."
            ton "So... Do you have what it takes?"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_open as cg
            with d3

            if states.cho.status.blowjob:
                cho "*Ehm*... Haven't I already proved--"
            else:
                cho "But he's my--{w=0.2} And you--{w=0.2} Surely I can't just--"

            call slap_her
            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed_happy as cg

            cho "{heart}*Ah*!{heart}"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks as cg
            with d3

            ton "You can do it."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite as cg
            with d3

            cho "*Ah*...{w=0.4} Okay then..."

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile tonks_eyes_open_down cho_eyes_open_down as cg
            with d3

            ton "Oh, looks like the moment has arrived!"

        "-Multitasking is too hard, keep beating it-": #Tonks spreads Cho's ass, Cho's wet, Cho then spreads Tonks' ass at the same time.

            #Cho opens eyes and looks at genie

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open cho_eyes_open_down as cg
            with d3

            ton "Very good..."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
            with d3

            ton "Now, I think it would be a good idea to give him something to look at as well."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_angry cho_eyes_wide_look_at_tonks as cg
            with d3

            cho "No, wait!"

            #Tonks spreads Cho's ass and she's wet
            show cho_strip_personal_t3_e3_on_knees tonks_body_grab_spread cho_wetness cho_mouth_open cho_eyes_wide_down as cg
            with d3

            pause 1

            gen "Whoa!"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open cho_eyes_wide_look_at_tonks as cg
            with d3

            ton "*Hmm*? What's wrong, sweetie?"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base cho_eyes_wide_down as cg
            with d3

            gen "She's--"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_look_at_tonks cho_mouth_angry as cg
            with d3

            cho "Nothing!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed_happy as cg
            with d3

            cho "I'm fine!"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_base as cg
            with d3

            nar "*Fap* *Fap* *Fap*"
            gen "Very fine indeed!"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_base cho_eyes_open_look_at_tonks as cg
            with d3

            ton "*Mmm*... You almost had me worried for a second..."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_open as cg
            with d3

            cho "*Ehm*... How long do I have to stay like this?"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open cho_mouth_base as cg
            with d3

            ton "Until he finishes, of course."

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_look_at_tonks tonks_mouth_base cho_mouth_angry as cg
            with d3

            cho "Until--{w=0.2} But professor!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks tonks_mouth_open cho_mouth_annoyed as cg
            with d3

            ton "Or is that not what we're doing?"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_closed as cg
            with d3

            ton "I thought that seduction was a big part of your winning strategy..."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base tonks_eyes_open_look_at_tits cho_mouth_open cho_eyes_wide_look_at_tonks as cg
            with d3

            cho "How did you--"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open tonks_eyes_open_look_at_cho cho_eyes_open_look_at_tonks as cg
            with d3

            ton "Please, Miss Chang...{w=0.4} You're talking to an expert..."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base as cg
            with d3

            ton "And as an expert, let me tell you, if you don't fully commit, you won't achieve your goals."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base cho_mouth_lip_bite cho_eyes_open_down as cg
            with d3

            cho "But I--{w=0.2} He can see my--"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open cho_eyes_open_look_at_tonks as cg
            with d3

            ton "Endurance, Miss Chang."
            ton "As a Quidditch player, I'm sure you know the importance of endurance."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base cho_eyes_wide_down cho_mouth_annoyed as cg
            with d3

            cho "That's not the problem!"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open cho_mouth_annoyed cho_eyes_open_look_at_tonks as cg
            with d3

            ton "Very well, Miss Chang..."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_lip_bite cho_mouth_base cho_eyes_open_look_at_tonks as cg
            with d3

            ton "You may help yourself to my buttocks."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_open cho_eyes_wide_look_at_tonks as cg
            with d3

            cho "Your--"
            gen "Yes please!"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_lip_bite cho_eyes_open_look_at_tits as cg
            with d3

            cho "..."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_base tonks_mouth_base as cg
            with d3

            ton "Go on then."

            #Cho spreads Tonks' Ass Tonks wet pussy
            show cho_strip_personal_t3_e3_on_knees cho_body_grab_spread tonks_wetness tonks_mouth_base as cg
            with d3

            pause.5

            gen "Whoa, you're--"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_down tonks_mouth_lip_bite tonks_blush_heavy as cg
            with d3

            ton "Shush!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks cho_mouth_lip_bite as cg
            with d3

            cho "Professor?"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
            with d3

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_closed tonks_mouth_open as cg
            with d3

            ton "*Ahem*...{w=0.4} Why don't you keep your eyes on what Professor Dumbledore is doing, Miss Chang."

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_closed tonks_mouth_base cho_mouth_annoyed as cg
            with d3

            cho "But--"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open as cg
            with d3

            ton "Be a good girl and listen to your teacher."

            #Tonks wet down legs, Closed eyes horny
            #Cho looks at genie, Tonks steals glances at Cho
            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_tits cho_eyes_open_down cho_mouth_lip_bite tonks_mouth_base as cg
            with d3

            pause .8

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_lip_bite as cg
            with d3

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_down as cg
            with d3

            gen "*Ah*..."

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks as cg
            with d3

            cho "Professor..."

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
            with d3

            ton "Huh? I wasn't--{w=0.4} Didn't I just tell you to--"

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_base cho_mouth_open as cg
            with d3

            cho "But Professor, I think he's about to-- *Ehm*..."

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_open tonks_eyes_open_down cho_mouth_lip_bite cho_eyes_open_down as cg
            with d3

            ton "*Huh*?" #looks at genie

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
            with d3

            ton "Oh, I see!"

    $ _temp_facial = False

    menu:
        "-Keep going and finish like this-": #Genie cums on desk

            #Base pose
            show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile as cg
            with d3

            ton "Go on coach, cum for us!"
            ton "Claim your pupil, claim your slut, shake that cock, cum on butt!"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_open cho_eyes_open_look_at_tonks as cg
            with d3

            cho "Professor!"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_closed as cg
            with d3

            play sound "sounds/giggle2_loud.ogg"
            ton "*Giggles*"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
            with d3

            ton "You tell him, Miss Chang!"

            show cho_strip_personal_t3_e3_on_knees cho_mouth_angry as cg
            with d3

            cho "I--"
            ton "Tell him to paint his slutty little Quidditch player in cum!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down tonks_eyes_open_down cho_mouth_lip_bite as cg
            with d3

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed as cg
            with d3

            cho "..."

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tits tonks_eyes_open_look_at_cho as cg
            with d3

            pause .5

            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_down cho_mouth_open as cg
            with d3

            cho "P-- Please, do it, sir!"

            show cho_strip_personal_t3_e3_on_knees tonks_body_idle tonks_eyes_open_look_at_cho cho_eyes_wide_look_at_tonks as cg
            with d3

            pause .5

            play sound "sounds/slap_02.ogg"
            show cho_strip_personal_t3_e3_on_knees cho_handprint cho_eyes_closed_happy cho_mouth_lip_bite as cg
            with flash

            cho "*Ah*!!"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
            with d3

            ton "More conviction!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_look_at_tonks tonks_eyes_open_look_at_tits as cg
            with d3

            cho "Conv--"

            play sound "sounds/slap_02.ogg"
            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed_happy cho_mouth_open as cg
            with flash

            cho "{heart}*Ah*!!{heart}"

            #Tonks spreads cho's ass (cho is wet)
            show cho_strip_personal_t3_e3_on_knees cho_eyes_open_look_at_tonks cho_mouth_lip_bite cho_wetness as cg
            with d3

            pause .5

            show cho_strip_personal_t3_e3_on_knees tonks_body_grab_spread tonks_eyes_open_look_at_cho as cg
            with d3

            ton "Say it!"

            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed tonks_eyes_open_down as cg
            with d3

            pause .8

            show cho_strip_personal_t3_e3_on_knees cho_eyes_closed tonks_eyes_open_down cho_mouth_smirk as cg
            with d3

            pause .5

            show cho_strip_personal_t3_e3_on_knees cho_eyes_wide_down cho_mouth_open as cg
            with d3

            cho "C-cum for me, [name_genie_cho]!" # Deliberate; Tonks will mention Cho's choice of calling him by nickname later

            gen "Aaargh!!"

            #Cho closed eyes
            show cho_strip_personal_t3_e3_on_knees -cho_body_grab_spread cho_eyes_closed_happy as cg
            with d3

            cho "*Eeek*!"

            # Cumblock -- Genie cum flying through the air.
            call cum_block
            show cho_strip_personal_t3_e3_on_knees desk_cum_spurt as cg
            play sound "sounds/slick_02.ogg"

            #fade to black
            pause 0.6

            show screen blkfade
            with d3

            ton "..."
            gen "*Ah*..."
            cho "Did--{w=0.2} Did he finish?"
            ton "*chuckles*"
            ton "Oh, he did finish alright..."
            cho "..."

            #Fade back to CG, cum on side of desk (none on Tonks or Cho)

            show cho_strip_personal_t3_e3_on_knees desk_cum_post cho_eyes_open_down cho_mouth_lip_bite as cg
            hide screen blkfade
            with d5

            pause 1

            show cho_strip_personal_t3_e3_on_knees cho_mouth_open as cg
            with d3

            cho "(He--{w=0.4} He missed...)"

            show cho_strip_personal_t3_e3_on_knees -tonks_body_grab_spread tonks_mouth_base cho_mouth_lip_bite as cg
            with d3

            gen "Fuck, I missed..."

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho cho_eyes_closed cho_mouth_smirk as cg
            with d3

            cho "*Phew*..."

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho tonks_mouth_smile as cg
            with d3

            play sound "sounds/giggle2_loud.ogg"
            ton "*Giggles*"

        "-Give Tonks a sign to get closer-": #Tonks and Cho lay down and genie cums on their faces

            $ _temp_facial = True

            show cho_strip_personal_t3_e3_on_knees tonks_mouth_smile cho_eyes_open_look_at_tonks as cg
            with d3

            ton "*Mmm*... You naughty boy..."

            show cho_strip_personal_t3_e3_on_knees cho_mouth_open as cg
            with d3

            cho "Professor?"

            show cho_strip_personal_t3_e3_on_knees tonks_eyes_open_look_at_cho as cg
            with d3

            ton "Follow my lead, Miss Chang."

            show screen blkfade
            with d3

            play sound "sounds/08_hop_on_desk.ogg"
            pause .8
            show cho_strip_personal_t3_e3_cho_staring tonks_body cho_eyes_wide_look_at_tits cho_mouth_open tonks_eyes_open_mid tonks_mouth_smile as cg
            hide screen blkfade
            with d5


            cho "Professor!"

            show cho_strip_personal_t3_e3_cho_staring cho_eyes_wide_down as cg
            with d3

            ton "Hurry up Miss Chang, don't leave your coach hanging."

            show cho_strip_personal_t3_e3_cho_staring cho_mouth_lip_bite as cg
            with d3

            ton "Lay down next to me, just like this."
            show cho_strip_personal_t3_e3_cho_staring cho_eyes_wide_look_at_tits as cg
            with d3

            cho "..."

            show screen blkfade
            with d3

            play sound "sounds/08_hop_on_desk.ogg"
            pause .8
            show cho_strip_personal_t3_e3_lying as cg
            hide screen blkfade
            with d5

            cho "Like this?"

            show cho_strip_personal_t3_e3_lying cho_mouth_base tonks_mouth_open as cg
            with d3

            ton "Yes, Very good Miss Chang..."

            show cho_strip_personal_t3_e3_lying cho_eyes_open_down cho_mouth_open tonks_mouth_base as cg
            with d3

            cho "But, why with our hands out?"

            show cho_strip_personal_t3_e3_lying cho_eyes_open_look_at_tonks tonks_mouth_smile cho_mouth_base as cg
            with d3

            ton "Oh... I think you already know the answer to that question..."
            nar "*Fap* *Fap* *Fap*"

            #Cho angry mouth
            show cho_strip_personal_t3_e3_lying cho_eyes_open_down tonks_mouth_smile cho_mouth_angry as cg
            with d3

            pause .5

            play sound "sounds/giggle2_loud.ogg"
            ton "*Giggles*"

            show cho_strip_personal_t3_e3_lying tonks_mouth_open as cg
            with d3

            ton "You're not going to chicken out on me now, are you, Miss Chang?"

            show cho_strip_personal_t3_e3_lying tonks_mouth_base cho_mouth_open as cg
            with d3

            cho "I--"

            #Cho looks at genie
            show cho_strip_personal_t3_e3_lying cho_mouth_base cho_eyes_open_mid as cg
            with d3

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_lying cho_eyes_closed cho_mouth_open as cg
            with d3

            cho "I won't."

            show cho_strip_personal_t3_e3_lying cho_mouth_base tonks_mouth_smile as cg
            with d3

            ton "Good..."

            show cho_strip_personal_t3_e3_lying cho_eyes_open_down tonks_mouth_open as cg
            with d3

            ton "Then give your Coach your biggest smile and repeat after me..."

            show cho_strip_personal_t3_e3_lying cho_eyes_open_look_at_tonks tonks_mouth_base cho_mouth_angry as cg
            with d3

            cho "You want me to--"

            show cho_strip_personal_t3_e3_lying tonks_mouth_smile cho_mouth_angry as cg
            with d3

            ton "Smile, Miss Chang..."
            cho "...{w=0.8}{nw}"

            #Cho smiles
            show cho_strip_personal_t3_e3_lying cho_mouth_smile as cg
            with d3

            pause .8

            ton "There you go... And such a pretty smile as well..."
            cho "Thank you..."

            nar "*Fap* *Fap* *Fap*"
            gen "*Ah*... Ladies..."

            #Tonks and Cho looks at genie
            show cho_strip_personal_t3_e3_lying tonks_eyes_open_mid cho_eyes_open_mid as cg
            with d3

            ton "Oh, of course, sir..."
            ton "Now, Miss Chang, keep your eyes on your coach and repeat after me..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_open cho_mouth_smile as cg
            with d3

            ton "\"Thank you coach, for being such a good mentor\"..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_base cho_mouth_open as cg
            with d3

            cho "Thank you coach... For being such a good mentor..."

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_lying tonks_mouth_open cho_mouth_smile as cg
            with d3

            ton "\"I'll always be in your debt after everything that you've done for me\"..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_base cho_mouth_open as cg
            with d3

            cho "I'll always be in your debt... After everything that you've done for me..."

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_lying tonks_mouth_open cho_mouth_smile as cg
            with d3

            ton "\"But I hope to be able to repay you some day\"..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_base cho_mouth_open as cg
            with d3

            ton "But I hope to be able to repay you some day..."

            nar "*Fap* *Fap* *Fap*"

            show cho_strip_personal_t3_e3_lying tonks_mouth_open cho_mouth_smile as cg
            with d3

            ton "\"With\"..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_base cho_mouth_open as cg
            with d3

            cho "With..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_open cho_mouth_smile as cg
            with d3

            ton "\"My\"..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_base cho_mouth_open as cg
            with d3

            cho "My..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_open cho_mouth_smile as cg
            with d3

            ton "\"Body\"..."

            show cho_strip_personal_t3_e3_lying tonks_mouth_smile cho_mouth_open as cg
            with d3

            cho "Body--"

            show cho_strip_personal_t3_e3_lying cho_mouth_smile as cg
            with d3

            pause .5

            #Cho looks at Tonks, angry mouth
            show cho_strip_personal_t3_e3_lying cho_eyes_open_look_at_tonks cho_mouth_angry as cg
            with d3

            cho "Wait, what?!"

            gen "*Aaargh*!!"

            show cho_strip_personal_t3_e3_lying tonks_mouth_tongue_out cho_mouth_open as cg
            with d3

            ton "Open wide, Cho!"

            #Tonks tongue out
            #Cho clenched eyes
            show cho_strip_personal_t3_e3_lying cho_eyes_open_mid cho_mouth_angry as cg
            with d3

            cho "Wait!"

            #Genie cums on their faces, and in tonks mouth.

            call cum_block
            show cho_strip_personal_t3_e3_lying cum_tongue cho_mouth_open cho_eyes_closed_happy as cg
            with flash

            cho "*Aaaah*!"

            gen "Yeeeees!! Take that, you sluts!"
            call cum_block

            show cho_strip_personal_t3_e3_lying cum_face tonks_eyes_closed as cg
            with flash
            show cho_strip_personal_t3_e3_lying cum_tits as cg
            with flash
            show cho_strip_personal_t3_e3_lying tonks_eyes_open_mid cum_hands as cg
            with flash


            cho "It's--{w=0.4} I can feel it on my hands!"
            cho "It's... So warm..."

            #Cho looks at tonks
            show cho_strip_personal_t3_e3_lying cho_eyes_open_look_at_tonks as cg
            cho "Professor--"

            #Tonks swallows + sound
            play sound "sounds/gulp.ogg"
            show cho_strip_personal_t3_e3_lying tonks_eyes_closed tonks_mouth_smile -cum_tongue as cg
            with d3

            ton "*Mmm*... Tasty..."
            cho "Whoa..."

            show cho_strip_personal_t3_e3_lying tonks_eyes_open_look_at_cho as cg
            with d3
            play sound "sounds/giggle2_loud.ogg"
            ton "*Giggles*"

            cho "You--{w=0.2} His--"
            ton "*Mmm*... I hope you're not ticklish, Miss Chang..."
            cho "What do you--"

            #fade to black
            play sound "sounds/08_hop_on_desk.ogg"
            show screen blkfade
            with d3

            cho "Oooh!!"
            ton "*slurp* *lick* *slurp*"
            cho "Professor!"

            play sound "sounds/giggle2_loud.ogg"
            ton "*giggles*..."

            $ states.cho.status.cumshot = True

    stop music fadeout 1.0
    show screen blkfade
    with d5
    hide cg
    hide cg_effects

    cho @ cheeks blush "" ("soft", "narrow", "base", "downR")
    ton @ cheeks blush "" ("grin", "base", "base", "L")

    hide screen blkfade
    with d5
    #Hide CG
    ## Transformation Section ##


    ton @ cheeks blush "Great job Miss Chang... I'm sure no man will be able to resist you now...{nw}" ("grin", "narrow", "base", "L")
    ton @ cheeks blush "Great job Miss Chang... I'm sure no man will be able to resist you now...{fast} Wouldn't you agree, professor?" ("grin", "narrow", "base", "mid")
    gen "What? Oh yes, sure! Nice job!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks blush "Thanks, [name_genie_cho]..." ("base", "narrow", "base", "down")

    if name_genie_cho in ("Sir", "Professor"): #Acceptable names that she should be using
        ton @ cheeks blush hair neutral "If you ever have any questions about men, you know where my door is..." ("base", "narrow", "base", "L")
        gen "Got it." ("base", xpos="far_left", ypos="head")
        ton @ cheeks blush "I was referring to Miss Chang." ("soft", "narrow", "base", "mid")
        gen "Oh... Yeah, me too." ("base", xpos="far_left", ypos="head")
    elif name_genie_cho == "Dumbledore":
        ton @ cheeks blush "Using first names already, I see..." ("soft", "base", "raised", "L")
        cho @ cheeks heavy_blush "I mean, Sir!" ("angry", "base", "base", "stare")
        ton @ cheeks blush "Don't worry Miss Chang, if that's what he would like you to call him, then I won't tell anyone." ("base", "wink", "base", "L")
        ton @ cheeks blush "" ("base", "base", "base", "L")
        cho @ cheeks heavy_blush "*Ehm*... Thank you, Professor." ("disgust", "narrow", "base", "down")
    elif name_genie_cho == "Coach":
        ton @ cheeks blush "So you do call him coach!" ("grin", "narrow", "shocked", "L")
        cho @ cheeks heavy_blush "Oh, *Ehm*... Well..." ("angry", "narrow", "base", "L")
        ton @ cheeks blush "Well, seeing that he's helping you, it's only appropriate." ("base", "narrow", "base", "L")
        gen "That's what I said." ("grin", xpos="far_left", ypos="head")
        cho @ cheeks heavy_blush "..." ("base", "narrow", "base", "down")
    else:
        gen "*Cough*..." ("base", xpos="far_left", ypos="head")
        cho @ cheeks blush "I mean--{w=0.2} Thank you, Sir..." ("angry", "base", "base", "mid")
        ton @ cheeks blush "*chuckles* So, this is what he has you call him... Well, nothing wrong with that..." ("soft", "base", "base", "mid")
        cho @ cheeks heavy_blush "..." ("base", "narrow", "base", "down")

    play music "music/fuzzball-parade-by-kevin-macleod.ogg" fadein 1 if_changed

    if _temp_facial:
        cho @ cheeks blush "*Ehm*...{w=0.4} Professor..." ("soft", "narrow", "base", "L")
        ton @ cheeks blush "Yes, Miss Chang?" ("base", "narrow", "raised", "L")
        cho @ cheeks heavy_blush "What did you mean when you said...{w=0.4} Repay him with my body?" ("open", "narrow", "base", "L")
        ton @ cheeks blush "*Hmm*?" ("base", "base", "raised", "mid")
        ton @ cheeks blush "You're selling favours to Professor Dumbledore, are you not?" ("base", "narrow", "base", "L")
        cho @ cheeks heavy_blush "I--{w=0.2} Yes, but that's not--{w=0.2} I mean...{w=0.2} They're meant to help me with Quidditch, I swear!" ("mad", "narrow", "base", "L")
    else:
        ton @ cheeks blush "*Mmm*... Your coach is very lucky to have the opportunity to buy favours from you." ("base", "base", "base", "mid")
        cho @ cheeks heavy_blush "He's--{w=0.2} They're meant to help me with Quidditch, I swear!" ("mad", "narrow", "base", "L")

    play sound "sounds/giggle2_loud.ogg"
    ton @ cheeks blush "*giggles*" ("crooked_smile", "closed", "base", "mid")

    ton @ cheeks blush "Your reasons for selling favours does not concern me, Miss Chang..." ("base", "narrow", "base", "L")
    cho @ cheeks blush "Oh..." ("disgust", "narrow", "base", "down")
    ton @ cheeks blush "As long as both ends of the bargain is met at a satisfactory level." ("soft", "narrow", "base", "mid")
    ton @ cheeks blush "They are, I presume?" ("normal", "narrow", "raised", "L")
    cho @ cheeks blush "Yes..." ("angry", "narrow", "base", "down")
    gen "I mean..." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush "Then that is everything I need to know." ("grin", "closed", "base", "mid")
    ton @ cheeks blush "Now... If that's everything... I think I'll better be off." ("soft", "base", "base", "R")
    cho @ cheeks blush "Oh... Okay then!" ("angry", "narrow", "base", "L")
    gen "*Ahem*... Miss Chang." ("base", xpos="far_left", ypos="head")
    cho @ cheeks blush "Yes, professor?" ("angry", "base", "base", "mid")
    gen "I think this would be the perfect time to ask Professor Tonks your question." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "W-what...{w=0.4} Oh, yes!" ("soft", "base", "raised", "mid")
    ton @ hair horny "*Hmm*?" ("base", "base", "raised", "L")
    cho @ cheeks blush "Professor Dumbledore told me about how you helped me during the Slytherin game." ("open", "base", "base", "L")
    ton @ hair neutral "What? You told her I'm a Metamorphmagi?" ("mad", "wide", "shocked", "mid")
    cho @ cheeks blush "You are?!?" ("open", "wide", "raised", "L")
    cho @ cheeks heavy_blush "That's so cool!" ("grin", "happyCl", "base", "mid")
    ton @ cheeks heavy_blush hair horny "Did I just spoil the surprise myself?{w=0.5} Whoopsie!" ("mad", "narrow", "worried", "downR")
    gen "Well... I didn't exactly tell her that much." ("base", xpos="far_left", ypos="head")
    ton @ cheeks blush hair horny "Well, what's done is done..." ("upset", "narrow", "worried", "downR")

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed

    gen "Show the girl your \"meta thing\" already!" ("grin", xpos="far_left", ypos="head")
    ton "My \"metamorphmagi\" ability." ("soft", "narrow", "base", "mid")
    cho @ cheeks blush "So, is this what you showed us in class before, professor?" ("crooked_smile", "base", "base", "mid")
    cho @ cheeks blush "You were changing your nose into that of a pig, and then a duck, and then--" ("silly", "happyCl", "base", "mid")
    ton "Yes... Well, that's usually about as much as I show people." ("crooked_smile", "narrow", "raised", "L")
    ton "Most aren't aware of what else I can do. It's far more beneficial to me if people are unaware..." ("grin", "narrow", "shocked", "mid")
    ton "You see, I can do far more than just change my nose, or the colour of my hair..." ("soft", "narrow", "raised", "L")
    cho @ cheeks blush "Wicked!... What else can you do?" ("grin", "base", "base", "L")
    gen "How about a busty, stuck-up Gryffindor slut!" ("grin", xpos="far_left", ypos="head")
    ton "Gladly." ("grin", "narrow", "base", "mid")
    stop music
    pause .8

    # Transforms into Hermione
    play sound "sounds/magic4.ogg"
    hide tonks_main
    $ hermione.strip("clothes")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ hermione_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("hide")
    call her_chibi("stand", 370, 360, flip=False)
    her "" ("crooked_smile", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=morph)
    pause .2

    cho @ cheeks heavy_blush "" ("open", "wide", "raised", "L")
    call ctc

    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 if_changed
    cho @ cheeks heavy_blush "{b}Holy shit!{/b}" ("open", "wide", "raised", "L")
    gen "Watch your language, girl..." ("base", xpos="far_left", ypos="head")
    her "" ("soft", "narrow", "angry", "L")
    ton "Yes. Watch your foul mouth, Chang!"
    cho @ cheeks heavy_blush "I-I'm sorry..." ("clench", "happyCl", "worried", "mid")
    gen "I'm just kidding... Swear as much as you want -- It's not going to bring up the age-ratings..." ("base", xpos="far_left", ypos="head")
    her "" ("annoyed", "narrow", "base", "down")
    ton "*Hmm*..."
    her "" ("soft", "narrow", "annoyed", "down")
    ton "I forgot Miss Granger is a bit heavier in the bosom area than I'm used to..."
    her "" ("grin", "narrow", "angry", "L")
    ton "What do you think, Miss Chang... Do they look that much larger than my own?"
    cho @ cheeks heavy_blush "I..." ("clench", "narrow", "worried", "down")
    cho @ cheeks heavy_blush "I'm sorry, this is so weird!" ("open", "happyCl", "worried", "mid")
    her "" ("grin", "narrow", "base", "down")
    ton "*Hmm*? I thought you'd like them..."
    her "" ("crooked_smile", "narrow", "angry", "L")
    ton "I've heard rumours that you're quite fond of these tits, Miss Chang."
    cho @ cheeks heavy_blush "Sorry! It's not that... It's just... you look exactly like her!" ("disgust", "narrow", "worried", "down")
    cho @ cheeks heavy_blush "You even sound like her!" ("soft", "narrow", "worried", "L")

    $ hermione.get_equipped("hair").set_color([[255, 87, 171, 255], [255, 210, 227, 255], [230, 141, 32, 255]])
    # Original: [[255, 105, 180, 255], [251, 205, 222, 255], [230, 141, 32, 255]]
    # Brown: [[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]]
    her @ cheeks blush "" ("crooked_smile", "happyCl", "base", "mid")
    play sound "sounds/giggle2_loud.ogg"
    ton "*giggles*..."

    $ hermione.get_equipped("hair").set_color([[152, 89, 48, 255], [195, 137, 89, 255], [230, 141, 32, 255]])
    her "" ("base", "narrow", "base", "R")
    ton "Naturally... That's the intended effect."
    cho @ cheeks heavy_blush "If I didn't know any better, I'd think you were her!" ("horny", "narrow", "raised", "down")
    her "" ("crooked_smile", "closed", "angry", "mid")
    ton "*Mhmm*... Last time I looked like this in front of you, you couldn't tell either."
    cho @ cheeks heavy_blush "What?! When was that?" ("soft", "base", "worried", "L")
    gen "Right after the last game, if I recall correctly." ("base", xpos="far_left", ypos="head")
    her "" ("base", "narrow", "base", "mid")
    ton "Oh, that wasn't the only time, Professor."
    gen "It wasn't?" ("base", xpos="far_left", ypos="head")
    her "" ("grin", "narrow", "base", "mid")
    ton "I sometimes stroll around the school grounds, disguised as one of the girls... Wearing nothing but a school robe..."

    if states.her.status.public_stripping:
        her "" ("crooked_smile", "narrow", "base", "down")
        ton "And If you ever had a boy say he got some tits flashed at him by Miss Granger... Then it was most likely me."
        cho @ cheeks blush "That's awesome!" ("grin", "base", "base", "L")
        gen "Well, I did tell Hermione to do it herself before." ("base", xpos="far_left", ypos="head")
        her @ cheeks blush "" ("open", "wide", "base", "stare")
        ton "Seriously? I had no idea!"
        cho @ cheeks blush "Me neither!" ("soft", "wide", "raised", "mid")
        her "" ("base", "narrow", "base", "down")
        ton "I guess that's one less thing to worry about while I do it..."

    cho @ cheeks blush "I hope you didn't do that kind of stuff while you looked like me, Professor!" ("open", "narrow", "angry", "L")
    her "" ("annoyed", "base", "base", "R")
    ton "*Ehm*..."
    cho @ cheeks blush "If I find out you've shown some boys my breasts, then--" ("open", "closed", "angry", "mid")
    her @ cheeks blush "" ("smile", "happyCl", "worried", "mid")
    ton "Of course not, sweetie."
    cho @ cheeks blush "..." ("annoyed", "narrow", "angry", "L")
    her @ cheeks blush "" ("grin", "base", "base", "R") # small text
    ton "It was your ass that I showed them..."
    cho @ cheeks heavy_blush "W-What?!" ("clench", "wide", "angry", "L")
    gen "*He-he-he-he*!" ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "" ("clench", "base", "angry", "L")
    her "" ("soft", "closed", "base", "mid")
    ton "It's not like you haven't done that yourself already..."
    her "" ("base", "narrow", "base", "L")
    ton "In front of the entire school, no less..."
    cho @ cheeks heavy_blush "..." ("annoyed", "narrow", "angry", "L") # blush
    her "" ("open", "closed", "base", "mid")
    ton "Well, that's enough fun for today."

    # Tonks transforms back.
    play sound "sounds/magic4.ogg"
    hide hermione_main
    call her_chibi("hide")
    $ cho_chibi.zorder = 3 # Reset to default.
    $ tonks_chibi.zorder = 2 # behind Cho. Default is 3.
    call ton_chibi("stand", 370, 360, flip=False)
    ton @ hair neutral "" ("base", "narrow", "base", "mid", xpos=345, ypos="base", flip=False, trans=morph)
    pause .2

    cho @ cheeks heavy_blush "" ("clench", "base", "raised", "down")
    call ctc

    ton @ hair horny "Let's do this again some other time, shall we." ("horny", "narrow", "raised", "mid")
    gen "Gladly." ("grin", xpos="far_left", ypos="head")
    ton @ cheeks heavy_blush hair horny "And, Miss Chang... if you ever want to have some quiet time with Miss Granger... my office door is always open." ("grin", "narrow", "base", "L")
    cho @ cheeks heavy_blush "I-- *Ehm*..." ("soft", "narrow", "worried", "downR") # super embarrassed
    gen "Maybe you could wait with that until Quidditch is over." ("base", xpos="far_left", ypos="head")
    gen "She has to stay focused, you know..." ("base", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "..." ("disgust", "narrow", "worried", "down")
    ton @ hair horny "*Sigh*... Alright..." ("open", "closed", "shocked", "mid")

    # Fade to black.
    call hide_characters
    hide screen bld1
    show screen blkfade
    with d5

    # The girls get dressed and wait at the door.
    $ cho.wear("all")
    $ tonks.wear("all")
    $ hermione.wear("all")

    # Reset zorder.
    $ cho.zorder = 15 # reset to default.
    $ tonks.zorder = 15 # reset to default.
    $ hermione.zorder = 15 # reset to default.
    $ cho_chibi.zorder = 3 # reset to default.
    $ tonks_chibi.zorder = 3 # reset to default.
    $ hermione_chibi.zorder = 3 # reset to default.
    hide screen cho_cloth_pile

    call cho_chibi("stand", 690, "base", flip=False)
    call ton_chibi("stand", "door", "base", flip=False)

    play sound "sounds/08_hop_on_desk.ogg"
    pause 2

    stop music fadeout 1
    hide screen blkfade
    with d5
    pause .5

    gen "And Tonks... Next time we do this, wear the clothes I usually ask you to wear around my office." ("grin", xpos="far_left", ypos="head")
    ton @ hair horny "With pleasure." ("base", "narrow", "base", "mid", ypos="head", flip=False)

    if game.daytime:
        ton @ hair horny "I'll escort you back to classes, Miss Chang." ("open", "narrow", "base", "L")
        ton @ hair horny "Have a good day, Professor." ("base", "narrow", "base", "mid")
    else:
        ton @ hair horny "I'll escort you back to your dormitories, Miss Chang." ("open", "narrow", "base", "L")
        ton @ hair horny "Have a good night, Professor." ("base", "narrow", "base", "mid")

    gen "Until next time." ("grin", xpos="far_left", ypos="head")
    cho @ cheeks heavy_blush "..." ("upset", "happyCl", "worried", "mid", ypos="head", flip=False)
    call bld("hide")
    pause .1

    # They both leave.
    call cho_chibi(flip=True)
    pause .3
    call ton_chibi(flip=True)
    with d3
    pause .2

    play sound "sounds/door.ogg"
    hide screen cho_chibi
    hide screen tonks_chibi
    with d3
    pause .5


    # Reset clothing.
    #$ cho.equip(cho_outfit_last)
    $ tonks.equip(ton_outfit_last)
    $ hermione.equip(her_outfit_last)

    $ states.ton.busy = True
    $ states.cho.status.dick_seen = True
    $ states.cho.ev.inspect_her_body.T3_E3_complete = True

    # End event.
    jump end_cho_strip_event

label cc_pf_strip_T3_repeat:

    call cc_pf_strip
    
    gen "I'm in the mood for another strip-show, [name_cho_genie]." ("base", xpos="far_left", ypos="head")
    cho "Of course you are, [name_genie_cho]." ("base", "narrow", "raised", "mid")
    cho "Who's going to watch me this time?" ("soft", "narrow", "base", "mid")
    gen "*Hmm*... how about--" ("base", xpos="far_left", ypos="head")

    menu:
        #"\"Miss Granger\"":
        #    jump cc_pf_strip_T3_hermione

        "\"Miss Tonks\"":
            cho "Alright then..." ("grin", "narrow", "base", "mid")
            jump cc_pf_strip_T3_tonks
