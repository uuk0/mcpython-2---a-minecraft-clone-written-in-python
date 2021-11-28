import command.Function as Function
import globals as G
import mathhelper

GAMEMODE_CONVERT = {"survival": 0, "creative": 1, "adventure": 2, "spectator": 3}


class Reload:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/reload"

    @staticmethod
    def executeCommand(command, entity, position):
        Function.FUNCTIONS = []
        Function.FUNCTIONTABLE = {}

    @staticmethod
    def getHelp():
        return "/reload: reload all datapacks"


G.commandhandler.register(Reload)
