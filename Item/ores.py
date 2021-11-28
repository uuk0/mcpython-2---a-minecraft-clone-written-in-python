import globals as G

"""class for coalore"""


class CoalOre(G.itemclass):
    def getName(self):
        return "minecraft:coal_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/COAL_ORE.png"


G.itemhandler.register(CoalOre)

"""class for diamondore"""


class DiamondOre(G.itemclass):
    def getName(self):
        return "minecraft:diamond_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/DIAMOND_ORE.png"


G.itemhandler.register(DiamondOre)

"""class for emeraldore"""


class EmeraldOre(G.itemclass):
    def getName(self):
        return "minecraft:emerald_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/EMERALD_ORE.png"


G.itemhandler.register(EmeraldOre)

"""class for goldore"""


class GoldOre(G.itemclass):
    def getName(self):
        return "minecraft:gold_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/GOLD_ORE.png"


G.itemhandler.register(GoldOre)

"""class for ironore"""


class IronOre(G.itemclass):
    def getName(self):
        return "minecraft:iron_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/IRON_ORE.png"


G.itemhandler.register(IronOre)

"""class for lapisore"""


class LapisOre(G.itemclass):
    def getName(self):
        return "minecraft:lapis_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/LAPIS_ORE.png"


G.itemhandler.register(LapisOre)

"""class for netherquartz"""


class NetherQuartz(G.itemclass):
    def getName(self):
        return "minecraft:nether_quartz_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/QUARTZ_ORE.png"


G.itemhandler.register(NetherQuartz)

"""class for redstoneore"""


class RedstoneOre(G.itemclass):
    def getName(self):
        return "minecraft:redstone_ore"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/REDSTONE_ORE.png"


G.itemhandler.register(RedstoneOre)
