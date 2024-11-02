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
animation_cooldown = 100

frame = 0

# loads the sprite sheet into program 
playerWalkUpSheetImage = pygame.image.load("Resources/Images/player-walking-up.png").convert_alpha()

# creates an object of the sprite sheet
playerWUSheet = Player.SpriteSheet(playerWalkUpSheetImage)

# creates a list to hold the different frames of the sprite 
playerWU = []
for x in range(8):
    playerWU.append(playerWUSheet.getImage(x+1, 64, 64, 1.5))

def main():
    running = True

    global lastUpdate, frame

    while running:
        
        # displays the tiles 

        for row in range(len(tileMap)):
            for col in range(len(tileMap[row])):
                tile = tileMap[row][col]
                config.SCREEN.blit(tile, (col*72, row*72))
        
        # update animation
        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate >= animation_cooldown:
            frame = frame + 1
            lastUpdate = currentTime
            if frame >= len(playerWU):
                frame = 0

        # show frame image
        config.SCREEN.blit(playerWU[frame], (100,500))

        for event in pygame.event.get():

            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        pygame.display.update()
                