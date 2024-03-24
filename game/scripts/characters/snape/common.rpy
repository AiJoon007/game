label update_snape:
    $ states.sna.image.xzoom = 1
    return

define character.snape_say = Character("Severus Snape", show_icon="snape")

init python:
    def sna(what, face=None, xpos=None, ypos=None, pos=None, flip=None, trans=None, animation=False, wand=False, **kwargs):
        redraw = False
        tag = "snape_main"
        layer = "screens"
        #showing = renpy.showing(name=tag, layer=layer)

        if xpos != None or ypos != None:
            xpos = states.sna.image.xpos if xpos == None else sprite_pos.get("x").get(xpos, xpos)
            ypos = states.sna.image.ypos if ypos == None else sprite_pos.get("y").get(ypos, ypos)
            states.sna.image.xpos = xpos
            states.sna.image.ypos = ypos
            redraw = True

        head_ypos = sprite_pos.get("y").get("head")
        head_only = states.sna.image.ypos == head_ypos

        # The easiest way to fix image positions for Snape is to use offsets.
        # It's not ideal, but it's better than having to change all calls manually.
        if states.sna.image.ypos in ("head", head_ypos):
            xoffset = -25
            yoffset = 150
        else:
            xoffset = -50
            yoffset = 0

        if face:
            states.sna.image.face = face
            redraw = True

        if animation != False:
            states.sna.image.animation = animation
            redraw = True

        if flip != None:
            states.sna.image.xzoom = -1 if flip else 1
            redraw = True

        if redraw:
            base_transform = doll_transform((states.sna.image.xpos + xoffset, states.sna.image.ypos + yoffset), states.sna.image.zoom, states.sna.image.xzoom)
            sprite = Image("characters/snape/main/"+states.sna.image.face+".webp")

            if wand:
                sprite = Fixed(sprite, "characters/snape/main/wand.webp")

            at_list = [base_transform]

            if animation:
                at_list.append(states.sna.image.animation)

            renpy.show(name=tag, at_list=at_list, layer=layer, what=sprite, zorder=states.sna.image.zorder)

            if not renpy.in_rollback():
                if trans:
                    renpy.with_statement(trans)
                else:
                    renpy.with_statement(d2)

        if what:
            character.snape_say(what, **kwargs)

        if head_only:
            renpy.hide(name=tag, layer=layer)
