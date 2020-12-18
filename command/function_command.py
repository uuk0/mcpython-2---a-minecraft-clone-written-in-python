import globals as G
import mathhelper
import command.Function as Function
import os


class FunctionCommand:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/function"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        index = splitted[1]
        if index not in Function.FUNCTIONTABLE and not index.startswith(
            G.local + "/datapacks"
        ):
            if os.path.isfile(G.local + "/datapacks/" + index + ".mcfunction"):
                index = G.local + "/datapacks/" + index + ".mcfunction"
            elif os.path.isfile(G.local + "/datapacks/" + index):
                index = G.local + "/datapacks/" + index
        Function.execute_function(index, entity, position)

    @staticmethod
    def getHelp():
        return "/function <name_or_file_or_index>: executes an function"


G.commandhandler.register(FunctionCommand)
