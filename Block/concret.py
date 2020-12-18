import globals as G
import log
import modsystem.ModLoader
import mathhelper


class Concret(G.iblockclass):
    """
    main class for concret
    """

    def getName(self):
        return "minecraft:" + str(self.getColor()) + "_concret"

    @staticmethod
    def getColor():
        return ""

    def getStateName(self, inst):
        return self.getColor()

    def get_model_address(self, inst):
        return "minecraft:concret"


class ConcretPowder(Concret):
    def getName(self):
        return "minecraft:" + str(self.getColor()) + "_concret_powder"

    def get_model_address(self, inst):
        return "minecraft:concret_powder"

    def on_block_update(self, inst):
        """makes the block falling"""
        (x, y, z) = inst.position
        cx, _, cz = mathhelper.sectorize(inst.position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if (
            not (x, y - 1, z) in chunkprovider.world
            and y > 0
            and not (hasattr(inst, "blocked") and not inst.blocked)
        ):
            inst.blocked = True
            G.tickhandler.tick(self.on_tick_update, args=[inst], tick=4)

    def on_tick_update(self, inst):
        """fall the block"""
        (x, y, z) = inst.position
        cx, _, cz = mathhelper.sectorize(inst.position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if not (x, y - 1, z) in chunkprovider.world and y > 0:
            G.model.add_block((x, y - 1, z), inst)
            G.model.remove_block((x, y, z))
        inst.blocked = False


class BlackConcret(Concret):
    @staticmethod
    def getColor():
        return "black"


class BlackConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "black"


class BlueConcret(Concret):
    @staticmethod
    def getColor():
        return "blue"


class BlueConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "blue"


class BrownConcret(Concret):
    @staticmethod
    def getColor():
        return "brown"


class BrownConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "brown"


class CyanConcret(Concret):
    @staticmethod
    def getColor():
        return "cyan"


class CyanConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "cyan"


class GrayConcret(Concret):
    @staticmethod
    def getColor():
        return "gray"


class GrayConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "gray"


class GreenConcret(Concret):
    @staticmethod
    def getColor():
        return "green"


class GreenConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "green"


class LightBlueConcret(Concret):
    @staticmethod
    def getColor():
        return "light_blue"


class LightBlueConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "light_blue"


class LightGrayConcret(Concret):
    @staticmethod
    def getColor():
        return "light_gray"


class LightGrayConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "light_gray"


class LimeConcret(Concret):
    @staticmethod
    def getColor():
        return "lime"


class LimeConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "lime"


class MagentaConcret(Concret):
    @staticmethod
    def getColor():
        return "magenta"


class MagentaConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "magenta"


class OrangeConcret(Concret):
    @staticmethod
    def getColor():
        return "orange"


class OrangeConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "orange"


class PinkConcret(Concret):
    @staticmethod
    def getColor():
        return "pink"


class PinkConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "pink"


class PurpleConcret(Concret):
    @staticmethod
    def getColor():
        return "purple"


class PurpleConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "purple"


class RedConcret(Concret):
    @staticmethod
    def getColor():
        return "red"


class RedConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "red"


class WhiteConcret(Concret):
    @staticmethod
    def getColor():
        return "white"


class WhiteConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "white"


class YellowConcret(Concret):
    @staticmethod
    def getColor():
        return "yellow"


class YellowConcretPowder(ConcretPowder):
    @staticmethod
    def getColor():
        return "yellow"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating concret & concretpowder",
)
def register_concret(*args):
    G.blockhandler.register(BlackConcret)
    G.blockhandler.register(BlackConcretPowder)
    G.blockhandler.register(BlueConcret)
    G.blockhandler.register(BlueConcretPowder)
    G.blockhandler.register(BrownConcret)
    G.blockhandler.register(BrownConcretPowder)
    G.blockhandler.register(CyanConcret)
    G.blockhandler.register(CyanConcretPowder)
    G.blockhandler.register(GrayConcret)
    G.blockhandler.register(GrayConcretPowder)
    G.blockhandler.register(GreenConcret)
    G.blockhandler.register(GreenConcretPowder)
    G.blockhandler.register(LightBlueConcret)
    G.blockhandler.register(LightBlueConcretPowder)
    G.blockhandler.register(LightGrayConcret)
    G.blockhandler.register(LightGrayConcretPowder)
    G.blockhandler.register(LimeConcret)
    G.blockhandler.register(LimeConcretPowder)
    G.blockhandler.register(MagentaConcret)
    G.blockhandler.register(MagentaConcretPowder)
    G.blockhandler.register(OrangeConcret)
    G.blockhandler.register(OrangeConcretPowder)
    G.blockhandler.register(PinkConcret)
    G.blockhandler.register(PinkConcretPowder)
    G.blockhandler.register(PurpleConcret)
    G.blockhandler.register(PurpleConcretPowder)
    G.blockhandler.register(RedConcret)
    G.blockhandler.register(RedConcretPowder)
    G.blockhandler.register(WhiteConcret)
    G.blockhandler.register(WhiteConcretPowder)
    G.blockhandler.register(YellowConcret)
    G.blockhandler.register(YellowConcretPowder)
