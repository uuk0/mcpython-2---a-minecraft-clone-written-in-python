import globals as G
import modsystem.ModLoader
import PIL.Image
import imagecutter
import log
import os


@modsystem.ModLoader.textureentry
def on_start(*args, **kwargs):
    log.printMSG("[VANILLA][TEXTUREGENERATOR] generating vanilla textures")

    # GUI AREA

    imagecutter.cut_image(G.local + "/assets/minecraft/textures/gui/widgets.png", (0, 0), (182, 22),
                          G.local + "/tmp/gui/hotbar.png")
    imagecutter.cut_image(G.local + "/assets/minecraft/textures/gui/container/inventory.png", (0, 0), (176, 166),
                          G.local + "/tmp/gui/playerinventory.png")
    imagecutter.cut_image(G.local + "/assets/minecraft/textures/gui/widgets.png", (0, 22), (24, 46),
                          G.local + "/tmp/gui/hotbar_select.png")
    imagecutter.resize_mutli(G.local + "/tmp/gui/hotbar.png", (2, 2))
    imagecutter.resize(G.local + "/tmp/gui/playerinventory.png", (375, 353))
    imagecutter.resize_mutli(G.local + "/tmp/gui/hotbar_select.png", (2, 2))

    # Block Area

    # - Grass

    os.makedirs(G.local + "/tmp/minecraft/block/grass")

    image = PIL.Image.open(G.local+"/assets/minecraft/textures/block/grass_top.png")
    image.save(G.local + "/tmp/minecraft/block/grass/item_0.png")

    """

    

    colormap = PIL.Image.open(G.local+"/assets/minecraft/textures/colormap/grass.png")
    index = 0

    convert_image(PIL.Image.open(G.local + "/assets/minecraft/textures/block/grass_block_top.png"), (11, 102, 35))\
        .save(G.local + "/tmp/minecraft/block/grass/item_" + str(index) + ".png")"""


def convert_image(image, groundimagecolor):
    image = image.convert("L")
    ground = PIL.Image.new("RGB", image.size, groundimagecolor)
    ground.putalpha(image)
    return ground







