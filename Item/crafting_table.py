import globals as G

"""class for crafting_table"""
class Bedrock(G.itemclass):
    def getName(self):
        return "minecraft:crafting_table"

    def hasBlock(self):
        return True

    def getTexturFile(self):
        return G.local+"/assets/textures/item/CRAFTING_TABLE.png"

G.itemhandler.register(Bedrock)