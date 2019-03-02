import config
import globals as G
import log
import mathhelper
import pyglet
import traceback
import modelloader
import modsystem.ModLoader

"""
block handler class
use G.blockhandler.register(class) to add new blocks
"""
class BlockHandler:
    def __init__(self):
        self.blocks = {}
        self.blocksall = {}
        self.fromoredict = {}

    """register an new blockclass to blocktable"""
    def register(self, blockclass):
        if not (hasattr(blockclass, "blockclassregigisterable") and blockclass.blockclassregigisterable) and config.DEBUG.PRINT_BLOCK_REGISTRATING:
            log.printMSG("[BLOCKHANDLER][ERROR] can't register block class "+str(blockclass)+". blockclass has no attribute blockclassregigisterable")
            return
        inst = blockclass()
        G.eventhandler.call("game:registry:on_block_registrated", inst)
        self.blocks[inst.getName()] = inst
        d = inst.getName().split(":")
        for i in range(len(d)):
            string = ""
            for e in d[i:]:
                string += ":" + e
            self.blocksall[string[1:]] = inst

        G.soundhandler.loadSound(inst.getBrakeSoundFile(None))
        if config.DEBUG.PRINT_BLOCK_REGISTRATING:
            log.printMSG("[BLOCKHANDLER][INFO] registrating block "+inst.getName())

        for e in inst.oredictnames:
            if not e in self.fromoredict: self.fromoredict[e] = []
            self.fromoredict[e].append(inst)
            G.notationhandler.notate("oredict", e, inst)
        for e in inst.destroygroupnames:
            G.notationhandler.notate("destroygroup", e, inst)
        G.eventhandler.call("game:registry:on_block_registrated", inst)

    """returns a new blockinst - class representing the block"""
    def getInst(self, name, position, blocksettedto=None):
        if self.getByName(name):
            return IBlockInstants(name, position, blocksettedto=blocksettedto)
        return None

    """returns the block class by name"""
    def getByName(self, name, exc=True):
        if name in self.blocks:
            return self.blocks[name]
        elif name in self.blocksall:
            return self.blocksall[name]
        else:
            log.printMSG("[BLOCKHANDLER][ERROR] can't access block named "+str(name))

G.blockhandler = BlockHandler()


