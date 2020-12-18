import globals as G

"""class for gravel"""


class Gravel(G.itemclass):
    def getName(self):
        return "minecraft:gravel"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/GRAVEL.png"


G.itemhandler.register(Gravel)
