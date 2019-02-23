import world.Dimensions
import config
import gen.OverWorld, gen.DebugWorldGenerator
import log
import config


OVERWORLD_GENERATOR = gen.OverWorld.OverWorldGenetor if not config.WorldGenerator.USED_DEBUG_GEN else \
    gen.DebugWorldGenerator.DebugWorldGenerator


class OverWorld(world.Dimensions.Dimension):
    def getID(self):
        return 0

    def getName(self):
        return "minecraft:overworld"

    def shouldBeOnGenerationInitialisated(self):
        return True

    def creatWorldGenerator(self):
        return OVERWORLD_GENERATOR(self.worldprovider)

    def getWorldSize(self):
        return config.WorldGenerator.WorldSize

    def prepare(self):
        if not config.WorldGenerator.USED_DEBUG_GEN:
            for cx in range(0, 1):
                for cz in range(0, 1):
                    log.printMSG("[OVERWORLD][GENERATOR][INFO] generating chunk "+str(cx)+"|"+str(cz))
                    self.worldprovider.generateChunkFor((cx, cz))
        else:
            self.worldprovider.generateChunkFor((0, 0))
            print(gen.DebugWorldGenerator.BLOCKTABLE.keys())
            for chunk in gen.DebugWorldGenerator.BLOCKTABLE.keys():
                self.worldprovider.generateChunkFor(chunk)

    def shouldBeShown(self, *args, **kwargs):
        return True



