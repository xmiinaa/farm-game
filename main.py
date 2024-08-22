# imports and initialise the pygame library

import pygame
pygame.init()

# dimensions of screen
WIDTH = 1010
HEIGHT = 675

# colours
BOX_OUTLINE = (91,164,211)
BOX_FILL = (211, 245, 253)

# text font
OCR = pygame.font.SysFont('Ocr', 35)

# set up window
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

MENU_BG = pygame.transform.scale(pygame.image.load('menu-background.png'), (WIDTH, HEIGHT))

class Box:
    def __init__(self, x, y, colour, width, height):
        self.x = x
        self.y = y
        self.colour = colour
        self.width = width
        self.height = height

    def draw(self, x, y, colour, width, height):
        pygame.draw.rect(SCREEN, colour, pygame.Rect(x, y, width, height),  2, 2)


box1 = Box(10, 10, BOX_OUTLINE, 20, 30)

def main():
    SCREEN.blit(MENU_BG, (0, 0))
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        box1.draw(10, 10, BOX_OUTLINE, 20, 30)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()