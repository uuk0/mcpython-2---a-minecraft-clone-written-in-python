import globals as G
import log

class Save:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/save"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        if len(splitted) > 1:
            d = G.local+"saves/"+splitted[1]
        elif G.window.worldname:
            d = G.window.worldname
        else:
            log.printMSG("[COMMANDPARSER][SAVE][ERROR] unknown dirname")
            return
        G.window.worldname = d
        G.storagehandler.saveWorld(d)

    @staticmethod
    def getHelp():
        return "/save [<worldname>]: save the world"

G.commandhandler.register(Save)