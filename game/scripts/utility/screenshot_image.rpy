
init -10 python:
    class ScreenshotImage(NoRollback):
        _image = None

        def __init__(self):
            pass

        def capture(self):
            self._image = Transform(im.Data(renpy.screenshot_to_bytes(None), "screenshot.png"), size=(config.screen_width, config.screen_height))

        @property
        def image(self):
            return self._image

    screenshot = ScreenshotImage()

    def displayable_to_file(d, path, size=(config.screen_width, config.screen_height), crop=None, coloralpha=(0, 255, 0)):
        crop = crop or (0, 0, size[0], size[1])
        gl_clear = renpy.config.gl_clear_color
        renpy.config.gl_clear_color = coloralpha

        d = d.render(size[0], size[1], 0, 0)
        surf = renpy.display.draw.screenshot(d)
        surf = pygame.transform.smoothscale(surf, (config.screen_width, config.screen_height)).convert()
        surf.set_colorkey(coloralpha)

        psurf = pygame.Surface(size, pygame.SRCALPHA).convert_alpha()
        psurf.blit(surf, (0, 0), crop)

        pygame.image.save(psurf, path, 9)
        renpy.config.gl_clear_color = gl_clear
