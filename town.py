import pygame
from config import *
import game, sys, farm
from Player import *

# returns tile image of from a specific index of tilemap array
def getTileImg(tilemap, row, col):

    tile = tilemap[row][col][0] # accesses tile from array

    return TILE_IMAGES.get(tile, GM_TILE) # if key is not found, grass middle tile is returned

def renderAnnabelleHouse(): # x: 0 y: -300
    townMap.blit(annaHouseTopWall, (332, 132))
    townMap.blit(annaHouseTopWall, (404, 132))
    townMap.blit(annaHouseTopWall, (476, 132))
    townMap.blit(annaHouseTopWall, (548, 132))

    townMap.blit(annaHouseBottomWall, (332, 204))
    townMap.blit(annaHouseBottomWall, (404, 204))
    townMap.blit(annaHouseBottomWall, (476, 204))
    townMap.blit(annaHouseBottomWall, (548, 204))

    townMap.blit(annaHouseMiddleFloor, (332, 274))
    townMap.blit(annaHouseMiddleFloor, (404, 274))
    townMap.blit(annaHouseMiddleFloor, (476, 274))
    townMap.blit(annaHouseMiddleFloor, (548, 274))

    townMap.blit(annaHouseMiddleFloor, (332, 344))
    townMap.blit(annaHouseMiddleFloor, (404, 344))
    townMap.blit(annaHouseMiddleFloor, (476, 344))
    townMap.blit(annaHouseMiddleFloor, (548, 344))

    townMap.blit(annaHouseMiddleFloor, (332, 414))
    townMap.blit(annaHouseMiddleFloor, (404, 414))
    townMap.blit(annaHouseMiddleFloor, (476, 414))
    townMap.blit(annaHouseMiddleFloor, (548, 414))

    townMap.blit(window1, (430, 160))
    townMap.blit(beigeCurtains, (425, 155))
    townMap.blit(lightpinkBed, (340, 235))
    townMap.blit(annaDresser, (410, 245))
    townMap.blit(MCbookshelf, (525, 195))
    townMap.blit(pinksquarerug, (335, 340))
    townMap.blit(flowepot, (422, 220))

    pygame.draw.rect(townMap, BROWN1, pygame.Rect(330, 130, 292, 356), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(328, 128, 296, 360), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(326, 126, 300, 364), 2)
    pygame.draw.rect(townMap, BROWN4, pygame.Rect(324, 124, 304, 368), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(322, 122, 308, 372), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(320, 120, 312, 376), 2)
    pygame.draw.rect(townMap, BROWN1, pygame.Rect(318, 118, 316, 380), 2)

    pygame.draw.rect(townMap, GM_GREEN, pygame.Rect(422, 485, 100, 14))

def renderWesleyHouse(): # x: +800 y: -200
    townMap.blit(wesleyHouseTopWall, (1232, 232))
    townMap.blit(wesleyHouseTopWall, (1304, 232))
    townMap.blit(wesleyHouseTopWall, (1376, 232))
    townMap.blit(wesleyHouseTopWall, (1448, 232))

    townMap.blit(wesleyHouseBottomWall, (1232, 304))
    townMap.blit(wesleyHouseBottomWall, (1304, 304))
    townMap.blit(wesleyHouseBottomWall, (1376, 304))
    townMap.blit(wesleyHouseBottomWall, (1448, 304))

    townMap.blit(wesleyHouseMiddleFloor, (1232, 374))
    townMap.blit(wesleyHouseMiddleFloor, (1304, 374))
    townMap.blit(wesleyHouseMiddleFloor, (1376, 374))
    townMap.blit(wesleyHouseMiddleFloor, (1448, 374))

    townMap.blit(wesleyHouseMiddleFloor, (1232, 444))
    townMap.blit(wesleyHouseMiddleFloor, (1304, 444))
    townMap.blit(wesleyHouseMiddleFloor, (1376, 444))
    townMap.blit(wesleyHouseMiddleFloor, (1448, 444))

    townMap.blit(wesleyHouseMiddleFloor, (1232, 514))
    townMap.blit(wesleyHouseMiddleFloor, (1304, 514))
    townMap.blit(wesleyHouseMiddleFloor, (1376, 514))
    townMap.blit(wesleyHouseMiddleFloor, (1448, 514))

    townMap.blit(window2, (1330, 260))
    townMap.blit(darkredCurtains, (1315, 255))
    townMap.blit(orangeBed, (1240, 335))
    townMap.blit(wesleyDresser, (1340, 345))
    townMap.blit(MCbookshelf, (1425, 295))
    townMap.blit(orangecirclerug, (1252, 460))
    townMap.blit(flowepot, (1352, 320))

    pygame.draw.rect(townMap, BROWN1, pygame.Rect(1230, 230, 292, 356), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(1228, 228, 296, 360), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(1226, 226, 300, 364), 2)
    pygame.draw.rect(townMap, BROWN4, pygame.Rect(1224, 224, 304, 368), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(1222, 222, 308, 372), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(1220, 220, 312, 376), 2)
    pygame.draw.rect(townMap, BROWN1, pygame.Rect(1218, 218, 316, 380), 2)

    pygame.draw.rect(townMap, GM_GREEN, pygame.Rect(1322, 585, 100, 14))

