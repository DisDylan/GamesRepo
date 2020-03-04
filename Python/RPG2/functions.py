#! usr/bin/env python3
#coding: utf-8
"""
Module with functions for main py
"""
from random import randrange, sample
from variables import XP_STAGE, ITEMS, COUNT_KILLS
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
    global COUNT_KILLS
    if TURN == 1:
        print("[][][][][][][][][][]\nUn ennemi apparait !!")
        if char_fast.__class__.__name__ == "Ennemy":
            print(char_fast)
        else:
            print(char_slow)
        next_fight = input('Appuyez sur entrée pour l\'affrontement ou entrez un lettre pour quitter\n[][][][][][][][][][]\n')
        if next_fight != '':
            print("\nVous avez vaincu {} ennemis pendant cette partie !".format(COUNT_KILLS))
            print('Goodbye !!')
            return exit()
        print('::::::::::\n{} a l\'initiative:\n::::::::::'.format(char_fast.name))
    char_slow.hp -= (char_fast.strength + char_fast.dmgWeapon - char_slow.armor)
    if game_over(char_slow):
        print('\n{} a quitté notre monde\n'.format(char_slow.name))
        TURN = 1
        return char_slow
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_slow.name, (char_fast.strength + char_fast.dmgWeapon - char_slow.armor), char_slow.hp))
    char_fast.hp -= (char_slow.strength + char_slow.dmgWeapon - char_fast.armor)
    if game_over(char_fast):
        print('\n\n{} a quitté notre monde\n'.format(char_fast.name))
        TURN = 1
        return char_fast
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_fast.name, (char_slow.strength + char_slow.dmgWeapon - char_fast.armor), char_fast.hp))
    TURN += 1
    return None


def fight(hero, ennemy):
    """
    Function to make an auto fight between our hero and an ennemy met
    """
    global COUNT_KILLS
    if velocity(hero, ennemy) == ennemy:
        fighters = fight_order(ennemy, hero)
    else:
        fighters = fight_order(hero, ennemy)
    if fighters == hero:
        print('Fin de la partie, merci d\'avoir joué !')
        return quit()
    elif fighters == ennemy:
        print('Vous avez vaincu !\n')
        COUNT_KILLS += 1
        hero.xp += ennemy.xp
        hero.gold += ennemy.gold
        print("Vous gagnez {} pièces d'or.".format(ennemy.gold))
        print("Vous gagnez {} points d'experience.".format(ennemy.xp))
        if hero.levelUp(XP_STAGE) == 1:
            upgradeStats(hero)
        return
    else:
        choice = input('Continuer à se battre(Touche entrée) ou quitter(Autre touche) ? ')
        print('\n')
        if choice != '':
            print("\nVous avez vaincu {} ennemis pendant cette partie !".format(COUNT_KILLS))
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
    print("\n**********\n**********\nTu as {} points de caracteristiques a distribuer.".format(character.sp))
    if character.sp > 0:
        choice = input("Utiliser des points (o/n): ")
        if choice.lower() == "o":
            statToUp = input("\nQuelle statistique augmenter ?\n(F)orce = 1 pour 1;\n(V)ie = 1 pour 5;\n(S)Vitesse = 1 pour 3;\nVotre choix : ")
            if statToUp.lower() == "f":
                character.strength += 1
                character.sp -= 1
            elif statToUp.lower() == "v":
                character.hp += 5
                character.hps += 5
                character.sp -= 1
            elif statToUp.lower() == "s":
                character.speed += 3
                character.sp -= 1
            else:
                print("Entrée inconnue ... Veuillez saisir un choix valide.")
            print(character)
            upgradeStats(character)
        elif choice.lower() == ("n" or ''):
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
    shop = input("\n///// Le vendeur se présente à vous ! \\\\\\\\\\\nSouhaitez vous voir ce qu'il vous propose (o/n)? ")
    if shop.lower() == 'o':
        selection = sample(ITEMS, k=4)
        for i in selection:
            print("\n{}\n".format(i))
            buyItems(char, i)
    elif shop.lower() != ('n' or ''):
        print("Entrée inconnue, veuillez ressaisir votre choix..\n")
        showItems(char)
    else:
        return


def buyPot(char):
    """
    Buy a selected number of potions
    """
    potCost = 5
    buyOne = input("\nL'alchimiste apparait, lui acheter une potion (o/n)? ")
    if buyOne.lower() == 'o':
        maxPot = floor(char.gold / potCost)
        howMany = int(input("Vous pouvez acheter {} potions, combien en voulez vous ?".format(maxPot)))
        if howMany > maxPot:
            print("\n!!! La maison ne fait pas crédit !!!\n")
            buyPot(char)
        else:
            char.gold -= (howMany * potCost)
            char.pot += howMany
            print("- - - Votre achat s'est bien déroulé.\n- - - Vous avez désormais {} potions.\n- - - Il vous reste {} pièces d'or.\n".format(char.pot, char.gold))
    return

def totalArmor(char):
    """
    Short func to update armor of the character
    """
    char.armor = char.helmet + char.plastron
    return

def totalSpeed(char, item):
    """
    Short func to update speed of the character (depend if he have boots or not)
    """
    if char.haveBoots == False:
        char.boots = item.speed
        char.speed += char.boots
    else:
        char.speed -= char.boots
        char.boots = item.speed
        char.speed += char.boots
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
                char.dmgWeapon = item.damage
            elif item.__class__.__name__ == "Helmet":
                char.helmet = item.armor
                totalArmor(char)
            elif item.__class__.__name__ == "Plastron":
                char.plastron = item.armor
                totalArmor(char)
            elif item.__class__.__name__ == "Boots":
                totalSpeed(char, item)
            print("\nVOTRE ACHAT S'EST BIEN DEROULE")
            print("Il vous reste {} en or.".format(char.gold))
            return
        elif buying.lower() == 'n':
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
