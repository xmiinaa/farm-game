import pygame, config

"""
tileMap = [["TL", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TE", "TL"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["LE", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "GM", "RE"]
           ["BL", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BE", "BL"]]
"""
def main():
    running = True
    while running:
        config.SCREEN.fill(config.WHITE)

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
                