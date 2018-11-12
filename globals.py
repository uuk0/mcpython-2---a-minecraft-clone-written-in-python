import sys, os

local = os.path.dirname(sys.argv[0])+"/"

generatehighmodel = None

blockhandler = None
texturhandler = None
blockclass = None
inventoryhandler = None
inventoryclass = None
inventorycollection = None
inventoryslot = None
itemhandler = None
itemclass = None
tickhandler = None
blockinst = None
biomehandler = None
biomeclass = None
eventhandler = None
multiblockhandler = None
entityhandler = None
entityclass = None
soundhandler = None
structurhandler = None
craftinghandler = None
texturedatahandler = None
commandhandler = None
commandclass = None
selectorhandler = None
statehandler = None

mod = None
MODS = []

modloader = None

chat = None

model = None
window = None
player = None

HighMAP = {}
TemperaturMAP = {}
BiomeMAP = {}
NoiseMap = {} #chunk -> (x, z) -> positions

BlockGenerateTasks = []
"""
list:
item 1 == 0:
add_block(position, blockname)
item 1 == 1:
function(*args, **kwargs)
item 1 == 2:
remove_block(position)
"""

GeneratedSectors = []

#game stage representing an stage
#0: not-started
#1: loading mods
#2: generating world
#3: game running
GAMESTAGE = 0

class LANG:
    active = None