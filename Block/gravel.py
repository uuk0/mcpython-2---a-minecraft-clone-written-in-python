import globals as G
import mathhelper
import modsystem.ModLoader
import mathhelper


class Gravel(G.iblockclass):
    """class for Gravel"""
    def getName(self):
        return "minecraft:gravel"

    def getModelFile(self, inst):
        return "minecraft:gravel"

    def getStateName(self, inst):
        return "default"

    def isBrakeAbleInGamemode0(self, inst):
        return True

    """makes the block falling"""
    def on_block_update(self, inst):
        (x, y, z) = inst.position
        cx, _, cz = mathhelper.sectorize(inst.position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if not (x, y-1, z) in chunkprovider.world and y > 0 and not (hasattr(inst, "blocked") and not inst.blocked):
            inst.blocked = True
            G.tickhandler.tick(self.on_tick_update, args=[inst], tick=4)

    """fall the block"""
    def on_tick_update(self, inst):
        (x, y, z) = inst.position
        cx, _, cz = mathhelper.sectorize(inst.position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if not (x, y - 1, z) in chunkprovider.world and y > 0:
            G.model.add_block((x, y-1, z), inst)
            G.model.remove_block((x, y, z))
        inst.blocked = False

    def getBrakeSoundFile(self, inst):
        return [G.local + "/assets/minecraft/sounds/brake/sand1.wma",
                G.local + "/assets/minecraft/sounds/brake/sand2.wma",
                G.local + "/assets/minecraft/sounds/brake/sand3.wma",
                G.local + "/assets/minecraft/sounds/brake/sand4.wma"]


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating gravel")
def register():
    G.blockhandler.register(Gravel)

