from random import *

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
		if (self.total_fp < self.cap) and (self.total_fp < self.cap):
			point = input('Mettre un point en Force [+1] ; [{}/{}]\nOU\nMettre un point en Vie [+3] ; [{}/{}]\n> '.format(self.total_fp, self.cap, self.total_vp, self.cap))
			if point.lower() == 'force':
				if self.total_fp < self.cap:
					self.strength += 1
					self.total_fp += 1
				else:
					print('Vous avez déjà placé les {} points maximum en force.'.format(self.cap))
					return self.level_up()
			elif point.lower() == 'vie':
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