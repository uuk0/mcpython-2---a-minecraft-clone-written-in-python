import globals as G
import mathhelper

GAMEMODE_CONVERT = {"survival": 0, "creative": 1, "adventure": 2, "spectator": 3}


class Gamemode:
    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/gamemode"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        if len(splitted) > 2:
            entity = G.selectorhandler.parse(splitted[2], entity, position)
        else:
            entity = [entity]
        mode = splitted[1]
        if mode in GAMEMODE_CONVERT:
            mode = GAMEMODE_CONVERT[mode]
        else:
            mode = int(mode)
        for entity in entity:
            entity.player.gamemode = mode
        if mode in [0, 2]:
            G.window.flying = False
        elif mode == 3:
            G.window.flying = True

    @staticmethod
    def getHelp():
        return "/gamemode {0, 1, 2, 3, survival, creative, adventure, spectator} [<player>]: set the gamemode of the player"


G.commandhandler.register(Gamemode)
