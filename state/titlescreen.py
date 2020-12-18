import globals as G
import pyglet
import log
import random
import mathhelper


class TitleScreen(G.State):
    def __init__(self):
        G.State.__init__(self)
        self.image1 = pyglet.sprite.Sprite(
            pyglet.image.load(G.local + "/assets/minecraft/textures/startmenupic1.png")
        )
        self.lable1 = pyglet.text.Label(color=(255, 255, 255, 255), text=G.VERSION_NAME)
        self.lable2 = pyglet.text.Label(
            color=(255, 255, 255, 255), text=G.LANG.active.data["menu.singleplayer"]
        )
        self.lable3 = pyglet.text.Label(
            color=(255, 255, 255, 255), text=G.LANG.active.data["menu.multiplayer"]
        )
        self.lable4 = pyglet.text.Label(
            color=(255, 255, 255, 255), text=G.LANG.active.data["menu.quit"]
        )

    def on_event(self, name, *args):
        if name == "opengl:draw2d":
            # G.window.set_size(1200, 620)
            G.window.set_exclusive_mouse(False)
            self.image1.draw()
            self.lable1.x = 90
            self.lable1.y = 3
            self.lable1.draw()
            self.lable2.x = 555
            self.lable2.y = 358
            self.lable2.draw()
            self.lable3.x = 550
            self.lable3.y = 318
            self.lable3.draw()
            self.lable4.x = 610
            self.lable4.y = 210
            self.lable4.draw()
        elif name == "core:window:on_mouse_press":
            x, y, button, mod = args
            if x >= 424 and y >= 348 and x <= 777 and y <= 381:
                G.window.flying = True
                G.window.position = (0, 4000, 0)
                G.dimensionhandler.generateclasses()
                G.player.dimension = G.dimensionhandler.dimensions[0]
                G.eventhandler.call("worldgen:newworld")
                G.window.time = 0
                G.window.day = 0
                chunk = (0, 0)
                x, y = random.randint(0, 15), random.randint(0, 15)
                x += chunk[0] * 16
                y += chunk[1] * 16
                G.window.position = (0, 255, 0)
                G.player.gamemode = 1
                G.window.flying = True
                G.SPAWNPOINT = G.window.position
                G.window.rotation = (0, 0)
                G.window.flying = False
                G.statehandler.setState("minecraft:game")
            elif x >= 550 and y >= 318 and x <= 777 and y <= 338:
                log.printMSG("[TITLESCREEN][ERROR] multiplayer is NOT arrival")
            elif x >= 605 and y >= 200 and x <= 777 and y <= 234:
                G.window.close()
            else:
                log.printMSG(args)

    def getName(self):
        return "minecraft:titlescreen"

    def activate(self):
        G.State.activate(self)
        if G.window:
            G.window.set_size(1200, 620)

    def deactivate(self):
        G.State.deactivate(self)


G.statehandler.register(TitleScreen)
