import globals as G
import log
import config
import world.WorldProvider
import log

class DimensionHandler:
    def __init__(self):
        self.dimensionclasses = {}
        self.dimensions = {}

    def register(self, klass):
        self.dimensionclasses[klass.getName(None)] = klass
        if klass.shouldBeOnGenerationInitialisated(None):
            klass()

    def prepare(self):
        for dim in self.dimensions.values():
            dim.prepare()
        log.printMSG("[DIMENSIONS][INFO] dimension generation finished")

    def registerINST(self, inst):
        self.dimensions[inst.getID()] = inst


G.dimensionhandler = DimensionHandler()


class Dimension:
    def __init__(self):
        self.worldprovider = world.WorldProvider.WorldProvider(self)
        self.worldgenerator = self.creatWorldGenerator()
        self.id = self.getID()
        G.dimensionhandler.registerINST(self)
        self.map = {}

    def creatWorldGenerator(self):
        return "worldgenerator"

    def getID(self):
        return 0

    def getName(self):
        return "minecraft:none"

    def shouldBeOnGenerationInitialisated(self):
        return False

    def getWorldSize(self): #in chunks
        return [(-3, -3), (3, 3)]

    def prepare(self):
        pass

    def join(self):
        if G.player.dimension:
            self.worldprovider.world = self.map.copy()
            G.player.dimension = self

    def leave(self):
        G.storagehandler.cleanUpModel()



