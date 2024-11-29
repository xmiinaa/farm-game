import pygame
from config import *
from game import *
from Player import *

# returns tile image of from a specific index of tilemap array
def getTileImg(tilemap, row, col):

    tile = tilemap[row][col] # accesses tile from array

    return TILE_IMAGES.get(tile, GM_TILE) # if key is not found, grass middle tile is returned

# creates farm map screen
def renderFarmMap():

    # displays tile images from tilemap onto surface
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):

            tileImg = getTileImg(tilemap, row, col) # gets image to display
            
            farmMap.blit(tileImg, (col*72, row*72))
    
    return farmMap

# tills the tile
def till(player, mousePos, key):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile is "tillable"
    if tilemap[playerTileY][playerTileX] == "GM":

        #  checks if the player pressed the key x
        if key == "x":

            # changes the tile to tilled land and displays it
            tilemap[playerTileY][playerTileX] = "TD"
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # changes the tile to tilled land and displays it
                tilemap[playerTileY][playerTileX] = "TD"
                farmMap = renderFarmMap()
    
    player.animateTillWater()
        
# waters the tile
def water(player, mousePos, key):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile is "tillable"
    if tilemap[playerTileY][playerTileX] == "TD":

        #  checks if the player pressed the key x
        if key == "x":

            # changes the tile to tilled land and displays it
            tilemap[playerTileY][playerTileX] = "WD"
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # changes the tile to tilled land and displays it
                tilemap[playerTileY][playerTileX] = "WD"
                farmMap = renderFarmMap()
    
    # animates the player
    player.animateTillWater()

# 2D array storing whole tilemap status
tilemap = [
    ["TL", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TR"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "WD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "TD", "TD", "TD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "TD", "WD", "WD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "WD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "TD", "TD", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "WD", "GM"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "WD", "GM"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "WD", "WD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "TD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "WD", "WD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "TD", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "WD", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "TD", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["BL", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BR"]]

# creates empty surface 
farmMap = pygame.Surface((1800, 1440))
        