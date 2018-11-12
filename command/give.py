import globals as G

class Give:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/give"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        if splitted[0] != "/give":
            G.chat.printLine("in /give: can't execute command as give. Command starts NOT with /give", color=(1, 0, 0))
            return
        if len(splitted) == 1:
            G.chat.printLine("in /give: missing selector & item name", color=(1, 0, 0))
            return
        selector = G.selectorhandler.parse(splitted[1], position, entity)
        if selector == None:
            G.chat.printLine("in /give: selector is not known", color=(1, 0, 0))
            return
        if len(selector) == 0:
            G.chat.printLine("in /give: selector is not selecting any entity", color=(1, 0, 0))
            return
        if len(selector) > 1:
            G.chat.printLine("in /give: selector is giving more than 1 entity back", color=(1, 0, 0))
            return
        selector = selector[0]
        if "player" in selector.tags:
            selector.player.addToInventory(splitted[2], 1 if len(splitted) == 3 else int(splitted[3]))
        else:
            G.chat.printLine("in /give: selector is not an player "+str(selector)+" "+str(selector.tags))

    @staticmethod
    def getHelp():
        return "/give <entity> <item> [<amount>]: gives the player the selected item"

G.commandhandler.register(Give)