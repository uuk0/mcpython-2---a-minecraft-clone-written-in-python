import globals as G
import mathhelper
import modsystem.ModLoader


SURROUNDING = [(0, 0, -1, "N"), (0, 0, 1, "S"), (0, -1, 0, "U"), (0, 1, 0, "D"), (-1, 0, 0, "W"), (1, 0, 0, "O")]


class RedstoneLamp(G.iblockclass):
    """class for redstone lamp"""

    def getName(self):
        return "minecraft:redstone_lamp"

    def getDefaultData(self, inst):
        return {"active":False}

    def getModelFile(self, inst):
        return "minecraft:redstone_lamp"

    def getStateName(self, inst):
        return "active" if inst.data["active"] else "inactive"

    def on_redstone_update(self, inst):
        """
        x, y, z = inst.position
        flag = False
        for dx, dy, dz, face in SURROUNDING:
            px, py, pz = x + dx, y+dy, z+dz
            cx, _, cz = mathhelper.sectorize((px, py, pz))
            chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
            if (px, py, pz) in chunkprovider.world and chunkprovider.world[(px, py, pz)].getErmittedRedstoneSignal(face) > 0:
                flag = True
        if inst.data["active"] != flag:
            inst.data["active"] = flag
            G.model.hide_block(inst.position, inst)
            G.model.show_block(inst.position)"""

    def on_block_update(self, inst):
        self.on_redstone_update(inst)


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating redstone lamp")
def register():
    G.blockhandler.register(RedstoneLamp)

