
label snape_picture:

    if game.daytime:

        if not states.map.snape_office.picture_examined:
            $ states.map.snape_office.picture_examined = True
            $ snape_office_picture_OBJ.set_image("snape_office_picture")

            call gen_chibi("stand_alt", xpos="painting", ypos="painting")
            with d5

            gen "Is that a self-portrait?" ("base", xpos="far_left", ypos="head")
            sna "Fuck yeah it is!"

            #Genie turns around towards the door
            call gen_chibi(flip=False)
            play sound "sounds/malegasp.ogg" volume 0.40

            gen "Severus! I can explain..." ("angry", xpos="far_left", ypos="head")
            gen "Wait..." ("base", xpos="far_left", ypos="head")
            gen "Are you invisible?" ("base", xpos="far_left", ypos="head")
            "Severus Snape" "Of course not! I'm here you blithering buffoon!"
            gen "Where?" ("base", xpos="far_left", ypos="head")
            "Severus Snape" "On the wall! Where else would I be, you dimwit?"
            gen "On the--" ("base", xpos="far_left", ypos="head")

            #Genie turns around to the Painting
            call gen_chibi(flip=True)
            with d3
            pause .2
            call gen_chibi("stand_alt")
            with d3

            gen "Oh, of course..." ("base", xpos="far_left", ypos="head")
            gen "You're another one of those weirdo paintings..." ("base", xpos="far_left", ypos="head")
            "The Painting" "Who are you calling weird... You old goat!"
            gen "And seemingly an asshole as well." ("base", xpos="far_left", ypos="head")
            "The Painting" "Hey, I am but an artist's interpretation. That's not my fault!"
            gen "Right..." ("base", xpos="far_left", ypos="head")
            gen "Could you tell me if there's anything useful in this office?" ("base", xpos="far_left", ypos="head")
            "The Painting" "Fuck no!"
            gen "Didn't think so..." ("base", xpos="far_left", ypos="head")

            call gen_chibi("stand", xpos="door", ypos="base", flip=True)
            with d5

            jump quests

        elif not states.map.snape_office.intro_e2:
            gen "(I don't have anything more to say to this asshole.)" ("base", xpos="far_left", ypos="head")
        else:
            random:
                block:
                    gen "So... What does Snape do on his free time?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "Crossword puzzles."
                    gen "Really?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "Of course not, what are you some kind of idiot?"
                block:
                    gen "How many girls has Snape brought in here?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "More than I could count!"
                    gen "Can paintings count?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "Wouldn't you like to know!"
                block:
                    gen "I thought Snape would be more organized than this..." ("base", xpos="far_left", ypos="head")
                    "The Painting" "Those panties are perfectly organized and labelled I'll have you know!"
                    gen "I was talking about the shelves..." ("base", xpos="far_left", ypos="head")
                block:
                    gen "The \"S\" on the chair stands for \"Slytherin\", right?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "No..."
                    gen "Don't tell me it--" ("base", xpos="far_left", ypos="head")
                    "The Painting" "It stands for, \"Stop asking stupid questions\"."
                    gen "I don't think that's how it works..." ("base", xpos="far_left", ypos="head")
                    "The Painting" "Pretty sure it does."
                block:
                    gen "So, what is a \"basi-lick\" anyway?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "It's this creature that slathers your--"
                    gen "Stop!" ("angry", xpos="far_left", ypos="head")
                    gen "Forget I asked!" ("angry", xpos="far_left", ypos="head")
                block:
                    gen "How come Snape has his office in the Dungeon?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "He's a vampire!"
                    gen "I knew it!" ("base", xpos="far_left", ypos="head")
                    "The Painting" "..."
                    gen "Oh, you're just messing with me..." ("base", xpos="far_left", ypos="head")
                block:
                    gen "Where does Snape store his ingredients?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "There's a compartment behind me..."
                    gen "Really?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "Just touch my hairy nut-sack and it will open for you."
                    gen "... {w=0.4} I think I'll get my own ingredients for now..." ("base", xpos="far_left", ypos="head")
                block:
                    gen "So, what's it like being a painting anyway?" ("base", xpos="far_left", ypos="head")
                    "The Painting" "You're asking what it's like to be stuck in the same small space that the artist decided to draw for you?"
                    "The Painting" "For years?"
                    gen "{size=-3}Try centuries why don't you...{/size}" ("base", xpos="far_left", ypos="head")
                    "The Painting" "What was that?"
                    gen "Never mind..." ("base", xpos="far_left", ypos="head")
    else:
        gen "(I don't think Snape would appreciate me shit-talking to his portrait...)" ("base", xpos="far_left", ypos="head")

    jump snape_office_menu
