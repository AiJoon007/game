
# Legacy styles (still in use)

style yesno_button:
    size_group "yesno"

style yesno_label_text:
    text_align 0.5
    layout "subtitle"

style soundtest_button:
    xalign 1.0

style gm_nav_button:
    size_group "gm_nav"

style mm_button:
    size_group "mm"

# Common control styles
# style default:
#     font "fonts/CREABBB.TTF"
#     size 16
#     color "#402313"
#     outline_scaling "linear"

# style button:
#     activate_sound "sounds/click3.ogg"
#     background "#5d5151e6"
#     hover_background "#897e75"
#     insensitive_background "#463b3be6"
#     selected_background "#766a6ae6"
#     selected_hover_background "#897e75"
#     #padding (5, 5, 5, 5)

# style button_text:
#     color "#9b8d84"
#     hover_color "#fff"
#     insensitive_color "#50443c"
#     selected_color "#eedfd5"
#     selected_hover_color "#fff"
#     outlines [(1, "#00000080", 1, 0)]

# style input:
#     color "#5c321b"

# # Day/night button styles
# style day_button:
#     background "#ac8d5ae6"
#     hover_background "#97681f"
#     insensitive_background "#d1a02eb3"
#     padding (5, 5, 5, 5)

# style night_button:
#     background "#5d5151e6"
#     hover_background "#897e75"
#     insensitive_background "#9e8449"
#     padding (5, 5, 5, 5)

# style day_button_text is default: # Don't inherit from button_text
#     color "#f9d592"
#     outlines [(1, "#00000080", 1, 0)]
#     hover_color "#fff"
#     insensitive_color "#50443c"
#     selected_color "#eedfd5"
#     selected_hover_color "#fff"

# style night_button_text is default: # Don't inherit from button_text
#     color "#9b8d84"
#     outlines [(1, "#00000080", 1, 0)]
#     hover_color "#fff"
#     insensitive_color "#50443c"
#     selected_color "#eedfd5"
#     selected_hover_color "#fff"

style dropdown:
    ysize 24
    focus_mask None

style light_dropdown:
    insensitive_background "light_check_none"
    selected_background "light_check_true"
    background "light_check_false"

style dark_dropdown:
    insensitive_background "dark_check_none"
    selected_background "dark_check_true"
    background "dark_check_false"

style dropdown_text:
    yalign 0.5
    first_indent 26
    size 12
    hover_color "#FFF"
    outlines [(1, "#00000080", 1, 0)]

style light_dropdown_text:
    color "#f9d592"
    insensitive_color "#ae9566"

style dark_dropdown_text:
    color "#9b8d84"
    insensitive_color "#6c625c"

# Hyperlinks
style hyperlink_text:
    underline False
    hover_color "#4cf"
    idle_color "#08f"
