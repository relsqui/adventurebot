#!/usr/bin/python

from verbs import punch, zap


class Player(object):
    def __init__(self, nickmask):
        self.nickmask = nickmask
        self.name = nickmask.split("!", 1)[0]
        self.target = None
        self.xp = 0
        self.roll_stats()

    def roll_stats(self):
        self.fight = 50
        self.cast = 50
        self.evade = 10
        self.resist = 10
        self.full_health = 100
        self.health = 100

    def auto(self):
        if self.target:
            damage = self.basic(self)
            if damage:
                self.target.hit(self, damage)

    def hit(self, origin, damage):
        self.health -= damage

class Fighter(Player):
    def __init__(self, *args, **kwargs):
        super(Fighter, self).__init__(*args, **kwargs)
        self.basic = punch

    def roll_stats(self):
        super(Fighter, self).roll_stats()
        self.fight += 10
        self.cast -= 5
        self.evade += 5


class Wizard(Player):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
        self.basic = zap

    def roll_stats(self):
        super(Wizard, self).roll_stats()
        self.fight -= 5
        self.cast += 10
        self.resist += 5

        
class Thief(Player):
    def __init__(self, *args, **kwargs):
        super(Thief, self).__init__(*args, **kwargs)
        self.basic = punch

    def roll_stats(self):
        super(Thief, self).roll_stats()
        self.fight -= 5
        self.cast += 10
        self.resist += 5

        
class Cleric(Player):
    def __init__(self, *args, **kwargs):
        super(Cleric, self).__init__(*args, **kwargs)
        self.basic = zap

    def roll_stats(self):
        super(Cleric, self).roll_stats()
        self.fight -= 5
        self.cast += 10
        self.evade += 5
