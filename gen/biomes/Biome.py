import globals as G
import gen.Random
import mathhelper
import log
import sys
import gen.noise
import modsystem.ModLoader


class BiomeHandler:
    def __init__(self):
        self.biomes = {}
        self.biomemap = []

    def register(self, biome):
        self.biomes[biome.getName()] = biome
        self.biomemap.append(biome)

    def registerOverwrite(self, orginal, biome):
        if orginal in self.biomemap:
            self.biomemap.remove(orginal)
        self.register(biome)

    def getBiomeEntry(
        self, r: gen.Random.Random, x: int, z: int, worldprovider, table: list
    ) -> list:
        v = gen.noise.noise(x, -100, z)
        v *= len(self.biomes) / 2
        v += len(self.biomes) / 2
        v = v % (len(self.biomes) - 1)
        return self.biomemap[round(v)].getName()
        """
        return
        possible = {} #abs -> values
        cx, _, cz = mathhelper.sectorize((x, 0, z))
        chunkprovider = worldprovider.getChunkProviderFor((cx, cz))
        for biome in self.biomes.values():
            a = abs(chunkprovider.generationcache["temperaturmap"][(x, z)]-biome.getBiomeTemperature())
            if not a in possible: possible[a] = []
            possible[a].append(biome)
        possiblestatus = list(possible.keys())
        possiblestatus.sort()

        surrounding = {} #biome -> how many
        for dx in range(-2, 3):
            for dz in range(-2, 3):
                cx, _, cz = mathhelper.sectorize((x+dx, 0, z+dz))
                chunkprovider = worldprovider.getChunkProviderFor((cx, cz))
                biome = chunkprovider.generationcache["biomemap"][(x+dx, z+dz)] if  \
                                        "biomemap" in chunkprovider.generationcache and \
                                        (x + dx, z + dz) in chunkprovider.generationcache["biomemap"] \
                                        else None
                if biome:
                    if not biome in surrounding: surrounding[biome] = 0
                    surrounding[biome] += 1

        selecttable = []
        m = len(possiblestatus)
        for i, k in enumerate(possiblestatus):
            for biome in possible[k]:
                selecttable += [biome.getName()] * (m - i + (
                    surrounding[biome.getName()] if biome.getName() in surrounding else 0))
        return selecttable[r.generateValueForPosition((x, -10, z), 0, len(selecttable)-1) if len(selecttable) > 1 else 0]"""


G.biomehandler = BiomeHandler()


class Biome:
    def __init__(self):
        pass

    @staticmethod
    def getName() -> str:
        return "biome:empty"

    @staticmethod
    def getBiomeTemperature():
        return 0

    @staticmethod
    def getMinHigh():
        return 30

    @staticmethod
    def getMaxHigh():
        return 80

    @staticmethod
    def getOreVeins():
        return []


G.biomeclass = Biome


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_biome_registrate_periode", "minecraft", info="registrating biomes"
)
def register():
    from gen.biomes import BirchForest, Plains
