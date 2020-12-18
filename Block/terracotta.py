import globals as G
import log
import modsystem.ModLoader


class Terracotta(G.iblockclass):
    @staticmethod
    def getColor():
        return ""

    def getName(self):
        return "minecraft:" + self.getColor() + "_terracotta"

    def getModelFile(self, inst):
        return "minecraft:terracotta"

    def getStateName(self, inst):
        return self.getColor()


class GlazedTerracotta(G.iblockclass):
    @staticmethod
    def getColor():
        return ""

    def getName(self):
        return "minecraft:" + self.getColor() + "_glazed_terracotta"

    def getModelFile(self, inst):
        return "minecraft:glazed_terracotta"

    def getStateName(self, inst):
        return self.getColor()


class RawTerracotta(G.iblockclass):
    def getName(self):
        return "minecraft:terracotta"

    def getModelFile(self, inst):
        return "minecraft:terracotta"


class BlackTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "black"


class BlackTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "black"


class BlueTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "blue"


class BlueTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "blue"


class BrownTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "brown"


class BrownTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "brown"


class CyanTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "cyan"


class CyanTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "cyan"


class GrayTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "gray"


class GrayTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "gray"


class GreenTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "green"


class GreenTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "green"


class LightBlueTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "light_blue"


class LightBlueTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "light_blue"


class LightGrayTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "light_gray"


class LightGrayTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "light_gray"


class LimeTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "lime"


class LimeTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "lime"


class MagentaTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "magenta"


class MagentaTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "magenta"


class OrangeTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "orange"


class OrangeTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "orange"


class PinkTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "pink"


class PinkTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "pink"


class PurpleTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "purple"


class PurpleTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "purple"


class RedTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "red"


class RedTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "red"


class WhiteTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "white"


class WhiteTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "white"


class YellowTerracotta(Terracotta):
    @staticmethod
    def getColor():
        return "yellow"


class YellowTerracottaGlazed(GlazedTerracotta):
    @staticmethod
    def getColor():
        return "yellow"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating terracotta & glazed terracotta",
)
def register_concret(*args):
    G.blockhandler.register(RawTerracotta)
    G.blockhandler.register(BlackTerracotta)
    G.blockhandler.register(BlackTerracottaGlazed)
    G.blockhandler.register(BlueTerracotta)
    G.blockhandler.register(BlueTerracottaGlazed)
    G.blockhandler.register(BrownTerracotta)
    G.blockhandler.register(BrownTerracottaGlazed)
    G.blockhandler.register(CyanTerracotta)
    G.blockhandler.register(CyanTerracottaGlazed)
    G.blockhandler.register(GrayTerracotta)
    G.blockhandler.register(GrayTerracottaGlazed)
    G.blockhandler.register(GreenTerracotta)
    G.blockhandler.register(GreenTerracottaGlazed)
    G.blockhandler.register(LightBlueTerracotta)
    G.blockhandler.register(LightBlueTerracottaGlazed)
    G.blockhandler.register(LightGrayTerracotta)
    G.blockhandler.register(LightGrayTerracottaGlazed)
    G.blockhandler.register(LimeTerracotta)
    G.blockhandler.register(LimeTerracottaGlazed)
    G.blockhandler.register(MagentaTerracotta)
    G.blockhandler.register(MagentaTerracottaGlazed)
    G.blockhandler.register(OrangeTerracotta)
    G.blockhandler.register(OrangeTerracottaGlazed)
    G.blockhandler.register(PinkTerracotta)
    G.blockhandler.register(PinkTerracottaGlazed)
    G.blockhandler.register(PurpleTerracotta)
    G.blockhandler.register(PurpleTerracottaGlazed)
    G.blockhandler.register(RedTerracotta)
    G.blockhandler.register(RedTerracottaGlazed)
    G.blockhandler.register(WhiteTerracotta)
    G.blockhandler.register(WhiteTerracottaGlazed)
    G.blockhandler.register(YellowTerracotta)
    G.blockhandler.register(YellowTerracottaGlazed)
