import pyglet
import globals as G
import random

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
        if file in self.sounds: return
        self.sounds[file] = pyglet.media.load(file, streaming=False)

    """play an sound"""
    def playSound(self, position, file):
        if type(file) == list:
            file = random.choice(file)
        self.sounds[file].play()

G.soundhandler = SoundHandler()