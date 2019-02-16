import globals as G


class ItemHelper:
    """
    main helper class for Items
    """
    def __init__(self, name):
        self.name = name
        self.imagefile = G.local+"/assets/minecraft/textures/missingtexture.png"
        self.hasblock = False
        self.oredictnotations = []

    def create(self):
        sup = self

        class FactoriedItemByGameObjectCreator(G.itemclass):
            def getName(self):
                return sup.name

            def hasBlock(self):
                return sup.hasblock

            def getTexturFile(self):
                return sup.imagefile

        G.itemhandler.register(FactoriedItemByGameObjectCreator)

        for e in self.oredictnotations:
            G.notationhandler.notate("oredict", e, FactoriedItemByGameObjectCreator)


