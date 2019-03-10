import globals as G
import log


class _Function:
    def __init__(self, data, index=None):
        self.data = data
        FUNCTIONS.append(self)
        if index:
            FUNCTIONTABLE[index] = self

    @staticmethod
    def from_file(file):
        if file.startswith(G.local+"/datapacks/"):
            index = file[len(G.local+"/datapacks/")+1:len(".mcfunction")]
        else:
            index = None
        if index in FUNCTIONTABLE: return FUNCTIONTABLE[index]
        with open(file) as f:
            return _Function(f.read(), index=index)

    def execute(self, entity=None, position=None):
        if not entity:
            entity = G.player.entity
        if not position:
            position = entity.position
        for line in self.data.split("\n"):
            if not line.startswith("#") and any([x not in [" ", "   "] for x in line]):
                if not line.startswith("/"):
                    line = "/" + line
                G.commandhandler.executeCommand(line, entity, position)


FUNCTIONS = []
FUNCTIONTABLE = {}


def get_function_for(file): return _Function.from_file(file)


def execute_function(file, entity=None, position=None):
    function = get_function_for(file)
    function.execute(entity=entity, position=position)

