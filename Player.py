import pygame, config

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


class Player():

    def __init__(self, image, x, y):

        self.x = x
        self.y = y

        self.vel = 5

        self.left = False
        self.right = False

        self.up = False
        self.Down = False

        self.action = "idle"

        self.image = image
        self.rect = self.image.get_rect(center = (self.x, self.y))


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
