label splashscreen:
    scene black

    call screen splashscreen with dissolve

    $ persistent.consent = True
    return

screen splashscreen():
    tag splashscreen
    style_prefix "splash"

    default consent = persistent.consent or False

    add Image("gui/splash/legal.webp", oversample=2) at splashcreen_zoomin

    add Image("gui/splash/rating.webp", oversample=2.5) align (0.05, 0.9)

    vbox:
        align (0.5, 0.9)
        text "The game contains strong language, nudity, explicit scenes, drinkin', smokin', bangin', use of drugs, and just about everything your mother ever told you not to do."
        text "{color=#ff0000}{b}NOT SUITABLE FOR CHILDREN{/b}{/color}!" size 22

    timer 7.0 action Return()

    if consent:
        use invisible_button(action=Return())

style splash_text:
    color "#ffffff"
    outlines [(2, "#000", 1, 1)]
    xsize 580
    xalign 0.5

transform splashcreen_zoomin:
    subpixel True
    transform_anchor True
    zoom 1.0
    align (0.5, 0.5)
    linear 100.0 zoom 1.5 align (0.5, 0.3)
