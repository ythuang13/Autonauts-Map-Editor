import json

def fileImport():
    global worldData

    with open("World.txt", "r") as file:
        worldData = json.load(file)


def fileToRaw():
    global worldData, rawMap, mapWide, mapHigh

    rawMap = worldData["Tiles"]["TileTypes"]
    mapWide = worldData["Tiles"]["TilesWide"]
    mapHigh = worldData["Tiles"]["TilesHigh"]


def rawToTile():
    global worldData, rawMap, mapWide, mapHigh, tileMap

    tileMap = [[] for x in range(mapHigh)]
    print(tileMap)
    counter = 0

    for tileType, tileCounts in zip(rawMap[::2], rawMap[1::2]):
        print(tileType, tileCounts)
        for i in range(tileCounts):
            tileMap[int(counter / mapWide)].append(tileType)
            counter += 1
    


def tileToRaw():
    pass

def rawToFile():
    pass

def fileExport():
    pass

def printTileMapToTxt():
    global tileMap
    with open("tileMap.txt", "w") as file:
        for row in tileMap:
            for tile in row:
                file.write(f"{tile:2}")
            file.write("\n")


mapTileNumber = {1:"grass", 2:"sand"}

if __name__ == "__main__":
    fileImport()
    fileToRaw()
    rawToTile()
    printTileMapToTxt()