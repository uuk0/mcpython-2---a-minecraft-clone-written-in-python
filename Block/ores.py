import globals as G
import mathhelper
import modsystem.ModLoader


class IOre(G.iblockclass):
    def getModelFile(self, inst):
        return "minecraft:ores"

    def getStateName(self, inst):
        return self.getName().split(":")[1]


class CoalOre(IOre):
    """class for coalore"""

    def getName(self):
        return "minecraft:coal_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:coal": 1}


class DiamondOre(IOre):
    """class for diamondore"""

    def getName(self):
        return "minecraft:diamond_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:diamond": 1}


class EmeraldOre(IOre):
    """class for emeraldore"""

    def getName(self):
        return "minecraft:emerald_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:emerald": 1}


class GoldOre(IOre):
    """class for goldore"""

    def getName(self):
        return "minecraft:gold_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}


class IronOre(IOre):
    """class for ironore"""

    def getName(self):
        return "minecraft:iron_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}


class LapisOre(IOre):
    """class for lapisore"""

    def getName(self):
        return "minecraft:lapis_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {"minecraft:lapis_lazuli": 5}


class NetherQuartz(IOre):
    """class for netherquartz"""

    def getName(self):
        return "minecraft:nether_quartz_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}


class RedstoneOre(IOre):
    """class for redstoneore"""

    def getName(self):
        return "minecraft:redstone_ore"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    def getDrop(self, inst):
        return {self.getItemName(inst): 1}


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating ores"
)
def register():
    G.blockhandler.register(RedstoneOre)
    G.blockhandler.register(NetherQuartz)
    G.blockhandler.register(LapisOre)
    G.blockhandler.register(IronOre)
    G.blockhandler.register(GoldOre)
    G.blockhandler.register(EmeraldOre)
    G.blockhandler.register(DiamondOre)
    G.blockhandler.register(CoalOre)
