#! usr/bin/env python3
#coding: utf-8
"""
Module with functions for main py
"""
from random import randrange
from variables import XP_STAGE
from classes import Hero

def velocity(hero, ennemy):
    """
    Return fighter with the higher speed value
    """
    if hero.speed >= ennemy.speed:
        return hero
    return ennemy


def game_over(character):
    """
    Return true if our hero die
    """
    if character.hp <= 0:
        return True
    return False

TURN = 1

def fight_order(char_fast, char_slow):
    """
    Made to fight in order of velocity
    """
    global TURN
    if TURN == 1:
        next_fight = input('Un ennemi apparait, appuyez sur entrée pour l\'affrontement ou entrez un lettre pour quitter: ')
        if next_fight != '':
            print('Goodbye !!')
            return exit()
        print('::::::::::\n{} a l\'initiative:\n::::::::::'.format(char_fast.name))
    char_slow.hp -= char_fast.dmgDeal
    if game_over(char_slow):
        print('\n{} a quitté notre monde\n'.format(char_slow.name))
        TURN = 1
        return char_slow
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_slow.name, char_fast.dmgDeal, char_slow.hp))
    char_fast.hp -= char_slow.dmgDeal
    if game_over(char_fast):
        print('\n\n{} a quitté notre monde\n'.format(char_fast.name))
        TURN = 1
        return char_fast
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_fast.name, char_slow.dmgDeal, char_fast.hp))
    TURN += 1
    return None


def fight(hero, ennemy):
    """
    Function to make an auto fight between our hero and an ennemy met
    """
    if velocity(hero, ennemy) == ennemy:
        fighters = fight_order(ennemy, hero)
    else:
        fighters = fight_order(hero, ennemy)
    if fighters == hero:
        print('Fin de la partie, merci d\'avoir joué !')
        return quit()
    elif fighters == ennemy:
        print('Vous avez vaincu !\n')
        hero.xp += ennemy.xp
        hero.gold += ennemy.gold
        if hero.levelUp(XP_STAGE) == 1:
            upgradeStats(hero)
        return
    else:
        choice = input('Continuer à se battre(Touche entrée) ou quitter(Autre touche) ? ')
        print('\n')
        if choice != '':
            print('Goodbye brother !')
            return exit()
        fight(hero, ennemy)


def makeEnnemies(func, base, number, liste, hero):
    """
    Test a function to create a number of ennemies
    """
    for i in range(number):
        new_monster = func(('Monster' + str((i + base))), randrange((hero.level), (hero.level + 2)))
        liste.append(new_monster)
    return liste

def upgradeStats(character):
    """
    Function to verify if you have stats points, and ask to user if he want use them
    """
    print("Tu as {} points de caracteristiques a distribuer.".format(character.sp))
    if character.sp > 0:
        choice = input("Utiliser des points (o/n): ")
        if choice.lower() == "o":
            statToUp = input("\nQuelle statistique augmenter ?\n(F)orce = 1 pour 1;\n(V)ie = 1 pour 5;\n(S)Vitesse = 1 pour 2;\nVotre choix : ")
            if statToUp.lower() == "f":
                character.strength += 1
                character.sp -= 1
                character.dmgDeal += 1
            elif statToUp.lower() == "v":
                character.hp += 5
                character.hps += 5
                character.sp -= 1
            elif statToUp.lower() == "s":
                character.speed += 1
                character.sp -= 1
            else:
                print("Entrée inconnue ... Veuillez saisir un choix valide.")
            print(character)
            upgradeStats(character)
        elif choice.lower() == "n":
            return
        else:
            print("Entrée inconnue ... Veuillez saisir un choix valide.")
            upgradeStats(character)
    else:
        return

def showInventory():
    return
