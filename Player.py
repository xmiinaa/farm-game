import pygame
from spritesheet import SpriteSheet
from config import *

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

    def getPosition(self):
        return self.rect.x, self.rect.y
    
    # moves the position of the entity in the direction it is facing
    def move(self):

        #if 0 <= self.rect.x < len(tilemap[0]) and 0 <= self.rect.y < len(tilemap):
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

    def __init__(self, x, y, spritesheet, name):
        super().__init__(x, y, spritesheet)

        # the players name is the username made by the user
        self.name = name

        # creates animation list using methods in spritesheet and storing as attrbutes in player
        self.idleList = self.spritesheet.createIdleList()
        self.walkList, self.tillWaterList, self.plantList = self.spritesheet.createAnimationList()

        # player is not moving at first
        self.moving = False
    
    def isMoving(self):
        return self.moving
    
    def setMoving(self, new):
        self.moving = new
    
    def whichDirection(self):
        return self.direction
    
    def changeDirection(self, direction):
        self.direction = direction

    # displays character image in direction it is facing
    def drawIdle(self):
        SCREEN.blit(self.idleList[self.direction], (self.rect.x, self.rect.y))

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
    

class Player(Character):
        
    def __init__(self, x, y, spritesheet, name):
        super().__init__(x, y, spritesheet, name)

        self.stamina = 100
        self.inventory = [[] for _ in range(20)]
        self.item = "hoe"
        self.money = 0

        # stores what action the player is currently doing
        self.action = "idle"
        self.active = False

        # creates a rectangle of the entity.
        self.rect = pygame.Rect((x, y), (72, 72))
        
        # (lower x, lower y, upper x, upper y) boundaries
        self.moveBox = [130, 130, 820, 470]
    
    def changeAction(self, action):
        self.action = action
    
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

    # moves the position of the entity in the direction it is facing
    def move(self):

        if self.direction == 0: # facing up

            # checks if the co-ordinate is at the box border
            if self.rect.y <= self.moveBox[1]:

                # checks if the player is at the top edge of the screen
                if self.mapPos[1] >= 360:
                    self.rect.y = max(0, self.rect.y-self.vel) # move character up
                else:
                    self.mapPos[1] += self.vel # move screen up
            else:
                self.rect.y = max(0, self.rect.y-self.vel) # move character up

        if self.direction == 1: # facing left

            # checks if the co-ordinate is at the box border
            if self.rect.x <= self.moveBox[0]:

                # checks if the player is at the left edge of the screen
                if self.mapPos[0] >= 180:
                    self.rect.x = max(0, self.rect.x-self.vel) # move character left
                else:
                    self.mapPos[0] += self.vel # move screen left
            else:
                self.rect.x = max(0, self.rect.x-self.vel) # move character left

        if self.direction == 2: # facing down

            # checks if the co-ordinate is at the box border
            if self.rect.y >= self.moveBox[3]:

                # checks if the player is at the bottom edge of the screen
                if self.mapPos[1] <= -360:
                    self.rect.y = min(HEIGHT-110, self.rect.y+self.vel) # move character down
                else:
                    self.mapPos[1] -= self.vel # move screen down
            else:
                self.rect.y = min(HEIGHT-110, self.rect.y+self.vel) # move character down

        if self.direction == 3: # facing right

            # checks if the co-ordinate is at the box border
            if self.rect.x >= self.moveBox[2]:
                # checks if the player is at the right edge of the screen
                if self.mapPos[0] <= -540:
                    self.rect.x = min(WIDTH-90, self.rect.x+self.vel) # move character right
                
                else:
                    self.mapPos[0] -= self.vel # move screen right
            else:
                self.rect.x = min(WIDTH-90, self.rect.x+self.vel) # move character right

    # animates the player tilling or watering
    def animateTillWater(self):
        
        if self.action == "tillWater" and not self.animationFinished:

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

