import globals as G

"""class for chainmail helmet"""


class ChainmailHelmet(G.itemclass):
    def getName(self):
        return "minecraft:chainmail_helmet"

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/chainmail_helmet.png"

    def hasBlock(self):
        return False

    def getMaxStackSize(self):
        return 1


G.itemhandler.register(ChainmailHelmet)

G.notationhandler.notate("oredict", "armor:heads", ChainmailHelmet)


"""class for chainmail chestplate"""


class ChainmailChestplate(G.itemclass):
    def getName(self):
        return "minecraft:chainmail_chestplate"

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/chainmail_helmet.png"

    def hasBlock(self):
        return False

    def getMaxStackSize(self):
        return 1


G.itemhandler.register(ChainmailChestplate)

G.notationhandler.notate("oredict", "armor:chestplate", ChainmailChestplate)

"""class for chainmail legging"""


class ChainmailLegging(G.itemclass):
    def getName(self):
        return "minecraft:chainmail_legging"

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/chainmail_leggings.png"

    def hasBlock(self):
        return False

    def getMaxStackSize(self):
        return 1


G.itemhandler.register(ChainmailLegging)

G.notationhandler.notate("oredict", "armor:chestplate", ChainmailLegging)

"""class for chainmail boots"""


class ChainmailBoots(G.itemclass):
    def getName(self):
        return "minecraft:chainmail_boots"

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/chainmail_boots.png"

    def hasBlock(self):
        return False

    def getMaxStackSize(self):
        return 1


G.itemhandler.register(ChainmailBoots)

G.notationhandler.notate("oredict", "armor:chestplate", ChainmailBoots)
