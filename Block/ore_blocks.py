import globals as G
import mathhelper

"""class for coal block"""
class CoalBlock(G.blockclass):
    def getName(self):
        return "minecraft:coal_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/coal_block"

    def getAllTexturFiles(self):
        return ["minecraft/coal_block"]

G.blockhandler.register(CoalBlock)

"""class for diamond block"""
class DiamondBlock(G.blockclass):
    def getName(self):
        return "minecraft:diamond_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/diamond_block"

    def getAllTexturFiles(self):
        return ["minecraft/diamond_block"]

G.blockhandler.register(DiamondBlock)

"""class for emerald block"""
class EmeraldBlock(G.blockclass):
    def getName(self):
        return "minecraft:emerald_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/emerald_block"

    def getAllTexturFiles(self):
        return ["minecraft/emerald_block"]

G.blockhandler.register(EmeraldBlock)

"""class for gold block"""
class GoldBlock(G.blockclass):
    def getName(self):
        return "minecraft:gold_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/gold_block"

    def getAllTexturFiles(self):
        return ["minecraft/gold_block"]

G.blockhandler.register(GoldBlock)

"""class for iron block"""
class IronBlock(G.blockclass):
    def getName(self):
        return "minecraft:iron_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/iron_block"

    def getAllTexturFiles(self):
        return ["minecraft/iron_block"]

G.blockhandler.register(IronBlock)

"""class for lapis block"""
class LapisBlock(G.blockclass):
    def getName(self):
        return "minecraft:lapis_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/lapis_block"

    def getAllTexturFiles(self):
        return ["minecraft/lapis_block"]

G.blockhandler.register(LapisBlock)

"""class for quartz block"""
class QuartzBlock(G.blockclass):
    def getName(self):
        return "minecraft:quartz_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 2), (0, 1), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/quartz_block"

    def getAllTexturFiles(self):
        return ["minecraft/quartz_block"]

G.blockhandler.register(QuartzBlock)

"""class for chiseled quartz block"""
class ChiseledQuartzBlock(G.blockclass):
    def getName(self):
        return "minecraft:chiseled_quartz_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 1), (0, 1), n2=3)

    def getTexturFile(self, inst):
        return "minecraft/chiseled_quartz_block"

    def getAllTexturFiles(self):
        return ["minecraft/chiseled_quartz_block"]

G.blockhandler.register(ChiseledQuartzBlock)

"""class for quartz pillar"""
class QuartzPillar(G.blockclass):
    def getName(self):
        return "minecraft:quartz_pillar"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 1), (0, 1), (0, 0), n2=3)

    def getTexturFile(self, inst):
        return "minecraft/quartz_pillar"

    def getAllTexturFiles(self):
        return ["minecraft/quartz_pillar"]

G.blockhandler.register(QuartzPillar)

"""class for redstone block"""
class RedstoneBlock(G.blockclass):
    def getName(self):
        return "minecraft:redstone_block"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/redstone_block"

    def getAllTexturFiles(self):
        return ["minecraft/redstone_block"]

    def getErmittedRedstoneSignal(self, inst, side):
        return 15

    def bindsToRedstoneWire(self, inst, side):
        return True

G.blockhandler.register(RedstoneBlock)