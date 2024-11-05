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
    
    # creates a list of the different idle images for a sprite
    def createIdleList(self):

        list = []

        # repeats for 4 directions
        for x in range(4):

            # adds that frame image to list
            list.append(self.getImage(0, x, 64, 64, 1.5))
        
        return list
    
    # creates and stores each animtaion of a sprite in its 4 directions within 2D lists
    def createAnimationList(self):

        # creates list of each frame and stores in variable
        playerWalkUp = self.createSpriteFrameList(8, 8)
        playerWalkLeft = self.createSpriteFrameList(8, 9)
        playerWalkDown = self.createSpriteFrameList(8, 10)
        playerWalkRight = self.createSpriteFrameList(8, 11)

        # creates a 2d list storing 4 lists for 4 directions
        playerWalkList = [playerWalkUp, playerWalkLeft, playerWalkDown, playerWalkRight]

        # creates list of each frame and stores in variable
        playerTillWaterUp = self.createSpriteFrameList(7, 4)
        playerTillWaterLeft = self.createSpriteFrameList(7, 5)
        playerTillWaterDown = self.createSpriteFrameList(7, 5)
        playerTillWaterRight = self.createSpriteFrameList(7, 6)

        # creates a 2d list storing 4 lists for 4 directions
        playerTillWaterList = [playerTillWaterUp, playerTillWaterLeft, playerTillWaterDown, playerTillWaterRight]

        # creates list of each frame and stores in variable
        playerPlantUp = self.createSpriteFrameList(5, 12)
        playerPlantLeft = self.createSpriteFrameList(5, 12)
        playerPlantDown = self.createSpriteFrameList(5, 12)
        playerPlantRight = self.createSpriteFrameList(5, 12)
        
        # creates a 2d list storing 4 lists for 4 directions
        playerPlantList = [playerPlantUp, playerPlantLeft, playerPlantDown, playerPlantRight]

        return playerWalkList, playerTillWaterList, playerPlantList