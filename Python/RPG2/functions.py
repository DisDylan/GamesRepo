#! usr/bin/env python3
#coding: utf-8
"""
Module with functions for main py
"""
from random import randrange, sample
from variables import ITEMS, COUNT_KILLS, MONSTER_TYPES
from classes import Hero, Ennemy
from math import floor
from window import *
import pygame
import time

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
    hpBar(char_slow)
    hpBar(char_fast)
    if TURN == 1:
        if char_fast.__class__.__name__ == "Ennemy":
            print(char_fast)
        else:
            print(char_slow)
        getEnter()
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
    hpBar(char_slow)
    hpBar(char_fast)
    return None


def fight(hero, ennemy):
    """
    Function to make an auto fight between our hero and an ennemy met
    """
    surface.blit(FIGHT_BG, (0, 0))
    surface.blit(ENNEMY_PIC, (400, 450))
    surface.blit(HERO, (100, 450))
    pygame.display.update()
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
        del ennemy
        if hero.levelUp() == 1:
            refreshMenu(hero)
            upgradeStats(hero)
            print("Up niveau {}".format(hero.level))
        return
    else:
        hpBar(hero)
        getEnter()
        fight(hero, ennemy)
                        


def makeEnnemies(func, base, number, liste, hero):
    """
    Test a function to create a number of ennemies
    """
    for i in range(number):
        new_monster = func(('Monster' + str((i + base))), randrange((hero.level), (hero.level + 2)))
        liste.append(new_monster)
    return liste

def refreshMenu(character):
    """
    Main func to refresh menu with stats of user
    """
    spDisturb = font.render("Vous avez {} points a distribuer".format(character.sp), True, (250, 250, 0))
    strength = fontStat.render("Point de (F)orce : {} (+1)".format(character.strength), True, (255, 255, 255))
    life = fontStat.render("Points de (V)ie : {}/{} (+5)".format(character.hp, character.hps), True, (255, 255, 255))
    speed = fontStat.render("(S)Vitesse : {} (+3)".format(character.speed), True, (255, 255, 255))
    surface.blit(MENU_BG, (0, 0))
    surface.blit(spDisturb, (100, 100))
    surface.blit(strength, (50, 250))
    surface.blit(life, (50, 350))
    surface.blit(speed, (50, 450))
    pygame.display.update()

def upgradeStats(character):
    """
    Function to verify if you have stats points, and allow user to use them on a menu screen
    """
    refreshMenu(character)
    continuer = 1
    if character.sp > 0:
        while continuer == 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        character.strength += 1
                        character.sp -= 1
                        continuer = 0
                    elif event.key == K_v:
                        character.hp += 5
                        character.hps += 5
                        character.sp -= 1
                        continuer = 0
                    elif event.key == K_s:
                        character.speed += 3
                        character.sp -= 1
                        continuer = 0
        print(character)
        upgradeStats(character)
    else:
        return


def showItems(char):
    """
    Function to show rand items to user and let him buy if has needed golds
    """
    shop = input("\n\033[33m///// Le vendeur se présente à vous ! \\\\\\\\\\\nSouhaitez vous voir ce qu'il vous propose (o/n)? \033[0m")
    if shop.lower() == 'o':
        selection = sample(ITEMS, k=4)
        for i in selection:
            print("\n\033[33m{}\033[0m\n".format(i))
            buyItems(char, i)
    elif shop.lower() != ('n' or ''):
        print("Entrée inconnue, veuillez ressaisir votre choix..\n")
        showItems(char)
    else:
        return


def buyPot(char):
    """
    GUI to buy potions
    """
    if randrange(100) < 50:
        continuer = 1
        potCost = 5
        while continuer == 1:
            surface.blit(BUY_POT_BG, (0, 0))
            maxPot = floor(char.gold / potCost)
            if maxPot == 0:
                return
            text = font.render("Vous pouvez acheter {} potions en voulez vous ?".format(maxPot), True, GREEN_COLOR)
            surface.blit(text, (50, 500))
            golds = font.render("Il vous reste {} pièces d'or".format(char.gold), True, YELLOW_COLOR)
            surface.blit(text, (50, 500))
            surface.blit(golds, (50, 550))
            pygame.display.update()
            if char.gold >= potCost:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_o:
                            if event.key == K_o:
                                char.gold -= potCost
                                char.pot += 1
                            elif event.key == K_n:
                                continuer = 0
                        elif event.key == K_n:
                            continuer = 0
        """
        if buyOne.lower() == 'o':
            howMany = int(input("Vous pouvez acheter {} potions, combien en voulez vous ?".format(maxPot)))
            if howMany > maxPot:
                print("\n!!! La maison ne fait pas crédit !!!\n")
                buyPot(char)
            else:
                char.gold -= (howMany * potCost)
                char.pot += howMany
                print("- - - Votre achat s'est bien déroulé.\n- - - Vous avez désormais {} potions.\n- - - Il vous reste {} pièces d'or.\n".format(char.pot, char.gold))
        return
        """


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
            del item
            return
        elif buying.lower() == 'n':
            return
        else:
            print("Erreur, recommencez.")
            buyItems(char, item)
    input("Désolé, vous n'avez pas assez d'argent .. Travaillez plus pour gagner plus !")
    return


