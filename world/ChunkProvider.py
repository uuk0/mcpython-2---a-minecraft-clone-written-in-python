
#import globals as G
import gen.ores


class ChunkProvider:
    def __init__(self, worldprovider, chunk):
        self.worldprovider = worldprovider
        self.chunk = chunk
        self.generationcache = {}
        self.generated = False
        self.shown = {}
        self.world = {}
        self.orechunkprovider = gen.ores.OreChunkProvider(chunk, self)

    def generate(self):
        if self.generated: return
        self.generated = True
        self.worldprovider.dimension.worldgenerator.generateChunk(self.chunk)




