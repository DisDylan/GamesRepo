#! usr/bin/env python3
#coding: utf-8
"""
Module with functions for main py
"""
from random import randrange, sample
from variables import XP_STAGE, HELMETS, WEAPONS
from math import floor

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
    char_slow.hp -= (char_fast.dmgDeal - char_slow.armor)
    if game_over(char_slow):
        print('\n{} a quitté notre monde\n'.format(char_slow.name))
        TURN = 1
        return char_slow
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_slow.name, (char_fast.dmgDeal - char_slow.armor), char_slow.hp))
    char_fast.hp -= (char_slow.dmgDeal - char_fast.armor)
    if game_over(char_fast):
        print('\n\n{} a quitté notre monde\n'.format(char_fast.name))
        TURN = 1
        return char_fast
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_fast.name, (char_slow.dmgDeal - char_fast.armor), char_fast.hp))
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


def showItems(char):
    """
    Function to show rand items to user and let him buy if has needed golds
    """
    shop = input("Le vendeur se présente à vous, souhaitez vous voir ce qu'il vous propose (o/n)? ")
    if shop.lower() == 'o':
        whichItem = input("Voir les (A)rmes ou les (P)rotections ? ")
        if whichItem.lower() == 'a':
            selection = sample(WEAPONS, k=2)
            for i in selection:
                print(i)
                print("\n")
                buyItems(char, i)
        elif whichItem.lower() == 'p':
            selection = sample(HELMETS, k=2)
            for i in selection:
                print(i)
                print("\n")
                buyItems(char, i)
        else:
            print("Entrée inconnue, veuillez ressaisir votre choix..\n")
            showItems(char)
    elif shop.lower() != 'n':
        print("Entrée inconnue, veuillez ressaisir votre choix..\n")
        showItems(char)
    else:
        return


def buyPot(char):
    """
    Buy a selected number of potions
    """
    potCost = 5
    buyOne = input("L'alchimiste apparait, lui acheter une potion (o/n)?")
    if buyOne.lower() == 'o':
        maxPot = floor(char.gold / potCost)
        howMany = input("Vous pouvez acheter {} potions, combien en voulez vous ?".format(maxPot))
        if howMany > maxPot:
            print("\n!!! La maison ne fait pas crédit !!!\n")
            buyPot(char)
        else:
            char.gold -= (howMany * potCost)
            char.pot += howMany
            print("- - - Votre achat s'est bien déroulé.\n- - - Vous avez désormais {} potions.\n- - - Il vous reste {} pièces d'or.".format(char.pot, char.gold))
    return


def buyItems(char, item):
    """
    Ask to user if he want buy item show
    """
    print("Vous avez {} pièces d'or actuellement.".format(char.gold))
    if char.gold >= item.price:
        buying = input("Acheter cet item (o/n)? ")
        if buying.lower() == 'o':
            char.gold -= item.price
            if item.__class__.__name__ == "Weapon":
                char.dmgDeal += item.damage
            elif item.__class__.__name__ == "Armory":
                char.armor += item.armor
            print("\nVOTRE ACHAT S'EST BIEN DEROULE")
            print("Il vous reste {} en or.".format(char.gold))
            return
        elif buying.lower == 'n':
            return
        else:
            print("Erreur, recommencez.")
            buyItems(char, item)
    input("Désolé, vous n'avez pas assez d'argent .. Travaillez plus pour gagner plus !")
    return


def usePot(char):
    """
    Allow user to recover HP before fighting
    """
    if char.pot > 0:
        use = input("-!-!-!-!-!-!-!-!-!-\nUtiliser une potion (o/n)")
        if use.lower() == 'o':
            diff = char.hp
            char.pot -= 1
            char.hp += 20
            if char.hp > char.hps:
                char.hp = char.hps
            diff = char.hp - diff
            print("(: Vous avez recuperé {} points de vie :)".format(diff))
            usePot(char)
        elif use.lower() == 'n':
            return
        else:
            print("Lettre 'o' ou lettre 'n' vindiou !!")
            usePot(char)
    else:
        print("Pas de potion, navré pour vous ..")
    return
