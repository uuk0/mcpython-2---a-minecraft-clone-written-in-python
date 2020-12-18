import globals as G
import pyglet
import Inventory.inventory
import log


class Crafting(G.inventoryclass):
    """class for crafting in crafting table"""

    tag = ["inventorys:crafting:crafting_table", "inventorys:crafting"]
    size = (3, 3)

    def __init__(self):
        self.slots = self.creatSlots()
        for e in self.slots:
            e.inventory = self
        self.active = False
        G.inventoryhandler._register_inventory(self)
        self.image = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/container/crafting_table.png"
            )
        )
        self.position = self.getBasePosition()

    def creatSlots(self):
        return []

    def getBasePosition(self):
        return (
            G.window.size[0] / 2 - self.image.width / 2,
            G.window.size[1] / 2 - self.image.height / 2,
        )

    def draw(self):
        self.position = self.getBasePosition()
        self.image.x, self.image.y = self.getBasePosition()
        self.image.draw()
        for e in self.slots:
            e.draw(self.position)

    def on_key_press(self, key, mod):
        pass

    def on_try_close(self):
        log.printMSG("I AM NOT CLOSED")
