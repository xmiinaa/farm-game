import pygame
from config import *

class Box:

    # instance method
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.colourFill = BOX_FILL
        self.colourBorder = BOX_OUTLINE
        self.width = width
        self.height = height

    # displays box onto screen
    def draw(self):
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 3)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 2, 3)

class TextBox(Box):

    # instance method
    def __init__(self, x, y,  width, height, font, content):
       super().__init__(x, y, width, height) 
       self.font = font
       self.content = content
       self.fontColour = FONT_COLOUR
       self.text = font.render(self.content, True, self.fontColour)
       self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))

    # displays text box onto screen
    def draw(self): 

        # displays the box
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)

        # displays the text
        SCREEN.blit(self.text, (self.textRect) )   

    # getter method to access text inside text box
    def getText(self):
        return self.content

    # method to change text in text box
    def changeText(self, newText):
        self.content = str(newText)
        self.font = self.font
        self.text = self.font.render(self.content, True, self.fontColour)
        self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))
    
class Button(TextBox):

    # instance method
    def __init__(self, x, y,  width, height, font, text):
        super().__init__(x, y, width, height, font, text)

    # checks to see if mouse click was on button, and returns True if so
    def onClick(self, position):

        # checks if mouse position is in range of the button
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            button1.play()
            return True
        else:
            return False
    
    # dispalys button onto screen
    def draw(self):

        # displays box
        pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.x, self.y, self.width, self.height), 3, 10)
        
        # displays text
        SCREEN.blit(self.text, self.textRect )

    # changes colour of button border if user is hovering over it with the cursor
    def checkHover(self, position):

        # checks if mouse position is in range of the button
        if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
            self.colourBorder = WHITE
        else:
            self.colourBorder = BOX_OUTLINE

    # changes colour of button border (used when choice is made)    
    def choiceClick(self):
        self.colourBorder = WHITE

class InputBox(Button):

    # instance method
    def __init__(self, x, y,  width, height, font, text):
        super().__init__(x, y, width, height, font, text)
        self.active = False

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    # getter method to access the activation status of the input box
    def checkActive(self):
        return self.active
    
    # changes colour of the text
    def changeColour(self, newcolour):
        self.fontColour = newcolour
        self.text = self.font.render(self.content, True, self.fontColour)
        self.textRect = self.text.get_rect(center = (self.width // 2 + self.x, self.height // 2 + self.y))

    # changes colour of box border depending on if the user is hovering over the box or if they have clicked it
    def checkHoverOrClick(self, position):
        if self.active:
            self.colourBorder = WHITE
        else:
            # checks if mouse position is in range of the input box
            if position[0] in range(self.x, self.x + self.width) and position[1] in range(self.y, self.y + self.height):
                self.colourBorder = WHITE
            else:
                self.colourBorder = BOX_OUTLINE

class Error():

    # instance method
    def __init__(self, image, imageX, imageY, text, width, height, textX, textY):
        self.image = image
        self.imageX = imageX
        self.imageY = imageY
        self.width = width
        self.height = height
        self.active = False
        self.rect = self.image.get_rect(center = (self.imageX, self.imageY))
        self.textX = textX
        self.textY = textY
        self.content = str(text)
        self.fontColour = ERROR_FONT_COLOUR
        self.colourBorder = (190,0, 0)
        font = OCR_ERROR
        self.text = font.render(self.content, True, self.fontColour)
        self.colourFill = WHITE
        self.textRect = self.text.get_rect(center = (self.width // 2 + self.textX, self.height // 2 + self.textY))
        
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    # getter method to access the activation status
    def checkActive(self):
        return self.active
    
    def draw(self):
        SCREEN.blit(self.image, (self.rect))

    def checkHover(self, position):

        # checks if mouse position is in range of the button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):

            # displays box
            pygame.draw.rect(SCREEN, self.colourFill, pygame.Rect(self.textX, self.textY , self.width, self.height))
            pygame.draw.rect(SCREEN, self.colourBorder, pygame.Rect(self.textX, self.textY , self.width, self.height), 1, 0)
            
            # displays text
            SCREEN.blit(self.text, self.textRect)

class ImageButton():

    # instance method
    def __init__(self, image, x, y, width, height):
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.active = False
    
    # changes colour of button border if user has clicked on the box
    def onClick(self, position):

        # checks if mouse position is in range of the button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            button1.play()
            self.activate()
            return True
        else:
            return False
    
    # changes colour of button border if user is hovering over it with the cursor
    def checkHover(self, position):
        # checks if mouse position is in range of the button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.drawBox()
        else:
            SCREEN.blit(self.image, self.rect)

    # displays the error image
    def draw(self):
        SCREEN.blit(self.image, self.rect)
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    # getter method to access the activation status of the box
    def checkActive(self):
        return self.active
    
    # displays the text box with the error message
    def drawBox(self):
        pygame.draw.rect(SCREEN, (255,255,255, 0), pygame.Rect(self.rect.left, self.rect.top, self.width, self.height), 2, 3)

class Text():

    # instance method
    def __init__(self, content, font, colour, x, y):
        self.content = content
        self.font = font
        self.colour = colour
        self.x = x
        self.y = y
        self.text = font.render(self.content, True, self.colour)
    
    # displays text on screen
    def draw(self):
        SCREEN.blit(self.text, (self.x, self.y))