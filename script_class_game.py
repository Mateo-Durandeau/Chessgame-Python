import pygame
from global_var import *


#################################################################################
# Class sur les pièces
#################################################################################

# Classe de base pour les pièces
class Piece(pygame.sprite.Sprite):
    def __init__(self, color, image_path, x, y, case_x, case_y, num_case):
        super().__init__()
        self.color = color
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (WIDTH//8, HEIGHT//8))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.case_x = case_x
        self.case_y = case_y
        self.num_case = num_case

    def get_pos(self):
        return (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
    
    def move(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    def set_case(self, new_case_x, new_case_y):
        self.case_x = new_case_x
        self.case_y = new_case_y

    def get_num_case(self):
        return self.num_case
    
    def get_number_cases(self):
        return (self.case_x, self.case_y)


# sous class de piece qui herite des méthodes de Piece
class Pion(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.life = True
        self.type = "pion"

class Tour(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.life = True
        self.type = "tour"


class Fou(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.life = True
        self.type = "fou"


class Roi(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.life = True
        self.check = False
        self.type = "roi"
        self.rock = False


class Reine(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.life = True
        self.type = "reine"

class Cavalier(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.life = True
        self.type = "cavalier"



 
#################################################################################
# Class sur le board
#################################################################################   


class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.row = 0
        self.line = 0
        self.piece = 0
        self.rect_size_x = width // 8
        self.rect_size_y = height // 8

    def draw_chessboard(self, screen):
        """ draw le chessboard """
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(screen, color=(75, 115, 153),
                                rect=(i * self.rect_size_x * 2, j * self.rect_size_y * 2, self.rect_size_x, self.rect_size_y))

        for i in range(8):
            for j in range(8):
                pygame.draw.rect(screen, color=(75, 115, 153), rect=(
                    (i * self.rect_size_x * 2) + self.rect_size_x, (j * self.rect_size_y * 2) + self.rect_size_y, self.rect_size_x, self.rect_size_y))