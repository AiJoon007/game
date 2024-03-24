label eating_for_pleasure_rewards:
    call unlock_clothing(text="New clothing items for Hermione have been unlocked!", item=her_outfit_pizza)
    return

label eating_for_pleasure:

    # Setup
    $ hermione.equip(her_outfit_default)
    $ game.daytime = False
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Eating for Pleasure{/color}{/size}"

    narrator "This story is best played when drunk...{w=0.4} or not at all...{w=0.4} it's the worst...{w=0.4} enjoy!"

    hide screen blkfade

    play music "music/fluffing-a-duck-by-kevin-macleod.ogg" if_changed

    gen "*Gah*... this place is so dull..." ("base", xpos="far_left", ypos="head")
    gen "Not a single gambling den or a whore house..." ("base", xpos="far_left", ypos="head")
    gen "And even if I don't need to eat, I'd do anything for a pizza right about now..." ("base", xpos="far_left", ypos="head")
    hat "Just call a pizza place then..."

    play sound "sounds/MaleGasp.ogg"
    gen "Did that hat just speak?!" ("angry", xpos="far_left", ypos="head") with vpunch
    hat "Of course I speak!"
    hat "Not only that... I know who you are..."
    gen "You do?" ("open", xpos="far_left", ypos="head")
    gen "Then why haven't you said anything until now!" ("angry", xpos="far_left", ypos="head")
    gen "I've been sitting here alone for months!" ("angry", xpos="far_left", ypos="head")
    hat "A wise man told me not to speak unless you have something to say."
    gen "Wait..." ("base", xpos="far_left", ypos="head")
    gen "The real Dumbledore told you to shut the fuck up?" ("grin", xpos="far_left", ypos="head")
    hat "..."
    gen "Anyway, what did you mean by \"call\"?" ("base", xpos="far_left", ypos="head")

    gen "I haven't seen a single phone in this place!" ("base", xpos="far_left", ypos="head")
    hat "Just use the floo-network."
    gen "The floo... is that like a sewer network or something?" ("base", xpos="far_left", ypos="head")
    gen "You guys got magic turtle pizza deliverers?" ("base", xpos="far_left", ypos="head")
    hat "No, I'm talking about the fireplace."
    hat "Wizards use it as a form of communication and travel."
    gen "Wait, so like a portal?" ("base", xpos="far_left", ypos="head")
    gen "I've been able to just travel to any ole fireplace this whole time?!" ("angry", xpos="far_left", ypos="head")
    hat "Hogwarts fireplaces are limited to voice communication, or we'd have all sorts of dark wizards roaming this place..."
    gen "(Sounds like discrimination to me...)" ("base", xpos="far_left", ypos="head")
    gen "How does it work then?" ("base", xpos="far_left", ypos="head")
    hat "There should be some powder in one of the drawers, take it and throw some in the fire and say out loud who you want to call."
    gen "Gimme a sec." ("base", xpos="far_left", ypos="head")

    pause 0.5
    call gen_chibi("jerk_off_behind_desk")
    with d5
    play sound "sounds/drawer_open.ogg"
    pause 0.75
    call gen_chibi("sit_behind_desk")
    with d5

    gen "Oh, that powder!" ("base", xpos="far_left", ypos="head")
    gen "I was wondering what it was for..." ("base", xpos="far_left", ypos="head")
    gen "Okay, let's do this!" ("base", xpos="far_left", ypos="head")
    show screen blkfade
    with d5
    play sound "sounds/08_hop_on_desk.ogg"
    pause 1.4
    call gen_chibi("stand", "desk", "base", flip=True)
    hide screen blkfade
    with d5
    pause 0.3
    call gen_walk(560, "base")
    pause 2.0
    gen "..." ("base", xpos="far_left", ypos="head")
    call gen_chibi("stand", flip=False)
    with d3
    gen "So I just throw it in and say who I'm calling?" ("base", xpos="far_left", ypos="head")
    hat "Yes... make sure you get right up next to it..."
    gen "Okay then..." ("base", xpos="far_left", ypos="head")
    call gen_chibi("stand_alt", flip=True)
    with d3
    pause 1.0
    call gen_chibi("grab_low")
    pause 0.5
    play sound "sounds/fire_woosh.ogg"
    $ states.fireplace_started = True
    show screen gfx_effect(690, 320, img="smoke", zoom=0.5)
    pause 0.1
    $ fireplace_OBJ.foreground = "fireplace_greenfire"
    with d5
    pause 1.0
    play sound "sounds/cough_male.ogg"
    gen "*Cough* *Cough*" ("base", xpos="far_left", ypos="head")
    hat "Say the name!"
    play sound "sounds/sniff.ogg"
    gen "*Ah* Piz-- *Ah-a*" ("base", xpos="far_left", ypos="head")
    play sound "sounds/sniff.ogg"
    pause 0.5
    play sound "sounds/sniff.ogg"
    pause 0.5
    call gen_chibi("sneeze")
    with d2
    play sound "sounds/glass_break.ogg"
    pause 0.4
    call gen_chibi("stand_alt")
    with d2
    "Pizza Hu--*shoo*lut!!!{fast}" with hpunch
    pause 1.0
    hat "Did you say Pizza--?"
    play sound "sounds/microphone_feedback.ogg"
    "*Static*... Welcome to Pizza slut, may I take your order?"
    hat "Well, I'll be damned..."
    gen "{size=+8}Yes! Hello, is this thing on?{/size}" ("base", xpos="far_left", ypos="head")
    "Sir, I can hear you... No need to shout."

    $ flag = None
    menu:
        "What will be your order, sir?"

        "-Meat Eater-":
            $ flag = 0
            gen "{size=+16}I'll have the pepperoni!{/size}" ("open", xpos="far_left", ypos="head") with vpunch
            "*Sigh* One pepperoni... anything else?"
            $ her_outfit_pizza.group[2].set_color([[180, 50, 10, 255]])
            $ her_outfit_pizza.group[3].set_color([[180, 50, 10, 255]])
        "-Vegan Delight-":
            $ flag = 1
            gen "{size=+16}I'll have the vegetariana!{/size}" ("open", xpos="far_left", ypos="head") with vpunch
            "*Sigh* One vegetariana... anything else?"
            $ her_outfit_pizza.group[2].set_color([[73, 226, 53, 255]])
            $ her_outfit_pizza.group[3].set_color([[73, 226, 53, 255]])

    $ hermione.equip(her_outfit_pizza)
    gen "{size=+8}Hold on...{/size}" ("base", xpos="far_left", ypos="head")
    call gen_chibi("stand", flip=False)
    with d3
    gen "Did you want anything?" ("base", xpos="far_left", ypos="head")
    hat "...{w=0.4}I'm a hat."
    gen "Oh... right." ("base", xpos="far_left", ypos="head")
    call gen_chibi("stand_alt", flip=True)
    with d3
    gen "{size=+16}That's all, thanks!{/size}" ("open", xpos="far_left", ypos="head") with hpunch
    "And your address?"
    gen "{size=+8}Headmaster's office, Hogwash!{/size}" ("base", xpos="far_left", ypos="head")
    "Hogwarts sir?"
    if flag == 0:
        gen "{size=+8}No, just pepperoni thanks!{/size}" ("open", xpos="far_left", ypos="head") with vpunch
    else:
        gen "{size=+8}No meat please, just olives!{/size}" ("open", xpos="far_left", ypos="head") with vpunch
    "..."
    "Okay then..."
    gen "{size=+8}Ten minutes or pizza's free?{/size}" ("base", xpos="far_left", ypos="head")
    "Of course, sir... we've never been late using the floo..."
    "Hold on a second..."
    "It seems like your floo-network fireplace has blocked incoming travel."
    gen "{size=+8}What a shame... I guess you'll have to make your way here the old-fashioned way.{/size}" ("grin", xpos="far_left", ypos="head")
    gen "{size=+8}Headmaster's office is on the seventh floor, enjoy the moving staircases!{/size}" ("grin", xpos="far_left", ypos="head")
    "But sir..."
    play sound "sounds/microphone_feedback.ogg"
    gen "{size=+16}Clock's ticking...{/size}" ("open", xpos="far_left", ypos="head") with hpunch
    "Okay then, your delivery will be as soon as... humanly possible..."
    pause 1.0
    call gen_chibi("stand", flip=False)
    with d3
    pause 0.5
    gen "Hat, how do I hang up?" ("base", xpos="far_left", ypos="head")
    hat "Just extinguish the fire."
    call gen_chibi("stand", flip=True)
    with d3
    gen "(A phone would have been so much easier...)" ("base", xpos="far_left", ypos="head")
    play sound "sounds/spit.ogg"
    gen "..." ("base", xpos="far_left", ypos="head")
    hat "No, just use the..."
    gen "Don't worry, I got this..." ("base", xpos="far_left", ypos="head")

    call gen_chibi("stand_alt")
    with d3
    pause 0.3
    show screen blkfade
    with d5
    gen "..." ("base", xpos="far_left", ypos="head")
    play sound "sounds/zipper.ogg"
    hat "Wait... what are you..."
    play sound "sounds/fuse.ogg"
    gen "Ah...{w=0.4} Must've been at least a hundred years..." ("grin", xpos="far_left", ypos="head")
    pause 1.0
    hide screen blkfade
    pause 1.0
    play sound "sounds/fire_woosh.ogg"
    $ fireplace_OBJ.foreground = None
    with d5
    $ states.fireplace_started = False
    pause 1.0

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Some time later...{/color}{/size}"

    call gen_chibi("sit_behind_desk")

    hide screen blkfade
    with d5

    gen "They sure are taking their goddamn time!" ("angry", xpos="far_left", ypos="head")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "Maybe I could jerk off a little..." ("base", xpos="far_left", ypos="head")
    call gen_chibi("jerk_off_behind_desk")
    with d5
    pause 1.2
    hat "Eww!"
    call gen_chibi("sit_behind_desk")
    with d5
    play sound "sounds/MaleGasp.ogg"
    gen "Ah fuck!" ("angry", xpos="far_left", ypos="head")
    gen "You're still here..." ("base", xpos="far_left", ypos="head")
    gen "How am I supposed to jerk off in peace... It will never be the same with a pervert hat ogling me!" ("angry", xpos="far_left", ypos="head")
    hat "{size=-4}..... It never seemed to bother you before......{/size}"
    gen "Because I wasn't aware of your existence!" ("angry", xpos="far_left", ypos="head")
    pause 1.0

    play sound "sounds/knocking.ogg"
    "*Knock-knock-knock*"
    pause 1.0
    gen "{size=+4}Who's there?{/size}" ("open", xpos="far_left", ypos="head")
    "{size=+5}Pizza!{/size}"
    gen "{size=+4}Pizza who?{/size}" ("base", xpos="far_left", ypos="head")
    "{cps=8}..........{/cps}"
    "{size=+5}Pizza slut,{w=0.5} sir........{/size}"
    gen "*he-he-heh*" ("grin", xpos="far_left", ypos="head")
    gen "Finally..." ("base", xpos="far_left", ypos="head")
    gen "{size=+4}Come in!{/size}" ("open", xpos="far_left", ypos="head")
    pause 0.5
    call her_walk(action="enter", xpos="desk", ypos="base")
    her "Your order, sir!" ("smile", "happyCl", "base", "mid", xpos="right", ypos="base", trans=d3)
    gen "What...{w=0.3} the hell...{w=0.3} is this!" ("open", xpos="far_left", ypos="head")
    her "What do you mean... Did we get the wrong toppings?" ("annoyed", "base", "worried", "mid")
    gen "Toppings?!" ("angry", xpos="far_left", ypos="head")
    gen "There's only two slices! And they're on your body!" ("angry", xpos="far_left", ypos="head")
    her @ cheeks blush "A-Actually,{w=0.5} sir,{w=0.5} there are three slices..." ("open", "base", "base", "R")
    gen "Don't lie to me, I can clearly see just tw--" ("angry", xpos="far_left", ypos="head")

    pause 0.5
    $ hermione.strip("bottom")
    play sound "sounds/cloth_sound3.ogg"

    her @ cheeks blush "" ("grin", "base", "base", "mid")
    pause 1.0
    gen "{cps=3}..............{/cps}" ("open", xpos="far_left", ypos="head")
    gen "You expect me to eat this?" ("angry", xpos="far_left", ypos="head")
    her "Sir, you ordered from pizza slut. A slut and a pizza!" ("annoyed", "base", "worried", "mid")
    her "Our slogan is \"Enjoy a nice pizza ass with every slice\"!" ("open", "closed", "base", "mid")
    her "" ("base", "wink", "base", "mid")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "But there's only three..." ("base", xpos="far_left", ypos="head")
    gen ".........." ("base", xpos="far_left", ypos="head")
    gen "Give me the pizza..." ("base", xpos="far_left", ypos="head")
    her "Of course!"
    $ hermione.strip("clothes")
    pause 1.0
    her "Now, what else would you like to--" ("smile", "wink", "base", "mid")
    gen "Get out..." ("base", xpos="far_left", ypos="head")
    her "Sir, the payme--" ("open", "base", "worried", "mid")
    gen "I said, get out!" ("angry", xpos="far_left", ypos="head")
    her "Okay..." ("disgust", "base", "worried", "down")
    call her_walk(action="leave")
    gen "..." ("base", xpos="far_left", ypos="head")
    gen "These wizard customs... ruining something as holy as pizza..." ("base", xpos="far_left", ypos="head")
    gen "Mmm... Come to Genie, you beautiful temptress..." ("grin", xpos="far_left", ypos="head")

    show screen blkfade
    with d5

    "{cps=5}.........{/cps}{nw}"
    pause 1.0
    play sound "sounds/gltch.ogg"
    "Genie" "Yes.... *Mhmmmmmmm*... Just like that."
    hat "By Merlins beard, that's disgusting!"
    "Genie" "Shut up hat! Don't judge me!"

    centered "{size=+7}{color=#cbcbcb}{cps=1}...{/cps}End?{/color}{/size}"

    $ renpy.end_replay()

### Fireplace ###
image fireplace_greenfire: #Fireplace fire.
    matrixcolor HueMatrix(100)

    "fireplace_fire"
