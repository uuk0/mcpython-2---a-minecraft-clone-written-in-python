import globals as G

"""class for acacia log"""
class AcaciaLog(G.itemclass):
    def getName(self):
        return "minecraft:acacia_plank"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/acacia_plank.png"

G.itemhandler.register(AcaciaLog)

"""class for birch log"""
class AcaciaLog(G.itemclass):
    def getName(self):
        return "minecraft:birch_plank"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Birch_Planks.png"

G.itemhandler.register(AcaciaLog)

