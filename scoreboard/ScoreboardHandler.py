import globals as G
import log
import modsystem.ModLoader


class ScoreBoardHandler:
    def __init__(self):
        self.scoreboards = {}
        self.scoreboardtypes = {}

    def add_scoreboard(self, name, scoreboardtype, *args, **kwargs):
        if scoreboardtype not in self.scoreboardtypes:
            log.printMSG("[SCOREBOARDHANDLER][ERROR] type "+str(scoreboardtype)+" is unknown")
            return
        self.scoreboards[name] = self.scoreboardtypes[scoreboardtype](name, *args, **kwargs)

    def remove_scoreboard(self, name):
        if name not in self.scoreboards:
            log.printMSG("[SCOREBOARDHANDLER][ERROR] can't remove scoreboard named "+str(name)+". These scoreboard"+
                         " is not created.")
            return
        self.scoreboards[name].delete()
        del self.scoreboards[name]

    def clear(self):
        for scoreboard in list(self.scoreboards.keys()):
            self.remove_scoreboard(scoreboard)

    def register_scoreboard_type(self, klass):
        self.scoreboardtypes[klass.getName()] = klass


G.scoreboardhandler = ScoreBoardHandler()

@modsystem.ModLoader.ModEventEntry("game:registry:on_command_registrate_periode", "minecraft",
                                   info="registrating scoreboard stuff")
def register_scoreboard_stuff(*args):
    import scoreboard.ObjectiveScoreboard

