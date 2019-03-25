import globals as G
import mathhelper
import modsystem.ModLoader


class NetherRack(G.iblockclass):
    """class for obsidian"""
    def getName(self):
        return "minecraft:netherrack"

    def getModelFile(self, inst):
        return "minecraft:netherrack"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating netherrack")
def register():
    G.blockhandler.register(NetherRack)

