#!/usr/bin/python

from random import choice


class Monster(object):
    def __init__(self):
        self.nicks = ["MONSTER", "A_MONSTER", "BASIC_MONSTER"]
        self.nick = self.nicks[0]
        self.health = 50
        self.damage = 10
        self.xp = 1
        self.targets = []

    def say(self, text):
        print('{} says, "{}"'.format(self.nick, text))

    def do(self, act):
        print("{} {}".format(self.nick, act))

    def idle(self):
        self.do("stands around looking menacing.")

    def auto(self):
        if not targets:
            return
        target = choice(targets)
        self.show_attack(target)
        target.hit(self.damage)

    def show_attack(self, target):
        self.do("punches {}.".format(target.nick))

    def hit(self, origin, damage):
        if origin not in targets:
            targets.append(origin)
        self.say("Arrrrrrgh!")
        self.do("dies.")
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
