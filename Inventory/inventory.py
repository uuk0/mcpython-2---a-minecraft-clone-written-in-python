import globals as G
import IItemStack
import log
import modsystem.ModLoader


class InventoryHandler:
    """inventory handler class
    register functions are only used in background
    """

    def __init__(self):
        self.inventorys = {}
        self.nextinvid = 0
        self.slots = {}
        self.nextslotid = 0
        self.inventorycollections = {}

        self.activeinventorys = []
        self.activeated = {}

    def _register_inventory(self, inv):
        """registers the inventorys"""
        inv.id = self.nextinvid
        self.inventorys[self.nextinvid] = inv
        self.nextinvid += 1

    def _register_slot(self, slot):
        """registers the slots"""
        slot.id = self.nextslotid
        self.slots[self.nextslotid] = slot
        self.nextslotid += 1

    def _register_inventorycollection(self, collection):
        """registers the inventorycollections"""
        collection.id = self.nextinvid
        self.inventorycollections[self.nextinvid] = collection
        self.inventorys[self.nextinvid] = collection
        self.nextinvid += 1

    def show_inventory(self, id):
        """shows the inventory"""
        if type(id) != int:
            id = id.id
        self.inventorys[id].active = True
        self.inventorys[id].on_show()
        self.activeinventorys.append(id)
        # log.printMSG(self.activeinventorys)
        if issubclass(type(self.inventorys[id]), InventoryCollection):
            for e in self.inventorys[id].getActiveInventorys():
                self.show_inventory(e)
                self.activeated[id] = self.inventorys[id].getActiveInventorys()

    def hide_inventory(self, id):
        """hides the inventory"""
        if type(id) != int:
            id = id.id
        self.inventorys[id].active = False
        self.inventorys[id].on_hide()
        if id not in self.activeinventorys:
            log.printMSG("[ERROR]")
            return
        self.activeinventorys.remove(id)
        if type(self.inventorys[id]) == InventoryCollection:
            for e in self.activeated[id]:
                del self.activeated[id]
                self.hide_inventory(e)

    def draw(self):
        """only callen by eventhandler
        draws all shown entitys"""
        data = []
        # function to remove double-inventorys. may be recoded by list(tuple(...))
        for e in self.activeinventorys:
            if not e in data:
                data.append(e)
        self.activeinventorys = data
        for e in self.activeinventorys:
            self.inventorys[e].draw()


G.inventoryhandler = InventoryHandler()


class Inventory:
    """Inventory class"""

    """you can 'tag' an inventory class for detecting it in runtime"""
    tag = []

    def __init__(self):
        self.position = self.getBasePosition()
        self.slots = self.creatSlots()
        for e in self.slots:
            e.inventory = self
        self.active = False
        G.inventoryhandler._register_inventory(self)

    def creatSlots(self):
        """returns a list of the slots that should be used"""
        return []

    def getBasePosition(self):
        """returns the position where the inventory should be drawn"""
        return (0, 0)

    def draw(self):
        """draw the inventory"""
        self.position = self.getBasePosition()
        for e in self.slots:
            e.draw(self.position)

    def on_show(self):
        """callen when the inventory is shown"""
        pass

    def on_hide(self):
        """callen when the inventory is hidden"""
        pass

    def isDisablyingGame(self):
        """callen to check if the inventory is an game-window. set to False if it is something like an overlay"""
        return True

    def shouldInteractWithPlayerInventoryMoving(self):
        """callen to check if we should use our detect system in player"""
        return True

    def on_try_close(self):
        pass

    def on_key_press(self, key, mod):
        pass


G.inventoryclass = Inventory


class InventoryCollection:
    """inventorycollection class"""

    """you can 'tag' an inventorycollection class for detecting it in runtime"""
    tag = []

    def __init__(self):
        self.inventorys = self.creatInventorys()
        self.active = False
        G.inventoryhandler._register_inventorycollection(self)

    def creatInventorys(self):
        """returns a list of used inventorys"""
        return []

    def draw(self):
        """draw the inventorys"""
        for e in self.getActiveInventorys():
            e.draw()

    def getActiveInventorys(self):
        """returns a list of all active inventorys"""
        return []

    def on_show(self):
        """callen when the inventory is shown"""
        pass

    def on_hide(self):
        """callen when the inventory is hidden"""
        pass

    def isDisablyingGame(self):
        """callen to check if the inventory is an game-window. set to False if it is something like an overlay"""
        return True

    def shouldInteractWithPlayerInventoryMoving(self):
        """callen to check if we should use our detect system in player"""
        return True

    def on_try_close(self):
        pass

    def on_key_press(self, key, mod):
        pass


G.inventorycollection = InventoryCollection


class Slot:
    """Slot class"""

    def __init__(
        self,
        position,
        stack=IItemStack.IItemStack(None),
        canplayersetitems=True,
        update_func=None,
        controll_function=None,
    ):
        self.position = position
        self.stack = stack
        self.stack.slot = self
        self.inventory = None
        self.canplayersetitems = canplayersetitems
        self.update_func = update_func
        self.controll_function = controll_function

    def draw(self, position):
        """draw the slot"""
        self.stack.drawImage(
            (self.position[0] + position[0], self.position[1] + position[1])
        )

    def setStack(self, stack):
        """set the stack which the slot is holding"""
        self.stack = stack
        self.stack.slot = self
        if self.update_func:
            self.update_func(self)
        self.stack.update_func = self.update_func

    def setItem(self, name, amount=1):
        """set the item of the slot"""
        self.stack = IItemStack.IItemStack(name, amount)
        self.stack.slot = self
        if self.update_func:
            self.update_func(self)
        self.stack.update_func = self.update_func


G.inventoryslot = Slot


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_inventory:registrate_periode",
    "minecraft",
    info="registrating inventorys",
)
def register():
    from . import player, crafting
