import logging

from kitnirc.modular import Module
from adventurebot.adventuremaster import AdventureMaster
from adventurebot import players


_log = logging.getLogger(__name__)

commands = [
        ["create", "AB_NEW"]
]

class AdventureModule(Module):
    def start(self, *args, **kwargs):
        super(AdventureModule, self).start(*args, **kwargs)
        self.add_commands(self.controller.client)
        self.master = AdventureMaster()

    def stop(self, *args, **kwargs):
        super(AdventureModule, self).stop(*args, **kwargs)
        self.clear_commands(self.controller.client)

    @Module.handle("COMMANDS")
    def add_commands(self, client):
        _log.info("Loading adventure commands.")
        for command in commands:
            self.trigger_event("ADDCOMMAND", client, command)

    def clear_commands(self, client):
        for command in commands:
            self.trigger_event("REMOVECOMMAND", client, command[:2])

    @Module.handle("AB_NEW")
    def create_character(self, client, actor, recipient, *args):
        nick, mask = actor.split("!", 1)
        if mask in self.master.players:
            client.reply(recipient, actor, "You already have a character!")
            return True
        try:
            role = args[0].lower().strip()
        except IndexError:
            client.reply(recipient, actor,
                         "Usage: create <class>. Available classes: "
                         "fighter, wizard, thief, cleric.")
            return True
        if role == "fighter":
            self.master.players[mask] = players.Fighter(mask)
            client.reply(recipient, actor,
                         "Created. Welcome, fighter {}!".format(nick))
        elif role == "wizard":
            self.master.players[mask] = players.Wizard(mask)
            client.reply(recipient, actor,
                         "Created. Welcome, wizard {}!".format(nick))
        elif role == "thief":
            self.master.players[mask] = players.Thief(mask)
            client.reply(recipient, actor,
                         "Created. Welcome, thief {}!".format(nick))
        elif role == "cleric":
            self.master.players[mask] = players.Cleric(mask)
            client.reply(recipient, actor,
                         "Created. Welcome, cleric {}!".format(nick))
        else:
            client.reply(recipient, actor,
                         "Usage: create <class>. Available classes: "
                         "fighter, wizard, thief, cleric.")
        return True


module = AdventureModule
