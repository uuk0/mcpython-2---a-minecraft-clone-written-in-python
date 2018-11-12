import globals as G
import mathhelper

"""class for coalore"""
class CoalOre(G.blockclass):
    def getName(self):
        return "minecraft:coal_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/coal_ore"

    def getAllTexturFiles(self):
        return ["minecraft/coal_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:coal":1}

G.blockhandler.register(CoalOre)

"""class for diamondore"""
class DiamondOre(G.blockclass):
    def getName(self):
        return "minecraft:diamond_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/diamond_ore"

    def getAllTexturFiles(self):
        return ["minecraft/diamond_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:diamond":1}

G.blockhandler.register(DiamondOre)

"""class for emeraldore"""
class EmeraldOre(G.blockclass):
    def getName(self):
        return "minecraft:emerald_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/emerald_ore"

    def getAllTexturFiles(self):
        return ["minecraft/emerald_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:emerald":1}

G.blockhandler.register(EmeraldOre)

"""class for goldore"""
class GoldOre(G.blockclass):
    def getName(self):
        return "minecraft:gold_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/gold_ore"

    def getAllTexturFiles(self):
        return ["minecraft/gold_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}

G.blockhandler.register(GoldOre)

"""class for ironore"""
class IronOre(G.blockclass):
    def getName(self):
        return "minecraft:iron_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/iron_ore"

    def getAllTexturFiles(self):
        return ["minecraft/iron_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}

G.blockhandler.register(IronOre)

"""class for lapisore"""
class LapisOre(G.blockclass):
    def getName(self):
        return "minecraft:lapis_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/lapis_ore"

    def getAllTexturFiles(self):
        return ["minecraft/lapis_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:lapis_lazuli":5}

G.blockhandler.register(LapisOre)

"""class for netherquartz"""
class NetherQuartz(G.blockclass):
    def getName(self):
        return "minecraft:nether_quartz_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/nether_quartz_ore"

    def getAllTexturFiles(self):
        return ["minecraft/nether_quartz_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}

G.blockhandler.register(NetherQuartz)

"""class for redstoneore"""
class RedstoneOre(G.blockclass):
    def getName(self):
        return "minecraft:redstone_ore"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/redstone_ore"

    def getAllTexturFiles(self):
        return ["minecraft/redstone_ore"]

    def isBrakeAble(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}

G.blockhandler.register(RedstoneOre)