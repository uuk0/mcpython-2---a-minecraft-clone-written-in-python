import globals as G
import log

class Load:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/load"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        if len(splitted) > 1:
            d = G.local+"saves/"+splitted[1]
        elif G.window.worldname:
            d = G.window.worldname
        else:
            log.printMSG("[COMMANDPARSER][LOAD][ERROR] unknown dirname")
            return
        G.window.worldname = d
        G.storagehandler.loadWorld(d)

    @staticmethod
    def getHelp():
        return "/load [<worldname>]: load the world"

G.commandhandler.register(Load)