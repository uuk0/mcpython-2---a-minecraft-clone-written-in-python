import globals as G
import log
import pyglet
import mathhelper
import config
from pyglet.window import key, mouse
import ticksystem
import texturhandler
import imagealphacreator

class StateHandler:
    def __init__(self):
        self.states = {}
        self.active_state = None

    def register(self, state):
        if type(state) != State: state = state()
        self.states[state.getName()] = state
        G.eventhandler.call("game:registry:on_state_registrated", state)

    def setState(self, name):
        if not name in self.states:
            log.printMSG("[STATEHANDLER][ERROR] can't access state named "+str(name))
            return
        if self.active_state:
            self.active_state.deactivate()
        self.active_state = self.states[name]
        self.active_state.activate()

G.statehandler = StateHandler()

EVENTNAMES = ["core:window:on_exclusive_mouse_change", "core:update", "core:window:on_mouse_press",
              "core:window:on_mouse_release", "core:window:on_mouse_motion", "core:window:on_key_press",
              "core:window:on_key_release", "core:window:on_resize", "core:window:on_close",
              "core:window:on_mouse_scroll", "opengl:draw2d", "opengl:draw3d", "game:on_block_add_by_player",
              "game:on_block_remove_by_player"]

class State:
    def __init__(self):
        self.binding_ids = []

    def activate(self):
        for e in EVENTNAMES:
            self.binding_ids.append(G.eventhandler.on_event(e, self.on_event))

    def deactivate(self):
        for e in self.binding_ids:
            G.eventhandler.remove_on_event(e)
        self.binding_ids = []

    def on_event(self, name, *args):
        pass

    def getName(self):
        return "minecraft:none"

