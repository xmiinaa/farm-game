# importing all libraries needed in this module, including other python files
import pygame, config, database, Classes.box as box, re, hashlib, game
pygame.init()

# checks to see if the password entered fits the requiremens and is valid
def checkNewPassword(password1, password2, matchError, characterError):

    # the re squence for the password string requirement
    required = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"

    # checks if the passwords match, is over 8 characters, and fulfills the string requirements
    if password1 == password2 and len(password1) >= 8 and bool(re.fullmatch(required, password1)):

        # deactivates all the error messages and returns the value True
        matchError.deactivate()
        characterError.deactivate()

        return True
    
    else:

        # checks if the password matches, and changes the activation status of the corresponding error
        if password1 == password2:
            matchError.deactivate()
        else:
            matchError.activate()

        # checks to see if password matches length and string requirements, and changes the activation status of the corresponding error
        if len(password1) >= 8 and bool(re.fullmatch(required, password1)):
            characterError.deactivate()
        else:
            characterError.activate()

        return False

# hashes the password that has been passed into the function
def hashing(password):

    # the string is encoded into byres, which is needed for the algorithm to work
    password = password.encode('utf-8')

    # the password is then hashed into a hex string using the SHA-256 function
    sha3_256 = hashlib.sha3_256
    hashedPassword = sha3_256(password).hexdigest()

    return hashedPassword

