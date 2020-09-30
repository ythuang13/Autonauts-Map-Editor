import pygame
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

TILES_TYPE_DICT = {0: pygame.Color("#81D800"), # grass
                 1: pygame.Color("#B98524"), # dirt
                 6: pygame.Color("#C0D3FD"), # coast
                 7: pygame.Color("#454FFF"), # ocean
                 8: pygame.Color("#A0FAFD"), # lake
                 9: pygame.Color("#1AF5B3"), # shallow water
                 10: pygame.Color("#FEF82D"), # sand
                 12: pygame.Color("#8FE58F"), # swamp
                 14: pygame.Color("#8E9A5D"), # metal ore
                 19: pygame.Color("#D84E09"), # clay
                 29: pygame.Color("#8E9A5D"), # metal ore
                 }

# game settings
ENLARGE = 7
FPS = 30
TITLE = "Autonauts Map Editor"
#BGCOLOR = DARKGREY

TILESIZE = ENLARGE