class Game(State):
    def __init__(self):
        State.__init__(self)
        # The label that is displayed in the top left of the canvas.
        self.label1 = pyglet.text.Label('', font_name='Arial', font_size=9,
                                       x=10, y=100, anchor_x='left', anchor_y='top',
                                       color=(0, 0, 0, 255))
        self.label2 = pyglet.text.Label('', font_name='Arial', font_size=9,
                                       x=10, y=75, anchor_x='left', anchor_y='top',
                                       color=(0, 0, 0, 255))
        self.reticle = None

    def getName(self):
        return "minecraft:game"

    def on_event(self, name, *args):
        if name == "opengl:draw3d":
            t = G.window.time + 12000 if G.window.time < 12000 else G.window.time
            w = (24000 - G.window.time) / 24000
            pyglet.gl.glClearColor(0.5*w, 0.69*w, 1.0*w, 1*w)
            pyglet.gl.glColor3d(w, w, w)
            G.model.batch.draw()
            self.draw_focused_block()
        elif name == "opengl:draw2d":
            self.draw_label()
            self.draw_reticle()
            G.inventoryhandler.draw()
        elif name == "core:window:on_resize":
            # label
            self.label1.y = G.window.height - 10
            self.label2.y = G.window.height - 25
            # reticle
            if self.reticle:
                self.reticle.delete()
            x, y = G.window.width // 2, G.window.height // 2
            n = 10
            self.reticle = pyglet.graphics.vertex_list(4,
                                                       ('v2i', (x - n, y, x + n, y, x, y - n, x, y + n))
                                                       )
        elif name == "core:window:on_key_release":
            symbol, modifiers = args

            if G.chat.active:
                G.window.strafe = [0, 0]
                return

            if symbol == config.Keyboard.WALK_FORWARD:
                G.window.strafe[0] += 1
            elif symbol == config.Keyboard.WALK_BACKWARD:
                G.window.strafe[0] -= 1
            elif symbol == config.Keyboard.WALK_LEFT:
                G.window.strafe[1] += 1
            elif symbol == config.Keyboard.WALK_RIGHT:
                G.window.strafe[1] -= 1
        elif name == "core:window:on_key_press":
            symbol, modifiers = args

            if G.chat.active:
                G.chat.on_key_press(symbol, modifiers)
                return

            if any([G.inventoryhandler.inventorys[inventory].isDisablyingGame() for inventory in G.inventoryhandler.activeinventorys]):
                print(symbol, key.ESCAPE)
                if symbol == key.ESCAPE:
                    for e in G.inventoryhandler.activeated:
                        inv = G.inventoryhandler.inventorys[e]
                        print(inv)
                        if "system:nothideable" not in inv.tag:
                            G.inventoryhandler.hide_inventory(e)
                return

            if symbol == config.Keyboard.WALK_FORWARD:
                G.window.strafe[0] -= 1
            elif symbol == config.Keyboard.WALK_BACKWARD:
                G.window.strafe[0] += 1
            elif symbol == config.Keyboard.WALK_LEFT:
                G.window.strafe[1] -= 1
            elif symbol == config.Keyboard.WALK_RIGHT:
                G.window.strafe[1] += 1
            elif symbol == config.Keyboard.JUMP:
                if G.window.dy == 0:
                    G.window.dy = config.Physiks.JUMP_SPEED
            elif symbol == config.Keyboard.CLOSE:
                if G.window.player.inventory.guitype == 1:
                    G.window.player.inventory.guitype = 0
                    G.window.set_exclusive_mouse(True)
                    G.inventoryhandler.hide_inventory(G.player.inventory.id)
                    G.inventoryhandler.show_inventory(G.player.inventory.id)
                elif G.chat.active:
                    G.inventoryhandler.hide_inventory(G.chat.id)
                    G.window.set_exclusive_mouse(True)
                    G.chat.active = False
                elif len(G.inventoryhandler.activeinventorys) > 3:
                    for e in G.inventoryhandler.activeinventorys:
                        e = G.inventoryhandler.inventorys[e]
                        if not "player:inventory" in e.tag:
                            G.inventoryhandler.hide_inventory(e.id)
                else:
                    G.statehandler.setState("minecraft:escape_menü")
            elif symbol == config.Keyboard.TOGGLE_FLYING:
                G.window.flying = not G.window.flying
            elif symbol in G.window.num_keys:
                index = (symbol - G.window.num_keys[0]) % 9
                G.player.selectedinventoryslot = index
            elif symbol == config.Keyboard.OPEN_INVENTORY:
                if G.window.player.inventory.guitype == 1:
                    G.window.player.inventory.guitype = 0
                    G.window.set_exclusive_mouse(True)
                    G.inventoryhandler.hide_inventory(G.window.player.inventory.id)
                    G.inventoryhandler.show_inventory(G.window.player.inventory.id)
                else:
                    G.window.player.inventory.guitype = 1
                    G.window.set_exclusive_mouse(False)
                    G.inventoryhandler.hide_inventory(G.window.player.inventory.id)
                    G.inventoryhandler.show_inventory(G.window.player.inventory.id)
            elif symbol == config.Keyboard.OPEN_CHAT:
                G.inventoryhandler.show_inventory(G.chat.id)
        elif name == "core:window:on_mouse_motion":
            x, y, dx, dy = args
            if G.player.inventory.inventorys[0].type == 1:
                G.player.on_mouse_motion(x, y, dx, dy)
                return
            if any([G.inventoryhandler.inventorys[inventory].isDisablyingGame() for inventory in G.inventoryhandler.activeinventorys]):
                G.player.on_mouse_motion(*args)
                return
            if G.window.exclusive:
                m = 0.15
                x, y = G.window.rotation
                x, y = x + dx * m, y + dy * m
                y = max(-90, min(90, y))
                G.window.rotation = (x, y)
        elif name == "core:window:on_mouse_press":
            x, y, button, modifiers = args
            if G.player.inventory.inventorys[0].type == 1:
                G.player.on_mouse_press(x, y, button, modifiers)
                return
            if any([G.inventoryhandler.inventorys[inventory].shouldInteractWithPlayerInventoryMoving() for inventory in G.inventoryhandler.activeinventorys]):
                G.player.on_mouse_press(*args)
                return
            if G.window.exclusive:
                vector = G.window.get_sight_vector()
                block, previous = G.window.model.hit_test(G.window.position, vector)
                if (button == mouse.RIGHT) or \
                        ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):
                    # ON OSX, control + left click = right click.
                    if previous and G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack and \
                            G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.item and \
                            G.player.inventory.inventorys[0].slots[
                                G.player.selectedinventoryslot].stack.item.hasBlock() and \
                            not G.model.world[block].isOpeningInventory(
                                G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.item):
                        G.model.add_block(previous, G.player.inventory.inventorys[0].slots[
                            G.player.selectedinventoryslot].stack.item.getBlockName(), blocksettedto=block)
                        G.eventhandler.call("game:on_block_add_by_player", vector, block, previous,
                                            G.player.inventory.inventorys[0].slots[
                                                G.player.selectedinventoryslot].stack.item.getBlockName())
                        G.model.world[previous].blocksettedto = block
                        G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.amount -= 1
                        block = G.model.world[previous]
                        G.soundhandler.playSound(previous, block.getBrakeSoundFile())
                    elif block and G.model.world[block].isOpeningInventory(
                            G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.item):
                        print(G.model.world[block], G.model.world[block].blockclass, G.model.world[block].getInventorys())
                        for e in G.model.world[block].getInventorys():
                            G.inventoryhandler.show_inventory(e if type(e) == int else e.id)
                            print(e if type(e) == int else e.id)
                elif button == pyglet.window.mouse.LEFT and block:
                    block = G.model.world[block]
                    if block.isBrakeAble():
                        G.soundhandler.playSound(block.position, block.getBrakeSoundFile())
                        drops = block.getDrop()
                        for e in drops.keys():
                            G.player.addToInventory(e, drops[e])
                        G.model.remove_block(block.position)
                        G.eventhandler.call("game:on_block_remove_by_player", vector, block, previous, drops)
            else:
                G.window.set_exclusive_mouse(True)

    def draw_focused_block(self):
        """ Draw black edges around the block that is currently under the
        crosshairs.

        """
        vector = G.window.get_sight_vector()
        block = G.window.model.hit_test(G.window.position, vector)[0]
        if block:
            x, y, z = block
            vertex_data = mathhelper.cube_vertices(x, y, z, 0.51)
            pyglet.gl.glColor3d(0, 0, 0)
            pyglet.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_LINE)
            pyglet.graphics.draw(24, pyglet.gl.GL_QUADS, ('v3f/static', vertex_data))
            pyglet.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_FILL)

    def draw_label(self):
        """ Draw the label in the top left of the screen.

        """
        x, y, z = G.window.position
        self.label1.text = '%02d (%.2f, %.2f, %.2f) %d / %d' % (
            pyglet.clock.get_fps(), x, y, z,
            len(G.model._shown), len(G.model.world))

        nx, ny, nz = mathhelper.normalize(G.window.position)
        if (nx, nz) in G.BiomeMAP: self.label1.text += "\nbiome: "+G.BiomeMAP[(nx, nz)].getName()
        self.label1.y = G.window.height - 10
        self.label1.draw()
        self.label2.y = G.window.height - 25
        self.label2.text = "daytime: "+str(round(G.window.time))+"; day: "+str(G.window.day)
        self.label2.draw()

    def draw_reticle(self):
        """ Draw the crosshairs in the center of the screen.

        """
        pyglet.gl.glColor3d(0, 0, 0)
        if self.reticle:
            self.reticle.draw(pyglet.gl.GL_LINES)
        else:
            self.on_event("core:window:on_resize")

    def activate(self):
        State.activate(self)
        if G.window: G.window.set_exclusive_mouse(True)

