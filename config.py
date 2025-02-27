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

GM_GREEN = (121,170,127)

BROWN1 = (185,98,26)
BROWN2 = (190,104,33)
BROWN3 = (210,116,37)
BROWN4 = (221,115,26)

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

TOP_SCREEN = pygame.transform.scale(pygame.image.load('Resources/Images/topscreen.png'), (1100, 40))

# spritesheet for crops and its different stages (seed to final)
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

# load assets for player and npc houses

MCHouseTopWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/MCTopWall.png"), (72,72))
MCHouseBottomWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/MCWallBottom.png"), (72,72))
MCHouseMiddleFloor = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/MCfloor.png"), (72,72))

annaHouseTopWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/AnnaWallTop.png"), (72,72))
annaHouseBottomWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/AnnaWallBottom.png"), (72,72))
annaHouseMiddleFloor = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/AnnaFloor.png"), (72,72))

wesleyHouseTopWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/WesleyWallTop.png"), (72,72))
wesleyHouseBottomWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/WesleyWallBottom.png"), (72,72))
wesleyHouseMiddleFloor = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/WesleyFloor.png"), (72,72))

andreHouseTopWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/AndreWallTop.png"), (72,72))
andreHouseBottomWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/AndreWallBottom.png"), (72,72))
andreHouseMiddleFloor = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/AndreFloor.png"), (72,72))

shaylaHouseTopWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/ShaylaWallTop.png"), (72,72))
shaylaHouseBottomWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/ShaylaWallBottom.png"), (72,72))
shaylaHouseMiddleFloor = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/ShaylaFloor.png"), (72,72))

joanHouseTopWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/JoanWallTop.png"), (72,72))
joanHouseBottomWall = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/JoanWallBottom.png"), (72,72))
joanHouseMiddleFloor = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/JoanFloor.png"), (72,72))

window1 = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/window.png").convert_alpha(), (70,70))
window2 = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/window2.png").convert_alpha(), (70,70))


blueBed = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/bluebed.png").convert_alpha(), (60,100))
bigblueBed = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightbluebed.png").convert_alpha(), (95,125))
orangeBed = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkorangebed.png").convert_alpha(), (95,125))
redBed = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkredbed.png").convert_alpha(), (60,100))
darkpinkBed = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkpinkbed.png").convert_alpha(), (60,100))
lightpinkBed = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/pinkbed.png").convert_alpha(), (60,100))

MCDresser = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightdresser1.png").convert_alpha(), (40,46))
shaylaDresser = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkdresser1.png").convert_alpha(), (40,46))
annaDresser = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightdresser1.png").convert_alpha(), (40,46))
wesleyDresser = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkdresser2.png").convert_alpha(), (40,46))
andreDresser = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkgametable.png").convert_alpha(), (40,46))
joanDresser = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightdresser2.png").convert_alpha(), (40,46))

blueCurtains = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/purplecurtain.png").convert_alpha(), (80,80))
darkbeigeCurtains = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkbeigecurtain.png").convert_alpha(), (100,80))
darkredCurtains = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkredcurtain2.png").convert_alpha(), (100,80))
redCurtains = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/redcurtain.png").convert_alpha(), (80,80))
beigeCurtains = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/beigecurtain.png").convert_alpha(), (80,80))

bluecirclerug = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/bluecirclerug.png").convert_alpha(), (70,41))
bluesquarerug = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/bluesquarerug.png").convert_alpha(), (70,41))
pinkcirclerug = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/pinkcirclerug.png").convert_alpha(), (70,41))
pinksquarerug = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/pinksquarerug.png").convert_alpha(), (70,41))
redcirclerug = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/redcirclerug.png").convert_alpha(), (70,41))
orangecirclerug = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/orangecirclerug.png").convert_alpha(), (70,41))

flowepot = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/flowerpot.png").convert_alpha(), (14,34))

MCbookshelf = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightbigbookcase.png").convert_alpha(), (84,104))
darkdressingtable = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkdressingtable.png").convert_alpha(), (84,104))
lightdressingtable = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightdressingtable.png").convert_alpha(), (84,104))
redstool = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/darkredstool.png").convert_alpha(), (84,104))
smalllightbookcase = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/smalllightbookcase.png").convert_alpha(), (84,104))
MCbookshelf = pygame.transform.scale( pygame.image.load("Resources/Images/Houses/lightbigbookcase.png").convert_alpha(), (84,104))

# load player sprite sheet
maleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/maleMC-spritesheet.png").convert_alpha()
femaleMCSpriteSheet = pygame.image.load("Resources/Images/sprites/femaleMC-spritesheet.png").convert_alpha()
andreSpriteSheet = pygame.image.load("Resources/Images/sprites/andre-spritesheet.png").convert_alpha()
annabelleSpriteSheet = pygame.image.load("Resources/Images/sprites/annabelle-spritesheet.png").convert_alpha()
joanSpriteSheet = pygame.image.load("Resources/Images/sprites/rosaline-spritesheet.png").convert_alpha()
shaylaSpriteSheet = pygame.image.load("Resources/Images/sprites/shayla-spritesheet.png").convert_alpha()
wesleySpriteSheet = pygame.image.load("Resources/Images/sprites/wesley-spritesheet.png").convert_alpha()

HOE = pygame.transform.scale(pygame.image.load("Resources/Images/tools/Hoe.png").convert_alpha(), (36,36))
WATERCAN = pygame.transform.scale(pygame.image.load("Resources/Images/tools/Watering Can.png").convert_alpha(), (46,34))
SCYTHE = pygame.transform.scale(pygame.image.load("Resources/Images/tools/Scythe.png").convert_alpha(), (36,36))

# creates an object of each crop
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
turnipGrowthStages = ["T1", "T1", "T1", "T2", "T2", "T3"]
onionGrowthStages = ["O1", "O2", "O2", "O3"]
radishGrowthStages = ["R1", "R1", "R1", "R2", "R2", "R2", "R3"]
carrotGrowthStages = ["C1", "C1", "C2", "C2", "C2", "C2", "C3"]
spinachGrowthStages = ["S1", "S2", "S2", "S2", "S3"]

SEED_TO_CROP_STAGES = { "potato seed": potatoGrowthStages, "turnip seed": turnipGrowthStages, "onion seed": onionGrowthStages, "radish seed": radishGrowthStages, "carrot seed": carrotGrowthStages, "spinach seed": spinachGrowthStages, }

CROP_STAGES = { "P1": potatoList[0], "P2": potatoList[1], "P3": potatoList[2], "T1": turnipList[0], "T2": turnipList[1], "T3": turnipList[2], "O1": onionList[0], "O2": onionList[1], "O3": onionList[2], "R1": radishList[0], "R2": radishList[1], "R3": radishList[2], "C1": carrotList[0], "C2": carrotList[1], "C3": carrotList[2], "S1": spinachList[0], "S2": spinachList[1], "S3": spinachList[2]}

# In-game time configuration
START_HOUR = 5  # Start time is 6:00 AM
START_MINUTE = 0
DAY_DURATION = 0.5 * 60  # Total duration of a day in seconds (15 minutes)

START_DATE = 1 # first date in the game

SEASONS = ["Spring", "Summer", "Autumn", "Winter"]
START_SEASON = 0

WEATHERS = ["Cloudy", "Sunny", "Rainy"]


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
