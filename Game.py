from Land import Land
from Territory import Territory
from Player import Player
from CApp import CApp
import os

Blue = Player("Blue")
Red = Player("Red")
Toulon = Territory("Toulon")
Marseille = Territory("Marseille")
Ollioules = Territory("Ollioules")
Rouen = Territory("Rouen")
Sanary = Territory("Sanary")
Hyeres = Territory("Hyeres")
Quincampoix = Territory("Quincampoix")

if __name__ == "__main__" :
    theApp = CApp()
    theApp.on_execute()
#game = Land([Toulon, Marseille, Ollioules, Rouen, Sanary, Hyeres], [Blue, Red], True, True)


# print(game)
# print(Toulon.get_ownership())
# Toulon.set_ownership(Blue)
# Blue.set_territoriesCount(Blue.get_territoriesCount() + 1)
# print(Toulon.get_ownership())
# Toulon.set_army(5)
# Marseille.set_ownership(Red)
# Red.set_territoriesCount(Red.get_territoriesCount() + 1)
# print(game)
# Marseille.set_army(10)
# Red.attack(Marseille, Toulon)
# print(game)
# print(Toulon.get_ownership())
