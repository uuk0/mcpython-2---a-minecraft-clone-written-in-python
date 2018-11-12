"""
from PIL import Image, ImageFilter

image = Image.open('picture1.png')
image = image.fill(yellow)
image.save('new_name.png')
"""

from PIL import Image, ImageDraw

def convert(file):
    image = Image.open(file)
    width, height = image.size
    center = (0, 0) #(int(0.5 * width), int(0.5 * height))
    ImageDraw.floodfill(image, xy=center, value=(0, 0, 0, 0))
    image.save(file)

if __name__ == "__main__":
    import sys
    convert(sys.argv[1])


