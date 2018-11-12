import globals as G

"""class for dirt"""
class Dirt(G.itemclass):
    def getName(self):
        return "minecraft:dirt"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/DIRT#0.png"

G.itemhandler.register(Dirt)