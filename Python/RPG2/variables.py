#! usr/bin/env python3
#coding: utf-8
"""
Module content all constants variables
"""
from classes import Weapon, Helmet, Plastron, Boots

COUNT_KILLS = 0

MONSTER_TYPES = ["Vampire", "Orc", "Loup-Garou", "Troll", "Ogre", "Géant", "Gobelin", "Chasseur", "Chevalier", "Vagabond", "?????", "Loup", "Ours", "Tigre", "Démon"]

ITEMS = []
ITEMS.append(Weapon('Épée en mousse', 20, 2))
ITEMS.append(Weapon('Épée en bois', 50, 5))
ITEMS.append(Weapon('Épée en fer', 100, 10))

ITEMS.append(Helmet('Casque en mousse', 20, 1))
ITEMS.append(Helmet('Casque en cuir', 50, 3))
ITEMS.append(Helmet('Casque en fer', 100, 6))

ITEMS.append(Plastron('Tunique en tissu', 40, 1))
ITEMS.append(Plastron('Plastron de cuir', 100, 5))
ITEMS.append(Plastron('Armure en fer', 200, 10))

ITEMS.append(Boots('Vieilles chaussettes', 30, 1))
ITEMS.append(Boots('Chaussons (aux pommes lol)', 120, 8))
ITEMS.append(Boots('Baskets air max', 250, 15))
