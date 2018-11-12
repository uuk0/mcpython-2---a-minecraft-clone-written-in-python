import globals as G
import random

"""class for structurhandler"""
class StructurHandler:
    def __init__(self):
        self.structurs = {}

    def register(self, klass):
        inst = klass()
        self.structurs[inst.getName()] = inst
        G.eventhandler.call("game:registry:on_structur_registrated", inst)

G.structurhandler = StructurHandler()

"""class for Structur"""
class Structur:
    def __init__(self):
        pass

    """get the name of the structur"""
    def getName(self):
        return "minecraft:none"

    """past the structur to a given position"""
    def past(self, position):
        pass

"""class for acacia tree"""
class AcaciaTree(Structur):
    def getName(self):
        return "minecraft:acacia_tree"

    def past(self, position):
        high = random.randint(3, 6)
        leavehigh = high - random.randint(3, 5)
        if leavehigh < 1: leavehigh = 1

        (x, y, z) = position
        for dy in range(high):
            G.BlockGenerateTasks.append([0, (x, y+dy, z), "minecraft:acacia_log"])

def loadStructurs(*args):
    G.structurhandler.register(AcaciaTree)

G.eventhandler.on_event("game:registry:on_structur_registrate_periode", loadStructurs)