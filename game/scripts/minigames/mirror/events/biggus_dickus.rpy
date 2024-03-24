
label biggus_dickus:

    # Setup
    $ hermione.equip(her_outfit_default)
    $ game.daytime = False
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    play music "music/Music for Manatees.ogg" fadein 1 if_changed
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Biggus Dickus{/color}{/size}"

    hide screen blkfade
    with d5

    call her_walk(action="enter", xpos="desk", ypos="base")

    her "Professor, I need a favour..." ("soft", "closed", "base", "down", xpos="mid", ypos="base", trans=dissolve)
    her "I understand it's supposed to be the other way around, but I do think with everything that I've done lately...." ("open", "base", "base", "mid")


    her "..." ("normal", "squint", "base", "mid")
    her "Professor?" ("clench", "narrow", "base", "mid")
    her "Are you even listening?" ("angry", "base", "base", "mid")

    play sound "sounds/card.ogg"
    pause .8
    gen "{size=-4}Hold on... How is Maslab's card a thirteen when I'm only a twelve!?{/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=-4}He's not even in this universe!{/size}" ("base", xpos="far_left", ypos="head")
    gen "{size=-4}Shit... Is he in this universe!? I should look into that...{/size}" ("base", xpos="far_left", ypos="head")
    her "Professor, could you please pay attention?" ("disgust", "narrow", "base", "mid")
    gen "Miss Granger? When did you get here?" ("base", xpos="far_left", ypos="head")
    her "Finally..." ("disgust", "closed", "base", "mid")
    her "I need to ask you a favour." ("open", "squint", "base", "mid")
    gen "Oh... Is it that time already? Very well." ("base", xpos="far_left", ypos="head")
    gen "I suppose I can spare Twenty five points if you flash me." ("base", xpos="far_left", ypos="head")
    her "That isn't what I meant." ("angry", "narrow", "base", "R")
    her "I'm not here to do you a favour, I need you to do me one." ("angry", "narrow", "base", "mid")
    her @ cheeks blush "I mean. I would like you to do me one, that is..." ("angry", "narrow", "base", "mid")
    gen "Ah...{w=0.4} Some quid pro quo eh?" ("base", xpos="far_left", ypos="head")
    gen "Very well... Let it never be said that I don't reciprocate a girl going down on me!" ("base", xpos="far_left", ypos="head")
    her "Professor! I just need you to buy me something!" ("clench", "squint", "base", "mid")
    gen "Oh...{w=0.4} Well, that's much less exciting." ("base", xpos="far_left", ypos="head")
    gen "Alright, you want some lollipops? Maybe some of that fairy chocolate?" ("base", xpos="far_left", ypos="head")
    gen "Though I don't know what I've done to annoy you this time." ("base", xpos="far_left", ypos="head")
    her "No professor...{w=0.4} I'm after something a bit more...{w=0.4} Adult." ("angry", "closed", "base", "down")
    gen "Very well...{w=0.4} Butterbeer then? Or are we being daring enough to try some wine for once?" ("base", xpos="far_left", ypos="head")


    her "No, Professor...{w=0.4} I would like you to buy..." ("open", "squint", "base", "mid")
    her "Three thestral strap-ons, please." ("soft", "squint", "base", "mid")
    gen "Is that all?{w=0.4} A little boring, but whatever you need, I suppose." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What? I--{w=0.4} Sir, I'm worried you didn't quite hear me." ("clench", "base", "base", "mid")
    her @ cheeks blush "I'm asking you to acquire three strap-ons...{w=0.4} Modelled after Thestrals." ("angry", "squint", "base", "mid")
    her @ cheeks blush "For me...{w=0.4} Your student." ("angry", "narrow", "base", "mid")
    gen "I heard you the first time, girl. I may be old, but I'm not deaf." ("base", xpos="far_left", ypos="head")
    gen "Do you need them immediately?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I-- yes.... Fastest delivery possible, please." ("angry", "closed", "base", "mid")
    her @ cheeks blush "If you don't mind, that is..." ("open", "squint", "base", "mid")
    gen "Certainly not, I'll put in the order tonight." ("base", xpos="far_left", ypos="head")
    gen "Can't very well have one of my students going without her study materials." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Thank you sir." ("soft", "squint", "base", "R")
    gen "Don't mention it. They should be here sometime tomorrow." ("base", xpos="far_left", ypos="head")
    gen "I assume you don't need them for one of your morning classes?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "No sir. I certainly won't be using these during my morning classes." ("angry", "narrow", "base", "R")
    gen "Very good. Is that all, then?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I...{w=0.4} I mean...{w=0.4} Could you also buy me some of those cute plush owls?" ("base", "narrow", "base", "down")


    her @ cheeks blush "I know I'm asking a lot..." ("angry", "closed", "base", "mid")
    gen "Some owl plushies, and three strap-ons." ("base", xpos="far_left", ypos="head")
    gen "Got it all written down, here." ("base", xpos="far_left", ypos="head")
    gen "If that is all, Miss Granger, then I suggest you head to your dorms." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Yes sir...{w=0.4} Thank you again." ("grin", "squint", "base", "R")
    her @ cheeks blush "Good night." ("base", "base", "base", "mid")
    gen "Good night, girl. Pleasant dreams." ("base", xpos="far_left", ypos="head")

    call her_walk("door")
    her @ cheeks blush "" ("normal", "squint", "base", "R", xpos="base", ypos="base", flip=True)
    call ctc

    gen "Anything else Miss Granger?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh... No, that's all... Bye then." ("angry", "base", "base", "L")

    call her_walk(action="leave")

    gen "Well... Now that THAT's over with.{#LINT_IGNORE}" ("base", xpos="far_left", ypos="head")
    play sound "sounds/card.ogg"
    pause .8
    gen "What's this now, a sixteen?!" ("angry", xpos="far_left", ypos="head")
    gen "This game is a scam!" ("base", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "She wants me to buy what!?" ("angry", xpos="far_left", ypos="head")

    show screen blkfade
    with d3

    centered "{size=+7}{color=#cbcbcb}One hefty purchase and a day later...{/color}{/size}"

    hide screen blkfade
    with d3


    call her_walk(action="enter", xpos="desk", ypos="base")

    her "Good evening, Professor." ("base", "base", "base", "mid", xpos="mid", ypos="base", flip=False, trans=dissolve)
    gen "Miss Granger...{w=0.4} I assume you are here for your gifts?" ("base", xpos="far_left", ypos="head")
    her "Yes Professor." ("grin", "base", "base", "mid")
    her "I mean, if you've acquired them already." ("open", "squint", "base", "mid")
    gen "Before I say anything else, I think I need to make some things clear." ("base", xpos="far_left", ypos="head")
    gen "I understand that our current...{w=0.4} Arrangement, might have led you to believe that you can rely on me for certain things." ("base", xpos="far_left", ypos="head")
    gen "I feel I need to remind you however that I am still your Headmaster." ("base", xpos="far_left", ypos="head")
    gen "There are some limits to what I am willing to do for you." ("base", xpos="far_left", ypos="head")
    gen "I have indeed acquired what you asked for, but against my better judgement." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I understand Professor." ("angry", "narrow", "base", "down")
    her @ cheeks blush "I would never have asked you to buy them for me if I thought I could get them myself!" ("angry", "squint", "base", "mid")
    her @ cheeks blush "I assure you, I won't tell anyone where I got them from!" ("open", "squint", "base", "mid")
    gen "Very well." ("base", xpos="far_left", ypos="head")
    gen "Now that things have been made clear..." ("base", xpos="far_left", ypos="head")
    gen "Why the hell did you ask me to buy you three fluffy owl plushies!?" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "The...{w=0.4} Owl plushies, sir?" ("clench", "squint", "base", "mid")
    her @ cheeks blush "That's what you have an issue with?" ("disgust", "squint", "base", "mid")
    gen "Yes, I thought you had gotten past liking such silly things." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "But...{w=0.4} What about the thestral strap-ons?" ("angry", "squint", "worried", "mid")
    her @ cheeks blush "You do remember me asking you for those, right?" ("disgust", "narrow", "worried", "mid")
    gen "Yes-yes, don't worry...{w=0.4} I got you your huge purple cocks." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "So...{w=0.4} just to be clear." ("open", "closed", "worried", "mid")
    her @ cheeks blush "You're not upset with the strap-ons...{w=0.4} But you are upset about the owls?" ("angry", "narrow", "base", "mid")
    gen "That is the situation...{w=0.4} Well done Miss Granger." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "{size=+5}WHY!?{/size}" ("angry", "happyCl", "annoyed", "mid")
    gen "Your hormones are obviously going wild." ("base", xpos="far_left", ypos="head")
    gen "It's no wonder you need some relief from time to time." ("base", xpos="far_left", ypos="head")
    gen "But the owls!? What kind of girl your age asks for plush owls!?" ("base", xpos="far_left", ypos="head")


    her @ cheeks blush "*Sigh*...{w=0.4} If you'll just hand over the things I asked you to buy, then I'll make things clear." ("angry", "closed", "annoyed", "mid")
    gen "I'm still not sure I should be allowing you to have these things..." ("base", xpos="far_left", ypos="head")
    her "" ("angry", "narrow", "annoyed", "mid")
    call ctc
    gen "But since I know you're a good student, however... Here you go!{fast}" ("base", xpos="far_left", ypos="head")

    nar "You hand Hermione the items."

    her "Thank you Professor..." ("grin", "narrow", "base", "mid")
    her "Now if you'll give me just a moment." ("base", "narrow", "base", "mid")

    play sound "sounds/cloth_sound.ogg"
    pause .8

    her "There we go! All done!" ("grin", "happyCl", "base", "mid")

    hide hermione_main
    with d3

    call give_reward("Hermione hands over her creation to you.", "interface/icons/plush_owl_strapon.webp")

    her "What do you think?" ("grin", "wink", "base", "mid", xpos="mid", ypos="base", trans=dissolve)
    gen "What the hell am I looking at!?" ("angry", xpos="far_left", ypos="head")
    her "Don't you like it?" ("annoyed", "base", "base", "mid")
    her @ cheeks blush "I think he's cute!" ("crooked_smile", "narrow", "base", "down")
    gen "You've just Macgyvered together an owl that's as hung as a horse..." ("base", xpos="far_left", ypos="head")
    gen "And you think it's cute?" ("base", xpos="far_left", ypos="head")
    her "He, sir!" ("annoyed", "base", "annoyed", "mid")
    her "And yes, I do think he's cute..." ("base", "narrow", "base", "down")
    her @ cheeks blush "Of course, I'm not really interested in him for his looks." ("base", "narrow", "base", "down")
    gen "Good, because he looks like an abomination unto the gods." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Don't be so mean!" ("angry", "narrow", "worried", "mid")
    her @ cheeks blush "I love him!" ("grin", "narrow", "base", "down")
    her @ cheeks blush "I think I'm going to name him...{w=0.4} Jeff!" ("grin", "closed", "base", "mid")
    gen "His name...{w=0.4} Is Jeff?" ("base", xpos="far_left", ypos="head")
    gen "And what exactly is it this...{w=0.4} \"Jeff\", is going to do?" ("base", xpos="far_left", ypos="head")
    her "Oh, that's easy!" ("grin", "happyCl", "base", "mid")
    her @ cheeks blush "He's going to fuck me silly, of course!" ("crooked_smile", "narrow", "base", "mid")
    gen "Wait...{w=0.4} {size=+5}What?{/size}" ("angry", xpos="far_left", ypos="head")
    gen "How? It's an inanimate object!" ("angry", xpos="far_left", ypos="head")
    gen "I mean sure, he's certainly big enough for it..." ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh don't worry about that!" ("grin", "narrow", "base", "mid")
    her @ cheeks blush "I'll just use magic of course..." ("smile", "closed", "base", "mid")
    gen "Right...{w=0.4} Of course..." ("base", xpos="far_left", ypos="head")
    gen "So it's just glorified masturbation--" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "I'll use a spell I just learned to bring little Jeffy here to life!" ("crooked_smile", "narrow", "base", "mid")
    gen "I see...{w=0.4} And what about the other two?" ("base", xpos="far_left", ypos="head")

    her @ cheeks blush "Well, when I found out about this spell in the library the other day...." ("base", "narrow", "base", "R")
    her @ cheeks blush "I also came across this thing called \"airtight\"." ("grin", "narrow", "base", "R")
    her @ cheeks blush "The girl in the pictures seemed to be enjoying herself!" ("crooked_smile", "narrow", "base", "mid")
    gen "I bet she was...." ("base", xpos="far_left", ypos="head")
    gen "Wait, they have stuff like that in the library?" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "So my plan is to strap these huge purple cocks to my plushies, bring them to life, and then let them have their way with me." ("grin", "narrow", "base", "down") #lust filled gaze
    gen "You little slut!" ("base", xpos="far_left", ypos="head")
    gen "Twenty points to Gryffindor!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "What? But I'm not even selling you a favour." ("angry", "base", "base", "mid")
    gen "I don't care! For that plan alone, you deserve some points." ("base", xpos="far_left", ypos="head")
    gen "Especially for saying it out loud!" ("base", xpos="far_left", ypos="head")
    her @ cheeks blush "Oh! Well, thank you, sir!" ("grin", "closed", "base", "mid")
    her @ cheeks blush "Now... If you don't mind, I'd like to head back to my dorm." ("base", "squint", "base", "R")
    gen "I bet you do...{w=0.4} Very well, off you go, Miss Granger." ("base", xpos="far_left", ypos="head")
    gen "Have fun with...{w=0.4} \"Jeff\"." ("base", xpos="far_left", ypos="head")
    her "Oh, I will..." ("base", "base", "base", "mid")
    her "Goodnight, sir!" ("base", "base", "base", "R")
    gen "Goodnight Miss Granger." ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d5

    pause 1.0

    play sound "sounds/door.ogg"
    pause .8
    play sound "sounds/giggle2.ogg"
    pause .5
    her "Now then Jeff, show me what you're made of..."
    play sound "sounds/sit_on_bed.ogg"
    pause .8
    her "Piertotum Locomotor!"
    play sound "sounds/magic4.ogg"
    pause .8
    her "It worked!"
    her "Now then... Come here and--"
    play sound "sounds/gasp2.ogg"
    her "Jeffrey!"
    play sound "sounds/gltch.ogg"
    with kissiris
    pause .8
    play background "sounds/sexloop.ogg"
    her "*Ah*...{w=0.4} *Ah*...{w=0.4} *Ah*...{heart}{heart}{heart}" with vpunch
    pause 1
    centered "{size=+7}{color=#cbcbcb}The end{/color}{/size}"

    $ renpy.end_replay()

    #end of story
