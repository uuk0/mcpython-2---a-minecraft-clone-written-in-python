import globals as G
import mathhelper
from Inventory.crafting import Crafting as CraftingInventory

"""class for crafting table"""
class CraftingTable(G.blockclass):
    def _getDefaultData(self, inst):
        return {"inventory":CraftingInventory()}

    def getName(self):
        return "minecraft:crafting_table"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 1), (0, 0), (0, 3), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/crafting_table"

    def getAllTexturFiles(self):
        return ["minecraft/crafting_table"]

    def hasInventory(self, inst):
        return True

    def getInventorys(self, inst):
        return [inst.data["inventory"]]

    def isOpeningInventory(self, inst, item):
        return True

G.blockhandler.register(CraftingTable)