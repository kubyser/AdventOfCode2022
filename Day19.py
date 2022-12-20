from timeit import default_timer as timer
ITEMS = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}
bps = {}
cache = {}


def hasEnough(bp, robot, resources):
    global bps
    for i in ITEMS:
        if resources[ITEMS[i]] < bps[bp][ITEMS[robot]][ITEMS[i]]:
            return False
    return True


def resMinus(bp, robot, resources):
    global bps
    res = list(resources)
    for i in ITEMS:
        res[ITEMS[i]] -= bps[bp][ITEMS[robot]][ITEMS[i]]
    return tuple(res)


def resPlus(resources, robots):
    res = list(resources)
    for i in ITEMS:
        res[ITEMS[i]] += robots[ITEMS[i]]
    return tuple(res)


def robotPlus(robot, robots):
    res = list(robots)
    res[ITEMS[robot]] += 1
    return tuple(res)


def solveBps(bp, resources, robots, couldBuild, steps):
    global bps
    global cache
    best = False
    if steps == 0:
        # print("Reached:", resources, robots)
        return resources[ITEMS["geode"]]
    if (resources, robots) in cache and cache[(resources, robots)] >= steps:
        return 0
    cache[(resources, robots)] = steps
    res = []
    for rob in ITEMS:
        if ITEMS[rob] not in couldBuild and hasEnough(bp, rob, resources):
            couldBuild.add(ITEMS[rob])
            resD = solveBps(bp, resPlus(resMinus(bp, rob, resources), robots), robotPlus(rob, robots), set(), steps-1)
            res.append(resD)
    if len(couldBuild) < len(ITEMS):
        resD = solveBps(bp, resPlus(resources, robots), robots, couldBuild, steps-1)
        res.append(resD)
    return max(res)


def solveToFirstRobot(bp, resources, robots, couldBuild, startRobotCount, steps):
    global bps
    global cache
    if steps == 0:
        #print("Reached:", resources, robots)
        return True, resources, robots
    if robots[ITEMS["geode"]] > startRobotCount:
        print("Robot built at step", steps)
        return False, resources, robots
    if (resources, robots) in cache and cache[(resources, robots)] >= steps:
        return 0
    cache[(resources, robots)] = steps
    res = []
    for rob in ITEMS:
        if ITEMS[rob] not in couldBuild and hasEnough(bp, rob, resources):
            couldBuild.add(ITEMS[rob])
            res.append(solveBps(bp, resPlus(resMinus(bp, rob, resources), robots), robotPlus(rob, robots), set(), startRobotCount, steps-1))
    if len(couldBuild) < len(ITEMS):
        res.append(solveBps(bp, resPlus(resources, robots), robots, couldBuild, startRobotCount, steps-1))
    return max(res)


def solveBFS(bp, startResources, startRobots, startSteps):
    toVisit = {(startResources, startRobots, startSteps)}
    res = []
    while len(toVisit) > 0:
        state = toVisit.pop()
        resources = state[0]
        robots = state[1]
        steps = state[2]
        if steps == 0:
            res.append(resources[ITEMS["geode"]])
            continue
        if (resources, robots) in cache and cache[(resources, robots)] >= steps:
            continue
        cache[(resources, robots)] = steps
        for rob in ITEMS:
            if hasEnough(bp, rob, resources):
                newState = (resPlus(resMinus(bp, rob, resources), robots), robotPlus(rob, robots), steps-1)
                toVisit.add(newState)
        newState = (resPlus(resources, robots), robots, steps-1)
        toVisit.add(newState)
    return max(res)


def solveBFSToFirst(bp, startResources, startRobots, startSteps):
    global bps
    toVisit = {(startResources, startRobots, startSteps, ())}
    res = []
    cache = set()
    maxRobots = startRobots[ITEMS["geode"]]
    while len(toVisit) > 0:
        toVisitNew = set()
        toVisitSolved = set()
        while len(toVisit) > 0:
            state = toVisit.pop()
            resources = state[0]
            robots = state[1]
            steps = state[2]
            couldBuild = set(state[3])
            if steps == 0:
                res.append(resources[ITEMS["geode"]])
                continue
            if (resources, robots, state[3]) in cache: # and cache[(resources, robots)] >= steps:
                continue
            # cache[(resources, robots)] = steps
            cache.add((resources, robots, state[3]))
            for rob in ITEMS:
                if ITEMS[rob] not in couldBuild and hasEnough(bp, rob, resources):
                    # if rob == "geode" and robots[ITEMS[rob]] == 0 and 24-steps+1 <= 19:
                    #     print("Robot built at step", 24-steps+1)
                    couldBuild.add(ITEMS[rob])
                    newState = (resPlus(resMinus(bp, rob, resources), robots), robotPlus(rob, robots), steps-1, ())
                    if rob == "geode":
                        toVisitSolved.add(newState)
                    else:
                        toVisitNew.add(newState)
            if len(couldBuild) < len(ITEMS):
                newState = (resPlus(resources, robots), robots, steps-1, tuple(couldBuild))
                toVisitNew.add(newState)
        if len(toVisitSolved) > 0:
            print("Robots build on step", steps, "(", 24-steps+1, "), cleaning level")
            toVisit = toVisitSolved
            maxRobots += 1
        else:
            toVisit = toVisitNew
    return max(res)





f = open("resources/day19_input.txt", "r")
lines = f.read().splitlines()
f.close()
for line in lines:
    line = line.replace("Blueprint ", "")
    line = line.replace(": Each ", ",")
    line = line.replace(". Each ", ",")
    line = line.replace(" robot costs ", ":")
    line = line.replace(" and ", "+")
    line = line.replace(".", "")
    print(line)
    line = line.split(",")
    num = int(line[0])
    bps[num] = [[]] * 4
    for r in line[1:]:
        rl = r.split(":")
        t = rl[0]
        bps[num][ITEMS[t]] = [0] * 4
        ings = rl[1].split("+")
        for ing in ings:
            ing = ing.split(" ")
            bps[num][ITEMS[t]][ITEMS[ing[1]]] = int(ing[0])
# print(bps)
if True:
    ql = 0
    start = timer()
    for bp in bps:
        print("Start calc for blueprint", bp)
        cache = {}
        #res = solveBFSToFirst(bp, (0, 0, 0, 0), (1, 0, 0, 0), 24)
        res = solveBps(bp, (0, 0, 0, 0), (1, 0, 0, 0), set(), 24)
        ql += bp * res
        print("Max resources for blueprint", bp, ":", res)
        print("Quality level=", ql)
    end = timer()
    print("Elapsed time: ", round(end - start, 3))
else:
    ql = 1
    start = timer()
    for bp in range(1, 3+1):
        print("Start calc for blueprint", bp)
        cache = {}
        res = solveBFSToFirst(bp, (0, 0, 0, 0), (1, 0, 0, 0), 32)
        ql *= res
        print("Max resources for blueprint", bp, ":", res)
        print("Quality level=", ql)
    end = timer()
    print("Elapsed time: ", round(end - start, 3))



