import importlib
import os
import sys
import time
import zipfile

import config
import globals as G
import log

import modsystem.ModSorter as ModSorter

import argumentparser


EVENTLIST = {}  # modname -> ModEventEntry
EVENTENTRYLIST = {}  # eventname -> entry

def _null_function(*args, **kwargs): pass


class ModEventEntry:
    """
    binding for mods to events. use @ModEventEntry(<eventname>, <modname>)\ndef <your_function_name>(name, <...>):
    """
    def __init__(self, name, modname, info=None, add=[]):
        self.__name = name
        self.modname = modname
        self.info = info
        self.add = add

    def __call__(self, *args, **kwargs):
        if not self.modname in EVENTLIST: EVENTLIST[self.modname] = {}
        if not self.__name in EVENTLIST[self.modname]: EVENTLIST[self.modname][self.__name] = []
        EVENTLIST[self.modname][self.__name].append([self, args[0]])
        entry = EVENTENTRYLIST[self.__name]
        if entry.on_event_binding: entry.on_event_binding(self.__name, self.modname, args[0])
        return args[0]


class ModEventCallEntry:
    """
    entry for modloader for loading stages of mods
    """
    def __init__(self, name, start_function=_null_function, end_function=_null_function,
                 on_event_binding=_null_function, on_event_call=_null_function):
        self.name = name
        self.start_function = start_function  # will be called before every other binding to these entry
        self.end_function = end_function
        self.on_event_binding = on_event_binding
        self.on_event_call = on_event_call
        EVENTENTRYLIST[name] = self
        G.modloader.registerRegistrationEvent(self)

    def __call__(self, *args, **kwargs):
        """
        binds an given function to these modeventcallentry
        """
        name = args[0].__name__
        if name  == "on_start":
            self.start_function = args[0]
        elif name == "on_end":
            self.end_function = args[0]
        elif name == "on_event_add":
            self.on_event_binding = args[0]
        elif name == "on_event_call":
            self.on_event_call = args[0]
        else:
            raise ValueError("can't bind function named "+str(name))
        return args[0]


