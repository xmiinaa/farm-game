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

# holds a quantity of an item
class ItemSlot:
    def __init__(self, num):
        self.type = None
        self.amount = 0
        
        if num < 10:
            self.rect = pygame.Rect(((num*TILE_SIZE) + 108, 620), (72, 72))
        #elif num in range(10, )
        else:
            self.rect = pygame.Rect(((num*TILE_SIZE) + 108, 320), (72, 72))

# has a certain number of slots for items.
class Inventory:

    # creates new inventory
    def __init__(self):
        self.capacity = 40 # there can only be 40 slots
        self.taken_slots = 4
        self.chosenSlot = 1
        
        # creates array of slots 
        self.slots = [ItemSlot(x) for x in range(self.capacity)]

        # for now i am initiating the tools here though it may change
        self.slots[0].type = hoe
        self.slots[0].amount = 1
        self.slots[1].type = waterCan 
        self.slots[1].amount = 1
        self.slots[2].type = scythe 
        self.slots[2].amount = 1
        self.slots[3].type = potatoSeed
        self.slots[3].amount = 15
    
    # displays the inventory main 10 slots
    def draw(self):
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(178, 618, 724, 76), 2) # draws a black outline for inventory
        
        # loop to go through all 10 slots
        for slot in range(1,11):

            # checks to see if the slot is the one currently selected
            if slot == self.chosenSlot:
                SCREEN.blit(CHOSEN_SLOT, ((self.chosenSlot*TILE_SIZE)+108,620)) # displays different image
            else:
                SCREEN.blit(SLOT, ( (TILE_SIZE*slot)+108 , 620))
            
            # checks to see if the slot has an item
            if self.slots[slot-1].type is not None:
                SCREEN.blit(self.slots[slot-1].type.icon, ((TILE_SIZE*(slot-1)+195 , 640))) # displays item
                if self.slots[slot-1].amount >1:
                    text = OCR_INVENTORY.render( str(self.slots[slot-1].amount), True, WHITE)
                    SCREEN.blit(text, ((TILE_SIZE*(slot-1)+186 , 624)))

    # changes currently chosen slot if user clicks correctly
    def click(self, mousePos):
        for slot in range(1,11):

            # checks if mouse position is in range of slot
            if mousePos[0] in range((TILE_SIZE * slot)+108, (TILE_SIZE * slot)+180) and mousePos[1] in range(620, 692):
                self.changeSlot(slot)
    
    # changes the current slot / item held
    def changeSlot(self, newSlot):
        self.chosenSlot = newSlot
    
    # changes slot image when mouse is hovering over it to let user aware
    def hover(self, mousePos):
        for slot in range(1,11):
            
            # checks if mouse position is in range of slot
            if mousePos[0] in range((TILE_SIZE * slot)+108, (TILE_SIZE * slot)+180) and mousePos[1] in range(620, 692):
                SCREEN.blit(CHOSEN_SLOT, ((slot*TILE_SIZE)+108,620)) # displays different slot
            
            # checks to see if the slot has an item
            if self.slots[slot].type is not None:
                SCREEN.blit(self.slots[slot-1].type.icon, ((TILE_SIZE*(slot-1))+195 , 640)) # displays item

                if self.slots[slot-1].amount >1:
                    text = OCR_INVENTORY.render( str(self.slots[slot-1].amount), True, WHITE)
                    SCREEN.blit(text, ((TILE_SIZE*(slot-1)+186 , 624)))
    
    # returns the item name that the player is currently holding
    def getItem(self):
        if self.slots[self.chosenSlot-1].type == None:
            return "None"
        else: 
            return self.slots[self.chosenSlot-1].type.name

    # adds a certain amount of an item to the inentory, returning any excess items it couldn't add    
    def add(self, itemType, amount=1): # defeault amount is 1

        # first sweep for any open stacks
        if ItemType.stackSize > 1:
            for slot in self.slots:
                if slot.type == itemType:
                    addAmo = amount
                    if addAmo > itemType.stackSize - slot.amount:
                        addAmo = itemType.stackSize  - slot.amount
                    slot.amount += addAmo
                    amount -= addAmo
                    if amount <= 0:
                        return 0
        
        # places the item in the next slot
        for slot in self.slots:
            if slot.type == None:
                slot.type = itemType
                if itemType.stackSize < amount:
                    slot.amount = itemType.stackSize
                    return self.add(itemType, amount - itemType.stackSize)
                else:
                    slot.amount = amount
                    return 0
    
    # removes an item from the inventory
    def remove(self, itemType, amount=1): # default amount is 1
        found = 0
        for slot in self.slots:
            if slot.type == itemType:

                # if there is not enough items in the slot
                if slot.amount < amount:
                    found += slot.amount
                    slot.amount = 0
                    slot.type = None
                    continue

                # if there is a perfect number of items in the slot
                elif slot.amount == amount:
                    found += amount
                    slot.amount = 0
                    slot.type = None
                    return found
                
                # if there is a surplus number of items in the slo
                else:
                    found += amount
                    slot.amount -= amount
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
        print(s)
        
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

"""
potato = ItemType("potato", HOE, 200, 100)
turnip = ItemType("turnip", HOE, 200, 100)
onion = ItemType("onion", HOE, 200, 100)
radish = ItemType("radish", HOE, 200, 100)
carrot = ItemType("carrot", HOE, 200, 100)
spinach = ItemType("spinach", HOE, 200, 100)
"""

potatoObject = SpriteSheet(POTATO_SHEET)
potatoList = []
for x in range(5):
    potatoList.append(potatoObject.getImage(x, 1, 16, 16, 3)) 

potatoSeed = ItemType("potato seed", potatoList[0], 300, 200)