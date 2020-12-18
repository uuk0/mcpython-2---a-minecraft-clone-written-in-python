import globals as G

"""class for obsidian"""


class Obsidian(G.itemclass):
    def getName(self):
        return "minecraft:obsidian"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/OBSIDIAN.png"


G.itemhandler.register(Obsidian)
