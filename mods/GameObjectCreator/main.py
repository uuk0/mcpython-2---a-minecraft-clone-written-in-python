"""
library for creating things better
it contains loader-code for different game object types
it may NOT used by big mods because it may take some time to generate new entries during runtime
"""

import globals as G


class GameObjectCreator(G.mod):
    def getName(self): return "gameobjectcreator"

    def getFileName(self): return "GameObjectCreator"

    def getDependencies(self): return [["minecraft"]]


G.modloader.register(GameObjectCreator)