def updatePot(char):
    surface.blit(POT_BG, (0, 0))
    text = font.render("Vous avez {} potions. PdV actuels: {}/{}".format(char.pot, char.hp, char.hps), True, RED_COLOR)
    surface.blit(text, (10, 550))
    pygame.display.update()


def usePot(char):
    """
    Allow user to recover HP before fighting
    """
    updatePot(char)
    if char.pot > 0:
        continuer = 1
        while continuer == 1:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_o:
                        char.pot -= 1
                        char.hp += 20
                        if char.hp > char.hps:
                            char.hp = char.hps
                        updatePot(char)
                        continuer = 0
                    elif event.key == K_n:
                        return
        usePot(char)
    return


def hpBar(char):
    """
    Show hp bar of characters
    """
    percentHp = (char.hp / char.hps) * 100
    if percentHp > 60:
        hpText = font.render("\n     {} / {} HP     \n".format(char.hp, char.hps), True, GREEN_COLOR, CIEL_COLOR)
    elif percentHp > 30:
        hpText = font.render("\n     {} / {} HP     \n".format(char.hp, char.hps), True, YELLOW_COLOR, CIEL_COLOR)
    else:
        hpText = font.render("\n     {} / {} HP     \n".format(char.hp, char.hps), True, RED_COLOR, CIEL_COLOR)
    if char.__class__.__name__ == "Ennemy":
        surface.blit(hpText, (370, 80))
    else:
        surface.blit(hpText, (70, 80))
    pygame.display.update()

def getName(char):
    """
    Made to get the name with touch pressed
    """
    surface.blit(FIGHT_BG, (0,0))
    text = font.render("Votre nom ?", True, GREEN_COLOR)
    surface.blit(text, (250, 250))
    pygame.display.update()
    continuer = 1
    while continuer == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    char.name += 'a'
                elif event.key == K_b:
                    char.name += 'b'
                elif event.key == K_c:
                    char.name += 'c'
                elif event.key == K_d:
                    char.name += 'd'
                elif event.key == K_e:
                    char.name += 'e'
                elif event.key == K_f:
                    char.name += 'f'
                elif event.key == K_g:
                    char.name += 'g'
                elif event.key == K_h:
                    char.name += 'h'
                elif event.key == K_i:
                    char.name += 'i'
                elif event.key == K_j:
                    char.name += 'j'
                elif event.key == K_k:
                    char.name += 'k'
                elif event.key == K_l:
                    char.name += 'l'
                elif event.key == K_m:
                    char.name += 'm'
                elif event.key == K_n:
                    char.name += 'n'
                elif event.key == K_o:
                    char.name += 'o'
                elif event.key == K_p:
                    char.name += 'p'
                elif event.key == K_q:
                    char.name += 'q'
                elif event.key == K_r:
                    char.name += 'r'
                elif event.key == K_s:
                    char.name += 's'
                elif event.key == K_t:
                    char.name += 't'
                elif event.key == K_u:
                    char.name += 'u'
                elif event.key == K_v:
                    char.name += 'v'
                elif event.key == K_w:
                    char.name += 'w'
                elif event.key == K_x:
                    char.name += 'x'
                elif event.key == K_y:
                    char.name += 'y'
                elif event.key == K_z:
                    char.name += 'z'
                elif event.key == K_RETURN:
                    char.name = char.name.capitalize()
                    continuer = 0
        nameText = font.render(char.name, True, GREEN_COLOR)
        surface.blit(nameText, (250, 350))
        pygame.display.update()

def collision(hero, listRect):
    """
    Return a rect if hero collide one
    """
    for i in listRect:
        if hero.colliderect(i):
            return i
    return 0


