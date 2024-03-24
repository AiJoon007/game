# Mirror story: An odd circumstance
image dark_overlay:
    "images/rooms/room_of_requirement/dark_overlay_1.webp" with d3
    pause 0.4
    "images/rooms/room_of_requirement/dark_overlay_2.webp" with d3
    pause 0.4
    "images/rooms/room_of_requirement/dark_overlay_3.webp" with d3
    pause 0.4
    repeat

label an_odd_circumstance:

    stop weather
    $ game.daytime = False
    $ game.weather = "clear"
    $ game.day = 69
    $ game.gold = 420
    $ hermione.equip(her_outfit_default)
    call room("main_room")
    stop music fadeout 1
    show image "dark_overlay" zorder 6 as dark_overlay
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}An odd circumstance{/color}{/size}"

    hide screen blkfade
    show layer screens at sepia
    with d5

    play music "music/jazz take 2.ogg" fadein 1 if_changed

    "It was a normal night..."
    "I was sitting in my office as usual, slowly chipping away at some leftover paperwork..."
    "Leaning back in my chair, I closed my eyes for a moment, thinking back on recent events."
    "It has been a weird few days for sure... Not just my appearing in this office, but also the whole situation in general..."
    "I sat back up and hunched myself over the parchment."
    "Well, I guess it could be worse... The weather is... acceptable."
    "Why do I have to do this stuff again? Surely there should be some kind of secretary around..."
    "Suddenly, the door opened as if my wishes had come true...{w=0.5} Something about this felt backwards somehow."

    call her_walk(action="enter")
    her "Mister D."
    "Said the figure at the door, appearing as merely a shadow in the low light..."
    gen "(Mister... what?)" ("base", xpos="far_left", ypos="head")
    "I thought...{w=0.3} Now trying my best to focus on the figure in front of me."
    "Mister D?"
    "After hearing the urgent tone in the voice, I responded... seemingly out of reflex..."
    gen "Yes?" ("base", xpos="far_left", ypos="head")
    "The figure shifted their posture in a relieved fashion, as if they had been trying to get a hold of me for hours, and said..."
    her "Mister D... I've been trying to contact you for hours. But it looks like your phone may be off..."
    gen "My phone?" ("base", xpos="far_left", ypos="head")
    "I said in a puzzled manner..."
    "I never had a phone in here... in fact, there's not a single electronic device in this office..."
    "After a few moments, the figure stepped into the light, illuminating a girl's face."
    call her_walk("desk")
    her "..." ("base", "base", "base", "mid", xpos="base", ypos="base", trans=d3)
    "Her hazel coloured flowing hair reminded me of a leather-bound book, filled to the brim with the secrets of the girl in front of me..."
    "I felt myself becoming lost in her mysterious brown eyes, which provoked a sense of great pain and suffering."
    hide hermione_main
    with d3
    her "I'm so glad I found you... I've been trying to locate you for ages, you're not an easy man to find..."
    "Lost in thought, my mouth seemed to move on its own as I replied to the girl..."
    gen "Of course..." ("base", xpos="far_left", ypos="head")
    "Taken aback by my own automatic response, I thought to myself..."
    gen "(What am I doing, this girl seems to think I'm someone called... mister D?)" ("base", xpos="far_left", ypos="head")
    "Surely, that can't be me... Unless this is some other secret alias of mine..."
    "It appears she may know me, though... I better press further..."
    her "I knew you were good, but I didn't think you'd manage to do it as discretely as you did..."
    her "How professional..."
    her "And such a looker too... I can't believe we've just met..."
    "The only thing I could gather so far is that I must've helped her with some sort of delicate matter..."
    "I looked down at my papers again, trying to find some kind of clue what this might be..."
    "Tax fraud?"
    her "..."
    "The girl stood there for a minute, looking as if she wanted to say something but being unsure how to go about doing so..."
    "My eyes met with hers again, as I looked back up from my desk."
    her "..."
    "She blushed, now with a slightly guilty expression, fidgeting, and clearly out of her comfort zone..."
    "As I was about to open my mouth and speak, a voice that came from no specific direction chimed in before I even got a word out..."

    play sound "sounds/magic4.ogg"
    hide dark_overlay
    show screen white
    with d1
    $ hermione_chibi.zorder = states.desk_chibi_zorder - 1
    call her_chibi("stand",210, 450, flip=True)
    hide screen white
    show image "dark_overlay" zorder 6 as dark_overlay
    with d1

    her "Silencio."
    pause 1
    "A few seconds later, I tried to ask where that voice and bright light had come from... But as I did, I could only feel my lips moving with no sound emerging..."
    call gen_chibi("stand_by_desk", -8, 614, flip=False)
    with d3
    "Taken aback by this, I jumped out of my chair while clutching at my vocal cords..."
    "I turned around, now feeling slightly worried, looking for the source of the voice."
    her "Don't say anything else... You know why I'm here, we had a deal, remember?"
    "The girl had moved behind me in a flash!"
    "Was this it... Did I break a deal of ours?"
    "Was this girl here to kill me, is that why she sounded so worried?"
    "Feeling rather dizzy, I steadied myself on my desk, trying to compose myself..."
    "Suddenly, I felt a sharp tug and I knew this must be it..."
    gen "..." ("base", xpos="far_left", ypos="head")
    "I waited a few moments for the pain to begin..."
    gen "..." ("base", xpos="far_left", ypos="head")
    "But it never came..."

    hide hermione_main
    $ hermione_chibi.zorder = 3

    call her_chibi_scene("bj_pause")
    $ desk_OBJ.hidden = True
    with d3

    her "I hope this should suffice... I couldn't stand the thought of discussing this any further..."
    her "I have a reputation to uphold after all..."
    "After regaining my focus, I looked down and found the girl kneeling in front of me, her hand wrapped around my shaft."
    "Even if I were able to respond, I had but a second's notice before her lips had wrapped themselves around my cock."

    call her_chibi_scene("bj")
    with d3

    her "*Slurp!* *Gulp!* *Slurp!*"
    "Her head now bobbing back and forth as if her life depended on it..."
    "I felt myself growing harder in her mouth as her lips pressed against my skin..."
    her "*Slurp!* *Gobble!*"
    "What was it that I had done for this girl, in exchange for her degrading herself in such a manner?"
    "The girl then glanced up into my eyes, seeing my confused look..."
    "Interpreting this expression as her efforts being unsatisfactory, she then concentrated on the task she had set for herself and pushed her head forwards, taking the whole length down her throat."
    her "*Gulp!* *Gobble!* *Gobble!*"
    "Since I couldn't make a sound, I let out a heavy breath of air and closed my eyes for a few seconds..."
    show screen blkfade
    with d3
    "After a few moments, I opened my eyes and turned my head down again to observe the scene playing out in front of me."
    hide screen blkfade
    with d3
    "The girl suddenly pulled her mouth away..."

    call her_chibi_scene("bj_pause")
    with d3

    her "*G-g-gah...*"
    "A string of saliva still attached between her mouth and my penis slowly found itself moving down and then disconnected, resting across the front of her chest."
    "Smiling up at me, the girl started massaging my cock with a mixture of pre-cum and her saliva..."
    "Feeling more relaxed about the whole situation, I couldn't help but forget about any consequences and began to just enjoy myself."

    call her_chibi_scene("bj")
    with d3

    "Without warning, her lips wrapped themselves back around my now throbbing cock..."
    her "*Slurp!* *Gulp!* *Slurp!*"
    "Her head yet again found itself further and further down my shaft, easily taking in the whole thing this time, as her tongue slowly moved across the bottom."
    her "*Slurp!* *Slurp!* *Slurp!*"
    "For a moment, I could feel her forehead pressed against my torso as my cock reached the bottom of her throat... it seemed as if time had stopped..."
    her "..."
    "Suddenly, she looked up into my eyes as she started to move her tongue, massaging the underside of my cock..."
    her "*Gobble!* *Gltch!* *Slurp!*"
    "I closed my eyes, and then I felt a sudden rush of ecstasy come over me."
    "Right after I let out an inaudible groan, my pelvic muscles tightened as I began cumming down her throat."

    call her_chibi_scene("bj_cum_in")
    with hpunch

    "I opened my eyes as hers locked with mine in surprise from the sudden overwhelming amount of semen hitting the back of her throat."
    play sound "sounds/gulp.ogg"
    her "*Gulp!*"
    play sound "sounds/gulp.ogg"
    her "*Gulp!*"
    "Her eyes watered, and she looked as if she was about to pass out, but she kept her mouth wrapped around my shaft as she tried to swallow it all, a couple of bubbles now forming around her nose."
    her "*Aahh!*"

    call her_chibi_scene("bj_cum_out")
    with d3

    "She then pulled away, satisfied with her deed, just as another spurt came out from my seemingly bottomless balls and coated her surprised face..."

    call her_chibi_scene("bj_cum_out_done")
    with d3

    "As the fluids started flowing down her cheeks, she wiped some off with her finger and let it slide into her open mouth..."
    her "Looks like I've made a mess again..."
    show screen blkfade
    with d3
    call gen_chibi("sit_behind_desk")
    call her_chibi("stand","mid",flip=False)
    "The girl stood up and walked around the desk."
    hide screen blkfade
    with d3
    her "I guess that's what I get for using the silencing charm."
    "Still being unable to say anything, I just stood there, my chest moving up and down as my breathing slowed down."
    "The girl, adjusting herself and still slightly covered in semen, made her way to the door, only turning around once more..."
    her "I hope that was satisfactory..."
    her "Let it be known that Hermione never backs down on a deal..."
    call her_walk(action="leave")
    "My breathing slowly returned to normal, as the pinching feeling in my vocal cords began to fade away."
    show screen blkfade
    with d3
    call gen_chibi("sit_behind_desk")
    "After clearing my throat and composing myself. I sat back down in my chair, trying to wrap my head around what had just transpired."
    hide screen blkfade
    with d3
    "\"Hermione\" she said..."
    "It was the only clue I had gotten on whom this mysterious girl was, and I still did not know what kind of favour I had granted her..."
    "But it didn't matter, the favour I had just received in return was more than enough to make up for anything I might have assisted her with..."
    "Or at least that's what I hoped..."

    hide dark_overlay
    show screen blkfade
    with d9

    $ renpy.end_replay()
