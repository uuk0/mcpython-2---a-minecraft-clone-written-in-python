import gen.biomes.Biome
import gen.ores
import globals as G


class Plains(gen.biomes.Biome.Biome):
    @staticmethod
    def getName():
        return "minecraft:plains"

    @staticmethod
    def getBiomeTemperature():
        return 80

    @staticmethod
    def getOreVeins():
        return []  # gen.ores.CoalOre]


G.biomehandler.register(Plains)
