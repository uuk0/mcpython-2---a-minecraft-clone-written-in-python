import globals as G
import mathhelper

"""class for acacia leave"""
class AcaciaLeave(G.blockclass):
    def getName(self):
        return "minecraft:acacia_leaves"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/acacia_leave"

    def getAllTexturFiles(self):
        return ["minecraft/acacia_leave"]

    def getDrop(self, inst):
        return {}

G.blockhandler.register(AcaciaLeave)
