import globals as G
import pyglet
import config
import traceback

def _isRecipi(recipi, slots):
    try:
        if not recipi: return [False, None]
        slots = slots[:-1]
        recipisize = len(recipi[0]), len(recipi[0][0])
        if recipisize == (1, 1):
            isitem = []
            slot = None
            for e in slots:
                isitem.append((e.stack and e.stack.item))
                if e.stack and e.stack.item and e.stack.item.getName() == recipi[2][recipi[0][0][0]][0] and \
                        e.stack.amount >= recipi[2][recipi[0][0][0]][1]:
                    slot = e
            if slot and isitem.count(None) == 3:
                return [True, [slot]]
        elif recipisize == (2, 2):
            items = []
            for e in recipi[0]:
                for e in e:
                    items.append(recipi[2][e] if e != " " else " ")
            flag = True
            for i, e in enumerate(items):
                if not ((slots[i].stack.item and e[0] == slots[i].stack.item.getName() and e[1] <= slots[i].stack.amount) or (not slots[i].stack.item and e[0] == " ")):
                    flag = False
            if flag:
                return [True, slots]
        elif recipisize == (1, 2):
            items = [recipi[2][recipi[0][0][0]], recipi[2][recipi[0][0][1]]]
            for i1, sl in enumerate([[slots[0], slots[2]], [slots[1], slots[3]]]):
                if all([x.stack.item and x.stack.item.getName() == items[i] for i, x in enumerate(sl)]):
                    return [True, sl]
        elif recipisize == (2, 1):
            items = [recipi[2][recipi[0][0][0]], recipi[2][recipi[0][1][0]]]
            for i1, sl in enumerate([[slots[0], slots[1]], [slots[2], slots[3]]]):
                if all([x.stack.item and x.stack.item.getName() == items[i] for i, x in enumerate(sl)]):
                    return [True, sl]
        return [False, None]
    except:
        if config.DEBUG.PRINT_CRAFTING_STUFF:
            traceback.print_exc()
        return [False, None]

"""class for playerinventory"""
class PlayerInventory(G.inventorycollection):
    tag = ["player:hotbar",
           "player:inventory",
           "system:nothideable"]
    def __init__(self):
        G.inventorycollection.__init__(self)
        self.guitype = 0

    def creatInventorys(self):
        return [Hotbar(), Rows(), Crafting()]

    def getActiveInventorys(self):
        return self.inventorys if self.guitype == 1 else self.inventorys[:1]

    def draw(self):
        self.inventorys[0].type = self.guitype
        if self.guitype == 0:
            self.inventorys[0].draw()
        else:
            for e in self.inventorys:
                e.draw()

    def shouldInteractWithPlayerInventoryMoving(self):
        return self.guitype != 0

    def isDisablyingGame(self):
        return self.guitype != 0

"""class of player inventory crafting part"""
class Crafting(G.inventoryclass):
    tag = ["player:inventory", "inventorys:crafting", "system:nothideable"]
    def __init__(self, *args, **kwargs):
        G.inventoryclass.__init__(self, *args, **kwargs)
        self.active_recipi = None
        self.used_slots = []

    def creatSlots(self):
        return [G.inventoryslot((210, 282), update_func=self.update_input),
                G.inventoryslot((248, 282), update_func=self.update_input),
                G.inventoryslot((210, 244), update_func=self.update_input),
                G.inventoryslot((248, 244), update_func=self.update_input),
                G.inventoryslot((328, (282+244)/2-2), canplayersetitems=False, update_func=self.update_input)]

    def getBasePosition(self):
        if not hasattr(G.window, "player"):
            return (0, 0)
        if G.window.player.inventory.inventorys[0].type == 1:
            return (G.window.size[0] / 2 - G.window.player.inventory.inventorys[0].image2.width / 2,
                    G.window.size[1] / 2 - G.window.player.inventory.inventorys[0].image2.height / 2)
        elif G.window.player.inventory.inventorys[0].type == 0:
            return (G.window.size[0] / 2 - G.window.player.inventory.inventorys[0].image1.width / 2,
                    G.window.size[1] / 2 - G.window.player.inventory.inventorys[0].image1.height / 2 - 270)

    """updates the recipi stored"""
    def update_input(self, slot):
        data = _isRecipi(self.active_recipi, self.slots)
        if slot in self.slots[:4] or slot == None:
            if slot and self.active_recipi and data[0] and data[1] == self.used_slots:
                return
            else:
                for e in G.craftinghandler.getRecipisFor("minecraft:crafting").values():
                    data = _isRecipi(e, self.slots)
                    if data[0]:
                        self.active_recipi = e
                        self.slots[4].setItem(*e[2][e[1][0][0]])
                        self.used_slots = data[1]
                        return
                self.active_recipi = None
                self.used_slots = []
                self.slots[4].setItem(None)
        else:
            if self.active_recipi and not (slot.stack and slot.stack.item):
                try:
                    i = 0
                    for l in self.active_recipi[0]:
                        for e in l:
                            if self.used_slots[i].stack:
                                self.used_slots[i].stack.amount -= self.active_recipi[2][e][1]
                                if i < len(self.used_slots) and self.used_slots[i].stack.amount == 0:
                                    self.used_slots[i].setItem(None)
                        i += 1
                    self.update_input(None)
                except:
                    pass

