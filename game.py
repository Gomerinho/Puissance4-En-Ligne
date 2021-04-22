import numpy as np
import pygame
import sys

COMPTEUR_LIGNE = 6
COMPTEUR_COLONNE = 7


def creation_plateau():
    plateau = np.zeros((COMPTEUR_LIGNE, COMPTEUR_COLONNE))
    return plateau


def piece_tombe(plateau, row, col, piece):
    plateau[row][col] = piece


def col_valid(plateau, col):
    return plateau[COMPTEUR_LIGNE - 1][col] == 0


def ligne_valid(plateau, col):
    for l in range(COMPTEUR_LIGNE):
        if plateau[l][col] == 0:
            return l


def affichage_plateau(plateau):
    print(np.flip(plateau, 0))


def tour_gagnant(plateau, piece):
    # Horizontal voir si il y a un gagnant
    for c in range(COMPTEUR_COLONNE - 3):
        for l in range(COMPTEUR_LIGNE):
            if plateau[l][c] == piece and plateau[l][c + 1] == piece and plateau[l][c + 2] and plateau[l][c + 3]:
                return True

    # Verification de la verticale
    for c in range(COMPTEUR_COLONNE):
        for l in range(COMPTEUR_LIGNE - 3):
            if plateau[l][c] == piece and plateau[l + 1][c] == piece and plateau[l + 2][c] and plateau[l + 3][c]:
                return True

    # Verification des diagonales positive :
    for c in range(COMPTEUR_COLONNE - 3):
        for l in range(COMPTEUR_LIGNE - 3):
            if plateau[l][c] == piece and plateau[l + 1][c + 1] == piece and plateau[l + 2][c + 2] and plateau[l + 3][
                c + 3]:
                return True

    # Verification des diagonales positive :
    for c in range(COMPTEUR_COLONNE - 3):
        for l in range(3, COMPTEUR_LIGNE):
            if plateau[l][c] == piece and plateau[l + -1][c + 1] == piece and plateau[l - 2][c + 2] and plateau[l - 3][c + 3]:
                return True


def dessin_plateau(plateau):
    for


plateau = creation_plateau()
fin_partie = False
tour = 0

pygame.init()

TAILLE_CARRE = 100
largeur = COMPTEUR_COLONNE * TAILLE_CARRE
hauteur = (COMPTEUR_LIGNE + 1) * TAILLE_CARRE

taille = (largeur, hauteur)

ecran = pygame.display.set_mode(taille)

while not fin_partie:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            print('')
        #     if tour == 0:
        #         col =
        #         if col_valid(plateau, col):
        #             ligne = ligne_valid(plateau, col)
        #             piece_tombe(plateau, ligne, col, 1)
        #             if tour_gagnant(plateau, 1):
        #                 print("Le joueur 1 gagne !! Bravo !!")
        #                 fin_partie = True
        #
        #     else:
        #         col = int(input("Player 2 make your selection"))
        #         if col_valid(plateau, col):
        #             ligne = ligne_valid(plateau, col)
        #             piece_tombe(plateau, ligne, col, 2)
        #             if tour_gagnant(plateau, 2):
        #                 print("Le joueur 2 gagne !! Bravo !!")
        #                 fin_partie = True
        # affichage_plateau(plateau)
        # tour += 1
        # tour = tour % 2






