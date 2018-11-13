import globals as G
import IItemStack

"""inventory handler class
register functions are only used in background
"""
class InventoryHandler:
    def __init__(self):
        self.inventorys = {}
        self.nextinvid = 0
        self.slots = {}
        self.nextslotid = 0
        self.inventorycollections = {}

        self.activeinventorys = []
        self.activeated = {}

    """registers the inventorys"""
    def _register_inventory(self, inv):
        inv.id = self.nextinvid
        self.inventorys[self.nextinvid] = inv
        self.nextinvid += 1

    """registers the slots"""
    def _register_slot(self, slot):
        slot.id = self.nextslotid
        self.slots[self.nextslotid] = slot
        self.nextslotid += 1

    """registers the inventorycollections"""
    def _register_inventorycollection(self, collection):
        collection.id = self.nextinvid
        self.inventorycollections[self.nextinvid] = collection
        self.inventorys[self.nextinvid] = collection
        self.nextinvid += 1

    """shows the inventory"""
    def show_inventory(self, id):
        self.inventorys[id].active = True
        self.inventorys[id].on_show()
        self.activeinventorys.append(id)
        if issubclass(type(self.inventorys[id]), InventoryCollection):
            for e in self.inventorys[id].getActiveInventorys():
                self.show_inventory(e.id)
                self.activeated[id] = self.inventorys[id].getActiveInventorys()

    """hides the inventory"""
    def hide_inventory(self, id):
        self.inventorys[id].active = False
        self.inventorys[id].on_hide()
        if id not in self.activeinventorys:
            return
        self.activeinventorys.remove(id)
        if type(self.inventorys[id]) == InventoryCollection:
            for e in self.activeated[id]:
                del self.activeated[id]
                self.hide_inventory(e.id)

    """only callen by eventhandler
    draws all shown entitys"""
    def draw(self):
        for e in self.activeinventorys:
            self.inventorys[e].draw()

G.inventoryhandler = InventoryHandler()

"""Inventory class"""
class Inventory:
    """you can 'tag' an inventory class for detecting it in runtime"""
    tag = []

    def __init__(self):
        self.position = self.getBasePosition()
        self.slots = self.creatSlots()
        for e in self.slots:
            e.inventory = self
        self.active = False
        G.inventoryhandler._register_inventory(self)

    """returns a list of the slots that should be used"""
    def creatSlots(self):
        return []

    """returns the position where the inventory should be drawn"""
    def getBasePosition(self):
        return (0, 0)

    """draw the inventory"""
    def draw(self):
        self.position = self.getBasePosition()
        for e in self.slots:
            e.draw(self.position)

    """callen when the inventory is shown"""
    def on_show(self):
        pass

    """callen when the inventory is hidden"""
    def on_hide(self):
        pass

    """callen to check if the inventory is an game-window. set to Fase if it is something like an overlay"""
    def isDisablyingGame(self):
        return True

    """callen to check if we should use our detect system in player"""
    def shouldInteractWithPlayerInventoryMoving(self):
        return True

G.inventoryclass = Inventory

"""inventorycollection class"""
class InventoryCollection:
    """you can 'tag' an inventorycollection class for detecting it in runtime"""
    tag = []

    def __init__(self):
        self.inventorys = self.creatInventorys()
        self.active = False
        G.inventoryhandler._register_inventorycollection(self)

    """returns a list of used inventorys"""
    def creatInventorys(self):
        return []

    """draw the inventorys"""
    def draw(self):
        for e in self.getActiveInventorys():
            e.draw()

    """returns a list of all active inventorys"""
    def getActiveInventorys(self):
        return []

    """callen when the inventory is shown"""
    def on_show(self):
        pass

    """callen when the inventory is hidden"""
    def on_hide(self):
        pass

    """callen to check if the inventory is an game-window. set to Fase if it is something like an overlay"""
    def isDisablyingGame(self):
        return True

    """callen to check if we should use our detect system in player"""
    def shouldInteractWithPlayerInventoryMoving(self):
        return True

G.inventorycollection = InventoryCollection

"""Slot class"""
class Slot:
    def __init__(self, position, stack=IItemStack.IItemStack(None),
                 canplayersetitems=True, update_func=None):
        self.position = position
        self.stack = stack
        self.stack.slot = self
        self.inventory = None
        self.canplayersetitems = canplayersetitems
        self.update_func = update_func

    """draw the slot"""
    def draw(self, position):
        self.stack.drawImage((self.position[0]+position[0],
                              self.position[1]+position[1]))

    """set the stack which the slot is holding"""
    def setStack(self, stack):
        self.stack = stack
        self.stack.slot = self
        if self.update_func: self.update_func(self)
        self.stack.update_func = self.update_func

    """set the item of the slot"""
    def setItem(self, name, amount=1):
        self.stack = IItemStack.IItemStack(name, amount)
        self.stack.slot = self
        if self.update_func: self.update_func(self)
        self.stack.update_func = self.update_func

G.inventoryslot = Slot

def loadInventorys(*args):
    from . import player, crafting

G.eventhandler.on_event("game:registry:on_inventory:registrate_periode", loadInventorys)