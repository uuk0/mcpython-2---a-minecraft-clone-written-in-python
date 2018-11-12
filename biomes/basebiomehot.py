import globals as G
from . import OreGenerator
import random

class BaseBiomeHot(G.biomeclass):
    oregenerator = OreGenerator.OreGenerator()
    oregenerator.addOre("minecraft:coal_ore", 0, 255, 5, 3, 32, 32, 2)
    oregenerator.addOre("minecraft:iron_ore", 1, 63, 20, 3, 4, 3, 2)
    oregenerator.addOre("minecraft:gold_ore", 1, 32, 4, 2, 2, 1, 2)
    oregenerator.addOre("minecraft:diamond_ore", 1, 16, 1, 1, 5, 5, 1)
    oregenerator.addOre("minecraft:emerald_ore", 4, 32, 5, 3, 1, 1, 2)
    oregenerator.addOre("minecraft:lapis_ore", 1, 31, 1, 1, 4, 1, 20)
    oregenerator.addOre("minecraft:redstone_ore", 1, 16, 4, 2, 6, 2, 2)

    def getOreGenerator(self):
        return self.oregenerator

    def getName(self):
        return "mcpython:base_biome:hot"

    def getHighDiffrents(self):
        return 3

    def getSmoothTime(self):
        return 3

    def getTemperatur(self):
        return 80

    def getMaterial(self, position, temperatur):
        x, y, z = position
        return "stone" if position[1] < G.HighMAP[(x, z)] - random.randint(5, 10) else "sand"

    def getMinHigh(self):
        return 80

    def getMaxHigh(self):
        return 120

    def getChangeValue(self):
        return 3

    def getChangeValues(self):
        return [1]

G.biomehandler.register(BaseBiomeHot)