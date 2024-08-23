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
    def __init__(self, x, y, colourFill, colourBorder, width, height):
        self.x = x
        self.y = y
        self.colourFill = colourFill
        self.colourBorder = colourBorder
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 3)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 3)


titleBox = Box(10, 10, BOX_FILL, BOX_OUTLINE, 20, 30)


def mainmenu():
    SCREEN.blit(MENU_BG, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # running = False
            pygame.quit()
        

    titleBox.draw()

    pygame.display.flip()




def main():

    running = True

    while running:
        mainmenu()


if __name__ == "__main__":
    main()