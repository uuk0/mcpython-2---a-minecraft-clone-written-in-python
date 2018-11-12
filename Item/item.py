import globals as G
import log

"""class for itemhandler"""
class ItemHandler:
    def __init__(self):
        self.itemclasses = {}
        self.prefixes = []

    """register an item-class"""
    def register(self, klass):
        self.itemclasses[klass.getName(None)] = klass
        self.prefixes.append(klass.getName(None).split(":")[0])
        G.eventhandler.call("game:registry:on_item_registrated", klass)

    """returns an item class by name"""
    def getByName(self, name, exc=True):
        if name in self.itemclasses:
            return self.itemclasses[name]
        else:
            for e in self.prefixes:
                if e+":"+name in self.itemclasses:
                    return self.itemclasses[e+":"+name]
            if exc:
                log.printMSG("[BLOCKHANDLER][ERROR] can't access item named "+str(name))

G.itemhandler = ItemHandler()

"""class for Item"""
class ItemClass:
    def __init__(self):
        pass

    """returns the name of item"""
    def getName(self):
        return "minecraft:none"

    """returns if the item has an block"""
    def hasBlock(self):
        return True

    """returns the textur file"""
    def getTexturFile(self):
        pass

    """returns how many items can be stacked"""
    def getMaxStackSize(self):
        return 64

    """returns the name of the block"""
    def getBlockName(self):
        return self.getName()


G.itemclass = ItemClass

def loadItems(*args):
    from . import stone, bedrock, brick, grass, sand, dirt, ores, log as _log, obsidian, leaves, cactus, crafting_table, plank
    from . import gravel, oredrops, ore_blocks, endstone, ice, barrel, glowstone, sandstone, tnt, redstone_lamp


G.eventhandler.on_event("game:registry:on_item_registrate_preiode", loadItems)