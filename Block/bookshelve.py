import globals as G
import mathhelper
import modsystem.ModLoader


class BookShelf(G.blockclass):
    """class for book shelf"""
    def getName(self):
        return "minecraft:bookshelf"

    def getModelFile(self, inst):
        return "minecraft:bookshelve"


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating book shelf")
def register():
    G.blockhandler.register(BookShelf)

