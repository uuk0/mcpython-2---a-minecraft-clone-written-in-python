import globals as G
import mathhelper
import modsystem.ModLoader


class NetherWartBlock(G.iblockclass):
    def getName(self):
        return "minecraft:nether_wart_block"

    def getModelFile(self, inst):
        return "minecraft:nether_wart_block"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating nether wart block")
def register():
    G.blockhandler.register(NetherWartBlock)

