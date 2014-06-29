#!/usr/bin/python

from verbs import Punch, Zap


class Player(object):
    def __init__(self, nickmask):
        self.nickmask = nickmask
        self.name = nickmask.split("!", 1)[0]
        self.target = None
        self.xp = 0
        self.roll_stats()
        self.equipment = {"head": None, "torso": None,
                          "weapon": None, "legs": None}

    def roll_stats(self):
        self.fight = 50
        self.cast = 50
        self.evade = 10
        self.resist = 10
        self.full_health = 100
        self.health = 100

    def modifiers(self, stat):
        modifier = 0
        for slot in ["head", "torso", "weapon", "legs"]:
            try:
                modifier += getattr(self.equipment[slot], stat, 0)
            except KeyError:
                pass
        return modifier

    def say(self, text):
        print('< {}> {}'.format(self.name, text))

    def do(self, act):
        print("* {} {}".format(self.name, act))

    def auto(self):
        if self.target and self.basic:
            damage = self.basic.do()
            if damage:
                self.do("{}s {}.".format(self.basic.s, self.target.name))
                self.target.hit(self, damage)
            else:
                self.do("misses {}.".format(self.target.name))

    def hit(self, origin, damage):
        self.health -= damage

class Fighter(Player):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.basic = Punch(self)

    def roll_stats(self):
        super(Fighter, self).roll_stats()
        self.fight += 10
        self.cast -= 5
        self.evade += 5


class Wizard(Player):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.basic = Zap(self)

    def roll_stats(self):
        super(Wizard, self).roll_stats()
        self.fight -= 5
        self.cast += 10
        self.resist += 5

        
class Thief(Player):
    def __init__(self, *args, **kwargs):
        super(Thief, self).__init__(*args, **kwargs)
        self.basic = Punch(self)

    def roll_stats(self):
        super(Thief, self).roll_stats()
        self.fight -= 5
        self.cast += 10
        self.resist += 5

        
class Cleric(Player):
    def __init__(self, *args, **kwargs):
        super(Cleric, self).__init__(*args, **kwargs)
        self.basic = Zap(self)

    def roll_stats(self):
        super(Cleric, self).roll_stats()
        self.fight -= 5
        self.cast += 10
        self.evade += 5
