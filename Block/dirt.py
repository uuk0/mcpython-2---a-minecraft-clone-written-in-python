import globals as G
import mathhelper
import notations

"""class for dirt"""
class Dirt(G.blockclass):
    oredictnames = [notations.OreDictItems.DIRT]

    def getName(self):
        return "minecraft:dirt"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/dirt"

    def getAllTexturFiles(self):
        return ["minecraft/dirt"]

    def getBrakeSoundFile(self, inst):
        return [G.local + "assets/sounds/brake/grass1.wma",
                G.local + "assets/sounds/brake/grass2.wma",
                G.local + "assets/sounds/brake/grass3.wma",
                G.local + "assets/sounds/brake/grass4.wma"]

G.blockhandler.register(Dirt)