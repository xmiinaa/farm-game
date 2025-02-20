import pygame
from config import *
import sys
import Player
import tile
import random, town
import game

# this would not be set in real game, but rather obtained from the database
chosenCharacter = "male"
weather = 0

# creates player object depending on the variable, chosenCharacter
if chosenCharacter == "male":
    player = Player.Player(540, 360, maleMCSpriteSheet, "Bob")

elif chosenCharacter == "female": # creates female player
    player = Player.Player(540, 360, femaleMCSpriteSheet, "Yue")

def main(fromTown=False):
    running = True

    global player

    pause = False

    player.setLocation("Farm")

    if fromTown:
        player.changeMapPos(-540, 0)
        player.setPosition(970, 300)

    # gets co-ordinates of camera
    cameraPos = player.getMapPos()

    # creates the farmMap
    farmMap = tile.renderFarmMap(weather)

    # displays time
    game.renderTime(player)

    keyPressed = ""
    mouseDrag = False
    slotItem = None

    while running:

        # gets player direction
        direction = player.whichDirection()

        # gets co-ordinates of mouse
        mousePos = pygame.mouse.get_pos()

        # displays background tiles
        SCREEN.blit(farmMap, (cameraPos[0]-180, cameraPos[1]-360))

        if tile.checkEdgeOfFarm(player) == True:
            town.main(player, True)

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
                    tile.till(player, mousePos, keyPressed, weather)
                
                elif player.getAction() == "untill":

                    # untills the farm tile
                    tile.untill(player, mousePos, keyPressed)
                
                elif player.getAction() == "water":

                    # waters the farm tile
                    tile.water(player, mousePos, keyPressed)
                
                elif player.getAction() == "planting":

                    tile.plant(player, mousePos, keyPressed)

                elif player.getAction() == "harvesting":

                    tile.harvest(player, mousePos, keyPressed)

        # displays the player in its idle state
        else:
            player.drawIdle()
        
        player.inventory.draw()
        player.inventory.hover(mousePos)

        if slotItem != None and mouseDrag: # checks to see if the player's mouse is holding an item
            player.inventory.displayItem(mousePos, slotItem) # displays item relative to player's mouse

        # displays time
        if not pause:
            game.renderTime(player)

        if player.nearBed():
            print("ok")

        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if player.inventory.isInventoryOpen() == False:

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

                        # gets the item that the player is currently holding
                        item = player.inventory.getItem()

                        # ensures the player is not already engaged in another action
                        if player.isActive() == False:

                            player.resetAnimation() # sets animation back to 0
                            player.activate()

                            if item == "hoe":

                                # changes the attribute as appropiate
                                player.changeAction("till")
                            
                            if item == "scythe":

                                # changes the attribute as appropiate
                                player.changeAction("untill")
                            
                            if item == "waterCan":

                                # changes the attribute as appropiate
                                player.changeAction("water")
                            
                            if "seed" in item:

                                player.offFlag()
                                
                                # changes the attribute as appropiate
                                player.changeAction("planting")

                            if item == "None":

                                # changes the attribute as appropiate
                                player.changeAction("harvesting")
                
                if keys[pygame.K_e]:
                    player.inventory.openCloseInventory()

                # checks to see if the user has pressed keys 1 to 0, changing the inventory slot if they have to the corresponding one
                if keys[pygame.K_1]:
                    player.inventory.changeSlot(0)
                if keys[pygame.K_2]:
                    player.inventory.changeSlot(1)
                if keys[pygame.K_3]:
                    player.inventory.changeSlot(2)
                if keys[pygame.K_4]:
                    player.inventory.changeSlot(3)
                if keys[pygame.K_5]:
                    player.inventory.changeSlot(4)
                if keys[pygame.K_6]:
                    player.inventory.changeSlot(5)
                if keys[pygame.K_7]:
                    player.inventory.changeSlot(6)
                if keys[pygame.K_8]:
                    player.inventory.changeSlot(7)
                if keys[pygame.K_9]:
                    player.inventory.changeSlot(8)
                if keys[pygame.K_0]:
                    player.inventory.changeSlot(9)
                        
            # checks if player is not pressing down a key
            if event.type == pygame.KEYUP:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                    player.setMoving(False)

            # checks if he player has clicked on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    keyPressed = "mouse"

                    player.inventory.click(mousePos)

                    mouseDrag = True

                    # checks if inventory is open
                    if player.inventory.isInventoryOpen():
                        slotItem = player.inventory.getDragItem(mousePos) # gets item that player is holding on

                    if player.mouseOnPlayer(mousePos):

                        # gets the item that the player is currently holding
                        item = player.inventory.getItem()
                    
                        if item != "None":

                            # ensures the player is not already engaged in another action
                            if player.isActive() == False:

                                player.resetAnimation() # sets animation back to 0
                                player.activate()

                                if item == "hoe":

                                    # changes the attribute as appropiate
                                    player.changeAction("till")
                                
                                if item == "scythe":

                                    # changes the attribute as appropiate
                                    player.changeAction("untill")
                                
                                if item == "waterCan":

                                    # changes the attribute as appropiate
                                    player.changeAction("water")
                                
                                if "seed" in item:

                                    player.offFlag()

                                    # changes the attribute as appropiate
                                    player.changeAction("planting")
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    mouseDrag = False

                    if player.inventory.isInventoryOpen() and (slotItem != None or slotItem == 0):
                        player.inventory.swapItems(slotItem, mousePos)
                
            if event.type == pygame.MOUSEMOTION:  
                if mouseDrag:
                    if player.inventory.isInventoryOpen():
                            if slotItem != None or slotItem == 0:
                                player.inventory.dragDropItem(mousePos, slotItem)  

            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        # maintains framerate of game
        CLOCK.tick(60)
        pygame.display.update()
                