
#import globals as G

import world.ChunkProvider

import pyglet

import gen.ores


class WorldProvider:
    def __init__(self, dimension):
        self.dimension = dimension
        self.chunkproviders = {}
        self.generator = None
        self.batch = pyglet.graphics.Batch()

    def getChunkProviderFor(self, chunk) -> world.ChunkProvider.ChunkProvider:
        if chunk not in self.chunkproviders: self.chunkproviders[chunk] = world.ChunkProvider.ChunkProvider(self, chunk)
        return self.chunkproviders[chunk]

    def generateChunkFor(self, chunk):
        self.getChunkProviderFor(chunk).generate()

