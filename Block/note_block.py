import globals as G
import mathhelper
import modsystem.ModLoader


class NoteBlock(G.iblockclass):
    """class for obsidian"""
    def getName(self):
        return "minecraft:note_block"

    def getModelFile(self, inst):
        return "minecraft:note_block"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating note block")
def register():
    G.blockhandler.register(NoteBlock)

