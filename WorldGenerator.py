import globals as G
import log
import time
import config
import random
import math
import mathhelper
import cavegenerator

def generateHighModel(sx, sy, ex, ey, thismap, min=10, max=255, rt=1, r=2):
    dt = time.time()
    i = 0
    todo = []
    cm = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for x in range(sx, ex):
        for y in range(sy, ey):
            if not (x, y) in thismap:
                amount = 0
                hights = []
                for e in cm:
                    if (x+e[0], y+e[1]) in thismap:
                        amount += 1
                        hights.append(thismap[(x+e[0], y+e[1])])
                if amount < config.WorldGenerator.GenerateMinTasks and len(thismap) != 0:
                    todo.append((x, y))
                elif len(thismap) == 0:
                    thismap[(x, y)] = random.randint(min, max)
                else: #prepare high data
                    v = 0
                    for e in hights:
                        v += e
                    v0 = random.randint(1, r)
                    while random.randint(0, v0) < math.sqrt(v0) and v > 2:
                        v0 = random.randint(1, r)
                    v1 = random.randint(-1, 0)
                    if v1 == 0: v1 = 1
                    thismap[(x, y)] = round(v / len(hights)) + v0 * v1
                    if thismap[(x, y)] < min:
                        thismap[(x, y)] = min
                    elif thismap[(x, y)] > max:
                        thismap[(x, y)] = max
            if time.time() - dt > 2:
                log.printMSG("[WORLDGENERATOR][HIGHMAP][INFO] generating highmap ("+str(round(i/((ex-sx)*(ey-sy))*100))+"%)")
                dt = time.time()
            i += 1
    l = len(todo)
    i = 0
    while len(todo) > 0:
        if time.time() - dt > 2:
            log.printMSG("[WORLDGENERATOR][HIGHMAP][INFO] generating highmap ("+str(round((i/l)*100))+")")
            dt = time.time()
        i += 1
        (x, y) = todo.pop(0)
        amount = 0
        hights = []
        for e in cm:
            if (x + e[0], y + e[1]) in thismap:
                amount += 1
                hights.append(thismap[(x + e[0], y + e[1])])
        if amount < config.WorldGenerator.GenerateMinTasks and len(thismap) != 0:
            todo.append((x, y))
        elif len(thismap) == 0:
            thismap[(x, y)] = random.randint(min, max)
        else:  # prepare high data
            v = 0
            for e in hights:
                v += e
            v0 = random.randint(1, r)
            while random.randint(0, v0) < math.sqrt(v0) and v > 2:
                v0 = random.randint(1, r)
            v1 = random.randint(-1, 0)
            if v1 == 0: v1 = 1
            thismap[(x, y)] = round(v / len(hights)) + v0 * v1
            if thismap[(x, y)] < min:
                thismap[(x, y)] = min
            elif thismap[(x, y)] > max:
                thismap[(x, y)] = max

def generateHighModelBiome(sx, sy, ex, ey, thismap, rt=1):
    dt = time.time()
    i = 0
    todo = []
    cm = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for x in range(sx, ex):
        for y in range(sy, ey):
            biome = G.BiomeMAP[(x, y)]
            r = biome.getHighDiffrents()
            if not (x, y) in thismap:
                amount = 0
                hights = []
                for e in cm:
                    if (x+e[0], y+e[1]) in thismap:
                        amount += 1
                        hights.append(thismap[(x+e[0], y+e[1])])
                if amount < config.WorldGenerator.GenerateMinTasks and len(thismap) != 0:
                    todo.append((x, y))
                elif len(thismap) == 0:
                    thismap[(x, y)] = random.randint(biome.getMinHigh(), biome.getMaxHigh())
                else: #prepare high data
                    v = 0
                    for e in hights:
                        v += e
                    if rt == 2:
                        thismap[(x, y)] = round(v / len(hights)) + round(random.randint(-10*(r-1)-8, 10*(r-1)+8)/10)
                    else:
                        v0 = random.randint(1, r)
                        while random.randint(0, v0) < math.sqrt(v0) and v > 2:
                            v0 = random.randint(1, r)
                        v1 = random.randint(-1, 0)
                        if v1 == 0: v1 = 1
                        thismap[(x, y)] = round(v / len(hights)) + v0 * v1
                    if thismap[(x, y)] < biome.getMinHigh():
                        thismap[(x, y)] = biome.getMinHigh()
                    elif thismap[(x, y)] > biome.getMaxHigh():
                        thismap[(x, y)] = biome.getMaxHigh()
            if time.time() - dt > 2:
                log.printMSG("[WORLDGENERATOR][HIGHMAP][INFO] generating highmap ("+str(round(i/((ex-sx)*(ey-sy))*100))+"%)")
                dt = time.time()
            i += 1
    while len(todo) > 0:
        if time.time() - dt > 2:
            log.printMSG("[WORLDGENERATOR][HIGHMAP][INFO] generating highmap")
            dt = time.time()
        (x, y) = todo.pop(0)
        amount = 0
        hights = []
        for e in cm:
            if (x + e[0], y + e[1]) in thismap:
                amount += 1
                hights.append(thismap[(x + e[0], y + e[1])])
        if amount < config.WorldGenerator.GenerateMinTasks and len(thismap) != 0:
            todo.append((x, y))
        elif len(thismap) == 0:
            thismap[(x, y)] = random.randint(min, max)
        else:  # prepare high data
            v = 0
            for e in hights:
                v += e
            thismap[(x, y)] = round(v / len(hights)) + round(random.randint(-18, 18)/10)
            if thismap[(x, y)] < min:
                thismap[(x, y)] = min
            elif thismap[(x, y)] > max:
                thismap[(x, y)] = max

