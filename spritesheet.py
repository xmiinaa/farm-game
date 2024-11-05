import pygame, config

class SpriteSheet():

    # initialises
    def __init__(self, image):
        self.sheet = image

    # gets and returns a specific image frame from spritesheet
    def getImage(self, frame, row, width, height, scale):

        # creates a surface for image to draw on
        image = pygame.Surface((width, height)).convert_alpha()

        # draws on part of spritesheet that has been requested
        image.blit(self.sheet, (0,0), ((frame*width), (row*height), width, height))

        # scales image accordingly
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # removes outer black background to make it transparent
        image.set_colorkey(config.BLACK)

        return image
    
    # creates a list of different sprite images
    def createSpriteFrameList(self, numFrames, row):

        list = []

        # repeats for each frame
        for x in range(numFrames):

            # adds that frame image to list
            list.append(self.getImage(x+1, row, 64, 64, 1.5))

        return list
    
    def createIdleList(self):

        list = []

        # repeats for 4 directions
        for x in range(4):

            # adds that frame image to list
            list.append(self.getImage(0, x, 64, 64, 1.5))
        
        return list
    
    def createAnimationList(self):

        playerWalkUp = self.createSpriteFrameList(8, 8)
        playerWalkLeft = self.createSpriteFrameList(8, 9)
        playerWalkDown = self.createSpriteFrameList(8, 10)
        playerWalkRight = self.createSpriteFrameList(8, 11)

        playerWalkList = [playerWalkUp, playerWalkLeft, playerWalkDown, playerWalkRight]

        playerTillWaterUp = self.createSpriteFrameList(7, 4)
        playerTillWaterLeft = self.createSpriteFrameList(7, 5)
        playerTillWaterDown = self.createSpriteFrameList(7, 5)
        playerTillWaterRight = self.createSpriteFrameList(7, 6)

        playerTillWaterList = [playerTillWaterUp, playerTillWaterLeft, playerTillWaterDown, playerTillWaterRight]

        playerPlantUp = self.createSpriteFrameList(5, 12)
        playerPlantLeft = self.createSpriteFrameList(5, 12)
        playerPlantDown = self.createSpriteFrameList(5, 12)
        playerPlantRight = self.createSpriteFrameList(5, 12)

        playerPlantList = [playerPlantUp, playerPlantLeft, playerPlantDown, playerPlantRight]

        return playerWalkList, playerTillWaterList, playerPlantList