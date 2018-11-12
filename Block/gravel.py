import globals as G
import mathhelper

"""class for Gravel"""
class Gravel(G.blockclass):
    def getName(self):
        return "minecraft:gravel"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=1)

    def getTexturFile(self, inst):
        return "minecraft/gravel"

    def getAllTexturFiles(self):
        return ["minecraft/gravel"]

    def isBrakeAble(self, inst):
        return True

    """makes the block falling"""
    def on_block_update(self, inst):
        (x, y, z) = inst.position
        if not (x, y-1, z) in G.model.world and y > 0 and not (hasattr(inst, "blocked") and not inst.blocked):
            inst.blocked = True
            G.tickhandler.tick(self.on_tick_update, args=[inst], tick=4)

    """fall the block"""
    def on_tick_update(self, inst):
        (x, y, z) = inst.position
        if not (x, y - 1, z) in G.model.world and y > 0:
            G.model.add_block((x, y-1, z), inst)
            G.model.remove_block((x, y, z))
        inst.blocked = False

    def getBrakeSoundFile(self, inst):
        return [G.local + "assets/sounds/brake/sand1.wma",
                G.local + "assets/sounds/brake/sand2.wma",
                G.local + "assets/sounds/brake/sand3.wma",
                G.local + "assets/sounds/brake/sand4.wma"]

G.blockhandler.register(Gravel)