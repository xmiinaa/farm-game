import pygame
from spritesheet import SpriteSheet
from config import *
import inventory

class Entity():
    def __init__(self, x, y, spritesheet):
        
        # the map surfaces starting co-ordinates on the display
        self.mapPos = [0,0]

        # the speed of the entity
        self.vel = 4

        # the direction the entitiy first is shown. 2 is facing down.
        self.direction = 2

        # the time between each animation frame in ms
        self.animationCooldown = 100

        # the time at which the last update for the animation is made
        self.lastUpdate = pygame.time.get_ticks()

        # the current frame
        self.frame = 0

        # creates an object of the image and stores it as an attribute
        self.spritesheet = SpriteSheet(spritesheet)

        # used to make sure animations play once
        self.animationFinished = True

    def getMapPos(self):
        return self.mapPos
    
    def changeMapPos(self, x, y):
        self.mapPos = [x,y]

    def getPosition(self):
        return self.rect.x, self.rect.y
    
    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    # moves the position of the entity in the direction it is facing
    def move(self):

        if self.direction == 0: # facing up
            self.rect.y = max(0, self.rect.y-self.vel)

        if self.direction == 1: # facing left
            self.rect.x = max(0, self.rect.x-self.vel)

        if self.direction == 2: # facing down
            self.rect.y = min(HEIGHT-100, self.rect.y+self.vel)

        if self.direction == 3: # facing right
            self.rect.x = min(WIDTH-75, self.rect.x+self.vel)

    # sets frame back to 0 so other animations begin from the start
    def resetAnimation(self):
        self.frame = 0
        self.animationFinished = False
    
    # animates the player
    def animate(self,action):

        # update animation
        currentTime = pygame.time.get_ticks()

        # checks to see if time last updated has exeeded animation cooldown time
        if currentTime - lastUpdate >= self.animationCooldown:

            # updates frame and sets new last updated time to current time
            frame = frame + 1 % len(action) # loops back to first frame
            lastUpdate = currentTime

        # show frame image
        SCREEN.blit(action[frame], (self.rect.x,self.rect.y))

class Character(Entity):

    def __init__(self, x, y, spritesheet, name, dialogueRoot):
        super().__init__(x, y, spritesheet)

        # the players name is the username made by the user
        self.name = name

        # creates animation list using methods in spritesheet and storing as attrbutes in player
        self.idleList = self.spritesheet.createIdleList()
        self.walkList, self.tillWaterList, self.plantList = self.spritesheet.createAnimationList()

        # creates a rectangle of the entity.
        self.rect = pygame.Rect((x, y), (72, 72))

        # player is not moving at first
        self.moving = False

        # (lower x, lower y, upper x, upper y) boundaries
        self.moveBox = [130, 130, 820, 470]

        self.dialogueRoot = dialogueRoot
    
    def isMoving(self):
        return self.moving
    
    def setMoving(self, new):
        self.moving = new
    
    def whichDirection(self):
        return self.direction
    
    def changeDirection(self, direction):
        self.direction = direction

    def getName(self):
        return self.name
    
    def getDialogueRoot(self):
        return self.dialogueRoot

    # displays character image in direction it is facing
    def drawIdle(self):
        
        from town import townMap

        x, y = self.getCoordinates()
        townMap.blit(self.idleList[self.direction], (x, y))

    # animates character moving in direction it is facing 
    def animateWalk(self):

        from town import townMap

        # update animation
        currentTime = pygame.time.get_ticks()

        # checks to see if time last updated has exeeded animation cooldown time
        if currentTime - self.lastUpdate >= self.animationCooldown:

            # updates frame and sets new last updated time to current time
            self.frame = self.frame + 1  # loops back to first frame
            self.lastUpdate = currentTime

            # ensures the frames loops back to the first frame if it reaches the end
            if self.frame >= len(self.walkList[self.direction]):
                self.frame = 0

        # show frame image
        townMap.blit(self.walkList[self.direction][self.frame], (self.rect.x, self.rect.y ))
    
    def getCoordinates(self):

        # gets the position of the player in relation to farmMap screen
        worldX = self.rect.x - self.mapPos[0]
        worldY = self.rect.y - self.mapPos[1]

        return (worldX, worldY)
    
    def nearCharacter(self, x, y):
        characterX, characterY = self.getCoordinates()
        if characterX - 60 < x < characterX + 90 and characterY - 60 < y < characterY + 90:
            return True
        else:
            return False

