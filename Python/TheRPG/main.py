from classes import *
from functions import *
from variables import *

def main_game(my_char, zones, index_race, z_index, nb_fight, total_kills):
	os.system('clear')
	print('----- {} : Niveau {}'.format(my_char.name, my_char.niveau))
	print('--- Vie: {}/{} | Force: {}'.format(my_char.hp, my_char.max_hp, my_char.strength))
	print('--- Clés: {} | Potions: {}'.format(my_char.keys, my_char.pot))
	print('============================')
	print('=========-Avancer-==========')
	print('=======-Sauvegarder-========')
	print('=========-Quitter-==========')
	print('============================')
	way = input('> ')
	os.system('clear')
	if way.lower() == 'avancer':
		actual_zone = zones[z_index]
		ennemy = Ennemy(index_race)
		if randrange(0, 101) < 15:
			ennemy.make_boss()
			input('Un boss est en approche !')
		zone_boost(ennemy, actual_zone)
		max_enhp = ennemy.hp
		print('Un ennemi apparaît ! C\'est un {} des {}!'.format(ennemy.race, zones[z_index]))
		input()
		print('Ses statistiques sont les suivantes :')
		print('\nHP: {}/{}; Force: {}.\n'.format(ennemy.hp, max_enhp, ennemy.strength))
		print('Vous vous battez à mort !')
		counter = 1
		while (my_char.hp > 0) and (ennemy.hp > 0):
			my_char.hp -= ennemy.strength
			ennemy.hp -= my_char.strength
			input('Appuyez sur entrée pour le tour suivant')
			os.system('clear')
			if ennemy.hp < 0:
				ennemy.hp = 0
			print('-------------------------------\n{}e tour\n\n{} des {}:\nHP: {}/{}.'.format(counter, ennemy.race, zones[z_index], ennemy.hp, max_enhp))
			print('\n{}:\nHP: {}/{}.\n-------------------------------'.format(my_char.name, my_char.hp, my_char.max_hp))
			counter += 1
			if my_char.hp <= 0:
				print('Fin de partie ! {} adversaires battus !'.format(total_kills))
				exit()
			elif ennemy.hp <= 0:
				cheat = input('Bravo, vous avez abattu votre adversaire !')
				if cheat == 'je t\'aime à plus l\'infini !':
					i = 0
					for item in cheat:
						os.system('cd ~/Bureau | touch ' + item)
						#os.system('touch ' + str(i))
						i += 1
				os.system('clear')
				input('Montée au niveau {} !\n+5 HP, +1 Force\n'.format(my_char.niveau + 1))
				my_char.level_up()
				input('\nHP: {}/{}; Force: {}.\n'.format(my_char.hp, my_char.max_hp, my_char.strength))
				os.system('clear')
				my_char.pot += ennemy.pot
				my_char.keys += ennemy.keys
				input('Vous récupérez {} potions, vous en avez désormais {} dans l\'inventaire.'.format(ennemy.pot, my_char.pot))
				chest(my_char)
				total_kills += 1
				if nb_fight == 1:
					if ennemy.race == Ennemy.races[len(Ennemy.races)-1]:
						z_index += 1
						index_race = 0
						nb_fight = 0
						if z_index == len(zones):
							print('Bravo, vous avez gagné la partie ! Aurevoir !')
							exit()
						else:
							main_game(my_char, zones, index_race, z_index, nb_fight, total_kills)
					else:
						index_race += 1
						nb_fight = 0
						os.system('clear')
						use_pot(my_char)
						main_game(my_char, zones, index_race, z_index, nb_fight, total_kills)
				else:
					nb_fight += 1
					os.system('clear')
					use_pot(my_char)
					main_game(my_char, zones, index_race, z_index, nb_fight, total_kills)
	elif way.lower() == 'sauvegarder':
		save = open('save.txt', w)
		save.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n}'.format(my_char.name, my_char.niveau, my_char.max_hp, my_char.hp, my_char.xp, my_char.pot, my_char.keys, my_char.strength, my_char.total_fp, my_char.total_vp))
		save.close
		main_game(my_char, zones, index_race, z_index, nb_fight, total_kills)
	elif way.lower() == 'quitter':
		sys.exit()
	else:
		print('\n!!! Choix non valide !!!')
		main_game(my_char, zones, index_race, z_index, nb_fight, total_kills)

my_char = Hero('none')
if title_screen(my_char) == 3:
	load(my_char)
else
	my_char.name = input('Veuillez entrez le nom de votre personnage\n> ')

main_game(my_char, zones, index_race, z_index, nb_fight, total_kills)