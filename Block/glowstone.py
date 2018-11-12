import globals as G
import mathhelper

"""class for glowstone"""
class Glowstone(G.blockclass):
    def getName(self):
        return "minecraft:glowstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/glowstone"

    def getAllTexturFiles(self):
        return ["minecraft/glowstone"]

    def isBrakeAble(self, inst):
        return True

G.blockhandler.register(Glowstone)