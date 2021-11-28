import globals as G
import mathhelper
import modsystem.ModLoader
from Inventory.crafting import Crafting as CraftingInventory


class CraftingTable(G.iblockclass):
    """class for crafting table"""

    def getDefaultData(self, inst):
        return {"inventory": CraftingInventory()}

    def getName(self):
        return "minecraft:crafting_table"

    def hasInventory(self, inst):
        return True

    def getInventorys(self, inst):
        return [inst.data["inventory"]]

    def isOpeningInventory(self, inst, item):
        return True

    def getStorageData(self, inst):
        return {"name": self.getName()}

    def setStorageData(self, inst):
        pass


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating crafting table",
)
def register():
    G.blockhandler.register(CraftingTable)
