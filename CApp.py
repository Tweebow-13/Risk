import pygame as pg
from pygame.locals import *
import cevent
import os

class CApp(cevent.CEvent):
    def __init__(self):
        self._running = True
        self.size = [self.weight, self.height] = [500, 317]
        #self.bg = None

    def on_exit(self):
        self._running = False

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        #bg = pg.display.set_mode(self.size)
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        
        # load image and quadruple
        imagename = os.path.join(main_dir, "data", "map.png")
        bitmap = pg.image.load(imagename)
        # bitmap = pg.transform.scale2x(bitmap)
        # bitmap = pg.transform.scale2x(bitmap)
        bitmap = bitmap.convert()
        
        self._display_surf.fill((0, 0, 255))
        self._display_surf.blit(bitmap, [0, 0])
        pg.display.flip()

        #self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._running = True

    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pg.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()