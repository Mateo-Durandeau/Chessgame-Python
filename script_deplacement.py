from retransicrip import *
import copy

################################################################################
    # gestion des déplacements
################################################################################

def verif_color(chess_2d, pos_y, pos_x):
    stat = ""
    b = retranscription_number(chess_2d[pos_y][pos_x])
    if b != 0:
        stat = b.color
    return stat

def verif_case(chess_2d, pos_x, pos_y, couleur_roi, type_piece):
    valeur_piece = chess_2d[pos_y][pos_x]

    if valeur_piece != 0 or valeur_piece == 5 or valeur_piece == 29:
        piece_temp = retranscription_number(valeur_piece)
        color_temp = piece_temp.color 
        type = piece_temp.type
        
        if color_temp != couleur_roi and type_piece == type:
            return False
    return True
    
def verif_case_libre(chess_2d, pos_x, pos_y):
    valeur_piece = chess_2d[pos_y][pos_x]
    if valeur_piece == 0 or valeur_piece == 29 or valeur_piece == 5:
        return True
    else:
        return False

def fonction_verif_roi(chess_2d, new_x, new_y, piece):
    

    verif = True
    verif_reine = True
    test_libre = True

    couleur_roi = piece.color

    

    # vérification des pions
    tab_pion_noir = [(1, 1), (-1, 1)]
    tab_pion_blanc = [(1, -1), (-1, -1)]

    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]  # Les directions possibles sur les diagonales
    directions_ligne = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    direction_cavalier = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    direction_roi = [(-1, -1), (0,-1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    
    
    # verification roi: 
        
    for direction in direction_roi:
        dx, dy = direction
        try: 
            pos_x = new_x + dx
            pos_y = new_y + dy


            if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    continue

            verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "roi")
            if verif == False:
                return verif
            
        except IndexError:
            pass


    if couleur_roi == "white":
        for pos_x_temp, pos_y_temp in tab_pion_blanc:
            try:
                pos_x = pos_x_temp + new_x
                pos_y = pos_y_temp + new_y
                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    continue
                verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "pion")
                if verif == False:
                    return verif
            except IndexError:
                pass
    else:
        for pos_x_temp, pos_y_temp in tab_pion_noir:
            try:
                pos_x = pos_x_temp + new_x
                pos_y = pos_y_temp + new_y
                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    continue
                verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "pion")
                if verif == False:
                    return verif
            except IndexError:
                pass

    # verification des pièces sur les diagonales

    for direction in directions:
        dx, dy = direction
        try:
            for i in range(1, 8):
                
                pos_x, pos_y = new_x + i * dx, new_y + i * dy

                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    break  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index 

                verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "fou")
                verif_reine = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "reine")
                test_libre = verif_case_libre(chess_2d, pos_x, pos_y)

                
                if verif == False:
                    return verif
                elif verif_reine == False:
                    return verif_reine
                elif test_libre == False:
                    break

        except IndexError:
            pass

    

    # vérification des pièces sur les lignes 

    for direction in directions_ligne:
        dx, dy = direction
        try:
            for i in range(1, 8):
                
                pos_x, pos_y = new_x + i * dx, new_y + i * dy

                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    break  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index 

                verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "tour")
                verif_reine = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "reine")
                test_libre = verif_case_libre(chess_2d, pos_x, pos_y)

                if verif == False:
                    return verif
                elif verif_reine == False:
                    return verif_reine
                elif test_libre == False:
                    break

        except IndexError:
            pass

    # verification cavalier : 
        
    for direction in direction_cavalier:
        dx, dy = direction
        try: 
            pos_x = new_x + dx
            pos_y = new_y + dy
            if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                continue
            verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "cavalier")
            if verif == False:
                return verif
        except IndexError:
            pass
        

    return verif 

def verif_case_king(chess_2d, pos_x, pos_y, couleur_roi, type_piece):
    valeur_piece = chess_2d[pos_y][pos_x]
    if valeur_piece != 0:
        piece_temp = retranscription_number(valeur_piece)
        color_temp = piece_temp.color
        type = piece_temp.type
        if color_temp != couleur_roi and type_piece == type:
            return False
    return True

