label a_white_christmas_rewards:

    if not ton_outfit_wrestling_coach.unlocked:
        call unlock_clothing(text="New clothing items for Tonks have been unlocked!", item=ton_outfit_wrestling_coach)
        call unlock_clothing(text="New clothing items for Hermione have been unlocked!", item=her_outfit_wrestling)

    if not xmas_lights_ITEM.owned:
        $ xmas_phoenix_ITEM.owned = 1
        $ xmas_owl_ITEM.owned = 1
        $ xmas_fireplace_ITEM.owned = 1
        $ xmas_lights_ITEM.owned = 1
        $ xmas_wreaths_ITEM.owned = 1
        $ xmas_giftchair_ITEM.owned = 1

        call give_reward("Christmas decorations have been unlocked!", gift="interface/icons/xmas_wreaths.webp")

    return

label a_white_christmas:

    # Setup
    $ xmas_phoenix_ITEM.owned = 1
    $ xmas_owl_ITEM.owned = 1
    $ xmas_fireplace_ITEM.owned = 1
    $ xmas_lights_ITEM.owned = 1
    $ xmas_wreaths_ITEM.owned = 1
    $ xmas_giftchair_ITEM.owned = 1

    $ xmas_phoenix_ITEM.use()
    $ xmas_owl_ITEM.use()
    $ xmas_fireplace_ITEM.use()
    $ xmas_lights_ITEM.use()
    $ xmas_wreaths_ITEM.use()
    $ xmas_giftchair_ITEM.use()

    $ fireplace_OBJ.foreground = "fireplace_fire"
    $ tonks.equip(ton_outfit_wrestling_coach)
    $ hermione.equip(her_outfit_wrestling)
    stop weather
    $ game.daytime = False
    $ game.weather = "snow"
    call room("main_room")
    call gen_chibi("sit_behind_desk")
    stop music fadeout 1

    $ hermione.strip("accessory")


    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}A white Christmas{/color}{/size}"

    hide screen blkfade
    with d5

    play weather "sounds/wind_long_loop.ogg" fadein 2 fadeout 2
    play music "music/Anguish.ogg" fadein 1 if_changed

    nar "'Twas a night like any other in the headmaster's room."
    nar "Bored out of his mind, Genie felt a bit of gloom."

    gen "And here I thought this day was special..." ("base", xpos="far_left", ypos="head")
    nar "As Christmas Day is what it was."
    nar "But he was all alone... Like the wife of Mr. Claus..."

    gen "Stuck in here again, whilst everyone's having fun..." ("base", xpos="far_left", ypos="head")
    gen "Perhaps I should join the students..." ("base", xpos="far_left", ypos="head")
    gen "But if I'm caught, my days are done..." ("base", xpos="far_left", ypos="head")

    gen "Where's that Snape guy, or Miss Tonks?" ("base", xpos="far_left", ypos="head")
    gen "Do they only visit when I have drinks?" ("base", xpos="far_left", ypos="head")
    gen "Some friends they are..." ("base", xpos="far_left", ypos="head")
    gen "Man, this place stinks..." ("base", xpos="far_left", ypos="head")

    nar "He then let out a sigh and slouched down in his chair..."
    nar "As if loneliness was new to him."
    gen "Suck my dick, narrator." ("base", xpos="far_left", ypos="head")
    nar "As if in total despair..."

    nar "With nothing to do, his Christmas was looking quite grey."
    gen "I guess I'll do what I always did... Stuck in that lamp all day." ("base", xpos="far_left", ypos="head")

    play sound "sounds/paper_rustle.ogg"
    nar "Hold on, that's not in the script..."
    gen "I don't care anymore...{w=0.4} Just rewrite the script and add a couple whores." ("base", xpos="far_left", ypos="head")

    nar "You know, I can't do that, this is a Christmas tale..."
    gen "Chris mah nuts." ("base", xpos="far_left", ypos="head")
    gen "Leave me alone, the cheque's in the mail." ("base", xpos="far_left", ypos="head")

    nar "No, this isn't right, we can't leave it at that."
    gen "Then what do you want from me? You narrating twat..." ("base", xpos="far_left", ypos="head")

    gen "Do you expect me to play a tune? Perhaps you want me to sing?" ("base", xpos="far_left", ypos="head")
    nar "Anything wholesome at this point..."
    gen "Just let me do my thing..." ("base", xpos="far_left", ypos="head")

    play sound "sounds/zipper.ogg"
    call gen_chibi("jerk_off_behind_desk")
    with d3
    pause.8

    nar "Whipping out his... instrument... He started, \"Playing a tune\"."
    gen "Is that what they call it now?" ("grin", xpos="far_left", ypos="head")
    nar "Stop doing that, you buffoon!"

    gen "Narrate this, bitch! You don't have a choice!" ("base", xpos="far_left", ypos="head")
    gen "If you want to get paid for this job." ("base", xpos="far_left", ypos="head")
    nar "...{w=0.4} I'll send you an invoice."

    nar "*Ahem*..."
    nar "Stroking his dick in a rhythmical fashion..."
    gen "*Heh-heh*" ("grin", xpos="far_left", ypos="head")
    nar "(Screw this, I'll change this tale...)"
    gen "Now where's that narrative passion?" ("base", xpos="far_left", ypos="head")

    nar "Smirking to himself, Genie forgot just one thing..."
    nar "That I'm in charge of this story."
    gen "What?" ("base", xpos="far_left", ypos="head")
    play sound "sounds/MaleClearThroat.ogg"
    nar "Now...{w=0.8}{nw}"
    nar "Now...{fast} Entering the ring!" with hpunch

    stop music fadeout 2

    show screen blkfade
    with d5

    nar "The office disappeared, and he got trapped in the void."
    gen "What the fuck have you done to me?" ("angry", xpos="far_left", ypos="head")
    nar "The narrative thread broken, now completely destroyed."

    call room("boxing_ring")
    play sound "sounds/microphone_feedback.ogg"
    call gen_chibi("dick_out", xpos="left", ypos="base")

    hide screen blkfade
    with d3
    nar "But then the void went away{nw}"
    play sound "sounds/killswitch_on.ogg"
    $ boxing_ring_lights = True
    play background "sounds/crowd.ogg" fadein 10
    nar "But then the void went away{fast} as a flash of light appeared!"

    nar "And with that, there was music and an audience who loudly cheered!"

    play sound "sounds/crowd_cheer.ogg"
    play music "music/Under-the-Radar by PhobyAk.ogg" fadein 1 fadeout 1 if_changed

    nar "As genie's vision came back into focus, he saw where he was stood."
    call gen_chibi("dick_out_shocked")
    nar "In a wrestling ring, with his cock out... Everyone checking out his wood."

    nar "Frozen on the spot, the only thing he could do was shout."
    gen "I'll kill you for this!" (face="open", base="hard", xpos=100, trans=d3)
    nar "The match now beginning."
    nar "The opponents, walking out."

    call gen_chibi("dick_out_normal")
    gen "So much for the Christmas theme." (face="angry", base="hard")

    call her_chibi("stand", xpos="right", ypos="base")
    with d3

    nar "Genie said as his opponent entered the ring..."
    her "" ("smile", "narrow", "base", "L", xpos="right", ypos="base", trans=d3)
    nar "With a smirk spread across her face...{w=0.4} Her eyes fixed on Genie's thing."

    nar "Her coach then appeared and jumped over the rope."

    call ton_chibi("stand", xpos="far_right", ypos="base")
    with d3

    ton "I want a clean match... No trickery!" ("open", "base", "annoyed", "L", xpos="base", ypos="base", trans=d3)
    ton "Don't you dare to even grope!" ("soft", "narrow", "annoyed", "L")

    play sound "sounds/crowd_stomping.ogg"
    nar "The audience was ecstatic, stomping loudly on the floor."
    nar "Until the opponents' coach raised their hand, and the stomping was no more."

    nar "Genie held his breath until there was a shout."
    ton "Now let's do this thing...{w=0.4} {size=+2}Let's start...{/size} {w=0.4}{size=+3}this...{/size} {w=0.4}{size=+4}silly...{/size} {w=0.4}{size=+5}bout!{/size}" ("mad", "base", "annoyed", "L")

    play sound "sounds/crowd_cheer.ogg"

    gen "That's not fair at all, I can't fight her like this!" (face="open", base="hard", trans=d3)
    gen "" (face="angry", base="hard", trans=d3)
    her "" ("smile", "narrow", "base", "R", trans=d3)
    ton "Oh, you've got this all wrong, my dear..." ("base", "narrow", "base", "L")
    ton "Hermione... Get out those tits!" ("horny", "base", "base", "L")

    her @ cheeks blush "" ("base", "narrow", "base", "L")
    pause .8

    $ hermione.strip("robe")
    play sound "sounds/crowd_cheer.ogg"

    gen "What kind of fight is this?" (face="base", base="hard", trans=d3)
    nar "Genie said, his cock twitching from the sight."
    gen "This is a wrestling ring, is it not? Are we not supposed to fight?" (face="angry", base="hard", trans=d3)

    ton "" ("base", "narrow", "base", "L")
    her @ cheeks blush "Fighting in your condition? Please don't make me laugh..." ("angry", "narrow", "base", "L")

    $ hermione.strip("bra")

    her @ cheeks blush "This is a test of will...{w=0.4} Fingers against staff..." ("smile", "narrow", "base", "L")

    $ hermione.strip("clothes")
    call ctc
    $ hermione.set_pose("hand_on_pussy")
    $ hermione.set_cum(pussy="wet")
    call her_chibi("masturbate_pause")
    #Finger inserted
    play sound "sounds/slick_02.ogg"
    her "" ("soft", "closed", "worried", "mid", trans=d3)
    with kissiris
    with d3

    nar "Hermione's panties then dropped and slid down to the floor, as she plunged her fingers inside her pussy, faster than she'd ever done before."

    ton @ cheeks blush "First to cum will win, now get to stroking that dick!" ("grin", "narrow", "base", "L")
    ton @ cheeks blush "Keep your eyes on your opponent." ("grin", "base", "base", "L")
    her "" ("soft", "base", "worried", "L", trans=d3)
    ton @ cheeks blush "Show who's the master of cumming quick!" ("horny", "base", "base", "L")

    call gen_chibi("dick_out")
    gen "Then you've picked the wrong opponent." (face="grin", base="hard", trans=d3)
    her "" ("soft", "happy", "base", "L")
    gen "You'll never have me beat." (face="grin", base="hard")
    gen "I've had hundreds of years of practice, of stroking this precious meat." (face="grin", base="hard", trans=d3)

    ton @ cheeks blush "Then hurry up will you, she's already begun." ("open", "base", "shocked", "L")
    ton @ cheeks blush "Start stroking that meat of yours, in five...{w=0.4} four...{w=0.4} three...{w=0.4} two...{w=0.4} one!" ("grin", "narrow", "annoyed", "L")

    play music "music/firebrand-by-kevin-macleod.ogg" fadein 1 if_changed
    play sound "sounds/wrestling_bell.ogg"

    call gen_chibi("hold_dick")
    gen "" (face="grin", base="grab_dick")
    with d3
    her "" ("grin", "narrow", "base", "L")
    nar "Genie followed Hermione's lead, and grabbed a hold of his member."
    call her_chibi("masturbate")
    call gen_chibi("jerk_off")
    with d3
    nar "Then began stroking like a mad man, as if he had just finished No Nut November."

    play sound "sounds/crowd_cheer.ogg"
    her @ cheeks blush "" ("crooked_smile", "narrow", "base", "L")
    nar "Hermione moaned loudly for the audience and flushed across her face."
    gen "Real crowd pleaser that one..." (face="angry", base="grab_dick")
    her @ cheeks blush "" ("soft", "narrow", "base", "R")
    ton "Remember our practice, girl! Keep a steady pace!" ("open", "base", "annoyed", "L")

    her @ cheeks blush "" ("grin", "narrow", "base", "L")
    gen "You've met your match girl, I have an endless supply!" (face="open", base="grab_dick")
    ton "" ("grin", "base", "base", "L")
    gen "There's enough cum in these balls to stop the desert from being dry." (face="grin", base="grab_dick")

    her @ cheeks blush "" ("grin", "narrow", "base", "stare")
    nar "Hermione started shaking... As she loved being in the spotlight."
    her @ cheeks blush "" ("open_wide_tongue", "narrow", "base", "up")
    gen "" (face="open", base="grab_dick")
    nar "Then she pushed her fingers deep inside her, her pussy gripping oh so tight..."

    gen "" (face="angry", base="grab_dick")
    ton "That's it, Miss Granger! Just make sure you don't get hurt!" ("mad", "narrow", "shocked", "L")
    ton "Show him who is boss, move those fingers until you squirt!" ("grin", "wink", "base", "L")

    ton "" ("grin", "base", "base", "L")
    nar "Genie tried to keep up--"
    gen "Fuck you, I'm close to ejaculating!" (face="angry", base="grab_dick")
    gen "She can't beat me at this! I will cover her like a painting!" (face="angry", base="grab_dick")

    her @ cheeks blush "" ("grin", "narrow", "base", "up")
    play sound "sounds/slick_02.ogg"
    nar "Hermione shook even more when she pushed deep into her gash..."
    ton @ cheeks blush "" ("horny", "narrow", "base", "down")
    nar "Genie loss imminent--"
    gen "NO!" (face="open", base="grab_dick")
    nar "As she pulled them out with a--"
    play sound "sounds/slick_01.ogg"
    #Hermione Squirts
    her @ cheeks blush "" ("open_wide_tongue", "wide", "base", "up")
    $ hermione.set_cum(pussy="squirt")
    with kissiris
    pause .8
    $ hermione.set_cum(pussy="squirt_post")
    her @ cheeks blush "" ("smile", "happyCl", "base", "mid")
    gen "" (face="angry", base="grab_dick")
    ton @ cheeks blush "" ("grin", "base", "base", "L")
    "{size=+4}*Splash!*{/size}" #Big text
    stop music fadeout 2
    call gen_chibi("hold_dick")
    call her_chibi("masturbate_pause")

    $ hermione.set_pose(None)
    $ hermione.set_cum(None)
    with d5
    her @ cheeks blush "I...{w=0.4} I won!" ("grin", "happy", "base", "stare")

    play sound "sounds/crowd_applause.ogg"
    $ hermione.wear("accessory")

    her @ cheeks blush "" ("grin", "happy", "base", "L")
    nar "Said the girl, as the crowd erupted with a roar."
    her @ cheeks blush "" ("base", "happy", "base", "R")
    nar "The genie finally defeated, like never seen--"
    play music "music/firebrand-by-kevin-macleod.ogg" fadein 1 if_changed
    her @ cheeks blush "" ("angry", "base", "base", "L")
    ton @ cheeks blush "" ("clench", "wide", "base", "L")
    call gen_chibi("jerk_off")
    with hpunch
    gen "{size=+4}You fucking whore!{/size}" (face="open", base="grab_dick")

    nar "Oh, no you don't!"
    nar "The girl is the winner!"
    gen "That slut started before I did!" (face="angry", base="grab_dick")
    gen "That slut started before I did!{fast} Now eat this semen...{w=0.4} {size=+4}Dinner!{/size}" (face="grin", base="grab_dick")

    nar "And with a yell and a grunt, genie emptied his balls."
    show screen blkfade
    with d5
    nar "As the arena faded away, shifting back to Hogwarts halls."

    stop music fadeout 2
    stop background fadeout 2

    play weather "sounds/wind_long_loop.ogg" fadein 2 fadeout 2

    gen "What the hell happened?" ("angry", xpos="far_left", ypos="head")
    nar "Genie said, as his vision went black."
    nar "Now what shall we do, dear audience... Where did he empty that pulsing sack?"

    nar "Oh yes... I know!"
    gen "Don't you dare." ("angry", xpos="far_left", ypos="head")
    nar "Back to the office, we go!"
    nar "His vision now returning."
    gen "Please let it be some sexy hoe..." ("angry", xpos="far_left", ypos="head")

    call room("main_room")
    call gen_chibi("cum_close", xpos="mid", ypos="base")
    call sna_chibi("snape_jizz_covered", xpos="right", ypos="base")

    hide screen blkfade
    with d9

    call gen_chibi("cum_close_done")
    pause .8
    play sound "sounds/malegasp.ogg"
    call gen_chibi("dick_out_shocked")
    with d3
    nar "Too shocked to even speak, and glazed like a cake."
    sna "" (face="snape_cum", xpos="base", ypos="base", trans=d3)
    nar "Snape stood covered in semen."
    gen "I've made the gravest of mistakes..." ("base", xpos="far_left", ypos="head")

    show screen blkfade
    with d5
    play sound "sounds/card_punch4.ogg"

    nar "Genie then learned that day to never fuck with the narration."
    nar "As he then endured the most terrible of spells..."
    play sound "sounds/magic2.ogg"
    with flash
    gen "Aaaah!"
    nar "Ball disintegration."

    gen santa "Happy Holidays." ("grin", xpos="far_left", ypos="head")

    $ renpy.end_replay()
