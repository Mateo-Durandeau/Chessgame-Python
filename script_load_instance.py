import pygame
from script_class_game import *

################################################################################
    # Chargement des pièces
################################################################################

def load_piece(TOUR):
    """ Chargement des pièces si elles sont en vie """

    all_sprites = pygame.sprite.Group()

    tab_piece = [white_pion1, white_pion2, white_pion3, white_pion4, white_pion5, white_pion6, white_pion7, white_pion8, 
                    black_pion1, black_pion2, black_pion3, black_pion4, black_pion5, black_pion6, black_pion7, black_pion8, 
                    white_tour1, white_tour2, black_tour1, black_tour2, 
                    white_cavalier1, white_cavalier2, black_cavalier1, black_cavalier2, 
                    white_fou1, white_fou2, black_fou1, black_fou2, 
                    white_roi, black_roi, white_reine, black_reine]
    
    for piece_selected in tab_piece: 
        if piece_selected.life == True: 
            if TOUR == 2 and piece_selected.turn == True: 
                piece_selected.rotate(180)  # Pivote la pièce de 180 degrés
                piece_selected.turn = False
            elif TOUR == 1 and piece_selected.turn == True:
                piece_selected.rotate(180)  # Pivote la pièce de 180 degrés
                piece_selected.turn = False
            
            
            # Ajout au groupe de sprite
            all_sprites.add(piece_selected)

    return all_sprites


################################################################################
    # Initialisation des pièces en variable global
################################################################################

white_pion1 = Pion('white', pos_0, pos_6, 'image/pion_blanc.png', 0, 6, 17)
white_pion2 = Pion('white', pos_1, pos_6, 'image/pion_blanc.png', 1, 6, 18)
white_pion3 = Pion('white', pos_2, pos_6, 'image/pion_blanc.png', 2, 6, 19)
white_pion4 = Pion('white', pos_3, pos_6, 'image/pion_blanc.png', 3, 6, 20)
white_pion5 = Pion('white', pos_4, pos_6, 'image/pion_blanc.png', 4, 6, 21)
white_pion6 = Pion('white', pos_5, pos_6, 'image/pion_blanc.png', 5, 6, 22)
white_pion7 = Pion('white', pos_6, pos_6, 'image/pion_blanc.png', 6, 6, 23)
white_pion8 = Pion('white', pos_7, pos_6, 'image/pion_blanc.png', 7, 6, 24)

black_pion1 = Pion('black', pos_0, pos_1, 'image/pion_noir.png', 0, 1, 9)
black_pion2 = Pion('black', pos_1, pos_1, 'image/pion_noir.png', 1, 1, 10)
black_pion3 = Pion('black', pos_2, pos_1, 'image/pion_noir.png', 2, 1, 11)
black_pion4 = Pion('black', pos_3, pos_1, 'image/pion_noir.png', 3, 1, 12)
black_pion5 = Pion('black', pos_4, pos_1, 'image/pion_noir.png', 4, 1, 13)
black_pion6 = Pion('black', pos_5, pos_1, 'image/pion_noir.png', 5, 1, 14)
black_pion7 = Pion('black', pos_6, pos_1, 'image/pion_noir.png', 6, 1, 15)
black_pion8 = Pion('black', pos_7, pos_1, 'image/pion_noir.png', 7, 1, 16)

white_tour1 = Tour('white', pos_0, pos_7,  'image/tour_blanche.png', 0, 7, 25)
white_tour2 = Tour('white', pos_7, pos_7,  'image/tour_blanche.png', 7, 7, 32)

black_tour1 = Tour('black', pos_0, pos_0,  'image/tour_noir.png', 0, 0, 1)
black_tour2 = Tour('black', pos_7, pos_0,  'image/tour_noir.png', 7, 0, 8)

white_fou1= Fou('white', pos_2, pos_7,  'image/fou_blanc.png', 2, 7, 27)
white_fou2= Fou('white', pos_5, pos_7,  'image/fou_blanc.png', 5, 7, 30)

black_fou1= Fou('black', pos_2, pos_0,  'image/fou_noir.png', 2, 0, 3)
black_fou2= Fou('black', pos_5, pos_0,  'image/fou_noir.png', 5, 0, 6)

white_cavalier1= Cavalier('white', pos_1, pos_7,  'image/cavalier_blanc.png', 1, 7, 26)
white_cavalier2= Cavalier('white', pos_6, pos_7,  'image/cavalier_blanc.png', 6, 7, 31)

black_cavalier1= Cavalier('black', pos_1, pos_0,  'image/cavalier_noir.png', 1, 0, 2)
black_cavalier2= Cavalier('black', pos_6, pos_0,  'image/cavalier_noir.png', 6, 0, 7)

white_roi= Roi('white', pos_4, pos_7,  'image/roi_blanc.png',4, 7, 29)
black_roi = Roi('black', pos_4, pos_0,  'image/roi_noir.png', 4, 0, 5)

white_reine= Reine('white', pos_3, pos_7,  'image/dame_blanche.png', 3, 7, 28)
black_reine = Reine('black', pos_3, pos_0,  'image/dame_noir.png', 3, 0, 4)

# tavleau contenant les intances des pieces
tab_piece_test = [white_pion1, white_pion2, white_pion3, white_pion4, white_pion5, white_pion6, white_pion7, white_pion8, 
                    black_pion1, black_pion2, black_pion3, black_pion4, black_pion5, black_pion6, black_pion7, black_pion8, 
                    white_tour1, white_tour2, black_tour1, black_tour2, 
                    white_cavalier1, white_cavalier2, black_cavalier1, black_cavalier2, 
                    white_fou1, white_fou2, black_fou1, black_fou2, 
                    white_roi, black_roi, white_reine, black_reine]
