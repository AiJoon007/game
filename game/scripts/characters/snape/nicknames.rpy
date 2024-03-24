label snape_nicknames_genie:
    menu:
        "-Mister G-":
            sna "Genie I presume?" ("snape_05")
            gen "Nah.... {i}G{/i} as in gangsta..." ("base", xpos="far_left", ypos="head")
            gen "{i}Wuddup it's mister G coming at you from the big Hog.{/i}" ("base", xpos="far_left", ypos="head")
            sna "Yeah, no... I'm not doing that." ("snape_04")
        "-Big D-":
            sna "I don't think that the real Albus Dumbledore would call himself that..." ("snape_03")
            gen "I suppose I am much greater than he is." ("base", xpos="far_left", ypos="head")
            sna "Greater than the real Albus Dumbledore?!" ("snape_25")
            sna "*Hmph*... You might be a Genie, but that is taking things too far..." ("snape_03")
        "-Master-":
            sna "I am not some common house elf..." ("snape_03")
            gen "What kind of elf are you then?" ("base", xpos="far_left", ypos="head")
            gen "A Dark elf?" ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_04")
            gen "I knew it..." ("base", xpos="far_left", ypos="head")
        "-Daddy-":
            sna "What did you just say?" ("snape_03")
            gen "(Why did I just say that?)" ("angry", xpos="far_left", ypos="head")
            menu:
                "-Say it again-":
                    gen "*Err*... Daddy?" ("base", xpos="far_left", ypos="head")
                    sna "Get the hell out of my office!" ("snape_33")
                    gen "Okay!" ("angry", xpos="far_left", ypos="head")

                    call gen_chibi("stand", xpos="400", ypos="460")
                    with d3
                    pause .3

                    #Genie leaves the office
                    call gen_walk(action="leave", speed=1.5)

                    pause 1
                    play sound "sounds/door.ogg"
                    call gen_chibi("stand", "door", "base", flip=False)
                    with d3
                    pause 0.8

                    gen "I thought this was my office." ("base", xpos="far_left", ypos="head")
                    sna "Sit the hell down in your chair and never say anything like that again!" ("snape_17")
                    gen "Yes sir!" ("angry", xpos="far_left", ypos="head")

                    call gen_walk(action="stand", xpos="400", ypos="460", speed=1.5)
                    call gen_chibi("sit_behind_desk")
                    with d3
                "-Don't-":
                    gen "Nothing. You have heard nothing." ("base", xpos="far_left", ypos="head")
                    sna "Just as I thought." ("snape_04")
        "-Sexy-":
            sna "Why on earth would I do that?" ("snape_05")
            gen "Because it's true." ("base", xpos="far_left", ypos="head")
            sna "You look like an old man." ("snape_03")
            gen "Hey, I'm only a sixtyfive thousand years old, thank you very much..." ("base", xpos="far_left", ypos="head")
            sna "I'm talking about--{w=0.4} You know what, nevermind..." ("snape_03")
        "-Lord Voldemort-":
            sna "..." ("snape_11")
            gen "No?" ("base", xpos="far_left", ypos="head")
            sna "Where did you--" ("snape_36")
            nar "Snape scratches his ass nervously."
            sna "How do you know that name?!" ("snape_36")
            gen "Alright fine... nevermind..." ("base", xpos="far_left", ypos="head")
        "-Custom Input-":
            gen "...{w=0.4} Why can't I type anything in?!" ("base", xpos="far_left", ypos="head")
            sna "What?" ("snape_05")
            gen "*Hmph*...{w=0.4} Must be a bug." ("base", xpos="far_left", ypos="head")
        "-Never mind-":
            pass

    return

label snape_nicknames:
    menu:
        "-Rus-":
            sna "What?" ("snape_03")
            gen "Rus, like short for Severus." ("base", xpos="far_left", ypos="head")
            sna "Doesn't \"Sev\" make more sense?" ("snape_05") #Lilly used to call him this
            gen "Oh yeah!" ("base", xpos="far_left", ypos="head")
            gen "So, can I call you--" ("base", xpos="far_left", ypos="head")
            sna "No." ("snape_04")
        "-Tall broody guy-":
            sna "What?" ("snape_01")
            gen "You like it?" ("base", xpos="far_left", ypos="head")
            sna "Sure." ("snape_03")
            gen "Really?" ("base", xpos="far_left", ypos="head")
            sna "No..." ("snape_04")
        "-Snake-":
            sna "..." ("snape_39")
            gen "A bit too on the nose perhaps..." ("base", xpos="far_left", ypos="head")
        "-Dungeon Dweller-":
            sna "You think you're some sort of jokester?" ("snape_43")
            gen "You can call me erection inhabitant if you like." ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_03")
        "-Anal Frickman-":
            sna "Is that supposed to be funny?" ("snape_03")
            gen "I'm sure it would be if anyone got any of my references in this universe." ("base", xpos="far_left", ypos="head")
        "-Snivellus-":
            sna "How about \"go fuck yourself\"." ("snape_04")
            gen "That's a weird nickname but sure." ("base", xpos="far_left", ypos="head")
            sna "..." ("snape_06")
        "-Master-":
            sna "Sure!" ("snape_37")
            sna "Finally I'm getting some recognition around this place..." ("snape_23")
            gen "..." ("base", xpos="far_left", ypos="head")
            sna "...{w=0.6}{nw}" ("snape_02")
            sna "...{fast} Oh, you were just doing one of your \"Hilarious\" jokes..." ("snape_01")
        "-Pantysniffer-" if states.map.snape_office.intro_e3:
            sna "I don't sniff panties!" ("snape_18")
            gen "Then what do you do with them?!" ("base", xpos="far_left", ypos="head")
            sna "I--{w=0.2} I just collect them..." ("snape_12")
            gen "Likely story..." ("base", xpos="far_left", ypos="head")
        "-Custom Input-":
            gen "...{w=0.4} Why can't I type anything in?!" ("base", xpos="far_left", ypos="head")
            sna "What?" ("snape_05")
            gen "*Hmph*...{w=0.4} Must be a bug." ("base", xpos="far_left", ypos="head")
        "-Never mind-":
            pass

    return
