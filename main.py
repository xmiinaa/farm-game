# imports and initialise the pygame library

import pygame
pygame.init()

# dimensions of screen
WIDTH = 1080
HEIGHT = 720

TITLE_WIDTH = 450
TITLE_HEIGHT = 90

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
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)

        text = self.font.render(self.content, True, self.fontColour) 
        textRect = text.get_rect(center = (self.width / 2 + self.x, self.height / 2 + self.y))
        SCREEN.blit(text, textRect )   





def mainmenu_loop():
    SCREEN.blit(MENU_BG, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # running = False
            pygame.quit()
        
    # argument values: (x_pos, y_pos, width, height, font, content)

    titleBox = TextBox(WIDTH / 2 - (TITLE_WIDTH / 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "THE Farm Game")

    newGameBox = TextBox(WIDTH / 2 - 140, 220, 280, 70, OCR_TEXT, "New Game")
    loadGameBox = TextBox(WIDTH / 2 - 140, 320, 280, 70, OCR_TEXT, "Load Game")
    instructionsBox = TextBox(WIDTH / 2 - 140, 420, 280, 70, OCR_TEXT, "How To Play")
    settingsBox = TextBox(WIDTH / 2 - 140, 520, 280, 70, OCR_TEXT, "Settings")

    titleBox.draw()
    newGameBox.draw()
    loadGameBox.draw()
    instructionsBox.draw()
    settingsBox.draw()

    pygame.display.flip()

def newgame1_loop():
    SCREEN.blit(MENU_BG, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # running = False
            pygame.quit()
        
    # argument values: (x_pos, y_pos, width, height, font, content)

    titleBox = TextBox(WIDTH / 2 - (TITLE_WIDTH / 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "New Game")

    backButton = TextBox(30, 30, 90, 70, OCR_TITLE, "<-"  )
    tickButton = TextBox( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

    save1Title = TextBox(220, 250, 280, 80, OCR_TEXT, "Save 1:")
    save2Title = TextBox(220, 370, 280, 80, OCR_TEXT, "Save 2:")
    save3Title = TextBox(220, 490, 280, 80, OCR_TEXT, "Save 3:")

    save1Content = TextBox(560, 250, 280, 80, OCR_TEXT, "no save")
    save2Content = TextBox(560, 370, 280, 80, OCR_TEXT, "no save")
    save3Content = TextBox(560, 490, 280, 80, OCR_TEXT, "no save")

    titleBox.draw()
    backButton.draw()
    tickButton.draw()
    save1Title.draw()
    save2Title.draw()
    save3Title.draw()
    save1Content.draw()
    save2Content.draw()
    save3Content.draw()

    pygame.display.flip()

def main():

    running = True

    while running:
        newgame1_loop()


if __name__ == "__main__":
    main()