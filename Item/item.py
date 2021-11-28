import traceback

import exceptionhandler
import globals as G
import language
import log
import modsystem.ModLoader
import textures.util


class ItemHandler:
    """class for itemhandler"""

    def __init__(self):
        self.itemclasses = {}
        self.prefixes = []

    def register(self, klass):
        """register an item-class"""
        self.itemclasses[klass.getName(None)] = klass
        self.prefixes.append(klass.getName(None).split(":")[0])
        G.eventhandler.call("game:registry:on_item_registrated", klass)

    def getByName(self, name, exc=True):
        """returns an item class by name"""
        if name in self.itemclasses:
            return self.itemclasses[name]
        else:
            for e in self.prefixes:
                if e + ":" + name in self.itemclasses:
                    return self.itemclasses[e + ":" + name]
            if exc:
                log.printMSG(
                    "[BLOCKHANDLER][ERROR] can't access item named " + str(name)
                )


G.itemhandler = ItemHandler()

"""class for Item"""


class ItemClass:
    oredictnames = []

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
        return G.local + "/assets/minecraft/textures/missingtexture.png"

    """returns how many items can be stacked"""

    def getMaxStackSize(self):
        return 64

    """returns the name of the block"""

    def getBlockName(self):
        return self.getName()

    def getToolTipText(self):
        text = ""
        for e in self.getName().split(":"):
            text += "." + e
        text = text[1:]
        if "block." + text in G.LANG.active.data:
            return G.LANG.active.data["block." + text]
        if "item" + text in G.LANG.active.data:
            return G.LANG.active.data["item" + text]
        return text


G.itemclass = ItemClass


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_item_registrate_preiode", "minecraft", info="registrating items"
)
def register():
    import importlib
    import os

    for e in os.listdir(G.local + "/Item"):
        importlib.import_module("Item." + e.split(".")[0])
