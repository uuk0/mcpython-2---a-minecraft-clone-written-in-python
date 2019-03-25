import globals as G
import mathhelper
import modsystem.ModLoader


class SlimeBlock(G.iblockclass):
    """class for slime block"""
    def getName(self):
        return "minecraft:slime_block"

    def getModelFile(self, inst):
        return "minecraft:slime_block"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating slime block")
def register():
    G.blockhandler.register(SlimeBlock)