class Player(Character):
        
    def __init__(self, x, y, spritesheet, name, dialogueRoot=None):
        super().__init__(x, y, spritesheet, name, dialogueRoot)

        self.stamina = 100
         
        # creates an object as the inventory
        self.inventory = inventory.Inventory()
        self.money = 1378

        # stores what action the player is currently doing
        self.action = "idle"
        self.active = False

        self.location = "farm"

        self.flag = False

        self.feetrect = pygame.Rect((x,y+52), (72, 20))
    
    def changeAction(self, action):
        self.action = action

    # displays character image in direction it is facing
    def drawIdle(self):
        SCREEN.blit(self.idleList[self.direction], (self.rect.x, self.rect.y))
    
    def onFlag(self):
        self.flag = True
    
    def offFlag(self):
        self.flag = False

    def getFlag(self):
        return self.flag
    
    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        self.location = newLocation
    
    def getAction(self):
        return self.action
    
    def isActive(self):
        return self.active
    
    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False
    
    def getItem(self):
        return self.item
    
    def changeItem(self, item):
        self.item = item

    def changeSpeed(self, speed):
        self.vel= speed

    def getMoney(self):
        return self.money
    
    def reduceMoney(self, value):
        self.money -= value
    
    def checkToMove(self, direction):
        canMove = True
        position = self.getCoordinates()

        if self.location == "Farm":

            if direction == 0: # facing up
                if (200 < position[0] < 510 and position[1] == 160) or ((190 < position[0] < 300 or 390 < position[0] < 510) and position[1] == 360) :
                    canMove = False
            
            if direction == 1: # facing left
                if (position[0] == 220 or position[0] == 520) and -40 < position[1] < 350:
                    canMove = False
            
            if direction == 2: # facing down
                if (175 < position[0] < 510 and position[1] == -40) or ((190 < position[0] < 300 or 390 < position[0] < 510) and 320 < position[1] < 330):
                    canMove = False
            
            if direction == 3: # facing right
                if (170 < position[0] < 180 or 470 < position[0] < 480) and -40 < position[1] < 350:
                    canMove = False

        return canMove

    # checks if the user is near their bed
    def nearBed(self):
        position = self.getCoordinates()
        if self.location == "Farm" and 210 < position[0] < 320 and 140 < position[1] < 210:
                return True
        else:
            return False

    # moves the position of the entity in the direction it is facing
    def move(self):

        if self.direction == 0: # facing up

            if self.checkToMove(self.direction) == True:

                # checks if the co-ordinate is at the box border
                if self.rect.y <= self.moveBox[1]:

                    # checks if the player is at the top edge of the screen
                    if self.mapPos[1] >= 360:
    
                        self.rect.y = max(0, self.rect.y-self.vel) # move character up
                        self.feetrect.y = self.rect.y

                    else:
                        self.mapPos[1] += self.vel # move screen up
                else:
                    self.rect.y = max(0, self.rect.y-self.vel) # move character up
                    self.feetrect.y = self.rect.y


        if self.direction == 1: # facing left

            if self.checkToMove(self.direction) == True:

                # checks if the co-ordinate is at the box border
                if self.rect.x <= self.moveBox[0]:

                    # checks if the player is at the left edge of the screen
                    if self.mapPos[0] >= 180:
                        self.rect.x = max(0, self.rect.x-self.vel) # move character left
                        self.feetrect.x = self.rect.x

                    else:
                        self.mapPos[0] += self.vel # move screen left
                else:
                    self.rect.x = max(0, self.rect.x-self.vel) # move character left
                    self.feetrect.x = self.rect.x

        if self.direction == 2: # facing down

            if self.checkToMove(self.direction) == True:

                # checks if the co-ordinate is at the box border
                if self.rect.y >= self.moveBox[3]:

                    # checks if the player is at the bottom edge of the screen
                    if self.mapPos[1] <= -285:
                        self.rect.y = min(HEIGHT-110, self.rect.y+self.vel) # move character down
                        #self.feetrect.y = self.rect.y

                    else:
                        self.mapPos[1] -= self.vel # move screen down
                else:
                    self.rect.y = min(HEIGHT-110, self.rect.y+self.vel) # move character down
                    #self.feetrect.y = self.rect.y


        if self.direction == 3: # facing right

            if self.checkToMove(self.direction) == True:

                # checks if the co-ordinate is at the box border
                if self.rect.x >= self.moveBox[2]:
                    
                    # checks if the player is at the right edge of the screen
                    if self.mapPos[0] <= -540:
                        self.rect.x = min(WIDTH-90, self.rect.x+self.vel) # move character right
                        self.feetrect.x = self.rect.x
                    
                    else:
                        self.mapPos[0] -= self.vel # move screen right
                else:
                    self.rect.x = min(WIDTH-90, self.rect.x+self.vel) # move character right
                    self.feetrect.x = self.rect.x

    # animates character moving in direction it is facing 
    def animateWalk(self):

        # update animation
        currentTime = pygame.time.get_ticks()

        # checks to see if time last updated has exeeded animation cooldown time
        if currentTime - self.lastUpdate >= self.animationCooldown:

            # updates frame and sets new last updated time to current time
            self.frame = self.frame + 1  # loops back to first frame
            self.lastUpdate = currentTime

            # ensures the frames loops back to the first frame if it reaches the end
            if self.frame >= len(self.walkList[self.direction]):
                self.frame = 0

        # show frame image
        SCREEN.blit(self.walkList[self.direction][self.frame], (self.rect.x, self.rect.y ))

    # animates the player tilling or watering
    def animateTillWater(self):
        
        if (self.action == "till" or self.action == "water" or self.action == "untill") and not self.animationFinished:

            # update animation
            currentTime = pygame.time.get_ticks()

            # checks to see if time last updated has exeeded animation cooldown time
            if currentTime - self.lastUpdate >= self.animationCooldown:

                # updates frame and sets new last updated time to current time
                self.frame += 1 
                self.lastUpdate = currentTime

                # handles the ending of the animation to stop at the last frame
                if self.frame >= len(self.tillWaterList[self.direction]):

                    self.frame = len(self.tillWaterList[self.direction]) -1 # stays on last frame

                    self.animationFinished = True # stops further animation updates
                    
                    self.deactivate()
                    self.action = "idle" # resets player to idle state

            # show frame image
            SCREEN.blit(self.tillWaterList[self.direction][self.frame], (self.rect.x,self.rect.y))
    
    # animates the player tilling or watering
    def animatePlanting(self):
        
        if self.action == "planting" and not self.animationFinished:

            # update animation
            currentTime = pygame.time.get_ticks()

            # checks to see if time last updated has exeeded animation cooldown time
            if currentTime - self.lastUpdate >= self.animationCooldown:

                # updates frame and sets new last updated time to current time
                self.frame += 1 
                self.lastUpdate = currentTime

                # handles the ending of the animation to stop at the last frame
                if self.frame >= len(self.plantList[self.direction]):

                    self.frame = len(self.plantList[self.direction]) -1 # stays on last frame

                    self.animationFinished = True # stops further animation updates
                    
                    self.deactivate()
                    self.action = "idle" # resets player to idle state

            # show frame image
            SCREEN.blit(self.plantList[self.direction][self.frame], (self.rect.x,self.rect.y))

    # gets tile position of player
    def getTilePosition(self):

        # gets the position of the player in relation to farmMap screen
        worldX = self.rect.x - self.mapPos[0]
        worldY = self.rect.y - self.mapPos[1]

        # calculates the correlating tile position in tileMap
        tileX = worldX // TILE_SIZE
        tileY = worldY // TILE_SIZE

        return tileX+3, tileY+6

    # checks to see if the player's mouse is within range of the player
    def mouseOnPlayer(self, mousePos):
        if self.rect.x < mousePos[0] < self.rect.x + 100 and self.rect.y < mousePos[1] < self.rect.y + 100:
            return True
        else:
            return False

    # returns the player's inventory array
    def getInventory(self):
        return self.inventory

