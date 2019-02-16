import globals as G

"""class for sand"""
class Sand(G.itemclass):
    def getName(self):
        return "minecraft:sand"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/SAND#0.png"

G.itemhandler.register(Sand)

"""class for redsand"""
class RedSand(G.itemclass):
    def getName(self):
        return "minecraft:red_sand"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/SAND#1.png"

G.itemhandler.register(RedSand)