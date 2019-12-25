#! usr/bin/env python3
#coding: utf-8
"""
Main module to execute the game
"""
from variables import ITEMS
from functions import fight
from functions import makeEnnemies
from classes import Ennemy

def main():
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
