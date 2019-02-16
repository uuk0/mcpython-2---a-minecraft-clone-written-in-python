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
        G.player.dimension.worldgenerator.prepareChunk(cx, cz)
        G.player.dimension.worldgenerator.generateChunk(cx, cz)
        G.tickhandler.tick(G.model.show_sector, args=[(cx, 0, cz)], tick=10)
        #G.model.show_sector((cx, 0, cz))

    @staticmethod
    def getHelp():
        return "/generate: generate the chunk in which you are in"

G.commandhandler.register(Generate)