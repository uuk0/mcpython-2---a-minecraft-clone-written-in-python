import globals as G
import mathhelper

GAMEMODE_CONVERT = {"survival":0, "creative":1, "adventure":2, "spectator":3}

class Reload:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/reload"

    @staticmethod
    def executeCommand(command, entity, position):
        G.model.change_sectors(G.window.get_motion_vector(), None)
        for chunkprovider in G.player.dimension.worldprovider.chunkproviders.values():
            for e in chunkprovider.shown.keys():
                if e in chunkprovider.world:
                    chunkprovider.world[e].hide()
                if e in chunkprovider.shown:
                    del chunkprovider.shown[e]
        G.tickhandler.tick(G.model.change_sectors, args=[None, G.window.get_motion_vector()], tick=5)

    @staticmethod
    def getHelp():
        return "/reload: reload the world"

G.commandhandler.register(Reload)