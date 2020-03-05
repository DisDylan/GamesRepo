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


class Helmet():
    """
    Class to make armors items with one price and armor assigned
    """
    def __init__(self, name, price, armor):
        self.name = name
        self.price = price
        self.armor = armor

    def __repr__(self):
        return '\n=====\n{}:\n-----\nPrix: {}\n-----\nArmure: {}\n====='.format(self.name, self.price, self.armor)


class Plastron():
    """
    Class to make armors items with one price and armor assigned
    """
    def __init__(self, name, price, armor):
        self.name = name
        self.price = price
        self.armor = armor

    def __repr__(self):
        return '\n=====\n{}:\n-----\nPrix: {}\n-----\nArmure: {}\n====='.format(self.name, self.price, self.armor)


class Boots():
    """
    Class to make armors items with one price and armor assigned
    """
    def __init__(self, name, price, speed):
        self.name = name
        self.price = price
        self.speed = speed

    def __repr__(self):
        return '\n=====\n{}:\n-----\nPrix: {}\n-----\nVitesse: {}\n====='.format(self.name, self.price, self.speed)


class Ennemy():
    """
    Class to make an ennemy with some different values
    """
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 10
        self.hps = level * 10
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
            self.hps = 1
            self.speed = 0

    def __repr__(self):
        return '\033[91m==========\n\033[31m{}\n\033[0m----------\n\033[91mNiveau: {}\n\033[0m----------\n\033[91mPoints de vie: {}\n\033[0m----------\n\033[91mDégats: {}\n\033[91m==========\033[0m'.format(self.name, self.level, self.hp, self.strength)

class Hero():
    """
    Main class for the character of the user
    """
    XP_STAGE = (0, 100, 150, 250, 400, 700, 1200, 1800, 2500, 3500)

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
        # Attributes to calculate armor, damage and velocity
        self.sword = 0
        self.helmet = 0
        self.plastron = 0
        self.haveBoots = False
        self.boots = 0

    def __repr__(self):
        return("\n\n=:=:=:=:=:=:=:=:=:=\n\033[92m{}, niveau {}\n\033[0m--------------------\n\033[90mForce: {}\n\033[31mPdV: {}/{}\n\033[35mVélocité: {}\n\033[93mPièces d'or: {}\n\033[91mPotions: {}\n\033[94mExperience: {}/{}\n\033[0m=:=:=:=:=:=:=:=:=:=\n\n".format(self.name, self.level, self.strength, self.hp, self.hps, self.speed, self.gold, self.pot, self.xp, self.XP_STAGE[self.level]))

    def levelUp(self):
        if self.xp >= self.XP_STAGE[self.level]:
            self.xp -= self.XP_STAGE[self.level]
            self.level += 1
            self.sp += 1
            print("\nVous progressez d'un niveau ! Vous êtes maintenant niveau {}.\nProgression de l'xp: {}/{}".format(self.level, self.xp, self.XP_STAGE[self.level]))
            return 1
        else:
            print("\nVotre barre d'experience a progressé : {}/{}".format(self.xp, self.XP_STAGE[self.level]))
            return 0
