#include "moyenneArray.h"

double moyenneTableau(double tableau[], double tailleTableau)
{
    double moyenne(0);
    for (int i(0); i < tailleTableau; i++)
    {
        moyenne += tableau[i];
    }
    return moyenne /= tailleTableau;
}
