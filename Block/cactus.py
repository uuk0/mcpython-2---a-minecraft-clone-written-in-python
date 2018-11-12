import globals as G
import mathhelper
import entity.boxmodel as boxmodel

"""class for cactus"""
class Cactus(G.blockclass):
    def getName(self):
        return "minecraft:cactus"

    def hasExternalDraw(self, inst):
        return True

    def show(self, inst):
        inst.data["shownid"] = G.eventhandler.on_event("opengl:draw3d", self.draw, [inst])
        inst.data["shown"] = True
        if inst.data["boxmodels"] == None:
            inst.data["boxmodels"] = []
            inst.data["boxmodels"].append(boxmodel.BoxModel(0.75, 1, 0.75, G.texturedatahandler.texturs["minecraft/cactus"],
                                                            12, 16, 12))
            inst.data["boxmodels"][-1].update_texture_data([(0, 128),
                                                            (0, 0),
                                                            (0, 64),
                                                            (0, 64),
                                                            (0, 64),
                                                            (0, 64)])

    def hide(self, inst):
        G.eventhandler.remove_on_event(inst.data["shownid"])
        inst.data["shown"] = False

    def draw(self, name, inst, *args):
        inst.data["boxmodels"][0].draw()

    def isFullSide(self, inst, side):
        return False

    def _getDefaultData(self, inst):
        return {"shown":False,
                "shownid":-1,
                "boxmodels":None}

    def onDelet(self, inst):
        self.hide(inst)

G.blockhandler.register(Cactus)

G.texturhandler.registerBoxModelTextur(G.local + "tmp/minecraft/cactus.png")