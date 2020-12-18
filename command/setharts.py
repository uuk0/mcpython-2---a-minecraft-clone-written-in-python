import globals as G
import log


class Setharts:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/setharts"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        amount = int(splitted[1])
        G.player.harts = amount
        G.player.updateHarts()

    @staticmethod
    def getHelp():
        return "/setharts <amount>: set the amount of harts of player"


G.commandhandler.register(Setharts)
