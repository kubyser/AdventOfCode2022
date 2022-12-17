from timeit import default_timer as timer

OPEN = "open"
FLOW = "flow"
TUNNELS = "tunnels"
OPENED = "opened"
ROOM = "room"

visited = {}
pathsExplored = [0]*30
globalBest = 0
rooms = {}


def explore(rooms, pos, opened, estimatedFlow, depth, potentialFlowPerMinute):
    global visited
    global globalBest
    if estimatedFlow > globalBest:
        globalBest = estimatedFlow
    vKey = (pos, frozenset(opened))
    #if pos in visited and visited[pos] > totalPotential:
    if vKey in visited and visited[vKey][0] >= depth and visited[vKey][1] >= estimatedFlow:
        return estimatedFlow, opened
    visited[vKey] = (depth, estimatedFlow)
#    visited[pos] = estimatedFlow + potentialFlowPerMinute * (depth-1)
    if depth == 0:
        return estimatedFlow, opened
    totalPotential = estimatedFlow + potentialFlowPerMinute * (depth-1)
    if totalPotential <= globalBest:
        return estimatedFlow, opened
    toExplore = []
    if pos not in opened and rooms[pos][FLOW] > 0:
        newOpened = opened.copy()
        newOpened.add(pos)
        flowIncrease = rooms[pos][FLOW] * (depth-1)
        toExplore.append({ROOM: pos, OPENED: newOpened, FLOW: (estimatedFlow + flowIncrease, potentialFlowPerMinute - rooms[pos][FLOW])})
    for tunnel in rooms[pos][TUNNELS]:
        toExplore.append({ROOM: tunnel, OPENED: opened.copy(), FLOW: (estimatedFlow, potentialFlowPerMinute)})
    bestFlow = estimatedFlow
    bestOpened = opened.copy()
    for step in toExplore:
        resFlow, resOpened = explore(rooms, step[ROOM], step[OPENED], step[FLOW][0], depth-1, step[FLOW][1])
        if resFlow > bestFlow:
            bestFlow = resFlow
            bestOpened = resOpened
    return bestFlow, bestOpened


def exploreWithElephant(pos, opened, estimatedFlow, depth, potentialFlowPerMinute):
    global visited
    global globalBest
    global rooms
    if estimatedFlow > globalBest:
        globalBest = estimatedFlow
    vKey = (frozenset(pos), frozenset(opened))
    totalPotential = estimatedFlow + potentialFlowPerMinute * (depth-1)
    if totalPotential <= globalBest:
        return estimatedFlow
    if vKey in visited and visited[vKey] >= totalPotential:
        return estimatedFlow
    visited[vKey] = totalPotential
    if depth == 0:
        return estimatedFlow
    toExplore = [[], []]
    for i in range(2):
        if pos[i] not in opened and rooms[pos[i]][FLOW] > 0 and (i == 0 or pos[0] != pos[1]):
            toExplore[i].append({ROOM: pos[i], OPEN: True})
        for tunnel in rooms[pos[i]][TUNNELS]:
            toExplore[i].append({ROOM: tunnel, OPEN: False})
    bestFlow = estimatedFlow
    for step1 in toExplore[0]:
        for step2 in toExplore[1]:
            newFlow = estimatedFlow
            potentialFlow = potentialFlowPerMinute
            if step1[OPEN] or step2[OPEN]:
                newOpened = opened.copy()
                if step1[OPEN]:
                    newOpened.add(step1[ROOM])
                    newFlow += rooms[step1[ROOM]][FLOW] * (depth-1)
                    potentialFlow -= rooms[step1[ROOM]][FLOW]
                if step2[OPEN]:
                    newOpened.add(step2[ROOM])
                    newFlow += rooms[step2[ROOM]][FLOW] * (depth-1)
                    potentialFlow -= rooms[step2[ROOM]][FLOW]
            else:
                newOpened = opened
            resFlow = exploreWithElephant([step1[ROOM], step2[ROOM]], newOpened, newFlow, depth-1, potentialFlow)
            if resFlow > bestFlow:
                bestFlow = resFlow
    global pathsExplored
    if depth > 20:
        pathsExplored[depth] += 1
        for i in range(26, 20, -1):
            print(" Depth:", i, "Explored:", pathsExplored[i], end='')
        print(" global=", globalBest)
    return bestFlow

f = open("resources/day16_input.txt", "r")
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
potential = sum(rooms[room][FLOW] for room in rooms)
start = timer()
#res, opened = explore(rooms, "AA", set(), 0, 30, potential)
#end = timer()
#print("Best flow just me:", res)
#print("Open valves just me:", opened)
res = exploreWithElephant(["AA", "AA"], set(), 0, 26, potential)
end = timer()
print("Best flow with elephant:", res)
print("Elapsed time: ", end - start)






