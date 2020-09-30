import sys
import pygame as pg
from settings import *
import AmeGui as ag

class Map:
    def __init__(self, tileMap):
        self.tileMap = tileMap
        self.WIDTH = len(tileMap[0]) * ENLARGE
        self.HEIGHT = len(tileMap) * ENLARGE

        pg.init()
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) # TODO
        self.load_data() # TODO


    def load_data(self): # TODO
        pass


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
    

    def colorPicker(self, num):
        if num not in TILES_TYPE_DICT:
            return pygame.Color("#142313") # default
        else:
            return TILES_TYPE_DICT[num]

    
    def drawMap(self):
        currentTile, lastTile = 0, -1
        for y in range(len(self.tileMap[0])):
            for x in range(len(self.tileMap)):
                currentTile = self.tileMap[x][y]
                if currentTile != lastTile:
                    tileColor = self.colorPicker(self.tileMap[x][y])
                lastTile = self.tileMap[x][y]
                pygame.draw.rect(self.screen, tileColor, [y * TILESIZE, x * TILESIZE, TILESIZE, TILESIZE])


    def update(self):
        self.drawMap()


    def draw_grid(self):
        for x in range(0, self.WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, self.HEIGHT))
        for y in range(0, self.HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (self.WIDTH, y))

    def brush(self, x, y):
        brushSize = 10
        for i in range(0 - brushSize // 2, brushSize // 2):
            for j in range(0 - brushSize // 2, brushSize // 2):
                if x + i >= 0 and x + i < (self.WIDTH / TILESIZE) and y + j >= 0 and x + j < (self.HEIGHT / TILESIZE):
                    self.tileMap[y + j][x + i] = 10



    def draw(self):
        #self.screen.fill(BGCOLOR)
        self.draw_grid()
        pg.display.flip()


    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    xPos, yPos = pygame.mouse.get_pos()
                    print(xPos // TILESIZE, yPos // TILESIZE)
                    xPos = xPos // TILESIZE
                    yPos = yPos // TILESIZE
                    self.brush(xPos, yPos)


def launchMap(tileMap):
    ameMap = Map(tileMap)
    while True:
        ameMap.run()