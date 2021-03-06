#! usr/bin/env python3
#coding: utf-8
"""
Main module for creating window with pygame and variables used for
"""
import pygame
import time
from random import choice, randrange
from pygame.locals import *

pygame.init() # Init pygame

# Window size
SURFACE_H = 600
SURFACE_W = 600

# Bloc's size (3x3)
BLOC_H = 100
BLOC_W = 100

# Char size
HERO_H = 100
HERO_W = 100

surface = pygame.display.set_mode((SURFACE_W, SURFACE_H)) # Define window size
pygame.display.set_caption('RPG-Poinsu') # Window's name
horloge = pygame.time.Clock()

WALL_PIC = pygame.image.load('sprites/map/wall.png')
WAY_PIC = pygame.image.load('sprites/map/sol.png')

FIGHT_BG = pygame.image.load('sprites/map/backgroundFight.png')
MENU_BG = pygame.image.load('sprites/map/bgMenu.png')
POT_BG = pygame.image.load('sprites/map/bgPot.png')
BUY_POT_BG = pygame.image.load('sprites/map/bgAlchy.png')

ENNEMY_PIC = pygame.image.load('sprites/chars/wolf.png')

X_POS = [0, 100, 200, 300, 400, 500]
Y_POS = [0, 100, 200, 300, 400, 500]

walls = []

HERO = pygame.image.load('sprites/heroes/character.png')
hero_rect = pygame.Rect(200, 200, 100, 100)

RED_COLOR = (150, 0, 0)
YELLOW_COLOR = (150, 150, 0)
GREEN_COLOR = (0, 150, 0)

CIEL_COLOR = (152, 199, 244)

font = pygame.font.SysFont("comicsansms", 30)
fontStat = pygame.font.SysFont("comicsansms", 60)

versusList = []
ennemiesMap = []