"""class of player inventory 'row' part"""
class Rows(G.inventoryclass):
    tag = ["player:inventory",
           "system:nothideable"]
    def creatSlots(self):
        slots = []
        for y in [64, 102, 140]:
            for x in [18, 56, 94, 132, 170, 209, 247, 286, 324]:
                slots.append(G.inventoryslot((x, y)))
        slots += [G.inventoryslot((18, 190)),
                  G.inventoryslot((18, 228)),
                  G.inventoryslot((18, 266)),
                  G.inventoryslot((18, 304))]
        slots.append(G.inventoryslot((165, 190)))
        return slots

    def getBasePosition(self):
        if not hasattr(G.window, "player"):
            return (0, 0)
        if G.window.player.inventory.inventorys[0].type == 1:
            return (G.window.size[0] / 2 - G.window.player.inventory.inventorys[0].image2.width / 2, G.window.size[1] / 2 - G.window.player.inventory.inventorys[0].image2.height / 2)
        elif G.window.player.inventory.inventorys[0].type == 0:
            return (G.window.size[0] / 2 - G.window.player.inventory.inventorys[0].image1.width / 2, G.window.size[1] / 2 - G.window.player.inventory.inventorys[0].image1.height / 2 - 270)

"""class of player inventory hotbar part"""
class Hotbar(G.inventoryclass):
    tag = ["player:hotbar",
           "player:inventory",
           "system:nothideable"]
    def __init__(self):
        self.image1 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "assets/textures/gui/hotbar.png"))
        self.image2 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "assets/textures/gui/container/playerinventory.png"))
        self.image3 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "assets/textures/gui/hotbar_select.png"))
        self.type = 0
        self.lasttype = 0
        G.inventoryclass.__init__(self)
        self.image1.position = self.position
        self.image2.position = self.position
        self.image3.position = self.position

    def creatSlots(self):
        return [G.inventoryslot((8, 6)),
                G.inventoryslot((47, 6)),
                G.inventoryslot((47+39, 6)),
                G.inventoryslot((47+39*2, 6)),
                G.inventoryslot((47+39*3+1, 6)),
                G.inventoryslot((47+39*4+1, 6)),
                G.inventoryslot((47+39*5+2, 6)),
                G.inventoryslot((47+39*6+2, 6)),
                G.inventoryslot((47+39*7+3, 6))]

    def draw(self):
        self.position = self.getBasePosition()
        if self.type != self.lasttype:
            if self.lasttype == 1:
                self.slots[0].position = (8, 6)
                self.slots[1].position = (47, 6)
                self.slots[2].position = (47+39, 6)
                self.slots[3].position = (47+39*2, 6)
                self.slots[4].position = (47+39*3+1, 6)
                self.slots[5].position = (47+39*4+1, 6)
                self.slots[6].position = (47+39*5+2, 6)
                self.slots[7].position = (47+39*6+2, 6)
                self.slots[8].position = (47+39*7+3, 6)

            elif self.lasttype == 0:
                self.slots[0].position = (18, 18)
                self.slots[1].position = (56, 18)
                self.slots[2].position = (56+38, 18)
                self.slots[3].position = (56+38*2, 18)
                self.slots[4].position = (56+38*3, 18)
                self.slots[5].position = (56+38*4+1, 18)
                self.slots[6].position = (56+38*5+1, 18)
                self.slots[7].position = (56+38*6+1, 18)
                self.slots[8].position = (56+38*7+1, 18)

            self.lasttype = self.type
        self.image1.position = self.position
        self.image2.position = self.position
        if self.type == 0:
            self.image1.draw()
            self.image3.x = self.image2.x + G.player.selectedinventoryslot * 40
            self.image3.y = self.image2.y
            self.image3.draw()
        elif self.type == 1:
            self.image2.draw()
        for e in self.slots:
            e.draw(self.position)

    def getBasePosition(self):
        if self.type == 1:
            return (G.window.size[0] / 2 - self.image2.width / 2, G.window.size[1] / 2 - self.image2.height / 2)
        elif self.type == 0:
            return (G.window.size[0] / 2 - self.image1.width / 2, G.window.size[1] / 2 - self.image1.height / 2 - 270)

    def shouldInteractWithPlayerInventoryMoving(self):
        return False

    def isDisablyingGame(self):
        return False
