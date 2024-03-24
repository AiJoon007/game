init python:

    def generate_puzzle(grid, difficulty, blank):
        tiles = grid*grid
        difficulty = difficulty * tiles

        puzzle = list(range(tiles))
        renpy.random.shuffle(puzzle)

        def is_valid():
            inversions = 0

            for x in range(tiles):
                for y in range(x+1, tiles):
                    if not (puzzle[x] == blank or puzzle[y] == blank) and puzzle[x] > puzzle[y]:
                        inversions += 1

            # If the grid width is odd, then every solvable state has an even number of inversions.
            # If the grid width is even, then every solvable state has:
            #       an even number of inversions if the blank is on an odd numbered row counting from the bottom OR
            #       an odd number of inversions if the blank is on an even numbered row counting from the bottom

            if (grid % 2 == 1):
                is_solvable = (inversions % 2 == 0)
            else:
                blank_row = grid - (puzzle.index(blank) // grid)
                is_solvable = (inversions % 2 != blank_row % 2)

            too_difficult = (inversions <= difficulty)
            return (is_solvable and not too_difficult)

        while not is_valid():
            renpy.random.shuffle(puzzle)

        return puzzle

screen puzzle_minigame():
    tag puzzle
    zorder 30

    default tries = 0
    default tiles = generate_puzzle(grid=4, difficulty=game.difficulty, blank=15)
    default hint = False
    $ score = 0

    add "gui_fade"
    use close_button()
    use meter(fill=100-tries)

    frame:
        align (0.5, 0.5)
        background Transform("interface/puzzle/background.webp", align=(0.5, 0.5))

        grid 4 4:
            for i, tile in enumerate(tiles):
                $ img = "interface/puzzle/{}.webp".format(tile)
                $ empty = tiles.index(15)
                $ is_valid = (i in (empty-1, empty+1, empty-4, empty+4)
                                and not ( (empty % 4 == 3) and (i % 4 == 0) )
                                and not ( (empty % 4 == 0) and (i % 4 == 3) ) )
                $ action = None
                $ hover = None

                if i is empty:
                    $ idle = Null()
                elif not is_valid:
                    $ idle = img
                else:
                    $ action = [SetScreenVariable("tries", tries+1), Function(list_swap_values, tiles, empty, i)]
                    $ idle = At(img, pulse_hover(pause=3.0, strength=0.075))
                    $ hover = image_hover(idle)

                if i == tile:
                    $ score += 1

                imagebutton:
                    xysize (94, 94)
                    idle idle
                    hover hover
                    action action
    if hint:
        button:
            style "empty"
            align (0.5, 0.5)
            background Transform("interface/puzzle/background.webp", align=(0.5, 0.5))
            add "interface/puzzle/puzzle.webp"
            action NullAction()

    if score >= 15:
        timer 0.1 action Return(True)

    vbox:
        yanchor 0.0
        align (0.5, 0.85)
        textbutton "-Hint-" xalign 0.5 action ToggleScreenVariable("hint", True, False)
        if tries >= 75:
            textbutton "-Force it open-" xalign 0.5 action Return(False) at pulse_hover
        if config.developer:
            textbutton "-Solve it-" xalign 0.5 action SetScreenVariable("tiles", list(range(16)))

label puzzle_minigame:
    call screen puzzle_minigame()
    $ renpy.block_rollback()

    if _return == True:
        gen "Finally..." ("base", xpos="far_left", ypos="head")
        gen "What is this?" ("base", xpos="far_left", ypos="head")
        gen "Sweet, phoenix tears! Down the hatch we go." ("base", xpos="far_left", ypos="head")
        play sound "sounds/pop03.ogg"
        play sound2 "sounds/gulp.ogg"
        pause 1
        play sound "sounds/gulp.ogg"
        gen "...." ("base", xpos="far_left", ypos="head")
        gen "I feel no difference..." ("base", xpos="far_left", ypos="head")
        $ achievements.unlock("puzzle")
    elif _return == False:
        gen "Fuck it..." ("angry", xpos="far_left", ypos="head")
        play sound "sounds/door_down.ogg"
        with hpunch
        "{size=32}*Smash*{/size}"
        play sound "sounds/glass_shatter.ogg"
        gen "A broken bottle..." ("base", xpos="far_left", ypos="head")
        gen "Oh well, too late now. Back to my usual--" ("base", xpos="far_left", ypos="head")
    else: # Closed
        gen "(Maybe next time...)" ("base", xpos="far_left", ypos="head")
        jump main_room_menu

    gen "Hold on a second, there's a book in here..." ("base", xpos="far_left", ypos="head")
    gen "Seems to be some sort of notebook, I'll skim through it..." ("base", xpos="far_left", ypos="head")

    call book_start

    gen "\"My dear phoenix has been losing his feathers lately, I think it's time soon\"..." ("base", xpos="far_left", ypos="head")
    gen "(Time for what?)" ("base", xpos="far_left", ypos="head")
    gen "\"That Potter boy is mighty cute, looks just like his father\"..." ("base", xpos="far_left", ypos="head")
    gen "(Well, well...)" ("grin", xpos="far_left", ypos="head")
    gen "\"Severus gave me a weird look today, I wonder what he thinks about my\"..." ("base", xpos="far_left", ypos="head")
    gen "(This is all trash...)" ("angry", xpos="far_left", ypos="head")
    gen "(Wait a minute... this seems interesting.)" ("base", xpos="far_left", ypos="head")
    gen "\"I was walking around in the seventh floor corridor looking for a bathroom\"..." ("base", xpos="far_left", ypos="head")
    gen "\"Whilst searching, a room that I had never seen before appeared, filled with chamber pots... But when I returned later, it was gone\"." ("base", xpos="far_left", ypos="head")

    call book_end

    gen "(I've seen enough magic to know where this is going... I should investigate that corridor on the seventh floor.)" ("base", xpos="far_left", ypos="head")
    call give_reward("You've unlocked something on the 7th floor, check your map to get there.","/images/rooms/room_of_requirement/mirror.webp")

    if states.cardgame.unlocked:
        gen "What's this?" ("base", xpos="far_left", ypos="head")
        call give_reward("You have found a card at the bottom of the box!", "images/cardgame/t1/other/elf_v1.webp")
    $ unlocked_cards += [card_item_elf]
    $ states.map.seventh_floor.unlocked = True
    $ puzzle_box_ITEM.owned = 0
    $ puzzle_box_ITEM.used = True

    $ chair_OBJ.hidden = False

    if game.daytime:
        jump night_start
    else:
        jump day_start
