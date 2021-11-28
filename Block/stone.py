import globals as G
import mathhelper
import modsystem.ModLoader
import notations


class Stone(G.iblockclass):
    """class for stone"""

    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:stone"

    def getDrop(self, inst):
        return {"minecraft:cobbelstone": 1}


class CobbelStone(G.iblockclass):
    """class for cobbelstone"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.COBBELSTONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:cobbelstone"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "cobbelstone"


class StoneBrick(G.iblockclass):
    """class for stonebrick"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "stone_brick"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class MossyStoneBrick(G.iblockclass):
    """class for mossy stone brick"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:mossy_stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "mossy_stone_brick"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class CrackedStoneBrick(G.iblockclass):
    """class for cracked stone brick"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:cracked_stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "cracked_stone_brick"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class ChiseledStoneBrick(G.iblockclass):
    """class for chiseled stone brick"""

    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:chiseled_stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "chiseled_stone_brick"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class MossyCobbelStone(G.iblockclass):
    """class for mossy cobbelstone"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.COBBELSTONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:mossy_cobbelstone"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "mossy_cobbelstone"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class Andesite(G.iblockclass):
    """class for andesite"""

    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:andesite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "andesite"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class PolishedAndesite(G.iblockclass):
    """class for polished andesite"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_andesite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "polished_andesite"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class Granite(G.iblockclass):
    """class for granite"""

    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:granite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "granite"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class PolishedGranite(G.iblockclass):
    """class for polished granite"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_granite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "polished_granite"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class Diorite(G.iblockclass):
    """class for diorite"""

    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:diorite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "diorite"

    def isBrakeAbleInGamemode0(self, inst):
        return True


class PolishedDiorite(G.iblockclass):
    """class for polished diorite"""

    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_diorite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "polished_diorite"

    def isBrakeAbleInGamemode0(self, inst):
        return True


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating stones"
)
def register():
    G.blockhandler.register(PolishedDiorite)
    G.blockhandler.register(Diorite)
    G.blockhandler.register(PolishedGranite)
    G.blockhandler.register(Granite)
    G.blockhandler.register(PolishedAndesite)
    G.blockhandler.register(Andesite)
    G.blockhandler.register(MossyCobbelStone)
    G.blockhandler.register(ChiseledStoneBrick)
    G.blockhandler.register(CrackedStoneBrick)
    G.blockhandler.register(MossyStoneBrick)
    G.blockhandler.register(StoneBrick)
    G.blockhandler.register(CobbelStone)
    G.blockhandler.register(Stone)
