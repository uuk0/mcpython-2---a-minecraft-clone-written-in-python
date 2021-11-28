import log

log.printMSG("[CONSTANTLOADER][INFO] loading constants...")

import math

import globals as G

DEFAULT_GAMEMODE = 1

SKIN = 0  # 0: steve, 1: alex


class DEBUG:
    PRINT_CRAFTING_STUFF = False
    PRINT_BLOCK_REGISTRATING = False
    PRINT_TEXTURDATAHANDLER_STUFF = False
    PRINT_MODLOADING_FORMAT_STUFF = False


class Physiks:
    TICKS_PER_SEC = 60

    # Size of sectors used to ease block loading.
    SECTOR_SIZE = 16

    WALKING_SPEED = 5
    FLYING_SPEED = 15

    GRAVITY = 20.0
    MAX_JUMP_HEIGHT = 1.0  # About the height of a block.
    # To derive the formula for calculating jump speed, first solve
    #    v_t = v_0 + a * t
    # for the time at which you achieve maximum height, where a is the acceleration
    # due to gravity and v_t = 0. This gives:
    #    t = - v_0 / a
    # Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
    #    s = s_0 + v_0 * t + (a * t^2) / 2
    JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
    TERMINAL_VELOCITY = 50

    MOUSE_REAKTION = 0.15


PLAYER_HEIGHT = 2

FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]

FACENAMES = ["U", "D", "S", "N", "E", "W"]
INVERTEDFACENAMES = ["D", "U", "N", "S", "W", "E"]

LANGUAGE_NAME = "en_us"


class AdvancedVanilla:
    class RECIPIS:
        GRASS_TO_DIRT = True
        DIRT_TO_GRASS = False

    START_INVENTORY = {}


class WorldGenerator:
    USED_DEBUG_GEN = False

    GenerateTerrainSmoothTime = 10
    GenerateTemperaturSmoothTime = 3
    GenerateBiomeSmoothTime = 3

    WorldSize = [(-1, -1), (2, 2)]

    # MIN_CAVE_ENTRYS_PER_CHUNK = 3
    # MAX_CAVE_ENTRYS_PRE_CHUNK = 10

    # PERLIN_MAX_POSITION_RANGE = 8
    # PERLIN_MAX_SIZE_RANGE = 1

    # PERLIN_MAX_SIZE = 5

    # PERLIN_SCALE = 4.0
    # PERLIN_OKTAVES = 10
    # PERLIN_PERSISTENCE = 0.5
    # PERLIN_LACUNARITY = 2.0

    # GENERATE_PERLIN = False


class SlotConfig:
    # Slot Image size definition
    ImageSize = [75, 75]
    # how much it should be moved
    ImagePreMove = [-15, -15]


from pyglet.window import key


class Keyboard:
    INVENTORY_1 = key._1
    INVENTORY_2 = key._2
    INVENTORY_3 = key._3
    INVENTORY_4 = key._4
    INVENTORY_5 = key._5
    INVENTORY_6 = key._6
    INVENTORY_7 = key._7
    INVENTORY_8 = key._8
    INVENTORY_9 = key._9
    WALK_FORWARD = key.W
    WALK_BACKWARD = key.S
    WALK_LEFT = key.A
    WALK_RIGHT = key.D
    JUMP = key.SPACE
    CLOSE = key.ESCAPE
    RUN_COMMAND = key.ENTER
    TOGGLE_FLYING = key.TAB
    OPEN_INVENTORY = key.E
    OPEN_CHAT = key.T
