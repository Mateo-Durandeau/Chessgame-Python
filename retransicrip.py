from script_load_instance import *
from global_var import *


################################################################################
    # Fonction de retranscription entre le 2D et pygame
################################################################################

def retranscription_pos(x_pos, y_pos):
    """Retranscrit la position x et y en case d'un tableau bi-dimention --> s'effectuer pour la gestion des clics """

    if pos_0 <= y_pos < pos_1:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 0
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 0
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 0
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 0
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 0
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 0
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 0
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 0
    elif pos_1 <= y_pos < pos_2:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 1
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 1
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 1
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 1
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 1
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 1
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 1
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 1
    elif pos_2 <= y_pos < pos_3:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 2
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 2
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 2
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 2
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 2
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 2
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 2
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 2
    elif pos_3 <= y_pos < pos_4:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 3
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 3
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 3
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 3
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 3
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 3
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 3
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 3
    elif pos_4 <= y_pos < pos_5:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 4
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 4
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 4
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 4
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 4
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 4
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 4
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 4
    elif pos_5 <= y_pos < pos_6:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 5
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 5
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 5
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 5
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 5
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 5
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 5
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 5
    elif pos_6 <= y_pos < pos_7:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 6
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 6
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 6
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 6
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 6
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 6
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 6
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 6
    elif pos_7 <= y_pos <= pos_8:
        if pos_0 <= x_pos < pos_1:
            case_x, case_y = 0, 7
        elif pos_1 <= x_pos < pos_2:
            case_x, case_y = 1, 7
        elif pos_2 <= x_pos < pos_3:
            case_x, case_y = 2, 7
        elif pos_3 <= x_pos < pos_4:
            case_x, case_y = 3, 7
        elif pos_4 <= x_pos < pos_5:
            case_x, case_y = 4, 7
        elif pos_5 <= x_pos < pos_6:
            case_x, case_y = 5, 7
        elif pos_6 <= x_pos < pos_7:
            case_x, case_y = 6, 7
        elif pos_7 <= x_pos <= pos_8:
            case_x, case_y = 7, 7
    
    #print(chess_2d[case_y][case_x])
    return case_x, case_y

################################################################################
    # retranscrit les cases en valeurs précise
################################################################################

def retranscription_case(case_x, case_y):
    """
    retranscris un numéro de case en position 

    utile pour les déplacements et l'échec et mat

    """

    if case_x == 0:
        pos_x = pos_0
    elif case_x == 1:
        pos_x = pos_1
    elif case_x == 2:
        pos_x = pos_2
    elif case_x == 3:
        pos_x = pos_3
    elif case_x == 4:
        pos_x = pos_4
    elif case_x == 5:
        pos_x = pos_5
    elif case_x == 6:
        pos_x = pos_6
    elif case_x == 7:
        pos_x = pos_7
    

    if case_y == 0:
        pos_y = pos_0
    elif case_y == 1:
        pos_y = pos_1
    elif case_y == 2:
        pos_y = pos_2
    elif case_y == 3:
        pos_y = pos_3
    elif case_y == 4:
        pos_y = pos_4
    elif case_y == 5:
        pos_y = pos_5
    elif case_y == 6:
        pos_y = pos_6
    elif case_y == 7:
        pos_y = pos_7


    return pos_x, pos_y

################################################################################
    # retourne la pièce qui correspond à la case du tableau 
################################################################################

def retranscription_piece(chess_2d, case_x, case_y):
    """
    retourne le numéro d'une pièce par rapport à un tableau 2D
    """
    return chess_2d[case_y][case_x]


################################################################################
    # Gestion de la pièce séléctionné ( cette fonction ne peux pas être déclaré dans un autre fichier jsp pourquoi)
################################################################################

def retranscription_number(number):
    """ Retourne une pièce par rapport à son numéro sur le tableau 2D"""
    piece_list = [
        0, black_tour1, black_cavalier1, black_fou1, black_reine, black_roi, black_fou2,
        black_cavalier2, black_tour2, black_pion1, black_pion2, black_pion3, black_pion4,
        black_pion5, black_pion6, black_pion7, black_pion8, white_pion1, white_pion2,
        white_pion3, white_pion4, white_pion5, white_pion6, white_pion7, white_pion8,
        white_tour1, white_cavalier1, white_fou1, white_reine, white_roi, white_fou2,
        white_cavalier2, white_tour2
    ]

    if 0 <= number < len(piece_list):
        return piece_list[number]
    else:
        return None


def type_of_piece(number_piece):
    """ Retour le type de la pièce pour gerer les déplacement par rapport au numéro de piece sur la tableau 2D"""
    type_piece = "none"
    if 9 <= number_piece <= 16:
        #print("Pion noir")
        type_piece = "Pion noir"
    elif 17 <= number_piece <= 24:
        #print("Pion blanc")
        type_piece = "Pion blanc"
    elif number_piece == 1 or number_piece == 8:
       # print("Tour noir")
        type_piece = "Tour noir"
    elif number_piece == 25 or number_piece == 32:
       # print("Tour blanche")
        type_piece = "Tour blanche"
    elif number_piece == 2 or number_piece == 7:
       # print("Cavalier noir")
        type_piece = "Cavalier noir"
    elif number_piece == 26 or number_piece == 31:
       # print("Cavalier blanc")
        type_piece = "Cavalier blanc"
    elif number_piece == 3 or number_piece == 6:
       # print("Fou noir")
        type_piece = "Fou noir"
    elif number_piece == 27 or number_piece == 30:
       # print("Fou blanc")
        type_piece = "Fou blanc"
    elif number_piece == 4:
       # print("Reine noir")
        type_piece = "Reine noir"
    elif number_piece == 5:
       # print("Roi noir")
        type_piece = "Roi noir"
    elif number_piece == 28:
       # print("Reine blanche")
        type_piece = "Reine blanche"
    elif number_piece == 29:
       # print("Roi blanc")
        type_piece = "Roi blanc"
    else: 
       print("Pas de piece selectionner")
    return type_piece
