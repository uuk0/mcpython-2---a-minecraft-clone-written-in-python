import globals as G
import mathhelper
import modsystem.ModLoader


class Glowstone(G.iblockclass):
    """class for glowstone"""

    def getName(self):
        return "minecraft:glowstone"

    def getModelFile(self, inst):
        return "minecraft:glowstone"

    def isBrakeAbleInGamemode0(self, inst):
        return True


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating glowstone",
)
def register():
    G.blockhandler.register(Glowstone)
