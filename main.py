# imports and initialise the pygame library, and oher libraries used and needed in program

import re, hashlib, pygame
import database, config
pygame.init()

# set up window
CLOCK = pygame.time.Clock()
pygame.display.set_caption('THE Farm Game')

pygame.mixer.music.load('Resources/Music/music1.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0) # todo: set to 5

button1 = pygame.mixer.Sound('Resources/Sound-effects/cbutton3.mp3')
button2 = pygame.mixer.Sound('Resources/Sound-effects/cbutton4.mp3')

for sounds in [button1, button2]:
    sounds.set_volume(0.5)
    
class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.colourFill = config.BOX_FILL
        self.colourBorder = config.BOX_OUTLINE
        self.width = width
        self.height = height

    # displays box onto screen
    def draw(self):
        pygame.draw.rect(config.SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 3)
        pygame.draw.rect(config.SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 3)

class TextBox(Box):
    def __init__(self, x, y,  width, height, font, content):
       super().__init__(x, y, width, height) 
       self.font = font
       self.content = content
       self.fontColour = config.FONT_COLOUR
       self.text = font.render(self.content, True, self.fontColour)
       self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))

    # displays text box onto screen
    def draw(self): 
        pygame.draw.rect(config.SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(config.SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)

        config.SCREEN.blit(self.text, (self.textRect) )   

    # getter method to access text inside text box
    def getText(self):
        return self.content

    # method to change text in text box
    def changeText(self, newText):
        self.content = str(newText)
        self.font = self.font
        self.text = self.font.render(self.content, True, self.fontColour)
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
        pygame.draw.rect(config.SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(config.SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)
        config.SCREEN.blit(self.text, self.textRect )

    # changes colour of button border if user is hovering over it with the cursor
    def checkHover(self, position):
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            self.colourBorder = config.WHITE
        else:
            self.colourBorder = config.BOX_OUTLINE

    # changes colour of button border (used when choice is made)    
    def choiceClick(self):
        self.colourBorder = config.WHITE

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
            self.colourBorder = config.WHITE
        else:
            if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
                self.colourBorder = config.WHITE
            else:
                self.colourBorder = config.BOX_OUTLINE

class Error():
    def __init__(self, image, imageX, imageY, text, width, height, textX, textY):
        self.image = image
        self.imageX = imageX
        self.imageY = imageY
        self.width = width
        self.height = height
        self.active = False
        self.rect = self.image.get_rect(center = (self.imageX, self.imageY))
        self.textX = textX
        self.textY = textY
        self.content = str(text)
        self.fontColour = config.ERROR_FONT_COLOUR
        self.colourBorder = (190,0, 0)
        font = config.OCR_ERROR
        self.text = font.render(self.content, True, self.fontColour)
        self.colourFill = config.WHITE
        self.textRect = self.text.get_rect(center = (self.width // 2 + self.textX, self.height // 2 + self.textY))
        
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def checkActive(self):
        return self.active
    
    def draw(self):
        config.SCREEN.blit(self.image, (self.rect))

    def checkHover(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            pygame.draw.rect(config.SCREEN, self.colourFill, pygame.Rect(self.textX, self.textY , self.width, self.height))
            pygame.draw.rect(config.SCREEN, self.colourBorder, pygame.Rect(self.textX, self.textY , self.width, self.height), 1, 0)
            config.SCREEN.blit(self.text, self.textRect)

class ImageButton():
    def __init__(self, image, x, y, width, height):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.active = False
    
    def onClick(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            button1.play()
            self.activate()
            return True
        else:
            return False
        
    def checkHover(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.drawBox()
        else:
            config.SCREEN.blit(self.image, self.rect)

    def draw(self):
        config.SCREEN.blit(self.image, self.rect)
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def checkActive(self):
        return self.active
    
    def drawBox(self):
        pygame.draw.rect(config.SCREEN, (255,255,255, 0), pygame.Rect(self.rect.left, self.rect.top, self.width, self.height), 2, 3)

def checkNewPassword(password1, password2, matchError, characterError):
    required = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"

    if password1 == password2 and len(password1) >= 8 and bool(re.fullmatch(required, password1)):
        matchError.deactivate()
        characterError.deactivate()
        return True
    else:
        if password1 == password2:
            matchError.deactivate()
        else:
            matchError.activate()

        if len(password1) >= 8 and bool(re.fullmatch(required, password1)):
            characterError.deactivate()
        else:
            characterError.activate()

        return False

def hashing(password):
    password = password.encode('utf-8')
    sha3_256 = hashlib.sha3_256
    hashedPassword = sha3_256(password).hexdigest()
    return hashedPassword

def mainmenu_loop():

    running = True

    # creation of objects
    titleBox = TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "THE Farm Game")

    newGameButton = Button(config.WIDTH // 2 - 140, 220, 280, 70, config.OCR_TEXT, "New Game")
    loadGameButton = Button(config.WIDTH // 2 - 140, 320, 280, 70, config.OCR_TEXT, "Load Game")
    instructionsButton = Button(config.WIDTH // 2 - 140, 420, 280, 70, config.OCR_TEXT, "How To Play")
    settingsButton = Button(config.WIDTH // 2 - 140, 520, 280, 70, config.OCR_TEXT, "Settings")

    while running:

        config.SCREEN.blit(config.MENU_BG, (0, 0))
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
            if event.type != pygame.QUIT:
                pygame.display.flip()
            else:
                pygame.quit()
                break

def newgame1_loop():

    running = True
    # creation of objects
    titleBox = TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "New Game")

    backButton = Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    tickButton = Button( (config.WIDTH-30-90) , (config.HEIGHT-30-70) , 90, 70, config.OCR_TITLE, "->")

    save1Label = TextBox(220, 250, 280, 80, config.OCR_TEXT, "Save 1:")
    save2Label = TextBox(220, 370, 280, 80, config.OCR_TEXT, "Save 2:")
    save3Label = TextBox(220, 490, 280, 80, config.OCR_TEXT, "Save 3:")

    save = database.getUsernames()

    save1Content = Button(560, 250, 280, 80, config.OCR_TEXT, save[0][0])
    save2Content = Button(560, 370, 280, 80, config.OCR_TEXT, save[1][0])
    save3Content = Button(560, 490, 280, 80, config.OCR_TEXT, save[2][0])

    # user's save choice
    saveChoice = -1
    userChoice = -1

    while running:

        config.SCREEN.blit(config.MENU_BG, (0, 0))
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

                if save1Content.onClick(mouse):
                    saveChoice = save1Content
                    saveChoice.choiceClick()    
                    userChoice = 1
                if save2Content.onClick(mouse):
                    saveChoice = save2Content
                    saveChoice.choiceClick()    
                    userChoice = 2
                if save3Content.onClick(mouse):
                    saveChoice = save3Content
                    saveChoice.choiceClick()    
                    userChoice = 3

                if tickButton.onClick(mouse):
                    if saveChoice != -1:
                        newgame2_loop(userChoice)
                
            #  ends program
            if event.type == pygame.QUIT:
                running = False
            
        pygame.display.flip()

    pygame.quit()

def newgame2_loop(saveChoice):

    FEMALE_MC = pygame.transform.scale(pygame.image.load('Resources/Images/girlMC.png'), (96, 144))
    MALE_MC = pygame.transform.scale(pygame.image.load('Resources/Images/maleMC.png'), (96, 144))
    ERROR = pygame.transform.scale(pygame.image.load('Resources/Images/error-icon.png'), (55, 48))

    running = True
    name = ""
    password1 = ""
    password1Display = ""
    password2 = ""
    password2Display = ""
    chosenCharacter = ""
    speed = "slow"
    validName = False

    # creation of objects 
    titleBox = TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "New Game")

    backButton = Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    startButton = Button(config.WIDTH // 2 - (240 // 2), 580, 240, 80, config.OCR_TEXT, "Start")
    speedButton = Button(690, 590, 170, 60, config.OCR_TEXT, "Slow")

    nameLabel = TextBox(205, 230, 300, 80, config.OCR_TEXT, "Name:")
    passwordLabel = TextBox(205, 330, 300, 80, config.OCR_TEXT, "Password:")
    save3Label = TextBox(205, 430, 300, 80, config.OCR_TEXT, "Password:")

    nameInputBox = InputBox(565, 230, 300, 80, config.OCR_TEXT, name)
    password1InputBox = InputBox(565, 330, 300, 80, config.OCR_TEXT, password1Display)
    password2InputBox = InputBox(565, 430, 300, 80, config.OCR_TEXT, password2Display)

    femaleCharacter = ImageButton(FEMALE_MC, 240, 610, 96, 144)
    maleCharacter = ImageButton(MALE_MC, 340, 610, 96, 144)

    usernameError = Error(ERROR, 900, 265, "Username already exists", 275, 34, 750, 205)
    matchError = Error(ERROR, 900, 365, "Passwords do not match", 265, 34, 750, 305)
    characterError = Error(ERROR, 900, 470, "Password must be over 8 characters and must include lowercase, uppercase and a number", 970, 34, 100, 405)
    noNameError = Error(ERROR, 900, 265, "You must enter a name", 275, 34, 750, 205)

    while running:

        config.SCREEN.blit(config.MENU_BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # dislpays all elements

        for button in [backButton, startButton, speedButton]:
            button.checkHover(mouse)
            button.draw()

        for textbox in [titleBox, nameLabel, passwordLabel, save3Label]:
            textbox.draw()

        for inputbox in [nameInputBox, password1InputBox, password2InputBox]:
            inputbox.checkHoverOrClick(mouse)
            inputbox.draw()
        
        for character in [femaleCharacter, maleCharacter]:
            if character.checkActive() == True:
                character.draw()
                character.drawBox()
            else:
                character.checkHover(mouse)
                character.draw()
        
        for error in [usernameError, matchError, characterError, noNameError]:
            if error.checkActive() == True:
                error.checkHover(mouse)
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
                
                if femaleCharacter.onClick(mouse):
                    chosenCharacter = "female"
                    femaleCharacter.activate()
                    maleCharacter.deactivate()
                
                if maleCharacter.onClick(mouse):
                    chosenCharacter = "male"
                    maleCharacter.activate()
                    femaleCharacter.deactivate()
                
                if speedButton.onClick(mouse):
                    if speedButton.getText() == "Slow":
                        speed = "Fast"
                        speedButton.changeText("Fast")
                    elif speedButton.getText() == "Fast":
                        speed = "Slow"
                        speedButton.changeText("Slow")

                if startButton.onClick(mouse):
                    correctPassword = checkNewPassword(password1, password2, matchError, characterError)
                    username = nameInputBox.getText()

                    if username == "":
                        noNameError.activate()
                    else:
                        noNameError.deactivate()
                        validName = database.checkUsername(str(username))
                    

                    if validName:
                        usernameError.deactivate()
                    else:
                        usernameError.activate()

                    if correctPassword and chosenCharacter != "" and validName:
                        passwordHash = hashing(password1)
                        database.create_newsave(username, passwordHash, saveChoice)

            
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
                        password1Display = password1Display[:-1]

                    elif len(password1) <= 11: 
                        password1 += event.unicode
                        
                    
                    password1Display = "*" * len(password1)
                    password1InputBox.changeText(password1Display)
                
                if password2InputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # get text input from 0 to -1 i.e. end. 
                        password2 = password2[:-1] 
                        password2Display = password2Display[:-1]


                    elif len(password2) <= 11: 
                        password2 += event.unicode
                    
                    password2Display = "*" * len(password2)
                    password2InputBox.changeText(password2Display)
                            
            # ends program
            if event.type == pygame.QUIT:
                running = False
        
            
        pygame.display.flip()
    
    pygame.quit()
            
def loadgame_loop():

    running = True
    saveChoice = -1
    userChoice = -1
    password = ""
    passwordDisplay = ""
    
    save = database.getUsernames()

    # creation of objects
    titleBox = TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "Load Game")

    backButton = Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    tickButton = Button( (config.WIDTH-30-90) , (config.HEIGHT-30-70) , 90, 70, config.OCR_TITLE, "->")

    save1Label = TextBox(230, 240, 280, 80, config.OCR_TEXT, "Save 1:")
    save2Label = TextBox(230, 350, 280, 80, config.OCR_TEXT, "Save 2:")
    save3Label = TextBox(230, 460, 280, 80, config.OCR_TEXT, "Save 3:")

    save1Content = Button(570, 240, 280, 80, config.OCR_TEXT, save[0][0])
    save2Content = Button(570, 350, 280, 80, config.OCR_TEXT, save[1][0])
    save3Content = Button(570, 460, 280, 80, config.OCR_TEXT, save[2][0])

    passwordInputBox = InputBox(config.WIDTH // 2 - (320 // 2), 580, 320, 80, config.OCR_TEXT, passwordDisplay)
    

    while running:
        config.SCREEN.blit(config.MENU_BG, (0, 0))
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

                if save1Content.onClick(mouse):
                    saveChoice = save1Content
                    saveChoice.choiceClick()    
                    userChoice = 1
                if save2Content.onClick(mouse):
                    saveChoice = save2Content
                    saveChoice.choiceClick()    
                    userChoice = 2
                if save3Content.onClick(mouse):
                    saveChoice = save3Content
                    saveChoice.choiceClick()    
                    userChoice = 3 
                
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
                    
                    passwordDisplay = "*" * len(password)
                    passwordInputBox.changeText(passwordDisplay)

            # ends program
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.flip()
    
    pygame.quit()

def instructions_loop():

    running = True
    # creation of objects
    titleBox = TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "How to Play")
    backButton = Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    
    while running:
        config.SCREEN.blit(config.MENU_BG, (0, 0))
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
                running = False
            
        pygame.display.flip()
    pygame.quit()

def settings_loop():

    running = True

    # creation of objects
    titleBox = TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "Settings")

    backButton = Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )

    musicLabel = TextBox(160, 250, 320, 70, config.OCR_TEXT, "Music")
    sfxLabel = TextBox(160, 390, 320, 70, config.OCR_TEXT, "Sound Effects")

    minusMusicButton = Button(570, 250, 90, 70, config.OCR_TITLE, "-"  )
    addMusicButton = Button(850, 250, 90, 70, config.OCR_TITLE, "+"  )
    minusSfxButton = Button(570, 390, 90, 70, config.OCR_TITLE, "-"  )
    addSfxButton = Button(850, 390, 90, 70, config.OCR_TITLE, "+"  )

    musicNum = TextBox(710, 250, 90, 70, config.OCR_TITLE, str(config.musicVal)  )
    sfxNum = TextBox(710, 390, 90, 70, config.OCR_TITLE, str(config.sfxVal)  )

    while running:
        config.SCREEN.blit(config.MENU_BG, (0, 0))
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
                    config.musicVal = int(musicNum.getText())
                    if config.musicVal > 0:
                        config.musicVal -= 1
                        pygame.mixer.music.set_volume(config.musicVal / 10)
                        musicNum.changeText(config.musicVal)
                
                if addMusicButton.onClick(mouse):
                    config.musicVal = int(musicNum.getText())
                    if config.musicVal < 10:
                        config.musicVal += 1
                        pygame.mixer.music.set_volume(config.musicVal / 10)
                        musicNum.changeText(config.musicVal)
                    
                if minusSfxButton.onClick(mouse):
                    config.sfxVal = int(sfxNum.getText())
                    if config.sfxVal > 0:
                        config.sfxVal -= 1
                        for effect in [button1, button2]:
                            effect.set_volume(config.sfxVal / 10)
                        sfxNum.changeText(config.sfxVal)
                    
                if addSfxButton.onClick(mouse):
                    config.sfxVal = int(sfxNum.getText())
                    if config.sfxVal < 10:
                        config.sfxVal += 1
                        for effect in [button1, button2]:
                            effect.set_volume(config.sfxVal / 10)
                        sfxNum.changeText(config.sfxVal)

            # ends program
            if event.type == pygame.QUIT:
                running = False
            
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    mainmenu_loop()
    
pygame.quit()