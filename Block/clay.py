import globals as G
import mathhelper
import modsystem.ModLoader


class Clay(G.iblockclass):
    """class for clay"""

    def getName(self):
        return "minecraft:clay_block"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating clay"
)
def register():
    G.blockhandler.register(Clay)
