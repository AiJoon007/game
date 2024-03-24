default _tooltip = None

screen tooltip():
    layer "interface"
    tag tooltip
    zorder 5
    style_prefix "tooltip"

    if settings.get("tooltip") and getattr(store, "_tooltip", None):
        window:
            id "tooltip"
            at tooltip_follow
            text "[_tooltip!i]"

style tooltip_window is empty:
    background "#00000080"
    padding (18, 12)
    xmaximum 300

style tooltip_text is default:
    color "#fff"
    size 10
    outlines [(1, "#00000080", 1, 0)]

transform tooltip_follow:
    events False
    function tooltip_func

init python:

    def tooltip_func(trans, st, at):
        x, y = renpy.get_mouse_pos()

        if trans.pos is not (x, y):
            cw, ch = trans.child.window_size

            xanchor = 1.0 if (x + int(cw)) > (config.screen_width) else 0.0
            yanchor = 1.0 if (y + int(ch)) > (config.screen_height) else 0.0

            xoffset = 18 if xanchor else 0
            yoffset = 24 if yanchor else 0
            trans.pos = (x, y)
            trans.anchor = (xanchor, yanchor)
            trans.offset = (xoffset, yoffset)

            return 0

    if not renpy.android:

        config.always_shown_screens.append("tooltip")
        config.per_frame_screens.append("tooltip")
