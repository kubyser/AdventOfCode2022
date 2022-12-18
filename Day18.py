rock = {}
pockets = {}
nextPocketNum = 0


def setPocket(pos, pocketNum):
    global rock
    global pockets
    rock[pos] = pocketNum
    if pocketNum in pockets:
        pockets[pocketNum].add(pos)
    else:
        pockets[pocketNum] = {pos}


def removePocket(pocketNum):
    global rock
    global pockets
    for pos in pockets[pocketNum]:
        rock.pop(pos)
    pockets.pop(pocketNum)


def mergePockets(newPocket, oldPocket):
    global rock
    global pockets
    for pos in pockets[oldPocket]:
        pockets[newPocket].add(pos)
        rock[pos] = newPocket
    pockets.pop(oldPocket)


f = open("resources/day18_input.txt", "r")
lines = f.read().splitlines()
f.close()
lava = {}
minPos = [int(x) for x in lines[0].split(",")]
maxPos = [int(x) for x in lines[0].split(",")]
dc = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
for line in lines:
    pos = [int(x) for x in line.split(",")]
    lava[(pos[0], pos[1], pos[2])] = 6
    if pos[0] < minPos[0]:
        minPos[0] = pos[0]
    if pos[1] < minPos[1]:
        minPos[1] = pos[1]
    if pos[2] < minPos[2]:
        minPos[2] = pos[2]
    if pos[0] > maxPos[0]:
        maxPos[0] = pos[0]
    if pos[1] > maxPos[1]:
        maxPos[1] = pos[1]
    if pos[2] > maxPos[2]:
        maxPos[2] = pos[2]
total = 0
for d in lava:
    count = lava[d]
    for diff in dc:
        if (d[0]+diff[0], d[1]+diff[1], d[2]+diff[2]) in lava:
            count -= 1
    lava[d] = count
    total += count
print("Total sides:", total)

for x in range(minPos[0]-1, maxPos[0]+2):
    for y in range(minPos[1]-1, maxPos[1]+2):
        for z in range(minPos[2]-1, maxPos[2]+2):
            if (x, y, z) in lava:
                continue
            curPocket = -1
            if (x-1, y, z) in rock:
                curPocket = rock[(x-1, y, z)]
                setPocket((x, y, z), curPocket)
            if (x, y-1, z) in rock:
                if curPocket == -1:
                    curPocket = rock[(x, y-1, z)]
                    setPocket((x, y, z), curPocket)
                elif curPocket != rock[(x, y-1, z)]:
                    mergePockets(curPocket, rock[(x, y-1, z)])
            if (x, y, z-1) in rock:
                if curPocket == -1:
                    curPocket = rock[(x, y, z-1)]
                    setPocket((x, y, z), curPocket)
                elif curPocket != rock[(x, y, z-1)]:
                    mergePockets(curPocket, rock[(x, y, z-1)])
            if curPocket == -1:
                curPocket = nextPocketNum
                nextPocketNum += 1
                setPocket((x, y, z), curPocket)
removePocket(rock[minPos[0]-1, minPos[1]-1, minPos[2]-1])
numPockets = len(pockets)
print("Number of pockets:", numPockets)
for d in lava:
    count = lava[d]
    for diff in dc:
        if (d[0]+diff[0], d[1]+diff[1], d[2]+diff[2]) in rock:
            total -= 1
print("Total external sides:", total)


