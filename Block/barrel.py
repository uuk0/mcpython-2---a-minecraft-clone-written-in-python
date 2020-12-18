import globals as G
import modsystem.ModLoader


class Barrel(G.iblockclass):
    """class for barrel
    todo: add inventory"""

    def getName(self):
        return "minecraft:barrel"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating barrel"
)
def register():
    """
    registrate the block/barrel-object
    """
    G.blockhandler.register(Barrel)