class ModLoader:
    """main class for modloading"""
    def __init__(self):
        self.mods = {}
        d = [G.local+"/mods"]
        for e in sys.argv[1:]:
            if os.path.isdir(e):
                sys.argv.remove(e)
                d.append(e)
        self.externaldirs = d
        for e in self.externaldirs:
            if not os.path.dirname(e) in sys.path:
                sys.path.append(os.path.dirname(e))
        self.mdirs = []
        self.events = []

    def registerRegistrationEvent(self, entry):
        self.events = self.events[:-2] + [entry] + self.events[-2:]

    def register(self, mod):
        """registrates a new mod to registry"""
        if not type(mod) == Mod: mod = mod()
        if any([x+"/"+mod.getFileName() in self.mdirs for x in self.externaldirs]):
            for e in self.externaldirs:
                if e+"/"+mod.getFileName() in self.mdirs:
                    mod.path = e+"/"+mod.getFileName()
        self.mods[mod.getName()] = mod

    def getModDirs(self):
        """search for mods in 'mods'-folder"""
        mods = []
        ed = []
        for e in self.externaldirs:
            if os.path.isdir(e):
                ed += [e + "/" + x for x in os.listdir(e)]
        self.mdirs = ed
        for e in os.listdir(G.local + "/mods") + ed:
            if zipfile.is_zipfile(e) and config.DEBUG.PRINT_MODLOADING_FORMAT_STUFF:
                log.printMSG("[MODLOADER][ERROR] can't load mods from zipfile")
            elif os.path.isdir(e) and e != "__pycache__":
                mods.append([1, e, e.split("/")[-1]])
            elif os.path.isfile(e) and e.endswith(".py"):
                mods.append([2, e, e.split("/")[-1]])
        return mods

    def loadMods(self, mods):
        import modsystem.main
        G.MODS.append(modsystem.main)
        for e in mods:
            # log.printMSG("[MODLOADER][INFO] found mod in " + str(e[1]))
            if e[0] == 2:
                G.MODS.append(importlib.import_module("mods." + e[2].split(".")[0]))
            elif e[0] == 1:
                try:
                    G.MODS.append(importlib.import_module("mods." + e[2].split(".")[0] + ".main"))
                except ModuleNotFoundError:
                    # log.printMSG("[MODLOADER][INFO] can't load mod from dir " + e[2])
                    pass
            else:
                raise RuntimeError()

    def checkDependecies(self):
        flag = True
        for mod in self.mods.keys():
            mod = self.mods[mod]
            versions = mod.getMcPythonVersions()
            if versions != None:
                if type(versions) == str:
                    if versions != G.VERSION_NAME and not "--deactivateversionicompatibles" in sys.argv:
                        log.printMSG("[MODLOADER][ERROR] mod " + str(mod) + " is requiring mc version " + str(versions))
                        flag = False
                else:
                    if not any([x == G.VERSION_NAME for x in
                                versions]) and not "--deactivateversionicompatibles" in sys.argv:
                        log.printMSG(
                            "[MODLOADER][ERROR] mod " + str(mod) + " is requiring one of mc versions " + str(versions))
                        flag = False
            for e in mod.getDependencies():
                if not e[0] in self.mods:
                    log.printMSG("[MODLOADER][ERROR] dependencie error: mod " + str(mod) + " needs mod " + str(e[0]))
                    flag = False
                elif len(e) > 1:
                    if callable(e[1]):
                        f = e[1]()
                        if not f:
                            flag = False
                    else:
                        modd = self.mods[e[0]]
                        depend_min = e[1][0] if len(e) > 1 else (-1, -1, -1)
                        depend_max = e[1][1] if len(e) > 1 and len(e[1]) > 1 else modd.getVersion()
                        depend_func = e[2] if len(e) > 2 else None
                        version_modd = modd.getVersion()
                        if not (depend_min[0] <= version_modd[0] <= depend_max[0] and depend_min[1] <= version_modd[
                            1] <= \
                                depend_max[1] and depend_min[2] <= version_modd[2] <= depend_max[2]) and \
                                ((depend_func and depend_func()) or not depend_func):
                            log.printMSG("[MODLOADER][ERROR] depenencie error: mod " + str(mod) + " needs mod " + str(
                                e[0]) + " in version range " + str([depend_min, depend_max]) + ", but " + str(
                                version_modd) + " is loaded")
                            flag = False
                        if len(e) > 2:
                            f = e[2]()
                            if not f: flag = False
        if not flag:
            log.printMSG(
                "[MODLOADER][ERROR] there were errors in mod initialisation phase. NOT beginning loading phase")
            sys.exit(-1)

    def searchForMods(self):
        #print(EVENTLIST, EVENTENTRYLIST)
        mods = self.getModDirs()
        self.loadMods(mods)
        self.checkDependecies()
        sorter = ModSorter.ModSorter(self.mods)
        sorter.sort()
        log.printMSG("[MODLOADER] we will load mods in the following order:")
        for mod in sorter.modlistsorted:
            log.printMSG("  :"+str(mod.getName()))
        self.bind_events(sorter)
        self.call_events(sorter)

    def bind_events(self, sorter):
        """
        for mod in sorter.modlistsorted:
            if mod.getName() in EVENTLIST:
                for buffer in EVENTLIST[mod.getName()]:
                    G.eventhandler.on_event(*buffer)"""
        for mod in self.mods.values():
            mod.register_event_bindings()

    def call_events(self, sorter):
        G.GAMESTAGE = 1

        for i, entry in enumerate(self.events):
            entry.start_function(entry)
            log.printMSG("[MODLOADER][INFO] loading "+str(entry.name))
            for mod in self.mods.values():
                name = mod.getName()
                dt = time.time()
                if name in EVENTLIST and entry.name in EVENTLIST[name]:
                    for info in EVENTLIST[name][entry.name]:
                        #print("\x1b[2K\r", end="")
                        log.printMSG("[MODLOADER]["+entry.name+"][INFO] mod "+str(info[0].modname)+" is "+\
                                     str(info[0].info))
                        info[1](*info[0].add)
                        entry.on_event_call(entry, info, name)
            entry.end_function(entry)

    def __call__(self, clas, *args, **kwargs):
        self.register(clas)
        return clas


