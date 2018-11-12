import globals as G

"""class for tnt"""
class Tnt(G.itemclass):
    def getName(self):
        return "minecraft:tnt"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/TNT.png"

G.itemhandler.register(Tnt)