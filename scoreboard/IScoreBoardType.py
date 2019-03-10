import globals as G
import log


class ScoreBoard:
    @staticmethod
    def getName(): return "minecraft:scoreboard:none"

    @staticmethod
    def getCommandName(): return None

    @staticmethod
    def execute_from_command(line):  # /scoreboard access to scoreboard
        pass

    def __init__(self, name, *args, **kwargs):
        self.name = name
        if hasattr(self, "create"):
            self.create(*args, **kwargs)
        elif len(args) + len(kwargs) > 0:
            log.printMSG("[SCOREBOARD][ERROR] getted arguments for scoreboard typed as "+str(type(self))+
                         " but it has no create-function for analysing it")
            return

    def set_value(self, index, value):
        raise NotImplementedError()

    def get_value(self, index):
        raise NotImplementedError()

    def get_value_names(self):
        raise NotImplementedError()

