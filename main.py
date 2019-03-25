import sys
import os
import log
import globals as G
import shutil

log.printMSG("--------------------------------------------------------------------------------")
log.printMSG("- MCPYTHON VERSION "+G.VERSION_NAME.upper()+" "*(60-len(G.VERSION_NAME))+"-")
log.printMSG("--------------------------------------------------------------------------------\n\n")

import exceptionhandler
exceptionhandler.add_header()

if sys.version_info[0] == 2:
    log.printMSG("[MAINTHREAD][ERROR] unsupported python version: ", sys.version_info)
    sys.exit(-1)

log.printMSG("[MAINTHREAD][INFO] clearing tmp-dir")

if not os.path.exists(G.local+"/tmp"): os.makedirs(G.local+"/tmp")
for e in os.listdir(G.local+"/tmp"):
    if e not in ["file.info"]:
        if os.path.isfile(G.local+"/tmp/"+e):
            os.remove(G.local+"/tmp/"+e)
        else:
            try:
                shutil.rmtree(G.local+"/tmp/"+e)
            except PermissionError: pass

log.printMSG("[MAINTHREAD][INFO] finished! Now looking after the packages we need")
os.makedirs(G.local+"/tmp/gui")
os.makedirs(G.local+"/tmp/entity")

try:
    import pyglet
except ImportError:
    log.printMSG("can't load pyglet. PLEASE INSTALL IT. IT IS USED FOR RENDERING EVERYTHING")

try:
    import PIL
    from PIL import ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
except ImportError:
    log.printMSG("can't load pillow. PLEASE INSTALL IT. IT IS USED FOR IMAGE HANDLING")

try:
    import numpy
except ImportError:
    log.printMSG("can't load numpy. PLEASE INSTALL IT. IT IS USED FOR 3D THINGS")

try:
    import noise
except ImportError:
    log.printMSG("can't load noise. IT IS USED FOR WORLD GEN")

try:
    import json
except ImportError:
    log.printMSG("can't load json. This is a strange thing because your python setup should have it installed"+\
                 " by installing it")

log.printMSG("[MAINTHREAD][INFO] everything fine (or not?). Starting loading submoduls step by step")

import gen.biomes.Biome
import eventhandler
import crafting
import language
import ticksystem
import scoreboard.ScoreboardHandler
import command.Command
import soundhandler
import state.State
import Block.block, Item.item, entity.entity, Inventory.inventory
import textures.modelloader
import textures.TextureAtlas
import gen.biomes.Biome
import state
import state.State
import storage.storagehandler
import crafting.CraftingHandler, crafting.CraftingTableGrid, crafting.FurnesGrid
import texturegenerator

log.printMSG("[MAINTHREAD][INFO] we are ready to start, only a few things to do")

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

import globals as G

import glfunctions

import soundhandler

from pyglet.gl import *

def main():
    """main function"""
    log.printMSG("[MAINTHREAD][INFO] creating window")
    import Inventory.inventory
    import window
    #window = window.Window(width=800, height=600, caption='mcp#ython 2', resizable=True)
    try:
        # Try and create a window with multisampling (antialiasing)
        config = Config(sample_buffers=1, samples=4,
                        depth_size=16, double_buffer=True, )
        window = window.Window(resizable=True, config=config, width=1200, height=620, caption='mcpython '+str(G.VERSION_NAME))
    except pyglet.window.NoSuchConfigException:
        # Fall back to no multisampling for old hardware
        window = pyglet.window.Window(resizable=True, width=1200, height=620, caption='mcpython 2')
    # Hide the mouse cursor and prevent the mouse from leaving the window.
    log.printMSG("[MAINTHREAD][INFO] setting up OpenGL")
    window.set_exclusive_mouse(True)
    glfunctions.setup()
    log.printMSG("[MAINTHREAD][INFO] nothing to do here, starting pyglet")
    pyglet.app.run()

import modsystem.ModLoader
G.modloader.searchForMods()

G.statehandler.setState("minecraft:titlescreen")

if __name__ == '__main__':
    try:
        main()
    except:
        exceptionhandler.add_crash()
