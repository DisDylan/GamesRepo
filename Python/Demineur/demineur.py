from random import *
import pygame

# CREATION PAR LE JOUEUR D'UNE GRILLE
x = int(input('Hauteur'))
y = int(input('Largeur'))
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