height = 0
width = 0
def getPossibleMoves(hMap, pos):
    res = []
    if (pos[0] > 0) and (hMap[(pos[0]-1, pos[1])] <= hMap[pos] + 1):
        res.append((pos[0]-1, pos[1]))
    if (pos[0] < width-1) and (hMap[(pos[0]+1, pos[1])] <= hMap[pos] + 1):
        res.append((pos[0]+1, pos[1]))
    if (pos[1] > 0) and (hMap[(pos[0], pos[1]-1)] <= hMap[pos] + 1):
        res.append((pos[0], pos[1]-1))
    if (pos[1] < height-1) and (hMap[(pos[0], pos[1]+1)] <= hMap[pos] + 1):
        res.append((pos[0], pos[1]+1))
    return res

f = open("resources/day12_input.txt", "r")
lines = f.read().splitlines()
f.close()
height = len(lines)
width = len(lines[0])
hMap = {}
sPos = (0, 0)
ePos = (0, 0)
for y in range(len(lines)):
    for x in range(len(lines[y])):
        c = lines[y][x]
        hMap[(x, y)] = 0 if c == 'S' else 25 if c == "E" else ord(c) - ord('a')
        if c == 'S':
            sPos = (x, y)
        if c == 'E':
            ePos = (x, y)
minPath = {}
for p in hMap:
    if hMap[p] == 0:
        #print("Trying", p)
        visited = {}
        toVisit = {p: 0}
        while True:
            if len(toVisit) == 0:
                #print("Nowhere to go")
                break
            pos = min(toVisit, key=toVisit.get)
            curLen = toVisit[pos]
            visited[pos] = toVisit[pos]
            toVisit.pop(pos)
            if pos == ePos:
                break
            moves = getPossibleMoves(hMap, pos)
            for move in moves:
                if move in visited and visited[move] > curLen+1:
                    visited.pop(move)
                    toVisit[move] = curLen+1
                elif move not in visited and move not in toVisit or move in toVisit and toVisit[move] > curLen+1:
                    toVisit[move] = curLen+1
        if ePos in visited:
            minPath[p] = visited[ePos]
            #print("Min path from", p, "is", minPath[p])
print("Min path from start:", minPath[sPos])
bestStart = min(minPath, key=minPath.get)
print("Best start is", bestStart, "with path", minPath[bestStart])

