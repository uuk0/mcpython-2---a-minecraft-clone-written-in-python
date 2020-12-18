import random
import time
from collections import deque

import pyglet
import pyglet.gl
import pyglet.graphics

import config
import globals as G
import log
import mathhelper
import world.Dimensions as Dimensions

import time


class Model(object):
    """class for model"""

    def __init__(self):

        G.model = self

        # Simple function queue implementation. The queue is populated with
        # _show_block() and _hide_block() calls
        self.queue = deque()

        G.eventhandler.on_event("worldgen:newworld", self._initialize)

    def _initialize(self, *args):
        """Initialize the world by placing all the blocks."""
        log.printMSG("[MAINTHREAD][WINDOW][MODEL][INFO] generating world...")
        import world.OverWorld

        G.dimensionhandler.register(world.OverWorld.OverWorld)

        G.dimensionhandler.dimensions[0].join()

        G.player.dimension = G.dimensionhandler.dimensions[0]

        G.dimensionhandler.prepare()

        G.GAMESTAGE = 3
        self.change_sectors(None, G.window.get_motion_vector())

    def hit_test(self, position, vector, max_distance=8):
        """Line of sight search from current position. If a block is
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
            cx, _, cz = mathhelper.sectorize(key)
            if (
                key != previous
                and key
                in G.player.dimension.worldprovider.getChunkProviderFor((cx, cz)).world
            ):
                return key, previous
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None

    def exposed(self, position):
        """Returns False is given `position` is surrounded on all 6 sides by solid
        blocks, True otherwise.

        """
        bcx, _, bcz = mathhelper.sectorize(position)
        basechunkprovider = G.player.dimension.worldprovider.getChunkProviderFor(
            (bcx, bcz)
        )
        flag1 = basechunkprovider.generated
        x, y, z = position
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if [dx, dy, dz].count(0) > 1 and not dx == dy == dz == 0:
                        nx, ny, nz = x + dx, y + dy, z + dz
                        cx, _, cz = mathhelper.sectorize((nx, ny, nz))
                        chunkprovider = (
                            G.player.dimension.worldprovider.getChunkProviderFor(
                                (cx, cz)
                            )
                        )
                        if (
                            (
                                (nx, ny, nz) not in chunkprovider.world
                                or G.GAMESTAGE != 3
                                or not chunkprovider.world[(nx, ny, nz)].isFullBlock()
                            )
                            and (nx, ny, nz) not in G.BlockGenerateTasks
                        ) and not (flag1 and not chunkprovider.generated):
                            return True
                        else:
                            pass
                            # log.printMSG((nx, ny, nz) not in chunkprovider.world,
                            # mathhelper.sectorize((nx, ny, nz)) in G.player.dimension.worldprovider.chunks,
                            # (nx, ny, nz) not in G.BlockGenerateTasks)
        return False

    def add_block(self, position, texture, immediate=True, blocksettedto=None):
        """Add a block with the given `texture` and `position` to the world.

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
        if position[1] < 0 or position[1] > 255:
            return
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if position in chunkprovider.world:
            self.remove_block(position, immediate)
        if texture in ["air", "minecraft:air"]:
            return
        if not type(texture) == G.blockinst:
            # todo: re-add blocksettedto
            block = G.blockhandler.getInst(
                texture, position
            )  # , blocksettedto=blocksettedto)
        else:
            block = texture
            block.position = position
        if not block:
            return
        chunkprovider.world[position] = block
        if immediate:
            if self.exposed(position):
                self.show_block(position)
            self.check_neighbors(position)
        if G.GAMESTAGE == 3:
            self.block_update(position)

    def remove_block(self, position, immediate=True):
        """Remove the block at the given `position`.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to remove.
        immediate : bool
            Whether or not to immediately remove block from canvas.

        """
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if position not in chunkprovider.world:
            return
        chunkprovider.world[position].delete()
        if immediate:
            if position in chunkprovider.shown:
                self.hide_block(position, chunkprovider.world[position])
            self.check_neighbors(position)
        self.block_update(position)
        del chunkprovider.world[position]

    def block_update(self, position):
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        x, y, z = position
        for dx, dy, dz in config.FACES:
            key = (x + dx, y + dy, z + dz)
            if key in chunkprovider.world:
                chunkprovider.world[key].on_block_update()
        if position in chunkprovider.world:
            chunkprovider.world[position].on_block_update()

    def check_neighbors(self, position):
        """Check all blocks surrounding `position` and ensure their visual
        state is current. This means hiding blocks that are not exposed and
        ensuring that all exposed blocks are shown. Usually used after a block
        is added or removed.

        """
        x, y, z = position
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if [dx, dy, dz].count(0) == 1:
                        key = (x + dx, y + dy, z + dz)
                        cx, _, cz = mathhelper.sectorize(key)
                        chunkprovider = (
                            G.player.dimension.worldprovider.getChunkProviderFor(
                                (cx, cz)
                            )
                        )
                        if key not in chunkprovider.world:
                            continue
                        if not self.exposed(key):
                            self.show_block(position)
                        else:
                            self.hide_block(key, chunkprovider.world[key])

    def show_block(self, position, immediate=True, test=True):
        """Show the block at the given `position`. This method assumes the
        block has already been added with add_block()

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to show.
        immediate : bool
            Whether or not to show the block immediately.

        """
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if not position in chunkprovider.world:
            return
        block = chunkprovider.world[position]
        chunkprovider.shown[position] = block
        if immediate and not (test and not self.exposed(position)):
            self._show_block(position, block)
        elif not immediate and not (test and not self.exposed(position)):
            self._enqueue(self._show_block, position, block)
        # else:
        # log.printMSG(position, self.exposed(position))

    def _show_block(self, position, block):
        """Private implementation of the `show_block()` method.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to show.
        block : an IBlockInstance-object

        """
        block.show()

    def hide_block(self, position, block, immediate=True):
        """Hide the block at the given `position`. Hiding does not remove the
        block from the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position of the block to hide.
        immediate : bool
            Whether or not to immediately remove the block from the canvas.

        """
        cx, _, cz = mathhelper.sectorize(position)
        chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
        if not position in chunkprovider.shown:
            return
        chunkprovider.shown.pop(position)
        if immediate:
            self._hide_block(position, block)
        else:
            self._enqueue(self._hide_block, position, block)

    def _hide_block(self, position, block):
        """Private implementation of the 'hide_block()` method."""
        block.hide()

    def show_sector(self, sector):
        """Ensure all blocks in the given sector that should be shown are
        drawn to the canvas.

        """
        if G.player.dimension:
            chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor(
                (sector[0], sector[2] if len(sector) > 2 else sector[1])
            )
            for position in chunkprovider.world.keys():
                chunkprovider.world[position].show()

    def hide_sector(self, sector):
        """Ensure all blocks in the given sector that should be hidden are
        removed from the canvas.

        """
        if G.player.dimension:
            chunkprovider = G.player.dimension.worldprovider.getChunkProviderFor(
                (sector[0], sector[2] if len(sector) > 2 else sector[1])
            )
            for position in chunkprovider.world.keys():
                chunkprovider.world[position].hide()

    def change_sectors(self, before, after):
        """Move from sector `before` to sector `after`. A sector is a
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
        if not after:
            after = mathhelper.sectorize(G.window.position)
        sector = after

    def _enqueue(self, func, *args):
        """Add `func` to the internal queue."""
        self.queue.append((func, args))

    def _dequeue(self):
        """Pop the top function from the internal queue and call it."""
        func, args = self.queue.popleft()
        func(*args)

    def process_queue(self):
        """Process the entire queue while taking periodic breaks. This allows
        the game loop to run smoothly. The queue contains calls to
        _show_block() and _hide_block() so this method should be called if
        add_block() or remove_block() was called with immediate=False

        """
        start = time.time()
        while self.queue and time.time() - start < 1.0 / config.Physiks.TICKS_PER_SEC:
            self._dequeue()

    def process_entire_queue(self):
        """Process the entire queue with no breaks."""
        while self.queue:
            self._dequeue()

    def clear(self):
        self.change_sectors(G.window.get_motion_vector(), None)
        for chunkprovider in G.player.dimension.worldprovider.chunkproviders.values():
            for e in chunkprovider.world.copy().keys():
                self.remove_block(e, immediate=True)
        G.entityhandler.entitys = []
        G.scoreboardhandler.clear()
        G.eventhandler.call("core:model:cleanup")
