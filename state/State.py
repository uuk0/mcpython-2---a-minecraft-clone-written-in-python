import pyglet
from pyglet.window import key, mouse

import config
import globals as G
import imagealphacreator
import log
import mathhelper
import Block.block
import modsystem.ModLoader


class StateHandler:
    def __init__(self):
        self.states = {}
        self.active_state = None

    def register(self, state):
        if type(state) != State:
            state = state()
        self.states[state.getName()] = state
        G.eventhandler.call("game:registry:on_state_registrated", state)

    def setState(self, name):
        if not name in self.states:
            log.printMSG("[STATEHANDLER][ERROR] can't access state named " + str(name))
            return
        if self.active_state:
            self.active_state.deactivate()
        self.active_state = self.states[name]
        self.active_state.activate()


G.statehandler = StateHandler()


EVENTNAMES = [
    "core:window:on_exclusive_mouse_change",
    "core:update",
    "core:window:on_mouse_press",
    "core:window:on_mouse_release",
    "core:window:on_mouse_motion",
    "core:window:on_key_press",
    "core:window:on_key_release",
    "core:window:on_resize",
    "core:window:on_close",
    "core:window:on_mouse_scroll",
    "opengl:draw2d",
    "opengl:draw3d",
    "game:on_block_add_by_player",
    "game:on_block_remove_by_player",
]


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


G.State = State


@modsystem.ModLoader.ModEventEntry(
    "game:registry:on_state_registrate_periode", "minecraft", info="registrating states"
)
def register():
    import state.game, state.escapemenu, state.titlescreen
