import json
import os
import pickle
import shutil
import sys

import globals as G
import log
import storage.loader
import storage.saver


class Loader(storage.loader.Loader):
    def getStorageVersion(self):
        return (0, 0, 0)

    def loadWorld(self, file):
        log.printMSG(
            "[SAVER][0.0.0][WARNING] version 0.0.0 is NOT supported. do this on your own risk"
        )
        with open(file + "/player.json") as f:
            playerdata = json.load(f)

        while (
            sum(
                [
                    len(chunkprovider.world)
                    for chunkprovider in G.player.dimension.worldprovider.chunkproviders.values()
                ]
            )
            != 0
        ):
            G.storagehandler.cleanUpModel()
        G.window.position = playerdata["pos"]
        G.window.rotation = playerdata["rot"]
        G.player.gamemode = playerdata["gamemode"]
        G.player.selectedinventoryslot = playerdata["selectedinventoryslot"]
        G.window.flying = True

        # do all neccasarius stuff
        self.loadDim(playerdata["dim"], file)

        G.window.flying = playerdata["flying"]

    def loadDim(self, dim, file):
        if type(dim) != int:
            dim = int(dim.id)
        file += "/DIM" + str(dim)
        for m in os.listdir(file):
            self.loadChunk(m.split(".")[0], m.split(".")[1], file + "/" + m)

    def loadChunk(self, cx, cz, file):
        log.printMSG(cx, cz)
        with open(file, mode="rb") as f:
            chunkdata = pickle.load(f)
        mx, mz = int(cx), int(cz)
        for rpos in chunkdata.keys():
            x, y, z = rpos.split(",")
            x = int(x[1:])
            y = int(y[1:])
            z = int(z[1:-1])
            pos = (x + mx * 16, y, z + mz * 16)
            G.BlockGenerateTasks[pos] = [
                chunkdata[rpos]["name"],
                "sdata",
                chunkdata[rpos],
            ]

    def isFile(self, file):
        if not os.path.isfile(file + "/storage.json"):
            return False
        with open(file + "/storage.json") as f:
            try:
                data = json.load(f)
            except:
                return False
        if data["version"] != list(self.getStorageVersion()):
            return False
        return True


G.storagehandler.register(Loader())


class Saver(storage.saver.Saver):
    def getStorageVersion(self):
        return (0, 0, 0)

    def saveWorld(self, file):
        log.printMSG(
            "[SAVER][0.0.0][WARNING] version 0.0.0 is NOT supported. do this on your own risk"
        )
        if not os.path.isdir(file):
            os.makedirs(file)
        self.saveDim(G.player.dimension, file + "/DIM" + str(G.player.dimension.id))
        playerdata = {
            "dim": G.player.dimension.id,
            "pos": G.window.position,
            "rot": G.window.rotation,
            "gamemode": G.player.gamemode,
            "flying": G.window.flying,
            "selectedinventoryslot": G.player.selectedinventoryslot,
        }
        with open(file + "/player.json", mode="w") as f:
            json.dump(playerdata, f)
        storagedata = {
            "version": self.getStorageVersion(),
            "gameversion": G.VERSION_ID,
            "gameversionanme": G.VERSION_NAME,
            "seed": G.seed,
        }
        with open(file + "/storage.json", mode="w") as f:
            json.dump(storagedata, f)

    def saveDim(self, dim, file):
        if not os.path.isdir(file):
            os.makedirs(file)
        if dim != G.player.dimension:
            log.printMSG(
                "[WORLDSAVER][0.0.0][ERROR] can't save unloaded dim " + str(dim)
            )
            return
        for cx, cz in G.player.dimension.worldprovider.chunkproviders.keys():
            self.saveChunk(cx, cz, file + "/" + str(cx) + "." + str(cz) + ".chunk")

    def _transformposition(self, cx, cz, x, y, z):
        return x - cx * 16, y, z - cz * 16

    def saveChunk(self, cx, cz, file):
        if not (cx, cz) in G.player.dimension.worldprovider.chunkproviders:
            log.printMSG(
                "[WORLDSAVER][0.0.0][ERROR] can't save unloaded chunk " + str(cx, cz)
            )
            return
        chunkdata = {}
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        for position in chunkprovider.world.keys():
            block = chunkprovider.world[position]
            chunkdata[
                str(self._transformposition(cx, cz, *position))
            ] = block.getStorageData()
        with open(file, mode="wb") as f:
            pickle.dump(chunkdata, f)


G.storagehandler.register(Saver())
