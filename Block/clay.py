import globals as G
import mathhelper
import modsystem.ModLoader


class Clay(G.blockclass):
    """class for clay"""
    def getName(self):
        return "minecraft:clay"

    def getModelFile(self, inst):
        return "minecraft:clay"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating clay")
def register():
    G.blockhandler.register(Clay)

