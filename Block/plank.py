import globals as G
import mathhelper
import notations

"""class for acacia plank"""
class AcaciaPlank(G.blockclass):
    oredictnames = [notations.OreDictItems.WOOD_PLANK]

    def getName(self):
        return "minecraft:acacia_plank"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/acacia_plank"

    def getAllTexturFiles(self):
        return ["minecraft/acacia_plank"]

G.blockhandler.register(AcaciaPlank)

class BirchPlank(G.blockclass):
    oredictnames = [notations.OreDictItems.WOOD_PLANK]

    def getName(self):
        return "minecraft:birch_plank"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/birch_plank"

    def getAllTexturFiles(self):
        return ["minecraft/birch_plank"]


G.blockhandler.register(BirchPlank)