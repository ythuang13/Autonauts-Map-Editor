import sys
import math
import pygame as pg
import PySimpleGUI as sg
from settings import *
from World import World
from Toolbar import Toolbar
from AmeExport import exportMain


class Map:
    def __init__(self, setWorld):
        self.world = setWorld
        self.TILESIZE = WINDOW_WIDTH // self.world.wide
        self.toolbar = Toolbar()

        pg.init()
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100) # TODO
        self.load_data() # TODO


    def load_data(self): # TODO
        pass


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        self.clicking = False

        self.drawMap()
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            

    def quit(self):
        self.toolbar.quit()
        pg.quit()
        exportMain(self.world)
    

    def colorPicker(self, num):
        if num not in TILES_TYPE_DICT:
            return pygame.Color("#142313") # default
        else:
            return TILES_TYPE_DICT[num]

    
    def drawMap(self):
        currentTile, lastTile = 0, -1
        for y in range(self.world.wide):
            for x in range(self.world.high):
                currentTile = self.world.tile2DMap[x][y]
                if currentTile != lastTile:
                    tileColor = self.colorPicker(self.world.tile2DMap[x][y])
                lastTile = self.world.tile2DMap[x][y]
                pygame.draw.rect(self.screen, tileColor, [y * self.TILESIZE, x * self.TILESIZE, self.TILESIZE, self.TILESIZE])


    def update(self):
        #self.drawMap()
        pass


    def draw_grid(self):
        for x in range(0, WINDOW_WIDTH, self.TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, self.TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WINDOW_WIDTH, y))


    def brush(self, x, y):
        for i in range(0 - self.brushSize // 2, self.brushSize // 2):
            for j in range(0 - self.brushSize // 2, self.brushSize // 2):
                if math.sqrt(i ** 2 + j ** 2) < (self.brushSize // 2) and 0 <= x + i < len(self.world.tile2DMap[0]) and 0 <= y + j < len(self.world.tile2DMap):
                    self.world.tile2DMap[y + j][x + i] = self.tileTypeValue
                    pygame.draw.rect(self.screen, self.colorPicker(self.tileTypeValue), [(x + i) * self.TILESIZE, (y + j) * self.TILESIZE, self.TILESIZE, self.TILESIZE])


    def draw(self):
        self.draw_grid()
        #update the canvas
        pg.display.flip()


    def events(self):
        event, values = self.toolbar.toolbarWindow.read(timeout=10)
        self.brushSize = int(values["-brushSize-"]) * 2
        self.tileTypeValue = int(values["-tileTypeSelect-"][0:2])
        if event == sg.WIN_CLOSED:
            self.quit()

        # catch all events here
        mx, my = pygame.mouse.get_pos()

        if self.clicking:
            print(mx // self.TILESIZE, my // self.TILESIZE)
            xPos = mx // self.TILESIZE
            yPos = my // self.TILESIZE
            self.brush(xPos, yPos)

        # event checking
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicking = False


def launchMap(worldPath: str) -> None:
    # initialized world
    world = World(worldPath)
    
    # launch map
    ameMap = Map(world)
    while True:
        ameMap.run()