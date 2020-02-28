#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int inGame = 1;
    while (inGame){
        const int MAX = 100, MIN = 1;
        srand(time(NULL));
        int mysteryNumber = (rand() % (MAX - MIN + 1)) + MIN;
        
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
