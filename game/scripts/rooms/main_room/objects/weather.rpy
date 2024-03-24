
label weather_sound:
    if game.weather == "blizzard":
        play weather "sounds/blizzard.ogg" fadeout 0.5 fadein 0.5 if_changed
    elif game.weather == "storm":
        play weather "sounds/storm.ogg" fadeout 0.5 fadein 0.5 if_changed
    elif game.weather == "rain":
        play weather "sounds/storm.ogg" fadeout 0.5 fadein 0.5 if_changed # TODO: Rain sound (without thunder)
    else:
        stop weather fadeout 0.5
    return

transform cloud_move:
    xpos 520
    choice:
        ypos 150
    choice:
        ypos 160
    choice:
        ypos 170
    choice:
        ypos 190
    choice:
        ypos 200

    linear 15.0 xpos 237
    pause 7
    repeat

image weather_clear = ConditionSwitch(
    "game.daytime == True", "images/rooms/main_room/weather/sky.webp",
    "game.moon == True", "images/rooms/main_room/weather/night_sky_moon.webp",
    "game.daytime == False", "images/rooms/main_room/weather/night_sky.webp",
    )

image weather_overcast = ConditionSwitch(
    "game.daytime == True", "images/rooms/main_room/weather/sky_overcast.webp",
    "game.moon == True", "images/rooms/main_room/weather/night_sky_moon_overcast.webp",
    "game.daytime == False", "images/rooms/main_room/weather/night_sky_overcast.webp",
    )

image weather_cloudy_clouds_night = Composite(
    (155, 230),
    (40, 40), "images/rooms/main_room/weather/night_cloud_01.webp",
    (60, 60), "images/rooms/main_room/weather/night_cloud_02.webp",
    (80, 80), "images/rooms/main_room/weather/night_cloud_03.webp",
    )

image weather_cloudy_clouds_day = Composite(
    (155, 230),
    (40, 40), "images/rooms/main_room/weather/day_cloud_01.webp",
    (60, 60), "images/rooms/main_room/weather/day_cloud_02.webp",
    (80, 80), "images/rooms/main_room/weather/day_cloud_03.webp",
    )

image weather_cloudy_clouds = ConditionSwitch(
    "game.daytime == True", "weather_cloudy_clouds_day",
    "game.daytime == False", "weather_cloudy_clouds_night",
    )

image weather_cloudy_fx:
    animation
    "weather_cloudy_clouds"
    choice:
        pos (-100, 0)
    choice:
        pos (-100, 15)
    choice:
        pos (-100, 30)

    ease 15.0 xpos 120
    pause 2
    repeat

image weather_cloudy = Fixed("weather_clear", "weather_cloudy_fx", fit_first=True)

image weather_rain_fx:
    animation
    "images/rooms/main_room/weather/rain_01.webp"
    pause.1
    "images/rooms/main_room/weather/rain_02.webp"
    pause.1
    "images/rooms/main_room/weather/rain_03.webp"
    pause.1
    repeat

image weather_rain = Fixed("weather_overcast", "weather_rain_fx", fit_first=True)

image weather_snow_fx:
    animation
    "images/rooms/main_room/weather/snow_01.webp"
    pause.07
    "images/rooms/main_room/weather/snow_02.webp"
    pause.07
    "images/rooms/main_room/weather/snow_03.webp"
    pause.07
    "images/rooms/main_room/weather/snow_04.webp"
    pause.07
    "images/rooms/main_room/weather/snow_05.webp"
    pause.07
    "images/rooms/main_room/weather/snow_06.webp"
    pause.07
    "images/rooms/main_room/weather/snow_07.webp"
    pause.07
    "images/rooms/main_room/weather/snow_08.webp"
    pause.07
    "images/rooms/main_room/weather/snow_09.webp"
    pause.07
    "images/rooms/main_room/weather/snow_10.webp"
    pause.07
    repeat

image weather_snow = Fixed("weather_overcast", "weather_snow_fx", fit_first=True)

image weather_blizzard_fx:
    animation
    "images/rooms/main_room/weather/blizzard_01.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_02.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_03.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_04.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_05.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_06.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_07.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_08.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_09.webp"
    pause.05
    "images/rooms/main_room/weather/blizzard_10.webp"
    pause.05
    repeat

image weather_blizzard= Fixed("weather_overcast", "weather_blizzard_fx", fit_first=True)

image weather_storm_fx:
    animation

    parallel:
        animation
        pause 20
        "images/rooms/main_room/weather/lightning_01.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_02.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_03.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_04.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_05.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_06.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_05.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_06.webp"
        pause.1
        "images/rooms/main_room/weather/lightning_05.webp"
        pause 20
        repeat

    parallel:
        animation
        "images/rooms/main_room/weather/rain_01.webp"
        pause.1
        "images/rooms/main_room/weather/rain_02.webp"
        pause.1
        "images/rooms/main_room/weather/rain_03.webp"
        pause.1
        repeat

image weather_storm = Fixed("weather_overcast", "weather_storm_fx", fit_first=True)
