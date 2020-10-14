import json
import copy


class World:

    def __init__(self, worldPath):
        self.path = worldPath
        self.tile2DMap = self.loadWorld()
        self.original = copy.deepcopy(self.tile2DMap)

    def loadWorld(self):
        
        # import file
        with open(self.path, "r") as file:
            self.rawData = json.load(file)

        # Error checking if it's correct txt file
        # TODO

        # file to raw data. Raw data stored the whole save
        self.rawMap = self.rawData["Tiles"]["TileTypes"]
        self.wide = self.rawData["Tiles"]["TilesWide"]
        self.high = self.rawData["Tiles"]["TilesHigh"]

        # raw data to tile
        tileMap = [[] for x in range(self.high)]
        counter = 0
        
        for tileType, tileCounts in zip(self.rawMap[::2], self.rawMap[1::2]):
            for i in range(tileCounts):
                tileMap[counter // self.wide].append(tileType)
                counter += 1

        return tileMap


    def exportWorld(self, path):
        self.rawList = []
        
        lastTileType = tileType = 0
        tileCounts = 0

        # encode tile2DMap back to rawMap
        for i in range(self.high):
            for j in range(self.wide):
                tileType = self.tile2DMap[i][j]
                if i == j and j == 0:
                    lastTileType = tileType

                if lastTileType == tileType:
                    tileCounts += 1
                else:
                    self.rawList.append(lastTileType)
                    self.rawList.append(tileCounts)
                    tileCounts = 1
                lastTileType = tileType
        self.rawList.append(lastTileType)
        self.rawList.append(tileCounts)
            
        self.rawData["Tiles"]["TileTypes"] = self.rawList
        with open(path + f"/World.txt", "w") as file:
            json.dump(self.rawData, file, separators=(",", ":"))



# debug printer to .txt
def printTileMapToTxt():
    global tileMap
    with open("tileMap.txt", "w") as file:
        for row in tileMap:
            for tile in row:
                file.write(f"{tile:2}")
            file.write("\n")
