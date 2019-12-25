from random import *

"""
TODO:
	-self.cap skills pv et force DONE
	-arranger code, methode fight, soulager un peu la fonction 'main'
	-exec(pull request commit score)
"""

# Classe personnage
class Character():
	def __init__(self):
		self.hp = 10
		self.xp = 0
		self.pot = 1
		self.keys = 0
		self.strength = 1
		self.total_fp = 0
		self.total_vp = 0

# Classe héro(personnage)
class Hero(Character):

	def __init__(self, name):
		Character.__init__(self)
		self.name = name
		#self.skills_p = 0
		#self.agility = 1
		#self.intel = 1
		self.niveau = 1
		self.max_hp = self.hp

	def __repr__(self):
		return 'nom: {}, hp:{}, force: {}, potions: {}, clés: {}.'.format(self.name, self.hp, self.strength, self.pot, self.keys)

	def level_up(self):
		self.niveau += 1
		self.strength += 1
		self.max_hp += 5
		self.hp += 2
		self.cap = 20
		if (self.total_fp < self.cap) or (self.total_fp < self.cap):
			point = input('Pour mettre un point en Force [+1] tapez \'F\' [{}/{}]\nPour mettre votre point en Vie [+3] tapez \'V\' [{}/{}]\n'.format(self.total_fp, self.cap, self.total_vp, self.cap))
			if point.lower() == 'f':
				if self.total_fp < self.cap:
					self.strength += 1
					self.total_fp += 1
				else:
					print('Vous avez déjà placé les {} points maximum en force.'.format(self.cap))
					return self.level_up()
			elif point.lower() == 'v':
				if self.total_fp < self.cap:
					self.max_hp += 3
					self.hp += 3
					self.total_vp += 1
				else:
					print('Vous avez déjà placé les {} points maximum en vie.'.format(self.cap))
					return self.level_up()
			else:
				print('Commande introuvable, veuillez saisir à nouveau votre choix.')
				self.niveau -= 1
				self.strength -= 1
				self.max_hp -= 5
				self.hp -= 5
				self.level_up()
		else:
			return
		#self.skills_p += 1

# Classe ennemis(personnage)
class Ennemy(Character):

	races = ['Gobelin', 'Orc', 'Troll', 'Ogre']

	def __init__(self, race_index):
		Character.__init__(self)
		self.race = Ennemy.races[race_index]
		self.pot = randrange(0, 2)
		self.keys = randrange(0, 2)
		if self.race == 'Gobelin':
			self.hp = 4
		elif self.race == 'Orc':
			self.hp = 8
			self.strength = 3
		elif self.race == 'Troll':
			self.hp = 15
			self.strength = 5
		elif self.race == 'Ogre':
			self.hp = 25
			self.strength = 5

	def __repr__(self):
		return 'race: {},  hp:{}, force: {}, potions: {}, clés: {}.'.format(self.race, self.hp, self.strength, self.pot, self.keys)

	def make_boss(self):
		self.hp = int(self.hp * 1.6)
		self.xp = self.xp * 3
		self.strength = int(self.strength * 2)
		self.pot += 1

# Liste d'ennemis par zones
zones = ['plaines', 'mines', 'glaces', 'sables', 'enfers']
hero_name = input('Bienvenue, veuillez entrez le nom de votre personnage :\n')
my_char = Hero(hero_name)
index_race = 0
z_index = 0
actual_zone = zones[z_index]
ennemy = Ennemy(index_race)
nb_fight = 0
total_kills = 0

def use_pot():
	global my_char
	#print('Vous avez {} points de vie restants sur {}.'.format(my_char.hp, my_char.max_hp))
	if my_char.pot > 0:
		use = input('Utiliser une potion ? Y/N:\n')
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
			use_pot()
		return my_char.hp
	else:
		print('Désolé, vous n\'avez aucune potion en stock !')
	return my_char.hp

def main_game():
	global my_char
	global zones
	global index_race
	global z_index
	global nb_fight
	global total_kills
	way = input('Z : Tout droit\nQ : À gauche\nD : À droite\nQuel chemin prendre ?')
	if (way.lower() == 'z') or (way.lower() == 'q') or (way.lower() == 'd'):
		ennemy = Ennemy(index_race)
		#ennemy.race = Ennemy.races[index_race]
		if randrange(0, 101) < 15:
			ennemy.make_boss()
			print('Un boss est en approche !')
	else:
		print('Chemin inconnu ...')
		main_game()
	zone_boost()
	print('Un ennemi apparaît ! C\'est un {} des {}!'.format(ennemy.race, zones[z_index]))
	print('\nHP: {}/{}; Force: {}.\n'.format(my_char.hp, my_char.max_hp, my_char.strength))
	print('Vous vous battez à mort !')
	counter = 1
	max_enhp = ennemy.hp
	while (my_char.hp > 0) and (ennemy.hp > 0):
		use_pot()
		input('Appuyez sur entrée pour afficher le tour de combat suivant\n')
		my_char.hp -= ennemy.strength
		ennemy.hp -= my_char.strength
		print('-------------------------------\n{}e tour\n\n{} des {}:\nHP: {}/{}'.format(counter, ennemy.race, zones[z_index], ennemy.hp, max_enhp))
		print('\n{}:\nHP: {}/{}; Force: {}.\n-------------------------------'.format(my_char.name, my_char.hp, my_char.max_hp, my_char.strength))
		counter += 1
		if my_char.hp <= 0:
			print('Fin de partie ! {} adversaires battus !'.format(total_kills))
			exit()
		elif ennemy.hp <= 0:
			print('Bravo, vous avez abattu votre adversaire !')
			my_char.level_up()
			print('Montée au niveau {} !\n(+5 HP, +1 Force)'.format(my_char.niveau))
			print('\nHP: {}/{}; Force: {}.\n'.format(my_char.hp, my_char.max_hp, my_char.strength))
			my_char.pot += ennemy.pot
			print('Vous récupérez {} potions, vous en avez désormais {} dans l\'inventaire.'.format(ennemy.pot, my_char.pot))
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
						main_game()
				else:
					index_race += 1
					nb_fight = 0
					main_game()
			else:
				nb_fight += 1
				main_game()

def zone_boost():
	global actual_zone
	global ennemy
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

main_game()