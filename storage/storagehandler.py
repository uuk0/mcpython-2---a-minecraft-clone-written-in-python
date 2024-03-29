import importlib
import os

import globals as G
import log
import storage.loader
import storage.saver

"""
TODO: add entitys
"""

"""
the following versions ARE supported:
    0.0.1
    
the following version ARE N O T supported:
    0.0.0
"""


class StorageHandler:
    def __init__(self):
        self.versions = {}
        self.latest = None

    def register(self, obj):
        if type(obj) == storage.saver.Saver or issubclass(
            type(obj), storage.saver.Saver
        ):
            if obj.getStorageVersion() not in self.versions:
                self.versions[obj.getStorageVersion()] = {}
            self.versions[obj.getStorageVersion()]["saver"] = obj
        elif type(obj) == storage.loader.Loader or issubclass(
            type(obj), storage.loader.Loader
        ):
            if obj.getStorageVersion() not in self.versions:
                self.versions[obj.getStorageVersion()] = {}
            self.versions[obj.getStorageVersion()]["loader"] = obj
        if not self.latest or obj.getStorageVersion() > self.latest:
            self.latest = obj.getStorageVersion()

    def getLatestSaver(self):
        return self.versions[self.latest]["saver"]

    def getLatestLoader(self):
        return self.versions[self.latest]["loader"]

    def getFor(self, file):
        for e in self.versions.values():
            if e["loader"].isFile(file):
                return e
        log.printMSG("[STORAGE][ERROR] unknown format in dir " + str(file))

    def update(self, file):
        self.getFor(file).loadWorld(file)
        self.getLatestSaver().saveWorld(file)

    def loadWorld(self, file):
        if G.window.worldname:
            self.saveWorld(G.window.worldname)
        obj = self.getFor(file)
        self.cleanUpModel()
        if not obj:
            return
        obj["loader"].loadWorld(file)
        G.model.change_sectors(None, G.window.get_motion_vector())

    def saveWorld(self, file, version="latest"):
        if version == "latest":
            version = self.latest
        if not version in self.versions:
            log.printMSG("[WORLDSAVER][ERROR] version is not supported")
            return
        obj = self.versions[version]
        obj["saver"].saveWorld(file)

    def cleanUpModel(self):
        G.model.clear()


G.storagehandler = StorageHandler()


for e in os.listdir(G.local + "/storage/datafixer"):
    importlib.import_module("storage.datafixer." + str(e.split(".")[0]))
