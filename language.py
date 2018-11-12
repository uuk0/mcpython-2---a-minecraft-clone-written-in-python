import globals as G
import json
import os
import config

class LanguageFile:
    def __init__(self, file):
        with open(file) as f:
            self.data = json.load(f)
        G.eventhandler.call("game:registry:on_language_registered", self)

for e in os.listdir(G.local+"lang"):
    setattr(G.LANG, e.split(".")[0], LanguageFile(G.local+"lang/"+e))

G.LANG.active = getattr(G.LANG, config.LANGUAGE_NAME)