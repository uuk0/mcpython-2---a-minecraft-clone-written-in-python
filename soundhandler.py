import random

import pyglet

import globals as G

"""handler for sounds"""


class SoundHandler:
    def __init__(self):
        self.sounds = {}

    """loads a sound to memory"""

    def loadSound(self, file):
        G.eventhandler.call("game:registry:on_sound_registrated", file)
        if type(file) == list:
            for e in file:
                self.loadSound(e)
            return
        if file in self.sounds:
            return
        try:
            self.sounds[file] = pyglet.media.load(file, streaming=False)
        except:
            pass

    """play an sound"""

    def playSound(self, position, file):
        if type(file) == list:
            file = random.choice(file)
        try:
            self.sounds[file].play()
        except KeyError:
            pass


G.soundhandler = SoundHandler()
