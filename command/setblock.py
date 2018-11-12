import globals as G

class Setblock:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/setblock"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        selector = G.selectorhandler.parse(splitted[1], position, entity)
        if selector != None:
            if len(selector) == 0:
                G.chat.printLine("in /setblock: selector is not selecting any entity", color=(1, 0, 0))
                return
            if len(selector) > 1:
                G.chat.printLine("in /setblock: selector is giving more than 1 entity back", color=(1, 0, 0))
                return
            splitted = splitted[2:]
            pos = selector[0].position
        else:
            pos = int(splitted[1]), int(splitted[2]), int(splitted[3])
        G.model.add_block(pos, splitted[4])

    @staticmethod
    def getHelp():
        return "/setblock {<x>, <y>, <z>; <entity>} <block>: set the given block to given position"

G.commandhandler.register(Setblock)