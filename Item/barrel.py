import globals as G

"""class for barrel"""
class Barrel(G.itemclass):
    def getName(self):
        return "minecraft:barrel"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Barrel.png"

G.itemhandler.register(Barrel)