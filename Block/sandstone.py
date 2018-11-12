import globals as G
import mathhelper

"""class for sandstone"""
class SandStone(G.blockclass):
    def getName(self):
        return "minecraft:sandstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/sandstone"

    def getAllTexturFiles(self):
        return ["minecraft/sandstone"]

G.blockhandler.register(SandStone)

"""class for chiseled sandstone"""
class ChiseledSandStone(G.blockclass):
    def getName(self):
        return "minecraft:chiseled_sandstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/chiseled_sandstone"

    def getAllTexturFiles(self):
        return ["minecraft/chiseled_sandstone"]

G.blockhandler.register(ChiseledSandStone)

"""class for cut sandstone"""
class CutSandStone(G.blockclass):
    def getName(self):
        return "minecraft:cut_sandstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/cut_sandstone"

    def getAllTexturFiles(self):
        return ["minecraft/cut_sandstone"]

G.blockhandler.register(CutSandStone)

"""class for red sandstone"""
class RedSandStone(G.blockclass):
    def getName(self):
        return "minecraft:red_sandstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/red_sandstone"

    def getAllTexturFiles(self):
        return ["minecraft/red_sandstone"]

G.blockhandler.register(RedSandStone)

"""class for red chiseled sandstone"""
class RedChiseledSandStone(G.blockclass):
    def getName(self):
        return "minecraft:red_chiseled_sandstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/red_chiseled_sandstone"

    def getAllTexturFiles(self):
        return ["minecraft/red_chiseled_sandstone"]

G.blockhandler.register(RedChiseledSandStone)

"""class for red cut sandstone"""
class RedCutSandStone(G.blockclass):
    def getName(self):
        return "minecraft:red_cut_sandstone"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 2), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/red_cut_sandstone"

    def getAllTexturFiles(self):
        return ["minecraft/red_cut_sandstone"]

G.blockhandler.register(RedCutSandStone)