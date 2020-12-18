import globals as G
import mathhelper
import modsystem.ModLoader


class PurpurBlock(G.iblockclass):
    def getName(self):
        return "minecraft:purpur_block"

    def getModelFile(self, inst):
        return "minecraft:purpur_block"

    def getStateName(self, inst):
        return "minecraft:purpur_block"


class PurpurPillar(G.iblockclass):
    def getName(self):
        return "minecraft:purpur_pillar"

    def getModelFile(self, inst):
        return "minecraft:purpur_block"

    def getStateName(self, inst):
        return "minecraft:purpur_pillar"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating purpur block",
)
def register():
    G.blockhandler.register(PurpurBlock)
    G.blockhandler.register(PurpurPillar)
