from . import basebiome
import globals as G


"""like basebiome, but some more highdiffrents"""
class BaseBiomeHills(basebiome.BaseBiome):
    def getHighDiffrents(self):
        return 14

    def getMaxHigh(self):
        return 255

    def getName(self):
        return "mcpython:basebiome:hills"

G.biomehandler.register(BaseBiomeHills)