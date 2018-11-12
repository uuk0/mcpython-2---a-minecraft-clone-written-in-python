import globals as G
import mathhelper

"""class for ice"""
class Ice(G.blockclass):
    def getName(self):
        return "minecraft:ice"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/ice"

    def getAllTexturFiles(self):
        return ["minecraft/ice"]

G.blockhandler.register(Ice)

"""class for packed ice"""
class PackedIce(G.blockclass):
    def getName(self):
        return "minecraft:packed_ice"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/packed_ice"

    def getAllTexturFiles(self):
        return ["minecraft/packed_ice"]

G.blockhandler.register(PackedIce)

"""class for blue ice"""
class BlueIce(G.blockclass):
    def getName(self):
        return "minecraft:blue_ice"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/blue_ice"

    def getAllTexturFiles(self):
        return ["minecraft/blue_ice"]

G.blockhandler.register(BlueIce)