def renderAndreHouse(): # x: +600 y: +500
    townMap.blit(andreHouseTopWall, (232, 832))
    townMap.blit(andreHouseTopWall, (304, 832))
    townMap.blit(andreHouseTopWall, (376, 832))
    townMap.blit(andreHouseTopWall, (448, 832))

    townMap.blit(andreHouseBottomWall, (232, 904))
    townMap.blit(andreHouseBottomWall, (304, 904))
    townMap.blit(andreHouseBottomWall, (376, 904))
    townMap.blit(andreHouseBottomWall, (448, 904))

    townMap.blit(andreHouseMiddleFloor, (232, 974))
    townMap.blit(andreHouseMiddleFloor, (304, 974))
    townMap.blit(andreHouseMiddleFloor, (376, 974))
    townMap.blit(andreHouseMiddleFloor, (448, 974))

    townMap.blit(andreHouseMiddleFloor, (232, 1044))
    townMap.blit(andreHouseMiddleFloor, (304, 1044))
    townMap.blit(andreHouseMiddleFloor, (376, 1044))
    townMap.blit(andreHouseMiddleFloor, (448, 1044))

    townMap.blit(andreHouseMiddleFloor, (232, 1114))
    townMap.blit(andreHouseMiddleFloor, (304, 1114))
    townMap.blit(andreHouseMiddleFloor, (376, 1114))
    townMap.blit(andreHouseMiddleFloor, (448, 1114))

    townMap.blit(window1, (330, 860))
    townMap.blit(redCurtains, (325, 855))
    townMap.blit(redBed, (240, 935))
    townMap.blit(andreDresser, (310, 945))
    townMap.blit(MCbookshelf, (425, 895))
    townMap.blit(redcirclerug, (235, 1040))
    townMap.blit(flowepot, (322, 920))

    pygame.draw.rect(townMap, BROWN1, pygame.Rect(230, 830, 292, 356), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(228, 828, 296, 360), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(226, 826, 300, 364), 2)
    pygame.draw.rect(townMap, BROWN4, pygame.Rect(224, 824, 304, 368), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(222, 822, 308, 372), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(220, 820, 312, 376), 2)
    pygame.draw.rect(townMap, BROWN1, pygame.Rect(218, 818, 316, 380), 2)

    pygame.draw.rect(townMap, GM_GREEN, pygame.Rect(322, 1185, 100, 14))

def renderShaylaHouse(): # x: +400 y: +300
    townMap.blit(shaylaHouseTopWall, (732, 632))
    townMap.blit(shaylaHouseTopWall, (804, 632))
    townMap.blit(shaylaHouseTopWall, (876, 632))
    townMap.blit(shaylaHouseTopWall, (948, 632))

    townMap.blit(shaylaHouseBottomWall, (732, 704))
    townMap.blit(shaylaHouseBottomWall, (804, 704))
    townMap.blit(shaylaHouseBottomWall, (876, 704))
    townMap.blit(shaylaHouseBottomWall, (948, 704))

    townMap.blit(shaylaHouseMiddleFloor, (732, 774))
    townMap.blit(shaylaHouseMiddleFloor, (804, 774))
    townMap.blit(shaylaHouseMiddleFloor, (876, 774))
    townMap.blit(shaylaHouseMiddleFloor, (948, 774))

    townMap.blit(shaylaHouseMiddleFloor, (732, 844))
    townMap.blit(shaylaHouseMiddleFloor, (804, 844))
    townMap.blit(shaylaHouseMiddleFloor, (876, 844))
    townMap.blit(shaylaHouseMiddleFloor, (948, 844))

    townMap.blit(shaylaHouseMiddleFloor, (732, 914))
    townMap.blit(shaylaHouseMiddleFloor, (804, 914))
    townMap.blit(shaylaHouseMiddleFloor, (876, 914))
    townMap.blit(shaylaHouseMiddleFloor, (948, 914))

    townMap.blit(window2, (830, 660))
    townMap.blit(darkbeigeCurtains, (815, 655))
    townMap.blit(darkpinkBed, (740, 735))
    townMap.blit(shaylaDresser, (810, 745))
    townMap.blit(MCbookshelf, (925, 695))
    townMap.blit(pinkcirclerug, (735, 840))
    townMap.blit(flowepot, (822, 720))

    pygame.draw.rect(townMap, BROWN1, pygame.Rect(730, 630, 292, 356), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(728, 628, 296, 360), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(726, 626, 300, 364), 2)
    pygame.draw.rect(townMap, BROWN4, pygame.Rect(724, 624, 304, 368), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(722, 622, 308, 372), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(720, 620, 312, 376), 2)
    pygame.draw.rect(townMap, BROWN1, pygame.Rect(718, 618, 316, 380), 2)

    pygame.draw.rect(townMap, GM_GREEN, pygame.Rect(822, 985, 100, 14))

