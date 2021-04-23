import pygame as pg
from pygame.locals import *
import cevent
import pygame.freetype
import os

from Territory import Territory
from Land import Land
from Player import Player

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 200)
GREY  = (204, 204, 204)

# Define the territories and their attributes
territories = ["Alaska", "Northwest_Territory", "Alberta" ,"Ontario", "Quebec", "Western_US", "Eastern_US", "Central_America", "Venezuela", "Perou", "Brazil", "Argentina", "Greenland", "Iceland", "Great_Britain", "Western_Europe", "Eastern_Europe", "Southern_Europe", "Scandinvia", "Ukraine", "Egypt", "North_Africa", "Congo", "East_Africa", "South_Africa", "Madagascar", "Middle_East", "Afghanistan", "Ural", "India", "Siberia", "Yakutsk", "Kamchatka", "Irkutsk", "Mongolia", "Japan", "China", "Siam", "Indonesia", "New_Guinea", "Western_Australia", "Eastern_Australia"]
coords = [[10, 30], [58, 30], [63, 62], [122, 72], [161, 63], [68, 109], [124, 119], [75, 152], [120, 206], [117, 237], [178, 231], [152, 292], [178, 1], [256, 63], [243, 92], [260, 151], [293, 106], [305, 145], [301, 47], [350, 41], [326, 208], [263, 202], [324, 271], [365, 240], [330, 310], [408, 325], [369, 173], [400, 119], [425, 46], [448, 183], [455, 16], [499, 19], [543, 29], [496, 72], [494, 113], [577, 96], [471, 141], [504, 195], [498, 263], [565, 253], [541, 314], [595, 297]]
sizes = [[50, 58], [100, 43], [58, 43], [37, 49], [43, 54], [56, 43], [52, 50], [55, 58], [74, 29], [62, 58], [60, 48], [36, 102], [76, 73], [37, 24], [43, 50], [41, 45], [52, 35], [46, 38], [45, 42], [69, 122], [55, 29], [69, 81], [46, 47], [47, 76], [67, 81], [26, 49], [71, 65], [59, 49], [45, 79], [60, 74], [36, 90], [44, 40], [48, 68], [53, 34], [63, 41], [34, 69], [93, 59], [43, 54], [67, 48], [55, 35], [55, 62], [53, 89]]

main_dir = os.path.split(os.path.abspath(__file__))[0]
fontname = os.path.join(main_dir, "data", "xirod.regular.ttf")
pg.freetype.init()
FONT_SIZE = 12
GAME_FONT = pygame.freetype.Font(fontname, FONT_SIZE)
imagename = os.path.join(main_dir, "data", "map.jpg")
BACKGROUND = pg.image.load(imagename)
BACKGROUND.set_colorkey(GREY)

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
        global BACKGROUND, FONT_SIZE
        BACKGROUND = pg.transform.scale(BACKGROUND, self.size)
        BACKGROUND = BACKGROUND.convert()
        self._display_surf.fill((150, 200, 255))
        self._display_surf.blit(BACKGROUND, [0, 0])
        global territories, coords, sizes
        for i in range(len(territories)):
            terr = territories[i]
            terr = Territory(terr, coords[i], sizes[i])
            territories[i] = terr
            # text_surface, rect = GAME_FONT.render(str(terr.get_army()), WHITE)
            # self._display_surf.blit(text_surface, [terr.get_x() + (terr.get_size()[0] - FONT_SIZE)/2, terr.get_y() + (terr.get_size()[1] - FONT_SIZE)/2])
            # #self.on_render(terr.get_rect())
        self.on_render()
        self._running = True
        self.on_setup()
    
    def on_setup(self):
        global territories
        Blue = Player("Blue", BLUE)
        Red = Player("Red", RED)
        players = [Blue, Red]
        # /////////////////
        randomTerr = True
        randomArmies = True
        # /////////////////
        land = Land(territories, players, randomTerr, randomArmies)
        self._display_surf.blit(BACKGROUND, [0, 0])
        if randomTerr:
            for i in range(land.get_nbTerritories()):
                player = land.players[i%land.get_nbPlayers()]
                land._setup_random_territories(player) 
            self.on_display()
        else:
            for i in range(land.get_nbTerritories()):
                player = land.players[i%land.get_nbPlayers()]
                terr = land._setup_territories(player)
                text_surface, rect = GAME_FONT.render(str(terr.get_army()), terr.get_ownership().get_color())
                self._display_surf.blit(text_surface, [terr.get_x() + (terr.get_size()[0] - FONT_SIZE)/2, terr.get_y() + (terr.get_size()[1] - FONT_SIZE)/2])
                self.on_render()
        print('\n',"////////////////////////////////////")
        print("Territories ready",'\n','\n')

        if randomArmies:
            for i in range(land.get_nbTerritories(), land.get_players()[0].get_army()*land.get_nbPlayers()):
                player = land.players[i%land.get_nbPlayers()]
                land._setup_random_armies(player)
            self.on_display()
        else:
            for i in range(land.get_nbTerritories(), land.get_players()[0].get_army()*land.get_nbPlayers()):
                player = land.players[i%land.get_nbPlayers()]
                terr = land._setup_armies(player)
                text_surface, rect = GAME_FONT.render(str(terr.get_army()), terr.get_ownership().get_color())
                self._display_surf.blit(text_surface, [terr.get_x() + (terr.get_size()[0] - FONT_SIZE)/2, terr.get_y() + (terr.get_size()[1] - FONT_SIZE)/2])
                self.on_render()
        print('\n',"////////////////////////////////////")
        print("Armies ready",'\n')
        print("Land ready for battle!",'\n')
        # for terr in territories:
        #     text_surface, rect = GAME_FONT.render(str(terr.get_army()), terr.get_ownership().get_color())
        #     self._display_surf.blit(text_surface, [terr.get_x() + (terr.get_size()[0] - FONT_SIZE)/2, terr.get_y() + (terr.get_size()[1] - FONT_SIZE)/2])
        self.on_render()

    def on_loop(self):
        pass
    def on_display(self):
        self._display_surf.blit(BACKGROUND, [0, 0])
        global territories, FONT_SIZE
        for i in range(len(territories)):
            terr = territories[i]
            text_surface, rect = GAME_FONT.render(str(terr.get_army()), terr.get_ownership().get_color())
            self._display_surf.blit(text_surface, [terr.get_x() + (terr.get_size()[0] - FONT_SIZE)/2, terr.get_y() + (terr.get_size()[1] - FONT_SIZE)/2])
        self.on_render()
    def on_render(self, rect = None):
        pg.display.update(rect)
    def on_cleanup(self):
        pg.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        global GAME_FONT
        text_surface, rect = GAME_FONT.render("1,2,3,4,5,6,7,8,9,10", WHITE)
 
        while( self._running ):
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()