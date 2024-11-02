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
animationCooldown = 100

frame = 0


def createSpriteFrameList(img, numFrames, row):

    # creates an object of the sprite sheet image
    spritesheet = Player.SpriteSheet(img)

    # creates a list to hold the different frames of the sprite 
    list = []
    for x in range(numFrames):
        list.append(spritesheet.getImage(x+1, row, 64, 64, 1.5))

    return list

# load player sprite sheet
maleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()

maleMC = Player.Player("Bob", maleMCSpriteSheet, 500, 400, maleMCSpriteSheet)

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
        maleMC.animatePlayer(playerWalkLeft, 500, 600)

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
                