class dialogueNode():
    def __init__(self, text):
        self.text = text # the text displayed to the user
        self.responses = {} # key: response option, value: next node

    # adds a response option to the dialogue presented to the user
    def addResponse(self, option, responseText, nextNode):
        self.responses[option] = (responseText, nextNode)

annabelleRoot = dialogueNode("Hii, is there anything I can help with?")
annabelleTalk = dialogueNode("Im Annabelle, and I have 8 cats even though im deathly allergic.")
annabelleBuy = dialogueNode("Oh you'd like to buy from me? Of course! What would you like to buy?")
annabelleSell = dialogueNode("You want to sell something? Sure, what do you have?")
annabelleBye = dialogueNode("It was nice chatting to you! Bye!!")
annabelleAmountBuy = dialogueNode("How many do you want to buy?")
#annabelleBuySuccess = 
annabelleAmountSell = dialogueNode("How many do you want to sell?")

annabelleRoot.addResponse(1, "Who are you?", annabelleTalk)
annabelleRoot.addResponse(2, "Buy", annabelleBuy)
annabelleRoot.addResponse(3, "Sell", annabelleSell)
annabelleRoot.addResponse(4, "Exit", annabelleBye)

annabelleTalk.addResponse(1, "Back to main options", annabelleRoot)

annabelleBuy.addResponse(1, "Potato seeds", annabelleAmountBuy)
annabelleBuy.addResponse(2, "Onion seeds", annabelleAmountBuy)
annabelleBuy.addResponse(3, "Change my mind", annabelleRoot)

