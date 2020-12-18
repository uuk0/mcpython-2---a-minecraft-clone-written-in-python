import math
import globals as G
import gen.Random
import mathhelper


def _rotatepoint(x, y, z, rx, ry, rz):

    # X
    y = y * math.cos(rx) - z * math.sin(rx)
    z = y * math.sin(rx) + z * math.cos(rx)

    # Y
    x = z * math.sin(ry) + x * math.cos(ry)
    z = z * math.cos(ry) - x * math.sin(ry)

    # Z
    x = x * math.cos(rz) - y * math.cos(rz)
    y = x * math.sin(rz) + y * math.cos(rz)

    return x, y, z


class OreHandler:
    def __init__(self):
        pass


class OreChunkProvider:
    def __init__(self, chunk, chunkprovider):
        self.generationtable = {}  # OreVeinClass -> chunkamount real
        self.chunk = chunk
        self.chunkprovider = chunkprovider
        self.random = gen.Random.Random(G.seed)

    def generate(self):
        if not self.chunkprovider.generated:
            raise RuntimeError()
        biomes = []
        biomeamount = {}
        for x, z in self.chunkprovider.generationcache["biomemap"].keys():
            biome = G.biomehandler.biomes[
                self.chunkprovider.generationcache["biomemap"][(x, z)]
            ]
            if not biome in biomes:
                biomes.append(biome)
                biomeamount[biome] = 1
            else:
                biomeamount[biome] += 1
        veintable = {}  # vein -> percent of chunk
        for biome in biomes:
            oreveins = biome.getOreVeins()
            for vein in oreveins:
                if not vein in self.generationtable:
                    self.generationtable[vein] = 0
                    veintable[vein] = (
                        biomeamount[biome] * vein.getChunkAmount(vein) / 256
                    )
                else:
                    veintable[vein] += (
                        biomeamount[biome] * vein.getChunkAmount(vein) / 256
                    )
        for orevein in self.generationtable.keys():
            while self.generationtable[orevein] < veintable[orevein]:
                x = self.random.generateValueForPosition(
                    (self.chunk[0] * 16, -12, self.chunk[1] * 16), 0, 15
                )
                x += self.chunkprovider.chunk[0] * 16
                z = self.random.generateValueForPosition(
                    (self.chunk[0] * 16, -14, self.chunk[1] * 16), 0, 15
                )
                z += self.chunkprovider.chunk[1] * 16
                cx, _, cz = mathhelper.sectorize((x, 0, z))
                chunkprovider = self.chunkprovider.worldprovider.getChunkProviderFor(
                    (cx, cz)
                )
                if chunkprovider.generated:
                    y = self.random.generateValueForPosition(
                        (x, -13, z),
                        0,
                        chunkprovider.generationcache["highmap"][(x, z)] - 5,
                    )
                    biome = G.biomehandler.biomes[
                        chunkprovider.generationcache["biomemap"][(x, z)]
                    ]
                    if orevein in biome.getOreVeins():
                        self.generationtable[orevein] += 1
                        orevein.past(orevein, self.chunkprovider, self.random, x, y, z)


class OreVein:
    def past(self, chunkprovider, r, x, y, z):
        pass

    def getChunkAmount(self):
        return 0


class BaseOreVein(OreVein):
    def past(self, chunkprovider, r, x, y, z):
        xrot = r.generateValueForPosition((x, y - 1000, z), -90, 90)
        yrot = r.generateValueForPosition((x, y - 1001, z), -90, 90)
        zrot = r.generateValueForPosition((x, y - 1002, z), -90, 90)
        xlenght = r.generateValueForPosition(
            (x, y - 1003, z), self.getMinSize(self) / 2, self.getMaxSize(self) / 2
        )
        ylenght = r.generateValueForPosition(
            (x, y - 1004, z), self.getMinSize(self) / 2, self.getMaxSize(self) / 2
        )
        zlenght = r.generateValueForPosition(
            (x, y - 1005, z), self.getMinSize(self) / 2, self.getMaxSize(self) / 2
        )
        if xlenght == 0 or ylenght == 0 or zlenght == 0:
            return  # this orevein is empty
        for dx in range(-xlenght, xlenght + 1):
            for dy in range(-ylenght, ylenght + 1):
                for dz in range(-zlenght, zlenght + 1):
                    mx, my, mz = _rotatepoint(x, y, z, xrot, yrot, zrot)
                    if (mx * mx) / (xlenght * xlenght) + (my * my) / (
                        ylenght * ylenght
                    ) + (mz * mz) / (
                        zlenght * zlenght
                    ) <= 1:  # valid position
                        # if (x+dx, y+dy, z+dz) in chunkprovider.generationcache["blocks"] and \
                        #        chunkprovider.generationcache["blocks"][(x + dx, y + dy, z + dz)] in \
                        #        self.getReplaceAbleBlocks(self):
                        cx, _, cz = mathhelper.sectorize((x + dx, 0, z + dz))
                        chunkprovider = chunkprovider.worldprovider.getChunkProviderFor(
                            (cx, cz)
                        )
                        if chunkprovider.generated:
                            chunkprovider.generationcache["blocks"][
                                (x + dx, y + dy, z + dz)
                            ] = self.getOreName(self)

    def getOreName(self):
        return ""

    def getMinSize(self):
        return 1

    def getMaxSize(self):
        return 5

    def getChunkAmount(self):
        return 0

    def getReplaceAbleBlocks(self):
        return ["minecraft:stone"]


class CoalOre(BaseOreVein):
    def getOreName(self):
        return "minecraft:coal_ore"

    def getMinSize(self):
        return 0

    def getMaxSize(self):
        return 64

    def getChunkAmount(self):
        return 10
