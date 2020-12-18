import globals as G
import mathhelper
import modsystem.ModLoader


class AcaciaLeave(G.iblockclass):
    """class for acacia leave"""

    def getName(self):
        return "minecraft:acacia_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "acacia_leaves"

    def getDrop(self, inst):
        return {}

    def isFullBlock(self):
        return False


class BirchLeave(G.iblockclass):
    """class for birch leave"""

    def getName(self):
        return "minecraft:birch_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "birch_leaves"

    def getDrop(self, inst):
        return {}

    def isFullBlock(self):
        return False


class DarkOakLeave(G.iblockclass):
    """class for dark oak leave"""

    def getName(self):
        return "minecraft:dark_oak_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "dark_oak_leaves"

    def getDrop(self, inst):
        return {}

    def isFullBlock(self):
        return False


class JungleLeave(G.iblockclass):
    """class for jungle leave"""

    def getName(self):
        return "minecraft:jungle_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "jungle_leaves"

    def getDrop(self, inst):
        return {}

    def isFullBlock(self):
        return False


class OakLeave(G.iblockclass):
    """class for oak leave"""

    def getName(self):
        return "minecraft:oak_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "oak_leaves"

    def getDrop(self, inst):
        return {}

    def isFullBlock(self):
        return False


class SpruceLeave(G.iblockclass):
    """class for spruce leave"""

    def getName(self):
        return "minecraft:spruce_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "spruce_leaves"

    def getDrop(self, inst):
        return {}

    def isFullBlock(self):
        return False


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating leaves"
)
def register():
    G.blockhandler.register(SpruceLeave)
    G.blockhandler.register(OakLeave)
    G.blockhandler.register(JungleLeave)
    G.blockhandler.register(DarkOakLeave)
    G.blockhandler.register(BirchLeave)
    G.blockhandler.register(AcaciaLeave)
