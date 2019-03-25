import globals as G
import mathhelper
import notations
import modsystem.ModLoader


class IPlank(G.iblockclass):
    oredictnames = [notations.OreDictItems.WOOD_PLANK]

    def getModelFile(self, inst):
        return "minecraft:plank"

    def getStateName(self, inst):
        return self.getName().split(":")[1]


class AcaciaPlank(IPlank):
    """class for acacia plank"""
    def getName(self):
        return "minecraft:acacia_plank"


class BirchPlank(IPlank):
    """class for birch plank"""
    def getName(self):
        return "minecraft:birch_plank"


class DarkOakPlank(IPlank):
    """class for dark oak plank"""
    def getName(self):
        return "minecraft:dark_oak_plank"


class JunglePlank(IPlank):
    """class for jungle plank"""
    def getName(self):
        return "minecraft:jungle_plank"


class OakPlank(IPlank):
    """class for oak plank"""
    def getName(self):
        return "minecraft:oak_plank"


class SprucePlank(IPlank):
    """class for spruce plank"""
    def getName(self):
        return "minecraft:spruce_plank"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating planks")
def register():
    G.blockhandler.register(SprucePlank)
    G.blockhandler.register(OakPlank)
    G.blockhandler.register(JunglePlank)
    G.blockhandler.register(DarkOakPlank)
    G.blockhandler.register(BirchPlank)
    G.blockhandler.register(AcaciaPlank)

