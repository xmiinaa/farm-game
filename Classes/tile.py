import pygame, config

class tile():
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        config.SCREEN.blit(self.image, (self.x, self.y))
