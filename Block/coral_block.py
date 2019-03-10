import globals as G
import mathhelper
import modsystem.ModLoader


class CoralBlock(G.blockclass):
    @staticmethod
    def getType():
        return ""

    def getName(self):
        return "minecraft:"+self.getType()+"_coral_block"

    def getModelFile(self, inst):
        return "minecraft:coral_block"

    def getStateName(self, inst):
        return self.getType()


class DeadCoralBlock(CoralBlock):
    def getStateName(self, inst):
        return "dead_"+self.getType()

    def getName(self):
        return "minecraft:dead_"+self.getType()+"_coral_block"


class BrainCoral(CoralBlock):
    @staticmethod
    def getType():
        return "brain"


class DeadBrainCoral(DeadCoralBlock):
    @staticmethod
    def getType():
        return "brain"


class bubbleCoral(CoralBlock):
    @staticmethod
    def getType():
        return "bubble"


class DeadbubbleCoral(DeadCoralBlock):
    @staticmethod
    def getType():
        return "bubble"


class fireCoral(CoralBlock):
    @staticmethod
    def getType():
        return "fire"


class DeadfireCoral(DeadCoralBlock):
    @staticmethod
    def getType():
        return "fire"


class hornCoral(CoralBlock):
    @staticmethod
    def getType():
        return "horn"


class DeadhornCoral(DeadCoralBlock):
    @staticmethod
    def getType():
        return "horn"


class tubeCoral(CoralBlock):
    @staticmethod
    def getType():
        return "tube"


class DeadtubeCoral(DeadCoralBlock):
    @staticmethod
    def getType():
        return "tube"


local = locals()


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating corals")
def register():
    for e in local.values():
        try:
            if issubclass(e, G.blockclass):
                G.blockhandler.register(e)
        except TypeError:
            pass

