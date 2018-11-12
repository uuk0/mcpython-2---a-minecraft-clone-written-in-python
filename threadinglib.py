import traceback

"""
libary for "threading" without realy threading
it's using an real Thread to switch between diffrent "threads"
"""

def dictToAttrList(d):
    al = ""
    for e in d.keys():
        al += str(e) + "=" + str(d[e]) + ", "
    return al if al == "" else al[:-2]
class Function:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
        self.command_list = []
        self.nextcommand = 0
        self.space = {}
        self.thread = None
        self.line_3_flag = False
        self.functionspace = {}

    def addPythonLine(self, line):
        self.command_list.append([0, line])
        return len(self.command_list) - 1

    def addCondition(self, condition, goto):
        self.command_list.append([1, condition, goto])
        return len(self.command_list) - 1

    def addReturn(self, valuename):
        self.command_list.append([2, valuename])
        return len(self.command_list) - 1

    def addWaitForThread(self, threadid, commandid):
        self.command_list.append([3, threadid, commandid])
        return len(self.command_list) - 1

    def addFunctionCall(self, function, args, kwargs):
        """function to add an call to another function
set command_list attribute to a function to make this possible
otherwise it will be stored to memory
"""
        if not hasattr(function, "command_list"):
            self.functionspace[function.__name__] = function
            self.addPythonLine(function.__name__+"("+str(args)[1:-1]+dictToAttrList(kwargs))
            return
        f = function.command_list
        fc = []
        for e in f:
            if e[0] == 1:
                e[2] += len(self.command_list)
            fc.append(e)
        id = len(self.command_list)
        self.command_list += fc
        return  id

    def executeOneLine(self, g):
        if self.nextcommand >= len(self.command_list): return False
        line = self.command_list[self.nextcommand]
        if line[0] == 0:
            self.nextcommand += 1
            exec(line[1], g, self.space)
        elif line[0] == 1:
            space = {}
            exec("a="+line[1], space)
            if space["a"]:
                self.nextcommand = line[2]
            else:
                self.nextcommand += 1
        elif line[0] == 2:
            if self.thread:
                self.thread.return_value = self.space[line[1]]
            return self.space[line[1]]
        elif line[0] == 3:
            if self.line_3_flag:
                self.line_3_flag = False
                self.nextcommand += 1
            elif NEXTTHREADID[line[1]].nextcommand == line[2]:
                self.self.line_3_flag = True

    def setAttr(self, *args, **kwargs):
        for i, e in enumerate(args):
            self.space[self.args[i]] = e
        for k in self.kwargs.keys():
            if k in kwargs: self.space[k] = kwargs[k]
            else: self.space[k] = self.kwargs[k]

    def __call__(self, *args, **kwargs):
        self.setAttr(*args, **kwargs)
        flag = None
        while flag != False:
            flag = self.executeOneLine(globals())
            if flag != None:
                return flag

    def copy(self):
        f = Function(self.args, self.kwargs)
        f.command_list = self.command_list
        f.thread = self.thread
        return f
        
THREADS = []
IDTOTHREAD = {}
NEXTTHREADID = 0
local = locals()

class Thread:
    def __init__(self, function, args, kwargs):
        self.function = function.copy()
        self.function.thread = self
        self.function.setAttr(*args, **kwargs)
        for e in self.function.functionspace.keys():
            self.function.space[e] = self.function.functionspace[e]
        THREADS.append(self)
        self.return_value = None
        self.id = NEXTTHREADID
        NEXTTHREADID += 1
        self.IDTOTHREAD[self.id] = self

def start():
    g = local
    tid = 0
    while len(THREADS) > 0:
        if tid > len(THREADS)-1:
            tid = 0
        thread = THREADS[tid]
        try:
            thread.function.executeOneLine(g)
        except:
            THREADS.remove(thread)
            traceback.print_exc()
        tid += 1
