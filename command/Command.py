import globals as G
from . import selector

"""command parser"""
class CommandHandler:
    def __init__(self):
        self.commands = []

    """execute an command"""
    def executeCommand(self, line, entity, position):
        for command in self.commands:
            if command.isCommand(line):
                command.executeCommand(line, entity, position)
                return
        G.chat.printLine("can't execute command. command is not found")
        G.chat.printLine(self.commands)

    def register(self, command):
        self.commands.append(command)
        G.eventhandler.call("game:registry:on_command_registrated", command)

G.commandhandler = CommandHandler()

class CommandClass:
    @staticmethod
    def isCommand(command):
        return False

    @staticmethod
    def executeCommand(command, entity, position):
        pass

    @staticmethod
    def getHelp():
        return ""

G.commandclass = CommandClass

def loadCommands(*args):
    from . import give, setblock, time

G.eventhandler.on_event("game:registry:on_command_registrate_periode", loadCommands)