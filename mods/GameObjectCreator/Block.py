import globals as G

import mods.GameObjectCreator.Model


class BlockHelper:
    def __init__(self, name):
        self.name = name
        self.tooltip = self.name
        self.drops = {self.name:1}
        self.model = "minecraft:notdefinited"
        self.modelinfo = "default"
        self.__created = False
        self.__model = None

    def add_model(self):
        """
        :return: a new modelhelper binded to these blockhelper
        """
        self.model = self.name
        model = mods.GameObjectCreator.Model.ModelHelper(self.name)
        self.__model = model
        return model

    def create(self):
        if self.__created: return
        self.__created = True
        sup = self

        class FactoriedBlockByGameObjectCreator(G.blockclass):
            def getName(self):
                return sup.name

            def getModelFile(self, inst):
                return sup.model

            def getStateName(self, inst):
                return sup.modelinfo

        G.blockhandler.register(FactoriedBlockByGameObjectCreator)

    def creat_model(self):
        if self.__model: self.__model.create()
