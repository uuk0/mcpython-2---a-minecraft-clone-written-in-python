import globals as G


class Notation:
    def __init__(self, name):
        self.items = {}
        self.name = name
        G.notationhandler._addNotation(self)

    def notate(self, object, string):
        if not string in self.items:
            self.addGroup(string)
        self.items[string].append(object)

    def addGroup(self, string):
        self.items[string] = []

    def getName(self):
        return self.name


class NotationHandler:
    def __init__(self):
        self.notations = {}

    def _addNotation(self, notation):
        if type(notation) != Notation:
            notation = notation()
        self.notations[notation.getName()] = notation

    def notate(self, notation, string, obj):
        self.notations[notation].notate(obj, string)


G.notationhandler = NotationHandler()

OREDICT = Notation("oredict")
OREDICT.addGroup("armor:heads")
OREDICT.addGroup("armor:bodys")
OREDICT.addGroup("armor:leggins")
OREDICT.addGroup("armor:foots")
DESTROYGROUP = Notation("destroygroup")


class OreDictItems:
    STONE = "minecraft:oredict:stone"
    STONEBRICK = "minecraft:oredict:stonebrick"
    POLISHED_STONE = "minecraft:oredict:polished_stone"
    COBBELSTONE = "minecraft:oredict:cobbelstone"
    WOOD_LOG = "minecraft:oredict:wood_log"
    WOOD_PLANK = "minecraft:oredict:wood_plank"
    DIRT = "minecraft:oredict:dirt"


class DestroyGroupItems:
    PICKAXE = "minecraft:destroygroup:pickaxe"


