# imports and initialise the pygame library

import pygame
pygame.init()

# dimensions of screen
WIDTH = 1080
HEIGHT = 720

# colours
BOX_OUTLINE = (91,164,211)
BOX_FILL = (211, 245, 253)
FONT_COLOUR = (2, 100, 106)

# text font
OCR = pygame.font.Font('Resources\OCR.ttf', 48)

# set up window
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('THE Farm Game')

MENU_BG = pygame.transform.scale(pygame.image.load('Resources\Images\menu-background.png'), (WIDTH, HEIGHT))

class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.colourFill = BOX_FILL
        self.colourBorder = BOX_OUTLINE
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 3)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 3)

class TextBox(Box):
    def __init__(self, x, y,  width, height, content):
       super().__init__(x, y, width, height)
       self.content = content
       self.font = OCR
       self.fontColour = FONT_COLOUR

    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 5)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 5)

        text = OCR.render(self.content, True, self.fontColour)  
        SCREEN.blit(text, (self.x, self.y) )   

# creating objects from classes
titleBox = TextBox(WIDTH / 2 - 225, 100, 450, 70, "THE Farm Game")


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