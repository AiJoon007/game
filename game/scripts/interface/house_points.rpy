### House-Points ###

label points_changes: # Gets called every day/night.

    python:
        progress_factor = max(1, int(math.log(game.day) * 5))

        # Bonuses based on Tonks and Snape friendship stat
        # Tonks' is lower since you can do events with her directly to increase points.
        bonus_g = states.her.tier # Passive bonus
        bonus_h = int((states.ton.level/100.0) * (progress_factor*0.7))
        bonus_s = int((states.sna.level/100.0) * progress_factor*0.7)
        bonus_r = states.cho.tier + states.lun.tier # Passive bonus

        leader = max(hufflepuff, ravenclaw, slytherin, gryffindor)

        difference_factor_g = min(leader, round((progress_factor + bonus_g) * max(hufflepuff, ravenclaw, slytherin)/float(gryffindor)))
        difference_factor_h = min(leader, round((progress_factor + bonus_h) * max(gryffindor, ravenclaw, slytherin)/float(hufflepuff)))
        difference_factor_r = min(leader, round((progress_factor + bonus_r) * max(gryffindor, hufflepuff, slytherin)/float(ravenclaw)))
        difference_factor_s = min(leader, round((progress_factor + bonus_s) * max(hufflepuff, ravenclaw, gryffindor)/float(slytherin)))

        points_g = renpy.random.randint(difference_factor_g//2, difference_factor_g)
        points_h = renpy.random.randint(difference_factor_h//2, difference_factor_h)
        points_r = renpy.random.randint(difference_factor_r//2, difference_factor_r)
        points_s = renpy.random.randint(difference_factor_s//2, difference_factor_s)

        gryffindor += points_g
        hufflepuff += points_h
        ravenclaw += points_r
        slytherin += points_s

    hide screen points_changes
    show screen points_changes(points_s, points_g, points_r, points_h)
    return

screen points_changes(points_s, points_g, points_r, points_h):
    tag points_changes
    zorder 35

    hbox:
        spacing 15
        align (0.5, 0.1)
        at transform:
            on start:
               alpha 0.0
            on show:
                yoffset 0
                alpha 1.0
                easein 3.0 yoffset -50 alpha 0.0

        text "+[points_s]" outlines [(1, "#000000BF", 1, 0)] size 24 color "#3A734B"
        text "+[points_g]" outlines [(1, "#000000BF", 1, 0)] size 24 color "#A74D2A"
        text "+[points_r]" outlines [(1, "#000000BF", 1, 0)] size 24 color "#5974C2"
        text "+[points_h]" outlines [(1, "#000000BF", 1, 0)] size 24 color "#FBC60A"

    timer 3.0 action Hide("points_changes")


