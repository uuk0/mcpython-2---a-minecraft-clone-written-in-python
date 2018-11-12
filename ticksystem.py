import globals as G
import log

"""tickhandler"""
class TickHandler:
    def __init__(self):
        self.totick = {}
        self.activetick = 0

    """callen when the game is ticked. only used by window"""
    def _tick(self, dt):
        if self.activetick in self.totick:
            funcs = self.totick[self.activetick]
            del self.totick[self.activetick]
            log.printMSG(funcs)
            self.activetick += 1
            for e in funcs:
                e[0](*e[1], **e[2])
        else:
            self.activetick += 1

    """adds an function to tickmap"""
    def tick(self, function, args=[], kwargs={}, tick=0):
        tick += self.activetick
        if not tick in self.totick: self.totick[tick] = []
        self.totick[tick].append([function, args, kwargs])

G.tickhandler = TickHandler()