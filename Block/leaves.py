import globals as G
import mathhelper
import modsystem.ModLoader


class AcaciaLeave(G.blockclass):
    """class for acacia leave"""
    def getName(self):
        return "minecraft:acacia_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "acacia_leaves"

    def getDrop(self, inst):
        return {}

class BirchLeave(G.blockclass):
    """class for birch leave"""
    def getName(self):
        return "minecraft:birch_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "birch_leaves"

    def getDrop(self, inst):
        return {}


class DarkOakLeave(G.blockclass):
    """class for dark oak leave"""
    def getName(self):
        return "minecraft:dark_oak_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "dark_oak_leaves"

    def getDrop(self, inst):
        return {}


class JungleLeave(G.blockclass):
    """class for jungle leave"""
    def getName(self):
        return "minecraft:jungle_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "jungle_leaves"

    def getDrop(self, inst):
        return {}


class OakLeave(G.blockclass):
    """class for oak leave"""
    def getName(self):
        return "minecraft:oak_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "oak_leaves"

    def getDrop(self, inst):
        return {}


class SpruceLeave(G.blockclass):
    """class for spruce leave"""
    def getName(self):
        return "minecraft:spruce_leaves"

    def getModelFile(self, inst):
        return "minecraft:leaves"

    def getStateName(self, inst):
        return "spruce_leaves"

    def getDrop(self, inst):
        return {}


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating leaves")
def register():
    G.blockhandler.register(SpruceLeave)
    G.blockhandler.register(OakLeave)
    G.blockhandler.register(JungleLeave)
    G.blockhandler.register(DarkOakLeave)
    G.blockhandler.register(BirchLeave)
    G.blockhandler.register(AcaciaLeave)
