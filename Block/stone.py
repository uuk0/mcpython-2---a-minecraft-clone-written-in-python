import globals as G
import mathhelper
import notations

"""class for stone"""
class Stone(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:stone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/stone"

    def getAllTexturFiles(self):
        return ["minecraft/stone"]

    def isBrakeAble(self, inst):
        return True

    """returns the drop: cobbelstone"""
    def getDrop(self, inst):
        return {"minecraft:cobbelstone":1}

G.blockhandler.register(Stone)

"""class for cobbelstone"""
class CobbelStone(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.COBBELSTONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:cobbelstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/cobbelstone"

    def getAllTexturFiles(self):
        return ["minecraft/cobbelstone"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(CobbelStone)

"""class for stonebrick"""
class StoneBrick(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:stone_brick"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/stone_brick"

    def getAllTexturFiles(self):
        return ["minecraft/stone_brick"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(StoneBrick)

"""class for mossy stone brick"""
class MossyStoneBrick(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:mossy_stone_brick"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/mossy_stone_brick"

    def getAllTexturFiles(self):
        return ["minecraft/mossy_stone_brick"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(MossyStoneBrick)

"""class for cracked stone brick"""
class CrackedStoneBrick(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.STONEBRICK]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:cracked_stone_brick"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/cracked_stone_brick"

    def getAllTexturFiles(self):
        return ["minecraft/cracked_stone_brick"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(CrackedStoneBrick)

"""class for chiseled stone brick"""
class ChiseledStoneBrick(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:chiseled_stone_brick"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/chiseled_stone_brick"

    def getAllTexturFiles(self):
        return ["minecraft/chiseled_stone_brick"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(ChiseledStoneBrick)

"""class for mossy cobbel stone"""
class MossyCobbelStone(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.COBBELSTONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:mossy_cobbelstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/mossy_cobbelstone"

    def getAllTexturFiles(self):
        return ["minecraft/mossy_cobbelstone"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(MossyCobbelStone)


"""class for andesite"""
class Andesite(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:andesite"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/andesite"

    def getAllTexturFiles(self):
        return ["minecraft/andesite"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(Andesite)

"""class for polished andesite"""
class PolishedAndesite(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_andesite"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/polished_andesite"

    def getAllTexturFiles(self):
        return ["minecraft/polished_andesite"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(PolishedAndesite)


"""class for granite"""
class Granite(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:granite"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/granite"

    def getAllTexturFiles(self):
        return ["minecraft/granite"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(Granite)

"""class for polished granite"""
class PolishedGranite(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_granite"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/polished_granite"

    def getAllTexturFiles(self):
        return ["minecraft/polished_granite"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(PolishedGranite)


"""class for diorite"""
class Diorite(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:diorite"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/diorite"

    def getAllTexturFiles(self):
        return ["minecraft/diorite"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(Diorite)

"""class for polished diorite"""
class PolishedDiorite(G.blockclass):
    oredictnames = [notations.OreDictItems.STONE, notations.OreDictItems.POLISHED_STONE]
    destroygroupnames = [notations.DestroyGroupItems.PICKAXE]

    def getName(self):
        return "minecraft:polished_diorite"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/polished_diorite"

    def getAllTexturFiles(self):
        return ["minecraft/polished_diorite"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(PolishedDiorite)