import pygame
import script_game

WIDTH_SCREEN = 1200
HEIGHT_SCREEN = 800

MID_X = WIDTH_SCREEN//2
MID_y = HEIGHT_SCREEN//2

POS_X_LG = 75
POS_Y_LG = 60

POS_X_BT1 = 75
POS_Y_BT1 = 240

POS_X_BT2 = 75
POS_Y_BT2 = 420

POS_X_BT3 = 75
POS_Y_BT3 = 600

LIST_INFORMATION_1V1 = []

def run_game_gestion():

    pygame.init()
    quit = True
    # Paramètre de l'écran 
    pygame.display.set_caption("Menu jeu")
    window_gestion = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    running_gestion = True


    # load des images
    text_affichage = pygame.image.load('image/LOGO.png')

    text_credit = pygame.image.load('image/QUIT.png')

    bouton_1V1 = pygame.image.load('image/1V1.png')
    bouton_VSAI = pygame.image.load('image/VSIA.png')

    # load nuage 
    nuage = pygame.image.load('image/nuage.png')
    nuage = pygame.transform.scale(nuage, (700, 500))

    while running_gestion:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_gestion = False
                quit = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    if mouse_pos[0] >= POS_X_BT1 and mouse_pos[0] <= (POS_X_BT1 + 400) and mouse_pos[1] >= POS_Y_BT1 and mouse_pos[1] <= (POS_Y_BT1 + 150):
                        LIST_INFORMATION_1V1.append(script_game.run_game_1V1())
                        running_gestion = False
                    elif mouse_pos[0] >= POS_X_BT2 and mouse_pos[0] <= (POS_X_BT2 + 400) and mouse_pos[1] >= POS_Y_BT2 and mouse_pos[1] <= (POS_Y_BT2 + 150):
                        pass
                    elif mouse_pos[0] >= POS_X_BT3 and mouse_pos[0] <= (POS_X_BT3 + 400) and mouse_pos[1] >= POS_Y_BT3 and mouse_pos[1] <= (POS_Y_BT3 + 150):
                        quit = False
                        running_gestion = False

            # gestion des clics 

        if running_gestion == False: 
            break


        window_gestion.fill((7, 75, 150))
        window_gestion.blit(nuage, (-50, 10))
        window_gestion.blit(nuage, (700, 300))
        window_gestion.blit(text_affichage, (POS_X_LG, POS_Y_LG))
        window_gestion.blit(text_credit, (POS_X_BT3,POS_Y_BT3))

        # AFFICHAGE DES BOUTONS

        window_gestion.blit(bouton_1V1, (POS_X_BT1,POS_Y_BT1))
        window_gestion.blit(bouton_VSAI, (POS_X_BT2, POS_Y_BT2))

        #Gestion du passage de la souris sur les boutons 
    
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] >= POS_X_BT1 and mouse_pos[0] <= (POS_X_BT1 + 400) and mouse_pos[1] >= POS_Y_BT1 and mouse_pos[1] <= (POS_Y_BT1 + 150):
            pygame.draw.rect(window_gestion, "Red", pygame.Rect(30, 30, 60, 60))
        elif mouse_pos[0] >= POS_X_BT2 and mouse_pos[0] <= (POS_X_BT2 + 400) and mouse_pos[1] >= POS_Y_BT2 and mouse_pos[1] <= (POS_Y_BT2 + 150):
            pygame.draw.rect(window_gestion, "Green", pygame.Rect(30, 30, 60, 60))
        elif mouse_pos[0] >= POS_X_BT3 and mouse_pos[0] <= (POS_X_BT3 + 400) and mouse_pos[1] >= POS_Y_BT3 and mouse_pos[1] <= (POS_Y_BT3 + 150):
            pygame.draw.rect(window_gestion, "Blue", pygame.Rect(30, 30, 60, 60))

        pygame.display.flip()        

    pygame.quit()

    return quit
