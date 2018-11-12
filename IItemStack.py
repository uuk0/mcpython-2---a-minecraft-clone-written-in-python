import globals as G
import texturhandler
import pyglet
import Item.item
import log

"""class for ItemStack"""
class IItemStack:
    def __init__(self, name, amount=1):
        self.slot = None
        if type(name) == str:
            self.name = name
            self.item = G.itemhandler.getByName(name)()
        elif type(name) == G.itemclass:
            self.name = name.getName()
            self.item = name
        elif name == None:
            self.name = None
            self.item = None
        else:
            log.printMSG("[IItemStack][ERROR] can't set item "+str(name))
            self.name = None
            self.item = None
        self.__amount = amount
        if self.item:
            texturhandler.resize(self.item.getTexturFile(), (32, 32), self.item.getTexturFile())
            self.image = pyglet.sprite.Sprite(pyglet.image.load(self.item.getTexturFile()))
        else:
            self.image = None
        self.texturfile = self.item.getTexturFile() if self.item else None
        self.lable = pyglet.text.Label('', font_name='Arial', font_size=10, anchor_x='left', anchor_y='top',
            color=(255, 255, 255, 255))
        self.update_func = None

    def __getamount(self):
        return self.__amount

    def __setamount(self, amount):
        self.__amount = amount
        if self.update_func: self.update_func(self.slot)

    amount = property(__getamount, __setamount)

    """draws the image of the item"""
    def drawImage(self, position):
        if self.amount == 0 and self.item:
            self.slot.setItem(None)
        if not self.item: return
        if self.item.getTexturFile() != self.texturfile:
            texturhandler.resize(self.item.getTexturFile(), (32, 32), self.item.getTexturFile())
            self.image = pyglet.sprite.Sprite(pyglet.image.load(self.item.getTexturFile()))
            self.texturfile = self.item.getTexturFile()
        self.image.position = position
        self.image.draw()
        self.lable.x = position[0] + 32
        self.lable.y = position[1] + 4
        if self.amount != 1:
            self.lable.text = str(self.amount)
            self.lable.draw()