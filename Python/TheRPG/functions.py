import sys
import os

# Function to boost ennemy by zone and hero lvl
def zone_boost(ennemy, actual_zone):
	if actual_zone == 'mines':
		ennemy.vie = ennemy.vie * 2
		ennemy.strength = ennemy.strength * 2
	elif actual_zone == 'glaces':
		ennemy.vie = ennemy.vie * 5
		ennemy.strength = ennemy.strength * 4
	elif actual_zone == 'sables':
		ennemy.vie = ennemy.vie * 10
		ennemy.strength = ennemy.strength * 10
	elif actual_zone == 'enfers':
		ennemy.vie = ennemy.vie * 18
		ennemy.strength = ennemy.strength * 18


#Asking user if he want use potion or not
def use_pot(my_char):
	if my_char.pot > 0:
		use = input('Utiliser une potion (+25)? Y/N:\n')
		if use.lower() == 'y':
			my_char.hp += 25
			if my_char.hp > my_char.max_hp:
				my_char.hp = my_char.max_hp
			my_char.pot -= 1
			print('Vous récuperez 25 points de vie !')
			print('Vous avez maintenant {} points de vie sur {}, et il vous reste {} potions.'.format(my_char.hp, my_char.max_hp, my_char.pot))
		if use.lower() == 'n':
			pass
		else:
			use_pot(my_char)
		return my_char.hp
	else:
		print('Désolé, vous n\'avez aucune potion en stock !')
	return my_char.hp

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
	print('# Welcome to the text RPG #')
	print('###########################')
	print('         - Jouer -         ')
	print('         - Aide -          ')
	print('         - Quitter -       ')
	print('       Bonne chance !      ')
	title_screen_selections()

def help_menu():
	print('###########################')
	print('# Welcome to the text RPG #')
	print('###########################')
	print('- Appuyez toujours sur entrée pour valider vos choix !')
	title_screen_selections()