# imports the pygame library, and other libraries used and needed in program
import pygame, database, config, menu

# initialises the pygame library so it can be used
pygame.init()

if __name__ == "__main__":

    # sets up and creates the database if it has not yet been created
    database.startupDatabase()

    # sets up sound / music 
    config.initialise()

    # calls the loops that displays the first screen
    menu.mainmenu_loop()