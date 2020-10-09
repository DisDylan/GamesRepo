import sys
import os
from random import *

# Function to boost ennemy by zone and hero lvl
def zone_boost(ennemy, actual_zone):
	if actual_zone == 'mines':
		ennemy.hp = ennemy.hp * 2
		ennemy.strength = ennemy.strength * 2
	elif actual_zone == 'glaces':
		ennemy.hp = ennemy.hp * 5
		ennemy.strength = ennemy.strength * 4
	elif actual_zone == 'sables':
		ennemy.hp = ennemy.hp * 10
		ennemy.strength = ennemy.strength * 10
	elif actual_zone == 'enfers':
		ennemy.hp = ennemy.hp * 18
		ennemy.strength = ennemy.strength * 18


#Asking user if he want use potion or not
def use_pot(my_char):
	input('Vos points de vie sont à {} sur {}.'.format(my_char.hp, my_char.max_hp))
	if my_char.pot > 0:
		use = input('Utiliser une potion (+25)?\n> ')
		if use.lower() == 'oui':
			my_char.hp += 25
			if my_char.hp > my_char.max_hp:
				my_char.hp = my_char.max_hp
			my_char.pot -= 1
			print('Vous récuperez 25 points de vie !')
			input('Vous avez maintenant {} points de vie sur {}, et il vous reste {} potions.'.format(my_char.hp, my_char.max_hp, my_char.pot))
			os.system('clear')
		if use.lower() == 'non':
			pass
		else:
			use_pot(my_char)
		return my_char.hp
	else:
		print('Désolé, vous n\'avez aucune potion en stock !')
	return my_char.hp

# Make a percent chance of chest appear
def chest(my_char):
	if randrange(0, 10) > 6:
		os.system('clear')
		input('Un coffre est apparu !')
		if my_char.keys != 0:
			open_it = input('Souhaitez vous l\'ouvrir ?\nVous possédez {} clé(s)\n(Tapez correctement oui pour l\'ouvrir)\n> '.format(my_char.keys))
			if open_it == 'oui':
				my_char.keys -= 1
				os.system('clear')
				input('Vous ouvrez le coffre et perdez une clé. Dedans ...')
				content = randrange(0, 3)
				if content == 1:
					input('Vous gagnez un point de force !')
					my_char.strength += 1
				elif content == 2:
					input('Vous gagnez deux point de vie !')
					my_char.hp += 2
					my_char.max_hp += 2
				else:
					input('.. Il n\'y a rien ! ..')
			else:
				os.system('clear')
				input('Vous continuez donc votre chemin.')
		else:
			input('Mais vous n\'avez pas de clé :(')

# MENU
def title_screen_selections():
	option = input("> ")
	if option.lower() == "jouer":
		return
	elif option.lower() == "aide":
		help_menu()
	elif option.lower() == "quitter":
		sys.exit()
	else:
		print("Entrez une commande valide.")
		title_screen_selections()

def title_screen():
	os.system('clear')
	print('###########################')
	print('# Bienvenue dans \'AiRPG\' !#')
	print('###########################')
	print('         - Jouer -         ')
	print('         - Aide -          ')
	print('         - Quitter -       ')
	print('       Bonne chance !      ')
	title_screen_selections()

def help_menu():
	print('###########################')
	print('# Bienvenue dans \'AiRPG\' !#')
	print('###########################')
	print('- Appuyez toujours sur entrée pour valider vos choix !')
	title_screen_selections()