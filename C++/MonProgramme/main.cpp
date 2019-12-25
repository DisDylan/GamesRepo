#include <iostream> /// Inclut la bibliothèque iostream (affichage de texte)
#include <string> /// Inclut la bibliothèque string, pour utiliser les chaines de caractères
#include <vector> /// Nécéssaire pour la création de tableaux dynamiques
#include <cmath> /// Bibliothèque avec des fonctions mathématiques
#include "math.h"
#include "seconds.h"
#include "moyenneArray.h"
using namespace std;

int main()
{
    int const nombreMeilleursScores(5);
    vector<int> meilleursScores;

    meilleursScores.push_back(96);
    meilleursScores.push_back(67);
    meilleursScores.push_back(32);
    meilleursScores.push_back(143);
    meilleursScores.push_back(76887253);
    meilleursScores.push_back(2);
    meilleursScores.push_back(567);

    for (int i(0); i < meilleursScores.size(); i++)
    {
        cout << meilleursScores[i] << endl;
    }

    return 0;
}
