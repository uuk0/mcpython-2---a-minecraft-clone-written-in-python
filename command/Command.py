import globals as G
from . import selector
import modsystem.ModLoader


class CommandHandler:
    """command parser"""

    def __init__(self):
        self.commands = []

    def executeCommand(self, line, entity, position):
        """execute an command"""
        for command in self.commands:
            if command.isCommand(line):
                command.executeCommand(line, entity, position)
                return True
        G.chat.printLine("can't execute command. command is not found")
        # G.chat.printLine(self.commands)
        return False

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


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_command_registrate_periode",
    "minecraft",
    info="registrating commands",
)
def register():
    from . import (
        give,
        setblock,
        time,
        generate,
        gamemode,
        reload,
        save,
        load,
        setharts,
        function_command,
        execute,
    )
