import math
import time

import pyglet

import config
import globals as G
import log
import mathhelper
import player
import world.model as model


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        G.window = self

        # Whether or not the window exclusively captures the mouse.
        self.exclusive = False

        # When flying gravity has no effect and speed is increased.
        self.flying = False

        # Strafing is moving lateral to the direction you are facing,
        # e.g. moving to the left or right while continuing to face forward.
        #
        # First element is -1 when moving forward, 1 when moving back, and 0
        # otherwise. The second element is -1 when moving left, 1 when moving
        # right, and 0 otherwise.
        self.strafe = [0, 0]

        # Current (x, y, z) position in the world, specified with floats. Note
        # that, perhaps unlike in math class, the y-axis is the vertical axis.
        self.position = (0, 255, 0)

        # First element is rotation of the player in the x-z plane (ground
        # plane) measured from the z-axis down. The second is the rotation
        # angle from the ground plane up. Rotation is in degrees.
        #
        # The vertical plane rotation ranges from -90 (looking straight down) to
        # 90 (looking straight up). The horizontal rotation range is unbounded.
        self.rotation = (0, 0)

        # Which sector the player is currently in.
        self.sector = None

        # The crosshairs at the center of the screen.
        self.reticle = None

        # Velocity in the y (upward) direction.
        self.dy = 0

        # Convenience list of num keys.
        self.num_keys = [
            config.Keyboard.INVENTORY_1,
            config.Keyboard.INVENTORY_2,
            config.Keyboard.INVENTORY_3,
            config.Keyboard.INVENTORY_4,
            config.Keyboard.INVENTORY_5,
            config.Keyboard.INVENTORY_6,
            config.Keyboard.INVENTORY_7,
            config.Keyboard.INVENTORY_8,
            config.Keyboard.INVENTORY_9,
        ]

        log.printMSG("[MAINTHREAD][WINDOW][INFO] creating model...")

        self.size = (800, 600)

        self.worldname = None

        # player instance
        self.player = player.player()

        # Instance of the model that handles the world.
        self.__model = model.Model()

        # minecraft time. value between 0 and 24000
        self.time = 0
        self.day = 1

        # This call schedules the `update()` method to be called
        # TICKS_PER_SEC. This is the main game event loop.
        pyglet.clock.schedule_interval(self.update, 1.0 / config.Physiks.TICKS_PER_SEC)

        # This is the call for TickHandler
        pyglet.clock.schedule_interval(G.tickhandler._tick, 1.0 / 20.0)
        pyglet.clock.schedule_interval(self.eventhandlertick, 1.0 / 20.0)

    def eventhandlertick(self, *args, **kwargs):
        G.eventhandler.call("core:tick", *args, **kwargs)

    def set_exclusive_mouse(self, exclusive):
        """If `exclusive` is True, the game will capture the mouse, if False
        the game will ignore the mouse.

        """
        super(Window, self).set_exclusive_mouse(exclusive)
        self.exclusive = exclusive
        G.eventhandler.call("core:window:on_exclusive_mouse_change", exclusive)

    def get_sight_vector(self):
        """Returns the current line of sight vector indicating the direction
        the player is looking.

        """
        x, y = self.rotation
        # y ranges from -90 to 90, or -pi/2 to pi/2, so m ranges from 0 to 1 and
        # is 1 when looking ahead parallel to the ground and 0 when looking
        # straight up or down.
        m = math.cos(math.radians(y))
        # dy ranges from -1 to 1 and is -1 when looking straight down and 1 when
        # looking straight up.
        dy = math.sin(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * m
        dz = math.sin(math.radians(x - 90)) * m
        return (dx, dy, dz)

    def get_motion_vector(self):
        """Returns the current motion vector indicating the velocity of the
        player.

        Returns
        -------
        vector : tuple of len 3
            Tuple containing the velocity in x, y, and z respectively.

        """
        if any(self.strafe):
            x, y = self.rotation
            strafe = math.degrees(math.atan2(*self.strafe))
            y_angle = math.radians(y)
            x_angle = math.radians(x + strafe)
            if self.flying:
                m = math.cos(y_angle)
                dy = math.sin(y_angle)
                if self.strafe[1]:
                    # Moving left or right.
                    dy = 0.0
                    m = 1
                if self.strafe[0] > 0:
                    # Moving backwards.
                    dy *= -1
                # When you are flying up or down, you have less left and right
                # motion.
                dx = math.cos(x_angle) * m
                dz = math.sin(x_angle) * m
            else:
                dy = 0.0
                dx = math.cos(x_angle)
                dz = math.sin(x_angle)
        else:
            dy = 0.0
            dx = 0.0
            dz = 0.0
        return (dx, dy, dz)

    def update(self, dt):
        """This method is scheduled to be called repeatedly by the pyglet
        clock.

        Parameters
        ----------
        dt : float
            The change in time since the last call.

        """
        G.model.process_queue()
        sector = mathhelper.sectorize(self.position)
        if (
            sector != self.sector
            and G.statehandler.active_state.getName() == "minecraft:game"
        ):
            G.model.change_sectors(self.sector, sector)
            if self.sector is None:
                G.model.process_entire_queue()
            self.sector = sector
        m = 8
        dt = min(dt, 0.2)
        for _ in range(m):
            self._update(dt / m)
        for entity in G.entityhandler.entitys:
            entity.update(dt)
        G.eventhandler.call("core:update")
        if G.statehandler.active_state.getName() == "minecraft:game":
            self.time += dt * 20
            self.day += round(self.time // 24000)
            self.time = round(self.time % 24000)
        if G.GAMESTAGE != 3:
            return
        i = 0
        max = len(G.BlockGenerateTasks)
        l = list(G.BlockGenerateTasks.keys())
        t = time.time()
        for position in l:
            G.model.add_block(
                position, G.BlockGenerateTasks[position][0], immediate=True
            )
            task = G.BlockGenerateTasks[position]
            if len(task) > 1:
                task = task[1:]
                while len(task) > 0:
                    st = task.pop(0)
                    cx, _, cz = mathhelper.sectorize(position)
                    chunkprovider = (
                        G.player.dimension.worldprovider.getChunkProviderFor((cx, cz))
                    )
                    if st == "sdata":
                        chunkprovider.world[position].setStorageData(task.pop(0))
                    else:
                        log.printMSG("[TASKS][ERROR] unknown subtask " + str(st))
            del G.BlockGenerateTasks[position]
            if time.time() - t > 0.1:
                return

    def _update(self, dt):
        """Private implementation of the `update()` method. This is where most
        of the motion logic lives, along with gravity and collision detection.

        Parameters
        ----------
        dt : float
            The change in time since the last call.

        """
        # walking
        speed = (
            config.Physiks.FLYING_SPEED if self.flying else config.Physiks.WALKING_SPEED
        )
        d = dt * speed  # distance covered this tick.
        dx, dy, dz = self.get_motion_vector()
        # New position in space, before accounting for gravity.
        dx, dy, dz = dx * d, dy * d, dz * d
        # gravity
        if (
            not self.flying
            and G.statehandler.active_state == G.statehandler.states["minecraft:game"]
        ):
            # Update your vertical speed: if you are falling, speed up until you
            # hit terminal velocity; if you are jumping, slow down until you
            # start falling.
            self.dy -= dt * config.Physiks.GRAVITY
            self.dy = max(self.dy, -config.Physiks.TERMINAL_VELOCITY)
            dy += self.dy * dt
        # collisions
        x, y, z = self.position
        if G.player.gamemode != 3:
            x, y, z = self.collide((x + dx, y + dy, z + dz), config.PLAYER_HEIGHT)
        else:
            x, y, z = x + dx, y + dy, z + dz
        self.position = (x, y, z)

    def collide(self, position, height):
        """Checks to see if the player at the given `position` and `height`
        is colliding with any blocks in the world.

        Parameters
        ----------
        position : tuple of len 3
            The (x, y, z) position to check for collisions at.
        height : int or float
            The height of the player.

        Returns
        -------
        position : tuple of len 3
            The new position of the player taking into account collisions.

        """
        return position

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when a mouse button is pressed. See pyglet docs for button
        amd modifier mappings.

        Parameters
        ----------
        x, y : int
            The coordinates of the mouse click. Always center of the screen if
            the mouse is captured.
        button : int
            Number representing mouse button that was clicked. 1 = left button,
            4 = right button.
        modifiers : int
            Number representing any modifying keys that were pressed when the
            mouse button was clicked.

        """
        G.eventhandler.call("core:window:on_mouse_press", x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        G.eventhandler.call("core:window:on_mouse_release", x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        """Called when the player moves the mouse.

        Parameters
        ----------
        x, y : int
            The coordinates of the mouse click. Always center of the screen if
            the mouse is captured.
        dx, dy : float
            The movement of the mouse.

        """
        G.eventhandler.call("core:window:on_mouse_motion", x, y, dx, dy)

    def on_key_press(self, symbol, modifiers):
        """Called when the player presses a key. See pyglet docs for key
        mappings.

        Parameters
        ----------
        symbol : int
            Number representing the key that was pressed.
        modifiers : int
            Number representing any modifying keys that were pressed.

        """
        G.eventhandler.call("core:window:on_key_press", symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        """Called when the player releases a key. See pyglet docs for key
        mappings.

        Parameters
        ----------
        symbol : int
            Number representing the key that was pressed.
        modifiers : int
            Number representing any modifying keys that were pressed.

        """
        G.eventhandler.call("core:window:on_key_release", symbol, modifiers)

    def on_resize(self, width, height):
        """Called when the window is resized to a new `width` and `height`."""
        G.eventhandler.call("core:window:on_resize", width, height)
        self.size = (width, height)

    def on_close(self):
        G.eventhandler.call("core:window:on_close")
        self.close()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        G.eventhandler.call("core:window:on_mouse_scroll", x, y, scroll_x, scroll_y)

    def set_2d(self):
        """Configure OpenGL to draw in 2d."""
        width, height = self.get_size()
        pyglet.gl.glDisable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glOrtho(0, width, 0, height, -1, 1)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glLoadIdentity()

    def set_3d(self):
        """Configure OpenGL to draw in 3d."""
        width, height = self.get_size()
        pyglet.gl.glEnable(pyglet.gl.GL_DEPTH_TEST)
        pyglet.gl.glViewport(0, 0, width, height)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
        pyglet.gl.glLoadIdentity()
        pyglet.gl.gluPerspective(65.0, width / float(height), 0.1, 60.0)
        pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
        pyglet.gl.glLoadIdentity()
        x, y = self.rotation
        pyglet.gl.glRotatef(x, 0, 1, 0)
        pyglet.gl.glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
        x, y, z = self.position
        pyglet.gl.glTranslatef(-x, -y, -z)

    def on_draw(self):
        """Called by pyglet to draw the canvas."""
        self.clear()
        self.set_3d()
        G.eventhandler.call("opengl:draw3d")
        self.set_2d()
        G.eventhandler.call("opengl:draw2d")
