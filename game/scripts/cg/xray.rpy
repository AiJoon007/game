
init python:
    renpy.register_shader("xray_shader", variables="""
        uniform float u_lod_bias;
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform sampler2D tex2;
        uniform vec2 u_pos;
        uniform float u_radius;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_600="""
        v_tex_coord = a_tex_coord;
    """, fragment_600="""
        vec4 color0 = texture2D(tex0, v_tex_coord.st, u_lod_bias);
        vec4 color1 = texture2D(tex1, v_tex_coord.st, u_lod_bias);
        vec4 mask = texture2D(tex2, v_tex_coord.st, u_lod_bias);

        float position = length(u_pos-v_tex_coord.st);
        float distance = sqrt(dot(position, position));
        float smoothing = smoothstep(u_radius+0.01, u_radius-0.1, distance);

        if ( (distance < u_radius) ) {
            vec4 masking = mix(color0, color1, mask.a);
            gl_FragColor = mix(color1, masking, smoothing);
        }
        else {
            gl_FragColor = color1;
        }
    """)

    class Xray(renpy.Displayable, NoRollback):
        nosave = [
            "child",
            "overlay",
            "mask",
        ]

        def __init__(self, child, overlay, mask=Null(), radius=0.25, tag_prefix="xray", **properties):
            super(Xray, self).__init__(**properties)

            self._child = child
            self._overlay = overlay
            self._mask = mask

            self.child = ImageReference(child) if isinstance(child, str) else child
            self.overlay = ImageReference(overlay) if isinstance(overlay, str) else overlay
            self.mask = ImageReference(mask) if isinstance(mask, str) else mask
            self.radius = radius
            self.tag_prefix = tag_prefix
            self.target = (0, 0)

        def render(self, width, height, st, at):
            child = renpy.render(self.child, width, height, st, at)
            overlay = renpy.render(self.overlay, width, height, st, at)
            mask = renpy.render(self.mask, width, height, st, at)

            rv = renpy.Render(width, height)

            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = 256.0 / (256.0 + 256.0)
            rv.operation_parameter = 256

            rv.mesh = True
            rv.add_shader("xray_shader")
            rv.add_uniform("u_pos", self.target)
            rv.add_uniform("u_radius", self.radius)
            rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(child, (0, 0))
            rv.blit(overlay, (0, 0))
            rv.blit(mask, (0, 0))

            return rv

        def per_interact(self):
            tag_prefix = self.tag_prefix
            redraw = False

            for layer in self.nosave:
                child = getattr(self, layer)

                if isinstance(child, ImageReference):
                    name = getattr(self, "_{}".format(layer))
                    attributes = renpy.get_attributes(name) or renpy.get_attributes("{}_{}".format(tag_prefix, layer))

                    if attributes:
                        attributes = " ".join(attributes)
                        child = ImageReference("{} {}".format(name, attributes))
                    elif child.name != name:
                        child = ImageReference(name)
                    else:
                        continue

                    setattr(self, layer, child)
                    redraw = True

            if redraw:
                renpy.redraw(self, 0)

        def event(self, ev, x, y, st):

            if not pygame.mouse.get_focused():
                return

            # if not ev.type == pygame.MOUSEMOTION:
            #     returnO

            xtarget, ytarget = self.target

            if (x != xtarget) or (y != ytarget):
                self.target = (float(x) / config.screen_width, float(y) / config.screen_height)
                renpy.redraw(self, 0)

        def visit(self):
            return [ self.child, self.overlay, self.mask ]
