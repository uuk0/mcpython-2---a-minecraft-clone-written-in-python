import globals as G
import mathhelper

"""class for endstone"""
class Endstone(G.blockclass):
    def getName(self):
        return "minecraft:endstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/endstone"

    def getAllTexturFiles(self):
        return ["minecraft/endstone"]

G.blockhandler.register(Endstone)

"""class for endstonebrick"""
class EndstoneBrick(G.blockclass):
    def getName(self):
        return "minecraft:endstone_brick"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/endstone_brick"

    def getAllTexturFiles(self):
        return ["minecraft/endstone_brick"]

G.blockhandler.register(EndstoneBrick)