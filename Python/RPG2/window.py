#! usr/bin/env python3
#coding: utf-8
"""
Main module for creating window with pygame and register events
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

ENNEMY_PIC = pygame.image.load('sprites/chars/wolf.png')

X_POS = [0, 100, 200, 300, 400, 500]
Y_POS = [0, 100, 200, 300, 400, 500]

walls = []

HERO = pygame.image.load('sprites/heroes/characterF.png')
hero_rect = pygame.Rect(200, 200, 100, 100)

