

import gen.biomes.Biome
import globals as G
import gen.ores


class BirchForest(gen.biomes.Biome.Biome):
    @staticmethod
    def getName(): return "minecraft:birch_forest"

    @staticmethod
    def getBiomeTemperature(): return 60

    @staticmethod
    def getOreVeins(): return [gen.ores.CoalOre]


G.biomehandler.register(BirchForest)

