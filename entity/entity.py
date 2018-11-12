import globals as G

class EntityHandler:
    def __init__(self):
        self.entitys = []

    def register(self, entity):
        self.entitys.append(entity)
        G.eventhandler.call("game:registry:on_entity_registrated", entity)

G.entityhandler = EntityHandler()

"""class for entitys
is not used at the moment"""
class Entity:
    tags = []

    def __init__(self):
        self.position = (0, 0, 0)

    """returns the name of the entity"""
    def getName(self):
        return "minecraft:none"

    """callen when the entity is shown"""
    def on_show(self):
        pass

    """callen when the entity is hidden"""
    def on_hide(self):
        pass

    """callen when the entity is drawn"""
    def draw(self):
        pass

    """returns the drop of the entity"""
    def getDrop(self):
        return {}

    """returns the drop-xp of the entity"""
    def getXP(self):
        return 0

    """returns the nbt-data of the entity"""
    def getNBT(self):
        return {}

    """sets the nbt-data"""
    def setNBT(self, nbt):
        pass

G.entityclass = Entity

from . import boxmodel

def loadEntititys(*args):
    from . import player

G.eventhandler.on_event("game:registry:on_entity_registrate_periode", loadEntititys)