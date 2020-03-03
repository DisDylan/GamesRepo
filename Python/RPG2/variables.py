#! usr/bin/env python3
#coding: utf-8
"""
Module content all constants variables
"""
from classes import Weapon, Armory

XP_STAGE = (0, 100, 150, 250, 400, 700)

MONSTER_TYPES = ["Vampire", "Orc", "Loup-Garou", "Troll", "Ogre", "Géant", "Gobelin", "Chasseur", "Chevalier", "Vagabond", "?????", "Loup", "Ours", "Tigre", "Démon"]

WEAPONS = []
WEAPONS.append(Weapon('Épée en mousse', 20, 2))
WEAPONS.append(Weapon('Épée en bois', 50, 5))
WEAPONS.append(Weapon('Épée en fer', 100, 10))

HELMETS = []
HELMETS.append(Armory('Casque en mousse', 20, 1))
HELMETS.append(Armory('Casque en cuir', 50, 3))
HELMETS.append(Armory('Casque en fer', 100, 6))
