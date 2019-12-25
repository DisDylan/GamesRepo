import os
import pandas
from random import *

class Character(object):

    randomInit = ["descend de son carrosse", "est sortie de sa capsule", "sort de terre", "tombe du ciel",  "est envoyé par les dieux", "arrive en moonwalk", "s'est perdu #Denis", "prend les armes", "déménage", "enleve sa cape d'invisibilité", "recherche à manger", "pose son café", "releve ses manches", "se réveille", "est push sur le terrain", "débarque à dos de licorne", "veut tout casser", "est pret à en decoudre", "a la grippe", "est pret pour le stand up", "rassemble ses chakras", "sort son chéquier"]    
    def __init__(self, nom, titre, arme, min_dmg, max_dmg, percent, vie):
        self.nom = nom
        self.titre = titre
        self.arme = arme
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.percent = percent
        self.vie = vie
        print('{} {} {} avec {} !'.format(self.titre, self.nom, choice(Character.randomInit), self.arme))

    def __repr__(self):
        return '{} {} avec {} points de vie.'.format(self.titre, self.nom, self.vie)

    def full_show(self):
        return 'Character: nom({}), titre({}), arme({}), dégats min({}), dégats max({}), pourcentage de touche({}), points de vie({})'.format(self.nom, self.titre, self.arme, self.min_dmg, self.max_dmg, self.percent, self.vie)

    def fight(self, ennemy):
        global chars_comp
        en = '{} {}'.format(ennemy.titre, ennemy.nom)
        sf = '{} {}'.format(self.titre, self.nom)
        print('HA ! {} s\'attaque à {} !'.format(sf, en))
        en_dmg = randrange(ennemy.min_dmg, ennemy.max_dmg)
        sf_dmg = randrange(self.min_dmg, self.max_dmg)
        if self.nom == "Ines" and ennemy.nom == "Hachem" or self.nom == "Hachem" and ennemy.nom == "Ines":
            print("La famille, on se bat pas !")
        elif self.nom == "Ludovic" and ennemy.nom == "Dylan" or self.nom == "Dylan" and ennemy.nom == "Ludovic":
            print("Les développeurs utilisent un hack, leur chance de toucher augmente de 20, leurs vie aussi et font en moyenne 20 dégats en plus")
            self.min_dmg += 20
            self.max_dmg += 20
            self.percent += 20
            self.vie += 20
            ennemy.min_dmg += 20
            ennemy.max_dmg += 20
            ennemy.percent += 20
            ennemy.vie += 20
        else:
            if randrange(0, 100) < ennemy.percent:
                print('{} inflige {} a {}'.format(en, en_dmg, sf))
                self.vie -= en_dmg
            else:
                print('{} a raté son coup'.format(en))                    
            if randrange(0, 100) < self.percent:
                print('{} inflige {} a {}'.format(sf, sf_dmg, en))
                ennemy.vie -= sf_dmg
            else:
                print('{} a raté son coup'.format(sf))                            
            if  randrange(0,100) < 10:
                print('\n{} trouve un café senseo et restaure 20 hp'.format(sf))
                self.vie += 20        
            if  randrange(0,100) < 10:
                print('\nBOUM ! Samba Sauvage apparait et lance GAOUUU il inflige 20 de degat à {} et {}\n'.format(en, sf))
                self.vie -= 20
                ennemy.vie -= 20        
            if  randrange(0,100) < 10:
                print("\nBOUM ! Rafik apparait et vous piege dans algorithme et vous force a vous rebattre\n")
                rafikNb = randrange(1,5)
                print('{} fois !!\n'.format(rafikNb))
                i = 0
                while i < rafikNb:
                    print('{} s\'attaque à nouveau à {} !'.format(sf, en))
                    print('Il lui inflige {} points de dégats et en subi {}\n'.format(sf_dmg, en_dmg))
                    self.vie -= en_dmg
                    ennemy.vie -= sf_dmg
                    i += 1
        c1 = '\n{} a encore {} points de vie.'.format(sf, self.vie)
        c2 = '{} a encore {} points de vie.'.format(en, ennemy.vie)          
        if randrange(0,100) < 5:
            print("\nBOUM ! Samba Sauvage apparait et lance FRAPPE LOURDE il detruit ", en , " et ", sf, "\n")
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        elif ennemy.vie > 0 and self.vie > 0:
            print(c1)
            print(c2)
        elif ennemy.vie <= 0 and self.vie > 0:
            print(c1)
            print('{} retourne dans sa pokéball ! Aurevoir {} !'.format(en, en))
            chars_comp.remove(ennemy)
        elif ennemy.vie <= 0 and self.vie <= 0:
            print('Doublette ! {} et {} se sont entretués !'.format(en, sf))
            chars_comp.remove(ennemy)
            chars_comp.remove(self)
        else:
            print("\n", c2)
            print('{} retourne dans sa pokéball ! Aurevoir {} !'.format(sf, sf))
            chars_comp.remove(self)

