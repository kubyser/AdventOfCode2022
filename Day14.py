PART2 = True

def findMin(cave, x, startY, maxY):
    if x not in cave:
        return -1 if not PART2 else maxY-1
    for y in cave[x]:
        if y > startY:
            return y-1
    return -1 if not PART2 else maxY-1


def isInCave(cave, x, y, maxY):
    if PART2 and y == maxY:
        return True
    if x not in cave:
        return False
    return y in cave[x]


f = open("resources/day14_input.txt", "r")
lines = f.read().splitlines()
f.close()
cave = {}
maxY = 0
for line in lines:
    coords = line.split(" -> ")
    for i in range(len(coords) - 1):
        p1 = [int(x) for x in coords[i].split(",")]
        p2 = [int(x) for x in coords[i+1].split(",")]
        for x in range(min([p1[0], p2[0]]), max([p1[0]+1, p2[0]+1])):
            for y in range(min([p1[1], p2[1]]), max([p1[1]+1, p2[1]+1])):
                if x not in cave:
                    cave[x] = set()
                cave[x].add(y)
                if y > maxY:
                    maxY = y
maxY += 2
for x in cave:
    cave[x] = sorted(cave[x])
print(cave)
finalReached = False
numGrains = 0
while not finalReached:
    pos = (500, findMin(cave, 500, 0, maxY))
    while True:
        if pos[1] == -1:
            finalReached = True
            break
        if not isInCave(cave, pos[0]-1, pos[1]+1, maxY):
            pos = (pos[0]-1, findMin(cave, pos[0]-1, pos[1]+1, maxY))
            continue
        if not isInCave(cave, pos[0]+1, pos[1]+1, maxY):
            pos = (pos[0]+1, findMin(cave, pos[0]+1, pos[1]+1, maxY))
            continue
        if pos[0] not in cave:
            cave[pos[0]] = [pos[1]]
        else:
            try:
                cave[pos[0]].insert(cave[pos[0]].index(pos[1]+1), pos[1])
            except ValueError:
                cave[pos[0]].append(pos[1])
        numGrains += 1
        if pos == (500, 0):
            finalReached = True
        break
print("Number of grains before abyss or top reached:", numGrains)


        