def fonction_verif_roi_check(chess_2d, new_x, new_y, roi):

    """Fonction qui verifie si le roi est en echec ou mat"""
    couleur_roi = roi.color
    echec = False

    # liste de mouvement possible sur la ligne du roi pour virifier si il y a une pièce et si elle cause un echec et mat.

    tab_pion_noir = [(1, 1), (-1, 1)]
    tab_pion_blanc = [(1, -1), (-1, -1)]

    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]  # Les directions possibles sur les diagonales
    directions_ligne = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    direction_cavalier = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

    for direction in directions_ligne:
        
        dx, dy = direction
        try:
            for i in range(1, 8):
                
                pos_x, pos_y = new_x + i * dx, new_y + i * dy

                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    break  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index 

                verif = verif_case_king(chess_2d, pos_x, pos_y, couleur_roi, "tour")
                verif_reine = verif_case_king(chess_2d, pos_x, pos_y, couleur_roi, "reine")
                test_libre = verif_case_libre(chess_2d, pos_x, pos_y)

                if verif == False:
                    return True
                elif verif_reine == False: 
                    return True
                elif test_libre == False:
                    break

        except IndexError:
            pass


    # verification des pièces sur les diagonales

    for direction in directions:
        dx, dy = direction
        try:
            for i in range(1, 8):
                
                pos_x, pos_y = new_x + i * dx, new_y + i * dy

                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    break  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index 

                verif = verif_case_king(chess_2d, pos_x, pos_y, couleur_roi, "fou")
                verif_reine = verif_case_king(chess_2d, pos_x, pos_y, couleur_roi, "reine")
                test_libre = verif_case_libre(chess_2d, pos_x, pos_y)

                
                if verif == False:
                    return True
                elif verif_reine == False: 
                    return True
                elif test_libre == False:
                    break

        except IndexError:
            pass

    for direction_cav in direction_cavalier:
        dx, dy = direction_cav
        try:           
            pos_x = new_x + dx
            pos_y = new_y + dy

            if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                continue  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index  
            verif = verif_case_king(chess_2d, pos_x, pos_y, couleur_roi, "cavalier")
            if verif == False:
                return True
            
        except IndexError:
            pass
        
    if couleur_roi == "white":
        for pos_x_temp, pos_y_temp in tab_pion_blanc:
            try:
                pos_x = pos_x_temp + new_x
                pos_y = pos_y_temp + new_y
                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    continue
                verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "pion")
                if verif == False:
                    return True
            except IndexError:
                pass
    else:
        for pos_x_temp, pos_y_temp in tab_pion_noir:
            try:
                pos_x = pos_x_temp + new_x
                pos_y = pos_y_temp + new_y

                if not (0 <= pos_x < 8 and 0 <= pos_y < 8):
                    continue
                verif = verif_case(chess_2d, pos_x, pos_y, couleur_roi, "pion")
                if verif == False:
                    return True
            except IndexError:
                pass
    


    return echec

def etat_echec(chess_2d, new_x, new_y, roi):
    """Lors d'un mouvement de pièce, on vérifie si les rois sont en echec"""
    echec = fonction_verif_roi_check(chess_2d, new_x, new_y, roi)
    if echec == True:
        roi.check = True
        print(f"le roi {roi.color} est en echec !!!")
    elif echec == False:
        roi.check == False



def test_prevision_deplacement(chess_2d, pos_roi_x, pos_roi_y, roi):
    
    liste_deplacement = []

    # Pour toute les pièces sur l'échiquier 
    for piece in tab_piece_test:

        if piece.color == roi.color and piece.life == True:
            # Faire un déplcament imaginaire et tester si il y a encore echec 
            tab_deplacement_piece = fonction_test(chess_2d, piece, pos_roi_x, pos_roi_y, roi)

            # s'il n'y a plus échec, ajouter les déplacement au déplacements possibles
            if tab_deplacement_piece != []:
                liste_deplacement.append(tab_deplacement_piece)


    return liste_deplacement


