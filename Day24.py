UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
MOVES = {UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0)}


def calcPos(turn):
    global data
    global size
    newData = {}
    for pos in data:
        for bliz in data[pos]:
            shift = [x*turn for x in MOVES[bliz]]
            newPos = tuple([(x+y) % z for (x, y, z) in zip(pos, shift, size)])
            if newPos in newData:
                newData[newPos].append(bliz)
            else:
                newData[newPos] = [bliz]
    return newData


def printState(data):
    s = "#" * (size[0]+2)
    print(s)
    for y in range(size[1]):
        s = "#"
        for x in range(size[0]):
            if (x, y) in data:
                if len(data[(x, y)]) == 1:
                    s += data[(x, y)][0]
                else:
                    s += str(len(data[(x, y)]))
            else:
                s += "."
        s += "#"
        print(s)
    s = "#" * (size[0]+2)
    print(s)


f = open("resources/day24_input.txt")
lines = f.read().splitlines()
f.close()
data = {}
future = {}
width = len(lines[0])-2
height = len(lines)-2
size = [width, height]
row = 0
for line in lines[1:-1]:
    pos = 0
    for s in line[1:-1]:
        if s in "<>^v":
            data[(pos, row)] = [s]
        pos += 1
    row += 1
printState(data)
pos = ([x-1 for x in range(len(lines[0])) if lines[0][x] == '.'][0], -1)
target = ([x-1 for x in range(len(lines[height+1])) if lines[height+1][x] == '.'][0], height)
print(pos, target)
toVisit = {pos}
turn = 0
targets = [target, pos, target]
for target in targets:
    stop = False
    while not stop:
        turn += 1
        print("Starting turn", turn)
        future[turn] = calcPos(turn)
        state = future[turn]
        # printState(state)
        toVisitNew = set()
        while len(toVisit) > 0 and not stop:
            pos = toVisit.pop()
            if pos not in state and pos not in toVisitNew:
                toVisitNew.add(pos)
            for m in MOVES:
                pp = tuple([x+y for (x, y) in zip(pos, MOVES[m])])
                if pp == target:
                    print("Got out!!!", turn)
                    toVisitNew = {pp}
                    stop = True
                    break
                if all(0 <= x < y for (x, y) in zip(pp, size)):
                    if pp not in state and pp not in toVisitNew:
                        toVisitNew.add(pp)
        toVisit = toVisitNew






