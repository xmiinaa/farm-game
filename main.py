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
BOX_HOVER_OUTLINE = (255,255,255)
BOX_FILL = (211, 245, 253)
FONT_COLOUR = (2, 100, 106)

# text font
OCR_TITLE = pygame.font.Font('Resources\OCR.ttf', 48)
OCR_TEXT = pygame.font.Font('Resources\OCR.ttf', 38)

# set up window
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('THE Farm Game')

# images 
MENU_BG = pygame.transform.scale(pygame.image.load('Resources\Images\menu-background.png'), (WIDTH, HEIGHT))
FEMALE_MC = pygame.image.load('Resources\Images\girlMC.png')
MALE_MC = pygame.image.load('Resources\Images\maleMC.png')

# music
musicVal = 0
sfxVal = 5

pygame.mixer.music.load('Resources\Music\music1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0) # this cause im gonna get sick of music when testing it 

button1 = pygame.mixer.Sound('Resources\Sound-effects\cbutton1.mp3')
button2 = pygame.mixer.Sound('Resources\Sound-effects\cbutton2.mp3')
button3 = pygame.mixer.Sound('Resources\Sound-effects\cbutton3.mp3')
button4 = pygame.mixer.Sound('Resources\Sound-effects\cbutton4.mp3')

for sounds in [button1, button2, button3, button4]:
    sounds.set_volume(0.5)

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
       self.font = font
       self.content = content
       self.text = font.render(self.content, True, FONT_COLOUR)
       self.fontColour = FONT_COLOUR
       self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))

    # displays text box onto screen
    def draw(self): 
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)

        SCREEN.blit(self.text, self.textRect )   

    # getter method to access text inside text box
    def getText(self):
        return self.content

    # setter method to change text in text box
    def changeText(self, newText):
        self.content = newText

class Button(TextBox):
    def __init__(self, x, y,  width, height, font, text):
        super().__init__(x, y, width, height, font, text)

    # checks to see if mouse click was on button, and returns True if so
    def onClick(self, position):
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            button4.play()
            return True
        else:
            return False
    
    def draw(self, position): 
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
            pygame.draw.rect(SCREEN, BOX_HOVER_OUTLINE, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)
            SCREEN.blit(self.text, self.textRect )
        else:
            pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
            pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)
            SCREEN.blit(self.text, self.textRect )


#class InputBox(Box):


