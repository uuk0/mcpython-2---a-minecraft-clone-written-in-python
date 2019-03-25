import globals as G
import modsystem.ModLoader


class Bedrock(G.iblockclass):
    """class for bedrock"""

    def getName(self):
        return "minecraft:none"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating none-block")
def register():
    """
    register the block/none-class
    """
    G.blockhandler.register(Bedrock)

