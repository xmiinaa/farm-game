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
OCR_TITLE = pygame.font.Font('Resources\OCR.ttf', 48)
OCR_TEXT = pygame.font.Font('Resources\OCR.ttf', 38)

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
    def __init__(self, x, y,  width, height, font, content):
       super().__init__(x, y, width, height)
       self.content = content
       self.font = font
       self.fontColour = FONT_COLOUR

    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 5)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 5)

        text = self.font.render(self.content, True, self.fontColour) 
        textRect = text.get_rect(center = (self.width / 2 + self.x, self.height / 2 + self.y))
        SCREEN.blit(text, textRect )   

# creating objects from classes
titleBox = TextBox(WIDTH / 2 - 225, 100, 450, 80, OCR_TITLE, "THE Farm Game")

newGameBox = TextBox(WIDTH / 2 - 150, 250, 300, 70, OCR_TEXT, "New Game")
loadGameBox = TextBox(WIDTH / 2 - 150, 350, 300, 70, OCR_TEXT, "Load Game")
instructionsBox = TextBox(WIDTH / 2 - 150, 450, 300, 70, OCR_TEXT, "How To Play")
settingsBox = TextBox(WIDTH / 2 - 150, 550, 300, 70, OCR_TEXT, "Settings")


def mainmenu_loop():
    SCREEN.blit(MENU_BG, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # running = False
            pygame.quit()
        

    titleBox.draw()
    newGameBox.draw()
    loadGameBox.draw()
    instructionsBox.draw()
    settingsBox.draw()

    pygame.display.flip()


def main():

    running = True

    while running:
        mainmenu_loop()


if __name__ == "__main__":
    main()