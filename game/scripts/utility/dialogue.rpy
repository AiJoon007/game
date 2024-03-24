
# Handling of doll transitions in dialogue

define sprite_pos = {
    "x": {
        "base": 640,
        "default": 640,
        "far_right": 650,
        "mid": 300,
        "left": 200,
        "far_left": 25,
        "right": 400,
        "wardrobe": 540,
        "close": 540
    },

    "y": {
        "base": 0,
        "default": 0,
        "head": 200,
        "low": 170
    }
}

init python:

    def replace_text(s):
        s = s.replace('--', u'\u2014') # em dash
        return s

    config.replace_text = replace_text
