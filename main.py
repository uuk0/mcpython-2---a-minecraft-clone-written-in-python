import sys
import os
import log
import globals as G
import shutil

log.printMSG("[MAINTHREAD][INFO] clearing tmp-dir")

for e in os.listdir(G.local+"tmp"):
    if e not in ["file.info"]:
        if os.path.isfile(G.local+"tmp/"+e):
            os.remove(G.local+"tmp/"+e)
        else:
            shutil.rmtree(G.local+"tmp/"+e)

try:
    import pyglet
    import PIL
    import numpy
    import noise
    import json
except:
    log.printMSG("[ERROR] can't load libarys")
    raise

import eventhandler
import biomes.biom
import eventhandler
import structur
import crafting
import texturedata
import language
import ticksystem
import Block.block, Item.item, entity.entity, Inventory.inventory
import state


pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')

if sys.version_info[0] == 2:
    log.printMSG("[MAINTHREAD][ERROR] unsupported python version: ", sys.version_info)
    sys.exit(-1)

import globals as G

import glfunctions

import soundhandler

from pyglet.gl import *

"""main function"""
def main():
    log.printMSG("[MAINTHREAD][INFO] creating window")
    import Inventory.inventory
    import window
    #window = window.Window(width=800, height=600, caption='mcp#ython 2', resizable=True)
    try:
        # Try and create a window with multisampling (antialiasing)
        config = Config(sample_buffers=1, samples=4,
                        depth_size=16, double_buffer=True, )
        window = window.Window(resizable=True, config=config, width=800, height=600, caption='mcpython 2')
    except pyglet.window.NoSuchConfigException:
        # Fall back to no multisampling for old hardware
        window = pyglet.window.Window(resizable=True, width=800, height=600, caption='mcpython 2')
    # Hide the mouse cursor and prevent the mouse from leaving the window.
    log.printMSG("[MAINTHREAD][INFO] setting up OpenGL")
    window.set_exclusive_mouse(True)
    glfunctions.setup()
    log.printMSG("[MAINTHREAD][INFO] giving the mainthread to pyglet...")
    pyglet.app.run()

import ModLoader
G.modloader.searchForMods()

G.statehandler.setState("minecraft:game")

if __name__ == '__main__':
    main()
