#include "personnage.h"
#define FILEPATH "D:/INTECH/Alternance-S9-S10/langageC/personnages.txt"

int main() {
    Personnage personnages[10];
    int tot = listePersonnages(personnages);
    afficherPersonnage(personnages, tot);
    sexe(personnages, tot);
    enregistrePersonnage();

    return EXIT_SUCCESS;
}

int listePersonnages(Personnage *personnages) {
    int ligne = 0;
    FILE *fichier = fopen(FILEPATH, "r");
    if (fichier == NULL) perror("Erreur");
    while (fscanf(fichier, "%d/%[^/]/%c/%d",
                  &personnages[ligne].id,
                  &personnages[ligne].nom,
                  &personnages[ligne].sexe,
                  &personnages[ligne].anneeNaissance) == 4)
        ++ligne;

    fclose(fichier);
    return ligne;
}

void afficherPersonnage(Personnage *personnages, int ligne) {
    for (int i = 0; i < ligne; i++) {
        Personnage y = personnages[i];
        printf("ID: %d \t Nom: %s \t Sexe: %c \t Annee de naissance: %d\n", y.id, y.nom, y.sexe, y.anneeNaissance);
    }
}

void sexe(Personnage *personnages, int ligne) {
    int totH;
    int totF;
    totH = 0;
    totF = 0;
        for (int i = 0; i < ligne; i++) {
            Personnage y = personnages[i];
            if (y.sexe == 'H') {
                ++totH;
            } else
                ++totF;
        }
    printf("Nombre d'homme: %d \t Nombre de Femme: %d \t", totH, totF);
}

void enregistrePersonnage() {
    Personnage y;
    printf("Saisir : ID Nom Sexe Annee de Naissance :\n");
    scanf("%d %s %c %d", &y.id,
          &y.nom,
          &y.sexe,
          &y.anneeNaissance);
    FILE *fichier = fopen(FILEPATH, "a");
    if (fichier == NULL) perror("Erreur");
    fprintf(fichier, "%d/%s/%c/%d\n", y.id, y.nom, y.sexe, y.anneeNaissance);
}