G.modloader = ModLoader()

ModEventCallEntry("game:registry:on_prepare_plugin_registrate_periode")
ModEventCallEntry("game:registry:on_argument_parser_type_registrate_periode")


@ModEventCallEntry("game:registry:on_texture_registrate_periode")
def on_end(entry):
    G.imageatlashandler.init()


ModEventCallEntry("game:registry:on_sound_registrate_periode")
ModEventCallEntry("game:registry:on_block_registrate_periode")


@ModEventCallEntry("game:registry:on_item_registrate_preiode")
def on_end(entry):
    """
    we know that this is stuff around blocks, but we need it to make shour we have all items registrated
    """
    import texturslitcher
    texturslitcher.ImageAtlas.save_image(
        texturslitcher.ImageAtlas.resize(
            texturslitcher.ImageAtlas.load_image(G.local + "/assets/minecraft/textures/missingtexture.png"),
            (32, 32)
        ),
        G.local + "/assets/minecraft/textures/missingtexture.png"
    )
    for b in G.blockhandler.blocks:
        if not G.blockhandler.blocks[b].getName() in G.itemhandler.itemclasses:
            if G.blockhandler.blocks[b].getItemFile(None):
                file = G.blockhandler.blocks[b].getItemFile(None)
                block = b

                class MissingItem(G.itemclass):
                    def getName(self): return block

                    def getTexturFile(self): return file
                G.itemhandler.register(MissingItem)
            else:
                log.printMSG("[CHECK][ERROR] block " + str(b) + " has no ITEM!!!")
                register_l_block(G.blockhandler.blocks[b].getName())


def register_l_block(blockname):
    class MissingItem(G.itemclass):
        def getName(self): return blockname

    G.itemhandler.register(MissingItem)


ModEventCallEntry("game:registry:on_biome_registrate_periode")
ModEventCallEntry("game:registry:on_inventory:registrate_periode")
ModEventCallEntry("game:registry:on_crafting_recipi_registrate_periode")
ModEventCallEntry("game:registry:on_structur_registrate_periode")
ModEventCallEntry("game:registry:on_multiblockstructur_registrate_periode")
ModEventCallEntry("game:registry:on_entity_registrate_periode")
ModEventCallEntry("game:registry:on_state_registrate_periode")
ModEventCallEntry("game:registry:on_command_registrate_periode")
ModEventCallEntry("game:registry:on_plugin_apply")
ModEventCallEntry("game:startup")


class Mod:
    """base class for Mod"""
    def __init__(self):
        G.eventhandler.call("game:registry:on_mod_registrated", self)
        self.path = None

    def register_event_bindings(self):
        """
        here you should import all your submoduls with the eventbindings
        """
        pass

    def getName(self):
        """returns the name of the mod"""
        return "mod:none"

    def getVersion(self):
        """returns the version of the mod as tupel of three ints"""
        return (0, 0, 0)

    def getDependencies(self):
        """returns all dependencies (a list of [modname, [{MINVERSION}, {MAXVERSION}],
        [function to detect if it is correct]])"""
        return []

    def getMcPythonVersions(self):
        """returns the version snapshot for which is it written (may be list. ends with None if upper is supported.
         may be None if all)
           use N[VERSION_NAME] for deacte an given version"""
        return None

    def getUserFriendlyName(self):
        """function which returns the user-freindly name of the mod."""
        return self.getName()

    def getFileName(self):
        """returns the file name of the folder of the mod. is used to do mod.path"""
        return ""


G.mod = Mod

