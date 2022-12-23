NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3
CHECKS = {NORTH: [(-1, -1), (0, -1), (1, -1)], SOUTH: [(-1, 1), (0, 1), (1, 1)],
          WEST: [(-1, -1), (-1, 0), (-1, 1)], EAST: [(1, -1), (1, 0), (1, 1)]}
MOVES = {NORTH: (0, -1), SOUTH: (0, 1), WEST: (-1, 0), EAST: (1, 0)}
data = set()
prop = {}
firstLookDir = NORTH

def vadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def checkAndPropose(pos):
    global data
    global prop
    global firstLookDir
    lookDir = firstLookDir
    freeDirs = []
    for i in range(4):
        busy = False
        for c in CHECKS[lookDir]:
            cpos = vadd(pos, c)
            if cpos in data:
                busy = True
                break
        if not busy:
            mPos = vadd(pos, MOVES[lookDir])
            freeDirs.append(mPos)
        lookDir = lookDir+1 if lookDir < EAST else NORTH
    if 0 < len(freeDirs) < 4:
        pDir = freeDirs[0]
        if pDir not in prop:
            prop[pDir] = [pos]
        else:
            prop[pDir].append(pos)


f = open("resources/day23_input.txt")
lines = f.read().splitlines()
f.close()
y = 0
for line in lines:
    for x in range(len(line)):
        if line[x] == '#':
            data.add((x, y))
    y += 1
numRounds = 1
# for i in range(numRounds):
while True:
    prop = {}
    moved = False
    for elf in data:
        checkAndPropose(elf)
    for p in prop:
        if len(prop[p]) == 1:
            oldPos = prop[p][0]
            data.add(p)
            data.remove(oldPos)
            moved = True
    if not moved:
        print("Round when no elf moved:", numRounds)
        break
    numRounds += 1
    firstLookDir = firstLookDir+1 if firstLookDir < EAST else NORTH
minX = min([x for (x, y) in data])
maxX = max([x for (x, y) in data])
minY = min([y for (x, y) in data])
maxY = max([y for (x, y) in data])
area = (maxX - minX + 1) * (maxY - minY + 1)
res = area - len(data)
print("Number of empty tiles:", res)



