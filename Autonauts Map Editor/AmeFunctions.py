import json
import os


def getDimension() -> (int, int):
    global mapWide, mapHigh
    return mapWide, mapHigh


def fileImport(path: str):
    global worldData

    with open(path, "r") as file:
        worldData = json.load(file)


def fileToRaw():
    global worldData, rawMap, mapWide, mapHigh

    rawMap = worldData["Tiles"]["TileTypes"]
    mapWide = worldData["Tiles"]["TilesWide"]
    mapHigh = worldData["Tiles"]["TilesHigh"]


def rawToTile():
    global worldData, rawMap, mapWide, mapHigh, tileMap

    tileMap = [[] for x in range(mapHigh)]
    counter = 0

    for tileType, tileCounts in zip(rawMap[::2], rawMap[1::2]):
        for i in range(tileCounts):
            tileMap[int(counter / mapWide)].append(tileType)
            counter += 1


def getTileMap():
    global tileMap
    return tileMap


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


def worldTxtLoad(path: str):
    global tileMap

    fileImport(path)
    fileToRaw()
    rawToTile()
    return tileMap


def exportSaveAs(path: str) -> None:
    pass