import globals as G
import mathhelper
import modsystem.ModLoader
import notations


class Grass(G.iblockclass):
    """class for grass"""

    oredictnames = [notations.OreDictItems.DIRT]

    def getName(self):
        return "minecraft:grass"

    """returns dirt as drop"""

    def getDrop(self, inst):
        return {"minecraft:dirt": 1}

    def getBrakeSoundFile(self, inst):
        return [
            G.local + "/assets/minecraft/sounds/brake/grass1.wma",
            G.local + "/assets/minecraft/sounds/brake/grass2.wma",
            G.local + "/assets/minecraft/sounds/brake/grass3.wma",
            G.local + "/assets/minecraft/sounds/brake/grass4.wma",
        ]


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating grass"
)
def register():
    G.blockhandler.register(Grass)
