init python early:
    # Import commonly used python modules
    import time
    import datetime
    import math
    import random
    import pygame
    import colorsys
    import fnmatch
    import posixpath
    import re
    import string
    import functools
    from bisect import bisect
    from operator import itemgetter
    from operator import add as _add
    from collections import OrderedDict

    get_volume_preference = renpy.game.preferences.get_volume

    def num_to_word(n, readable=True):
        """Transcript numbers (integers) into readable words."""
        n = int(n)
        units = ("","one","two","three","four","five","six","seven","eight","nine")
        teens = ("","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")
        tens = ("","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety")
        thousands = ("","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion","undecillion","duodecillion","tredecillion","quattuordecillion","sexdecillion","septendecillion","octodecillion","novemdecillion","vigintillion")

        output = []
        if n == 0:
            output.append("zero")
        else:
            s = str(n)
            groups = (len(s)+2)//3
            s = s.zfill(groups*3)

            for i in range(0, groups*3, 3):
                h,t,u = int(s[i]), int(s[i+1]), int(s[i+2])
                g = groups-(i//3+1)

                if h > 0:
                    output.append(units[h]+" hundred")
                if t > 1:
                    if u > 0:
                        output.append(tens[t]+"-"+units[u])
                    else:
                        output.append(tens[t])
                elif t == 1:
                    if u > 0:
                        output.append(teens[u])
                    else:
                        output.append(tens[t])
                else:
                    if u > 0:
                        output.append(units[u])

                if g > 0 and (h+t+u) > 0:
                    if i == (groups*3)-6:
                        output.append(thousands[g]+" and")
                    else:
                        output.append(thousands[g]+",")

        if readable:
            output = " ".join(output)
        return output

    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))

    def white_tint(image):
        return Transform( image, matrixcolor=TintMatrix((1.1, 1.1, 1.1)) )

    def gray_tint(image):
        return Transform( image, matrixcolor=SaturationMatrix(0.0) )

    def yellow_tint(image):
        return Transform( image, matrixcolor=TintMatrix((1.2, 1.1, 0.7)) )

    def image_hover(image, brightness=0.12):
        """Returns slightly brighter image used during hover events"""
        return Transform( image, matrixcolor=BrightnessMatrix(brightness) )

    def image_alpha(image, alpha=0.5):
        """Returns an image with changed alpha 0 - fully transparent 1 - fully visible"""
        return Transform( image, matrixcolor=OpacityMatrix(alpha) )

    def set_clipboard(txt):
        txt = str(txt)
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, txt.encode())

    def get_clipboard():
        clipboard = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)
        if clipboard:
            return clipboard.decode()
        return None

    def evaluate(txt):
        try:
            return __import__('ast').literal_eval(txt)
        except Exception as e:
            print("Error evaluating data:")
            print(e)

    def reset_variables(*args):
        """Resets the given variables to their default values."""
        # Refer to renpy.ast.Default.set_default for implementation details
        defaults_set = renpy.store._defaults_set
        changed_set = renpy.store.__dict__.ever_been_changed
        for arg in args:
            if arg in defaults_set:
                if arg in changed_set:
                    defaults_set.remove(arg)
                    changed_set.remove(arg)
            elif config.developer:
                raise Exception("The variable `{}` was not previously set with a default value.".format(arg))
        renpy.execute_default_statement(False)

    def disable_game_menu():
        setattr(renpy.store, "_game_menu_screen", None)

    def enable_game_menu():
        setattr(renpy.store, "_game_menu_screen", "save_screen")

    def make_revertable(obj):
        if isinstance(obj, _list):
            return [make_revertable(x) for x in obj]
        elif isinstance(obj, _dict):
            return dict([(make_revertable(k), make_revertable(v)) for (k,v) in obj.items()])
        else:
            return obj

    def is_integer(s):
        def zero(s):
            return (len(s) > 1 and s.startswith("0"))

        s = str(s)

        if s and s[0] in ("-", "+"):
            return (not zero(s[1:]) and s[1:].isdigit())
        return (not zero(s) and s.isdigit())

    def timeit(func, loops=10000, args=(), kwargs={}):
        start = time.time()
        for i in range(loops):
            func(*args, **kwargs)
        end = time.time()
        print(f"The task has taken {end-start} seconds to finish")

    def list_swap_values(l, val1, val2):
        """Mutates the original list."""
        l[val1], l[val2] = l[val2], l[val1]

    def natsort_key(s, pattern=re.compile("([0-9]+)")):
        return [int(t) if t.isdigit() else t.lower() for t in pattern.split(str(s))]

    def tts(s):
        renpy.display.tts.tts(str(s))

    def is_in_lead(house):
        if isinstance(house, str):
            house = getattr(renpy.store, house)

        return (house == max(gryffindor, slytherin, ravenclaw, hufflepuff))

    def play_potion_return(who):
        if game.daytime:
            return

        for i in inventory.get_instances_of_type("potion"):
            if not who in i.usable_on:
                continue

            if not i.in_progress[who]:
                continue

            i.ret(who)

    def strip(s):
        # We need a custom strip implementation because we cannot tell
        # if the raw argument isn't encapsulated in double, or triple quotes
        if s.startswith(('"', "'")) and s.endswith(('"', "'")):
            return s[1:-1]
        return s

    def matches(s1, s2, filter=" "):
        return s1.replace(filter, "") == s2.replace(filter, "")

    def istype(inst, clss):
        if not isinstance(clss, (list, tuple, set)):
            clss = (clss,)
        return type(inst) in clss

    class IntLike(python_object):
        # Does not support rollback

        def __init__(self, callable):
            self._callable = callable

        def __call__(self):
            return self._callable()

        def __repr__(self):
            return repr(self())

        def __add__(self, value):
            raise Exception("IntLike does not support add")

        def __eq__(self, value):
            return self._callable() == value

        def __gt__(self, value):
            return self._callable() > value

        def __lt__(self, value):
            return self._callable() < value

        def __ge__(self, value):
            return self.__gt__(value) or self.__eq__(value)

        def __le__(self, value):
            return self.__lt__(value) or self.__eq__(value)

        def __len__(self):
            return len(self._callable())

    def execute_callbacks(callbacks):
        for callback in callbacks: callback()