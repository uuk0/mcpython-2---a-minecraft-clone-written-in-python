import globals as G

"""class for glowstone"""
class Glowstone(G.itemclass):
    def getName(self):
        return "minecraft:glowstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/GLOWSTONE.png"

G.itemhandler.register(Glowstone)

"""class for glowstone"""
class GlowstoneDust(G.itemclass):
    def getName(self):
        return "minecraft:glowstone_dust"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/glowstone_dust.png"

    def hasBlock(self):
        return False

G.itemhandler.register(GlowstoneDust)