class EscapeMenü(State):
    def __init__(self):
        State.__init__(self)
        self.label = pyglet.text.Label(text=G.LANG.active.data["menu.game"])
        self.sprite1 = pyglet.sprite.Sprite(pyglet.image.load(G.local+"assets/textures/gui/gui_parts/BackToGame.png"))
        self.label1  = pyglet.text.Label(text=G.LANG.active.data["menu.returnToGame"])
        self.sprite2 = pyglet.sprite.Sprite(pyglet.image.load(G.local+"assets/textures/gui/gui_parts/Advancements.png"))
        self.label2  = pyglet.text.Label(text=G.LANG.active.data["gui.advancements"])
        self.sprite3 = pyglet.sprite.Sprite(pyglet.image.load(G.local+"assets/textures/gui/gui_parts/Statistics.png"))
        self.label3  = pyglet.text.Label(text=G.LANG.active.data["gui.stats"])
        self.sprite4 = pyglet.sprite.Sprite(pyglet.image.load(G.local+"assets/textures/gui/gui_parts/Options.png"))
        self.label4  = pyglet.text.Label(text=G.LANG.active.data["menu.options"])
        self.sprite5 = pyglet.sprite.Sprite(pyglet.image.load(G.local+"assets/textures/gui/gui_parts/OpenToLan.png"))
        self.label5  = pyglet.text.Label(text=G.LANG.active.data["menu.shareToLan"])
        self.sprite6 = pyglet.sprite.Sprite(pyglet.image.load(G.local+"assets/textures/gui/gui_parts/SaveAndQuit.png"))
        self.label6  = pyglet.text.Label(text=G.LANG.active.data["menu.returnToMenu"])

    def getName(self):
        return "minecraft:escape_menü"

    def on_event(self, name, *args):
        if name == "opengl:draw3d":
            pyglet.gl.glColor3d(0.8, 0.8, 0.8)
            G.model.batch.draw()
        elif name == "opengl:draw2d":
            self.label.draw()
            self.sprite1.draw()
            self.label1.draw()
            self.sprite2.draw()
            self.label2.draw()
            self.sprite3.draw()
            self.label3.draw()
            self.sprite4.draw()
            self.label4.draw()
            self.sprite5.draw()
            self.label5.draw()
            self.sprite6.draw()
            self.label6.draw()
            G.statehandler.states["minecraft:game"].draw_reticle()
        elif name == "core:window:on_resize":
            x, y = G.window.size
            self.label.x = x / 2 - 40
            self.label.y = y / 2 + 160
            self.sprite1.x = x / 2 - 200
            self.sprite1.y = y / 2 + 80
            self.label1.x  = x / 2 - 80
            self.label1.y  = y / 2 + 94
            self.sprite2.x = x / 2 - 200
            self.sprite2.y = y / 2 + 30
            self.label2.x  = x / 2 - 160
            self.label2.y  = y / 2 + 44
            self.sprite3.x = x / 2 + 4
            self.sprite3.y = y / 2 + 30
            self.label3.x  = x / 2 + 64
            self.label3.y  = y / 2 + 44
            self.sprite4.x = x / 2 - 200
            self.sprite4.y = y / 2 - 70
            self.label4.x  = x / 2 - 160
            self.label4.y  = y / 2 - 56
            self.sprite5.x = x / 2 + 4
            self.sprite5.y = y / 2 - 70
            self.label5.x  = x / 2 + 64
            self.label5.y  = y / 2 - 56
            self.sprite6.x = x / 2 - 200
            self.sprite6.y = y / 2 - 120
            self.label6.x  = x / 2 - 100
            self.label6.y  = y / 2 - 106
        elif name == "core:window:on_mouse_press":
            x, y, = args[:2]
            if x >= self.sprite1.x and x <= self.sprite1.x + 400 and y >= self.sprite1.y and y <= self.sprite1.y + 40:
                G.statehandler.setState("minecraft:game")
            elif x >= self.sprite2.x and x <= self.sprite2.x + 196 and y >= self.sprite2.y and y <= self.sprite2.y + 40:
                log.printMSG("[STATE][ERROR] can't handle event 'escapemenü:on_advancement_pressed': Advancements are NOT arival")
            elif x >= self.sprite3.x and x <= self.sprite3.x + 196 and y >= self.sprite3.y and y <= self.sprite3.y + 40:
                log.printMSG("[STATE][ERROR] can't handle event 'escapemenü:on_statistics_pressed': Statistics are NOT arival")
            elif x >= self.sprite4.x and x <= self.sprite4.x + 196 and y >= self.sprite4.y and y <= self.sprite4.y + 40:
                log.printMSG("[STATE][ERROR] can't handle event 'escapemenü:on_options_pressed': Options are NOT arival")
            elif x >= self.sprite5.x and x <= self.sprite5.x + 196 and y >= self.sprite5.y and y <= self.sprite5.y + 40:
                log.printMSG("[STATE][ERROR] can't handle event 'escapemenü:on_opentolan_pressed': Open to LAN is NOT arival")
            elif x >= self.sprite6.x and x <= self.sprite6.x + 400 and y >= self.sprite6.y and y <= self.sprite6.y + 40:
                G.window.close()
            elif args[2] == mouse.LEFT:
                G.statehandler.setState("minecraft:game")
        elif name == "core:window:on_key_press":
            if args[0] == key.ESCAPE:
                G.statehandler.setState("minecraft:game")

    def activate(self):
        State.activate(self)
        if G.window:
            G.window.set_exclusive_mouse(False)
            self.on_event("core:window:on_resize")

