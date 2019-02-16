import globals as G
import mathhelper
import notations
import modsystem.ModLoader


class Stone(G.blockclass):
    """class for stone"""
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:stone"

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:cobbelstone":1}

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "stone"


class CobbelStone(G.blockclass):
    """class for cobbelstone"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.COBBELSTONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:cobbelstone"

    def isBrakeAble(self, inst):
        return True

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "cobbelstone"


class StoneBrick(G.blockclass):
    """class for stonebrick"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "stone_brick"

    def isBrakeAble(self, inst):
        return True


class MossyStoneBrick(G.blockclass):
    """class for mossy stone brick"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:mossy_stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "mossy_stone_brick"

    def isBrakeAble(self, inst):
        return True


class CrackedStoneBrick(G.blockclass):
    """class for cracked stone brick"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:cracked_stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "cracked_stone_brick"

    def isBrakeAble(self, inst):
        return True


class ChiseledStoneBrick(G.blockclass):
    """class for chiseled stone brick"""
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:chiseled_stone_brick"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "chiseled_stone_brick"

    def isBrakeAble(self, inst):
        return True


class MossyCobbelStone(G.blockclass):
    """class for mossy cobbelstone"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.COBBELSTONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:mossy_cobbelstone"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "mossy_cobbelstone"

    def isBrakeAble(self, inst):
        return True


class Andesite(G.blockclass):
    """class for andesite"""
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:andesite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "andesite"

    def isBrakeAble(self, inst):
        return True


class PolishedAndesite(G.blockclass):
    """class for polished andesite"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_andesite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "polished_andesite"

    def isBrakeAble(self, inst):
        return True


class Granite(G.blockclass):
    """class for granite"""
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:granite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "granite"

    def isBrakeAble(self, inst):
        return True


class PolishedGranite(G.blockclass):
    """class for polished granite"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_granite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "polished_granite"

    def isBrakeAble(self, inst):
        return True


class Diorite(G.blockclass):
    """class for diorite"""
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:diorite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "diorite"

    def isBrakeAble(self, inst):
        return True


class PolishedDiorite(G.blockclass):
    """class for polished diorite"""
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_diorite"

    def getModelFile(self, inst):
        return "minecraft:stone"

    def getStateName(self, inst):
        return "polished_diorite"

    def isBrakeAble(self, inst):
        return True


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating stones")
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

