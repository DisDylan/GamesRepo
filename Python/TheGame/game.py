""" https://www.youtube.com/watch?v=ERLT1iU0DVY """

# Python Text RPG
# DisDylan (github)

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


##### Player Setup #####
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []

myPlayer = Player()


##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == "jouer":
        start_game() # placeholder until written
    elif option.lower() == "aide":
        help_menu()
    elif option.lower() == "quitter":
        sys.exit()
    while option.lower() not in ['jouer', 'aide', 'quitter']:
        print("S'il vous plaît, entrez une commande valide.")
        if option.lower() == "jouer":
            start_game() # placeholder until written
        elif option.lower() == "aide":
            help_menu()
        elif option.lower() == "quitter":
            sys.exit()
    
def title_screen():
    os.system('clear')
    print('###########################')
    print('# Welcome to the text RPG #')
    print('###########################')
    print('         - Jouer -         ')
    print('         - Aide -          ')
    print('         - Quitter -       ')
    title_screen_selections()

def help_menu():
    print('###########################')
    print('# Welcome to the text RPG #')
    print('###########################')
    print('- Utilisez haut, bas gauche et droit pour bouger')
    print('- Tapez vos commandes pour les executer')
    print('- Utilisez "examiner" pour inspecter quelque chose')
    title_screen_selections()


##### GAME FUNCTIONALITY #####
def start_game():


##### MAP #####
"""
 1  2  3  4
-------------
|  |  |  |  | A
-------------
|  |  |  |  | B
-------------
|  |  |  |  | C
-------------
|  |  |  |  | D
-------------
"""
# Exemple map
## Player start at B2

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examiner'
SOLVED = False
UP = 'haut', 'nord'
DOWN = 'bas', 'sud'
LEFT = 'gauche', 'ouest'
RIGHT = 'droite', 'est'

solved_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'b2': {
        ZONENAME: "Maison",
        DESCRIPTION = 'C\'est votre maison'
        EXAMINATION = 'Votre maison n\'a pas changé, vous ne trouvez rien'
        SOLVED = False
        UP = 'a2'
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'b3'
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'd1': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examiner'
        SOLVED = False
        UP = 'haut', 'nord'
        DOWN = 'bas', 'sud'
        LEFT = 'gauche', 'ouest'
        RIGHT = 'droite', 'est'
    },
    
}