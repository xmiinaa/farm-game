import pygame, config, game

class SpriteSheet():

    # initialises sprite sheet
    def __init__(self, image):
        self.sheet = image

    # gets and returns a specific image frame from spritesheet
    def getImage(self, frame, row, width, height, scale):

        # creates a surface for image to draw on
        image = pygame.Surface((width, height)).convert_alpha()

        # draws on part of spritesheet that has been requested
        image.blit(self.sheet, (0,0), ((frame*width), (row*height), width, height))

        # scales image accordingly
        image = pygame.transform.scale(image, (width * scale, height * scale))

        image.set_colorkey(config.BLACK)

        return image
    
class Entity():
    def __init__(self, x, y, spritesheet, image):
        self.x = x
        self.y = y

        self.image = image
        try:
            self.rect = self.image.get_rect(center = (self.x, self.y))
        except TypeError as e:
            print(e)

        # creates a list of sprite animation frames
        self.playerWalkUp = game.createSpriteFrameList(spritesheet, 8, 8)
        self.playerWalkLeft = game.createSpriteFrameList(spritesheet, 8, 9)
        self.playerWalkDown = game.createSpriteFrameList(spritesheet, 8, 10)
        self.playerWalkRight = game.createSpriteFrameList(spritesheet, 8, 11)
    
    def getPosition(self):
        return self.x, self.y
    
    def changePosition(self, x, y):
        self.x = x
        self.y =y

    def animateEntity(action, x, y):

        if action == "WL":
            # update animation
            currentTime = pygame.time.get_ticks()

            # checks to see if time last updated has exeeded animation cooldown time
            if currentTime - lastUpdate >= config.ANIMATION_COOLDOWN:

                # updates frame and sets new last updated time to current time
                frame = frame + 1
                lastUpdate = currentTime

                # ensures the frames loops back to the first frame if it reaches the end
                if frame >= len(action):
                    frame = 0

            # show frame image
            config.SCREEN.blit(action[frame], (x,y))

class Character(Entity):

    def __init__(self, name, x, y, spritesheet, image):
        super().__init__(x, y, spritesheet, image)

        self.name = name
    
        self.vel = 5

        self.moving = False
        self.direction = "Right"
    
    

class Player(Character):
        
    def __init__(self, name, x, y, spritesheet, image):
        super().__init__(name, spritesheet, x, y, image)
        self.stamina = 100
        self.inventory = [[] for _ in range(20)]
        self.item = ""
        self.money = 0
        self.action = "idle"

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y > self.vel:
            self.y -= self.vel
            self.up = True
            self.down = False

        elif keys[pygame.K_DOWN] and self.y < config.WIDTH - self.vel:
            self.y += self.vel
            self.down = True
            self.up = False

        if keys[pygame.K_RIGHT]:
            self.x -= self.vel
            self.left = True
            self.right = False

        elif keys[pygame.K_LEFT]:
            self.y += self.vel
            self.right = True
            self.left = False
        
        else:
            self.up = False
            self.down = False
            self.left = False
            self.right = False
