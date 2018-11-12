import globals as G
import random
import biomes.OreGenerator as OreGenerator


"""
Handler for every biome
use G.biomehandler.register(class) to register an biome
"""
class BiomeHandler:
    def __init__(self):
        self.biomes = {} #name -> biome class
        self.temperaturbiome = {} #temperatur -> biome class

    """returns the biome named like the given name"""
    def getByName(self, name):
        return self.biomes[name]

    """returns all biomes that are at the nearest at the given temperatur"""
    def getPossibleByTemperatur(self, temp):
        if temp in self.temperaturbiome:
            return self.temperaturbiome[temp]
        index = None
        flag = False
        data = list(self.temperaturbiome.keys())
        data.sort()
        for e in data:
            if not flag and e > temp:
                index = e
                flag = True
        if not flag:
            index = data[-1]
        return self.temperaturbiome[index]

    """registers an biome to the biometable"""
    def register(self, biome):
        self.biomes[biome.getName(None)] = biome
        if not biome.getTemperatur(None) in self.temperaturbiome: self.temperaturbiome[biome.getTemperatur(None)] = []
        self.temperaturbiome[biome.getTemperatur(None)].append(biome)
        G.eventhandler.call("game:registry:on_biome_registrated", biome)

G.biomehandler = BiomeHandler()

"""Base class for every biome
instances are created by worldgenerator
attributes may be definited changeable"""
class BiomeClass:
    def __init__(self):
        self.oregenerator = self.getOreGenerator()

    """generate all given (x, z) positions with these biome.
    need an preared G.HighMap and G.TemperaturMap"""
    def generatePositions(self, positions):
        for x, z in positions: #x, z positions
            high = G.HighMAP[(x, z)]
            temp = G.TemperaturMAP[(x, z)]
            G.BlockGenerateTasks.append([0, (x, 0, z), "bedrock"])
            for y in range(1, 6):
                if random.randint(0, 2) == 0:
                    G.BlockGenerateTasks.append([0, (x, y, z), "bedrock"])
            for y in range(1, high+1):
                if not (x, y, z) in G.model.world:
                    if y < high - random.randint(5, 10):
                        ore = self.oregenerator.generateOre((x, y, z))
                        if ore:
                            pass
                        else:
                            G.BlockGenerateTasks.append([0, (x, y, z), self.getMaterial((x, y, z), G.TemperaturMAP[(x, z)])])
                    else:
                        G.BlockGenerateTasks.append([0, (x, y, z), self.getMaterial((x, y, z), G.TemperaturMAP[(x, z)])])
            self.addStructurs(x, z, high, temp)

    """returns the material for the given position and temperatur"""
    def getMaterial(self, position, temperatur):
        return "air"

    """returns the high diffrents of these biomes.
    is used in WorldGen for preparing G.HighMap"""
    def getHighDiffrents(self):
        return 2

    """returns the name of the biome
    used in biometable"""
    def getName(self):
        return ""

    """returns the temperatur of the biome
    used for worldgen for biomeselection"""
    def getTemperatur(self): #value between 0 and 100
        return 50

    """the minimum of the high in these biome"""
    def getMinHigh(self):
        return 80

    """the maximum of the high in these biome"""
    def getMaxHigh(self):
        return 255

    """returns a oregenerator for these biome
    See OreGenerator-class for more informations"""
    def getOreGenerator(self):
        return OreGenerator.OreGenerator()

    """used in worldgen highmapgeneration
    see these functions for more informations"""
    def getChangeValue(self):
        return 10

    """used in worldgen highmapgeneration
        see these functions for more informations"""
    def getChangeValues(self):
        return [1]

    """adds the structures to the given (x, z)-position"""
    def addStructurs(self, x, z, high, temperatur):
        pass

G.biomeclass = BiomeClass


def loadBiomes(*args):
    from . import basebiome, basebiomehills, basebiomehot

G.eventhandler.on_event("game:registry:on_biome_registrate_periode", loadBiomes)



