import globals as G
import mathhelper
import modsystem.ModLoader


class Brick(G.blockclass):
    """class for brick"""
    def getName(self):
        return "minecraft:brick"

    def getModelFile(self, inst):
        return "minecraft:brick"

    def isBrakeAble(self, inst):
        return True


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating brick")
def register():
    G.blockhandler.register(Brick)

