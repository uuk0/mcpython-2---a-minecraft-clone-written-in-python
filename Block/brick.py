import globals as G
import modsystem.ModLoader


class Brick(G.iblockclass):
    """class for brick"""

    def getName(self):
        return "minecraft:brick"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating brick")
def register():
    G.blockhandler.register(Brick)

