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
        return '\n=====\n{}:\n-----\nPrix: {}\n-----\nDégats: {}\n====='.format(self.name, self.price, self.damage)


class Armory():
    """
    Class to make armors items with one price and armor assigned
    """
    def __init__(self, name, price, armor):
        self.name = name
        self.price = price
        self.armor = armor

    def __repr__(self):
        return '\n=====\n{}:\n-----\nPrix: {}\n-----\nArmure: {}\n====='.format(self.name, self.price, self.armor)


class Ennemy():
    """
    Class to make an ennemy with some different values
    """
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 8
        self.strength = 2 * int(level * 1.10)
        self.speed = level * 2
        self.xp = level * 40
        self.gold = level * 5
        self.dmgWeapon = 0
        self.armor = 0

        if self.level <= 0:
            self.name = "Mannequin d'entrainement"
            self.level = 0
            self.gold = 10
            self.xp = 100
            self.strength = 0
            self.hp = 1
            self.speed = 0

    def __repr__(self):
        return '==========\n{}:\n----------\nNiveau: {}\n----------\nPoints de vie: {}\n----------\nDégats: {}\n=========='.format(self.name, self.level, self.hp, self.strength)

class Hero():
    """
    Main class for the character of the user
    """
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.sp = 5
        self.strength = 3 # 3
        self.hp = 25 # 25
        self.hps = 25
        self.speed = 4
        self.xp = 0
        self.dmgWeapon = 0
        self.gold = 20
        self.armor = 0
        self.pot = 1

    def __repr__(self):
        return("\n\n=:=:=:=:=:=:=:=:=:=\n{}, niveau {}:\nForce: {}\nPdV: {}/{}\nVélocité: {}\nPièces d'or: {}\n=:=:=:=:=:=:=:=:=:=\n\n".format(self.name, self.level, self.strength, self.hp, self.hps, self.speed, self.gold))

    def levelUp(self, steps):
        if self.xp >= steps[self.level]:
            self.xp -= steps[self.level]
            self.level += 1
            self.sp += 1
            print("\nVous progressez d'un niveau ! Vous êtes maintenant niveau {}.\nProgression de l'xp: {}/{}".format(self.level, self.xp, steps[self.level]))
            return 1
        else:
            print("\nVotre barre d'experience a progressé : {}/{}".format(self.xp, steps[self.level]))
            return 0
