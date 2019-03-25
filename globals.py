import sys, os

# local directory
local = os.path.dirname(sys.argv[0])

# the blockhandler instance mainly used
blockhandler = None

# the main block interface. all blocks should include this
iblockclass = None

# reference to the BlockReference-class
blockreferenceclass = None

#generatehighmodel = None

#handler for all blocks. see Block.block
blockhandler = None

#super class for Blocks. see Block.block
blockclass = None

#class for IBlockInstances. see Block.block
blockinst = None

#handler for inventorys. see Inventory.inventory
inventoryhandler = None

#super class for inventorys. see Inventory.inventory
inventoryclass = None

#super class for inventorycollections. see Inventory.inventory
inventorycollection = None

#super class and object class for an inventory slot. see Inventory.inventory
inventoryslot = None

#handler for items. see Item.item
itemhandler = None

#super class for items. see Item.item
itemclass = None

#(not good) tickhandler. see TickHandler
tickhandler = None

#handler for biomes. see biomes.biome
biomehandler = None

#super class for biomes. see biomes.biome
biomeclass = None

#a handler for everything which is callen during runtime - only some direct-events are callen direct from pyglet
eventhandler = None

#(not good) multiblockhandler. see multiblock
multiblockhandler = None

#entity handler. see entity.entity
entityhandler = None

#super class for entitys. see entity.entity
entityclass = None

#handler for all you hear - out of the game. see soundhandler
soundhandler = None

#handler for everthing that can be definited and is not to big - like trees. see structur
structurhandler = None

#handler for everything you can make out of other things. like crafting an craftingtable
craftinghandler = None

#handler for everything you can trigger when you are entering something into chat. see command.Command
commandhandler = None

#super class for commands. see command.Command
commandclass = None

#handler for the selection of who you want to do with. see command.selector
selectorhandler = None

#handler for the diffrent looks of the window - may be callen states. see state.State
statehandler = None

#handler for the diffrent worlds. see Dimensions
dimensionhandler = None

#handler for the things that objects can have - some tags which they have like others. see notations
notationhandler = None

#handler for the ability to store things
storagehandler = None

#The active state of game
State = None

#super class for all Mods. see ModLoader
mod = None

#list of all loaded mods
MODS = []

#handler for all mods. see ModLoader
modloader = None

#the chat of the game. see chat
chat = None

#the active model of the whole world. see model
model = None

#the active window. see window
window = None

#ok, that's you. Don't ask what is stored there. Or if you want, look in player.py
player = None

#system for images
textureatlashandler = None

#system for what it look like
modelhandler = None

#system for what you give us to run with
argumenthandler = None

# system for scoreboards
scoreboardhandler = None


import random
#the seed of the world. is overwritten when loading an world
seed = random.randint(-1000, 1000) * 10

#outdated gen objects
#HighMAP = {}
#TemperaturMAP = {}
#BiomeMAP = {}
#NoiseMap = {} #chunk -> (x, z) -> positions

#a usefull system for blocks which should be setted step by step
BlockGenerateTasks = {} #position -> [<name>,  optional:<data>]

GeneratedSectors = []

#game stage representing an stage
#0: not-started
#1: loading mods
#2: generating world
#3: game running
GAMESTAGE = 0

#language system. see language
class LANG:
    active = None

with open(local+"/version.info") as f:
    _data = f.read()
_line = None
for l in _data.split("\n"):
    if not l.startswith(" ") and l != "" and not "fix" in l:
        _line = l
VERSION_NAME = _line.split(" ")[1][:-1]
#format: [YEAR][WEEK][VERSION_PRE_FROM_LETTER]
LETTER_DICT = {}
for i, e in enumerate(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")):
    LETTER_DICT[e] = i

def convertNameToId(name):
    return int("20"+name[:2]+name[3:5]+str(LETTER_DICT[name[5]]))
VERSION_ID = convertNameToId(VERSION_NAME)

SPAWNPOINT = (0, 0, 0)
