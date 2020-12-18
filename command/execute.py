"""
this is an raw implementation of the execute command of minecraft.
it is very unstable
use it on your own risk
"""

import log
import globals as G
import command.util as commandutil
import mathhelper

log.printMSG(__doc__)


class ExecuteCommand(G.commandclass):
    CONDITIONS = {}
    # a list of extra conditions in format <conditionname>:<function to check>
    # returns an bool and an int containg if the condition is True and how much space is used
    # the function is definited as: <function>(command: list[str], index: int, entity, position: tuple)

    @staticmethod
    def isCommand(command):
        return command.split(" ")[0] == "/execute"

    @staticmethod
    def executeCommand(command, entity, position):
        splitted = command.split(" ")
        index = 1
        while index < len(splitted) - 1:
            c = splitted[index]
            index += 1
            if c == "as":
                entitys = G.selectorhandler.parse(splitted[index], position, entity)
                index += 1
                for e in entitys:
                    ExecuteCommand.executeCommand(
                        "/execute " + " ".join(splitted[index:]), e, position
                    )
                return
            elif c == "at":
                entitys = G.selectorhandler.parse(splitted[index], position, entity)
                index += 1
                for e in entitys:
                    ExecuteCommand.executeCommand(
                        "execute " + " ".join(splitted[index:]), entity, e.position
                    )
                return
            elif c == "positioned":
                x, y, z = tuple(splitted[index : index + 3])
                x, y, z = float(x), float(y), float(z)
                position = commandutil.parseStringPosition(x, y, z, position)
                index += 3
            elif c == "if":
                sc = splitted[index]
                index += 1
                if sc == "entity":
                    entitys = G.selectorhandler.parse(splitted[index], entity, position)
                    if len(entitys) == 0:
                        return
                    index += 1
                elif sc == "block":
                    pos = tuple(splitted[index : index + 3])
                    index += 3
                    pos = mathhelper.normalize(
                        commandutil.parseStringPosition(
                            pos[0], pos[1], pos[2], position
                        )
                    )
                    cx, _, cz = mathhelper.sectorize(pos)
                    chunkprovider = (
                        G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    )
                    if (
                        pos not in chunkprovider.world
                        and splitted[index] not in ["", "0", "air", "minecraft:air"]
                    ) or chunkprovider.world[pos].getName() != splitted[index]:
                        return
                    index += 1
                elif sc in ExecuteCommand.CONDITIONS:
                    function = ExecuteCommand.CONDITIONS[sc]
                    flag, index = function(splitted, index, entity, position)
                    if not flag:
                        return
                else:
                    log.printMSG("[EXECUTE][ERROR] no condition found named " + str(sc))
                    return
            elif c == "unless":
                sc = splitted[index]
                index += 1
                if sc == "entity":
                    entitys = G.selectorhandler.parse(splitted[index])
                    if len(entitys) != 0:
                        return
                    index += 1
                elif sc == "block":
                    pos = tuple(splitted[index : index + 3])
                    index += 3
                    pos = mathhelper.normalize(
                        commandutil.parseStringPosition(
                            pos[0], pos[1], pos[2], position
                        )
                    )
                    cx, _, cz = mathhelper.sectorize(pos)
                    chunkprovider = (
                        G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    )
                    flag1 = (
                        pos in chunkprovider.world
                        and chunkprovider.world[pos].getName() == splitted[index]
                    ) or splitted[index] in ["", "0", "air", "minecraft:air"]
                    if flag1:
                        return
                    index += 1
                elif sc in ExecuteCommand.CONDITIONS:
                    function = ExecuteCommand.CONDITIONS[sc]
                    flag, index = function(splitted, index, entity, position)
                    if flag:
                        return
                else:
                    log.printMSG("[EXECUTE][ERROR] no condition found named " + str(sc))
                    return
            elif c == "run":
                command = " ".join(splitted[index:])
                if not command.startswith("/"):
                    command = "/" + command
                G.commandhandler.executeCommand(command, entity, position)
                return

    @staticmethod
    def getHelp():
        return """/execute [...]: execute something. [...] is a list of commands of the following:
as [selector]: execute the command as the given entity(s)
at [selector]: execute the command at the given entity(s)
positioned [position]: like at, but instead of an entity, an real position is given
if entity [selector]: only executed if selector entity amount > 0
if block [position] [blockname]: only executed if position contains blockname
unless entity [selector]: only executed if selector entity amount == 0
unless block [position] [blockname]: only executed if position contains not blockname
run [command]: run another command if all on the left it excecuted right. the line ends after the command"""


G.commandhandler.register(ExecuteCommand)
