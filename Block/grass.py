import globals as G
import mathhelper
import notations

"""class for grass"""
class Grass(G.blockclass):
    oredictnames = [notations.OreDictItems.DIRT]

    def getName(self):
        return "minecraft:grass"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/grass"

    def getAllTexturFiles(self):
        return ["minecraft/grass"]

    """returns dirt as drop"""
    def getDrop(self, inst):
        return {"minecraft:dirt":1}

    def getBrakeSoundFile(self, inst):
        return [G.local + "assets/sounds/brake/grass1.wma",
                G.local + "assets/sounds/brake/grass2.wma",
                G.local + "assets/sounds/brake/grass3.wma",
                G.local + "assets/sounds/brake/grass4.wma"]

G.blockhandler.register(Grass)