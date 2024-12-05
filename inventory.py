import pygame
import sys
from config import *

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
    def __init__(self):
        self.type = None
        self.amount = 0
    

# has a certain number of slots for items.
class Inventory:

    # creates new inventory
    def __init__(self):
        self.capacity = 20
        self.taken_slots = 0
        self.chosenSlot = 10
        
        # creates array of slots 
        self.slots = []
        for _ in range(self.capacity):
            self.slots.append(ItemSlot())
    
    def draw(self):
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(178, 618, 724, 76), 2)
        for slot in range(1,11):
            if slot == self.chosenSlot:
                SCREEN.blit(CHOSEN_SLOT, ((self.chosenSlot*TILE_SIZE)+108,620))
            else:
                SCREEN.blit(SLOT, ( (TILE_SIZE*slot)+108 , 620))

    def click(self, mousePos):
        for slot in range(1,11):
            if mousePos[0] in range((TILE_SIZE * slot)+108, (TILE_SIZE * slot)+180) and mousePos[1] in range(620, 692):
                self.chosenSlot = slot
    
    def hover(self, mousePos):
        for slot in range(1,11):
            if mousePos[0] in range((TILE_SIZE * slot)+108, (TILE_SIZE * slot)+180) and mousePos[1] in range(620, 692):
                SCREEN.blit(CHOSEN_SLOT, ((slot*TILE_SIZE)+108,620))
    
    def getItem(self):
        return self.slots[self.chosenSlot]

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
    def __str__(self):
        s = ""

        for i in self.slots:
            if i.type is not None:
                s += str(i.type.name) + ":" + str(i.amount) + "\t"
            else:
                s += "Empty slot\t"
            return s
        
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
    