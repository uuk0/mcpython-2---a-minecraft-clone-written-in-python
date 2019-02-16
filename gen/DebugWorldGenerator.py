
import gen.WorldGenerator
import globals as G
import math
import mathhelper
import log

BLOCKTABLE = {}  # sector -> blocks


class DebugWorldGenerator(gen.WorldGenerator.WorldGenerator):
    def generateSurfaceToChunkProvider(self, chunk):
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor(chunk)
        chunkprovider.generationcache["blocks_main"] = {}
        if not chunk in BLOCKTABLE: return
        for chunk in BLOCKTABLE.keys():
            for position in BLOCKTABLE[chunk]:
                chunkprovider.generationcache["blocks_main"][position] = BLOCKTABLE[chunk][position]

    def generateHighMapToChunkProvider(self, chunk):
        """
        this function should renamed to something like debugblockselector
        """
        if len(BLOCKTABLE) != 0: return
        blocks = list(G.blockhandler.blocks.keys())
        blocks.sort()
        blocks.remove("minecraft:none")
        xr = math.ceil(math.sqrt(len(blocks))/2)*2 + 1
        for x in range(-round(xr/2), round(xr/2)):
            for y in range(-round(xr / 2), round(xr / 2)):
                index = (xr+x) * xr + xr+y
                if len(blocks) > index:
                    block = blocks[index]
                    cx, _, cz = mathhelper.sectorize((x, 0, y))
                    if (cx, cz) not in BLOCKTABLE: BLOCKTABLE[(cx, cz)] = {}
                    BLOCKTABLE[(cx, cz)][(x*4, 5, y*4)] = block
        # print(BLOCKTABLE)

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
        print("\x1b[2K\r", end="")
        chunkprovider.generationcache["blocks_main"] = {}
        for chunk in BLOCKTABLE.keys():
            chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor(chunk)
            #chunkprovider.generated = True
            G.model.show_sector(chunk)

