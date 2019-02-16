import globals as G
import mathhelper
import modsystem.ModLoader


class WhiteWool(G.blockclass):
    """class for white wool"""
    def getName(self):
        return "minecraft:white_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class OrangeWool(G.blockclass):
    """class for orange wool"""
    def getName(self):
        return "minecraft:orange_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class magentaWool(G.blockclass):
    """class for magenta wool"""
    def getName(self):
        return "minecraft:magenta_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class light_blueWool(G.blockclass):
    """class for light blue wool"""
    def getName(self):
        return "minecraft:light_blue_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_light_blue"


class yellowWool(G.blockclass):
    """class for yellow wool"""
    def getName(self):
        return "minecraft:yellow_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class limeWool(G.blockclass):
    """class for lime wool"""
    def getName(self):
        return "minecraft:lime_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class pinkWool(G.blockclass):
    """class for pink wool"""
    def getName(self):
        return "minecraft:pink_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class grayWool(G.blockclass):
    """class for gray wool"""
    def getName(self):
        return "minecraft:gray_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class light_grayWool(G.blockclass):
    """class for light gray wool"""
    def getName(self):
        return "minecraft:light_gray_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_light_gray"


class cyanWool(G.blockclass):
    """class for cyan wool"""
    def getName(self):
        return "minecraft:cyan_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class purpleWool(G.blockclass):
    """class for purple wool"""
    def getName(self):
        return "minecraft:purple_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class blueWool(G.blockclass):
    """class for blue wool"""
    def getName(self):
        return "minecraft:blue_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class brownWool(G.blockclass):
    """class for brown wool"""
    def getName(self):
        return "minecraft:brown_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class greenWool(G.blockclass):
    """class for green wool"""
    def getName(self):
        return "minecraft:green_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class redWool(G.blockclass):
    """class for red wool"""
    def getName(self):
        return "minecraft:red_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


class blackWool(G.blockclass):
    """class for black wool"""
    def getName(self):
        return "minecraft:black_wool"

    def getModelFile(self, inst):
        return "minecraft:wool"

    def getStateName(self, inst):
        return "wool_"+str(self.getName().split(":")[1].split("_")[0])


@modsystem.ModLoader.ModEventEntry("game:registry:on_block_registrate_periode", "minecraft",
                                   info="registrating wool")
def register():
    G.blockhandler.register(blackWool)
    G.blockhandler.register(redWool)
    G.blockhandler.register(greenWool)
    G.blockhandler.register(brownWool)
    G.blockhandler.register(blueWool)
    G.blockhandler.register(purpleWool)
    G.blockhandler.register(cyanWool)
    G.blockhandler.register(light_grayWool)
    G.blockhandler.register(grayWool)
    G.blockhandler.register(pinkWool)
    G.blockhandler.register(limeWool)
    G.blockhandler.register(yellowWool)
    G.blockhandler.register(light_blueWool)
    G.blockhandler.register(magentaWool)
    G.blockhandler.register(OrangeWool)
    G.blockhandler.register(WhiteWool)

