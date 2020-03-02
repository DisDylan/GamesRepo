#! usr/bin/env python3
#coding: utf-8
"""
Main module to execute the game
"""
from random import randrange
from random import choice
from variables import ITEMS
from variables import XP_STAGE
from variables import MONSTER_TYPES
from functions import fight
from functions import makeEnnemies
from functions import upgradeStats
from classes import Ennemy
from classes import Hero

def main():
    """
    Main function to test
    """
    print("Bienvenue dans l'aventure de tous les dangers !")
    yourHero = Hero(input("Indiquez votre nom d'aventurier : "))
    print("\nBienvenue à toi {} ! Nous allons distribuer tes caracteristiques.".format(yourHero.name))
    print(yourHero)
    upgradeStats(yourHero)
    """
    my_list1 = []
    my_list2 = []
    makeEnnemies(Ennemy, len(my_list1), 10, my_list1, yourHero)
    makeEnnemies(Ennemy, len(my_list1), 10, my_list2, yourHero)
    for item in my_list1:
        print(item)
        fight(yourHero, item)
        print(yourHero)
    for item in my_list2:
        fight(yourHero, item)
    """
    increment = 0
    while yourHero.hp > 0:
        versus = Ennemy(choice(MONSTER_TYPES), randrange((yourHero.level), (yourHero.level + 2)))
        print(versus)
        fight(yourHero, versus)
        print(yourHero)
        increment += 1

if __name__ == '__main__':
    main()
