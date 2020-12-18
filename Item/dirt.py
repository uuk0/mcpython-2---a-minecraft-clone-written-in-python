import globals as G

"""class for dirt"""


class Dirt(G.itemclass):
    def getName(self):
        return "minecraft:dirt"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/DIRT#0.png"


G.itemhandler.register(Dirt)

"""class for coarse dirt"""


class CoarseDirt(G.itemclass):
    def getName(self):
        return "minecraft:coarse_dirt"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/DIRT#1.png"


G.itemhandler.register(CoarseDirt)
