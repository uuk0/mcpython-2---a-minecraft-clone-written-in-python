import globals as G
import mathhelper
import modsystem.ModLoader


class ISandStone(G.iblockclass):
    def getModelFile(self, inst):
        return "minecraft:sandstone"

    def getStateName(self, inst):
        return self.getName().split(":")[1]


class SandStone(ISandStone):
    """class for sandstone"""
    def getName(self):
        return "minecraft:sandstone"


class ChiseledSandStone(ISandStone):
    """class for chiseled sandstone"""
    def getName(self):
        return "minecraft:chiseled_sandstone"


class CutSandStone(ISandStone):
    """class for cut sandstone"""
    def getName(self):
        return "minecraft:cut_sandstone"


class RedSandStone(ISandStone):
    """class for red sandstone"""
    def getName(self):
        return "minecraft:red_sandstone"


class RedChiseledSandStone(ISandStone):
    """class for red chiseled sandstone"""
    def getName(self):
        return "minecraft:red_chiseled_sandstone"


class RedCutSandStone(ISandStone):
    """class for red cut sandstone"""
    def getName(self):
        return "minecraft:red_cut_sandstone"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating sandstones")
def register():
    G.blockhandler.register(RedCutSandStone)
    G.blockhandler.register(RedChiseledSandStone)
    G.blockhandler.register(RedSandStone)
    G.blockhandler.register(CutSandStone)
    G.blockhandler.register(ChiseledSandStone)
    G.blockhandler.register(SandStone)

