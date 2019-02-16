import globals as G

"""class for AcaciaLog"""
class AcaciaLog(G.itemclass):
    def getName(self):
        return "minecraft:acacia_log"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/LOG2#0.png"

G.itemhandler.register(AcaciaLog)

"""class for AcaciaLog"""
class BirchLog(G.itemclass):
    def getName(self):
        return "minecraft:birch_log"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/LOG#2.png"

G.itemhandler.register(BirchLog)