
init python:
    def cg_pov_switch(tag1="cg", tag2="cg2", layer=None, controller="cho_dual_cg"):
        layer = layer or config.default_tag_layer
        zpairs = renpy.get_zorder_list(layer)
        zdict = {key: value for key, value in zpairs}

        z1 = zdict.get(tag1, None)
        z2 = zdict.get(tag2, None)

        if None in (z1, z2):
            return

        renpy.change_zorder(layer, tag1, z2)
        renpy.change_zorder(layer, tag2, z1)

        focused = tag1 if z1 > z2 else tag2

        renpy.show_screen(controller, focused)

screen cho_dual_cg(focused, _layer="screens", bubble="cho_handjob_bubble", mask="cho_handjob_bubble_mask"):
    tag switcher
    zorder 300

    $ d = renpy.display.core.displayable_by_tag(_layer, focused) # Updates once per interaction
    $ flip = (-1 if focused == "cg" else 1)

    if d:
        $ btn = AlphaMask(Fixed(Transform(d, align=( (1.0, 0.05) if flip else (0.0, 0.05) ), zoom=0.5, xzoom=flip)), Transform(mask, zoom=0.25))
        $ btn = Fixed(Transform(bubble, zoom=0.25), btn)
        
        imagebutton:
            idle Transform(btn, alpha=0.75)
            hover Transform(btn, alpha=1.0)
            action Function(cg_pov_switch, layer=_layer)
            focus_mask True
            at transform:
                xzoom flip