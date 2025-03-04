# imports the pygame library, and oher libraries used and needed in program
import pygame, database, config, menu, farm

# initiailses the pygame library so it can be used
pygame.init()

if __name__ == "__main__":

    # sets up and creates the database if it has not yet been createdd
    database.startupDatabase()

    # sets up sound / music 
    config.initialise()

    # calls the loops that displdays the first screen
    menu.instructions_loop()