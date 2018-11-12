import globals as G
import mathhelper
import random
import log
SURROUNDING = [(0, 0, -1, "N"), (0, 0, 1, "S"), (0, -1, 0, "U"), (0, 1, 0, "D"), (-1, 0, 0, "W"), (1, 0, 0, "O")]

"""class for tnt"""
class Tnt(G.blockclass):
    def getName(self):
        return "minecraft:tnt"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 0), (0, 2), (0, 1), n2=4)

    def getTexturFile(self, inst):
        return "minecraft/tnt"

    def getAllTexturFiles(self):
        return ["minecraft/tnt"]

    def light(self):
        G.tickhandler.tick(self.explose, tick=random.random(15, 25))

    def explose(self):
        log.printMSG("can't explose TNT. function is not definited.\n" + \
                     "to definit, add an block named minecraft:tnt with these functions")

    def on_redstone_update(self, inst):
        x, y, z = inst.position
        flag = False
        for dx, dy, dz, face in SURROUNDING:
            px, py, pz = x + dx, y+dy, z+dz
            if (px, py, pz) in G.model.world and G.model.world[(px, py, pz)].getErmittedRedstoneSignal(face) > 0:
                flag = True
        if flag:
            self.explose()

    def on_block_update(self, inst):
        self.on_redstone_update(inst)

G.blockhandler.register(Tnt)