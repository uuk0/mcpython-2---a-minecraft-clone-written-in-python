import globals as G

"""class for endstone"""


class Endstone(G.itemclass):
    def getName(self):
        return "minecraft:endstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/END_STONE.png"


G.itemhandler.register(Endstone)

"""class for endstone brick"""


class Endstone(G.itemclass):
    def getName(self):
        return "minecraft:endstone_brick"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/END_BRICKS.png"


G.itemhandler.register(Endstone)
