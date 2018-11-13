import importlib
import os
import sys
import time
import zipfile

import config
import globals as G
import log

sys.path.append(G.local+"mods")

"""main class for modloading"""
class ModLoader:
    def __init__(self):
        self.mods = {}

    """registrates a new mod to registry"""
    def register(self, mod):
        if not type(mod) == Mod: mod = mod()
        self.mods[mod.getName()] = mod
        for e in ["game:registry:on_biome_registrate_periode", "game:registry:on_block_registrate_periode",
                  "game:registry:on_entity_registrate_periode", "game:registry:on_inventory:registrate_periode",
                  "game:registry:on_item_registrate_preiode", "game:registry:on_crafting_recipi_registrate_periode",
                  "game:registry:on_texture_registrate_periode", "game:registry:on_multiblockstructur_registrate_periode",
                  "game:registry:on_sound_registrate_periode", "game:registry:on_state_registrate_periode",
                  "game:registry:on_command_registrate_periode", "game:registry:on_plugin_apply",
                  "game:registry:on_structur_registrate_periode"]:
            G.eventhandler.on_event(e, mod.on_event)

    """search for mods in 'mods'-folder"""
    def searchForMods(self):
        mods = []
        for e in os.listdir(G.local+"mods"):
            if zipfile.is_zipfile(G.local+"mods/"+e) and config.DEBUG.PRINT_MODLOADING_FORMAT_STUFF:
                log.printMSG("[MODLOADER][ERROR] can't load mods from zipfile")
            elif os.path.isdir(G.local+"mods/"+e) and e != "__pycache__":
                mods.append([1, G.local+"mods/"+e, e])
            elif os.path.isfile(G.local+"mods/"+e) and e.endswith(".py"):
                mods.append([2, G.local+"mods/"+e, e])
        for e in mods:
            log.printMSG("[MODLOADER][INFO] found mod in "+str(e[1]))
            if e[0] == 2:
                G.MODS.append(importlib.import_module(e[2].split(".")[0]))
            elif e[0] == 1:
                G.MODS.append(importlib.import_module(e[2].split(".")[0]+".main"))
        flag = True
        for mod in self.mods.keys():
            mod = self.mods[mod]
            for e in mod.getDependencies():
                if not e[0] in self.mods:
                    log.printMSG("[MODLOADER][ERROR] dependencie error: mod "+str(mod)+" needs mod "+str(e[0]))
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
                        if not (depend_min[0] <= version_modd[0] <= depend_max[0] and depend_min[1] <= version_modd[1] <= \
                                depend_max[1] and depend_min[2] <= version_modd[2] <= depend_max[2]) and \
                                ((depend_func and depend_func()) or not depend_func):
                            log.printMSG("[MODLOADER][ERROR] depenencie error: mod "+str(mod)+" needs mod "+str(e[0])+" in version range "+str([depend_min, depend_max])+", but "+str(version_modd)+" is loaded")
                            flag = False
                        if len(e) > 2:
                            f = e[2]()
                            if not f:
                                flag = False
        if not flag:
            log.printMSG("[MODLOADER][ERROR] there were errors in mod initialisation phase. NOT beginning loading phase")
            sys.exit(-1)

        G.GAMESTAGE = 1

        log.printMSG("[MODLOADER][INFO] applying registry plugins...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_prepare_plugin_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading sounds...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_sound_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in "+str(time.time()-dt)+" secound")
        log.printMSG("[MODLOADER][INFO] loading texturs...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_texture_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading blocks...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_block_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading items...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_item_registrate_preiode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading inventorys...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_inventory:registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading entitys...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_entity_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading recipis...")
        dt = time.time()
        G.eventhandler.call("game:registry:on_crafting_recipi_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading multiblockstructurs")
        dt = time.time()
        G.eventhandler.call("game:registry:on_multiblockstructur_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading structurs")
        dt = time.time()
        G.eventhandler.call("game:registry:on_structur_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        log.printMSG("[MODLOADER][INFO] loading biomes")
        dt = time.time()
        G.eventhandler.call("game:registry:on_biome_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")

        log.printMSG("[MODLOADER][INFO] loading commands")
        dt = time.time()
        G.eventhandler.call("game:registry:on_command_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")

        log.printMSG("[MODLOADER][INFO] loading states")
        dt = time.time()
        G.eventhandler.call("game:registry:on_state_registrate_periode")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")

        log.printMSG("[MODLOADER][INFO] applying plugins")
        dt = time.time()
        G.eventhandler.call("game:registry:on_plugin_apply")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")

        log.printMSG("[MODLOADER][INFO] loading mod-startup...")
        dt = time.time()
        G.eventhandler.call("game:startup")
        log.printMSG("[MODLOADER][INFO] finished in " + str(time.time() - dt) + " secound")
        G.GAMESTAGE = 2

G.modloader = ModLoader()

"""base class for Mod"""
class Mod:
    def __init__(self):
        G.eventhandler.call("game:registry:on_mod_registrated", self)

    """returns the name of the mod"""
    def getName(self):
        return "mod:none"

    """callen when an event named 'game:registry:on_[...]' is callen"""
    def on_event(self, name, *args, **kwargs):
        pass

    """returns the version of the mod as tupel of three ints"""
    def getVersion(self):
        return (0, 0, 0)

    """returns all dependencies (a list of [modname, [{MINVERSION}, {MAXVERSION}], [function to detect if it is correct]])"""
    def getDependencies(self):
        return []

G.mod = Mod