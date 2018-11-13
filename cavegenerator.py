import time

import noise

import config
import globals as G

"""function to generate an chunk"""
def generateChunk(cx, cz):
    max = 16 * 16 * 64
    dt = time.time()
    for i in range(cx*16-1, cx*16+16):
        for j in range(cz*16-1, cz*16+16):
            for k in range(5, G.HighMAP[(i, j)]+1):
                value = noise.pnoise3(i / config.WorldGenerator.PERLIN_SCALE, j / config.WorldGenerator.PERLIN_SCALE,
                                      k / config.WorldGenerator.PERLIN_SCALE,
                                      octaves=config.WorldGenerator.PERLIN_OKTAVES,
                                      persistence=config.WorldGenerator.PERLIN_PERSISTENCE,
                                      lacunarity=config.WorldGenerator.PERLIN_LACUNARITY,
                                      repeatx=1024,
                                      repeaty=1024,
                                      base=0)
                if value < 0:
                    surrounding = []
                    for x in range(i-1, i+2):
                        for y in range(k-1, k+1):
                            for z in range(j-1, j+2):
                                surrounding.append(noise.pnoise3(i / config.WorldGenerator.PERLIN_SCALE,
                                                                 j / config.WorldGenerator.PERLIN_SCALE,
                                                                 k / config.WorldGenerator.PERLIN_SCALE,
                                                                 octaves=config.WorldGenerator.PERLIN_OKTAVES,
                                                                 persistence=config.WorldGenerator.PERLIN_PERSISTENCE,
                                                                 lacunarity=config.WorldGenerator.PERLIN_LACUNARITY,
                                                                 repeatx=1024,
                                                                 repeaty=1024,
                                                                 base=0) < 0)
                    if surrounding.count(True) > 13:
                        G.BlockGenerateTasks.append([2, (i, k, j)])

                if time.time() - dt > 2:
                    print((i/max)*100, "%")
                    dt = time.time()






