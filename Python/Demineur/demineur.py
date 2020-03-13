from random import *
import time
import pygame
from pygame.locals import *

pygame.init()

BLOC = pygame.image.load('wall.png')


# CREATION PAR LE JOUEUR D'UNE GRILLE
x = int(input('Hauteur'))
y = int(input('Largeur'))

surface = pygame.display.set_mode((x*30, y*30)) # Define window size
pygame.display.set_caption('Demineur') # Window's name
horloge = pygame.time.Clock()

f = open('terrain.txt', 'a+')
for i in range(x):
	for a in range(y):
		f.write('0')
	f.write('\n')
f.close()

dem = open('terrain.txt', 'r')
new_game = dem.readlines()
largeur = len(new_game[0])-1
hauteur = len(new_game)
delete = open('terrain.txt', 'w')
delete.write('')
delete.close
mines_list = []
nb_mines = 0

while nb_mines != int((hauteur * largeur)*0.15):
	mines_list.append('X')
	nb_mines += 1

case = [[0 for col in range(largeur)] for row in range(hauteur)]
for i in mines_list:
	case[randrange(hauteur)][randrange(largeur)] = i

count_mines = 0
for x in range(hauteur):
	for y in range(largeur):
		if (x > 0) and (y > 0):
			if case[x-1][y-1] == 'X':
				count_mines += 1
		if y > 0:
			if case[x][y-1] == 'X':
				count_mines += 1
		if (x < (hauteur-1)) and (y > 0):
			if case[x+1][y-1] == 'X':
				count_mines += 1
		if x < (hauteur-1):
			if case[x+1][y] == 'X':
				count_mines += 1
		if (x < (hauteur-1)) and (y < (largeur-1)):
			if case[x+1][y+1] == 'X':
				count_mines += 1
		if y < (largeur-1):
			if case[x][y+1] == 'X':
				count_mines += 1
		if (y < (largeur-1)) and (x > 0):
			if case[x-1][y+1] == 'X':
				count_mines += 1
		if x > 0:
			if case[x-1][y] == 'X':
				count_mines += 1
		if case[x][y] == 'X':
			count_mines = 'X'
		if case[x][y] != 'X':
			case[x][y] = count_mines
		else:
			case[x][y] = 'X'
		print(count_mines,end="")
		count_mines = 0
	print()
print()
print(case)

new_case = []
for i in range(hauteur):
	for j in range(largeur):
		position = (i, j)
		new_case.append(position)
print(new_case)


y_pos = 0
for i in range(largeur):
	x_pos = 0
	for j in range(hauteur):
		surface.blit(BLOC, (x_pos, y_pos))
		x_pos += 30
	y_pos += 30
pygame.display.update()
print("x={}, y={}, x_pos={}, y_pos={}".format(x, y, x_pos, y_pos))

font = pygame.font.SysFont("comicsansms", 30)
"""
def showNear(x, y):
	gotNone = 0
		if (x > 0) and (y > 0):
			if case[x-1][y-1] == 0:
				gotNone += 1
		if y > 0:
			if case[x][y-1] == 0:
				gotNone += 1
		if (x < (hauteur-1)) and (y > 0):
			if case[x+1][y-1] == 0:
				gotNone += 1
		if x < (hauteur-1):
			if case[x+1][y] == 0:
				gotNone += 1
		if (x < (hauteur-1)) and (y < (largeur-1)):
			if case[x+1][y+1] == 0:
				gotNone += 1
		if y < (largeur-1):
			if case[x][y+1] == 0:
				gotNone += 1
		if (y < (largeur-1)) and (x > 0):
			if case[x-1][y+1] == 0:
				gotNone += 1
		if x > 0:
			if case[x-1][y] == 0:
				gotNone += 1
		if gotNone != 0:
			sh
"""
continuer = True
while continuer == True:
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			y = int(pos[0]/30)
			x = int(pos[1]/30)
			print(y, x)
			print(case[x][y])
			if case[x][y] == 'X':
				print('perdu')
				quit()
			elif case[x][y] == 0:
				showNear(x, y)
			else:
				show = str(case[x][y])
				text = font.render("{}".format(show), True, (200, 0, 0))
				y *= 30
				x *= 30
				surface.blit(text, (y+8, x+8))
				pygame.display.update()
"""
for i in range(len(recList)):
	for j in range(len(i))
		if recList.collide == True:
			if case[i][j] == 'X':
				quit()
			else:
				value = case[i][j]
				text = text.render(value, True, (0, 0, 0))
				surface.blit(text, (i*size, j*size))
				pygame.display.update()
				
while True:
    for event in pygame.event.get():
        if event.type == pygame.mouse.get_pressed():
            ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()
            ## check if cursor is on button ##
            if button.collidepoint(pos):
                ## exit ##
                return
				"""