def SmoothMap(thismap, sx, sy, ex, ey, prior_1=1):
    cm = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for x in range(sx, ex):
        for y in range(sy, ey):
            sorrounding = []
            for e in cm:
                if (x + e[0], y + e[1]) in thismap:
                    sorrounding.append(thismap[(x+e[0], y+e[1])])
            if prior_1 > 1:
                for _ in range(prior_1-1):
                    sorrounding.append(thismap[(x, y)])
            thismap[(x, y)] = round(sum(sorrounding) / len(sorrounding))

G.generatehighmodel = [generateHighModel, SmoothMap]

def generateArea(sx, sy, ex, ey, pregame=False):
    if G.GAMESTAGE != 2 and not pregame: return
    ex += 1; ey += 1

    i = 0
    m = (ex - sx) * (ey - sy)
    dt = time.time()
    for x in range(sx, ex):
        for z in range(sy, ey):
            if not mathhelper.sectorize((x, 0, z)) in G.GeneratedSectors: G.GeneratedSectors.append(mathhelper.sectorize((x, 0, z)))
            G.BiomeMAP[(x, z)].generatePositions([(x, z)])
            if time.time() - dt > 2:
                log.printMSG("[WORLDGENERATOR][INFO] generating positon "+str((x, z))+" (" + str(round(i/m*100))+"%)")
                dt = time.time()
            i += 1

def generateChunk(cx, cz):
    sx, sy, ex, ey = cx * 16, cz * 16, cx * 16 + 15, cz * 16 + 15
    ex += 1; ey += 1
    generateHighModel(sx, sy, ex, ey, G.TemperaturMAP, min=0, max=100, r=20, rt=2)

    for _ in range(config.WorldGenerator.GenerateTemperaturSmoothTime):
        SmoothMap(G.TemperaturMAP, sx, sy, ex, ey)
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
    generateHighModel(sx, sy, ex, ey, G.HighMAP)
    for _ in range(config.WorldGenerator.GenerateTerrainSmoothTime):
        SmoothMap(G.HighMAP, sx, sy, ex, ey)
    i = 0
    m = (ex - sx) * (ey - sy)
    dt = time.time()
    for x in range(sx, ex):
        for z in range(sy, ey):
            if not mathhelper.sectorize((x, 0, z)) in G.GeneratedSectors: G.GeneratedSectors.append(
                mathhelper.sectorize((x, 0, z)))
            G.BiomeMAP[(x, z)].generatePositions([(x, z)])
            if time.time() - dt > 2:
                log.printMSG(
                    "[WORLDGENERATOR][INFO] generating positon " + str((x, z)) + " (" + str(round(i / m * 100)) + "%)")
                dt = time.time()
            i += 1
    if config.WorldGenerator.GENERATE_PERLIN:
        cavegenerator.generateChunk(cx, cz)

def _generateTasks(pipeIN, pipeOUT):
    while True:
        chunk = pipeIN.get()
        generateChunk(chunk[0], chunk[1])


