import globals as G
import mathhelper
import modsystem.ModLoader


class RedNetherBrick(G.blockclass):
    def getName(self):
        return "minecraft:red_nether_bricks"

    def getModelFile(self, inst):
        return "minecraft:red_nether_bricks"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating red nether brick")
def register():
    G.blockhandler.register(RedNetherBrick)

