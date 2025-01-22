import pygame
from config import *
from game import *
from Player import *

plantingDone = False

# returns tile image of from a specific index of tilemap array
def getTileImg(tilemap, row, col):

    tile = tilemap[row][col][0] # accesses tile from array

    return TILE_IMAGES.get(tile, GM_TILE) # if key is not found, grass middle tile is returned

def getCropImg(tilemap, row, col):

    tile = tilemap[row][col][1] # accesses crop from array

    return CROP_STAGES.get(tile, None) # if key is not found, grass middle tile is returned

# creates farm map screen
def renderFarmMap():

    # displays tile images from tilemap onto surface
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):

            tileImg = getTileImg(tilemap, row, col) # gets image to display
            
            farmMap.blit(tileImg, (col*72, row*72))

            if tilemap[row][col][1] != None:

                cropImg = getCropImg(tilemap, row, col)
                if cropImg is not None:
                    farmMap.blit(cropImg, ((col*72) +10, (row*72) -30))
    
    return farmMap

# tills the tile
def till(player, mousePos, key):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile is "tillable"
    if tilemap[playerTileY][playerTileX][0] == "GM":

        #  checks if the player pressed the key x
        if key == "x":

            # changes the tile to tilled land and displays it
            tilemap[playerTileY][playerTileX][0] = "TD"
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # changes the tile to tilled land and displays it
                tilemap[playerTileY][playerTileX][0] = "TD"
                farmMap = renderFarmMap()
    
    player.animateTillWater()

# restores the tile back to its original state
def untill(player, mousePos, key):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile has been tilled
    if tilemap[playerTileY][playerTileX][0] == "TD" or tilemap[playerTileY][playerTileX][0] == "WD":

        #  checks if the player pressed the key x
        if key == "x":

            # changes the tile to untilled land and displays it
            tilemap[playerTileY][playerTileX][0] = "GM"
            tilemap[playerTileY][playerTileX][1] = None
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # changes the tile to untilled land and displays it
                tilemap[playerTileY][playerTileX][0] = "GM"
                tilemap[playerTileY][playerTileX][1] = None
                farmMap = renderFarmMap()
    
    # animates the player
    player.animateTillWater()

# waters the tile
def water(player, mousePos, key):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile is "tillable"
    if tilemap[playerTileY][playerTileX][0] == "TD":

        #  checks if the player pressed the key x
        if key == "x":

            # changes the tile to tilled land and displays it
            tilemap[playerTileY][playerTileX][0] = "WD"
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # changes the tile to tilled land and displays it
                tilemap[playerTileY][playerTileX][0] = "WD"
                farmMap = renderFarmMap()
    
    # animates the player
    player.animateTillWater()

def plant(player, mousePos, key):
    global farmMap, plantingDone

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    playerItem = player.inventory.getItem()
    
    # checks to see if the tile is "plantable"
    if (tilemap[playerTileY][playerTileX][0] == "TD" or tilemap[playerTileY][playerTileX][0] == "WD") and tilemap[playerTileY][playerTileX][1] == None:

        #  checks if the player pressed the key x
        if key == "x" and player.isActive():

            # calculates the code for the crop
            cropList = SEED_TO_CROPS.get(playerItem, None)

            tilemap[playerTileY][playerTileX][1] = cropList[0]
            farmMap = renderFarmMap()

            if player.getFlag() == False:

                player.inventory.removeItemHeld()
                player.onFlag()

        # checks to see if the player clicked on the mouse
        if key == "mouse" and player.isActive():
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # calculates the code for the crop
                cropList = SEED_TO_CROPS.get(playerItem, None)

                tilemap[playerTileY][playerTileX][1] = cropList[0]
                farmMap = renderFarmMap()

                if player.getFlag() == False:

                    player.inventory.removeItemHeld()
                    player.onFlag()

    player.animatePlanting()

# 2D array storing whole tilemap status
tilemap = [
    [["TL", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TE", None], ["TR", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["LE", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["GM", None], ["RE", None]],
    [["BL", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BE", None], ["BR", None]] ]

# creates empty surface 
farmMap = pygame.Surface((1800, 1440))
        