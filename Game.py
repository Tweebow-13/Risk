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

# main_dir = os.path.split(os.path.abspath(__file__))[0]

# def load_image(file):
#     """ loads an image, prepares it for play
#     """
#     file = os.path.join(main_dir, "data", file)
#     try:
#         surface = pg.image.load(file)
#     except pg.error:
#         raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
#     return surface.convert()

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
