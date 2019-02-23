
import gen.WorldGenerator
import globals as G
import gen.biomes.Biome
import log
import gen.noise


class OverWorldGenetor(gen.WorldGenerator.WorldGenerator):
    BIOMES = ["minecraft:birch_forest", "minecraft:plains"]

    def generateTemperaturMapToChunkProvider(self, chunk):
        r = self.random
        chunkprovider = self.worldprovider.getChunkProviderFor(chunk)
        chunkprovider.generationcache["temperaturmap"] = {}
        cx, cz = chunk #if len(chunk) == 2 else chunk[0], chunk[2]
        for dx in range(0, 16):
            for dz in range(0, 16):
                x, z = cx * 16 + dx, cz * 16 + dz
                chunkprovider.generationcache["temperaturmap"][(x, z)] = r.generateValueForPosition((x, -10, z), 0, 100)

    def generateBiomeMapToChunkProvider(self, chunk):
        r = self.random
        chunkprovider = self.worldprovider.getChunkProviderFor(chunk)
        chunkprovider.generationcache["biomemap"] = {}
        cx, cz = chunk  # if len(chunk) == 2 else chunk[0], chunk[2]
        for dx in range(0, 16):
            for dz in range(0, 16):
                x, z = cx * 16 + dx, cz * 16 + dz
                chunkprovider.generationcache["biomemap"][(x, z)] = G.biomehandler.getBiomeEntry(r, x, z,
                                                                                                 self.worldprovider,
                                                                                                 self.BIOMES)

    def generateHighMapToChunkProvider(self, chunk):
        r = self.random
        chunkprovider = self.worldprovider.getChunkProviderFor(chunk)
        chunkprovider.generationcache["highmap"] = {}
        cx, cz = chunk  # if len(chunk) == 2 else chunk[0], chunk[2]
        for dx in range(0, 16):
            for dz in range(0, 16):
                x, z = cx * 16 + dx, cz * 16 + dz
                biome = G.biomehandler.biomes[chunkprovider.generationcache["biomemap"][(x, z)]]
                chunkprovider.generationcache["highmap"][(x, z)] = round((gen.noise.noise(x, -10, z, level=3) * \
                                                                   (biome.getMaxHigh() - biome.getMinHigh())) * \
                                                    (gen.noise.noise(x, -11, z, freq=1000, level=4)+0.25)) + \
                                                                   biome.getMinHigh()

    def generateSurfaceToChunkProvider(self, chunk):
        r = self.random
        chunkprovider = self.worldprovider.getChunkProviderFor(chunk)
        chunkprovider.generationcache["blocks"] = {}
        chunkprovider.generationcache["blocks_main"] = {}
        cx, cz = chunk  # if len(chunk) == 2 else chunk[0], chunk[2]
        for dx in range(0, 16):
            for dz in range(0, 16):
                x, z = cx * 16 + dx, cz * 16 + dz
                biome = chunkprovider.generationcache["biomemap"][(x, z)]
                high = chunkprovider.generationcache["highmap"][(x, z)]
                for y in range(chunkprovider.generationcache["highmap"][(x, z)]+1):
                    if y == 0:
                        chunkprovider.generationcache["blocks"][(x, y, z)] = "bedrock"
                    #elif y == high:
                    #    chunkprovider.generationcache["blocks_main"][(x, y, z)] = "grass"
                    #elif y > high - 5:
                    #    chunkprovider.generationcache["blocks"][(x, y, z)] = "dirt"
                    #else:
                    #    chunkprovider.generationcache["blocks"][(x, y, z)] = "stone"

    def generateBlocksFromChunkProvider(self, chunk):
        r = self.random
        chunkprovider = self.worldprovider.getChunkProviderFor(chunk)
        log.printMSG("[WORLDGEN][INFO] generating blocks...")
        i = 0
        m = len(chunkprovider.generationcache["blocks_main"])
        for e in chunkprovider.generationcache["blocks_main"].keys():
            G.model.add_block(e, chunkprovider.generationcache["blocks_main"][e])
            if i != 0 and i % 10 == 0:
                print("\x1b[2K\r", end="")
                log.printMSG("[GENERATOR][INFO] added "+str(i)+" blocks. need "+str(m-i)+" more", end="")
            i += 1

        for k in chunkprovider.generationcache["blocks"].keys():
            G.BlockGenerateTasks[k] = [chunkprovider.generationcache["blocks"][k]]
        print("\x1b[2K\r", end="")
        chunkprovider.generationcache["blocks"] = {}
        chunkprovider.generationcache["blocks_main"] = {}



