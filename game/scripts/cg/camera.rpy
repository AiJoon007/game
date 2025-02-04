
transform CGCamera(zoom, endzoom, pos, endpos, rotate, endrotate, t):
    subpixel True

    offset pos
    zoom zoom
    rotate rotate
    parallel:
        ease_quad t zoom endzoom
    parallel:
        ease_quad t xoffset endpos[0] yoffset endpos[1]
    parallel:
        linear t rotate endrotate

init python:

    class CGController(object):
        default_timer = 1.0

        def __init__(self, min_zoom=0.1, max_zoom=5.0):
            self.imagepath = None
            self.scale = 1.0

            self.last_type = 0
            self.type = 0 # 0 - image, 1 - Movie

            self.last_image = None
            self.image = None
            self.overlay = None

            self.max_zoom = max_zoom
            self.min_zoom = min_zoom

            self.last_zoom = min_zoom
            self.zoom = min_zoom

            self.last_pos = (0, 0)
            self.pos = (0, 0)

            self.last_rotate = 0
            self.rotate = 0

            self.child = None

        def set_imagepath(self, path):
            self.imagepath = f"images/CG/{path}/".replace("//", "/")

        def set_image(self, img, trans=d1):
            p = max(0, self.get_pause())

            self.last_image = self.image

            if isinstance( (vid := renpy.get_registered_image(img)), Movie ):
                self.image = vid
            elif isinstance(img, str) and self.imagepath:
                self.image = f"{self.imagepath}{img}.webp"
            else:
                self.image = img

            # Reset last variables to new variables to not redraw the transform.
            self.last_zoom = self.zoom
            self.last_pos = self.pos
            self.last_rotate = self.rotate

            if self.last_type == 0:
                renpy.pause(p - 0.1)
                self.redraw(0)
                renpy.with_statement(trans)
            else:
                renpy.pause(p - 0.1)
                self.redraw(0)
                renpy.with_statement(trans)

        def set_overlay(self, overlay):
            if (img := renpy.get_registered_image(overlay)):
                self.overlay = img
            elif self.imagepath and isinstance(img, str):
                self.overlay = f"{self.imagepath}{overlay}.webp"
            else:
                self.overlay = img

            self.redraw(0)

        def set_zoom(self, n):
            self.last_zoom = self.zoom
            self.zoom = float(clamp(n, self.min_zoom, self.max_zoom))

        def set_rotation(self, n):
            self.last_rotate = self.rotate
            self.rotate = n

        def set_pos(self, pos):
            self.last_pos = tuple(self.pos)
            self.pos = pos

        def set(self, zoom=None, rotate=None, pos=None, t=None, initialize=False, pause=False, image=None, overlay=False, trans=d1):
            if zoom is None:
                zoom=self.last_zoom
            if rotate is None:
                rotate=self.last_rotate
            if pos is None:
                pos=self.last_pos
            if t is None:
                t = self.default_timer

            self.set_zoom(zoom)
            self.set_rotation(rotate)
            self.set_pos(pos)

            if initialize:
                self.last_zoom = zoom
                self.last_rotate = rotate
                self.last_pos = pos

            if image:
                self.set_image(image, trans)

            if overlay is not False:
                self.set_overlay(overlay)

            self.redraw(t)

            if pause:
                renpy.pause(t)

        def redraw(self, t):
            if (d := self.image) is None:
                return

            if isinstance(d, Movie):
                self.scale = 2.0
                self.last_type = self.type
                self.type = 1
            else:
                self.scale = 1.0
                self.last_type = self.type
                self.type = 0

            if self.overlay:
                overlay = Transform(self.overlay, zoom=1.0/self.scale)
                d = Fixed(d, overlay, fit_first=True)

            last_zoom = self.last_zoom * self.scale
            zoom = self.zoom * self.scale

            self.child = At(d, CGCamera(last_zoom, zoom, self.last_pos, self.pos, self.last_rotate, self.rotate, t))

        def get_image(self):
            return self.child

        def get_pause(self):
            d = self.image

            if d is None:
                return 0

            if isinstance(d, Movie) and renpy.music.is_playing(d.channel):
                p = renpy.music.get_pos(d.channel) or 0.0
                t = renpy.music.get_duration(d.channel)
                return t - p
            else:
                return 0

default camera = CGController()

screen animatedCG():
    tag cg
    zorder 16

    add camera.get_image() align (0.5, 0.5)
