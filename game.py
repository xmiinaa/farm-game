# imports and initialise the pygame library, and oher libraries used and needed in program
import pygame
from config import *
import sys
from Player import *
import tile, menu, farm, town
from Classes import box
import numpy as np
import filesaving
import database

# sets up all global variables to 0 or constants from config.py
weather = 0
lastUpdatedDay = 0
gameHour = START_HOUR
gameMinute = START_MINUTE
currentDay = START_DATE
currentSeason = START_HOUR
dayDuration = DAY_DURATION * 60
tilemap = None

# displays information box on top of screen
def renderTime(player, skippedDay=False):

    global elapsedRealTime, weather, lastUpdatedDay, gameHour, gameMinute, dayDuration

    # Get the time elapsed since the last frame in milliseconds
    deltaTime = CLOCK.get_time()

    elapsedRealTime += deltaTime

    # Convert real elapsed time into in-game time
    elapsedGameTime = (elapsedRealTime / 1000) * (24 * 60 * 60 / dayDuration)  # Scale to a 24-hour day
    
    # calculates hour and minute
    gameHour = (START_HOUR + int(elapsedGameTime // 3600)) % 24
    gameMinute = int((START_MINUTE + (elapsedGameTime % 3600) // 60) % 60)

    # checks if the player went to bed to skip time
    if skippedDay:

        # Get current in-game time in seconds
        currentGameTimeInSeconds = (gameHour * 3600) + (gameMinute * 60)

        # Target time is 6 AM next day in seconds (6 hours after midnight)
        targetTimeInSeconds = (24 * 3600) + (6 * 3600)  # Full day + 6 hours

        # Time difference to reach 6 AM the next day
        timeToSkipInSeconds = targetTimeInSeconds - currentGameTimeInSeconds

        # Convert game time to real-time milliseconds
        timeToSkipInMilliseconds = (timeToSkipInSeconds / (24 * 60 * 60)) * (dayDuration * 1000)

        elapsedRealTime += timeToSkipInMilliseconds  # Add the exact time needed

    else:
        elapsedRealTime += deltaTime

        # Convert real elapsed time into in-game time
        elapsedGameTime = (elapsedRealTime / 1000) * (24 * 60 * 60 / dayDuration)  # Scale to a 24-hour day
        gameHour = (START_HOUR + int(elapsedGameTime // 3600)) % 24
        gameMinute = int((START_MINUTE + (elapsedGameTime % 3600) // 60) % 60)

    # Convert real elapsed time to in-game days
    elapsedDays = int((elapsedRealTime / 1000) // dayDuration)

    # Calculate the in-game date
    currentDay = int((START_DATE + elapsedDays) % 30)
    currentSeason = int((START_SEASON + (START_DATE + elapsedDays) // 30) % 4)

    money = player.getMoney()

    # Format in-game time as hh:mm
    timeString = f"Time: {gameHour:02}:{gameMinute:02}"
    dateString = f"Date: {SEASONS[currentSeason]} {currentDay}"
    moneyString = f"Money: {money}"
    weatherString = f"Weather: {WEATHERS[weather]}"

    # Render the time
    timeSurface = OCR_ERROR.render(timeString, True, (255, 255, 255))  # White text
    dateSurface = OCR_ERROR.render(dateString, True, (255, 255, 255))  # White text
    moneySurface = OCR_ERROR.render(moneyString, True, (255, 255, 255))  # White text
    weatherSurface = OCR_ERROR.render(weatherString, True, (255, 255, 255))  # White text

    # displays information on screen
    SCREEN.blit(TOP_SCREEN, (-10, -5))

    SCREEN.blit(timeSurface, (7, 5))
    SCREEN.blit(dateSurface, (267, 5))
    SCREEN.blit(moneySurface, (507, 5))
    SCREEN.blit(weatherSurface, (737, 5))

    pygame.draw.rect(SCREEN, DARK_GREY, pygame.Rect(-10, -5, 1100, 40), 1, 0)

    # checks if it is a new day
    if gameHour == 6 and gameMinute == 00 and currentDay != lastUpdatedDay:
        newDay(SEASONS[currentSeason])
        lastUpdatedDay = currentDay

# creates a new empty save of the game filling in defaeult data in json file
def createNewSave(saveNo, name, gender, speed):

    # checks the speed chosen and edits value of dayDuration as a result
    if speed == "Slow":
        dayDuration = 15 * 60
    elif speed == "Fast":
        dayDuration = 10 * 60

    # creates default inventory as a dictionary
    inventory = {0: ['potato seed', 5], 1: ['onion seed', 5], 2: [None, 0], 3: [None, 0], 4: [None, 0], 5: [None, 0], 6: [None, 0], 7: ['hoe', 1], 8: ['waterCan', 1], 9: ['scythe', 1], 10: [None, 0], 11: [None, 0], 12: [None, 0], 13: [None, 0], 14: [None, 0], 15: [None, 0], 16: [None, 0], 17: [None, 0], 18: [None, 0], 19: [None, 0], 20: [None, 0], 21: [None, 0], 22: [None, 0], 23: [None, 0], 24: [None, 0], 25: [None, 0], 26: [None, 0], 27: [None, 0], 28: [None, 0], 29: [None, 0], 30: [None, 0], 31: [None, 0], 32: [None, 0], 33: [None, 0], 34: [None, 0], 35: [None, 0], 36: [None, 0], 37: [None, 0], 38: [None, 0], 39: [None, 0]}
    
    # 2D array storing whole tilemap status
    tilemap = [
    [["TL", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TR", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["DE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["DE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["XX", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["BL", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BR", None, None]] ]

    # saves information to json file
    filesaving.saveGame(saveNo, name , 540, 360, 0, 0, 1000, "Farm", gender, inventory, tilemap, 1, "Spring", 6, 0, 0, dayDuration, 0)

# saves users current progress in the game to a json file
def saveTheGame(player):

    global elapsedRealTime, weather, gameHour, gameMinute, currentDay, currentSeason, dayDuration, tilemap

    # gets the save number which the player is using by searching with username
    saveNo = database.getSaveNo(player.getName())

    # gets information to save
    playerX, playerY = player.getPosition()
    cameraPos = player.getMapPos()
    name = player.getName()
    money = player.getMoney()
    location = player.getLocation()
    gender = player.getGender()
    inventory = player.inventory.dictionary()

    weather = int(weather)

    day = currentDay
    season = currentSeason
    hour = gameHour
    minute = gameMinute

    # updates json file with save information
    filesaving.saveGame(saveNo, name , playerX, playerY, cameraPos[0], cameraPos[1], money, location, gender, inventory, tilemap, day, season, hour, minute, weather, dayDuration, elapsedRealTime)

# loads the player's progress from the json file into the game
def loadTheGame(saveNo):

    global elapsedRealTime, weather, gameHour, gameMinute, currentDay, currentSeason, dayDuration, tilemap

    # gets the data from the json file as a dictionary
    data = filesaving.loadGame(saveNo)

    # gets each component of data
    name = data.get("name", None)
    playerX = data.get("playerX", None)
    playerY = data.get("playerY", None)
    cameraX = data.get("cameraX", None)
    cameraY = data.get("cameraY", None)
    money = data.get("money", None)
    location = data.get("location", None)
    gender = data.get("gender", None)
    invent = data.get("inventory", None)
    tilemap = data.get("tilemap", None)
    currentDay = data.get("day", None)
    currentSeason = data.get("season", None)
    gameHour = data.get("hour", None)
    gameMinute = data.get("minute", None)
    weather = data.get("weather", None)
    dayDuration = data.get("dayDuration", None)
    elapsedRealTime = data.get("elapsedRealTime", None)

    # creates the player object using data collected
    if gender == "Male":
        player = Player(playerX, playerY, maleMCSpriteSheet, name, gender)
    elif gender == "Female":
        player = Player(playerX, playerY, femaleMCSpriteSheet, name, gender)
    
    # sets up more game systems 
    player.inventory.setUpInventory(invent)
    player.changeMapPos(cameraX, cameraY)
    player.setMoney(money)
    player.setLocation(location)

    # calls either the farm or town function depending on which location the player was last at
    if location == "Farm":
        farm.main(player)
    elif location == "Town":
        town.main(player)
    
# updates data when it is 6:00am of a new day
def newDay(currentSeason):
    global weather

    # generates different weather with each season having different probabilities
    # 0 = Cloudy, 1 = Sunny, 2 = Rainy
    if currentSeason == "Spring":
        weather = np.random.choice([0,1,2], p=[0.3, 0.4, 0.3])
    elif currentSeason == "Summer":
        weather = np.random.choice([0,1,2], p=[0.3, 0.5, 0.2])
    elif currentSeason == "Autumn":
        weather = np.random.choice([0,1,2], p=[0.3, 0.3, 0.4])
    elif currentSeason == "Winter":
        weather = np.random.choice([0,1,2], p=[0.2, 0.2, 0.6])

    # updates tilemap with information
    tile.itsanewDay(WEATHERS[weather])

    # re-displays tilemap onto farmMap so it is up-to-date
    farmMap = tile.renderFarmMap()

# handles the game paused and gives options to the user
def pauseScreen(player):
    global elapsedRealTime

    running = True

    # creation of objects
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Paused")

    continueButton = box.Button(WIDTH // 2 - 160, 220, 320, 70, OCR_TEXT, "Continue")
    saveButton = box.Button(WIDTH // 2 - 160, 320, 320, 70, OCR_TEXT, "Save progress")
    quitButton = box.Button(WIDTH // 2 - 160, 420, 320, 70, OCR_TEXT, "Exit to menu")
    instructionsButton = box.Button(WIDTH // 2 - 160, 520, 320, 70, OCR_TEXT, "How To Play")
    settingsButton = box.Button(WIDTH // 2 - 160, 620, 320, 70, OCR_TEXT, "Settings")

    # checks which location the player is at and displays the map
    if player.getLocation() == "Farm":
        map = tile.renderFarmMap()
    elif player.getLocation() == "Town":
        map = town.renderTownMap()

    # gets co-ordinates of camera
    cameraPos = player.getMapPos()

    # displays NPCs if player is in the town
    if player.getLocation() == "Town":
        shayla.drawIdle()
        wesley.drawIdle()
        joan.drawIdle()
        andre.drawIdle()
        annabelle.drawIdle()

    # displays background tiles
    SCREEN.blit(map, (cameraPos[0]-180, cameraPos[1]-360))

    player.drawIdle() # displays player
        
    player.inventory.draw() # displayes player's hotbar

    renderTime(player) # displays information box at top of screen

    # displays translucent background
    for _ in range(2):
        SCREEN.blit(PAUSE_SCREEN, (-50, -50))

    while running:

        # the current position of the mouse is saved to a variable, mouse
        mouse = pygame.mouse.get_pos()

        # displays all elements
        titleBox.draw()

        for button in [continueButton, saveButton, quitButton, instructionsButton, settingsButton]:

            # checks to see if the user's mouse is hovering over the button, which will draw the object differently
            button.checkHover(mouse)
            button.draw()

        # handling user interaction
        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                # checks if the player is exiting the menu
                if keys[pygame.K_ESCAPE]:

                    # checks which location the player is at, and calls the corresponding main function
                    if player.getLocation() == "Farm":
                        farm.main(player)
                    elif player.getLocation() == "Town":
                        town.main(player)

            # checks to see if user clicks with the mosue, and calls the corresponding loop depending on the button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                # checks if the player is exiting the menu
                if continueButton.onClick(mouse):

                    # checks which location the player is at, and calls the corresponding main function
                    if player.getLocation() == "Farm":
                        farm.main(player)
                    elif player.getLocation() == "Town":
                        town.main(player)

                # saves user's progess in game
                if saveButton.onClick(mouse):
                    saveTheGame(player)
                
                # exits game and switches to main menu screen
                if quitButton.onClick(mouse):
                    menu.mainmenu_loop()

                # switches to instructions screen
                if instructionsButton.onClick(mouse):
                    menu.instructions_loop(True, player)
                
                # switches to settings screen
                if settingsButton.onClick(mouse):
                    menu.settings_loop(True, player)
            
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