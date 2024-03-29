import globals as G
import mathhelper
import modsystem.ModLoader
import notations


class Dirt(G.iblockclass):
    """class for dirt"""

    oredictnames = [notations.OreDictItems.DIRT]

    def getName(self):
        return "minecraft:dirt"

    def getBrakeSoundFile(self, inst):
        return [
            G.local + "/assets/minecraft/sounds/brake/grass1.wma",
            G.local + "/assets/minecraft/sounds/brake/grass2.wma",
            G.local + "/assets/minecraft/sounds/brake/grass3.wma",
            G.local + "/assets/minecraft/sounds/brake/grass4.wma",
        ]


class CoarseDirt(Dirt):
    """class for coarse dirt"""

    def getName(self):
        return "minecraft:coarse_dirt"

    def getStateName(self, inst):
        return "coarse_dirt"


class Mycelium(Dirt):
    def getName(self):
        return "minecraft:mycelium"

    def getStateName(self, inst):
        return "mycelium"


class Podzol(Dirt):
    def getName(self):
        return "minecraft:podzol"

    def getStateName(self, inst):
        return "podzol"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating dirt & coarse dirt",
)
def register():
    G.blockhandler.register(CoarseDirt)
    G.blockhandler.register(Dirt)
    G.blockhandler.register(Mycelium)
    G.blockhandler.register(Podzol)
