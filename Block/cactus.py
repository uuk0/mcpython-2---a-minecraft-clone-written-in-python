import globals as G
import mathhelper
import entity.boxmodel as boxmodel
import modsystem.ModLoader


class Cactus(G.blockclass):
    """class for cactus"""
    def getName(self):
        return "minecraft:cactus"

    def isFullSide(self, inst, side):
        return False

    def _getDefaultData(self, inst):
        return {"shown":False,
                "shownid":-1,
                "boxmodels":None}


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating cactus")
def register():
    G.blockhandler.register(Cactus)

