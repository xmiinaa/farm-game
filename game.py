import pygame
from config import *
import sys
import Player
import tile
import time

# this would not be set in real game, but rather obtained from the database
chosenCharacter = "female"

def renderTime():

    global elapsedRealTime

    # Get the time elapsed since the last frame in milliseconds
    deltaTime = CLOCK.get_time()
    elapsedRealTime += deltaTime

    # Convert real elapsed time into in-game time
    elapsedGameTime = (elapsedRealTime / 1000) * (24 * 60 * 60 / DAY_DURATION)  # Scale to a 24-hour day
    gameHour = (START_HOUR + int(elapsedGameTime // 3600)) % 24
    gameMinute = int((START_MINUTE + (elapsedGameTime % 3600) // 60) % 60)

    date = START_DATE

    # Format in-game time as hh:mm
    timeString = f"Time: {gameHour:02}:{gameMinute:02}"
    dateString = f"Date: Spring {date}"
    moneyString = "Money: 300"
    weatherString = "Weather: Sunny"

    # Render the time
    timeSurface = OCR_ERROR.render(timeString, True, (255, 255, 255))  # White text
    dateSurface = OCR_ERROR.render(dateString, True, (255, 255, 255))  # White text
    moneySurface = OCR_ERROR.render(moneyString, True, (255, 255, 255))  # White text
    weatherSurface = OCR_ERROR.render(weatherString, True, (255, 255, 255))  # White text

    SCREEN.blit(TOP_SCREEN, (-10, -5))

    SCREEN.blit(timeSurface, (7, 5))
    SCREEN.blit(dateSurface, (267, 5))
    SCREEN.blit(moneySurface, (507, 5))
    SCREEN.blit(weatherSurface, (737, 5))

    pygame.draw.rect(SCREEN, DARK_GREY, pygame.Rect(-10, -5, 1100, 40), 1, 0)

    if gameHour == 6:
        date = (date + 1) % 24
        print(date)
        newDay()

def newDay():
    farmMap = tile.renderFarmMap(True)

def main():
    running = True

    global chosenCharacter

    # creates player object depending on the variable, chosenCharacter
    if chosenCharacter == "male":
        player = Player.Player(540, 360, maleMCSpriteSheet, "Bob")

    elif chosenCharacter == "female": # creates female player
        player = Player.Player(540, 360, femaleMCSpriteSheet, "Yue")

    # gets co-ordinates of camera
    cameraPos = player.getMapPos()

    # creates the farmMap
    farmMap = tile.renderFarmMap()

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
                
                elif player.getAction() == "untill":

                    # untills the farm tile
                    tile.untill(player, mousePos, keyPressed)
                
                elif player.getAction() == "water":

                    # waters the farm tile
                    tile.water(player, mousePos, keyPressed)
                
                elif player.getAction() == "planting":

                    tile.plant(player, mousePos, keyPressed)

        # displays the player in its idle state
        else:
            player.drawIdle()
        
        player.inventory.draw()
        player.inventory.hover(mousePos)

        if slotItem != None and mouseDrag: # checks to see if the player's mouse is holding an item
            player.inventory.displayItem(mousePos, slotItem) # displays item relative to player's mouse

        # displays time
        renderTime()


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
                    
                        if item == "hoe" or item == "scythe" or item == "waterCan" or "seed" in item:

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
                