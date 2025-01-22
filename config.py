# imports and initialise the pygame library, and oher libraries used and needed in program

import pygame
from spritesheet import SpriteSheet
pygame.init()

# dimensions of screen
WIDTH = 1080
HEIGHT = 720

# dimensions of the title box
TITLE_WIDTH = 450
TITLE_HEIGHT = 90

# colours
BOX_OUTLINE = (91,164,211)
WHITE = (255,255,255)
BOX_FILL = (211, 245, 253)
FONT_COLOUR = (2, 100, 106)
ERROR_FONT_COLOUR = (255, 45, 45)
GREY = (160, 160, 160)
DARK_GREY = (70, 70, 70)
BLACK = (0, 0, 0)
TEST = (0,0,70)

# text font
OCR_TITLE = pygame.font.Font('Resources/OCR.ttf', 48)
OCR_TEXT = pygame.font.Font('Resources/OCR.ttf', 38)
OCR_ERROR = pygame.font.Font('Resources/OCR.ttf', 20)
OCR_INVENTORY = pygame.font.Font('Resources/OCR.ttf', 15)

# images 
MENU_BG = pygame.transform.scale(pygame.image.load('Resources/Images/Menu/menu-background.png'), (WIDTH, HEIGHT))

BL_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 0)
TL_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 270)
BR_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 90)
TR_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass corner.png'), 180)

BE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 90)
TE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 270)
LE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 0)
RE_TILE = pygame.transform.rotate(pygame.image.load('Resources/Images/tiles/grass edge.png'), 180) 

GM_TILE = pygame.image.load('Resources/Images/tiles/grass middle.png') 
DE_TILE = pygame.image.load('Resources/Images/tiles/grass middle.png') 

TD_TILE = pygame.image.load('Resources/Images/tiles/tilled land.png') 
WD_TILE = pygame.image.load('Resources/Images/tiles/tilled and watered land.png') 

SLOT = pygame.image.load('Resources/Images/slot.png')
CHOSEN_SLOT = pygame.image.load('Resources/Images/chosenSlot.png')

TOP_SCREEN = pygame.transform.scale(pygame.image.load('Resources/Images/topscreen.png'), (200, 100))

POTATO_SHEET = pygame.image.load('Resources/Images/Crops/Spring/Potato.png')
TURNIP_SHEET = pygame.image.load('Resources/Images/Crops/Spring/Turnip.png')
ONION_SHEET = pygame.image.load('Resources/Images/Crops/Summer/Onion.png')
RADISH_SHEET = pygame.image.load('Resources/Images/Crops/Summer/Radish.png')
CARROT_SHEET = pygame.image.load('Resources/Images/Crops/Fall/Carrot.png')
SPINACH_SHEET = pygame.image.load('Resources/Images/Crops/Fall/Spinach.png')

# dictionary of tile images 
TILE_IMAGES = { "TL": TL_TILE, "TR": TR_TILE, "BL": BL_TILE, "BR": BR_TILE, "TE": TE_TILE, "LE": LE_TILE, "RE": RE_TILE, "BE": BE_TILE, "GM": GM_TILE, "DE": DE_TILE, "TD": TD_TILE, "WD": WD_TILE}

TILE_SIZE = 72

# music
musicVal = 0 # todo: set this to 5
sfxVal = 5

# sound effects
button1 = pygame.mixer.Sound('Resources/Sound-effects/cbutton3.mp3')
button2 = pygame.mixer.Sound('Resources/Sound-effects/cbutton4.mp3')

# screen
SCREEN = pygame.display.set_mode([WIDTH,HEIGHT])

CLOCK = pygame.time.Clock()

