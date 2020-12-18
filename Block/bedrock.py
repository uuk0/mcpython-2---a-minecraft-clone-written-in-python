import globals as G
import modsystem.ModLoader


class Bedrock(G.iblockclass):
    """class for bedrock"""

    def getName(self):
        return "minecraft:bedrock"

    def isBrakeAbleInGamemode0(self, inst):
        return False


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating bedrock",
)
def register():
    """
    register the block/bedrock-class
    """
    G.blockhandler.register(Bedrock)
