
label cho_quid_E14_retrospection:

    # $ disable_game_menu()

    camera screens at sepia(0.66)

    call cc_gt_return.introspection

    #New scene, Flashback Shifts to CG with liquid luck potion bottle on bed
    # TODO: Add CG

    show cho_quidditch_outro bedroom potion as cg with fade
    play music "music/anticipations-by-tim-kulig-from-filmmusic-io.ogg" fadein 1 if_changed
    cho "(What's this?)"
    cho "(A bottle of...{w=0.3} liquid luck?!)"
    cho "(Did coach leave this for me?)"

    play sound "sounds/pickup_item.ogg"
    show cho_quidditch_outro bedroom -potion as cg with d3

    #Bottle is removed from covers.

    cho "(That must be why he wasn't so concerned about my equipment...)"
    cho "(Unless it's a placebo...)"

    play sound "sounds/bottle.ogg"
    pause .5
    play sound "sounds/sniff.ogg"
    cho "*Sniff*"

    cho "(No, that's liquid luck alright, no doubts about it...)"
    cho "(After all, he would know that you can't trick a Ravenclaw...)"
    cho "(But to think he'd give me this... Just so I could win the finals...)"
    cho "(...)"
    cho "(I'll just put it in my pocket for now...)"

    #New scene, Flashback shifts to daytime. Cho is at the quidditch pitch entrance. (early morning shader?)
    stop music fadeout 1

    call room("quidditch_pitch")
    call cho_chibi("stand", "mid", "base")
    play background "sounds/outskirts.ogg" fadein 2
    with fade

    cho "(*Hmm*... He's not here yet...)"
    cho "(I guess I'll sit down and wait for him.)"
    #cloth sound

    #Fade to New CG potion held up into sky

    play sound "sounds/rustling_metal.ogg"
    show cho_quidditch_outro pitch as cg with fade

    cho "(Liquid luck...)"
    cho "(I never thought I'd hold one of those in my hand...)"
    cho "([name_genie_cho] must really want me to win if he's willing to risk his career by giving me this...)"
    cho "(But why did we go through all those lewd favours, if he was just going to give me a luck potion anyway...)"
    cho "(Did he agree to train me because of--)"
    cho "(... No, he wouldn't, would he?)"
    cho "(The training is over if I win...{w=0.4} If he just wanted me for my body, then...)"
    cho "(He must want to help me succeed, like he said from the start...)"
    cho "(Help me succeed... No matter--{w=0.2} *Yawn*... The cost.)"

    show cho_quidditch_outro pitch snape_talk as cg with fade

    #CG goes blurry for a moment and back again as Cho blinks, as the CG comes back, Snape's head appear inside the potion.

    sna "Today's lesson will be about Felix Felicis."
    sly1 "Who's that?"

    show cho_quidditch_outro pitch snape_angry as cg with d3

    sna "It's a potion, you idiot! A luck potion, more specifically."

    show cho_quidditch_outro pitch snape_talk as cg with d3

    sna "This potion provides the drinker with a tremendous amount of luck, turning an ordinary day into an extraordinary one."

    show cho_quidditch_outro pitch snape_smile as cg with d3

    sna "When under its effect, it will make the one who drinks it succeed in whatever activity they partake in, no matter what it is."

    show cho_quidditch_outro pitch snape_talk as cg with d3

    sna "However, it is highly toxic in large quantities, therefore can only be consumed a handful of times during one's lifetime."
    sly2 "Have you ever tried it yourself, sir?"

    show cho_quidditch_outro pitch snape_smile as cg with d3

    sna "Certainly!"

    show cho_quidditch_outro pitch snape_talk as cg with d3

    sna "I brewed and drank my very first one when I was about your age."
    sna "Even though I knew about how it worked, I still couldn't believe that consuming it was enough to solve all my problems."
    sly1 "What problems did it solve, sir?"

    show cho_quidditch_outro pitch snape_smile as cg with d3

    sna "Why, losing my virginity of course!"

    # hide snape's head
    show cho_quidditch_outro pitch -snape_smile as cg with d3

    with vpunch
    cho "Gross!!"
    cho "(What am I thinking...)"
    cho "(I can't achieve my goals like this!)"

    show screen blkfade
    hide cg
    with d5

    #Fade to black
    play sound "sounds/bottle.ogg"
    pause .6
    play sound "sounds/spill.ogg"
    nar "Cho spills the yellow-tinted liquid on the grass."

    pause .6
    #Pouring liquid sound


    cho "(It's done... There's no going back now.)"
    cho "(Hold on... Didn't Snape say luck potion is expensive...)"
    cho "(Blimey! I could have sold it, and bought a new broom...)"
    cho "(Too late for that now. I better find the best alternative broom I can!)"

    call cho_quid_E12.introspection

    stop music fadeout 1

    call gryffindor_match.introspection1
    call gryffindor_match.introspection2

    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}Few minutes into the game...{/color}{/size}"

    hide screen blkfade
    call gryffindor_match.introspection3

    call gryffindor_match_return.introspection

    show screen blkfade
    with d5

    $ renpy.end_replay()
