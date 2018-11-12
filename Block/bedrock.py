import globals as G
import mathhelper

"""class for bedrock"""
class Bedrock(G.blockclass):
    def getName(self):
        return "minecraft:bedrock"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/bedrock"

    def getAllTexturFiles(self):
        return ["minecraft/bedrock"]

    def isBrakeAble(self, inst):
        return False

G.blockhandler.register(Bedrock)