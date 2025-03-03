import pygame
from config import *
import sys
import Player
import tile
import random, town
import numpy as np

weather = 0
lastUpdatedDay = 0

def renderTime(player):

    global elapsedRealTime, weather, lastUpdatedDay

    # Get the time elapsed since the last frame in milliseconds
    deltaTime = CLOCK.get_time()
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
