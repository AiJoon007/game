
init 5 python:

    class Mirror(object):
        def __init__(self):
            self.items = set()

        def add(self, item):
            self.items.add(item)

        def remove(self, item):
            self.items.remove(item)

        def get_instances(self):
            return self.items

        def get_instances_of_tag(self, tag):
            tag = tag.capitalize()

            if tag == "All":
                return self.get_instances()

            return [x for x in self.get_instances() if tag in x.tags]

        def get_tags(self):
            return sorted({"All"} | {tag for x in self.get_instances() for tag in x.tags})

    class MirrorEvent(object):
        def __init__(self, id, name, cast=[], desc="", unlocked=False, label=None, label_rewards=None, image="default", req=None, authors=[], tags=[]):
            self.id = id
            self.name = name
            self.cast = cast
            self.desc = desc
            self.unlocked = unlocked
            self.label = label
            self.label_rewards = label_rewards
            self.image = "interface/icons/{}.webp".format(self.id) if image == "default" else image
            self.req = self.validate_req(req)
            self.authors = authors
            self.tags = tags
            self.seen = False
            self.played = False

            mirror.add(self)

        def is_unlocked(self):
            if self.unlocked:
                return True

            cast = all(get_character_unlock(x) for x in self.cast)
            req = eval(self.req) if self.req else True

            return (cast and req)

        def validate_req(self, req):
            # Validate requirements at init phase to reduce number of possible bugs
            if req is None:
                return None

            if not isinstance(req, str):
                raise TypeError("MirrorEvent '{}' requirement has to be a string, got '{}'.".format(self.id, type(req)))

            output = eval(req)

            if not isinstance(output, bool):
                raise TypeError("MirrorEvent '{}' requirement must evaluate to a boolean type, got '{}'.".format(self.id, type(output)))
            return req

        def play(self):
            self.played = True

            if self.label:
                renpy.call_replay(self.label)

            if self.label_rewards:
                if renpy.context_nesting_level() > 0:
                    renpy.call_in_new_context(self.label_rewards)
                else:
                    renpy.call(self.label_rewards)

default mirror = Mirror()
