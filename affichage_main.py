import pygame
import script_game

WIDTH_SCREEN = 1200
HEIGHT_SCREEN = 800

MID_X = WIDTH_SCREEN//2
MID_y = HEIGHT_SCREEN//2

POS_X_BT1 = MID_X//4
POS_Y_BT1 = MID_y-70

POS_X_BT2 = MID_X+50
POS_Y_BT2 = MID_y-70

pygame.init()

# Paramètre de l'écran 
pygame.display.set_caption("Menu jeu")
window_gestion = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
running_gestion = True


# load des images
text_affichage = pygame.image.load('image/LOGO.png')
text_affichage = pygame.transform.scale(text_affichage, (800, 170))

#text_credit = pygame.image.load('image/credit.png')
#text_affichage = pygame.transform.scale(text_affichage, (800, 170))

bouton_1V1 = pygame.image.load('image/1V1.png')
bouton_VSAI = pygame.image.load('image/VSIA.png')

# load nuage 
nuage = pygame.image.load('image/nuage.png')
nuage = pygame.transform.scale(nuage, (700, 500))

nuage_1 = nuage.get_rect()


while running_gestion:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_gestion = False
        # gestion des clics 



    window_gestion.fill((7, 75, 150))
    window_gestion.blit(nuage, (-50, 10))
    window_gestion.blit(nuage, (700, 300))
    window_gestion.blit(text_affichage, (200,50))
    #window_gestion.blit(text_credit, (50,50))
    window_gestion.blit(bouton_1V1, (POS_X_BT1,POS_Y_BT1))
    window_gestion.blit(bouton_VSAI, (POS_X_BT2, POS_Y_BT2))
   

    pygame.display.flip()        

pygame.quit()

#script_game.run_game()