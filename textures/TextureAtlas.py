import globals as G
import textures.util
import PIL.Image
import PIL.ImageDraw
import pyglet

TEXTURE_ENTRY_SIZE = 64
TEXTURE_IMAGE_SIZE = 64


class TextureAtlasHandler:
    def __init__(self):
        self.atlases = []
        self.file_to_index_array = {}
        self.todo = []
        self.indexarray = {}
        self.nextindex = 0

    def add_file_collection(self, files):
        """
        adds the file to the system
        make shure that these are in the same atlas
        :param files: the files to add
        :return: an list[ (texture_atlas_index, texture_index) ] - like object
        """
        indexes = list(range(self.nextindex, len(files) + self.nextindex + 1))
        self.nextindex += len(files)
        self.todo.append((files, indexes))
        return indexes

    def _add_file_collection(self, files, raw_indexes):
        indexes = []
        files = [
            textures.util.join_file(file) if type(file) == str else file
            for file in files
        ]
        if len(files) > 256:
            raise ValueError("can't add more than 256 images to an image atlas")
        for textureatlas in self.atlases:
            need = len(files)
            for file in files:
                if type(file) == str and file in textureatlas.files:
                    need -= 1
            if textureatlas.free_places >= need:
                for file in files:
                    if type(file) == str:
                        textures.util.resize_file(file, (64, 64))
                        if file not in textureatlas.files:
                            indexes.append(
                                textureatlas.add_image(textures.util.load_image(file))
                            )
                            textureatlas.files[file] = indexes[-1]
                        else:
                            indexes.append(textureatlas.files[file])
                            textureatlas.files[file] = indexes[-1]
                    else:
                        file = textures.util.resize(file, (64, 64))
                        indexes.append(textureatlas.add_image(file))

                for i, index in enumerate(indexes):
                    self.indexarray[raw_indexes[i]] = index
                return indexes
        textureatlas = TextureAtlas(len(self.atlases))
        self.atlases.append(textureatlas)
        for file in files:
            textures.util.resize_file(file, (64, 64))
            indexes.append(
                [
                    textureatlas.textureatlasid,
                    textureatlas.add_image(
                        textures.util.load_image(file) if type(file) == str else file
                    ),
                ]
            )
            textureatlas.files[file] = indexes[-1]
        for i, index in enumerate(indexes):
            self.indexarray[raw_indexes[i]] = index
        return indexes

    def add_file(self, file):
        """
        adds an new file to the whole system
        :param file: the file to add
        :return: an index (int) for accessing all needed data
        """
        index = self.nextindex
        self.nextindex += 1
        self.todo.append(([file], index))
        return index

    def _add_file_raw(self, file, raw_index):
        if type(file) == str:
            if file in self.file_to_index_array:
                return self.file_to_index_array[file]
            self.file_to_index_array[file] = self._add_file(file)
            index = self.file_to_index_array[file]
            self.indexarray[raw_index] = index
            self.atlases[index[0]].files[index[1]] = file
            return index
        else:
            return self._add_file(file)

    def _add_file(self, file):
        for textureatlas in self.atlases:
            if textureatlas.free_places > 0:
                if type(file) == str:
                    textures.util.resize_file(file, (64, 64))
                else:
                    textures.util.resize(file, (64, 64))
                return textureatlas.add_image(
                    textures.util.load_image(file) if type(file) == str else file
                )
        textureatlas = TextureAtlas(len(self.atlases))
        self.atlases.append(textureatlas)
        return textureatlas.textureatlasid, textureatlas.add_image(
            textures.util.load_image(file) if type(file) == str else file
        )

    def generate(self):
        textures.util.construct()
        # self.todo.sort(key=lambda x: x[0][0].split("/")[-1] if len(x[0]) > 0 else "", reverse=True)
        self.todo.sort(key=lambda x: len(x[0]), reverse=True)
        for data in self.todo:
            if len(data[0]) == 1:
                self._add_file_raw(data[0][0], data[1][0])
            else:
                self._add_file_collection(*data)
        for i, textureatlas in enumerate(self.atlases):
            textureatlas.baseimage.save(
                G.local + "/tmp/texture_atlas_" + str(i) + ".png"
            )
            textureatlas.pyglet_atlas = pyglet.graphics.TextureGroup(
                pyglet.image.load(
                    G.local + "/tmp/texture_atlas_" + str(i) + ".png"
                ).get_texture()
            )
        for model in G.modelhandler.models.values():
            model.construct()


G.textureatlashandler = TextureAtlasHandler()


class TextureAtlas:
    def __init__(self, textureatlasid: int):
        self.textureatlasid = textureatlasid
        self.baseimage = PIL.Image.new(
            "RGBA",
            (16 * TEXTURE_ENTRY_SIZE, 16 * TEXTURE_ENTRY_SIZE),
            (255, 255, 255, 255),
        )
        nondefimage = textures.util.load_image(
            G.local + "/assets/minecraft/textures/missingtexture.png"
        )
        nondefimage = textures.util.resize(
            nondefimage, (TEXTURE_IMAGE_SIZE, TEXTURE_IMAGE_SIZE)
        )
        for x in range(16):
            for y in range(16):
                image = nondefimage.crop((0, 0, TEXTURE_IMAGE_SIZE, TEXTURE_IMAGE_SIZE))
                d = PIL.ImageDraw.Draw(image)
                d.multiline_text(
                    (10, 10),
                    str((x + (15 - y) * 16)) + "\n" + str(self.textureatlasid),
                    fill=255,
                )
                self.baseimage.paste(
                    image, (x * TEXTURE_ENTRY_SIZE, y * TEXTURE_ENTRY_SIZE)
                )
        self.nextindex = [0, 0]
        self.free_places = 256
        self.pyglet_atlas = None
        self.files = {}

    def add_image(self, image: PIL.Image.Image) -> tuple:
        index = tuple(self.nextindex)
        self.nextindex[0] += 1
        if self.nextindex[0] > 15:
            self.nextindex[0] = 0
            self.nextindex[1] += 1
        self.baseimage.paste(
            image, (index[0] * TEXTURE_ENTRY_SIZE, (15 - index[1]) * TEXTURE_ENTRY_SIZE)
        )
        return self.textureatlasid, index
