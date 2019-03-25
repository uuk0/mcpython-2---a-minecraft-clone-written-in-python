import globals as G
import mathhelper
import modsystem.ModLoader


class Pumpkin(G.iblockclass):
    def getName(self):
        return "minecraft:pumpkin"

    def getModelFile(self, inst):
        return "minecraft:pumpkin"


class CarvedPumpkin(G.iblockclass):
    def getName(self):
        return "minecraft:pumpkin"

    def getModelFile(self, inst):
        return "minecraft:pumpkin"

    def getStateName(self, inst):
        return "carved"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating pumpkin")
def register():
    G.blockhandler.register(Pumpkin)
    G.blockhandler.register(CarvedPumpkin)

