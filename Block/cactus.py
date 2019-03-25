import globals as G
import modsystem.ModLoader


class Cactus(G.iblockclass):
    """class for cactus
    todo: add boxmodel for these"""

    def getName(self):
        return "minecraft:cactus"

    def isFullSide(self, inst, side):
        return False


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating cactus")
def register():
    G.blockhandler.register(Cactus)

