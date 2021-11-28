import noise as _noise

import globals as G


def noise(x, y, z, freq=30, level=1):
    return abs(_noise.pnoise3(x / freq, y / freq + level * G.seed, z / freq))
