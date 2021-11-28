import globals as G
import mathhelper
import modsystem.ModLoader
import notations


class Log(G.iblockclass):
    """the base class for Logs"""

    oredictnames = [notations.OreDictItems.WOOD_LOG]

    def getDefaultData(self, inst):
        return {"rotation": "UD"}


class McLog(Log):
    """base class of all here listed logs"""

    def getBrakeSoundFile(self, inst):
        return [
            G.local + "/assets/minecraft/sounds/brake/wood1.wma",
            G.local + "/assets/minecraft/sounds/brake/wood2.wma",
            G.local + "/assets/minecraft/sounds/brake/wood3.wma",
            G.local + "/assets/minecraft/sounds/brake/wood4.wma",
        ]

    def getModelFile(self, inst):
        return "minecraft:log"


class AcaciaLog(McLog):
    """acacia Log class"""

    def getStateName(self, inst):
        return "acacia_log"

    def getName(self):
        return "minecraft:acacia_log"


class StrippedAcaciaLog(McLog):
    """stripped acacia Log class"""

    def getStateName(self, inst):
        return "stripped_acacia_log"

    def getName(self):
        return "minecraft:stripped_acacia_log"


class BirchLog(McLog):
    """birch Log class"""

    def getStateName(self, inst):
        return "birch_log"

    def getName(self):
        return "minecraft:birch_log"


class StrippedBirchLog(McLog):
    """stripped birch Log class"""

    def getStateName(self, inst):
        return "stripped_birch_log"

    def getName(self):
        return "minecraft:stripped_birch_log"


class DarkOakLog(McLog):
    """dark oak Log class"""

    def getStateName(self, inst):
        return "dark_oak_log"

    def getName(self):
        return "minecraft:dark_oak_log"


class StrippedDarkOakLog(McLog):
    """stripped dark oak Log class"""

    def getStateName(self, inst):
        return "stripped_dark_oak_log"

    def getName(self):
        return "minecraft:stripped_dark_oak_log"


class JungleLog(McLog):
    """jungle Log class"""

    def getStateName(self, inst):
        return "jungle_log"

    def getName(self):
        return "minecraft:jungle_log"


class StrippedJungleLog(McLog):
    """stripped jungle Log class"""

    def getStateName(self, inst):
        return "stripped_jungle_log"

    def getName(self):
        return "minecraft:stripped_jungle_log"


class OakLog(McLog):
    """oak Log class"""

    def __init__(self, *args, **kwargs):
        McLog.__init__(self, *args, **kwargs)

    def getStateName(self, inst):
        return "oak_log"

    def getName(self):
        return "minecraft:oak_log"


class StrippedOakLog(McLog):
    """stripped oak Log class"""

    def getStateName(self, inst):
        return "stripped_oak_log"

    def getName(self):
        return "minecraft:stripped_oak_log"


class SpruceLog(McLog):
    """spruce Log class"""

    def getStateName(self, inst):
        return "spruce_log"

    def getName(self):
        return "minecraft:spruce_log"


class StrippedSpruceLog(McLog):
    """stripped spruce Log class"""

    def getStateName(self, inst):
        return "stripped_spruce_log"

    def getName(self):
        return "minecraft:stripped_spruce_log"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating logs"
)
def register():
    G.blockhandler.register(StrippedSpruceLog)
    G.blockhandler.register(SpruceLog)
    G.blockhandler.register(StrippedOakLog)
    G.blockhandler.register(OakLog)
    G.blockhandler.register(StrippedJungleLog)
    G.blockhandler.register(JungleLog)
    G.blockhandler.register(StrippedDarkOakLog)
    G.blockhandler.register(DarkOakLog)
    G.blockhandler.register(StrippedBirchLog)
    G.blockhandler.register(BirchLog)
    G.blockhandler.register(StrippedAcaciaLog)
    G.blockhandler.register(AcaciaLog)
