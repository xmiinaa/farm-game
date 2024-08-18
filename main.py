# imports and initialise the pygame library

import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600

# set up window
screen = pygame.display.set_mode([WIDTH,HEIGHT])


def main():
   
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()