import globals as G

"""handler for multiblockstructurs"""
class MultiBlockHandler:
    def __init__(self):
        self.multiblocks = {}
        self.usedblocks = {}
        self.usedbymulti = {}
        G.eventhandler.call("game:registry:on_multiblockstructurs_registrated", self)

    """register an multiblockstructur"""
    def register(self, multiblock):
        name = multiblock.getName(None)
        self.multiblocks[name] = multiblock
        for e in multiblock.getUsedBlocks(None):
            if not e in self.usedblocks: self.usedblocks[e] = []
            self.usedblocks[e].append(name)

    def check_add(self, name, vector, block, previous, blockname):
        if G.model.world[previous].getName() in self.usedblocks:
            for e in self.usedblocks[G.model.world[previous].getName()]:
                self.checkfront(e, previous, G.model.world[previous].getName())
        for e in G.model.world[previous].multiblockstructurlist:
            self.checkactive(e)

    def check_remove(self, name, vector, block, previous, drops):
        if block in self.usedbymulti:
            for e in self.usedbymulti[block]:
                self.checkactive(e)

    def checkfront(self, multiblock, blockfrompos, blockname):
        (x, y, z) = blockfrompos
        blocks = multiblock.getStructur(None)
        for block in blocks.keys():
            if blocks[block] == blockname:
                (xr, yr, zr) = block
                if self._isMultiBlock((x-xr, y-yr, z-zr), multiblock):
                    self.multiblock[(x-xr, y-yr, z-zr)] = multiblock((x-xr, y-yr, z-zr))
                    return

    def checkactive(self, multiblock):
        if not self._isMultiBlock(multiblock.position, multiblock):
            multiblock.on_delet()
            del self.multiblock[multiblock.position]

    def _isMultiBlock(self, position, klass):
        if issubclass(klass, MultiBlockHandler): klass = klass((0, 0, 0))
        blocks = klass.getStructur()
        for rpos in blocks.keys():
            npos = (rpos[0]+position[0], rpos[1]+position[1], rpos[2]+position[2])
            if not (npos not in G.model.world and blocks[rpos] in [None, "air", "minecraft:air"]): return False
            if G.model.world[npos].getName() != blocks[rpos]: return False
        return True

G.multiblockhandler = MultiBlockHandler()
G.eventhandler.on_event("game:on_block_add_by_player", G.multiblockhandler.check_add)
G.eventhandler.on_event("game:on_block_remove_by_player", G.multiblockhandler.check_remove)


"""class for multiblockstructurs"""
class MultiBlockStructur:
    def __init__(self, position):
        self.position = position
        self.on_creat()

    """callen when the multiblock is fullfilled"""
    def on_creat(self):
        pass

    """callen when the multiblock is deleted"""
    def on_delet(self):
        pass

    """returns the structur of the structur"""
    def getStructur(self):
        return {}

    """returns a list of all used blocks"""
    def getUsedBlocks(self):
        return []

    """returns the name of the structur"""
    def getName(self):
        return "minecraft:none"