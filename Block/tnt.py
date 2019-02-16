import random

import globals as G
import log
import mathhelper
import modsystem.ModLoader

SURROUNDING = [(0, 0, -1, "N"), (0, 0, 1, "S"), (0, -1, 0, "U"), (0, 1, 0, "D"), (-1, 0, 0, "W"), (1, 0, 0, "O")]


class Tnt(G.blockclass):
    """class for tnt"""
    def getName(self):
        return "minecraft:tnt"

    def getModelFile(self, inst):
        return "minecraft:tnt"

    def light(self, inst=None):
        G.tickhandler.tick(self.explose, args=[inst], tick=random.randint(15, 25))

    def explose(self, inst):
        #cavegenerator._cutoutcircle(inst.position[0], inst.position[1], inst.position[2],
        #5)
        pass

    def on_redstone_update(self, inst):
        x, y, z = inst.position
        flag = False
        for dx, dy, dz, face in SURROUNDING:
            px, py, pz = x + dx, y+dy, z+dz
            cx, _, cz = mathhelper.sectorize((px, py, pz))
            chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
            if (px, py, pz) in chunkprovider.world and \
                    chunkprovider.world[(px, py, pz)].getErmittedRedstoneSignal(face) > 0:
                flag = True
        if flag:
            self.light(inst)

    def on_block_update(self, inst):
        self.on_redstone_update(inst)

    def getInventorys(self, inst):
        self.light(inst)
        return []

    def isOpeningInventory(self, inst, item):
        return item.item.getName() == "minecraft:flint_and_steel"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating tnt")
def register():
    G.blockhandler.register(Tnt)

