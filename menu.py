# importing all libraries needed in this module, including other python files
import pygame, database, Classes.box as box, re, hashlib, game, sys, farm
from config import *

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
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Arable  Adventures")

    newGameButton = box.Button(WIDTH // 2 - 140, 220, 280, 70, OCR_TEXT, "New Game")
    loadGameButton = box.Button(WIDTH // 2 - 140, 320, 280, 70, OCR_TEXT, "Load Game")
    instructionsButton = box.Button(WIDTH // 2 - 140, 420, 280, 70, OCR_TEXT, "How To Play")
    settingsButton = box.Button(WIDTH // 2 - 140, 520, 280, 70, OCR_TEXT, "Settings")

    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

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
        CLOCK.tick(60)
    
    # cleanly exits the program
    pygame.quit()
    sys.exit()

# handles the first screen that is displayed when the user clicks on new game
def newgame1_loop():

    running = True
    # gets the usernames of all 3 saves and stores it in a list called save
    save = database.getUsernames()

    # replaces all "Null" saves with "no save" for displaying
    save = [('no save',) if save[0] == 'NULL' else save for save in save]

    # creation of objects 
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Choose a save")

    backButton = box.Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    tickButton = box.Button( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

    save1Label = box.TextBox(230, 260, 280, 80, OCR_TEXT, "Save 1:")
    save2Label = box.TextBox(230, 380, 280, 80, OCR_TEXT, "Save 2:")
    save3Label = box.TextBox(230, 500, 280, 80, OCR_TEXT, "Save 3:")

    save1Content = box.Button(570, 260, 280, 80, OCR_TEXT, save[0][0])
    save2Content = box.Button(570, 380, 280, 80, OCR_TEXT, save[1][0])
    save3Content = box.Button(570, 500, 280, 80, OCR_TEXT, save[2][0])

    # save choice stores the save as an object and user choice stores the save as an integer
    saveChoice = -1
    userChoice = -1

    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

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
        CLOCK.tick(60)
    
    # exits the program
    pygame.quit()
    sys.exit()

# handles the second screen needed to start a new game 
def newgame2_loop(saveChoice):

    # loads the required images and scales them to the correct dimensions needed to display on this screen
    FEMALE_MC = pygame.transform.scale(pygame.image.load('Resources/Images/Menu/girlMC.png'), (96, 144))
    MALE_MC = pygame.transform.scale(pygame.image.load('Resources/Images/Menu/maleMC.png'), (96, 144))
    ERROR = pygame.transform.scale(pygame.image.load('Resources/Images/Menu/error-icon.png'), (55, 48))

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
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "New Game")

    backButton = box.Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    startButton = box.Button(WIDTH // 2 - (240 // 2), 580, 240, 80, OCR_TEXT, "Start")
    speedButton = box.Button(690, 590, 170, 60, OCR_TEXT, "Slow")

    nameLabel = box.TextBox(205, 220, 300, 80, OCR_TEXT, "Name:")
    passwordLabel = box.TextBox(205, 320, 300, 80, OCR_TEXT, "Password:")
    save3Label = box.TextBox(205, 420, 300, 80, OCR_TEXT, "Password:")

    modeLabel = box.Text("Mode:", OCR_TEXT, BOX_FILL, 720, 540)
    characterLabel = box.Text("Character:", OCR_TEXT, BOX_FILL, 180, 510)

    nameInputBox = box.InputBox(565, 220, 300, 80, OCR_TEXT, name)
    password1InputBox = box.InputBox(565, 320, 300, 80, OCR_TEXT, password1Display)
    password2InputBox = box.InputBox(565, 420, 300, 80, OCR_TEXT, password2Display)

    femaleCharacter = box.ImageButton(FEMALE_MC, 240, 630, 96, 144)
    maleCharacter = box.ImageButton(MALE_MC, 340, 630, 96, 144)

    usernameError = box.Error(ERROR, 900, 265, "Username already exists", 275, 34, 750, 205)
    matchError = box.Error(ERROR, 900, 365, "Passwords do not match", 265, 34, 750, 305)
    characterError = box.Error(ERROR, 900, 470, "Password must be over 8 characters and must include lowercase, uppercase and a number", 970, 34, 100, 405)
    noNameError = box.Error(ERROR, 900, 265, "You must enter a name", 275, 34, 750, 205)
    chosenCharacterError = box.Error(ERROR, 150, 630, "You must choose a character", 310, 34, 20, 570)

    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # dislpays all elements
        for button in [backButton, startButton, speedButton]:

            # checks to see if the user is hovering over a button, which will change how it is drawn
            button.checkHover(mouse)
            button.draw()

        for textbox in [titleBox, nameLabel, passwordLabel, save3Label]:
            textbox.draw()

        for inputbox in [nameInputBox, password1InputBox, password2InputBox]:

            # checks to see if the user is hovering over a box or has clicked on it, which will change how it is drawn
            inputbox.checkHoverOrClick(mouse)
            inputbox.draw()
        
        for character in [femaleCharacter, maleCharacter]:

            # checks to see if the character image has been clicked on, and draws it differently depending on it
            if character.checkActive() == True:
                character.draw()
                character.drawBox()
            else:
                character.checkHover(mouse)
                character.draw()
        
        for error in [usernameError, matchError, characterError, noNameError, chosenCharacterError]:

            # checks to see if each error has been activated so it can be displayed
            if error.checkActive() == True:
                error.checkHover(mouse)
                error.draw()
        
        for label in [modeLabel, characterLabel]:
            label.draw()

        # handles user interaction
        for event in pygame.event.get():

            # checks to see if the user has clicked on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                if backButton.onClick(mouse):
                        newgame1_loop()
                
                # checks to see if an input box has been clicked, and draws it differently depending on it
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
                
                # checks to see if a character image has been clicked, and draws it differently depending on it
                if femaleCharacter.onClick(mouse):
                    chosenCharacter = "Female"
                    femaleCharacter.activate()
                    maleCharacter.deactivate()
                
                if maleCharacter.onClick(mouse):
                    chosenCharacter = "Male"
                    maleCharacter.activate()
                    femaleCharacter.deactivate()
                
                # changes the speed between fast and slow when the user clicks on the button
                if speedButton.onClick(mouse):
                    if speedButton.getText() == "Slow":
                        speed = "Fast"
                        speedButton.changeText("Fast")
                    elif speedButton.getText() == "Fast":
                        speed = "Slow"
                        speedButton.changeText("Slow")

                # checks if the user clicks on the start button
                if startButton.onClick(mouse):
                    
                    # sends the 2 passwords inputted into a function, along with the errors, and checks to see if it is valid
                    correctPassword = checkNewPassword(password1, password2, matchError, characterError)

                    # this gets the user's input in the name input box
                    username = nameInputBox.getText()

                    # checks to see if the user has chosen a character, and displays an error message if not
                    if chosenCharacter == "":
                        chosenCharacterError.activate()
                    else:
                        chosenCharacterError.deactivate()

                    # checks to see if the user has inputted a name, and activates an error message if not
                    if username == "":
                        noNameError.activate()
                    else:
                        noNameError.deactivate()

                        #  checks to see if the name inputted already exists
                        validName = database.checkUsername(str(username))
                    

                    if validName:
                        usernameError.deactivate()
                    else:
                        usernameError.activate()

                    # this happens when all the conditions needed to create a new save has been fulfilled
                    if correctPassword and chosenCharacter != "" and validName:

                        # applies the hashing function on the user's password
                        passwordHash = hashing(password1)

                        # this creates a new save in the database using the information inputted
                        database.create_newsave(username, passwordHash, saveChoice)

                        game.createNewSave(saveChoice, username, chosenCharacter, speed)
                        game.loadTheGame(saveChoice)

            # checks to see if the user has pressed a key
            if event.type == pygame.KEYDOWN: 
                
                # checks to see if any of the input boxes are active to type in
                if nameInputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # deletes the last character in the variable
                        name = name[:-1] 

                    # checks to see if the length of the variable does not exceed the boundary
                    elif len(name) <= 11: 
                        name += event.unicode
                    
                    # updates the text that is displayed in the input box on the screen
                    nameInputBox.changeText(name)
                
                # checks to see if any of the input boxes are active to type in
                if password1InputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # deletes the last character in the variables
                        password1 = password1[:-1] 
                        password1Display = password1Display[:-1]

                    # checks to see if the length of the variable does not exceed the boundary
                    elif len(password1) <= 11: 
                        password1 += event.unicode
                        
                    # updates the text that is displayed in the input box on the screen
                    password1Display = "*" * len(password1)
                    password1InputBox.changeText(password1Display)
                
                # checks to see if any of the input boxes are active to type in
                if password2InputBox.checkActive():

                    if event.key == pygame.K_BACKSPACE: 
        
                        # deletes the last character in the variables 
                        password2 = password2[:-1] 
                        password2Display = password2Display[:-1]

                    # checks to see if the length of the variable does not exceed the boundary
                    elif len(password2) <= 11: 
                        password2 += event.unicode
                    
                    # updates the text that is displayed in the input box on the screen
                    password2Display = "*" * len(password2)
                    password2InputBox.changeText(password2Display)
                            
            # exits program if user clicks on exit button (pygame.QUIT)
            if event.type == pygame.QUIT:
                running = False

        # update the display
        pygame.display.flip()
        
        # control frame rate
        CLOCK.tick(60)

    # Cleanly exit the program
    pygame.quit()
    sys.exit()

# handles the first screen that is displayed when the user clicks on new game        
def loadgame_loop():

    running = True

    # loads the error image 
    ERROR = pygame.transform.scale(pygame.image.load('Resources/Images/Menu/error-icon.png'), (55, 48))

    # save choice stores the save as an object and user choice stores the save as an integer
    saveChoice = -1
    userChoice = -1

    # stores the user's input for the password in a variable
    password = ""

    # this is the placeholder text that is displayed on the input box as a prompt for the user
    passwordDisplay = "Enter Password"
    
    # gets the usernames of all 3 saves and stores it in a list called save
    save = database.getUsernames()

    # replaces all "Null" saves with "no save" for displaying
    save = [('no save',) if save[0] == 'NULL' else save for save in save]

    # creation of objects
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Load Game")

    backButton = box.Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    tickButton = box.Button( (WIDTH-30-90) , (HEIGHT-30-70) , 90, 70, OCR_TITLE, "->")

    save1Label = box.TextBox(230, 240, 280, 80, OCR_TEXT, "Save 1:")
    save2Label = box.TextBox(230, 350, 280, 80, OCR_TEXT, "Save 2:")
    save3Label = box.TextBox(230, 460, 280, 80, OCR_TEXT, "Save 3:")

    save1Content = box.Button(570, 240, 280, 80, OCR_TEXT, save[0][0])
    save2Content = box.Button(570, 350, 280, 80, OCR_TEXT, save[1][0])
    save3Content = box.Button(570, 460, 280, 80, OCR_TEXT, save[2][0])

    passwordInputBox = box.InputBox(WIDTH // 2 - (320 // 2), 580, 340, 80, OCR_TEXT, passwordDisplay)

    passwordError = box.Error(ERROR, 320, 620, "Password is incorrect", 275, 34, 190, 560)
    noNameError = box.Error(ERROR, 320, 620, "No existing save", 205, 34, 220, 560)
    
    # this sets the placeholder text in the box to grey from the original green
    passwordInputBox.changeColour(GREY)

    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # dislpays all elements
        for textbox in [titleBox, save1Label, save2Label, save3Label]:
            textbox.draw()

        for button in [backButton, tickButton, save1Content, save2Content, save3Content]:

            # checks to see if the button drawn is the chosen save, and draws it differently depending on it
            if button == saveChoice:
                button.draw()
            else:
                
                # checks to see if the user is hovering over the buttton before drawing it
                button.checkHover(mouse)
                button.draw()

        for inputbox in [passwordInputBox]:
            
            # checks to see if the user has clicked or is hovering over a box before displaying it
            inputbox.checkHoverOrClick(mouse)
            inputbox.draw()
        
        for error in [passwordError, noNameError]:

            # checks to see if there is an error in the users password
            if error.checkActive() == True:
                error.checkHover(mouse)
                error.draw()

        # handles user interaction
        for event in pygame.event.get():

            # checks to see if the user clicks on a button on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                # this will bring the user back to the initial screen
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

                # checks to see if the user has clicked on the inputbox or not
                if passwordInputBox.onClick(mouse):
                    passwordInputBox.activate()
                else:
                    passwordInputBox.deactivate()

                # this checks to see if the password matches the password hash saved in the database for that particular save
                if tickButton.onClick(mouse):

                    # this checks to see if the user has entered a password
                    if password != "" and userChoice != -1:

                        # checks to see if the save the user chose has a save stored in it or not
                        if save[userChoice-1][0] == "no save":

                            # displays different error on screen
                            passwordError.deactivate()
                            noNameError.activate()

                        else:

                            # hashes the password
                            passwordHash = hashing(password)

                            # checks to see if the password matches the hashed one save
                            correct = database.checkPassword(userChoice, passwordHash)

                            if correct:
                                game.loadTheGame(userChoice)
                            else:
                                passwordError.activate()
            
            # checks if the user has pressed a key down
            if event.type == pygame.KEYDOWN: 
                
                # checks to see if the input box has been clicked on for the user to type on
                if passwordInputBox.checkActive():

                    # changes the colour of the text in the input box from grey to green
                    passwordInputBox.changeColour(FONT_COLOUR)

                    if event.key == pygame.K_BACKSPACE: 
        
                        # deletes the last character in the variable password 
                        password = password[:-1] 

                    # checks to see if the password inputted has reached the character limit
                    elif len(password) <= 11: 

                        # stores the characters entered
                        password += event.unicode
                    
                    # this creates the censored version of the password that is displayed to the user
                    passwordDisplay = "*" * len(password)
                    passwordInputBox.changeText(passwordDisplay)

            # exits program if user clicks on exit button (pygame.QUIT)
            if event.type == pygame.QUIT:
                running = False

        # update the display
        pygame.display.flip()
        
        # control frame rate
        CLOCK.tick(60)

    # Cleanly exit the program
    pygame.quit()
    sys.exit()

# handles the instructions screen 
def instructions_loop(fromGame=False, player=False):

    running = True

    # creation of objects
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "How to Play")
    backButton = box.Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    nextButton = box.Button(900, 610, 150, 50, OCR_ERROR, "Next page" )


    instruction1 = box.TextBox(300, 290, 170, 40, OCR_ERROR, "Move player")
    instruction2 = box.TextBox(220, 430, 280, 40, OCR_ERROR, "Open / close inventory")
    instruction3 = box.TextBox(220, 540, 270, 40, OCR_ERROR, "Use item / interact")
    instruction4 = box.TextBox(710, 280, 280, 40, OCR_ERROR, "Change inventory slot")
    instruction5 = box.TextBox(750, 430, 70, 40, OCR_ERROR, "Run")
    instruction6 = box.TextBox(710, 540, 210, 40, OCR_ERROR, "Pause / Unpause")
    
    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        SCREEN.blit(W_IMG, (150, 255))
        SCREEN.blit(A_IMG, (95, 310))
        SCREEN.blit(S_IMG, (150, 310))
        SCREEN.blit(D_IMG, (205, 310))

        SCREEN.blit(E_IMG, (120, 420))

        SCREEN.blit(X_IMG, (120, 530))

        SCREEN.blit(ZERO_IMG, (570, 270))
        SCREEN.blit(NINE_IMG, (640, 270))

        SCREEN.blit(SHIFT_IMG, (570, 420))

        SCREEN.blit(ESC_IMG, (570, 535))
        

        # displays all elements
        for textBox in [titleBox, instruction1, instruction2, instruction3, instruction4, instruction5, instruction6]:
          textBox.draw()

        for button in [backButton, nextButton]:

            # checks to see if the user's mouse is hovering over the button
            button.checkHover(mouse)
            button.draw()
        
        # handles user interaction
        for event in pygame.event.get():

            # checks to see if the user has clicked on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                # this goes back to the main menu screen if the back button is clicked on
                if backButton.onClick(mouse):
                    if fromGame:
                        game.pauseScreen(player)
                    else:
                        mainmenu_loop()
                if nextButton.onClick(mouse):
                    instructions_loop2(True, player)

            # exits program if user clicks on exit button (pygame.QUIT)
            if event.type == pygame.QUIT:
                running = False

        # update the display
        pygame.display.flip()
        
        # control frame rate
        CLOCK.tick(60)

    # Cleanly exit the program
    pygame.quit()
    sys.exit()

# handles the instructions screen 
def instructions_loop2(fromGame=False, player=False):

    running = True

    # creation of objects
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "How to Play")
    backButton = box.Button(30, 30, 90, 70, OCR_TITLE, "<-"  )
    
    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # displays all elements
        for textBox in [titleBox]:
          textBox.draw()

        for button in [backButton]:

            # checks to see if the user's mouse is hovering over the button
            button.checkHover(mouse)
            button.draw()
        
        # handles user interaction
        for event in pygame.event.get():

            # checks to see if the user has clicked on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                # this goes back to the main menu screen if the back button is clicked on
                if backButton.onClick(mouse):
                    if fromGame:
                        instructions_loop(True, player)
                    else:
                        instructions_loop()

            # exits program if user clicks on exit button (pygame.QUIT)
            if event.type == pygame.QUIT:
                running = False

        # update the display
        pygame.display.flip()
        
        # control frame rate
        CLOCK.tick(60)

    # Cleanly exit the program
    pygame.quit()
    sys.exit()

# handles the settings screen and the functions within
def settings_loop(fromGame=False, player=False):

    running = True

    global musicVal, sfxVal

    # creation of objects
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Settings")

    backButton = box.Button(30, 30, 90, 70, OCR_TITLE, "<-"  )

    musicLabel = box.TextBox(160, 250, 320, 70, OCR_TEXT, "Music")
    sfxLabel = box.TextBox(160, 390, 320, 70, OCR_TEXT, "Sound Effects")

    minusMusicButton = box.Button(570, 250, 90, 70, OCR_TITLE, "-"  )
    addMusicButton = box.Button(850, 250, 90, 70, OCR_TITLE, "+"  )
    minusSfxButton = box.Button(570, 390, 90, 70, OCR_TITLE, "-"  )
    addSfxButton = box.Button(850, 390, 90, 70, OCR_TITLE, "+"  )

    musicNum = box.TextBox(710, 250, 90, 70, OCR_TITLE, str(musicVal)  )
    sfxNum = box.TextBox(710, 390, 90, 70, OCR_TITLE, str(sfxVal)  )

    while running:

        # displays menu image background
        SCREEN.blit(MENU_BG, (0, 0))

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # displays all elements
        for button in [backButton, minusMusicButton, addMusicButton, minusSfxButton, addSfxButton ]:

            # checks to see if the user's mouse is hovering over a button, which will draw it differently
            button.checkHover(mouse)
            button.draw()
        
        for textbox in [titleBox, musicLabel, sfxLabel, musicNum, sfxNum]:
            textbox.draw()
        
        # handles user interaction
        for event in pygame.event.get():

            # checks to see if the user has clicked on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:

                # this goes back to the main menu screen if the back button is clicked on
                if backButton.onClick(mouse):
                    if fromGame:
                        game.pauseScreen(player)
                    else:
                        mainmenu_loop()

                # checks to see if the user clicked on the minus music button
                if minusMusicButton.onClick(mouse):

                    # this gets the current sound volume of the music
                    musicVal = int(musicNum.getText())

                    # ensures the lowest music volume is 0
                    if musicVal > 0:

                        # decreases the volume of the music
                        musicVal -= 1
                        pygame.mixer.music.set_volume(musicVal / 10)

                        # changes the volume value displayed
                        musicNum.changeText(musicVal)
                
                # checks to see if the user clicked on the add music button
                if addMusicButton.onClick(mouse):

                    # this gets the current sound volume of the music
                    musicVal = int(musicNum.getText())

                    # ensures the music volume does not exceed 10
                    if musicVal < 10:

                        # increases the volume of the music
                        musicVal += 1
                        pygame.mixer.music.set_volume(musicVal / 10)

                        # changes the volume value displayed
                        musicNum.changeText(musicVal)
                
                # checks to see if the user clicked on the minus sound effects button
                if minusSfxButton.onClick(mouse):

                    # this gets the current sound volume of the music
                    sfxVal = int(sfxNum.getText())

                    # ensures the sound effects volume is not lower than 0
                    if sfxVal > 0:

                        # decreases the volume of the sound effects
                        sfxVal -= 1
                        for effect in [button1, button2]:
                            effect.set_volume(sfxVal / 10)

                        # changes the volume value displayed
                        sfxNum.changeText(sfxVal)
                    
                # checks to see if the user clicked on the add sound effects button
                if addSfxButton.onClick(mouse):

                    # this gets the current sound volume of the music
                    sfxVal = int(sfxNum.getText())

                    # ensures the volume of the sound effects does not exceed 10
                    if sfxVal < 10:

                        # increases the volume of the sound effects
                        sfxVal += 1
                        for effect in [button1, button2]:
                            effect.set_volume(sfxVal / 10)
                        
                        # changes the volume value displayed
                        sfxNum.changeText(sfxVal)

            # exits program if user clicks on exit button (pygame.QUIT)
            if event.type == pygame.QUIT:
                running = False

        # update the display
        pygame.display.flip()
        
        # control frame rate
        CLOCK.tick(60)

    # Cleanly exit the program
    pygame.quit()
    sys.exit()