import globals as G
import mathhelper
import modsystem.ModLoader


class Glass(G.blockclass):
    """class for brick"""
    def getName(self):
        return "minecraft:glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False


class BlackStained(G.blockclass):
    """class for brick"""
    def getName(self):
        return "minecraft:black_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "black_stained_glass"


class blueStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:blue_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "blue_stained_glass"


class brownStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:brown_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "brown_stained_glass"


class cyanStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:cyan_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "cyan_stained_glass"


class grayStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:gray_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "gray_stained_glass"


class greenStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:green_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "green_stained_glass"


class light_blueStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:light_blue_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "light_blue_stained_glass"


class light_grayStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:light_gray_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "light_gray_stained_glass"


class limeStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:lime_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "lime_stained_glass"


class magentaStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:magenta_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "magenta_stained_glass"


class orangeStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:orange_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "orange_stained_glass"


class pinkStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:pink_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "pink_stained_glass"


class purpleStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:purple_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "purple_stained_glass"


class redStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:red_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "red_stained_glass"


class whiteStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:white_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "white_stained_glass"


class yellowStained(G.blockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:yellow_stained_glass"

    def getModelFile(self, inst):
        return "minecraft:glass"

    def isFullBlock(self):
        return False

    def getStateName(self, inst):
        return "yellow_stained_glass"


local = locals()


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating glass")
def register(*args):
    # G.blockhandler.register(Glass)

    for e in local.values():
        try:
            if issubclass(e, G.blockclass):
                G.blockhandler.register(e)
        except TypeError:
            pass

