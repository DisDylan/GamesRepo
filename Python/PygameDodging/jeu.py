import pygame
import time

BLUE_COLOR = (113, 177, 227)
WHITE_COLOR = (255, 255, 255)

pygame.init() # Initialisation du module pygame

SURFACE_W = 600
SURFACE_H = 700
OCTOCAT_W = 100
OCTOCAT_H = 100
STONE_W = 200
STONE_H = 200

surface = pygame.display.set_mode((SURFACE_W, SURFACE_H)) # On définit la taille de la fenêtre
pygame.display.set_caption('Octocat run') # On définit le titre de notre jeu
horloge = pygame.time.Clock()

img = pygame.image.load('octocat.png')
img_rock = pygame.image.load('stone.png')

def stones(x_stone, y_stone, espace):
    surface.blit(img_rock, (x_stone, y_stone))
    

def rejoueOuQuitte():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None


def creaTexteObj(texte, police):
    texteSurface = police.render(texte, True, WHITE_COLOR)
    return texteSurface, texteSurface.get_rect()


def message(texte):
    GOTexte = pygame.font.Font('Girassol-Regular.ttf', 100)
    petitTexte = pygame.font.Font('Girassol-Regular.ttf', 20)

    GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte)
    GOTexteRect.center = SURFACE_W / 2, ((SURFACE_H / 2) - 50)
    surface.blit(GOTexteSurf, GOTexteRect)
    petitTexteSurf, petitTexteRect = creaTexteObj("Appuyez sur une touche pour relancer !", petitTexte)
    petitTexteRect.center = SURFACE_W / 2, ((SURFACE_H / 2) + 50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)


    while rejoueOuQuitte() == None:
        horloge.tick()

    main()


def gameOver():
    message("!! CRASH !!")


def octocat(x, y, image):
    """
    /def: Ajoute l'image sur la surface
    /param: position axe x, y et l'image a ajouter
    /return: null
    """
    surface.blit(image, (x, y)) # Ajout par dessus la surface l'image indiquée


def main():
    """
    /def: Fonction principale qui permet de lancer le jeu et de rafraichir
    /param: null
    /return: null
    """

    x_pos = 400
    Y_POS = SURFACE_H - 120
    x_move = 0
    speed = 10

    game_over = False

    pygame.key.set_repeat(1, 10)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if x_pos > 0 and x_pos < (SURFACE_W - 100):
                    if event.key == pygame.K_LEFT:
                        x_pos -= speed
                    elif event.key == pygame.K_RIGHT:
                        x_pos += speed
                else:
                    if x_pos <= 0:
                        x_pos = 1
                    elif x_pos >= (SURFACE_W - 100):
                        x_pos = SURFACE_W - 101
        
        #x_pos += x_move

        background = pygame.image.load('background.jpg')
        surface.blit(background, (0, 0))
        octocat(x_pos, Y_POS, img) # On affiche le personnage

        if x_pos > (SURFACE_W - 150) or x_pos < 20:
            gameOver()

        pygame.display.update() # On rafraichit la fenêtre pour prendre en compte le(s) changement(s)

if __name__ == '__main__':
    main()

pygame.quit()
quit()