class ItemFileCreator(State):
    def __init__(self):
        State.__init__(self)
        self.blocks = list(G.blockhandler.blocks.values())
        self.lastblock = None
        self.nextposition = (0, 0, 0)

    def getName(self):
        return "minecraft:blockitemfilecreator"

    def on_event(self, name, *args):
        G.window.flying = True
        if name == "opengl:draw3d":
            pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1)
            G.model.batch.draw()

    def activate(self):
        State.activate(self)
        if G.window:
            G.window.set_exclusive_mouse(True)
            self.on_event("core:window:on_resize")
        G.tickhandler.tick(self.next)

    def next(self):
        print(self.nextposition, self.lastblock, self.blocks)
        x, y, z = self.nextposition
        self.nextposition = (x+10, y, z)
        G.window.set_size(150, 150)
        G.window.position = (x-1, x+1.8, x-1)
        G.window.rotation = (-228, -56)
        #if (x, y, z) in G.model.world and G.model.world[(x, y, z)].getName() != self.lastblock.getName():
            #G.tickhandler.tick(self.next, tick=5)
            #return
        if self.lastblock:
            itemclass = G.itemhandler.getByName(self.lastblock.getItemName(None))()
            pyglet.image.get_buffer_manager().get_color_buffer().save(itemclass.getTexturFile())
            imagealphacreator.convert(itemclass.getTexturFile())
        if len(self.blocks) > 0:
            block = self.blocks.pop(0)
            G.model.hide_block((x, y, z))
            G.model.remove_block((x, y, z))
            G.model.add_block((x, y, z), block.getName())
            G.model.show_block((x, y, z))
            G.model.hide_block((x, y, z))
            G.model.show_block((x, y, z))
            self.lastblock = block
            G.tickhandler.tick(self.next, tick=5)
            return
        G.window.position = (0, 255, 0)
        for e in list(G.model.world.keys()):
            G.model.remove_block(e)
        G.window.set_size(800, 600)
        G.statehandler.setState("minecraft:game")
        G.eventhandler.call("worldgen:newworld")
        G.GAMESTAGE = 3

def loadStates(*args):
    G.statehandler.register(Game)
    G.statehandler.register(EscapeMenü)
    G.statehandler.register(ItemFileCreator)

G.eventhandler.on_event("game:registry:on_state_registrate_periode", loadStates)