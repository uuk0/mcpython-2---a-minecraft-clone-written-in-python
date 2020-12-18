import globals as G


class Saver:
    def __init__(self):
        pass

    def getStorageVersion(self):
        raise NotImplementedError()

    def saveWorld(self, file):
        self.saveDim(G.player.dimension, file + "/DIM" + str(G.player.dimension.id))

    def saveDim(self, dim, file):
        raise NotImplementedError()

    def saveChunk(self, cx, cz, file):
        raise NotImplementedError()
