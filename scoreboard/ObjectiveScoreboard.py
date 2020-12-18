import globals as G
import scoreboard.IScoreBoardType


class ObjectiveScoreboard(scoreboard.IScoreBoardType.ScoreBoard):
    @staticmethod
    def getName():
        return "minecraft:scoreboard:objective"

    @staticmethod
    def getCommandName():
        return "objective"

    @staticmethod
    def execute_from_command(line):  # /scoreboard access to scoreboard
        splitted = line.split(" ")
        if splitted[2] == "add":
            name = splitted[3]
            G.scoreboardhandler.add_scoreboard(name, ObjectiveScoreboard.getName())

    def create(self, *args, **kwargs):
        self.table = {}

    def set_value(self, index, value):
        self.table[index] = value

    def get_value(self, index):
        return self.table[index]

    def get_value_names(self):
        return self.table.keys()


G.scoreboardhandler.register_scoreboard_type(ObjectiveScoreboard)
