import traceback

import pyglet
from pyglet.window import key as keys

import config
import crafting.IGridInventory
import globals as G
import imagecutter
import notations


class PlayerInventory(G.inventorycollection):
    """class for playerinventory"""

    tag = ["player:hotbar", "player:inventory", "system:nothideable"]

    def __init__(self):
        G.inventorycollection.__init__(self)
        self.guitype = 0
        self.inventorys[-1].main = self

    def creatInventorys(self):
        return [Hotbar(), Rows(), Crafting()]

    def getActiveInventorys(self):
        return self.inventorys if self.guitype == 1 else self.inventorys[:1]

    def draw(self):
        self.inventorys[0].type = self.guitype
        if self.guitype == 0:
            self.inventorys[0].draw()
        else:
            for e in self.inventorys:
                e.draw()

    def shouldInteractWithPlayerInventoryMoving(self):
        return self.guitype != 0

    def isDisablyingGame(self):
        return self.guitype != 0

    def on_try_close(self):
        self.guitype = 0
        G.inventoryhandler.hide_inventory(self)
        G.inventoryhandler.show_inventory(self)
        G.window.set_exclusive_mouse(True)

    def on_key_press(self, key, mod):
        if key == keys.E:
            self.on_try_close()

    def on_show(self):
        for e in self.inventorys:
            if e.active:
                G.inventoryhandler.hide_inventory(e)
        if self.guitype == 0:
            G.inventoryhandler.show_inventory(self.inventorys[0])
        else:
            for e in self.inventorys:
                G.inventoryhandler.show_inventory(e)

    def on_hide(self):
        for e in self.inventorys:
            if e.active:
                G.inventoryhandler.hide_inventory(e)


class Crafting(G.inventoryclass, crafting.IGridInventory.IGridInventory):
    """class of player inventory crafting part"""

    tag = ["player:inventory", "inventorys:crafting", "system:nothideable"]

    def get_grid_size(self):
        return (2, 2)

    def get_output_size(self):
        return (1, 1)

    def get_input_slots(self):
        return [self.slots[:2], self.slots[2:-1]]

    def get_output_slots(self):
        return [self.slots[-1]]

    def __init__(self, *args, **kwargs):
        G.inventoryclass.__init__(self, *args, **kwargs)
        crafting.IGridInventory.IGridInventory.__init__(self)
        self.used_slots = []

    def creatSlots(self):
        return [
            self.add_input((210, 282)),
            self.add_input((248, 282)),
            self.add_input((210, 244)),
            self.add_input((248, 244)),
            self.add_output((328, (282 + 244) / 2 - 2)),
        ]

    def getBasePosition(self):
        if not hasattr(G.window, "player"):
            return (0, 0)
        if G.window.player.inventory.inventorys[0].type == 1:
            return (
                G.window.size[0] / 2
                - G.window.player.inventory.inventorys[0].image2.width / 2,
                G.window.size[1] / 2
                - G.window.player.inventory.inventorys[0].image2.height / 2,
            )
        elif G.window.player.inventory.inventorys[0].type == 0:
            return (
                G.window.size[0] / 2
                - G.window.player.inventory.inventorys[0].image1.width / 2,
                G.window.size[1] / 2
                - G.window.player.inventory.inventorys[0].image1.height / 2
                - 270,
            )

    """updates the recipi stored"""

    def update_input(self, slot):
        pass


class Rows(G.inventoryclass):
    """class of player inventory 'row' part"""

    tag = ["player:inventory", "system:nothideable"]

    def creatSlots(self):
        slots = []
        for y in [64, 102, 140]:
            for x in [18, 56, 94, 132, 170, 209, 247, 286, 324]:
                slots.append(G.inventoryslot((x, y)))
        slots += [
            G.inventoryslot((18, 190), controll_function=self.headcheck),
            G.inventoryslot((18, 228), controll_function=self.bodycheck),
            G.inventoryslot((18, 266), controll_function=self.leggincheck),
            G.inventoryslot((18, 304), controll_function=self.bootcheck),
        ]
        slots.append(G.inventoryslot((165, 190)))
        return slots

    def headcheck(self, stack):
        if (
            type(stack.item)
            in G.notationhandler.notations["oredict"].items["armor:heads"]
        ):
            return True
        return False

    def bodycheck(self, stack):
        if (
            type(stack.item)
            in G.notationhandler.notations["oredict"].items["armor:bodys"]
        ):
            return True
        return False

    def leggincheck(self, stack):
        if (
            type(stack.item)
            in G.notationhandler.notations["oredict"].items["armor:leggins"]
        ):
            return True
        return False

    def bootcheck(self, stack):
        if (
            type(stack.item)
            in G.notationhandler.notations["oredict"].items["armor:foots"]
        ):
            return True
        return False

    def getBasePosition(self):
        if not hasattr(G.window, "player"):
            return (0, 0)
        if G.window.player.inventory.inventorys[0].type == 1:
            return (
                G.window.size[0] / 2
                - G.window.player.inventory.inventorys[0].image2.width / 2,
                G.window.size[1] / 2
                - G.window.player.inventory.inventorys[0].image2.height / 2,
            )
        elif G.window.player.inventory.inventorys[0].type == 0:
            return (
                G.window.size[0] / 2
                - G.window.player.inventory.inventorys[0].image1.width / 2,
                G.window.size[1] / 2
                - G.window.player.inventory.inventorys[0].image1.height / 2
                - 270,
            )


