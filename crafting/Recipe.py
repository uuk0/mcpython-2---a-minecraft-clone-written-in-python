"""
main file for recipes
"""
import globals as G


class Recipe:
    def __init__(self, gridname, inputs, outputs, *args, mod="minecraft", **kwargs):
        self.gridname = gridname
        self.inputs = inputs
        self.outputs = outputs
        self.mod = mod
        self.args = args
        self.kwargs = kwargs

