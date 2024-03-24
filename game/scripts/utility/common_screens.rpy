screen blkfade():
    tag blkfade
    zorder 25
    add Color("#000")

screen whitefade():
    tag whitefade
    zorder 25
    add Color("#fff")

screen blktone(alpha=0.5):
    tag blktone
    zorder 14
    add Color("#000", alpha=alpha)

screen white():
    zorder 20
    add Color("#fff")

screen bld1():
    zorder 10
    tag bld1

    add "interface/bld.webp"

screen bld2():
    zorder 10
    add Transform("interface/bld.webp", yzoom=-1.0)

screen notes():
    add "notes" xpos 320+140 ypos 330
    zorder 1

screen clothing_unlock(item):
    zorder 30
    modal True

    use notes
    on "show" action Play("sound", "sounds/win2.ogg")

    if isinstance(item, DollCloth):
        add item.icon align (0.5, 0.5) zoom 0.5
    elif isinstance(item, DollOutfit):
        add item.image align (0.5, 0.0) yoffset -50 zoom 0.4

screen invisible_button(action=NullAction(), keysym=None, alternate=None):

    # Note: Actions cannot be passed as transclude, separate parameter is required.
    button style "empty":
        keyboard_focus False
        action action
        keysym keysym
        alternate alternate
        transclude