"""
Main Block Class
"""
class BlockClass:
    """says if these block-class can be registert
    set to False if it is an dummy-class"""
    blockclassregigisterable = True
    oredictnames = []
    destroygroupnames = []

    def __init__(self):
        pass

    """returns the name of the block"""
    def getName(self):
        return "minecraft:none"

    """callen when the block is created"""
    def onCreat(self, inst):
        pass

    """calllen when the block is deleted"""
    def onDelet(self, inst):
        pass

    """returns if the block is brakeable in gamemode 0"""
    def isBrakeAble(self, inst):
        return True

    """returns the drops of the block
    format: as dict: itename:amount"""
    def getDrop(self, inst):
        return {self.getItemName(inst):1}

    """returns the name of the given back item
    only used if getDrop is not overwritten"""
    def getItemName(self, inst):
        return self.getName()

    """callen when the block should updated"""
    def on_block_update(self, inst):
        pass

    """returns the sound which is played when block is broken. may be a list if more than 1 is possible"""
    def getBrakeSoundFile(self, inst):
        return [G.local + "/assets/minecraft/sounds/brake/stone1.wma",
                G.local + "/assets/minecraft/sounds/brake/stone2.wma",
                G.local + "/assets/minecraft/sounds/brake/stone3.wma",
                G.local + "/assets/minecraft/sounds/brake/stone4.wma"]

    def show(self, inst):
        try:
            G.modelhandler.models[inst.getModelFile()].addToBatch(inst, inst.position)
        except:
            log.printMSG(inst.getName())
            raise

    def hide(self, inst):
        G.modelhandler.models[inst.getModelFile()].removeFromBatch(inst, inst.position)

    """returns if a side is a full side. These Meanes you can't look through it
    side is N, E, S, W, U or D
    per default, every side is true"""
    def isFullSide(self, inst, side):
        return True

    """returns the default data for block inst"""
    def _getDefaultData(self, inst):
        return {}

    """returns if the block has an inventory"""
    def hasInventory(self, inst):
        return False

    """returns the inventorys as a list of the block. may be only Inventory ID'S
    callen after isOpeningInventory by window to get the inventorys to show.
    if you want to have your own system, use this and return []"""
    def getInventorys(self, inst):
        return []

    """returns if the given item opens the inventory"""
    def isOpeningInventory(self, inst, item):
        return False

    """returns the redstone strenght of the block (0-15 normal)"""
    def getErmittedRedstoneSignal(self, inst, side):
        return 0

    """returns if redstone should connected to the block"""
    def bindsToRedstoneWire(self, inst, side):
        return False

    """callen on redstone update"""
    def on_redstone_update(self, inst):
        pass

    """returns if the block is redstoneable"""
    def can_be_redstone_powered(self, inst):
        return True

    """returns the cube verticens of the block"""
    def getCubeVerticens(self, inst, x, y, z, n):
        return mathhelper.cube_vertices(x, y, z, n)

    """convert the given base position to an renderable position"""
    def convertPositionToRenderable(self, inst, position):
        return position

    def isVisableInWorld(self, inst):
        return True #not G.model.exposed(inst.position)

    def getStorageData(self, inst):
        cx, _, cz = mathhelper.sectorize(inst.position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        return {"name": self.getName(), "data": inst.data,
                "shown": inst.position in chunkprovider.shown}

    def setStorageData(self, data, inst):
        inst.data = data["data"]

    def getStateName(self, inst):
        return "default"

    def getModelFile(self, inst):
        return "minecraft:notdefinited"

    def getItemFile(self, inst):
        return None

G.blockclass = BlockClass


"""
class holding all block data
overwrites every function with (inst) without it
"""
class IBlockInstants(BlockClass):
    blockclassregigisterable = False

    def __oredictnames(self):
        return self.blockclass.oredictnames

    oredictnames = property(__oredictnames)

    def __destroygroupnames(self):
        return self.blockclass.destroygroupnames

    destroygroupnames = property(__destroygroupnames)

    def __init__(self, blockname, position, blocksettedto=None):
        self.blockclass = G.blockhandler.getByName(blockname)
        self.position = position
        self.onCreat()
        self.blocksettedto = blocksettedto
        self.multiblockstructurlist = []
        self.data = self.blockclass._getDefaultData(self)
        if not "redstone_state" in self.data and self.can_be_redstone_powered():
            self.data["redstone_state"] = False
        self.showndata = []

    def getName(self):
        return self.blockclass.getName()

    def getTexturData(self):
        return self.blockclass.getTexturData(self)

    def getTexturFile(self):
        return self.blockclass.getTexturFile(self)

    def onCreat(self):
        self.blockclass.onCreat(self)

    def onDelet(self):
        G.eventhandler._blockremoveupdate(self.position)
        self.blockclass.onDelet(self)

    def isBrakeAble(self):
        return self.blockclass.isBrakeAble(self)

    def getDrop(self):
        return self.blockclass.getDrop(self)

    def getItemName(self):
        return self.blockclass.getItemName(self)

    def on_block_update(self):
        self.blockclass.on_block_update(self)
        G.eventhandler._blockupdate(self.position)

    def getBrakeSoundFile(self):
        return self.blockclass.getBrakeSoundFile(self)

    def show(self):
        self.blockclass.show(self)

    def hide(self):
        self.blockclass.hide(self)

    def isFullSide(self, side):
        self.blockclass.isFullSide(self, side)

    def hasInventory(self):
        return self.blockclass.hasInventory(self)

    def getInventorys(self):
        return self.blockclass.getInventorys(self)

    def isOpeningInventory(self, item):
        return self.blockclass.isOpeningInventory(self, item)

    def getErmittedRedstoneSignal(self, side):
        return self.blockclass.getErmittedRedstoneSignal(self, side)

    def bindsToRedstoneWire(self, inst, side):
        return self.blockclass.bindsToRedstoneWire(side)

    def on_redstone_update(self):
        self.blockclass.on_redstone_update(self)

    def can_be_redstone_powered(self):
        self.blockclass.can_be_redstone_powered(self)

    def getCubeVerticens(self, x, y, z, n):
        return self.blockclass.getCubeVerticens(self, x, y, z, n)

    def convertPositionToRenderable(self, position):
        return self.blockclass.convertPositionToRenderable(self, position)

    def isVisableInWorld(self):
        return self.blockclass.isVisableInWorld(self)

    def getStorageData(self):
        return self.blockclass.getStorageData(self)

    def setStorageData(self, data):
        self.blockclass.setStorageData(data, self)

    def getStateName(self):
        return self.blockclass.getStateName(self)

    def getModelFile(self):
        return self.blockclass.getModelFile(self)

    def getItemFile(self):
        return self.blockclass.getItemFile(self)


G.blockinst = IBlockInstants


def loadBlocks(*args):
    import importlib, os
    for e in os.listdir(G.local + "/Block"):
        importlib.import_module("Block." + e.split(".")[0])


loadBlocks()

