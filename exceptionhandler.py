import traceback, time, datetime
import globals as G
import os
import platform
import log
try:
    import pyglet
except ImportError:
    # will be handled somewhere else
    pyglet = None


def _add_text(text):
    with open(G.local+"/exception.txt", mode="a") as f: f.write("\n"+text)


def _print_mods():
    for mod in G.modloader.mods.values():
        _add_text(":"+str(mod.getName())+" version | "+str(mod.getVersion()))


def add_header(head=True):
    if head:
        _add_text("\n--------------------------------------------------------------------------------")
        _add_text("- MCPYTHON VERSION " + G.VERSION_NAME.upper() + " " * (60 - len(G.VERSION_NAME)) + "-")
        _add_text("--------------------------------------------------------------------------------")
        _add_text("informations about os, location, version etc.")
    _add_text(":timestamp | " + log.getStamp())
    _add_text(":versionid | "+str(G.VERSION_ID))
    _add_text(":G.local | "+str(G.local))
    _add_text(":os name | "+str(platform.system()))
    _add_text(":os version | "+str(platform.version()))
    _add_text(":os proccessor | "+str(platform.processor()))
    _add_text(":os proccessor architektur | "+str(platform.architecture()))
    if pyglet: _add_text(":pyglet | "+str(pyglet.version))
    else: _add_text(":pyglet | NOT INSTALLED")


def add_traceback():
    _add_text("stamp: "+log.getStamp())
    _add_text("an exception occured\n")
    with open(G.local + "/exception.txt", mode="a") as f: traceback.print_exc(file=f)


def add_crash():
    log.printMSG("THE GAME CRASHED!!!")
    traceback.print_exc()
    try:
        _add_text("####################################")
        _add_text("the game crashed")
        _add_text("\nwith the following mods:")
        _print_mods()
        _add_text("\n")
        add_traceback()
        _add_text("------------------------------------")
        _add_text("you are looking at the informations about the crash. look above for the real crash")
        add_header(head=False)
        _add_text("------------------------------------")
        _add_text("these is an redone of the log:")
        _add_text("++++++++++++++++++++++++++++++++++++")
        for e in log.CASH:
            _add_text(" ".join(e))
        _add_text("++++++++++++++++++++++++++++++++++++")
        _add_text("####################################")
    except:
        _add_text("????????????????????????????????????")
        _add_text("EXCEPTION DURING HANDLING EXCEPTION")
        add_traceback()
        _add_text("????????????????????????????????????")

