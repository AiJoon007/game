init -100 python:
    def show_gold(st, at, old, new):
        if st > 1.0:
            return Text("G {}".format(new)), None
        else:
            if new > old:
                value = int( (new-old)*(1.0-st) ) + 1
                d = Text("G {}\n+{}".format(old + int((new-old)*st), value))
            else:
                value = int( (old-new)*(1.0-st) ) + 1
                d = Text("G {}\n-{}".format(old - int((old-new)*st), value))
            return d, 0.01

    class Game(object):
        weather_types = ("clear", "cloudy", "overcast", "blizzard", "snow", "storm", "rain")
        weather_weights = (35, 35, 20, 5, 10, 10, 15)

        def __init__(self, gold=0, day=0):
            # Protected values
            self._gold = gold
            self._day = day
            self._gryf = 0
            self._slyt = 0
            self._rave = 0
            self._huff = 0
            self._weather = "clear"

            # Normal values
            self.daytime = True
            self.difficulty = 2
            self.cheats = False
            self.moon = True

        @property
        def gold(self):
            return self._gold

        @gold.setter
        def gold(self, value):
            old = self._gold
            self._gold = max(0, min(value, 99999))

            if not renpy.in_rollback() and not _in_replay:
                renpy.hide_screen("gold")
                renpy.show_screen("gold", old, self._gold)

        @property
        def day(self):
            return self._day

        @day.setter
        def day(self, value):
            self._day = max(0, min(value, 99999))

        @property
        def weather(self):
            return self._weather

        @weather.setter
        def weather(self, value):
            if value == "random":
                value = renpy.random.choices(self.weather_types, weights=self.weather_weights)[0]

            if not value in self.weather_types:
                raise ValueError("Unsupported weather type: '{}'".format(value))

            self._weather = value

            moon_cycle = renpy.random.randint(5, 9)
            self.moon = (self.day % moon_cycle == 0)

screen gold(old, new):
    tag gold
    zorder 50

    default d = DynamicDisplayable(show_gold, old, new)

    frame:
        xpadding 10
        ysize 44
        xminimum 80
        background Frame(gui.format("interface/frames/{}/iconmed.webp"), 6, 6)
        pos (50, 50)

        add d yoffset 3

    timer 3.0 action Hide("gold")

init offset = -99

default game = Game()

# Points change displayable
# Day change displayable
# Add one of X generator