class Hotbar(G.inventoryclass):
    """class of player inventory hotbar part"""

    tag = ["player:hotbar", "player:inventory", "system:nothideable"]

    def __init__(self):
        self.image1 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "/tmp/gui/hotbar.png")
        )
        self.image2 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "/tmp/gui/playerinventory.png")
        )
        self.image3 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "/tmp/gui/hotbar_select.png")
        )
        self.type = 0
        self.lasttype = 0
        G.inventoryclass.__init__(self)
        self.image1.position = self.position
        self.image2.position = self.position
        self.image3.position = self.position

    def creatSlots(self):
        return [
            G.inventoryslot((8, 6)),
            G.inventoryslot((47, 6)),
            G.inventoryslot((47 + 39, 6)),
            G.inventoryslot((47 + 39 * 2, 6)),
            G.inventoryslot((47 + 39 * 3 + 1, 6)),
            G.inventoryslot((47 + 39 * 4 + 1, 6)),
            G.inventoryslot((47 + 39 * 5 + 2, 6)),
            G.inventoryslot((47 + 39 * 6 + 2, 6)),
            G.inventoryslot((47 + 39 * 7 + 3, 6)),
        ]

    def draw(self):
        self.position = self.getBasePosition()
        if self.type != self.lasttype:
            if self.lasttype == 1:
                self.slots[0].position = (8, 6)
                self.slots[1].position = (47, 6)
                self.slots[2].position = (47 + 39, 6)
                self.slots[3].position = (47 + 39 * 2, 6)
                self.slots[4].position = (47 + 39 * 3 + 1, 6)
                self.slots[5].position = (47 + 39 * 4 + 1, 6)
                self.slots[6].position = (47 + 39 * 5 + 2, 6)
                self.slots[7].position = (47 + 39 * 6 + 2, 6)
                self.slots[8].position = (47 + 39 * 7 + 3, 6)

            elif self.lasttype == 0:
                self.slots[0].position = (18, 18)
                self.slots[1].position = (56, 18)
                self.slots[2].position = (56 + 38, 18)
                self.slots[3].position = (56 + 38 * 2, 18)
                self.slots[4].position = (56 + 38 * 3, 18)
                self.slots[5].position = (56 + 38 * 4 + 1, 18)
                self.slots[6].position = (56 + 38 * 5 + 1, 18)
                self.slots[7].position = (56 + 38 * 6 + 1, 18)
                self.slots[8].position = (56 + 38 * 7 + 1, 18)

            self.lasttype = self.type
        self.image1.position = self.position
        self.image2.position = self.position
        if self.type == 0:
            self.image1.draw()
            self.image3.x = self.image2.x + G.player.selectedinventoryslot * 40 - 1
            self.image3.y = self.image2.y - 1
            self.image3.draw()
        elif self.type == 1:
            self.image2.draw()
        for e in self.slots:
            e.draw(self.position)

    def getBasePosition(self):
        if self.type == 1:
            return (
                G.window.size[0] / 2 - self.image2.width / 2,
                G.window.size[1] / 2 - self.image2.height / 2,
            )
        elif self.type == 0:
            return (
                G.window.size[0] / 2 - self.image1.width / 2,
                G.window.size[1] / 2 - self.image1.height / 2 - 270,
            )

    def shouldInteractWithPlayerInventoryMoving(self):
        return False

    def isDisablyingGame(self):
        return False
