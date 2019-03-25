import config
import globals as G
import log
import mathhelper
import exceptionhandler


class BlockHandler:
    """
    block handler class
    use G.blockhandler.register(class) to add new blocks
    todo: implement an plugin system for functions / constants to  blocks
    """

    def __init__(self):
        """
        creates an new BlockHandler-object
        """
        self.blocktable = {}

    def register(self, blockclass):
        """
        register an new blockclass to the blocktable
        """
        instance = blockclass()
        sname = instance.getName().split(":")
        iname = sname[:]
        sname.reverse()
        names = []
        for i, part in enumerate(sname):
            name = ":".join(iname[i:])
            self.blocktable[name] = instance
            names.append(name)
        G.eventhandler.call("game:registry:on_block_registrated", instance, names)

    def getInst(self, name, position):
        """returns a new blockinst - class representing the block"""
        return BlockReference(name, position)

    def getByName(self, name):
        """returns the block class by name"""
        if name in self.blocktable:
            return self.blocktable[name]
        return self.getByName("minecraft:none")


G.blockhandler = BlockHandler()


class IBlock:
    """
    Main Block Class
    every block should include this
    """

    def getName(self):
        return "minecraft:none"

    def onCreat(self, inst):
        """callen when the block is created"""
        pass

    def onDelet(self, inst):
        """calllen when the block is deleted"""
        pass

    def isBrakeAbleInGamemode0(self, inst):
        """returns if the block is brakeable in gamemode 0"""
        return True

    def getDrop(self, inst):
        """returns the drops of the block
        format: as dict: itename:amount
        todo: move to loottable"""
        return {self.getName(): 1}

    def on_block_update(self, inst):
        """callen when the block should updated"""
        pass

    @staticmethod
    def getBrakeSoundFile(inst):
        """returns the sound which is played when block is broken. may be a list if more than 1 is possible"""
        return [G.local + "/assets/minecraft/sounds/brake/stone1.wma",
                G.local + "/assets/minecraft/sounds/brake/stone2.wma",
                G.local + "/assets/minecraft/sounds/brake/stone3.wma",
                G.local + "/assets/minecraft/sounds/brake/stone4.wma"]

    def show(self, inst):
        """
        only for historical. here in the past the show function was located
        """
        if self.get_model_address(inst) in G.modelhandler.models:
            G.modelhandler.models[self.get_model_address(inst)].entrys[inst.getStateName()].show(
                G.player.dimension.worldprovider.batch, inst)

    def hide(self, inst):
        """
        only for historical. here in the past the hide function was located
        """
        if self.get_model_address(inst) in G.modelhandler.models:
            G.modelhandler.models[self.get_model_address(inst)].entrys[inst.getStateName()].hide(
                G.player.dimension.worldprovider.batch, inst)

    def isFullSide(self, inst, side):
        """returns if a side is a full side. These Meanes you can't look through it
        side is N, E, S, W, U or D
        per default, every side is true
        todo: move model.exposed() usojg this instead of isFullBlock(...)"""
        return True

    def isFullBlock(self):
        """
        :return: if the block is full or not
        """
        return True

    @staticmethod
    def getDefaultData(inst):
        """returns the default data for block inst"""
        return {}

    def hasInventory(self, inst):
        """returns if the block has an inventory"""
        return False

    def getInventorys(self, inst):
        """returns the inventorys as a list of the block. may be only Inventory ID'S
        callen after isOpeningInventory by window to get the inventorys to show.
        if you want to have your own system, use this and return []
        DO NOT USE IT IF YOU DON'T WANT TO DEBUG EVERYTHING BECAUSE THESE IS VERY UNSTABLE"""
        return []

    def isOpeningInventory(self, inst, item):
        """returns if the given item opens the inventory"""
        return False

    def getCubeVerticens(self, inst, x, y, z, n):
        """returns the cube verticens of the block
        only for historical reasons. in the past it was used in self.show()"""
        return mathhelper.cube_vertices(x, y, z, n)

    def convertPositionToRenderable(self, inst, position):
        """convert the given base position to an renderable position"""
        return position

    def isVisableInWorld(self, inst):
        """returns if the block is theoretcly visable in the world.
        only for historical reasons. was used in model.show_sector(...)"""
        return True

    def getStorageData(self, inst):
        """returns the data that should be stored. should be storeable by pickle"""
        cx, _, cz = mathhelper.sectorize(inst.position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        return {"name": self.getName(), "data": inst.data,
                "shown": inst.position in chunkprovider.shown}

    def setStorageData(self, data, inst):
        """set stored data to these block. data comes from Block.getStorageData(...)"""
        inst.data = data["data"]

    def getStateName(self, inst):
        """return the model state name (the name under which it can be found in the main {})"""
        return "default"

    def get_model_address(self, inst):
        return self.getName()

    def getItemFile(self, inst):
        """returns the itemfile for these block. is used for autogen of items"""
        return None


G.iblockclass = IBlock


class BlockReference:
    """
    reference in world to an IBlock-class
    """

    def __init__(self, blockname_or_object_or_to_copy, position):
        self.blockclass = None
        if issubclass(type(blockname_or_object_or_to_copy), IBlock):
            self.blockclass = blockname_or_object_or_to_copy
        elif issubclass(type(blockname_or_object_or_to_copy), BlockReference):
            self.blockclass = blockname_or_object_or_to_copy.blockclass
        elif issubclass(type(blockname_or_object_or_to_copy), str):
            self.blockclass = G.blockhandler.getByName(blockname_or_object_or_to_copy)
        if not self.blockclass:
            log.printMSG("[BLOCK][ERROR] can't construct block from "+str(blockname_or_object_or_to_copy)+
                         ". using minecraft:none instead")
            self.blockclass = G.blockhandler.getByName("minecraft:none")
        self.position = position
        self.settedto = None
        self.data = self.blockclass.getDefaultData(self)
        self.showndata = []
        self.create()

    def create(self):
        self.blockclass.onCreat(self)

    def getName(self):
        return self.blockclass.getName()

    def delete(self):
        self.blockclass.onDelet(self)

    def isBrakeAbleInGamemode0(self):
        return self.blockclass.isBrakeAbleInGamemode0(self)

    def getDrop(self):
        return self.blockclass.getDrop()

    def on_block_update(self):
        self.blockclass.on_block_update(self)

    def getBrakeSoundFile(self):
        return self.blockclass.getBrakeSoundFile(self)

    def show(self):
        self.blockclass.show(self)

    def hide(self):
        self.blockclass.hide(self)

    def isFullSide(self, side):
        return self.blockclass.isFullSide(self, side)

    def isFullBlock(self):
        return self.blockclass.isFullBlock()

    def getDefaultData(self):
        return self.blockclass.getDefaultData()

    def hasInventory(self):
        return self.blockclass.hasInventory(self)

    def getInventorys(self):
        return self.blockclass.getInventorys(self)

    def isOpeningInventory(self, item):
        return self.blockclass.isOpeningInventory(self, item)

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

    def getItemFile(self):
        return self.blockclass.getItemFile(self)

    def get_model_address(self):
        return self.blockclass.getName(self)


G.blockreferenceclass = BlockReference


def loadBlocks(*args):
    import importlib, os
    for e in os.listdir(G.local + "/Block"):
        importlib.import_module("Block." + e.split(".")[0])


loadBlocks()

