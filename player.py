import globals as G
import Inventory.player as playerinventory
import chat
import log
from pyglet.window import key, mouse
import IItemStack
import config
from entity.player import PlayerEntity as PlayerEntity

"""class for player"""
class player:
    def __init__(self):
        G.player = self
        self.inventory = playerinventory.PlayerInventory()
        self.dimension = None #!
        self.name = "mcpython_test_player"
        self.chat = chat.chat()
        G.inventoryhandler.show_inventory(self.inventory.id)
        self.gamemdoe = 0
        self.selectedinventoryslot = 0
        self.movingslot = None
        self.movingslotstart = None
        self.entity = PlayerEntity()

    """kill the player"""
    def kill(self):
        log.printMSG("[CHAT] player died")
        G.window.position = (0, 10, 0)
        self.inventory.clear()

    """add item(s) to the playerinventory"""
    def addToInventory(self, item, amount=1):
        if type(item) != str:
            item = item.getName()
        slots = []
        for e in self.inventory.inventorys:
            slots += e.slots
        for e in slots:
            if e.stack.item and e.stack.item.getName() == item:
                if e.stack.amount + amount <= e.stack.item.getMaxStackSize():
                    e.stack.amount += amount
                    return
                else:
                    amount = amount - (e.stack.item.getMaxStackSize() - e.stack.amount)
                    e.stack.amount = e.stack.item.getMaxStackSize()
        for e in slots:
            if e.stack.item == None:
                e.setItem(item, amount)
                return
        log.printMSG("[PLAYER][ERROR] can't give player item "+str(item)+". No Place found")

    """callen when the mouse is pressed. only used by eventhandler
    used to detect mousepress on inventoryitems"""
    def on_mouse_press(self, x, y, button, modifiers):
        if self.movingslot != None and not (self.movingslot.stack and self.movingslot.stack.item):
            self.movingslot.position = self.movingslotstart
            return
        x -= config.SlotConfig.ImagePreMove[0]
        y -= config.SlotConfig.ImagePreMove[1]
        #log.printMSG("[PLAYER][INVENTORY][HOVERING] "+str(x)+" "+str(y)+" "+str(self.movingslot))
        slots = []
        for e in G.inventoryhandler.activeinventorys:
            e = G.inventoryhandler.inventorys[e]
            #print(e, type(e), issubclass(type(e), G.inventoryclass))
            if issubclass(type(e), G.inventoryclass):
                slots += e.slots
        slot = None
        for e in slots:
            if (e.stack and e.stack.item and e != self.movingslot and not self.movingslot):
                if e.stack.image and x >= e.stack.image.x and x <= e.stack.image.x+config.SlotConfig.ImageSize[0]:
                    if y >= e.stack.image.y and y <= e.stack.image.y+config.SlotConfig.ImageSize[1]:
                        slot = e
            elif (self.movingslot != None and self.movingslot != e):
                sx, sy = e.position
                sx += e.inventory.position[0]
                sy += e.inventory.position[1]
                if y >= sy and y <= sy+config.SlotConfig.ImageSize[0] and x >= sx and x <= sx+config.SlotConfig.ImageSize[1] and not slot:
                    #print(x, y, sx, sy, e, e.position, e.inventory, e.inventory.position)
                    slot = e
        if slot:
            if not self.movingslot:
                if button == mouse.LEFT:
                    self.movingslot = slot
                    self.movingslotstart = slot.position
                elif button == mouse.MIDDLE:
                    self.movingslot = slot
                    self.movingslotstart = slot.position
                    self.movingslot.stack.amount = self.movingslot.stack.item.getMaxStackSize()
            elif self.movingslot.stack.item:
                if button == mouse.LEFT:
                    if not (slot.stack and slot.stack.item) and slot.canplayersetitems:
                        slot.setStack(self.movingslot.stack)
                        self.movingslot.setItem(None)
                        self.movingslot.position = self.movingslotstart
                        self.movingslot = None
                    elif slot.canplayersetitems and self.movingslot.stack.item.getName() == slot.stack.item.getName():
                        if self.movingslot.stack.amount + slot.stack.amount <= slot.stack.item.getMaxStackSize():
                            slot.stack.amount += self.movingslot.stack.amount
                            self.movingslot.stack = IItemStack.IItemStack(None)
                            self.movingslot.position = self.movingslotstart
                            self.movingslot = None
                        else:
                            self.movingslot.stack.amount -= slot.stack.item.getMaxStackSize() - slot.stack.amount
                            slot.stack.amount = slot.stack.item.getMaxStackSize()
                    elif slot.canplayersetitems:
                        stack1 = slot.stack
                        slot.setStack(self.movingslot.stack)
                        self.movingslot.setStack(stack1)
                elif button == mouse.RIGHT:
                    if not (slot.stack and slot.stack.item) and slot.canplayersetitems:
                        slot.setItem(self.movingslot.stack.item.getName(), amount=1)
                        self.movingslot.stack.amount -= 1
                        if self.movingslot.stack.amount == 0:
                            self.movingslot.setItem(None)
                            self.movingslot.position = self.movingslotstart
                            self.movingslot = None
                    elif self.movingslot.stack.item.getName() == slot.stack.item.getName() and \
                        slot.stack.amount < slot.stack.item.getMaxStackSize() and slot.canplayersetitems:
                        slot.stack.amount += 1
                        self.movingslot.stack.amount -= 1
                        if self.movingslot.stack.amount == 0:
                            self.movingslot.setItem(None)
                            self.movingslot.position = self.movingslotstart
                            self.movingslot = None

    """callen when the mouse is moved. only used by eventhandler"""
    def on_mouse_motion(self, x, y, dx, dy):
        if self.movingslot:
            self.movingslot.position = (self.movingslot.position[0]+dx,
                                        self.movingslot.position[1]+dy)
