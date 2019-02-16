import globals as G
import mathhelper
import modsystem.ModLoader


class Bedrock(G.blockclass):
    """class for bedrock"""
    def getName(self):
        return "minecraft:bedrock"

    def getModelFile(self, inst):
        return "minecraft:bedrock"

    def isBrakeAble(self, inst):
        return False


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating bedrock")
def register():
    G.blockhandler.register(Bedrock)

