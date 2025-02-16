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

    stage = tilemap[row][col][2]

    tile = tilemap[row][col][1][stage] # accesses crop from array

    return CROP_STAGES.get(tile, None) # if key is not found, grass middle tile is returned

# creates farm map screen
def renderFarmMap(newDay=False):

    # displays tile images from tilemap onto surface
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):

            tileImg = getTileImg(tilemap, row, col) # gets image to display
            
            farmMap.blit(tileImg, (col*72, row*72))

            if tilemap[row][col][1] != None:

                if newDay == True:
                        
                    # gets the number of days the crop has been growing for
                    stage = tilemap[row][col][2]

                    # gets the stage it is at
                    tile = tilemap[row][col][1][stage]

                    # checks if the crop is not fully grown and the tile has been watered
                    if tile[1] != "3" and tilemap[row][col][0] == "WD":
                        stage += 1
                        tilemap[row][col][2] = stage
                        tilemap[row][col][0] = "TD"
 
                cropImg = getCropImg(tilemap, row, col)

                if cropImg is not None:
                    farmMap.blit(cropImg, ((col*72) +10, (row*72) -30))

            if newDay:
                if tilemap[row][col][0] == "WD":
                    tilemap[row][col][0] = "TD"
    
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

            tilemap[playerTileY][playerTileX][1] = cropList
            tilemap[playerTileY][playerTileX][2] = 0
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

                tilemap[playerTileY][playerTileX][1] = cropList
                tilemap[playerTileY][playerTileX][2] = 0

                farmMap = renderFarmMap()

                if player.getFlag() == False:

                    player.inventory.removeItemHeld()
                    player.onFlag()

    player.animatePlanting()

# 2D array storing whole tilemap status
tilemap = [
    [["TL", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TR", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["BL", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BR", None, None]] ]

# creates empty surface 
farmMap = pygame.Surface((1800, 1440))
        