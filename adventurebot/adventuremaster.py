import logging

from players import roles
from monsters import Monster


_log = logging.getLogger(__name__)


class AdventureMaster(object):
    def __init__(self, controller):
        self.client = controller.client
        self.config = controller.config
        self.channel = "#" + self.config.items("channels")[0][0]
        self.players = {}
        self.monsters = {}

    def cleanup(self):
        for monster in self.monsters:
            self.monsters[monster].quit()

    def announce(self, text):
        _log.info("Announcing '{}' to {}.".format(text, self.channel))
        self.client.msg(self.channel, text)

    def create(self, nickmask, role):
        nick, mask = nickmask.split("!", 1)
        self.players[mask] = roles[role](self, nickmask)
        self.announce("The {} {} joins the party!".format(role, nick))
        _log.info("Added {} {}.".format(role, nickmask))

    def spawn(self):
        monster = Monster(self)
        self.monsters[monster.name] = monster
        _log.info("Spawning {}.".format(monster.name))
        monster.connect()
