#! usr/bin/env python3
#coding: utf-8
"""
Module with functions for main py
"""
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
    if character.hps <= 0:
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
    char_slow.hps -= char_fast.strength
    if game_over(char_slow):
        print('\n{} a quitter notre monde\n'.format(char_slow.name))
        TURN = 1
        return char_slow
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_slow.name, char_fast.strength, char_slow.hps))
    char_fast.hps -= char_slow.strength
    if game_over(char_fast):
        print('\n\n{} a quitter notre monde\n'.format(char_fast.name))
        TURN = 1
        return char_fast
    print('{} subi {} de dégats. Il lui reste {} points de vie.'.format(char_fast.name, char_slow.strength, char_fast.hps))
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
        return
    else:
        choice = input('Continuer à se battre(Touche entrée) ou quitter(Autre touche) ? ')
        print('\n')
        if choice != '':
            print('Goodbye brother !')
            return exit()
        fight(hero, ennemy)


def makeEnnemies(func, base, number, liste):
    """
    Test a function to create a number of ennemies
    """
    for i in range(number):
        new_monster = func(('Monster' + str((i + base))), (base + i))
        liste.append(new_monster)
    return liste
