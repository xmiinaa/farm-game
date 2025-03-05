import pygame
from config import *
import sys
import Player
import tile, menu, farm, town
from Classes import box
import numpy as np

weather = 0
lastUpdatedDay = 0

def renderTime(player, skippedDay=False):

    global elapsedRealTime, weather, lastUpdatedDay

    # Get the time elapsed since the last frame in milliseconds
    deltaTime = CLOCK.get_time()

    elapsedRealTime += deltaTime

    # Convert real elapsed time into in-game time
    elapsedGameTime = (elapsedRealTime / 1000) * (24 * 60 * 60 / DAY_DURATION)  # Scale to a 24-hour day
    
    gameHour = (START_HOUR + int(elapsedGameTime // 3600)) % 24
    gameMinute = int((START_MINUTE + (elapsedGameTime % 3600) // 60) % 60)

    if skippedDay:

        # Get current in-game time in seconds
        currentGameTimeInSeconds = (gameHour * 3600) + (gameMinute * 60)

        # Target time is 6 AM next day in seconds (6 hours after midnight)
        targetTimeInSeconds = (24 * 3600) + (6 * 3600)  # Full day + 6 hours

        # Time difference to reach 6 AM the next day
        timeToSkipInSeconds = targetTimeInSeconds - currentGameTimeInSeconds

        # Convert game time to real-time milliseconds
        timeToSkipInMilliseconds = (timeToSkipInSeconds / (24 * 60 * 60)) * (DAY_DURATION * 1000)

        elapsedRealTime += timeToSkipInMilliseconds  # Add the exact time needed

    else:
        elapsedRealTime += deltaTime

        # Convert real elapsed time into in-game time
        elapsedGameTime = (elapsedRealTime / 1000) * (24 * 60 * 60 / DAY_DURATION)  # Scale to a 24-hour day
        gameHour = (START_HOUR + int(elapsedGameTime // 3600)) % 24
        gameMinute = int((START_MINUTE + (elapsedGameTime % 3600) // 60) % 60)

    # Convert real elapsed time to in-game days
    elapsedDays = int((elapsedRealTime / 1000) // DAY_DURATION)

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

    SCREEN.blit(TOP_SCREEN, (-10, -5))

    SCREEN.blit(timeSurface, (7, 5))
    SCREEN.blit(dateSurface, (267, 5))
    SCREEN.blit(moneySurface, (507, 5))
    SCREEN.blit(weatherSurface, (737, 5))

    pygame.draw.rect(SCREEN, DARK_GREY, pygame.Rect(-10, -5, 1100, 40), 1, 0)

    flag = False
    if gameHour == 6 and gameMinute == 00 and currentDay != lastUpdatedDay:
        newDay(SEASONS[currentSeason])
        lastUpdatedDay = currentDay
    

def newDay(currentSeason):
    global weather

    if currentSeason == "Spring":
        weather = np.random.choice([0,1,2], p=[0.3, 0.4, 0.3])
    elif currentSeason == "Summer":
        weather = np.random.choice([0,1,2], p=[0.3, 0.5, 0.2])
    elif currentSeason == "Autumn":
        weather = np.random.choice([0,1,2], p=[0.3, 0.3, 0.4])
    elif currentSeason == "Winter":
        weather = np.random.choice([0,1,2], p=[0.2, 0.2, 0.6])

    tile.itsanewDay(WEATHERS[weather])

    farmMap = tile.renderFarmMap()


# handles the game paused and gives options to the user
def pauseScreen(player):
    running = True

    # creation of objects
    titleBox = box.TextBox(WIDTH // 2 - (TITLE_WIDTH // 2), 100, TITLE_WIDTH, TITLE_HEIGHT, OCR_TITLE, "Pause")

    continueButton = box.Button(WIDTH // 2 - 140, 220, 300, 70, OCR_TEXT, "Continue")
    saveButton = box.Button(WIDTH // 2 - 140, 320, 300, 70, OCR_TEXT, "Save progress")
    quitButton = box.Button(WIDTH // 2 - 140, 420, 300, 70, OCR_TEXT, "Exit to menu")
    instructionsButton = box.Button(WIDTH // 2 - 140, 520, 300, 70, OCR_TEXT, "How To Play")
    settingsButton = box.Button(WIDTH // 2 - 140, 620, 300, 70, OCR_TEXT, "Settings")

    while running:

        # displays translucent background
        SCREEN.blit(PAUSE_SCREEN, (0, 0))

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

                if keys[pygame.K_ESCAPE]:
                    if player.getLocation() == "Farm":
                        farm.main()
                    elif player.getLocation() == "Town":
                        town.main(player)

            # checks to see if user clicks with the mosue, and calls the corresponding loop depending on the button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.onClick(mouse):
                    if player.getLocation() == "Farm":
                        farm.main()
                    elif player.getLocation() == "Town":
                        town.main(player)
                if quitButton.onClick(mouse):
                    menu.mainmenu_loop()
                if instructionsButton.onClick(mouse):
                    menu.instructions_loop()
                if settingsButton.onClick(mouse):
                    menu.settings_loop()
            
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