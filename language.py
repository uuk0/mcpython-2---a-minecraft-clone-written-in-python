import json
import os

import config
import globals as G
import log


def _decodeJSON(file):
    with open(file) as f:
        return json.load(f)


def _decodeOLD(file):
    with open(file, mode="rb") as f:
        raw = f.read()
    raw = raw.decode()
    data = {}
    for line in raw.split("\n"):
        if not line.startswith("#") and line.count("=") > 0:
            data[line.split("=")[0]] = line.split("=")[1]
    return data


class LanguageExtension:
    def __init__(self, file, format="old"):
        if format == "old":
            self.data = _decodeOLD(file)
        elif format == "json":
            self.data = _decodeJSON(file)
        else:
            log.printMSG(
                "[LANGUAGE][ERROR] can't load lang extension file " + str(file)
            )
            self.data = {}
        self.name = file.split("/")[-1].split(".")[0]
        if hasattr(G.LANG, self.name):
            getattr(G.LANG, self.name)._applyExtenstion(self)
        else:
            setattr(
                G.LANG,
                file.split("/")[-1].split(".")[0],
                LanguageFile(file, format="old"),
            )

    @staticmethod
    def applyFromDir(d):
        for file in os.listdir(d):
            if os.path.isfile(d + "/" + file):
                LanguageExtension(d + "/" + file)


class LanguageFile:
    def __init__(self, file, format="json"):
        if format == "old":
            self.data = _decodeOLD(file)
        elif format == "json":
            self.data = _decodeJSON(file)
        else:
            log.printMSG("[LANGUAGE][ERROR] can't load lang file " + str(file))
        G.eventhandler.call("game:registry:on_language_registered", self)

    def _applyExtenstion(self, ext):
        for key in ext.data:
            self.data[key] = ext.data[key]


for e in os.listdir(G.local + "/lang"):
    setattr(G.LANG, e.split(".")[0], LanguageFile(G.local + "/lang/" + e))

G.LANG.active = getattr(G.LANG, config.LANGUAGE_NAME)
