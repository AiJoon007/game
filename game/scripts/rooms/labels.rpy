# Set the scene for a given room
label room(room=None, hide_screens=True, stop_sound=True):

    # Hide all screens (only room related screens are shown)
    if hide_screens:
        $ renpy.scene("screens")

    # Stop sound effects (necessary when changing rooms)
    if stop_sound:
        stop background fadeout 0.5
        stop weather fadeout 0.5

    $ renpy.stop_predict_screen(states.room)
    $ renpy.stop_predict("images/rooms/{}/*.webp".format(states.room))
    $ states.room = room
    $ renpy.start_predict_screen(states.room)
    $ renpy.start_predict("images/rooms/{}/*.webp".format(states.room))

    if room == "main_room":
        # Update sound effects
        call weather_sound

        show screen main_room

        if mailbox.get_letters():
            $ owl_OBJ.hidden = False
            play sound "sounds/owl.ogg"

        if mailbox.get_parcels():
            $ parcel_OBJ.hidden = False

        # User interface
        call update_ui_points
        show screen ui_top_bar

    elif room == "weasley_store":
        show screen weasley_store_room

    elif room == "clothing_store":
        show screen clothing_store

    elif room == "seventh_floor":
        show screen seventh_floor

    elif room == "room_of_requirement":
        show screen room_of_requirement
        show screen room_of_requirement_overlay

    elif room == "quidditch_pitch":
        show screen quid_pitch_back
        show screen quid_pitch_mid
        show screen quid_pitch_front

    elif room == "quidditch_stands":
        call quidditch_stands(reset=True)

    elif room == "quidditch_stands2":
        call quidditch_stands2(reset=True)

    elif room == "snape_office":
        show screen snape_office

    elif room == "boxing_ring":
        show screen boxing_ring
        show screen boxing_ring_overlay

    return
