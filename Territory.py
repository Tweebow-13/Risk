import pygame as pg
from pygame.locals import *
import pygame.freetype
import os

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# main_dir = os.path.split(os.path.abspath(__file__))[0]
# fontname = os.path.join(main_dir, "data", "xirod.regular.ttf")
# pg.freetype.init()
# GAME_FONT = pygame.freetype.Font(fontname, 18)

class Territory(pg.sprite.Sprite):

    def __init__(self, inName, inCoord = [0, 0], inSize = [30, 30]):
        super().__init__()
        self.name = inName
        self.army = 0
        self.ownership = None
        self.x = inCoord[0]
        self.y = inCoord[1]
        self.size = inSize
        self.image = pg.Surface(inSize)
        self.rect = self.image.get_rect()
    
    def __str__(self):
        return(str(self.name) + " : " + str(self.army) + " units")
    
    def get_name(self):
        return self.name
    
    def get_army(self):
        return self.army

    def get_rect(self):
        return self.rect

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_size(self):
        return self.size

    def get_ownership(self):
        return self.ownership
    
    def set_army(self, inArmy):
        self.army = inArmy
    
    def set_ownership(self, inOwnership):
        self.ownership = inOwnership        