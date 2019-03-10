import globals as G
import mathhelper
import modsystem.ModLoader


class Melon(G.blockclass):
    def getName(self):
        return "minecraft:melon"

    def getModelFile(self, inst):
        return "minecraft:melon"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating melon")
def register():
    G.blockhandler.register(Melon)

