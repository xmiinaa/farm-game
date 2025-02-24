import pygame
from config import *
from game import *
from Player import *
from furniture import *
from inventory import *

plantingDone = False

# returns tile image of from a specific index of tilemap array
def getTileImg(tilemap, row, col):

    tile = tilemap[row][col][0] # accesses tile from array

    return TILE_IMAGES.get(tile, GM_TILE) # if key is not found, grass middle tile is returned

def getCropImg(tilemap, row, col):

    stage = tilemap[row][col][2] # gets the stage of the crop

    tile = tilemap[row][col][1][stage] # accesses crop from array

    return CROP_STAGES.get(tile, None) # if key is not found, grass middle tile is returned

# creates farm map screen
def renderFarmMap():


    # displays tile images from tilemap onto surface
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):

            tileImg = getTileImg(tilemap, row, col) # gets image to display
            
            farmMap.blit(tileImg, (col*72, row*72))

            # checks if there is a crop
            if tilemap[row][col][1] != None:

                cropImg = getCropImg(tilemap, row, col)

                if cropImg is not None:
                    farmMap.blit(cropImg, ((col*72) +10, (row*72) -30))
    
    displayMCHouse()
    
    return farmMap

def displayMCHouse():
    farmMap.blit(MCHouseTopWall, (432, 432))
    farmMap.blit(MCHouseTopWall, (504, 432))
    farmMap.blit(MCHouseTopWall, (576, 432))
    farmMap.blit(MCHouseTopWall, (648, 432))

    farmMap.blit(MCHouseBottomWall, (432, 504))
    farmMap.blit(MCHouseBottomWall, (504, 504))
    farmMap.blit(MCHouseBottomWall, (576, 504))
    farmMap.blit(MCHouseBottomWall, (648, 504))

    farmMap.blit(MCHouseMiddleFloor, (432, 574))
    farmMap.blit(MCHouseMiddleFloor, (504, 574))
    farmMap.blit(MCHouseMiddleFloor, (576, 574))
    farmMap.blit(MCHouseMiddleFloor, (648, 574))

    farmMap.blit(MCHouseMiddleFloor, (432, 644))
    farmMap.blit(MCHouseMiddleFloor, (504, 644))
    farmMap.blit(MCHouseMiddleFloor, (576, 644))
    farmMap.blit(MCHouseMiddleFloor, (648, 644))

    farmMap.blit(MCHouseMiddleFloor, (432, 714))
    farmMap.blit(MCHouseMiddleFloor, (504, 714))
    farmMap.blit(MCHouseMiddleFloor, (576, 714))
    farmMap.blit(MCHouseMiddleFloor, (648, 714))

    farmMap.blit(window1, (530, 460))
    farmMap.blit(blueCurtains, (525, 455))
    farmMap.blit(blueBed, (440, 535))
    farmMap.blit(MCDresser, (510, 545))
    farmMap.blit(MCbookshelf, (625, 495))
    farmMap.blit(bluecirclerug, (435, 640))
    farmMap.blit(flowepot, (522, 520))

    pygame.draw.rect(farmMap, BROWN1, pygame.Rect(430, 430, 292, 356), 2)
    pygame.draw.rect(farmMap, BROWN2, pygame.Rect(428, 428, 296, 360), 2)
    pygame.draw.rect(farmMap, BROWN3, pygame.Rect(426, 426, 300, 364), 2)
    pygame.draw.rect(farmMap, BROWN4, pygame.Rect(424, 424, 304, 368), 2)
    pygame.draw.rect(farmMap, BROWN3, pygame.Rect(422, 422, 308, 372), 2)
    pygame.draw.rect(farmMap, BROWN2, pygame.Rect(420, 420, 312, 376), 2)
    pygame.draw.rect(farmMap, BROWN1, pygame.Rect(418, 418, 316, 380), 2)

    pygame.draw.rect(farmMap, GM_GREEN, pygame.Rect(522, 785, 100, 14))


