label hermione_map_BJ:
    stop weather fadeout 1
    stop music fadeout 1

    $ her_outfit_last.save()
    $ hermione.equip(her_outfit_s_rain)

    $ renpy.call('forest_BJ_'+str(states.her.ev.forest_bj.stage))
    $ states.her.busy = True
    call set_her_map_location("gryffindor_room")

    #End event
    stop background fadeout 1
    $ hermione.set_cum(None)
    $ hermione.wear("all")
    $ hermione.equip(her_outfit_last)

    jump return_office

label forest_BJ_1: #BJ in the forest interrupted by moaning myrtle
    show screen blkfade
    with d3

    call gen_chibi("hide")

    play background "sounds/night.ogg" fadein 1
    play sound "sounds/steps_grass.ogg"

    nar "Sure enough, the map seems to {b}magically{/b} guide you towards the girl at the edge of the forest..."
    nar "As you get closer, you finally spot her outline in the moonlight, followed by little clouds of condensation escaping her mouth with each breath of midnight air."
    nar "After getting your hopes up, you realise that the cause for her heavy breathing is due to her being preoccupied with scraping some resin off a tree..."

    show her_forest bj as cg zorder 15
    hide screen blkfade
    with d3

    gen "[name_hermione_genie]? What are you doing out here at this time of night?" ("base", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    her "[name_genie_hermione]! I--{w=0.2} *Ehm*...{w=0.4} I wasn't doing anything bad, I swear!" ("angry", "wide", "base", "R", xpos="base", ypos="base", trans=d5)
    gen "..." ("base", xpos="far_left", ypos="base")
    her "*Ugh*, fine! If you must know, I was out here gathering up some mastic resin." ("upset", "narrow", "worried", "down")
    her "I know students aren't {i}technically{/i} supposed to touch the stuff, since it's normally used to make belch powder..." ("annoyed", "base", "base", "R")
    her "But I'm using it in my research for a non-addictive analgesic!" ("open", "closed", "base", "mid")
    gen "Right..." ("base", xpos="far_left", ypos="base")

    menu:
        "-Let her get back to her botany-":
            gen "Well, I better leave you be then..." ("base", xpos="far_left", ypos="base")
            her "Really?" ("upset", "wide", "worried", "shocked")
            her "You mean you don't want to--" ("upset", "wide", "worried", "shocked")
            her "..." ("upset", "narrow", "worried", "down")
            nar "You turn away from the miffed girl."
            gen "..." ("base", xpos="far_left", ypos="base")
            gen "(What's wrong with me?)" ("base", xpos="far_left", ypos="base")
            return
        "-Tell her to take care of your stem-":
            gen "Well, seeing that we're all alone out here..." ("base", xpos="far_left", ypos="base")
            her "Oh...{w=0.4} I--{w=0.2} *Ehm*...{w=0.4} I suppose we are..." ("open", "wide", "base", "R")
            gen "How about you take care of this dick?" ("base", xpos="far_left", ypos="base")
            her "Oh, thank goodness...{w=0.4} I thought you were going to murder me for a second..." ("base", "happyCl", "base", "mid", trans=hpunch)
            gen "What? How could you even think of such a thing!" ("base", xpos="far_left", ypos="base")
            her "Sorry [name_genie_hermione]... I don't know why I said that!" ("angry", "narrow", "base", "mid")
            her "I should just learn to shut my mouth sometimes..." ("base", "narrow", "base", "mid")
            gen "How about you open it instead, and let me ensure that you can't voice such nonsense?" ("base", xpos="far_left", ypos="base")
            her "*Hmm*...{w=0.4} Alright..." ("base", "narrow", "base", "down")
            $ states.her.ev.forest_bj.stage = 2

    play sound "sounds/cloth_sound3.ogg"
    $ hermione.strip("robe")
    $ hermione.equip(her_top_school5)
    with d3

    nar "The girl carefully removes her robes and tie, then puts them on the cool grass before kneeling down on them, in front of your steaming cock."

    hide hermione_main
    hide genie
    show her_forest bj h1 as cg
    with fade

    her "*Mmmm*...{w=0.4} Don't you ever get sick of me sucking your cock?"
    gen "The only thing I'll get sick of is having to wait for you to put it in your mouth."
    show her_forest bj h2 as cg
    her "*Hmph*...{w=0.4} Now, now, [name_genie_hermione]...{w=0.4} Patience is a virtue."
    show her_forest bj h3 as cg
    her "Besides, doesn't my hand feel nice?"
    gen "Not as nice as your mouth."
    her "Alright then...{w=0.4} Have it your way."
    show her_forest bj h4 as cg
    nar "Hermione leans forward and engulfs the head of your cock in her mouth."
    anon "{size=-4}Wow...{/size}"
    show her_forest bj h5 as cg
    her "!!!"
    her "Did you hear something?"
    gen "I don't believe so..."
    gen "Not unless you count the sounds of you putting your headmaster's dick in your mouth..."
    gen "Speaking of which..."
    show her_forest bj h6 as cg
    her "..."
    show her_forest bj h7 as cg
    nar "Hermione goes back to work, slobbering her way up and down your cock."
    gen "Gods...{w=0.4} They'd make you a queen for sucking cock like this in Agrabah..."
    show her_forest bj h8 as cg
    her "(Where?)"
    gen "*Mmm*... Fuck yes..."
    play sound "sounds/giggle2_loud.ogg"
    anon "{size=-8}*Te-he-he-he*...{/size}"
    show her_forest bj h5 as cg
    her "!!!"
    show her_forest bj h9 as cg
    her "Please tell me you heard something that time, [name_genie_hermione]!"

    menu:
        "-Tell her to get back to work-":
            gen "All I hear is a mouth that needs to get back to sucking."
            show her_forest bj h10 as cg
            her "Not now, [name_genie_hermione]!"
            her "I think someone else is here..."
            her "Or something else..."
            gen "Wait..."
            gen "You don't mean..."
        "-Agree with her-":
            show her_forest bj h10 as cg
            gen "You might be right..."
            gen "Did it sound like someone laughing?"
            her "Yeah..."
            her "{size=+10}Show yourselves!!!{/size}"

    show her_forest bj h9 m1 as cg
    myr "*Te-he-he-he*... Hi Hermione..."
    show her_forest bj h11 m1 as cg
    with hpunch
    gen "{size=+10}AH! A G-G-GHOST!{/size}"
    myr "*Ha-ha-ha-hah*!"
    myr "Good one Dumbledore! You always were a joker."
    her "Myrtle!"
    her "This isn't what it looks like!"
    myr "Isn't it?"
    myr "I think it looks lovely..."
    her "*Argh*! Please don't tell anyone!!!"
    show screen blkfade
    with d3

    nar "Hermione hastily covers up and sprints away, as the ghostly apparition fades away..."
    nar "You stumble back to your office in a confused and blue-balled stupor..."

    return


label forest_BJ_2:
    $ states.her.ev.forest_bj.stage = 3
    show screen blkfade
    with d3

    call gen_chibi("hide")

    play background "sounds/night.ogg" fadein 1
    play sound "sounds/steps_grass.ogg"

    nar "The map, yet again, leads you to the curly haired girl at the edge of the forest, who's currently in the midst of picking mushrooms."

    show her_forest bj as cg zorder 15
    hide screen blkfade
    with d3

    gen "More late night gardening?" ("base", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    pause.1
    her "{size=+10}[name_genie_hermione]!{/size}" ("shock", "wide", "base", "stare", xpos="base", ypos="base", trans=hpunch)
    her "Don't startle me like that!" ("annoyed", "base", "base", "R")
    her "And yes, I've been collecting some mushroom samples." ("soft", "base", "base", "mid")
    gen "Fascinating..." ("base", xpos="far_left", ypos="base")
    her "What are you doing out here?" ("base", "base", "base", "mid")
    her "I didn't expect to see anyone at this time of night." ("soft", "squint", "base", "mid")
    gen "Oh, you know me... Just looking for any opportunity to connect with my students..." ("base", xpos="far_left", ypos="base")
    her "*Mhmmm*...{w=0.4} That's what you're down here for? To {i}connect{/i}?" ("base", "happy", "base", "mid")
    gen "In a sense..." ("base", xpos="far_left", ypos="base")
    her "Fine...{w=0.4} Just let me take my robes off..." ("base", "base", "base", "R")

    play sound "sounds/cloth_sound3.ogg"
    $ hermione.strip("robe")
    $ hermione.equip(her_top_school5)
    with d3

    nar "Hermione quietly folds up her robe and places it, along with her tie on the cold ground before kneeling down on them."

    hide hermione_main
    hide genie
    show her_forest bj h12 as cg
    with fade

    gen "So...{w=0.4} You're not afraid that the ghost might show up again?"
    her "Are you talking about Myrtle?"
    gen "Yeah, that ghost girl."
    show her_forest bj h10 as cg
    her "Ghosts aren't really scary... It's only her tendency to gossip that I'm worried about..."
    gen "Gossip?"
    show her_forest bj h13 as cg
    her "Of course! Everyone knows that Myrtle's the biggest gossiper in the history of gossips..."
    show her_forest bj h4 as cg
    nar "Hermione quickly pops your cock into her mouth in between her words..."
    show her_forest bj h10 as cg
    her "*Pop*...{w=0.4} Not to mention the fact that she never forgets! Can you believe that she's {b}still{/b} going on about the whole McCartney thing?"
    show her_forest bj h8 as cg
    her "*Shlrp* *Schkk* *Slurp*"
    gen "*Mmmm*..."
    gen "So, have you heard of any gossip floating around then?"
    show her_forest bj h10 as cg
    her "Surprisingly not..."
    show her_forest bj h14 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h13 as cg
    her "Perhaps she doesn't want to upset you..."
    show her_forest bj h4 as cg
    her "*Shlrp* *Schkk* *Slurp*"
    gen "*Mmmm*..."
    show her_forest bj h10 as cg
    her "Still...{w=0.4} I didn't think she'd be able to help herself..."
    show her_forest bj h14 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h15 as cg
    her "Albus Dumbledore having his {b}cock{/b} sucked by Hermione Granger in the forest..."
    show her_forest bj h16 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h12 as cg
    her "It'd be the gossip of the century..."
    show her_forest bj h18 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    gen "You almost sound disappointed that she didn't tell anyone."
    show her_forest bj h17 as cg
    her "What? How could you say such a thing!"
    show her_forest bj h16 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h19 as cg
    her "I'd never be able to show my face around Hogwarts again..."
    show her_forest bj h20 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h21 as cg
    her "Everyone would just be imagining me on my knees..."
    show her_forest bj h18 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h21 as cg
    her "{b}Covered{/b} in your thick spunk..."
    show her_forest bj h20 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h17 as cg
    her "Word of it would probably even reach my mom and dad..."
    show her_forest bj h16 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h19 as cg
    her "Imagine what they'd think if they heard that their little girl--"
    show her_forest bj h18 as cg
    her "*Slurp* *Schkk* *Shlrp*"
    show her_forest bj h21 as cg
    her "-- Is sucking such copious amounts of cum out her headmaster's fat, {size=+2}juicy,{/size} {size=+2}cock...{/size}{heart}"
    gen "*Argh*!! That's it girl!"
    gen "Here it comes!"
    show her_forest bj h22 as cg
    nar "You grab a hold of the back of Hermione's head and thrust forward, planting your cock firmly down her throat."
    show her_forest bj h22 m1 as cg
    myr "Wow...{w=0.4} I never thought you'd fit all of it..."
    show her_forest bj h23 m1 as cg
    her "!!!"
    nar "Not even the sudden appearance of a ghost could stop your colossal orgasm at this point--"
    nar "--and you start firing off a thick deluge of cum down Hermione's tender throat, the presence of someone else only serving to coax more out of your balls..."
    gen "*ARGH*!!!"
    show her_forest bj h24 m1 as cg
    call cum_block
    her "!!!!!!"
    show her_forest bj h25 m1 as cg
    call cum_block
    gen "Gods, I needed this!"
    show her_forest bj h26 m1 as cg
    myr "So much...{heart}{heart}{heart}"
    show her_forest bj h25 m1 as cg
    nar "Your balls continue to pump more and more cum down Hermione's throat."
    show her_forest bj h26 m1 as cg
    her "..."
    show her_forest bj h25 m1 as cg
    myr "Bye Hermione...{heart}{heart}{heart}"

    show screen blkfade
    with d3

    nar "Eventually your orgasm subsides, and you allow your softening member to slide out of Hermione's cum coated throat."
    show her_forest bj none as cg

    hide screen blkfade
    with d3

    her "I can't believe you just did that!" ("shock", "base", "angry", "mid")
    gen "Really? After everything that we've done?" ("base", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    her "It's a figure of speech! And more importantly..." ("angry", "closed", "angry", "mid")
    her "{size=+10}You just came down my throat, in front of moaning Myrtle!{/size}" ("scream", "closed", "angry", "mid")
    her "She's going to tell everyone about this now!" ("annoyed", "base", "angry", "mid")
    gen "So?" ("base", xpos="far_left", ypos="base")
    her "*Argh*!" ("disgust", "squint", "angry", "R")
    her "You can't keep treating me like some {heart}dirty{heart} little--" ("angry", "closed", "annoyed", "mid")
    gen "Cum dump?" ("grin", xpos="far_left", ypos="base")
    her "Yes! You can't just keep using me as you please!" ("angry", "squint", "base", "mid")
    her "Can't keep coating me in your, filthy, nasty {b}{heart}cum{heart}{/b}..." ("angry", "narrow", "angry", "R")
    her "..." ("angry", "narrow", "base", "dead")
    her "Well...{w=0.4} I hope you've learned your lesson!" ("open", "narrow", "base", "stare")
    her "I'm going to go back, and..." ("angry", "closed", "base", "R")
    her "*Geh*...{w=0.4} Wash the taste out of my mouth..." ("open", "squint", "worried", "up")
    her "And remember for next time--" ("open", "narrow", "base", "up")
    her "Don't{size=-1}... {b}cum{/b}... {size=-1}so... {size=-1}much... {size=-1}down... {size=-1}my... {size=-1}throat...{heart}{heart}{heart}{/size}{/size}{/size}{/size}{/size}{/size}" ("angry", "narrow", "base", "dead")
    show screen blkfade
    hide cg
    with d3

    nar "With that, Hermione staggers back to the castle, still coated in your thick layer of seed."

    return


label forest_BJ_3: #Complete BJ with Myrtle appearing after the cumshot
    $ states.her.ev.forest_bj.stage = 4
    show screen blkfade
    with d3

    call gen_chibi("hide")

    play background "sounds/night.ogg" fadein 1
    play sound "sounds/steps_grass.ogg"

    nar "Surely enough, the map once again manages to lead you to the lone girl at the edge of an imposing forest."
    nar "However, she doesn't appear to be preoccupied with her usual botany."

    show her_forest bj as cg zorder 15
    hide screen blkfade
    with d3

    gen "Good evening, [name_hermione_genie]." ("base", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    her "Good evening, [name_genie_hermione]...{w=0.4} Fancy meeting you here." ("soft", "base", "base", "R", xpos="base", ypos="base", trans=d5)
    gen "What are you doing out here at this hour? You don't appear to be collecting anything." ("base", xpos="far_left", ypos="base")
    her "Oh...{w=0.4} I just thought I'd come out here to--{w=0.2} Get some fresh air..." ("open", "base", "base", "down", xpos="base", ypos="base")
    play sound "sounds/sniff.ogg"
    her "*Aah*..." ("base", "base", "base", "mid", xpos="base", ypos="base")
    gen "I see..." ("base", xpos="far_left", ypos="base")
    gen "So you're not waiting out here for your headmaster to arrive, just so you can suck his cock out in the open?" ("base", xpos="far_left", ypos="base")
    her "What! O-of course not!" ("base", "narrow", "worried", "down")
    her "I'm just out here to admire the moon!" ("base", "base", "base", "R")
    gen "What moon?" ("base", xpos="far_left", ypos="base")
    nar "Hermione frantically looks at the cloudy sky, unable to even glimpse the moon through the impenetrable greyness."
    her "Oh...{w=0.4} *Uhm*..." ("open", "happy", "base", "R")
    gen "It's alright...{w=0.4} Just admit that you're a dirty little cumslut, [name_hermione_genie]." ("base", xpos="far_left", ypos="base")
    her "It's not like that!" ("upset", "narrow", "annoyed", "mid")
    her "{size=-4}I--{w=0.2} I just wanted to...{/size}" ("upset", "narrow", "base", "R_soft")
    gen "So you don't want me to cover you in cum like the cumslut you are?" ("base", xpos="far_left", ypos="base")
    her "..." ("base", "narrow", "worried", "down")
    her "*Ugh*...{w=0.4} If you must..." ("base", "narrow", "base", "dead")
    show screen blkfade
    with d3

    nar "Hermione studiously removes, folds, and lays her robe and tie on the cool night grass."

    show her_forest bj h15 as cg
    hide hermione_main
    hide genie
    hide screen blkfade
    with d3

    her "(Maybe I wouldn't have ended up a dirty little cumslut if your dick wasn't so enticing...)"

    #Hermione sucks Genie's cock
    show her_forest bj h16 as cg
    pause
    her "*Glck* *Shlrp* *Gluck*"
    show her_forest bj h17 as cg
    her "*Ah*....{heart}{heart}{heart}"
    her "I'm surprised how often we bump into each other out here, [name_genie_hermione]..."
    show her_forest bj h16 as cg
    her "*Glck* *Shlrp* *Gluck*"
    show her_forest bj h19 as cg
    her "It's almost as if you knew I was going to be here..."
    show her_forest bj h18 as cg
    her "*Glck* *Shlrp* *Gluck*"
    gen "I'm sure it's just a coincidence...{w=0.4} Although speaking of bumping, how about you help me bump this dick into the back of your throat."
    show her_forest bj h20 as cg
    her "*Khes* *sh-r*! (Yes sir!)"
    show her_forest bj h27 as cg
    nar "In response to your request, Hermione thrusts her entire lithe frame forwards, forcing your thick cock all the way down her throat."
    show her_forest bj h28 as cg
    gen "*Ugh*.... That's it, [name_hermione_genie]!"
    show her_forest bj h29 as cg
    gen "I'm surprised anyone could even take it this deep."
    show her_forest bj h17 as cg
    her "*Hmm*...{w=0.4} I suppose I've had a good teacher."
    show her_forest bj h19 as cg
    gen "That's true..."
    nar "You lower your hand and rest it on the back of the little sluts head..."
    show her_forest bj h30 as cg
    gen "THIS--"
    pause
    show her_forest bj h31 as cg
    gen "-can't be taught!"
    show her_forest bj h30 as cg
    her "*Glck* *Shlrp* *Gluck*"
    show her_forest bj h31 as cg
    nar "You vigorously start fucking the poor girl's throat with little regard for her well-being."
    show her_forest bj h32 as cg
    her "*Glck* *Shlrp* *Gluck*"
    show her_forest bj h33 as cg
    gen "You were destined to be a cocksucker."
    show her_forest bj h32 as cg
    her "*Glck* *Shlrp* *Gluck*"
    show her_forest bj h33 as cg
    gen "It's just taken you until now to realise."
    show her_forest bj h32 as cg
    her "*Glck* *Shlrp* *Gluck*"

    show her_forest bj h33  as cg
    show her_forest bj m2 as cg with d9

    nar "You're so focused on your face fucking session, that you almost fail to notice the ghostly apparition of an attractive little witch appearing behind Hermione."
    play sound "sounds/giggle2_loud.ogg"
    pause .3
    show her_forest bj h32 as cg
    gen "!!!"
    show her_forest bj h33 as cg
    nar "Before you even have time to scream, the ghost, raises her finger to her lips, shushing you."
    show her_forest bj h32 as cg
    nar "Instead of making herself known, it appears like she only wants to watch Hermione have her throat fucked silly..."
    show her_forest bj h34 as cg
    gen "Well, if it's a show you want, {size=+3}it's{/size} {size=+3}a{/size} {size=+3}show{/size} {size=+3}you'll{/size} {size=+3}get!{/size}"
    show her_forest bj h35 as cg
    her "???"
    show her_forest bj h34 as cg
    nar "Coaxed on by the prospect of an ethereal audience, you begin to get into a firm, and rough rhythm of properly fucking Hermione's throat raw."
    show her_forest bj h35 as cg
    her "*Glck*-*Glck*-*Glck*!!"
    show her_forest bj h34 as cg
    her "*Glck*{heart}*Glck*{heart}*Glck*"
    show her_forest bj h35 as cg
    myr "..."
    show her_forest bj h34 as cg
    her "*Slurp*! *Gulp*! *Slurp*!"
    show her_forest bj h35 as cg
    gen "Yes, just like that...{w=0.4} That's a good little slut..."
    show her_forest bj h34 as cg
    her "*Slurp*! *Slurp*! *Slurp*!"
    show her_forest bj h35 as cg
    gen "Now, go a bit deeper, would you?"
    show her_forest bj h34 as cg
    her "*Slurp*! *Slurp*! *Slurp*!"
    show her_forest bj h35 as cg
    gen "Come on, [name_hermione_genie]."
    show her_forest bj h36 as cg
    her "*Slurp*! *Gobble*! *Gobble*!"
    show her_forest bj h37 as cg
    gen "Deeper!"
    show her_forest bj h36 as cg
    her "*Gobble-gobble-slurp-gobble*!"
    show her_forest bj h37 as cg
    gen "Yes, like that!"
    show her_forest bj h36 as cg
    her "{size=+5}*Gobble-gobble-slurp-gobble*!{/size}"
    show her_forest bj h34 as cg
    gen "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    show her_forest bj h35 as cg
    gen "See? I told you that your body was made for this..."
    show her_forest bj h36 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h37 as cg
    gen "Made to take my cock!"
    show her_forest bj h36 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h37 as cg
    gen "Any time of day!"
    show her_forest bj h34 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h35 as cg
    gen "Anywhere you can get it!"
    show her_forest bj h34 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h37 as cg
    gen "And in front of anyone who will watch you!"
    show her_forest bj h38 as cg
    her "{size=+10}!!!{/size}"
    show her_forest bj h37 as cg
    myr "*He-he-he*...{w=0.4} Hi Hermione..."
    show her_forest bj h36 as cg
    her "*Glck* Sto--{w=0.3}! *glck*{heart}*glck*"
    show her_forest bj h37 as cg
    nar "Hermione's throat momentarily lessens its grip around your cock."
    nar "Her face now even redder than before, she starts to pull back, either due to embarrassment or lack of air..."
    show her_forest bj h36 as cg
    nar "Unfortunately for the petite witch, her shame only serves to intensify your pleasure."
    show her_forest bj h37 as cg
    gen "{size=+4}*ARGH*!!! HERE IT COMES, [name_hermione_genie]!{/size}"
    show her_forest bj h36 as cg
    call cum_block

    gen "{size=+7}*ARGH*!{/size}"
    show her_forest bj h37 as cg
    gen "{size=+7}Eat my cum, slut!{/size}"
    show her_forest bj h34 as cg
    call cum_block
    show her_forest bj h39 as cg
    call cum_block

    nar "Your cock starts firing off a huge load against the back of the poor girl's throat, quickly overflowing all the way up through her nostrils and back at you."

    her "{size=+14}!!!{/size}"
    myr "{size=+3}Oh{/size} {size=+3}my{/size} {size=+3}God!{/size}"
    show her_forest bj h39 as cg
    call cum_block

    myr "I've never seen this much cum in my whole life, or even since then!"
    myr "Look over here Dumbledore, and shoot some more!"
    show screen blkfade
    with d3
    show her_forest bj h39 m3 as cg

    nar "Moaning Myrtle rises up from the dewy ground, and flashes her spectral breasts towards you."
    show her_forest bj h41 m3 as cg
    hide screen blkfade
    with d3
    call cum_block

    gen "{size=+7}*ARGH*! YES!!!{/size}"
    show her_forest bj h42 m3 as cg
    nar "Your orgasm now renewed by the sight of some heavenly cans, you begin shooting cum down Hermione's throat anew."
    show her_forest bj h41 m3 as cg
    call cum_block

    her "*Gulp* *Gargggglelggg* *Gobble*...."
    show her_forest bj h42 m3 as cg
    call cum_block

    myr "More, Dumbledore, more!"
    show her_forest bj h41 m3 as cg
    call cum_block
    gen "{size=+15}*ARGH*!!!!{/size}"
    show her_forest bj h42 m3 as cg
    call cum_block

    her "*Gllllgggggg*..."
    show her_forest bj h41 m3 as cg
    call cum_block
    myr "{size=+14}MORE!!!{/size}"
    show her_forest bj h42 m3 as cg
    call cum_block

    show her_forest bj -m3 as cg with d9

    nar "Eventually, your orgasm comes to a halt, and you finally pull your sloppy cock out of Hermione's well-used hole..."
    show screen blkfade
    with hpunch
    play sound "sounds/fall.ogg"
    nar "She then collapses onto her robe, no longer held up by your member."
    show her_forest bj none as cg
    hide screen blkfade
    with d9
    gen "You did good, [name_hermione_genie]..." ("grin", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    gen "Wouldn't you say the same, ghost?" ("grin", xpos="far_left", ypos="base")
    gen "Ghost?" ("base", xpos="far_left", ypos="base")
    gen "Oh well..." ("base", xpos="far_left", ypos="base")
    nar "You notice that the limp body of Hermione has started to shiver in the cold air..."
    gen "I suppose I better get you back to the castle..." ("base", xpos="far_left", ypos="base")

    show screen blkfade
    hide cg
    hide genie
    with d3

    play sound "sounds/steps_grass.ogg"
    stop background fadeout 1

    nar "You wrap Hermione's robe over her like a blanket, and carry her back to your office."

    play sound "sounds/fire_woosh.ogg"
    nar "You carefully place her into a chair in front of the fireplace, light it, and then drape her cum covered robes over her."

    menu:
        gen "(Should I clean her up a bit?)"
        "-clean her up-":
            gen "(I suppose I should...)"
            nar "You grab the edge of her robes and wipe her face clean with it."
            her "*Zzz*...{w=0.4} No...{w=0.4} *Zzz*...{w=0.4} I wanna be a--{w=0.2} *zzz*...{w=0.4} Cumslut..."
            gen "*Shhh*...{w=0.4} Don't worry, [name_hermione_genie]...{w=0.4} There's plenty where that came from..."
        "-leave her be-":
            gen "(She looks better like this anyway...)"
            nar "Just as you're about to turn to walk over to your desk, you notice a content smile spreading across Hermione's face as she pulls her robes up over her shoulders."
            her "{size=-4}Night [name_genie_hermione]...{/size}"
            her "{size=-8}I love you...{/size}"

    nar "You walk over and sit down behind your desk, and then fall soundly asleep..."
    her "*Ouch*..."
    nar "After some time, you awake at just the right moment to see Hermione stumble, and then slip out through the office door."

    $ hermione.equip(her_outfit_last)
    hide screen blkfade
    return

label forest_BJ_4: #Moaning myrtle dirty talk (Repeatable) (Threaten to expose)
    $ states.her.ev.forest_bj.stage = 3 #Repeats 3rd event after this one.
    show screen blkfade
    with d3

    call gen_chibi("hide")

    play background "sounds/night.ogg" fadein 1
    play sound "sounds/steps_grass.ogg"

    nar "Once more, the marauders map leads you to Hermione at the edge of the forest, waiting patiently, apparently having dropped all pretences botanical."

    show her_forest bj as cg zorder 15
    hide screen blkfade
    with d3

    gen "[name_hermione_genie]..." ("base", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    her "About time you got here, [name_genie_hermione]!" ("upset", "narrow", "annoyed", "mid", xpos="base", ypos="base", trans=d5)
    her "Do you know how long I've been waiting out here in the cold?" ("annoyed", "happy", "base", "mid")

    menu:
        "-Apologise-":
            gen "Sorry about that..." ("base", xpos="far_left", ypos="base")
            gen "I'll try and be on time for our blowjobs from now on." ("base", xpos="far_left", ypos="base")
            her "Good...{w=0.4} It's the least you can do..." ("base", "closed", "angry", "mid")
        "\"You know where my office is.\"":
            her "*Hmph*..." ("upset", "narrow", "angry", "R")

    show screen blkfade
    with d3

    nar "Hermione removes her robes and tie, then kneels down onto a pillow and rug that she must have prepared before your arrival."
    nar "You quickly walk over to the girl, and present her with your thick cock."

    show her_forest bj h15 as cg

    hide hermione_main
    hide genie
    hide screen blkfade
    with d3

    her "*Mmmmm*..."
    show her_forest bj h17 as cg
    her "I can't believe you're making me come down here during these circumstances..."
    gen "Say what?"
    her "You heard me..."
    show her_forest bj h19 as cg
    her "Not only that, the only thing you're allowing me as a way to keep myself warm is sucking your dick..."
    show her_forest bj h16 as cg
    nar "Hermione quickly pops her head forward, wrapping her soft lips around the tip of your shaft."
    her "*Mmmmm*..."
    show her_forest bj h18 as cg
    her "*Slurp* *Glck* *Slrp*"
    show her_forest bj h20 as cg
    gen "*Ughhhh*...{w=0.4} That's it, [name_hermione_genie]..."
    gen "Be a good little cockslut for your headmaster..."
    show her_forest bj h16 as cg
    her "*Slurp*{heart}*Slurp*{heart}*Glck*"
    #Myrtle fade in
    show her_forest bj h16 m2 as cg
    gen "And for Casper, the slutty ghost here..."
    show her_forest bj h43 m2 as cg
    her "*Slurp*!!!*Slurp*!!!*Glck*!!!"

    menu:
        nar "Hermione, once again, tries to pull her mouth off your cock..."
        "-Let her-":
            nar "Reluctantly, you allow the girl to pull herself off your throbbing member..."
            show her_forest bj h10 m2 as cg
            her "Myrtle! Why are you always showing up like this?"
            myr "Aren't I allowed a bit of fun in my afterlife?"
            myr "It's not like I ever got any when I was alive..."
            show her_forest bj h6 m2 as cg
            her "Oh, alright then..."
            show her_forest bj h10 m2 as cg
            her "Just don't go blabbing to everyone in the girls' bathroom, okay?"
            myr "Deal."
            gen "Good..."
        "-Face fuck her-":
            pass

    show her_forest bj h28 m2 as cg
    nar "You place your hand on the back of Hermione's head, and pull it hard onto your waiting cock, impaling the poor girl's throat..."
    show her_forest bj h29 m2 as cg
    her "{size=+10}!!!{/size}"
    show her_forest bj h30 m2 as cg
    gen "*Ugh*...{w=0.4} Fuck yes..."
    show her_forest bj h31 m2 as cg
    her "{size=+5}*Gobble-gobble-slurp-gobble!* !!!{/size}"
    show her_forest bj h30 m2 as cg
    gen "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    show her_forest bj h31 m2 as cg
    myr "Wow...{w=0.4} You're so rough on her..."
    show her_forest bj h32 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h33 m2 as cg
    gen "*Ugh*...{w=0.4} Don't worry...{w=0.4} She loves it..."
    show her_forest bj h32 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h33 m2 as cg
    gen "She's probably wetter than the Nile down there..."
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h32 m2 as cg
    myr "You think so?"
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h33 m2 as cg
    gen "Go see for yourself!"
    show her_forest bj h32 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h33 m2 as cg
    myr "..."
    show her_forest bj h32 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h33 m2 as cg
    nar "Myrtle floats down into the earth."
    show her_forest bj h34 as cg
    her "{size=+10}!!!{/size}"
    show her_forest bj h35 as cg
    myr "She's dripping!"
    show her_forest bj h34 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h35 as cg
    myr "Not to mention, she isn't wearing any panties!"
    show her_forest bj h34 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h35 as cg
    gen "Yes, she tends to take them off whenever she gets the chance."
    show her_forest bj h34 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h35 m2 as cg
    myr "Hermione! You dirty little minx!"
    show her_forest bj h34 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h35 m2 as cg
    myr "Just wait until everyone in the girls' bathrooms hears about this tonight!"
    gen "What--"
    nar "You look over at Myrtle who gives you a quick wink."
    show her_forest bj h34 m2 as cg
    her "{size=+5}*Glck*HNNOOO*glck*{/size}"
    show her_forest bj h44 m2 as cg
    myr "So long as you're alright with that, Sir...{w=0.4} I don't have to mention you! It can just be Hermione!"
    show her_forest bj h34 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h35 m2 as cg

    menu:
        "\"Go nuts.\"":
            show her_forest bj h34 m2 as cg
            myr "Really?"
            show her_forest bj h35 m2 as cg
            her "{size=+5}*Glck*{heart}PRFFSSRR!!!{heart}*Glck*{/size}"
            show her_forest bj h34 m2 as cg
            myr "Oh, thank you, thank you, thank you!"
            show her_forest bj h35 m2 as cg
            her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
            show her_forest bj h34 m2 as cg
            myr "This is going to be the best decade of my afterlife!"
            show her_forest bj h35 m2 as cg
            her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
            show her_forest bj h34 m2 as cg
        "\"You can say it was me.\"":
            show her_forest bj h34 m2 as cg
            myr "{size=+2}{b}Really?{/b}{/size}"
            show her_forest bj h35 m2 as cg
            her "{size=+5}*Glck*{heart}WHHTT!!!{heart}*Glck*{/size}"
            show her_forest bj h34 m2 as cg
            myr "Oh, thank you, thank you, thank you!"
            show her_forest bj h35 m2 as cg
            her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
            show her_forest bj h34 m2 as cg
            myr "This is going to be the best decade of my afterlife!"
            show her_forest bj h35 m2 as cg
            her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"

    show her_forest bj h34 m2 as cg
    myr "I can't wait to tell everyone!!!"
    show her_forest bj h35 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "I'll go to rave--{w=0.2} No... The Slytherin bathroom first!"
    show her_forest bj h44 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "Then Gryffindor's!"
    show her_forest bj h35 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "Then Ravenclaw's!"
    show her_forest bj h35 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "Can't forget Hufflepuff!"
    show her_forest bj h35 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "Or the prefects' bathroom!"
    show her_forest bj h35 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "Then there's the teachers'!"
    show her_forest bj h35 m2 as cg
    her "{size=+5}*Glck*{heart}*Glck*{heart}*Glck*{/size}"
    show her_forest bj h34 m2 as cg
    myr "And Hogsmeade!"
    show her_forest bj h35 m2 as cg
    myr "{size=+2}THEN{/size} {size=+2}THE{/size} {size=+2}WHOLE{/size} {size=+2}WORLD!!!{/size}"
    show her_forest bj h34 m2 as cg
    gen "*ARGH*, HERE IT COMES, SLUTS!"
    show her_forest bj h35 m2 as cg
    gen "{size=+7}*ARGH*!{/size}"
    show her_forest bj h34 m2 as cg
    gen "{size=+7}Eat my cum, [name_hermione_genie]!{/size}"
    show screen blkfade
    with d3

    show her_forest bj h34 as cg
    nar "At the edge of your orgasm, Hermione forcefully pushes herself off your dick, then rips her top and skirt off in one swoop, before wrapping her hair around your cock."
    show her_forest bj h45 m2 as cg
    hide screen blkfade
    with d3

    her "{size=+5}That's it, [name_genie_hermione]! Cum for me! Cover me, in front of Myrtle!{/size}"
    with hpunch
    gen "{size=+5}What the hell is this?!{/size}"
    show her_forest bj h46 m2 as cg
    her "{size=+5}Go on [name_genie_hermione]! Didn't you call me a dirty little cumslut?{/size}"
    gen "*Argh*! You cum obsessed whore!"
    show her_forest bj h45 m2 as cg
    her "{size=+5}Yes I am!{/size}"
    her "{size=+5}Nothing but your cum hungry little slut, [name_genie_hermione]!{/size}"
    show her_forest bj h47 m2 as cg
    her "{size=+5}Now, show Myrtle what a real load looks like!{/size}"
    with hpunch
    gen "{size=+7}*Argh*!!!{/size}"
    gen "{size=+7}Take this!!!{/size}"

    show screen white
    pause .1
    hide screen white
    with hpunch
    show her_forest bj h48 m2 as cg
    her "{size=+5}*Ah*! Yes, [name_genie_hermione]! Yes! Cum all over me!{/size}"
    show screen white
    pause.1
    hide screen white
    show her_forest bj h49 m2 as cg
    pause.2
    show screen white
    pause .1
    hide screen white
    with hpunch
    gen "{size=+7}*ARGH*!{/size}"
    gen "{size=+7}*Argh*!!! YES!!!{/size}"
    show her_forest bj h50 m2 as cg
    her "{heart}{heart}{heart}{heart}"
    show screen blkfade
    with d3

    #Genie and Hermione back in the forest...
    $ hermione.set_cum(hair="heavy")
    $ hermione.strip("clothes")
    show her_forest bj none as cg

    hide screen blkfade
    with d3

    her "Wow, that was--" ("angry", "narrow", "worried", "down")
    her "Hold on...{w=0.4} Where's Myrtle?" ("angry", "narrow", "worried", "mid_soft")
    gen "Oh, she probably left to do that gossiping you were so worried about." ("base", xpos="far_left", ypos="base")
    show genie zorder 16 with None
    her "So you're telling me I got my hair all sticky for--" ("upset", "closed", "annoyed", "mid_soft")
    her "{size=+4}Wait, what did you say?!{/size}" ("scream", "wide", "base", "stare")
    gen "Yeah, didn't she say something about visiting the girls' bathrooms--" ("base", xpos="far_left", ypos="base")
    her "She can't do that! I'll have to stop her!" ("angry", "wide", "annoyed", "stare")
    play sound "sounds/giggle2_loud.ogg"
    myr "*Giggles*"
    gen "*Heh*-*Heh*!" ("grin", xpos="far_left", ypos="base")
    her "Oh...{w=0.4} So, she was just making a fool out of me..." ("soft", "narrow", "angry", "down")
    gen "I mean, it's not that difficult, seeing that you're standing naked in a forest, with your hair drenched in semen." ("base", xpos="far_left", ypos="base")
    her "*Hmm*...{w=0.4} Yes, I should probably get dressed..." ("soft", "base", "base", "down")
    gen "Go ahead...{w=0.4} But leave the semen in your hair, would you?" ("base", xpos="far_left", ypos="base")
    her "But, what if someone--" ("angry", "wide", "base", "stare")
    gen "*Hmm*?" ("base", xpos="far_left", ypos="base")
    her "Of course, [name_genie_hermione]..." ("soft", "narrow", "base", "down")
    play sound "sounds/giggle2_loud.ogg"
    myr "*Giggles*"
    gen "Good girl..." ("base", xpos="far_left", ypos="base")

    show screen blkfade
    hide cg
    with d3

    nar "After Hermione gets dressed, you both head back to the castle together. Along the way, she complains about how sticky her hair feels."

    return
