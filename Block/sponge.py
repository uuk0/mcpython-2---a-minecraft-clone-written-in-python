import globals as G
import mathhelper
import modsystem.ModLoader


class Sponge(G.iblockclass):
    def getName(self):
        return "minecraft:sponge"

    def getModelFile(self, inst):
        return "minecraft:sponge"

    def getStateName(self, inst):
        return "sponge"


class WetSponge(G.iblockclass):
    def getName(self):
        return "minecraft:wet_sponge"

    def getModelFile(self, inst):
        return "minecraft:sponge"

    def getStateName(self, inst):
        return "wet_sponge"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating sponge")
def register():
    G.blockhandler.register(Sponge)
    G.blockhandler.register(WetSponge)

