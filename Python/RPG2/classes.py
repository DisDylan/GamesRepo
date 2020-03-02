#! usr/bin/env python3
#coding: utf-8
"""
Module contenting all classes to create weapons, armors, ennemies ect.
"""
class Weapon():
    """
    Class used to make weapons with one price and damages assigned
    """
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

    def __repr__(self):
        return '=====\n{}:\n-----\nPrix: {}\n-----\nDégats: {}\n====='.format(self.name, self.price, self.damage)


class Armory():
    """
    Class to make armors items with one price and armor assigned
    """
    def __init__(self, name, price, armor):
        self.name = name
        self.price = price
        self.armor = armor

    def __repr__(self):
        return '=====\n{}:\n-----\nPrix: {}\n-----\nArmure: {}\n====='.format(self.name, self.price, self.armor)


class Ennemy():
    """
    Class to make an ennemy with some different values
    """
    def __init__(self, name, level=1, hps=10, strength=2, speed=1):
        self.name = name
        self.level = level
        self.hps = level * hps
        self.strength = strength * int(level * 1.25)
        self.speed = speed * (level * 2)

    def __repr__(self):
        return '==========\n{}:\n----------\nNiveau: {}\n----------\nPoints de vie: {}\n----------\nDégats: {}\n=========='.format(self.name, self.level, self.hps, self.strength)

class Hero():
    """
    Main class for the character of the user
    """
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.sp = 3
        self.strength = 2
        self.hps = 10
        self.speed = 4
