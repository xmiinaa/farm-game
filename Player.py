import pygame, config

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