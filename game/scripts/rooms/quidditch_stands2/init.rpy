
# Quidditch stands

default quidditch_stands2 = {
    "weather": "sun_high",
    "crowd": [],
    "crowd_react": [None, None, None],
}

label quidditch_stands2(hidden=False, reset=False, **kwargs):
    if reset:
        $ reset_variables("quidditch_stands2")
    $ quidditch_stands2.update(kwargs)
    if not hidden:
        show screen quidditch_stands_back2(**quidditch_stands2)
        show screen quidditch_stands_front2(**quidditch_stands2)
    return

screen quidditch_stands_back2(weather, crowd=[], crowd_react=[None, None, None], **kwargs):
    zorder 0

    add "images/rooms/quidditch_stands2/bg_{}.webp".format(weather) zoom 0.5

    for c in set(crowd):
        add "images/rooms/quidditch_stands2/crowd_{}.webp".format(c) zoom 0.5

    add crowd_react[0] pos (570, 140)
    add crowd_react[1] pos (720, 90)
    add crowd_react[2] pos (960, 60)

screen quidditch_stands_front2(weather, **kwargs):
    zorder 8

    add "images/rooms/quidditch_stands2/fg_{}.webp".format(weather) zoom 0.5
