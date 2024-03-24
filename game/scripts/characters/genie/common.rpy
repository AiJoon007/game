
define character.genie_say = Character("Genie", show_icon="genie")

init python:
    def gen(what, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, **kwargs):
        redraw = False
        tag = "genie_main"
        layer = "screens"
        side = None
        #showing = renpy.showing(name=tag, layer=layer)

        if xpos != None or ypos != None:
            xpos = states.gen.image.xpos if xpos == None else sprite_pos.get("x").get(xpos, xpos)
            ypos = states.gen.image.ypos if ypos == None else sprite_pos.get("y").get(ypos, ypos)
            states.gen.image.xpos = xpos
            states.gen.image.ypos = ypos

        head_ypos = sprite_pos.get("y").get("head")
        far_xpos = sprite_pos.get("x").get("far_left")

        if states.gen.image.ypos in ("head", head_ypos):
            states.gen.image.offset = (-25, 630)
        else:
            states.gen.image.offset = (0, 600)

        if face:
            variant = "genie {}".format(face)
            renpy.set_tag_attributes(variant)
            side = "genie"

            at_list = []

            if animation:
                at_list.append(animation)

            if renpy.showing("genie", layer=layer):
                renpy.show(variant, layer=layer, tag="genie", at_list=at_list)

        if flip != None:
            states.gen.image.xzoom = -1 if flip else 1

        if what:
            character.genie_say(what, image=side, **kwargs)

label update_genie:

    $ states.gen.image.xzoom = 1
    $ states.gen.image.zorder = 15
    call gen_chibi("sit_behind_desk")

    return
