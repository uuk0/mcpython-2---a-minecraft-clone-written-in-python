import globals as G

"""class for bedrock"""
class Bedrock(G.itemclass):
    def getName(self):
        return "minecraft:bedrock"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/BEDROCK.png"

G.itemhandler.register(Bedrock)