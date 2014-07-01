from random import randrange


class Verb(object):
    name = None
    s = None

    def __init__(self, player):
        self.player = player

    def do(self):
        raise NotImplementedError


class BasicAttack(Verb):
    def do(self):
        if randrange(100) < getattr(self.player, self.stat):
            return max(1, 10 + self.player.modifiers(self.stat))
        return 0


class Punch(BasicAttack):
    def __init__(self, *args, **kwargs):
        super(Punch, self).__init__(*args, **kwargs)
        self.stat = "fight"
        self.name = "punch"
        self.s = "punches"


class Zap(BasicAttack):
    def __init__(self, *args, **kwargs):
        super(Zap, self).__init__(*args, **kwargs)
        self.stat = "cast"
        self.name = "zap"
        self.s = "zaps"