class Arme:

    def __init__(self, nom, damage_min, damage_max, percent):
        self.nom = nom
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.percent = percent

weapon_list = []
weapon_list.append(Arme('un pistolet', 12, 15, 80))
weapon_list.append(Arme('un couteau', 5, 9, 95))
weapon_list.append(Arme('un M16', 20, 24, 65))
weapon_list.append(Arme('un AK47', 24, 30, 50))
weapon_list.append(Arme('un lance-roquette', 60, 80, 20))
weapon_list.append(Arme('un sniper', 200, 201, 5))

titres = ['Princesse', 'Petite fée', 'Vagabond', 'Voleur', 'Génie', 'Collabo', 'Dragon', 'Tyran', 'Dictateur', 'Leader', 'Sa majesté', 'Chef', 'Sauvage', 'Roi de la jungle', 'Chasseur', 'Kangourou']

vies = []
for i in range(140, 151):
    vies.append(i)

f = pandas.read_csv('DataJungleFighterz.csv')
f = f.values.tolist()

new_f = []
for i in f:
    new_f = new_f + i

chars_comp = []
for i in new_f:
    weap = choice(weapon_list)
    chars_comp.append(Character(i, choice(titres), weap.nom, weap.damage_min, weap.damage_max, weap.percent, choice(vies)))

def reset_game():
    global chars_comp
    chars_comp = []
    for i in new_f:
        weap = choice(weapon_list)
        chars_comp.append(Character(i, choice(titres), weap.nom, weap.damage_min, weap.damage_max, weap.percent, choice(vies)))

def end_game():
    new_game = input('New game ? Y/N :')
    if new_game.lower() == 'y':
        reset_game()
        game()
    elif new_game.lower() == 'n':
        return '\nAurevoir ! Merci d\'avoir joué !'
    else:
        end_game()

def game():
    global chars_comp
    continue_game = input('\nAppuyez sur entrée pour le combat suivant ou entrez une touche auparavant pour quitter\n')
    if continue_game == '':
        if len(chars_comp) > 1:
            char_a = choice(chars_comp)
            chars_comp.remove(char_a)
            char_b = choice(chars_comp)
            chars_comp.append(char_a)
            char_a.fight(char_b)
            print("\n {} Fighterz En Vie:\n".format(len(chars_comp)))
            chars_comp = sorted(chars_comp, key= lambda char: char.vie, reverse=True)
            for i in chars_comp:
                print(i)
            if len(chars_comp) == 0:
                print('Personne n\'a gagné :(')
                end_game()
            elif len(chars_comp) == 1:
                winner = chars_comp[0]
                print('\n{} {} a gagné ! BRAVOOOOOOOOOOO !'.format(winner.titre, winner.nom))
                end_game()
            else:
                game()
    elif continue_game == 'showall':
        for i in chars_comp:
            print(i.full_show())
        game()
    elif continue_game == 'hack':
        hacking = input('Commande a executer : \n')
        exec(hacking)
        game()
    else:
        return print('Aurevoir, merci et à bientôt !')
game()