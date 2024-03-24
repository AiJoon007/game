transform vibrator_interface_transform:

    zoom 0.4
    align (0.5, 0.0)

    on show:
        alpha 0.0
        linear 0.66 alpha 1.0
        pause 4.0
        linear 0.66 alpha 0.0

    on replace: # New widget
        linear 0.66 alpha 1.0
        pause 4.0
        linear 0.66 alpha 0.0

    on replaced: # Old widget
        alpha 0.0

    on hide:
        linear 0.66 alpha 0.0

transform vibrator_interface_captions_transform:
    pause 1.0
    linear 0.66 alpha 0.0

layeredimage vibrator_interface:
    fit_first True

    always "vibrator_interface_background"

    group emoji multiple variant "emoji":
        attribute low default if_not "low_disabled"
        attribute medium default if_not "medium_disabled"
        attribute high default if_not "high_disabled"
        attribute low_disabled
        attribute medium_disabled
        attribute high_disabled

    group vibration auto prefix "vibration":
        attribute off null default

        at shake

    group caption prefix "caption":
        attribute low default
        attribute medium default
        attribute high default

        at vibrator_interface_captions_transform

    at vibrator_interface_transform
