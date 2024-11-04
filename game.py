import pygame, config
from Classes import tile
import sys
from spritesheet import SpriteSheet
import Player

tileMap = [
    [config.TL_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TE_TILE, config.TR_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.LE_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.GM_TILE, config.RE_TILE],
    [config.BL_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BE_TILE, config.BR_TILE]
    ]

# this would not be set in real game, but rather obtained from database or previous screen
chosenCharacter = "female"

# how long each frame lasts
ANIMATION_COOLDOWN = 100

# stores time since last frame has been updated
lastUpdate = pygame.time.get_ticks()

frame = 0

# load player sprite sheet
maleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()
femaleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/femaleMC-spritesheet.png").convert_alpha()

# creates a list of different sprite images
def createSpriteFrameList(img, numFrames, row):

    # creates an object of the sprite sheet image
    spritesheet = SpriteSheet(img)

    list = []

    # repeats for each frame
    for x in range(numFrames):

        # adds that frame image to list
        list.append(spritesheet.getImage(x+1, row, 64, 64, 1.5))

    return list

def createIdleList(img):

    # creates an object of the sprite sheet image
    spritesheet = SpriteSheet(img)

    list = []

    # repeats for 4 directions
    for x in range(4):

        # adds that frame image to list
        list.append(spritesheet.getImage(0, x, 64, 64, 1.5))
    
    return list
                       
def createAnimationList(spritesheet):

    playerWalkUp = createSpriteFrameList(spritesheet, 8, 8)
    playerWalkLeft = createSpriteFrameList(spritesheet, 8, 9)
    playerWalkDown = createSpriteFrameList(spritesheet, 8, 10)
    playerWalkRight = createSpriteFrameList(spritesheet, 8, 11)

    playerWalkList = [playerWalkUp, playerWalkLeft, playerWalkDown, playerWalkRight]

    playerTillWaterUp = createSpriteFrameList(spritesheet, 7, 4)
    playerTillWaterLeft = createSpriteFrameList(spritesheet, 7, 5)
    playerTillWaterDown = createSpriteFrameList(spritesheet, 7, 6)
    playerTillWaterRight = createSpriteFrameList(spritesheet, 7, 7)

    playerTillWaterList = [playerTillWaterUp, playerTillWaterLeft, playerTillWaterDown, playerTillWaterRight]

    playerPlantUp = createSpriteFrameList(spritesheet, 5, 12)
    playerPlantLeft = createSpriteFrameList(spritesheet, 5, 13)
    playerPlantDown = createSpriteFrameList(spritesheet, 5, 14)
    playerPlantRight = createSpriteFrameList(spritesheet, 5, 15)

    playerPlantList = [playerPlantUp, playerPlantLeft, playerPlantDown, playerPlantRight]

    return playerWalkList, playerTillWaterList, playerPlantList

def main():
    running = True

    global chosenCharacter

    if chosenCharacter == "male":
        walkList, tillWaterList, plantList = createAnimationList(maleMCSpriteSheet)
        idleList = createIdleList(maleMCSpriteSheet)
    else:
        walkList, tillWaterList, plantList = createAnimationList(femaleMCSpriteSheet)
        idleList = createIdleList(femaleMCSpriteSheet)

    player = Player.Player(300, 500, maleMCSpriteSheet, idleList, "Bob", walkList, tillWaterList, plantList)

    while running:
        
        # displays the tiles 
        for row in range(len(tileMap)):
            for col in range(len(tileMap[row])):
                tile = tileMap[row][col]
                config.SCREEN.blit(tile, (col*72, row*72))

        # gets player direction and co-ordinates
        direction = player.whichDirection()
        x, y = player.getPosition()

        if player.isMoving():

            player.animateWalk()

        else:
            player.drawIdle()
        

        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()
    
                if keys[pygame.K_a]:
                    player.setMoving(True)
                    player.changeDirection(1)
                    player.changePosition(x-5, y)
                    print("a")

                if keys[pygame.K_d]:
                    player.setMoving(True)
                    player.changeDirection(3)
                    player.changePosition(x+5, y)

                if keys[pygame.K_w]:
                    player.setMoving(True)
                    player.changeDirection(0)
                    player.changePosition(x, y-5)

                if keys[pygame.K_s]:
                    player.setMoving(True)
                    player.changeDirection(2)
                    player.changePosition(x, y+5)

                
            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        pygame.display.update()
                