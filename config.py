# imports and initialise the pygame library, and oher libraries used and needed in program

import pygame
pygame.init()

# dimensions of screen
WIDTH = 1080
HEIGHT = 720

# dimensions of the box
TITLE_WIDTH = 450
TITLE_HEIGHT = 90

# colours
BOX_OUTLINE = (91,164,211)
WHITE = (255,255,255)
BOX_FILL = (211, 245, 253)
FONT_COLOUR = (2, 100, 106)
ERROR_FONT_COLOUR = (255, 45, 45)
GREY = (160, 160, 160)

# text font
OCR_TITLE = pygame.font.Font('Resources/OCR.ttf', 48)
OCR_TEXT = pygame.font.Font('Resources/OCR.ttf', 38)
OCR_ERROR = pygame.font.Font('Resources/OCR.ttf', 20)

# images 
MENU_BG = pygame.transform.scale(pygame.image.load('Resources/Images/menu-background.png'), (WIDTH, HEIGHT))

BL_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 0)
TL_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 270)
BR_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 90)
TR_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 180)

TE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 90)
BE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 270)
LE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 0)
RE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 180) 

GM_TILE = pygame.image.load('Resources/Images/tiles/grass middle.png') 

# music
musicVal = 0 # todo: set this to 5
sfxVal = 5

# sound effects
button1 = pygame.mixer.Sound('Resources/Sound-effects/cbutton3.mp3')
button2 = pygame.mixer.Sound('Resources/Sound-effects/cbutton4.mp3')

# screen
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

CLOCK = pygame.time.Clock()

# needed when starting up program
def initialise():

    # set up window
    pygame.display.set_caption('THE Farm Game')

    # loads up music and plays it
    pygame.mixer.music.load('Resources/Music/music1.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0) # todo: set to 5

    # sets up sound effects
    for sounds in [button1, button2]:
        sounds.set_volume(0.5)
