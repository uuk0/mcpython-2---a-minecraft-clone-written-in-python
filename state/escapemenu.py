import pyglet
from pyglet.window import key, mouse

import globals as G
import log


class EscapeMenu(G.State):
    def __init__(self):
        G.State.__init__(self)
        self.label = pyglet.text.Label(text=G.LANG.active.data["menu.game"])
        self.sprite1 = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/gui_parts/big.png"
            )
        )
        self.label1 = pyglet.text.Label(text=G.LANG.active.data["menu.returnToGame"])
        self.sprite2 = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/gui_parts/small.png"
            )
        )
        self.label2 = pyglet.text.Label(text=G.LANG.active.data["gui.advancements"])
        self.sprite3 = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/gui_parts/small.png"
            )
        )
        self.label3 = pyglet.text.Label(text=G.LANG.active.data["gui.stats"])
        self.sprite4 = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/gui_parts/small.png"
            )
        )
        self.label4 = pyglet.text.Label(text=G.LANG.active.data["menu.options"])
        self.sprite5 = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/gui_parts/small.png"
            )
        )
        self.label5 = pyglet.text.Label(text=G.LANG.active.data["menu.shareToLan"])
        self.sprite6 = pyglet.sprite.Sprite(
            pyglet.image.load(
                G.local + "/assets/minecraft/textures/gui/gui_parts/big.png"
            )
        )
        self.label6 = pyglet.text.Label(text=G.LANG.active.data["menu.returnToMenu"])

    def getName(self):
        return "minecraft:escape_menu"

    def on_event(self, name, *args):
        if name == "opengl:draw3d":
            pyglet.gl.glColor3d(0.8, 0.8, 0.8)
            G.player.dimension.worldprovider.batch.draw()
        elif name == "opengl:draw2d":
            G.statehandler.states["minecraft:game"].draw_label()
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
            self.label1.x = x / 2 - 80
            self.label1.y = y / 2 + 94
            self.sprite2.x = x / 2 - 200
            self.sprite2.y = y / 2 + 30
            self.label2.x = x / 2 - 160
            self.label2.y = y / 2 + 44
            self.sprite3.x = x / 2 + 4
            self.sprite3.y = y / 2 + 30
            self.label3.x = x / 2 + 64
            self.label3.y = y / 2 + 44
            self.sprite4.x = x / 2 - 200
            self.sprite4.y = y / 2 - 70
            self.label4.x = x / 2 - 160
            self.label4.y = y / 2 - 56
            self.sprite5.x = x / 2 + 4
            self.sprite5.y = y / 2 - 70
            self.label5.x = x / 2 + 64
            self.label5.y = y / 2 - 56
            self.sprite6.x = x / 2 - 200
            self.sprite6.y = y / 2 - 120
            self.label6.x = x / 2 - 100
            self.label6.y = y / 2 - 106
        elif name == "core:window:on_mouse_press":
            (
                x,
                y,
            ) = args[:2]
            if (
                x >= self.sprite1.x
                and x <= self.sprite1.x + 400
                and y >= self.sprite1.y
                and y <= self.sprite1.y + 40
            ):
                G.statehandler.setState("minecraft:game")
            elif (
                x >= self.sprite2.x
                and x <= self.sprite2.x + 196
                and y >= self.sprite2.y
                and y <= self.sprite2.y + 40
            ):
                log.printMSG(
                    "[STATE][ERROR] can't handle event 'escapemenü:on_advancement_pressed': Advancements are NOT arival"
                )
            elif (
                x >= self.sprite3.x
                and x <= self.sprite3.x + 196
                and y >= self.sprite3.y
                and y <= self.sprite3.y + 40
            ):
                log.printMSG(
                    "[STATE][ERROR] can't handle event 'escapemenü:on_statistics_pressed': Statistics are NOT arival"
                )
            elif (
                x >= self.sprite4.x
                and x <= self.sprite4.x + 196
                and y >= self.sprite4.y
                and y <= self.sprite4.y + 40
            ):
                log.printMSG(
                    "[STATE][ERROR] can't handle event 'escapemenü:on_options_pressed': Options are NOT arival"
                )
            elif (
                x >= self.sprite5.x
                and x <= self.sprite5.x + 196
                and y >= self.sprite5.y
                and y <= self.sprite5.y + 40
            ):
                log.printMSG(
                    "[STATE][ERROR] can't handle event 'escapemenü:on_opentolan_pressed': Open to LAN is NOT arival"
                )
            elif (
                x >= self.sprite6.x
                and x <= self.sprite6.x + 400
                and y >= self.sprite6.y
                and y <= self.sprite6.y + 40
            ):
                G.model.clear()
                G.statehandler.setState("minecraft:titlescreen")
            elif args[2] == mouse.LEFT:
                G.statehandler.setState("minecraft:game")
        elif name == "core:window:on_key_press":
            if args[0] == key.ESCAPE:
                G.statehandler.setState("minecraft:game")

    def activate(self):
        G.State.activate(self)
        if G.window:
            G.window.set_exclusive_mouse(False)
            self.on_event("core:window:on_resize")


G.statehandler.register(EscapeMenu)
