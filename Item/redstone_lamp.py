import globals as G

"""class for redstone lamp"""


class RedstoneLamp(G.itemclass):
    def getName(self):
        return "minecraft:redstone_lamp"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/REDSTONE_LAMP.png"


G.itemhandler.register(RedstoneLamp)
