#! usr/bin/env python3
#coding: utf-8
"""
Main module to execute the game
"""
from random import randrange, choice
from variables import HELMETS, WEAPONS, XP_STAGE, MONSTER_TYPES
from functions import fight, makeEnnemies, upgradeStats, showItems, usePot, buyPot
from classes import Ennemy, Hero

def main():
    """
    Main function to test
    """
    print("Bienvenue dans l'aventure de tous les dangers !")
    yourHero = Hero(input("Indiquez votre nom d'aventurier : "))
    print("\nBienvenue à toi {} ! Nous allons distribuer tes caracteristiques.".format(yourHero.name))
    print(yourHero)
    upgradeStats(yourHero)
    
    while yourHero.hp > 0:
        versus = Ennemy(choice(MONSTER_TYPES), randrange((yourHero.level), (yourHero.level + 2)))
        print(versus)

        usePot(yourHero)

        fight(yourHero, versus)
        print(yourHero)

        buyPot(yourHero)
        showItems(yourHero)

if __name__ == '__main__':
    main()
