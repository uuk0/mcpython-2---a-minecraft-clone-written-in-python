import globals as G
import modsystem.ModLoader


class BookShelf(G.iblockclass):
    """class for book shelf"""

    def getName(self):
        return "minecraft:bookshelf"


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_block_registrate_periode",
    "minecraft",
    info="registrating book shelf",
)
def register():
    G.blockhandler.register(BookShelf)
