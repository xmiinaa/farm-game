import pygame, config

def main():
    running = True
    while running:
        config.SCREEN.fill(config.WHITE)

        for event in pygame.event.get():
            if event.type != pygame.QUIT:
                pygame.display.flip()
            else:
                running  = False
                pygame.quit()
                