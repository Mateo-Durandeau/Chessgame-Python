import pygame
from retransicrip import *
from script_class_game import *
from script_deplacement import *
from script_load_instance import *
from global_var import *


pygame.init()



def run_game_1V1():
    # A gerer plus tard c'est pour les statisiques
    list_game_information = []

    # Création du tableau / echiquer 
    board = Board(WIDTH, HEIGHT)

    # définition du tour des blancs au début de partie
    TOUR = 1

    # pygame setup
    pygame.init()

    # parametrage de l'écran
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    # INIT SELECTION 
    # Point 
    image_pos = pygame.image.load('image/positionement.png')
    image_pos = pygame.transform.scale(image_pos, (WIDTH//8, HEIGHT//8))

    # initialisation de la variable a qui stockera les instances des pièces séléctionner lors des events de clic
    a = white_pion1
    a.selected = False

    # initation de l'etat d'échec à False
    stat = False

    # Init du running en true pour lancer la boucle de jeu
    running = True

    # boucle principam 
    while running:

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:  # Clic gauche de la souris
                    
                    ###############################################################################
                        #   gestion des déplacements pour une pièce deja séléctionné
                    ###############################################################################
                    if a.selected == True and stat == False: 

                        # Recherche des mouvements possible par rapport à la pièce séléctionné 
                        tab_dep = deplacement(chess_2d, type_piece, pos[0], pos[1], a)

                        # stockage de la position du nouveau clic
                        new_mouse_x, new_mouse_y = event.pos
                        # retranscription des positions en case
                        new_pos = retranscription_pos(new_mouse_x, new_mouse_y)

                        new_pos_x = new_pos[0]
                        new_pos_y = new_pos[1]

                        # nombre de la piece du nouveau clic
                        pi_temp = chess_2d[new_pos_y][new_pos_x]
                        
                        # création de l'intance de la seconde pièce séléctionné.
                        if pi_temp != 0:
                            b = retranscription_number(pi_temp)

                        # retranscription des valeurs de positionnement du nouveau mouvement
                        val = retranscription_case(new_pos_x, new_pos_y)

                        # Parcous des mouvement possible
                        for val_X, Val_Y in tab_dep:      

                            # Si l'endroit sélectionné est dans les mouvements possibles 
                            if new_pos_x == val_X and Val_Y == new_pos_y:
                                
                                # gestion du tableau la restranscription tableau 2D = pièce de l'echequier 
                                chess_2d[new_pos_y][new_pos_x] = number_piece
                                chess_2d[pos[1]][pos[0]] = 0

                                a.set_case(new_pos_x, new_pos_y)

                                # Si une pièce est mangé non affichage de la nouvelle pièce par rapport à l'instance
                                if pi_temp != 0:
                                    b.life = False

                                # mouvement de la piece
                                a.move(val[0], val[1])

                                # si la piece est un pion changement de son status
                                if type_piece == "Pion blanc" or type_piece == "Pion noir":
                                    a.status = True

                                if type_piece == "Roi blanc" or type_piece == "Roi noir":
                                    a.status = False


                                #############################################################
                                # changement de tour + vérification d'un échec
                                if TOUR == 1:
                                    TOUR = 2
                                    pos_roi_temp = black_roi.get_number_cases()
                                    pos_roi_x = pos_roi_temp[0]
                                    pos_roi_y = pos_roi_temp[1]
                                    etat_echec(chess_2d, pos_roi_x, pos_roi_y, black_roi)
                                    if black_roi.check == True:
                                        # import des déplacements possible en etat d'échec !
                                        tab_check_piece = test_prevision_deplacement(chess_2d, pos_roi_x, pos_roi_y, black_roi)

                                        if tab_check_piece == []:
                                            print("echec et mat")
                                            running = False

                                elif TOUR == 2:
                                    TOUR = 1
                                    pos_roi_temp = white_roi.get_number_cases()
                                    pos_roi_x = pos_roi_temp[0]
                                    pos_roi_y = pos_roi_temp[1]
                                    etat_echec(chess_2d, pos_roi_x, pos_roi_y, white_roi)
                                    if white_roi.check == True: 
                                        # import des déplacements possible en etat d'échec !
                                        tab_check_piece = test_prevision_deplacement(chess_2d, pos_roi_x, pos_roi_y, white_roi)
                                        if tab_check_piece == []:
                                            print("echec et mat")
                                            running = False


                                # sorti de la boucle pour eviter des tours supplémentaire
                                break
                      

                        # déselection de la pièce 
                        a.selected = False

                    ###############################################################################
                            #  gestion des déplacements pendant l'echec
                    ###############################################################################
                         
                    elif stat == True and a.selected == True: 

                        # stockage de la position du nouveau clic
                        new_mouse_x, new_mouse_y = event.pos
                        # retranscription des positions en case
                        new_pos = retranscription_pos(new_mouse_x, new_mouse_y)

                        new_pos_x = new_pos[0]
                        new_pos_y = new_pos[1]

                        # nombre de la piece du nouveau clic
                        pi_temp = chess_2d[new_pos_y][new_pos_x]
                        
                        # création de l'intance de la seconde pièce séléctionné.
                        if pi_temp != 0:
                            b = retranscription_number(pi_temp)

                        # retranscription des valeurs de positionnement du nouveau mouvement
                        val = retranscription_case(new_pos_x, new_pos_y)
                            
                        # Gestion du tableau des pieces
                        if tab_check_piece != []:
                            for  L in tab_check_piece:
                                for  piece, val_X, Val_Y in L:      
                                    # Si l'endroit sélectionné est dans les mouvements possibles 
                                    if new_pos_x == val_X and Val_Y == new_pos_y and a.num_case == piece:
                                            
                                        # gestion du tableau la restranscription tableau 2D = pièce de l'echequier 
                                        chess_2d[new_pos_y][new_pos_x] = number_piece
                                        chess_2d[pos[1]][pos[0]] = 0

                                        a.set_case(new_pos_x, new_pos_y)


                                        # Si une pièce est mangé non affichage de la nouvelle pièce par rapport à l'instance
                                        if pi_temp != 0:
                                            b.life = False

                                        # mouvement de la piece
                                        a.move(val[0], val[1])

                                        # si la piece est un pion changement de son status
                                        if type_piece == "Pion blanc" or type_piece == "Pion noir":
                                            a.status = True
                                        if type_piece == "Roi blanc" or type_piece == "Roi noir":
                                            a.status = False

                                        if TOUR == 1 and white_roi.check == True:
                                            # mettre fonction qui gère le déplacement lors de l'echec
                                            white_roi.check = False
                                            stat = False
                                            TOUR = 2
                                            a.selected = False
                                        elif TOUR == 2 and black_roi.check == True:
                                            # mettre fonction qui gère le déplacement lors de l'echec
                                            stat = False
                                            black_roi.check = False
                                            TOUR = 1
                                            a.selected = False
                                        
                                            # sorti de la boucle pour eviter des tours supplémentaire
                        
                                        break    
                        a.selected = False


                    else:
                        ###############################################################################
                            #  Selection d'une pièce 
                        ###############################################################################

                        # récuperation des positions du clic
                        mouse_x, mouse_y = event.pos
                        # retranscription des la positions au numéro de la case
                        pos = retranscription_pos(mouse_x, mouse_y)     
                        # récupération de la case                
                        number_piece = retranscription_piece(chess_2d, pos[0], pos[1])
                        
                        # gestion des mouvements de pièces
                        if TOUR == 1 and white_roi.check == True:
                            # mettre fonction qui gère le déplacement lors de l'echec
                            stat = True

                        elif TOUR == 2 and black_roi.check == True:
                            # mettre fonction qui gère le déplacement lors de l'echec
                            stat = True
                        
                        if number_piece != 0:
                            # Création d'un pointeur sur l'instance de la pièce séléctionné
                            a = retranscription_number(number_piece)

                            # gestion de tour 
                            couleur = a.color
                            if couleur == "white" and TOUR == 1:
                                a.selected = True
                                print(f"{a.type} à été selectionné")
                            elif couleur == "black" and TOUR == 2:
                                a.selected = True
                                print(f"{a.type} à été selectionné")

                            elif couleur == "white" and TOUR == 2:
                                print("Au tour des Noirs") 
                            else:
                                print("Au tour des Blancs")
                                
                        # stockage du type de la pièces
                        type_piece = type_of_piece(number_piece)
                        
                        

                       # Gestion du relaché de clic à gerer plus tard
                        
        #################################################################################
            #elif event.type == pygame.MOUSEBUTTONUP:
                #if event.button == 1:  # Relâchez le clic gauche de la souris
                    #break
                    #mouse_x, mouse_y = event.pos
                    #print(mouse_x, mouse_y)
                    #a.move(mouse_x, mouse_y)
                    #a.selected = False
        #################################################################################


        # chargement du tableau 
        screen.fill((234, 233, 210))
        board.draw_chessboard(screen)

        if a.selected == True:
            # affichage de la piece selectionné :
            pygame.draw.rect(screen, (176, 112, 82), pygame.Rect(a.rect[0], a.rect[1], WIDTH//8, HEIGHT//8))


        # chargement des pieces
        all_sprites = load_piece()
        all_sprites.draw(screen)


        # affichage des mouvements possible
        if a.selected == True:
            tab_dep_temp = deplacement(chess_2d, type_piece, pos[0], pos[1], a)
            if stat == False:
                for X, Y in tab_dep_temp:
                    tab_dep_pos = retranscription_case(X, Y) 
                    screen.blit(image_pos, (tab_dep_pos[0], tab_dep_pos[1]))
            # pendant l'échec
            elif stat == True: 
                for  L in tab_check_piece:
                    for  piece, X, Y in L: 
                        if a.num_case == piece: 
                            tab_dep_pos = retranscription_case(X, Y) 
                            screen.blit(image_pos, (tab_dep_pos[0], tab_dep_pos[1]))



         # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(30)  # limits FPS to 60

    pygame.quit()

    # destruction de toutes les informations des instances / reload 

    return list_game_information


def preparation_inversion_ecran(screen):
        
        # FAIRE FONCTION RETRANSCRIP POSITION INVERSE 

        # RETOURNER LES PIECES NOIRS ET BLANCHE

        # Avant l'actualisation graphique, inversez l'écran Y-axis  
        flipped_screen = pygame.transform.flip(screen, False, True)  # False pour non flip X, True pour flip y
        # Remettez le screen inversé à l'écran d'affichage
        pygame.display.get_surface().blit(flipped_screen, (0, 0))

