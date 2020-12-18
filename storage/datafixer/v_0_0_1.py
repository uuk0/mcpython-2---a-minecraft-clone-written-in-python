"""
new version system since 19w08a
"""

import storage.loader, storage.saver
import globals as G
import log
import json
import pickle
import os
import Inventory.inventory
import traceback


class Saver(storage.saver.Saver):
    def getStorageVersion(self):
        return (0, 0, 1)

    def saveWorld(self, file):
        if not os.path.exists(file):
            os.makedirs(file)
        log.printMSG("[SAVER][0.0.1][INFO] collecting world & player info...")
        worldinfo = {
            "version_name": G.VERSION_NAME,
            "version_id": G.VERSION_ID,
            "main_player_name": G.player.name,
            "seed": G.seed,
            "storage_version": self.getStorageVersion(),
            "player_table": {
                G.player.name: {
                    "position": G.window.position,
                    "rotation": G.window.rotation,
                    "selectedinventoryslot": G.player.selectedinventoryslot,
                    "inventory": G.player.inventory.id,
                    "gamemode": G.player.gamemode,
                    "dimension": G.player.dimension.id,
                    "flying": G.window.flying,
                    "harts": G.player.harts,
                }
            },
            "dimension_table": {},
        }
        for dim in G.dimensionhandler.dimensions.values():
            worldinfo["dimension_table"][dim.getName()] = dim.id
        with open(file + "/world.info", mode="w") as f:
            json.dump(worldinfo, f, separators=(",\n", ": "))
        log.printMSG("[SAVER][0.0.1][INFO] collecting inventory data")
        inventorytable = {}
        for id in G.inventoryhandler.inventorys.keys():
            inventory = G.inventoryhandler.inventorys[id]
            if issubclass(type(inventory), Inventory.inventory.Inventory):
                inventorydata = {"type": "INVENTORY", "slots": []}
                for slot in inventory.slots:
                    if slot.stack.item:
                        inventorydata["slots"].append(
                            {
                                "item": slot.stack.item.getName(),
                                "amount": slot.stack.amount,
                            }
                        )
                    else:
                        inventorydata["slots"].append({"item": None, "amount": 0})
                inventorytable[id] = inventorydata
            elif issubclass(type(inventory), Inventory.inventory.InventoryCollection):
                inventorydata = {
                    "type": "INVENTORYCOLLECTION",
                    "subinventorys": [inv.id for inv in inventory.inventorys],
                }
                inventorytable[id] = inventorydata
        with open(file + "/inventorys.info", mode="w") as f:
            json.dump(inventorytable, f, separators=(",\n", ": "))
        log.printMSG("[SAVER][0.0.1][INFO] collecting entitys")
        entitytable = []
        for entity in G.entityhandler.entitys:
            entitydata = {
                "position": entity.position,
                "rotation": None,
                "name": entity.getName(),
                "nbt": entity.getNBT(),
            }
            entitytable.append(entitydata)
        with open(file + "/entitys.info", mode="w") as f:
            json.dump(entitytable, f)
        self.saveDim(G.player.dimension, file + "/DIM" + str(G.player.dimension.id))

    def saveDim(self, dim, file):
        if not os.path.exists(file):
            os.makedirs(file)
        worldprovider = dim.worldprovider
        for chunk in worldprovider.chunkproviders.keys():
            self.saveChunk(
                chunk[0],
                chunk[1],
                file
                + "/c."
                + str(round(chunk[0]))
                + "."
                + str(round(chunk[1]))
                + ".chunk",
            )

    def saveChunk(self, cx, cz, file):
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if len(chunkprovider.world) == 0:
            return
        log.printMSG("[SAVER][0.0.1][INFO] collecting chunk " + str((cx, cz)))
        chunkdata = {
            "saved_version": G.VERSION_ID,
            "position": (cx, cz),
            "blocks": {},
            "inventorybindings": {},
        }
        for position in chunkprovider.world.keys():
            chunkdata["blocks"][position] = chunkprovider.world[
                position
            ].getStorageData()
            inventorys = chunkprovider.world[position].getInventorys()
            if len(inventorys) > 0:
                chunkdata["inventorybindings"][position] = [
                    inventory.id for inventory in inventorys
                ]
        with open(file, mode="wb") as f:
            pickle.dump(chunkdata, f)


G.storagehandler.register(Saver())


class Loader(storage.loader.Loader):
    def getStorageVersion(self):
        return (0, 0, 1)

    def loadWorld(self, file):
        log.printMSG("[LOADER][0.0.1][INFO] collecting world & player info...")
        with open(file + "/world.info", mode="r") as f:
            worlddata = json.load(f)
        if G.VERSION_ID < worlddata["version_id"]:
            log.printMSG(
                "can't load world. world is saved in an NEWER version of mcpython"
            )
            raise RuntimeError()
        G.player.name = worlddata["main_player_name"]
        G.seed = worlddata["seed"]
        G.window.position = worlddata["player_table"][G.player.name]["position"]
        G.window.rotation = worlddata["player_table"][G.player.name]["rotation"]
        G.player.selectedinventoryslot = worlddata["player_table"][G.player.name][
            "selectedinventoryslot"
        ]
        G.player.gamemode = worlddata["player_table"][G.player.name]["gamemode"]
        G.window.flying = True  # this is for falling down reasons only
        G.player.harts = worlddata["player_table"][G.player.name]["harts"]
        self.loadDim(
            worlddata["player_table"][G.player.name]["dimension"],
            file + "/DIM" + str(worlddata["player_table"][G.player.name]["dimension"]),
        )
        G.window.flying = worlddata["player_table"][G.player.name]["flying"]

    def loadDim(self, dim, file):
        worldprovider = G.dimensionhandler.dimensions[dim].worldprovider
        for f in os.listdir(file):
            if f.endswith(".chunk"):
                _, cx, cz, _ = tuple(f.split("."))
                cx, cz = int(cx), int(cz)
                self._loadChunk(
                    worldprovider.getChunkProviderFor((cx, cz)), file + "/" + f
                )

    def loadChunk(self, cx, cz, file):
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        self._loadChunk(
            chunkprovider, file + "/c." + str(cx) + "." + str(cz) + ".chunk"
        )

    def _loadChunk(self, chunkprovider, file):
        log.printMSG("[LOADER][0.0.1][INFO] loading chunk " + str(file))
        if not os.path.isfile(file):
            log.printMSG("can't access file named " + file)
            traceback.print_stack()
            return
        with open(file, mode="rb") as f:
            chunkdata = pickle.load(f)
        cx, cz = chunkdata["position"]
        chunkprovider = chunkprovider.worldprovider.getChunkProviderFor((cx, cz))
        for position in chunkdata["blocks"].keys():
            if chunkdata["blocks"][position]["shown"]:
                G.model.add_block(
                    position, chunkdata["blocks"][position]["name"], immediate=True
                )
                chunkprovider.world[position].setStorageData(
                    chunkdata["blocks"][position]
                )
            else:
                G.BlockGenerateTasks[position] = [
                    chunkdata["blocks"][position]["name"],
                    "sdata",
                    chunkdata["blocks"][position],
                ]

    def isFile(self, file):
        with open(file + "/world.info", mode="r") as f:
            worlddata = json.load(f)
        return "storage_version" in worlddata and worlddata["storage_version"] == list(
            self.getStorageVersion()
        )


G.storagehandler.register(Loader())
