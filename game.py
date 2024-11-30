import pygame
from config import *
import sys
import Player
import tile

# this would not be set in real game, but rather obtained from database or previous screen
chosenCharacter = "male"

def draw():
    pygame.draw.rect(SCREEN, BLACK, pygame.Rect(178, 618, 724, 76), 2)
    x = 72
    y = 620
    for i in range(1,11):
        SCREEN.blit(SLOT, ((x*i)+108,y))
    SCREEN.blit(CHOSEN_SLOT, (252,620))

def main():
    running = True

    global chosenCharacter

    # creates player object depending on the variable, chosenCharacter
    if chosenCharacter == "male":
        player = Player.Player(540, 360, maleMCSpriteSheet, "Bob")

    else: # creates female player
        player = Player.Player(540, 360, femaleMCSpriteSheet, "Yue")

    # gets co-ordinates of camera
    cameraPos = player.getMapPos()

    # creates the farmMap
    farmMap = tile.renderFarmMap()

    keyPressed = ""

    while running:

        # gets player direction
        direction = player.whichDirection()

        # gets co-ordinates of mouse
        mousePos = pygame.mouse.get_pos()

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

                if player.getAction() == "till":
    
                    # tills the farm tile
                    tile.till(player, mousePos, keyPressed)
                
                elif player.getAction() == "water":

                    # waters the farm tile
                    tile.water(player, mousePos, keyPressed)
                
                elif player.getAction() == "planting":

                    player.animatePlanting()

        # displays the player in its idle state
        else:
            player.drawIdle()
        
        draw()

    
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

                if keys[pygame.K_LSHIFT]:
                    player.changeSpeed(6)
                else:
                    player.changeSpeed(4)

                if keys[pygame.K_x]:

                    keyPressed = "x"

                    # ensures the player is not already engaged in another action
                    if player.isActive() == False:

                        player.resetAnimation() # sets animation back to 0
                        player.activate()

                        # gets the item that the player is currently holding
                        item = player.getItem()
                    
                        if item == "hoe":

                            # changes the attribute as appropiate
                            player.changeAction("till")
                        
                        if item == "waterCan":

                            # changes the attribute as appropiate
                            player.changeAction("water")
                        
                        if item == "seed":

                            # changes the attribute as appropiate
                            player.changeAction("planting")


            # checks if player is not pressing down a key
            if event.type == pygame.KEYUP:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                    player.setMoving(False)
    
            # checks if he player has clicked on the mouse
            if pygame.mouse.get_pressed()[0]:

                keyPressed = "mouse"

                if player.mouseOnPlayer(mousePos):

                    # ensures the player is not already engaged in another action
                    if player.isActive() == False:

                        player.resetAnimation() # sets animation back to 0
                        player.activate()

                        # gets the item that the player is currently holding
                        item = player.getItem()
                    
                        if item == "hoe":

                            # changes the attribute as appropiate
                            player.changeAction("till")
                        
                        if item == "waterCan":

                            # changes the attribute as appropiate
                            player.changeAction("water")
                        
                        if item == "seed":

                            # changes the attribute as appropiate
                            player.changeAction("planting")
                    
            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        # maintains framerate of game
        CLOCK.tick(60)
        pygame.display.update()
                