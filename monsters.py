#!/usr/bin/python

from random import choice


class Monster(object):
    def __init__(self):
        self.nicks = ["MONSTER", "A_MONSTER", "BASIC_MONSTER"]
        self.name = self.nicks[0]
        self.health = 50
        self.damage = 10
        self.xp = 1
        self.targets = []

    def say(self, text):
        print('< {}> {}'.format(self.name, text))

    def do(self, act):
        print("* {} {}".format(self.name, act))

    def idle(self):
        self.do("stands around looking menacing.")

    def auto(self):
        if not self.targets:
            return
        target = choice(self.targets)
        self.show_attack(target)

    def show_attack(self, target):
        self.do("punches {}.".format(target.name))

    def hit(self, origin, damage):
        if origin not in self.targets:
            self.targets.append(origin)
        self.health -= damage
        if self.health < 0:
            self.die()
            return True
        else:
            self.show_hit()
            return False

    def show_hit(self):
        self.say("Ow!")

    def die(self):
        self.show_die()
        for target in self.targets:
            target.give_xp(self.xp)

    def show_die(self):
        self.say("Arrrrrrgh!")
        self.do("dies.")
