# imports and initialise the pygame library

import re
import sqlite3
import hashlib
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
ERROR_FONT_COLOUR = (255, 45, 45)

# text font
OCR_TITLE = pygame.font.Font('Resources\OCR.ttf', 48)
OCR_TEXT = pygame.font.Font('Resources\OCR.ttf', 38)
OCR_ERROR = pygame.font.Font('Resources\OCR.ttf', 26)

# set up window
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('THE Farm Game')

# images 
MENU_BG = pygame.transform.scale(pygame.image.load('Resources\Images\menu-background.png'), (WIDTH, HEIGHT))
FEMALE_MC = pygame.transform.scale(pygame.image.load('Resources\Images\girlMC.png'), (100, 300))
MALE_MC = pygame.image.load('Resources\Images\maleMC.png')

# music
musicVal = 0
sfxVal = 5

pygame.mixer.music.load('Resources\Music\music1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0) # this cause im gonna get sick of music when testing it 

button1 = pygame.mixer.Sound('Resources\Sound-effects\cbutton3.mp3')
button2 = pygame.mixer.Sound('Resources\Sound-effects\cbutton4.mp3')

salt = "5gz"

# saves files
savesFile = open("saveFile.txt", "a+")
savesFile.close()

for sounds in [button1, button2]:
    sounds.set_volume(0.5)

class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.colourFill = BOX_FILL
        self.colourBorder = BOX_OUTLINE
        self.width = width
        self.height = height

    # displays box onto screen
    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 3)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 3)

class TextBox(Box):
    def __init__(self, x, y,  width, height, font, content):
       super().__init__(x, y, width, height) 
       self.font = font
       self.content = content
       self.fontColour = FONT_COLOUR
       self.text = font.render(self.content, True, self.fontColour)
       self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))

    # displays text box onto screen
    def draw(self): 
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)

        SCREEN.blit(self.text, self.textRect )   

    # getter method to access text inside text box
    def getText(self):
        return self.content

    # method to change text in text box
    def changeText(self, newText):
        self.content = str(newText)
        font = self.font
        self.text = font.render(self.content, True, self.fontColour)
        self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))
    

class Button(TextBox):
    def __init__(self, x, y,  width, height, font, text):
        super().__init__(x, y, width, height, font, text)

    # checks to see if mouse click was on button, and returns True if so
    def onClick(self, position):
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            button1.play()
            return True
        else:
            return False
    
    # dispalys button onto screen
    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)
        SCREEN.blit(self.text, self.textRect )

    # changes colour of button border if user is hovering over it with the cursor
    def checkHover(self, position):
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            self.colourBorder = BOX_HOVER_OUTLINE
        else:
            self.colourBorder = BOX_OUTLINE

    # changes colour of button border (used when choice is made)    
    def choiceClick(self):
        self.colourBorder = BOX_HOVER_OUTLINE

class InputBox(Button):
    def __init__(self, x, y,  width, height, font, text):
        super().__init__(x, y, width, height, font, text)
        self.active = False

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def checkActive(self):
        return self.active

    # changes colour of box border depending on if the user is hovering over the box or if they have clicked it
    def checkHoverOrClick(self, position):
        if self.active:
            self.colourBorder = BOX_HOVER_OUTLINE
        else:
            if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
                self.colourBorder = BOX_HOVER_OUTLINE
            else:
                self.colourBorder = BOX_OUTLINE

class Text():
    def __init__(self, x, y, font, colour, content):
        self.x = x
        self.y = y
        self.font = font
        self.fontColour = colour
        self.content = content
        self.active = False
        self.text = font.render(self.content, True, self.fontColour)
        self.textRect = self.text.get_rect()
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def checkActive(self):
        return self.active
    
    def draw(self):
        SCREEN.blit(self.text, (self.x, self.y))

class ImageButton():
    def __init__(self, image, x, y, width, height):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = self.image.get_rect(centre=(self.x, self,y))
    
    def onClick(self, position):
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            button1.play()
            return True
        else:
            return False
    
    def draw(self):
        SCREEN.blit(self.image, self.rect)

def checkNewPassword(password1, password2, error1, error2, error3):
    required = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
    print("checking")

    if password1 == password2 and len(password1) >= 8 and bool(re.fullmatch(required, password1)):
        return True
    else:
        if password1 == password2:
            error1.deactivate()
        else:
            error1.activate()
        
        if len(password1) >= 8:
            error2.deactivate()
        else:
            error2.activate()
    
        if bool(re.fullmatch(required, password1)):
            error3.deactivate()
        else:
            error3.activate()

        return False
"""
    if password1 == password2:
        print("pass 1")
        error1.deactivate()
        if len(password1) >= 8:
            print("pass 2")
            error2.deactivate()
            if bool(re.fullmatch(required, password1)):
                print("pass 3")
                error3.deactivate()
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1
"""

