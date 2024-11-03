import pygame, config
from Classes import tile
import sys
from spritesheet import SpriteSheet

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

# how long each frame lasts
ANIMATION_COOLDOWN = 100

# stores time since last frame has been updated
lastUpdate = pygame.time.get_ticks()

frame = 0

# load player sprite sheet
maleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()
femaleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()

# creates a list of different sprite images
def createSpriteFrameList(img, numFrames, row):

    # creates an object of the sprite sheet image
    spritesheet = SpriteSheet(img)

    list = []

    for x in range(numFrames):
        list.append(spritesheet.getImage(x+1, row, 64, 64, 1.5))

    return list

def animatePlayer(action, x, y):

    global ANIMATION_COOLDOWN, lastUpdate, frame

    # update animation
    currentTime = pygame.time.get_ticks()

    # checks to see if time last updated has exeeded animation cooldown time
    if currentTime - lastUpdate >= ANIMATION_COOLDOWN:

        # updates frame and sets new last updated time to current time
        frame = frame + 1
        lastUpdate = currentTime

        # ensures the frames loops back to the first frame if it reaches the end
        if frame >= len(action):
            frame = 0

    # show frame image
    config.SCREEN.blit(action[frame], (x,y))
                       

# creates a list of sprite animation frames
animationList = []
animationSteps = 9

def createActionAnimationList(spritesheet):

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

createActionAnimationList(maleMCSpriteSheet)
createActionAnimationList(femaleMCSpriteSheet)

def main():
    running = True
    flag = False

    global lastUpdate, frame

    while running:
        
        # displays the tiles 
        for row in range(len(tileMap)):
            for col in range(len(tileMap[row])):
                tile = tileMap[row][col]
                config.SCREEN.blit(tile, (col*72, row*72))

        # animates player moving left
        animatePlayer(
        

        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # sets a flag to true indicating character has moved
                flag = True
                
            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        pygame.display.update()
                