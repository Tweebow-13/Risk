from Territory import Territory
from Player import Player

import numpy as np

class Land:

    def __init__(self, inTerritories, inPlayers, randomTerr = False, randomArmies = False):
        self.nbTerritories = len(inTerritories)
        self.nbPlayers = len(inPlayers)
        self.players = inPlayers
        self.territories = inTerritories
        self._setup(randomTerr, randomArmies)
        print(self)
    
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
            print("Player", str(player.get_color()), "owns", str(player.get_territoriesCount()), "territories with a total army of", str(player.get_army()),"soldiers.")
            player.show_player(self)
        return("")
    
    def _available_terr(self):
        available = []
        for i in range(self.get_nbTerritories()):
            terr = self.get_territories()[i]
            if terr.get_ownership() == None:
                available.append([i, terr.get_name()])
        return available

    def _setup(self, randomTerr, randomArmies):
        if randomTerr:
            self._setup_random_territories()
        else:
            self._setup_territories()
        if randomArmies:
            self._setup_random_armies()
        else:
            self._setup_armies()

    def _setup_random_territories(self):
        for i in range(self.get_nbTerritories()):
            player = self.players[i%self.get_nbPlayers()]
            available_terr = self._available_terr()
            index = np.random.randint(len(available_terr))
            terr = self.get_territories()[available_terr[index][0]]
            player.assign(terr)
        print('\n',"////////////////////////////////////")
        print("Territories ready",'\n','\n')

    def _setup_territories(self):
        for i in range(self.get_nbTerritories()):
            player = self.players[i%self.get_nbPlayers()]
            print("It's player", player, "'s turn")
            terr = self._unoccupiedTerr()
            player.assign(terr)
        print('\n',"////////////////////////////////////")
        print("Territories ready",'\n','\n')
    
    def _setup_random_armies(self):
        for i in range(self.get_nbTerritories(), self.get_players()[0].get_army()*self.get_nbPlayers()):
            player = self.players[i%self.get_nbPlayers()]
            owned_terr = player.ownedTerrList(self)
            index = np.random.randint(len(owned_terr))
            terr = self.get_territories()[owned_terr[index][0]]
            player.assign(terr)
        print('\n',"////////////////////////////////////")
        print("Armies ready",'\n')
        print("Land ready for battle!",'\n')
    
    def _setup_armies(self):
        for i in range(self.get_nbTerritories(), self.get_players()[0].get_army()*self.get_nbPlayers()):
            player = self.players[i%self.get_nbPlayers()]
            print("It's player", player, "'s turn")
            terr = self._ownedTerr(player)
            player.assign(terr)
        print('\n',"////////////////////////////////////")
        print("Armies ready",'\n')
        print("Land ready for battle!",'\n')
    
    def _unoccupiedTerr(self):
        print("Please enter the index of the territory you want to conquer within the following list of unoccupied ones:", '\n', self._available_terr())
        index = int(input())
        n = self.get_nbTerritories()
        if (index < 0) or (index >= n):
            while (index < 0) or (index >= n):
                print("Please enter the index of the territory you want to conquer within the following list of unoccupied ones:", '\n', self._available_terr())
                index = int(input())
                #n = len(self.get_nbTerritories())
        terr = self.get_territories()[index]
        if terr.get_ownership() == None:
            return terr
        else:
            terr = self._unoccupiedTerr()
            return terr
    
    def _ownedTerr(self, player):
        print("Please enter the index of the territory you want to put a soldier in within the following list of your occupied ones:", '\n', player.ownedTerrList(self))
        index = int(input())
        n = self.get_nbTerritories()
        if (index < 0) or (index >= n):
            while (index < 0) or (index >= n):
                print("Please enter the index of the territory you want to put a soldier in within the following list of your occupied ones:", '\n', player.ownedTerrList(self))
                index = int(input())
                #n = len(slef.get_nbTerritories())
        terr = self.get_territories()[index]
        if terr.get_ownership() == player:
            return terr
        else:
            terr = self._ownedTerr(player)
            return terr