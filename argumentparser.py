import sys
import globals as G

class ArgumentError(Exception): pass

class ArgumentHandler:
    def __init__(self):
        self.argumenttypes = []

    def register(self, type):
        self.argumenttypes.append(type)

    def parseArguments(self):
        argumentpointer = 1
        while len(sys.argv)-1 >= argumentpointer:
            flag = True
            for e in self.argumenttypes:
                if flag and e.isArgument(argumentpointer):
                    e.parseArgument(argumentpointer)
                    argumentpointer += e.getCommandLenght(argumentpointer)
                    flag = False
            if flag:
                raise ArgumentError("unknown argument for system at "+str(argumentpointer)+" in "+str(sys.argv))


G.argumenthandler = ArgumentHandler()


class ArgumentType:
    @staticmethod
    def isArgument(argumentindex):
        return False

    @staticmethod
    def getCommandLenght(argumentindex):
        return 1

    @staticmethod
    def parseArgument(argumentindex):
        pass


class IgnoreVersionIncompatibles(ArgumentType):
    @staticmethod
    def isArgument(argumentindex):
        return sys.argv[argumentindex] == "--deactivateversionicompatibles"


G.argumenthandler.register(IgnoreVersionIncompatibles)
