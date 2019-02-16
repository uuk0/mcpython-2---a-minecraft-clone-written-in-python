import globals as G

class Saver:
    def __init__(self):
        pass

    def getStorageVersion(self):
        return None

    def saveWorld(self, file):
        self.saveDim(G.player.dimension, file+"/DIM"+str(G.player.dimension.id))

    def saveDim(self, dim, file):
        pass

    def saveChunk(self, cx, cz, file):
        pass