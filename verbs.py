#!/usr/bin/python

from random import randrange

def basic_attack(player, stat):
    if randrange(100) < getattr(player, stat):
        try:
            return getattr(player.equipment.weapon, stat) + 10
        except AttributeError:
            return 10
    return 0

def punch(player):
    return basic_attack(player, "fight")

def zap(player):
    return basic_attack(player, "cast")
