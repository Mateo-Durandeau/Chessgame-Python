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
        self.turn = False

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
    
    def reset(self, color, x, y, case_x, case_y, num_case, type_game):
        self.color = color
        self.rect = self.image.get_rect(topleft=(x, y))
        self.case_x = case_x
        self.case_y = case_y
        self.num_case = num_case
        self.status = False
        self.selected = False
        self.life = True
        self.type = type_game

    def reset_pion(self, color, x, y, case_x, case_y, num_case, type_game, image_path):
        self.reset(color, x, y, case_x, case_y, num_case, type_game)
        self.changement = False
        self.passant = False
        self.attente = False
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (WIDTH//8, HEIGHT//8))

    def reset_roi(self, color, x, y, case_x, case_y, num_case, type_game):
        self.reset(color, x, y, case_x, case_y, num_case, type_game)
        self.rock = False
        self.check = False

    @staticmethod
    def type_p(number):

        if 9 <= number <= 16:
            return "pion noir"
        if 17 <= number <= 24:
            return "pion blanc"
        
        if number == 1 or number == 8:
            return "tour noir"
        if number == 25 or number == 32:
            return "tour blanche"
        
        if number == 2 or number == 7:
            return "cavalier noir"
        if number == 26 or number == 31:
            return "cavalier blanc"
        
        if number == 3 or number == 6:
            return "fou noir"
        if number == 27 or number == 30:
            return "fou blanc"
        
        if number == 4:
            return "reine noir"
        if number == 28:
            return "reine blanche"
        
        if number == 5:
            return "roi noir"
        
        if number == 29:
            return "roi blanc"
        return "F"
    
    def rotate(self, angle):
        """Pivote la pièce d'un certain angle."""
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)





# sous class de piece qui herite des méthodes de Piece
class Pion(Piece):
    def __init__(self, color, x, y, path, case_x, case_y, num_case):
        super().__init__(color, path, x, y, case_x, case_y, num_case)
        self.selected = False
        self.status = False
        self.changement = False
        self.life = True
        self.type = "pion"
        self.passant = False
        self.attente = False
        self.valuation = 0

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
                
                
        pygame.draw.rect(screen, color=('black'), rect=(WIDTH, 0, 300, HEIGHT))