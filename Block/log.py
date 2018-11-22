import globals as G
import mathhelper
import notations

"""the base class for Logs"""
class Log(G.blockclass):
    oredictnames = [notations.OreDictItems.WOOD_LOG]

    def getName(self):
        return "minecraft:log"

    """returns the textur file position for the front"""
    def getFrontTextur(self):
        return None

    """returns the textur file position for the side"""
    def getSideTextur(self):
        return None

    """returns the right formated textur data"""
    def getTexturData(self, inst):
        data = []
        if not inst.blocksettedto:
            data = [self.getFrontTextur()] * 2 + [self.getSideTextur()] * 4
        elif inst.blocksettedto[1] != inst.position[1] and inst.blocksettedto[0] == inst.position[0] and inst.blocksettedto[2] == inst.position[2]:
            data = [self.getFrontTextur()] * 2 + [self.getSideTextur()] * 4
        else:
            data = [self.getFrontTextur()] * 2 + [self.getSideTextur()] * 4
        return mathhelper.text_coords_complex(*data+self.getTexturSize())

"""base class of all here listed logs"""
class McLog(Log):
    def getTexturSize(self):
        return [1, 4]

    def getFrontTextur(self):
        return (0, 1)

    def getSideTextur(self):
        return (0, 2)

    def getBrakeSoundFile(self, inst):
        return [G.local + "assets/sounds/brake/wood1.wma",
                G.local + "assets/sounds/brake/wood2.wma",
                G.local + "assets/sounds/brake/wood3.wma",
                G.local + "assets/sounds/brake/wood4.wma"]

"""oak log class"""
class OakLog(McLog):
    def getTexturFile(self, inst):
        return "minecraft/oak_log"

    def getName(self):
        return "minecraft:oak_log"

G.blockhandler.register(OakLog)

"""stripped oak class"""
class StrippedOakLog(McLog):
    def getTexturFile(self, inst):
        return "minecraft/stripped_oak_log"

    def getName(self):
        return "minecraft:stripped_oak_log"

G.blockhandler.register(StrippedOakLog)

"""acacia Log class"""
class AcaciaLog(Log):
    def getAllTexturFiles(self):
        return ["minecraft/acacia_log"]

    def getTexturFile(self, inst):
        return "minecraft/acacia_log"

    def getTexturSize(self):
        return [1, 4]

    def getFrontTextur(self):
        return (0, 1)

    def getSideTextur(self):
        return (0, 2)

    def getName(self):
        return "minecraft:acacia_log"

    def getBrakeSoundFile(self, inst):
        return [G.local + "assets/sounds/brake/wood1.wma",
                G.local + "assets/sounds/brake/wood2.wma",
                G.local + "assets/sounds/brake/wood3.wma",
                G.local + "assets/sounds/brake/wood4.wma"]

G.blockhandler.register(AcaciaLog)

"""birch class"""
class BirchLog(Log):
    def getAllTexturFiles(self):
        return ["minecraft/birch_log"]

    def getTexturFile(self, inst):
        return "minecraft/birch_log"

    def getTexturSize(self):
        return [1, 4]

    def getFrontTextur(self):
        return (0, 1)

    def getSideTextur(self):
        return (0, 2)

    def getName(self):
        return "minecraft:birch_log"

    def getBrakeSoundFile(self, inst):
        return [G.local + "assets/sounds/brake/wood1.wma",
                G.local + "assets/sounds/brake/wood2.wma",
                G.local + "assets/sounds/brake/wood3.wma",
                G.local + "assets/sounds/brake/wood4.wma"]

G.blockhandler.register(BirchLog)