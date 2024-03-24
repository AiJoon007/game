image seventh_door:
    zoom 0.5

    "images/rooms/seventh_floor/door.webp"

image seventh_fire_basin:
    zoom 0.5

    contains:
        "images/rooms/seventh_floor/fire_basin.webp"

    contains:
        "images/rooms/seventh_floor/fire0.webp"
        pause.12
        "images/rooms/seventh_floor/fire1.webp"
        pause.12
        "images/rooms/seventh_floor/fire2.webp"
        pause.12
        "images/rooms/seventh_floor/fire3.webp"
        pause.12
        "images/rooms/seventh_floor/fire4.webp"
        pause.12
        "images/rooms/seventh_floor/fire5.webp"
        pause.12
        repeat

image seventh_fire_basin_right:
    xzoom -1
    "seventh_fire_basin"
