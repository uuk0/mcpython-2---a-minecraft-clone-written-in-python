import globals as G
import mathhelper
import modsystem.ModLoader


class MagmaBlock(G.blockclass):
    def getName(self):
        return "minecraft:magma_block"

    def getModelFile(self, inst):
        return "minecraft:magma_block"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating magma block")
def register():
    G.blockhandler.register(MagmaBlock)

