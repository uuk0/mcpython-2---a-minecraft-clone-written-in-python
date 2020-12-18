import globals as G

"""class for coal"""


class Coal(G.itemclass):
    def getName(self):
        return "minecraft:coal"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/COAL#0.png"


G.itemhandler.register(Coal)

"""class for charcoal"""


class CharCoal(G.itemclass):
    def getName(self):
        return "minecraft:charcoal"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/COAL#1.png"


G.itemhandler.register(CharCoal)

"""class for diamond"""


class Diamond(G.itemclass):
    def getName(self):
        return "minecraft:diamond"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Diamond.png"


G.itemhandler.register(Diamond)

"""class for emerald"""


class Emerald(G.itemclass):
    def getName(self):
        return "minecraft:emerald"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Emerald.png"


G.itemhandler.register(Emerald)

"""class for gold ingot"""


class Gold(G.itemclass):
    def getName(self):
        return "minecraft:gold_ingot"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Gold_Ingot.png"


G.itemhandler.register(Gold)

"""class for iron ingot"""


class Iron(G.itemclass):
    def getName(self):
        return "minecraft:iron_ingot"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Iron_Ingot.png"


G.itemhandler.register(Iron)

"""class for lapis"""


class Lapis(G.itemclass):
    def getName(self):
        return "minecraft:lapis_lazuli"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Lapis_Lazuli.png"


G.itemhandler.register(Lapis)

"""class for nether quartz"""


class NetherQuartz(G.itemclass):
    def getName(self):
        return "minecraft:nether_quartz"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Nether_Quartz.png"


G.itemhandler.register(NetherQuartz)

"""class for redstone"""


class Redstone(G.itemclass):
    def getName(self):
        return "minecraft:redstone"

    def hasBlock(self):
        return False

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/Redstone_Dust.png"


G.itemhandler.register(Redstone)
