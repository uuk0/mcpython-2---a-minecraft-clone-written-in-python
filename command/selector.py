import globals as G

class SelectorHandler:
    def __init__(self):
        self.selectors = []

    def register(self, selector):
        self.selectors.append(selector)

    def parse(self, selector, position, executeentity):
        for e in self.selectors:
            if e.isSelector(selector):
                return e.getEntitys(selector, position, executeentity)
        return None


G.selectorhandler = SelectorHandler()

class Selector:
    @staticmethod
    def isSelector(selector):
        return False

    @staticmethod
    def getEntitys(selector, position, executeentity):
        return []


class At_s(Selector):
    @staticmethod
    def isSelector(selector):
        return selector == "@s"

    @staticmethod
    def getEntitys(selector, position, executeentity):
        return [executeentity]

G.selectorhandler.register(At_s)