import pygame as pg
from pygame.locals import *
import cevent
import os

from Territory import Territory
from Player import Player

import numpy as np

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 200)
GREY  = (204, 204, 204)

main_dir = os.path.split(os.path.abspath(__file__))[0]
imagename = os.path.join(main_dir, "data", "map.jpg")
BACKGROUND = pg.image.load(imagename)
BACKGROUND.set_colorkey((204,204,204))
fontname = os.path.join(main_dir, "data", "xirod.regular.ttf")
pg.freetype.init()
FONT_SIZE = 12
GAME_FONT = pg.freetype.Font(fontname, FONT_SIZE)

class Land(cevent.CEvent):

    def __init__(self, inTerritories, inPlayers, randomTerr = False, randomArmies = False):
        global BACKGROUND
        BACKGROUND = pg.transform.scale(BACKGROUND, pg.display.get_surface().get_size())
        BACKGROUND = BACKGROUND.convert()
        self.nbTerritories = len(inTerritories)
        self.nbPlayers = len(inPlayers)
        self.players = inPlayers
        self.territories = inTerritories
        # self._setup(randomTerr, randomArmies)
        #print(self)
    
    def get_players(self):
        return self.players
    
    def get_territories(self):
        return self.territories
    
    def get_nbTerritories(self):
        return self.nbTerritories

    def get_nbPlayers(self):
        return self.nbPlayers
    
    def __str__(self):
        print('\n', self.nbPlayers, "players are still in the game for this land of", self.nbTerritories, "territories.",'\n')
        for player in self.players:
            print("Player", str(player.get_name()), "owns", str(player.get_territoriesCount()), "territories with a total army of", str(player.get_army()),"soldiers.")
            player.show_player(self)
        return("")
    
    def _available_terr(self):
        available = []
        for i in range(self.get_nbTerritories()):
            terr = self.get_territories()[i]
            if terr.get_ownership() == None:
                available.append([i, terr.get_name()])
        return available

    # def _setup(self, randomTerr, randomArmies):
    #     if randomTerr:
    #         self._setup_random_territories()
    #     else:
    #         self._setup_territories()
    #     if randomArmies:
    #         self._setup_random_armies()
    #     else:
    #         self._setup_armies()

    def _setup_random_territories(self, player):
        available_terr = self._available_terr()
        index = np.random.randint(len(available_terr))
        terr = self.get_territories()[available_terr[index][0]]
        player.assign(terr)

    def _setup_territories(self, player):
        print("It's player", player, "'s turn")
        terr = self._unoccupiedTerr()
        player.assign(terr)
        return(terr)
    
    def _unoccupiedTerr(self):
        print("Please click on the territory you want to conquer within the unoccupied ones:")
        picking = True
        n = self.get_nbTerritories()
        terr_rect_list = [terr.get_rect() for terr in self.get_territories()]
        while picking:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.on_exit()
                    quit()
                if (event.type == MOUSEBUTTONUP) and (event.button == 1):
                    click = self.on_event(event)
                    for i in range(len(terr_rect_list)):
                        rect = terr_rect_list[i]
                        if rect.collidepoint(click):
                            picking = False
                            index = i
        terr = self.get_territories()[index]
        if terr.get_ownership() == None:
            return terr
        else:
            return(self._unoccupiedTerr())
    
    def _setup_random_armies(self, player):
        owned_terr = player.ownedTerrList(self)
        index = np.random.randint(len(owned_terr))
        terr = self.get_territories()[owned_terr[index][0]]
        player.assign(terr)
    
    def _setup_armies(self, player):
        # print("It's player", player, "'s turn")
        terr = self._ownedTerr(player)
        player.assign(terr)
        print('')
        return(terr)
    
    def _ownedTerr(self, player):
        print("Please click on the territory you want to put a soldier in within your owned ones:")
        picking = True
        n = self.get_nbTerritories()
        terr_rect_list = [terr.get_rect() for terr in self.get_territories()]
        while picking:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.on_exit()
                    quit()
                if (event.type == MOUSEBUTTONUP) and (event.button == 1):
                    click = self.on_event(event)
                    for i in range(len(terr_rect_list)):
                        rect = terr_rect_list[i]
                        if rect.collidepoint(click):
                            picking = False
                            index = i
        terr = self.get_territories()[index]
        if terr.get_ownership() == player:
            return terr
        else:
            return(self._ownedTerr(player))
    
    def attack(self, player, till_end = True):
        terr_rect_list = [terr.get_rect() for terr in self.get_territories()]
        picking = True
        click1 = None
        click2 = None
        while picking:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.on_exit()
                    quit()
                if (event.type == MOUSEBUTTONUP) and (event.button == 1):
                    if click1 == None:
                        click1 = self.on_event(event)
                        for i in range(len(terr_rect_list)):
                            rect = terr_rect_list[i]
                            if rect.collidepoint(click1):
                                index = i
                                terr1 = self.get_territories()[index]
                                if terr1.get_ownership() != player:
                                    print("This is not your territory", '\n', "Can't attack")
                                    self.attack(player)
                                elif terr1.get_army() < 2:
                                    print("Too few soldiers on this territory.", '\n', "Can't attack")
                                    self.attack(player)
                    else:
                        click2 = self.on_event(event)
                        for i in range(len(terr_rect_list)):
                            rect = terr_rect_list[i]
                            if rect.collidepoint(click2):
                                index = i
                                terr2 = self.get_territories()[index]
                                if terr2.get_ownership() == player:
                                    print("You already own this territory", '\n', "Can't attack")
                                    self.attack(player)
                        picking = False

        battle = player.battle(terr1.get_army(), terr2.get_army(), till_end)
        terr2.get_ownership().set_army(terr2.get_ownership().get_army() - battle[4])
        player.set_army(player.get_army() - battle[3])
        print("Battle finished")
        if battle[0]:
            terr2.get_ownership().set_territoriesCount(terr2.get_ownership().get_territoriesCount() - 1)
            terr2.set_ownership(player)
            player.set_territoriesCount(player.get_territoriesCount() + 1)
            terr1.set_army(terr1.get_army() - battle[3] - 1)
            terr2.set_army(1)
            print(player, "took ownership of", terr2.get_name(), "loosing", battle[3], "soldiers.", '\n')
        else:
            terr1.set_army(terr1.get_army() - battle[3])
            terr2.set_army(terr2.get_army() - battle[4])
            print("The defender held his position loosing", battle[4], "soldiers.", '\n')

    # def on_render(self, rect = None):
    #     pg.display.update(rect)
    def on_exit(self):
        pg.quit()