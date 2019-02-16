import globals as G
import json, texturslitcher, os
import pyglet
import mathhelper
import log
import modsystem.ModLoader


class ModelHandler:
    def __init__(self):
        self.models = {}

    def loadFromFile(self, file):
        model = Model(file)
        self.models[model.blockname] = model

    def loadFromDir(self, dir):
        for e in os.listdir(dir):
            self.loadFromFile(dir+"/"+e)


G.modelhandler = ModelHandler()


class IModelType:
    TYPES = []

    @staticmethod
    def addToBatch(data, blockinst, position):
        pass

    @staticmethod
    def removeFromBatch(data, blockinst, position):
        pass

    @staticmethod
    def getTypeName():
        return None

    @staticmethod
    def prepareData(data):
        pass


class Cube(IModelType):
    @staticmethod
    def getTypeName():
        return "cube:full"

    @staticmethod
    def addToBatch(data, inst, position):
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if len(inst.showndata) > 0: Cube.removeFromBatch(data, inst, position)
        if not G.model.exposed(inst.position): return
        if not inst.position in chunkprovider.world: return
        x, y, z = inst.position
        vertex_data = chunkprovider.world[inst.position].getCubeVerticens(
            *list(chunkprovider.world[inst.position].convertPositionToRenderable(inst.position))+[0.5])
        try:
            atlas = G.imageatlashandler.atlases[data["blockname"]]
            texture_data = atlas.getImageDataFor(list(data["side_indexes"]))
        except:
            log.printMSG(inst, inst.getName())
            raise
        # create vertex list
        # FIXME Maybe `add_indexed()` should be used insteads
        inst.showndata.append(G.player.dimension.worldprovider.batch.add(24, pyglet.gl.GL_QUADS,
                                                                       atlas.pygletatlas,
            ('v3f/static', vertex_data),
            ('t2f/static', texture_data)))

    @staticmethod
    def removeFromBatch(data, inst, position):
        for e in inst.showndata:
            e.delete()
        inst.showndata = []

    @staticmethod
    def prepareData(datalist):
        texturefiles = []
        names = []
        for data in datalist:
            texturefiles += data["side_texture_files"]
            n = data["blockname"]
            if n not in names: names.append(n)
        l = len(texturefiles)
        mindexstart = []
        sindex = sum([len(e["side_texture_files"]) for e in datalist[1:]])
        for data in datalist:
            mindexstart.append(sindex)
            flag = "relative_index" not in data or data["relative_index"]
            for i, e in enumerate(data["side_indexes"]):
                data["side_indexes"][i] = (l - (e + sindex) - 1) if flag else e
            sindex -= len(data["side_texture_files"])
        G.imageatlashandler.creat_image_atlas_for(datalist[0]["blockname"], texturefiles)
        G.imageatlashandler.othernames[datalist[0]["blockname"]] = names


IModelType.TYPES.append(Cube)


class Log(IModelType):
    @staticmethod
    def addToBatch(data, inst, position):
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if len(inst.showndata) > 1: Cube.removeFromBatch(data, inst, position)
        if not G.model.exposed(inst.position): return
        if not inst.position in chunkprovider.world: return
        x, y, z = inst.position
        vertex_data = chunkprovider.world[inst.position].getCubeVerticens(
            *list(chunkprovider.world[inst.position].convertPositionToRenderable(inst.position)) + [
                0.5])
        try:
            atlas = G.imageatlashandler.atlases[data["blockname"]]
            texture_data = atlas.getImageDataFor(Log.transform(inst, data))
        except:
            log.printMSG(inst, inst.getName())
            raise
        # create vertex list
        # FIXME Maybe `add_indexed()` should be used insteads
        inst.showndata.append(G.player.dimension.worldprovider.batch.add(24, pyglet.gl.GL_QUADS,
                                                                       atlas.pygletatlas,
                                                                       ('v3f/static', vertex_data),
                                                                       ('t2f/static', texture_data)))

    @staticmethod
    def transform(inst, data):
        rotation = inst.data["rotation"] #possible: "UD", "NS", "OW"
        if rotation == "UD":
            return [data["FRONT_INDEX"], data["FRONT_INDEX"]] + \
                    [data["SIDE_INDEX"]] * 4
        return [0, 0, 0, 0, 0, 0]

    @staticmethod
    def removeFromBatch(data, inst, position):
        for e in inst.showndata:
            e.delete()
        inst.showndata = []

    @staticmethod
    def getTypeName():
        return "cube:log"

    @staticmethod
    def prepareData(datalist):
        texturefiles = []
        names = []
        for data in datalist:
            texturefiles += [G.local + "/" + e for e in data["side_texture_files"]]
            n = data["blockname"]
            if n not in names: names.append(n)
        l = len(texturefiles)
        mindexstart = []
        sindex = 0#2 * (len(datalist) - 1)
        for data in datalist:
            mindexstart.append(sindex)
            data["SIDE_INDEX"] += sindex
            data["FRONT_INDEX"] += sindex
            sindex += 2
        G.imageatlashandler.creat_image_atlas_for(datalist[0]["blockname"], texturefiles)
        G.imageatlashandler.othernames[datalist[0]["blockname"]] = names


IModelType.TYPES.append(Log)


class Model:
    def __init__(self, file):
        with open(file) as f:
            self.data = json.load(f)
        self.blockname = self.data["blockaddress"]
        sorted_by_type = {}
        for e in self.data.keys():
            if not e in ["blockaddress"]:
                state = self.data[e]["name"]
                for item in IModelType.TYPES:
                    if item.getTypeName() == state:
                        if not item in sorted_by_type:
                            sorted_by_type[item] = []
                        sorted_by_type[item].append(self.data[e])
        for k in sorted_by_type.keys():
            k.prepareData(sorted_by_type[k])

    def addToBatch(self, blockinst, position):
        # print(self.data, blockinst.blockclass, blockinst.getStateName())
        state = self.data[blockinst.getStateName()]["name"]
        for e in IModelType.TYPES:
            if e.getTypeName() == state:
                e.addToBatch(self.data[blockinst.getStateName()], blockinst, position)
                return

    def removeFromBatch(self, blockinst, position):
        state = self.data[blockinst.getStateName()]["name"]
        for e in IModelType.TYPES:
            if e.getTypeName() == state:
                e.removeFromBatch(self.data[blockinst.getStateName()], blockinst, position)
                return


for file in os.listdir(G.local+"/assets/minecraft/models/blocks"):
    @modsystem.ModLoader.ModEventEntry("game:registry:on_texture_registrate_periode", "minecraft",
                                       info="registrating model "+file, add=[file])
    def register(f):
        G.modelhandler.loadFromFile(G.local+"/assets/minecraft/models/blocks/"+f)

