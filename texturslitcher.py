

import globals as G
import PIL, os, json
from PIL import Image
import mathhelper
import pyglet
import log


class ImageAtlasHandler:
    def __init__(self):
        os.makedirs(G.local+"/tmp/imageatlas_data")
        self.atlases = {}
        self.othernames = {}
        self.imageatlases = []
        self.nextatlasindex = 0
        self.tmpindex = 0

    def creat_image_atlas_for(self, name, filelist):
        atlas = ImageAtlas(name)
        index = 0
        for e in filelist:
            index += atlas.add_image_from_file(e, index)
        return atlas

    def register_image_atlas(self, atlas):
        if not issubclass(type(atlas), ImageAtlas): raise ValueError("can only register ImageAtlas-like objects")
        self.atlases[atlas.addressname] = atlas

    def init(self):
        log.printMSG("initing image atlases...")
        for i, e in enumerate(self.atlases.values()):
            log.printMSG(i, "/", len(self.atlases))
            e.init()
        log.printMSG("creating image atlasses...")
        for i, e in enumerate(self.imageatlases):
            log.printMSG(i, "/", len(self.atlases))
            e.init()
        log.printMSG("transforming names...")
        for e in self.othernames.keys():
            for v in self.othernames[e]:
                if not v in self.atlases:
                    self.atlases[v] = self.atlases[e]

class IImageType:
    TYPES = []

    @staticmethod
    def getName():
        return None

    @staticmethod
    def getSubImages(image, data):
        return []

class ToSplit(IImageType):
    @staticmethod
    def getName():
        return "split"

    @staticmethod
    def getSubImages(image, data):
        size = data["size"]
        ImageAtlas.resize(image, (size[0] * 64, size[1] * 64))
        images = []
        stepsize = (image.size[0] / size[0], image.size[1] / size[1])
        for rx in range(size[0]):
            for ry in range(size[1]):
                x, y = rx * stepsize[0], ry * stepsize[1]
                images.append(image.crop((x, y, x+stepsize[0], y+stepsize[1])))
        return images


IImageType.TYPES.append(ToSplit)


class ImageAtlas:
    @staticmethod
    def resize(image, newsize):
        return image.resize(newsize)

    @staticmethod
    def convertFileName(file):
        if not os.path.isfile(file):
            l = G.modloader.mods.values()
            for i, e in enumerate([G.local] + [mod.path for mod in l]):
                if e:
                    #log.printMSG([(mod.path, mod, file) for mod in G.modloader.mods.values()])
                    if os.path.isfile(e+"/"+file):
                        file = e + "/" + file
                        return file
        return file

    @staticmethod
    def load_image(file):
        old_file = file
        file = ImageAtlas.convertFileName(file)
        if file == "":
            raise ValueError("unsupported file "+old_file)
        image = Image.open(file)
        return image

    @staticmethod
    def save_image(image, file):
        file = ImageAtlas.convertFileName(file)
        return image.save(file)

    def __init__(self, addressname, size=(16, 16)):
        self.addressname = addressname
        self._size = size
        self.imagefiles = []
        self.imageindexes = {}
        self.__inited = False
        self.pygletatlas = None
        self._imageatlas = None
        self.relativeindex = 0

        if type(self) == _ImageAtlas:
            self.vimage = Image.new("RGBA", (size[0] * 64, size[1] * 64))
        else:
            G.imageatlashandler.register_image_atlas(self)

    def init(self):
        if self.__inited: raise RuntimeError("can't init an inited ImageAtlas")
        self.__inited = True
        for imageatlas in G.imageatlashandler.imageatlases:
            if len(imageatlas.imagefiles) + len(self.imagefiles) < imageatlas._size[0] * imageatlas._size[1]:
                self.relativeindex = len(imageatlas.imagefiles)
                for e in self.imagefiles:
                    imageatlas.add_image_from_file(e[0], e[2])
                self._imageatlas = imageatlas
                return
        atlas = _ImageAtlas(G.imageatlashandler.nextatlasindex)
        atlas.storeto = G.local+"/tmp/"+str(G.imageatlashandler.nextatlasindex)+".png"
        G.imageatlashandler.nextatlasindex += 1
        self.relativeindex = 0
        for e in self.imagefiles:
            atlas.add_image_from_file(e[0], e[2])
        self._imageatlas = atlas
        G.imageatlashandler.imageatlases.append(atlas)

    def add_image_from_file(self, file, index):
        if self.__inited: raise RuntimeError("can't add an image to an closed image atlas")
        file = self.convertFileName(file)
        image = self.load_image(file)
        if os.path.exists(file+".json"):
            with open(file+".json") as f: data = json.load(f)
            for e in IImageType.TYPES:
                if e.getName() == data["type"]:
                    images = e.getSubImages(image, data)
                    for i, e in enumerate(images):
                        self.__add_image(e, G.local+"/tmp/imageatlas_data/"+str(G.imageatlashandler.tmpindex)+"_imageatlas_split.png", index+i)
                        G.imageatlashandler.tmpindex += 1
                    return len(images)
        self.__add_image(image, file, index)
        return 1

    def __add_image(self, image, file, index):
        image = self.resize(image, (64, 64))
        self.save_image(image, file)
        self.imagefiles.append([file, self.load_image(file), index])

    def getImageDataFor(self, side_indexes):
        self.pygletatlas = self._imageatlas.pygletatlas
        return self._imageatlas.getImageDataFor([x + self.relativeindex for x in side_indexes])

class _ImageAtlas(ImageAtlas):
    def __init__(self, *args, **kwargs):
        ImageAtlas.__init__(self, *args, **kwargs)
        self.storeto = None
    
    def get_image_index(self, file):
        if not self.__inited: raise RuntimeError("can't get imageposition of an image in an opened imageatlas")
        if not file in self.imageindexes: raise ValueError("file "+str(file)+" not found")
        return self.imageindexes[file]

    def get_size(self):
        return self._size

    size = property(get_size)

    def init(self):
        if self.__inited: raise RuntimeError("can't init an inited ImageAtlas")
        self.__inited = True
        images = []
        imagedict = {}
        for e in self.imagefiles:
            images.append(e[1])
            imagedict[e[2]] = e[1]

        x = 0
        y = 0
        i = 0
        for e in images:
            e = self.resize(e, (64, 64,))
            self.vimage.paste(e, (x*64, y*64,))
            self.imageindexes[i] = (x, 16 - y - 1)
            x += 1
            if x >= self._size[0]:
                x = 0
                y += 1
            #if y >= self._size[1] and i < 256:
                #raise RuntimeError("unsupported image lenght at index "+str(i))
            i += 1
        d = os.path.dirname(self.storeto)
        if not os.path.exists(d): os.makedirs(d)
        self.resize(self.vimage, (self.size[0] * 16, self.size[1] * 16))
        self.resize(self.vimage, (self.size[0] * 64, self.size[1] * 64))
        self.save_image(self.vimage, self.storeto)
        self.pygletatlas = pyglet.graphics.TextureGroup(
            pyglet.image.load(self.storeto).get_texture())

    def getImageDataFor(self, side_indexes):
        return mathhelper.text_coords_complex(*[self.imageindexes[i] for i in side_indexes], n1=16, n2=16)


G.imageatlashandler = ImageAtlasHandler()