annabelleSell.addResponse(1, "Potato seeds", annabelleAmountBuy)
annabelleSell.addResponse(2, "Onion seeds", annabelleAmountBuy)
annabelleSell.addResponse(3, "Change my mind", annabelleRoot)

annabelleAmountBuy.addResponse(1, "", annabelleRoot)
annabelleAmountBuy.addResponse(2, "Change my mind", annabelleRoot)

annabelleAmountSell.addResponse(1, "", annabelleRoot)
annabelleAmountSell.addResponse(2, "Change my mind", annabelleRoot)

annabelleBye.addResponse(1, "Bye!", None)

wesleyRoot = dialogueNode("Hello, did you need something?")
wesleyTalk = dialogueNode("I am Wesley, and I chop wood in my free time.")
wesleyBuy = dialogueNode("You want to buy something? What do you wanna buy?")
wesleySell = dialogueNode("Sell something? To me? What are you selling?")
wesleyBye = dialogueNode("Great convo, bye!")
wesleyAmountBuy = dialogueNode("How many do you want to buy?")
wesleyAmountSell = dialogueNode("How many do you want to sell?")

wesleyRoot.addResponse(1, "Who are you?", wesleyTalk)
wesleyRoot.addResponse(2, "Buy", wesleyBuy)
wesleyRoot.addResponse(3, "Sell", wesleySell)
wesleyRoot.addResponse(4, "Exit", wesleyBye)

wesleyTalk.addResponse(1, "Back to main options", wesleyRoot)

wesleyBuy.addResponse(1, "Potato seeds", wesleyAmountBuy)
wesleyBuy.addResponse(2, "Onion seeds", wesleyAmountBuy)
wesleyBuy.addResponse(3, "Change my mind", wesleyRoot)

wesleySell.addResponse(1, "Potato", wesleyAmountBuy)
wesleySell.addResponse(2, "Onion", wesleyAmountBuy)
wesleySell.addResponse(3, "Change my mind", wesleyRoot)

wesleyAmountBuy.addResponse(1, "", wesleyRoot)
wesleyAmountBuy.addResponse(2, "Change my mind", wesleyRoot)

wesleyAmountSell.addResponse(1, "", wesleyRoot)
wesleyAmountSell.addResponse(2, "Change my mind", wesleyRoot)

wesleyBye.addResponse(1, "Bye!", None)

shaylaRoot = dialogueNode("Hey girly pop! How are you?")
shaylaTalk = dialogueNode("I'm shayla, and I built my own home with galvanised steel and eco-friendly wood!")
shaylaBuy = dialogueNode("Oh you want to buy from me? What do you want to buy?")
shaylaSell = dialogueNode("You want to sell something? Okay girl, what do you have?")
shaylaBye = dialogueNode("Bye Bye!")
shaylaAmountBuy = dialogueNode("How many do you want to buy?")
shaylaAmountSell = dialogueNode("How many do you want to sell?")

shaylaRoot.addResponse(1, "Who are you?", shaylaTalk)
shaylaRoot.addResponse(2, "Buy", shaylaBuy)
shaylaRoot.addResponse(3, "Sell", shaylaSell)
shaylaRoot.addResponse(4, "Exit", shaylaBye)

shaylaTalk.addResponse(1, "Back to main options", shaylaRoot)

shaylaBuy.addResponse(1, "Potato seeds", shaylaAmountBuy)
shaylaBuy.addResponse(2, "Onion seeds", shaylaAmountBuy)
shaylaBuy.addResponse(3, "Change my mind", shaylaRoot)

