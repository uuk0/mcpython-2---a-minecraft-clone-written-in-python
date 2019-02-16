import globals as G
import json


class ModelEntry:
    FULL_BLOCK = "cube:full"

    def __init__(self, name):
        self.name = name
        self.modeltype = self.FULL_BLOCK
        self.extradata = []
        self.relativeinfo = True

    def compile(self):
        data = {"blockname": self.name,
                "name": self.modeltype,
                "side_texture_files": self.extradata[0],
                "side_indexes": self.extradata[1],
                "relative_index": self.relativeinfo}
        return data

    @staticmethod
    def simplified_manager_1_for_full_block(name, sidefiles):
        modelentry = ModelEntry(name)
        indextable = {}  # file -> index
        index = 0
        for i, file in enumerate(sidefiles):
            if not file in indextable:
                indextable[file] = index
                index += 1
        modelentry.extradata = [list(indextable.keys()), [indextable[x] for x in sidefiles]]
        return modelentry


class ModelHelper:
    def __init__(self, addressname):
        self.addressname = addressname
        self.__created = False
        self.__modes = []

    def add_entry(self, name):
        self.__modes.append(ModelEntry(name))
        return self.__modes[-1]

    def add_extisting_entry(self, entry):
        self.__modes.append(entry)

    def create(self):
        if self.__created: return
        self.__created = True
        path = G.local+sum(["/"+e for e in self.addressname.split(":")])
        data = {"blockaddress":self.addressname}
        for modelentry in self.__modes:
            data[modelentry.name] = modelentry.compile()
        with open(path, mode="w") as f:
            json.dump(data, f)

