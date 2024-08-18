# imports and initialise the pygame library

import pygame
pygame.init()

WIDTH = 1010
HEIGHT = 675

# set up window
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

MENU_BG = pygame.transform.scale(pygame.image.load('menu-background.png'), (WIDTH, HEIGHT))

def main():
    SCREEN.blit(MENU_BG, (0, 0))
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()