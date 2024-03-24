
# Transforms used by the chibi class or chibi images

transform combine_transforms(one, two):
  one
  two

transform chibi_base(position, flip, scale):
    pos position
    anchor (0.0, 1.0)
    xzoom (-1 if flip else 1)
    zoom (0.5 * scale)

transform chibi_walk(path, times):
    function renpy.partial(chibi_path_move, path, times, _warper.linear)

transform chibi_fly:
    block:
        yoffset absolute(0)
        ease 2 yoffset absolute(-10)
        ease 2 yoffset absolute(10)
        ease 2 yoffset absolute(0)
        repeat

transform chibi_fly_move(path, times):
    parallel:
        function renpy.partial(chibi_path_move, path, times, _warper.ease_quad)

    parallel:
        yoffset absolute(0)
        ease 2 yoffset absolute(-10)
        ease 2 yoffset absolute(10)
        ease 2 yoffset absolute(0)
        repeat

transform chibi_wand:
    xoffset -72 # Note: Offset seems to be applied after zoom

transform chibi_lie:
    rotate 90
    transform_anchor True
    anchor (0.5, 0.65)
    xzoom 1 # Negate flip

transform chibi_float_move(path, times):
    combine_transforms(chibi_lie, chibi_fly_move(path, times))

transform random_blink(close_image, open_image=Null()):
    close_image
    pause .08
    open_image
    choice:
        pause 6
    choice:
        pause 3
    choice:
        # Double blink
        close_image
        pause .08
        open_image
        pause 5
    repeat

transform emote_effect():
    alpha 0.0
    on show:
        zoom 0.8
        linear .2 zoom 1.0 alpha 1.0
    on hide:
        linear .2 zoom 1.2 alpha 0.0

init python:
    def chibi_path_move(path, times, warp, trans, st, at):
        if st >= sum(times):
            trans.pos = path[-1]
            return None

        it = 0
        seg = 0
        for i in range(len(times)):
            if it + times[i] > st:
                seg = i
                break
            it += times[i]

        segt = (st - it) / times[seg]
        segt = warp(segt)
        trans.pos = renpy.atl.interpolate(segt, path[seg], path[seg + 1], renpy.atl.PROPERTIES["pos"])
        return 0
