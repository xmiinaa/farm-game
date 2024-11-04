import pygame, config, game
    
class Entity():
    def __init__(self, x, y, spritesheet, image):
        self.x = x
        self.y = y

        self.animationCooldown = 100
        self.lastUpdate = pygame.time.get_ticks()
        self.frame = 0

        self.spritesheet = spritesheet

        self.image = image
    
    def getPosition(self):
        return self.x, self.y
    
    def changePosition(self, x, y):
        self.x = x
        self.y = y
    
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

    def __init__(self, x, y, spritesheet, idleList, name, walkList, tillWaterList, plantList):
        super().__init__(x, y, spritesheet, idleList)

        self.name = name
    
        self.vel = 5

        self.idleList = idleList
        self.walkList = walkList
        self.tillWaterList = tillWaterList
        self.plantList = plantList

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
        
    def __init__(self, x, y, spritesheet, idleList, name, walkList, tillWaterList, plantList):
        super().__init__(x, y, spritesheet, idleList, name, walkList, tillWaterList, plantList)

        self.stamina = 100
        self.inventory = [[] for _ in range(20)]
        self.item = ""
        self.money = 0

