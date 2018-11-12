import globals as G
import log

"""class for eventhandler"""
class EventHandler:
    def __init__(self):
        self.eventnames = {}
        self.functions = {}
        self.nextid = 0

        self.blockupdatebinds = {} #position -> function list

    """adds an new eventname"""
    def addEventName(self, name):
        if name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to add event named "+str(name)+", but it is known")
            return
        self.eventnames[name] = []

    """clear all functions to an event"""
    def clearEvent(self, name):
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to clear an unknown event: "+str(name))
            return
        for e in self.eventnames[name]:
            del self.functions[e]
        self.eventnames[name] = []

    """remove an event"""
    def removeEvent(self, name):
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to remove an unknown event: "+str(name))
            return
        self.clearEvent()
        del self.eventnames[name]

    """binds an function to an event"""
    def on_event(self, name, func, bargs=[]):
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to add an function ("+str(function)+") to an unknown event named "+str(name))
            return
        id = self.nextid
        self.nextid += 1
        self.eventnames[name].append(id)
        self.functions[id] = [func, name, bargs]
        return id

    """"unbinds an function to an event"""
    def remove_on_event(self, id):
        if not id in self.functions:
            log.printMSG(
                "[EVENTHANDLER][ERROR] try to remove an unknown function "+str(id))
            return
        self.eventnames[self.functions[id][1]].remove(id)
        del self.functions[id]

    """call an event"""
    def call(self, name, *args, **kwargs):
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to call an unknown event named "+str(name))
            return
        for e in self.eventnames[name]:
            self.functions[e][0](name, *list(self.functions[e][2])+list(args), **kwargs)

    """binds an function to a blockupdate"""
    def on_block_update(self, position, function):
        if not position in self.blockupdatebinds: self.blockupdatebinds[position] = []
        self.blockupdatebinds[position].append(function)

    """call an blockupdate"""
    def _blockupdate(self, position):
        if not position in self.blockupdatebinds: return
        for e in self.blockupdatebinds[position]:
            e(position)

    """call an blockupdate for deletion"""
    def _blockremoveupdate(self, position):
        if not position in self.blockupdatebinds: return
        for e in self.blockupdatebinds[position]:
            e(position, delet=True)

    """unbinds an function to a blockupdate"""
    def remove_on_block_update(self, position, function):
        self.blockupdatebinds[position].remove(function)
        if len(self.blockupdatebinds[position]) == 0:
            del self.blockupdatebinds[position]


G.eventhandler = EventHandler()
G.eventhandler.addEventName("core:tick")
G.eventhandler.addEventName("core:window:on_exclusive_mouse_change")
G.eventhandler.addEventName("core:update")
G.eventhandler.addEventName("core:window:on_mouse_press")
G.eventhandler.addEventName("core:window:on_mouse_release")
G.eventhandler.addEventName("core:window:on_mouse_motion")
G.eventhandler.addEventName("core:window:on_key_press")
G.eventhandler.addEventName("core:window:on_key_release")
G.eventhandler.addEventName("core:window:on_resize")
G.eventhandler.addEventName("core:window:on_close")
G.eventhandler.addEventName("core:window:on_mouse_scroll")
G.eventhandler.addEventName("opengl:draw2d")
G.eventhandler.addEventName("opengl:draw3d")
G.eventhandler.addEventName("game:on_block_add_by_player")
G.eventhandler.addEventName("game:on_block_remove_by_player")

G.eventhandler.addEventName("game:registry:on_prepare_plugin_registrate_periode")
G.eventhandler.addEventName("game:registry:on_biome_registrate_periode")
G.eventhandler.addEventName("game:registry:on_block_registrate_periode")
G.eventhandler.addEventName("game:registry:on_entity_registrate_periode")
G.eventhandler.addEventName("game:registry:on_inventory:registrate_periode")
G.eventhandler.addEventName("game:registry:on_item_registrate_preiode")
G.eventhandler.addEventName("game:registry:on_crafting_recipi_registrate_periode")
G.eventhandler.addEventName("game:registry:on_texture_registrate_periode")
G.eventhandler.addEventName("game:registry:on_multiblockstructur_registrate_periode")
G.eventhandler.addEventName("game:registry:on_sound_registrate_periode")
G.eventhandler.addEventName("game:registry:on_structur_registrate_periode")
G.eventhandler.addEventName("game:registry:on_plugin_apply")
G.eventhandler.addEventName("game:registry:on_command_registrate_periode")
G.eventhandler.addEventName("game:registry:on_state_registrate_periode")
G.eventhandler.addEventName("game:startup")
G.eventhandler.addEventName("worldgen:newworld")

G.eventhandler.addEventName("game:registry:on_language_registered")
G.eventhandler.addEventName("game:registry:on_mod_registrated")
G.eventhandler.addEventName("game:registry:on_multiblockstructurs_registrated")
G.eventhandler.addEventName("game:registry:on_sound_registrated")
G.eventhandler.addEventName("game:registry:on_state_registrated")
G.eventhandler.addEventName("game:registry:on_structur_registrated")
G.eventhandler.addEventName("game:registry:on_biome_registrated")
G.eventhandler.addEventName("game:registry:on_block_registrated")
G.eventhandler.addEventName("game:registry:on_command_registrated")
G.eventhandler.addEventName("game:registry:on_entity_registrated")
G.eventhandler.addEventName("game:registry:on_item_registrated")

#G.eventhandler.addEventName("game:command:on_reload")