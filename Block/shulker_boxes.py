import globals as G
import mathhelper
import modsystem.ModLoader


class ShulkerBox(G.blockclass):
    def getName(self):
        return "minecraft:shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False


class BlackShulkerBox(G.blockclass):
    """class for brick"""
    def getName(self):
        return "minecraft:black_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "black_shulker_box"


class blueShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:blue_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "blue_shulker_box"


class brownShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:brown_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "brown_shulker_box"


class cyanShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:cyan_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "cyan_shulker_box"


class grayShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:gray_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "gray_shulker_box"


class greenShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:green_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "green_shulker_box"


class light_blueShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:light_blue_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "light_blue_shulker_box"


class light_grayShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:light_gray_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "light_gray_shulker_box"


class limeShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:lime_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "lime_shulker_box"


class magentaShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:magenta_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "magenta_shulker_box"


class orangeShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:orange_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "orange_shulker_box"


class pinkShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:pink_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "pink_shulker_box"


class purpleShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:purple_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "purple_shulker_box"


class redShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:red_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "red_shulker_box"


class whiteShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:white_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "white_shulker_box"


class yellowShulkerBox(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:yellow_shulker_box"

    def getModelFile(self, inst):
        return "minecraft:shulker_box"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "yellow_shulker_box"


local = locals()


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating shulker boxes")
def register(*args):
    # G.blockhandler.register(Glass)

    for e in local.values():
        try:
            if issubclass(e, G.blockclass):
                G.blockhandler.register(e)
        except TypeError:
            pass

