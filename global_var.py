################################################################################
    # Variables global
################################################################################

# peut ne pas etre fonctionnel avec deux valeurs qui ne seraient pas égal
WIDTH = 800
HEIGHT = WIDTH

# taille d'une case
rect_size_x = WIDTH //8

# positionnement des cases pour les pièces 
pos_0 = 0
pos_1 = rect_size_x * 1
pos_2 = rect_size_x * 2
pos_3 = rect_size_x * 3
pos_4 = rect_size_x * 4
pos_5 = rect_size_x * 5
pos_6 = rect_size_x * 6
pos_7 = rect_size_x * 7
pos_8 = rect_size_x * 8


# initialisation du positionnement de la souris
mouse_x = 0
mouse_y = 0

# tableau 2D du jeu d'échec
chess_2d = [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 10, 11, 12, 13, 14, 15, 16],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [17, 18, 19, 20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29, 30, 31, 32]
           ]


# tableau des déplacements possible lors de l'echec 
tab_check = []