def itsanewDay(weather):
    
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):
            # checks if there is a crop
            if tilemap[row][col][1] != None:
                        
                # gets the number of days the crop has been growing for
                stage = tilemap[row][col][2]

                # gets the stage it is at
                tile = tilemap[row][col][1][stage]

                # checks if the crop is not fully grown and the tile has been watered
                if tile[1] != "3" and tilemap[row][col][0] == "WD":
                    stage += 1
                    tilemap[row][col][2] = stage

            if weather == "Rainy":
                if tilemap[row][col][0] == "TD" or tilemap[row][col][0] == "WD":
                    tilemap[row][col][0] = "WD"

            elif weather == "Sunny" or weather == "Cloudy":
                if tilemap[row][col][0] == "TD" or tilemap[row][col][0] == "WD":
                    tilemap[row][col][0] = "TD"

# tills the tile
def till(player, mousePos, key, weather):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile is "tillable"
    if tilemap[playerTileY][playerTileX][0] == "GM":

        #  checks if the player pressed the key x
        if key == "x":

            # if it is raining
            if weather == 2:
                tilemap[playerTileY][playerTileX][0] = "WD" # tile is already watered from rain
            
            else:
                # changes the tile to tilled land and displays it
                tilemap[playerTileY][playerTileX][0] = "TD"
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                if weather == 2:
                    tilemap[playerTileY][playerTileX][0] = "WD"
            
                else:
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
            tilemap[playerTileY][playerTileX][2] = None
            farmMap = renderFarmMap()

        # checks to see if the player clicked on the mouse
        if key == "mouse":
            
            # checks to see if the user had clicked the player
            if player.mouseOnPlayer(mousePos):

                # changes the tile to untilled land and displays it
                tilemap[playerTileY][playerTileX][0] = "GM"
                tilemap[playerTileY][playerTileX][1] = None
                tilemap[playerTileY][playerTileX][2] = None
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

# plants seeds in a tile
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
            cropList = SEED_TO_CROP_STAGES.get(playerItem, None)

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
                cropList = SEED_TO_CROP_STAGES.get(playerItem, None)

                tilemap[playerTileY][playerTileX][1] = cropList
                tilemap[playerTileY][playerTileX][2] = 0

                farmMap = renderFarmMap()

                if player.getFlag() == False:

                    player.inventory.removeItemHeld()
                    player.onFlag()

    player.animatePlanting()

# restores the tile back to its original state
def harvest(player, mousePos, key):

    global farmMap

    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    # checks to see if the tile has a crop planted
    if tilemap[playerTileY][playerTileX][1] != None:

        stage = tilemap[playerTileY][playerTileX][2] # gets the current stage of the crop

        if tilemap[playerTileY][playerTileX][1][stage][1] == "3": # checks if the crop is at its last stage

            #  checks if the player pressed the key x or has clicked on the player
            if key == "x" or (key == "mouse" and player.mouseOnPlayer(mousePos)):

                cropStage = tilemap[playerTileY][playerTileX][1][stage]

                crop = CROP_STAGE3_TO_CROP.get(cropStage, None)

                player.inventory.add(crop)

                # changes the tile to untilled land and displays it
                tilemap[playerTileY][playerTileX][0] = "GM"
                tilemap[playerTileY][playerTileX][1] = None
                tilemap[playerTileY][playerTileX][2] = None
                farmMap = renderFarmMap()
            
            else:
                player.deactivate()
                player.changeAction("idle") # resets player to idle state
    
        else:
            player.deactivate()
            player.changeAction("idle") # resets player to idle state

    else:
        player.deactivate()
        player.changeAction("idle") # resets player to idle state

def checkEdgeOfFarm(player):
    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    if tilemap[playerTileY][playerTileX][0] == "DE":
        return True
    else:
        return False

# 2D array storing whole tilemap status
tilemap = [
    [["TL", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TR", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["DE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["DE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["BL", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BR", None, None]] ]

# creates empty surface 
farmMap = pygame.Surface((1800, 1440))
house = pygame.Rect(417,417, 318, 160)
