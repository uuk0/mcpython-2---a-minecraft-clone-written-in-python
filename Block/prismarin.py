import globals as G
import mathhelper
import modsystem.ModLoader


class DarkPrismarin(G.iblockclass):
    """class for clay"""

    def getName(self):
        return "minecraft:dark_prismarin"

    def getModelFile(self, inst):
        return "minecraft:prismarin"

    def getStateName(self, inst):
        return "dark_prismarine"


class Prismarin(G.iblockclass):
    """class for clay"""

    def getName(self):
        return "minecraft:prismarin"

    def getModelFile(self, inst):
        return "minecraft:prismarin"

    def getStateName(self, inst):
        return "prismarine"


class PrismarinBrick(G.iblockclass):
    """class for clay"""

    def getName(self):
        return "minecraft:prismarin_brick"

    def getModelFile(self, inst):
        return "minecraft:prismarin"

    def getStateName(self, inst):
        return "prismarine_brick"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating prismarin",
)
def register():
    G.blockhandler.register(DarkPrismarin)
    G.blockhandler.register(Prismarin)
    G.blockhandler.register(PrismarinBrick)
