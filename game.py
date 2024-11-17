import pygame
from config import *
#from Classes import tile
import sys
from spritesheet import SpriteSheet
import Player

tileMap = [
    [TL_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TE_TILE, TR_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [LE_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, GM_TILE, RE_TILE],
    [BL_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BE_TILE, BR_TILE]
    ]

MAP_WIDTH, MAP_HEIGHT = 1440, 1440#
TILE_SIZE = 72
VIEW_WIDTH, VIEW_HEIGHT = 15, 10

class Tile():
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

tilemap = [
    ["TL", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TR"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE" ],
    ["BL", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BR"] ]

for row in range(len(tilemap)):
    for col in range(len(tilemap[row])):

        if col == "TL":
            tile = Tile(TL_TILE, col*72, row*72)
        elif col == "TR":
            tile = Tile(TR_TILE, col*72, row*72)
        elif col == "BL":
            tile = Tile(BL_TILE, col*72, row*72)
        elif col == "BR":
            tile = Tile(BR_TILE, col*72, row*72)

        elif col == "TE":
            tile = Tile(TE_TILE, col*72, row*72)
        elif col == "LE":
            tile = Tile(LE_TILE, col*72, row*72)
        elif col == "RE":
            tile = Tile(RE_TILE, col*72, row*72)
        elif col == "BE":
            tile = Tile(BE_TILE, col*72, row*72)

        else:
            tile = Tile(GM_TILE, col*72, row*72)
        
        tilemap[row][col] = tile

print(tilemap)

# this would not be set in real game, but rather obtained from database or previous screen
chosenCharacter = "female"

def main():
    running = True

    global chosenCharacter

    # creates player object depending on the variable, chosenCharacter
    if chosenCharacter == "male":
        player = Player.Player(300, 500, maleMCSpriteSheet, "Bob")

    else: # creates female player
        player = Player.Player(300, 500, femaleMCSpriteSheet, "Yue")


    while running:
        
        # displays the tiles 
        for row in range(len(tileMap)):
            for col in range(len(tileMap[row])):
                tile = tileMap[row][col]
                SCREEN.blit(tile, (col*72, row*72))

        # gets player direction and co-ordinates
        x, y = player.getPosition()

        # checks if the player is moving, and displays it appropiately if they are
        if player.isMoving():

            player.animateWalk()
            player.move()

        # checks to see if the player is currently doing an action
        elif player.getAction() != "idle":

            if player.isActive():
    
                player.animateTillWater()

        # displays the player in its idle state
        else:
            player.drawIdle()
    
        
        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
                    player.setMoving(True)
    
                if keys[pygame.K_a]:
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

                player.resetAnimation()
                player.activate()

                # changes the attribute as appropiate
                player.changeAction("tillWater")
            
            else:

                player.changeAction("idle")
                
            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        pygame.display.update()
                