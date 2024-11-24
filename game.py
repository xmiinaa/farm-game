import pygame
from config import *
import sys
from spritesheet import SpriteSheet
import Player

# returns tile image of from a specific index of tilemap array
def getTileImg(tilemap, row, col):

    tile = tilemap[row][col] # accesses tile from array

    return TILE_IMAGES.get(tile, GM_TILE) # if key is not found, grass middle tile is returned


def renderMap(tilemap, playerX, playerY):

    # calculates the top-left corner co-ordinates of the displayed map
    VIEW_X = max(0, playerX - VIEW_WIDTH // 2) # max ensures that the value is never below 0
    VIEW_Y = max(0, playerY - VIEW_HEIGHT // 2)

    # Ensure the viewport doesn't go out of bounds
    VIEW_X = min(VIEW_X, len(tilemap[0]) - VIEW_WIDTH) # min ensures that the value is never to far out
    VIEW_Y = min(VIEW_Y, len(tilemap) - VIEW_HEIGHT)

    # displays visible portion of the map
    for row in range(VIEW_WIDTH):
        for col in range(VIEW_WIDTH):

            # calculates actual tile position in map
            tileX = VIEW_X + col
            tileY = VIEW_Y + row

            if 0 <= tileX < len(tilemap[0]) and 0 <= tileY < len(tilemap): 

                # gets tile image to display
                tileImage = getTileImg(tilemap, tileY, tileX)

                SCREEN.blit(tileImage, (col * TILE_SIZE, row * TILE_SIZE))

# creates farm map screen
def renderFarmMap():

    # creates empty surface 
    farmMap = pygame.Surface((1800, 1440))

    # displays tile images from tilemap onto surface
    for row in range(len(tilemap)):
        for col in range(len(tilemap[row])):

            tileImg = getTileImg(tilemap, row, col) # gets image to display
            
            farmMap.blit(tileImg, (col*72, row*72))
    
    return farmMap

# this would not be set in real game, but rather obtained from database or previous screen
chosenCharacter = "female"

def main():
    running = True

    global chosenCharacter

    # creates player object depending on the variable, chosenCharacter
    if chosenCharacter == "male":
        player = Player.Player(540, 360, maleMCSpriteSheet, "Bob")

    else: # creates female player
        player = Player.Player(540, 360, femaleMCSpriteSheet, "Yue")

    # creates the farmMap
    farmMap = renderFarmMap()

    # gets co-ordinates of camera
    cameraPos = player.getMapPos()

    while running:

        # gets player direction and co-ordinates
        x, y = player.getPosition()
        direction = player.whichDirection()

        # displays background tiles
        SCREEN.blit(farmMap, (cameraPos[0]-180, cameraPos[1]-360))

        # checks if the player is moving and they are not in another action, and displays it appropiately if they are
        if player.isMoving() and player.isActive() == False:

            player.animateWalk()
            player.move()

        # checks to see if the player is currently doing an action
        elif player.getAction() != "idle":

            # checks to see if the player is active
            if player.isActive():

                if player.getAction() == "tillWater":
    
                    player.animateTillWater()
                
                elif player.getAction() == "planting":

                    player.animatePlanting()

        # displays the player in its idle state
        else:
            player.drawIdle()
    
        #renderMap(tilemap, x, y)
        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
                    player.setMoving(True)
    
                if keys[pygame.K_a] and direction != 1:
                    player.changeDirection(1)

                elif keys[pygame.K_d]:
                    player.changeDirection(3)

                if keys[pygame.K_w]:
                    player.changeDirection(0)

                elif keys[pygame.K_s]:
                    player.changeDirection(2)

            # checks if player is not pressing down a key
            if event.type == pygame.KEYUP:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                    player.setMoving(False)
    
            # checks if he player has clicked on the mouse
            if pygame.mouse.get_pressed()[0]:

                # ensures the player is not already engaged in another action
                if player.isActive() == False:

                    player.resetAnimation() # sets animation back to 0
                    player.activate()

                    # gets the item that the player is currently holding
                    item = player.getItem()
                
                    if item == "hoe" or item == "waterCan":

                        # changes the attribute as appropiate
                        player.changeAction("tillWater")
                    
                    if item == "seed":

                        # changes the attribute as appropiate
                        player.changeAction("planting")
                
            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        CLOCK.tick(60)
        pygame.display.update()
                