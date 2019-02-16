import globals as G


class Loader:
    def __init__(self):
        pass

    def getStorageVersion(self):
        return None

    def loadWorld(self, file):
        pass

    def loadDim(self, dim, file):
        pass

    def loadChunk(self, cx, cz, file):
        pass

    def isFile(self, file):
        return False