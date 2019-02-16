import globals as G

"""class for ice"""
class Ice(G.itemclass):
    def getName(self):
        return "minecraft:ice"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/ICE.png"

G.itemhandler.register(Ice)

"""class for packed ice"""
class PackedIce(G.itemclass):
    def getName(self):
        return "minecraft:packed_ice"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/PACKED_ICE.png"

G.itemhandler.register(PackedIce)

"""class for blue ice"""
class BlueIce(G.itemclass):
    def getName(self):
        return "minecraft:blue_ice"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/BLUE_ICE.png"

G.itemhandler.register(BlueIce)