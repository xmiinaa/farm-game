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


"""
class allSprites(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(group)
        self.allSprites = pygame.sprite.Group()
    
    def run(self):
        self.allSprites.draw(config.SCREEN)
        self.allSprites.update()
    

class Player(allSprites):

    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((32, 64))
        self.image.fill(config.WHITE)
        self.rect = self.image.get_rect(center = pos)

    def input(Self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            print("Up")
        elif keys[pygame.K_DOWN]:
            print("Down")
        
        if keys[pygame.K_RIGHT]:
            print("Right")
        elif keys[pygame.K_LEFT]:
            print("Left")
        """