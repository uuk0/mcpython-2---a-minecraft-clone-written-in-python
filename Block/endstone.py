import globals as G
import mathhelper
import modsystem.ModLoader


class Endstone(G.blockclass):
    """class for endstone"""
    def getName(self):
        return "minecraft:endstone"

    def getModelFile(self, inst):
        return "minecraft:endstone"

    def getStateName(self, inst):
        return "endstone"


class EndstoneBrick(G.blockclass):
    """class for endstonebrick"""
    def getName(self):
        return "minecraft:endstone_brick"

    def getModelFile(self, inst):
        return "minecraft:endstone"

    def getStateName(self, inst):
        return "endstonebrick"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating endstone & endstonebrick")
def register():
    G.blockhandler.register(EndstoneBrick)
    G.blockhandler.register(Endstone)

