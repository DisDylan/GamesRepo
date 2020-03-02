#! usr/bin/env python3
#coding: utf-8
"""
Main module to execute the game
"""
from variables import ITEMS
from functions import fight
from functions import makeEnnemies
from functions import showStats
from functions import upgradeStats
from classes import Ennemy
from classes import Hero

def main():

    print("Bienvenue dans l'aventure de tous les dangers !")
    yourHero = Hero(input("Indiquez votre nom d'aventurier : "))
    print("\nBienvenue à toi {} ! Nous allons distribuer tes caracteristiques.")
    showStats(yourHero)
    upgradeStats(yourHero)
    """
    Main function to test
    """
    my_list1 = []
    my_list2 = []
    makeEnnemies(Ennemy, len(my_list1), 10, my_list1)
    makeEnnemies(Ennemy, len(my_list1), 10, my_list2)
    hero = Ennemy('Moi ROI DES ROIS', 20, 60)
    for item in my_list1:
        fight(hero, item)
    for item in my_list2:
        fight(hero, item)

if __name__ == '__main__':
    main()
