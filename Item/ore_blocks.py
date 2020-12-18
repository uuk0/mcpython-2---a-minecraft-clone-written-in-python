import globals as G

"""class for coal block"""


class CoalBlock(G.itemclass):
    def getName(self):
        return "minecraft:coal_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/COAL_BLOCK.png"


G.itemhandler.register(CoalBlock)

"""class for diamond block"""


class DiamondBlock(G.itemclass):
    def getName(self):
        return "minecraft:diamond_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/DIAMOND_BLOCK.png"


G.itemhandler.register(DiamondBlock)

"""class for emerald block"""


class EmeraldBlock(G.itemclass):
    def getName(self):
        return "minecraft:emerald_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/EMERALD_BLOCK.png"


G.itemhandler.register(EmeraldBlock)

"""class for gold block"""


class GoldBlock(G.itemclass):
    def getName(self):
        return "minecraft:gold_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/GOLD_BLOCK.png"


G.itemhandler.register(GoldBlock)

"""class for iron block"""


class IronBlock(G.itemclass):
    def getName(self):
        return "minecraft:iron_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/IRON_BLOCK.png"


G.itemhandler.register(IronBlock)

"""class for lapis block"""


class LapisBlock(G.itemclass):
    def getName(self):
        return "minecraft:lapis_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/LAPIS_BLOCK.png"


G.itemhandler.register(LapisBlock)

"""class for quartz block"""


class QuartzBlock(G.itemclass):
    def getName(self):
        return "minecraft:quartz_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/QUARTZ_BLOCK#0.png"


G.itemhandler.register(QuartzBlock)

"""class for chiseled quartz block"""


class ChiseledQuartzBlock(G.itemclass):
    def getName(self):
        return "minecraft:chiseled_quartz_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/QUARTZ_BLOCK#1.png"


G.itemhandler.register(ChiseledQuartzBlock)

"""class for quartz pillar"""


class QuartzPillar(G.itemclass):
    def getName(self):
        return "minecraft:quartz_pillar"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/QUARTZ_BLOCK#2.png"


G.itemhandler.register(QuartzPillar)

"""class for redstone block"""


class RedstoneBlock(G.itemclass):
    def getName(self):
        return "minecraft:redstone_block"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/REDSTONE_BLOCK.png"


G.itemhandler.register(RedstoneBlock)
