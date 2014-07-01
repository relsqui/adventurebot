import logging

from kitnirc.modular import Module
from kitnirc.contrib.admintools import is_admin
from adventurebot.adventuremaster import AdventureMaster
from adventurebot import players


_log = logging.getLogger(__name__)

commands = [
        ["create", "AB_NEW"],
        ["spawn", "AB_SPAWN"],
        ["attack", "AB_ATTACK"],
]


class AdventureModule(Module):
    def start(self, *args, **kwargs):
        super(AdventureModule, self).start(*args, **kwargs)
        self.add_commands(self.controller.client)
        self.master = AdventureMaster(self.controller)

    def stop(self, *args, **kwargs):
        self.master.cleanup()
        self.clear_commands(self.controller.client)
        super(AdventureModule, self).stop(*args, **kwargs)

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
            return
        try:
            role = args[0].lower().strip()
        except IndexError:
            role = None
        if not role or role not in players.roles:
            client.reply(recipient, actor,
                         "Usage: create <role>. Available roles: "
                         "fighter, wizard, thief, cleric.")
            return
        self.master.create(actor, role)

    @Module.handle("AB_SPAWN")
    def spawn_monster(self, client, actor, recipient, *args):
        if is_admin(self.controller, client, actor):
            self.master.spawn()
        else:
            client.reply(recipient, actor, "You can't spawn monsters.")

    @Module.handle("AB_ATTACK")
    def attack(self, client, actor, recipient, *args):
        nick, mask = actor.split("!", 1)
        if mask not in self.master.players:
            _log.debug("{} tried to attack but has no character.".format(actor))
            client.reply(recipient, actor,
                         "You don't have a character yet! Use create <role> "
                         "to make one.")
            return
        player = self.master.players[mask]

        if not self.master.monsters:
            _log.debug("{} tried to attack but there is no "
                       "monster.".format(actor))
            client.reply(recipient, actor, "There's nothing here to attack!")
            return
        if not args:
            _log.debug("{} tried to attack but didn't specify a "
                       "target.".format(actor))
            client.reply(recipient, actor, "Attack which monster?")
            return
        monster = args[0].upper()

        if monster not in self.master.monsters:
            _log.debug("{} tried to attack nonexistent target "
                       "{}.".format(actor, args[0]))
            client.reply(recipient, actor,
                         "There's no {} here to attack.".format(args[0]))
            return
        monster = self.master.monsters[monster]

        _log.info("{} attacked {}".format(actor, monster))
        player.target = monster
        player.auto()

module = AdventureModule
