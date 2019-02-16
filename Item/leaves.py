import globals as G

"""class for AcaciaLeave"""
class AcaciaLeave(G.itemclass):
    def getName(self):
        return "minecraft:acacia_leaves"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/LEAVES.png"

G.itemhandler.register(AcaciaLeave)