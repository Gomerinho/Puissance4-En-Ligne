import numpy as np
import pygame
import sys
import math

BLEU = (0, 0, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)

COMPTEUR_LIGNE = 6
COMPTEUR_COLONNE = 7


def creation_plateau():
    plateau = np.zeros((COMPTEUR_LIGNE, COMPTEUR_COLONNE))
    return plateau


def piece_tombe(plateau, ligne, col, piece):
    plateau[ligne][col] = piece


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
            if plateau[l][c] == piece and plateau[l][c + 1] == piece and plateau[l][c + 2] == piece and plateau[l][c + 3] == piece:
                return True

    # Verification de la verticale
    for c in range(COMPTEUR_COLONNE):
        for l in range(COMPTEUR_LIGNE - 3):
            if plateau[l][c] == piece and plateau[l + 1][c] == piece and plateau[l + 2][c] == piece and plateau[l + 3][c] == piece:
                return True

    # Verification des diagonales positive :
    for c in range(COMPTEUR_COLONNE - 3):
        for l in range(COMPTEUR_LIGNE - 3):
            if plateau[l][c] == piece and plateau[l + 1][c + 1] == piece and plateau[l + 2][c + 2] == piece and plateau[l + 3][c + 3] == piece:
                return True

    # Verification des diagonales positive :
    for c in range(COMPTEUR_COLONNE - 3):
        for l in range(3, COMPTEUR_LIGNE):
            if plateau[l][c] == piece and plateau[l - 1][c + 1] == piece and plateau[l - 2][c + 2] == piece and plateau[l - 3][c + 3]== piece:
                return True


def dessin_plateau(plateau):
    for c in range(COMPTEUR_COLONNE):
        for r in range(COMPTEUR_LIGNE):
            pygame.draw.rect(ecran, BLEU,
                             (c * TAILLE_CARRE, r * TAILLE_CARRE + TAILLE_CARRE, TAILLE_CARRE, TAILLE_CARRE))
            pygame.draw.circle(ecran, NOIR, (
            int(c * TAILLE_CARRE + TAILLE_CARRE / 2), int(r * TAILLE_CARRE + TAILLE_CARRE + TAILLE_CARRE / 2)), RAYON)
    for c in range(COMPTEUR_COLONNE):
        for r in range(COMPTEUR_LIGNE):
            if plateau[r][c] == 1:
                pygame.draw.circle(ecran, ROUGE, (
                    int(c * TAILLE_CARRE + TAILLE_CARRE / 2), hauteur - int(r * TAILLE_CARRE + TAILLE_CARRE / 2)),
                                   RAYON)
            elif plateau[r][c] == 2:
                pygame.draw.circle(ecran, JAUNE, (
                    int(c * TAILLE_CARRE + TAILLE_CARRE / 2), hauteur - int(r * TAILLE_CARRE + TAILLE_CARRE / 2)),
                                   RAYON)
    pygame.display.update()


plateau = creation_plateau()
fin_partie = False
tour = 0

pygame.init()

TAILLE_CARRE = 100
largeur = COMPTEUR_COLONNE * TAILLE_CARRE
hauteur = (COMPTEUR_LIGNE + 1) * TAILLE_CARRE

RAYON = int(TAILLE_CARRE / 2 - 5)

taille = (largeur, hauteur)

ecran = pygame.display.set_mode(taille)
dessin_plateau(plateau)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 35)


while not fin_partie:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()

        if evenement.type == pygame.MOUSEMOTION:
            pygame.draw.rect(ecran, NOIR, (0,0, largeur, TAILLE_CARRE))
            posx = evenement.pos[0]
            if tour == 0:
                pygame.draw.circle(ecran, ROUGE, (posx, int(TAILLE_CARRE / 2)), RAYON)
            else:
                pygame.draw.circle(ecran, JAUNE, (posx, int(TAILLE_CARRE / 2)), RAYON)
        pygame.display.update()

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(ecran, NOIR, (0, 0, largeur, TAILLE_CARRE))
            # print(evenement.pos)
            if tour == 0:
                posx = evenement.pos[0]
                col = math.floor(posx / TAILLE_CARRE)
                if col_valid(plateau, col):
                    ligne = ligne_valid(plateau, col)
                    piece_tombe(plateau, ligne, col, 1)
                    if tour_gagnant(plateau, 1):
                        label = myfont.render("Le joueur 1 a gagné", 1, ROUGE)
                        ecran.blit(label, (40,10))
                        fin_partie = True

            else:
                posx = evenement.pos[0]
                col = math.floor(posx / TAILLE_CARRE)
                if col_valid(plateau, col):
                    ligne = ligne_valid(plateau, col)
                    piece_tombe(plateau, ligne, col, 2)
                    if tour_gagnant(plateau, 2):
                        label = myfont.render("Le joueur 2 a gagné", 1, JAUNE)
                        ecran.blit(label, (40, 10))
                        fin_partie = True

            affichage_plateau(plateau)
            dessin_plateau(plateau)
            tour += 1
            tour = tour % 2

            if fin_partie :
                pygame.time.wait(3000)
