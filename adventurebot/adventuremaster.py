import logging

from players import roles


_log = logging.getLogger(__name__)


class AdventureMaster(object):
    def __init__(self, controller):
        self.client = controller.client
        self.config = controller.config
        self.channel = "#" + self.config.items("channels")[0][0]
        self.players = {}
        self.monsters = {}

    def announce(self, text):
        _log.info("Announcing '{}' to {}.".format(text, self.channel))
        self.client.msg(self.channel, text)

    def create(self, nickmask, role):
        nick, mask = nickmask.split("!", 1)
        self.players[mask] = roles[role](self, nickmask)
        self.announce("The {} {} joins the party!".format(role, nick))
