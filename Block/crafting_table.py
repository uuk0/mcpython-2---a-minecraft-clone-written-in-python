import globals as G
import mathhelper
from Inventory.crafting import Crafting as CraftingInventory
import modsystem.ModLoader


class CraftingTable(G.blockclass):
    """class for crafting table"""
    def _getDefaultData(self, inst):
        return {"inventory":CraftingInventory()}

    def getName(self):
        return "minecraft:crafting_table"

    def getModelFile(self, inst):
        return "minecraft:crafting_table"

    def getStateName(self, inst):
        return "crafting_table"

    def hasInventory(self, inst):
        return True

    def getInventorys(self, inst):
        return [inst.data["inventory"]]

    def isOpeningInventory(self, inst, item):
        return True


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating crafting table")
def register():
    G.blockhandler.register(CraftingTable)

