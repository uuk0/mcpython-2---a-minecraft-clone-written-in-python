import sys
from PIL import Image
import numpy as np
import PIL
import globals as G
import pyglet
import mathhelper
import pyglet

"""store the given files into one"""
def storetexturs(file, texturfiles):
    for e in texturfiles:
        resize(e, [64, 64])
    imgs = [PIL.Image.open(i) for i in texturfiles]
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save(file)

"""resize an image"""
def resize(file, size, nfile=None):
    if not nfile: nfile = file
    img = Image.open(file)
    img = img.resize(size)
    img.save(nfile)

"""handler for texturs"""
class TexturHandler:
    def __init__(self):
        self.texturs = {}

    """registers an block textur"""
    def registerBlockTextur(self, file):
        group = pyglet.graphics.TextureGroup(pyglet.image.load(file).get_texture())
        self.texturs[file] = group

    """register an boxmodel textur"""
    def registerBoxModelTextur(self, file):
        self.texturs[file] = mathhelper.load_image(file)

    """get an texturfile by name"""
    def getByName(self, name):
        return self.texturs[name]

G.texturhandler = TexturHandler()

if __name__ == "__main__":
    storetexturs(sys.argv[1], sys.argv[2:])
