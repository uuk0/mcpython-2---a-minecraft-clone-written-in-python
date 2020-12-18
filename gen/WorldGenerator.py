"""
main system for world generation
"""

import gen.Random
import globals as G


class WorldGeneratorHandler:
    def __init__(self):
        self.generators = {}

    def registerWorldGenerator(self, generator):
        self.generators[generator.getName()] = generator


class WorldGenerator:
    def __init__(self, worldprovider):
        self.worldprovider = worldprovider
        worldprovider.generator = self
        self.random = gen.Random.Random(-100)

    @staticmethod
    def getName():
        return "worldgenerator:none"

    def generateHighMapToChunkProvider(self, chunk):
        pass

    def generateBiomeMapToChunkProvider(self, chunk):
        pass

    def generateTemperaturMapToChunkProvider(self, chunk):
        pass

    def generateSurfaceToChunkProvider(self, chunk):
        pass

    def generatePerlinToChunkProvider(self, chunk):
        pass

    def generateOres(self, chunk):
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor(chunk)
        if "biomemap" in chunkprovider.generationcache:
            chunkprovider.orechunkprovider.generate()

    def generateUnderGroundStructursToChunkProvider(self, chunk):
        pass

    def generateSurfaceStructursToChunkProvider(self, chunk):
        pass

    def generateSurfaceLook(self, chunk):
        pass

    def generateBlocksFromChunkProvider(self, chunk):
        pass

    def generateChunk(self, chunk):
        self.generateTemperaturMapToChunkProvider(chunk)
        self.generateBiomeMapToChunkProvider(chunk)
        self.generateHighMapToChunkProvider(chunk)
        self.generateSurfaceToChunkProvider(chunk)
        self.generatePerlinToChunkProvider(chunk)
        # self.generateOres(chunk)
        self.generateUnderGroundStructursToChunkProvider(chunk)
        self.generateSurfaceStructursToChunkProvider(chunk)
        self.generateSurfaceLook(chunk)
        self.generateBlocksFromChunkProvider(chunk)
