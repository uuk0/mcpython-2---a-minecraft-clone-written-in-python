import globals as G
import mathhelper
import modsystem.ModLoader


class Ice(G.iblockclass):
    """class for ice"""

    def getName(self):
        return "minecraft:ice"

    def getModelFile(self, inst):
        return "minecraft:ice"

    def getStateName(self, inst):
        return "ice"


class PackedIce(G.iblockclass):
    """class for packed ice"""

    def getName(self):
        return "minecraft:packed_ice"

    def getModelFile(self, inst):
        return "minecraft:ice"

    def getStateName(self, inst):
        return "packed_ice"


class BlueIce(G.iblockclass):
    """class for blue ice"""

    def getName(self):
        return "minecraft:blue_ice"

    def getModelFile(self, inst):
        return "minecraft:ice"

    def getStateName(self, inst):
        return "blue_ice"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode", "minecraft", info="registrating ice"
)
def register():
    G.blockhandler.register(BlueIce)
    G.blockhandler.register(PackedIce)
    G.blockhandler.register(Ice)
