"""
resource table system for mods
should be used for ores, ingots etc.
"""

__table = {}


def addEntry(name, *args, **kwargs):
    if isEntry(name): return
    __table[name] = [args, kwargs]


def getEntry(name):
    return None if name not in __table else __table[name]


def isEntry(name):
    return name in __table


"""
predefinited entrys:
ore/adamantine
ore/antimony
ore/bismuth
"""