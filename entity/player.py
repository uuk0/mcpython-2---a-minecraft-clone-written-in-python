import globals as G

class PlayerEntity(G.entityclass):
    tags = ["player"]

    def __init__(self):
        G.entityclass.__init__(self)
        self.player = G.player

    def getName(self):
        return "minecraft:player"

    def on_show(self):
        pass

    def on_hide(self):
        pass

    def draw(self):
        pass

    def getDrop(self):
        return {}

    def getXP(self):
        return 0

G.entityhandler.register(PlayerEntity)