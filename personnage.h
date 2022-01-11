#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define FILENAME "D:/INTECH/Alternance-S9-S10/langageC/personnages.txt"

typedef struct Personnage {
    int id;
    char nom[20];
    char sexe;
    int anneeNaissance;
} Personnage;

int listePersonnages(Personnage*);
void afficherPersonnage(Personnage*, int);
void sexe(Personnage*, int);
void enregistrePersonnage();