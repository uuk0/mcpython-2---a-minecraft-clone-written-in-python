import globals as G
import log
import config
import traceback
import Item.item

"""class for crafting system"""
class CraftingHandler:
    def __init__(self):
        self.recipis = {}
        self.recipinames = {}
        self.grids = []

    """adds a new crafting grid to registry"""
    def addGrid(self, name):
        if not name in self.grids:
            self.grids.append(name)
            self.recipis[name] = {}
        else:
            log.printMSG("[CRAFTING][WARN] can't add grid named "+str(name)+". It is registert")

    """remove an existing grid from the registry by removing all it's recipis"""
    def removeGrid(self, name):
        if name in self.grids:
            self.grids.remove(name)
            del self.recipis[name]
        else:
            log.printMSG("[CRAFTING][ERROR] can't remove grid named "+str(name)+". It is not known")

    """returns all registert recipis for a given grid"""
    def getRecipisFor(self, grid):
        if grid in self.grids:
            return self.recipis[grid]
        else:
            log.printMSG("[CRAFTING][ERROR] can't get recipis for "+str(grid)+". grid is unknown")
            return []

    """remove all recipis for a given grid"""
    def removeAllRecipisFor(self, grid):
        if grid in self.grids:
            self.recipis[grid] = {}
        else:
            log.printMSG("[CRAFTING][ERROR] can't get recipis for "+str(grid)+". grid is unknown")

    """removes ALL recipis"""
    def removeAll(self):
        for e in self.grids:
            self.removeAllRecipisFor(e)

    """add an new recipi
    if name is registered, '_' will be added until name is free"""
    def addRecipi(self, grid, name, inputs, outputs, itemtable, extra={}):
        if config.DEBUG.PRINT_CRAFTING_STUFF: log.printMSG("[CRAFTING][INFO] registrating recipi named "+str(name))
        if not grid in self.grids:
            log.printMSG("[CRAFTING][ERROR] try to add an recipi to an unknown grid named "+str(grid))
            return
        if name in self.recipinames:
            self.addRecipi(grid, name+"_", inputs, outputs, itemtable, extra)
            return
        self.recipis[grid][name] = [inputs, outputs, itemtable, extra]
        self.recipinames[name] = grid

    """remove an recipi by his name"""
    def removeRecipiByName(self, name):
        if not name in self.recipinames:
            log.printMSG("[CRAFTING][ERROR] try to remove an unknown recipi named "+str(name))
            return
        del self.recipis[self.recipinames[name]][name]
        del self.recipinames[name]

G.craftinghandler = CraftingHandler()
G.craftinghandler.addGrid("minecraft:crafting")

if config.AdvancedVanilla.RECIPIS.GRASS_TO_DIRT:
    G.craftinghandler.addRecipi("minecraft:crafting", "dirttograss_1", ["Y"], ["X"], {"X":("minecraft:dirt", 1),
                                                                                      "Y":("minecraft:grass", 1)})
if config.AdvancedVanilla.RECIPIS.DIRT_TO_GRASS:
    G.craftinghandler.addRecipi("minecraft:crafting", "grasstodirt_1", ["X"], ["Y"], {"X": ("minecraft:dirt", 1),
                                                                                      "Y": ("minecraft:grass", 1)})

G.craftinghandler.addRecipi("minecraft:crafting", "test", ["XX", "XX"], ["Y"],
                            {"X": ("minecraft:cobbelstone", 1),
                             "Y": ("minecraft:stone", 1)})

import os, json

"""loads an recipi from .json file"""
def loadRecipiFromFile(file, name=None):
    if name == None: name = file
    with open(file) as f:
        data = json.load(f)
    #print(file, data)
    if data["type"] == 'crafting_shaped':
        result = ["%"]
        table = {}
        for e in data["key"].keys():
            if "item" in data["key"][e]:
                if config.DEBUG.PRINT_CRAFTING_STUFF and not G.itemhandler.getByName(e, exc=False) == None:
                    log.printMSG("[CRAFTING][WARN] can't access item named "+str(e))
                table[e] = (data["key"][e]["item"], 1)
            elif "tag" in data["key"][e]:
                table[e] = (data["key"][e]["tag"], 1)
                if config.DEBUG.PRINT_CRAFTING_STUFF:
                    log.printMSG("[CRAFTING][ERROR] found unknow tag-notation named "+str(data["key"][e]["tag"]))
        table["%"] = (data["result"]["item"], data["result"]["count"] if "count" in data["result"] else 1)

        G.craftinghandler.addRecipi("minecraft:crafting", name, data["pattern"], result, table)
    else:
        if config.DEBUG.PRINT_CRAFTING_STUFF:
            log.printMSG("[CRAFTING][ERROR] can't load recipi named "+str(name)+". Unknown type "+str(data["type"]))


def loadRecipis(*args):
    G.craftinghandler.addRecipi("minecraft:crafting", "acacia_wood_1", ["X"], ["Y"],
                                {"X":("minecraft:acacia_log", 1),
                                 "Y":("minecraft:acacia_plank", 4)})
    G.craftinghandler.addRecipi("minecraft:crafting", "crafting_table_1", ["XX", "XX"], ["Y"],
                                {"X":("minecraft:acacia_plank", 1),
                                 "Y":("minecraft:crafting_table", 1)})



    for e in os.listdir(G.local+"assets/data/minecraft/recipes"):
        try:
            loadRecipiFromFile(G.local+"assets/data/minecraft/recipes/"+e)
        except:
            if config.DEBUG.PRINT_CRAFTING_STUFF:
                traceback.print_exc()

G.eventhandler.on_event("game:registry:on_crafting_recipi_registrate_periode", loadRecipis)


