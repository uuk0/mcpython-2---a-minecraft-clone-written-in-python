import globals as G
import modsystem.ModLoader
import pyglet.gl


class EntityHandler:
    def __init__(self):
        self.entitys = []
        self.entityclasses = {}
        G.eventhandler.on_event("opengl:draw3d", self.draw)

    def register(self, entity):
        self.entityclasses[entity.getName(None)] = entity
        G.eventhandler.call("game:registry:on_entity_registrated", entity)

    def draw(self, *args, **kwargs):
        pyglet.gl.glColor3d(1, 1, 1)
        for entity in self.entitys:
            entity.draw()

    def add_entity(self, name, position):
        entity = self.entityclasses[name](position)
        self.entitys.append(entity)
        return entity


G.entityhandler = EntityHandler()


class Entity:
    """class for entitys
    is not used at the moment"""

    tags = []

    def __init__(self, position=(0, 0, 0)):
        self.position = position

    """returns the name of the entity"""

    def getName(self):
        return "minecraft:none"

    def draw(self):
        """callen when the entity is drawn"""
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

    def update(self, dt):
        pass


G.entityclass = Entity

from . import boxmodel


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_entity_registrate_periode",
    "minecraft",
    info="registrating entitys",
)
def register():
    from . import player
