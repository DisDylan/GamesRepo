#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int inGame = 1;
    while (inGame) {

        int numberPlayers = 0;
        printf("Jouer a 1 ou 2 joueur(s) ? \n");
        scanf("%d", &numberPlayers);
        int mysteryNumber = 0;

        if (numberPlayers == 1) {
            printf("Quelle difficulte choisissez vous ?\n1. FACILE\n2. MOYEN\n3. DIFFICILE\n");
            const int MIN = 1;
            int difficult;
            int maxNumber;
            scanf("%d", &difficult);
            switch (difficult) {
                case 1:
                    maxNumber = 100;
                    break;
                case 2:
                    maxNumber = 1000;
                    break;
                case 3:
                    maxNumber = 10000;
                    break;
                default:
                    break;
            }
            srand(time(NULL));
            mysteryNumber = (rand() % (maxNumber - MIN + 1)) + MIN;

        } else {
            mysteryNumber = 0;
            printf("Saisissez le nombre mystere a trouver: ");
            scanf("%d", &mysteryNumber);
        }

        int numberEntry = 0;
        int compteurCoups = 0;

        printf("=!=!=BIENVENUE A TOI=!=!=\n");
        printf("Tu dois trouver le bon nombre choisi par l'ordinateur..\n");
        //printf(".. attention ! Tu n'as que 7 essais !\n\n");

        do {
            printf("Entre un nombre : ");
            scanf("%d", &numberEntry);
            if (numberEntry > mysteryNumber) {
                printf("C'est moins !\n");
            } else if (numberEntry < mysteryNumber) {
                printf("C'est plus !\n");
            }
            compteurCoups++;
        } while (numberEntry != mysteryNumber);

        printf("Bravo, tu as trouve en %d coups !\n\n", compteurCoups);

        printf("Rejouer ?\n0 = NON\n1 = OUI\n");
        scanf("%d", &inGame);
    }

    return 0;
    }
