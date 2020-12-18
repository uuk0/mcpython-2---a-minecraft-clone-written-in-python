import globals as G
import log


class Time:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/time"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        if splitted[1] == "set":
            if len(splitted) > 3:
                G.chat.printLine("in /time: too much paramters were given. expected 3")
                return
            amount = splitted[2]
            if amount == "day":
                amount = 1000
            elif amount == "night":
                amount = 13000
            elif amount == "midnight":
                amount = 18000
            elif amount == "noon":
                amount = 6000
            G.window.time = int(amount)
        elif splitted[1] == "add":
            amount = splitted[2]
            if amount.endswith("d"):
                amount = int(amount[:-1]) * 24000
            elif amount.endswith("h"):
                amount = int(amount[:-1]) * 1000
            G.window.time += int(amount)

    @staticmethod
    def getHelp():
        return [
            "/time set {<time>, 'day', 'night', 'midnight', 'noon'}",
            "/time add <time>",
        ]


G.commandhandler.register(Time)