shaylaSell.addResponse(1, "Potato", shaylaAmountBuy)
shaylaSell.addResponse(2, "Onion", shaylaAmountBuy)
shaylaSell.addResponse(3, "Change my mind", shaylaRoot)

shaylaAmountBuy.addResponse(1, "", shaylaRoot)
shaylaAmountBuy.addResponse(2, "Change my mind", shaylaRoot)

shaylaAmountSell.addResponse(1, "", shaylaRoot)
shaylaAmountSell.addResponse(2, "Change my mind", shaylaRoot)

shaylaBye.addResponse(1, "Bye!", None)

andreRoot = dialogueNode("Hmmm?")
andreTalk = dialogueNode("If you must know, I'm Andre and i'm banned from 5 countries, including this one.")
andreBuy = dialogueNode("Fine. What do you want to buy.")
andreSell = dialogueNode("Oh? You want to get rid of something? What item?")
andreBye = dialogueNode("Ok, bye.")
andreAmountBuy = dialogueNode("How many do you want to buy?")
andreAmountSell = dialogueNode("How many do you want to sell?")

andreRoot.addResponse(1, "Who are you?", andreTalk)
andreRoot.addResponse(2, "Buy", andreBuy)
andreRoot.addResponse(3, "Sell", andreSell)
andreRoot.addResponse(4, "Exit", andreBye)

andreTalk.addResponse(1, "Back to main options", andreRoot)

andreBuy.addResponse(1, "Potato seeds", andreAmountBuy)
andreBuy.addResponse(2, "Onion seeds", andreAmountBuy)
andreBuy.addResponse(3, "Change my mind", andreRoot)

andreSell.addResponse(1, "Potato", andreAmountBuy)
andreSell.addResponse(2, "Onion", andreAmountBuy)
andreSell.addResponse(3, "Change my mind", andreRoot)

andreAmountBuy.addResponse(1, "", andreRoot)
andreAmountBuy.addResponse(2, "Change my mind", andreRoot)

andreAmountSell.addResponse(1, "", andreRoot)
andreAmountSell.addResponse(2, "Change my mind", andreRoot)

andreBye.addResponse(1, "Bye!", None)

joanRoot = dialogueNode("Salut mon ami, was there something you wanted to talk to me about?")
joanTalk = dialogueNode("Im joan, and I am, to some, considered a saint in France")
joanBuy = dialogueNode("I see, you want to purchase something. What do you want to buy?")
joanSell = dialogueNode("You want to sell? Sell what?")
joanBye = dialogueNode("Au revoir! I'll see you around")
joanAmountBuy = dialogueNode("How many do you want to buy?")
joanAmountSell = dialogueNode("How many do you want to sell?")

joanRoot.addResponse(1, "Who are you?", joanTalk)
joanRoot.addResponse(2, "Buy", joanBuy)
joanRoot.addResponse(3, "Sell", joanSell)
joanRoot.addResponse(4, "Exit", joanBye)

joanTalk.addResponse(1, "Back to main options", joanRoot)

joanBuy.addResponse(1, "Potato seeds", joanAmountBuy)
joanBuy.addResponse(2, "Onion seeds", joanAmountBuy)
joanBuy.addResponse(3, "Change my mind", joanRoot)

joanSell.addResponse(1, "Potato", joanAmountBuy)
joanSell.addResponse(2, "Onion", joanAmountBuy)
joanSell.addResponse(3, "Change my mind", joanRoot)

joanAmountBuy.addResponse(1, "", joanRoot)
joanAmountBuy.addResponse(2, "Change my mind", joanRoot)

joanAmountSell.addResponse(1, "", joanRoot)
joanAmountSell.addResponse(2, "Change my mind", joanRoot)

joanBye.addResponse(1, "Bye!", None)

# dictionary to pair npc with dialogue tree
#NPC_TO_DIALOGUE = {"Annabelle": annabelleRoot, "Shayla": shaylaRoot, "Wesley": wesleyRoot, "Andre": andreRoot, "Joan": joanRoot}

annabelle = Character(400, 335, annabelleSpriteSheet, "Annabelle", annabelleRoot)
wesley = Character(1360, 410, wesleySpriteSheet, "Wesley", wesleyRoot)
andre = Character(320, 980, andreSpriteSheet, "Andre", andreRoot)
joan = Character(1450, 1080, joanSpriteSheet, "Joan", joanRoot)
shayla = Character(810, 780, shaylaSpriteSheet, "Shayla", shaylaRoot)