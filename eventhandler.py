import globals as G
import log
import exceptionhandler
import traceback


class EventHandler:
    """class for eventhandler"""
    def __init__(self):
        self.eventnames = {}
        self.functions = {}
        self.nextid = 0
        self.blockupdatebinds = {} #position -> function list


    def addEventName(self, name, msg=True):
        """
        adds an new eventname
        :param name: the name of the event
        """
        if name in self.eventnames:
            if msg: log.printMSG("[EVENTHANDLER][ERROR] try to add event named "+str(name)+", but it is known")
            return
        self.eventnames[name] = []

    def clearEvent(self, name):
        """
        clear all functions to an event
        :param name: the name of the event to clear
        """
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to clear an unknown event: "+str(name))
            return
        for e in self.eventnames[name]:
            del self.functions[e]
        self.eventnames[name] = []

    def removeEvent(self, name):
        """
        remove an event
        :param name: the name of the event to remove
        """
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to remove an unknown event: "+str(name))
            return
        self.clearEvent(name)
        del self.eventnames[name]

    def on_event(self, name, func, bargs=[]):
        """
        binds an function to an event
        :param name: the name of the event to bind to
        :param func: the function to bind
        :param bargs: arguments which should be added when calling these function
        :return: the id of the eventbinding
        """
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to add an function ("+str(func)+") to an unknown event named "+str(name))
            raise RuntimeError()
            return
        id = self.nextid
        self.nextid += 1
        self.eventnames[name].append(id)
        self.functions[id] = [func, name, bargs]
        return id

    def remove_on_event(self, id):
        """
        unbinds an function to an event
        :param id: the id of the binding
        """
        if not id in self.functions:
            log.printMSG(
                "[EVENTHANDLER][ERROR] try to remove an unknown function "+str(id))
            return
        self.eventnames[self.functions[id][1]].remove(id)
        del self.functions[id]

    def call(self, name, *args, **kwargs):
        """
        call an event
        :param name: the name of the event
        :param args: extra arguments
        :param kwargs: extra positional arguments
        """
        if not name in self.eventnames:
            log.printMSG("[EVENTHANDLER][ERROR] try to call an unknown event named "+str(name))
            return
        for e in self.eventnames[name]:
            try:
                self.functions[e][0](name, *list(self.functions[e][2])+list(args), **kwargs)
            except:
                exceptionhandler.add_traceback()
                traceback.print_exc()

    def on_block_update(self, position, function):
        """
        binds an function to a blockupdate
        :param position: position of the block
        :param function: the function to bind
        """
        if not position in self.blockupdatebinds: self.blockupdatebinds[position] = []
        self.blockupdatebinds[position].append(function)

    def _blockupdate(self, position):
        """
        call an blockupdate
        :param position: the position of the block
        """
        if not position in self.blockupdatebinds: return
        for e in self.blockupdatebinds[position]:
            e(position)

    def _blockremoveupdate(self, position):
        """
        call an blockupdate for deletion
        :param position: the position of the block
        """
        if not position in self.blockupdatebinds: return
        for e in self.blockupdatebinds[position]:
            e(position, delet=True)

    def remove_on_block_update(self, position, function):
        """
        unbinds an function to a blockupdate
        :param position: the position of the block
        :param function: the function to unbind
        """
        self.blockupdatebinds[position].remove(function)
        if len(self.blockupdatebinds[position]) == 0:
            del self.blockupdatebinds[position]


G.eventhandler = EventHandler()

# I/O EVENTS
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
G.eventhandler.addEventName("core:model:cleanup")

#REGISTRATE PERIODES EVENTS
"""
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
G.eventhandler.addEventName("game:registry:on_argument_parser_type_registrate_periode")
G.eventhandler.addEventName("game:registry:on_registryperiode_registrate_periode")
G.eventhandler.addEventName("game:startup")"""

#RUNTIME EVENTS FROM MCPYTHON
G.eventhandler.addEventName("worldgen:newworld")

#REGISTRATE EVENTS
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