def renderJoanHouse(): # x: +600 y: +500
    townMap.blit(joanHouseTopWall, (1332, 932))
    townMap.blit(joanHouseTopWall, (1404, 932))
    townMap.blit(joanHouseTopWall, (1476, 932))
    townMap.blit(joanHouseTopWall, (1548, 932))

    townMap.blit(joanHouseBottomWall, (1332, 1004))
    townMap.blit(joanHouseBottomWall, (1404, 1004))
    townMap.blit(joanHouseBottomWall, (1476, 1004))
    townMap.blit(joanHouseBottomWall, (1548, 1004))

    townMap.blit(joanHouseMiddleFloor, (1332, 1074))
    townMap.blit(joanHouseMiddleFloor, (1404, 1074))
    townMap.blit(joanHouseMiddleFloor, (1476, 1074))
    townMap.blit(joanHouseMiddleFloor, (1548, 1074))

    townMap.blit(joanHouseMiddleFloor, (1332, 1144))
    townMap.blit(joanHouseMiddleFloor, (1404, 1144))
    townMap.blit(joanHouseMiddleFloor, (1476, 1144))
    townMap.blit(joanHouseMiddleFloor, (1548, 1144))

    townMap.blit(joanHouseMiddleFloor, (1332, 1214))
    townMap.blit(joanHouseMiddleFloor, (1404, 1214))
    townMap.blit(joanHouseMiddleFloor, (1476, 1214))
    townMap.blit(joanHouseMiddleFloor, (1548, 1214))

    townMap.blit(window2, (1430, 960))
    townMap.blit(blueCurtains, (1425, 955))
    townMap.blit(bigblueBed, (1340, 1035))
    townMap.blit(joanDresser, (1440, 1045))
    townMap.blit(MCbookshelf, (1525, 995))
    townMap.blit(bluesquarerug, (1352, 1160))
    townMap.blit(flowepot, (1452, 1020))

    pygame.draw.rect(townMap, BROWN1, pygame.Rect(1330, 930, 292, 356), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(1328, 928, 296, 360), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(1326, 926, 300, 364), 2)
    pygame.draw.rect(townMap, BROWN4, pygame.Rect(1324, 924, 304, 368), 2)
    pygame.draw.rect(townMap, BROWN3, pygame.Rect(1322, 922, 308, 372), 2)
    pygame.draw.rect(townMap, BROWN2, pygame.Rect(1320, 920, 312, 376), 2)
    pygame.draw.rect(townMap, BROWN1, pygame.Rect(1318, 918, 316, 380), 2)

    pygame.draw.rect(townMap, GM_GREEN, pygame.Rect(1422, 1285, 100, 14))

# creates farm map screen
def renderTownMap():

    # displays tile images from tilemap onto surface
    for row in range(len(townTileMap)):
        for col in range(len(townTileMap[row])):

            tileImg = getTileImg(townTileMap, row, col) # gets image to display
            
            townMap.blit(tileImg, (col*72, row*72))
    
    renderAnnabelleHouse()
    renderWesleyHouse()
    renderAndreHouse()
    renderShaylaHouse()
    renderJoanHouse()
    
    return townMap

def checkEdgeOfTown(player):
    # gets the tile position of the player
    playerTileX, playerTileY = player.getTilePosition()

    if townTileMap[playerTileY][playerTileX][0] == "DE":
        return True
    else:
        return False

