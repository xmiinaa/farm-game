import pygame
import sys
from config import *
from spritesheet import *

pygame.init()

# information about each type of item the player can have / interact with
class ItemType:
    def __init__(self, name, icon, price, value, stackSize=1): # default stack size = 1
        self.name = name
        self.icon = icon
        self.value = value
        self.price = price
        self.stackSize = stackSize
    
    def getPrice(self):
        return self.price
    
    def getValue(self):
        return self.value
    
    def getStackSize(self):
        return self.stackSize

# holds a quantity of an item
class ItemSlot:
    def __init__(self, num):
        self.type = None
        self.amount = 0
        self.width = 72
        self.height = 72

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        if num < 10:
            self.rect = pygame.Rect(((num*TILE_SIZE) + 180, 620), (self.width, self.height))
        
        elif 10 <= num < 16:
            self.rect = pygame.Rect( ( ( (num-7)*TILE_SIZE) + 108, 250), (self.width, self.height)) # how it is for now but will update and change when creating rest of inventory
        elif 16 <= num < 22:
            self.rect = pygame.Rect((((num-13)*TILE_SIZE) + 108, 322), (self.width, self.height))
        elif 22 <= num < 28:
            self.rect = pygame.Rect((((num-19)*TILE_SIZE) + 108, 394), (self.width, self.height))
        elif 28 <= num < 34:
            self.rect = pygame.Rect((((num-25)*TILE_SIZE) + 108, 466), (self.width, self.height))
        elif 34 <= num <= 40:
            self.rect = pygame.Rect((((num-31)*TILE_SIZE) + 108, 538), (self.width, self.height))

