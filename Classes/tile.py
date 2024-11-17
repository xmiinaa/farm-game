import pygame
from config import *

class Tile():
    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

def initialiseTiles():

    tileMap = [
        "AEEEEEEEEEEEEEEEEEEB",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "F------------------G",
        "CHHHHHHHHHHHHHHHHHHD",

    ]
    
    for row in tileMap:
        for tile in row:
            if tile == "A":
                img = TL_TILE
            if tile == "A":

                
                SCREEN.blit(img, (tile*72, row*72))
    
    for i in range(20):
        for j in range(20):

            if i == 0 and j == 0:
                tile = Tile(TR_TILE, i*20, j*20)
            elif i == 0 and j == 19:
                tile = Tile(GM_TILE, i*20, j*20)
            elif i == 19 and j == 0:
                tile = Tile(GM_TILE, i*20, j*20)
            elif i == 19 and j == 19:
                tile = Tile(BR_TILE, i*20, j*20)

            elif i == 0:
                tile = Tile(GM_TILE, i*20, j*20)
            elif i == 19:
                tile = Tile(GM_TILE, i*20, j*20)
            elif j == 0:
                tile = Tile(GM_TILE, i*20, j*20)
            elif j == 19:
                tile = Tile(GM_TILE, i*20, j*20)
            

            tileMap[i][j] = tile

        