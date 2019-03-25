import PIL.Image
import os
import globals as G

PATHS = []


def construct():
    PATHS = [G.local] + [mod.path for mod in G.modloader.mods.values()]
    for path in PATHS[:]:
        if path:
            if os.path.isdir(os.path.join(path, "assets")):
                PATHS.append(os.path.join(path, "assets"))
                PATHS += [os.path.join(path, "assets", x) for x in os.listdir(os.path.join(path, "assets"))]


def join_file(file):
    if type(file) != str: return file
    if os.path.exists(file): return file
    for path in PATHS:
        f = os.path.join(path, file)
        if os.path.exists(f):
            return f
    return file


def resize(image: PIL.Image.Image, size: tuple) -> PIL.Image.Image:
    return image.resize(size)


def resize_file(file: str, size: tuple, store=None):
    file = join_file(file)
    if not store: store = file
    resize(PIL.Image.open(file), size).save(store)


def load_image(file: str) -> PIL.Image.Image:
    return PIL.Image.open(join_file(file))