# has a certain number of slots for items.
class Inventory:

    # creates new inventory
    def __init__(self):
        self.capacity = 40 # there can only be 40 slots
        self.taken_slots = 9
        self.chosenSlot = 0
        
        # creates array of slots 
        self.slots = [ItemSlot(x) for x in range(self.capacity)]

        self.inventoryOpen = False

    
    # displays the inventory main 10 slots
    def draw(self):
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(178, 618, 724, 76), 2) # draws a black outline for inventory
        
        # loop to go through all 10 slots
        for slot in range(0,10):

            # checks to see if the slot is the one currently selected
            if slot == self.chosenSlot:
                SCREEN.blit(CHOSEN_SLOT, (self.slots[self.chosenSlot].rect.x, self.slots[self.chosenSlot].rect.y) ) # displays different image
            else:
                SCREEN.blit(SLOT, (self.slots[slot].rect.x, self.slots[slot].rect.y) ) # displays normal slot
            
            # checks to see if the slot has an item
            if self.slots[slot].type is not None:

                SCREEN.blit(self.slots[slot].type.icon, ((self.slots[slot].rect.centerx - self.slots[slot].type.icon.get_width() / 2, self.slots[slot].rect.centery - self.slots[slot].type.icon.get_height() / 2 + 2))) # displays item


                if self.slots[slot].amount > 1:
                    text = OCR_INVENTORY.render( str(self.slots[slot].amount), True, WHITE) # creates text version of quantity
                    SCREEN.blit(text, (self.slots[slot].rect.x + 5, self.slots[slot].rect.y + 4)) # displays text in top left corner
        
        if self.inventoryOpen:

            pygame.draw.rect(SCREEN, BLACK, pygame.Rect(322, 248, 436, 364), 2)

            # loop to go through all 10 slots
            for slot in range(11,41):
                slot -= 1

                # checks to see if the slot is the one currently selected
                if slot == self.chosenSlot:
                    SCREEN.blit(CHOSEN_SLOT, (self.slots[self.chosenSlot].rect.x, self.slots[self.chosenSlot].rect.y) ) # displays different image
                else:
                    SCREEN.blit(SLOT, (self.slots[slot].rect.x, self.slots[slot].rect.y) ) # displays normal slot
                
                # checks to see if the slot has an item
                if self.slots[slot].type is not None:

                    SCREEN.blit(self.slots[slot].type.icon, ((self.slots[slot].rect.centerx - self.slots[slot].type.icon.get_width() / 2, self.slots[slot].rect.centery - self.slots[slot].type.icon.get_height() / 2 + 2))) # displays item


                    if self.slots[slot].amount > 1:
                        text = OCR_INVENTORY.render( str(self.slots[slot].amount), True, WHITE) # creates text version of quantity
                        SCREEN.blit(text, (self.slots[slot].rect.x + 5, self.slots[slot].rect.y + 4)) # displays text in top left corner

    # changes currently chosen slot if user clicks correctly
    def click(self, mousePos):

        if self.inventoryOpen:
            num = 40
        else:
            num = 10

        for slot in range(num):

            # checks if mouse position is in range of slot
            if mousePos[0] in range(self.slots[slot].rect.x, self.slots[slot].rect.x + self.slots[slot].width) and mousePos[1] in range(self.slots[slot].rect.y, self.slots[slot].rect.y + self.slots[slot].height):
                self.changeSlot(slot)
    
    # changes the current slot / item held
    def changeSlot(self, newSlot):
        self.chosenSlot = newSlot
    
    # changes slot image when mouse is hovering over it to let user aware
    def hover(self, mousePos):

        if self.inventoryOpen:
            num = 40
        else:
            num = 10

        for slot in range(num):
            
            # checks if mouse position is in range of slot
            if mousePos[0] in range(self.slots[slot].rect.x, self.slots[slot].rect.x + self.slots[slot].width) and mousePos[1] in range(self.slots[slot].rect.y, self.slots[slot].rect.y + self.slots[slot].height):
                SCREEN.blit(CHOSEN_SLOT, (self.slots[slot].rect.x, self.slots[slot].rect.y)) # displays different slot
            
            # checks to see if the slot has an item
            if self.slots[slot].type is not None:

                SCREEN.blit(self.slots[slot].type.icon, ((self.slots[slot].rect.centerx - self.slots[slot].type.icon.get_width() / 2, self.slots[slot].rect.centery - self.slots[slot].type.icon.get_height() / 2 + 2))) # displays item

                if self.slots[slot].amount > 1:
                    text = OCR_INVENTORY.render( str(self.slots[slot].amount), True, WHITE) # creates text version of quantity
                    SCREEN.blit(text, (self.slots[slot].rect.x + 5, self.slots[slot].rect.y + 4)) # displays text in top left corner
    
    # returns the item name that the player is currently holding
    def getItem(self):
        if self.slots[self.chosenSlot].type == None:
            return "None"
        else: 
            return self.slots[self.chosenSlot].type.name
    
    def openCloseInventory(self):
        self.inventoryOpen = not self.inventoryOpen
    
    def isInventoryOpen(self):
        return self.inventoryOpen

    def getInventory(self):
        return self.slots

    def dragDropItem(self, mousePos, slot):
        if self.slots[slot].type != None:
            SCREEN.blit(self.slots[slot].type.icon, (mousePos[0] - self.slots[slot].type.icon.get_width() // 2, mousePos[1] - self.slots[slot].type.icon.get_height() // 2 + 2))
    
    def getDragItem(self, mousePos):
        slot = None
        for slot in range(40):
            if mousePos[0] in range(self.slots[slot].rect.x, self.slots[slot].rect.x + self.slots[slot].width) and mousePos[1] in range(self.slots[slot].rect.y, self.slots[slot].rect.y + self.slots[slot].height):
                return slot
        
    def displayItem(self, mousePos, slot):
        if self.slots[slot].type != None:
            SCREEN.blit(self.slots[slot].type.icon, (mousePos[0] - self.slots[slot].type.icon.get_width() // 2, mousePos[1] - self.slots[slot].type.icon.get_height() // 2 + 2))

    def swapItems(self, changeSlot, mousePos):
        swapSlot = None
        for slot in range(40):
            if mousePos[0] in range(self.slots[slot].rect.x, self.slots[slot].rect.x + self.slots[slot].width) and mousePos[1] in range(self.slots[slot].rect.y, self.slots[slot].rect.y + self.slots[slot].height):
                swapSlot = slot
        
        if swapSlot != None and changeSlot != None and self.slots[changeSlot].type != None:
            
            tempType = self.slots[changeSlot].type
            tempAmount = self.slots[changeSlot].amount
    
            self.slots[changeSlot].type = self.slots[swapSlot].type
            self.slots[changeSlot].amount = self.slots[swapSlot].amount
            
            self.slots[swapSlot].type = tempType
            self.slots[swapSlot].amount = tempAmount

    def initialiseInventory(self):
        # for now i am initiating the items here though it may change
        self.slots[7].type = hoe
        self.slots[7].amount = 1
        self.slots[8].type = waterCan 
        self.slots[8].amount = 1
        self.slots[9].type = scythe 
        self.slots[9].amount = 1

        self.slots[0].type = potatoSeed
        self.slots[0].amount = 5
        self.slots[2].type = onionSeed
        self.slots[2].amount = 5


    # adds a certain amount of an item to the inentory, returning any excess items it couldn't add    
    def add(self, itemType, amount=1): # defeault amount is 1

        initialAmount = amount
        # first sweep for any open stacks
        if itemType.stackSize > 1:
            for slot in self.slots:
                if slot.type == itemType:
                    addAmo = amount
                    if addAmo > itemType.stackSize - slot.amount:
                        addAmo = itemType.stackSize  - slot.amount
                    slot.amount += addAmo
                    amount -= addAmo
                    if amount <= 0:
                        return True
        
        space = False
        # places the item in the next slot
        for slot in self.slots:
            if slot.type == None:
                space = True
                slot.type = itemType
                if itemType.stackSize < amount:
                    slot.amount = itemType.stackSize
                    return self.add(itemType, amount - itemType.stackSize)
                else:
                    slot.amount = amount
                    return True
        if space == False:
            return amount
    
    def removeItemHeld(self):
        if self.slots[self.chosenSlot].amount == 1:
            self.slots[self.chosenSlot].type = None
        self.slots[self.chosenSlot].amount -= 1

    # removes an item from the inventory
    def remove(self, itemType, amount=1): # default amount is 1
        found = 0
        for slot in self.slots:
            if slot.type == itemType:

                # if there is not enough items in the slot
                if slot.amount < amount:
                    amount -= slot.amount
                    found += slot.amount
                    slot.amount = 0
                    slot.type = None
                    continue

                # if there is a perfect number of items in the slot
                elif slot.amount == amount:
                    found += amount
                    slot.amount = 0
                    slot.type = None
                    amount -= slot.amount
                    return found
                
                # if there is a surplus number of items in the slot
                elif slot.amount > amount:
                    found += amount
                    slot.amount -= amount
                    amount -= slot.amount
                    return found
                
        return found # returns number of items found and therefore removed
    
    # returns whether a certain amount of an item is present in the inventory
    def has(self, itemType, amount=1):
        found = 0

        # goes through each slots
        for slot in self.slots:
            if slot.type == itemType: # checks if slot item is one searched for
                found += slot.amount
                if found >= amount:
                    return True
        return False # there is no / not enough of item
    
    # returns the first slot number of where an item is
    def getIndex(self, itemType):
        for index, slot in enumerate(self.slots):
            if slot.type == itemType:
                return index
        return -1 # returned if item is not found
    
    # creates a string version of the inventory to view
    def string(self):
        s = ""

        for i in range(self.capacity):
            if self.slots[i].type is not None:
                s += str(self.slots[i].type.name) + ":" + str(self.slots[i].amount) + "\t"
            else:
                s += "Empty slot\t"
        return s

    # creates a dictionary of inventory to store in json file
    def dictionary(self):
        dict = {}

        for i in range(self.capacity):
            if self.slots[i].type is not None:
                dict[i] = [str(self.slots[i].type.name), self.slots[i].amount]
            else:
                dict[i] = [None, 0]
        
        return dict
        
    def setUpInventory(self, dictionary):

        STRING_TO_OBJECT = {"hoe": hoe, "waterCan": waterCan, "scythe": scythe, "potato seed": potatoSeed, "potato": potato, "turnip seed": turnipSeed, "turnip": turnip, "onion seed": onionSeed, "onion": onion, "radish seed": radishSeed, "radish": radish, "carrot seed": carrotSeed, "carrot": carrot, "spinach seed": spinachSeed, "spinach": spinach}

        for i in range(self.capacity):
            values = dictionary.get(str(i), None)
            print(values)
            if values[0] is not None:
                self.slots[i].type = STRING_TO_OBJECT.get(values[0])
                self.slots[i].amount = values[1]

    # returns how many slots are currently open
    def getFreeSlots(self):
        i = 0
        for slot in self.slots:
            if slot.type is None:
                i += 1
        return i

    # returns true if all slots have an item, otherwise False
    def isFull(self):
        return self.getFreeSlots() == 0
    
hoe = ItemType("hoe", HOE, 200, 100)
waterCan = ItemType("waterCan", WATERCAN, 200, 100)
scythe = ItemType("scythe", SCYTHE, 200, 100)

potatoSeed = ItemType("potato seed", potatoObject.getImage(0, 1, 16, 16, 3), 300, 200, 15)
potato = ItemType("potato", potatoObject.getImage(1, 1, 16, 16, 3), 500, 400, 30)
turnipSeed = ItemType("turnip seed", turnipObject.getImage(0, 1, 16, 16, 3), 300, 200, 15)
turnip = ItemType("turnip", turnipObject.getImage(1, 1, 16, 16, 3), 500, 400, 30)
onionSeed = ItemType("onion seed", onionObject.getImage(0, 1, 16, 16, 3), 300, 200, 15)
onion = ItemType("onion", onionObject.getImage(1, 1, 16, 16, 3), 500, 400, 30)
radishSeed = ItemType("radish seed", radishObject.getImage(0, 1, 16, 16, 3), 300, 200, 15)
radish = ItemType("radish", radishObject.getImage(1, 1, 16, 16, 3), 500, 400, 30)
carrotSeed = ItemType("carrot seed", carrotObject.getImage(0, 1, 16, 16, 3), 300, 200, 15)
carrot = ItemType("carrot", carrotObject.getImage(1, 1, 16, 16, 3), 500, 400, 30)
spinachSeed = ItemType("spinach seed", spinachObject.getImage(0, 1, 16, 16, 3), 300, 200, 15)
spinach = ItemType("spinach", spinachObject.getImage(1, 1, 16, 16, 3), 500, 400, 30)

CROP_STAGE3_TO_CROP = { "P3": potato, "T3": turnip, "O3": onion, "R3": radish, "C3": carrot, "S3": spinach}