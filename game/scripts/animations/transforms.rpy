transform sepia(strength=1.0, tint='#ffeec2', desat=(0.2126, 0.7152, 0.0722), brightness=0.0):
    matrixcolor TintMatrix(tint) * SaturationMatrix(1.0-strength, desat) * BrightnessMatrix(brightness)

transform move_in(x, t):
    xpos x
    linear t xpos 0
    pause t

transform move_fade:
    on show, appear, start:
        alpha 0.0
        xoffset 200
        easein_back 1.0 alpha 1.0 xoffset absolute(0)

    on hide:
        alpha 1.0
        xoffset 0
        easeout_back 1.0 alpha 0.0 xoffset absolute(200)

transform fade_show(t):
    alpha 0
    on show:
        linear t alpha 1

transform fade_show_hide(t):
    alpha 0
    linear t alpha 1
    on hide:
        linear t alpha 0

transform fade_hide(t):
    on hide:
        linear t alpha 0.0

transform blink:
    on show:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat

transform blink_repeat:
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat

transform bob(t=1):
    on show, appear, start:
        yoffset absolute(0)
        ease t yoffset absolute(10)
        ease t yoffset absolute(0)
        repeat

transform doll_blink(normal, blink):
    events False

    normal

    choice:
        pause 4
    choice:
        pause 3
    choice:
        pause 2

    choice:
        blink
        pause 0.1
        normal
        pause 0.1
        blink
    choice:
        blink

    pause 0.1
    repeat

transform pulse:
    on show:
        xzoom 1.0
        yzoom 1.0
        linear 0.8 xzoom 1.2 yzoom 1.2
        linear 0.8 xzoom 1.0 yzoom 1.0
        repeat

transform move_to(start_x=0, start_y=0, target_x=0, target_y=0, duration=1.0):
    on show:
        xpos start_x
        ypos start_y
        linear duration xpos target_x ypos target_y

transform main_sprite_position(x, y, flip, scale):
    xpos x
    ypos y
    xzoom flip
    zoom (1.0/scale)

transform random_rotation(a=-45, b=45):
    rotate random.randint(a, b)

transform pulse_hover(t=2.0, strength=0.2, pause=0.0):
    matrixcolor BrightnessMatrix(value=0.0)

    on start:
        linear t/2 matrixcolor BrightnessMatrix(value=strength)
        linear t/2 matrixcolor BrightnessMatrix(value=0.0)
        pause pause
        repeat

transform gui_animation:
    nearest True
    events False

    on show:
        zoom 0
        alpha 0
        xoffset config.screen_width
        easein_cubic 0.3 zoom 1.0 alpha 1.0 xoffset 0
        events True
        nearest False

    on hide:
        events False
        nearest True
        easeout_cubic 0.3 zoom 0.0 alpha 0.0 xoffset config.screen_width

transform shake:
    events False
    function shake_func

transform shake_xlinear(speed=1.0):
    xoffset 1
    linear 0.1/speed xoffset -2
    linear 0.1/speed xoffset 2
    repeat

init python:
    def shake_func(trans, st, at):
        trans.xoffset = renpy.random.randint(-2, 2)
        trans.yoffset = renpy.random.randint(-2, 2)
        return clamp(1.0 - st, 0.05, 1.0)