# handles the initial screen loaded when opening the game
def mainmenu_loop():

    running = True

    # creation of objects
    titleBox = box.TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "THE Farm Game")

    newGameButton = box.Button(config.WIDTH // 2 - 140, 220, 280, 70, config.OCR_TEXT, "New Game")
    loadGameButton = box.Button(config.WIDTH // 2 - 140, 320, 280, 70, config.OCR_TEXT, "Load Game")
    instructionsButton = box.Button(config.WIDTH // 2 - 140, 420, 280, 70, config.OCR_TEXT, "How To Play")
    settingsButton = box.Button(config.WIDTH // 2 - 140, 520, 280, 70, config.OCR_TEXT, "Settings")

    while running:

        # displays menu image background
        config.SCREEN.blit(config.MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # displays all elements
        titleBox.draw()

        for button in [newGameButton, loadGameButton, instructionsButton, settingsButton]:

            # checks to see if the user's mouse is hovering over the button, which will draw the object differently
            button.checkHover(mouse)
            button.draw()

        # handling user interaction
        for event in pygame.event.get():

            # checks to see if user clicks with the mosue, and calls the corresponding loop depending on the button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if newGameButton.onClick(mouse):
                    newgame1_loop()
                if loadGameButton.onClick(mouse):
                    loadgame_loop()
                if instructionsButton.onClick(mouse):
                    instructions_loop()
                if settingsButton.onClick(mouse):
                    settings_loop()
            
            #  stops the loop if user clicks quit
            if event.type == pygame.QUIT:
                exit()
        
        # updates the display
        pygame.display.flip()

        # controls the frame rate
        config.CLOCK.tick(60)
    
    # cleanly exits the program
    pygame.quit()

# handles the first screen that is displayed when the user clicks on new game
def newgame1_loop():

    running = True
    # gets the usernames of all 3 saves and stores it in a list called save
    save = database.getUsernames()

    # replaces all "Null" saves with "no save" for displaying
    save = [('no save',) if save[0] == 'NULL' else save for save in save]

    # creation of objects 
    titleBox = box.TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "New Game")

    instruction = box.Text("Choose a save:", config.OCR_TEXT, config.BOX_FILL, 390, 220)

    backButton = box.Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    tickButton = box.Button( (config.WIDTH-30-90) , (config.HEIGHT-30-70) , 90, 70, config.OCR_TITLE, "->")

    save1Label = box.TextBox(220, 290, 280, 80, config.OCR_TEXT, "Save 1:")
    save2Label = box.TextBox(220, 400, 280, 80, config.OCR_TEXT, "Save 2:")
    save3Label = box.TextBox(220, 520, 280, 80, config.OCR_TEXT, "Save 3:")

    save1Content = box.Button(560, 290, 280, 80, config.OCR_TEXT, save[0][0])
    save2Content = box.Button(560, 400, 280, 80, config.OCR_TEXT, save[1][0])
    save3Content = box.Button(560, 520, 280, 80, config.OCR_TEXT, save[2][0])

    # save choice stores the save as an object and user choice stores the save as an integer
    saveChoice = -1
    userChoice = -1

    while running:

        # displays menu image background
        config.SCREEN.blit(config.MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # displays all elements
        for button in [backButton, tickButton, save1Content, save2Content, save3Content]:
            if button == saveChoice:
                button.draw()
            else:
                # checks to see if the user's mouse is hovering over the button, which changes the way the button is drawn
                button.checkHover(mouse)
                button.draw()

        for textbox in [titleBox, save1Label, save2Label, save3Label]:
            textbox.draw()

        for inputbox in []:
            inputbox.draw()

        instruction.draw()

        # handles user interaction
        for event in pygame.event.get():
            
            # checks to see if user clicks with the mouse, and checks to see if a specific button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # this goes back to the previous screen
                if backButton.onClick(mouse):
                    mainmenu_loop()        

                # checks to see if any of the 3 saves have been clicked one, and assigns the savechoice and userchoice to that specific save, displaying it differently
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

                # checks to see if user clicks on the tick button
                if tickButton.onClick(mouse):

                    # checks to see if the user has clicked on a save to overwrite
                    if saveChoice != -1:

                        # calls the next screen loop 
                        newgame2_loop(userChoice)
                
            #  stops the loop if user clicks quit
            if event.type == pygame.QUIT:
                running = False
            
        # updates the display
        pygame.display.flip()

        # controls the frame rate
        config.CLOCK.tick(60)
    
    # exits the program
    pygame.quit()

# handles the second screen needed to start a new game 
def newgame2_loop(saveChoice):

    # loads the required images and scales them to the correct dimensions needed to display on this screen
    FEMALE_MC = pygame.transform.scale(pygame.image.load('Resources/Images/girlMC.png'), (96, 144))
    MALE_MC = pygame.transform.scale(pygame.image.load('Resources/Images/maleMC.png'), (96, 144))
    ERROR = pygame.transform.scale(pygame.image.load('Resources/Images/error-icon.png'), (55, 48))

    running = True

    # stores the user's input for the name in a variable
    name = ""

    # stores the user's input for the passwords in different variables
    password1 = ""
    password2 = ""

    # stores the passwords that will be displayed to the user (only *)
    password1Display = ""
    password2Display = ""

    # stores the user's character choice
    chosenCharacter = ""

    # stores the user's mode choice
    speed = "slow"

    # automatically set to False and only turns to true if username entered does not exist yet
    validName = False

    # creation of objects 
    titleBox = box.TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "New Game")

    backButton = box.Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    startButton = box.Button(config.WIDTH // 2 - (240 // 2), 580, 240, 80, config.OCR_TEXT, "Start")
    speedButton = box.Button(690, 590, 170, 60, config.OCR_TEXT, "Slow")

    nameLabel = box.TextBox(205, 220, 300, 80, config.OCR_TEXT, "Name:")
    passwordLabel = box.TextBox(205, 320, 300, 80, config.OCR_TEXT, "Password:")
    save3Label = box.TextBox(205, 420, 300, 80, config.OCR_TEXT, "Password:")

    modeLabel = box.Text("Mode:", config.OCR_TEXT, config.BOX_FILL, 720, 540)
    characterLabel = box.Text("Character:", config.OCR_TEXT, config.BOX_FILL, 180, 510)

    nameInputBox = box.InputBox(565, 220, 300, 80, config.OCR_TEXT, name)
    password1InputBox = box.InputBox(565, 320, 300, 80, config.OCR_TEXT, password1Display)
    password2InputBox = box.InputBox(565, 420, 300, 80, config.OCR_TEXT, password2Display)

    femaleCharacter = box.ImageButton(FEMALE_MC, 240, 630, 96, 144)
    maleCharacter = box.ImageButton(MALE_MC, 340, 630, 96, 144)

    usernameError = box.Error(ERROR, 900, 265, "Username already exists", 275, 34, 750, 205)
    matchError = box.Error(ERROR, 900, 365, "Passwords do not match", 265, 34, 750, 305)
    characterError = box.Error(ERROR, 900, 470, "Password must be over 8 characters and must include lowercase, uppercase and a number", 970, 34, 100, 405)
    noNameError = box.Error(ERROR, 900, 265, "You must enter a name", 275, 34, 750, 205)

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
        
        for label in [modeLabel, characterLabel]:
            label.draw()

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
                        game.main()

            
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
        config.CLOCK.tick(60)
    
    pygame.quit()
            
def loadgame_loop():

    running = True
    saveChoice = -1
    userChoice = -1
    password = ""
    passwordDisplay = "Enter Password"
    
    save = database.getUsernames()
    save = [('no save',) if save[0] == 'NULL' else save for save in save]

    # creation of objects
    titleBox = box.TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "Load Game")

    backButton = box.Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    tickButton = box.Button( (config.WIDTH-30-90) , (config.HEIGHT-30-70) , 90, 70, config.OCR_TITLE, "->")

    save1Label = box.TextBox(230, 240, 280, 80, config.OCR_TEXT, "Save 1:")
    save2Label = box.TextBox(230, 350, 280, 80, config.OCR_TEXT, "Save 2:")
    save3Label = box.TextBox(230, 460, 280, 80, config.OCR_TEXT, "Save 3:")

    save1Content = box.Button(570, 240, 280, 80, config.OCR_TEXT, save[0][0])
    save2Content = box.Button(570, 350, 280, 80, config.OCR_TEXT, save[1][0])
    save3Content = box.Button(570, 460, 280, 80, config.OCR_TEXT, save[2][0])

    passwordInputBox = box.InputBox(config.WIDTH // 2 - (320 // 2), 580, 340, 80, config.OCR_TEXT, passwordDisplay)
    
    passwordInputBox.changeColour(config.GREY)

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
                    if passwordInputBox.getText() != "":
                        passwordHash = hashing(password)
                        correct = database.checkPassword(userChoice, passwordHash)
                        if correct:
                            game.main()
                
            if event.type == pygame.KEYDOWN: 
                
                if passwordInputBox.checkActive():

                    passwordInputBox.changeColour(config.FONT_COLOUR)

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
        config.CLOCK.tick(60)
    
    pygame.quit()

def instructions_loop():

    running = True
    # creation of objects
    titleBox = box.TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "How to Play")
    backButton = box.Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )
    
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
        config.CLOCK.tick(60)
    pygame.quit()

def settings_loop():

    running = True

    # creation of objects
    titleBox = box.TextBox(config.WIDTH // 2 - (config.TITLE_WIDTH // 2), 100, config.TITLE_WIDTH, config.TITLE_HEIGHT, config.OCR_TITLE, "Settings")

    backButton = box.Button(30, 30, 90, 70, config.OCR_TITLE, "<-"  )

    musicLabel = box.TextBox(160, 250, 320, 70, config.OCR_TEXT, "Music")
    sfxLabel = box.TextBox(160, 390, 320, 70, config.OCR_TEXT, "Sound Effects")

    minusMusicButton = box.Button(570, 250, 90, 70, config.OCR_TITLE, "-"  )
    addMusicButton = box.Button(850, 250, 90, 70, config.OCR_TITLE, "+"  )
    minusSfxButton = box.Button(570, 390, 90, 70, config.OCR_TITLE, "-"  )
    addSfxButton = box.Button(850, 390, 90, 70, config.OCR_TITLE, "+"  )

    musicNum = box.TextBox(710, 250, 90, 70, config.OCR_TITLE, str(config.musicVal)  )
    sfxNum = box.TextBox(710, 390, 90, 70, config.OCR_TITLE, str(config.sfxVal)  )

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
                        for effect in [config.button1, config.button2]:
                            effect.set_volume(config.sfxVal / 10)
                        sfxNum.changeText(config.sfxVal)
                    
                if addSfxButton.onClick(mouse):
                    config.sfxVal = int(sfxNum.getText())
                    if config.sfxVal < 10:
                        config.sfxVal += 1
                        for effect in [config.button1, config.button2]:
                            effect.set_volume(config.sfxVal / 10)
                        sfxNum.changeText(config.sfxVal)

            # ends program
            if event.type == pygame.QUIT:
                running = False
            
        pygame.display.flip()
        config.CLOCK.tick(60)

    pygame.quit()
