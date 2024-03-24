############################################
###       Programmable Xmas Lights       ###
### - Because why the fock not Edition - ###
############################################

default xmas_lights_hue1 = 0
default xmas_lights_hue2 = 0
default xmas_lights_brightness = 0.0
default xmas_lights_alpha = 1.0

label xmas_lights_settings:

    menu:
        "-Set Animation-":
            label .animation:

            menu:
                "-Static-":
                    $ xmas_lights_ITEM.room_image = Transform("xmas_lights_static", zoom=xmas_lights_ITEM.room_scale)
                    $ xmas_lights_ITEM.room_image_hover = xmas_lights_ITEM.room_image
                "-Alternate-":
                    $ xmas_lights_ITEM.room_image = Transform("xmas_lights_alternate", zoom=xmas_lights_ITEM.room_scale)
                    $ xmas_lights_ITEM.room_image_hover = xmas_lights_ITEM.room_image
                "-Cycle-":
                    $ xmas_lights_ITEM.room_image = Transform("xmas_lights_cycle", zoom=xmas_lights_ITEM.room_scale)
                    $ xmas_lights_ITEM.room_image_hover = xmas_lights_ITEM.room_image
                "-Pulse-":
                    $ xmas_lights_ITEM.room_image = Transform("xmas_lights_pulse", zoom=xmas_lights_ITEM.room_scale)
                    $ xmas_lights_ITEM.room_image_hover = xmas_lights_ITEM.room_image
                "-Back-":
                    jump xmas_lights_settings

            jump .animation

        "-Set Hue-":
            label .hue:

            menu:
                "-Default-":
                    $ xmas_lights_hue1 = 0
                    $ xmas_lights_hue2 = 0
                "-Blue and Red-":
                    $ xmas_lights_hue1 = 160
                    $ xmas_lights_hue2 = 280
                "-Orange and Blue-":
                    $ xmas_lights_hue1 = 330
                    $ xmas_lights_hue2 = 160
                "-Red and Green-":
                    $ xmas_lights_hue1 = 280
                    $ xmas_lights_hue2 = 20
                "-Custom-":
                    $ input_val1 = renpy.input("(Enter first hue rotation value between 0 - 360)", xmas_lights_hue1, "1234567890", length=3)
                    $ xmas_lights_hue1 = clamp(int(input_val1), 0, 360)
                    $ input_val2 = renpy.input("(Enter second hue rotation value between 0 - 360)", xmas_lights_hue2, "1234567890", length=3)
                    $ xmas_lights_hue2 = clamp(int(input_val2), 0, 360)
                "-Back-":
                    jump xmas_lights_settings

            jump .hue

        "-Set Brightness-":
            label .brightness:

            menu:
                "-100%%-":
                    $ xmas_lights_brightness = 0.0
                    $ xmas_lights_alpha = 1.0
                "-80%%-":
                    $ xmas_lights_brightness = -0.1
                    $ xmas_lights_alpha = 0.8
                "-60%%-":
                    $ xmas_lights_brightness = -0.2
                    $ xmas_lights_alpha = 0.6
                "-40%%-":
                    $ xmas_lights_brightness = -0.3
                    $ xmas_lights_alpha = 0.4
                "-30%%-":
                    $ xmas_lights_brightness = -0.4
                    $ xmas_lights_alpha = 0.2
                "-Back-":
                    jump xmas_lights_settings

            jump .brightness

        "-Exit-":
            jump main_room_menu

init python:
    def xmas_lights_set1_bulbs(st, at):
        d = Transform("images/rooms/main_room/decorations/xmas_lights/bulbset_1.webp", matrixcolor=HueMatrix(xmas_lights_hue1)*BrightnessMatrix(xmas_lights_brightness))
        return d, 1.0

    def xmas_lights_set2_bulbs(st, at):
        d = Transform("images/rooms/main_room/decorations/xmas_lights/bulbset_2.webp", matrixcolor=HueMatrix(xmas_lights_hue2)*BrightnessMatrix(xmas_lights_brightness))
        return d, 1.0

    def xmas_lights_set1_glow(st, at):
        d = Transform("images/rooms/main_room/decorations/xmas_lights/glowset_1.webp", alpha=xmas_lights_alpha, matrixcolor=HueMatrix(xmas_lights_hue1)*BrightnessMatrix(xmas_lights_brightness))
        return d, 1.0

    def xmas_lights_set2_glow(st, at):
        d = Transform("images/rooms/main_room/decorations/xmas_lights/glowset_2.webp", alpha=xmas_lights_alpha, matrixcolor=HueMatrix(xmas_lights_hue2)*BrightnessMatrix(xmas_lights_brightness))
        return d, 1.0

image xmas_lights_set1_bulbs = DynamicDisplayable(xmas_lights_set1_bulbs)
image xmas_lights_set2_bulbs = DynamicDisplayable(xmas_lights_set2_bulbs)
image xmas_lights_set1_glow = DynamicDisplayable(xmas_lights_set1_glow)
image xmas_lights_set2_glow = DynamicDisplayable(xmas_lights_set2_glow)
