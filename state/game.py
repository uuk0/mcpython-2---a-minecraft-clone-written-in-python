import globals as G

import pyglet
from pyglet.window import key, mouse

import config

import mathhelper

import IItemStack

import config
import log


class Game(G.State):
    def __init__(self):
        G.State.__init__(self)
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
            G.player.dimension.worldprovider.batch.draw()
            self.draw_focused_block()
        elif name == "opengl:draw2d":
            self.draw_label()
            self.draw_reticle()
            G.inventoryhandler.draw()
            G.player.on_draw()
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

            if any([G.inventoryhandler.inventorys[inventory].isDisablyingGame() for inventory in \
                    G.inventoryhandler.activeinventorys]):
                #log.printMSG([G.inventoryhandler.inventorys[inventory] for inventory in G.inventoryhandler.activeinventorys])
                if symbol == key.ESCAPE:
                    for e in G.inventoryhandler.activeated:
                        inv = G.inventoryhandler.inventorys[e]
                        log.printMSG(inv)
                        if "system:nothideable" not in inv.tag:
                            G.inventoryhandler.hide_inventory(e)
                        else:
                            inv.on_try_close()
                else:
                    for e in G.inventoryhandler.activeated:
                        inv = G.inventoryhandler.inventorys[e]
                        inv.on_key_press(*args)
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
                    G.statehandler.setState("minecraft:escape_menu")
            elif symbol == config.Keyboard.TOGGLE_FLYING and G.player.gamemode == 1:
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
                    for e in G.player.inventory.inventorys[1:]:
                        return G.player.checkinventorysforslots.remove(e)
                else:
                    G.window.player.inventory.guitype = 1
                    G.window.set_exclusive_mouse(False)
                    G.inventoryhandler.hide_inventory(G.window.player.inventory.id)
                    G.inventoryhandler.show_inventory(G.window.player.inventory.id)
                    G.player.checkinventorysforslots += G.player.inventory.inventorys[1:]

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
                m = config.Physiks.MOUSE_REAKTION
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
                block, previous = G.model.hit_test(G.window.position, vector)
                if (button == mouse.RIGHT) or \
                        ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):
                    chunkprovider = chunkprovider2 = None
                    if previous:
                        cx, _, cz = mathhelper.sectorize(previous)
                        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    if block:
                        cx, _, cz = mathhelper.sectorize(block)
                        chunkprovider2 = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    # ON OSX, control + left click = right click.
                    if previous and G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack and \
                            G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.item and \
                            G.player.inventory.inventorys[0].slots[
                                G.player.selectedinventoryslot].stack.item.hasBlock() and \
                            not chunkprovider2.world[block].isOpeningInventory(
                                G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack):
                        G.model.add_block(previous, G.player.inventory.inventorys[0].slots[
                            G.player.selectedinventoryslot].stack.item.getBlockName(), blocksettedto=block)
                        G.model.check_neighbors(previous)
                        if not G.model.exposed(previous):
                            G.model.show_block(previous)
                        G.eventhandler.call("game:on_block_add_by_player", vector, block, previous,
                                            G.player.inventory.inventorys[0].slots[
                                                G.player.selectedinventoryslot].stack.item.getBlockName())
                        chunkprovider.world[previous].blocksettedto = block
                        if G.player.gamemode != 1:
                            G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.amount -= 1
                        block = chunkprovider.world[previous]
                        G.soundhandler.playSound(previous, block.getBrakeSoundFile())
                    elif block and chunkprovider.world[block].isOpeningInventory(
                            G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack):
                        #log.printMSG(chunkprovider.world[block], chunkprovider.world[block].blockclass, chunkprovider.world[block].getInventorys())
                        for e in chunkprovider.world[block].getInventorys():
                            G.inventoryhandler.show_inventory(e if type(e) == int else e.id)
                            #log.printMSG(e if type(e) == int else e.id)
                elif button == pyglet.window.mouse.LEFT and block:
                    cx, _, cz = mathhelper.sectorize(block)
                    chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    block = chunkprovider.world[block]
                    if block.isBrakeAble() or G.player.gamemode == 1:
                        G.soundhandler.playSound(block.position, block.getBrakeSoundFile())
                        if G.player.gamemode != 1:
                            drops = block.getDrop()
                            for e in drops.keys():
                                G.player.addToInventory(e, drops[e])
                        else:
                            drops = {}
                        G.model.remove_block(block.position)
                        G.model.hide_block(block.position, block)
                        #G.model.check_neighbors(block.position)
                        G.eventhandler.call("game:on_block_remove_by_player", vector, block, previous, drops)
                elif button == pyglet.window.mouse.MIDDLE and G.player.gamemode == 1:
                    vector = G.window.get_sight_vector()
                    block, previous = G.model.hit_test(G.window.position, vector)
                    cx, _, cz = mathhelper.sectorize(block)
                    chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack = \
                        IItemStack.IItemStack(chunkprovider.world[block].getItemName())
                    if G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.item:
                        G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.amount = \
                        G.player.inventory.inventorys[0].slots[G.player.selectedinventoryslot].stack.item.getMaxStackSize()
            else:
                G.window.set_exclusive_mouse(True)

    def draw_focused_block(self):
        """ Draw black edges around the block that is currently under the
        crosshairs.

        """
        if G.player.gamemode == 3: return
        vector = G.window.get_sight_vector()
        block = G.model.hit_test(G.window.position, vector)[0]
        if block:
            x, y, z = block
            vertex_data = mathhelper.cube_vertices(x, y, z, 0.50)
            pyglet.gl.glColor3d(0, 0, 0)
            pyglet.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_LINE)
            pyglet.graphics.draw(24, pyglet.gl.GL_QUADS, ('v3f/static', vertex_data))
            pyglet.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_FILL)

    def draw_label(self):
        """ Draw the label in the top left of the screen.

        """
        x, y, z = G.window.position
        self.label1.text = '%02d (%.2f, %.2f, %.2f) %d' % (
            pyglet.clock.get_fps(), x, y, z,
            len(G.player.dimension.worldprovider.chunkproviders))

        nx, ny, nz = mathhelper.normalize(G.window.position)
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
        G.State.activate(self)
        if G.window: G.window.set_exclusive_mouse(True)

G.statehandler.register(Game)