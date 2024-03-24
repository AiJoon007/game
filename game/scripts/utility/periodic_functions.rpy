init python:
    def periodic_achievements():
        if not hasattr(store, "achievements") or _in_replay:
            return

        if not achievements.status('gold') and game.gold >= 10000:
            achievements.unlock("gold")

        if not achievements.status('drunkard') and wine_ITEM.owned >= 25:
            achievements.unlock("drunkard")

        if not achievements.status('peta') and (game.day-states.bird_fed_times) >= 50:
            achievements.unlock("peta")

        if not achievements.status('petpal') and states.bird_petted_times >= 25:
            achievements.unlock("petpal")

        if not achievements.status('bros') and states.sna.level >= 100:
            achievements.unlock("bros")

        if not achievements.status('overwhored') and states.her.level >= 24:
            achievements.unlock("overwhored")

        if not achievements.status('fireplace') and states.fireplace_started_times >= 5:
            achievements.unlock("fireplace")

        if not achievements.status('workaholic') and states.paperwork_reports_times >= 5:
            achievements.unlock("workaholic")

    def periodic_callbacks():
        """Call functions that need to be checked periodically (i.e. achievement unlocks) at around 20Hz"""
        periodic_achievements()

define config.periodic_callback = periodic_callbacks
