import globals as G
import mathhelper

"""class for obsidian"""
class Obsidian(G.blockclass):
    def getName(self):
        return "minecraft:obsidian"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/obsidian"

    def getAllTexturFiles(self):
        return ["minecraft/obsidian"]

G.blockhandler.register(Obsidian)