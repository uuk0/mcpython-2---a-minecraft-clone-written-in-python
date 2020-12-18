import globals as G
import mathhelper


class Generate:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/generate"

    @staticmethod
    def executeCommand(command, entity, position):
        chunk = mathhelper.sectorize(G.window.position)
        cx, cz = chunk[0], chunk[2]
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        chunkprovider.generate()

    @staticmethod
    def getHelp():
        return "/generate: generate the chunk in which you are in"


G.commandhandler.register(Generate)
