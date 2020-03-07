#! usr/bin/env python3
#coding: utf-8
"""
Main module to execute the game
"""
from random import randrange, choice
from variables import ITEMS
from functions import fight, makeEnnemies, upgradeStats, showItems, usePot, buyPot, heroMove, makeMap, resetMap, getName
from classes import Ennemy, Hero
from window import *
import pygame
from pygame.locals import *


def main():
    """
    Main function to play
    """
    yourChamp = Hero("")
    getName(yourChamp)
    print(yourChamp.name)
    upgradeStats(yourChamp)
    makeMap(yourChamp, walls, ennemiesMap)
    surface.blit(HERO, hero_rect)

    ingame = 1
    while ingame != 0:
        if heroMove(yourChamp, HERO, hero_rect, walls, ennemiesMap):
            fight(yourChamp, versusList[0])
            del versusList[0]
            usePot(yourChamp)
            resetMap(ennemiesMap)
            makeMap(yourChamp, walls, ennemiesMap)
            surface.blit(HERO, hero_rect)


if __name__ == '__main__':
    main()
