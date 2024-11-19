import pygame
from spritesheet import SpriteSheet
from config import *

class Entity():
    def __init__(self, x, y, spritesheet):
        
        # the map surfaces starting co-ordinates on the display
        self.mapPos = [x,y]

        # (lower x, lower y, upper x, upper y) boundaries
        self.moveBox = [180, 360, 1260, 1080]

        # the speed of the entity
        self.vel = 3

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

    
    def getPosition(self):
        return self.mapPos[0], self.mapPos[1]
    
    # moves the position of the entity in the direction it is facing
    def move(self):

        #if 0 <= self.mapPos[0] < len(tilemap[0]) and 0 <= self.mapPos[1] < len(tilemap):
        if self.direction == 0: # facing up
            self.mapPos[1] = max(0, self.mapPos[1]-self.vel)

        if self.direction == 1: # facing left
            self.mapPos[0] = max(0, self.mapPos[0]-self.vel)

        if self.direction == 2: # facing down
            self.mapPos[1] = min(HEIGHT-100, self.mapPos[1]+self.vel)

        if self.direction == 3: # facing right
            self.mapPos[0] = min(WIDTH-75, self.mapPos[0]+self.vel)

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
        SCREEN.blit(action[frame], (self.mapPos[0],self.mapPos[1]))

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
        SCREEN.blit(self.idleList[self.direction], (self.mapPos[0], self.mapPos[1]))

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
        SCREEN.blit(self.walkList[self.direction][self.frame], (self.mapPos[0],self.mapPos[1]))
    

class Player(Character):
        
    def __init__(self, x, y, spritesheet, name):
        super().__init__(x, y, spritesheet, name)

        self.stamina = 100
        self.inventory = [[] for _ in range(20)]
        self.item = ""
        self.money = 0

        # stores what action the player is currently doing
        self.action = "idle"
        self.active = False
    
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
            SCREEN.blit(self.tillWaterList[self.direction][self.frame], (self.mapPos[0],self.mapPos[1]))