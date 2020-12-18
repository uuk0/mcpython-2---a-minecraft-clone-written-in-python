import globals as G

"""class for brick"""


class Brick(G.itemclass):
    def getName(self):
        return "minecraft:brick"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local + "/assets/minecraft/textures/item/BRICK_BLOCK.png"


G.itemhandler.register(Brick)
