OPEN = "open"
FLOW = "flow"
TUNNELS = "tunnels"
OPENED = "opened"
ROOM = "room"

visited = {}
pathsExplored = 0
globalBest = 0


def explore(rooms, pos, opened, estimatedFlow, depth):
    global visited
    vKey = (pos, frozenset(opened))
    visited[vKey] = (depth, estimatedFlow)
    if depth == 0:
        return estimatedFlow, opened
    toExplore = []
    if pos not in opened and rooms[pos][FLOW] > 0:
        newOpened = opened.copy()
        newOpened.add(pos)
        flowIncrease = rooms[pos][FLOW] * (depth-1)
        toExplore.append({ROOM: pos, OPENED: newOpened, FLOW: estimatedFlow + flowIncrease})
    for tunnel in rooms[pos][TUNNELS]:
        toExplore.append({ROOM: tunnel, OPENED: opened.copy(), FLOW: estimatedFlow})
    bestFlow = estimatedFlow
    bestOpened = opened.copy()
    for step in toExplore:
        vKey = (step[ROOM], frozenset(step[OPENED]))
        if vKey not in visited or visited[vKey][0] < depth or visited[vKey][1] < step[FLOW]:
            resFlow, resOpened = explore(rooms, step[ROOM], step[OPENED], step[FLOW], depth-1)
            if resFlow > bestFlow:
                bestFlow = resFlow
                bestOpened = resOpened
    return bestFlow, bestOpened


def exploreWithElephant(rooms, pos, opened, estimatedFlow, depth):
    vKey = (frozenset(pos), frozenset(opened))
    visited[vKey] = (depth, estimatedFlow)
    if depth == 0:
        return estimatedFlow
    toExplore = [[], []]
    for i in range(2):
        if pos[i] not in opened and rooms[pos[i]][FLOW] > 0 and (i == 0 or pos[0] != pos[1]):
            toExplore[i].append({ROOM: pos[i], OPEN: True})
        for tunnel in rooms[pos[i]][TUNNELS]:
            toExplore[i].append({ROOM: tunnel, OPEN: False})
    bestRes = estimatedFlow
    for step1 in toExplore[0]:
        for step2 in toExplore[1]:
            newFlow = estimatedFlow
            if step1[OPEN] or step2[OPEN]:
                newOpened = opened.copy()
                if step1[OPEN]:
                    newOpened.add(step1[ROOM])
                    newFlow += rooms[step1[ROOM]][FLOW] * (depth-1)
                if step2[OPEN]:
                    newOpened.add(step2[ROOM])
                    newFlow += rooms[step2[ROOM]][FLOW] * (depth-1)
            else:
                newOpened = opened
            vKey = (frozenset([step1[ROOM], step2[ROOM]]), frozenset(newOpened))
            if vKey not in visited or visited[vKey][0] < depth or visited[vKey][1] < newFlow:
                res = exploreWithElephant(rooms, [step1[ROOM], step2[ROOM]], newOpened, newFlow, depth-1)
                if res > bestRes:
                    bestRes = res
    global pathsExplored
    pathsExplored += 1
    if depth > 20:
        print("Explored:", pathsExplored)
    return bestRes


f = open("resources/day16_test_input.txt", "r")
lines = f.read().splitlines()
f.close()
rooms = {}
for line in lines:
    line = line.split()
    name = line[1]
    flow = int(line[4].split("=")[1].split(";")[0])
    tunnels = []
    for i in range(9, len(line)):
        tunnels.append(line[i].replace(",", ""))
    rooms[name] = {FLOW: flow, TUNNELS: tunnels}
#print(rooms)
#res, opened = explore(rooms, "AA", set(), 0, 26)
#print("Best flow just me:", res)
#print("Open valves just me:", opened)
res = exploreWithElephant(rooms, ["AA", "AA"], set(), 0, 3)
print("Best flow with elephant:", res)





