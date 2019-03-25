import globals as G
import mathhelper
import modsystem.ModLoader


class Sand(G.iblockclass):
    """class for sand"""
    def getName(self):
        return "minecraft:sand"

    def getModelFile(self, inst):
        return "minecraft:sand"

    def getStateName(self, inst):
        return "sand"

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


class RedSand(Sand):
    """class for redsand"""
    def getName(self):
        return "minecraft:red_sand"

    def getModelFile(self, inst):
        return "minecraft:sand"

    def getStateName(self, inst):
        return "red_sand"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating sand & red sand")
def register():
    G.blockhandler.register(RedSand)
    G.blockhandler.register(Sand)

