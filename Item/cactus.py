import globals as G

"""class for cactus"""
class Bedrock(G.itemclass):
    def getName(self):
        return "minecraft:cactus"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/minecraft/textures/item/CACTUS.png"

G.itemhandler.register(Bedrock)