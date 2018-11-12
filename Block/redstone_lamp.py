import globals as G
import mathhelper

SURROUNDING = [(0, 0, -1, "N"), (0, 0, 1, "S"), (0, -1, 0, "U"), (0, 1, 0, "D"), (-1, 0, 0, "W"), (1, 0, 0, "O")]

"""class for redstone lamp"""
class RedstoneLamp(G.blockclass):
    def _getDefaultData(self, inst):
        return {"active":False}

    def getName(self):
        return "minecraft:redstone_lamp"

    def getTexturData(self, inst):
        return mathhelper.tex_coords((0, 1), (0, 1), (0, 1), n2=2) if not inst.data["active"] else mathhelper.tex_coords((0, 0), (0, 0), (0, 0), n2=2)

    def getTexturFile(self, inst):
        return "minecraft/redstone_lamp"

    def getAllTexturFiles(self):
        return ["minecraft/redstone_lamp"]

    def on_redstone_update(self, inst):
        x, y, z = inst.position
        flag = False
        for dx, dy, dz, face in SURROUNDING:
            px, py, pz = x + dx, y+dy, z+dz
            if (px, py, pz) in G.model.world and G.model.world[(px, py, pz)].getErmittedRedstoneSignal(face) > 0:
                flag = True
        if inst.data["active"] != flag:
            inst.data["active"] = flag
            G.model.hide_block(inst.position)
            G.model.show_block(inst.position)

    def on_block_update(self, inst):
        self.on_redstone_update(inst)

G.blockhandler.register(RedstoneLamp)