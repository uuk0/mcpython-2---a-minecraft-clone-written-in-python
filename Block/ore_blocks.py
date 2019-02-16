import globals as G
import mathhelper
import Block.log
import modsystem.ModLoader


class IOreBlock(G.blockclass):
    def getModelFile(self, inst):
        return "minecraft:ore_blocks"

    def getStateName(self, inst):
        return self.getName().split(":")[1]


class CoalBlock(IOreBlock):
    """class for coal block"""
    def getName(self):
        return "minecraft:coal_block"


class DiamondBlock(IOreBlock):
    """class for diamond block"""
    def getName(self):
        return "minecraft:diamond_block"


class EmeraldBlock(IOreBlock):
    """class for emerald block"""
    def getName(self):
        return "minecraft:emerald_block"


class GoldBlock(IOreBlock):
    """class for gold block"""
    def getName(self):
        return "minecraft:gold_block"


class IronBlock(IOreBlock):
    """class for iron block"""
    def getName(self):
        return "minecraft:iron_block"


class LapisBlock(IOreBlock):
    """class for lapis block"""
    def getName(self):
        return "minecraft:lapis_block"


class QuartzBlock(IOreBlock):
    """class for quartz block"""
    def getName(self):
        return "minecraft:quartz_block"


class ChiseledQuartzBlock(IOreBlock):
    """class for chiseled quartz block"""
    def getName(self):
        return "minecraft:chiseled_quartz_block"


class QuartzPillar(Block.log.McLog, IOreBlock):
    """class for quartz pillar"""
    def getName(self):
        return "minecraft:quartz_pillar"

    def getModelFile(self, inst):
        return "minecraft:ore_blocks"

    def getStateName(self, inst):
        return self.getName().split(":")[1]


class RedstoneBlock(IOreBlock):
    """class for redstone block"""
    def getName(self):
        return "minecraft:redstone_block"

    def getErmittedRedstoneSignal(self, inst, side):
        return 15

    def bindsToRedstoneWire(self, inst, side):
        return True


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating ore blocks")
def register():
    G.blockhandler.register(RedstoneBlock)
    G.blockhandler.register(QuartzPillar)
    G.blockhandler.register(ChiseledQuartzBlock)
    G.blockhandler.register(QuartzBlock)
    G.blockhandler.register(LapisBlock)
    G.blockhandler.register(IronBlock)
    G.blockhandler.register(GoldBlock)
    G.blockhandler.register(EmeraldBlock)
    G.blockhandler.register(DiamondBlock)
    G.blockhandler.register(CoalBlock)

