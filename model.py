import random
import time
from collections import deque

import pyglet
import pyglet.gl
import pyglet.graphics

import WorldGenerator
import config
import globals as G
import log
import mathhelper

"""class for model"""
class Model(object):
    def __init__(self):

        G.model = self

        # A Batch is a collection of vertex lists for batched rendering.
        self.batch = pyglet.graphics.Batch()

        # A mapping from position to the texture of the block at that position.
        # This defines all the blocks that are currently in the world.
        self.world = {}

        # Same mapping as `world` but only contains blocks that are shown.
        self.shown = {}

        # Mapping from position to a pyglet `VertextList` for all shown blocks.
        self._shown = {}

        # Mapping from sector to a list of positions inside that sector.
        self.sectors = {}

        # Simple function queue implementation. The queue is populated with
        # _show_block() and _hide_block() calls
        self.queue = deque()

        G.eventhandler.on_event("worldgen:newworld", self._initialize)

        G.eventhandler.call("worldgen:newworld")
        G.GAMESTAGE = 3

    def _initialize(self, *args):
        """ Initialize the world by placing all the blocks.

        """
        log.printMSG("[MAINTHREAD][WINDOW][MODEL][INFO] generating world...")
        WorldGenerator.generateHighModel(-64, -64, 64, 64, G.TemperaturMAP, min=0, max=100, r=20, rt=2)
        for _ in range(config.WorldGenerator.GenerateTemperaturSmoothTime):
            WorldGenerator.SmoothMap(G.TemperaturMAP, -64, -64, 64, 64)
        sx, sy, ex, ey = -64, -64, 64, 64
        cm = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for x in range(sx, ex):
            for z in range(sy, ey):
                biomes = G.biomehandler.getPossibleByTemperatur(G.TemperaturMAP[(x, z)])
                surrounding = []
                for e in cm:
                    if (x + e[0], z + e[1]) in G.BiomeMAP and G.BiomeMAP[(x + e[0], z + e[1])] not in surrounding:
                        surrounding.append(G.BiomeMAP[(x + e[0], z + e[1])])
                items = []
                for e in surrounding:
                    if type(e) in biomes:
                        items.append(e)
                if len(surrounding) > 0:
                    l = [biome.getChangeValue() for biome in surrounding]
                    s = round(sum(l) / len(l))
                if len(items) > 0 and random.randint(1, s) in random.choice(items).getChangeValues():
                    G.BiomeMAP[(x, z)] = random.choice(items)
                else:
                    G.BiomeMAP[(x, z)] = random.choice(biomes)()
        WorldGenerator.generateHighModel(sx, sy, ex, ey, G.HighMAP)
        for _ in range(config.WorldGenerator.GenerateTerrainSmoothTime):
            WorldGenerator.SmoothMap(G.HighMAP, sx, sy, ex, ey, prior_1=config.WorldGenerator.PRIORITY_HIGHMAP_SELF)

        WorldGenerator.generateChunk(0, 0)
        lenght = len(G.BlockGenerateTasks)

        for x in range(-1, 2):
            for z in range(-1, 2):
                if (x, z) != (0, 0):
                    WorldGenerator.generateChunk(x, z)
        dt = time.time()
        i = 0
        l = lenght
        for _ in range(lenght):
            task = G.BlockGenerateTasks.pop(0)
            if task[0] == 0:
                G.model.add_block(*task[1:], immediate=False)
            elif task[0] == 1:
                task[1](*task[2], **task[3])
            elif task[0] == 2:
                G.model.remove_block(*task[1:], immediate=task[1][1] >= G.HighMAP[(task[1][0], task[1][2])])
            else:
                log.printMSG("[MAINTHREAD][TASKS][ERROR] can't execute task named " + str(task))
            if time.time() - dt > 2:
                dt = time.time()
                log.printMSG("[MAINTHREAD][TASKS] executing task " + str(i) + " (" + str(round((i / l) * 100)) + "%)")
            i += 1

    def hit_test(self, position, vector, max_distance=8):
        """ Line of sight search from current position. If a block is
        intersected it is returned, along with the block previously in the line
        of sight. If no block is found, return None, None.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position to check visibility from.
        vector : tuple of len 3
            The line of sight vector.
        max_distance : int
            How many blocks away to search for a hit.

        """
        m = 8
        x, y, z = position
        dx, dy, dz = vector
        previous = None
        for _ in range(max_distance * m):
            key = mathhelper.normalize((x, y, z))
            if key != previous and key in self.world:
                return key, previous
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None

    def exposed(self, position):
        """ Returns False is given `position` is surrounded on all 6 sides by solid
        blocks, True otherwise.

        """
        x, y, z = position
        for i, (dx, dy, dz) in enumerate(config.FACES):
            if (x + dx, y + dy, z + dz) not in self.world:
                return True
            if not self.world[(x+dx, y+dy, z+dz)].isFullSide(config.INVERTEDFACENAMES[i]):
                return True
        return False

    def add_block(self, position, texture, immediate=True, blocksettedto=None):
        """ Add a block with the given `texture` and `position` to the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to add.
        texture : list of len 3
            The coordinates of the texture squares. Use `tex_coords()` to
            generate.
        immediate : bool
            Whether or not to draw the block immediately.

        """
        if position in self.world:
            self.remove_block(position, immediate)
        if texture in ["air", "minecraft:air"]:
            return
        if not type(texture) == G.blockinst:
            block = G.blockhandler.getInst(texture, position, blocksettedto=blocksettedto)
        else:
            block = texture
            block.position = position
        self.world[position] = block
        self.sectors.setdefault(mathhelper.sectorize(position), []).append(position)
        if immediate:
            if self.exposed(position):
                self.show_block(position)
            self.check_neighbors(position)
        self.block_update(position)

    def remove_block(self, position, immediate=True):
        """ Remove the block at the given `position`.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to remove.
        immediate : bool
            Whether or not to immediately remove block from canvas.

        """
        if position not in self.world:
            return
        self.world[position].onDelet()
        del self.world[position]
        self.sectors[mathhelper.sectorize(position)].remove(position)
        if immediate:
            if position in self.shown:
                self.hide_block(position)
            self.check_neighbors(position)
        self.block_update(position)

    def block_update(self, position):
        x, y, z = position
        for dx, dy, dz in config.FACES:
            key = (x + dx, y + dy, z + dz)
            if key in self.world:
                self.world[key].on_block_update()
        if position in self.world:
            self.world[position].on_block_update()

    def check_neighbors(self, position):
        """ Check all blocks surrounding `position` and ensure their visual
        state is current. This means hiding blocks that are not exposed and
        ensuring that all exposed blocks are shown. Usually used after a block
        is added or removed.

        """
        x, y, z = position
        for dx, dy, dz in config.FACES:
            key = (x + dx, y + dy, z + dz)
            if key not in self.world:
                continue
            if self.exposed(key):
                if key not in self.shown:
                    self.show_block(key)
            else:
                if key in self.shown:
                    self.hide_block(key)

    def show_block(self, position, immediate=True):
        """ Show the block at the given `position`. This method assumes the
        block has already been added with add_block()

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to show.
        immediate : bool
            Whether or not to show the block immediately.

        """
        if not position in self.world: return
        texture = self.world[position]
        self.shown[position] = texture
        if immediate:
            self._show_block(position, texture)
        else:
            self._enqueue(self._show_block, position, texture)

    def _show_block(self, position, texture):
        """ Private implementation of the `show_block()` method.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to show.
        texture : list of len 3
            The coordinates of the texture squares. Use `tex_coords()` to
            generate.

        """
        if not position in self.world: return
        if self.world[position].hasExternalDraw():
            self.world[position].show()
            return
        x, y, z = position
        vertex_data = G.model.world[position].getCubeVerticens(
            *list(G.model.world[position].convertPositionToRenderable(position))+[0.5])
        texture_data = list(texture.getTexturData())
        # create vertex list
        # FIXME Maybe `add_indexed()` should be used instead
        if self.world[position].getTexturFile() in G.texturhandler.texturs:
            tex = G.texturhandler.getByName(self.world[position].getTexturFile())
        else:
            tex = G.texturhandler.getByName(G.texturedatahandler.texturs[self.world[position].getTexturFile()])
        self._shown[position] = self.batch.add(24, pyglet.gl.GL_QUADS, tex,
            ('v3f/static', vertex_data),
            ('t2f/static', texture_data))

    def hide_block(self, position, immediate=True):
        """ Hide the block at the given `position`. Hiding does not remove the
        block from the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to hide.
        immediate : bool
            Whether or not to immediately remove the block from the canvas.

        """
        self.shown.pop(position)
        if immediate:
            self._hide_block(position)
        else:
            self._enqueue(self._hide_block, position)

    def _hide_block(self, position):
        """ Private implementation of the 'hide_block()` method.

        """
        if position in self.world and self.world[position].hasExternalDraw():
            self.world[position].hide()
            return
        if position in self._shown:
            self._shown.pop(position).delete()


    def show_sector(self, sector):
        """ Ensure all blocks in the given sector that should be shown are
        drawn to the canvas.

        """
        for position in self.sectors.get(sector, []):
            if position not in self.shown and self.exposed(position):
                if position[1] >= G.HighMAP[(position[0], position[2])]:
                    self.show_block(position, False)
                else:
                    G.BlockGenerateTasks.append([1, self.show_block, [position, False], {}])

    def hide_sector(self, sector):
        """ Ensure all blocks in the given sector that should be hidden are
        removed from the canvas.

        """
        for position in self.sectors.get(sector, []):
            if position in self.shown:
                if (position[0], position[2]) in G.HighMAP and position[1] >= G.HighMAP[(position[0], position[2])]:
                    self.hide_block(position, False)
                else:
                    G.BlockGenerateTasks.append([1, self.hide_block, [position, False], {}])

    def change_sectors(self, before, after):
        """ Move from sector `before` to sector `after`. A sector is a
        contiguous x, y sub-region of world. Sectors are used to speed up
        world rendering.

        """
        before_set = set()
        after_set = set()
        pad = 4
        for dx in range(-pad, pad + 1):
            for dy in [0]:  # range(-pad, pad + 1):
                for dz in range(-pad, pad + 1):
                    if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
                        continue
                    if before:
                        x, y, z = before
                        before_set.add((x + dx, y + dy, z + dz))
                    if after:
                        x, y, z = after
                        after_set.add((x + dx, y + dy, z + dz))
        show = after_set - before_set
        hide = before_set - after_set
        for sector in show:
            self.show_sector(sector)
        for sector in hide:
            self.hide_sector(sector)
        if not after: after = mathhelper.sectorize(G.window.position)
        sector = after
        if not after in G.GeneratedSectors:
            WorldGenerator.generateArea(sector[0] * 16, sector[0] * 16 + 14,
                                        sector[2] * 16, sector[2] * 16 + 14)

    def _enqueue(self, func, *args):
        """ Add `func` to the internal queue.

        """
        self.queue.append((func, args))

    def _dequeue(self):
        """ Pop the top function from the internal queue and call it.

        """
        func, args = self.queue.popleft()
        func(*args)

    def process_queue(self):
        """ Process the entire queue while taking periodic breaks. This allows
        the game loop to run smoothly. The queue contains calls to
        _show_block() and _hide_block() so this method should be called if
        add_block() or remove_block() was called with immediate=False

        """
        start = time.clock()
        while self.queue and time.clock() - start < 1.0 / config.Physiks.TICKS_PER_SEC:
            self._dequeue()

    def process_entire_queue(self):
        """ Process the entire queue with no breaks.

        """
        while self.queue:
            self._dequeue()
