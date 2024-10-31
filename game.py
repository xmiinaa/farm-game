import pygame, config, Classes
from Classes import tile


tileMap = [
    ["TL", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TL"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"],
    ["BL", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BL"]
    ]


def main():
    running = True
    while running:
        
        for row in range(len(tileMap)):
            for column in range(len(tileMap[row])):
                val = str(tileMap[row][column])
                val += "_TILE"
                print(val)
                config.SCREEN.blit(val, (row*72,column*72))
                         
        config.SCREEN.blit(config.TL_TILE, (0,0))
        config.SCREEN.blit(config.BL_TILE ,(0,648))
        config.SCREEN.blit(config.TR_TILE, (1008,0))
        config.SCREEN.blit(config.BR_TILE, (1008,648))

        for event in pygame.event.get():
            if event.type != pygame.QUIT:
                pygame.display.flip()
            else:
                running  = False
                pygame.quit()
                