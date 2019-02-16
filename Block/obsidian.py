import globals as G
import mathhelper
import modsystem.ModLoader


class Obsidian(G.blockclass):
    """class for obsidian"""
    def getName(self):
        return "minecraft:obsidian"

    def getModelFile(self, inst):
        return "minecraft:obsidian"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating obsidian")
def register():
    G.blockhandler.register(Obsidian)

