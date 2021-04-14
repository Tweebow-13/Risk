import pygame as pg
from pygame.locals import *
import pygame.freetype
import cevent
import os

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class CApp(cevent.CEvent):
    def __init__(self):
        self._running = True
        self.size = [self.weight, self.height] = [650, 400]
        #self.bg = None

    def on_exit(self):
        self._running = False

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self.size, pg.RESIZABLE | pg.SCALED)
        #self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        
        imagename = os.path.join(main_dir, "data", "map.jpg")
        picture = pg.image.load(imagename)
        #for grey in [(205,204,204),(205,205,204),(205,205,205),(206,205,204),(207,205,206),(204,204,204)]:
        picture.set_colorkey((204,204,204))
        picture = pg.transform.scale(picture, self.size)
        picture = picture.convert()
        self._display_surf.fill((150, 200, 255))
        self._display_surf.blit(picture, [0, 0])

        self._running = True

    def on_loop(self):
        pass
    def on_render(self):
        pg.display.update()
    def on_cleanup(self):
        pg.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        
        fontname = os.path.join(main_dir, "data", "xirod.regular.ttf")
        GAME_FONT = pygame.freetype.Font(fontname, 24)
        text_surface, rect = GAME_FONT.render("Hello World!", WHITE)
 
        while( self._running ):
            for event in pg.event.get():
                self.on_event(event, self._display_surf, text_surface)
            self.on_loop()
            self.on_render()

        self.on_cleanup()