def fonction_test(chess_2d, piece, pos_roi_x, pos_roi_y, roi):

    tab_dep = []
    cp_chess_2d = copy.deepcopy(chess_2d)

    type_piece = type_of_piece(piece.num_case) 

    deplacement_post_traitement_roi = deplacement(chess_2d, type_piece, piece.case_x, piece.case_y, piece)


    if type_piece == "Roi blanc" or type_piece == "Roi noir" :
        for x, y in deplacement_post_traitement_roi:
            verif_nouvelle_case = fonction_verif_roi_check(chess_2d, x, y, roi)
            if verif_nouvelle_case == False:
                tab_dep.append([piece.num_case, x, y])

    else :
        for x, y in deplacement_post_traitement_roi:

            # Appel du déplacement imaginaire de la piece
            cp_chess_2d[piece.case_y][piece.case_x] = 0
            cp_chess_2d[y][x] = piece.num_case

            # test de l'état déchec avec un déplacement imaginaire
            test_echec = fonction_verif_roi_check(cp_chess_2d, pos_roi_x, pos_roi_y, roi)

            if test_echec == False: 
                tab_dep.append([piece.num_case, x, y])

            cp_chess_2d = copy.deepcopy(chess_2d)

    return tab_dep
















def deplacement(chess_2d, type_piece, pos_x, pos_y, piece):
    """ 
    Ajout dans un tableau les positions possible pour une pièces séléctionner --> mettre se tableau dans la seconde gestion du clic
    """

    # Try pour gerer les erreurs d'index lors des pièces proche des bords ou du cavalier 

    # tableau qui va stocker les déplacements possible si il y en a
    tab_deplacement_possible = []


    ##############################################
        # Déplacement des pions 
    ##############################################

    # Pions blanc
    if type_piece == "Pion blanc":

        # Si le pion n'a pas été bougé : Déplacement sur 2 cases
        if piece.status == False:
            try :
                if chess_2d[pos_y-1][pos_x] == 0:
                    tab_deplacement_possible.append((pos_x, pos_y - 1))
                    if chess_2d[pos_y-2][pos_x] == 0:
                        tab_deplacement_possible.append((pos_x, pos_y - 2))
                        # si il n'y a pas de pièce devant le pion ajouter les déplacements au tableau                    
                    
            except IndexError:
                pass

        # Si le pion a été bougé : Déplacement sur 1 case
        elif piece.status == True:
            try: 
                if chess_2d[pos_y-1][pos_x] != 0:
                    pass
                # si il n'y a pas de pièce devant le pion ajouter les déplacements au tableau
                else:
                    tab_deplacement_possible.append((pos_x, pos_y - 1))
            except IndexError:
                pass

        # vérifi s'il y a une piece d'une autre couleurs sur les diagonales du pions
        try:         
            stat = verif_color(chess_2d, (pos_y-1), (pos_x+1))
            if chess_2d[pos_y-1][pos_x+1] != 0 and stat != "white": 
                tab_deplacement_possible.append((pos_x + 1, pos_y - 1))
        except IndexError:
            pass

        try:    
            stat = verif_color(chess_2d, (pos_y-1), (pos_x-1))
            if chess_2d[pos_y-1][pos_x-1] != 0  and stat != "white": 
                tab_deplacement_possible.append((pos_x - 1, pos_y - 1))
        except IndexError:
            pass
                
    # Pion noir // pour détail voir commentaire des pions blancs
    if type_piece == "Pion noir":
        if piece.status == False:
            try :
                if chess_2d[pos_y+1][pos_x] != 0:
                    pass
                else:
                    tab_deplacement_possible.append((pos_x, pos_y + 1))
                    if chess_2d[pos_y+2][pos_x] == 0:
                        tab_deplacement_possible.append((pos_x, pos_y + 2))
            except IndexError:
                pass


        elif piece.status == True:
            try: 
                if chess_2d[pos_y+1][pos_x] != 0:
                    pass
                else:
                    tab_deplacement_possible.append((pos_x, pos_y + 1))
            except IndexError:
                pass

        try:        

            stat = verif_color(chess_2d, (pos_y+1), (pos_x+1))
            if chess_2d[pos_y+1][pos_x+1] != 0 and stat != "black": 
                tab_deplacement_possible.append((pos_x + 1, pos_y + 1))
        except IndexError:
            pass

        try:    
            stat = verif_color(chess_2d, (pos_y+1), (pos_x-1))
            if chess_2d[pos_y+1][pos_x-1] != 0 and stat != "black": 
                tab_deplacement_possible.append((pos_x - 1, pos_y + 1))
        except IndexError:
            pass
        

    ##############################################
        # Déplacement des Fous 
    ##############################################
        
    if type_piece == "Fou noir" or type_piece == "Fou blanc":
        couleur_fou = piece.color

        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]  # Les directions possibles pour un fou

        for direction in directions:
            dx, dy = direction
            try:
                for i in range(1, 8):
                    new_x, new_y = pos_x + i * dx, pos_y + i * dy

                    if not (0 <= new_x < 8 and 0 <= new_y < 8):
                        break  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index 

                    if chess_2d[new_y][new_x] == 0:
                        tab_deplacement_possible.append((new_x, new_y))
                    else:
                        piece_chemin = retranscription_number(chess_2d[new_y][new_x])
                        couleur_piece_chemin = piece_chemin.color

                        if couleur_piece_chemin == couleur_fou:
                            break
                        else:
                            tab_deplacement_possible.append((new_x, new_y))
                            break
            except IndexError:
                pass



    ##############################################
        # Déplacement des Cavaliers
    ##############################################

    if type_piece == "Cavalier noir" or type_piece == "Cavalier blanc":
        couleur_cavalier = piece.color

        tableau_pos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

        for i in tableau_pos:
            new_x, new_y = pos_x + i[1], pos_y + i[0]  # Inversion des indices pour correspondre à la notation (x, y)

            try:
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if chess_2d[new_y][new_x] == 0:
                        tab_deplacement_possible.append((new_x, new_y))
                    else:
                        piece_chemin = retranscription_number(chess_2d[new_y][new_x])
                        couleur_piece_chemin = piece_chemin.color

                        if couleur_piece_chemin != couleur_cavalier:
                            tab_deplacement_possible.append((new_x, new_y))
            except IndexError:
                pass

        

    ##############################################
        # Déplacement des Tours
    ##############################################
            
    # Déplacement de la tour
    if type_piece == "Tour noir" or type_piece == "Tour blanche":
        couleur_tour = piece.color

        # Tableau des directions pour la tour
        directions_tour = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions_tour:
            dx, dy = direction
            try:
                for i in range(1, 8):
                    new_x, new_y = pos_x + i * dx, pos_y + i * dy

                    if 0 <= new_x < 8 and 0 <= new_y < 8:
                        if chess_2d[new_y][new_x] == 0:
                            tab_deplacement_possible.append((new_x, new_y))
                        else:
                            piece_chemin = retranscription_number(chess_2d[new_y][new_x])
                            couleur_piece_chemin = piece_chemin.color
                            if couleur_piece_chemin != couleur_tour:
                                tab_deplacement_possible.append((new_x, new_y))
                            break
                    else:
                        break
            except IndexError:
                pass


    ##############################################
        # Déplacement des reine
    ##############################################
        
    if type_piece == "Reine noir" or type_piece == "Reine blanche":
        couleur_reine = piece.color

        # Tableau des directions pour la tour
        directions_tour = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions_tour:
            dx, dy = direction
            try:
                for i in range(1, 8):
                    new_x, new_y = pos_x + i * dx, pos_y + i * dy

                    if 0 <= new_x < 8 and 0 <= new_y < 8:
                        if chess_2d[new_y][new_x] == 0:
                            tab_deplacement_possible.append((new_x, new_y))
                        else:
                            piece_chemin = retranscription_number(chess_2d[new_y][new_x])
                            couleur_piece_chemin = piece_chemin.color
                            if couleur_piece_chemin != couleur_reine:
                                tab_deplacement_possible.append((new_x, new_y))
                            break
                    else:
                        break
            except IndexError:
                pass

        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]  # Les directions possibles pour un fou

        for direction in directions:
            dx, dy = direction
            try:
                for i in range(1, 8):
                    new_x, new_y = pos_x + i * dx, pos_y + i * dy

                    if not (0 <= new_x < 8 and 0 <= new_y < 8):
                        break  # Sortir de la boucle si en dehors de l'échiquier | permet de faire Les 4 testes en 1 et ne génère par une erreur d'index 

                    if chess_2d[new_y][new_x] == 0:
                        tab_deplacement_possible.append((new_x, new_y))
                    else:
                        piece_chemin = retranscription_number(chess_2d[new_y][new_x])
                        couleur_piece_chemin = piece_chemin.color

                        if couleur_piece_chemin == couleur_reine:
                            break
                        else:
                            tab_deplacement_possible.append((new_x, new_y))
                            break
            except IndexError:
                pass

    ##############################################
        # Déplacement des Rois
    ##############################################

    if type_piece == "Roi noir" or type_piece == "Roi blanc":
        couleur_roi = piece.color

        tab_deplacement_temporaire = []

        tab_coups_possible = [(-1, -1), (0,-1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        for coup in tab_coups_possible:
            new_x = pos_x + coup[0]
            new_y = pos_y + coup[1]
            try: 
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if chess_2d[new_y][new_x] == 0:
                        tab_deplacement_temporaire.append((new_x, new_y))
                    else:
                        piece_chemin = retranscription_number(chess_2d[new_y][new_x])
                        couleur_piece_chemin = piece_chemin.color

                        if couleur_piece_chemin != couleur_roi:
                            # verifier que la pièce n'est protégé par aucune autre pièce
                            tab_deplacement_temporaire.append((new_x, new_y))
                            
            except IndexError:
                pass

        try : 
            # ajout de la fonctionnalité du rock 
            if piece.status == False and piece.check == False: 
                if piece.color == "white":
                    if chess_2d[pos_y][pos_x+1] == 0 and chess_2d[pos_y][pos_x+2] == 0 and chess_2d[pos_y][pos_x+3] == 32 and white_tour2.status == False:
                        piece.rock = True
                        tab_deplacement_temporaire.append((pos_x+2, pos_y))
                    if chess_2d[pos_y][pos_x-1] == 0 and chess_2d[pos_y][pos_x-2] == 0 and chess_2d[pos_y][pos_x-3] == 0 and chess_2d[pos_y][pos_x-4] == 25 and white_tour1.status == False:
                        piece.rock = True
                        tab_deplacement_temporaire.append((pos_x-2, pos_y))

                elif piece.color == "black":
                    if chess_2d[pos_y][pos_x+1] == 0 and chess_2d[pos_y][pos_x+2] == 0 and chess_2d[pos_y][pos_x+3] == 8 and black_tour2.status == False:
                        piece.rock = True
                        tab_deplacement_temporaire.append((pos_x+2, pos_y))
                    if chess_2d[pos_y][pos_x-1] == 0 and chess_2d[pos_y][pos_x-2] == 0 and chess_2d[pos_y][pos_x-3] == 0 and chess_2d[pos_y][pos_x-4] == 1 and black_tour1.status == False:
                        piece.rock = True
                        tab_deplacement_temporaire.append((pos_x-2, pos_y))
        except IndexError:
            pass

                

        for coup_temp in tab_deplacement_temporaire:
            new_x = coup_temp[0]
            new_y = coup_temp[1]
            verif = False
            # appel fonction qui verifi si un fou, une tour, un pion, une dame : d'une autre couleur que le roi se trouve sur la ligne de la case potentiel
            verif = fonction_verif_roi(chess_2d, new_x, new_y, piece)
            if verif == True:
                tab_deplacement_possible.append((new_x, new_y))

    return tab_deplacement_possible