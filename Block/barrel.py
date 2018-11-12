import globals as G
import mathhelper

"""class for barrel"""
class Barrel(G.blockclass):
    def getName(self):
        return "minecraft:barrel"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 2), (0, 1), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/barrel"

    def getAllTexturFiles(self):
        return ["minecraft/barrel"]

G.blockhandler.register(Barrel)