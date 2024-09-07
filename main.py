# imports and initialise the pygame library, and oher libraries used and needed in program

import re, hashlib, pygame
import database, config, game, Classes.box as box, menu
pygame.init()

if __name__ == "__main__":
    database.startupDatabase()
    config.initialise()
    menu.mainmenu_loop()
    
pygame.quit()