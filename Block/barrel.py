import globals as G
import mathhelper
import modsystem.ModLoader


class Barrel(G.blockclass):
    """class for barrel"""
    def getName(self):
        return "minecraft:barrel"

    def getModelFile(self, inst):
        return "minecraft:barrel"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating barrel")
def register():
    G.blockhandler.register(Barrel)