def mainmenu_loop():

    # creation of objects
    titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "THE Farm Game")

    newGameButton = Button(WIDTH // 2 - 140, 220, 280, 70, OCR_TEXT, "New Game")
    loadGameButton = Button(WIDTH // 2 - 140, 320, 280, 70, OCR_TEXT, "Load Game")
    instructionsButton = Button(WIDTH // 2 - 140, 420, 280, 70, OCR_TEXT, "How To Play")
    settingsButton = Button(WIDTH // 2 - 140, 520, 280, 70, OCR_TEXT, "Settings")

    while True:

        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # displays all elements
        titleBox.draw()
        for button in [newGameButton, loadGameButton, instructionsButton, settingsButton]:
            button.checkHover(mouse)
            button.draw()

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
            
            # exits program
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()

def newgame1_loop():

    # creation of objects
    titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "New Game")

    backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    tickButton = Button( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

    save1Label = TextBox(220, 250, 280, 80, OCR_TEXT, "Save 1:")
    save2Label = TextBox(220, 370, 280, 80, OCR_TEXT, "Save 2:")
    save3Label = TextBox(220, 490, 280, 80, OCR_TEXT, "Save 3:")

    save1Content = Button(560, 250, 280, 80, OCR_TEXT, "no save")
    save2Content = Button(560, 370, 280, 80, OCR_TEXT, "no save")
    save3Content = Button(560, 490, 280, 80, OCR_TEXT, "no save")

    # user's save choice
    saveChoice = -1

    while True:

        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # displays all elements
        for button in [backButton, tickButton, save1Content, save2Content, save3Content]:
            if button == saveChoice:
                button.draw()
            else:
                button.checkHover(mouse)
                button.draw()

        for textbox in [titleBox, save1Label, save2Label, save3Label]:
            textbox.draw()

        for inputbox in []:
            inputbox.draw()

        # handles user interaction
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                if backButton.onClick(mouse):
                    mainmenu_loop()

                for choice in [save1Content, save2Content, save3Content]:
                    if choice.onClick(mouse):
                        saveChoice = choice
                        saveChoice.choiceClick() 

                if tickButton.onClick(mouse):
                    if saveChoice != -1:
                        newgame2_loop()
                
            #  ends program
            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()


def newgame2_loop():

    name = ""
    password1 = ""
    password2 = ""

    # creation of objects 
    titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "New Game")

    backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    startButton = Button(WIDTH // 2 - (240 // 2), 520, 240, 80, OCR_TEXT, "Start")
    speedButton = Button(720, 530, 170, 60, OCR_TEXT, "Slow")

    nameLabel = TextBox(210, 220, 300, 75, OCR_TEXT, "Name:")
    passwordLabel = TextBox(210, 310, 300, 75, OCR_TEXT, "Password:")
    save3Label = TextBox(210, 400, 300, 75, OCR_TEXT, "Password:")

    nameInputBox = InputBox(560, 220, 300, 75, OCR_TEXT, name)
    password1InputBox = InputBox(560, 310, 300, 75, OCR_TEXT, password1)
    password2InputBox = InputBox(560, 400, 300, 75, OCR_TEXT, password2)

    femaleCharacter = ImageButton(FEMALE_MC, 170, 530, 100, 150)
    maleCharacter = ImageButton(MALE_MC, 290, 530, 100, 150)

    usernameError = Text(50, 600, OCR_ERROR, ERROR_FONT_COLOUR, "Error - Username already exists" )
    error3 = Text(50, 630, OCR_ERROR, ERROR_FONT_COLOUR, "Error - password must include uppercase, lowercase and a number" )
    error2 = Text(50, 660, OCR_ERROR, ERROR_FONT_COLOUR, "Error - Password must be 8 characters or longer" )
    error1 = Text(50, 690, OCR_ERROR, ERROR_FONT_COLOUR, "Error - Passwords do not match" )

    while True:

        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # dislpays all elements
        SCREEN.blit(FEMALE_MC, (170,530) )
        SCREEN.blit(MALE_MC, (290,530) )

        
        for button in [backButton, startButton, speedButton]:
            button.checkHover(mouse)
            button.draw()

        for textbox in [titleBox, nameLabel, passwordLabel, save3Label]:
            textbox.draw()

        for inputbox in [nameInputBox, password1InputBox, password2InputBox]:
            inputbox.checkHoverOrClick(mouse)
            inputbox.draw()
        
        for character in [femaleCharacter, maleCharacter]:
            character.draw()
        
        for error in [usernameError, error1, error2, error3]:
           #if error.checkActive() == True:
            error.draw()

        # handles user interaction
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                if backButton.onClick(mouse):
                        newgame1_loop()
                
                if nameInputBox.onClick(mouse):
                    nameInputBox.activate()
                else:
                    nameInputBox.deactivate()

                if password1InputBox.onClick(mouse):
                    password1InputBox.activate()
                else:
                    password1InputBox.deactivate()
                
                if password2InputBox.onClick(mouse):
                    password2InputBox.activate()
                else:
                    password2InputBox.deactivate()
                
                if startButton.onClick(mouse):
                    correct = checkNewPassword(password1, password2, error1, error2, error3)
                    print(correct)
                    if correct:
                        print("passwords are good to go")
                        dataBase_password = password1+salt
                        hashed = hashlib.md5(dataBase_password.encode())
                        print(hashed.hexdigest())

            
            if event.type == pygame.KEYDOWN: 
                
                if nameInputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                        name = name[:-1] 

                    elif len(name) <= 11: 
                        name += event.unicode
                    
                    nameInputBox.changeText(name)
                
                if password1InputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                        password1 = password1[:-1] 

                    elif len(password1) <= 11: 
                        password1 += event.unicode
                    
                    password1InputBox.changeText(password1)
                
                if password2InputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                        password2 = password2[:-1] 

                    elif len(password2) <= 11: 
                        password2 += event.unicode
                    
                    password2InputBox.changeText(password2)
            
            # ends program
            if event.type == pygame.QUIT:
                pygame.quit()
            

        pygame.display.flip()


def loadgame_loop():

    saveChoice = -1
    password = ""

    # creation of objects
    titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Load Game")

    backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    tickButton = Button( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

    save1Label = TextBox(230, 240, 280, 80, OCR_TEXT, "Save 1:")
    save2Label = TextBox(230, 350, 280, 80, OCR_TEXT, "Save 2:")
    save3Label = TextBox(230, 460, 280, 80, OCR_TEXT, "Save 3:")

    save1Content = Button(570, 240, 280, 80, OCR_TEXT, "no save")
    save2Content = Button(570, 350, 280, 80, OCR_TEXT, "no save")
    save3Content = Button(570, 460, 280, 80, OCR_TEXT, "no save")

    passwordInputBox = InputBox(WIDTH // 2 - (320 // 2), 580, 320, 80, OCR_TEXT, password)
    

    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # dislpays all elements
        for textbox in [titleBox, save1Label, save2Label, save3Label]:
            textbox.draw()

        for button in [backButton, tickButton, save1Content, save2Content, save3Content]:
            if button == saveChoice:
                button.draw()
            else:
                button.checkHover(mouse)
                button.draw()

        for inputbox in [passwordInputBox]:
            inputbox.checkHoverOrClick(mouse)
            inputbox.draw()

        # handles user interaction
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                if backButton.onClick(mouse):
                    mainmenu_loop()

                for choice in [save1Content, save2Content, save3Content]:
                    if choice.onClick(mouse):
                        saveChoice = choice
                        saveChoice.choiceClick() 
                
                if passwordInputBox.onClick(mouse):
                    passwordInputBox.activate()
                else:
                    passwordInputBox.deactivate()

                if tickButton.onClick(mouse):
                    print(saveChoice)
                
            if event.type == pygame.KEYDOWN: 
                
                if passwordInputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                        password = password[:-1] 

                    elif len(password) <= 11: 
                        password += event.unicode
                    
                    passwordInputBox.changeText(password)

            # ends program
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()

def instructions_loop():

    # creation of objects
    titleBox = TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "How to Play")
    backButton = Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    
    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # displays all elements
        for textBox in [titleBox]:
          textBox.draw()

        for button in [backButton]:
            button.checkHover(mouse)
            button.draw()
        
        # handles user interaction
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                    mainmenu_loop()

            # ends program
            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()

def settings_loop():

    global musicVal
    global sfxVal


    # creation of objects
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

    while True:
        SCREEN.blit(MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # displays all elements
        for button in [backButton, minusMusicButton, addMusicButton, minusSfxButton, addSfxButton ]:
            button.checkHover(mouse)
            button.draw()
        
        for textbox in [titleBox, musicLabel, sfxLabel, musicNum, sfxNum]:
            textbox.draw()
        
        # handles user interaction
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.onClick(mouse):
                    mainmenu_loop()
                if minusMusicButton.onClick(mouse):
                    musicVal = int(musicNum.getText())
                    if musicVal > 0:
                        musicVal -= 1
                        pygame.mixer.music.set_volume(musicVal / 10)
                        musicNum.changeText(musicVal)
                
                if addMusicButton.onClick(mouse):
                    musicVal = int(musicNum.getText())
                    if musicVal < 10:
                        musicVal += 1
                        pygame.mixer.music.set_volume(musicVal / 10)
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

            # ends program
            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()


if __name__ == "__main__":
    while True:
        newgame2_loop()

pygame.quit()