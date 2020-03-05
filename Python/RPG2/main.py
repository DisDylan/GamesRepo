#! usr/bin/env python3
#coding: utf-8
"""
Main module to execute the game
"""
from random import randrange, choice
from variables import ITEMS, MONSTER_TYPES
from functions import fight, makeEnnemies, upgradeStats, showItems, usePot, buyPot
from classes import Ennemy, Hero
from window import *
import pygame
from pygame.locals import *

versusList = []
ennemiesMap = []
yourchamp = Hero("YourHero")

def collision(hero, listRect):
    for i in listRect:
        if hero.colliderect(i):
            return i
    return 0


def resetMap(listEnnemies):
    for i in listEnnemies:
        i.x = -1000
        i.y = -1000


def makeMap(listR, listE):
    for i in X_POS:
        for j in Y_POS:
            if (i==0 and j==0) or (i==100 and j==0) or (i==0 and j==100) or (i==0 and j==400) or (i==0 and j==500) or (i==100 and j==500) or (i==400 and j==0) or (i==500 and j==0) or (i==500 and j==100) or (i==500 and j==400) or (i==400 and j==500) or (i==500 and j==500):
                wall = pygame.Rect(i, j, 95, 95)
                listR.append(wall)
                surface.blit(WALL_PIC, wall)
            else:
                surface.blit(WAY_PIC, (i, j))
            if randrange(0, 100) < 40:
                versus = Ennemy(choice(MONSTER_TYPES), (randrange((yourchamp.level - 2), (yourchamp.level + 2))))
                versusList.append(versus)
                addEnnemy = pygame.Rect(i, j, 95, 95)
                listE.append(addEnnemy)
                surface.blit(ENNEMY_PIC, addEnnemy)




def heroMove(char, hero_rect, listWall, listEnnemy):
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
        makeMap(listWall, listEnnemy)
        surface.blit(char, hero_rect)

    elif hero_rect.x > 500:
        hero_rect.x = 0
        resetMap(listEnnemy)
        makeMap(listWall, listEnnemy)
        surface.blit(char, hero_rect)

    elif hero_rect.y < 0:
        hero_rect.y = 500
        resetMap(listEnnemy)
        makeMap(listWall, listEnnemy)
        surface.blit(char, hero_rect)

    elif hero_rect.y > 500:
        hero_rect.y = 0
        resetMap(listEnnemy)
        makeMap(listWall, listEnnemy)
        surface.blit(char, hero_rect)
        
    pygame.display.update()
    return fight

makeMap(walls, ennemiesMap)
surface.blit(HERO, hero_rect)

ingame = 1
while ingame != 0:
    if heroMove(HERO, hero_rect, walls, ennemiesMap):
        fight(yourchamp, choice(versusList))
        resetMap(ennemiesMap)
        makeMap(walls, ennemiesMap)
        surface.blit(HERO, hero_rect)

"""
def main():
    
    Main function to test
    
    print("Bienvenue dans l'aventure de tous les dangers !")
    yourHero = Hero(input("Indiquez votre nom d'aventurier : "))
    print("\nBienvenue à toi {} ! Nous allons distribuer tes caracteristiques.".format(yourHero.name))
    print(yourHero)
    upgradeStats(yourHero)
    
    while yourHero.hp > 0:
        versus = Ennemy(choice(MONSTER_TYPES), (randrange((yourHero.level - 2), (yourHero.level + 2))))

        fight(yourHero, versus)
        print(yourHero)
        usePot(yourHero)

        buyPot(yourHero)
        showItems(yourHero)
"""

if __name__ == '__main__':
    main()
