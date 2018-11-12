import globals as G
import mathhelper

"""class for brick"""
class Brick(G.blockclass):
    def getName(self):
        return "minecraft:brick"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/brick"

    def getAllTexturFiles(self):
        return ["minecraft/brick"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(Brick)