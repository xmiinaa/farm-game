import pygame, config, Classes
from Classes import tile
import sys
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

# stores time since last frame has been updated
lastUpdate = pygame.time.get_ticks()

# how long each frame lasts
animationCooldown = 500

frame = 0

def createSpriteFrameList(img, numFrames, row):

    # creates an object of the sprite sheet image
    spritesheet = Player.SpriteSheet(img)

    # creates a list to hold the different frames of the sprite 
    list = []
    for x in range(numFrames):
        list.append(spritesheet.getImage(x+1, row, 64, 64, 1.5))

    return list

def animatePlayer(action, x, y):
    frame = 0

    global animationCooldown, lastUpdate

    # update animation
    currentTime = pygame.time.get_ticks()

    # checks to see if time last updated has exeeded animation cooldown time
    if currentTime - lastUpdate >= animationCooldown:

        # updates frame and sets new last updated time to current time
        frame = frame + 1
        lastUpdate = currentTime

        # ensures the frames loops back to the first frame if it reaches the end
        if frame >= len(action):
            frame = 0

    # show frame image
    config.SCREEN.blit(action[frame], (x,y))

# load player sprite sheet
maleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()

# creates a list of sprite animation frames
playerWalkUp = createSpriteFrameList(maleMCSpriteSheet, 8, 8)
playerWalkLeft = createSpriteFrameList(maleMCSpriteSheet, 8, 9)
playerWalkDown = createSpriteFrameList(maleMCSpriteSheet, 8, 10)
playerWalkRight = createSpriteFrameList(maleMCSpriteSheet, 8, 11)
playerIDK = createSpriteFrameList(maleMCSpriteSheet, 7, 6)

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
        
        # checks to see if user has pressed key down
        if flag:

            # animates player moving left
            animatePlayer(playerWalkLeft, 500, 600)

        """
        # update animation
        currentTime = pygame.time.get_ticks()

        # checks to see if time last updated has exeeded animation cooldown time
        if currentTime - lastUpdate >= animation_cooldown:

            # updates frame and sets new last updated time to current time
            frame = frame + 1
            lastUpdate = currentTime

            # ensures the frames loops back to the first frame if it reaches the end
            if frame >= len(playerWalkUp):
                frame = 0

        # show frame image
        config.SCREEN.blit(playerWalkUp[frame], (100,500))
        config.SCREEN.blit(playerWalkDown[frame], (300,500))
        config.SCREEN.blit(playerWalkLeft[frame], (500,500))
        config.SCREEN.blit(playerWalkRight[frame], (700,500))

        config.SCREEN.blit(playerIDK[frame], (400,200))
"""
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
                