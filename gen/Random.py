"""
main system for random
"""

import math
import random, pickle


class Random:
    def __init__(self, seed):
        self.seed = int(seed)
        self.pmap = {}

    def generateValueForPosition(self, pos, MIN, MAX):
        x, y, z = pos
        if not (x, y, z) in self.pmap: self.pmap[(x, y, z)] = self.seed * x * y * z
        random.seed(self.pmap[(x, y, z)])
        try:
            v = random.randint(round(MIN), round(MAX))
        except:
            print(round(MIN), round(MAX))
            raise
        self.pmap[(x, y, z)] = v
        return v




