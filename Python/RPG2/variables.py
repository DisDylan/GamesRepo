#! usr/bin/env python3
#coding: utf-8
"""
Module content all constants variables
"""
from classes import Weapon, Armory

ITEMS = []

WOOD_SWORD = Weapon('Épée en bois', 10, 4)
IRON_SWORD = Weapon('Épée en métal', 80, 15)
LEATH_HELMET = Armory('Casque en cuir', 20, 3)
ITEMS.extend([WOOD_SWORD, IRON_SWORD, LEATH_HELMET])
