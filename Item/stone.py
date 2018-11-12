import globals as G

"""class for stone"""
class Stone(G.itemclass):
    def getName(self):
        return "minecraft:stone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/STONE.png"

G.itemhandler.register(Stone)

"""class for cobbelstone"""
class CobbelStone(G.itemclass):
    def getName(self):
        return "minecraft:cobbelstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/COBBLESTONE.png"

G.itemhandler.register(CobbelStone)

"""class for stonebrick"""
class StoneBrick(G.itemclass):
    def getName(self):
        return "minecraft:stone_brick"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/STONEBRICK#0.png"

G.itemhandler.register(StoneBrick)

"""class for mossy stonebrick"""
class MossyStoneBrick(G.itemclass):
    def getName(self):
        return "minecraft:mossy_stone_brick"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/STONEBRICK.png"

G.itemhandler.register(MossyStoneBrick)

"""class for mossy stonebrick"""
class CrackedStoneBrick(G.itemclass):
    def getName(self):
        return "minecraft:cracked_stone_brick"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/STONEBRICK#2.png"

G.itemhandler.register(CrackedStoneBrick)

"""class for chiseled stonebrick"""
class ChiseledStoneBrick(G.itemclass):
    def getName(self):
        return "minecraft:chiseled_stone_brick"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/STONEBRICK#3.png"

G.itemhandler.register(ChiseledStoneBrick)

"""class for mossy cobbelstone"""
class MossyCobbelStone(G.itemclass):
    def getName(self):
        return "minecraft:mossy_cobbelstone"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/MOSSY_COBBLESTONE.png"

G.itemhandler.register(MossyCobbelStone)

"""class for andesite"""
class Andesite(G.itemclass):
    def getName(self):
        return "minecraft:andesite"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Andesite.png"

G.itemhandler.register(Andesite)

"""class for polished andesite"""
class PolishedAndesite(G.itemclass):
    def getName(self):
        return "minecraft:polished_andesite"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Polished_Andesite.png"

G.itemhandler.register(PolishedAndesite)


"""class for granite"""
class Granite(G.itemclass):
    def getName(self):
        return "minecraft:granite"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Granite.png"

G.itemhandler.register(Granite)

"""class for polished granite"""
class PolishedGranite(G.itemclass):
    def getName(self):
        return "minecraft:polished_granite"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Polished_Granite.png"

G.itemhandler.register(PolishedGranite)


"""class for diorite"""
class Diorite(G.itemclass):
    def getName(self):
        return "minecraft:diorite"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Diorite.png"

G.itemhandler.register(Diorite)

"""class for polished diorite"""
class PolishedDiorite(G.itemclass):
    def getName(self):
        return "minecraft:polished_diorite"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/Polished_Diorite.png"

G.itemhandler.register(PolishedDiorite)