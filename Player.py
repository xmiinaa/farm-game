import pygame, config, game
    
class Entity():
    def __init__(self, x, y, spritesheet, image):
        self.x = x
        self.y = y

        self.spritesheet = spritesheet

        self.image = image
    
    def getPosition(self):
        return self.x, self.y
    
    def changePosition(self, x, y):
        self.x = x
        self.y =y

class Character(Entity):

    def __init__(self, x, y, spritesheet, image, name):
        super().__init__(x, y, spritesheet, image)

        self.name = name
    
        self.vel = 5

        self.moving = False
        self.direction = "Right"
    
    def isMoving(self):
        return self.moving
    
    def setMoving(self, new):
        self.moving = new
    
    def whichDirection(self):
        return self.direction
    
    def changeDirection(self, direction):
        self.direction = direction

class Player(Character):
        
    def __init__(self, x, y, spritesheet, image, name):
        super().__init__(x, y,spritesheet, image, name)

        self.stamina = 100
        self.inventory = [[] for _ in range(20)]
        self.item = ""
        self.money = 0

        self.moving = False
        self.direction = 2
