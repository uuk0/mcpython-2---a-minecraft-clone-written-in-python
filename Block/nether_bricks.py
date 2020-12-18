import globals as G
import mathhelper
import modsystem.ModLoader


class NetherBricks(G.iblockclass):
    def getName(self):
        return "minecraft:nether_bricks"

    def getModelFile(self, inst):
        return "minecraft:nether_bricks"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating nether bricks",
)
def register():
    G.blockhandler.register(NetherBricks)
