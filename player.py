import pyglet
from pyglet.window import key, mouse

import chat
import config
import globals as G
import IItemStack
import Inventory.player as playerinventory
import log
import tooltip
from entity.player import PlayerEntity as PlayerEntity


class player:
    """class for player"""

    def __init__(self):
        G.player = self
        self.inventory = playerinventory.PlayerInventory()
        self.dimension = None
        self.name = "mcpython_test_player"
        self.chat = chat.chat()
        G.inventoryhandler.show_inventory(self.inventory.id)
        self.gamemode = config.DEFAULT_GAMEMODE
        self.selectedinventoryslot = 0
        self.movingslot = None
        self.movingslotstart = None
        self.entity = PlayerEntity()
        self.tooltip = tooltip.ToolTip()
        self.active_tooltip = False
        self.tooltipslot = None
        self.checkinventorysforslots = [self.inventory.inventorys[0]]
        self.harts = 20
        self.__oldharts = None
        self.hartsprites = []
        self.hartimages = [
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/icons/hards_full.png"
            ),
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/icons/hards_half.png"
            ),
        ]
        self.drawn_sprites = 0
        for i in range(10):
            self.hartsprites.append(pyglet.sprite.Sprite(self.hartimages[0]))
            self.hartsprites[-1].position = (
                self.inventory.inventorys[0].getBasePosition()[0] + i * 17,
                70,
            )
        self.updateHarts()

        for k in config.AdvancedVanilla.START_INVENTORY.keys():
            self.addToInventory(k, config.AdvancedVanilla.START_INVENTORY[k])

    def updateHarts(self):
        for i in range(10):
            self.hartsprites[i].position = (
                self.inventory.inventorys[0].getBasePosition()[0] + i * 17,
                70,
            )
        if self.harts != self.__oldharts:
            self.__oldharts = self.harts
            for i in range(self.harts // 2):
                self.hartsprites[i].image = self.hartimages[0]
            if self.harts % 2 == 1:
                self.hartsprites[self.harts // 2].image = self.hartimages[1]
            self.drawn_sprites = round(self.harts / 2)

    def drawHarts(self):
        self.updateHarts()
        for i in range(self.drawn_sprites):
            self.hartsprites[i].draw()

    """kill the player"""

    def kill(self):
        log.printMSG("[CHAT] player died")
        G.window.position = (0, 10, 0)
        self.inventory.clear()

    """add item(s) to the playerinventory"""

    def addToInventory(self, item, amount=1):
        if type(item) != str:
            item = item.getName()
        else:
            item = G.itemhandler.getByName(item).getName(None)
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
        log.printMSG(
            "[PLAYER][ERROR] can't give player item " + str(item) + ". No Place found"
        )

    def getSlotFor(self, x, y):
        x -= config.SlotConfig.ImagePreMove[0]
        y -= config.SlotConfig.ImagePreMove[1]
        # log.printMSG("[PLAYER][INVENTORY][HOVERING] "+str(x)+" "+str(y)+" "+str(self.movingslot))
        slots = []
        for e in self.checkinventorysforslots:
            if type(e) == int:
                e = G.inventoryhandler.inventorys[e]
            # log.printMSG(e, type(e), issubclass(type(e), G.inventoryclass))
            if issubclass(type(e), G.inventoryclass):
                slots += e.slots
        slot = None
        for e in slots:
            if (
                e.stack
                and e.stack.item
                and e != self.movingslot
                and not self.movingslot
            ):
                if (
                    e.stack.image
                    and x >= e.stack.image.x
                    and x <= e.stack.image.x + config.SlotConfig.ImageSize[0]
                ):
                    if (
                        y >= e.stack.image.y
                        and y <= e.stack.image.y + config.SlotConfig.ImageSize[1]
                    ):
                        slot = e
            elif self.movingslot != None and self.movingslot != e:
                sx, sy = e.position
                sx += e.inventory.position[0]
                sy += e.inventory.position[1]
                if (
                    y >= sy
                    and y <= sy + config.SlotConfig.ImageSize[0]
                    and x >= sx
                    and x <= sx + config.SlotConfig.ImageSize[1]
                    and not slot
                ):
                    # log.printMSG(x, y, sx, sy, e, e.position, e.inventory, e.inventory.position)
                    slot = e
        return slot

    """callen when the mouse is pressed. only used by eventhandler
    used to detect mousepress on inventoryitems"""

    def on_mouse_press(self, x, y, button, modifiers):
        if self.movingslot != None and not (
            self.movingslot.stack and self.movingslot.stack.item
        ):
            self.movingslot.position = self.movingslotstart
            return
        slot = self.getSlotFor(x, y)
        if slot:
            if not self.movingslot:
                if button == mouse.LEFT:
                    self.movingslot = slot
                    self.movingslotstart = slot.position
                elif button == mouse.MIDDLE:
                    self.movingslot = slot
                    self.movingslotstart = slot.position
                    self.movingslot.stack.amount = (
                        self.movingslot.stack.item.getMaxStackSize()
                    )
            elif self.movingslot.stack.item:
                if button == mouse.LEFT:
                    if (
                        not (slot.stack and slot.stack.item)
                        and slot.canplayersetitems
                        and (
                            not slot.controll_function
                            or slot.controll_function(self.movingslot.stack)
                        )
                    ):
                        slot.setStack(self.movingslot.stack)
                        self.movingslot.setItem(None)
                        self.movingslot.position = self.movingslotstart
                        self.movingslot = None
                    elif (
                        slot.stack.item
                        and slot.canplayersetitems
                        and self.movingslot.stack.item.getName()
                        == slot.stack.item.getName()
                        and (
                            not slot.controll_function
                            or slot.controll_function(self.movingslot.stack)
                        )
                    ):
                        if (
                            self.movingslot.stack.amount + slot.stack.amount
                            <= slot.stack.item.getMaxStackSize()
                        ):
                            slot.stack.amount += self.movingslot.stack.amount
                            self.movingslot.stack = IItemStack.IItemStack(None)
                            self.movingslot.position = self.movingslotstart
                            self.movingslot = None
                        else:
                            self.movingslot.stack.amount -= (
                                slot.stack.item.getMaxStackSize() - slot.stack.amount
                            )
                            slot.stack.amount = slot.stack.item.getMaxStackSize()
                    elif (
                        slot
                        and slot.canplayersetitems
                        and (
                            not slot.controll_function
                            or slot.controll_function(self.movingslot.stack)
                        )
                    ):
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
                    elif (
                        self.movingslot.stack.item.getName()
                        == slot.stack.item.getName()
                        and slot.stack.amount < slot.stack.item.getMaxStackSize()
                        and slot.canplayersetitems
                    ):
                        slot.stack.amount += 1
                        self.movingslot.stack.amount -= 1
                        if self.movingslot.stack.amount == 0:
                            self.movingslot.setItem(None)
                            self.movingslot.position = self.movingslotstart
                            self.movingslot = None

    """callen when the mouse is moved. only used by eventhandler"""

    def on_mouse_motion(self, x, y, dx, dy):
        if self.movingslot:
            self.movingslot.position = (
                self.movingslot.position[0] + dx,
                self.movingslot.position[1] + dy,
            )
        slot = self.getSlotFor(x, y)
        if self.movingslot:
            slot = self.movingslot
        if slot:
            self.tooltip.setStack(slot.stack)
            self.tooltip.draw((x, y))
            self.active_tooltip = True
            self.tooltipslot = slot
        else:
            self.active_tooltip = False
            self.tooltipslot = None

    def on_draw(self, *args):
        if self.active_tooltip:
            x, y = self.tooltipslot.position
            x += config.SlotConfig.ImageSize[0] * 2
            y += config.SlotConfig.ImageSize[1] * 2
            self.tooltip.draw((x, y))
        if self.gamemode in [0, 2]:
            self.drawHarts()
