import logging
from random import choice

from kitnirc.client import Client


_log = logging.getLogger(__name__)


class Monster(object):
    def __init__(self, master):
        self.nicks = ["MONSTER", "A_MONSTER", "BASIC_MONSTER"]
        self.name = self.nicks[0]
        self.master = master
        self.channel = self.master.channel
        self.client = Client()
        self.health = 50
        self.damage = 10
        self.xp = 1
        self.targets = []
        self.dead = False

    def connect(self):
        host = self.master.client.server.host
        port = self.master.client.server.port
        _log.info("Connecting {} to {}:{}.".format(self.name, host, port))
        self.client.connect(self.name, host=host, port=port)
        self.client.join(self.channel)

    def quit(self, message=None):
        if message == None:
            message = "{} runs away.".format(self.name)
        self.client.quit(message)

    def say(self, text):
        self.client.msg(self.channel, text)

    def do(self, act):
        self.client.emote(self.channel, text)

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
        else:
            self.show_hit()

    def show_hit(self):
        self.say("Ow!")

    def die(self):
        self.show_die()
        for target in self.targets:
            target.give_xp(self.xp)
        self.quit("{} dies.".format(self.name))
        self.dead = True


    def show_die(self):
        self.say("Arrrrrrgh!")
