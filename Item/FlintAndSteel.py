import globals as G

"""class for flint and steel"""


class Barrel(G.itemclass):
    def getName(self):
        return "minecraft:flint_and_steel"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/textures/item/flint_and_steel.png"


G.itemhandler.register(Barrel)
