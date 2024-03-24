screen meter(fill=100, caption=None):
    tag meter
    zorder 30

    default fill = fill
    style_prefix "meter"

    frame:
        background gui.format("interface/meter/{}/meter.webp")
        foreground "interface/meter/glass.webp"

        vbar value AnimatedValue(fill, range=100, delay=0.5)
        if caption:
            text caption

style meter_frame is empty:
    xysize (60, 500)
    align (0.05, 0.5)

style meter_vbar:
    top_bar None
    thumb None
    insensitive_thumb None
    bottom_bar "interface/meter/fill.webp"
    xsize 60

style meter_text:
    size 8
    color "#fff"
    vertical True
    align (0.0, 0.5)
    xoffset 5

screen swear_bubble(type):
    tag bubble
    zorder 30

    add "interface/meter/bubble/"+str(type)+".webp" ypos 100 xpos 100
    timer 1.0 action Hide("swear_bubble")
