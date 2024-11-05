import pygame, config, game
from spritesheet import SpriteSheet

class Entity():
    def __init__(self, x, y, spritesheet):
        self.x = x
        self.y = y

        self.animationCooldown = 100
        self.lastUpdate = pygame.time.get_ticks()
        self.frame = 0

        self.spritesheet = SpriteSheet(spritesheet)

    
    def getPosition(self):
        return self.x, self.y
    
    def changePosition(self, x, y):
        self.x = x
        self.y = y

    def resetAnimation(self):
        self.frame = 0
    
    def animate(self,action):

        # update animation
        currentTime = pygame.time.get_ticks()

        # checks to see if time last updated has exeeded animation cooldown time
        if currentTime - lastUpdate >= self.animationCooldown:

            # updates frame and sets new last updated time to current time
            frame = frame + 1 % len(action) # loops back to first frame
            lastUpdate = currentTime

        # show frame image
        config.SCREEN.blit(action[frame], (self.x,self.y))

class Character(Entity):

    def __init__(self, x, y, spritesheet, name):
        super().__init__(x, y, spritesheet)

        self.name = name
    
        self.vel = 5

        self.idleList = self.spritesheet.createIdleList()
        self.walkList, self.tillWaterList, self.plantList = self.spritesheet.createAnimationList()

        self.moving = False
        self.direction = 2
    
    def isMoving(self):
        return self.moving
    
    def setMoving(self, new):
        self.moving = new
    
    def whichDirection(self):
        return self.direction
    
    def changeDirection(self, direction):
        self.direction = direction

    def drawIdle(self):
        config.SCREEN.blit(self.idleList[self.direction], (self.x, self.y))

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
        config.SCREEN.blit(self.walkList[self.direction][self.frame], (self.x,self.y))
    

class Player(Character):
        
    def __init__(self, x, y, spritesheet, name):
        super().__init__(x, y, spritesheet, name)

        self.stamina = 100
        self.inventory = [[] for _ in range(20)]
        self.item = ""
        self.money = 0

    def animateTillWater(self):

        flag = False

        while not flag:

            # update animation
            currentTime = pygame.time.get_ticks()

            # checks to see if time last updated has exeeded animation cooldown time
            if currentTime - self.lastUpdate >= self.animationCooldown:

                # updates frame and sets new last updated time to current time
                self.frame = self.frame + 1 
                self.lastUpdate = currentTime

                # handles the ending of the animation to stop at the last frame
                if self.frame <= len(self.tillWaterList[self.direction]):
                    flag = True

        # show frame image
        config.SCREEN.blit(self.tillWaterList[self.direction][self.frame], (self.x,self.y))
