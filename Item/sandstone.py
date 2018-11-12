import globals as G

"""class for sandstone"""
class Sandstone(G.itemclass):
    def getName(self):
        return "minecraft:sandstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/SANDSTONE#0.png"

G.itemhandler.register(Sandstone)

"""class for chiseled sandstone"""
class ChiseledSandstone(G.itemclass):
    def getName(self):
        return "minecraft:chiseled_sandstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/SANDSTONE#1.png"

G.itemhandler.register(ChiseledSandstone)

"""class for chiseled sandstone"""
class CutSandstone(G.itemclass):
    def getName(self):
        return "minecraft:cut_sandstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/SANDSTONE#2.png"

G.itemhandler.register(CutSandstone)

"""class for red sandstone"""
class RedSandstone(G.itemclass):
    def getName(self):
        return "minecraft:red_sandstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/RED_SANDSTONE.png"

G.itemhandler.register(RedSandstone)

"""class for red chiseled sandstone"""
class RedChiseledSandStone(G.itemclass):
    def getName(self):
        return "minecraft:red_chiseled_sandstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/RED_SANDSTONE#1.png"

G.itemhandler.register(RedChiseledSandStone)

"""class for red chiseled sandstone"""
class RedCutSandStone(G.itemclass):
    def getName(self):
        return "minecraft:red_cut_sandstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/RED_SANDSTONE#2.png"

G.itemhandler.register(RedCutSandStone)

