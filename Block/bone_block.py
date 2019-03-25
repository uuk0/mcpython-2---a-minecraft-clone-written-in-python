import globals as G
import modsystem.ModLoader


class BoneBlock(G.iblockclass):
    """class for bone block"""

    def getName(self):
        return "minecraft:bone_block"

    def getModelFile(self, inst):
        return "minecraft:bone_block"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating bone block")
def register():
    G.blockhandler.register(BoneBlock)

