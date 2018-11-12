import mathhelper
import globals as G
import random

class OreGenerator:
    def __init__(self):
        self.ores = []
        self.chunkhandler = {}

    def addOre(self, blockname, minhigh, maxhigh, amountavg, amountrange, sizeavg, sizerange, randomamount):
        self.ores.append([blockname, minhigh, maxhigh, amountavg, amountrange, sizeavg, sizerange,
                          randomamount])

    def generateOre(self, position):
        if len(self.ores) == 0: return False
        chunk = mathhelper.sectorize(position)
        if not chunk in self.chunkhandler:
            self.chunkhandler[chunk] = []
            for e in self.ores:
                amount = random.randint(e[3]-e[4], e[3]+e[4])
                if amount == 0: amount = 1
                self.chunkhandler[chunk].append([0, amount,
                                                 random.randint(e[5]-e[6], e[5]+e[6])])
        indexes = []
        for i, e in enumerate(self.ores):
            if self.chunkhandler[chunk][0] <= self.chunkhandler[chunk][1] and position[1] >= e[1] and position[1] <= e[2]:
                indexes.append(i)
        if len(indexes) < 0: return False
        for e in indexes:
            if random.randint(0, self.ores[e][7]) != 0: return False
        if len(indexes) == 0: return False
        oreindex = random.choice(indexes)
        self.chunkhandler[chunk][oreindex][0] += 1

        positions = [position]
        amount = 0
        while len(positions) > 0:
            x, y, z = pos = positions.pop(0)
            #G.model.add_block(pos, self.ores[oreindex][0], immediate=False)
            G.BlockGenerateTasks.append([0, pos, self.ores[oreindex][0]])
            amount += 1
            if amount + len(positions) >= self.chunkhandler[chunk][oreindex][2]:
                positions = []
            elif random.randint(1, 5) == 1:
                positions.append((x+1, y, z))
            elif random.randint(1, 5) == 1:
                positions.append((x-1, y, z))
            elif random.randint(1, 5) == 1:
                positions.append((x, y+1, z))
            elif random.randint(1, 5) == 1:
                positions.append((x, y-1, z))
            elif random.randint(1, 5) == 1:
                positions.append((x, y, z+1))
            elif random.randint(1, 5) == 1:
                positions.append((x, y, z-1))
        return (amount, position, oreindex, self.ores[oreindex])