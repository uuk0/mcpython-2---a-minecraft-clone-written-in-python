import globals as G


class Loader:
    def __init__(self):
        pass

    def getStorageVersion(self):
        raise NotImplementedError()

    def loadWorld(self, file):
        raise NotImplementedError()

    def loadDim(self, dim, file):
        raise NotImplementedError()

    def loadChunk(self, cx, cz, file):
        raise NotImplementedError()

    def isFile(self, file):
        return False

