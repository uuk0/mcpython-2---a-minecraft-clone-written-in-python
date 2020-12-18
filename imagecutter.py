import PIL, PIL.Image
import globals as G


def cut_image(file, fromposition, toposition, store):
    image = PIL.Image.open(file)
    subimage = image.crop(tuple(list(fromposition) + list(toposition)))
    subimage.save(store)


def resize(file, newsize):
    image = PIL.Image.open(file)
    image = image.resize(newsize)
    image.save(file)


def resize_mutli(file, multi):
    image = PIL.Image.open(file)
    image = image.resize((multi[0] * image.size[0], multi[1] * image.size[1]))
    image.save(file)