def resetMap(listEnnemies):
    """
    Put out of the screen all rect in list
    """
    for i in listEnnemies:
        i.x = -1000
        i.y = -1000


def makeMap(yourchamp, listR, listE):
    """
    Build map with walls and ennemies, pictures and rects
    """
    for i in versusList:
        del i
    for i in X_POS:
        for j in Y_POS:
            if (i==0 and j==0) or (i==100 and j==0) or (i==0 and j==100) or (i==0 and j==400) or (i==0 and j==500) or (i==100 and j==500) or (i==400 and j==0) or (i==500 and j==0) or (i==500 and j==100) or (i==500 and j==400) or (i==400 and j==500) or (i==500 and j==500):
                wall = pygame.Rect(i, j, 95, 95)
                listR.append(wall)
                surface.blit(WALL_PIC, wall)
            else:
                surface.blit(WAY_PIC, (i, j))
            if randrange(0, 100) < 15:
                versusList.append(Ennemy(choice(MONSTER_TYPES), (randrange((yourchamp.level - 1), (yourchamp.level + 2)))))
                addEnnemy = pygame.Rect(i, j, 95, 95)
                listE.append(addEnnemy)
                surface.blit(ENNEMY_PIC, addEnnemy)
    pygame.display.update()




def heroMove(champ, char, hero_rect, listWall, listEnnemy):
    """
    Main func to move our hero, change map, collide walls and collide ennemies to fight
    """
    fight = False
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                hero_rect.move_ip(-100, 0)
                collide_w = collision(hero_rect, listWall)
                collide_e = collision(hero_rect, listEnnemy)
                if collide_w != 0:
                    hero_rect.move_ip(100, 0)
                elif collide_e != 0:
                    print("fight ici")
                    fight = True
                    collide_e.x = -1000
                    collide_e.y = -1000
                surface.blit(WAY_PIC,((hero_rect.x + 100), hero_rect.y))
                surface.blit(char, hero_rect)

            elif event.key == pygame.K_RIGHT:
                hero_rect.move_ip(100, 0)
                collide_e = collision(hero_rect, listEnnemy)
                collide_w = collision(hero_rect, listWall)
                if collide_w != 0:
                    hero_rect.move_ip(-100, 0)
                elif collide_e != 0:
                    print("fight ici")
                    fight = True
                    collide_e.x = -1000
                    collide_e.y = -1000
                surface.blit(WAY_PIC,((hero_rect.x - 100), hero_rect.y))
                surface.blit(char, hero_rect)

            elif event.key == pygame.K_DOWN:
                hero_rect.move_ip(0, 100)
                collide_w = collision(hero_rect, listWall)
                collide_e = collision(hero_rect, listEnnemy)
                if collide_w != 0:
                    hero_rect.move_ip(0, -100)
                elif collide_e != 0:
                    print("fight ici")
                    fight = True
                    collide_e.x = -1000
                    collide_e.y = -1000
                surface.blit(WAY_PIC,(hero_rect.x, (hero_rect.y - 100)))
                surface.blit(char, hero_rect)

            elif event.key == pygame.K_UP:
                hero_rect.move_ip(0, -100)
                collide_e = collision(hero_rect, listEnnemy)
                collide_w = collision(hero_rect, listWall)
                if collide_w != 0:
                    hero_rect.move_ip(0, 100)
                elif collide_e != 0:
                    print("fight ici")
                    fight = True
                    collide_e.x = -1000
                    collide_e.y = -1000
                surface.blit(WAY_PIC,(hero_rect.x, (hero_rect.y + 100)))
                surface.blit(char, hero_rect)

    if hero_rect.x < 0:
        hero_rect.x = 500
        resetMap(listEnnemy)
        makeMap(champ, listWall, listEnnemy)
        surface.blit(char, hero_rect)

    elif hero_rect.x > 500:
        hero_rect.x = 0
        resetMap(listEnnemy)
        makeMap(champ, listWall, listEnnemy)
        surface.blit(char, hero_rect)

    elif hero_rect.y < 0:
        hero_rect.y = 500
        resetMap(listEnnemy)
        makeMap(champ, listWall, listEnnemy)
        surface.blit(char, hero_rect)

    elif hero_rect.y > 500:
        hero_rect.y = 0
        resetMap(listEnnemy)
        makeMap(champ, listWall, listEnnemy)
        surface.blit(char, hero_rect)
        
    pygame.display.update()
    return fight


def getEnter():
    """
    Lock screen while user dont press return
    """
    continuer = 1
    while continuer == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    continuer = 0
                else:
                    continue
    return
