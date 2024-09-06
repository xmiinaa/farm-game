# imports and initialise the pygame library, and oher libraries used and needed in program

import pygame
pygame.init()

# dimensions of screen
WIDTH = 1080
HEIGHT = 720

TITLE_WIDTH = 450
TITLE_HEIGHT = 90

# colours
BOX_OUTLINE = (91,164,211)
WHITE = (255,255,255)
BOX_FILL = (211, 245, 253)
FONT_COLOUR = (2, 100, 106)
ERROR_FONT_COLOUR = (255, 45, 45)

# text font
OCR_TITLE = pygame.font.Font('Resources/OCR.ttf', 48)
OCR_TEXT = pygame.font.Font('Resources/OCR.ttf', 38)
OCR_ERROR = pygame.font.Font('Resources/OCR.ttf', 20)

# images 
MENU_BG = pygame.transform.scale(pygame.image.load('Resources/Images/menu-background.png'), (WIDTH, HEIGHT))

# music
musicVal = 0 # todo: set this to 5
sfxVal = 5

# sound effects
button1 = pygame.mixer.Sound('Resources/Sound-effects/cbutton3.mp3')
button2 = pygame.mixer.Sound('Resources/Sound-effects/cbutton4.mp3')

# screen
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])