# load player sprite sheet
maleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()
femaleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/femaleMC-spritesheet.png").convert_alpha()
andreSpriteSheet = pygame.image.load("Resources/Images/sprites/andre-spritesheet.png").convert_alpha()
annabelleSpriteSheet = pygame.image.load("Resources/Images/sprites/annabelle-spritesheet.png").convert_alpha()
rosalineSpriteSheet = pygame.image.load("Resources/Images/sprites/rosaline-spritesheet.png").convert_alpha()
shaylaSpriteSheet = pygame.image.load("Resources/Images/sprites/shayla-spritesheet.png").convert_alpha()
wesleySpriteSheet = pygame.image.load("Resources/Images/sprites/wesley-spritesheet.png").convert_alpha()

HOE = pygame.transform.scale(pygame.image.load("Resources/Images/tools/Hoe.png").convert_alpha(), (36,36))
WATERCAN = pygame.transform.scale(pygame.image.load("Resources/Images/tools/Watering Can.png").convert_alpha(), (46,34))
SCYTHE = pygame.transform.scale(pygame.image.load("Resources/Images/tools/Scythe.png").convert_alpha(), (36,36))

potatoObject = SpriteSheet(POTATO_SHEET)
turnipObject = SpriteSheet(TURNIP_SHEET)
onionObject = SpriteSheet(ONION_SHEET)
radishObject = SpriteSheet(RADISH_SHEET)
carrotObject = SpriteSheet(CARROT_SHEET)
spinachObject = SpriteSheet(SPINACH_SHEET)

potatoList, turnipList, onionList, radishList, carrotList, spinachList = [], [], [], [], [], []

for x in range(2,5):
    potatoList.append(potatoObject.getImage(x, 0, 16, 32, 3)) 
for x in range(2,5):
    turnipList.append(turnipObject.getImage(x, 0, 16, 32, 3)) 
for x in range(2,5):
    onionList.append(onionObject.getImage(x, 0, 16, 32, 3)) 
for x in range(2,5):
    radishList.append(radishObject.getImage(x, 0, 16, 32, 3)) 
for x in range(2,5):
    carrotList.append(carrotObject.getImage(x, 0, 16, 32, 3)) 
for x in range(2,5):
    spinachList.append(spinachObject.getImage(x, 0, 16, 32, 3)) 

potatoGrowthStages = ["P1", "P1", "P2", "P2", "P3"]
turnipGrowthStages = ["P1", "P1", "P1", "P2", "P2", "P3"]
onionGrowthStages = ["P1", "P2", "P2", "P3"]
radishGrowthStages = ["P1", "P1", "P1", "P2", "P2", "P2", "P3"]
carrotGrowthStages = ["P1", "P1", "P2", "P2", "P2", "P2", "P3"]
spinachGrowthStages = ["P1", "P2", "P2", "P2", "P3"]

SEED_TO_CROPS = { "potato seed": potatoGrowthStages, "turnip seed": turnipGrowthStages, "onion seed": onionGrowthStages, "radish seed": radishGrowthStages, "carrot seed": carrotGrowthStages, "spinach seed": spinachGrowthStages, }

CROP_STAGES = { "P1": potatoList[0], "P2": potatoList[1], "P3": potatoList[2], "T1": turnipList[0], "T2": turnipList[1], "T3": turnipList[2], "O1": onionList[0], "O2": onionList[1], "O3": onionList[2], "R1": radishList[0], "R2": radishList[1], "R3": radishList[2], "C1": carrotList[0], "C2": carrotList[1], "C3": carrotList[2], "S1": spinachList[0], "S2": spinachList[1], "S3": spinachList[2]}

# In-game time configuration
START_HOUR = 6  # Start time is 6:00 AM
START_MINUTE = 0
DAY_DURATION = 15 * 60  # Total duration of a day in seconds (15 minutes)

# Tracks elapsed real time (in milliseconds)
elapsedRealTime = 0

# needed when starting up program
def initialise():

    # set up window
    pygame.display.set_caption('Arable Valley')

    # loads up music and plays it
    pygame.mixer.music.load('Resources/Music/music1.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0) # todo: set to 5

    # sets up sound effects
    for sounds in [button1, button2]:
        sounds.set_volume(0.5)