def main(player, fromFarm=False):

    player.setLocation("Town")

    # creates the farmMap
    townMap = renderTownMap()

    if fromFarm:
        player.changeMapPos(180, 0)
        player.setPosition(40, 300)

    # gets co-ordinates of camera
    cameraPos = player.getMapPos()

    keyPressed = ""
    mouseDrag = False
    slotItem = None

    running = True
    while running:

        # gets player direction
        direction = player.whichDirection()

        # gets co-ordinates of mouse
        mousePos = pygame.mouse.get_pos()

        # displays background tiles
        SCREEN.blit(townMap, (cameraPos[0]-180, cameraPos[1]-360))

        #print(player.getCoordinates())

        if checkEdgeOfTown(player) == True:
            farm.main(True)

        # checks if the player is moving and they are not in another action, and displays it appropiately if they are
        if player.isMoving() and player.isActive() == False:

            player.animateWalk()
            player.move()
        
        # displays the player in its idle state
        else:
            player.drawIdle()

        shayla.drawIdle()
        wesley.drawIdle()
        joan.drawIdle()
        andre.drawIdle()
        annabelle.drawIdle()

        x,y = player.getCoordinates()
        
        player.inventory.draw()
        player.inventory.hover(mousePos)

        if slotItem != None and mouseDrag: # checks to see if the player's mouse is holding an item
            player.inventory.displayItem(mousePos, slotItem) # displays item relative to player's mouse

        # displays time
        game.renderTime(player)

        for event in pygame.event.get():

            # checks if player presses down a key
            if event.type == pygame.KEYDOWN:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if player.inventory.isInventoryOpen() == False:

                    if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
                        player.setMoving(True)
        
                    if keys[pygame.K_a] and direction != 1:
                        player.changeDirection(1)

                    elif keys[pygame.K_d]:
                        player.changeDirection(3)

                    if keys[pygame.K_w]:
                        player.changeDirection(0)

                    elif keys[pygame.K_s]:
                        player.changeDirection(2)
                    
                    if keys[pygame.K_x]:

                        for npc in [shayla, wesley, joan, andre, annabelle]:
                            if npc.nearCharacter(x+200, y+400):
                                print(npc.getName())

                    if keys[pygame.K_LSHIFT]:
                        player.changeSpeed(6)
                    else:
                        player.changeSpeed(4)
                
                if keys[pygame.K_e]:
                    player.inventory.openCloseInventory()

                # checks to see if the user has pressed keys 1 to 0, changing the inventory slot if they have to the corresponding one
                if keys[pygame.K_1]:
                    player.inventory.changeSlot(0)
                if keys[pygame.K_2]:
                    player.inventory.changeSlot(1)
                if keys[pygame.K_3]:
                    player.inventory.changeSlot(2)
                if keys[pygame.K_4]:
                    player.inventory.changeSlot(3)
                if keys[pygame.K_5]:
                    player.inventory.changeSlot(4)
                if keys[pygame.K_6]:
                    player.inventory.changeSlot(5)
                if keys[pygame.K_7]:
                    player.inventory.changeSlot(6)
                if keys[pygame.K_8]:
                    player.inventory.changeSlot(7)
                if keys[pygame.K_9]:
                    player.inventory.changeSlot(8)
                if keys[pygame.K_0]:
                    player.inventory.changeSlot(9)
                        
            # checks if player is not pressing down a key
            if event.type == pygame.KEYUP:
                
                # collects all keys Boolean value of whether it has been pressed or not and stores in list
                keys = pygame.key.get_pressed()

                if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
                    player.setMoving(False)
    
            # checks if he player has clicked on the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    keyPressed = "mouse"

                    player.inventory.click(mousePos)

                    mouseDrag = True

                    # checks if inventory is open
                    if player.inventory.isInventoryOpen():
                        slotItem = player.inventory.getDragItem(mousePos) # gets item that player is holding on
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:

                    mouseDrag = False

                    if player.inventory.isInventoryOpen() and (slotItem != None or slotItem == 0):
                        player.inventory.swapItems(slotItem, mousePos)
                
            if event.type == pygame.MOUSEMOTION:  
                if mouseDrag:
                    if player.inventory.isInventoryOpen():
                            if slotItem != None or slotItem == 0:
                                player.inventory.dragDropItem(mousePos, slotItem)  

            # handles the exit of the game
            if event.type == pygame.QUIT:
                running  = False

                # exits the game
                pygame.quit()
                sys.exit() 
        
        # maintains framerate of game
        CLOCK.tick(60)
        pygame.display.update()


townMap = pygame.Surface((1800, 1440))
townTileMap = [
    [["TL", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TE", None, None], ["TR", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["DE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["DE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["LE", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["GM", None, None], ["RE", None, None]],
    [["BL", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BE", None, None], ["BR", None, None]] ]
