import pyglet

import config
import log

log.printMSG("[MAINTHREAD][INFO] loading math functions...")


def cube_vertices(x, y, z, n):
    """Return the vertices of the cube at position x, y, z with size 2*n."""
    return [
        x - n,
        y + n,
        z - n,
        x - n,
        y + n,
        z + n,
        x + n,
        y + n,
        z + n,
        x + n,
        y + n,
        z - n,  # top
        x - n,
        y - n,
        z - n,
        x + n,
        y - n,
        z - n,
        x + n,
        y - n,
        z + n,
        x - n,
        y - n,
        z + n,  # bottom
        x - n,
        y - n,
        z - n,
        x - n,
        y - n,
        z + n,
        x - n,
        y + n,
        z + n,
        x - n,
        y + n,
        z - n,  # left
        x + n,
        y - n,
        z + n,
        x + n,
        y - n,
        z - n,
        x + n,
        y + n,
        z - n,
        x + n,
        y + n,
        z + n,  # right
        x - n,
        y - n,
        z + n,
        x + n,
        y - n,
        z + n,
        x + n,
        y + n,
        z + n,
        x - n,
        y + n,
        z + n,  # front
        x + n,
        y - n,
        z - n,
        x - n,
        y - n,
        z - n,
        x - n,
        y + n,
        z - n,
        x + n,
        y + n,
        z - n,  # back
    ]


def cube_vertices_2(x, y, z, nx, ny, nz):
    return [
        x - nx,
        y + ny,
        z - nz,
        x - nx,
        y + ny,
        z + nz,
        x + nx,
        y + ny,
        z + nz,
        x + nx,
        y + ny,
        z - nz,  # top
        x - nx,
        y - ny,
        z - nz,
        x + nx,
        y - ny,
        z - nz,
        x + nx,
        y - ny,
        z + nz,
        x - nx,
        y - ny,
        z + nz,  # bottom
        x - nx,
        y - ny,
        z - nz,
        x - nx,
        y - ny,
        z + nz,
        x - nx,
        y + ny,
        z + nz,
        x - nx,
        y + ny,
        z - nz,  # left
        x + nx,
        y - ny,
        z + nz,
        x + nx,
        y - ny,
        z - nz,
        x + nx,
        y + ny,
        z - nz,
        x + nx,
        y + ny,
        z + nz,  # right
        x - nx,
        y - ny,
        z + nz,
        x + nx,
        y - ny,
        z + nz,
        x + nx,
        y + ny,
        z + nz,
        x - nx,
        y + ny,
        z + nz,  # front
        x + nx,
        y - ny,
        z - nz,
        x - nx,
        y - ny,
        z - nz,
        x - nx,
        y + ny,
        z - nz,
        x + nx,
        y + ny,
        z - nz,  # back
    ]


def tex_coord(x, y, n1=4, n2=4):
    """Return the bounding vertices of the texture square."""
    m1 = 1.0 / n1
    m2 = 1.0 / n2
    dx = x * m1
    dy = y * m2
    return dx, dy, dx + m1, dy, dx + m1, dy + m2, dx, dy + m2


def tex_coords(top, bottom, side, n1=1, n2=1):
    """Return a list of the texture squares for the top, bottom and side."""
    top = tex_coord(*top, n1=n1, n2=n2)
    bottom = tex_coord(*bottom, n1=n1, n2=n2)
    side = tex_coord(*side, n1=n1, n2=n2)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result


def text_coords_complex(top, bottom, n, o, s, w, n1=1, n2=1):
    top = tex_coord(*top, n1=n1, n2=n2)
    bottom = tex_coord(*bottom, n1=n1, n2=n2)
    n = tex_coord(*n, n1=n1, n2=n2)
    o = tex_coord(*o, n1=n1, n2=n2)
    s = tex_coord(*s, n1=n1, n2=n2)
    w = tex_coord(*w, n1=n1, n2=n2)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(n)
    result.extend(o)
    result.extend(s)
    result.extend(w)
    return result


def tex_coords_better(
    top,
    bottom,
    n,
    o,
    s,
    w,
    stop=(
        16,
        16,
    ),
    sbottom=(
        16,
        16,
    ),
    sn=(
        16,
        16,
    ),
    so=(
        16,
        16,
    ),
    ss=(
        16,
        16,
    ),
    sw=(
        16,
        16,
    ),
):
    top = tex_coord(*list(top) + list(stop))
    bottom = tex_coord(*list(bottom) + list(sbottom))
    n = tex_coord(*list(n) + list(sn))
    o = tex_coord(*list(o) + list(so))
    s = tex_coord(*list(s) + list(ss))
    w = tex_coord(*list(w) + list(sw))
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(n)
    result.extend(o)
    result.extend(s)
    result.extend(w)
    return result


def normalize(position):
    """Accepts `position` of arbitrary precision and returns the block
    containing that position.

    Parameters
    ----------
    position : tuple of len 3

    Returns
    -------
    block_position : tuple of ints of len 3

    """
    x, y, z = position
    x, y, z = (int(round(x)), int(round(y)), int(round(z)))
    return (x, y, z)


def sectorize(position):
    """Returns a tuple representing the sector for the given `position`.

    Parameters
    ----------
    position : tuple of len 3

    Returns
    -------
    sector : tuple of len 3

    """
    x, y, z = normalize(position)
    x, y, z = (
        x // config.Physiks.SECTOR_SIZE,
        y // config.Physiks.SECTOR_SIZE,
        z // config.Physiks.SECTOR_SIZE,
    )
    return (x, 0, z)


def get_texture_coordinates(x, y, height, width, texture_height, texture_width):
    if x == -1 and y == -1:
        return ()
    x /= float(texture_width)
    y /= float(texture_height)
    height /= float(texture_height)
    width /= float(texture_width)
    return x, y, x + width, y, x + width, y + height, x, y + height


def load_image(path):
    return pyglet.image.load(path)
