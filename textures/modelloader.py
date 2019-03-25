import globals as G
import textures.util
import textures.TextureAtlas
import json
import modsystem.ModLoader
import os
import mathhelper
import pyglet
import PIL.Image


def tex_coord(x, y, n1=4, n2=4):
    """ Return the bounding vertices of the texture square.
    moved for the config of TextureAtlas.
    for removing, delete delta here and set TextureAtlas constants to 64
    """
    m1 = 1.0 / n1  # (n1 + 15.5)
    m2 = 1.0 / n2  # (n2 + 15)
    dx = x * m1
    dy = y * m2
    return dx, dy, dx + m1, dy, dx + m1, dy + m2, dx, dy + m2


def text_coords_complex(top, bottom, n, o, s, w, n1=1, n2=1):
    top = tex_coord(*top, n1=n1, n2=n2)
    bottom = tex_coord(*bottom, n1=n1, n2=n2)
    n = tex_coord(*n, n1=n1, n2=n2)
    o = tex_coord(*o, n1=n1, n2=n2)
    s = tex_coord(*s, n1=n1, n2=n2)
    w = tex_coord(*w, n1=n1, n2=n2)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(n)
    result.extend(o)
    result.extend(s)
    result.extend(w)
    return result


class ModelHandler:
    def __init__(self):
        self.models = {}

    def load_from_file(self, file, extend_in_case=True):
        with open(file) as f:
            data = json.load(f)
            if "name" in self.models:
                Model.extend_model(self.models[data["name"]], data)
                return self.models[data["name"]]
            return Model(data)


G.modelhandler = ModelHandler()


class IModelEntry:
    """
    todo: add stairs, slabs, custom data, cross textures, doors, (logs?), alpha-attribute to all (-> rendersystem)
    todo: "super" models that can be included for custom data
    """
    TYPES = []

    @staticmethod
    def getName():
        return ""

    def __init__(self, entry, model):
        self.entry = entry
        self.model = model

    def show(self, batch, blockinst):
        raise NotImplementedError()

    def hide(self, batch, blockinst):
        raise NotImplementedError()


class CubeEntry(IModelEntry):
    @staticmethod
    def getName():
        return "cube:full"

    def __init__(self, entry, model):
        IModelEntry.__init__(self, entry, model)

    def show(self, batch, blockinst):
        position = blockinst.position
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if len(blockinst.showndata) > 0: self.hide(batch, blockinst)
        if not G.model.exposed(blockinst.position):
            return
        if not blockinst.position in chunkprovider.world:
            return
        x, y, z = blockinst.position
        vertex_data = chunkprovider.world[blockinst.position].getCubeVerticens(
            *list(chunkprovider.world[blockinst.position].convertPositionToRenderable(blockinst.position)) + [0.5])
        textureatlas = G.textureatlashandler.atlases[self.model.indexes[0][0] if hasattr(self.model.indexes[0],
                                                     "__getitem__") else
                                                     G.textureatlashandler.indexarray[self.model.indexes[0]][0]]
        texture_data = text_coords_complex(*[self.model.indexes[i][1][1] if hasattr(self.model.indexes[i][1][1],
                                                                                    "__getitem__") else
                                             self.model.indexes[i][1] for i in self.entry["sides"]],
                                             n1=16, n2=16)
        # create vertex list
        # FIXME Maybe `add_indexed()` should be used insteads
        blockinst.showndata.append(batch.add(24, pyglet.gl.GL_QUADS, textureatlas.pyglet_atlas,
                                             ('v3f/static', vertex_data),
                                             ('t2f/static', texture_data)))

    def hide(self, batch, blockinst):
        for e in blockinst.showndata:
            e.delete()
        blockinst.showndata = []


IModelEntry.TYPES.append(CubeEntry)


class ITextureGeneratorEntry:
    """
    todo: add overlay & color map
    """
    ENTRYS = {}

    @staticmethod
    def getName():
        pass

    @staticmethod
    def get_images_for(data, model):
        return []


class Rotate(ITextureGeneratorEntry):
    @staticmethod
    def getName():
        return "texture:rotate"

    @staticmethod
    def get_images_for(data, model):
        image = PIL.Image.open(textures.util.join_file(data["file"]))
        return [image.rotate(data["degrees"])]


ITextureGeneratorEntry.ENTRYS[Rotate.getName()] = Rotate


class Split(ITextureGeneratorEntry):
    @staticmethod
    def getName():
        return "texture:split"

    @staticmethod
    def get_images_for(data, model):
        image = PIL.Image.open(textures.util.join_file(data["file"]))
        images = []
        size = data["size"]
        for x in range(size[0]):
            for y in range(size[1]):
                images.append(image.grap((image.size[0] / size[0] * x,
                                          image.size[1] / size[1] * y,
                                          image.size[0] / size[0] * (x + 1) - 1,
                                          image.size[1] / size[1] * (y + 1) - 1)))
        return images


ITextureGeneratorEntry.ENTRYS[Split.getName()] = Split


class Model:
    def __init__(self, data, prepare=True):
        if not "texture generator" in data: data["texture generator"] = []
        self.data = data
        self.name = data["name"]  # name is the name of the block to bind to
        self.files = data["files"]  # a list of files to load with these block
        self.entrydata = data["entrys"]
        self.entrys = {}
        for entry in self.entrydata:
            for imodelentry in IModelEntry.TYPES:
                if imodelentry.getName() == entry["type name"]:
                    self.entrys[entry["state name"]] = imodelentry(entry, self)
        for extiondata in data["texture generator"]:
            if extiondata["type"] in ITextureGeneratorEntry.ENTRYS:
                self.files += ITextureGeneratorEntry.ENTRYS[extiondata["type"]].get_images_for(extiondata, self)
        G.modelhandler.models[self.name] = self
        self.indexes = None
        if prepare:
            self.prepare()

    def prepare(self):
        self.indexes = G.textureatlashandler.add_file_collection(self.files)

    @staticmethod
    def extend_model(model, data: dict):
        if not "texture generator" in data: data["texture generator"] = []
        model.entrydata.append(data["entrys"])
        for entry in data["entrys"]:
            for imodelentry in IModelEntry.TYPES:
                if imodelentry.getName() == entry["type name"]:
                    model.entrys[entry["state name"]] = imodelentry(entry, model)
        for extiondata in data["texture generator"]:
            if extiondata["type"] in ITextureGeneratorEntry.ENTRYS:
                model.files += ITextureGeneratorEntry.ENTRYS[extiondata["type"]].get_images_for(extiondata, model)

    def construct(self):
        self.indexes = [G.textureatlashandler.indexarray[x] if x in G.textureatlashandler.indexarray else 0
                        for x in self.indexes]


for file in os.listdir(G.local+"/assets/minecraft/models/blocks"):
    file = G.local+"/assets/minecraft/models/blocks/"+file
    if os.path.isfile(file):
        @modsystem.ModLoader.ModEventEntry("game:registry:on_texture_registrate_periode", "minecraft",
                                           info="registrating model "+file, add=[file])
        def register(f):
            G.modelhandler.load_from_file(f)