def mainmenu_loop():

    while True:

        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()
        
        # creation of objects
        titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "THE Farm Game")

        newGameButton = Button(WIDTH // 2 - 140, 220, 280, 70, OCR_TEXT, "New Game")
        loadGameButton = Button(WIDTH // 2 - 140, 320, 280, 70, OCR_TEXT, "Load Game")
        instructionsButton = Button(WIDTH // 2 - 140, 420, 280, 70, OCR_TEXT, "How To Play")
        settingsButton = Button(WIDTH // 2 - 140, 520, 280, 70, OCR_TEXT, "Settings")

        # displays all elements
        titleBox.draw()
        for button in [newGameButton, loadGameButton, instructionsButton, settingsButton]:
            button.draw(mouse)

        # handling user interaction
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if newGameButton.onClick(mouse):
                    newgame1_loop()
                if loadGameButton.onClick(mouse):
                    loadgame_loop()
                if instructionsButton.onClick(mouse):
                    instructions_loop()
                if settingsButton.onClick(mouse):
                    settings_loop()

            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()

def newgame1_loop():

    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "New Game")

        backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
        tickButton = Button( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

        save1Label = TextBox(220, 250, 280, 80, OCR_TEXT, "Save 1:")
        save2Label = TextBox(220, 370, 280, 80, OCR_TEXT, "Save 2:")
        save3Label = TextBox(220, 490, 280, 80, OCR_TEXT, "Save 3:")

        save1Content = Button(560, 250, 280, 80, OCR_TEXT, "no save")
        save2Content = Button(560, 370, 280, 80, OCR_TEXT, "no save")
        save3Content = Button(560, 490, 280, 80, OCR_TEXT, "no save")

        titleBox.draw()

        for button in [backButton, tickButton, save1Content, save2Content, save3Content]:
            button.draw(mouse)

        for textbox in [save1Label, save2Label, save3Label]:
            textbox.draw()

        for inputbox in []:
            inputbox.draw()

        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                    mainmenu_loop()

                if tickButton.onClick(mouse):
                    newgame2_loop()

            if event.type == pygame.QUIT:
                pygame.quit()
            

        
        pygame.display.flip()

def newgame2_loop():
    while True:

        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "New Game")

        backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
        startButton = Button(WIDTH // 2 - (240 // 2), 570, 240, 80, OCR_TEXT, "Start")
        speedButton = Button(720, 580, 170, 60, OCR_TEXT, "Slow")

        nameLabel = TextBox(230, 240, 280, 80, OCR_TEXT, "Name:")
        passwordLabel = TextBox(230, 350, 280, 80, OCR_TEXT, "Password:")
        save3Label = TextBox(230, 460, 280, 80, OCR_TEXT, "Password:")

        nameInputBox = TextBox(570, 240, 280, 80, OCR_TEXT, "")
        password1InputBox = TextBox(570, 350, 280, 80, OCR_TEXT, "")
        password2InputBox = TextBox(570, 460, 280, 80, OCR_TEXT, "")

        SCREEN.blit(FEMALE_MC, (100,500) )
        SCREEN.blit(MALE_MC, (200,500) )

        
        for button in [backButton, startButton, speedButton]:
            button.draw(mouse)

        for textbox in [titleBox, nameLabel, passwordLabel, save3Label]:
            textbox.draw()

        for inputbox in [nameInputBox, password1InputBox, password2InputBox]:
            inputbox.draw()


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                        newgame1_loop()
            
            if event.type == pygame.QUIT:
                pygame.quit()
            

        pygame.display.flip()


def loadgame_loop():
    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Load Game")

        backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
        tickButton = Button( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

        save1Label = TextBox(230, 240, 280, 80, OCR_TEXT, "Save 1:")
        save2Label = TextBox(230, 350, 280, 80, OCR_TEXT, "Save 2:")
        save3Label = TextBox(230, 460, 280, 80, OCR_TEXT, "Save 3:")

        save1Content = Button(570, 240, 280, 80, OCR_TEXT, "no save")
        save2Content = Button(570, 350, 280, 80, OCR_TEXT, "no save")
        save3Content = Button(570, 460, 280, 80, OCR_TEXT, "no save")

        passwordInputBox = TextBox(WIDTH // 2 - (300 // 2), 580, 300, 80, OCR_TEXT, "")

        for textbox in [titleBox, save1Label, save2Label, save3Label]:
            textbox.draw()

        for button in [backButton, tickButton, save1Content, save2Content, save3Content]:
            button.draw(mouse)

        for inputbox in [passwordInputBox]:
            inputbox.draw()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                    mainmenu_loop()

            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()

def instructions_loop():
    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "How to Play:")

        backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )

        titleBox.draw()

        for button in [backButton]:
            button.draw(mouse)
        
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                    mainmenu_loop()

            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()

def settings_loop():

    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        global musicVal
        global sfxVal

        titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Settings")

        backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )

        musicLabel = TextBox(160, 250, 320, 70, OCR_TEXT, "Music")
        sfxLabel = TextBox(160, 390, 320, 70, OCR_TEXT, "Sound Effects")

        minusMusicButton = Button(570, 250, 90, 70, OCR_TITLE, "-"  )
        addMusicButton = Button(850, 250, 90, 70, OCR_TITLE, "+"  )
        minusSfxButton = Button(570, 390, 90, 70, OCR_TITLE, "-"  )
        addSfxButton = Button(850, 390, 90, 70, OCR_TITLE, "+"  )

        musicNum = TextBox(710, 250, 90, 70, OCR_TITLE, str(musicVal)  )
        sfxNum = TextBox(710, 390, 90, 70, OCR_TITLE, str(sfxVal)  )

        titleBox.draw()

        for button in [backButton, minusMusicButton, addMusicButton, minusSfxButton, addSfxButton ]:
            button.draw(mouse)
        
        for textbox in [musicLabel, sfxLabel, musicNum, sfxNum]:
            textbox.draw()
        
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                    mainmenu_loop()
                if minusMusicButton.onClick(mouse):
                    musicVal = int(musicNum.getText())
                    if musicVal > 0:
                        musicVal -= 1
                        pygame.mixer.music.set_volume(musicVal / 10)
                        print(musicVal/10)
                        musicNum.changeText(musicVal)
                
                if addMusicButton.onClick(mouse):
                    musicVal = int(musicNum.getText())
                    if musicVal < 10:
                        musicVal += 1
                        pygame.mixer.music.set_volume(musicVal / 10)
                        print(musicVal/10)
                        musicNum.changeText(musicVal)
                    
                if minusSfxButton.onClick(mouse):
                    sfxVal = int(sfxNum.getText())
                    if sfxVal > 0:
                        sfxVal -= 1
                        for effect in [button1, button2, button3, button4]:
                            effect.set_volume(sfxVal / 10)
                        sfxNum.changeText(sfxVal)
                    
                if addSfxButton.onClick(mouse):
                    sfxVal = int(sfxNum.getText())
                    if sfxVal < 10:
                        sfxVal += 1
                        for effect in [button1, button2, button3, button4]:
                            effect.set_volume(sfxVal / 10)
                        sfxNum.changeText(sfxVal)

            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()


if __name__ == "__main__":
    while True:
        mainmenu_loop()

pygame.quit()