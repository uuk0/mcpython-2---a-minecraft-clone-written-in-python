import pyglet
import globals as G
import IItemStack
import log


class ToolTip:
    def __init__(self, stack=None):
        self.__stack = stack
        self.image = pyglet.sprite.Sprite(pyglet.image.load(G.local+"/assets/minecraft/textures/tooltip.png"))
        self.labels = []

    def setStack(self, stack):
        if type(stack) != IItemStack.IItemStack:
            stack = IItemStack.IItemStack(stack)
        self.__stack = stack

    def getStack(self):
        return self.__stack

    def draw(self, position):
        if not (self.stack and self.stack.item):
            return
        if G.player.inventory.inventorys[0] == 0:
            return
        self.image.x, self.image.y = position
        self.image.draw()
        text = self.__stack.item.getToolTipText()
        if text.count("\n")+1 > len(self.labels):
            for i in range(len(self.labels), text.count("\n") - len(self.labels)+1):
                self.labels.append(pyglet.text.Label(color=(0, 0, 0, 255)))
                # log.printMSG(self.labels[-1].x, position[0])
        for i, e in enumerate(self.labels):
            self.labels[i].x = position[0] + 10
            self.labels[i].y = position[1] + 180 - (i + 1) * 5
        for i, e in enumerate(text.split("\n")):
            self.labels[i].text = e
            self.labels[i].draw()

    stack = property(getStack, setStack)

