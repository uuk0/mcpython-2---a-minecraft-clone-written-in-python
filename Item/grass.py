import globals as G

"""class for grass"""


class Grass(G.itemclass):
    def getName(self):
        return "minecraft:grass"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/GRASS.png"


G.itemhandler.register(Grass)
