#! usr/bin/env python3
#coding: utf-8
"""
Module content all constants variables
"""
from classes import Weapon, Armory

XP_STAGE = (0, 100, 150, 250, 400, 700)

ITEMS = []
FOAM_SWORD = Weapon('Épée en mousse', 20, 2)
WOOD_SWORD = Weapon('Épée en bois', 50, 5)
IRON_SWORD = Weapon('Épée en métal', 100, 10)
LEATH_HELMET = Armory('Casque en cuir', 20, 1)
ITEMS.extend([FOAM_SWORD, WOOD_SWORD, IRON_SWORD, LEATH_HELMET])

MONSTER_TYPES = ["Vampire", "Orc", "Loup-Garou", "Troll", "Ogre", "Géant", "Gobelin", "Chasseur", "Chevalier", "Vagabond", "?????", "Loup", "Ours", "Tigre", "Démon"]
