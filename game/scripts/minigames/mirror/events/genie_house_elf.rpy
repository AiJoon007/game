
# Mirror story: The genie, the desk and the door
label genie_house_elf:

    # Setup
    $ game.daytime = True
    $ game.weather = "clear"
    stop weather
    call room("main_room")
    stop music fadeout 1
    show screen blkfade
    with d5

    centered "{size=+7}{color=#cbcbcb}The Genie, the Desk and the Door{/color}{/size}" #Play on "The Lion, the Witch and the Wardrobe"

    hide screen blkfade
    with d5

    nar "This story takes place after the introduction of Snape and before meeting Hermione."
    gen "(How does that door work?)" ("base", xpos="far_left", ypos="head")
    nar "The genie thought."
    gen "(How do the people know I've summoned them? I don't have a secretary... that I know of, anyway.)" ("base", xpos="far_left", ypos="head")
    gen "Have they been keeping a secretary from me? I should ask Sn..." ("base", xpos="far_left", ypos="head")
    nar "Snape then opened the door, his pointy nose protruding under his silky hair."

    call sna_walk(action="enter", xpos="mid", ypos="base")

    sna "You called?" ("snape_23", xpos="base", ypos="base")
    nar "Snape said with a smirk, doing his best to hide his amusement."
    gen "How did you, how do you..." ("angry", xpos="far_left", ypos="head")
    gen "This door, how does it work?" ("base", xpos="far_left", ypos="head")
    nar "The genie said, now even more frustrated."
    nar "The genie wasn't used to this... this unfamiliar magic."
    nar "He was used to knowing the ins and outs of the universe. But this world, it was too alien to him..."
    nar "At least he knew things about aliens..."
    sna "Well, you're the headmaster are you not?" ("snape_06", xpos="base", ypos="base")
    nar "Snape said as if that meant anything."
    nar "A look of confusion spread across the genie's face, which only made Snape smirk even more."
    nar "He then composed himself after seeing this unusual expression on the headmaster's face."
    sna "I keep forgetting that you don't know these things." ("snape_01", xpos="base", ypos="base")
    sna "students learn it on day one." ("snape_01", xpos="base", ypos="base")
    sna "The headmaster is in control of the school and its inhabitants." ("snape_24", xpos="base", ypos="base")
    nar "Snape said in a matter of fact sort of way."
    gen "I know that, we have schools in my world too." ("base", xpos="far_left", ypos="head")
    gen "But generally, we don't wave wooden sticks around yelling random words." ("base", xpos="far_left", ypos="head")
    nar "Snape flinched, as if the notion of magic consisting of waving a wand and yelling random words was utterly absurd."
    sna "No. You're literally in control of the school... look." ("snape_08", xpos="base", ypos="base")
    nar "Snape said, pulling his wand out and waving it."

    sna "Revelio!" ("snape_01", xpos="base", ypos="base")
    hide snape_main
    hide screen bld1
    nar "After a flash of light and a small pop, a house elf appeared in the corner of the room."
    helf "..."
    gen "What the hell is that?" ("open", xpos="far_left", ypos="head")
    nar "The genie said, jumping onto the desk as if things appearing out of thin air was new to him."

    sna "That... is a house elf." ("snape_01", xpos="base", ypos="base")
    gen "A house... elf?" ("base", xpos="far_left", ypos="head")
    gen "Is that like Santa's elves?" ("smile", xpos="far_left", ypos="head")
    nar "The genie said, now climbing down to sit on his chair."
    sna "Sort of, they don't get paid, so they do have that in common..." ("snape_05", xpos="base", ypos="base")
    nar "Snape muttered under his breath..."
    sna "The houses elves here can send us messages, so we can go where we're needed." ("snape_05", xpos="base", ypos="base")
    sna "He just sits here invisible during the day and cleans and eats at night." ("snape_01", xpos="base", ypos="base")
    gen "The house elf cleans?" ("base", xpos="far_left", ypos="head")
    gen "I thought I had some sort of magic self-cleaning desk..." ("base", xpos="far_left", ypos="head")
    nar "The genie said sheepishly."
    hide snape_main
    hide screen bld1
    helf "No sir..."
    nar "Said the elf, trying its hardest to bite his tongue, but failing."
    helf "I see it all, I clean it all... every... last... bit of it."
    sna "..." ("snape_08", xpos="base", ypos="base")

    nar "After a few moments, Snape turned around, started walking towards the door and said."
    sna "If that is all, I'll be in the dungeons." ("snape_01", xpos="base", ypos="base")
    sna "I've been working on a new cleaning solution." ("snape_01", xpos="base", ypos="base")
    sna "It might come in handy sooner than I thought." ("snape_02", xpos="base", ypos="base")

    call sna_walk(action="leave")

    nar "The door shut and silence spread across the room, only interrupted after a few minutes by the house elf."
    helf "So, should I turn invisible again sir?"
    gen "Yes... Yes that would be for the best." ("base", xpos="far_left", ypos="head")

    call blkfade

    centered "{size=+7}{color=#cbcbcb}The end{/color}{/size}"

    $ renpy.end_replay()
